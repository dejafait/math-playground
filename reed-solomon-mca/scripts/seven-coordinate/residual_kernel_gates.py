"""Exact L109 gates on all 266 audited L111 residual occurrences.

Run: python3 scripts/seven-coordinate/residual_kernel_gates.py
Full certificates stay on disk. No original chart or equality completion
is inferred from a passing four-row projective plane.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import zero_anchor_support_filter as support

P = 97
HERE = Path(__file__).resolve().parent
PAIRS = list(combinations(range(7), 2))
QUADS = list(combinations(range(7), 4))
PAIR_INDEX = {pair: n for n, pair in enumerate(PAIRS)}


def trim(a):
    a = [x % P for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def add(a, b):
    return trim([(a[n] if n < len(a) else 0) +
                 (b[n] if n < len(b) else 0) for n in range(max(len(a), len(b)))])


def scale(a, c):
    return trim([x*c for x in a])


def mul(a, b):
    c = [0]*max(0, len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] = (c[i+j]+x*y) % P
    return trim(c)


def divrem(a, b):
    a, b = trim(a), trim(b)
    assert b
    q = [0]*max(0, len(a)-len(b)+1)
    while len(a) >= len(b):
        d, c = len(a)-len(b), a[-1]*pow(b[-1], -1, P) % P
        q[d] = c
        a = add(a, [0]*d+scale(b, -c))
    return trim(q), a


def xgcd(a, b):
    u, v, uu, vv = [1], [], [], [1]
    while b:
        q, r = divrem(a, b)
        a, b = b, r
        u, uu = uu, add(u, scale(mul(q, uu), -1))
        v, vv = vv, add(v, scale(mul(q, vv), -1))
    if not a:
        return [], [], []
    c = pow(a[-1], -1, P)
    return scale(a, c), scale(u, c), scale(v, c)


def gcd_certificate(polys):
    gcd, coefficients = [], []
    for f in polys:
        gcd, a, b = xgcd(gcd, f)
        coefficients = [mul(a, c) for c in coefficients]+[b]
    total = []
    for c, f in zip(coefficients, polys):
        total = add(total, mul(c, f))
        if gcd:
            assert not divrem(f, gcd)[1]
    assert total == gcd
    return gcd, coefficients


def plucker_polynomials(basis):
    # p(s,t)=s*basis[0]+t*basis[1], homogeneous coefficients s^2,st,t^2.
    b0 = basis[0]
    b1 = basis[1] if len(basis) == 2 else [0]*21
    ans = []
    for a, b, c, d in QUADS:
        q = []
        for sign, ij, kl in [(1, (a, b), (c, d)),
                             (-1, (a, c), (b, d)),
                             (1, (a, d), (b, c))]:
            i, k = PAIR_INDEX[ij], PAIR_INDEX[kl]
            q = add(q, scale(mul([b0[i], b1[i]], [b0[k], b1[k]]), sign))
        ans.append(q+[0]*(3-len(q)))
    return ans


def plane_gates(p, rows):
    a, b = PAIRS[next(n for n, x in enumerate(p) if x)]
    alternating = [[0]*7 for _ in range(7)]
    for (x, y), value in zip(PAIRS, p):
        alternating[x][y], alternating[y][x] = value, -value % P
    u = [alternating[x][b]*pow(alternating[a][b], -1, P) % P for x in range(7)]
    v = alternating[a][:]
    assert support.wedge(u, v) == p
    gates = []
    for row in rows:
        i, k = row['I'], row['K']
        block = support.block(i, k)
        qu, qv = [[sum(x*y for x, y in zip(c, w)) % P
                   for c in block['covectors']] for w in (u, v)]
        minors = [(qu[x]*qv[y]-qu[y]*qv[x]) % P for x, y in combinations(range(4), 2)]
        assert not any(minors)
        gate = {'Q_u': qu, 'Q_v': qv, 'projection_minors': minors}
        if not any(qu+qv):
            gate.update(projection_rank=0, passes=False, failed_gates=['projection_rank_zero'])
        else:
            n = next(n for n in range(4) if qu[n] or qv[n])
            alpha, beta = -qv[n] % P, qu[n]
            h = [(alpha*x+beta*y) % P for x, y in zip(u, v)]
            assert any(h)
            assert not any((alpha*x+beta*y) % P for x, y in zip(qu, qv))
            z = block['pivot']
            lam = h[support.S.index(z)]*pow(support.g(k, z), -1, P) % P
            assert all(h[support.S.index(x)] == lam*support.g(k, x) % P
                       for x in support.S if x not in i)
            overlap = [(h[support.S.index(x)]-lam*support.g(k, x)) % P for x in i]
            error = dict(zip(i, overlap))
            error.update({x: -lam*support.g(k, x) % P for x in k})
            moments = [sum(((h[support.S.index(x)] if x in support.S else 0)-error.get(x, 0))*
                           pow(x, d, P) for x in support.H) % P for d in range(1, 9)]
            assert not any(moments)
            failed = (['lambda_zero'] if not lam else []) + [
                f'overlap_weight_zero_at_{x}' for x, w in zip(i, overlap) if not w]
            gate.update(projection_rank=1, direction_coefficients=[alpha, beta],
                        intersection_vector=h, lambda_value=lam, overlap_weights=overlap,
                        error_weights=[error[x] for x in i+k], moment_residuals=moments,
                        prescribed_finite_gate={'D_coefficient': alpha, 'C_coefficient': -beta % P},
                        passes=not failed, failed_gates=failed)
        gates.append(gate)
    return {'pivot_indices': [a, b], 'u': u, 'v': v, 'bivector': p,
            'row_gates': gates, 'passes_intrinsic_gates': all(g['passes'] for g in gates)}


def run():
    source_bytes = (HERE/'third-row-variation.json').read_bytes()
    assert sha256(source_bytes).hexdigest() == '34d6bb68537b8e5b153552801426c2f37266c96fa1446bb8ec89ae03885f85c2'
    source = json.loads(source_bytes)
    assert source['failures'] == [] and source['modulus'] == P
    assert source['S'] == support.S and source['H'] == support.H
    assert source['column_pairs'] == [[support.S[a], support.S[b]] for a, b in PAIRS]
    records, counts = [], Counter()
    expected_index = {(tuple(seed['third_I']), tuple(seed['third_K']), x['case_index'])
                      for seed in source['residual_seeds'] for x in seed['survivors']}
    for seed_index, seed in enumerate(source['seeds']):
        if seed['reused_audited_L110']:
            continue
        first_three = source['first_two']+[{'I': seed['third_I'], 'K': seed['third_K']}]
        for case_index, case in enumerate(seed['cases']):
            if not case['pairwise_linear'] or case['rank'] == 21:
                continue
            basis = case['kernel_basis']
            assert len(basis) == 21-case['rank'] in (1, 2)
            rows = first_three+[{'I': case['I'], 'K': case['K']}]
            matrix = [r for row in rows for r in support.block(row['I'], row['K'])['matrix']]
            residuals = [[sum(x*y for x, y in zip(row, v)) % P for row in matrix] for v in basis]
            assert not any(map(any, residuals))
            polys = plucker_polynomials(basis)
            gcd, bezout = gcd_certificate([trim(q) for q in polys])
            infinity = len(basis) == 2 and all(q[2] == 0 for q in polys)
            status = ('point_decomposable' if not any(q[0] for q in polys) else 'point_rejected') if len(basis) == 1 else (
                'whole_line' if not gcd else 'finite_roots')
            counts[status] += 1
            rec = {'seed_index': seed_index, 'case_index': case_index,
                   'rows': rows, 'rank': case['rank'], 'kernel_basis': basis,
                   'kernel_residuals': residuals, 'homogeneous_plucker_coefficients': polys,
                   'affine_gcd': gcd, 'bezout_coefficients': bezout,
                   'infinity_is_decomposable': infinity, 'plucker_status': status}
            if len(basis) == 1:
                points = [('unique', basis[0])] if status == 'point_decomposable' else []
            else:
                # The complete computed gcd certificate is t and infinity is a root.
                # Thus only [s:t]=[1:0],[0:1] survive over ANY extension field.
                assert gcd == [0, 1] and infinity
                assert any(q[1] for q in polys)
                assert all(q[0] == q[2] == 0 for q in polys)
                points = [('s=1,t=0', basis[0]), ('s=0,t=1', basis[1])]
            rec['decomposable_points'] = [dict(projective_kernel_point=label,
                                               **plane_gates(p, rows)) for label, p in points]
            records.append(rec)
    actual_index = {(tuple(r['rows'][2]['I']), tuple(r['rows'][2]['K']), r['case_index']) for r in records}
    assert actual_index == expected_index and len(records) == len(expected_index) == 266
    summary = {'actual_occurrences': len(records), 'required_occurrences': 266,
               'kernel_dimensions': dict(Counter(len(r['kernel_basis']) for r in records)),
               'plucker_status_counts': dict(counts)}
    planes = [p for r in records for p in r['decomposable_points']]
    row_gates = [g for p in planes for g in p['row_gates']]
    assert all(p['row_gates'][3]['lambda_value'] == 0 for p in planes)
    per_seed = []
    for seed_index in sorted({r['seed_index'] for r in records}):
        subset = [r for r in records if r['seed_index'] == seed_index]
        points = [p for r in subset for p in r['decomposable_points']]
        per_seed.append({'third': subset[0]['rows'][2], 'occurrences': len(subset),
                         'projective_points': len(points),
                         'fourth_row_lambda_zero_points': sum(p['row_gates'][3]['lambda_value'] == 0
                                                              for p in points)})
    summary.update(decomposable_projective_points=len(planes), required_point_cases=257+2*9,
                   intrinsically_passing_points=sum(p['passes_intrinsic_gates'] for p in planes),
                   checked_projection_rows=len(row_gates), required_projection_rows=4*(257+2*9),
                   projection_rank_counts=dict(Counter(g['projection_rank'] for g in row_gates)),
                   fourth_row_lambda_zero_points=len(planes), per_seed=per_seed,
                   failed_gate_counts=dict(Counter(f for g in row_gates for f in g['failed_gates'])),
                   first_failed_gate_counts=dict(Counter(next((f for g in p['row_gates']
                                                               for f in g['failed_gates']), 'passes')
                                                        for p in planes)))
    assert len(planes) == 275 and len(row_gates) == 1100
    output = {'source_sha256': sha256(source_bytes).hexdigest(),
              'modulus': P, 'S': support.S, 'H': support.H,
              'scope': 'all L111 indexed linear deficient four-row occurrences; necessary gates only',
              'original_chart_condition': 'For u_original=A*u+B*v, v_original=C*u+D*v with AD-BC!=0, require D*alpha-C*beta!=0 for each row direction (alpha,beta). Intrinsic failures exclude every chart.',
              'summary': summary, 'records': records, 'failures': []}
    path = HERE/'residual-kernel-gates.json'
    path.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Failures: 0; certificate: {path}')


if __name__ == '__main__':
    run()
