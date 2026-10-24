#!/usr/bin/env python3
"""Exact bounded S-unit eligibility and simultaneous localization certificate.

Imports only L122's audited field operations/tables. No class backend or
claim about completeness of the global supported group is used.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

import marked_octic_two_adic_image as local

BASE = Path(__file__).parent
SOURCE = BASE / 'marked-octic-two-adic-image-certificate.json'
OUT = BASE / 'marked-octic-bounded-linear-certificate.json'
F = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
SUPPORT = (2, 3, 5, 11)


def evaluate(t):
    result = Q(0)
    for c in reversed(F):
        result = result*t+c
    return result


def norm_data(a, b):
    homogeneous = sum(c*a**i*b**(8-i) for i, c in enumerate(F))
    n = Q(homogeneous, 275)
    assert n
    numerator, denominator = abs(n.numerator), n.denominator
    exponents = []
    for p in SUPPORT:
        exponent = 0
        while numerator % p == 0:
            numerator //= p
            exponent += 1
        while denominator % p == 0:
            denominator //= p
            exponent -= 1
        exponents.append(exponent)
    return dict(homogeneous_F=homogeneous, norm=n, sign=1 if n > 0 else -1,
                support_exponents=exponents, numerator_remainder=numerator,
                denominator_remainder=denominator,
                eligible=numerator == denominator == 1)


def reduce_vector(value, basis):
    for pivot in sorted(basis, reverse=True):
        if value >> pivot & 1:
            value ^= basis[pivot]
    return value


def main():
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required, passed=actual == required))

    source = json.loads(SOURCE.read_text())
    check('actual unchanged polynomial', source['input']['G'], [11*c for c in F])
    check('actual theta transport', source['field']['actual_theta_transports'], ['alpha', '-alpha'])
    check('strict threshold', source['input']['strict_threshold'], 8)
    error_bound = source['field']['alpha_error_lower_bound']
    check('alpha error bound', error_bound, 20)
    alpha = tuple(map(Q, source['field']['alpha_approximation']))
    cosets = {tuple(row['residue']): row['label'] for row in source['residue_ring']['complete_unit_cosets']}
    table = source['residue_ring']['unit_multiplication_table']
    scalar_labels = source['scalar_labels']
    point_image = {tuple(pair) for pair in source['point_image']}
    check('actual dyadic image', sorted(point_image), [(0, 0), (0, 5), (0, 8), (0, 22), (2, 6)])

    def multiply_labels(a, b):
        return 32*((a//32) ^ (b//32))+table[a % 32][b % 32]

    # Construct and verify a complete F2 coordinate system on L*/L*2.
    field_codes = {0: 0}
    field_basis = []
    for label in range(64):
        if label in field_codes:
            continue
        bit = 1 << len(field_basis)
        field_basis.append(label)
        field_codes.update({multiply_labels(old, label): code ^ bit
                            for old, code in list(field_codes.items())})
    check('field coordinate size and dimension', [len(field_codes), len(field_basis)], [64, 6])
    check('all field products match XOR', all(field_codes[multiply_labels(a, b)] == field_codes[a] ^ field_codes[b]
                                             for a in range(64) for b in range(64)), True)
    scalar_basis = {}
    scalar_rows = []
    for label in scalar_labels:
        vector = field_codes[label] | (field_codes[label] << 6)
        reduced = reduce_vector(vector, scalar_basis)
        if reduced:
            scalar_basis[reduced.bit_length()-1] = reduced
        scalar_rows.append(dict(label=label, raw_code=vector, reduced_at_insertion=reduced))
    check('common scalar dimension', len(scalar_basis), 3)

    def canonical(pair):
        return min((multiply_labels(pair[0], s), multiply_labels(pair[1], s)) for s in scalar_labels)

    def local_code(pair):
        return reduce_vector(field_codes[pair[0]] | (field_codes[pair[1]] << 6), scalar_basis)

    code_to_pair = {}
    quotient_consistency = True
    for a in range(64):
        for b in range(64):
            code, pair = local_code((a, b)), canonical((a, b))
            if code in code_to_pair and code_to_pair[code] != pair:
                quotient_consistency = False
            code_to_pair[code] = pair
    check('complete common scalar quotient coding', [len(code_to_pair), quotient_consistency], [512, True])

    pairs = []
    for a in range(-16, 17):
        for b in range(1, 17):
            if gcd(a, b) != 1:
                continue
            pairs.append(dict(a=a, b=b, norm_data=norm_data(a, b)))
    eligible = [row for row in pairs if row['norm_data']['eligible']]
    check('every denominator residual is one', all(row['norm_data']['denominator_remainder'] == 1 for row in pairs), True)

    # Refine L118's eight exact intervals only as far as these ratios need.
    intervals = [(Q(5, 2), Q(3)), (Q(3, 2), Q(2)), (Q(3, 4), Q(1)), (Q(1, 4), Q(1, 2)),
                 (Q(-1, 2), Q(-1, 4)), (Q(-1), Q(-3, 4)), (Q(-2), Q(-3, 2)), (Q(-3), Q(-5, 2))]
    root_rows = []
    ratios = [Q(row['a'], row['b']) for row in eligible]
    for index, (lo, hi) in enumerate(intervals):
        start = (lo, hi)
        trace = []
        assert evaluate(lo)*evaluate(hi) < 0
        while any(lo < ratio < hi for ratio in ratios):
            mid = (lo+hi)/2
            v = evaluate(mid)
            assert v
            trace.append(dict(midpoint=mid, F_value=v))
            if evaluate(lo)*v < 0:
                hi = mid
            else:
                lo = mid
        root_rows.append(dict(index=index+1, initial_interval=start, bisections=trace,
                              interval=(lo, hi), F_endpoint_values=(evaluate(lo), evaluate(hi))))
    check('eight complete disjoint root intervals', len(root_rows) == 8 and
          all(root_rows[i+1]['interval'][1] < root_rows[i]['interval'][0] for i in range(7)), True)

    generator_rows = []
    for index, row in enumerate(eligible):
        a, b, nd = row['a'], row['b'], row['norm_data']
        norm_bits = int(nd['sign'] < 0)
        for j, exponent in enumerate(nd['support_exponents'], 1):
            norm_bits |= (exponent % 2) << j
        sign_bits = 0
        sign_evidence = []
        for j, root in enumerate(root_rows):
            lo, hi = root['interval']
            bounds = (a-b*hi, a-b*lo)
            assert bounds[0] >= 0 or bounds[1] <= 0
            negative = bounds[1] <= 0
            sign_bits |= int(negative) << j
            sign_evidence.append(dict(strict_value_interval=bounds, negative=negative))
        check('norm/sign compatibility generator '+str(index), sign_bits.bit_count() % 2, norm_bits & 1)
        real_code = sign_bits ^ (255 if sign_bits & 1 else 0)
        components = [local.sub(local.scalar(a), local.scale(alpha, b)),
                      local.add(local.scalar(a), local.scale(alpha, b))]
        labels, component_rows = [], []
        for component in components:
            valuation = local.val(component)
            assert valuation is not None
            normalized = local.mul(component, local.power(local.PI, -valuation))
            residue = local.residue(normalized)
            label = 32*(valuation % 2)+cosets[residue]
            margin = error_bound+4*local.v2(b)-valuation
            check('strict dyadic generator '+str(index)+' component '+str(len(labels)), margin > 8, True)
            labels.append(label)
            component_rows.append(dict(approximation=component, valuation=valuation,
                                       normalized_residue=residue, label=label,
                                       absolute_error_lower_bound=error_bound+4*local.v2(b),
                                       relative_error_lower_bound=margin))
        quotient = canonical(labels)
        dyadic_code = local_code(labels)
        joint = norm_bits | (real_code << 5) | (dyadic_code << 13)
        generator_rows.append(dict(index=index, pair=(a, b), norm_data=nd, norm_bits=norm_bits,
                                    ordered_sign_bits=sign_bits, sign_evidence=sign_evidence,
                                    real_code=real_code, components=component_rows,
                                    raw_dyadic_labels=labels, dyadic_quotient=quotient,
                                    dyadic_code=dyadic_code, joint_code=joint))

    # Elimination certifies the whole joint image; witnesses are generator masks.
    basis, elimination_rows, relations = {}, [], []
    for row in generator_rows:
        value, witness = row['joint_code'], 1 << row['index']
        trace = []
        for pivot in sorted(basis, reverse=True):
            if value >> pivot & 1:
                trace.append(pivot)
                value ^= basis[pivot]['value']
                witness ^= basis[pivot]['witness']
        if value:
            basis[value.bit_length()-1] = dict(value=value, witness=witness)
        else:
            relations.append(witness)
        elimination_rows.append(dict(generator=row['index'], pivot_trace=trace,
                                     remainder=value, witness=witness))
    image = {0: 0}
    for pivot in sorted(basis):
        br = basis[pivot]
        extension = {value ^ br['value']: witness ^ br['witness'] for value, witness in image.items()}
        assert not (image.keys() & extension.keys())
        image.update(extension)
    check('full joint image size', len(image), 1 << len(basis))
    check('every generator reduces to zero', all(reduce_vector(row['joint_code'], {p: v['value'] for p, v in basis.items()}) == 0
                                                for row in generator_rows), True)
    real_image = {0, 252, 240, 192}  # b0,b2,b4,b6 with first sign positive
    norm_rows, real_rows, removed, survivors = [], [], [], []
    for value, witness in sorted(image.items()):
        norm_bits, real_code, dyadic_code = value & 31, (value >> 5) & 255, value >> 13
        if norm_bits:
            continue
        result = dict(joint_code=value, witness_mask=witness, real_code=real_code,
                      dyadic_code=dyadic_code, dyadic_quotient=code_to_pair[dyadic_code])
        norm_rows.append(result)
        if real_code not in real_image:
            continue
        real_rows.append(result)
        (survivors if result['dyadic_quotient'] in point_image else removed).append(result)
    # Replay every stored exponent witness, including joint-zero relations.
    def replay(witness):
        value = 0
        for row in generator_rows:
            if witness >> row['index'] & 1:
                value ^= row['joint_code']
        return value
    check('all image witnesses replay', all(replay(witness) == value for value, witness in image.items()), True)
    check('all joint relations replay', all(replay(witness) == 0 for witness in relations), True)
    counts = dict(pairs=len(pairs), eligible=len(eligible), ineligible=len(pairs)-len(eligible),
                  joint_rank=len(basis), joint_image=len(image), norm_admissible=len(norm_rows),
                  real_survivors=len(real_rows), dyadic_removed_after_real=len(removed),
                  dyadic_survivors_after_real=len(survivors))
    failures = [row['name'] for row in checks if not row['passed']]
    cert = dict(input=dict(F=F, leading_coefficient_G=3025, support=SUPPORT,
                           bounds=dict(a_min=-16, a_max=16, b_min=1, b_max=16, gcd=1)),
                local_input=dict(path=SOURCE.name, sha256=sha256(SOURCE.read_bytes()).hexdigest()),
                pair_decisions=pairs, roots=root_rows, generators=generator_rows,
                field_coordinates=dict(basis=field_basis, labels_to_codes=field_codes),
                common_scalars=dict(rows=scalar_rows, echelon_basis=scalar_basis),
                local_code_to_canonical_pair=code_to_pair, real_image_codes=sorted(real_image),
                dyadic_point_image=sorted(point_image), elimination=elimination_rows,
                joint_basis=basis, joint_zero_relations=relations,
                complete_joint_image=[dict(code=value, witness_mask=witness) for value, witness in sorted(image.items())],
                norm_admissible_image=norm_rows, real_surviving_image=real_rows,
                removed_after_real=removed, surviving_both=survivors, counts=counts,
                precision=dict(actual_minimum=min(c['relative_error_lower_bound'] for r in generator_rows for c in r['components']),
                               required_strictly_above=8), checks=checks, failures=failures,
                limitations=['Joint image rank is not global subgroup rank', 'No complete supported group',
                             'No point completeness or integer exclusion', 'Critical audit pending'])
    OUT.write_text(json.dumps(local.clean(cert), indent=2)+'\n')
    print(json.dumps(dict(counts=counts, precision=cert['precision'], failures=failures, path=str(OUT))))
    if removed:
        best = min(removed, key=lambda row: (row['witness_mask'].bit_count(), row['witness_mask']))
        print(json.dumps(dict(example=best, product_pairs=[r['pair'] for r in generator_rows if best['witness_mask'] >> r['index'] & 1])))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
