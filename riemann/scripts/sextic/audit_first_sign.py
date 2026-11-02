"""Replay L607 and independently check its exact error/enclosure arithmetic.

This is not a second quadrature algorithm. Analytic applicability and the
interval-program inclusion proof are documented in L607's audit section.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from io import StringIO
from math import comb, factorial
from pathlib import Path
import json
import runpy

source = Path('scripts/sextic/certify_first_sign.py')
certificate = Path('scripts/sextic/first-sign-certificate.json')
before = certificate.read_bytes()
with redirect_stdout(StringIO()):
    state = runpy.run_path(str(source))
after = certificate.read_bytes()
data = json.loads(after)
checks = {'replay_byte_identical': before == after}
checks['parameters'] = (data['parameter_b'], data['frequency_x'],
                        data['N'], data['scale_bits']) == (4, 10, 8192, 256)
checks['no_extra_search'] = data['exploratory_evaluations_added'] == 0
checks['original_failures_empty'] = data['failures'] == []
N, scale = 8192, 2**256

# Exact polynomial pair coefficients, P^(n+1)=P^(n)' + (-Q'+10i)P^(n).
# Then (u^j exp(-Q+10iu))^(4) = P^(4)(u) exp(-Q+10iu).
qprime = {1: (-8, 0), 5: (-6, 0), 0: (0, 10)}
def next_derivative(p):
    out = {}
    def accumulate(k, re, im):
        a, b = out.get(k, (0, 0))
        out[k] = (a + re, b + im)
    for k, (re, im) in p.items():
        if k:
            accumulate(k-1, k*re, k*im)
        for m, (a, b) in qprime.items():
            accumulate(k+m, re*a-im*b, re*b+im*a)
    return {k: z for k, z in out.items() if z != (0, 0)}

polynomials, independent_bounds = [], []
for j in range(3):
    p = {j: (1, 0)}
    for _ in range(4):
        p = next_derivative(p)
    polynomials.append({str(k): list(p[k]) for k in sorted(p)})
    independent_bounds.append(sum((abs(a)+abs(b))*2**k
                                  for k, (a, b) in p.items()))
M = data['derivative_constants']['Ms']
checks['independent_fourth_derivative_bounds'] = all(
    a <= b for a, b in zip(independent_bounds, M))
checks['published_constants'] = data['derivative_constants'] == dict(
    A=218, B=488, C=960, D=1440, H2=48012,
    H3=10680344, H4=2399233840,
    Ms=[2399233840, 4841189056, 9768397008])

remainders = [F(5, 8)**k / factorial(k) for k in (81, 82, 83)]
checks['all_taylor_remainders_below_one_unit'] = all(r < F(1, scale)
                                                             for r in remainders)
checks['mesh_exactness'] = all(
    (r*scale).denominator == 1
    for i in range(N+1) for u in (F(2*i, N),)
    for r in (u, u*u, u**6+4*u*u, (u**6+4*u*u)/128, 10*u, 10*u/32))
errors = [2*F(2, 180)*F(2, N)**4*m for m in M]
tails = [F(2, 2**80)*sum(F(comb(j, k)*2**(j-k)*factorial(k), 208**(k+1))
                        for k in range(j+1)) for j in range(3)]
checks['simpson_spacing_and_full_line_factor'] = errors == list(map(F, data['simpson_error_bounds']))
checks['all_three_full_moment_tails'] = tails == list(map(F, data['tail_bounds']))
sums = state['sums']
checks['interval_order'] = all(lo <= hi for lo, hi in sums)
intervals = [(F(4*lo, 3*N*scale)-err-tail,
              F(4*hi, 3*N*scale)+err+tail)
             for (lo, hi), err, tail in zip(sums, errors, tails)]
checks['complete_rational_enclosures_reconstructed'] = intervals == [
    tuple(map(F, pair)) for pair in data['integral_enclosures']]
coarse = [(F(2041, 10**6), F(2043, 10**6)),
          (F(-552, 10**6), F(-550, 10**6)),
          (F(777, 10**6), F(779, 10**6))]
checks['coarse_values'] = coarse == [tuple(map(F, pair)) for pair in data['coarse_enclosures']]
gaps = [(lo-c_lo, c_hi-hi) for (lo, hi), (c_lo, c_hi) in zip(intervals, coarse)]
checks['all_six_coarse_margins_positive'] = all(a > 0 and b > 0 for a, b in gaps)
checks['product_lower_bounds_positive'] = coarse[0][0] > 0 and coarse[2][0] > 0
d_upper = max(v*v for v in coarse[1])-min(a*b for a in coarse[0] for b in coarse[2])
checks['determinant_upper_bound'] = d_upper == F(data['determinant_upper_bound']) == F(-1281153, 10**12)
checks['strict_negative'] = d_upper < 0 == F(data['required_upper_bound'])
failures = [name for name, passed in checks.items() if not passed]
output = dict(kind='L607_REPLAY_AND_INDEPENDENT_ERROR_AUDIT',
    source_sha256=sha256(source.read_bytes()).hexdigest(),
    certificate_sha256=sha256(after).hexdigest(),
    checks=checks, fourth_derivative_polynomials=polynomials,
    independent_fourth_derivative_bounds=independent_bounds,
    published_fourth_derivative_bounds=M,
    taylor_remainders=list(map(str, remainders)),
    required_taylor_bound=str(F(1, scale)),
    simpson_error_bounds=list(map(str, errors)), tail_bounds=list(map(str, tails)),
    raw_simpson_integer_sums=sums,
    reconstructed_integral_enclosures=[[str(a), str(b)] for a, b in intervals],
    exact_coarse_margins=[[str(a), str(b)] for a, b in gaps],
    determinant_upper_bound=str(d_upper), required_upper_bound='0', failures=failures,
    limitation='Same interval quadrature replay; analytic and program-inclusion audit is in L607.')
path = Path('scripts/sextic/first-sign-audit.json')
path.write_text(json.dumps(output, indent=2)+'\n')
print(json.dumps(dict(result='PASS' if not failures else 'FAIL', checks=len(checks),
    independent_derivative_bounds=independent_bounds, required_bounds=M,
    determinant_upper_bound=str(d_upper), required_upper_bound='0',
    certificate_unchanged=checks['replay_byte_identical'], failures=failures,
    path=str(path)), indent=2))
if failures:
    raise SystemExit(1)
