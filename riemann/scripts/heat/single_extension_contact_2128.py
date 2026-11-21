"""Exact finite checks for C874b; no actual-theta realization is tested."""
from fractions import Fraction as F
import json
from pathlib import Path


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def check_case(name, atoms, c, zero_last=None):
    c = list(map(F, c))
    moments = {k: sum((F(w) * F(t) ** (k - 2) for t, w in atoms), F(0))
               for k in range(2, 9)}
    if zero_last is not None:
        assert not atoms
        moments[8] = F(zero_last)
    h3 = [[moments[i + j + 2] for j in range(4)] for i in range(4)]
    gram = [[sum((F(w) * F(t) ** i * F(t) ** j for t, w in atoms), F(0))
             for j in range(4)] for i in range(4)]
    if zero_last is not None:
        gram[3][3] += F(zero_last)
    null = [dot(row[:3], c) for row in h3[:3]]
    # D_n is affine in the arbitrary S_1. Retain both coefficients.
    def derivative(n):
        constant = -2 * n * (2 * n + 1) * moments[n + 1]
        slope = F(0)
        for a in range(1, n + 1):
            b = n + 1 - a
            if a == 1:
                slope += 4 * n * moments[b]
            elif b == 1:
                slope += 4 * n * moments[a]
            else:
                constant += 4 * n * moments[a] * moments[b]
        return constant, slope
    flux = [sum((c[i] * c[j] * derivative(i + j + 2)[a]
                 for i in range(3) for j in range(3)), F(0)) for a in (0, 1)]
    root_values = [sum((c[i] * F(t) ** i for i in range(3)), F(0))
                   for t, _ in atoms]
    atom_flux = sum((8 * F(w) * F(t) * (c[1] + 2 * c[2] * F(t)) ** 2
                     * (F(w) - F(t) ** 2) for t, w in atoms), F(0))
    failures = []
    if h3 != gram:
        failures.append("full Gram identity")
    if any(F(w) <= 0 for _, w in atoms):
        failures.append("positive masses")
    if zero_last is not None and F(zero_last) < 0:
        failures.append("zero-mass last diagonal")
    if any(null):
        failures.append("H2 null vector")
    if any(root_values):
        failures.append("support roots")
    if flux != [atom_flux, F(0)]:
        failures.append("atomic flux or S1 cancellation")
    return dict(name=name, moments={str(k): str(v) for k, v in moments.items()},
                c=list(map(str, c)), H3=[[str(v) for v in row] for row in h3],
                null=list(map(str, null)), support_roots=list(map(str, root_values)),
                flux_constant=str(flux[0]), flux_S1_coefficient=str(flux[1]),
                atomic_flux=str(atom_flux), required_upper_bound="0", failures=failures)


cases = [
    check_case("lower_degree_positive_obstruction", [(1, 2)], [-1, 1, 0]),
    check_case("full_degree_positive_obstruction", [(0, 1), (1, 2)], [0, -1, 1]),
    check_case("lower_degree_negative_control", [(1, F(1, 2))], [-1, 1, 0]),
    check_case("negative_root_positive_flux", [(-1, F(1, 2))], [1, 1, 0]),
    check_case("repeated_root_equality", [(1, 2)], [1, -2, 1]),
    check_case("two_nonzero_roots", [(1, 2), (2, 4)], [2, -3, 1]),
    check_case("zero_mass_constant", [], [1, 0, 0], zero_last=7),
    check_case("zero_mass_full_degree", [], [1, -2, 3], zero_last=7),
]
failures = [{"case": case["name"], "failed": case["failures"]}
            for case in cases if case["failures"]]
for case in cases[:2]:
    if case["flux_constant"] != "16":
        failures.append({"case": case["name"], "failed": "required flux 16"})
output = Path(__file__).with_name("single-extension-contact-2128.json")
output.write_text(json.dumps(dict(cases=cases, failures=failures,
    summary=dict(cases=len(cases), failures=len(failures),
                 obstruction_flux="16", required_upper_bound="0",
                 actual_theta_realization="not asserted")), indent=2) + "\n")
print(f"Exact cases: {len(cases)}; failures: {len(failures)}")
print("Obstruction flux: 16; required upper bound: 0")
print(f"Certificate: {output.relative_to(Path.cwd())}")
if failures:
    print(failures)
    raise SystemExit(1)
