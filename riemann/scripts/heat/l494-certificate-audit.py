#!/usr/bin/env python3
"""Consume the complete L494 scalar certificate with independent exact sums.

This validates scalar evidence only. The analytic audit is in canonical L494.
No producer module or floating point library supplies the exponential bounds.
"""
from decimal import Decimal, localcontext, ROUND_CEILING
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'frozen-cutoff-cauchy-certificate.json'
OUTPUT = HERE / 'l494-certificate-audit.json'
original = SOURCE.read_bytes()
data = json.loads(original)
checks = []


def fraction(value):
    return F(int(value['numerator']), int(value['denominator']))


def rational(value):
    return {'numerator': str(value.numerator), 'denominator': str(value.denominator)}


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})


def display(value):
    with localcontext() as context:
        context.prec = 19
        context.rounding = ROUND_CEILING
        return str(Decimal(value.numerator) / Decimal(value.denominator))


check('24 scalar comparisons present', len(data['checks']) == 24)
for item in data['checks']:
    actual = fraction(item['actual_upper'])
    required = fraction(item['required_strict_upper'])
    check(item['name'], actual < required and item['passed'] is True)

check('all seven exponential evaluations present', len(data['exponential_evaluations']) == 7)
evaluations = []
for index, item in enumerate(data['exponential_evaluations']):
    argument = fraction(item['argument'])
    a = abs(argument)
    check(f'exp {index}: tail ratio domain', 0 <= a < 182)
    check(f'exp {index}: producer degree', item['terms_through'] == 180)
    # Exact, unrounded Taylor terms: independent of the producer's grid recurrence.
    term = total = F(1)
    for degree in range(1, 221):
        term *= a / degree
        total += term
        if degree == 180:
            exact_sum_180, exact_term_180 = total, term
    tail_180 = exact_term_180 * a / 181 / (1 - a / 182)
    sum_lo, sum_hi = (fraction(item[k]) for k in ('positive_sum_lower', 'positive_sum_upper'))
    check(f'exp {index}: full stored positive sum', sum_lo <= exact_sum_180 <= sum_hi)
    check(f'exp {index}: full stored last term',
          fraction(item['last_term_lower']) <= exact_term_180 <= fraction(item['last_term_upper']))
    stored_tail = fraction(item['tail_upper'])
    check(f'exp {index}: full stored tail', stored_tail >= tail_180)
    outer_lo, outer_hi = (fraction(item[k]) for k in ('lower', 'upper'))
    if argument >= 0:
        endpoint_check = outer_lo <= sum_lo and outer_hi >= sum_hi + stored_tail
    else:
        endpoint_check = outer_lo <= 1 / (sum_hi + stored_tail) and outer_hi >= 1 / sum_lo
    check(f'exp {index}: sign and endpoint construction', endpoint_check)

    # The first omitted term is degree 221; later ratios are at most a/222.
    exact_lo, exact_hi = total, total + term * a / 221 / (1 - a / 222)
    if argument < 0:
        exact_lo, exact_hi = 1 / exact_hi, 1 / exact_lo
    grid = 10**70
    lo = F((exact_lo.numerator * grid) // exact_lo.denominator, grid)
    hi = F(-((-exact_hi.numerator * grid) // exact_hi.denominator), grid)
    nested = outer_lo <= lo <= hi <= outer_hi
    check(f'exp {index}: independent degree-220 enclosure contained', nested)
    evaluations.append({'index': index, 'argument': rational(argument),
                        'independent_terms_through': 220, 'grid_denominator': str(grid),
                        'independent_lower': rational(lo), 'independent_upper': rational(hi),
                        'stored_lower': rational(outer_lo), 'stored_upper': rational(outer_hi),
                        'contained': nested})

run = subprocess.run([sys.executable, str(HERE / 'frozen-cutoff-cauchy-certificate.py')],
                     capture_output=True, text=True)
replayed = SOURCE.read_bytes()
if original != replayed:
    SOURCE.with_name('l494-pre-audit-certificate.json').write_bytes(original)
check('producer replay succeeds', run.returncode == 0)
check('producer replay byte-identical to original evidence', original == replayed)
check('original status agrees with validated comparisons', data['result'] == 'PASS' and data['failures'] == [])
failures = [item['name'] for item in checks if not item['passed']]
result = {
    'result': 'PASS' if not failures else 'FAIL',
    'scope': 'Complete L494 scalar certificate; independent exact Taylor consumption and producer replay. Analytic reduction and imported saddle theorem are not proved by this script.',
    'source': 'scripts/heat/frozen-cutoff-cauchy-certificate.json',
    'source_sha256': sha256(original).hexdigest(),
    'replay_sha256': sha256(replayed).hexdigest(),
    'independent_method': 'Unrounded rational Taylor terms through 220, geometric tail with first omitted term 221 and later ratio <= abs(argument)/222; invert for negative arguments; outward 10^-70 endpoints.',
    'exponential_evaluations': evaluations,
    'checks': checks,
    'scalar_comparisons': data['checks'],
    'producer_replay_stdout': run.stdout,
    'producer_replay_stderr': run.stderr,
    'failures': failures,
}
OUTPUT.write_text(json.dumps(result, indent=2) + '\n')
for item in data['checks']:
    print(f"{item['name']}: actual upper {display(fraction(item['actual_upper']))}; required < {display(fraction(item['required_strict_upper']))}")
print(f"{result['result']}: {len(checks)} checks, seven full exponential records consumed; failures={failures}; certificate={OUTPUT}")
raise SystemExit(0 if not failures else 1)
