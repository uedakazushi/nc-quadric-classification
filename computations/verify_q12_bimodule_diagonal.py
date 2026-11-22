"""Exact full bimodule diagonal test for a Q12 noncubic rank-24 algebra.

Run: python3 computations/verify_q12_bimodule_diagonal.py
Requires Python 3 and SymPy. A finite rational sample certificate, NOT
a proof of relative exactness for every base or of H2 recognition.
"""
import sympy as S
from collections import defaultdict

# Basis element (source,target,index) in a directed four-vertex algebra.
block = {(i,i):1 for i in range(4)}
block.update({(0,1):2,(1,2):2,(2,3):2,(0,2):4,(1,3):4,(0,3):6})
basis = [(i,j,h) for (i,j),v in sorted(block.items()) for h in range(v)]
assert len(basis) == 24
U=[(0,1,i) for i in range(2)]
V=[(1,2,i) for i in range(2)]
W=[(2,3,i) for i in range(2)]
u,x=(0,2,3),(1,3,3)
arrows=U+V+W+[u,x]

# E,F are (4 quadratic paths + 1 diagonal arrow)/(q), with
# nondecomposable q=(00)+(11). Choose (01,10,11,diagonal) as basis.
A=S.zeros(4,4)
for j in range(4):
    if j==0:A[2,j]=-1
    else:A[j-1,j]=1

# B has 8 cubic paths, 2 paths through u, and 2 through x.
# Four short-relation consequences and two independent long relations.
theta=S.zeros(12,6)
q=[1,0,0,1]
for w in range(2):
    for v in range(2):
        for a in range(2):theta[4*w+2*v+a,w]=q[2*v+a]
for a in range(2):
    for w in range(2):
        for v in range(2):theta[4*w+2*v+a,2+a]=q[2*w+v]
theta[2,4]=theta[5,5]=1
piv=list(range(6));free=list(range(6,12))
P=theta.extract(piv,range(6))
assert P.det()!=0
m=S.zeros(6,12)
coeff=-theta.extract(free,range(6))*P.inv()
for k in range(6):
    for j in range(6):m[k,piv[j]]=coeff[k,j]
    m[k,free[k]]=1
assert m*theta==S.zeros(6,6)
emb=S.zeros(5,4)
for j,i in enumerate([1,2,3,4]):emb[i,j]=1
cpre=S.zeros(12,10);dpre=S.zeros(12,10)
for w in range(2):
    for j in range(5):cpre[4*w+j if j<4 else 8+w,5*w+j]=1
for j in range(4):
    for a in range(2):dpre[2*j+a,2*j+a]=1
for a in range(2):dpre[10+a,8+a]=1
C=m*cpre*S.kronecker_product(S.eye(2),emb)
D=m*dpre*S.kronecker_product(emb,S.eye(2))
assert C*S.kronecker_product(S.eye(2),A)==D*S.kronecker_product(A,S.eye(2))

def prod(left,right):
    s,t,i=left; a,b,j=right
    if s!=b:return {}
    if s==t:return {right:S.Integer(1)}
    if a==b:return {left:S.Integer(1)}
    if (a,s,t)==(0,1,2):col=2*i+j;mat=A;key=(0,2)
    elif (a,s,t)==(1,2,3):col=2*i+j;mat=A;key=(1,3)
    elif (a,s,t)==(0,2,3):col=4*i+j;mat=C;key=(0,3)
    elif (a,s,t)==(0,1,3):col=2*i+j;mat=D;key=(0,3)
    else:raise ValueError((left,right))
    return {(key[0],key[1],h):mat[h,col] for h in range(mat.rows) if mat[h,col]}

def mul_expr(x,y):
    out=defaultdict(lambda:S.Integer(0))
    for k,a in x.items():
        for h,b in y.items():
            for j,v in prod(k,h).items():out[j]+=a*b*v
    return {k:v for k,v in out.items() if v}

def path_prod(path):
    out={path[0]:S.Integer(1)}
    for g in path[1:]:out=mul_expr({g:S.Integer(1)},out)
    return out

# Relations are lists of paths in execution order.
rel=[
 (0,2,[([U[0],V[0]],1),([U[1],V[1]],1)]),
 (1,3,[([V[0],W[0]],1),([V[1],W[1]],1)]),
 (0,3,[([U[0],V[1],W[0]],1)]),
 (0,3,[([U[1],V[0],W[1]],1)])
]
for source,target,words in rel:
    acc={}
    for path,v in words:
        for elem,b in path_prod(path).items():acc[elem]=acc.get(elem,0)+v*b
    assert all(v==0 for v in acc.values())

c0=[(L,R) for L in basis for R in basis if L[0]==R[1]]
c1=[(L,a,R) for a in arrows for L in basis for R in basis
    if L[0]==a[1] and R[1]==a[0]]
c2=[(L,r,R) for r,(i,j,_) in enumerate(rel) for L in basis for R in basis
    if L[0]==j and R[1]==i]
assert (len(c0),len(c1),len(c2))==(68,52,8)
loc0={k:i for i,k in enumerate(c0)}
loc1={k:i for i,k in enumerate(c1)}
d1=S.zeros(68,52);d2=S.zeros(52,8)
for n,(L,a,R) in enumerate(c1):
    for h,v in prod(L,a).items():d1[loc0[(h,R)],n]+=v
    for h,v in prod(a,R).items():d1[loc0[(L,h)],n]-=v
for n,(L,rid,R) in enumerate(c2):
    for path,coefficient in rel[rid][2]:
        for j,a in enumerate(path):
            left={L:S.Integer(1)}
            for g in reversed(path[j+1:]):
                left=mul_expr(left,{g:S.Integer(1)})
            right={R:S.Integer(1)}
            for g in path[:j]:
                right=mul_expr({g:S.Integer(1)},right)
            for L2,b in left.items():
                for R2,v in right.items():
                    d2[loc1[(L2,a,R2)],n]+=coefficient*b*v
assert d1*d2==S.zeros(68,8)
assert (d1.rank(),d2.rank())==(44,8)
print("PASS: C0,C1,C2 dimensions (68,52,8); Lambda dimension 24")
print("PASS: d1*d2=0; exact ranks (44,8); no bimodule degree-2 syzygy")
print("PASS: all identities computed over Q in a noncubic Q12 sample")
