"""Independent complete-data replay of the saved1814 Ihat-only execution.

Does not import the executor. Uses direct integer Taylor identities,
common-denominator block identities and closed-form cell selection.
Verifier arithmetic, including integer division, is outside evaluator cost.
"""
from fractions import Fraction as Q
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import time
import argparse
import math

from direct_positive_real_ihat_integer_backend_1814 import enable

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
INDEX = HERE / "direct_positive_real_ihat_execution_1814.json"
OUT = HERE / "direct_positive_real_ihat_replay_1814.json"
checks, hashes = {}, {}
started = time.monotonic()


def decode(v):
    if isinstance(v, dict):
        if set(v) == {"numerator_hex", "denominator_hex"}:
            n, d = int(v["numerator_hex"], 16), int(v["denominator_hex"], 16)
            if d <= 0:
                raise ValueError("nonpositive rational denominator")
            return Q(n, d)
        return {k: decode(x) for k, x in v.items()}
    if isinstance(v, list):
        return [decode(x) for x in v]
    return v


def load(path):
    raw = path.read_bytes()
    hashes[str(path.relative_to(NOTEBOOK))] = hashlib.sha256(raw).hexdigest()
    return decode(json.loads(raw))


def check(name, passed):
    checks[name] = bool(passed)
    if not passed:
        raise ArithmeticError("First failed identity: "+name)


def save(report):
    report.update({"checks": checks, "check_count": len(checks),
                   "failures": [k for k, v in checks.items() if not v],
                   "inputs_sha256": hashes, "elapsed_seconds": round(time.monotonic()-started, 3)})
    temporary = OUT.with_suffix(".tmp")
    temporary.write_text(json.dumps(report, indent=2)+"\n")
    temporary.replace(OUT)


def polynomial_power(z, degree, squarings, expected):
    n, d = z.numerator, z.denominator
    fac = factorial(degree)
    den = fac*d**degree
    num = sum(n**k*d**(degree-k)*(fac//factorial(k)) for k in range(degree+1))
    num = max(0, min(den, num))
    power = 2**squarings
    return num**power*expected.denominator == expected.numerator*den**power


def sum_identity(values, expected):
    den = 1
    for value in values:
        den = (den//math.gcd(den, value.denominator))*value.denominator
    num = sum(v.numerator*(den//v.denominator) for v in values)
    return num*expected.denominator == expected.numerator*den


def direct_poly(coefficients, x):
    return sum((c*x**k for k, c in enumerate(coefficients)), Q(0))


def weight_integral(nodes, index):
    coefficients = [Q(1)]
    denominator = Q(1)
    for j, root in enumerate(nodes):
        if j == index:
            continue
        new = [Q(0)]*(len(coefficients)+1)
        for k, value in enumerate(coefficients):
            new[k] -= root*value
            new[k+1] += value
        coefficients = new
        denominator *= nodes[index]-root
    return sum((2*c/Q(k+1) for k, c in enumerate(coefficients) if k % 2 == 0), Q(0))/denominator


def main():
    global INDEX, OUT
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=Path, default=INDEX)
    parser.add_argument("--suffix", default="1814")
    parser.add_argument("--follow", action="store_true")
    args = parser.parse_args()
    INDEX = args.index.resolve()
    OUT = HERE / ("direct_positive_real_ihat_replay_"+args.suffix+".json")
    if OUT.exists():
        raise SystemExit("Preserve1814 replay evidence: choose a new replay ID")
    backend = enable()
    run = load(INDEX)
    report = {"status": "REPLAY_IN_PROGRESS", "samples_replayed": 0,
        "checkpoints_replayed": 0, "scalars_certified": 0,
        "full_execution_count_verified": False,
        "scope": "Every saved completed sample/block; no analytic-source, scalar or full-ledger verification",
        "required_samples": 224, "required_checkpoints": 56, "integer_backend": backend,
        "extra_Ihat_error_bound": "7/536870912", "checkpoint_error_bound": "1/4294967296"}
    save(report)
    try:
        check("execution:replay_mode", args.follow or not run["status"].startswith("RUNNING"))
        artifact_paths = {Path(a["path"]).name: NOTEBOOK/a["path"] for a in run["artifacts"]}
        check("artifacts:unique_names", len(artifact_paths) == len(run["artifacts"]))
        for name, expected in run["input_sha256"].items():
            path = NOTEBOOK / name
            check("input_hash:"+name, hashlib.sha256(path.read_bytes()).hexdigest() == expected)
        for artifact in run["artifacts"]:
            path = NOTEBOOK / artifact["path"]
            check("artifact_hash:"+path.name,
                  hashlib.sha256(path.read_bytes()).hexdigest() == artifact["sha256"]
                  and path.stat().st_size == artifact["bytes"])
        # Keep the artifact lookup independent of the generator's data directory.
        def saved_data(name):
            return load(artifact_paths[name+".json"])
        source = HERE / "direct_positive_real_execution_1808/reference_rule14.json"
        rule = load(source)
        coefficient_data = load(HERE / "direct_positive_real_execution_1808/inner_nodes.json")
        check("table:all41_coefficients", coefficient_data["taylor_coefficients_ascending"]
              == [Q(1, factorial(k)) for k in range(41)])
        # Independent P14 by Rodrigues, every root bracket and cardinal weight.
        c = [Q(0)]*15
        for j in range(7, 15):
            c[2*j-14] = Q((-1)**(14-j)*comb(14, j)*factorial(2*j),
                         2**14*factorial(14)*factorial(2*j-14))
        check("rule:Rodrigues_coefficients", c == rule["coefficients"] and rule["degree"] == 14)
        known = load(HERE / "direct_positive_real_completion_1803.json")["root_rule"]
        check("rule:matches_audited_coefficients", c == list(map(Q, known["coefficients_ascending"])))
        for j, (interval, node, weight, old) in enumerate(zip(
                rule["intervals"], rule["nodes"], rule["weights"], known["roots"])):
            lo, hi = interval
            check(f"rule{j}:matches_audited_exact_data", lo == Q(old["left"])
                  and hi == Q(old["right"]) and node == Q(old["midpoint"])
                  and weight == Q(old["weight"]))
            check(f"rule{j}:bracket_and_radius", -1 < lo < hi < 1
                  and direct_poly(c, lo)*direct_poly(c, hi) < 0
                  and node == (lo+hi)/2 and (hi-lo)/2 <= Q(1, 2**168))
            check(f"rule{j}:cardinal_integral", weight == weight_integral(rule["nodes"], j))
        check("rule:all14_ordered", len(rule["nodes"]) == len(rule["weights"])
              == len(rule["intervals"]) == len(known["roots"]) == 14
              and all(rule["intervals"][j][1] < rule["intervals"][j+1][0] for j in range(13)))
        check("rule:all14_moments", all(sum((w*x**k for w, x in zip(rule["weights"], rule["nodes"])), Q(0))
              == (Q(2, k+1) if k % 2 == 0 else 0) for k in range(14)))
        prior = Q(0)
        terms = []
        block_evidence = []
        data = INDEX.with_suffix("")
        eta = Q(1, 2**32)
        n = 224 if args.follow else run["samples_completed"]
        for index in range(n):
            if args.follow:
                while True:
                    run = decode(json.loads(INDEX.read_text()))
                    running = run["status"].startswith("RUNNING")
                    available = index < run["samples_completed"]
                    block_available = (index+1) % 4 != 0 or (index+1)//4 <= run["checkpoints_completed"]
                    if (available and (block_available or not running)) or not running:
                        break
                    time.sleep(1)
                if not available:
                    break
                artifact_paths = {Path(a["path"]).name: NOTEBOOK/a["path"] for a in run["artifacts"]}
            sample = saved_data(f"sample_{index:03d}")
            panel, j = divmod(index, 14)
            x, omega, A, u, denominator, h, v = (sample[k] for k in
                ("x", "omega", "A", "u", "denominator", "h", "weighted"))
            check(f"sample{index}:index_node_weight", sample["index"] == index
                  and x == panel+(1+rule["nodes"][j])/2
                  and omega == max(Q(0), min(Q(1), rule["weights"][j]/2)))
            check(f"sample{index}:A_integer_identity", polynomial_power(-x*x/256, 20, 8, A))
            check(f"sample{index}:u_integer_identity", polynomial_power(-x/16, 20, 3, u))
            check(f"sample{index}:denominator_range", denominator == 1-u**4 > Q(1, 512))
            check(f"sample{index}:combined_quotient", h*denominator == (A-u)*u)
            check(f"sample{index}:weight_product_range", v == omega*h and abs(h) < 7 and abs(v) < 7)
            if index == 21:
                legacy = load(HERE / "direct_positive_real_execution_1808/Ihat_sample_021.json")
                check("legacy_unused22:complete_exact_equality", all(legacy[k] == sample[k]
                      for k in ("index", "x", "omega", "A", "u", "denominator", "h")))
                report["legacy_unused22_algebraically_replayed_by_exact_equality"] = True
            check(f"sample{index}:operation_record", run["sample_records"][index]["index"] == index
                  and run["sample_records"][index]["operations"] == 108)
            terms.append(v)
            report["samples_replayed"] = index+1
            if (index+1) % 4 == 0 and (index+1)//4 <= run["checkpoints_completed"]:
                block = (index+1)//4
                saved = saved_data(f"checkpoint_{block:02d}")
                S = saved["input"]
                check(f"block{block}:exact_four_term_identity", saved["block"] == block
                      and saved["previous"] == prior and sum_identity([prior]+terms, S))
                # Closed form reproduces strict comparison ties at lower cells.
                coordinate = (S+2048)/(2*eta)
                ceil_coordinate = -((-coordinate.numerator)//coordinate.denominator)
                cell = max(0, ceil_coordinate-1)
                lo = Q(-2048)+cell*2*eta
                hi = lo+2*eta
                new = (lo+hi)/2
                check(f"block{block}:independent_cell_and_output", saved["lo"] == lo
                      and saved["hi"] == hi and saved["output"] == new)
                # All43 branch choices, including their exact strict comparison.
                left, right = Q(-2048), Q(2048)
                branch_checks = []
                for branch in saved["strict_upper_branches"]:
                    middle = (left+right)/2
                    decision = S.numerator*middle.denominator > middle.numerator*S.denominator
                    branch_checks.append(type(branch) is bool and branch == decision)
                    if branch:
                        left = middle
                    else:
                        right = middle
                check(f"block{block}:all43_strict_branches", len(branch_checks) == 43
                      and all(branch_checks) and left == lo and right == hi)
                check(f"block{block}:containment_radius_grid", -2048 < S < 2048
                      and lo <= S <= hi and hi-lo == 2*eta and abs(new-S) <= eta
                      and (new*2**32).denominator == 1 and abs(new) < 1568+56*eta)
                check(f"block{block}:operations", saved["operations"] == 131
                      and run["checkpoint_records"][block-1]["operations"] == 131)
                block_evidence.append({"block": block, "all_four_samples_replayed": True,
                    "all43_branches_replayed": True, "rounding_error_at_most": str(eta),
                    "output": str(new), "inductive_error_bound": str(block*eta)})
                prior = new
                terms = []
                report["checkpoints_replayed"] = block
            if (index+1) % 4 == 0:
                report["blocks"] = block_evidence
                save(report)
            if (index+1) % 28 == 0:
                print(f"Replayed samples {index+1}/{n}; checkpoints {report['checkpoints_replayed']}/56", flush=True)
        if args.follow:
            while run["status"].startswith("RUNNING"):
                time.sleep(1)
                run = decode(json.loads(INDEX.read_text()))
            run = load(INDEX)
            n = run["samples_completed"]
            artifact_paths = {Path(a["path"]).name: NOTEBOOK/a["path"] for a in run["artifacts"]}
            check("artifacts:final_unique_names", len(artifact_paths) == len(run["artifacts"]))
            for item in run["artifacts"]:
                path = NOTEBOOK/item["path"]
                check("final_artifact_hash:"+path.name,
                      hashlib.sha256(path.read_bytes()).hexdigest() == item["sha256"]
                      and path.stat().st_size == item["bytes"])
        check("execution:finished_process", not run["status"].startswith("RUNNING"))
        # Validate partial evidence even when execution stopped within a block.
        partial_path = data / "partial.json"
        if partial_path.exists():
            check("partial:hash", hashlib.sha256(partial_path.read_bytes()).hexdigest() == run["partial_sha256"])
            partial = load(partial_path)
            # partial.json is written before the most recent conversion.
            last_block = n//4
            if n % 4 == 0 and last_block <= run["checkpoints_completed"]:
                last = saved_data(f"checkpoint_{last_block:02d}")
                check("partial:before_last_conversion", partial["value"] == last["input"]
                      and partial["last_completed_rounded"] == last["previous"])
            else:
                check("partial:integer_sum", sum_identity([prior]+terms, partial["value"]))
            check("partial:sample_count", partial["samples_completed"] == n)
        if n == 224 and run["checkpoints_completed"] == 56:
            final = saved_data("Ihat")
            check("final:value_and_error", final["value"] == prior and run["rounded_Ihat"] == str(prior)
                  and final["additional_error_from_original_exact_sum"] == 56*eta)
            check("final:all_records", len(run["sample_records"]) == 224
                  and len(run["checkpoint_records"]) == 56 and len(block_evidence) == 56)
            breakdown = run.get("prescribed_complete_scope_operation_breakdown",
                                run.get("executed_scope_operation_breakdown"))
            check("cost:prescribed_complete_scope", breakdown == {
                "unit_maps_and_weight_clamps": 1134, "samples_and_weighted_additions": 24192,
                "shared_negation_and_conversions": 7337}
                and sum(breakdown.values()) == 32663)
            reused = run.get("reused_completed_samples", 0)
            segment_operations = 15+113*(224-reused)+131*(56-reused//4)
            generated, converted = 224-reused, 56-reused//4
            expected_categories = {"add": 43*generated+44*converted,
                "multiply": 56*generated, "subtract": 2*generated,
                "divide": 14+4*generated+44*converted,
                "negate": 1+2*generated, "compare": 6*generated+43*converted}
            check("cost:all_measured_categories", run["executed_operation_counts"] == expected_categories)
            check("cost:measured_segment", sum(run["executed_operation_counts"].values())
                  == run["executed_operation_total"] == segment_operations)
            if "continuation_from" in run:
                previous_path = NOTEBOOK/run["continuation_from"]
                previous = load(previous_path)
                check("continuation:previous_hash", hashes[str(previous_path.relative_to(NOTEBOOK))]
                      == run["continuation_sha256"])
                prefix_operations = 15+113*reused+131*(reused//4)
                check("continuation:accounting", reused == 4*run["reused_completed_checkpoints"]
                      and run["inherited_prefix_required_operations"] == prefix_operations
                      and run["previous_segment_executed_operations"] == previous["executed_operation_total"]
                      and run["previous_segment_abandoned_operations"]
                           == previous["executed_operation_total"]-prefix_operations >= 0
                      and run["all_segments_measured_operations"]
                           == previous["executed_operation_total"]+segment_operations)
                report["all_segments_measured_operations"] = run["all_segments_measured_operations"]
                report["abandoned_segment_operations"] = run["previous_segment_abandoned_operations"]
            check("cost:full_ledger_not_execution", run["inherited_full_ledger"] == 997104 <= 1000000
                  and run["full_execution_count_verified"] is False and run["scalars_evaluated"] == 0)
            report["status"] = "PASS_COMPLETE_IHAT_ONLY"
            report["rounded_Ihat"] = str(prior)
            report["prescribed_complete_scope_operations"] = 32663
            report["current_segment_measured_operations"] = segment_operations
        else:
            report["status"] = "PASS_SAVED_IHAT_PREFIX_ONLY"
        report["limits"] = ["Error bound imports audited1810/1812 induction; no exact224-term unrounded total computed",
            "No scalar, full evaluator count, bit-cost theorem or analytic/source verification",
            "Legacy1808 unused22nd sample replayed by complete equality to independently checked fresh sample if reached"]
    except KeyboardInterrupt:
        report["status"] = "INTERRUPTED_SAVED_PREFIX_ONLY"
        raise
    except Exception as exc:
        report["status"] = "REPLAY_FAILED"
        report["exception"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        save(report)
        print(f"{report['status']}: {len(checks)} checks; failures {[k for k, v in checks.items() if not v]}")
        print(f"Samples {report['samples_replayed']}/224; checkpoints {report['checkpoints_replayed']}/56; scalar certificates0")
        if report["status"] == "PASS_COMPLETE_IHAT_ONLY":
            print(f"Rounded Ihat: {report['rounded_Ihat']}; extra error <=7/536870912, per-checkpoint <=1/4294967296")
            print(f"Prescribed Ihat path32663; current measured segment {report['current_segment_measured_operations']}; full997104 <=1000000 remains inherited")
        print(f"Certificate: {OUT.relative_to(NOTEBOOK)}")


if __name__ == "__main__":
    main()
