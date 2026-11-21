"""O-only rational replay; analytic justification is canonical in C033c.

No zero coordinates, quadrature, R/E bounds, or dictionary optimization.
The external divisor/counting inputs are conditional, not checked here.
"""
from fractions import Fraction as Q
from pathlib import Path
import json

base, epsilon = Q(3, 8), Q(1, 10**100)
A = 3 * (40 * base**18 + epsilon)
checks = []


def less(name, actual, required):
    checks.append(dict(name=name, actual_exact=str(actual),
                       required_exact=str(required), relation="<",
                       passed=actual < required))


less("count_at_100", Q(911, 24), Q(40))
less("tail_shift_up_to_13_over_4", Q(13, 4), Q(50))
less("sixth_power", base**6, Q(1, 256))
less("high_divisor_gaussian_tail", 1200 * base**312, epsilon)
less("small_additive_error", 48 * epsilon, Q(1, 131072))
less("disk_bound_via_elementary_comparison", 16 * A, Q(1, 8192))
less("requested_O_allowance", 16 * A, Q(1, 16))

saved_path = Path(__file__).with_name("bounded_variation_dual_1571.json")
saved_A = Q(json.loads(saved_path.read_text())["elementary_bounds"]["A2"])
checks.append(dict(name="same_saved_A2", actual_exact=str(A),
                   required_exact=str(saved_A), relation="=",
                   passed=A == saved_A))
failures = [c["name"] for c in checks if not c["passed"]]
certificate = dict(
    canonical_proof="lemmas/C033c-saved-odd-enclosure-audit.md",
    prior_assessment="drafts/literature/2026-11-18-saved-odd-enclosure-audit-1617.md",
    scope="O only; real 1<=sigma<=2; full closed complex disk |w|<=2",
    qualified_inputs=[
        "C032m actual positive-ordinate divisor and entire straight primitive",
        "multiplicity; gamma>14; |delta|<1/2; no ordinate-zero input omitted",
        "N(T)=O(T log(T+2)); qualified fixed-v1 count/finite-zero/heat inputs",
        "N(100)<40; sum_gamma_gt_100 gamma^-2<3/25 from C032s(8) and count",
        "source-wide correctness and zero data not independently verified",
    ],
    unused_for_O_upper_bound=[
        "reality of zeros through 100", "existence of a zero in (14,15)",
        "individual coordinates", "R/E bounds", "lower boxes and optimizer",
        "probability-law positivity", "global profile positivity", "RH",
    ],
    exact_values=dict(base=str(base), epsilon=str(epsilon), A=str(A),
                      absolute_disk_bound=str(16 * A),
                      required_strict_bound="1/16",
                      ratio_to_allowance=str(256 * A)),
    checks=checks, failures=failures,
    conclusion="Conditional saved O enclosure pays allowance; no direct-prime evaluator or weighted residual certified",
)
path = Path(__file__).with_suffix(".json")
path.write_text(json.dumps(certificate, indent=2) + "\n")
print(f"O absolute disk bound = {float(16*A):.12g}; required < 0.0625 (1/16)")
print(f"exact comparisons: 16*A < 1/8192 < 1/16; failures={failures}")
print(f"certificate={path}; analytic proof={certificate['canonical_proof']}")
raise SystemExit(bool(failures))
