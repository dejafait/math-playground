"""Exact integer-polynomial checks for L370; uses only the standard library."""
import json
from pathlib import Path


class Poly:
    n = 8

    def __init__(self, terms):
        self.terms = {m: c for m, c in terms.items() if c}

    @classmethod
    def constant(cls, c):
        return cls({(0,) * cls.n: c})

    @classmethod
    def variable(cls, i):
        m = [0] * cls.n
        m[i] = 1
        return cls({tuple(m): 1})

    def __add__(self, other):
        other = other if isinstance(other, Poly) else self.constant(other)
        terms = dict(self.terms)
        for m, c in other.terms.items():
            terms[m] = terms.get(m, 0) + c
        return Poly(terms)

    __radd__ = __add__

    def __neg__(self):
        return Poly({m: -c for m, c in self.terms.items()})

    def __sub__(self, other):
        other = other if isinstance(other, Poly) else self.constant(other)
        return self + (-other)

    def __mul__(self, other):
        other = other if isinstance(other, Poly) else self.constant(other)
        terms = {}
        for m, c in self.terms.items():
            for v, d in other.terms.items():
                key = tuple(x + y for x, y in zip(m, v))
                terms[key] = terms.get(key, 0) + c * d
        return Poly(terms)

    __rmul__ = __mul__

    def records(self):
        return [{"powers": list(m), "coefficient": c}
                for m, c in sorted(self.terms.items())]


def discriminant(a, b, c, d, e, h):
    cross = 2*b*e-a*h-c*d
    return cross*cross-4*(b*b-a*c)*(e*e-d*h)


f, u, v, g, x, y, a, q = [Poly.variable(i) for i in range(8)]
w, wp, k = f*x-u*g, f*y-v*g, u*y-v*x
base = wp*wp-4*w*k
checks = {
    "six_jet_identity": discriminant(f, u, v, g, x, y)-base,
    "envelope_identity": discriminant(
        f, u+a*f, v+2*a*u+(q+a*a)*f,
        g, x+a*g, y+2*a*x+(q+a*a)*g)-base-4*q*w*w,
    "transformed_third_minor": (
        (u+a*f)*(y+2*a*x+(q+a*a)*g)
        -(v+2*a*u+(q+a*a)*f)*(x+a*g)
        -k-a*wp-(a*a-q)*w),
}
result = {
    "arithmetic": "exact integer sparse polynomial expansion",
    "variables": ["f", "f_prime", "f_second", "g", "g_prime", "g_second", "A_prime_over_A", "q"],
    "domain": "all real jets, including zeros; envelope division requires A>0",
    "checks": {name: {"residual_coefficients": p.records(), "required": [],
                      "passed": not p.terms} for name, p in checks.items()},
    "curvature_polynomial": (4*q*w*w).records(),
    "discriminant_polynomial": base.records(),
    "normalization": "Divide physical identity by A^4 T^4 L^4; T,L>0",
    "retained_bound": "4 K_q (P_0 V_1-P_1 V_0)^2/(T^2 L^2)",
    "coarse_bound": "4 K_q (E_0 D_1+E_1 D_0)^2/(T L^2)",
    "limitations": "Bounds are proved in L370, not checked numerically here; no actual-theta residual sign or relative margin is certified.",
    "failures": [name for name, p in checks.items() if p.terms],
}
path = Path(__file__).with_name("pointwise-identity-certificate.json")
path.write_text(json.dumps(result, indent=2) + "\n")
for name, check in result["checks"].items():
    print(f'{name}: {"PASS" if check["passed"] else "FAIL"}; actual nonzero residual coefficients={len(check["residual_coefficients"])}, required=0')
print("Curvature bound: " + result["coarse_bound"] + "; constants unevaluated")
print("Failures: " + str(result["failures"]))
print("Certificate: scripts/discriminant/pointwise-identity-certificate.json")
raise SystemExit(bool(result["failures"]))
