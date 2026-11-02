"""Exact finite normalization checks for C645y; no numerical quadrature.

The uniform proof is in the lemma. These small rational cases check the
retained residues, polynomial identity, inverse Gram norm, and every prefix.
"""
from dataclasses import dataclass
from fractions import Fraction as F
import json
from pathlib import Path


@dataclass(frozen=True)
class G:
    """Gaussian rationals, following the existing C645o certificate convention."""
    re: F
    im: F = F(0)

    @staticmethod
    def cast(v):
        return v if isinstance(v, G) else G(F(v))

    def __add__(self, v):
        v = G.cast(v)
        return G(self.re + v.re, self.im + v.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, v):
        return self + (-G.cast(v))

    def __rsub__(self, v):
        return G.cast(v) - self

    def __mul__(self, v):
        v = G.cast(v)
        return G(self.re*v.re-self.im*v.im, self.re*v.im+self.im*v.re)

    __rmul__ = __mul__

    def conjugate(self):
        return G(self.re, -self.im)

    def abs_squared(self):
        return self.re*self.re + self.im*self.im

    def __truediv__(self, v):
        v = G.cast(v)
        den = v.abs_squared()
        if not den:
            raise ZeroDivisionError("zero Gaussian-rational divisor")
        num = self*v.conjugate()
        return G(num.re/den, num.im/den)

    def __rtruediv__(self, v):
        return G.cast(v)/self


ZERO, ONE = G(F(0)), G(F(1))
R, U, x = F(11, 8), F(121, 64), G(F(-5, 4))


def product(xs):
    out = ONE
    for v in xs:
        out *= v
    return out


def add(p, q):
    return [(p[k] if k < len(p) else ZERO) +
            (q[k] if k < len(q) else ZERO)
            for k in range(max(len(p), len(q)))]


def scale(p, c):
    return [c*v for v in p]


def mul(p, q):
    out = [ZERO]*(len(p)+len(q)-1)
    for j, a in enumerate(p):
        for k, b in enumerate(q):
            out[j+k] += a*b
    return out


def root_poly(roots):
    out = [ONE]
    for a in roots:
        out = mul(out, [-a, ONE])
    return out


def kernel_norm(poles, residues):
    return sum((ca*cb.conjugate()/(U-a*b.conjugate())
                for a, ca in zip(poles, residues)
                for b, cb in zip(poles, residues)), ZERO)


def solve(matrix, rhs):
    rows = [[G.cast(v) for v in row]+[rhs[j]]
            for j, row in enumerate(matrix)]
    n = len(rows)
    for k in range(n):
        pivot = next(j for j in range(k, n) if rows[j][k] != ZERO)
        rows[k], rows[pivot] = rows[pivot], rows[k]
        div = rows[k][k]
        rows[k] = [v/div for v in rows[k]]
        for j in range(n):
            if j != k:
                c = rows[j][k]
                rows[j] = [a-c*b for a, b in zip(rows[j], rows[k])]
    return [row[-1] for row in rows]


def case(n, u, poles, rs):
    ts = [F(j, n) for j in range(n)]
    bs = [t*u for t in ts]
    B = lambda z, K=n: product(R*(z-bs[j])/(U-bs[j].conjugate()*z)
                              for j in range(K))
    L = lambda z: sum((r/(z-a) for a, r in zip(poles, rs)), ZERO)
    bx = B(x)
    qres = [r*bx/B(a) for a, r in zip(poles, rs)]
    gres = []
    for j, b in enumerate(bs):
        derivative = R/(U-b.abs_squared())*product(
            R*(b-bs[k])/(U-bs[k].conjugate()*b)
            for k in range(n) if k != j)
        gres.append(bx*L(b)/derivative)
    qnorm = kernel_norm(poles, qres)
    gnorm = kernel_norm(bs, gres)
    lnorm = kernel_norm(poles, [G.cast(r) for r in rs])
    coeff_sq = [bx.abs_squared()*(1-ts[j]*ts[j]/U)*
                sum((r/(B(a, j)*(a-bs[j])) for a, r in zip(poles, rs)),
                    ZERO).abs_squared() for j in range(n)]
    ell = [L(b) for b in bs]
    matrix = [[1/(1-ti*tj/U) for tj in ts] for ti in ts]
    sol = solve(matrix, ell)
    gram_norm = bx.abs_squared()*sum(
        (v.conjugate()*w for v, w in zip(ell, sol)), ZERO)

    repeated = [a for a, r in zip(poles, rs) for _ in range(r)]
    P = root_poly(repeated)
    A = root_poly(bs)
    D = [ONE]
    for b in bs:
        D = mul(D, [G(U), -b.conjugate()])
    V = [ZERO]
    for a, residue in zip(poles, qres):
        rest = list(repeated)
        rest.remove(a)
        V = add(V, scale(root_poly(rest), residue))
    h = [ZERO]
    for j, residue in enumerate(gres):
        h = add(h, scale(root_poly(bs[:j]+bs[j+1:]), residue))
    dp = [k*P[k] for k in range(1, len(P))]
    bezout_difference = add(add(mul(A, V), mul(P, h)),
                            scale(mul(D, dp), -bx/(R**n)))
    prefix_checks = []
    for K in range(n+1):
        response = kernel_norm(poles, [r*bx/B(a, K)
                                      for a, r in zip(poles, rs)])
        rhs = bx.abs_squared()*lnorm + sum(coeff_sq[:K], F(0))
        prefix_checks.append({"K": K, "actual_minus_required": response-rhs,
                              "response_norm_squared": response,
                              "pass": response == rhs})
    checks = {
        "admissible": (u.abs_squared() == 1 and x in poles and
                       sum(rs) <= F(n, 3) and all(r > 0 for r in rs) and
                       all(a.re == x.re and a.abs_squared() <= F(273, 200)**2
                           for a in poles)),
        "energy_split": qnorm == bx.abs_squared()*lnorm + gnorm,
        "all_grid_residues_match_orthogonal_energy": gnorm == G(sum(coeff_sq)),
        "inverse_gram_energy": gnorm == gram_norm,
        "polynomial_identity_every_coefficient": all(v == ZERO for v in bezout_difference),
        "proper_rational_sum": sum(qres+gres, ZERO) == ZERO,
        "all_prefixes": all(v["pass"] for v in prefix_checks),
    }
    return {"n": n, "u": u, "poles": poles, "residues": rs,
            "P_coefficients_ascending": P, "A_coefficients_ascending": A,
            "D_coefficients_ascending": D, "V_coefficients_ascending": V,
            "h_coefficients_ascending": h, "grid_residues": gres,
            "log_derivative_samples": ell, "gram_solution": sol,
            "q_norm_squared": qnorm, "grid_norm_squared": gnorm,
            "old_response_norm_squared": bx.abs_squared()*lnorm,
            "orthogonal_coefficient_squares": coeff_sq,
            "polynomial_identity_difference": bezout_difference,
            "prefix_checks": prefix_checks, "checks": checks}


def encode(v):
    if isinstance(v, F):
        return {"numerator": str(v.numerator), "denominator": str(v.denominator)}
    if isinstance(v, G):
        return {"real": encode(v.re), "imaginary": encode(v.im)}
    if isinstance(v, dict):
        return {k: encode(x) for k, x in v.items()}
    if isinstance(v, list):
        return [encode(x) for x in v]
    return v


cases = [case(6, u, [x, x+G(F(0), F(1, 4))], [1, 1])
         for u in [ONE, G(F(0), F(1)), G(F(3, 5), F(4, 5))]]
cases += [case(9, G(F(3, 5), F(-4, 5)),
               [x, x+G(F(0), F(-1, 3))], [2, 1]),
          case(9, G(F(-1)), [x], [3])]
failures = [{"case": i, "check": key}
            for i, c in enumerate(cases) for key, ok in c["checks"].items() if not ok]
summary = {"case_count": len(cases), "aggregate_checks": sum(len(c["checks"]) for c in cases),
           "prefix_equalities": sum(len(c["prefix_checks"]) for c in cases),
           "actual_max_absolute_identity_error": "0" if not failures else "FAILED",
           "required_max_absolute_identity_error": "0", "failures": failures,
           "scope": "exact small-case algebra checks; not a uniform angular lower bound"}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(encode({"summary": summary, "cases": cases}), indent=2)+'\n')
print(json.dumps({**summary, "certificate": str(output)}, sort_keys=True))
if failures:
    raise SystemExit(1)
