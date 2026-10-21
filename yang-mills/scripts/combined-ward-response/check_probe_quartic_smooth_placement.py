#!/usr/bin/env python3
"""Exact Q_2 row-order check against L184's polynomial/Wick calculation."""
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path

from check_probe_quartic_wick import M as n, mm, run


def check(pinned):
    reference = run(pinned)
    p = [[F(int(i == j and (not pinned or i != 0)))
          for j in range(n)] for i in range(n)]
    s, b, a = [mm(mm(p, x), p) for x in (
        [[2, 1, 0, 1], [1, 3, 1, 0], [0, 1, 4, 1], [1, 0, 1, 3]],
        [[1, 2, -1, 0], [2, 1, 2, -1], [-1, 2, 0, 1], [0, -1, 1, 2]],
        [[2, 1, 0, 2], [1, 2, 1, 2], [0, 1, -1, 0], [2, 2, 0, 1]])]
    tilt_cov = [[2*x for x in row] for row in mm(mm(s, a), s)]
    phi, q = [F(1), F(1), F(-1), F(2)], [F(1), F(2), F(-1), F(3)]
    v = [[q[e]*phi[r] for r in range(n)] for e in range(n)]
    h = [[F(int(e == r))-(phi[r]/2 if e == 0 else F(0))
          for r in range(n)] for e in range(n)]

    def transpose(x):
        return [list(row) for row in zip(*x)]

    def cov(x, y):
        return mm(mm(x, s), transpose(y))

    chv, cvv, chh, cvh = cov(h, v), cov(v, v), cov(h, h), cov(v, h)
    vp, hp = mm(v, p), mm(h, p)
    hm, vm = mm(h, tilt_cov), mm(v, tilt_cov)
    # B=sum_k unit_k (B[k,:])^T, so MB has columns M unit_k.
    terms = [F(0) for _ in range(4)]
    for k, e, g in product(range(n), repeat=3):
        weights = (hm[g][k]*chv[e][g]*vp[e][g],
                   -hm[g][k]*cvv[e][g]*hp[e][g],
                   -vm[g][k]*chh[e][g]*vp[e][g],
                   vm[g][k]*cvh[e][g]*hp[e][g])
        for j, weight in enumerate(weights):
            terms[j] += 3*b[k][e]*weight
    expected = F(reference['three_placements'][1])
    assert sum(terms) == expected
    return {'case': reference['case'], 'four_signed_row_terms': list(map(str, terms)),
            'row_sum': str(sum(terms)), 'polynomial_Q2': str(expected),
            'exact_match': True}


if __name__ == '__main__':
    rows = [check(False), check(True)]
    certificate = {
        'scope': 'Synthetic rational algebra only; actual-mesh bounds are analytic in L185.',
        'checks': rows, 'failures': [], 'required': 'Exact Q_2 equality in both cases',
        'analytic_bound_reference': 'lemmas/L185-probe-quartic-smooth-tilt-placement-subcubic.md',
        'numerical_actual_probe_bound': None, 'required_cubic_bound': 'O(N^3)',
        'joint_group_limit': None}
    out = Path(__file__).with_name('probe-quartic-smooth-placement-certificate.json')
    out.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Q_2 signed row-order checks: 2/2 PASS; failures: 0')
    print('L185 analytic bound: O(N^(3/2)); required O(N^3); no joint limit certified')
    print(out)
