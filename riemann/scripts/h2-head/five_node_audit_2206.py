"""Independent replay of C919i's frozen r=158 witness; no search.

Run from riemann. Correct CPython integer/Fraction execution is assumed.
The original generator/certificate is read-only. Binomial integer powers
and factored P evaluation replace its repeated squaring and Horner rule.
The all-shift conclusion is the written inequality, not a numerical test.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, gcd, lcm
from pathlib import Path
import json
import sys

sys.set_int_max_str_digits(0)
source = Path("scripts/h2-head/five_node_2204.json")
source_bytes = source.read_bytes()
raw = json.loads(source_bytes)
checks = {}
comparisons = {}
bad_rationals = []
rational_count = 0


def check(name, condition):
    checks[name] = bool(condition)


def decode(x, pointer=""):
    global rational_count
    if isinstance(x, dict) and set(x) == {"numerator", "denominator"}:
        n, d = int(x["numerator"]), int(x["denominator"])
        rational_count += 1
        if d <= 0 or gcd(n, d) != 1:
            bad_rationals.append(pointer)
        return F(n, d)
    if isinstance(x, dict):
        return {k: decode(v, pointer + "/" + k) for k, v in x.items()}
    if isinstance(x, list):
        return [decode(v, pointer + "/" + str(j)) for j, v in enumerate(x)]
    return x


saved = decode(raw)


def match(pointer, expected):
    actual = saved
    for key in pointer.strip("/").split("/"):
        actual = actual[int(key)] if isinstance(actual, list) else actual[key]
    comparisons[pointer] = {"expected": expected, "saved": actual,
                            "equal": actual == expected}
    check("match" + pointer, actual == expected)


def product(z, w):
    return [z[0]*w[0] - z[1]*w[1], z[0]*w[1] + z[1]*w[0]]


def binomial_power(z, n):
    """Expand (A+iB)^n/D^n using integer binomial sums."""
    d = lcm(z[0].denominator, z[1].denominator)
    a, b = int(z[0]*d), int(z[1]*d)
    re = sum((-1)**(j//2)*comb(n, j)*a**(n-j)*b**j
             for j in range(0, n+1, 2))
    im = sum((-1)**((j-1)//2)*comb(n, j)*a**(n-j)*b**j
             for j in range(1, n+1, 2))
    return [F(re, d**n), F(im, d**n)]


def linear_power(z, n):
    """Separate finite product for the direct weighted-polynomial formula."""
    ans = [F(1), F(0)]
    for _ in range(n):
        ans = product(ans, z)
    return ans


alpha = [[F(57, 4), F(0)], [F(21), F(0)], [F(25), F(0)],
         [F(101), F(1, 4)], [F(101), F(-1, 4)]]
beta = [[(x*x-y*y)/(x*x+y*y)**2, -2*x*y/(x*x+y*y)**2]
        for x, y in alpha]
boxes = [[F(14), F(29, 2)], [F(41, 2), F(43, 2)], [F(49, 2), F(51, 2)]]
match("/alpha", alpha)
match("/beta", beta)
match("/multiplicities", [1]*5)
match("/boxes", boxes)
match("/scaled_matrix_D", [1, 200, 40000])
check("five_nonzero_distinct_opposite_classes",
      all(x > 0 for x, y in alpha) and len(set(map(tuple, alpha))) == 5)
check("both_conjugates", beta[3] == [beta[4][0], -beta[4][1]])
check("box_hypotheses", all(lo <= x <= hi and y == 0
                           for (x, y), (lo, hi) in zip(alpha, boxes)))

b, gram = F(4, 2601), F(1, 700000000)
norm2 = alpha[3][0]**2 + alpha[3][1]**2
# Onset exponents come directly from beta^(2r)*w*w^T at r=4.
error_terms = [2*F(1, 101**20), 2*F(40000, 101**24),
               2*F(1600000000, 101**28)]
C = 1 + F(40000, 101**4) + F(1600000000, 101**8)
h4, t4 = gram*b**8, sum(error_terms)
ratio = F(1, 101**4)/b**2
cross = h4.numerator*t4.denominator-t4.numerator*h4.denominator
for key, value in {"b": b, "gram_margin": gram, "h4": h4}.items():
    match("/head/" + key, value)
match("/head/input", "C919e")
for key, value in {"occurrence_count": 2, "alpha_modulus_squared": norm2,
                   "C": C, "t4": t4}.items():
    match("/error/" + key, value)
for key, value in {"h4_minus_t4": h4-t4, "h4_over_t4": h4/t4,
                   "cross_product": str(cross), "extension_ratio": ratio,
                   "required_ratio_upper_bound": 1}.items():
    match("/comparison/" + key, value)
check("head_nodes_at_least_b", all(z[1] == 0 and z[0] >= b for z in beta[:3]))
check("both_exterior_moduli", all(x*x+y*y == norm2 > 101**2 for x, y in alpha[3:]))
check("onset_margin", h4 > t4 > 0 and cross > 0)
check("uniform_geometric_ratio", 0 < ratio < 1)

u, v, w = [z[0] for z in beta[:3]]
coefficients = [-u*v*w, u*v+u*w+v*w, -(u+v+w), F(1)]
values = []
for z in beta:
    value = [F(1), F(0)]
    for node in (u, v, w):
        value = product(value, [z[0]-node, z[1]])
    values.append(value)
match("/P_coefficients_increasing_degree", coefficients)
match("/selected/P_values", values)
check("real_head_annihilated", values[:3] == [[0, 0]]*3)
check("exterior_P_nonzero", values[3] != [0, 0])
check("P_conjugates", values[3] == [values[4][0], -values[4][1]])

r = 158
terms, direct_terms, powers = [], [], []
for z, value in zip(beta, values):
    zn = binomial_power(z, 2*r+2)
    powers.append(zn)
    terms.append(product(zn, product(value, value)))
    q = product(linear_power(z, r), value)
    direct_terms.append(product(product(z, z), product(q, q)))
total = [sum(t[j] for t in terms) for j in range(2)]
normalizing_divisor = norm2**(-2*r-2)
normalized = total[0]/normalizing_divisor
upper = -F(1, 10**30)
for key, value in {"r": r, "q_degree": r+3, "five_terms": terms,
                   "direct_five_terms": direct_terms, "Q": total[0],
                   "Q_imaginary": total[1], "normalized_Q": normalized,
                   "normalizing_positive_factor": normalizing_divisor,
                   "normalized_Q_strict_upper_bound": upper}.items():
    match("/selected/" + key, value)
check("two_independent_power_methods", terms == direct_terms)
check("three_zero_terms", terms[:3] == [[0, 0]]*3)
check("conjugate_terms", terms[3] == [terms[4][0], -terms[4][1]])
check("real_total_and_two_occurrence_formula", total == [2*terms[3][0], 0])
check("strict_negative_Q", total[0] < 0)
check("positive_normalizing_divisor", normalizing_divisor > 0)
check("proof_multiplier_matches_divisor_reciprocal",
      normalized == norm2**318*total[0])
check("strict_normalized_threshold", normalized < upper)
negative_cross = -10**30*normalized.numerator-normalized.denominator
check("strict_normalized_integer_cross_product", negative_cross > 0)
match("/search_range", [4, 1000])
check("selected_in_frozen_range", 4 <= r <= 1000)
# Only the selected search entry is load-bearing. No earlier sign/minimality claim.
selected_entries = [e for e in saved["evaluated_search"] if e["r"] == r]
check("saved_selected_search_entry", selected_entries == [{"r": r, "Q": total[0]}])
check("original_flags_true", all(v is True for v in saved["checks"].values()))
match("/failures", [])
match("/result", "PASS")
check("all_saved_rationals_reduced_positive_denominator", not bad_rationals)

# Independently transcribed displayed scalars: check proof as well as JSON.
displayed = {
    "C": (C, F(10832731072320801, 10828567056280801)),
    "h4": (h4, F(256, 5727708301326206498092619377734375)),
    "t4": (t4, F(21665462144641602,
                 132129096689825080931822600853816049099831724850779782801)),
    "cross_product": (cross, 33825048628501773340614204837476958493862762733806493928306),
    "ratio": (ratio, F(6765201, 1664966416)),
    "norm2": (norm2, F(163217, 16)),
    "z": (beta[3], [F(2611440, 26639789089), -F(12928, 26639789089)]),
    "P": (coefficients, [-F(16, 895505625), F(4061, 179101125),
                         -F(874826, 99500625), F(1)]),
    "Pz": (values[3], [-F(53254884017141348482037596182944,
                          3386028897813546182502688387904073865125),
                       -F(34473439179388475382824589440,
                          3386028897813546182502688387904073865125)]),
}
for name, (actual, expected) in displayed.items():
    check("displayed_" + name, actual == expected)
check("source_unchanged", source.read_bytes() == source_bytes)


def encode(x):
    if isinstance(x, F):
        return {"numerator": str(x.numerator), "denominator": str(x.denominator)}
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [encode(v) for v in x]
    return x


failures = [name for name, ok in checks.items() if not ok]
result = {
    "step": "2206", "result": "PASS" if not failures else "FAIL",
    "source": str(source), "source_sha256": sha256(source_bytes).hexdigest(),
    "assumption": "Correct CPython integer and Fraction execution; C919e as audited",
    "scope": "Frozen r=158 only; uniform proof reviewed separately; no search replay",
    "method": "Integer binomial powers + factored P; separate 158-fold products",
    "rational_records_validated": rational_count, "bad_rational_paths": bad_rationals,
    "full_comparisons": comparisons, "displayed_operands": displayed,
    "reconstructed_powers": powers, "error_terms": error_terms,
    "thresholds": {"head_over_error": h4/t4, "required_head_over_error": 1,
                   "extension_ratio": ratio, "required_extension_upper_bound": 1,
                   "Q": total[0], "required_Q_upper_bound": 0,
                   "normalized_Q": normalized, "normalized_upper_bound": upper,
                   "strict_normalized_cross_product": str(negative_cross)},
    "checks": checks, "failures": failures,
}
path = Path("scripts/h2-head/five_node_audit_2206.json")
path.write_text(json.dumps(encode(result), indent=2) + "\n")
print(f"result={result['result']}; checks={len(checks)}; failures={failures}; certificate={path}")
print(f"head/error={h4/t4}; required >1; extension ratio={ratio}; required <1")
print(f"r={r}; Q<0={total[0]<0}; normalized Q<-1/10^30={normalized<upper}; "
      f"complete field comparisons={len(comparisons)}; rational records={rational_count}")
sys.exit(bool(failures))
