"""Replay every seed, row and rejection; independently solve syndrome lines.

No producer imports. Candidate row completeness is checked using inverses
of four-column moment matrices and all four remaining moment equations,
rather than the shortening-polynomial ratio tests used by the producer.
"""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json

F = 97
BASE = Path(__file__).parent


def inverse(matrix):
    n = len(matrix)
    a = [list(row)+[int(i == j) for j in range(n)] for i, row in enumerate(matrix)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if a[i][j] % F)
        a[j], a[pivot] = a[pivot], a[j]
        r = pow(a[j][j], -1, F)
        a[j] = [r*v % F for v in a[j]]
        for i in range(n):
            if i != j:
                r = a[i][j]
                a[i] = [(u-r*v) % F for u, v in zip(a[i], a[j])]
    return [row[n:] for row in a]


def mv(matrix, vector):
    return [sum(x*y for x, y in zip(row, vector)) % F for row in matrix]


def run():
    source = BASE / 'fixed-split-table.json'
    data = json.loads(source.read_text())
    h = tuple(x for x in range(1, F) if pow(x, 16, F) == 1)
    pset, qset, c = (1, 8, 12), (18, 22, 27), 33
    s = (*pset, *qset, c)
    jset = tuple(x for x in h if x not in s)
    ks = list(combinations(jset, 2))
    rows = [(x, y, ki) for x in pset for y in qset for ki in range(36)]
    assert data['H'] == list(h) and data['P'] == list(pset) and data['Q'] == list(qset)
    assert data['c'] == c and data['J'] == list(jset)
    assert data['K_order'] == [list(k) for k in ks]
    assert data['row_order'] == [list(r) for r in rows]
    gv = []
    generator_checks = 0
    for k in ks:
        values = {}
        for x in h:
            value = 1
            for z in sorted(set(jset)-set(k)):
                value = (value*(x-z)) % F
            values[x] = value
        assert all(values[x] for x in (*s, *k))
        assert all(values[x] == 0 for x in set(jset)-set(k))
        for power in range(1, 9):
            assert sum(values[x]*pow(x, power, F) for x in h) % F == 0
            generator_checks += 1
        gv.append(values)

    # Independent normalized 3-by-3 linear systems for the tree solutions.
    tree_cache = {}
    def tree(triple, omitted1, omitted2, k1, k2):
        key = (triple, omitted1, omitted2, k1, k2)
        if key not in tree_cache:
            matrix = [[1, 0, 0]]
            for omit, ki in ((omitted1, k1), (omitted2, k2)):
                left, right = [x for x in triple if x != omit]
                matrix.append([gv[ki][right] if z == left else
                               -gv[ki][left] if z == right else 0 for z in triple])
            tree_cache[key] = tuple(mv(inverse(matrix), (1, 0, 0)))
        return tree_cache[key]

    expected_seed_ids = []
    for (x1, y1), (x2, y2) in combinations(product(pset, qset), 2):
        if x1 == x2 or y1 == y2:
            continue
        expected_seed_ids.extend((x1, y1, x2, y2, k1, k2)
                                 for k1 in range(36) for k2 in range(36) if k1 != k2)
    assert len(expected_seed_ids) == 22680
    assert [tuple(seed[0]) for seed in data['seeds']] == expected_seed_ids
    keys = [tuple(candidate['key']) for candidate in data['candidates']]
    assert len(set(keys)) == len(keys)
    reached = set()
    seed_counts = Counter()
    for seed, recorded_status, candidate_id in data['seeds']:
        x1, y1, x2, y2, k1, k2 = seed
        p = dict(zip(pset, tree(pset, x1, x2, k1, k2)))
        q = dict(zip(qset, tree(qset, y1, y2, k1, k2)))
        mu, cv, overlaps = [], [], []
        for x, y, ki in ((x1, y1, k1), (x2, y2, k2)):
            z = next(z for z in pset if z != x)
            zz = next(z for z in qset if z != y)
            # Solve the two equations mu*p_z = B*g(z), q_zz = B*g(zz).
            bb = q[zz]*pow(gv[ki][zz], -1, F) % F
            mu.append(bb*gv[ki][z]*pow(p[z], -1, F) % F)
            cv.append(bb*gv[ki][c] % F)
            overlaps.append((x, y, ki, bb))
        if mu[0] == mu[1]:
            status = 'mu'
        else:
            u, v = mv(inverse([[mu[0], -1], [mu[1], -1]]), cv)
            if u == 0 or v == 0:
                status = 'u' if u == 0 else 'v'
            else:
                failed = []
                for t, (x, y, ki, bb) in enumerate(overlaps):
                    if (mu[t]*p[x]-bb*gv[ki][x]) % F == 0:
                        failed.append('x')
                    elif (q[y]-bb*gv[ki][y]) % F == 0:
                        failed.append('y')
                status = 'weight:' + ''.join(failed) if failed else 'retained'
        assert status == recorded_status, ('seed status', seed, status, recorded_status)
        seed_counts[status] += 1
        if status == 'retained':
            key = (*[p[z] for z in pset], *[q[z] for z in qset], u, v)
            assert keys[candidate_id] == key
            reached.add(candidate_id)
        else:
            assert candidate_id is None
    assert reached == set(range(len(keys)))

    # For each A, solve its first four moment equations for the weights.
    # Four residual equations then characterize all extension-field points
    # of the syndrome line meeting U_A, not just prime-field samples.
    blocks = []
    for x, y, ki in rows:
        support = (x, y, *ks[ki])
        matrix = [[pow(z, power, F) for z in support] for power in range(1, 9)]
        inv = inverse(matrix[:4])
        weights_by_s = [mv(inv, [pow(z, power, F) for power in range(1, 5)]) for z in s]
        weights = [list(column) for column in zip(*weights_by_s)]
        residual = [[(pow(z, power, F)-sum(matrix[power-1][i]*weights[i][a]
                      for i in range(4))) % F for a, z in enumerate(s)] for power in range(5, 9)]
        blocks.append((support, matrix, weights, residual))
    successes_total = 0
    row_counts, histogram = Counter(), Counter()
    for cid, (candidate, key) in enumerate(zip(data['candidates'], keys)):
        pv, qv, u, v = key[:3], key[3:6], key[6], key[7]
        w0, wi = (0, 0, 0, *qv, -v % F), (*pv, 0, 0, 0, u)
        syndrome0 = [sum(w*pow(z, power, F) for w, z in zip(w0, s)) % F for power in range(1, 9)]
        syndromei = [sum(w*pow(z, power, F) for w, z in zip(wi, s)) % F for power in range(1, 9)]
        assert len(candidate['codes']) == 324
        direct_successes = []
        for rid, ((x, y, ki), (support, matrix, weights, residual)) in enumerate(zip(rows, blocks)):
            # Replay recorded first-failed gates by cross products, with
            # division only after both pair compatibilities have passed.
            z, zz = [t for t in pset if t != x]
            p = dict(zip(pset, pv))
            q = dict(zip(qset, qv))
            if (p[z]*gv[ki][zz]-p[zz]*gv[ki][z]) % F:
                code = 'p'
            else:
                zq, zzq = [t for t in qset if t != y]
                if (q[zq]*gv[ki][zzq]-q[zzq]*gv[ki][zq]) % F:
                    code = 'q'
                else:
                    aa = p[z]*pow(gv[ki][z], -1, F) % F
                    bb = q[zq]*pow(gv[ki][zq], -1, F) % F
                    test_mu = bb*pow(aa, -1, F) % F
                    if (test_mu*u-v-bb*gv[ki][c]) % F:
                        code = 'c'
                    elif (test_mu*p[x]-bb*gv[ki][x]) % F == 0:
                        code = 'x'
                    elif (q[y]-bb*gv[ki][y]) % F == 0:
                        code = 'y'
                    else:
                        code = 's'
            assert candidate['codes'][rid] == code, ('row code', cid, rid)
            row_counts[code] += 1
            r0, ri = mv(residual, w0), mv(residual, wi)
            assert any(ri), ('whole-line or infinity exception', cid, rid)
            pivot = next(i for i, value in enumerate(ri) if value)
            mu = -r0[pivot]*pow(ri[pivot], -1, F) % F
            moment_success = False
            if all((a+mu*b) % F == 0 for a, b in zip(r0, ri)):
                assert mu != 0
                lift = [(a+mu*b) % F for a, b in zip(w0, wi)]
                recovered = mv(weights, lift)
                moment_success = all(recovered)
                if moment_success:
                    assert mv(matrix, recovered) == [(a+mu*b) % F for a, b in zip(syndrome0, syndromei)]
                    direct_successes.append([rid, mu])
                    successes_total += 1
            assert moment_success == (code == 's'), ('moment comparison', cid, rid)
        assert candidate['successes'] == direct_successes
        scalars = sorted({mu for _, mu in direct_successes})
        assert candidate['scalars'] == scalars
        assert len(scalars) == len(direct_successes)
        histogram[len(scalars)] += 1
        if (cid+1) % 5000 == 0:
            print(f'Replayed {cid+1}/{len(keys)} candidates; failures 0', flush=True)
    summary = data['summary']
    assert summary['distinct_candidates'] == len(keys)
    assert summary['seed_dispositions'] == dict(seed_counts)
    assert summary['row_dispositions'] == dict(row_counts)
    assert summary['distinct_scalar_histogram'] == {str(k): v for k, v in histogram.items()}
    maximum = max(histogram)
    maxima = [i for i, candidate in enumerate(data['candidates']) if len(candidate['scalars']) == maximum]
    threshold = [i for i, candidate in enumerate(data['candidates']) if len(candidate['scalars']) >= 6]
    assert summary['maximum_distinct_scalars'] == maximum
    assert summary['maximum_candidate_ids'] == maxima
    assert summary['threshold_candidate_ids'] == threshold
    assert summary['row_tests_actual'] == 324*len(keys)
    assert summary['seed_cases_actual'] == summary['seed_cases_required'] == 22680
    assert summary['row_tests_required_per_candidate'] == 324
    assert summary['equality_required_scalars'] == 6
    assert summary['failures_actual'] == summary['failures_required'] == 0
    result = {'certificate_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'seed_cases_actual': len(expected_seed_ids), 'seed_cases_required': 22680,
              'candidates_actual': len(keys), 'candidates_required': summary['distinct_candidates'],
              'row_tests_actual': 324*len(keys), 'row_tests_required': summary['row_tests_actual'],
              'generator_moment_checks': generator_checks,
              'successful_all_eight_moment_replays': successes_total,
              'maximum_distinct_scalars': maximum, 'equality_required_scalars': 6,
              'threshold_candidate_ids': threshold, 'maximum_candidate_ids': maxima,
              'distinct_scalar_histogram': dict(histogram),
              'failures': [], 'failures_actual': 0, 'failures_required': 0,
              'qualifications': 'Same Python runtime and prime-field arithmetic; not a separate critical proof audit.'}
    out = BASE / 'fixed-split-table-verification.json'
    out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({**result, 'maximum_candidate_ids': maxima[:5], 'output': str(out)}, sort_keys=True))


if __name__ == '__main__':
    run()
