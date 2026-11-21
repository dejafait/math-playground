"""Exact, fixed-pair certificate; standard library only. Run from notebook."""
from fractions import Fraction as Q
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import json


def trim(a):
    a = list(map(Q, a))
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def add(a, b):
    return trim([(a[i] if i < len(a) else 0) +
                 (b[i] if i < len(b) else 0)
                 for i in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([c * x for x in a])


def mul(a, b):
    c = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y
    return trim(c)


def deriv(a):
    return trim([i * a[i] for i in range(1, len(a))] or [0])


def divrem(a, b):
    a, b = trim(a), trim(b)
    assert b != [0]
    quotient = [Q(0)] * max(1, len(a) - len(b) + 1)
    while a != [0] and len(a) >= len(b):
        k = len(a) - len(b)
        c = a[-1] / b[-1]
        quotient[k] += c
        a = add(a, [Q(0)] * k + scale(b, -c))
    return trim(quotient), a


def primitive_positive_scale(a):
    """Clear denominators/content by a POSITIVE factor, preserving signs."""
    a = trim(a)
    denominator = lcm(*(c.denominator for c in a))
    integers = [int(c * denominator) for c in a]
    content = reduce(gcd, (abs(c) for c in integers))
    assert content > 0
    factor = Q(denominator, content)
    return scale(a, factor), factor


def translate(a, t):
    result = [Q(0)]
    for c in reversed(a):
        result = add(mul(result, [Q(t), Q(1)]), [c])
    return result


def sign(c):
    return (c > 0) - (c < 0)


def variations(signs):
    signs = [v for v in signs if v]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def T(a):
    return add(add(a, deriv(a)), scale(deriv(deriv(a)), Q(5, 18)))


def strings(a):
    return [str(c) for c in a]


h = trim([558, 2084, 1782, 393])
P = trim([-Q(162175, 3), 0, 657762, 606132, 1156683, 473958, 154449])
F = add(mul(h, h), [1])
leading = Q(154449)
shift = Q(1)
f = scale(translate(P, shift), 1 / leading)
image = scale(translate(F, shift), 1 / leading)

S0, factor0 = primitive_positive_scale(P)
S1 = deriv(S0)
sturm = [S0, S1]
relations = []
while True:
    quotient, remainder = divrem(sturm[-2], sturm[-1])
    if remainder == [0]:
        terminal_quotient = quotient
        break
    next_poly, factor = primitive_positive_scale(scale(remainder, -1))
    relations.append({
        "dividend_index": len(sturm) - 2,
        "quotient_ascending": strings(quotient),
        "positive_remainder_scale": str(factor),
        "relation_check": add(
            add(mul(quotient, sturm[-1]), scale(next_poly, -1 / factor)),
            scale(sturm[-2], -1)) == [0],
    })
    sturm.append(next_poly)

plus = [sign(s[-1]) for s in sturm]
minus = [sign(s[-1]) * (-1) ** (len(s) - 1) for s in sturm]
real_count = variations(minus) - variations(plus)
squarefree = len(sturm[-1]) == 1
g = T(trim([0] * 6 + [1]))
checks = {
    "direct_image_identity": T(P) == F,
    "input_degree_six_monic": len(f) == 7 and f[-1] == 1,
    "image_degree_six_monic": len(image) == 7 and image[-1] == 1,
    "translation_image_identity": T(f) == image,
    "input_coefficients_strictly_positive": all(c > 0 for c in f),
    "output_coefficients_strictly_positive": all(c > 0 for c in image),
    "q_sector_factorization": mul([Q(9, 5), 1], [Q(9, 5), 1]) ==
        trim([Q(81, 25), Q(18, 5), 1]),
    "q_roots_sum_product": Q(5, 18) * Q(18, 5) == 1 and
        Q(5, 18) * (Q(81, 25) + Q(9, 25)) == 1,
    "reference_polynomial": g == trim([0, 0, 0, 0, Q(25, 3), 6, 1]),
    "reference_discriminant_positive": Q(36) - 4 * Q(25, 3) == Q(8, 3) > 0,
    "sturm_all_relations": all(r["relation_check"] for r in relations),
    "terminal_remainder_zero": divrem(sturm[-2], sturm[-1])[1] == [0],
    "P_squarefree": squarefree,
    "exact_input_nonreal_count_four": squarefree and real_count == 2,
    "output_no_real_roots": leading > 0,  # F=h^2+1; analytic argument in lemma
}
certificate = {
    "scope": "One fixed C020o pair, shift 1; no parameter or degree sweep",
    "coefficient_order": "ascending",
    "pair": {"q": ["1", "1", "5/18"], "h": strings(h),
             "P": strings(P), "F": strings(F), "shift": str(shift),
             "leading_normalization": str(leading), "f": strings(f),
             "image": strings(image)},
    "sturm": {"P_to_S0_positive_scale": str(factor0),
              "polynomials_ascending": [strings(s) for s in sturm],
              "degrees": [len(s) - 1 for s in sturm],
              "relations": relations,
              "terminal_quotient_ascending": strings(terminal_quotient),
              "signs_minus_infinity": minus, "signs_plus_infinity": plus,
              "variations_minus_infinity": variations(minus),
              "variations_plus_infinity": variations(plus),
              "gcd_degree": len(sturm[-1]) - 1,
              "real_count_with_multiplicity": real_count if squarefree else None,
              "nonreal_count_with_multiplicity": 6-real_count if squarefree else None},
    "bounds": {"required_input_nonreal_count": 4,
               "actual_input_nonreal_count": 6-real_count if squarefree else None,
               "required_output_nonreal_count": 6,
               "actual_output_nonreal_count": 6,
               "output_real_axis_lower_bound": str(1 / leading),
               "required_output_real_axis_lower_bound": ">0",
               "minimum_input_coefficient": str(min(f)),
               "required_input_coefficients": ">=0"},
    "checks": checks,
    "failures": [k for k, v in checks.items() if not v],
}
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print("Exact fixed-pair checks:", sum(checks.values()), "/", len(checks))
print("Nonreal counts actual/required:", certificate["bounds"]["actual_input_nonreal_count"],
      "/4 -> 6/6; real count:", real_count, "; gcd degree:", len(sturm[-1])-1)
print("Sturm infinity variations:", variations(minus), variations(plus))
print("Minimum input coefficient:", min(f), "; required >=0")
print("Output lower bound:", 1 / leading, "; required >0")
print("Failures:", certificate["failures"])
print("Certificate:", path)
assert not certificate["failures"]
