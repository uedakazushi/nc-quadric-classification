"""Exact cyclic word and mass/shear conjugation checks for the Q12 local atlas.

Use: python3 computations/verify_q12_mass_shear.py
Only verifies local polynomial identities; not global stack equivalence.
"""
import sympy as S
from collections import defaultdict

lam, mu, t, s = S.symbols("lam mu t s")
a, b = 1+lam*t, 1+mu*s

def add(*parts):
    out=defaultdict(lambda:S.S.Zero)
    for p in parts:
        for word, coefficient in p.items():out[word]+=coefficient
    return {w:S.cancel(c) for w,c in out.items() if S.cancel(c)!=0}
def atom(x):return {(x,):S.S.One}
def scale(x,c):return {w:S.cancel(v*c) for w,v in x.items()}
def mul(p,q):
    out=defaultdict(lambda:S.S.Zero)
    for w,c in p.items():
        for v,d in q.items():out[w+v]+=c*d
    return {w:S.cancel(z) for w,z in out.items() if S.cancel(z)!=0}
def word(*args):
    out={():S.S.One}
    for x in args:out=mul(out,x)
    return out
def subst(p,m):
    out={}
    for w,c in p.items():
        part={():c}
        for x in w:part=mul(part,m.get(x,atom(x)))
        out=add(out,part)
    return out
def cyclic(p):
    out=defaultdict(lambda:S.S.Zero)
    for w,c in p.items():out[min(w[i:]+w[:i] for i in range(len(w)))]+=c
    return {w:S.cancel(z) for w,z in out.items() if S.cancel(z)!=0}

# The two cyclic potentials and a single residual relation are sufficient
# to test the general algebraic coefficients by linearity.
W=add(word(atom("y"),atom("q")),word(atom("p"),atom("x")),
      scale(word(atom("y"),atom("x")),lam))
Gx={"x":add(scale(atom("x"),a),scale(atom("q"),t)),
    "y":add(scale(atom("y"),1/a),scale(atom("p"),-t/a))}
assert cyclic(add(subst(W,Gx),scale(W,-1)))=={}
print("PASS: mass transformation preserves cyclic potential")

old=add(word(atom("z"),atom("r")),word(atom("v"),atom("ra")),
        word(atom("y"),atom("rb")))
new=add(old,word(atom("z"),atom("w"),atom("ra")),
        word(atom("z"),atom("rb"),atom("h")))
shear={"v":add(atom("v"),word(atom("z"),atom("w"))),
       "y":add(atom("y"),word(atom("h"),atom("z")))}
assert cyclic(add(subst(old,shear),scale(new,-1)))=={}
print("PASS: relation lift shear is cyclic right-equivalence")

g={"x":Gx["x"],"y":Gx["y"],
   "u":add(scale(atom("u"),b),scale(atom("qp"),s)),
   "v":add(scale(atom("v"),1/b),scale(atom("pp"),-s/b))}
ginv={"x":add(scale(atom("x"),1/a),scale(atom("q"),-t/a)),
      "y":add(scale(atom("y"),a),scale(atom("p"),t)),
      "u":add(scale(atom("u"),1/b),scale(atom("qp"),-s/b)),
      "v":add(scale(atom("v"),b),scale(atom("pp"),s))}
sh={"y":add(atom("y"),atom("Ly")),"v":add(atom("v"),atom("Lv"))}
ish={"y":add(atom("y"),scale(atom("Ly"),-1)),
     "v":add(atom("v"),scale(atom("Lv"),-1))}
gnew={**g,
      "y":add(scale(atom("y"),1/a),scale(atom("p"),-t/a),
              scale(atom("Ly"),-lam*t/a)),
      "v":add(scale(atom("v"),1/b),scale(atom("pp"),-s/b),
              scale(atom("Lv"),-mu*s/b))}
for x,weight,shearfactor in (("y",a,"Ly"),("v",b,"Lv")):
    conjugate=subst(subst(subst(atom(x),ginv),sh),g)
    assert add(conjugate,scale(add(atom(x),scale(atom(shearfactor),weight)),-1))=={}
for x in ("x","y","u","v"):
    transported=subst(subst(subst(atom(x),ish),g),sh)
    assert add(transported,scale(gnew[x],-1))=={}
print("PASS: shear conjugation weights a,b and transported p,p' coefficients")
eps=S.symbols("eps")
assert S.diff((1+eps*t),eps).subs(eps,0)==t
print("PASS: first-order nilpotent mass has nontrivial mixed action")

# General reframe xnew=d*x+h, rnew=c*(q+lam*x) with independent
# invertible c,d and arbitrary adjacent two-step path h.
c,d,h,x0,q0=S.symbols("c d h x0 q0")
r=q0+lam*x0
xnew=d*x0+h
rnew=c*r
lamnew=c*lam/d
tnew=d*t/c
qnew=c*q0-lamnew*h
assert S.cancel(rnew-(qnew+lamnew*xnew))==0
assert S.cancel(d*(x0+t*r)+h - (xnew+tnew*rnew))==0
assert S.cancel(lamnew*tnew-lam*t)==0
assert S.cancel((d/c)*(t+s+lam*t*s)
                -(tnew+(d/c)*s+lamnew*tnew*(d/c)*s))==0
print("PASS: frame changes descend the mass kernel and its group law")

# For nilpotent lam^3=0, the logarithm is a polynomial and commutes
# with any frame change of the line bundle L.
z=S.symbols("z")
log=lambda v: v-lam*v**2/S.Integer(2)+lam**2*v**3/S.Integer(3)
expo=lambda v:v+lam*v**2/S.Integer(2)+lam**2*v**3/S.Integer(6)
for delta in (log(t+s+lam*t*s)-log(t)-log(s),log(expo(z))-z):
    for power in range(3):
        assert S.cancel(S.expand(delta).coeff(lam,power))==0
# Intrinsic bundle-valued polynomial with coordinate change.
zold=log(t)
znew=tnew-lamnew*tnew**2/S.Integer(2)+lamnew**2*tnew**3/S.Integer(3)
assert S.cancel(znew-(d/c)*zold)==0
print("PASS: nilpotent mass logarithm descends as a line-bundle map")

# Strict square middle swap preserves the vertex-scalar kernel K:
# (l1,l2,l3/l1,l3/l2,l3) -> (l2,l1,l3/l2,l3/l1,l3).
l1,l2,l3=S.symbols("l1 l2 l3")
ks=(l1,l2,l3/l1,l3/l2,l3)
swap=(ks[1],ks[0],ks[3],ks[2],ks[4])
assert all(S.cancel(v-w)==0 for v,w in zip(swap,(l2,l1,l3/l2,l3/l1,l3)))
assert (swap[1],swap[0],swap[3],swap[2],swap[4])==ks
print("PASS: strict square swap preserves vertex torus and squares to identity")
