"""Preserve the saved-table integer cross-check used in L110.

This is construction verification, not the later separate critical audit.
Every exact ratio remains losslessly factored in the input certificate.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

B = Path(__file__).resolve().parent
SOURCE = B/'equilateral-capacity-allowance.json'
OUT = B/'equilateral-capacity-saved-verification.json'
r = json.loads(SOURCE.read_text())
N = r['N']
E = {z['i']: z['E'] for z in r['equilateral_counts']}
P = r['pair_numerators']
M = F(N-2, E[5])
maxcube = F(*r['maximum']['ratio_cube'])
checks = []


def ck(name, test):
    checks.append(dict(name=name, passed=bool(test)))


ck('exact_equilateral_maximum', M**3 == maxcube)
ck('distance_five_count', E[5] == 89469195005112)
ck('exact_maximum_bracket', F(*r['maximum']['ratio_lower']) <= M < F(*r['maximum']['ratio_strict_upper']))
seen = set()
counts = dict(below_one=0, above_one=0, equal_one=0)
for row in r['permitted_side_classes']:
    i,j,h = row['distances']
    ck(f'unique_{i}_{j}_{h}', (i,j,h) not in seen)
    seen.add((i,j,h))
    b = min(P[i],P[j],P[h])
    num = (N-2)**3*P[i]*P[j]*P[h]
    den = E[i]*E[j]*E[h]*b**3
    ck(f'positive_denominator_{i}_{j}_{h}', den > 0)
    ck(f'bounded_by_maximum_{i}_{j}_{h}', num*maxcube.denominator <= den*maxcube.numerator)
    label = 'below_one' if num < den else 'above_one' if num > den else 'equal_one'
    ck(f'capacity_comparison_{i}_{j}_{h}', label == row['comparison_with_one'])
    counts[label] += 1
ck('comparison_counts', all(r[k] == v for k,v in counts.items()))
ck('side_class_count', len(seen) == r['side_class_count'] == 28215)
ck('source_entry_count', sum(z['source_entries'] for z in r['permitted_side_classes']) == 1490200)
ck('construction_failures', r['failures'] == [])
failures = [z['name'] for z in checks if not z['passed']]
report = dict(source_path=str(SOURCE.relative_to(B.parent.parent)),
              source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              scope='Saved-table integer comparisons only; not separate critical review.',
              exact_maximum_allowance=[M.numerator,M.denominator],
              required_maximum_at_most=1, comparisons=counts,
              check_count=len(checks), checks=checks, failures=failures)
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(f'Saved factor verification: {len(checks)} exact checks; failures: {failures}')
print('All 28215 ratio cubes <= the stated maximum; maximum allowance = (N-2)/89469195005112 > required 1.')
print(f'Full verification certificate: {OUT}')
assert not failures
