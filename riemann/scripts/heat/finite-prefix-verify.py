#!/usr/bin/env python3
"""Consume every prefix row with finer, independently evaluated enclosures.

Does not import or execute the producer. This is part of the numerical
reproduction, not a separate-turn critical mathematical audit.
"""
from array import array
from fractions import Fraction as F
from pathlib import Path
import gzip
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent
Q = 10**40
SOURCE_GRID = 10**30
RATIO = Q//SOURCE_GRID
failed = []
comparisons = 0


def ceilq(a, b):
    assert b > 0
    return -((-a)//b)


def rat(q):
    q = F(q)
    return q.numerator*Q//q.denominator, ceilq(q.numerator*Q, q.denominator)


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def minus(a, b):
    return a[0]-b[1], a[1]-b[0]


def times(a, b):
    v = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(v)//Q, ceilq(max(v), Q)


def rational_times(a, r):
    r = F(r)
    v = (a[0]*r.numerator, a[1]*r.numerator)
    return min(v)//r.denominator, ceilq(max(v), r.denominator)


def inv(a):
    assert a[0] > 0
    return Q*Q//a[1], ceilq(Q*Q, a[0])


def small_log(n, d):
    assert d <= n <= 2*d
    z = (Q*(n-d)//(n+d), ceilq(Q*(n-d), n+d))
    z2 = times(z, z)
    # Horner evaluation, rather than the producer's forward powers.
    p = rat(F(1, 89))
    for j in range(43, -1, -1):
        p = plus(rat(F(1, 2*j+1)), times(z2, p))
    v = rational_times(times(z, p), 2)
    return v[0], v[1]+1


L2 = small_log(2, 1)


def lograt(q):
    q = F(q)
    assert q > 0
    n, d, k = q.numerator, q.denominator, 0
    while n >= 2*d:
        d *= 2
        k += 1
    while n < d:
        n *= 2
        k -= 1
    return plus(rational_times(L2, k), small_log(n, d))


def logiv(a):
    return lograt(F(a[0], Q))[0], lograt(F(a[1], Q))[1]


def exponential(q):
    assert q[0] <= q[1] <= 0
    a = ((-q[1])//32, ceilq(-q[0], 32))
    assert a[1] <= Q//2
    # Horner's 1+(a/k)*P evaluates the degree-32 Taylor polynomial.
    p = (Q, Q)
    for k in range(32, 0, -1):
        p = plus((Q, Q), rational_times(times(a, p), F(1, k)))
    p = p[0], p[1]+1
    for _ in range(5):
        p = times(p, p)
    return inv(p)


def test(name, yes, detail=None):
    global comparisons
    comparisons += 1
    if not yes:
        failed.append(dict(check=name, detail=detail))
        if len(failed) >= 10:
            raise AssertionError(failed)


def contained(name, narrow, coarse):
    test(name, int(coarse[0])*RATIO <= narrow[0] <= narrow[1] <= int(coarse[1])*RATIO,
         dict(narrow=list(map(str,narrow)), coarse=list(map(str,coarse))))


def digest(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for b in iter(lambda:f.read(1<<20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    cert_path = ROOT/"finite-prefix-certificate.json"
    data = json.loads(cert_path.read_text())
    t, x = F(".16836"), F("6000284561421.5")
    test("fixed_inputs", data["inputs"] == dict(t=str(t), x=str(x), ell0=str(F("24.18022820120389")), prime_limit=307))
    test("source_grid", data["method"]["grid"] == str(SOURCE_GRID))
    test("log_tail", F(2, 3**91)*F(9, 91*8) < F(1, Q))
    test("exp_tail", F(1, 2**33*math.factorial(33))*F(68, 67) < F(1, Q))
    for e in data["evidence"]:
        test("evidence_hash", digest(ROOT/e["path"]) == e["sha256"], e["path"])
    test("producer_hash", digest(ROOT/"finite-prefix-certificate.py") == data["producer_sha256"])
    atans = []
    for n in (5, 239):
        s = sum((F((-1)**j, (2*j+1)*n**(2*j+1)) for j in range(70)), F(0))
        atans.append((rat(s)[0], rat(s+F(1, 141*n**141))[1]))
    pi = minus(rational_times(atans[0], 16), rational_times(atans[1], 4))
    log4pi = logiv(rational_times(pi, 4))
    lstar = minus(rational_times(lograt(1+x*x), F(1, 2)), log4pi)
    sigma = minus(plus(rat(F(1, 2)), rational_times(lstar, t/4)), rat(t/(2*(1+x*x))))
    cutoff_square = plus(rational_times(inv(rational_times(pi, 4)), x), rat(t/16))
    N = math.isqrt(cutoff_square[0]//Q)
    test("cutoff", N == data["scalars"]["N"] and N*N*Q <= cutoff_square[0] <= cutoff_square[1] < (N+1)**2*Q)
    for name, v in dict(pi=pi,lstar=lstar,sigma=sigma,cutoff_square=cutoff_square,logN=lograt(N)).items():
        contained(name, v, data["scalars"][name])
    test("weight_one", F(lograt(N)[1], Q) < F("24.18022820120389"))
    test("domain", rational_times(minus(lograt(x), log4pi), t)[1] < rat(F("5.17"))[0])
    # An independent sieve keeps the largest small prime divisor.
    factor = array("I", [0])*(N+1)
    primes = []
    for p in range(2, N+1):
        if factor[p] == 0:
            if p <= 307:
                primes.append(p)
            for m in range(p*p, N+1, p):
                factor[m] = p
    logslo, logshi = [0]*(N+1), [0]*(N+1)
    clo, chi = [0]*(N+1), [0]*(N+1)
    radii = {}
    with gzip.open(ROOT/"finite-prefix-certificate-initial.tsv.gz", "rt") as f:
        test("initial_header", next(f).strip() == "n\tlog_lower\tlog_upper\ta_lower\ta_upper")
        for n in range(1, N+1):
            row = list(map(int,next(f).split()))
            test("initial_index", row[0] == n)
            p = factor[n]
            if n == 1:
                h, a = (0,0), (Q,Q)
            else:
                h = (logslo[p]+logslo[n//p], logshi[p]+logshi[n//p]) if p else lograt(n)
                a = exponential(minus(rational_times(times(h,h),t/4), times(sigma,h)))
            contained(f"log_{n}", h, row[1:3])
            contained(f"initial_{n}", a, row[3:5])
            logslo[n], logshi[n] = h
            clo[n], chi[n] = a
            if n in primes:
                radii[n] = a
            if n % 200000 == 0:
                print(f"Verified initial enclosures {n}/{N}", flush=True)
        test("initial_eof", f.read() == "")
    del logslo, logshi, factor
    test("prime_set", primes == [s["p"] for s in data["computation"]["stages"]])
    # Opposite factor order; generic four-endpoint multiplication.
    for p in reversed(primes):
        for m in range((N//p)*p, p-1, -p):
            v = times(radii[p], (clo[m//p],chi[m//p]))
            clo[m], chi[m] = clo[m]-v[1], chi[m]-v[0]
    original_sum_lo = original_sum_hi = finer_lo = finer_hi = 0
    counts = dict(positive=0,negative=0,straddling=0,exact_zero=0)
    with gzip.open(ROOT/"finite-prefix-certificate-coefficients.tsv.gz", "rt") as f:
        test("coefficient_header", next(f).strip() == "m\tc_lower\tc_upper\tabs_lower\tabs_upper")
        for m in range(2, N+1):
            row = list(map(int,next(f).split()))
            test("coefficient_index", row[0] == m)
            contained(f"coefficient_{m}", (clo[m],chi[m]), row[1:3])
            a,b = row[1:3]
            if a > 0:
                lo,hi,kind = a,b,"positive"
            elif b < 0:
                lo,hi,kind = -b,-a,"negative"
            else:
                lo,hi,kind = 0,max(-a,b),"exact_zero" if a==b==0 else "straddling"
            test("abs_interval", row[3:5] == [lo,hi])
            counts[kind] += 1
            original_sum_lo += lo
            original_sum_hi += hi
            a,b = clo[m],chi[m]
            finer_lo += a if a>0 else -b if b<0 else 0
            finer_hi += max(abs(a),abs(b))
        test("coefficient_eof", f.read() == "")
    test("complete_sum", [str(original_sum_lo),str(original_sum_hi)] == data["result"]["prefix_interval_grid"])
    test("sign_counts", counts == data["result"]["counts"])
    contained("sum", (finer_lo,finer_hi), (original_sum_lo,original_sum_hi))
    test("unit_budget", original_sum_hi < SOURCE_GRID and finer_hi < Q)
    out = ROOT/"finite-prefix-verification.json"
    out.write_text(json.dumps(dict(scope="Complete finer-grid numerical consumer; separate-turn proof audit pending.",
        grid=str(Q), source_sha256=digest(cert_path), verifier_sha256=digest(Path(__file__)),
        comparisons=comparisons, failures=failed, initial_rows=N, coefficient_rows=N-1,
        source_sum_grid=[str(original_sum_lo),str(original_sum_hi)],
        finer_sum_grid=[str(finer_lo),str(finer_hi)], counts=counts,
        required_upper="1", all_checks_passed=not failed), indent=2)+"\n")
    print(f"Complete consumer: {comparisons} checks, {len(failed)} failures, {N} initial and {N-1} coefficient rows; required upper<1", flush=True)
    print(f"Evidence: {out.relative_to(ROOT.parent.parent)}", flush=True)
    assert not failed


if __name__ == "__main__":
    main()
