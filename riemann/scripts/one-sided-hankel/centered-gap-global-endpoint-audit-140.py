#!/usr/bin/env python3
"""Replay and independently assemble L702's existing rational comparisons."""

import hashlib
import importlib.util
import json
from fractions import Fraction as F
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent
    source = directory / "centered-gap-global-endpoint-138.json"
    generator = directory / "centered-gap-global-endpoint-138.py"
    replay = directory / "centered-gap-global-endpoint-replay-140.json"
    output = Path(__file__).with_suffix(".json")
    original = source.read_bytes()
    cert = json.loads(original)
    spec = importlib.util.spec_from_file_location("endpoint138", generator)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # main() chooses its output from __file__; preserve the original artifact.
    module.__file__ = str(replay.with_suffix(".py"))
    replay_exit = module.main()
    checks = []

    def equal(name, actual, required):
        checks.append({"name": name, "actual": actual, "required": required,
                       "passed": actual == required})

    def rat(value):
        return f"{value.numerator}/{value.denominator}"

    equal("replay_exit", replay_exit, 0)
    equal("replay_byte_identical", replay.read_bytes() == original, True)
    equal("original_preserved", source.read_bytes() == original, True)
    equal("step", cert["step"], 138)
    equal("scope", cert["scope"],
          "Exact constants only; analytic limits and profile selection are proved in L702.")

    # Assemble both 12-term sums by recurrence, without calling log_bounds().
    logs = {}
    for key, argument, z in [("log_5", F(5), F(2, 3)),
                             ("log_121_over_41", F(121, 41), F(40, 81))]:
        power, total, terms = z, F(0), []
        for k in range(12):
            term = 2 * power / (2 * k + 1)
            terms.append(rat(term))
            total += term
            power *= z * z
        remainder = 2 * power / (25 * (1 - z * z))
        expected = {"argument": rat(argument), "z": rat(z), "terms": 12,
                    "lower": rat(total), "upper": rat(total + remainder),
                    "tail_upper": rat(remainder), "strict": True}
        equal(key, cert["log_bounds"][key], expected)
        logs[key] = {"terms": terms, "lower": rat(total),
                     "upper": rat(total + remainder), "tail_upper": rat(remainder)}

    lo = F(27, 10) * (F(logs["log_5"]["lower"]) - F(4, 5)
                         + F(121, 100) * F(logs["log_121_over_41"]["lower"]))
    hi = F(27, 10) * (F(logs["log_5"]["upper"]) - F(4, 5)
                         + F(121, 100) * F(logs["log_121_over_41"]["upper"]))
    equal("omega_bounds", cert["omega_bounds"],
          {"lower": rat(lo), "upper": rat(hi),
           "required_lower": "11/2", "required_upper": "6/1"})
    d, u, a, y = F(5, 4), F(121, 64), F(27, 10), F(9, 20)
    numerator = u - 2 * d + 1
    difference = numerator / (d * u)
    squared_gap = difference / d
    denominator = 1 + (y / (d - 1)) ** 2
    loss = squared_gap * F(2, 5) ** 2 / denominator
    expected_rows = [
        ("frequency_lower", lo, ">", F(11, 2)),
        ("frequency_upper", hi, "<", F(6)),
        ("seven_pi_over_four_upper_uses_pi_lt_22_over_7", F(7, 4) * F(22, 7), "==", F(11, 2)),
        ("two_pi_lower_uses_pi_gt_3", 2 * F(3), "==", F(6)),
        ("positive_factor_numerator", numerator, "==", F(25, 64)),
        ("beta_minus_alpha_lower", difference, "==", F(20, 121)),
        ("beta_square_minus_alpha_square_lower", squared_gap, "==", F(16, 121)),
        ("factor_square_denominator_upper", denominator, "==", F(106, 25)),
        ("factor_square_loss", loss, "==", F(32, 6413)),
        ("product_decay_rate", loss / 2, "==", F(16, 6413)),
        ("uniform_real_kernel_derivative_upper", a * (1 / (u - d) + 1 / (d - 1)), "<", F(16)),
        ("actual_outer_endpoint_at_n_63", y - F(9, 8) * a / 63, ">", F(2, 5)),
    ]
    relations = {">": lambda x, y: x > y, "<": lambda x, y: x < y,
                 "==": lambda x, y: x == y}
    expected = []
    for name, actual, relation, required in expected_rows:
        passed = relations[relation](actual, required)
        expected.append({"name": name, "actual": rat(actual), "relation": relation,
                         "required": rat(required), "passed": passed})
    equal("complete_comparison_array", cert["checks"], expected)
    equal("all_reassembled_comparisons_pass", all(row["passed"] for row in expected), True)
    equal("failures", cert["failures"], [])
    equal("passed", cert["passed"], True)
    failures = [row["name"] for row in checks if not row["passed"]]
    result = {"step": 140, "scope": "Audit of existing L702 constants only; same Fraction backend, independent recurrence and formula assembly. Analytic proof audited separately in L702.",
              "original_sha256": hashlib.sha256(original).hexdigest(),
              "replay_path": replay.name, "log_reassembly": logs,
              "comparisons": expected, "audit_checks": checks,
              "failures": failures, "passed": not failures}
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(f"Audit checks: {len(checks) - len(failures)}/{len(checks)}; failures={failures}")
    print(f"Replay byte-identical: {replay.read_bytes() == original}; original preserved")
    print("All 12 original comparisons independently assembled with exact Fraction arithmetic.")
    print(f"Certificate: {output.as_posix()}")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
