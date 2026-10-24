#!/usr/bin/env python3
"""Arithmetic replay of bounded linear test, without importing its producer.

Reuses L123's audited full multiplication-matrix norm and L122 arithmetic.
Enumerates all 32 products directly, independently of F2 elimination.
This is not the later critical mathematical audit.
"""
from fractions import Fraction as Q
from itertools import product
from math import gcd
from pathlib import Path
import json

import marked_octic_small_global_witness as global_arithmetic
import marked_octic_two_adic_image as local

BASE = Path(__file__).parent
SOURCE = BASE / 'marked-octic-bounded-linear-certificate.json'
OUT = BASE / 'marked-octic-bounded-linear-replay.json'


def main():
    cert = json.loads(SOURCE.read_text())
    old = json.loads((BASE / 'marked-octic-two-adic-image-certificate.json').read_text())
    checks, norm_rows, generator_rows = [], [], []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required, passed=actual == required))

    expected_pairs = [(a, b) for a in range(-16, 17) for b in range(1, 17) if gcd(a, b) == 1]
    check('exact complete coprime pair list', [(row['a'], row['b']) for row in cert['pair_decisions']], expected_pairs)
    eligible = []
    for i, row in enumerate(cert['pair_decisions']):
        a, b = row['a'], row['b']
        nd = global_arithmetic.gnorm(tuple(map(Q, [a, -b]+[0]*6)))
        fac = global_arithmetic.factor(nd['norm'])
        check('full determinant norm '+str(i), str(nd['norm']), row['norm_data']['norm'])
        allowed = fac['numerator_remainder'] == fac['denominator_remainder'] == 1
        check('exact eligibility '+str(i), allowed, row['norm_data']['eligible'])
        check('complete signed norm data '+str(i),
              [fac['sign'], list(fac['exponents'].values()), fac['numerator_remainder'], fac['denominator_remainder']],
              [row['norm_data']['sign'], row['norm_data']['support_exponents'],
               row['norm_data']['numerator_remainder'], row['norm_data']['denominator_remainder']])
        if allowed:
            eligible.append((a, b))
        norm_rows.append(dict(pair=(a, b), multiplication_determinant=nd, factorization=fac, eligible=allowed))
    check('eligible pair list', eligible, [(-3, 1), (-1, 1), (0, 1), (1, 1), (3, 1)])
    check('generator exact order', [tuple(row['pair']) for row in cert['generators']], eligible)

    cosets = {tuple(row['residue']): row['label'] for row in old['residue_ring']['complete_unit_cosets']}
    table, scalars = old['residue_ring']['unit_multiplication_table'], old['scalar_labels']
    alpha = tuple(map(Q, old['field']['alpha_approximation']))

    def label(element):
        valuation = local.val(element)
        residue = local.residue(local.mul(element, local.power(local.PI, -valuation)))
        return dict(valuation=valuation, normalized_residue=residue,
                    label=32*(valuation % 2)+cosets[residue])

    def lm(a, b):
        return 32*((a//32) ^ (b//32))+table[a % 32][b % 32]

    def canonical(pair):
        return min((lm(pair[0], s), lm(pair[1], s)) for s in scalars)

    def real_canonical(bits):
        return bits ^ (255 if bits & 1 else 0)

    for i, ((a, b), row) in enumerate(zip(eligible, cert['generators'])):
        bits = 0
        for j, root in enumerate(cert['roots']):
            lo, hi = map(Q, root['interval'])
            vlo, vhi = global_arithmetic.local.ev(global_arithmetic.F, lo), global_arithmetic.local.ev(global_arithmetic.F, hi)
            check('strict sign-changing root '+str(i)+' '+str(j), vlo*vhi < 0, True)
            left, right = a-b*hi, a-b*lo
            assert left >= 0 or right <= 0
            bits |= int(right <= 0) << j
        check('all eight signs '+str(i), bits, row['ordered_sign_bits'])
        components = [label(local.sub(local.scalar(a), local.scale(alpha, b))),
                      label(local.add(local.scalar(a), local.scale(alpha, b)))]
        for j, component in enumerate(components):
            check('complete component evidence '+str(i)+' '+str(j), local.clean(component),
                  {key: row['components'][j][key] for key in component})
            margin = 20+4*local.v2(b)-component['valuation']
            check('strict precision '+str(i)+' '+str(j), [margin, margin > 8],
                  [row['components'][j]['relative_error_lower_bound'], True])
        generator_rows.append(dict(pair=(a, b), norm=Q(row['norm_data']['norm']), signs=bits,
                                   local_pair=tuple(c['label'] for c in components)))

    # Enumerate every product before quotienting; independent of the producer's coordinates.
    rows, joint = [], set()
    real_image = {0, 252, 240, 192}
    point_image = {tuple(row) for row in old['point_image']}
    for mask in range(32):
        norm, bits, pair = Q(1), 0, (0, 0)
        for i, row in enumerate(generator_rows):
            if mask >> i & 1:
                norm *= row['norm']
                bits ^= row['signs']
                pair = tuple(lm(pair[j], row['local_pair'][j]) for j in range(2))
        fac = global_arithmetic.factor(norm)
        norm_code = int(norm < 0)
        for i, exponent in enumerate(fac['exponents'].values(), 1):
            norm_code |= (exponent % 2) << i
        triple = (norm_code, real_canonical(bits), canonical(pair))
        joint.add(triple)
        rows.append(dict(mask=mask, norm=norm, ordered_sign_bits=bits, raw_local_pair=pair,
                         triple=triple, norm_admissible=fac['square'], real_survives=triple[1] in real_image,
                         dyadic_survives=triple[2] in point_image))
    pair_lookup = {int(key): tuple(value) for key, value in cert['local_code_to_canonical_pair'].items()}
    stored_image = {(row['code'] & 31, (row['code'] >> 5) & 255, pair_lookup[row['code'] >> 13])
                    for row in cert['complete_joint_image']}
    check('full joint closure by independent 32-product enumeration', sorted(joint), sorted(stored_image))
    by_mask = {row['mask']: row['triple'] for row in rows}
    for row in cert['complete_joint_image']:
        code = row['code']
        check('representative replay '+str(code), by_mask[row['witness_mask']],
              (code & 31, (code >> 5) & 255, pair_lookup[code >> 13]))
    n = [row for row in joint if row[0] == 0]
    r = [row for row in n if row[1] in real_image]
    d = [row for row in r if row[2] not in point_image]
    check('all image counts', [len(joint), len(n), len(r), len(d)], [16, 4, 2, 1])
    witness = rows[5]
    check('load-bearing witness norm', witness['norm'], Q(7776, 275)**2)
    check('load-bearing witness signs', witness['ordered_sign_bits'], 240)
    check('load-bearing witness quotient', witness['triple'][2], (2, 24))
    check('witness passes norm/real and fails dyadic',
          [witness['norm_admissible'], witness['real_survives'], witness['dyadic_survives']], [True, True, False])
    exact_norm = global_arithmetic.gnorm(tuple(map(Q, [0, 3, 1]+[0]*5)))
    check('direct quadratic-element determinant', exact_norm['norm'], witness['norm'])
    direct_components = [label(local.add(local.mul(alpha, alpha), local.scale(alpha, 3))),
                         label(local.sub(local.mul(alpha, alpha), local.scale(alpha, 3)))]
    check('direct quadratic local labels', [row['label'] for row in direct_components], list(witness['raw_local_pair']))
    # For alpha^2 +/- 3alpha the error multiplier alpha+alpha0 +/- 3 is a unit.
    check('direct quadratic relative precision', [20-row['valuation'] > 8 for row in direct_components], [True, True])
    orbit = sorted((lm(18, s), lm(17, s)) for s in scalars)
    check('complete scalar orbit minimum', min(orbit), (2, 24))
    check('complete scalar orbit avoids the point image', all(pair not in point_image for pair in orbit), True)
    direct_witness = dict(expression='theta(theta+3)', coordinates=[0, 3, 1]+[0]*5,
                          norm_evidence=exact_norm, norm_square_root=Q(7776, 275),
                          norm_divided_by_3025_square_root=Q(7776, 15125),
                          ordered_signs='++++----', real_class='----++++',
                          components=direct_components, absolute_error_lower_bound=20,
                          relative_error_lower_bounds=[20-row['valuation'] for row in direct_components],
                          common_scalar_orbit=orbit, quotient=(2, 24))
    failures = [row['name'] for row in checks if not row['passed']]
    result = dict(norm_recomputations=norm_rows, generators=generator_rows, all_32_products=rows,
                  complete_joint_triples=sorted(joint), witness=witness, direct_witness=direct_witness,
                  checks=checks, failures=failures,
                  qualification='Arithmetic replay only; separate critical mathematical audit pending')
    OUT.write_text(json.dumps(local.clean(result), indent=2)+'\n')
    print(json.dumps(dict(checks=len(checks), failures=failures, pair_determinants=len(norm_rows),
                          product_rows=len(rows), joint_image=len(joint), witness=local.clean(witness), path=str(OUT))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
