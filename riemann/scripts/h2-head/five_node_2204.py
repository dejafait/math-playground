"""One frozen rational-complex test. Run from the active notebook.

Assumes correct CPython integers and fractions.Fraction arithmetic.
No floating point enters a certificate assertion. See C919i for the
uniform-in-r argument; this finite program does not sample that claim.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import sys

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0]


def power(z, n):
    assert n >= 0
    out = F(1), F(0)
    while n:
        if n % 2:
            out = mul(out, z)
        z = mul(z, z)
        n //= 2
    return out


def inverse(z):
    den = z[0]**2 + z[1]**2
    assert den > 0
    return z[0]/den, -z[1]/den


def evaluate(coeffs, z):
    out = F(0), F(0)
    for a in reversed(coeffs):
        out = add(mul(out, z), (a, F(0)))
    return out


def encode(x):
    if isinstance(x, F):
        return {"numerator": str(x.numerator), "denominator": str(x.denominator)}
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


checks = {}


def check(name, truth):
    checks[name] = bool(truth)
    return checks[name]


alpha = [(F(57, 4), F(0)), (F(21), F(0)), (F(25), F(0)),
         (F(101), F(1, 4)), (F(101), F(-1, 4))]
beta = [power(inverse(a), 2) for a in alpha]
boxes = [(F(14), F(29, 2)), (F(41, 2), F(43, 2)), (F(49, 2), F(51, 2))]
for j, (lo, hi) in enumerate(boxes):
    check(f"real_box_{j+1}", lo <= alpha[j][0] <= hi and alpha[j][1] == 0)
check("five_distinct_nonzero_opposite_classes",
      all(a[0] > 0 for a in alpha) and len(set(alpha)) == 5)
check("conjugate_occurrences_retained", beta[3] == (beta[4][0], -beta[4][1]))
b = F(4, 2601)
for j in range(3):
    check(f"head_beta_{j+1}_at_least_b", beta[j][0] >= b and beta[j][1] == 0)
norm_squared = alpha[3][0]**2 + alpha[3][1]**2
check("exterior_modulus_at_least_101", norm_squared >= 101**2)
C = 1 + F(40000, 101**4) + F(1600000000, 101**8)
h4 = b**8 / 700000000
t4 = 2 * F(1, 101**20) * C
margin = h4 - t4
ratio = F(1, 101**4) / b**2
check("strict_onset_margin", h4 > t4 > 0)
check("uniform_extension_ratio", 0 < ratio < 1)
check("positive_denominators", all(q.denominator > 0 for q in (b, C, h4, t4, margin, ratio)))

# Build the prescribed monic cubic, in increasing degree order.
P = [F(1)]
for z in beta[:3]:
    assert z[1] == 0
    new = [F(0)] * (len(P) + 1)
    for i, a in enumerate(P):
        new[i] -= z[0] * a
        new[i+1] += a
    P = new
P_values = [evaluate(P, z) for z in beta]
for j in range(3):
    check(f"annihilator_zero_{j+1}", P_values[j] == (0, 0))
check("monic_cubic", len(P) == 4 and P[-1] == 1)
check("nonzero_exterior_P", P_values[3] != (0, 0))

search = []
selected = None
# Do not proceed past a failed head/error bound.
if all(checks.values()):
    for r in range(4, 1001):
        terms = [mul(power(z, 2*r+2), mul(p, p)) for z, p in zip(beta, P_values)]
        total = (F(0), F(0))
        for term in terms:
            total = add(total, term)
        check(f"Q_real_r_{r}", total[1] == 0)
        search.append({"r": r, "Q": total[0]})
        if total[1] != 0:
            break
        if total[0] < 0:
            # Check the full weighted-polynomial formula, not just cancellation.
            direct_terms = []
            for z, p in zip(beta, P_values):
                q = mul(power(z, r), p)
                direct_terms.append(mul(mul(z, z), mul(q, q)))
            check("full_Q_identity", direct_terms == terms)
            check("selected_range", 4 <= r <= 1000)
            check("selected_negative", total[0] < 0)
            normalized = total[0] / (norm_squared**(-2*r-2))
            check("compact_negative_upper_bound", normalized < -F(1, 10**30))
            selected = {"r": r, "q_degree": r+3, "P_values": P_values,
                        "five_terms": terms, "direct_five_terms": direct_terms,
                        "Q": total[0], "Q_imaginary": total[1],
                        "normalized_Q": normalized,
                        "normalizing_positive_factor": norm_squared**(-2*r-2),
                        "normalized_Q_strict_upper_bound": -F(1, 10**30)}
            break
check("witness_found_in_frozen_range", selected is not None)
failures = [name for name, passed in checks.items() if not passed]
certificate = {
    "step": "2204", "arithmetic_assumption": "Correct CPython integer and Fraction arithmetic",
    "normalization": "S_m=sum beta^m; Q(q)=sum beta^2*q(beta)^2; H_2r[i,j]=S_(2r+i+j+2); algebraic squares",
    "multiplicities": [1]*5, "alpha": alpha, "beta": beta, "boxes": boxes,
    "scaled_matrix_D": [1, 200, 40000],
    "head": {"input": "C919e", "b": b, "gram_margin": F(1,700000000), "h4": h4},
    "error": {"occurrence_count": 2, "alpha_modulus_squared": norm_squared, "C": C, "t4": t4},
    "comparison": {"h4_minus_t4": margin, "h4_over_t4": h4/t4,
                   "cross_product": str(h4.numerator*t4.denominator - t4.numerator*h4.denominator),
                   "extension_ratio": ratio, "required_ratio_upper_bound": 1,
                   "uniform_argument": "For k=r-4>=0: head>=h4*b^(2k) I; error norm<=t4*101^(-4k); difference>=b^(2k)*(h4-t4)>0."},
    "P_coefficients_increasing_degree": P,
    "search_range": [4, 1000], "evaluated_search": search, "selected": selected,
    "checks": checks, "failures": failures,
    "result": "PASS" if not failures else "STOP",
}
path = Path("scripts/h2-head/five_node_2204.json")
path.write_text(json.dumps(encode(certificate), indent=2) + "\n")
print(f"result={certificate['result']}; failures={failures}; certificate={path}")
print(f"head h4={h4}; error t4={t4}; required h4>t4; ratio h4/t4 approximately {float(h4/t4):.8g}")
print(f"extension ratio={ratio}; required <1; selected r={selected['r'] if selected else None}; Q sign={'negative' if selected else 'not certified'}")
sys.exit(bool(failures))
