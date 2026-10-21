"""Independent complete audit of saved L047 evidence; never runs the search.

Reconstructs only the recorded trials. Growth scores validate saved prefixes;
no unrecorded candidate is assembled or tested. No original code is imported.
"""
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'embedded-quadratic-search-results.json'
OUT = HERE / 'embedded-quadratic-critical-audit-results.json'
P, G, A = 65537, 19139, 137
T = [16, 64, 70, 102, 112, 118, 121]
report = {'checks': [], 'failures': [], 'trials': [], 'draws': []}


def check(name, condition):
    report['checks'].append({'check': name, 'passed': bool(condition)})
    if not condition:
        report['failures'].append(name)
        raise AssertionError(name)


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def mul(a, b):
    assert a and b and all(len(row) == len(b) for row in a)
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))] for i in range(len(a))]


def column_rank(rows, n):
    # Column-space echelon basis, independent of the original row RREF.
    basis = {}
    for j in range(n):
        v = [r[j] for r in rows]
        for pivot in sorted(basis):
            factor = v[pivot]
            v = [(x-factor*y) % P for x, y in zip(v, basis[pivot])]
        pivot = next((i for i, x in enumerate(v) if x), None)
        if pivot is not None:
            inverse = pow(v[pivot], -1, P)
            basis[pivot] = [x*inverse % P for x in v]
    return len(basis)


def verify_elimination(name, mat, reduced, transform, ops, pivots, n):
    r = len(mat)
    check(name+' dimensions', len(reduced) == r and len(transform) == r
          and all(len(row) == n for row in mat+reduced)
          and all(len(row) == r for row in transform))
    check(name+' residues', all(0 <= x < P for row in mat+reduced+transform for x in row))
    replay = [row[:] for row in mat]
    u = eye(r)
    for ordinal, op in enumerate(ops):
        kind, i, *rest = op
        assert 0 <= i < r
        if kind == 'swap':
            j, = rest
            assert 0 <= j < r and i != j
            for z in (replay, u):
                z[i], z[j] = z[j], z[i]
        elif kind == 'scale':
            scalar, = rest
            assert 0 < scalar < P
            for z in (replay, u):
                z[i] = [scalar*x % P for x in z[i]]
        elif kind == 'subtract':
            j, scalar = rest
            assert 0 <= j < r and i != j and 0 <= scalar < P
            for z in (replay, u):
                z[i] = [(x-scalar*y) % P for x, y in zip(z[i], z[j])]
        else:
            raise AssertionError((name, ordinal, op))
    check(name+' full invertible operation replay', replay == reduced and u == transform)
    check(name+' full transformation identity', mul(transform, mat) == reduced)
    leading = [next((j for j, x in enumerate(row) if x), None) for row in reduced]
    rank = len(pivots)
    check(name+' RREF and every zero row',
          pivots == sorted(set(pivots)) and leading == pivots+[None]*(r-rank)
          and all(reduced[i][p] == int(i == k)
                  for k, p in enumerate(pivots) for i in range(r)))
    check(name+' independent column rank', column_rank(mat, n) == rank)
    return {'rows': r, 'columns': n, 'rank': rank, 'operations': len(ops)}


def pair_rows(i, j, d):
    return [[((int(block == i)-int(block == j))*int(power == degree)) % P
             for block in range(d-1) for degree in range(3)] for power in range(3)]


def audit():
    raw = SOURCE.read_bytes()
    report['source_sha256'] = sha256(raw).hexdigest()
    saved = json.loads(raw)
    core = [pow(G, j, P) for j in range(61)]
    h = [pow(G, j, P) for j in range(1024)]
    check('prime fields by trial division', all(n % d for n in (P, A)
          for d in range(2, int(n**0.5)+1)))
    check('generator and full order', pow(3, 64, P) == G and pow(G, 1024, P) == 1
          and pow(G, 512, P) == P-1 and len(set(h)) == 1024)
    check('complete graph injection and dummy bijection',
          len(h[61:1020]) == 959 and len(h[1020:]) == 4
          and set(h[61:1020]).isdisjoint(core)
          and set(h[61:1020]+h[1020:]) == set(h)-set(core))
    check('parameters', saved['parameters'] == dict(prime=P, auxiliary_prime=A,
          generator=G, T=T, core=core, trial_limit=512, size_limit=8, seed=137061))
    pool = set(product((0, 1, 136), repeat=3))
    for u, v in combinations(T, 2):
        for lam, offset in product(range(1, 5), range(4)):
            pool.add(((offset+lam*u*v) % A, (-lam*(u+v)) % A, lam))
    pool = sorted(pool)
    check('complete prescribed pool', saved['pool'] == [list(q) for q in pool]
          and len(pool) == 363)
    vals = [[(q[0]+t*(q[1]+t*q[2])) % A for t in T] for q in pool]
    check('all pool graphs distinct', len(set(map(tuple, vals))) == len(pool))
    report['pool'] = [list(q) for q in pool]
    report['dummy_labels'] = h[1020:]
    check('recorded horizon', len(saved['trials']) == 11 and len(saved['draws']) == 49)
    state, draw_index = 137061, 0
    first_obstruction = None
    for b, trial in enumerate(saved['trials']):
        d = 2+b % 7
        ids = trial['pool_indices']
        check(f'{b}: size and indices', trial['trial'] == b and trial['d'] == d
              and len(ids) == len(set(ids)) == d and all(0 <= q < len(pool) for q in ids))
        # Validate exactly the saved candidate prefixes, not a new search.
        growth = []
        for position, selected in enumerate(ids):
            if position == 0:
                eligible, phase, scores = list(range(len(pool))), 'initial', None
            else:
                previous = ids[:position]
                occupied = {(j, vals[q][j]) for q in previous for j in range(7)}
                scores = [[q, sum((j, vals[q][j]) in occupied for j in range(7))]
                          for q in range(len(pool)) if q not in previous]
                maximum = max(s for q, s in scores)
                eligible = [q for q, s in scores if s == maximum]
                phase = f'growth-{position}'
                growth.append(dict(increase=maximum, tied=eligible, selected=selected))
            state = (1664525*state+1013904223) % 2**32
            expected = dict(trial=b, phase=phase, state=state, eligible=eligible,
                            residue=state % len(eligible), selected=selected)
            check(f'{b}: draw {position}', saved['draws'][draw_index] == expected
                  and selected == eligible[state % len(eligible)])
            report['draws'].append(dict(transcript=expected, all_growth_scores=scores))
            draw_index += 1
        check(f'{b}: complete growth transcript', trial['growth'] == growth)
        values = [vals[q] for q in ids]
        exponents = [[61+137*j+y for j, y in enumerate(v)] for v in values]
        labels = [[h[e] for e in es] for es in exponents]
        supports = [sorted(core+row) for row in labels]
        for key, expected in [('polynomials', [list(pool[q]) for q in ids]),
                              ('graph_values', values), ('label_exponents', exponents),
                              ('outside_labels', labels), ('supports', supports)]:
            check(f'{b}: complete {key}', trial[key] == expected)
        check(f'{b}: support sizes', all(len(set(s)) == 68 for s in supports))
        intersections, outside = [], []
        for size in range(2, d+1):
            for indices in combinations(range(d), size):
                points = sorted(set.intersection(*(set(labels[i]) for i in indices)))
                # Independent auxiliary-coordinate equality reconstruction.
                aux = sorted(h[61+137*j+values[indices[0]][j]] for j in range(7)
                             if all(values[i][j] == values[indices[0]][j] for i in indices))
                check(f'{b}: intersection {indices}', points == aux)
                outside.append(dict(indices=list(indices), points=points))
                intersections.append(dict(indices=list(indices), points=sorted(core+points)))
        check(f'{b}: all saved intersections', trial['all_intersections'] == intersections
              and trial['outside_intersections'] == outside)
        mat, stars = [], []
        for x in sorted(set.union(*(set(row) for row in labels))):
            incident = [i for i in range(d) if x in labels[i]]
            anchor = incident[0]
            for other in incident[1:]:
                stars.append(dict(point=x, anchor=anchor, other=other, incident=incident))
                mat.append([((int(block == anchor)-int(block == other))*pow(x, degree, P)) % P
                            for block in range(d-1) for degree in range(3)])
        n = 3*(d-1)
        check(f'{b}: complete signed stars and matrix', trial['row_labels'] == stars
              and trial['matrix'] == mat and trial['columns'] == n and trial['w'] == len(mat))
        base = verify_elimination(f'{b}: base', mat, trial['rref'], trial['row_transform'],
                                  trial['operations'], trial['pivots'], n)
        check(f'{b}: rank', base['rank'] == trial['rank'])
        check(f'{b}: complete pair order', [item['pair'] for item in trial['pair_tests']]
              == [list(pair) for pair in combinations(range(d), 2)])
        pair_reports = []
        for item in trial['pair_tests']:
            i, j = item['pair']
            name = f'{b}: pair {i},{j}'
            difference = pair_rows(i, j, d)
            aug = mat+difference
            check(name+' full difference and augmentation', item['map'] == difference
                  and item['augmented_matrix'] == aug)
            pair_result = verify_elimination(name, aug, item['augmented_rref'],
                item['augmented_transform'], item['augmented_operations'], item['augmented_pivots'], n)
            check(name+' augmented rank', item['augmented_rank'] == pair_result['rank'])
            increment = pair_result['rank']-base['rank']
            check(name+' correct stopping increment', increment > 0 if b < 10 else increment == 0)
            if increment == 0:
                witness = item['row_space_witness']
                check(name+' complete row-space identity', len(witness) == 3
                      and mul(witness, mat) == difference)
                check(name+' inverse-derived witness', witness == mul(difference, trial['row_transform']))
                if first_obstruction is None:
                    first_obstruction = dict(trial=b, pair=[i,j], rank=base['rank'], columns=n,
                        row_space_witness=witness, difference_map=difference)
            else:
                check(name+' no claimed witness', 'row_space_witness' not in item)
            pair_reports.append(dict(pair=[i,j], increment=increment, **pair_result))
        report['trials'].append(dict(trial=b, pool_indices=ids, graph_values=values,
            label_exponents=exponents, outside_labels=labels, supports=supports,
            all_intersections=intersections, outside_intersections=outside,
            row_labels=stars, matrix=mat, base=base, pairs=pair_reports))
    check('complete draw consumption and exact early stop', draw_index == len(saved['draws'])
          and first_obstruction == saved['obstruction'] and first_obstruction['trial'] == 10)
    final = saved['trials'][10]
    mat, inv = final['matrix'], final['row_transform']
    check('both full inverse identities', mul(mat, inv) == eye(12) and mul(inv, mat) == eye(12))
    # Independently obtain the integer determinant using rational Gaussian
    # elimination with last available pivot, rather than first-pivot Bareiss.
    rational = [[Fraction(x) for x in row] for row in mat]
    determinant, rational_trace = Fraction(1), []
    for k in range(12):
        at = max(i for i in range(k, 12) if rational[i][k])
        if at != k:
            rational[k], rational[at] = rational[at], rational[k]
            determinant = -determinant
        pivot = rational[k][k]
        determinant *= pivot
        for i in range(k+1, 12):
            factor = rational[i][k]/pivot
            rational[i] = [x-factor*y for x, y in zip(rational[i], rational[k])]
        rational_trace.append(dict(column=k, swap_row=at, pivot=str(pivot),
                                   matrix=[[str(x) for x in row] for row in rational]))
    check('independent rational integer determinant', determinant.denominator == 1
          and determinant.numerator == final['integer_determinant']
          == -49740849785522550165823979466653588692992014892312)
    check('determinant residue', determinant.numerator % P == final['determinant_mod_prime'] == 26669)
    # Validate every supplied Bareiss intermediate integer and exact division.
    integer, previous, sign, division_count = [row[:] for row in mat], 1, 1, 0
    check('complete Bareiss trace length', len(final['bareiss_trace']) == 11)
    for k, entry in enumerate(final['bareiss_trace']):
        at = next(i for i in range(k, 12) if integer[i][k])
        if at != k:
            integer[k], integer[at] = integer[at], integer[k]
            sign *= -1
        pivot = integer[k][k]
        for i in range(k+1, 12):
            for j in range(k+1, 12):
                numerator = pivot*integer[i][j]-integer[i][k]*integer[k][j]
                quotient, remainder = divmod(numerator, previous)
                check(f'Bareiss exact division {k},{i},{j}', remainder == 0)
                division_count += 1
                integer[i][j] = quotient
        for i in range(k+1, 12):
            integer[i][k] = 0
        check(f'Bareiss complete state {k}', entry == dict(column=k, swap_row=at,
              pivot=pivot, previous_divisor=previous, matrix=integer))
        previous = pivot
    check('Bareiss final signed value', sign*integer[-1][-1] == determinant)
    factor = 1
    for op in final['operations']:
        if op[0] == 'swap': factor = -factor % P
        if op[0] == 'scale': factor = factor*pow(op[2], -1, P) % P
    check('modular operation determinant', factor == 26669)
    # Match every finite value printed in the canonical lemma to the audit.
    lemma = (HERE.parent.parent / 'lemmas/L047-embedded-quadratic-common-center-obstruction.md').read_text()
    blocks = re.findall(r'```text\n(.*?)\n```', lemma, re.S)
    printed_matrices = [[[int(x) for x in row.split()] for row in block.splitlines()]
                        for block in blocks if len(block.splitlines()) == 12
                        and all(len(row.split()) == 12 for row in block.splitlines())]
    check('both complete canonical printed matrices', printed_matrices == [mat, inv])
    printed_q = [[int(x) for x in triple.split(',')]
                 for triple in re.findall(r'q\d=\((\d+,\d+,\d+)\)', blocks[0])]
    check('canonical five polynomials', printed_q == final['polynomials'])
    block = blocks[1].splitlines()
    expo = [[int(x) for x in row.split()[1].split(',')] for row in block[1:6]]
    labs = [[int(x) for x in row.split()[1].split(',')] for row in block[8:13]]
    check('canonical full exponent and label rows', expo == final['label_exponents'] and labs == final['outside_labels'])
    printed_stars = [[int(x) for x in row.split()] for row in blocks[3].splitlines()[1:]]
    check('canonical full star list', printed_stars == [[r['point'], r['anchor'], r['other']] for r in final['row_labels']])
    check('selected old pair/triple incidence restrictions',
          all(len(set(final['outside_labels'][i]) & set(final['outside_labels'][j])) <= 2
              for i,j in combinations(range(5), 2))
          and all(not (all(len(set(final['outside_labels'][i]) & set(final['outside_labels'][j])) == 2
                           for i,j in combinations(triple, 2))
                       and not set.intersection(*(set(final['outside_labels'][i]) for i in triple)))
                  for triple in combinations(range(5), 3)))
    old_summary = dict(trials=11, pool_size=363, draw_count=49, checks=285, failed_checks=0,
        stop='verified obstruction', rank_rows_columns=[[t['base']['rank'],t['base']['rows'],t['base']['columns']]
                                                       for t in report['trials']])
    check('saved summary and all first-pass flags', saved['summary'] == old_summary
          and len(saved['checks']) == 285 and all(c['passed'] is True for c in saved['checks'])
          and saved['failures'] == [])
    check('original certificate unchanged', sha256(SOURCE.read_bytes()).hexdigest() == report['source_sha256'])
    report['final'] = dict(matrix=mat, inverse=inv, integer_determinant=int(determinant),
        determinant_mod_prime=26669, rational_trace=rational_trace,
        bareiss_divisions=division_count, pair_witnesses=final['pair_tests'], obstruction=first_obstruction)
    report['summary'] = dict(checks=len(report['checks']), failures=len(report['failures']),
        trials=11, draws=49, pool_size=363, pair_tests=sum(len(t['pairs']) for t in report['trials']),
        replayed_operations=sum(t['base']['operations']+sum(p['operations'] for p in t['pairs']) for t in report['trials']),
        final_rank=12, required_full_rank=12, determinant_mod_prime=26669,
        final_intersections=len(final['all_intersections']), new_search_trials=0)


if __name__ == '__main__':
    try:
        audit()
    except Exception as error:
        report['error'] = repr(error)
        if not report['failures']:
            report['failures'].append(repr(error))
        raise
    finally:
        OUT.write_text(json.dumps(report, indent=2)+'\n')
        print(json.dumps(report.get('summary', {'failures': report['failures']}), sort_keys=True))
        print('failures:', report['failures'])
        print('full audit certificate:', OUT.relative_to(HERE.parent.parent))
