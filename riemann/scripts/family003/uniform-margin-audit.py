"""Exact replay of the pinned balanced-endpoint identity; no numerical sampling."""
from fractions import Fraction as F
from pathlib import Path
import json


class P(dict):
    # Sparse polynomials in y, delta, with exact rational coefficients.
    @staticmethod
    def lift(value):
        return value if isinstance(value, P) else P({(0, 0): F(value)})

    def __add__(self, other):
        out = P(self)
        for key, value in P.lift(other).items():
            out[key] = out.get(key, F(0)) + value
        return P({key: value for key, value in out.items() if value})

    __radd__ = __add__

    def __neg__(self):
        return P({key: -value for key, value in self.items()})

    def __sub__(self, other):
        return self + -P.lift(other)

    def __rsub__(self, other):
        return P.lift(other) + -self

    def __mul__(self, other):
        out = P()
        for (a, b), c in self.items():
            for (d, e), f in P.lift(other).items():
                key = (a + d, b + e)
                out[key] = out.get(key, F(0)) + c * f
        return P({key: value for key, value in out.items() if value})

    __rmul__ = __mul__

    def __pow__(self, exponent):
        assert isinstance(exponent, int) and exponent >= 0
        result = P.lift(1)
        for _ in range(exponent):
            result = result * self
        return result


def terms(poly):
    return [{"y_degree": a, "delta_degree": b, "coefficient": str(c)}
            for (a, b), c in sorted(poly.items()) if c]


y, delta = P({(1, 0): F(1)}), P({(0, 1): F(1)})
h, alpha = F(13, 16), F(5, 6)
D = (37 + 34*y) * F(1, 18)
Q = (7 + 18*y + 8*y**2) * F(1, 9)
J = (alpha - delta)*D + delta*Q
R_times_J = (1-delta)*J + (alpha-delta)*delta*Q*F(1, 2)
E_times_J = (-F(1, 48) + F(2, 3)*delta
             + (F(1, 2)-y)*delta*F(1, 6))*J - h*(J-R_times_J)
v = 51 + 41*y
lhs = -10368*v*E_times_J
rhs = ((3+5*y)*((4*v*delta-79)**2+49)
       + 4*y*(4*v*delta*((1+3*y)*(15+32*y)*delta+9-13*y)+265+3485*y))
residual = lhs-rhs
values = {
    "endpoint_lower_bound": (F(49, 440640), F(1, 10000), ">"),
    "floor_exponent": (-F(1, 48)+F(3, 4)*F(1, 50), -F(7, 1200), "="),
    "intermediate_exponent": (-F(529, 2400)+F(25, 96)*alpha, -F(49, 14400), "="),
    "small_row_exponent": (h*(F(17, 50)-F(1, 6))-F(23, 96)+F(2, 100), -F(63, 800), "="),
    "delta_margin_coefficient": (1-h/4, F(51, 64), "="),
    "supply_excess_at_h": (F(1, 6)/h-F(7, 37), F(23, 1443), "="),
    "extension_supply_excess": (F(1, 5)-F(7, 37), F(2, 185), "="),
    "extension_slope_bound": (F(139, 96)+F(1, 2)-F(17, 50), F(2), "<"),
}
checks = {}
for name, (actual, required, relation) in values.items():
    passed = {"=": actual == required, ">": actual > required, "<": actual < required}[relation]
    checks[name] = {"actual": str(actual), "required": str(required),
                    "relation": relation, "passed": passed}
failures = ([] if not residual else ["endpoint_polynomial_identity"])
failures += [name for name, check in checks.items() if not check["passed"]]
certificate = {
    "source_commit": "1581d4cbdd69a0faf34b2089614fe2a814316a6a",
    "source_labels": ["lem:balanced-endpoint", "eq:balanced-endpoint-certificate", "prop:parameter-order"],
    "scope": "Exact polynomial identity and listed rational values only; positivity domains and quantifiers require the written proof.",
    "domain": {"y": "[0,1/2]", "delta": "[0,5/6]", "J_bounds": "[35/54,5/2]"},
    "identity": {"lhs": terms(lhs), "rhs": terms(rhs), "residual": terms(residual), "passed": not residual},
    "rational_checks": checks,
    "failures": failures,
    "passed": not failures,
}
path = Path(__file__).with_name("uniform-margin-certificate.json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print("Endpoint identity: " + ("PASS (all coefficients equal)" if not residual else "FAIL"))
for name, check in checks.items():
    print(f"{name}: actual={check['actual']}; required {check['relation']} {check['required']}; pass={check['passed']}")
print(f"Failures: {failures}; certificate: {path}")
raise SystemExit(bool(failures))
