#!/usr/bin/env python3
"""Exact fixed-grid enclosure of the approved Planat coefficient prefix.

No binary floating-point value enters any mathematical comparison.
See L497 for the interval algorithm, series tails and convolution proof.
"""
from array import array
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json
import math
import time

Q = 10**30
LOG_TERMS = 35
EXP_DEGREE = 26
ROOT = Path(__file__).resolve().parent
NAME = "finite-prefix-certificate"
checks = []


def ceildiv(a, b):
    assert b > 0
    return -((-a)//b)


def point(q):
    q = F(q)
    return q.numerator*Q//q.denominator, ceildiv(q.numerator*Q, q.denominator)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v)//Q, ceildiv(max(v), Q)


def scale(a, q):
    q = F(q)
    v = [x*q.numerator for x in a]
    return min(v)//q.denominator, ceildiv(max(v), q.denominator)


def reciprocal(a):
    assert a[0] > 0
    return Q*Q//a[1], ceildiv(Q*Q, a[0])


def log_unit(n, d):
    assert d <= n <= 2*d
    zn, zd = n-d, n+d
    z = (zn*Q//zd, ceildiv(zn*Q, zd))
    z2 = mul(z, z)
    power = z
    slo = shi = 0
    for j in range(LOG_TERMS):
        slo += power[0]//(2*j+1)
        shi += ceildiv(power[1], 2*j+1)
        power = mul(power, z2)
    # Uniform exact positive tail is <1/Q, checked in main().
    return 2*slo, 2*shi+1


LOG2 = log_unit(2, 1)


def log_rational(q):
    q = F(q)
    assert q > 0
    n, d = q.numerator, q.denominator
    k = n.bit_length()-d.bit_length()
    if k >= 0:
        d <<= k
    else:
        n <<= -k
    if n < d:
        n <<= 1
        k -= 1
    assert d <= n < 2*d
    return add(scale(LOG2, k), log_unit(n, d))


def logarithm(a):
    assert a[0] > 0
    return log_rational(F(a[0], Q))[0], log_rational(F(a[1], Q))[1]


def exp_negative(a):
    assert a[0] <= a[1] <= 0
    # exp(-a/32), then five squarings, then reciprocal.
    lo, hi = (-a[1])//32, ceildiv(-a[0], 32)
    assert 0 <= lo <= hi <= Q//2
    tlo = thi = slo = shi = Q
    for j in range(1, EXP_DEGREE+1):
        tlo = tlo*lo//(Q*j)
        thi = ceildiv(thi*hi, Q*j)
        slo += tlo
        shi += thi
    shi += 1  # Uniform Taylor tail <1/Q, checked in main().
    for _ in range(5):
        slo, shi = slo*slo//Q, ceildiv(shi*shi, Q)
    return reciprocal((slo, shi))


def check(name, passed, actual, required):
    checks.append(dict(name=name, passed=bool(passed), actual=actual, required=required))
    assert passed, name


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def decimal_bound(v):
    sign = "-" if v < 0 else ""
    v = abs(v)
    return f"{sign}{v//Q}.{v%Q:030d}"


def main():
    started = time.monotonic()
    t, x = F(".16836"), F("6000284561421.5")
    ell0 = F("24.18022820120389")
    logtail = F(2, 3**71)*F(9, 71*8)
    exptail = F(1, 2**27*math.factorial(27))*F(56, 55)
    check("uniform_log_tail", logtail < F(1, Q), str(logtail), f"<1/{Q}")
    check("uniform_exp_tail", exptail < F(1, Q), str(exptail), f"<1/{Q}")
    atan = []
    for n in (5, 239):
        s = sum((F((-1)**j, (2*j+1)*n**(2*j+1)) for j in range(50)), F(0))
        tail = F(1, 101*n**101)
        atan.append((point(s)[0], point(s+tail)[1]))
    pi = sub(scale(atan[0], 16), scale(atan[1], 4))
    log4pi = logarithm(scale(pi, 4))
    lstar = sub(scale(log_rational(1+x*x), F(1, 2)), log4pi)
    sigma = sub(add(point(F(1, 2)), scale(lstar, t/4)), point(t/(2*(1+x*x))))
    cutoff_square = add(scale(reciprocal(scale(pi, 4)), x), point(t/16))
    N = math.isqrt(cutoff_square[0]//Q)
    check("cutoff_lower", N*N*Q <= cutoff_square[0], str(cutoff_square[0]), f">={N*N*Q}")
    check("cutoff_upper", cutoff_square[1] < (N+1)**2*Q, str(cutoff_square[1]), f"<{(N+1)**2*Q}")
    logN = log_rational(N)
    check("prefix_weight_one", F(logN[1], Q) < ell0, list(map(str, logN)), f"log(N)<{ell0}")
    domain_log = sub(log_rational(x), log4pi)
    domain_tlog = scale(domain_log, t)
    check("L494_domain", domain_tlog[1] < point(F("5.17"))[0], list(map(str, domain_tlog)), "<5.17")
    check("sigma_positive", sigma[0] > 0, list(map(str, sigma)), ">0")
    print(f"Certified N={N}, sigma in [{decimal_bound(sigma[0])},{decimal_bound(sigma[1])}], h=1", flush=True)

    spf = array("I", [0])*(N+1)
    for p in range(2, math.isqrt(N)+1):
        if spf[p] == 0:
            for m in range(p*p, N+1, p):
                if spf[m] == 0:
                    spf[m] = p
    llo, lhi = [0]*(N+1), [0]*(N+1)
    clo, chi = [0]*(N+1), [0]*(N+1)
    clo[1] = chi[1] = Q
    primes, radii = [], {}
    init_path = ROOT/(NAME+"-initial.tsv.gz")
    final_path = ROOT/(NAME+"-coefficients.tsv.gz")
    max_initial_width = 0
    prime_log_count = 0
    with gzip.open(init_path, "wt", compresslevel=1) as f:
        f.write("n\tlog_lower\tlog_upper\ta_lower\ta_upper\n")
        f.write(f"1\t0\t0\t{Q}\t{Q}\n")
        for n in range(2, N+1):
            p = spf[n]
            if p:
                h = (llo[p]+llo[n//p], lhi[p]+lhi[n//p])
            else:
                h = log_rational(n)
                prime_log_count += 1
                if n <= 307:
                    primes.append(n)
            llo[n], lhi[n] = h
            exponent = sub(scale(mul(h, h), t/4), mul(sigma, h))
            a = exp_negative(exponent)
            clo[n], chi[n] = a
            max_initial_width = max(max_initial_width, a[1]-a[0])
            if n in primes:
                radii[n] = a
            f.write(f"{n}\t{h[0]}\t{h[1]}\t{a[0]}\t{a[1]}\n")
            if n % 100000 == 0:
                print(f"Initial intervals {n}/{N}", flush=True)
    del llo, lhi, spf
    check("prime_set_size", len(primes) == 63 and primes[-1] == 307, primes, "all primes <=307 (sieve), count=63")
    check("all_euler_radii", all(0 < a[0] <= a[1] < Q for a in radii.values()), {str(p):list(map(str,a)) for p,a in radii.items()}, "0<r_p<1")
    stages = []
    updates = 0
    for p in primes:
        rlo, rhi = radii[p]
        for m in range((N//p)*p, p-1, -p):
            j = m//p
            # Multiplication of positive r by an arbitrary signed interval.
            if clo[j] >= 0:
                plo, phi = rlo*clo[j]//Q, ceildiv(rhi*chi[j], Q)
            elif chi[j] <= 0:
                plo, phi = rhi*clo[j]//Q, ceildiv(rlo*chi[j], Q)
            else:
                plo, phi = rhi*clo[j]//Q, ceildiv(rhi*chi[j], Q)
            clo[m], chi[m] = clo[m]-phi, chi[m]-plo
            updates += 1
        stages.append(dict(p=p, updates=N//p))
    total_lo = total_hi = 0
    counts = dict(positive=0, negative=0, straddling=0, exact_zero=0)
    max_width = 0
    with gzip.open(final_path, "wt", compresslevel=1) as f:
        f.write("m\tc_lower\tc_upper\tabs_lower\tabs_upper\n")
        for m in range(2, N+1):
            a, b = clo[m], chi[m]
            assert a <= b
            if a > 0:
                lo, hi = a, b
                counts["positive"] += 1
            elif b < 0:
                lo, hi = -b, -a
                counts["negative"] += 1
            elif a == b == 0:
                lo = hi = 0
                counts["exact_zero"] += 1
            else:
                lo, hi = 0, max(-a, b)
                counts["straddling"] += 1
            max_width = max(max_width, b-a)
            total_lo += lo
            total_hi += hi
            f.write(f"{m}\t{a}\t{b}\t{lo}\t{hi}\n")
    check("all_outputs_counted", sum(counts.values()) == N-1, sum(counts.values()), N-1)
    check("unit_budget", total_hi < Q, [str(total_lo), str(total_hi)], f"upper<{Q}")
    data = dict(
        scope="Fixed-corner complete prefix only; no edge, tail, charge, collision or RH conclusion.",
        inputs=dict(t=str(t), x=str(x), ell0=str(ell0), prime_limit=307),
        method=dict(grid=str(Q), log_terms=LOG_TERMS, exp_degree=EXP_DEGREE, exp_scaling=32,
                    coefficient_algorithm="descending prime convolution of normalized heat coefficients"),
        scalars=dict(pi=list(map(str,pi)), lstar=list(map(str,lstar)), sigma=list(map(str,sigma)),
                     cutoff_square=list(map(str,cutoff_square)), N=N, logN=list(map(str,logN))),
        result=dict(prefix_interval_grid=[str(total_lo), str(total_hi)],
                    prefix_interval_decimal=[decimal_bound(total_lo),decimal_bound(total_hi)],
                    required_upper="1", margin_lower_grid=str(Q-total_hi),
                    enclosure_width_grid=str(total_hi-total_lo), counts=counts,
                    max_initial_width_grid=str(max_initial_width), max_coefficient_width_grid=str(max_width)),
        computation=dict(prime_log_evaluations=prime_log_count, coefficient_updates=updates,
                         stages=stages, rows_initial=N, rows_coefficients=N-1),
        checks=checks, failures=[c for c in checks if not c["passed"]],
        evidence=[dict(path=p.name, sha256=sha(p)) for p in (init_path, final_path)],
        producer_sha256=sha(Path(__file__)), elapsed_seconds=round(time.monotonic()-started, 2))
    out = ROOT/(NAME+".json")
    out.write_text(json.dumps(data, indent=2)+"\n")
    print(f"S_N in [{decimal_bound(total_lo)}, {decimal_bound(total_hi)}]; required upper<1", flush=True)
    print(f"All {N-1} outputs; signs={counts}; failures=0; updates={updates}", flush=True)
    print(f"Certificate: {out.relative_to(ROOT.parent.parent)}; full rows: {init_path.name}, {final_path.name}", flush=True)


if __name__ == "__main__":
    main()
