#!/usr/bin/env python3
"""Characteristic-zero tangent certificate at the O(2,2) ring of P1 x P1.

Optional check; do not add to the default verification suite. Dependencies:
numpy>=1.24, numba>=0.60, and the project's usual SymPy installation.
Run from the repository root:
    python3 computations/verify_commutative_quadric_tangent.py

The sibling verify_noncubic_degree3_tangent.py supplies only three modular
elimination routines, loaded through its AST without running its other checks.
The present construction uses the toric monomial basis of the (2,2) ring.
There is no floating point, random sampling, or rank estimation.

The integer degree-three constraint matrix has shape 16072 x 1400. Its rank
1311 modulo 101 is a LOWER bound on its characteristic-zero rank. We also
check 95 explicit integer kernel columns, whose rank is 89 modulo 101. Their
exact integer residuals vanish, giving the opposite rank bound 1400-89=1311.
Thus the characteristic-zero tangent dimension is exactly 89. Six explicit,
independent integer stabilizer dependencies, together with modular rank 74,
certify the PGL9 orbit rank 74. The quotient tangent dimension is therefore 15.

Intermediate integer matrix products use int64, apart from the large
constraint matrix and batched residual products, which use int32 after
explicit absolute-sum bounds. The modular row reducer stores residues in
uint8/int16; for p=101 its elementary products have absolute value <=10000.
Assertions check the relevant bounds before any potentially narrowing step.
Changing the prime, dimensions, or formulas requires rechecking these bounds;
an unchecked fixed-width computation would not be an integer certificate.
Elapsed time includes imports and Numba compilation.
"""
import ast
from pathlib import Path
from time import perf_counter

started = perf_counter()
import numpy as np
import sympy as sp
from numba import njit

src=Path(__file__).with_name('verify_noncubic_degree3_tangent.py')
if not src.is_file():
    raise SystemExit('Place this script beside verify_noncubic_degree3_tangent.py.')
tree=ast.parse(src.read_text())
names={'rank_mod','rref_mod','rank_rows_mod'}
functions=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
assert {n.name for n in functions}==names
exec(compile(ast.Module(body=functions,type_ignores=[]),str(src),'exec'))
p=101
assert p<256 and (p-1)**2<np.iinfo(np.int16).max

def absmax(a):
    return int(np.abs(a).max())

def product_bound(a,b,limit=np.iinfo(np.int64).max):
    """Bound every partial sum in a dense integer matrix product."""
    bound=a.shape[-1]*absmax(a)*absmax(b)
    assert bound<=limit, ('integer product overflow risk',bound,limit)
    return bound

mons=[(a,b) for a in range(3) for b in range(3)]
q=np.zeros((25,81),dtype=np.int64)
for i,(a,b) in enumerate(mons):
    for j,(c,d) in enumerate(mons):q[5*(a+c)+b+d,9*i+j]=1
P=np.array([int(np.flatnonzero(q[r])[0]) for r in range(25)])
N=np.array([j for j in range(81) if j not in set(P)])
pairs=[divmod(int(z),9) for z in P]
notpairs=[divmod(int(z),9) for z in N]
assert np.array_equal(q[:,P],np.eye(25,dtype=np.int64))
rel=np.zeros((81,56),dtype=np.int64)
rel[N,np.arange(56)]=1;rel[P,:]=-q[:,N]
assert not np.any(q@rel)
L=np.zeros((225,504),dtype=np.int64)
for g in range(9):
    for j in range(56):
        for z in np.flatnonzero(rel[:,j]):
            b,c=divmod(int(z),9)
            L[c::9,9*j+g]+=int(rel[z,j])*q[:,9*g+b]
echelon,piv=rref_mod(L,p)
assert len(piv)==176
free=[j for j in range(504) if j not in set(piv)]
S=np.zeros((504,328),dtype=np.int64)
S[free,np.arange(328)]=1;S[piv,:]=-echelon[:,free]
S=(S+50)%101-50
assert np.array_equal(S[free,:],np.eye(328,dtype=np.int64))
product_bound(L,S)
assert not np.any(L@S), 'Integer cycle lifts must solve L S=0.'
KT=S.T.reshape(328,56,9).transpose(0,2,1)
q3=np.zeros((49,225),dtype=np.int64)
for h,(b,c) in enumerate(pairs):
    for g,(a,d) in enumerate(mons):
        aa=mons[b][0]+mons[c][0]+a
        bb=mons[b][1]+mons[c][1]+d
        q3[7*aa+bb,9*h+g]=1
assert np.all(q3.sum(axis=0)==1)
assert set(q3.argmax(axis=0))==set(range(49))
product_bound(q3,L)
assert not np.any(q3@L)
assert rank_mod(q3,p)==49
# q3 is a split integral quotient of rank 49, so q3 L=0 bounds rank(L)
# above by 225-49=176; its modular rank gives equality in characteristic zero.
# The identity submatrix in S proves that its 328 integer columns are a basis
# of ker(L) over Q. Hence the full fixed-rank linearization is being tested.
C=np.zeros((1400,49*328),dtype=np.int32)
R=rel.reshape(9,9,56)
inter_bound=56*absmax(KT)*absmax(R)
H_bound=25*absmax(q3)*absmax(q)
constraint_bound=9*inter_bound*absmax(q3)+9*absmax(KT)*H_bound
assert inter_bound<2**63 and H_bound<2**63
assert constraint_bound<2**31
inter=np.einsum('tgj,bcj->tgbc',KT,R)
for k,(g,b) in enumerate(notpairs):
    for h in range(25):
        C[56*h+k,:]=(inter[:,g,b,:]@q3[:,9*h:9*h+9].T).reshape(-1)
for h,(b,c) in enumerate(pairs):
    H=np.empty((9,49),dtype=np.int64)
    for g in range(9):H[g,:]=q3[:,c::9]@q[:,9*g+b]
    term=np.einsum('tgj,gz->jtz',KT,H)
    for j in range(56):C[56*h+j,:]-=term[j].reshape(-1).astype(np.int32)
assert absmax(C)<=constraint_bound

directions=[]
for i in range(9):
    for j in range(9):
        if (i,j)==(8,8):continue
        deriv=np.zeros((81,56),dtype=np.int64)
        for z in range(9):
            deriv[9*i+z,:]+=rel[9*j+z,:]
            deriv[9*z+i,:]+=rel[9*z+j,:]
        product_bound(q,deriv)
        directions.append((q@deriv).reshape(-1))

x=sp.symbols('x0:4');x0,x1,x2,x3=x
quad=x0*x3-x1*x2
gens=[x0*x0,x0*x1,x1*x1,x0*x2,x0*x3,x1*x3,x2*x2,x2*x3,x3*x3]
forms=[x0*x0,x0*x1,x0*x2,x1*x1,x1*x2,x1*x3,x2*x2,x2*x3,x3*x3]
def coordinates(f):
    # Accumulate symbolic coefficients as Python integers before narrowing.
    v=[0]*25
    for e,c in sp.Poly(sp.expand(f),*x).terms():
        v[5*(e[2]+e[3])+e[1]+e[3]]+=int(c)
    assert max(map(abs,v))<2**63
    return np.array(v,dtype=np.int64)
for form in forms:
    bracket={}
    for i in range(4):
        for j in range(4):
            bracket[i,j]=sum(sp.LeviCivita(i,j,r,s)*sp.diff(quad,x[r])*sp.diff(form,x[s]) for r in range(4) for s in range(4))
    dq=np.zeros((25,81),dtype=np.int64)
    for i,a in enumerate(gens):
        for j,b in enumerate(gens):
            value=sum(sp.diff(a,x[r])*sp.diff(b,x[s])*bracket[r,s] for r in range(4) for s in range(4))
            dq[:,9*i+j]=coordinates(value)
    product_bound(dq,rel)
    directions.append((-dq@rel).reshape(-1))

stabilizer=[]
for factor in range(2):
    for kind in range(3):
        D=np.zeros((9,9),dtype=np.int64)
        for i,ab in enumerate(mons):
            a=ab[factor];out=list(ab)
            if kind==0:
                if a==0:continue
                out[factor]-=1;c=a
            elif kind==1:
                if a==2:continue
                out[factor]+=1;c=2-a
            else:c=2-2*a
            D[mons.index(tuple(out)),i]=c
        # The orbit basis omits E_88 and represents gl9/k*Id. Subtracting
        # D_88*Id expresses this infinitesimal automorphism in that basis.
        D_mod_scalar=D-int(D[8,8])*np.eye(9,dtype=np.int64)
        stabilizer.append(D_mod_scalar.reshape(-1)[:80])
        dq=np.zeros((25,81),dtype=np.int64)
        for i in range(9):
            for j in range(9):
                for z in np.flatnonzero(D[:,i]):dq[:,9*i+j]+=D[z,i]*q[:,9*z+j]
        product_bound(dq,rel)
        directions.append((-dq@rel).reshape(-1))

dirs=np.stack(directions,axis=1)
assert dirs.shape==(1400,95)
ranks=[rank_mod(dirs[:,:80],p),rank_mod(dirs[:,:89],p),rank_mod(dirs,p)]
print('Mod-101 ranks: orbit / orbit+Jacobian / all directions =',ranks,flush=True)
assert ranks==[74,83,89]
stabilizer=np.stack(stabilizer,axis=1)
assert stabilizer.shape==(80,6) and rank_mod(stabilizer,p)==6
product_bound(dirs[:,:80],stabilizer)
assert not np.any(dirs[:,:80]@stabilizer)
print('Six independent exact integer stabilizer dependencies verified.',flush=True)
residual_bound=product_bound(dirs.T,C,np.iinfo(np.int32).max)
for start in range(0,C.shape[1],512):
    residual=dirs.T.astype(np.int32)@C[:,start:start+512].astype(np.int32)
    assert not np.any(residual),'Integer linearized residual must vanish.'
print('All 95 direction columns solve every integer linearized equation.',flush=True)
rk,_,_=rank_rows_mod((C.T%p).astype(np.uint8).copy(),p)
print('Matrix ranks: L (225 x 504) = 176; q3 (49 x 225) = 49;',flush=True)
print('  constraints (16072 x 1400) modulo 101 =',rk,flush=True)
assert rk==1311
print('PASS: characteristic-zero X3 tangent 89, PGL9 orbit 74, quotient tangent 15.',flush=True)
print('Rank lower bound 1311 mod101 + 89 independent exact integer kernel vectors.',flush=True)
print('Max absolute entries: syzygies =',absmax(S),'; constraints =',absmax(C),'; directions =',absmax(dirs),flush=True)
print('Integer residual absolute-sum bound =',residual_bound,'< 2^31.',flush=True)
print(f'Elapsed seconds, including imports and JIT: {perf_counter()-started:.3f}',flush=True)
