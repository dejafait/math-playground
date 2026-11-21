"""Bounded remaining C033y/z execution1816, exact except reused Ihat1814.

The tail is copied from the preserved1808 formula driver, with additional
checkpoints only. All old data are read-only. The inherited997104 upper
ledger is not a measured completed evaluator count; no partial prefix is a
scalar enclosure. Both error allowances and separate residual targets remain.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import signal
import time

from direct_positive_real_execution_1808 import write_json, bits, horner, power2, clamp, Deadline
from direct_positive_real_execution_remaining_1808 import decode, inverse_root, atanh_series, quotient

ROOT=Path(__file__).resolve().parent
NOTEBOOK=ROOT.parent.parent
INPUT=ROOT/"direct_positive_real_execution_1808"
OUT=ROOT/"direct_positive_real_remaining_execution_1816"
RESULT=ROOT/"direct_positive_real_remaining_execution_1816.json"
IHAT=ROOT/"direct_positive_real_ihat_execution_1814c.json"
REPLAY=ROOT/"direct_positive_real_ihat_replay_1814fast.json"


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=300)
    args=parser.parse_args()
    if RESULT.exists() or OUT.exists():
        raise SystemExit("Preserve evidence: refuses to overwrite1816")
    OUT.mkdir()
    started=time.monotonic()
    report={"status":"RUNNING_REMAINING_CONSTRUCTORS", "time_limit_seconds":args.seconds,
        "assessment":"drafts/literature/2026-11-19-direct-positive-real-post-ihat-scalar-execution-review-1814.md",
        "scalars_evaluated":0, "profiles_evaluated":0, "fixed_summands_completed":0,
        "artifacts":[], "inputs_sha256":{}, "failures":[], "pending":"reused Ihat/replay",
        "arithmetic":"Exact Python Fraction; only Ihat uses the already replayed prescribed rounding",
        "required_scalar_radius":"1/256", "inherited_full_operation_upper":997104,
        "required_operation_cap":1000000, "actual_complete_operation_count_verified":False,
        "reserved_exponent_allowance":"1/1024", "reserved_final_exponential_allowance":"1/1024",
        "unresolved":["No scalar/error/cap assertion before full saved evidence and independent replay",
            "Reused constructors remain charged in997104; no measured full evaluator cost",
            "No source-wide/zero-data validity, bit-cost, interpolation, TV or actual-Xi claim"]}

    def checkpoint():
        report["elapsed_seconds"]=round(time.monotonic()-started,3)
        write_json(RESULT,report)

    def load(path):
        raw=path.read_bytes()
        report["inputs_sha256"][str(path.relative_to(NOTEBOOK))]=hashlib.sha256(raw).hexdigest()
        return decode(json.loads(raw))

    def read(name):
        return load(INPUT/(name+".json"))

    def save(name,value):
        path=OUT/(name+".json")
        write_json(path,value)
        report["artifacts"].append({"path":str(path.relative_to(NOTEBOOK)),
            "bytes":path.stat().st_size,"sha256":hashlib.sha256(path.read_bytes()).hexdigest()})
        report["last_completed_artifact"]=str(path.relative_to(NOTEBOOK))
        checkpoint()

    def pending(value):
        report["pending"]=value
        checkpoint()

    def timeout(_signum,_frame):
        raise Deadline()

    # Reject an incompatible input; these are validation, not evaluator work.
    old=load(IHAT)
    replay=load(REPLAY)
    assert old["status"]=="IHAT_EXECUTION_COMPLETE_REPLAY_REQUIRED"
    assert replay["status"]=="PASS_COMPLETE_IHAT_ONLY" and not replay["failures"]
    Ihat=F(old["rounded_Ihat"])
    assert Ihat==F(-1252177417,4294967296)
    report["reused_Ihat"]=str(Ihat)
    report["reuse_accounting"]={"Ihat_required_path_measured":32663,
        "Ihat_abandoned_block":452,"Ihat_repeated_setup":15,
        "Ihat_actual_historical_kernel":33130,
        "scope":"Historical Ihat kernel only; rule/coefficient generation, verification and full scalar cost unmeasured"}
    report["executor_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report["formula_driver_sha256"]=hashlib.sha256((ROOT/"direct_positive_real_execution_remaining_1808.py").read_bytes()).hexdigest()
    signal.signal(signal.SIGALRM,timeout)
    signal.alarm(args.seconds)
    checkpoint()
    try:
        pending("Shared constants")
        ell = 2*sum((F(1, 3**(2*j+1)*(2*j+1)) for j in range(64)), F(0))
        atan = lambda base: sum((F((-1)**j, (2*j+1)*base**(2*j+1)) for j in range(32)), F(0))
        pi = 16*atan(5)-4*atan(239)
        lo, hi = F(1), F(2)
        for _ in range(64):
            mid = (lo+hi)/2
            if mid*mid > pi:
                hi = mid
            else:
                lo = mid
        p = (lo+hi)/2
        gamma = sum((F(1, k) for k in range(1, 4097)), F(0))-12*ell-F(1, 8192)
        ac = [F(2, 2*j+1) for j in range(32)]
        clog = 4*ell+atanh_series((pi-4)/(pi+4), ac[:16])
        K = (clog+gamma+2*Ihat)/(4*pi)
        save("constants", {"ell": ell, "pi": pi, "p": p, "gamma": gamma, "clog": clog, "K": K})
        pending("Prime powers, logarithms and suppression schedule")
        # Fixed finite sieve, rather than trial integer remainders.
        marked = [False]*33
        primes = []
        for n in range(2, 33):
            if not marked[n]:
                primes.append(n)
                multiple = n+n
                while multiple <= 32:
                    marked[multiple] = True
                    multiple += n
        powers = {}
        for prime in primes:
            n = prime
            while n <= 32:
                powers[n] = prime
                n *= prime
        logs = {}
        for n in powers:
            k = n.bit_length()-1
            logs[n] = k*ell+atanh_series(F(n-2**k, n+2**k), ac)
        prime_coeff = {n: logs[prime]*inverse_root(F(n)) for n, prime in powers.items()}
        log_squares = {n: value*value for n, value in logs.items()}
        schedules = []
        for panel in range(20):
            lower_exponent = (F(28)-F(7*(panel+1), 5)).__floor__()
            for sigma in (F(1), F(3, 2), F(2)):
                lower = sigma+F(2)**lower_exponent
                retained, suppressed = [], []
                for n in powers:
                    (suppressed if lower*log_squares[n] >= 32 else retained).append(n)
                schedules.append({"panel": panel, "sigma": sigma, "lower_exponent": lower_exponent,
                    "lower_width": lower, "retained": retained, "suppressed": suppressed})
        save("prime_constants", {"powers": powers, "logs": logs, "coefficients": prime_coeff,
            "log_squares": log_squares, "schedules": schedules})
        inner = read("inner_nodes")["nodes_and_weights"]
        tcoeff = read("inner_nodes")["taylor_coefficients_ascending"]
        a = read("moment_inputs")["a"]
        ecoeff = [F(1, 2**k*factorial(k)) for k in range(1, 17)]
        ucoeff = [F(1, factorial(2*j+1)) for j in range(1, 11)]
        fixed = F(0)
        for j, ((x, _), aj) in enumerate(zip(inner, a)):
            pending(f"Fixed Jhat(1) quotient {j+1}/48")
            value = quotient(x, ecoeff, ucoeff)
            term = aj*value
            save(f"fixed_sample_{j:02d}", {"index": j, "x": x, "a": aj, "quotient": value, "term": term})
            pending(f"Fixed Jhat(1) weighted addition {j+1}/48")
            fixed += term
            save(f"fixed_partial_{j+1:02d}", {"summands_completed": j+1, "value": fixed})
            report["fixed_summands_completed"] = j+1
            checkpoint()
        c = []
        for n in range(29):
            an = F(1, 2**(n+1)*factorial(n+1))
            if n % 2:
                an -= F(1, factorial(n+2))
            c.append(an/2-sum((c[n-2*j]/factorial(2*j+1) for j in range(1, n//2+1)), F(0)))
        d = [ck*read(f"moment_{k:02d}")["value"] for k, ck in enumerate(c)]
        save("shared_core", {"fixed": fixed, "coefficients": c, "d": d})
        r13 = read("reference_rules")["rules"][1]
        outer_weights = [(7*ell/10)*clamp(w, F(0), F(2)) for w in r13["weights"]]
        sigmas = (F(1), F(3, 2), F(2))
        exponents = {(s, sigma): F(0) for s in (1, 2) for sigma in sigmas}
        for panel in range(20):
            lower_exponent = (F(28)-F(7*(panel+1), 5)).__floor__()
            for j, root in enumerate(r13["nodes"]):
                pending(f"Outer inputs panel{panel+1}/20 node{j+1}/13")
                v = clamp(ell*(30-F(7*panel, 5)-F(7, 10)*(1+root)), F(0), F(21))
                E = power2(horner(tcoeff, v/32), 5)
                t = clamp(1/E, F(0), F(1, 4))
                r = power2(horner(tcoeff[:21], v/64), 5)
                save(f"outer_inputs_{panel*13+j:03d}", {"panel": panel, "node": j, "v": v, "E": E, "t": t, "r": r})
                pending(f"Outer g factors panel{panel+1}/20 node{j+1}/13")
                g = {s: p*r*(1-clamp(horner(tcoeff[:21], -s*t))) for s in (1, 2)}
                weighted_g = {s: outer_weights[j]*g[s] for s in (1, 2)}
                save(f"outer_factors_{panel*13+j:03d}", {"g": g, "weighted_g": weighted_g})
                for sigma in sigmas:
                    pending(f"Profile panel{panel+1}/20 node{j+1}/13 width{sigma}")
                    w = sigma+E/4
                    q = clamp(inverse_root(w), F(0), F(1, 4) if panel < 17 else F(1))
                    if panel < 17:
                        J = q*horner(d, 4*q)
                    else:
                        J = q*sum((aj*quotient(x*q, ecoeff, ucoeff)
                                   for (x, _), aj in zip(inner, a)), F(0))
                    save(f"core_{panel*13+j:03d}_{str(sigma).replace('/', '_')}", {"w": w, "q": q, "J": J})
                    pending(f"Prime/profile assembly panel{panel+1}/20 node{j+1}/13 width{sigma}")
                    D = J-fixed
                    psum = F(0)
                    selected = next(row["retained"] for row in schedules
                                    if row["panel"] == panel and row["sigma"] == sigma)
                    for n in selected:
                        arg = w*log_squares[n]
                        if arg < 32:
                            psum += prime_coeff[n]*power2(clamp(horner(tcoeff[:21], -arg/32)), 5)
                    x = 4*sigma*t
                    logw = v-2*ell+atanh_series(x/(2+x), ac[:16])
                    save(f"logprime_{panel*13+j:03d}_{str(sigma).replace('/', '_')}", {"D": D, "prime_sum": psum, "logw": logw})
                    pole = q*horner(tcoeff[:11], q*q/16)/(2*p)
                    profile = pole-K+logw/(8*pi)-D/(2*pi)-psum/(2*pi)
                    for s in (1, 2):
                        exponents[s, sigma] += weighted_g[s]*profile
                    report["profiles_evaluated"] += 1
                    save(f"profile_{panel*13+j:03d}_{str(sigma).replace('/', '_')}",
                         {"w": w, "q": q, "profile": profile, "exponents": {str(key): value for key, value in exponents.items()}})
        final = []
        for label, s, sigma in ([(f"m({s})", s, F(1)) for s in (1, 2)]
                + [(f"k({s},{sigma})", s, sigma) for s in (1, 2) for sigma in sigmas]):
            pending(f"Final scalar {label}")
            X = clamp(exponents[s, sigma], F(0), F(128))
            scalar = power2(clamp(horner(tcoeff[:21], -X/128)), 7)
            final.append({"label": label, "center": scalar, "exponent": X})
            report["scalars_evaluated"] += 1
            save(f"scalar_{len(final)}", final[-1])
        report["status"] = "EIGHT_EXACT_CENTERS_COMPLETED_IMPLEMENTATION_COST_AUDIT_REQUIRED"
        report["pending"] = "Independent implementation replay/cost audit before any cap-certified enclosure claim"
    except Deadline:
        signal.alarm(0)
        report["status"]="TIME_LIMIT_EXACT_CONSTRUCTORS_INCOMPLETE"
        report["failures"].append("Operational time limit; no scalar radius or full evaluator cost established")
    except Exception as exc:
        signal.alarm(0)
        report["status"]="EXECUTION_ERROR_INCOMPLETE"
        report["failures"].append(f"{type(exc).__name__}: {exc}")
        raise
    finally:
        signal.alarm(0)
        checkpoint()
        print(f"Status: {report['status']}; fixed {report['fixed_summands_completed']}/48; profiles {report['profiles_evaluated']}/780; scalars {report['scalars_evaluated']}/8")
        print(f"Required scalar radius <1/256; full cost <=1000000: NOT ESTABLISHED")
        print(f"Inherited upper ledger997104; full measured count unverified; pending: {report['pending']}")
        print(f"Failures: {report['failures']}; certificate: {RESULT.relative_to(NOTEBOOK)}")


if __name__=="__main__":
    main()
