"""Execute only the previously audited C033z Ihat block construction.

All sample operations are exact Fraction operations. Only the prescribed
four-sample conversions round, using 43 strict midpoint comparisons.
Instrumentation covers executed node/weight maps, samples and conversions;
the reused P14 rule/coefficient table and full scalar ledger are not measured.
"""
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json
import signal
import time

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
OUT = HERE / "direct_positive_real_ihat_execution_1814"
INDEX = HERE / "direct_positive_real_ihat_execution_1814.json"
SOURCE = HERE / "direct_positive_real_execution_1808/reference_rule14.json"
COEFFICIENTS = HERE / "direct_positive_real_execution_1808/inner_nodes.json"


def encode(v):
    if isinstance(v, Q):
        return {"numerator_hex": hex(v.numerator), "denominator_hex": hex(v.denominator)}
    if isinstance(v, dict):
        return {str(k): encode(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [encode(x) for x in v]
    return v


def decode(v):
    if isinstance(v, dict):
        if set(v) == {"numerator_hex", "denominator_hex"}:
            return Q(int(v["numerator_hex"], 16), int(v["denominator_hex"], 16))
        return {k: decode(x) for k, x in v.items()}
    if isinstance(v, list):
        return [decode(x) for x in v]
    return v


def write(path, data):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(encode(data), indent=2)+"\n")
    temporary.replace(path)


class Arithmetic:
    def __init__(self):
        self.counts = Counter()

    def op(self, kind, x, y=None):
        self.counts[kind] += 1
        if kind == "add":
            return x+y
        if kind == "subtract":
            return x-y
        if kind == "multiply":
            return x*y
        if kind == "divide":
            return x/y
        if kind == "negate":
            return -x
        if kind == "compare":
            return x > y
        raise ValueError(kind)

    def clamp(self, x):
        below = self.op("compare", Q(0), x)
        above = self.op("compare", x, Q(1))
        return Q(0) if below else Q(1) if above else x

    def horner(self, coefficients, x):
        value = coefficients[-1]
        for c in reversed(coefficients[:-1]):
            value = self.op("add", self.op("multiply", value, x), c)
        return value

    def power(self, x, squarings):
        for _ in range(squarings):
            x = self.op("multiply", x, x)
        return x

    def total(self):
        return sum(self.counts.values())


class Deadline(Exception):
    pass


def main():
    global OUT, INDEX
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=600)
    parser.add_argument("--continue-from", type=Path)
    parser.add_argument("--suffix", default="1814")
    args = parser.parse_args()
    if args.continue_from:
        args.continue_from = args.continue_from.resolve()
    if not args.suffix.replace("_", "").isalnum():
        raise SystemExit("Use an alphanumeric run suffix")
    OUT = HERE / ("direct_positive_real_ihat_execution_"+args.suffix)
    INDEX = HERE / ("direct_positive_real_ihat_execution_"+args.suffix+".json")
    if INDEX.exists() or OUT.exists():
        raise SystemExit("Preserve1814 evidence: this driver refuses to overwrite a run")
    OUT.mkdir()
    started = time.monotonic()
    math = Arithmetic()
    report = {"status": "RUNNING_IHAT_ONLY", "samples_completed": 0,
        "checkpoints_completed": 0, "scalars_evaluated": 0, "failures": [],
        "assessment": "drafts/literature/2026-11-19-direct-positive-real-rounded-ihat-execution-review-1812.md",
        "input_sha256": {str(p.relative_to(NOTEBOOK)): hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (SOURCE, COEFFICIENTS)},
        "artifacts": [], "sample_records": [], "checkpoint_records": [],
        "pending": "load exact saved rule/table", "time_limit_seconds": args.seconds,
        "required_samples": 224, "required_checkpoints": 56,
        "Ihat_additional_error_bound": "7/536870912", "checkpoint_error_bound": "1/4294967296",
        "required_scalar_radius": "1/256", "inherited_full_ledger": 997104,
        "required_full_cap": 1000000, "full_execution_count_verified": False,
        "independent_replay_completed": False,
        "limits": ["Ihat-only construction, not a scalar or analytic-source verification",
                   "Rule/table reused, not charged as measured generation",
                   "997104 is inherited full ledger, not completed-run cost",
                   "Source/zero-data, bit cost, interpolation, TV and Xi gaps remain"]}
    first_sample = 0
    inherited_rounded = Q(0)
    if args.continue_from:
        previous_raw = args.continue_from.read_bytes()
        previous = decode(json.loads(previous_raw))
        if previous["status"] != "TIME_LIMIT_IHAT_INCOMPLETE":
            raise SystemExit("Continuation requires an interrupted exact1814 run")
        completed_blocks = previous["checkpoints_completed"]
        first_sample = 4*completed_blocks
        kept_names = {f"sample_{i:03d}.json" for i in range(first_sample)}
        kept_names |= {f"checkpoint_{i:02d}.json" for i in range(1, completed_blocks+1)}
        artifacts = [a for a in previous["artifacts"] if Path(a["path"]).name in kept_names]
        for item in artifacts:
            if hashlib.sha256((NOTEBOOK/item["path"]).read_bytes()).hexdigest() != item["sha256"]:
                raise SystemExit("Continuation input hash failure")
        if completed_blocks:
            last_path = next(NOTEBOOK/a["path"] for a in artifacts
                             if Path(a["path"]).name == f"checkpoint_{completed_blocks:02d}.json")
            inherited_rounded = decode(json.loads(last_path.read_text()))["output"]
        report.update({"samples_completed": first_sample, "checkpoints_completed": completed_blocks,
            "artifacts": artifacts, "sample_records": previous["sample_records"][:first_sample],
            "checkpoint_records": previous["checkpoint_records"][:completed_blocks],
            "continuation_from": str(args.continue_from.relative_to(NOTEBOOK)),
            "continuation_sha256": hashlib.sha256(previous_raw).hexdigest(),
            "previous_segment_executed_operations": previous["executed_operation_total"],
            "reused_completed_samples": first_sample,
            "reused_completed_checkpoints": completed_blocks,
            "inherited_prefix_required_operations": 15+113*first_sample+131*completed_blocks,
            "previous_segment_abandoned_operations": previous["executed_operation_total"]
                  -(15+113*first_sample+131*completed_blocks),
            "continuation_limit": "Resume at last saved complete block; prior unfinished block preserved, not overwritten"})

    def checkpoint():
        report["elapsed_seconds"] = round(time.monotonic()-started, 3)
        report["executed_operation_counts"] = dict(math.counts)
        report["executed_operation_total"] = math.total()
        write(INDEX, report)

    def save(name, data):
        path = OUT / (name+".json")
        write(path, data)
        report["artifacts"].append({"path": str(path.relative_to(NOTEBOOK)),
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest(), "bytes": path.stat().st_size})

    def pending(text):
        report["pending"] = text
        checkpoint()

    def timeout(_signum, _frame):
        raise Deadline()

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(args.seconds)
    checkpoint()
    try:
        rule = decode(json.loads(SOURCE.read_text()))
        coeff = decode(json.loads(COEFFICIENTS.read_text()))["taylor_coefficients_ascending"][:21]
        weights = [math.op("divide", w, Q(2)) for w in rule["weights"]]
        negative_endpoint = math.op("negate", Q(2048))
        rounded = inherited_rounded
        subtotal = rounded
        for index in range(first_sample, 224):
            panel, j = divmod(index, 14)  # Fixed loop coordinates, not evaluator arithmetic.
            x = math.op("add", Q(panel), math.op("divide",
                math.op("add", Q(1), rule["nodes"][j]), Q(2)))
            omega = math.clamp(weights[j])
            before = math.total()
            tick = time.monotonic()
            pending(f"sample{index+1}/224: exact A/u/quotient")
            z = math.op("divide", math.op("negate", math.op("multiply", x, x)), Q(256))
            A = math.power(math.clamp(math.horner(coeff, z)), 8)
            z = math.op("divide", math.op("negate", x), Q(16))
            u = math.power(math.clamp(math.horner(coeff, z)), 3)
            denominator = math.op("subtract", Q(1), math.power(u, 2))
            h = math.op("divide", math.op("multiply", math.op("subtract", A, u), u), denominator)
            # Validation below is outside the evaluator ledger.
            if not (denominator > Q(1, 512) and abs(h) < 7):
                raise ArithmeticError(f"sample range failure at {index}")
            weighted = math.op("multiply", omega, h)
            save(f"sample_{index:03d}", {"index": index, "x": x, "omega": omega,
                "A": A, "u": u, "denominator": denominator, "h": h, "weighted": weighted})
            pending(f"sample{index+1}/224: weighted addition")
            subtotal = math.op("add", subtotal, weighted)
            if math.total()-before != 108:
                raise ArithmeticError("sample instrumentation differs from audited108")
            write(OUT / "partial.json", {"samples_completed": index+1, "value": subtotal,
                "rounded_checkpoints_completed": index//4, "last_completed_rounded": rounded})
            report["samples_completed"] = index+1
            report["sample_records"].append({"index": index, "operations": 108,
                "seconds": round(time.monotonic()-tick, 6),
                "h_denominator_bits": h.denominator.bit_length(),
                "subtotal_denominator_bits": subtotal.denominator.bit_length()})
            if (index+1) % 4 == 0:
                block = (index+1)//4
                pending(f"checkpoint{block}/56: 43 strict midpoint bisections")
                before = math.total()
                lo, hi = negative_endpoint, Q(2048)
                branches = []
                for _ in range(43):
                    mid = math.op("divide", math.op("add", lo, hi), Q(2))
                    upper = math.op("compare", subtotal, mid)
                    branches.append(upper)
                    if upper:
                        lo = mid
                    else:
                        hi = mid
                new = math.op("divide", math.op("add", lo, hi), Q(2))
                if math.total()-before != 131:
                    raise ArithmeticError("conversion instrumentation differs from audited131")
                save(f"checkpoint_{block:02d}", {"block": block, "previous": rounded,
                    "input": subtotal, "lo": lo, "hi": hi, "output": new,
                    "strict_upper_branches": branches, "operations": 131})
                rounded = new
                subtotal = rounded
                report["checkpoints_completed"] = block
                report["checkpoint_records"].append({"block": block, "operations": 131,
                    "output": str(new), "output_denominator_bits": new.denominator.bit_length()})
            checkpoint()
        save("Ihat", {"value": rounded, "additional_error_from_original_exact_sum": Q(56, 2**32),
            "original_sample_weight_error": "<2^-30; analytic quadrature/tail separate"})
        report["status"] = "IHAT_EXECUTION_COMPLETE_REPLAY_REQUIRED"
        report["pending"] = "independent complete sample/checkpoint replay"
        report["rounded_Ihat"] = str(rounded)
        report["prescribed_complete_scope_operation_breakdown"] = {
            "unit_maps_and_weight_clamps": 1134, "samples_and_weighted_additions": 224*108,
            "shared_negation_and_conversions": 1+56*131}
        expected_segment = 15+113*(224-first_sample)+131*(56-first_sample//4)
        report["expected_current_segment_operations"] = expected_segment
        report["prescribed_complete_scope_operations"] = 32663
        report["all_segments_measured_operations"] = math.total()+report.get("previous_segment_executed_operations", 0)
        if math.total() != expected_segment:
            raise ArithmeticError("executed Ihat scope total mismatch")
    except Deadline:
        signal.alarm(0)
        report["status"] = "TIME_LIMIT_IHAT_INCOMPLETE"
        report["failures"].append("Operational time limit; incomplete evidence is not a mathematical obstruction")
    except Exception as exc:
        signal.alarm(0)
        report["status"] = "IHAT_EXECUTION_FAILED"
        report["failures"].append(f"{type(exc).__name__}: {exc}")
        raise
    finally:
        signal.alarm(0)
        partial = OUT / "partial.json"
        if partial.exists():
            report["partial_sha256"] = hashlib.sha256(partial.read_bytes()).hexdigest()
        checkpoint()
        print(f"{report['status']}: samples {report['samples_completed']}/224; checkpoints {report['checkpoints_completed']}/56")
        print(f"Executed Ihat scope operations {math.total()}; full997104 ledger remains inherited")
        print(f"Failures: {report['failures']}; certificate: {INDEX.relative_to(NOTEBOOK)}")


if __name__ == "__main__":
    main()
