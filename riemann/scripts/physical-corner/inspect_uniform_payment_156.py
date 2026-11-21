#!/usr/bin/env python3
"""Inspect ALL whole-edge blocks and exact scalar endpoints; no evaluator import."""
from fractions import Fraction as F
from math import isqrt, factorial
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = HERE/'uniform-payment-inspection-156.json'


def main():
    path = HERE/'uniform-payment-156.json'
    d = json.loads(path.read_text())
    original = json.loads((HERE/'time-edge-152.json').read_text())
    checks, failures = [], []

    def need(ok, name):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            failures.append(name)

    def iv(v):
        den = 1 << v['denominator_power_two']
        l, h = F(int(v['lo']), den), F(int(v['hi']), den)
        assert l <= h
        return l, h

    def add(a, b): return a[0]+b[0], a[1]+b[1]
    def mul(a, b):
        v = [x*y for x in a for y in b]
        return min(v), max(v)
    def scale(a, c): return mul(a, (F(c), F(c)))
    def contains(a, b): return a[0] <= b[0] <= b[1] <= a[1]
    def overlap(a, b): return max(a[0], b[0]) <= min(a[1], b[1])
    def cv(z): return [iv(z[k]) for k in ['re', 'im']]

    need(d['status'] == 'FAIL' and d['failures'] == ['ArithmeticError: R_upper_lt677over100'],
         'preserved driver stop at extra old-norm comparison')
    need(d['source_sha256'] == hashlib.sha256((HERE/'uniform_payment_156.py').read_bytes()).hexdigest(), 'evaluator hash')
    need(d['inputs'] == {'t_lower': '98/625', 't_upper': '1/5', 'x': 6000000185827}, 'exact closed-edge inputs')
    need(d['bits'] == 224 and d['N'] == d['completed_through'] == 690988, 'full intended support and scale')
    for name, gate in d['gates'].items():
        if name == 'R_upper_lt677over100':
            need(not gate['passed'], 'extra norm comparison failure preserved')
        else:
            need(gate['passed'], 'essential gate '+name)
    for name in ['floor_lower', 'floor_upper', 'ell_logN_gt13', 'shift_gt0', 'shift_lt25', 'amplitudes_nonpositive_exponents']:
        need(iv(d['gates'][name]['evidence'])[0] > 0, 'strict domain margin '+name)
    need(contains(iv(d['constants']['t']), (F(98, 625), F(1, 5))), 'time interval inclusion')
    need(d['series'] == {'log_terms': 64, 'exp_degree': 28, 'cos_degree': 46,
                        'sin_degree': 47, 'angle_doublings': 4, 'exp_squarings': 8}, 'audited finite series')
    for k, exact in [('exp', F(1, 8**29*factorial(29))),
                     ('cos', F(1, 4**48*factorial(48))),
                     ('sin', F(1, 4**49*factorial(49)))]:
        den = 1 << d['remainders']['denominator_power_two']
        h = F(int(d['remainders'][k]), den)
        need(exact <= h < exact+F(1, den), k+' exact outward remainder')
    # Original values are comparisons only, accessed after independent execution.
    for name in set(d['constants']).intersection(original['constants']):
        need(overlap(iv(d['constants'][name]), iv(original['constants'][name])), 'carrier comparison '+name)
    N, pos, direct, prime_count = d['N'], 1, 0, 0
    prime = bytearray(b'\x01')*(N+1)
    prime[:2] = b'\x00\x00'
    for p in range(2, isqrt(N)+1):
        if prime[p]:
            prime[p*p:N+1:p] = b'\x00'*((N-p*p)//p+1)
    sums = [(F(0), F(0)), (F(0), F(0))]
    need(len(d['blocks']) == len(original['blocks']) == 338, 'all338 blocks')
    for j, b in enumerate(d['blocks']):
        o = original['blocks'][j]
        need(b['lo'] == pos and b['count'] == b['hi']-b['lo']+1
             and b['hi'] == min(N, b['lo']+2047), f'block{j} exact adjacency and count')
        need(b['all_term_gates_passed'] and int(b['min_amplitude']) > 0
             and int(b['min_reduction_margin']) > 0, f'block{j} every elementary domain')
        v = iv(b['exponent_range'])
        need(-32 <= v[0] <= v[1] <= 0, f'block{j} full negative exponential domain')
        need(b['prime_count'] == sum(prime[b['lo']:b['hi']+1]), f'block{j} independently counted primes')
        need(b['direct_phases'] == b['count']-int(b['lo'] == 1), f'block{j} every nonconstant direct phase')
        need(int(b['max_elementary_width']) >= 0 and int(b['max_reduction_integer']) >= 0,
             f'block{j} width records retained')
        need(b['lo'] == o['lo'] and b['hi'] == o['hi'], f'block{j} comparison support')
        for k, part in enumerate(['re', 'im']):
            a = iv(b['A_block'][part])
            sums[k] = add(sums[k], a)
            need(overlap(a, iv(o['sums']['A'][part])), f'block{j} {part} comparison')
        direct += b['direct_phases']
        prime_count += b['prime_count']
        pos = b['hi']+1
    need(pos == N+1 and direct == N-1 and prime_count == sum(prime), 'entire support, phase and prime counts')
    need(sums == cv(d['sums']['A']), 'exact sum of EVERY block endpoint')
    r = d['result']
    norm2 = sum(max(abs(z) for z in part)**2 for part in sums)
    rec = r['norm_squared_exact_upper']
    need(norm2 == F(int(rec['numerator']), 1 << rec['denominator_power_two']), 'exact rectangular norm square')
    dyadic = iv(r['norm_squared_dyadic_enclosure'])
    need(dyadic[0] == 0 and dyadic[1] >= norm2, 'outward rounded norm square')
    R = iv(r['R_upper_enclosure'])
    need(R[0] == 0 and R[1]**2 >= dyadic[1], 'sqrt by exact squared inequality')
    need(F(677, 100) < R[1] < F(679, 100), 'independent norm exceeds old comparison but is below679/100')
    need(iv(d['gates']['R_upper_lt677over100']['evidence']) == R, 'failed comparison exact evidence')
    p, q = F(101, 200000000), F(142, 10000000)+F(1, 250000000000)
    need(contains(iv(r['p']), (p, p)) and contains(iv(r['q']), (q, q)), 'exact p,q inclusion')
    E = add(add(scale(add(scale(R, 25), (F(81, 2), F(81, 2))), p), scale(R, q)), (p*q, p*q))
    need(contains(iv(r['E']), E), 'full payment including pq by exact endpoints')
    need(iv(r['E'])[1] < F(203, 1000000), 'required strict payment upper bound')
    need(d['required_bound'] == 'E_upper<203/1000000', 'unchanged approved threshold')
    for k in ['R_upper_enclosure', 'E', 'p', 'q']:
        need(overlap(iv(r[k]), iv(original['result'][k])), k+' final comparison')
    out = {'status': 'VERIFIED_PAYMENT_WITH_DRIVER_COMPARISON_STOP' if not failures else 'FAIL',
           'driver_status': d['status'], 'driver_failures': d['failures'],
           'old_norm_comparison_reproduced': False, 'checks': checks, 'failures': failures,
           'replay_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
           'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'comparison_sha256': hashlib.sha256((HERE/'time-edge-152.json').read_bytes()).hexdigest(),
           'blocks': len(d['blocks']), 'N': N, 'direct_phases': direct, 'prime_count': prime_count,
           'actual_R_upper': str(R[1]), 'actual_E_upper': str(iv(r['E'])[1]),
           'required_E_upper': '203/1000000',
           'qualification': 'Exhaustive exact endpoint inspection supplements independently justified elementary replay; comparisons are not premises.'}
    OUT.write_text(json.dumps(out, separators=(',', ':'))+'\n')
    print(json.dumps({'status': out['status'], 'checks': len(checks), 'blocks': len(d['blocks']),
          'actual_E_upper': float(iv(r['E'])[1]), 'required': '<203/1000000',
          'failures': failures, 'path': str(OUT)}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
