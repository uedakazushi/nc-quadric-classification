"""
Exact first-order AS4-cover lifting at three noncubic representatives.

Work over Q.  Set f1=u*v, f2=(u-a*v)*(b*u-v), theta=1-a*b,
delta^2=theta, and use the exchange automorphism
sigma(u)=(u-a*v)/delta, sigma(v)=(b*u-v)/delta,
sigma(c)=d/delta, sigma(d)=-delta*c.
The tested quadratic algebra is B_f^sigma (right Zhang product).
The cover uses the six relations centrality(u,v) and rc-rd/theta.

The Gr(7,16) tangent is computed from the degree-three overlap kernel.
For E=B^!, normality of w in E_2 is linearized in E_3, including
the change in the quotient map caused by varying the relations of E.
This is a first-order calculation at the selected rational points only;
it does not prove higher lifting, universal Noetherianity, or algebraicity.
Run: python3 computations/verify_noncubic_cover_tangent.py --case generic
Requires SymPy.  All ranks use exact rational arithmetic.
"""
import sympy as s
from itertools import product
import argparse
import json
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument("--case",choices=["generic","shared","coincident"],default="generic")
case=parser.parse_args().case
a0,b0,delta={"generic":(1,-3,2),"shared":(0,-3,1),"coincident":(0,0,1)}[case]
theta=1-a0*b0
assert delta*delta==theta
eta=s.Rational(1,theta)
N=4
def word_index(t):
 z=0
 for x in t:z=z*N+x
 return z
def tensor_row(r,side,v):
 out=s.zeros(1,64)
 for i,a in enumerate(r):
  if a:out[0,(i*N+v if side=='R' else v*16+i)]=a
 return out
def insert_rel(R):
 return s.Matrix.vstack(*[tensor_row(R.row(j),side,v) for side in ['L','R'] for j in range(R.rows) for v in range(4)])
def quotient(R):
 rr,p=R.rref(); rr=rr[:len(p),:]
 free=[i for i in range(R.cols) if i not in p]
 Q=s.zeros(len(free),R.cols)
 for a,j in enumerate(free):
  Q[a,j]=1
  for b,i in enumerate(p):Q[a,i]=-rr[b,j]
 return rr,list(p),free,Q
def rel(terms):
 a=s.zeros(1,16)
 for i,j,c in terms:a[0,i*4+j]+=c
 return a
u,v,c,d=range(4)
rows=[rel([(a,b,1),(b,a,-1)]) for a,b in [(u,v),(u,c),(u,d),(v,c),(v,d)]]
rc=rel([(c,c,1),(u,v,-1)])
rd=rel([(d,d,1),(u,u,-b0),(u,v,1+a0*b0),(v,v,-a0)])
R0=s.Matrix.vstack(*rows,rc,rd)
Sig=s.Matrix([[1,b0,0,0],[-a0,-1,0,0],[0,0,0,-theta],[0,0,1,0]])/delta
# Columns are images of generators. Twist multiplication a*b=a sigma(b).
T=s.kronecker_product(s.eye(4),Sig.inv()).T
Rorig=R0*T
R,p,free,Q=quotient(Rorig)
J=insert_rel(R)
Jrr,p3,f3,Q3=quotient(J)
K=J.T.nullspace()
Kmat=s.Matrix.hstack(*K)
print('B ranks',R.rows,J.rank(),'syzygies',Kmat.cols,'B3',Q3.rows,flush=True)
var=[(j,f) for j in range(7) for f in free]
# Linear map of relation perturbations, evaluated on syzygies and projected to B3.
base_cols=[]
for j,f in var:
 dr=s.zeros(7,16);dr[j,f]=1
 dj=insert_rel(dr)
 ob=Q3*dj.T*Kmat
 base_cols.append(s.Matrix(list(ob)))
O=s.Matrix.hstack(*base_cols)
tb=O.nullspace()
TB=s.Matrix.hstack(*tb)
print('quadratic Hilbert tangent',TB.cols,'rank constraint',O.rank(),flush=True)
# E=B^!, relations annihilate R.
L=s.Matrix.vstack(*[s.eye(16).row(f)-sum((R[j,f]*s.eye(16).row(p[j]) for j in range(7)),s.zeros(1,16)) for f in free])
JE=insert_rel(L)
rrE,pe,fe,QE=quotient(JE)
basis_rows=list(JE.T.rref()[1])
JB=JE[basis_rows,:]
Minv=JB[:,pe].inv()
print('E ranks',L.rows,JE.rank(),'E3',QE.rows,flush=True)
# AS cover H=centrality five relations + rc-eta rd.
H0=s.Matrix.vstack(*rows,rc-eta*rd)*T
Hcoef=H0[:,p]
wvec=Hcoef.nullspace()[0]
wvec=wvec/next(a for a in wvec if a)
w=s.zeros(1,16)
for j,a in enumerate(wvec):w[0,p[j]]=a
LW=s.Matrix.hstack(*[QE*tensor_row(w,'R',i).T for i in range(4)])
RW=s.Matrix.hstack(*[QE*tensor_row(w,'L',i).T for i in range(4)])
Tau=RW.gauss_jordan_solve(LW)[0] # w*x = Tau(x)*w
assert RW*Tau==LW
print('normal quadratic coordinates',list(wvec),'normalizer',Tau.tolist(),flush=True)
# Eq indexed generator then E3 coordinate.
def commutator(delta_w,delta_tau):
 cols=[]
 for i in range(4):
  z=tensor_row(delta_w,'R',i)
  for a in range(4):
   z-=Tau[a,i]*tensor_row(delta_w,'L',a)
   z-=delta_tau[a,i]*tensor_row(w,'L',a)
  cols.extend(QE*z.T)
 return s.Matrix(cols)
lift_cols=[]
for j in range(7):
 dw=s.zeros(1,16);dw[0,p[j]]=1
 lift_cols.append(commutator(dw,s.zeros(4)))
for a,i in product(range(4),repeat=2):
 dt=s.zeros(4);dt[a,i]=1
 lift_cols.append(commutator(s.zeros(1,16),dt))
LIFT=s.Matrix.hstack(*lift_cols)
# Fixed words commutator is a linear combination of JE basis.
lambdas=[]
for i in range(4):
 z=tensor_row(w,'R',i)
 for a in range(4):z-=Tau[a,i]*tensor_row(w,'L',a)
 lam=z[:,pe]*Minv
 assert lam*JB==z
 lambdas.append(lam)
baseobs=[]
for j,f in var:
 dl=s.zeros(9,16);dl[free.index(f),p[j]]=-1
 dJE=insert_rel(dl)[basis_rows,:]
 col=[]
 for lam in lambdas:col.extend(-QE*(lam*dJE).T)
 baseobs.append(s.Matrix(col))
BO=s.Matrix.hstack(*baseobs)*TB
rank_l=LIFT.rank();rank_aug=LIFT.row_join(BO).rank()
print('normal lift rank',rank_l,'with base',rank_aug,'obstruction quotient rank',rank_aug-rank_l,flush=True)
assert TB.cols == (19 if case=="coincident" else 18)
assert rank_l == rank_aug == 22
assert Tau == s.diag(1,1,-1,-1)
print("PASS: exact first-order normal-line lifting; no higher-order claim")
data={'tangent_dim':TB.cols,'normal_lift_rank':rank_l,'augmented_rank':rank_aug,'w':list(wvec),'normalizer':Tau}
print(json.dumps({'case':case,'a':a0,'b':b0,'delta':delta,**data},default=str,ensure_ascii=False,sort_keys=True))
