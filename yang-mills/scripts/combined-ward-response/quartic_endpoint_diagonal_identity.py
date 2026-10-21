"""Exact noncommutative word check for C212i(3)--(4), not an asymptotic test."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def add(*terms):
    result = {}
    for term in terms:
        for word, value in term.items():
            result[word] = result.get(word, F(0)) + value
    return {word: value for word, value in result.items() if value}


def scale(poly, value):
    return {word: value * coefficient for word, coefficient in poly.items()}


def mul(left, right):
    result = {}
    for x, a in left.items():
        for y, b in right.items():
            result[x + y] = result.get(x + y, F(0)) + a * b
    return result


def bracket(left, right):
    return add(mul(left, right), scale(mul(right, left), -1))


def nested(x, y, z):
    return bracket(x, bracket(y, z))


z, v, w = ({(name,): F(1)} for name in ("z", "v", "w"))
p, q = scale(v, -1), w
u0, j0 = add(v, scale(w, -1)), scale(w, -1)
u, j = add(z, u0), add(z, j0)


def full_endpoint(u_arg, j_arg):
    return add(scale(nested(p, p, u_arg), F(1, 12)),
               scale(nested(u_arg, u_arg, p), F(1, 12)),
               scale(nested(q, p, u_arg), F(-1, 4)),
               scale(nested(j_arg, j_arg, q), F(1, 12)),
               scale(nested(q, q, j_arg), F(1, 12)))


full = full_endpoint(u, j)
pure = full_endpoint(u0, j0)
h, d = scale(add(v, w), F(1, 2)), add(w, scale(v, -1))
pure_formula = scale(nested(h, h, d), F(-1, 3))
remainder = add(
    scale(nested(p, p, z), F(1, 12)),
    scale(add(nested(z, u0, p), nested(u0, z, p), nested(z, z, p)), F(1, 12)),
    scale(nested(q, p, z), F(-1, 4)),
    scale(add(nested(z, j0, q), nested(j0, z, q), nested(z, z, q)), F(1, 12)),
    scale(nested(q, q, z), F(1, 12)))
words = list(product(("z", "v", "w"), repeat=3))
rows = [{"word": "".join(word),
         "full": str(full.get(word, F(0))),
         "pure": str(pure.get(word, F(0))),
         "pure_formula": str(pure_formula.get(word, F(0))),
         "remainder": str(remainder.get(word, F(0)))} for word in words]
checks = {
    "pure_prefix_identity": not add(pure, scale(pure_formula, -1)),
    "complete_remainder_identity": not add(full, scale(add(pure_formula, remainder), -1)),
    "every_remainder_word_contains_direct_z": all("z" in word for word in remainder),
    "all_27_words_recorded": len(rows) == 27,
}
certificate = {"scope": "Exact free associative cubic words only; no response bound or limit verified.",
               "checks": checks, "failures": [key for key, ok in checks.items() if not ok],
               "rows": rows}
destination = Path(__file__).with_name("quartic-endpoint-diagonal-identity-certificate.json")
destination.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"Exact endpoint algebra: {sum(checks.values())}/{len(checks)} checks; 27/27 words.")
print(f"Failures: {certificate['failures']}; certificate: {destination}")
if not all(checks.values()):
    raise SystemExit(1)
