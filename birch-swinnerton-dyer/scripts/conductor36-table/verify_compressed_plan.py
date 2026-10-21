#!/usr/bin/env python3
"""Independent complete finite replay. No import of either plan producer.

The unchanged structural verifier is reused; elementary rational/interval
operations, cusp equivalence, matrices, weights and cutoffs are rebuilt here.
This never certifies an analytic table from its planning certificate.
"""
import importlib.util
import json
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent


def period_replay(old):
    D = 1 << 96
    assert old['bits'] == 96 and old['scale'] == D
    def out(values):
        return [(min(values)*D).__floor__(), -((-max(values)*D).__floor__())]
    def exact(v): return out([Q(v)])
    def op(a, b, fn):
        return out([fn(Q(x, D), Q(y, D)) for x in a for y in b])
    def root(a):
        assert 0 <= a[0] <= a[1]
        lo, hi = isqrt(a[0]*D), isqrt(a[1]*D)
        if hi*hi < a[1]*D: hi += 1
        assert lo*lo <= a[0]*D < (lo+1)**2
        assert hi*hi >= a[1]*D and (hi == 0 or (hi-1)**2 < a[1]*D)
        return [lo, hi]
    pi = old['pi']; assert pi['J'] == 40
    brackets = []
    for denominator, saved in zip((5, 239), pi['atan']):
        total = sum((Q((-1)**j, (2*j+1)*denominator**(2*j+1)) for j in range(40)), Q(0))
        remainder = Q(1, 81*denominator**81)
        bracket = [total, total+remainder]
        assert saved == list(map(str, bracket))
        brackets.append(bracket)
    low = 16*brackets[0][0]-4*brackets[1][1]
    high = 16*brackets[0][1]-4*brackets[1][0]
    assert 3 < low < high < 4
    assert pi['exact'] == list(map(str, (low, high))) and pi['interval'] == out([low, high])
    p = old['period']
    # Exact one-real-root factorization (x+1)(x^2-x+1), quadratic disc=-3.
    assert p['real_root'] == '-1' and p['conjugate_real'] == '1/2'
    assert p['v_squared'] == exact(Q(3, 4)) and p['d'] == exact(Q(-3, 2))
    R = root(exact(3)); assert R == p['R'] and Q(R[0], D) > Q(3, 2)
    A = root(R)
    G = root(op(op(R, exact(Q(-3, 2)), lambda x, y: x+y), exact(Q(1, 2)), lambda x, y: x*y))
    assert G[0] > 0 and p['agm_steps'][0] == [A, G]
    assert len(p['agm_steps']) == 13
    for saved in p['agm_steps'][1:]:
        avg = op(op(A, G, lambda x, y: x+y), exact(Q(1, 2)), lambda x, y: x*y)
        geom = root(op(A, G, lambda x, y: x*y))
        A, G = avg, geom
        assert saved == [A, G]
    bracket = [G[0], A[1]]
    assert bracket == p['agm_bracket'] and bracket[0] > 0
    omega = op(pi['interval'], bracket, lambda x, y: x/y)
    assert p['components'] == 1 and p['total'] == omega
    return {'lower': str(Q(omega[0], D)), 'upper': str(Q(omega[1], D)),
            'agm_iterations': 12, 'positive': True, 'component_factor': 1}


def replay(data):
    assert data['schema'] == 'conductor36-cusp-compression-plan-v1'
    path = HERE/'presentation.json'; source = json.loads(path.read_text())
    spec = importlib.util.spec_from_file_location('structural_replay', HERE.parent/'general-relative/verify_certificate.py')
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    checker = module.Checker(); structure = module.replay(checker, source, 36, [])
    assert data['presentation_sha256'] == sha256(path.read_bytes()).hexdigest()
    analytic = HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json'
    assert data['audited_analytic_sha256'] == sha256(analytic.read_bytes()).hexdigest()
    old = json.loads(analytic.read_text())
    assert old['arithmetic']['model'] == [0, 0, 0, 0, 1] and old['ell'] == data['ell'] == 37
    assert 37 % 36 == 1 and all(37%d for d in range(2, isqrt(37)+1))
    # Recount just the closing prime; other coefficients remain the audited L051 input.
    squares = [0]*37
    for y in range(37): squares[y*y % 37] += 1
    count = 1+sum(squares[(x*x*x+1) % 37] for x in range(37))
    assert data['h'] == old['h'] == count == 48
    period = period_replay(old); omega = Q(period['lower'])
    assert Q(data['omega_lower']) == omega > 0
    assert old['T'] == 4860

    domain = sorted({tuple(e) for pair in source['endpoints'] for e in pair},
                    key=lambda c: (c[1], abs(c[0]), c[0]))
    assert data['domain'] == list(map(list, domain))
    for a, m in domain:
        assert m >= 0 and gcd(a, m) == 1 and (m != 0 or a == 1)
    units = [u for u in range(36) if gcd(u, 36) == 1]
    # Independent Cremona criterion, including homogeneous infinity.
    def equivalent(r, s):
        a, m = r; b, n = s
        return any((n-u*m) % 36 == 0 and (u*b-a) % gcd(m, 36) == 0 for u in units)
    representatives = []; expected_assignment = []
    for r in domain:
        matches = [i for i, s in enumerate(representatives) if equivalent(s, r)]
        if not matches:
            matches = [len(representatives)]; representatives.append(r)
        assert len(matches) == 1
        expected_assignment.append(matches[0])
    assert data['representatives'] == list(map(list, representatives))
    inequivalences = []
    for i, r in enumerate(representatives):
        for j in range(i):
            s = representatives[j]; assert not equivalent(s, r)
            # All 12 unit choices fail; retain actual residues rather than a label.
            residues = [[u, (r[1]-u*s[1]) % 36, (u*r[0]-s[0]) % gcd(s[1], 36)] for u in units]
            assert all(x or y for _, x, y in residues)
            inequivalences.append({'pair': [j, i], 'unit_residues': residues})

    primitives = data['primitives']; keys = []
    budget = Q(1, 1 << 38); assert Q(data['tail_budget']) == budget
    rho = Q(data['primitive_radius_budget']); assert rho > 0
    tails = []
    for primitive in primitives:
        assert set(primitive) == {'x_reduced', 'y', 'H', 'tail_radius'}
        x, y = Q(primitive['x_reduced']), Q(primitive['y']); H = primitive['H']
        assert -Q(1, 2) <= x < Q(1, 2) and 0 < y <= 1
        assert type(H) is int and H >= 0
        def tail(n): return Q(1, 1 << (6*n*y).__floor__())/(6*y)
        R = tail(H)
        assert Q(primitive['tail_radius']) == R <= rho
        assert H == 0 or tail(H-1) > rho
        keys.append((x, y)); tails.append(R)
    assert keys == sorted(set(keys))
    point_uses = set(); all_transports = []; zero_count = 0; point_checks = 0
    def multiply(a, b):
        return [[sum(a[i][k]*b[k][j] for k in (0, 1)) for j in (0, 1)] for i in (0, 1)]
    def transport(row, r, v):
        nonlocal zero_count, point_checks
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
        assert multiply(matrix, inverse) == multiply(inverse, matrix) == [[1, 0], [0, 1]]
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
            assert (u, w) == (Q(A, C), Q(1, abs(C)))
            assert row['zero_translation'] is None
        else:
            assert A == D and abs(D) == 1 and (x, y) == (0, 1)
            assert Q(row['zero_translation']) == Q(B, D) and Q(B, D).denominator == 1
            assert (u, w) == (x+Q(B, D), y)
            zero_count += 1
        reduced = []
        for point, shift in zip(((x, y), (u, w)), row['reduction_shifts']):
            xx, yy = point
            assert type(shift) is int and shift == (xx+Q(1, 2)).__floor__()
            assert -Q(1, 2) <= xx-shift < Q(1, 2)
            reduced.append((xx-shift, yy)); point_checks += 1
        assert len(row['reduction_shifts']) == 2
        ids = row['primitive_ids']
        if C == 0:
            assert reduced[0] == reduced[1] and ids == []
        else:
            assert len(ids) == 2
            for i, point in zip(ids, reduced):
                assert type(i) is int and 0 <= i < len(keys) and keys[i] == point
                point_uses.add(i)
        all_transports.append(row)

    assert len(data['assignments']) == len(domain)
    for a, r, repid in zip(data['assignments'], domain, expected_assignment):
        assert a['endpoint'] == list(r) and a['representative_id'] == repid
        transport(a['transport'], representatives[repid], r)
    assert len(data['closures']) == len(representatives)
    for closure, s in zip(data['closures'], representatives):
        assert closure['representative'] == list(s)
        if s[1] == 0:
            assert s == (1, 0) and closure['transports'] == []
            continue
        r = Q(*s); assert gcd(r.denominator, 37) == 1
        expected = [37*r]+[(r+j)/37 for j in range(37)]
        assert len(closure['transports']) == 38
        for row, v in zip(closure['transports'], expected):
            assert equivalent(s, (v.numerator, v.denominator))
            transport(row, s, (v.numerator, v.denominator))
    assert point_uses == set(range(len(keys)))

    # Independently expand the two original endpoints. Keep every occurrence
    # in the conservative tail sum; signed cancellations only form the
    # exact future finite-evaluation expression.
    endpoint_index = {r: i for i, r in enumerate(domain)}
    def terms(row, tau_weight, image_weight):
        if row['zero_translation'] is not None: return []
        i, j = row['primitive_ids']
        return [[i, str(tau_weight)], [j, str(image_weight)]]
    Wmax = Q(0); maximum_width = Q(0); generator_checks = 0
    assert len(data['generators']) == len(source['endpoints']) == 72
    for gen, pair in zip(data['generators'], source['endpoints']):
        ids = [endpoint_index[tuple(endpoint)] for endpoint in pair]
        assert gen['endpoints'] == pair and gen['assignment_ids'] == ids
        occurrences = []
        for endpoint_id, sign in zip(ids, (-1, 1)):
            assignment = data['assignments'][endpoint_id]
            occurrences.extend(terms(assignment['transport'], Q(-sign), Q(sign)))
            for t in data['closures'][assignment['representative_id']]['transports']:
                occurrences.extend(terms(t, Q(sign, 48), -Q(sign, 48)))
        assert gen['occurrences'] == occurrences
        combined = {}
        for i, weight in occurrences: combined[i] = combined.get(i, Q(0))+Q(weight)
        assert gen['combined'] == [[i, str(w)] for i, w in sorted(combined.items()) if w]
        W = sum((abs(Q(w)) for _, w in occurrences), Q(0))
        assert Q(gen['absolute_occurrence_weight']) == W
        width = sum((2*abs(Q(w))*tails[i]/omega for i, w in occurrences), Q(0))
        assert Q(gen['normalized_tail_width']) == width <= budget
        Wmax = max(Wmax, W); maximum_width = max(maximum_width, width); generator_checks += 1
    assert Q(data['maximum_occurrence_weight']) == Wmax > 0
    assert rho == budget*omega/(2*Wmax)
    worst = max(range(len(primitives)), key=lambda i: primitives[i]['H'])
    summary = {'generators': 72, 'endpoint_occurrences': sum(map(len, source['endpoints'])),
               'distinct_endpoints': len(domain), 'representatives': len(representatives),
               'endpoint_transports': len(domain),
               'closing_transports': sum(len(c['transports']) for c in data['closures']),
               'zero_translations': zero_count, 'points': len(keys),
               'max_H': max(p['H'] for p in primitives), 'Fourier_terms': sum(p['H'] for p in primitives),
               'worst_primitive_id': worst, 'max_normalized_tail_width': str(maximum_width)}
    assert data['summary'] == summary
    failures = []
    if summary['max_H'] > 4860: failures.append('maximum cutoff exceeds 4860')
    if summary['Fourier_terms'] > 1000000: failures.append('total primitive terms exceed 1000000')
    witness_uses = []
    for kind, rows in [('endpoint', [(i, a['transport']) for i, a in enumerate(data['assignments'])]),
                       ('closing', [(i, t) for i, c in enumerate(data['closures']) for t in c['transports']])]:
        for i, row in rows:
            if worst in row['primitive_ids']: witness_uses.append({'kind': kind, 'index': i, 'transport': row})
    # Within this fixed point domain and conservative tail convention,
    # no redistribution of precision can pass with every H<=4860: R_H
    # decreases with H. Recompute all rows at the largest permitted H.
    capped_tails = [Q(1, 1 << (6*4860*y).__floor__())/(6*y) for _, y in keys]
    capped_widths = [sum((2*abs(Q(w))*capped_tails[i]/omega for i, w in g['occurrences']), Q(0))
                     for g in data['generators']]
    capped_worst = max(range(72), key=lambda i: capped_widths[i])
    cutoff_obstruction = {'all_primitive_H': 4860, 'generator_id': capped_worst,
                          'endpoints': source['endpoints'][capped_worst],
                          'normalized_tail_bound': str(capped_widths[capped_worst]),
                          'required': str(budget), 'passes': capped_widths[capped_worst] <= budget,
                          'scope': 'fixed points and uncombined absolute-occurrence rational tail convention only'}
    return {'replay_passed': True, 'workload_passed': not failures, 'table_complete': False,
            'actual': summary, 'required': {'max_H': 4860, 'Fourier_terms': 1000000,
                'normalized_two_sided_tail_width': str(budget), 'endpoint_occurrences': 144, 'generators': 72},
            'failures': [], 'threshold_failures': failures, 'structural_actual': checker.counts,
            'structural_required': checker.required, 'structure': structure,
            'period': period, 'closing_point_count': count,
            'checks': {'endpoint_assignments': len(domain), 'endpoint_compositions': 144,
                'matrices_and_inverses': len(all_transports), 'positive_interior_points': point_checks,
                'generator_weight_and_width_rows': generator_checks, 'primitive_tails_and_H_minus_one': len(keys),
                'pairwise_inequivalences': len(inequivalences)},
            'inequivalence_witnesses': inequivalences,
            'worst_primitive': primitives[worst], 'worst_primitive_uses': witness_uses,
            'cutoff_obstruction': cutoff_obstruction,
            'unperformed': ['new finite Fourier sums and arithmetic errors', 'all-generator integer isolation',
                            'table/source/saturated relation replay', 'separate critical audit']}


if __name__ == '__main__':
    source = HERE/'compressed_plan.json'; destination = HERE/'compressed_plan_verification.json'
    try:
        report = replay(json.loads(source.read_text()))
    except Exception as exc:
        report = {'replay_passed': False, 'workload_passed': False, 'table_complete': False,
                  'failures': [repr(exc)], 'traceback': traceback.format_exc()}
    report['plan_sha256'] = sha256(source.read_bytes()).hexdigest()
    destination.write_text(json.dumps(report, indent=2)+'\n')
    print('compressed replay=', report['replay_passed'], 'workload=', report['workload_passed'],
          'actual=', report.get('actual'), 'required=', report.get('required'),
          'failures=', report['failures'], 'threshold failures=', report.get('threshold_failures'),
          'report=', destination)
    raise SystemExit(0 if report['replay_passed'] else 1)
