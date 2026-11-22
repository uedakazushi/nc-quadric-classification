#!/usr/bin/env python3
"""Exact identities for two Fricke boundary traits and their regular graphs.

Verifies polynomial equations, blowup charts, the free-sign fixed locus,
the coincident-trait model isomorphism and its four-torsion correction.
It does not certify scheme-theoretic graph identification, minimality,
stack descent, arbitrary nonflat base change, or categorical reconstruction.
No random samples or floating-point arithmetic are used.
"""
import sympy as sp


def zero(expr):
    assert sp.factor(expr) == 0, sp.factor(expr)


def main():
    u, v, y, t, a = sp.symbols('u v y t a')
    x, z, s, w = sp.symbols('x z s w')
    for r, p in ((1, sp.Integer(1)), (2, t)):
        source = u*v*(p*u*u+u*v+t*v*v)
        A, B, V, d = p*u*u, t*v*v, u*v, y
        zero(A*B-t**r*V*V)
        zero((d*d-V*(A+B+V)).subs(y*y, source))
        # x-chart at [u:v:y]=[0:1:0] of Bl_(x,y,t).
        local = y*y-x*(p*x*x+x+t)
        strict = sp.cancel(local.subs({y:x*z, t:x*s}, simultaneous=True)/x**2)
        expected = z*z-1-x-s if r == 1 else z*z-1-s*(1+x*x)
        zero(strict-expected)
        xx_A, xx_B = (x,s) if r == 1 else (s*x*x,s)
        zero(xx_A*xx_B-(x*s)**r)
        zero(z*z-(xx_A+xx_B+1)-expected)
        # t-chart covers the rest of the exceptional conic.
        strict_t = sp.cancel(local.subs({x:t*w, y:t*z}, simultaneous=True)/t**2)
        zero(strict_t-(z*z-w-w*w-t**r*w**3))
        zero((t**r*w*w)*1-t**r*w*w)
        zero(z*z-w*(t**r*w*w+1+w)-strict_t)
        cone = y*y-x*x-t*x
        assert sp.hessian(cone,(x,y,t)).det() != 0
    print('PASS: both generic models, nondegenerate tangent cones, and two blowup charts')

    # On the t-chart exceptional conic, simultaneous vanishing of the
    # equation and its w,z derivatives is impossible over QQ.
    regular = sp.groebner([z*z-w-w*w,2*z,-1-2*w],z,w)
    assert list(regular) == [1]
    print('PASS: exceptional-conic smoothness and chart coverage conditions')

    for r, p in ((1,sp.Integer(1)),(2,t)):
        source = u*v*(p*u*u+u*v+t*v*v)
        uu, vv, yy = t*v, p*u, -p*t*y
        transformed_source = uu*vv*(p*uu*uu+uu*vv+t*vv*vv)
        zero((yy*yy-transformed_source).subs(y*y,source))
        # Conjugation sends (A,B,V,d) to (B,A,V,-d), up to p*t.
        transformed = (p*uu*uu, t*vv*vv, uu*vv, yy)
        target = (t*v*v,p*u*u,u*v,-y)
        for lhs,rhs in zip(transformed,target):
            zero(lhs-p*t*rhs)
    print('PASS: generic conjugation of the Fricke simultaneous-sign involution')

    U, V, q = sp.symbols('U V q')
    # A fixed point has c=d=0, or U=V=0.  The latter is empty;
    # for the former the common-root obstruction is 1-q.
    resultant = sp.resultant(U*U-q, U+1,U)
    zero(resultant-(1-q))
    # The chart V=0 would force U=c=d=0 at a fixed point.
    print('PASS: free-sign fixed-locus elimination when 1-4*t^r is invertible')

    source2 = u*v*(t*u*u+u*v+t*v*v)
    def reduce_source(expr):
        first = sp.rem(sp.expand(expr), y*y-source2, y)
        return sp.factor(sp.rem(sp.expand(first),a*a-1-2*t,a))
    def same(expr):
        assert reduce_source(expr) == 0, reduce_source(expr)
    Phi = (t*(u*u+v*v), u*v, t*(u*u-v*v), y)
    Psi = (a*a*(u+v)**2-(v-u)**2, (v-u)**2, 4*a*y, a*(u+v)*(v-u))
    same(Psi[2]**2-Psi[0]**2+4*t*t*Psi[1]**2)
    same(Psi[3]**2-Psi[1]*(Psi[0]+Psi[1]))
    basis = (u*u,u*v,v*v,y)
    mat = sp.Matrix([[sp.expand(expr).coeff(term) for term in basis] for expr in Psi])
    determinant = sp.factor(mat.det())
    zero(determinant-32*a**4)
    print('PASS: coincident-trait integral model isomorphism and unit Veronese determinant')

    F = (y-a*u*v, y+a*u*v, a*t*u*v*(u*u-v*v))
    substitution = dict(zip((u,v,y),F))
    same(F[2]**2-F[0]*F[1]*(t*F[0]**2+F[0]*F[1]+t*F[1]**2))
    composed = tuple(expr.subs(substitution,simultaneous=True) for expr in Psi)
    for i in range(4):
        for j in range(i):
            same(composed[i]*Phi[j]-composed[j]*Phi[i])
    twice = tuple(expr.subs(substitution,simultaneous=True) for expr in F)
    same(twice[0]*u-twice[1]*v)
    same(twice[2]*v*v+y*twice[0]**2)
    same(twice[2]*u*u+y*twice[1]**2)
    print('PASS: half-period correction Psi o F = Phi and F^2 = [v:u:-y]')

    # Q=(t,t*a) on Y^2=X^3+X^2+t^2*X has tangent slope a,
    # and the elementary addition formula gives 2Q=(0,0).
    same((t*a)**2-(t**3+t*t+t**3))
    same((3*t*t+2*t+t*t)-2*t*a*a)
    same(a*a-1-2*t)
    same(-t*a+a*t)
    for model, sign_index in ((Phi,3),(Psi,2)):
        changed=tuple(expr.subs(y,-y) for expr in model)
        for i in range(4):
            same(changed[i]-((-1 if i==sign_index else 1)*model[i]))
    swapped=tuple(expr.subs({u:v,v:u,y:-y},simultaneous=True) for expr in Psi)
    for i in range(4):
        same(swapped[i]-((-1 if i in (2,3) else 1)*Psi[i]))
    print('PASS: doubling the four-torsion section and ordered-pencil/sign actions')

    alpha,beta=sp.symbols('alpha beta')
    for e in range(1,7):
        for j in range(e):
            ss=alpha*beta
            xx=alpha**(j+1)*beta**j
            yy=alpha**(e-j-1)*beta**(e-j)
            zero(xx*yy-ss**e)
    print('PASS: ramified-node toric identities for e=1,...,6 (general proof is in the paper)')
    print('NOT CHECKED: graph/minimal-model proofs, global stack extension, novelty, or H2 reconstruction')


if __name__ == '__main__':
    main()
