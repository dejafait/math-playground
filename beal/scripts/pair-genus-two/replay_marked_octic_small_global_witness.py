#!/usr/bin/env python3
"""Independent arithmetic replay of the eight-product certificate.

Uses companion shifts and permutation determinants, not producer imports.
This arithmetic replay is not a separate critical mathematical audit.
"""
from fractions import Fraction as Q
from itertools import permutations, product
from pathlib import Path
import json

BASE = Path(__file__).parent
SOURCE = BASE / 'marked-octic-small-global-witness-certificate.json'
OUT = BASE / 'marked-octic-small-global-witness-replay.json'


def main():
    data = json.loads(SOURCE.read_text())
    loc = json.loads((BASE / data['local_input']['path']).read_text())
    checks, evidence = [], []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required, passed=actual == required))

    f = list(map(Q, [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]))

    def theta_times(a):
        return [Q(0)]+a[:-1] if not a[-1] else [([Q(0)]+a[:-1])[i]-a[-1]*f[i]/275 for i in range(8)]

    norms = [Q(1), Q(1024, 275), Q(1024, 275), Q(1024, 275)**2,
             Q(243, 275), Q(243*1024, 275**2), Q(243*1024, 275**2), Q(243*1024**2, 275**3)]
    check('all eight exponent vectors in order', [r['exponents'] for r in data['rows']], list(map(list, product(range(2), repeat=3))))
    for k, row in enumerate(data['rows']):
        abc = row['exponents']
        coeff = [Q(1)]+[Q(0)]*7
        for bit, sign, constant in zip(abc, (1, -1, 1), (0, 1, 1)):
            if bit:
                shifted = theta_times(coeff)
                coeff = [constant*a+sign*b for a, b in zip(coeff, shifted)]
        check(f'row {k} coordinates', list(map(str, coeff)), row['coordinates'])
        columns = []
        column = coeff
        for j in range(8):
            columns.append(column)
            column = theta_times(column)
        matrix = [[columns[j][i] for j in range(8)] for i in range(8)]
        check(f'row {k} full matrix', [[str(x) for x in r] for r in matrix], row['norm_evidence']['matrix'])
        terms = []
        for perm in permutations(range(8)):
            if any(not matrix[i][perm[i]] for i in range(8)):
                continue
            sign = (-1)**sum(perm[i] > perm[j] for i in range(8) for j in range(i+1, 8))
            value = Q(sign)
            for i in range(8):
                value *= matrix[i][perm[i]]
            terms.append(dict(permutation=perm, signed_product=str(value)))
        determinant = sum((Q(t['signed_product']) for t in terms), Q(0))
        check(f'row {k} permutation determinant', str(determinant), row['norm_evidence']['norm'])
        check(f'row {k} direct norm formula', determinant, norms[k])
        evidence.append(dict(exponents=abc, nonzero_determinant_terms=terms))

    # Recompute (-4r)/pi^10 by a separate quotient multiplication.
    e = list(map(Q, loc['field']['monic_E']))

    def multiply(a, b):
        result = [Q(0)]*7
        for i in range(4):
            for j in range(4):
                result[i+j] += a[i]*b[j]
        for i in range(6, 3, -1):
            for j in range(4):
                result[i-4+j] -= result[i]*e[j]
        return result[:4]

    inverse_pi = [-e[i]/e[0] for i in range(1, 5)]
    check('exact pi inverse', multiply([Q(0), Q(1), Q(0), Q(0)], inverse_pi), [Q(1), Q(0), Q(0), Q(0)])
    normalized = [-4*Q(x) for x in loc['field']['r']]
    for i in range(10):
        normalized = multiply(normalized, inverse_pi)
    residue = [c.numerator*pow(c.denominator, -1, m) % m for c, m in zip(normalized, (8, 4, 4, 4))]
    check('exact normalized diagonal residue', residue, [1, 2, 3, 3])
    label = next(row['label'] for row in loc['residue_ring']['complete_unit_cosets'] if row['residue'] == residue)
    check('exact diagonal field class', label, 25)
    check('diagonal class is outside rational scalar image', label not in loc['scalar_labels'], True)
    table = loc['residue_ring']['unit_multiplication_table']
    orbit = sorted([table[label][s], table[label][s]] for s in loc['scalar_labels'])
    check('all common scalar orbit representatives', orbit, data['rows'][3]['common_scalar_orbit'])
    check('canonical witness class', min(orbit), [1, 1])
    check('rejected by exact point image', min(orbit) not in loc['point_image'], True)
    failures = [x['name'] for x in checks if not x['passed']]
    output = dict(checks=checks, failures=failures, full_determinant_terms=evidence,
                  witness_normalized_coefficients=list(map(str, normalized)),
                  witness_residue=residue, witness_scalar_orbit=orbit)
    def clean(x):
        if isinstance(x, Q):
            return str(x)
        if isinstance(x, dict):
            return {k: clean(v) for k, v in x.items()}
        if isinstance(x, (tuple, list)):
            return [clean(v) for v in x]
        return x
    OUT.write_text(json.dumps(clean(output), indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks), failures=failures, rows=8, required_rows=8,
                          residue=residue, required_residue=[1, 2, 3, 3],
                          class_outside_point_image=[1, 1], path=str(OUT))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
