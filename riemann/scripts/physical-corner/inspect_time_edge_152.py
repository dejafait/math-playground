#!/usr/bin/env python3
"""Exhaust every block and recompute scalar endpoints with exact Fractions."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = HERE/'time-edge-inspection-152.json'


def main():
    d = json.loads((HERE/'time-edge-152.json').read_text())
    checks, failures = [], []

    def need(ok, name):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            failures.append(name)

    def iv(v):
        q = 1 << v['denominator_power_two']
        l, h = F(int(v['lo']), q), F(int(v['hi']), q)
        assert l <= h
        return l, h

    def add(a, b): return a[0]+b[0], a[1]+b[1]
    def mul(a, b):
        p = [x*y for x in a for y in b]
        return min(p), max(p)
    def scale(a, r): return mul(a, (F(r), F(r)))
    def contains(a, b): return a[0] <= b[0] <= b[1] <= a[1]
    def cv(z): return [iv(z[k]) for k in ['re', 'im']]
    def ca(a, b): return [add(a[k], b[k]) for k in range(2)]
    def cs(a, r): return [mul(a[k], r) for k in range(2)]
    def dot(a, b): return add(mul(a[0], b[0]), mul(a[1], b[1]))

    need(d['status'] in ['POSITIVE_PAID', 'INCONCLUSIVE_WIDTH'], 'completed mathematical enclosure')
    need(d['N'] == d['completed_through'] == 690988, 'complete intended support')
    for name, h in d['hashes'].items():
        path = HERE/name if name != 'rational_replay_140.py' else HERE.parent/'centred-moment'/name
        need(hashlib.sha256(path.read_bytes()).hexdigest() == h, 'input hash '+name)
    for name, g in d['gates'].items():
        need(g['passed'], 'gate '+name)
        if name not in ['audited_anchor_passed', 'complete_support']:
            need(iv(g['evidence'])[0] > 0, 'strict margin '+name)
    anchor = json.loads((HERE/'independent-audit-150.json').read_text())
    need(contains(iv(d['anchor_F']), iv(anchor['result']['F'])), 'audited anchor exact inclusion')
    N, pos, prime_total = d['N'], 1, 0
    prime = bytearray(b'\x01')*(N+1)
    prime[:2] = b'\x00\x00'
    for p in range(2, isqrt(N)+1):
        if prime[p]:
            prime[p*p:N+1:p] = b'\x00'*((N-p*p)//p+1)
    sums = {k: [(F(0), F(0)), (F(0), F(0))] for k in ['A', 'L', 'At', 'Lt']}
    for j, b in enumerate(d['blocks']):
        need(b['lo'] == pos and b['count'] == b['hi']-b['lo']+1 and b['hi'] <= N,
             f'block{j} adjacency and count')
        need(b['all_term_gates_passed'] and int(b['min_amplitude_lower']) > 0
             and int(b['min_prime_reduction_margin']) > 0, f'block{j} elementary domains')
        need(b['prime_count'] == sum(prime[b['lo']:b['hi']+1]), f'block{j} prime count')
        for k in sums:
            for c, v in enumerate(cv(b['sums'][k])):
                sums[k][c] = add(sums[k][c], v)
        pos, prime_total = b['hi']+1, prime_total+b['prime_count']
    need(pos == N+1 and prime_total == d['prime_count'] == sum(prime), 'every required integer and prime')
    for k in sums:
        need(sums[k] == cv(d['sums'][k]), 'exact complete block sum '+k)
    r, c = d['result'], d['constants']
    A, L, At, Lt = [sums[k] for k in ['A', 'L', 'At', 'Lt']]
    ell, ellt = iv(c['ell']), iv(c['ell_prime'])
    S = ca(cs(A, ell), cs(L, (F(-2), F(-2))))
    St = ca(ca(cs(A, ellt), cs(At, ell)), cs(Lt, (F(-2), F(-2))))
    need(all(contains(a, b) for a, b in zip(cv(r['S']), S)), 'S inclusion')
    need(all(contains(a, b) for a, b in zip(cv(r['S_derivative']), St)), 'S derivative inclusion')
    D = add(dot(At, cv(r['S'])), dot(A, cv(r['S_derivative'])))
    need(contains(iv(r['F_derivative']), D), 'complete F derivative inclusion')
    elapsed = iv(r['elapsed'])
    need(elapsed[0] == 0 and elapsed[1] >= F(1, 5)-F(98, 625), 'full closed elapsed interval')
    propagated = add(iv(d['anchor_F']), mul(elapsed, iv(r['F_derivative'])))
    need(contains(iv(r['F_propagated']), propagated), 'mean value propagation inclusion')
    rho2 = sum(max(abs(x) for x in part)**2 for part in A)
    radius = iv(r['R_upper_enclosure'])
    need(radius[0] == 0 and radius[1]**2 >= rho2, 'norm upper bound by exact square comparison')
    p, q = F(101, 200000000), F(142, 10000000)+F(1, 250000000000)
    need(contains(iv(r['p']), (p, p)) and contains(iv(r['q']), (q, q)), 'exact p and q')
    E = add(add(scale(add(scale(radius, 25), (F(81, 2), F(81, 2))), p),
                scale(radius, q)), (p*q, p*q))
    need(contains(iv(r['E']), E), 'complete scalar payment including pq')
    expected_paid = (iv(r['F_propagated'])[0]-iv(r['E'])[1],
                     iv(r['F_propagated'])[1]-iv(r['E'])[0])
    paid = iv(r['F_minus_E'])
    need(contains(paid, expected_paid), 'final paid interval inclusion')
    need(r['required_positive_threshold'] == '0', 'required strict zero threshold')
    required_D = (iv(r['E'])[1]-iv(d['anchor_F'])[0])/(F(1, 5)-F(98, 625))
    derivative = iv(r['F_derivative'])
    need(-145424 < derivative[0] < -145423 and 136035 < derivative[1] < 136036,
         'stated rational derivative endpoints')
    need(-3480 < required_D < -3479, 'required derivative lower threshold')
    need(-6133 < paid[0] < -6132 and 6027 < paid[1] < 6028,
         'stated rational paid endpoints')
    need(radius[1] < F(677, 100) and iv(r['E'])[1] < F(203, 10**6),
         'stated rational norm and payment upper bounds')
    if d['status'] == 'INCONCLUSIVE_WIDTH':
        need(paid[0] < 0 < paid[1], 'zero remains inside unpaid enclosure')
        need(d['failures'] == ['whole_edge_derivative_enclosure_does_not_pay_zero_threshold'],
             'honest inconclusive failure record')
    else:
        need(paid[0] > 0 and not d['failures'], 'positive paid classification')
    result = {'status': 'PASS' if not failures else 'FAIL', 'checks': checks,
              'failures': failures, 'blocks': len(d['blocks']), 'N': N,
              'required_derivative_lower_strictly_above': str(required_D),
              'actual_derivative_lower': str(derivative[0]),
              'qualification': 'Endpoint and block verification, not independent elementary replay.'}
    OUT.write_text(json.dumps(result, separators=(',', ':'))+'\n')
    print(json.dumps({'status': result['status'], 'checks': len(checks),
                      'failures': failures, 'blocks': len(d['blocks']), 'path': str(OUT)}))
    assert not failures


if __name__ == '__main__':
    main()
