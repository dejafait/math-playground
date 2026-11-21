"""Bounded exact execution prefix of audited C033z; never a scalar certificate.

No rounded arithmetic or substituted evaluator is used. Exact rationals are
stored as signed hexadecimal numerator / positive hexadecimal denominator.
The operation ledger is inherited, not a measured runtime or bit-cost bound.
Certificate serialization and verification are outside that evaluator ledger.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import signal
import time

from direct_positive_real_inputs_1802 import (
    evaluate, legendre_polynomials, cardinal_weight,
)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "direct_positive_real_execution_1808"
SUMMARY = ROOT / "direct_positive_real_execution_1808.json"


def rational(value):
    return {"numerator_hex": hex(value.numerator),
            "denominator_hex": hex(value.denominator)}


def encode(value):
    if isinstance(value, F):
        return rational(value)
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value


def bits(value):
    return {"numerator": abs(value.numerator).bit_length(),
            "denominator": value.denominator.bit_length()}


def write_json(path, value):
    temp = path.with_suffix(".tmp")
    temp.write_text(json.dumps(encode(value), indent=2) + "\n")
    temp.replace(path)


def horner(coefficients, x):
    value = coefficients[-1]
    for c in reversed(coefficients[:-1]):
        value = value*x + c
    return value


def power2(value, squarings):
    for _ in range(squarings):
        value = value*value
    return value


def clamp(value, lo=F(0), hi=F(1)):
    return lo if value < lo else hi if value > hi else value


def rule(coefficients, n):
    grid = [F(j, 128) for j in range(129)]
    values = [evaluate(coefficients, x) for x in grid]
    seeds = [(grid[j], grid[j+1]) for j in range(128)
             if (values[j] < 0) != (values[j+1] < 0)
             and values[j] and values[j+1]]
    intervals = []
    for left, right in seeds:
        sign = evaluate(coefficients, left) > 0
        for _ in range(160):
            mid = (left+right)/2
            value = evaluate(coefficients, mid)
            if value == 0:
                left = right = mid
            elif (value > 0) == sign:
                left = mid
            else:
                right = mid
        intervals.append((left, right))
    intervals = [(-b, -a) for a, b in reversed(intervals)] + (
        [(F(0), F(0))] if n % 2 else []) + intervals
    assert len(intervals) == n
    nodes = [(a+b)/2 for a, b in intervals]
    weights = [cardinal_weight(nodes, j) for j in range(n)]
    # These are verification operations, outside the evaluator ledger.
    assert all(b-a <= F(1, 2**167) for a, b in intervals)
    assert all((a == b and evaluate(coefficients, a) == 0)
               or evaluate(coefficients, a)*evaluate(coefficients, b) < 0
               for a, b in intervals)
    return {"degree": n, "coefficients": coefficients,
            "intervals": intervals, "nodes": nodes, "weights": weights}


class Deadline(Exception):
    pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=180)
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    # Fresh execution; refuse to overwrite existing completed evidence.
    if SUMMARY.exists():
        raise SystemExit("Existing1808 evidence preserved; choose a separate run ID before replay")
    started = time.monotonic()
    report = {
        "status": "RUNNING_EXACT_PREFIX", "target": "C033y/C033z eight scalar execution",
        "assessment": "drafts/literature/2026-11-19-direct-positive-real-scalar-execution-review-1806.md",
        "arithmetic": "Python fractions.Fraction, exact rational operations only",
        "time_limit_seconds": args.seconds,
        "prescribed_complete_operation_upper": 989767, "required_operation_cap": 1000000,
        "actual_complete_operation_count_verified": False,
        "required_scalar_radius": "1/256", "analytic_allowance": "25/16384",
        "reserved_exponent_arithmetic_allowance": "1/1024",
        "reserved_final_exponential_allowance": "1/1024",
        "scalars_evaluated": 0, "profiles_evaluated": 0,
        "gaussian_inputs_completed": 0, "moments_completed": 0,
        "artifacts": [], "gaussian_records": [], "moment_records": [],
        "failures": [], "pending": "reference rule construction",
        "limitations": ["No scalar or exponent follows from this prefix",
                        "989767 is the prescribed full-construction ledger, not a completed-run count",
                        "Time and bit sizes are operational evidence, not a mathematical lower bound",
                        "All C033y/z analytic and source qualifications remain in force"],
    }

    def checkpoint():
        report["elapsed_seconds"] = round(time.monotonic()-started, 3)
        write_json(SUMMARY, report)

    def save(name, data):
        path = OUT / (name+".json")
        write_json(path, data)
        report["artifacts"].append({"path": str(path.relative_to(ROOT.parent.parent)),
            "bytes": path.stat().st_size,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
        checkpoint()

    def timeout(_signum, _frame):
        raise Deadline()

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(args.seconds)
    checkpoint()
    try:
        polynomials = legendre_polynomials()
        rules = [rule(polynomials[n], n) for n in (12, 13)]
        save("reference_rules", {"rules": rules})
        coefficients = [F(1, factorial(k)) for k in range(41)]
        inner = []
        for panel in range(4):
            for root, weight in zip(rules[0]["nodes"], rules[0]["weights"]):
                x = panel+(1+root)/2
                omega = clamp(weight/2)
                inner.append((x, omega))
        save("inner_nodes", {"nodes_and_weights": inner,
            "taylor_coefficients_ascending": coefficients})
        gaussian = []
        for index, (x, omega) in enumerate(inner):
            report["pending"] = f"Gaussian input {index+1}/48: T40(-x^2/16), clamp, four squarings"
            checkpoint()
            tick = time.monotonic()
            z = (x*x)/(-16)
            polynomial = clamp(horner(coefficients, z))
            value = power2(polynomial, 4)
            gaussian.append(value)
            record = {"index": index, "value_bits": bits(value),
                      "seconds": round(time.monotonic()-tick, 6)}
            # Complete exact value, not a decimal preview or sampled enclosure.
            save(f"gaussian_{index:02d}", {"index": index, "x": x, "omega": omega,
                "reduced_argument": z, "clamped_T40": polynomial, "value": value,
                "constructor": "C033z(13)", "proved_error": "<2^-150",
                "required_input_error": "<=2^-60"})
            report["gaussian_inputs_completed"] = len(gaussian)
            report["gaussian_records"].append(record)
            checkpoint()
        # C033z's shared moments: successive powers, exact products and sums.
        a = [omega*e for (_, omega), e in zip(inner, gaussian)]
        v = [x/4 for x, _ in inner]
        powers = [F(1)]*48
        save("moment_inputs", {"a": a, "v": v})
        for k in range(29):
            partial = F(0)
            for j in range(48):
                report["pending"] = f"M_{k}: adding summand {j+1}/48"
                checkpoint()
                partial += a[j]*powers[j]
                # Retain the full prefix sum after each expensive addition.
                # Replaces only this run's latest prefix, never historical data.
                write_json(OUT / "moment_partial.json", {"k": k,
                    "summands_completed": j+1, "value": partial})
                report["latest_moment_prefix"] = {"k": k,
                    "summands_completed": j+1, "value_bits": bits(partial)}
                checkpoint()
            save(f"moment_{k:02d}", {"k": k, "value": partial})
            report["moments_completed"] = k+1
            report["moment_records"].append({"k": k, "value_bits": bits(partial)})
            checkpoint()
            if k < 28:
                for j in range(48):
                    powers[j] *= v[j]
        report["status"] = "INPUT_MOMENT_PREFIX_COMPLETE_SCALARS_NOT_EXECUTED"
        report["pending"] = "Remaining audited outer/profile/scalar constructors are not implemented in this prefix driver"
    except Deadline:
        signal.alarm(0)
        report["status"] = "TIME_LIMIT_EXACT_PREFIX_INCOMPLETE"
        report["failures"].append("Bounded wall-time execution did not complete; no scalar enclosure")
    except Exception as exc:
        signal.alarm(0)
        report["status"] = "EXECUTION_ERROR_PREFIX_INCOMPLETE"
        report["failures"].append(f"{type(exc).__name__}: {exc}")
        raise
    finally:
        signal.alarm(0)
        partial_path = OUT / "moment_partial.json"
        if partial_path.exists():
            report["latest_partial_artifact"] = {
                "path": str(partial_path.relative_to(ROOT.parent.parent)),
                "bytes": partial_path.stat().st_size,
                "sha256": hashlib.sha256(partial_path.read_bytes()).hexdigest()}
        checkpoint()
        print(f"Status: {report['status']}; Gaussian inputs {report['gaussian_inputs_completed']}/48; moments {report['moments_completed']}/29")
        print(f"Scalars {report['scalars_evaluated']}/8; required radius <1/256: NOT ESTABLISHED")
        print("Full prescribed operations <=989767 versus cap1000000; completed-run count NOT ESTABLISHED")
        print(f"Pending: {report['pending']}; failures: {report['failures']}")
        print(f"Certificate: {SUMMARY.relative_to(ROOT.parent.parent)}; exact data: {OUT.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
