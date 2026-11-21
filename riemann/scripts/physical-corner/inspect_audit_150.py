#!/usr/bin/env python3
"""Exhaustive Fraction endpoint checks and comparisons; imports no evaluator."""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib
import json

HERE = Path(__file__).resolve().parent
OUT = HERE/'inspection-150.json'


def main():
    replay = json.loads((HERE/'independent-audit-150.json').read_text())
    original = json.loads((HERE/'certificate-148.json').read_text())
    checks, failures = [], []

    def need(test, name):
        checks.append({'name': name, 'passed': bool(test)})
        if not test:
            failures.append(name)

    def iv(v):
        q = 1 << v['denominator_power_two']
        a, b = F(int(v['lo']), q), F(int(v['hi']), q)
        assert a <= b
        return a, b

    def add(a, b): return a[0]+b[0], a[1]+b[1]
    def mul(a, b):
        v = [x*y for x in a for y in b]
        return min(v), max(v)
    def sub(a, b): return a[0]-b[1], a[1]-b[0]
    def scale(a, b): return mul(a, (F(b), F(b)))
    def contains(a, b): return a[0] <= b[0] <= b[1] <= a[1]
    def overlap(a, b): return max(a[0], b[0]) <= min(a[1], b[1])

    need(replay['status'] == 'PASS' and replay['failures'] == [], 'successful full replay')
    need(replay['source_sha256'] == hashlib.sha256((HERE/'independent_audit_150.py').read_bytes()).hexdigest(), 'replay source hash')
    need(all(v['passed'] for v in replay['gates'].values()), 'every replay gate passed')
    # Every constant is compared; numerical agreement is not used as a premise.
    for name, v in replay['constants'].items():
        need(overlap(iv(v), iv(original['constants'][name])), 'carrier comparison '+name)
    for name in ['floor_lower', 'floor_upper', 'ell_logN_gt13', 'shift_gt0', 'shift_lt25']:
        need(iv(replay['gates'][name]['evidence'])[0] > 0, 'strict carrier margin '+name)
    need(replay['N'] == replay['completed_through'] == original['N'] == 690988, 'exact required support')
    N = replay['N']
    prime = bytearray(b'\x01')*(N+1)
    prime[:2] = b'\x00\x00'
    for p in range(2, isqrt(N)+1):
        if prime[p]:
            prime[p*p:N+1:p] = b'\x00'*((N-p*p)//p+1)
    totals = {name: [(F(0), F(0)), (F(0), F(0))] for name in ['A', 'L']}
    position, direct, primes, width = 1, 0, 0, 0
    need(len(replay['blocks']) == len(original['blocks']) == 338, '338 exhaustive blocks')
    for j, b in enumerate(replay['blocks']):
        o = original['blocks'][j]
        need(b['lo'] == position and b['count'] == b['hi']-b['lo']+1
             and b['lo'] == o['lo'] and b['hi'] == o['hi'], f'block{j} exact contiguous support')
        need(b['all_term_gates_passed'] and int(b['min_amplitude']) > 0
             and int(b['min_reduction_margin']) > 0, f'block{j} all elementary domains')
        need(b['direct_phases'] == b['count']-int(b['lo'] == 1), f'block{j} direct phases')
        need(b['prime_count'] == sum(prime[b['lo']:b['hi']+1]), f'block{j} independent prime count')
        width = max(width, int(b['max_elementary_width']))
        need(F(int(b['max_elementary_width']), 1 << replay['bits']) < F(1, 10**30), f'block{j} full widths below1e-30')
        for name in ['A', 'L']:
            for k, part in enumerate(['re', 'im']):
                v = iv(b[name+'_block'][part])
                totals[name][k] = add(totals[name][k], v)
                need(overlap(v, iv(o[name+'_block'][part])), f'block{j} {name}.{part} comparison')
        position = b['hi']+1
        direct += b['direct_phases']
        primes += b['prime_count']
    need(position == N+1 and direct == N-1 and primes == sum(prime), 'complete direct replay counts')
    for name in ['A', 'L']:
        for j, part in enumerate(['re', 'im']):
            need(totals[name][j] == iv(replay['sums'][name][part]), name+'.'+part+' exact block-endpoint sum')
    A, L = totals['A'], totals['L']
    r = replay['result']
    S = [iv(r['S'][part]) for part in ['re', 'im']]
    for j in range(2):
        need(contains(S[j], sub(mul(iv(replay['constants']['ell']), A[j]), scale(L[j], 2))), f'S component{j} exact inclusion')
    norm = add(mul(A[0], A[0]), mul(A[1], A[1]))
    R = iv(r['R'])
    need(0 < R[0] and R[0]**2 <= norm[0] <= norm[1] <= R[1]**2, 'norm square inequalities')
    value = add(mul(A[0], S[0]), mul(A[1], S[1]))
    need(contains(iv(r['F']), value), 'F endpoint recomputation')
    p, q = F(101, 200000000), F(142, 10000000)+F(1, 250000000000)
    payment = add(add(scale(add(scale(R, 25), (F(81, 2), F(81, 2))), p), scale(R, q)), (p*q, p*q))
    need(contains(iv(r['p']), (p, p)) and contains(iv(r['q']), (q, q)), 'exact p and q')
    need(contains(iv(r['E']), payment), 'complete payment including pq')
    need(contains(iv(r['F_minus_E']), sub(iv(r['F']), iv(r['E'])))
         and contains(iv(r['F_plus_E']), add(iv(r['F']), iv(r['E']))), 'both scalar endpoints included')
    for name, low, high in [('F', '150.30628', '150.30629'), ('R', '2.49096', '2.49097'), ('E', '0.00008727', '0.00008728')]:
        a, b = iv(r[name])
        need(F(low) < a <= b < F(high), name+' exact printed bounds')
    need(iv(r['F_minus_E'])[0] > F('150.30619'), 'strict required paid reserve')
    for name in ['F', 'R', 'E', 'F_minus_E', 'F_plus_E', 'p', 'q']:
        need(overlap(iv(r[name]), iv(original['result'][name])), name+' final comparison')
    output = {'status': 'PASS' if not failures else 'FAIL', 'checks': checks, 'failures': failures,
              'actual_paid_lower': r['F_minus_E'], 'required_paid_lower': '150.30619',
              'blocks': len(replay['blocks']), 'direct_nonconstant_phases': direct, 'prime_count': primes,
              'maximum_elementary_width': {'numerator': str(width), 'denominator_power_two': replay['bits']},
              'replay_sha256': hashlib.sha256((HERE/'independent-audit-150.json').read_bytes()).hexdigest(),
              'original_sha256': hashlib.sha256((HERE/'certificate-148.json').read_bytes()).hexdigest(),
              'qualification': 'Endpoint inspection supplements the independently implemented elementary replay; comparisons are not numerical premises.'}
    OUT.write_text(json.dumps(output, separators=(',', ':'))+'\n')
    print(json.dumps({'status': output['status'], 'checks': len(checks), 'blocks': output['blocks'],
          'actual_bound': 'F-E>150.30619' if not failures else 'unconfirmed', 'required': '>150.30619',
          'failures': failures, 'path': str(OUT)}))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
