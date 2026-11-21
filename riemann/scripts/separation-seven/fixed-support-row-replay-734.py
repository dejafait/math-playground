#!/usr/bin/env python3
"""Exact independent replay of the single load-bearing failed row.

Does not import/run the candidate constructor. Reconstructs Chebyshev
polynomials as integer coefficients and evaluates by Horner, whereas
the constructor uses a recurrence on values. All35 entries are checked.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import sys

sys.set_int_max_str_digits(0)
HERE = Path(__file__).resolve()
SOURCE = HERE.with_name('fixed-support-shared-734.json')
OUT = HERE.with_suffix('.json')
data = json.loads(SOURCE.read_text())
block = data['blocks'][0]
labels = data['parameters']['labels']
row = block['exact_failed_row']['index']
Rrow = list(map(F,data['anchor']['interpolation_preconditioner'][row]))
J = 2**block['k']
indices = [J+(i*(J-1))//128 for i in labels]
nodes = [F(4*j+1-6*J,2*J) for j in indices]
polys = [[1],[0,1]]
for n in range(2,35):
    poly = [0]*(n+1)
    for i in range(n):
        poly[i+1] += 2*polys[n-1][i]
    for i in range(n-1):
        poly[i] -= polys[n-2][i]
    polys.append(poly)


def evaluate(poly,t):
    value = F(0)
    for coefficient in reversed(poly):
        value = value*t+coefficient
    return value


entries = [F(int(row==j))-sum((r*evaluate(poly,t) for r,poly in zip(Rrow,polys)),F(0))
           for j,t in enumerate(nodes)]
norm = sum((abs(v) for v in entries),F(0))
checks = {'first_required_block_k11': block['k']==11,
          'full35_label_and_preconditioner_row': len(labels)==len(set(labels))==len(Rrow)==35,
          'exact_floor_indices_match': indices==block['indices'],
          'all35_exact_nodes_match': nodes==list(map(F,block['nodes'])),
          'all35_error_entries_match': entries==list(map(F,block['exact_failed_row']['entries'])),
          'all35_outward_intervals_contain_exact_entries': all(F(a)<=v<=F(b) for (a,b),v in zip(block['interpolation']['error_intervals'][row],entries)),
          'full_absolute_sum_matches': norm==F(block['exact_failed_row']['absolute_sum']),
          'row_norm_strictly_above_1_58635': norm>F(158635,100000),
          'row_norm_strictly_below_1_58636': norm<F(158636,100000),
          'constructor_source_hash_unchanged': data['script_sha256']==sha256(HERE.with_name('fixed-support-shared-734.py').read_bytes()).hexdigest()}
report = {'scope': 'exact row33 of I-R_A A_11 only; no quadrature or cost upper bound',
          'script_sha256': sha256(HERE.read_bytes()).hexdigest(),
          'input_sha256': sha256(SOURCE.read_bytes()).hexdigest(),
          'row': row, 'exact_error_entries': list(map(str,entries)),
          'row_absolute_sum': str(norm),
          'comparison_interval': ['1.58635','1.58636'],
          'checks': checks, 'failed_checks': [k for k,v in checks.items() if not v]}
OUT.write_text(json.dumps(report,indent=2)+'\n')
print('Exact row replay:',sum(checks.values()),'/',len(checks),'; failed:',report['failed_checks'])
print('Actual row norm in (1.58635,1.58636); strict-inclusion threshold: <1')
print('Certificate:',OUT.relative_to(HERE.parents[2]))
if report['failed_checks']:
    raise SystemExit(1)
