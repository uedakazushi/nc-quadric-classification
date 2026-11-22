"""Exact four-stratum certificate for one Q12 two-mass diagonal family.

Use q'=V0U0+V1U1 and q=W0V0+W1V1, short relations
r_a=q'+mu*u and r_b=q+lam*x, and long relations
W0 V1 U0 and W1 V0 U1.  Each mass is tested at 0 and 1.
Rescaling the diagonal arrows identifies any nonzero value with 1,
so these four points cover geometric fibers of THIS family only.

Over Q[lam,mu] the six relation vectors have a constant unimodular
minor; all path modules and the algebra are free.  Fiber exactness
then implies split exactness after arbitrary Q-algebra base change.
This does NOT prove the universal statement for all foundations.

The products and d1*d2 are exact integer matrices.  Ranks modulo
101 give rigorous lower bounds over Q; multiplication and the number
of columns give matching upper bounds, so no floating point is used.
"""
from collections import defaultdict
import sympy as S

BLOCK = {(i,i): 1 for i in range(4)}
BLOCK.update({(0,1):2,(1,2):2,(2,3):2,(0,2):4,(1,3):4,(0,3):6})
BASIS = [(i,j,h) for (i,j),dim in sorted(BLOCK.items()) for h in range(dim)]
U = [(0,1,i) for i in range(2)]
V = [(1,2,i) for i in range(2)]
W = [(2,3,i) for i in range(2)]
u, x = (0,2,3), (1,3,3)
ARROWS = U + V + W + [u,x]
C0 = [(L,R) for L in BASIS for R in BASIS if L[0] == R[1]]
C1 = [(L,a,R) for a in ARROWS for L in BASIS for R in BASIS
      if L[0] == a[1] and R[1] == a[0]]
REL_ENDPOINTS=[(0,2),(1,3),(0,3),(0,3)]
C2 = [(L,r,R) for r,(src,tgt) in enumerate(REL_ENDPOINTS)
      for L in BASIS for R in BASIS if L[0]==tgt and R[1]==src]
assert (len(BASIS),len(C0),len(C1),len(C2))==(24,68,52,8)
LOC0 = {v:i for i,v in enumerate(C0)}
LOC1 = {v:i for i,v in enumerate(C1)}

def modular_rank(M, p=101):
    """Gaussian elimination in F_p: certified rank lower bound over Q."""
    a = [[int(M[i,j]) % p for j in range(M.cols)] for i in range(M.rows)]
    h = 0
    for j in range(M.cols):
        pivot = next((i for i in range(h, M.rows) if a[i][j]), None)
        if pivot is None: continue
        a[h], a[pivot] = a[pivot], a[h]
        scale = pow(a[h][j], -1, p)
        for k in range(j,M.cols):a[h][k]=a[h][k]*scale % p
        for i in range(h+1,M.rows):
            if (coeff := a[i][j]):
                for k in range(j,M.cols):a[i][k]=(a[i][k]-coeff*a[h][k]) % p
        h += 1
        if h==M.rows:break
    return h

def verify(lam, mu):
    # Quadratic path 00 = -11 - mass * diagonal; 01,10,11 are free.
    def quadratic(mass):
        A = S.zeros(4,4)
        A[2,0] = -1
        A[3,0] = -mass
        for j in range(1,4):A[j-1,j] = 1
        return A
    E, F = quadratic(mu), quadratic(lam)
    theta = S.zeros(12,6)
    q = [1,0,0,1]
    for w in range(2):
        for v in range(2):
            for a in range(2):theta[4*w+2*v+a,w]=q[2*v+a]
        theta[8+w,w] = mu
    for a in range(2):
        for w in range(2):
            for v in range(2):theta[4*w+2*v+a,2+a]=q[2*w+v]
        theta[10+a,2+a] = lam
    theta[2,4]=1
    theta[5,5]=1
    piv=list(range(6));free=list(range(6,12))
    P=theta.extract(piv,range(6))
    assert P.det()==1
    quotient=S.zeros(6,12)
    coeff=-theta.extract(free,range(6))*P.inv()
    for k in range(6):
        for j in range(6):quotient[k,piv[j]] = coeff[k,j]
        quotient[k,free[k]] = 1
    assert quotient*theta==S.zeros(6,6)
    emb=S.zeros(5,4)
    for j,i in enumerate([1,2,3,4]):emb[i,j]=1
    cpre=S.zeros(12,10);dpre=S.zeros(12,10)
    for w in range(2):
        for j in range(5):cpre[4*w+j if j<4 else 8+w,5*w+j]=1
    for j in range(4):
        for a in range(2):dpre[2*j+a,2*j+a]=1
    for a in range(2):dpre[10+a,8+a]=1
    C=quotient*cpre*S.kronecker_product(S.eye(2),emb)
    D=quotient*dpre*S.kronecker_product(emb,S.eye(2))
    assert C*S.kronecker_product(S.eye(2),E)==D*S.kronecker_product(F,S.eye(2))

    def prod(left,right):
        s,t,i=left; a,b,j=right
        if s!=b:return {}
        if s==t:return {right:S.Integer(1)}
        if a==b:return {left:S.Integer(1)}
        if (a,s,t)==(0,1,2):col=2*i+j; mat=E; key=(0,2)
        elif (a,s,t)==(1,2,3):col=2*i+j; mat=F; key=(1,3)
        elif (a,s,t)==(0,2,3):col=4*i+j; mat=C; key=(0,3)
        elif (a,s,t)==(0,1,3):col=2*i+j; mat=D; key=(0,3)
        else:raise AssertionError((left,right))
        return {(key[0],key[1],h):mat[h,col] for h in range(mat.rows) if mat[h,col]}

    def mul_expr(a,b):
        out=defaultdict(int)
        for k,c in a.items():
            for h,d in b.items():
                for v,w in prod(k,h).items():out[v]+=c*d*w
        return {k:v for k,v in out.items() if v}

    def path_prod(path):
        out={path[0]:S.Integer(1)}
        for g in path[1:]:out=mul_expr({g:S.Integer(1)},out)
        return out
    rel=[
        [([U[0],V[0]],1),([U[1],V[1]],1),([u],mu)],
        [([V[0],W[0]],1),([V[1],W[1]],1),([x],lam)],
        [([U[0],V[1],W[0]],1)],
        [([U[1],V[0],W[1]],1)],
    ]
    for words in rel:
        acc=defaultdict(int)
        for path,v in words:
            for elem,b in path_prod(path).items():acc[elem]+=v*b
        assert all(v==0 for v in acc.values())

    d1=S.zeros(68,52);d2=S.zeros(52,8)
    for n,(L,a,R) in enumerate(C1):
        for h,v in prod(L,a).items():d1[LOC0[(h,R)],n]+=v
        for h,v in prod(a,R).items():d1[LOC0[(L,h)],n]-=v
    for n,(L,rid,R) in enumerate(C2):
        for path,coefficient in rel[rid]:
            for j,a in enumerate(path):
                left={L:S.Integer(1)}
                for g in reversed(path[j+1:]):left=mul_expr(left,{g:S.Integer(1)})
                right={R:S.Integer(1)}
                for g in path[:j]:right=mul_expr({g:S.Integer(1)},right)
                for L2,b in left.items():
                    for R2,v in right.items():d2[LOC1[(L2,a,R2)],n]+=coefficient*b*v
    assert d1*d2==S.zeros(68,8)
    # Multiplication C0 -> Lambda has a section, so its kernel has rank
    # 68-24=44.  Since im d1 lies in this kernel, rank d1 <=44.
    # The relation term has eight columns, so rank d2 <=8.
    ranks=(modular_rank(d1),modular_rank(d2))
    assert ranks==(44,8), (lam,mu,ranks)
    print(f"PASS: lam={lam}, mu={mu}, quadratic ranks=({4 if mu else 3},{4 if lam else 3}), d1=44,d2=8")

if __name__ == "__main__":
    for lam,mu in [(0,0),(1,0),(0,1),(1,1)]:verify(lam,mu)
    print("PASS: all four zero/nonzero strata of the explicit Q12 two-mass family")
