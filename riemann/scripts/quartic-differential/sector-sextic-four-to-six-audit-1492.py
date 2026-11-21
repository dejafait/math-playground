"""Independent coefficient-identity audit of the fixed C020x witness.

Uses sparse polynomials and binomial translation, not the producer's
division, Horner translation or primitive-normalization implementation.
All signed-remainder identities are checked from the supplied quotients.
The imported Walsh/Sturm hypotheses are audited in the canonical proof.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile


BASE = Path(__file__).resolve().parent
SOURCE = BASE / "sector-sextic-four-to-six-1490.py"
ORIGINAL = SOURCE.with_suffix(".json")
OUTPUT = BASE / "sector-sextic-four-to-six-audit-1492.json"
REPLAY = BASE / "sector-sextic-four-to-six-replay-1492.json"


def poly(values):
    return {i: Q(c) for i, c in enumerate(values) if Q(c)}


def combine(*terms):
    result = {}
    for scalar, p in terms:
        for i, c in p.items():
            result[i] = result.get(i, Q(0)) + scalar * c
    return {i: c for i, c in result.items() if c}


def product(a, b):
    result = {}
    for i, a_i in a.items():
        for j, b_j in b.items():
            result[i+j] = result.get(i+j, Q(0)) + a_i*b_j
    return {i: c for i, c in result.items() if c}


def derivative(p, k=1):
    return {i-k: c*Q(factorial(i), factorial(i-k))
            for i, c in p.items() if i >= k}


def shift_one(p):
    return {j: sum((c*comb(i, j) for i, c in p.items() if i >= j), Q(0))
            for j in range(max(p)+1)}


def operator(p):
    return combine((1, p), (1, derivative(p)), (Q(5, 18), derivative(p, 2)))


def vector(p):
    return [str(p.get(i, Q(0))) for i in range(max(p, default=0)+1)]


def variation(signs):
    return sum(signs[i] != signs[i+1] for i in range(len(signs)-1))


def sgn(c):
    return 1 if c > 0 else -1 if c < 0 else 0


saved = json.loads(ORIGINAL.read_text())
checks = {}
identities = {}


def check(name, condition):
    checks[name] = bool(condition)


def identity(name, lhs, rhs):
    residual = combine((1, lhs), (-1, rhs))
    identities[name] = {"lhs": vector(lhs), "rhs": vector(rhs),
                        "residual": vector(residual)}
    check(name, not residual)


# Explicit coefficients transcribed from the canonical statement and proof.
A = Q(154449)
q = poly([1, 1, Q(5, 18)])
h = poly([558, 2084, 1782, 393])
P = poly([-Q(162175, 3), 0, 657762, 606132, 1156683, 473958, 154449])
F = poly([311365, 2325744, 6331768, 7865964, 4813548, 1400652, 154449])
f = poly([Q(8984777, 463347), Q(3685712, 51483), Q(5490857, 51483),
          Q(4353808, 51483), Q(1947736, 51483), Q(1188, 131), 1])
image = poly([Q(23203490, 154449), Q(65771318, 154449),
              Q(75134203, 154449), Q(14738552, 51483),
              Q(4711181, 51483), Q(1974, 131), 1])
for name, p in {"q": q, "h": h, "P": P, "F": F, "f": f,
                "image": image}.items():
    identity("saved_pair_"+name, p, poly(saved["pair"][name]))
check("saved_shift_and_normalization", saved["pair"]["shift"] == "1"
      and Q(saved["pair"]["leading_normalization"]) == A)
identity("F_is_square_plus_one", F, combine((1, product(h, h)), (1, poly([1]))))
identity("direct_image", operator(P), F)
identity("binomial_input_translation", f, combine((1/A, shift_one(P))))
identity("binomial_output_translation", image, combine((1/A, shift_one(F))))
identity("translated_image", operator(f), image)
check("input_and_output_degree_monic", max(f) == max(image) == 6
      and f[6] == image[6] == 1)
check("every_input_coefficient_positive", all(f.get(j, 0) > 0 for j in range(7)))
check("every_output_coefficient_positive", all(image.get(j, 0) > 0 for j in range(7)))
check("input_IVT_signs", P[0] < 0 and max(P) == 6 and P[6] > 0)
check("strict_square_lower_bound", A > 0 and 1/A == Q(1, 154449))

# q=(5/18)((z+9/5)^2+(3/5)^2), with the required negative-real roots.
u, v = Q(9, 5), Q(3, 5)
symbol_factored = combine((Q(5, 18), product(poly([u, 1]), poly([u, 1]))),
                          (Q(5, 18)*v*v, poly([1])))
identity("complete_symbol_factorization", q, symbol_factored)
check("closed_sector_boundary", u > 0 and v > 0 and v/u == Q(1, 3))
check("symbol_degree_constant_and_signs", max(q) == 2 <= 6 and q[0] == 1
      and all(q.get(j, 0) > 0 for j in range(3)))
g = poly([0, 0, 0, 0, Q(25, 3), 6, 1])
identity("reference_polynomial", operator(poly([0]*6+[1])), g)
check("reference_discriminant", Q(36)-4*Q(25, 3) == Q(8, 3) > 0)
walsh_coefficients = [Q(factorial(6-k), factorial(6))*g.get(6-k, 0)
                      for k in range(7)]
check("full_Walsh_factorial_normalization",
      walsh_coefficients == [Q(1), Q(1), Q(5, 18), 0, 0, 0, 0])

# The complete displayed chain is checked, not just producer booleans.
displayed = [
    [-162175, 0, 1973286, 1818396, 3470049, 1421874, 463347],
    [0, 3946572, 5455188, 13880196, 7109370, 2780082],
    [21244925, 44070054, -111417378, 35890584, -72137508],
    [-8934397682925, -35555930659525, 21301855128216, -49337589698506],
    [-44971094689888174916875, -118493320081253974313436,
     126584707461355888116048],
    [29362654455251567260891958254975, 126171402727656343640644465559104],
    [1],
]
S = [poly(row) for row in displayed]
check("full_displayed_chain_matches_saved", S == [poly(row) for row in
      saved["sturm"]["polynomials_ascending"]])
identity("initial_positive_scale", S[0], combine((3, P)))
check("saved_initial_scale", Q(saved["sturm"]["P_to_S0_positive_scale"]) == 3)
identity("initial_derivative", S[1], derivative(S[0]))
check("strict_degree_descent", [max(s) for s in S] == list(range(6, -1, -1)))
relations = saved["sturm"]["relations"]
check("exactly_five_nonterminal_relations", len(relations) == 5)
verified_relations = []
for index, r in enumerate(relations):
    quotient = poly(r["quotient_ascending"])
    c = Q(r["positive_remainder_scale"])
    check(f"relation_{index}_index_and_positive_scale",
          r["dividend_index"] == index and c > 0)
    check(f"relation_{index}_remainder_degree", max(S[index+2]) < max(S[index+1]))
    rhs = combine((1, product(quotient, S[index+1])), (-1/c, S[index+2]))
    identity(f"signed_remainder_{index}", S[index], rhs)
    verified_relations.append({"index": index, "quotient": vector(quotient),
                               "positive_scale": str(c),
                               "remainder": vector(combine((-1/c, S[index+2])))})
terminal_q = poly(saved["sturm"]["terminal_quotient_ascending"])
identity("terminal_zero_remainder", S[-2], product(terminal_q, S[-1]))
check("constant_nonzero_terminal_gcd", S[-1] == poly([1]))
minus = [sgn(s[max(s)]) * (-1)**max(s) for s in S]
plus = [sgn(s[max(s)]) for s in S]
vm, vp = variation(minus), variation(plus)
check("both_full_infinity_sign_lists", minus == [1, -1, -1, 1, 1, -1, 1]
      and plus == [1, 1, -1, -1, 1, 1, 1])
check("saved_infinity_sign_lists", minus == saved["sturm"]["signs_minus_infinity"]
      and plus == saved["sturm"]["signs_plus_infinity"])
check("exact_variations_and_real_count", (vm, vp, vm-vp) == (4, 2, 2))
check("saved_counts_and_squarefreeness", saved["sturm"]["gcd_degree"] == 0
      and saved["sturm"]["real_count_with_multiplicity"] == 2
      and saved["sturm"]["nonreal_count_with_multiplicity"] == 4)
expected_bounds = {
    "required_input_nonreal_count": 4, "actual_input_nonreal_count": 4,
    "required_output_nonreal_count": 6, "actual_output_nonreal_count": 6,
    "output_real_axis_lower_bound": "1/154449",
    "required_output_real_axis_lower_bound": ">0",
    "minimum_input_coefficient": "1", "required_input_coefficients": ">=0",
}
check("full_saved_bounds", saved["bounds"] == expected_bounds)
check("minimum_input_coefficient", min(f.values()) == 1 and len(f) == 7)
check("producer_reports_no_failures", not saved["failures"]
      and len(saved["checks"]) == 15 and all(saved["checks"].values()))

# Reproduce in a temporary directory: do not overwrite the original certificate.
with tempfile.TemporaryDirectory(prefix="c020x-audit1492-") as tmp:
    copy = Path(tmp) / SOURCE.name
    copy.write_bytes(SOURCE.read_bytes())
    run = subprocess.run([sys.executable, str(copy)], capture_output=True, text=True)
    check("original_script_replay_exit_zero", run.returncode == 0)
    replay_bytes = copy.with_suffix(".json").read_bytes()
    replay = json.loads(replay_bytes)
    REPLAY.write_bytes(replay_bytes)
check("complete_replay_matches_saved_certificate", replay == saved)

certificate = {
    "scope": "Fixed C020x rational witness only; no degree or parameter sweep",
    "original_source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    "original_certificate_sha256": hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
    "coefficient_order": "ascending",
    "identities": identities,
    "sturm": {"polynomials": [vector(s) for s in S],
              "verified_relations": verified_relations,
              "terminal_quotient": vector(terminal_q),
              "minus_infinity_signs": minus, "plus_infinity_signs": plus,
              "variations": [vm, vp], "gcd_degree": 0,
              "real_count_with_multiplicity": vm-vp},
    "symbol": {"negative_real_part_magnitude": str(u),
               "imaginary_part_magnitude": str(v), "sector_ratio": str(v/u),
               "reference_discriminant": "8/3",
               "Walsh_coefficients": [str(c) for c in walsh_coefficients]},
    "bounds": expected_bounds,
    "replay": {"certificate": REPLAY.name, "exit_code": run.returncode,
               "stdout": run.stdout, "stderr": run.stderr,
               "complete_certificate_equal": replay == saved},
    "checks": checks, "failures": [name for name, ok in checks.items() if not ok],
    "logical_qualifications": [
        "Walsh and Sturm theorem applicability is checked in C020x, not proved by code.",
        "Output count uses degree six and the exact real square lower bound; no simplicity premise.",
        "P is squarefree by the verified constant-terminal signed remainder chain.",
        "No inverse moments, actual-Xi applicability or exceptional-loss payment is assumed.",
    ],
}
OUTPUT.write_text(json.dumps(certificate, indent=2)+"\n")
print(f"Independent exact audit: {sum(checks.values())}/{len(checks)} checks")
print(f"Counts actual/required: input {6-(vm-vp)}/4, output 6/6; gcd degree 0")
print(f"Sturm variations actual/required: {vm},{vp} / 4,2")
print(f"Input minimum actual/required: {min(f.values())} / >=0")
print(f"Output lower bound actual/required: {1/A} / >0")
print(f"Failures: {certificate['failures']}")
print(f"Audit certificate: {OUTPUT}")
print(f"Preserved-source replay certificate: {REPLAY}")
if certificate["failures"]:
    raise SystemExit(1)
