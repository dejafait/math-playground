"""Audit every feature/term record and the full-time rational budget.

Weak-integral table enclosures rely on the generator's outward induction;
this audit independently checks coverage, exact coefficients and contraction.
"""
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

from check_continuum_pure_sectors import operators
from check_continuum_tensor import product_terms

ROOT = Path(__file__).parent
PATH = ROOT/'full-time-sensitivity-enclosure-certificate.json'


def nested(x):
    return tuple(nested(y) for y in x) if isinstance(x, list) else x


def up(a, b):
    return -((-a)//b)


def main():
    data = json.loads(PATH.read_text())
    scale = int(data['scale'])
    assert scale == 10**80 and data['cutoff'] == 112 and data['eta'] == '1/1000000000000'
    source = ROOT/data['input_path']
    assert hashlib.sha256(source.read_bytes()).hexdigest() == data['input_sha256']
    z = isqrt(scale*scale//8)
    assert data['zero_amplitude_interval'] == dict(lo=str(z), hi=str(z+1))
    assert int(data['pi_interval']['lo']) > 3*scale
    assert len(data['heat_upper']) == 113
    assert all(0 <= int(x) <= scale for x in data['heat_upper'])
    tables = {}
    for row in data['feature_tables']:
        key = row['alpha'], row['component'], row['axis'], nested(row['key'])
        assert key not in tables
        b, d = int(row['baseline_upper']), int(row['allowance_upper'])
        assert b >= 0 and d >= 0
        tables[key] = b, d
    algebra = [operators(pair) for pair in ((0, 2), (1, 3))]
    products = {(alpha, i, c): product_terms(algebra[alpha][0][i], algebra[alpha][1], c)
                for alpha in range(2) for i in range(2) for c in range(4)}
    expected = {(alpha, c, j, key[j]) for (alpha, i, c), op in products.items()
                for key in op for j in range(4)}
    assert set(tables) == expected
    seen, totals = set(), [0, 0]
    for row in data['collected_terms']:
        alpha, c, i = row['alpha'], row['component'], (3, 6).index(row['probe'])
        key = nested(row['key'])
        label = alpha, i, c, key
        assert label not in seen
        seen.add(label)
        coefficient = products[alpha, i, c][key]
        assert F(row['coefficient']) == coefficient
        # Enumerate all 15 nonempty perturbation subsets, independently of
        # the generator's recurrence. Outward recurrence may be larger.
        entries = [tables[alpha, c, j, key[j]] for j in range(4)]
        raw = 0
        for mask in range(1, 16):
            p = 1
            for j, (b, d) in enumerate(entries):
                p *= d if mask & (1 << j) else b
            raw += p
        subset_upper = up(raw, scale**3)
        recurrence_upper = int(row['initial_allowance_upper'])
        assert subset_upper <= recurrence_upper
        # Recompute recurrence exactly to detect even small altered records.
        p, e = scale, 0
        for b, d in entries:
            p, e = up(p*b, scale), up(e*(b+d), scale)+up(p*d, scale)
        assert e == recurrence_upper
        v = abs(coefficient)
        contribution = up(v.numerator*e, v.denominator)
        assert contribution == int(row['contribution_upper'])
        totals[i] += contribution
    assert seen == {(alpha, i, c, key) for (alpha, i, c), op in products.items() for key in op}
    assert totals == [int(x) for x in data['initial_heat_allowance_upper']]
    factor = F(8)*F(64, 27)**3
    assert F(data['full_time_multiplier']) == factor
    bounds = [up(x*factor.numerator, factor.denominator) for x in totals]
    assert bounds == [int(x) for x in data['full_time_sensitivity_upper']]
    assert all(x < b*scale for x, b in zip(bounds, (100, 1000)))
    assert data['passed'] and not data['failures'] and not data['signed_response_enclosed']
    audit = dict(status='PASS', feature_records_checked=len(tables),
                 collected_terms_checked=len(seen), nonempty_subsets_per_term=15,
                 actual_upper=data['full_time_decimal_upper'], required=[100, 1000], failures=[],
                 certificate_sha256=hashlib.sha256(PATH.read_bytes()).hexdigest(),
                 qualification='All aggregate records checked; base weak-integral tables rely on generator interval arithmetic, not an independent reevaluation.')
    output = PATH.with_name('full-time-sensitivity-enclosure-audit.json')
    output.write_text(json.dumps(audit, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', features=len(tables), terms=len(seen),
                          actual_upper=audit['actual_upper'], required=audit['required'],
                          failures=[], path=str(output))))


if __name__ == '__main__':
    main()
