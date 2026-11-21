#!/usr/bin/env python3
"""Exact F_101 and rational tangent-rank certificate for noncubic H2.

Optional dependencies: numpy>=1.24 and numba>=0.60 (also the usual SymPy).
Run: python3 computations/verify_noncubic_degree3_tangent.py
No floating point, random sampling, or rank estimation is used.

Computes ranks of the 80 PGL9 tangent directions, six binary-quadratic
coefficient directions, and the differential of the degree-three Hilbert
rank condition at three root configurations. This is a finite-field
certificate plus explicit rational nullspace lifts, checked against the
integer linearized equations. The characteristic-zero dimensions are exact.
"""
from __future__ import annotations
import numpy as np
import sympy as sp
from numba import njit
import verify_noncubic_antiserre_pivots as chart

prime=101
names=list(chart.gens)
pairs=[(names.index(a),names.index(b)) for a,b in chart.pivots]
notpairs=[(i,j) for i in range(9) for j in range(9) if (i,j) not in pairs]
P=np.array([9*i+j for i,j in pairs])
N=np.array([9*i+j for i,j in notpairs])
parameters=[chart.a,chart.b,chart.c,chart.aa,chart.bb,chart.cc]
Q=sp.Matrix.hstack(*(chart.coordinates(chart.star(a,b))
                      for a in names for b in names))
assert Q.shape==(25,81)
def rank_mod(M,p):
    a=M.copy()%p
    rank=0
    for col in range(a.shape[1]):
        v=np.flatnonzero(a[rank:,col])
        if not len(v):continue
        j=rank+int(v[0]);a[[rank,j]]=a[[j,rank]]
        a[rank,col:]=a[rank,col:]*pow(int(a[rank,col]),-1,p)%p
        rows=np.flatnonzero(a[rank+1:,col])+rank+1
        if len(rows):
            a[rows,col:]=(a[rows,col:]-a[rows,col,None]*a[rank,None,col:])%p
        rank+=1
        if rank==a.shape[0]:break
    return rank
def rref_mod(M,p):
    a=M.copy()%p
    rank=0;piv=[]
    for col in range(a.shape[1]):
        v=np.flatnonzero(a[rank:,col])
        if not len(v):continue
        j=rank+int(v[0]);a[[rank,j]]=a[[j,rank]]
        a[rank,col:]=a[rank,col:]*pow(int(a[rank,col]),-1,p)%p
        rows=np.flatnonzero(a[:,col])
        rows=rows[rows!=rank]
        if len(rows):
            a[rows,col:]=(a[rows,col:]-a[rows,col,None]*a[rank,None,col:])%p
        piv.append(col);rank+=1
        if rank==a.shape[0]:break
    return a[:rank],piv
@njit
def rank_rows_mod(a,p):
    nrows,ncols=a.shape
    piv=np.zeros((ncols,ncols),dtype=np.int16)
    occupied=np.zeros(ncols,dtype=np.uint8)
    rank=0
    for row in range(nrows):
        v=a[row].astype(np.int16)
        for col in range(ncols):
            c=int(v[col])
            if not c:continue
            if occupied[col]:
                for j in range(col,ncols):
                    v[j]=(v[j]-c*piv[col,j])%p
            else:
                inv=1
                while (c*inv)%p!=1:inv+=1
                for j in range(col,ncols):
                    piv[col,j]=v[j]*inv%p
                occupied[col]=1;rank+=1
                break
    return rank,piv,occupied

# The 49 degree-six PBW words: alternating c,d words, central binary
# monomials of the complementary degree. The twist by iota acts only
# on the middle of the three degree-two factors.
words=['','c','d','cd','dc','cdc','dcd','cdcd','dcdc',
       'cdcdc','dcdcd','cdcdcd','dcdcdc']
basis=[(chart.u**i*chart.v**(6-len(w)-i),w)
       for w in words for i in range(7-len(w))]
assert len(basis)==49

def triple(pair,last,evaluation):
    d=chart.star(names[pair[0]],names[pair[1]])
    coeff,w=chart.gens[names[last]]
    result={}
    for word,pol in d.items():
        for word2,pol2 in chart.reduce_word(word+w).items():
            result[word2]=sp.expand(result.get(word2,0)+pol*coeff*pol2)
    return np.array([
        int(sp.Poly(result.get(w,0),chart.u,chart.v)
              .coeff_monomial(mon).subs(evaluation))%prime
        for mon,w in basis],dtype=np.int64)

cases=[
  ('disjoint',(0,1,0,1,0,1),80,1317),
  ('one-root-shared',(0,1,0,-1,1,0),80,1317),
  ('coincident',(0,1,0,0,1,0),79,1316)
]
SECOND_ORDER_CASE_DATA = {}
for label,data,orbit_expected,degree3_rank_expected in cases:
    ev=dict(zip(parameters,data))
    q=np.array(Q.subs(ev).tolist(),dtype=np.int64)%prime
    qp=q[:,P]
    assert np.array_equal(qp.T@qp%prime,np.eye(25,dtype=np.int64))
    d2=qp.T@q%prime
    rel=np.zeros((81,56),dtype=np.int64)
    rel[N,np.arange(56)]=1
    rel[P,:]=-d2[:,N]
    rel%=prime
    assert not np.any(q@rel%prime)

    # Grassmann tangent dimensions for the PGL9 orbit and the form chart.
    directions=[]
    for i in range(9):
        for j in range(9):
            if i==j==8:continue
            deriv=np.zeros((81,56),dtype=np.int64)
            for z in range(9):
                deriv[9*i+z,:]+=rel[9*j+z,:]
                deriv[9*z+i,:]+=rel[9*z+j,:]
            directions.append((qp.T@q@deriv%prime).reshape(-1))
    for parameter in parameters:
        dq=np.array(Q.diff(parameter).subs(ev).tolist(),dtype=np.int64)%prime
        assert not np.any(dq[:,P])
        directions.append((-qp.T@dq[:,N]%prime).reshape(-1))
    tangent=np.stack(directions,axis=1)%prime
    ranks=(rank_mod(tangent[:,:80],prime),
           rank_mod(tangent[:,80:],prime),
           rank_mod(tangent,prime))
    assert ranks==(orbit_expected,6,81),(label,ranks)

    # Degree-three relation map: V tensor J -> (V^2/J) tensor V.
    # Rank 176 is equivalent to dim R_3=49.
    L=np.zeros((225,504),dtype=np.int64)
    for g in range(9):
        for j in range(56):
            for index in np.flatnonzero(rel[:,j]):
                b,c=divmod(int(index),9)
                L[c::9,9*j+g]+=int(rel[index,j])*d2[:,9*g+b]
    L%=prime
    echelon,pivots=rref_mod(L,prime)
    assert len(pivots)==176
    free=[j for j in range(504) if j not in set(pivots)]
    assert len(free)==328
    syzygies=np.zeros((504,328),dtype=np.int64)
    syzygies[free,np.arange(328)]=1
    syzygies[pivots,:]=-echelon[:,free]
    syzygies%=prime
    assert not np.any(L@syzygies%prime)
    KT=syzygies.T.reshape(328,56,9).transpose(0,2,1)

    # Reduce the cokernel of L to the 49 PBW basis vectors in R_3.
    q3=np.zeros((49,225),dtype=np.int64)
    for h,pair in enumerate(pairs):
        for g in range(9):
            q3[:,9*h+g]=triple(pair,g,ev)
    assert not np.any(q3@L%prime)

    # The linearized fixed-rank condition is
    #    coker(L) <- delta(L) | ker(L) = 0.
    # Its 49*328 equations in 25*56 unknown Grassmann tangents.
    constraints=np.zeros((1400,49*328),dtype=np.uint8)
    R=rel.reshape(9,9,56)
    inter=np.einsum('tgj,bcj->tgbc',KT,R)%prime
    for k,(g,b) in enumerate(notpairs):
        for h in range(25):
            constraints[56*h+k,:]=(
                inter[:,g,b,:]@q3[:,9*h:9*h+9].T%prime
            ).reshape(-1)
    for h,(b,c) in enumerate(pairs):
        H=np.empty((9,49),dtype=np.int64)
        for g in range(9):
            H[g,:]=q3[:,c::9]@d2[:,9*g+b]%prime
        term=np.einsum('tgj,gz->jtz',KT,H)%prime
        for j in range(56):
            constraints[56*h+j,:]=(
                constraints[56*h+j,:].astype(np.int64)
                -term[j].reshape(-1)
            )%prime

    # Check all 86 known orbit/form directions in every linear condition.
    assert not np.any(constraints.T.astype(np.int64)
                      @ tangent.astype(np.int64)%prime)

    # Row-rank without random sampling (all 16072 constraints).
    rank,rows,occupied=rank_rows_mod(constraints.T.copy(),prime)
    assert rank==degree3_rank_expected,(label,rank)
    free_vars=np.flatnonzero(1-occupied)
    assert len(free_vars)==1400-rank

    # Rational reconstruction from F_101. The tested exact points have
    # rational nullspace vectors whose coordinates have denominators <= 2
    # and numerators <= 5, as verified below over the integers.
    nullspace=np.zeros((1400,len(free_vars)),dtype=np.int64)
    nullspace[free_vars,np.arange(len(free_vars))]=1
    for c in range(1399,-1,-1):
        if occupied[c]:
            nullspace[c,:]=(
                -rows[c,c+1:].astype(np.int64)@nullspace[c+1:,:]
            )%prime

    def rational_reconstruct(z):
        choices=[]
        for d in (1,2):
            n=(int(z)*d)%prime
            if n>prime//2:n-=prime
            if abs(n)<=5:
                choices.append((max(abs(n),d),abs(n)+d,d,n))
        if not choices:raise AssertionError(('rational-reconstruction',z))
        _,_,d,n=min(choices)
        return n,d

    exact_candidates=np.empty_like(nullspace)
    for j in range(nullspace.shape[1]):
        pairs_nd=[rational_reconstruct(z) for z in nullspace[:,j]]
        denominator=np.lcm.reduce([d for _,d in pairs_nd])
        exact_candidates[:,j]=[
            n*(denominator//d) for n,d in pairs_nd
        ]

    # Independent lift of the syzygy basis ker(L) over Z.
    qZ=np.array(Q.subs(ev).tolist(),dtype=np.int64)
    d2Z=qZ[:,P].T@qZ
    relZ=np.zeros((81,56),dtype=np.int64)
    relZ[N,np.arange(56)]=1
    relZ[P,:]=-d2Z[:,N]
    LZ=np.zeros((225,504),dtype=np.int64)
    for g in range(9):
        for j in range(56):
            for index in np.flatnonzero(relZ[:,j]):
                b,c=divmod(int(index),9)
                LZ[c::9,9*j+g]+=int(relZ[index,j])*d2Z[:,9*g+b]
    kerZ=syzygies.copy()
    kerZ[kerZ>prime//2]-=prime
    assert not np.any(LZ@kerZ)

    # At these three integral base points, all entries of the PBW
    # triple-product matrix are small; the centered mod-101 lift is exact.
    q3Z=q3.copy()
    q3Z[q3Z>prime//2]-=prime
    assert not np.any(q3Z@LZ)
    KTz=kerZ.T.reshape(328,56,9).transpose(0,2,1)
    interZ=np.einsum('tgj,bcj->tgbc',KTz,relZ.reshape(9,9,56))
    constraintsZ=np.zeros((1400,49*328),dtype=np.int16)
    for k,(g,b) in enumerate(notpairs):
        for h in range(25):
            constraintsZ[56*h+k,:]=(
                interZ[:,g,b,:]@q3Z[:,9*h:9*h+9].T
            ).reshape(-1)
    for h,(b,c) in enumerate(pairs):
        H=np.empty((9,49),dtype=np.int64)
        for g in range(9):
            H[g,:]=q3Z[:,c::9]@d2Z[:,9*g+b]
        term=np.einsum('tgj,gz->jtz',KTz,H)
        for j in range(56):
            constraintsZ[56*h+j,:]-=term[j].reshape(-1)

    assert not np.any(constraintsZ.astype(np.int64)%prime != constraints)
    # This is a genuine exact integer check, not a reduction modulo 101.
    assert not np.any(constraintsZ.T.astype(np.int64)@exact_candidates)
    # The free rows form a nonsingular diagonal submatrix after scaling.
    assert np.all(exact_candidates[free_vars,np.arange(len(free_vars))]!=0)
    print(label,': orbit/form/combined',ranks,
          '; rank(F_101)',rank,
          '; rational tangent dimension',len(free_vars),
          '; max exact numerator',np.max(np.abs(exact_candidates)),
          flush=True)
    # Reusable exact matrices for the independent order-two obstruction certificate.
    SECOND_ORDER_CASE_DATA[label] = {
        "rank": rank, "relZ": relZ, "d2Z": d2Z,
        "LZ": LZ, "kerZ": kerZ, "q3Z": q3Z,
        "constraintsZ": constraintsZ, "constraints": constraints,
        "tangent": tangent, "exact_candidates": exact_candidates,
        "pivots_L": pivots,
    }
print('PASS: full F_101 ranks and exact rational bases of dimension 83,83,84.')
