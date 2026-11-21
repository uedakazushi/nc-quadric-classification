"""Exact checks for noncubic moduli fibers and special stabilizers.
Run: python3 computations/verify_noncubic_boundary.py (SymPy).
This proves polynomial identities and the displayed finite matrix group order;
it does not certify relative moduli equivalence or the abstract smoothness proof.
"""
import sympy as s
from collections import deque
u,v,a,b,c,aa,bb,cc,xi,t=s.symbols('u v a b c aa bb cc xi t')
I=s.I

def zero(x): return s.cancel(s.expand(x)) == 0

def eq(name,x): assert zero(x),(name,s.factor(x))

def meq(name,X): assert all(zero(x) for x in X),(name,X)

def sub(f,A):
    x,y=A*s.Matrix([u,v])
    return s.expand(f.subs({u:x,v:y}, simultaneous=True))

Delta=b*b-4*a*c
chi=b*b/Delta
F=(1-xi)*b*b+4*xi*a*c
eq('fiber equation',b*b-xi*Delta-F)
eq('fiber zero',F.subs(xi,0)-b*b)
eq('fiber one',F.subs(xi,1)-4*a*c)
eq('derivative a',s.diff(chi,a)-4*b*b*c/Delta**2)
eq('derivative b',s.diff(chi,b)+8*a*b*c/Delta**2)
eq('derivative c',s.diff(chi,c)-4*b*b*a/Delta**2)
eq('coincident local quotient',chi.subs(b,1)-1-4*a*c/(1-4*a*c))
eq('coincident mixed Hessian',s.diff(chi.subs(b,1),a,c).subs({a:0,c:0})-4)
D=b*bb-2*a*cc-2*aa*c
Delta2=bb*bb-4*aa*cc
Syl=s.Matrix([[a,b,c,0],[0,a,b,c],[aa,bb,cc,0],[0,aa,bb,cc]])
eq('resultant',D*D-Delta*Delta2-4*Syl.det())

f1=u*v
f2=u*u-v*v
R=s.diag(s.Matrix([[0,-1],[1,0]]),I,I)
T=s.diag(s.Matrix([[-1,1],[1,1]]),s.Matrix([[0,I],[-2*I,0]]))
S=s.diag(1,-1,I,1)
e1=s.diag(1,1,-1,1)
e2=s.diag(1,1,1,-1)
for name,A,targets in [('R',R,(-f1,-f2)),('T',T,(-f2,-4*f1)),('S',S,(-f1,f2))]:
    eq(name+' f1',sub(f1,A[:2,:2])-targets[0])
    eq(name+' f2',sub(f2,A[:2,:2])-targets[1])
meq('R squared',R**2+s.eye(4))
meq('T squared',T**2-2*s.eye(4))
meq('S squared is e1',S**2-e1)
meq('S fourth',S**4-s.eye(4))
meq('S commutes e1',S*e1-e1*S)
meq('S commutes e2',S*e2-e2*S)

def normal(A):
    nz=next(x for x in A if x!=0)
    return tuple(s.expand(x/nz) for x in A)

def closure(gens,n,cap):
    one=normal(s.eye(n)); seen={one}; todo=deque([one])
    while todo:
        X=s.Matrix(n,n,todo.popleft())
        for g in gens:
            q=normal(X*g)
            if q not in seen:
                seen.add(q);todo.append(q)
                assert len(seen)<=cap,'unexpected group growth'
    return seen
H0=closure([R,T,S,e1,e2],4,32)
assert len(H0)==32
base=closure([R[:2,:2],T[:2,:2],S[:2,:2]],2,8)
assert len(base)==8
base_one=normal(s.eye(2))
kernel=[x for x in H0 if normal(s.Matrix(4,4,x)[:2,:2])==base_one]
assert len(kernel)==4
for E in (s.eye(4),e1,e2,e1*e2):
    meq('every lift of extra involution squares to e1',(S*E)**2-e1)

# Coincident pair: O(uv) on W and signed permutations D8 on c,d.
Tt=s.diag(t,1/t,1,1)
J=s.diag(s.Matrix([[0,1],[1,0]]),s.eye(2))
tau=s.diag(s.eye(2),s.Matrix([[0,1],[1,0]]))
eq('torus preserves uv',sub(f1,Tt[:2,:2])-f1)
eq('reflection preserves uv',sub(f1,J[:2,:2])-f1)
meq('reflection inverts torus',J*Tt*J-Tt.subs(t,1/t))
meq('ruling exchange swaps signs',tau*e1*tau-e2)
meq('diagonal mu2 kernel',Tt.subs(t,-1)*(e1*e2)+s.eye(4))
D8=closure([e1,e2,tau],4,8)
assert len(D8)==8
# First-order boundary representation has weights 2,-2.
new=sub(a*u*u+u*v+c*v*v,Tt[:2,:2])
eq('positive tangent weight',s.Poly(new,u,v).coeff_monomial(u*u)-t*t*a)
eq('negative tangent weight',s.Poly(new,u,v).coeff_monomial(v*v)-c/(t*t))
print('PASS: exact fiber/resultant/derivative identities; harmonic projective stabilizer order32, root image8 and kernel4; coincident quotient relations and boundary torus weights')

# Coincident connected-inertia action on the intrinsic transverse directions.
D0 = s.diag(1, -1)
DL = s.diag(1, 1, -1, -1)
J = s.BlockMatrix([[s.zeros(4), DL], [-DL, s.zeros(4)]]).as_explicit()
omega = J.inv()
L = s.Matrix([
    [0, 0, -1, 0], [0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 1, 0],
    [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, -1],
])
assert L.T * omega * L == s.zeros(4)
z = s.Symbol("z", nonzero=True)
Tz = s.diag(z, 1)
rho = s.diag(s.kronecker_product(Tz.inv().T, Tz.T),
             s.kronecker_product(Tz, Tz.inv().T))
RL = s.diag(z, 1/z, 1, 1)
assert rho * L == L * RL
assert rho.T * omega * rho == omega

pairs = [(i, j) for i in range(4) for j in range(i, 4)]
L_weights = [1, -1, 0, 0]
weights = [-L_weights[i]-L_weights[j] for i, j in pairs]

def coordinates(Q):
    assert Q == Q.T
    return s.Matrix([Q[i, j] for i, j in pairs])

orbit = []
for factor in range(2):
    for i in range(2):
        for j in range(2):
            a, b = s.zeros(2), s.zeros(2)
            (a if factor == 0 else b)[i, j] = 1
            c, k = D0*a*D0, -b.T
            infinitesimal = s.diag(
                -s.kronecker_product(a.T, s.eye(2))
                -s.kronecker_product(s.eye(2), b.T),
                s.kronecker_product(c, s.eye(2))
                -s.kronecker_product(s.eye(2), k.T),
            )
            orbit.append(coordinates(L.T*omega*infinitesimal*L))
O = s.Matrix.hstack(*orbit)
assert O.rank() == 6
assert all(len({weights[i] for i in range(10) if O[i, j] != 0}) <= 1
           for j in range(O.cols))

normal_indices = [pairs.index((2, 2)), pairs.index((3, 3))]
assert O[normal_indices, :] == s.zeros(2, 8)
assert [weights[i] for i in normal_indices] == [0, 0]

expected_tangent = {-2: 1, -1: 2, 0: 4, 1: 2, 2: 1}
expected_orbit = {-2: 0, -1: 2, 0: 2, 1: 2, 2: 0}
expected_hh2 = {-2: 1, -1: 0, 0: 2, 1: 0, 2: 1}
for weight in range(-2, 3):
    rows = [i for i, w in enumerate(weights) if w == weight]
    rank = O[rows, :].rank()
    assert len(rows) == expected_tangent[weight]
    assert rank == expected_orbit[weight]
    assert len(rows)-rank == expected_hh2[weight]

dbeta, dgamma = s.zeros(8, 4), s.zeros(8, 4)
dbeta[5, 1] = 1
dgamma[6, 0] = -1
qb, qg = coordinates(L.T*omega*dbeta), coordinates(L.T*omega*dgamma)
assert O.row_join(qb).row_join(qg).rank() == 8
assert all(qb[i] == 0 or weights[i] == 2 for i in range(10))
assert all(qg[i] == 0 or weights[i] == -2 for i in range(10))
normal_basis = s.eye(10)[:, normal_indices]
assert O.row_join(qb).row_join(qg).row_join(normal_basis).rank() == 10

print("PASS: symplectic stabilizer torus and tautological weights (1,-1,0,0)")
print("PASS: LG tangent weights", expected_tangent)
print("PASS: orbit weights", expected_orbit)
print("PASS: HH2 weights -2,0,0,2; boundary weights -2,2; normal weights 0,0")
