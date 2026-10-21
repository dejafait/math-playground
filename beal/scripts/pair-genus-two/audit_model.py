"""Independent L110 replay: integer polynomial triples, no producer imports.

Elements are (A+B*y)/C, y^2=D, with a single common denominator.
All comparisons are exact; all residual coefficients go to the certificate.
"""
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from math import comb, gcd, lcm
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def trim(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, n):
    return trim([n*x for x in a])


def mul(a, b):
    c = [0] * max(0, len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def prim(a):
    a = trim(a)
    if not a:
        return []
    g = abs(reduce(gcd, a))
    if a[-1] < 0:
        g = -g
    return [x//g for x in a]


def pgcd(a, b):
    a, b = prim(a), prim(b)
    while b:
        r = a
        while len(r) >= len(b):
            r = prim(add(scale(r, b[-1]),
                         scale([0]*(len(r)-len(b))+b, -r[-1])))
        a, b = b, r
    return prim(a)


def exact(a, b):
    r = list(map(Fraction, a))
    q = [Fraction(0)]*max(0, len(a)-len(b)+1)
    while r and len(r) >= len(b):
        n, c = len(r)-len(b), r[-1]/b[-1]
        q[n] = c
        r = add(r, scale([0]*n+b, -c))
    assert not r
    assert all(x.denominator == 1 for x in q)
    return trim([int(x) for x in q])


def derivative(a):
    return [i*a[i] for i in range(1, len(a))]


class E:
    def __init__(self, D, a=0, b=0, c=1):
        self.D = D
        a, b, c = [trim(x if isinstance(x, list) else [x])
                   for x in (a, b, c)]
        assert c
        g = pgcd(pgcd(a, b), c)
        a, b, c = [exact(x, g) for x in (a, b, c)]
        content = abs(reduce(gcd, a+b+c))
        if c[-1] < 0:
            content = -content
        self.a, self.b, self.c = [[x//content for x in p] for p in (a, b, c)]

    def lift(self, other):
        if isinstance(other, E):
            assert other.D == self.D
            return other
        return E(self.D, other)

    def __add__(self, other):
        o = self.lift(other)
        return E(self.D, add(mul(self.a, o.c), mul(o.a, self.c)),
                 add(mul(self.b, o.c), mul(o.b, self.c)), mul(self.c, o.c))

    __radd__ = __add__

    def __neg__(self):
        return E(self.D, scale(self.a, -1), scale(self.b, -1), self.c)

    def __sub__(self, other):
        return self + -self.lift(other)

    def __rsub__(self, other):
        return self.lift(other) + -self

    def __mul__(self, other):
        o = self.lift(other)
        return E(self.D, add(mul(self.a, o.a), mul(self.D, mul(self.b, o.b))),
                 add(mul(self.a, o.b), mul(self.b, o.a)), mul(self.c, o.c))

    __rmul__ = __mul__

    def __truediv__(self, other):
        o = self.lift(other)
        norm = add(mul(o.a, o.a), scale(mul(self.D, mul(o.b, o.b)), -1))
        assert norm
        return self * E(self.D, mul(o.a, o.c), scale(mul(o.b, o.c), -1), norm)

    def __rtruediv__(self, other):
        return self.lift(other)/self

    def __pow__(self, n):
        if n < 0:
            return (1/self)**(-n)
        r, a = self.lift(1), self
        while n:
            if n & 1:
                r = r*a
            n //= 2
            if n:
                a = a*a
        return r

    def data(self):
        return {"constant_numerator": self.a, "quadratic_numerator": self.b,
                "common_denominator": self.c}


def ev(coeff, x):
    r = x*0
    for c in reversed(coeff):
        r = r*x+c
    return r


checks, residuals = {}, {}


def check(name, ok):
    assert name not in checks
    checks[name] = bool(ok)


def zero(name, val):
    residuals[name] = val.data()
    check(name, not val.a and not val.b)


raw = (HERE/'model-certificate.json').read_bytes()
saved = json.loads(raw)
input_raw = (HERE.parent.parent/saved['input']).read_bytes()
source = json.loads(input_raw)
check("input_hash", sha256(input_raw).hexdigest() == saved["input_sha256"])

phi = [1]
for _ in range(5):
    phi = mul(phi, [1, 1, 3])
phi = mul(phi, [1, -5])
check("phi", phi == source["phi_coefficients_ascending"])
H = [{}, {}]
for i, ci in enumerate(phi):
    for j in range(i+1):
        m = (i-j, j//2)
        H[j % 2][m] = H[j % 2].get(m, 0)+ci*comb(i, j)*(-3)**(j//2)
H = [{m: c for m, c in h.items() if c} for h in H]
for label, h in zip(("H0", "H1"), H):
    check(label+"_complete", source["invariant_polynomials"][label] ==
          [{"exponents_u_z": list(m), "coefficient": c} for m, c in sorted(h.items())])

F, K, L = [1, 3, -3, -4, 1, 1], [-1, -1, 1], [-1, 1, 1]
R = [77, 572, -66, -704, -275]
f = mul([-4, 0, 1], R)
delta = add(scale(mul([1]*6, [1]*6), 121), scale([1]*11, -396))
P = exact(delta, [1, -2, 1])
polys = {"Delta": delta, "P8": P, "R4": R, "f6": f, "F": F, "K": K, "L": L}
for name, p in polys.items():
    check("coefficients_"+name, list(map(Fraction, saved["coefficients_ascending"][name])) == p)
check("sextic_squarefree", pgcd(f, derivative(f)) == [1])
check("ordered_squarefree", pgcd(P, derivative(P)) == [1])
check("degree", len(f)-1 == saved["actual_degree"] == 6 and saved["required_degree"] == [5, 6])
check("saved_gcd", saved["squarefree_gcd"] == ["1"])
check("P_reciprocal", P == P[::-1])


def forward(T, W):
    u = (ev(F, T)-11-ev(K, T)*W)/(60*ev(F, T))
    z = -(2-10*u)**2*(T-2)*ev(L, T)**2/(300*(T+2)*ev(K, T)**2)
    return u, z


def backward(u, z):
    d, e = 3*u*u+u+1-9*z, 6*u+1
    T = 2*(d*d-3*z*e*e)/(d*d+3*z*e*e)
    return T, (ev(F, T)-11-60*ev(F, T)*u)/ev(K, T)


def invpoly(h, u, z):
    up, zp = [u**i for i in range(12)], [z**j for j in range(6)]
    return sum((c*up[i]*zp[j] for (i, j), c in h.items()), u*0)


T, W = E(f, [0, 1]), E(f, 0, 1)
u, z = forward(T, W)
J = (T+2)*(T*T-1)
N, Nb = 11*J+W, 11*J-W
zero("F_plus_one_factor", ev(F, T)+1-ev(K, T)*J)
zero("z_removable_K_chart", z+N*N*(T-2)*ev(L, T)**2/(10800*(T+2)*ev(F, T)**2))
zero("conjugate_chart_product", N*Nb-396*(T+2)*ev(F, T))
zero("u_cancelled_F_chart", u-(E(f, 1)/5-33*ev(K, T)*(T+2)/(5*Nb)))
zero("z_cancelled_F_chart", z+363*(T*T-4)*ev(L, T)**2/(25*Nb*Nb))
print("Checking complete model-side relations and saved maps...", flush=True)
zero("H1_on_model", invpoly(H[1], u, z))
Tb, Wb = backward(u, z)
zero("T_model_composition", Tb-T)
zero("W_model_composition", Wb-W)
s = invpoly(H[0], u, z)


def decode_rat(item, D):
    a = list(map(Fraction, item["numerator"]))
    b = list(map(Fraction, item["denominator"]))
    den = lcm(*(v.denominator for v in a+b))
    return E(D, [int(v*den) for v in a], 0, [int(v*den) for v in b])


for name, val in (("u", u), ("z", z), ("s", s)):
    old = saved["model_maps"][name]
    decoded = decode_rat(old["constant"], f)+W*decode_rat(old["quadratic"], f)
    zero("saved_full_map_"+name, val-decoded)
check("u_nonconstant", bool(u.b))
check("z_nonzero", bool(z.a or z.b))
check("s_nonzero", bool(s.a or s.b))
check("s_minus_one_nonzero", bool((s-1).a or (s-1).b))

print("Checking ordered field, swap, scalar and reverse maps...", flush=True)
t, Y = E(P, [0, 1]), E(P, 0, 1)
x = (11*ev([1]*6, t)+(t-1)*Y)/(6*ev([1]*11, t))
y = t**5*x
a, b = (1-x)/5, (1-y)/5
qa, qb = 3*a*a+a+1, 3*b*b+b+1
zero("ordered_quadratic_equation", 3*ev([1]*11, t)*x*x-11*ev([1]*6, t)*x+33)
zero("ordered_q_ratio", qa-t*qb)
zero("ordered_phi_equality", ev(phi, a)-ev(phi, b))
TT, WW = t+1/t, Y*(t*t-1)/t**3
zero("reciprocal_R", ev(P, t)/t**4-ev(R, TT))
zero("ordered_model_relation", WW*WW-ev(f, TT))
swapped_x = (11*ev([1]*6, 1/t)+(1/t-1)*(-Y/t**4))/(6*ev([1]*11, 1/t))
zero("swap_x", swapped_x-y)
zero("swap_W", (-Y/t**4)*((1/t)**2-1)/(1/t)**3-WW)
uo, zo = (a+b)/2, -(a-b)**2/12
Tu, Wu = backward(uo, zo)
zero("T_pair_map", Tu-TT)
zero("W_pair_map", Wu-WW)
ur, zr = forward(Tu, Wu)
zero("u_pair_composition", ur-uo)
zero("z_pair_composition", zr-zo)
zero("s_ordered_transport", invpoly(H[0], uo, zo)-ev(phi, a))
zero("S11_identity", ev([1]*11, t)/t**5-ev(F, TT))
zero("S6_identity", (1+t**5)*ev([1]*6, t)/t**5-ev(F, TT)-1)
zero("K_identity", (1+t**5)/(t*t*(t+1))-ev(K, TT))
zero("L_identity", (t**5-1)**2/t**5-(TT-2)*ev(L, TT)**2)
zero("K_square_identity", (t**5+1)**2/t**5-(TT+2)*ev(K, TT)**2)

# Complete exceptional-locus polynomial tests. No point is deleted.
for name, p in (("F", F), ("K", K), ("L", L)):
    check(name+"_simple", pgcd(p, derivative(p)) == [1])
    check(name+"_disjoint_branch", pgcd(p, f) == [1])
check("F_K_disjoint", pgcd(F, K) == [1])
check("F_L_disjoint", pgcd(F, L) == [1])
check("K_L_disjoint", pgcd(K, L) == [1])
for name, p, n, expected in (
    ("F_minus_two", F, -2, -1), ("F_plus_two", F, 2, 11),
    ("K_minus_two", K, -2, 5), ("K_plus_two", K, 2, 1),
    ("L_minus_two", L, -2, 1), ("L_plus_two", L, 2, 5),
    ("R_minus_two", R, -2, -99), ("R_plus_two", R, 2, -9075)):
    check(name, sum(c*n**i for i, c in enumerate(p)) == expected)
check("normalized_minus_two_z", -Fraction(396*(-4), 10800) == Fraction(11, 75))
check("normalized_plus_two_z", -Fraction(1, 12*(-36300)) == Fraction(1, 660**2))
check("infinity_polynomial", f[::-1] == [-275, -704, 1034, 3388, 341, -2288, -308])

# Check the complete original residual records against recomputed identities.
for name, record in saved["exact_residuals"].items():
    if name == "sextic_squarefree":
        check("original_residual_"+name, record == ["1"] and checks[name])
    else:
        check("original_residual_"+name, name in checks and checks[name] and
              record == {"constant": {"numerator": [], "denominator": ["1"]},
                         "quadratic": {"numerator": [], "denominator": ["1"]}})
original_checks = {
    "phi_all_coefficients": checks["phi"],
    "ordered_discriminant_degree_eight": len(P)-1 == 8,
    "P8_reciprocal": checks["P_reciprocal"],
    "P8_squarefree": checks["ordered_squarefree"],
    "sextic_degree": checks["degree"],
    "F_at_minus_two": checks["F_minus_two"],
    "R4_at_minus_two": checks["R_minus_two"],
    "normalized_z_at_minus_two": checks["normalized_minus_two_z"],
    "u_at_minus_two": Fraction(-1-11, 60*(-1)) == Fraction(1, 5),
    "u_z_at_plus_two": checks["F_plus_two"] and checks["K_plus_two"],
    "H0_input_coefficients": checks["H0_complete"],
    "H1_input_coefficients": checks["H1_complete"],
}
for name in saved["checks"]:
    if name not in original_checks:
        original_checks[name] = checks[name]
check("all_original_checks", saved["checks"] == original_checks and all(original_checks.values()))
check("original_check_count", saved["check_count"] == len(original_checks) == 31)
check("original_failures", saved["failures"] == [])
failures = [name for name, ok in checks.items() if not ok]
report = {
    "original_sha256": sha256(raw).hexdigest(),
    "original_input_sha256": sha256(input_raw).hexdigest(),
    "coefficient_reconstruction": polys,
    "invariant_polynomials": {
        label: [{"exponents_u_z": list(m), "coefficient": c} for m, c in sorted(h.items())]
        for label, h in zip(("H0", "H1"), H)},
    "independent_maps": {name: val.data() for name, val in (("u", u), ("z", z), ("s", s))},
    "residuals": residuals, "checks": checks, "failures": failures,
    "original_checks": original_checks, "check_count": len(checks),
    "actual_degree": 6, "required_degree": [5, 6], "squarefree_gcd": pgcd(f, derivative(f)),
    "qualification": "Exact arithmetic audit; field generation and proper/local-ring arguments are in L110. No rational-point classification."
}
out = HERE/'model-audit-certificate.json'
out.write_text(json.dumps(report, indent=2)+'\n')
print(f"Checks: {len(checks)}; failures: {failures}; degree 6, required 5 or 6; gcd = {report['squarefree_gcd']}")
print(f"Full certificate: {out}")
assert not failures
