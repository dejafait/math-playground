"""Replay complete saved1816 stages without importing its evaluator.

Integer Taylor identities replace Horner; dyadic-cell/root inequalities
replace root iteration. Each saved fixed-core prefix is checked by an
integer common-denominator identity. GMP accelerates verifier gcd only.
No partial execution certifies a scalar or the full evaluator cost.
"""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import math
import signal
import time

from direct_positive_real_ihat_integer_backend_1814 import enable

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parent.parent
INDEX = HERE/"direct_positive_real_remaining_execution_1816.json"
OUT = HERE/"direct_positive_real_remaining_replay_1816.json"
DATA = HERE/"direct_positive_real_remaining_execution_1816"
OLD = HERE/"direct_positive_real_execution_1808"
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
        raise ArithmeticError("First failed check: "+name)


def save(report):
    report.update({"checks": checks, "check_count": len(checks),
        "failures": [k for k, v in checks.items() if not v],
        "inputs_sha256": hashes, "elapsed_seconds": round(time.monotonic()-started, 3)})
    temp = OUT.with_suffix(".tmp")
    temp.write_text(json.dumps(report, indent=2)+"\n")
    temp.replace(OUT)


def sum_matches(values, expected):
    den = 1
    for v in values:
        den = den//math.gcd(den, v.denominator)*v.denominator
    num = sum(v.numerator*(den//v.denominator) for v in values)
    return num*expected.denominator == expected.numerator*den


def polynomial(coefficients, x):
    # Independent direct powers, rather than the evaluator's Horner loop.
    return sum((c*x**k for k, c in enumerate(coefficients)), Q(0))


def taylor_power_matches(z, degree, squarings, expected, clamped=False):
    n, d = z.numerator, z.denominator
    fac = factorial(degree)
    den = fac*d**degree
    num = sum(n**k*d**(degree-k)*(fac//factorial(k)) for k in range(degree+1))
    if clamped:
        num = max(0, min(den, num))
    p = 2**squarings
    return num**p*expected.denominator == expected.numerator*den**p


def root_cell(w, midpoint, left, right):
    half = (right-left)/2**65
    lo, hi = midpoint-half, midpoint+half
    coordinate = (midpoint-left)/(right-left)*2**65
    return (coordinate.denominator == 1 and coordinate.numerator % 2 == 1
        and left <= lo < hi <= right and w*lo*lo <= 1 <= w*hi*hi)


def main():
    if OUT.exists():
        raise SystemExit("Preserve replay evidence: refuses to overwrite1816")
    backend = enable()
    run = load(INDEX)
    report = {"status": "REPLAY_IN_PROGRESS", "backend": backend,
        "fixed_summands_replayed": 0, "outer_inputs_replayed": 0,
        "outer_factors_replayed": 0, "artifacts_replayed": [],
        "scalars_certified": 0, "full_evaluator_count_verified": False,
        "limitations": ["Complete saved prefix only; absent profiles/scalars not certified",
            "Inherited997104 remains an upper ledger, not a measured completed run",
            "No source-wide/zero-data, interpolation, TV, bit-cost or Xi assertion"]}

    class Limit(Exception):
        pass

    def timeout(_signum, _frame):
        raise Limit()

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(300)
    try:
        check("executor_stopped", not run["status"].startswith("RUNNING"))
        for path, digest in run["inputs_sha256"].items():
            check("input_hash:"+path, hashlib.sha256((NOTEBOOK/path).read_bytes()).hexdigest() == digest)
        for item in run["artifacts"]:
            check("artifact_hash:"+item["path"],
                hashlib.sha256((NOTEBOOK/item["path"]).read_bytes()).hexdigest() == item["sha256"])
        check("executor_hash", hashlib.sha256((HERE/"direct_positive_real_remaining_execution_1816.py").read_bytes()).hexdigest() == run["executor_sha256"])
        check("inherited_ledger_not_completed_cost", run["inherited_full_operation_upper"] == 997104
            and run["required_operation_cap"] == 1000000 and not run["actual_complete_operation_count_verified"])
        ihat = Q(run["reused_Ihat"])
        check("Ihat_reuse", ihat == Q(-1252177417, 4294967296))
        constants = load(DATA/"constants.json")
        ell, pi, p, gamma, clog, K = [constants[k] for k in ("ell", "pi", "p", "gamma", "clog", "K")]
        check("ell_integer_sum", sum_matches([Q(2, 3**(2*j+1)*(2*j+1)) for j in range(64)], ell))
        pi_terms = [Q(16*(-1)**j, (2*j+1)*5**(2*j+1))
                    - Q(4*(-1)**j, (2*j+1)*239**(2*j+1)) for j in range(32)]
        check("pi_integer_sum", sum_matches(pi_terms, pi))
        half = Q(1, 2**65)
        check("sqrt_pi_dyadic_cell", (p*2**65).denominator == 1 and (p*2**65).numerator % 2 == 1
            and 1 <= p-half < p+half <= 2 and (p-half)**2 <= pi <= (p+half)**2)
        check("gamma_integer_sum", sum_matches([Q(1, k) for k in range(1, 4097)], gamma+12*ell+Q(1,8192)))
        z = (pi-4)/(pi+4)
        check("log4pi_direct_series", sum_matches([Q(2,2*j+1)*z**(2*j+1) for j in range(16)], clog-4*ell))
        check("K_identity", 4*pi*K == clog+gamma+2*ihat)
        report["artifacts_replayed"].append("constants.json")
        save(report)

        primes = load(DATA/"prime_constants.json")
        expected_powers = {2:2,3:3,4:2,5:5,7:7,8:2,9:3,11:11,13:13,16:2,
                           17:17,19:19,23:23,25:5,27:3,29:29,31:31,32:2}
        check("all18_prime_powers", {int(n):int(v) for n,v in primes["powers"].items()} == expected_powers)
        for n, prime in expected_powers.items():
            k = n.bit_length()-1
            z = Q(n-2**k, n+2**k)
            logn = primes["logs"][str(n)]
            check(f"log{n}_integer_sum", sum_matches([Q(2,2*j+1)*z**(2*j+1) for j in range(32)], logn-k*ell))
            check(f"log{n}_square", primes["log_squares"][str(n)] == logn*logn)
            inv = primes["coefficients"][str(n)]/primes["logs"][str(prime)]
            check(f"inverse_root{n}_cell", root_cell(Q(n), inv, Q(0), Q(1)))
        schedules = primes["schedules"]
        check("all60_schedules", len(schedules) == 60 and
            {(row["panel"],row["sigma"]) for row in schedules} ==
            {(j,s) for j in range(20) for s in (Q(1),Q(3,2),Q(2))})
        for row in schedules:
            panel, sigma = row["panel"], row["sigma"]
            exponent = (Q(28)-Q(7*(panel+1),5)).__floor__()
            lower = sigma+Q(2)**exponent
            check(f"schedule{panel}_{sigma}:lower", row["lower_exponent"] == exponent and row["lower_width"] == lower)
            kept = {n for n in expected_powers if lower*primes["log_squares"][str(n)] < 32}
            check(f"schedule{panel}_{sigma}:complete_partition", set(row["retained"]) == kept
                and set(row["suppressed"]) == set(expected_powers)-kept)
        report["artifacts_replayed"].append("prime_constants.json")
        save(report)

        inner = load(OLD/"inner_nodes.json")["nodes_and_weights"]
        aa = load(OLD/"moment_inputs.json")["a"]
        terms = []
        fixed_paths = sorted(DATA.glob("fixed_sample_*.json"))
        for j, path in enumerate(fixed_paths):
            record = load(path)
            x, a = inner[j][0], aa[j]
            check(f"fixed{j}:input", record["index"] == j and record["x"] == x and record["a"] == a)
            e = polynomial([Q(1,2**k*factorial(k)) for k in range(1,17)], x)
            t = sum((x**(2*k-1)/factorial(2*k+1) for k in range(1,11)), Q(0))
            check(f"fixed{j}:quotient_identity", record["quotient"]*2*(1+x*t) == e-t)
            check(f"fixed{j}:term_identity", record["term"] == a*record["quotient"])
            terms.append(record["term"])
            partial_path = DATA/f"fixed_partial_{j+1:02d}.json"
            if partial_path.exists():
                partial = load(partial_path)
                check(f"fixed{j}:complete_prefix_sum", partial["summands_completed"] == j+1
                    and sum_matches(terms, partial["value"]))
                report["fixed_summands_replayed"] = j+1
                report["artifacts_replayed"].append(partial_path.name)
            report["artifacts_replayed"].append(path.name)
            save(report)
        check("fixed_completed_count", report["fixed_summands_replayed"] == run["fixed_summands_completed"])

        if (DATA/"shared_core.json").exists():
            core = load(DATA/"shared_core.json")
            check("shared_fixed_value", len(terms) == 48 and sum_matches(terms, core["fixed"]))
            cc = core["coefficients"]
            check("all29_core_coefficients", len(cc) == 29 and len(core["d"]) == 29)
            for n in range(29):
                rhs = Q(1,2**(n+1)*factorial(n+1))-(Q(1,factorial(n+2)) if n % 2 else 0)
                check(f"coefficient{n}:defining_identity", sum_matches(
                    [2*cc[n-2*j]/factorial(2*j+1) for j in range(n//2+1)], rhs))
                moment = load(OLD/f"moment_{n:02d}.json")["value"]
                check(f"coefficient{n}:moment_product", core["d"][n] == cc[n]*moment)
            report["artifacts_replayed"].append("shared_core.json")
            save(report)

        roots = load(OLD/"reference_rules.json")["rules"][1]
        for path in sorted(DATA.glob("outer_inputs_*.json")):
            data = load(path)
            panel,j = data["panel"],data["node"]
            v = ell*(30-Q(7*panel,5)-Q(7,10)*(1+roots["nodes"][j]))
            v = max(Q(0),min(Q(21),v))
            check(f"outer{panel}_{j}:v", data["v"] == v)
            check(f"outer{panel}_{j}:E_integer_T40_power", taylor_power_matches(v/32,40,5,data["E"]))
            check(f"outer{panel}_{j}:t", data["t"] == max(Q(0),min(Q(1,4),1/data["E"])))
            check(f"outer{panel}_{j}:r_integer_T20_power", taylor_power_matches(v/64,20,5,data["r"]))
            report["outer_inputs_replayed"] += 1
            report["artifacts_replayed"].append(path.name)
            factors_path = DATA/path.name.replace("outer_inputs", "outer_factors")
            if factors_path.exists():
                factors = load(factors_path)
                weight = Q(7,10)*ell*max(Q(0),min(Q(2),roots["weights"][j]))
                for s in (1,2):
                    # Recover u from the recorded g, then verify its entire
                    # Taylor numerator without the executor's Horner calls.
                    g = factors["g"][str(s)]
                    u = 1-g/(p*data["r"])
                    check(f"outer{panel}_{j}:u{s}_integer_T20", taylor_power_matches(-s*data["t"],20,0,u,True))
                    check(f"outer{panel}_{j}:weight_g{s}", factors["weighted_g"][str(s)] == weight*g)
                report["outer_factors_replayed"] += 1
                report["artifacts_replayed"].append(factors_path.name)
            save(report)

        # Refuse to call a prefix complete if a later artifact needs more replay.
        all_files = {Path(item["path"]).name for item in run["artifacts"]}
        check("all_saved_constructor_artifacts_replayed", all_files == set(report["artifacts_replayed"]))
        check("no_absent_scalar_claim", run["profiles_evaluated"] == 0 and run["scalars_evaluated"] == 0)
        report["status"] = "PASS_COMPLETE_SAVED_PREFIX_ONLY"
    except Limit:
        signal.alarm(0)
        report["status"] = "TIME_LIMIT_SAVED_REPLAY_PREFIX_ONLY"
    except Exception as exc:
        signal.alarm(0)
        report["status"] = "REPLAY_ERROR_SAVED_PREFIX_ONLY"
        report["error"] = f"{type(exc).__name__}: {exc}"
        raise
    finally:
        signal.alarm(0)
        save(report)
        print(f"Replay: {report['status']}; checks{len(checks)}; failures{report['failures']}")
        print(f"Fixed sums {report['fixed_summands_replayed']}/48; outer inputs{report['outer_inputs_replayed']}; scalars certified0/8")
        print(f"Radius<1/256 and full cost<=1000000 NOT ESTABLISHED; certificate: {OUT.relative_to(NOTEBOOK)}")


if __name__ == "__main__":
    main()
