"""Continue1808's saved exact prefix through the prescribed scalar constructors.

This implements the existing C033z formulas only. An interrupted run retains
all completed exact values; the inherited analytic bound certifies no scalar
until its complete exponent and final exponential have been evaluated.
"""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
import argparse
import hashlib
import json
import signal
import time

from direct_positive_real_execution_1808 import (
    ROOT, OUT, SUMMARY, write_json, bits, horner, power2, clamp, rule, Deadline,
)
from direct_positive_real_inputs_1802 import legendre_polynomials

RESULT = ROOT / "direct_positive_real_execution_remaining_1808.json"


def decode(value):
    if isinstance(value, dict):
        if set(value) == {"numerator_hex", "denominator_hex"}:
            return F(int(value["numerator_hex"], 16), int(value["denominator_hex"], 16))
        return {k: decode(v) for k, v in value.items()}
    if isinstance(value, list):
        return [decode(v) for v in value]
    return value


def read(name):
    return decode(json.loads((OUT / (name+".json")).read_text()))


def inverse_root(w):
    lo, hi = F(0), F(1)
    for _ in range(64):
        mid = (lo+hi)/2
        if w*mid*mid > 1:
            hi = mid
        else:
            lo = mid
    return (lo+hi)/2


def atanh_series(z, coefficients):
    return z*horner(coefficients, z*z)


def quotient(z, ecoeff, ucoeff):
    t = z*horner(ucoeff, z*z)
    return (horner(ecoeff, z)-t)/(2*(1+z*t))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=int, default=180)
    args = parser.parse_args()
    if RESULT.exists():
        raise SystemExit("Existing remaining1808 evidence preserved; use a distinct run ID")
    initial = json.loads(SUMMARY.read_text())
    assert initial["gaussian_inputs_completed"] == 48 and initial["moments_completed"] == 29
    started = time.monotonic()
    report = {"status": "RUNNING_REMAINING_EXACT_CONSTRUCTORS",
        "prefix_certificate": str(SUMMARY.relative_to(ROOT.parent.parent)),
        "time_limit_seconds": args.seconds, "scalars_evaluated": 0,
        "profiles_evaluated": 0, "Ihat_samples_completed": 0,
        "Ihat_records": [], "artifacts": [], "failures": [],
        "pending": "P14 rule", "required_scalar_radius": "1/256",
        "prescribed_complete_operation_upper": 989767, "required_operation_cap": 1000000,
        "actual_complete_operation_count_verified": False,
        "limitations": ["Exact Python Fraction; no rounded/alternative evaluator",
                        "Prescribed989767 ledger is not independently instrumented code cost",
                        "All analytic/source/finite-zero assumptions remain qualified",
                        "Input-only data or a partial Ihat sum certify no scalar"]}

    def checkpoint():
        report["elapsed_seconds"] = round(time.monotonic()-started, 3)
        write_json(RESULT, report)

    def pending(text):
        report["pending"] = text
        checkpoint()

    def save(name, value):
        path = OUT / (name+".json")
        write_json(path, value)
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
        polys = legendre_polynomials()
        n = 13
        a, b = polys[-1], polys[-2]
        p14 = [((2*n+1)*(a[k-1] if 1 <= k <= len(a) else 0)
                - n*(b[k] if k < len(b) else 0))/(n+1) for k in range(n+2)]
        r14 = rule(p14, 14)
        save("reference_rule14", r14)
        tcoeff = read("inner_nodes")["taylor_coefficients_ascending"]
        Ihat = F(0)
        for panel in range(16):
            for j, (root, weight) in enumerate(zip(r14["nodes"], r14["weights"])):
                index = panel*14+j
                x = panel+(1+root)/2
                omega = clamp(weight/2)
                tick = time.monotonic()
                pending(f"Ihat sample {index+1}/224: Ahat polynomial/power")
                A = power2(clamp(horner(tcoeff[:21], -(x*x)/256)), 8)
                pending(f"Ihat sample {index+1}/224: uhat polynomial/power")
                u = power2(clamp(horner(tcoeff[:21], -x/16)), 3)
                pending(f"Ihat sample {index+1}/224: denominator and combined quotient")
                denominator = 1-power2(u, 2)
                assert denominator > F(1, 512)
                h = ((A-u)*u)/denominator
                save(f"Ihat_sample_{index:03d}", {"index": index, "x": x,
                    "omega": omega, "A": A, "u": u, "denominator": denominator,
                    "h": h, "constructor": "C033z(19)"})
                pending(f"Ihat weighted accumulation {index+1}/224")
                Ihat += omega*h
                write_json(OUT / "Ihat_partial.json", {"summands_completed": index+1, "value": Ihat})
                report["Ihat_samples_completed"] = index+1
                report["Ihat_records"].append({"index": index, "h_bits": bits(h),
                    "sum_bits": bits(Ihat), "seconds": round(time.monotonic()-tick, 6)})
                checkpoint()
        save("Ihat", {"value": Ihat, "proved_error_from_exact_finite_rule": "<2^-30"})
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
        primes = [n for n in range(2, 33) if all(n % d for d in range(2, n))]
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
        save("prime_constants", {"powers": powers, "logs": logs, "coefficients": prime_coeff})
        inner = read("inner_nodes")["nodes_and_weights"]
        a = read("moment_inputs")["a"]
        ecoeff = [F(1, 2**k*factorial(k)) for k in range(1, 17)]
        ucoeff = [F(1, factorial(2*j+1)) for j in range(1, 11)]
        fixed = F(0)
        for j, ((x, _), aj) in enumerate(zip(inner, a)):
            pending(f"Fixed Jhat(1) quotient {j+1}/48")
            fixed += aj*quotient(x, ecoeff, ucoeff)
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
                g = {s: p*r*(1-clamp(horner(tcoeff[:21], -s*t))) for s in (1, 2)}
                weighted_g = {s: outer_weights[j]*g[s] for s in (1, 2)}
                for sigma in sigmas:
                    pending(f"Profile panel{panel+1}/20 node{j+1}/13 width{sigma}")
                    w = sigma+E/4
                    q = clamp(inverse_root(w), F(0), F(1, 4) if panel < 17 else F(1))
                    if panel < 17:
                        J = q*horner(d, 4*q)
                    else:
                        J = q*sum((aj*quotient(x*q, ecoeff, ucoeff)
                                   for (x, _), aj in zip(inner, a)), F(0))
                    D = J-fixed
                    psum = F(0)
                    lower = sigma+F(2)**lower_exponent
                    for n in powers:
                        if lower*log_squares[n] >= 32:
                            continue
                        arg = w*log_squares[n]
                        if arg < 32:
                            psum += prime_coeff[n]*power2(clamp(horner(tcoeff[:21], -arg/32)), 5)
                    x = 4*sigma*t
                    logw = v-2*ell+atanh_series(x/(2+x), ac[:16])
                    pole = q*horner(tcoeff[:11], q*q/16)/(2*p)
                    profile = pole-K+logw/(8*pi)-D/(2*pi)-psum/(2*pi)
                    for s in (1, 2):
                        exponents[s, sigma] += weighted_g[s]*profile
                    report["profiles_evaluated"] += 1
                    save(f"profile_{panel*13+j:03d}_{str(sigma).replace('/', '_')}",
                         {"w": w, "q": q, "profile": profile})
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
        report["status"] = "TIME_LIMIT_EXACT_CONSTRUCTORS_INCOMPLETE"
        report["failures"].append("Bounded exact execution incomplete; scalar radius not established")
    except Exception as exc:
        signal.alarm(0)
        report["status"] = "EXECUTION_ERROR_INCOMPLETE"
        report["failures"].append(f"{type(exc).__name__}: {exc}")
        raise
    finally:
        signal.alarm(0)
        path = OUT / "Ihat_partial.json"
        if path.exists():
            report["latest_partial_artifact"] = {
                "path": str(path.relative_to(ROOT.parent.parent)),
                "bytes": path.stat().st_size,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
        checkpoint()
        print(f"Status: {report['status']}; Ihat sums {report['Ihat_samples_completed']}/224; profiles {report['profiles_evaluated']}/780; scalars {report['scalars_evaluated']}/8")
        print("Required scalar radius <1/256 and complete-run cost <=1000000: NOT ESTABLISHED")
        print(f"Pending: {report['pending']}; failures: {report['failures']}")
        print(f"Certificate: {RESULT.relative_to(ROOT.parent.parent)}")


if __name__ == "__main__":
    main()
