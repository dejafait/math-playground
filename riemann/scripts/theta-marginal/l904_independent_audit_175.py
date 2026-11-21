"""Audit the existing L904 grid, without changing mesh, domain or allocation.

Independent 90-digit interval evaluations check every saved cache and weight;
exact integer/Fraction accumulation checks every box. L037's Decimal and
interpreter contracts remain trusted. Complete evidence is saved separately.
"""
import hashlib
import json
from decimal import (Context, Decimal, ROUND_FLOOR, ROUND_CEILING,
                     ROUND_HALF_EVEN, DivisionByZero, InvalidOperation,
                     Overflow, Underflow, Subnormal)
from fractions import Fraction as F
from math import factorial
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
ORIGINAL = HERE / "equal-neighbor-budget-135-m32.json"
OUTPUT = HERE / "l904-independent-audit-175.json"
contexts = [Context(prec=90, rounding=r) for r in
            (ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN)]
down, up, near = contexts
for ctx in contexts:
    for sig in (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal):
        ctx.traps[sig] = True


def rat(x):
    x = F(x)
    n, d = Decimal(x.numerator), Decimal(x.denominator)
    return down.divide(n, d), up.divide(n, d)


def add(a, b):
    return down.add(a[0], b[0]), up.add(a[1], b[1])


def neg(a):
    return a[1].copy_negate(), a[0].copy_negate()


def mul(a, b):
    return (min(down.multiply(x, y) for x in a for y in b),
            max(up.multiply(x, y) for x in a for y in b))


def scale(a, x):
    return mul(a, rat(x))


def exp(a):
    return near.next_minus(near.exp(a[0])), near.next_plus(near.exp(a[1]))


def power(a, n):
    result = rat(1)
    for _ in range(n):
        result = mul(result, a)
    return result


def data(a):
    return dict(lower=str(a[0]), upper=str(a[1]))


def exact(v):
    return F(v["lower"]), F(v["upper"])


def fadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def fmul(a, b):
    p = [x*y for x in a for y in b]
    return min(p), max(p)


def fscale(a, x):
    return fmul(a, (F(x), F(x)))


def fdiv(a, b):
    if b[0] <= 0 <= b[1]:
        raise ArithmeticError("Zero in divisor")
    return fmul(a, (1/b[1], 1/b[0]))


def atan_bounds(d):
    terms = 110
    s = sum((F((-1)**k, (2*k+1)*d**(2*k+1)) for k in range(terms)), F(0))
    following = F((-1)**terms, (2*terms+1)*d**(2*terms+1))
    return min(s, s+following), max(s, s+following)


def fixed_sine(x, pi):
    turns = (F(x[0])/(2*F(pi[0])) + F(1, 2)) // 1
    r = add(x, neg(scale(pi, 2*turns)))
    radius = max(z.copy_abs() for z in r)
    if radius > 4:
        raise ArithmeticError("Taylor reduction outside approved radius")
    square = mul(r, r)
    value = rat(0)
    for j in range(24, -1, -1):
        value = add(mul(value, square), rat(F((-1)**j, factorial(2*j+1))))
    error = scale(power((radius, radius), 50), F(1, factorial(50)))[1]
    return add(mul(value, r), (error.copy_negate(), error))


def reflect(a, b):
    # Image of the whole integer-coordinate interval under absolute value.
    return (0 if a <= 0 <= b else min(abs(a), abs(b))), max(abs(a), abs(b))


def integer_endpoints(values):
    places = max(max(0, -Decimal(v[k]).as_tuple().exponent)
                 for v in values for k in ("lower", "upper"))
    den = 10**places
    converted = []
    for v in values:
        pair = [F(v[k])*den for k in ("lower", "upper")]
        if any(x.denominator != 1 for x in pair):
            raise ArithmeticError("Nonintegral decimal scaling")
        converted.append(tuple(x.numerator for x in pair))
    return den, converted


def main():
    cert = json.loads(ORIGINAL.read_text())
    checks, failures = {}, []
    evidence = {"kernel_boxes": {}, "cosine_weights": {}, "exact_reconstruction": {}}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)

    def contains(name, saved, interval, section=None):
        outer = exact(saved)
        inner = tuple(F(x) for x in interval)
        check(name, outer[0] <= inner[0] <= inner[1] <= outer[1])
        if section is not None:
            evidence[section][name] = {"saved": saved, "independent": data(interval)}

    check("fixed_parameters", all(cert[k] == v for k, v in {
        "mesh": 32, "t_cells": 1024, "q_cells": 160, "box_count": 163840,
        "precision": 70, "theta_terms": 4, "t_cutoff": "pi/2",
        "cell_sign_counts": {"positive": 96, "negative": 64}}.items()))
    a, b = atan_bounds(5), atan_bounds(239)
    pi = (rat(16*a[0]-4*b[1])[0], rat(16*a[1]-4*b[0])[1])
    h = scale(pi, F(1, 2048))
    contains("pi", cert["pi"], pi)
    contains("h", cert["h"], h)
    check("pi_between_3_and_4", 3 < pi[0] < pi[1] < 4)
    check("exp3_positive_series", sum((F(3**k, factorial(k)) for k in range(9)), F(0)) > 20)
    expected_keys = {(i, i+1) for i in range(1024)}
    for j in range(160):
        for i in range(1024):
            expected_keys.add((i+j, i+j+2))
            expected_keys.add(reflect(i-j-1, i-j+1))
    cache = cert["kernel_cache"]
    check("complete_cache_keys", set(cache) == {f"{a}:{b}" for a, b in expected_keys})
    for key, saved in cache.items():
        a, b = map(int, key.split(":"))
        u = (scale(h, a)[0], scale(h, b)[1])
        e2 = exp(scale(u, 2))
        total = rat(0)
        for n in range(1, 5):
            v = mul(scale(pi, n*n), e2)
            poly = add(mul(scale(v, 8), v), neg(scale(v, 12)))
            total = add(total, mul(poly, exp(neg(v))))
        value = mul(exp(scale(u, F(1, 2))), total)
        value = max(value[0], Decimal(0)), min(value[1], Decimal(16))
        check("kernel_cap_"+key, 0 <= F(saved["lower"]) <= F(saved["upper"]) <= 16)
        contains("kernel_"+key, saved, value, "kernel_boxes")

    sines = [fixed_sine(scale(pi, F(j, 64)), pi) for j in range(161)]
    for j, v in ((0, 0), (32, 1), (64, 0), (96, -1), (128, 0), (160, 1)):
        check("exact_sine_"+str(j), sines[j][0] <= v <= sines[j][1])
        sines[j] = rat(v)
    check("all_weights_present", len(cert["cosine_integrated_weights"]) == 160)
    for j, saved in enumerate(cert["cosine_integrated_weights"]):
        weight = scale(add(sines[j+1], neg(sines[j])), F(1, 16))
        contains("cosine_"+str(j), saved, weight, "cosine_weights")
        # Exact phase cell [j*pi/64,(j+1)*pi/64] stays in its cosine lobe.
        check("cosine_sign_"+str(j), F(saved["upper"]) < 0 if 32 <= j < 96
              else F(saved["lower"]) > 0)

    kd, kv = integer_endpoints(list(cache.values()))
    ki = dict(zip(cache, kv))
    qd, qi = integer_endpoints(cert["cosine_integrated_weights"])
    accum = [[0, 0] for _ in range(3)]
    for j in range(160):
        transverse = [0, 0]
        for i in range(1024):
            kp = ki[f"{i+j}:{i+j+2}"]
            a, b = reflect(i-j-1, i-j+1)
            km = ki[f"{a}:{b}"]
            delta = (i+1)**3-i**3
            for side in (0, 1):
                transverse[side] += delta*kp[side]*km[side]
        products = [x*y for x in transverse for y in qi[j]]
        which = 0 if j < 32 else (1 if j < 96 else 2)
        accum[which][0] += min(products)
        accum[which][1] += max(products)
    eh = exact(cert["h"])
    h3 = eh[0]**3, eh[1]**3
    finite = [fscale(fmul(tuple(F(z, kd*kd*qd) for z in v), h3), F(2, 3))
              for v in accum]
    result, bounds = cert["result"], cert["bounds"]
    for j, v in enumerate(finite):
        contains("finite_lobe_"+str(j), result["finite_signed_lobes"][j], v,
                 "exact_reconstruction")
    moments = []
    for r in (0, 2):
        sums = [sum(ki[f"{i}:{i+1}"][side] * (1 if r == 0 else (i+1)**3-i**3)
                    for i in range(1024)) for side in (0, 1)]
        value = fmul(tuple(F(z, kd) for z in sums), eh if r == 0 else fscale(h3, F(1, 3)))
        error = exact(bounds["normalizer_spatial_errors"][str(r)])[1] + exact(bounds["normalizer_theta_errors"][str(r)])[1]
        value = value[0], value[1]+error
        moments.append(value)
        contains("moment_"+str(r), result["moments"][str(r)], value, "exact_reconstruction")

    eps = scale(exp(rat(-75)), 160000)
    et = scale(eps, F(512, 3))
    es = scale(exp(rat(-106)), 131072*(F(9, 4*231)+F(3, 231**2)+F(2, 231**3)))
    for name, value in (("kernel_uniform_theta_error", eps), ("theta_density_error", et),
                        ("spatial_density_error", es)):
        contains(name, bounds[name], value, "exact_reconstruction")
    errors = [mul(scale(pi, width), add(et, es)) for width in (F(1, 32), F(1, 16), F(1, 16))]
    for j, value in enumerate(errors):
        contains("lobe_error_"+str(j), bounds["lobe_full_tail_errors"][j], value, "exact_reconstruction")
    contains("weighted_tail", bounds["weighted_numerator_tail_error"],
             add(add(errors[0], errors[1]), scale(errors[2], F(1, 2))), "exact_reconstruction")
    for r, coefficient in ((0, F(1, 115)), (2, F(9, 4*115)+F(3, 115**2)+F(2, 115**3))):
        contains("moment_spatial_"+str(r), bounds["normalizer_spatial_errors"][str(r)],
                 scale(exp(rat(-53)), 256*coefficient), "exact_reconstruction")
        contains("moment_theta_"+str(r), bounds["normalizer_theta_errors"][str(r)],
                 scale(eps, 2 if r == 0 else F(8, 3)), "exact_reconstruction")
    full = []
    for j, v in enumerate(finite):
        error = exact(bounds["lobe_full_tail_errors"][j])[1]
        full.append((v[0]-error, v[1]+error))
        contains("complete_lobe_"+str(j), result["complete_signed_lobes"][j], full[-1], "exact_reconstruction")
    finite_n = fadd(fadd(finite[0], finite[1]), fscale(finite[2], F(1, 2)))
    full_n = fadd(fadd(full[0], full[1]), fscale(full[2], F(1, 2)))
    a0 = fscale(fmul(*moments), 2)
    budget = fdiv(full_n, a0)
    for name, value in (("finite_numerator", finite_n), ("complete_numerator", full_n),
                        ("positive_normalizer_A0", a0), ("J", budget)):
        contains(name, result[name], value, "exact_reconstruction")
    coarse = {
        "complete_numerator": (F("-0.000696"), F("-0.000053")),
        "positive_normalizer_A0": (F("0.022"), F("0.024")),
        "J": (F("-0.032"), F("-0.002")),
    }
    for name, outer in coarse.items():
        value = exact(result[name])
        check("strict_rational_"+name, outer[0] < value[0] <= value[1] < outer[1])
    check("theta_density_bound", exact(bounds["theta_density_error"])[1] < F("7.315e-26"))
    check("spatial_density_bound", exact(bounds["spatial_density_error"])[1] < F("1.185e-43"))
    check("weighted_tail_bound", exact(bounds["weighted_numerator_tail_error"])[1] < F("2.873e-26"))
    check("positive_normalizer", exact(result["positive_normalizer_A0"])[0] > 0)
    check("negative_threshold", exact(result["J"])[1] < F(-1, 1000))
    check("no_recorded_failures", result["failures"] == [] and result["decision"] == "NEGATIVE")
    old = json.loads((HERE / "equal-neighbor-budget-135-rational-check.json").read_text())
    check("retained_rational_check_values", old["actual_J"] == result["J"] and old["all_passed"] and all(old["checks"].values()))
    replay = HERE / "equal-neighbor-budget-175-replay.json"
    check("complete_original_replay", json.loads(replay.read_text()) == cert)
    inputs = [ORIGINAL, replay, HERE / "equal_neighbor_budget_135.py",
              ROOT / "scripts/laguerre/certify_conditional_cosine.py",
              ROOT / "scripts/hankel/certify_hankel.py", Path(__file__)]
    report = {"scope": "L904 fixed x=16,y=0,M=32 audit only", "trusted": "L037 Decimal and interpreter contracts",
              "input_sha256": {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs},
              "checks": checks, "failures": failures, "all_passed": not failures,
              "counts": {"kernel_boxes": len(cache), "cosine_weights": len(qi), "product_boxes": 163840},
              "actual_J": result["J"], "required": "J>=0", "retained_strict_bounds": "-32/1000<J<-2/1000",
              "evidence": evidence}
    OUTPUT.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps({"all_passed": not failures, "failed_checks": failures, "checks": len(checks),
                      "counts": report["counts"], "actual_J": result["J"], "required": "J>=0",
                      "certificate": str(OUTPUT.relative_to(ROOT))}))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
