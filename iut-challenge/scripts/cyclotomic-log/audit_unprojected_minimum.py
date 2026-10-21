#!/usr/bin/env python3
"""Independent finite checks for L038; audited L031/L034 are inputs.

No builder imports and no claim to certify the analytic or orbit-module
arguments. All checked coordinates and word images are saved to disk.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'unprojected-minimum-independent-audit.json'
PIN = 'ad5ea1741a5cc54d5413ab679fd4fba387e8a2aafc8d9c7c2b6d31e799159102'
report = {'checks': {}, 'failures': []}


def check(name, ok):
    report['checks'][name] = bool(ok)
    if not ok:
        raise ValueError(name)


def v3(x):
    x = Q(x)
    if not x:
        return None
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % 3 == 0:
        n //= 3
        v += 1
    while d % 3 == 0:
        d //= 3
        v -= 1
    return v


def field_v(col):
    return min(Q(v3(x)) + Q(i // 4, 27)
               for i, x in enumerate(col) if x)


def mod3(x):
    x = Q(x)
    return x.numerator * pow(x.denominator, -1, 3) % 3


def rank3(rows):
    a = [[mod3(x) for x in row] for row in rows]
    rank = 0
    for j in range(len(a[0])):
        k = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if k is None:
            continue
        a[rank], a[k] = a[k], a[rank]
        unit = pow(a[rank][j], -1, 3)
        a[rank] = [(unit*x) % 3 for x in a[rank]]
        for i in range(len(a)):
            if i != rank:
                c = a[i][j]
                a[i] = [(x-c*y) % 3 for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank, a


def main():
    jb = (BASE / 'enlarged-basis.json').read_bytes()
    mb = (BASE / 'projected-container-homothety.json').read_bytes()
    jd, md = json.loads(jb), json.loads(mb)
    report['input_sha256'] = {'enlarged-basis.json': sha256(jb).hexdigest(),
                             'projected-container-homothety.json': sha256(mb).hexdigest()}
    check('pinned_complete_J', sha256(jb).hexdigest() == PIN == md['source_sha256'])
    b = jd['integer_basis_matrix']
    a = md['kernel_transform']
    m = md['M_basis_times_9']
    for name, mat, nr, nc in [('B', b, 108, 108), ('A', a, 108, 108), ('9M', m, 108, 107)]:
        check(name+'_shape_and_integrality', len(mat) == nr and
              all(len(row) == nc and all(type(x) is int for x in row) for row in mat))
    tau = [4, -1, -1, -1] + [0]*104
    check('full_trace_row', md['trace_row_divided_by_27'] == tau)
    check('full_M_basis_identity', all(m[i][j] == sum(b[i][k]*a[k][j+1] for k in range(108))
                                     for i in range(108) for j in range(107)))
    check('full_M_trace_zero', all(sum(tau[i]*m[i][j] for i in range(108)) == 0 for j in range(107)))
    jvals = [field_v([Q(b[i][j], 9) for i in range(108)]) for j in range(108)]
    mvals = [field_v([Q(m[i][j], 9) for i in range(108)]) for j in range(107)]
    report['all_J_basis_valuations'] = jvals
    report['all_M_basis_valuations'] = mvals
    check('complete_J_lower_bound', min(jvals) == -2)
    check('complete_M_lower_bound', min(mvals) == -2)
    bottom = [row[:] for row in m[:4]]
    rank, reduced = rank3(bottom)
    report['complete_M_bottom_matrix'] = bottom
    report['complete_M_bottom_reduced_mod3'] = reduced
    report['complete_M_bottom_rank'] = rank
    check('complete_bottom_rank_three', rank == 3)

    cols = [[Q(b[i][36+j], 9) for i in range(108)] for j in range(4)]
    constants = [[9*x for x in col[:4]] for col in cols]
    traces = [27*sum(t*x for t, x in zip(tau, col)) for col in cols]
    check('all_four_constant_columns', constants == [[4,0,0,0], [24,24,24,25], [0,1,0,3], [26,26,2,26]])
    check('all_four_full_traces', traces == [48,69,-12,150])
    coefs = [-Q(23,16), Q(1,4), -Q(25,8)]
    witnesses = [[x+c*y for x, y in zip(cols[j+1], cols[0])] for j, c in enumerate(coefs)]
    rhos = [[mod3(9*x) for x in w[:4]] for w in witnesses]
    check('integral_witness_coefficients', all(v3(c) >= 0 for c in coefs))
    check('all_witness_traces_zero', all(sum(t*x for t, x in zip(tau, w)) == 0 for w in witnesses))
    check('all_witness_valuations_minus_two', all(field_v(w) == -2 for w in witnesses))
    check('all_witness_residues', rhos == [[1,0,0,1], [1,1,0,0], [0,2,2,2]])
    wrank, wrref = rank3(list(map(list, zip(*rhos))))
    check('witness_rank_three', wrank == 3)
    report['four_complete_basis_columns'] = cols
    report['four_traces'] = traces
    report['complete_witnesses'] = witnesses
    report['witness_residues'] = rhos
    report['witness_reduced_mod3'] = wrref

    # Coordinates are (y_1,e_1,f_1,...,e_53,f_53); apply v first, u second.
    images = []
    for j in range(107):
        z = [int(i == j) for i in range(107)]
        for pair in range(53):
            e, f = 1+2*pair, 2+2*pair
            for _ in range(3):
                z[f] -= z[e]
                z[e] += z[f]
        expected = [int(i == j)*(1 if j == 0 else -1) for i in range(107)]
        check('word_basis_column_'+str(j), z == expected)
        images.append(z)
    report['complete_word_images_by_column'] = images
    report['pair_count'] = 53
    report['bounds'] = {'complete_bottom_rank_actual': rank, 'complete_bottom_rank_required': 3,
                        'complement_bottom_rank_lower': rank-1, 'complement_bottom_rank_required': 1,
                        'M_minimum_actual': -2, 'M_minimum_required': -2,
                        'orbit_minimum_proved_in_L038': -6, 'hull_radius': 729}
    report['scope'] = 'Finite evidence only; analytic inputs, arbitrary presentations, integral orbit splitting and finite-sum attainment are justified in canonical L038.'


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        report['failures'].append(str(exc))
    OUT.write_text(json.dumps(report, indent=2, default=str)+'\n')
    print('L038 finite audit:', len(report['checks']), 'checks;', len(report['failures']), 'failures')
    if report['failures']:
        print('Failures:', report['failures'])
    else:
        print('53 pairs and fixed direction pass; bottom rank actual/required = 3/3; complement rank lower/required = 2/1')
        print('M minimum actual/required = -2/-2; L038 orbit minimum = -6; field hull radius = 729')
    print('Full certificate:', OUT.relative_to(BASE.parent.parent))
    raise SystemExit(bool(report['failures']))
