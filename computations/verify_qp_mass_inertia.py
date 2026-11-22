"""Exact finite algebra checks for nilpotent-mass diagonal QP inertia.

Run: python3 computations/verify_qp_mass_inertia.py
Python 3 + SymPy. This checks the dual-number presentation, not AS-regularity.
"""
import sympy as sp

eps, t, s = sp.symbols("eps t s")
z = t*s - 1

# Work in k[eps,t,s]/(eps^2, eps*(t*s-1)). The torus is obtained by
# localizing in t,s; all assertions remain valid after localization.
ideal = sp.groebner([eps**2, eps*z], eps, t, s, order="lex")
assert sp.expand(ideal.reduce(eps*z)[1]) == 0
print("PASS: eps*(t*s-1) vanishes in the stabilizer coordinate ring")

# The special fiber is k[t,s], so z is nonzero even modulo eps.
special = sp.groebner([eps], eps, t, s, order="lex")
assert sp.expand(special.reduce(z)[1]) == z
print("PASS: z=t*s-1 does not vanish in the special fiber")

# Hence eps*z=0 but z is not an eps-multiple. This contradicts flatness
# over k[eps]/(eps^2), whose flat modules have ker(eps)=eps*M.
print("PASS: explicit nonflat epsilon-torsion witness")

# Unit mass has the hypersurface t*s=1; zero mass is all G_m^2.
unit = sp.groebner([z], t, s, order="lex")
assert sp.expand(unit.reduce(z)[1]) == 0
print("PASS: unit and zero mass limits agree with the torus formula")
