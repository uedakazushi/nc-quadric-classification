#!/usr/bin/env python3
"""Exact second-order cubic-Hilbert lifting certificate at three noncubic H2 points.

Run:
    python3 computations/verify_noncubic_second_order.py

Dependencies: SymPy (requirements.txt), NumPy>=1.24, Numba>=0.60.
This imports and re-runs the exact degree-three tangent certificate.
All final assertions are integer identities. No numerical tolerances.

The result concerns degree-three Hilbert flatness through t^2, not a
higher-order formal family or the intrinsic relative H2 Abel stack.
"""
import numpy as np
from numba import njit

import verify_noncubic_degree3_tangent as base

p=base.prime
P=base.P
N=base.N
nvars=1400

def row_reduction(A):
    """Reduced-echelon form over F_p, with pivot-column indices."""
    T=A.astype(np.int64).copy()%p
    r=0
    pivot=[]
    for j in range(T.shape[1]):
        nz=np.flatnonzero(T[r:,j])
        if not len(nz):
            continue
        h=r+int(nz[0])
        T[[r,h]]=T[[h,r]]
        T[r,j:]=T[r,j:]*pow(int(T[r,j]),-1,p)%p
        rows=np.flatnonzero(T[:,j])
        rows=rows[rows!=r]
        if len(rows):
            T[rows,j:]=(T[rows,j:]-T[rows,j,None]*T[r,None,j:])%p
        pivot.append(j)
        r+=1
        if r==T.shape[0]:
            break
    return T[:r], pivot

def invert(A):
    n=A.shape[0]
    X=np.hstack((A.copy()%p,np.eye(n,dtype=np.int64)))
    for j in range(n):
        nz=np.flatnonzero(X[j:,j])
        assert len(nz)
        h=j+int(nz[0])
        X[[j,h]]=X[[h,j]]
        X[j]=X[j]*pow(int(X[j,j]),-1,p)%p
        rows=np.flatnonzero(X[:,j])
        rows=rows[rows!=j]
        if len(rows):
            X[rows]=(X[rows]-X[rows,j,None]*X[j,None])%p
    return X[:,n:]

def centered(A):
    X=A.copy()%p
    X[X>p//2]-=p
    return X

@njit
def echelon_augmented(A,prime):
    """Row-echelon system [M | rhs] over F_prime, all rows tested."""
    nrows,ncols=A.shape
    E=np.zeros((ncols,ncols),dtype=np.int16)
    selected=np.zeros(ncols,dtype=np.uint8)
    rank=0
    for row in range(nrows):
        v=A[row].astype(np.int16)
        for col in range(ncols):
            c=int(v[col])
            if c==0:
                continue
            if selected[col]:
                for j in range(col,ncols):
                    v[j]=(v[j]-c*E[col,j])%prime
            else:
                inv=1
                while c*inv%prime != 1:
                    inv+=1
                for j in range(col,ncols):
                    E[col,j]=v[j]*inv%prime
                selected[col]=1
                rank+=1
                break
    return E,selected,rank

def modular_solution(A,rhs,rank):
    E,selected,computed=echelon_augmented(
        np.column_stack((A%p,rhs%p)).astype(np.uint8),p
    )
    assert computed==rank, (rank,computed)
    x=np.zeros(nvars+1,dtype=np.int64)
    for col in range(nvars-1,-1,-1):
        if selected[col]:
            x[col]=(int(E[col,nvars]) -
                    E[col,col+1:nvars].astype(np.int64)@x[col+1:nvars])%p
    assert not np.any((A@x[:nvars]-rhs)%p)
    return x[:nvars]

def rational_lift(AZ,b,mod_solution,rank):
    """Solve AZ*x=-b exactly over Q by F_p then F_{p^2} reconstruction."""
    x=centered(mod_solution)
    if not np.any(AZ@x+b):
        return x,1
    # Hensel correction, using a fixed full-rank minor.
    x0=mod_solution.copy()%p
    residual=AZ@x0+b
    assert not np.any(residual%p)
    y=modular_solution(AZ%p,-(residual//p),rank)
    modulus=p*p
    xx=(x0+p*y)%modulus
    for bound in (35,60,80):
        numer=[]
        denom=[]
        for z in xx:
            candidates=[]
            for d in range(1,bound+1):
                if d%p==0:
                    continue
                n=int(z)*d%modulus
                if n>modulus//2:
                    n-=modulus
                if abs(n)<=(modulus//2)//bound:
                    candidates.append((abs(n)+d,n,d))
            if not candidates:
                break
            _,n,d=min(candidates)
            numer.append(n)
            denom.append(d)
        if len(numer)!=nvars:
            continue
        common=int(np.lcm.reduce(denom))
        if common>100000:
            continue
        x=np.array([n*(common//d) for n,d in zip(numer,denom)],
                   dtype=np.int64)
        if not np.any(AZ@x+common*b):
            return x,common
    raise AssertionError("Could not certify exact rational second-order correction")

def complement_basis(case):
    """Choose a Q-basis of tangent directions transverse to orbit+forms."""
    orbit=case["tangent"]
    _,pivotcols=row_reduction(orbit)
    assert len(pivotcols)==81
    span=orbit[:,pivotcols].copy()%p
    trans=[]
    for v0 in case["exact_candidates"].T:
        v=v0.copy()%p
        _,pivotrows=row_reduction(span.T)
        assert len(pivotrows)==span.shape[1]
        coeff=invert(span[pivotrows,:])@v[pivotrows]%p
        if np.any((v-span@coeff)%p):
            # v0 is an actual integer Hochschild cocycle, not just mod p.
            assert not np.any(case["constraintsZ"].T.astype(np.int64)@v0)
            trans.append(v0.copy())
            span=np.column_stack((span,v))
    assert len(trans)==case["tangent"].shape[0]-case["rank"]-81
    return trans

for label,case in base.SECOND_ORDER_CASE_DATA.items():
    rel=case["relZ"]
    d2=case["d2Z"]
    L=case["LZ"]
    K=case["kerZ"]
    Q3=case["q3Z"]
    AZ=case["constraintsZ"].T.astype(np.int64)
    rank=case["rank"]
    pivL=case["pivots_L"]

    _,pivRows=row_reduction((L[:,pivL]%p).T)
    assert len(pivRows)==176
    inv0=centered(invert(L[np.ix_(pivRows,pivL)]%p))
    assert np.array_equal(
        L[np.ix_(pivRows,pivL)]@inv0,
        np.eye(176,dtype=np.int64)
    )

    def first_second_L(v):
        phi=v.reshape(25,56)
        q1=np.zeros((25,81),dtype=np.int64)
        q1[:,N]=phi
        r1=np.zeros((81,56),dtype=np.int64)
        r1[P,:]=-phi
        L1=np.zeros_like(L)
        L2=np.zeros_like(L)
        for x in range(9):
            for j in range(56):
                column=9*j+x
                for index in np.flatnonzero(rel[:,j]):
                    b,c=divmod(int(index),9)
                    L1[c::9,column]+=int(rel[index,j])*q1[:,9*x+b]
                for index in np.flatnonzero(r1[:,j]):
                    b,c=divmod(int(index),9)
                    L1[c::9,column]+=int(r1[index,j])*d2[:,9*x+b]
                    L2[c::9,column]+=int(r1[index,j])*q1[:,9*x+b]
        return L1,L2

    def quadratic_obstruction(v):
        L1,L2=first_second_L(v)
        # The full integer linearization must agree, in (syzygy, PBW) order.
        assert np.array_equal(
            (Q3@L1@K).T.reshape(-1),AZ@v
        )
        assert not np.any(AZ@v)
        Y=L1@K
        coeff=inv0@Y[pivRows,:]
        assert np.array_equal(L[:,pivL]@coeff,Y)
        return (Q3@(L2@K-L1[:,pivL]@coeff)).T.reshape(-1)

    trans=complement_basis(case)
    expected={"disjoint":2,"one-root-shared":2,"coincident":3}[label]
    assert len(trans)==expected
    lifts={}
    vectors=[(f"v{i}",trans[i]) for i in range(len(trans))]
    vectors += [(f"v{i}+v{j}",trans[i]+trans[j])
                for i in range(len(trans)) for j in range(i+1,len(trans))]
    for name,v in vectors:
        obstruction=quadratic_obstruction(v)
        modular=modular_solution(AZ%p,-obstruction,rank)
        correction,den=rational_lift(AZ,obstruction,modular,rank)
        # Exact integer equality, not merely modulo 101 or 101^2.
        assert not np.any(AZ@correction+den*obstruction)
        lifts[name]=(correction,den)
    print("PASS",label,
          "transverse tangent dimension",len(trans),
          "quadratic obstruction coefficients",len(vectors),
          "exact corrections",len(lifts),
          "denominators",[lifts[name][1] for name,_ in vectors],
          flush=True)

print("PASS: all transverse quadratic obstruction classes vanish in exact characteristic zero.")
print("Scope: only order-two extensions of degree-three Hilbert flatness; not intrinsic H2.")
