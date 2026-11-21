#!/usr/bin/env python3
"""Inspect ALL block records and exact final bounds; not an independent replay.

Uses Fraction endpoints, imports no generating code. Full results on disk.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
CERT = HERE / 'certificate-148.json'
OUT = HERE / 'inspection-148.json'


def main():
    data = json.loads(CERT.read_text())
    checks, failures = [], []

    def need(test, name):
        checks.append({'name': name, 'passed': bool(test)})
        if not test:
            failures.append(name)

    bits = data['bits']
    Q = 1 << bits

    def box(v):
        assert v['denominator_power_two'] == bits
        a, b = F(int(v['lo']), Q), F(int(v['hi']), Q)
        assert a <= b
        return a, b

    def add(a, b): return a[0]+b[0], a[1]+b[1]
    def neg(a): return -a[1], -a[0]
    def sub(a, b): return add(a, neg(b))
    def mul(a, b):
        v = [x*y for x in a for y in b]
        return min(v), max(v)
    def scale(a, v): return mul(a, (v, v))
    def contains(a, b): return a[0] <= b[0] <= b[1] <= a[1]
    def comp(v): return box(v['re']), box(v['im'])
    def rounded(v, lo, hi): return F(lo) < v[0] <= v[1] < F(hi)

    need(data['source_sha256'] == hashlib.sha256((HERE/'certify_148.py').read_bytes()).hexdigest(), 'generating source hash matches')
    helper = HERE.parent/'centred-moment'/'rational_replay_140.py'
    need(data['helper_sha256'] == hashlib.sha256(helper.read_bytes()).hexdigest(), 'helper hash matches')
    need(data['status'] == 'POSITIVE_PAID' and data['failures'] == [], 'completed positive result without recorded failures')
    need(len(data['gates']) == 11 and all(v['passed'] is True for v in data['gates'].values()), 'all11 global gates passed')
    # Independent elementary prime sieve for complete prime counts by block.
    N = data['N']
    prime = bytearray(b'\x01')*(N+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2, isqrt(N)+1):
        if prime[p]:
            prime[p*p:N+1:p] = b'\x00'*((N-p*p)//p+1)
    A, L = [(0, 0), (0, 0)], [(0, 0), (0, 0)]
    position, count, max_width = 1, 0, 0
    block_evidence = []
    for j, b in enumerate(data['blocks']):
        lo, hi = b['lo'], b['hi']
        need(lo == position and lo <= hi <= N and b['count'] == hi-lo+1, f'block{j} exact contiguous support')
        need(b['all_term_and_factorization_gates_passed'] is True and int(b['min_amplitude_lower']) > 0
             and int(b['min_prime_reduction_margin']) > 0, f'block{j} all term and reduction gates')
        need(b['prime_count'] == sum(prime[lo:hi+1]), f'block{j} independently checked prime count')
        widths = [int(b[k]) for k in ['max_log_width', 'max_chi_component_width', 'max_amplitude_width', 'max_prime_theta_width']]
        need(all(0 <= v < F(Q, 10**20) for v in widths), f'block{j} all recorded widths below1e-20')
        max_width = max(max_width, *widths)
        for total, name in [(A, 'A_block'), (L, 'L_block')]:
            z = comp(b[name])
            total[0], total[1] = add(total[0], z[0]), add(total[1], z[1])
        position, count = hi+1, count+b['count']
        block_evidence.append({'block': j, 'lo': lo, 'hi': hi, 'prime_count': b['prime_count']})
    need(position == N+1 and count == N == data['completed_through'] == 690988, 'all690988 integers exactly once')
    need(len(data['blocks']) == 338, 'all338 blocks present')
    need(data['prime_count'] == sum(prime), 'total prime count independently checked')
    need(tuple(A) == comp(data['sums']['A']) and tuple(L) == comp(data['sums']['L']), 'exact block endpoints sum to recorded totals')
    ell = box(data['constants']['ell'])
    r = data['result']
    S = comp(r['S'])
    for i in range(2):
        need(contains(S[i], sub(mul(ell, A[i]), scale(L[i], F(2)))), f'S component{i} independently included')
    value = add(mul(A[0], S[0]), mul(A[1], S[1]))
    recordedF = box(r['F'])
    need(contains(recordedF, value), 'F rational endpoint recomputation included')
    norm = add(mul(A[0], A[0]), mul(A[1], A[1]))
    R = box(r['R'])
    need(0 < R[0] and R[0]**2 <= norm[0] <= norm[1] <= R[1]**2, 'R exact square comparisons')
    p, q = F(101, 200000000), F(142, 10000000)+F(1, 250000000000)
    payment = add(add(scale(add(scale(R, 25), (F(81, 2), F(81, 2))), p), scale(R, q)), (p*q, p*q))
    E, paid, ceiling = box(r['E']), box(r['F_minus_E']), box(r['F_plus_E'])
    need(contains(E, payment), 'E exact rational endpoint recomputation included')
    need(contains(paid, sub(recordedF, E)) and contains(ceiling, add(recordedF, E)), 'both two-sided comparison endpoints included')
    need(rounded(recordedF, '150.30628', '150.30629'), '150.30628<F<150.30629')
    need(rounded(R, '2.49096', '2.49097'), '2.49096<R<2.49097')
    need(rounded(E, '0.00008727', '0.00008728'), '0.00008727<E<0.00008728')
    need(paid[0] > F('150.30619'), 'F-E>150.30619>0')
    result = {'status': 'PASS' if not failures else 'FAIL', 'checks': checks,
              'failures': failures, 'full_block_inspection': block_evidence,
              'maximum_recorded_width': {'numerator': str(max_width), 'denominator_power_two': bits},
              'actual_paid_lower_bound': r['F_minus_E']['lo'],
              'required_paid_lower_bound': '0', 'reported_rational_lower_bound': '150.30619',
              'certificate_sha256': hashlib.sha256(CERT.read_bytes()).hexdigest(),
              'qualification': 'Complete record/endpoint inspection; not independent transcendental replay.'}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'status': result['status'], 'checks': len(checks), 'blocks': len(block_evidence),
                      'failures': failures, 'actual_paid_lower_bound': '>150.30619', 'required': '>0', 'path': str(OUT)}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
