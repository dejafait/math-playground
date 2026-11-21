"""One bounded trial diagnostic; floating spectra are never certificates.

Run from riemann: OPENBLAS_NUM_THREADS=1 python3 scripts/logarithmic-gcd/critical-pilot-226.py
All certified operations below use Python integers. No external log value
is used for a certificate. Full vectors, coefficients and log intervals
are saved to critical-pilot-226.json beside this script.
"""
import json
import math
from pathlib import Path
import sys
import numpy as np


SCALE = 10**80
TERMS = 100
ROUND_SCALE = 10**9


def ceildiv(a, b):
    return -((-a) // b)


def log_ratio_bounds(a, b):
    """For 1<=a/b<=2, integer bounds on SCALE*log(a/b).

    With t=(a-b)/(a+b) in [0,1/3], log(a/b) is twice
    sum t^(2i+1)/(2i+1). Each floored summand loses <1/SCALE.
    The omitted positive tail is at most
    2*t^(2*TERMS+1)/((2*TERMS+1)*(1-t*t)).
    """
    assert b <= a <= 2*b
    u, v = a-b, a+b
    lo = 0
    for i in range(TERMS):
        e = 2*i+1
        lo += 2*(SCALE*pow(u, e)//((e)*pow(v, e)))
    e = 2*TERMS+1
    tail = ceildiv(2*SCALE*pow(u, e)*v*v,
                   e*pow(v, e)*(v*v-u*u))
    return lo, lo+2*TERMS+tail


LOG2 = log_ratio_bounds(2, 1)


def log_bounds(n):
    k = n.bit_length()-1
    lo, hi = log_ratio_bounds(n, 2**k)
    return lo+k*LOG2[0], hi+k*LOG2[1]


def arithmetic(n):
    phi = list(range(n+1))
    phi[1] = 1
    factors = [{} for _ in range(n+1)]
    primes = []
    for p in range(2, n+1):
        if not factors[p]:
            primes.append(p)
            for m in range(p, n+1, p):
                phi[m] -= phi[m]//p
                q, e = m, 0
                while q % p == 0:
                    q //= p
                    e += 1
                factors[m][p] = e
    mu = [0]+[(-1)**len(factors[m]) if all(e == 1 for e in factors[m].values()) else 0
              for m in range(1, n+1)]
    return phi, factors, primes, mu


def evaluate(n, B, phi, factors, primes, mu):
    # Integer b coordinates: c_m=sqrt(m)*b_m, so no square roots remain.
    b = [0]+[sum(mu[k]*B[d*k] for k in range(1, n//d+1))
             for d in range(1, n+1)]
    inversion_ok = all(B[d] == sum(b[d::d]) for d in range(1, n+1))
    Q = sum(phi[d]*B[d]**2 for d in range(1, n+1))
    coeff = {p: 2*factors[n].get(p, 0)*Q for p in primes}
    # Full kappa contribution, plus every prime-power cross term in (7).
    for d in range(1, n+1):
        for p in factors[d]:
            assert phi[d] % (p-1) == 0
            coeff[p] += 2*(phi[d]//(p-1))*B[d]**2
        for p in primes:
            r = p
            while d*r <= n:
                coeff[p] -= 2*phi[d]*B[d]*B[d*r]
                r *= p
    # Independent original-gcd evaluation of Q and each log coefficient.
    original_Q = sum(m*b[m]**2 for m in range(1, n+1))
    original_coeff = {p: 2*factors[n].get(p, 0)*Q for p in primes}
    for m in range(1, n+1):
        for k in range(m+1, n+1):
            g = math.gcd(m, k)
            w = 2*b[m]*b[k]*g
            original_Q += w
            for p in factors[m].keys() | factors[k].keys():
                original_coeff[p] += w*(2*factors[g].get(p, 0)
                                        -factors[m].get(p, 0)-factors[k].get(p, 0))
    logs = {p: log_bounds(p) for p in primes}
    flo = sum(a*(logs[p][0] if a >= 0 else logs[p][1]) for p, a in coeff.items())
    fhi = sum(a*(logs[p][1] if a >= 0 else logs[p][0]) for p, a in coeff.items())
    # Outward rounding to 12 decimal places of the exact quotient interval.
    decimals = 10**12
    qlo = flo*decimals//(SCALE*Q)
    qhi = ceildiv(fhi*decimals, SCALE*Q)
    checks = dict(inversion=inversion_ok, Q_positive=Q > 0,
                  original_Q_equals_divisor_Q=Q == original_Q,
                  all_log_coefficients_equal=coeff == original_coeff,
                  interval_ordered=flo <= fhi,
                  # Verifies the deliberately coarse displayed enclosure.
                  displayed_enclosure=(qlo*SCALE*Q <= flo*decimals
                                       and qhi*SCALE*Q >= fhi*decimals))
    assert all(checks.values()), checks
    return dict(B_integer=B[1:], b_integer=b[1:], Q_exact=Q,
                log_coefficients={str(p): a for p, a in coeff.items()},
                log_scaled_intervals={str(p): list(logs[p]) for p in primes},
                F_scaled_interval=[flo, fhi], quotient_denominator=SCALE*Q,
                quotient_display_scaled_1e12=[qlo, qhi], checks=checks)


def main():
    if len(sys.argv) == 2 and sys.argv[1] == '--verify':
        path = Path(__file__).with_suffix('.json')
        saved = json.loads(path.read_text())
        assert saved['log_scale'] == SCALE and saved['series_terms'] == TERMS
        assert [r['N'] for r in saved['records']] == [2**j for j in range(1, 10)]
        for record in saved['records']:
            n = record['N']
            phi, factors, primes, mu = arithmetic(n)
            replay = evaluate(n, [0]+record['B_integer'], phi, factors, primes, mu)
            for key, value in replay.items():
                assert record[key] == value, (n, key)
        assert saved['failures'] == []
        print(f'Full certificate replay passed for all nine vectors, all exact '
              f'coefficients, Q values, log intervals and quotients: {path}')
        return
    assert len(sys.argv) == 1
    records = []
    for j in range(1, 10):
        n = 2**j
        phi, factors, primes, mu = arithmetic(n)
        H = np.eye(n)*(2*math.log(n))
        for d in range(1, n+1):
            H[d-1, d-1] += 2*sum(math.log(p)/(p-1) for p in factors[d])
            for p in primes:
                r = p
                while d*r <= n:
                    v = math.log(p)*math.sqrt(phi[d]/phi[d*r])
                    H[d-1, d*r-1] -= v
                    H[d*r-1, d-1] -= v
                    r *= p
        values, vectors = np.linalg.eigh(H)
        raw = vectors[:, 0]/np.sqrt(np.array(phi[1:], dtype=float))
        raw /= max(abs(raw))
        B = [0]+[int(round(ROUND_SCALE*x)) for x in raw]
        result = evaluate(n, B, phi, factors, primes, mu)
        # These summaries suggest patterns only; all vectors are retained.
        result.update(N=n, floating_min_eigenvalue=float(values[0]),
                      floating_eigen_residual=float(np.linalg.norm(H@vectors[:, 0]-values[0]*vectors[:, 0])),
                      B_sign_counts={"positive":sum(x > 0 for x in B[1:]),
                                     "negative":sum(x < 0 for x in B[1:]),
                                     "zero":sum(x == 0 for x in B[1:])})
        records.append(result)
        lo, hi = result['quotient_display_scaled_1e12']
        print(f'N={n}: certified trial F/Q in [{lo/1e12:.12f}, {hi/1e12:.12f}], '
              f'Q>0={result["checks"]["Q_positive"]}; all exact checks passed', flush=True)
    output = dict(step=226, scope="finite explicit trials only; no spectral lower bound",
                  required_threshold="inf over all N>=2 and nonzero complex c of F_(2 log N)/Q > -infinity",
                  input="L737 equations (5)-(7),(11); real trials are allowed complex trials",
                  certificate_method="integer atanh partial sums and geometric tail; independent original/divisor coefficients",
                  log_scale=SCALE, series_terms=TERMS, trial_round_scale=ROUND_SCALE,
                  floating_spectra_certified=False, records=records,
                  failures=[], universal_bound_proved=False)
    path = Path(__file__).with_suffix('.json')
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(f'Certificate: {path}; failures: []; required uniform threshold remains undecided.')


if __name__ == '__main__':
    main()
