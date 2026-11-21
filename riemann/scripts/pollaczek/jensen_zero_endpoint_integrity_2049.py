#!/usr/bin/env python3
"""Check complete stored endpoint sums and readable bounds, not products.

Run from riemann: python3 scripts/pollaczek/jensen_zero_endpoint_integrity_2049.py
An independent coefficient/Newton/determinant-product audit remains separate.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations
import hashlib
import json
import sys

sys.set_int_max_str_digits(0)


def main():
    p = Path(__file__).with_name('jensen-zero-endpoint-2049.json')
    x = json.loads(p.read_text())

    def iv(v):
        return F(v['lower']), F(v['upper'])

    checks = {}
    checks['script_hash'] = hashlib.sha256(p.with_name('jensen_zero_endpoint_2049.py').read_bytes()).hexdigest() == x['script_sha256']
    checks['all_checks_and_no_failures'] = all(x['checks'].values()) and not x['failures'] and not x['unresolved_determinants']
    checks['normalization_strict_negative'] = iv(x['normalization_denominator'])[1] < 0
    checks['all_saved_newton_intervals_ordered'] = all(iv(v)[0] <= iv(v)[1] for v in x['newton_sums_0_to_10'])
    for n, m in enumerate(x['minors'], 1):
        perms = [tuple(t['permutation_zero_based']) for t in m['terms']]
        checks[f'minor{n}_complete_expression'] = sorted(perms) == list(permutations(range(n)))
        checks[f'minor{n}_parities'] = all(t['sign'] == (-1)**sum(a[i] > a[j] for i in range(n) for j in range(i+1, n)) for t, a in zip(m['terms'], perms))
        total = tuple(sum((iv(t['signed_product_interval'])[j] for t in m['terms']), F(0)) for j in (0, 1))
        checks[f'minor{n}_full_endpoint_sums'] = total == iv(m['interval'])
        r = m['readable_outer_enclosure']
        outer = tuple(t*F(10)**r['power_of_ten'] for t in iv(r['scaled_interval']))
        checks[f'minor{n}_exact_outer_containment'] = outer[0] <= total[0] <= total[1] <= outer[1]
        checks[f'minor{n}_strict_sign'] = m['sign'] == (1 if total[0] > 0 else -1 if total[1] < 0 else 0) and m['sign'] != 0
    report = {
        'method': 'Complete stored rational endpoint sums, permutation completeness/parity and outward containment; no determinant-product or source-formula independent audit claimed',
        'reproduction': 'python3 scripts/pollaczek/jensen_zero_endpoint_integrity_2049.py',
        'input_sha256': hashlib.sha256(p.read_bytes()).hexdigest(),
        'checks': checks, 'failures': [k for k, v in checks.items() if not v],
    }
    out = p.with_name('jensen-zero-endpoint-integrity-2049.json')
    out.write_text(json.dumps(report, indent=2)+'\n')
    print('Certificate integrity:', len(checks), 'checks; failures:', report['failures'])
    print('Exact determinant endpoints and all 873 signed terms read without truncation; no independent product replay.')
    print('Certificate:', out.relative_to(Path.cwd()))
    assert not report['failures']


if __name__ == '__main__':
    main()
