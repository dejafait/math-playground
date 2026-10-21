#!/usr/bin/env python3
"""Complete independent T_5 plan replay; imports no plan producer.

Reuses only the unchanged structural verifier and independent positive
period replay. All coupled equations, weights and finite bounds are rebuilt.
"""
import importlib.util
import json
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

from verify_compressed_plan import period_replay

HERE = Path(__file__).resolve().parent


def multiply(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def read_matrix(a, nr, nc):
    assert len(a) == nr and all(len(row) == nc for row in a)
    return [list(map(Q, row)) for row in a]


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def replay(data):
    assert data['schema'] == 'conductor36-coupled-T5-plan-v1'
    path = HERE/'presentation.json'; source = json.loads(path.read_text())
    spec = importlib.util.spec_from_file_location('structural_replay', HERE.parent/'general-relative/verify_certificate.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    checker = module.Checker(); structure = module.replay(checker, source, 36, [])
    assert data['presentation_sha256'] == sha256(path.read_bytes()).hexdigest()
    analytic = HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json'
    assert data['audited_analytic_sha256'] == sha256(analytic.read_bytes()).hexdigest()
    old = json.loads(analytic.read_text())
    saved = HERE/'compressed_plan.json'
    assert data['saved_compression_sha256'] == sha256(saved.read_bytes()).hexdigest()
    assert old['arithmetic']['model'] == [0, 0, 0, 0, 1] and old['T'] == 4860
    assert data['ell'] == 5 and gcd(5, 36) == 1
    assert all(5 % d for d in range(2, isqrt(5)+1))
    # Exhaustively reconstructed y-lists, including the point at infinity.
    lists = [[y for y in range(5) if y*y % 5 == (x*x*x+1) % 5] for x in range(5)]
    points = [[x, y] for x, ys in enumerate(lists) for y in ys]
    count = 1+sum(map(len, lists)); trace = 6-count
    assert data['affine_points'] == points and data['point_count'] == count
    assert data['a_ell'] == trace == old['coefficients'][5]
    period = period_replay(old); omega = Q(period['lower'])
    assert Q(data['omega_lower']) == omega > 0

    domain = sorted({tuple(e) for pair in source['endpoints'] for e in pair},
                    key=lambda c: (c[1], abs(c[0]), c[0]))
    assert data['domain'] == list(map(list, domain))
    for a, m in domain:
        assert m >= 0 and gcd(a, m) == 1 and (m != 0 or a == 1)
    units = [u for u in range(36) if gcd(u, 36) == 1]
    def equivalent(r, s):
        a, m = r; b, n = s
        return any((n-u*m) % 36 == 0 and (u*b-a) % gcd(m, 36) == 0 for u in units)
    reps = []
    for r in domain:
        matches = [i for i, s in enumerate(reps) if equivalent(s, r)]
        if not matches: reps.append(r)
        else: assert len(matches) == 1
    assert reps[0] == (1, 0) and len(reps) == 12
    assert data['representatives'] == list(map(list, reps)) == json.loads(saved.read_text())['representatives']
    inequivalences = []
    for i, r in enumerate(reps):
        for j, s in enumerate(reps[:i]):
            residues = [[u, (r[1]-u*s[1]) % 36, (u*r[0]-s[0]) % gcd(s[1], 36)] for u in units]
            assert all(x or y for _, x, y in residues)
            inequivalences.append({'pair': [j, i], 'unit_residues': residues})

    primitives = data['primitives']; keys = []; tails = []
    budget = Q(1, 1 << 38); assert Q(data['tail_budget']) == budget
    rho = Q(data['primitive_radius_budget']); assert rho > 0
    for p in primitives:
        assert set(p) == {'x_reduced', 'y', 'H', 'tail_radius'}
        x, y = Q(p['x_reduced']), Q(p['y']); H = p['H']
        assert -Q(1, 2) <= x < Q(1, 2) and 0 < y <= 1
        assert type(H) is int and H >= 0
        def tail(n): return Q(1, 1 << (6*n*y).__floor__())/(6*y)
        R = tail(H); assert Q(p['tail_radius']) == R <= rho
        assert H == 0 or tail(H-1) > rho
        keys.append((x, y)); tails.append(R)
    assert keys == sorted(set(keys))
    point_uses = set(); all_transports = []; zero_count = 0
    def transport(row, r, v):
        nonlocal zero_count
        a, m = r; p, q = v
        assert row['source'] == list(r) and row['target'] == list(v)
        sr, tr = row['bezout_source']; sv, tv = row['bezout_target']; t = row['t']
        assert all(type(n) is int for n in (sr, tr, sv, tv, t))
        assert a*sr-m*tr == p*sv-q*tv == 1
        matrix = multiply(multiply([[p, tv], [q, sv]], [[1, t], [0, 1]]), [[sr, -tr], [-m, a]])
        A, B = matrix[0]; C, D = matrix[1]
        assert row['matrix'] == [A, B, C, D] and A*D-B*C == 1 and C % 36 == 0
        assert q*(A*a+B*m) == p*(C*a+D*m) and (A*a+B*m, C*a+D*m) != (0, 0)
        inverse = [[D, -B], [-C, A]]
        assert row['inverse'] == [D, -B, -C, A]
        assert multiply(matrix, inverse) == multiply(inverse, matrix) == identity(2)
        coefficient = m*q
        if coefficient:
            step = coefficient*(36//gcd(coefficient, 36))
            assert abs(C) <= abs(C-step) and abs(C) <= abs(C+step)
        x, y = map(Q, row['tau']); u, w = map(Q, row['image'])
        divisor = (C*x+D)**2+C*C*y*y
        assert y > 0 and w > 0 and divisor > 0
        assert u == ((A*x+B)*(C*x+D)+A*C*y*y)/divisor and w == y/divisor
        if C:
            assert (x, y) == (-Q(D, C), Q(1, abs(C)))
            assert (u, w) == (Q(A, C), Q(1, abs(C))) and row['zero_translation'] is None
        else:
            assert A == D and abs(D) == 1 and (x, y) == (0, 1)
            assert Q(row['zero_translation']) == Q(B, D) and Q(B, D).denominator == 1
            assert (u, w) == (x+Q(B, D), y)
            zero_count += 1
        assert len(row['reduction_shifts']) == 2
        reduced = []
        for point, shift in zip(((x, y), (u, w)), row['reduction_shifts']):
            xx, yy = point
            assert type(shift) is int and shift == (xx+Q(1, 2)).__floor__()
            reduced.append((xx-shift, yy))
            assert -Q(1, 2) <= xx-shift < Q(1, 2)
        ids = row['primitive_ids']
        if C == 0: assert reduced[0] == reduced[1] and ids == []
        else:
            assert len(ids) == 2
            for i, point in zip(ids, reduced):
                assert type(i) is int and 0 <= i < len(keys) and keys[i] == point
                point_uses.add(i)
        all_transports.append(row)
    def assignment(row, v):
        matches = [i for i, s in enumerate(reps) if equivalent(s, v)]
        assert len(matches) == 1 and row['representative_id'] == matches[0]
        assert row['endpoint'] == list(v)
        transport(row['transport'], reps[matches[0]], v)
        return matches[0]
    assert len(data['assignments']) == len(domain)
    for row, v in zip(data['assignments'], domain): assignment(row, v)
    adjacency = [[0]*12 for _ in reps]
    assert len(data['closures']) == 12
    for i, (closure, s) in enumerate(zip(data['closures'], reps)):
        assert closure['representative'] == list(s)
        if i == 0: images = [(1, 0)]*6
        else:
            r = Q(*s)
            images = [(v.numerator, v.denominator) for v in [5*r]+[(r+j)/5 for j in range(5)]]
        assert len(closure['images']) == 6
        for row, v in zip(closure['images'], images):
            adjacency[i][assignment(row, v)] += 1
    assert point_uses == set(range(len(keys)))
    assert data['adjacency'] == adjacency and all(sum(row) == 6 for row in adjacency)
    matrix = [[trace*int(i == j)-adjacency[i][j] for j in range(12)] for i in range(12)]
    normalized = matrix+[[int(j == 0) for j in range(12)]]
    assert data['matrix'] == matrix and data['normalized_matrix'] == normalized
    el = data['elimination']; E = read_matrix(el['transform'], 13, 13)
    Ei = read_matrix(el['inverse_transform'], 13, 13)
    assert multiply(E, Ei) == multiply(Ei, E) == identity(13)
    required_rref = identity(12)+[[Q(0)]*12]
    assert multiply(E, normalized) == read_matrix(el['rref'], 13, 12) == required_rref
    assert el['rank'] == 12 and el['pivots'] == list(range(12))
    labels = [(i, k) for i, c in enumerate(data['closures']) for k, a in enumerate(c['images'])
              if a['transport']['zero_translation'] is None]
    assert data['rhs_labels'] == list(map(list, labels))
    rhs = [[Q(i == label[0]) for label in labels] for i in range(12)]+[[Q(0)]*len(labels)]
    ER = multiply(E, rhs)
    assert ER == read_matrix(el['transformed_rhs'], 13, len(labels))
    assert ER[12] == [Q(0)]*len(labels) and ER[0] == [Q(0)]*len(labels)
    # Both original equations and infinity normalization are retained.
    weights = read_matrix(data['solution_equation_weights'], 12, 12)
    assert weights == [row[:12] for row in E[:12]]
    assert multiply(normalized, weights) == [[Q(i == j) for j in range(12)] for i in range(12)]+[weights[0]]
    assert multiply(normalized, ER[:12]) == rhs

    def terms(t, w):
        if t['zero_translation'] is not None or not w: return []
        a, b = t['primitive_ids']; return [[a, str(-w)], [b, str(w)]]
    def rep_terms(i, sign):
        return [term for j, c in enumerate(data['closures']) for a in c['images']
                for term in terms(a['transport'], sign*weights[i][j])]
    assert data['representative_occurrences'] == [rep_terms(i, Q(1)) for i in range(12)]
    endpoint_index = {r: i for i, r in enumerate(domain)}
    assert len(data['generators']) == len(source['endpoints']) == 72
    Wmax = Q(0); widths = []; capped_widths = []; generated_point_uses = set()
    capped_tails = [Q(1, 1 << (6*4860*y).__floor__())/(6*y) for _, y in keys]
    for g, pair in zip(data['generators'], source['endpoints']):
        ids = [endpoint_index[tuple(v)] for v in pair]
        assert g['endpoints'] == pair and g['assignment_ids'] == ids
        occ = []
        for i, sign in zip(ids, (-1, 1)):
            a = data['assignments'][i]
            occ.extend(terms(a['transport'], Q(sign)))
            occ.extend(rep_terms(a['representative_id'], Q(sign)))
        assert g['occurrences'] == occ
        combined = {}
        for j, w in occ:
            combined[j] = combined.get(j, Q(0))+Q(w); generated_point_uses.add(j)
        assert g['combined'] == [[j, str(w)] for j, w in sorted(combined.items()) if w]
        W = sum((abs(Q(w)) for _, w in occ), Q(0))
        assert Q(g['absolute_occurrence_weight']) == W
        width = sum((2*abs(Q(w))*tails[j]/omega for j, w in occ), Q(0))
        assert Q(g['normalized_tail_width']) == width <= budget
        capped_widths.append(sum((2*abs(Q(w))*capped_tails[j]/omega for j, w in occ), Q(0)))
        widths.append(width); Wmax = max(Wmax, W)
    assert generated_point_uses == set(range(len(keys)))
    assert Q(data['maximum_occurrence_weight']) == Wmax > 0
    assert rho == budget*omega/(2*Wmax)
    summary = {'generators': 72, 'endpoint_occurrences': sum(map(len, source['endpoints'])),
               'distinct_endpoints': len(domain), 'representatives': 12,
               'endpoint_transports': len(domain), 'closing_transports': 72,
               'zero_translations': zero_count, 'points': len(keys), 'normalized_rank': 12,
               'max_H': max(p['H'] for p in primitives), 'Fourier_terms': sum(p['H'] for p in primitives),
               'max_normalized_tail_width': str(max(widths))}
    assert data['summary'] == summary
    threshold_failures = []
    if summary['max_H'] > 4860: threshold_failures.append('maximum cutoff exceeds 4860')
    if summary['Fourier_terms'] > 1000000: threshold_failures.append('total primitive terms exceed 1000000')
    worst = max(range(len(keys)), key=lambda i: primitives[i]['H'])
    uses = [{'transport_id': i, 'transport': t} for i, t in enumerate(all_transports) if worst in t['primitive_ids']]
    capped_worst = max(range(72), key=lambda i: capped_widths[i])
    # A compact exact lower contribution within that conservative upper
    # bound: preserve both points of every correction at the worst height.
    selected = [[j, w] for j, w in data['generators'][capped_worst]['occurrences']
                if keys[j][1] == keys[worst][1]]
    selected_bound = sum((2*abs(Q(w))*capped_tails[j]/omega for j, w in selected), Q(0))
    assert selected_bound <= capped_widths[capped_worst]
    return {'replay_passed': True, 'workload_passed': not threshold_failures, 'table_complete': False,
            'actual': summary, 'required': {'normalized_rank': 12, 'formal_consistency': True,
                'max_H': 4860, 'Fourier_terms': 1000000, 'normalized_two_sided_tail_width': str(budget),
                'endpoint_occurrences': 144, 'generators': 72},
            'failures': [], 'threshold_failures': threshold_failures,
            'structure': structure, 'structural_actual': checker.counts, 'structural_required': checker.required,
            'period': period, 'point_count_y_lists': lists, 'a_5': trace,
            'checks': {'endpoint_assignments': len(domain), 'Hecke_image_assignments': 72,
                'matrices_and_inverses': len(all_transports), 'positive_interior_points': 2*len(all_transports),
                'pairwise_inequivalences': len(inequivalences), 'normalized_equations': 13,
                'formal_rhs_variables': len(labels), 'endpoint_compositions': 144,
                'generator_weight_and_width_rows': 72, 'primitive_tails_and_H_minus_one': len(keys)},
            'inequivalence_witnesses': inequivalences,
            'infinity': {'Hecke_row': matrix[0], 'normalized_solution_row': list(map(str, weights[0])),
                         'actual_solution_rhs_zero': True, 'full_equation_retained': True},
            'worst_primitive_id': worst, 'worst_primitive': primitives[worst], 'worst_primitive_uses': uses,
            'cutoff_obstruction': {'all_primitive_H': 4860, 'generator_id': capped_worst,
                 'endpoints': source['endpoints'][capped_worst],
                 'normalized_tail_bound': str(capped_widths[capped_worst]), 'required': str(budget),
                 'passes': capped_widths[capped_worst] <= budget,
                 'selected_worst_height_occurrences': selected,
                 'selected_contribution': str(selected_bound),
                 'selected_contribution_exceeds_required': selected_bound > budget,
                 'scope': 'fixed points and uncombined absolute-occurrence rational tail convention only'},
            'unperformed': ['new finite Fourier sums/arithmetic errors', 'integer isolation and full table',
                            'separate critical audit']}


if __name__ == '__main__':
    source = HERE/'coupled_plan.json'; destination = HERE/'coupled_plan_verification.json'
    try: report = replay(json.loads(source.read_text()))
    except Exception as exc:
        report = {'replay_passed': False, 'workload_passed': False, 'table_complete': False,
                  'failures': [repr(exc)], 'traceback': traceback.format_exc()}
    report['plan_sha256'] = sha256(source.read_bytes()).hexdigest()
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print('coupled replay=', report['replay_passed'], 'workload=', report['workload_passed'],
          'actual=', report.get('actual'), 'required=', report.get('required'),
          'failures=', report['failures'], 'threshold failures=', report.get('threshold_failures'),
          'report=', destination)
    raise SystemExit(0 if report['replay_passed'] else 1)
