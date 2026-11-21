"""Replay equality and exact load-bearing comparisons for the L719--L720 audit."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).parent
original = ROOT / 'analytic-symbol-saddle-certificate-190.json'
replayed = ROOT / 'analytic-symbol-saddle-replay-192.json'
old, new = (json.loads(p.read_text()) for p in (original, replayed))


def rational(record):
    return F(record['numerator'], record['denominator'])


def encode(x):
    return {'numerator': x.numerator, 'denominator': x.denominator}


rows = []
for name, row in new['checks'].items():
    actual, required = rational(row['actual']), rational(row['required'])
    relation = row['relation']
    assert relation in ('<', '>')
    passed = actual < required if relation == '<' else actual > required
    rows.append({'name': name, 'actual': encode(actual), 'relation': relation,
                 'required': encode(required), 'passed': passed,
                 'matches_report': passed == row['passed']})

extra = {
    'complex_local_s_pole_separation':
        (F(7, 20) - F(21, 8) * F(101, 899), F(1, 20)),
    'quadratic_real_phase_coefficient':
        ((F(24, 35) - F(1, 10)) ** 2 / 6, F(1, 20)),
}
for name, (actual, required) in extra.items():
    rows.append({'name': name, 'actual': encode(actual), 'relation': '>',
                 'required': encode(required), 'passed': actual > required,
                 'matches_report': True})

checks = {
    'complete_certificate_equality': old == new,
    'all_moment_rows_present': len(new['moment_rows']) == 80,
    'all_sum_rows_present': len(new['sum_rows']) == 80,
    'original_check_count': len(new['checks']) == 15,
    'reported_failures_empty': new['failures'] == [],
    'all_exact_comparisons': all(r['passed'] and r['matches_report'] for r in rows),
}
failures = [name for name, passed in checks.items() if not passed]
result = {
    'purpose': __doc__,
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'input_paths': [str(original), str(replayed)],
    'input_sha256': [hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (original, replayed)],
    'checks': checks, 'comparisons': rows, 'failures': failures,
    'qualification': 'Exact replay and scalar checks only; analytic audit is canonical in L719 Section 7 and L720 Section 5.',
}
output = Path(__file__).with_suffix('.json')
output.write_text(json.dumps(result, indent=2) + '\n')
print('Full certificate equality:', checks['complete_certificate_equality'])
print('Original rational comparisons:', len(new['checks']), '; all pass:', checks['all_exact_comparisons'])
for name, (actual, required) in extra.items():
    print(f'{name}: actual {actual} > required {required}; pass={actual > required}')
print('Failures:', failures, '; full audit certificate:', output)
if failures:
    raise SystemExit(1)
