#!/usr/bin/env python3
"""Inspect all saved partial blocks and identify the failed cap; no retry.

Exact Fraction block accounting. The separate short diagnostic uses the
established dyadic log routine only on the unfinished block, never sums
its physical coefficients or resumes the failed enclosure.
"""
from fractions import Fraction as F
from pathlib import Path
from math import isqrt
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'centred-moment'))
from rational_replay_140 import IV, Q, log_point

OUT = HERE/'time-taylor-partial-inspection-154.json'


def main():
    d = json.loads((HERE/'time-taylor-154.json').read_text())
    checks, failures = [], []

    def need(ok, name):
        checks.append({'name': name, 'passed': bool(ok)})
        if not ok:
            failures.append(name)

    def iv(z):
        den = 1 << z['denominator_power_two']
        return F(int(z['lo']), den), F(int(z['hi']), den)

    def add(a, b):
        return a[0]+b[0], a[1]+b[1]

    def load(z):
        assert z['denominator_power_two'] == 256
        return IV.raw(int(z['lo']), int(z['hi']))

    need(d['status'] == 'FAILED' and d['failures'] == ['AssertionError: '], 'honest failed status')
    need('result' not in d and 'product_trace' not in d, 'no final polynomial or sign claim')
    for name, h in d['hashes'].items():
        need(hashlib.sha256((HERE.parent/name).read_bytes()).hexdigest() == h, 'hash '+name)
    for name, g in d['gates'].items():
        need(g['passed'], 'startup gate '+name)
    N, pos = d['N'], 1
    prime = bytearray(b'\x01')*(N+1)
    prime[:2] = b'\x00\x00'
    for p in range(2, isqrt(N)+1):
        if prime[p]:
            prime[p*p:N+1:p] = b'\x00'*((N-p*p)//p+1)
    totals = {key: [[(F(0), F(0)) for _ in range(2)] for _ in range(13)] for key in ['A', 'L']}
    remainders = {'rhoA': (F(0), F(0)), 'rhoL': (F(0), F(0))}
    for i, b in enumerate(d['blocks']):
        need(b['lo'] == pos and b['count'] == b['hi']-b['lo']+1, f'block{i} adjacency')
        need(b['all_term_gates_passed'] and int(b['min_amplitude_lower']) > 0
             and int(b['min_prime_reduction_margin']) > 0, f'block{i} elementary gates')
        need(0 <= int(b['max_v_upper']) <= 2*Q, f'block{i} auxiliary cap')
        need(b['prime_count'] == sum(prime[b['lo']:b['hi']+1]), f'block{i} prime count')
        for key in totals:
            need(len(b['coefficients'][key]) == 13, f'block{i} coefficient count '+key)
            for j, z in enumerate(b['coefficients'][key]):
                for c, name in enumerate(['re', 'im']):
                    totals[key][j][c] = add(totals[key][j][c], iv(z[name]))
        for key in remainders:
            remainders[key] = add(remainders[key], iv(b[key]))
        pos = b['hi']+1
    need(pos == d['completed_through']+1 and pos <= N, 'partial support, explicitly incomplete')
    for key in totals:
        for j, z in enumerate(d['totals'][key]):
            for c, name in enumerate(['re', 'im']):
                need(totals[key][j][c] == iv(z[name]), f'exact total {key} {j} {name}')
    for key in remainders:
        need(remainders[key] == iv(d['remainders'][key]), 'exact accumulated '+key)
    # Inspect just the failed block's auxiliary condition. No physical phases,
    # A/L coefficients, new cap, continuation or final sign are computed here.
    au, av, h = [load(d['constants'][key]) for key in ['alpha_re', 'alpha_im', 'h']]
    first = None
    diagnostics = []
    for n in range(pos, min(N, pos+d['block_size']-1)+1):
        k = log_point(F(n))
        r, q = h*(k*k/4-au*k/2), -h*av*k/2
        # In this block r and q are strictly negative, so this signed sum
        # supplies a lower as well as an upper bound on the true majorant.
        need(r.h < 0 and q.h < 0, f'diagnostic signs n={n}')
        v = -r-q
        if v.h > 2*Q:
            first = n
            need(v.l > 2*Q, 'first cap failure has strict lower endpoint >2')
            diagnostics.append({'n': n, 'v': v.enc(), 'required_upper': '2',
                                'excess_over_2': (v-2).enc()})
            break
    need(first is not None, 'failed cap located in unfinished block')
    record = {'status': 'PASS_PARTIAL_INSPECTION' if not failures else 'FAIL',
              'qualification': 'Partial record inspection and failed-cap diagnostic only; no sign certificate.',
              'source_certificate_sha256': hashlib.sha256((HERE/'time-taylor-154.json').read_bytes()).hexdigest(),
              'checks': checks, 'failures': failures, 'completed_through': d['completed_through'],
              'required_support': N, 'first_failed_cap_direct_log': first,
              'diagnostics': diagnostics}
    OUT.write_text(json.dumps(record, separators=(',', ':'))+'\n')
    print(json.dumps({'status': record['status'], 'checks': len(checks), 'failures': failures,
                     'completed': d['completed_through'], 'required': N,
                     'first_failed_cap': first,
                     'v': [float(F(int(z), Q)) for z in [diagnostics[0]['v']['lo'], diagnostics[0]['v']['hi']]] if diagnostics else None,
                     'required_upper': 2, 'path': str(OUT)}))


if __name__ == '__main__':
    main()
