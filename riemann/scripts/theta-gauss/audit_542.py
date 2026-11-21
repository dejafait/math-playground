"""Independent finite L805 audit; never imports or runs step540's program.

Exact tuple/Fraction arithmetic; a separate 10^-42 integer-bisection square
root and refined root brackets accompany checks of every saved bound.
Inherited analytic/Decimal contracts are premises, not verified here.
"""
from fractions import Fraction as Q
from itertools import product
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('audit-certificate-542.json')
checks, failures, evidence = [], [], {}


def check(name, proposition):
    checks.append({'name': name, 'passed': bool(proposition)})
    if not proposition:
        failures.append(name)


def box(values):
    a, b = map(Q, values)
    if a > b:
        raise ValueError('reversed endpoints')
    return a, b


def const(value):
    return Q(value), Q(value)


def plus(a, b):
    return a[0]+b[0], a[1]+b[1]


def minus(a, b):
    return a[0]-b[1], a[1]-b[0]


def times(a, b):
    values = [x*y for x, y in product(a, b)]
    return min(values), max(values)


def over(a, b):
    if b[0] <= 0 <= b[1]:
        raise ValueError('denominator meets zero')
    return times(a, (1/b[1], 1/b[0]))


def power(a, n):
    result = const(1)
    for _ in range(n):
        result = times(result, a)
    return result


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def serial(a):
    return [str(v) for v in a]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def square_floor(value):
    """Integer binary search, not the original math.isqrt implementation."""
    lo, hi = 0, 1 << ((value.bit_length()+1)//2)
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid*mid <= value:
            lo = mid
        else:
            hi = mid
    # Handle the possibility that the initial upper bound was exact.
    return hi if hi*hi <= value else lo


def sqrt_enclosure(a):
    scale = 10**42
    lower = square_floor((a[0]*scale**2).__floor__())
    upper = square_floor((a[1]*scale**2).__floor__())+1
    result = Q(lower, scale), Q(upper, scale)
    check('independent sqrt lower square', result[0]**2 <= a[0])
    check('independent sqrt upper square', result[1]**2 >= a[1])
    return result


def h(x):
    return ((x-30)*x+180)*x-120


# Polynomial algebra in t1,t2,t3,x,y,A,B, independently represented as
# sparse coefficient maps. No saved zero residual is accepted as evidence.
ZERO = (0,)*7


def polynomial(value):
    return {ZERO: Q(value)} if value else {}


def add(*terms):
    out = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, Q(0))+value
    return {key: value for key, value in out.items() if value}


def scale(a, factor):
    return {key: value*factor for key, value in a.items() if value*factor}


def multiply(*terms):
    out = polynomial(1)
    for term in terms:
        next_out = {}
        for key, value in out.items():
            for other_key, other_value in term.items():
                target = tuple(x+y for x, y in zip(key, other_key))
                next_out[target] = next_out.get(target, Q(0))+value*other_value
        out = {key: value for key, value in next_out.items() if value}
    return out


def symbolic_audit():
    t1, t2, t3, x, y, a, b = [
        {tuple(int(i == j) for i in range(7)): Q(1)} for j in range(7)]
    sub = lambda u, v: add(u, scale(v, -1))
    d = sub(t2, multiply(t1, t1))
    n = sub(t3, multiply(t1, t2))
    m = sub(multiply(n, t1), multiply(d, t2))
    sep, left, right = sub(y, x), sub(y, t1), sub(t1, x)
    residuals = {
        'orthogonality0': add(multiply(d, t2), scale(multiply(n, t1), -1), m),
        'orthogonality1': add(multiply(d, t3), scale(multiply(n, t2), -1), multiply(m, t1)),
        'weight_sum': sub(add(left, right), sep),
        'weighted_first_moment': sub(add(multiply(left, x), multiply(right, y)), multiply(t1, sep)),
        'second_moment_recurrence': sub(sub(multiply(n, t1), m), multiply(d, t2)),
        'third_moment_recurrence': sub(sub(multiply(n, t2), multiply(m, t1)), multiply(d, t3)),
    }
    # A weighted recurrence follows from q(x)=q(y)=0, not merely from
    # an interval residual containing zero. Clear the weight denominator.
    qx = add(multiply(x, x), scale(multiply(a, x), -1), b)
    qy = add(multiply(y, y), scale(multiply(a, y), -1), b)
    for j in (0, 1):
        xp, yp = polynomial(1), polynomial(1)
        for _ in range(j):
            xp, yp = multiply(xp, x), multiply(yp, y)
        sj = add(multiply(left, xp), multiply(right, yp))
        sj1 = add(multiply(left, xp, x), multiply(right, yp, y))
        sj2 = add(multiply(left, xp, x, x), multiply(right, yp, y, y))
        recurrence = add(sj2, scale(multiply(a, sj1), -1), multiply(b, sj))
        node_terms = add(multiply(left, xp, qx), multiply(right, yp, qy))
        residuals[f'node_implies_recurrence_{j}'] = sub(recurrence, node_terms)
    for name, residual in residuals.items():
        check('symbolic '+name, not residual)
    factors = [Q(factorial(2*j), factorial(j)) for j in range(4)]
    ref = [(-1)**j*comb(3, j)/factors[j] for j in range(4)]
    check('reference cubic coefficients', ref == list(map(Q, ['1', '-3/2', '1/4', '-1/120'])))
    conversions = [ref[j]*factors[j]-(-1)**j*comb(3, j) for j in range(4)]
    check('all factorial conversion identities', conversions == [0]*4)
    return {'variables': ['t1', 't2', 't3', 'x', 'y', 'A', 'B'],
            'cleared_residuals': {name: list(value.items()) for name, value in residuals.items()},
            'reference_coefficients': list(map(str, ref)),
            'conversion_factors': list(map(str, factors)),
            'conversion_residuals': list(map(str, conversions)),
            'qualification': 'Recurrence uses exact node equations; interval zero containment is not exactness.'}


def main():
    saved_path = ROOT/'scripts/theta-gauss/two-node-certificate-540.json'
    source_path = ROOT/'scripts/central-jacobi/fixed-model-certificate-476.json'
    audit_path = ROOT/'scripts/central-jacobi/audit-478/audit-report.json'
    saved, source, audit = [json.loads(p.read_text()) for p in (saved_path, source_path, audit_path)]
    original_paths = set(saved['provenance']) | set(audit['original_hashes'])
    original_paths.add(str(saved_path.relative_to(ROOT)))
    original_paths |= {'scripts/actual-fredholm/audit-433/audit-report.json',
                       'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'}
    before = {name: digest(ROOT/name) for name in sorted(original_paths)}
    for name, expected in saved['provenance'].items():
        check('step540 provenance '+name, before[name] == expected)
    for name, expected in audit['original_hashes'].items():
        check('step478 original '+name, before[name] == expected)
    check('all inherited original hashes retained', saved['inherited_original_hashes'] == audit['original_hashes'])
    check('L791 fixed source digest', digest(source_path) == '2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e')
    check('step478 PASS', audit['status'] == 'PASS' and audit['failures'] == [])
    names = ['inherited source hash matches L791', 'inherited source hash matches L778 audit',
             'inherited evaluator equals complete audited replay', 'prior L778 audit passed',
             'complex Cauchy radius', 'inherited error positive and below stated bound',
             'error interval retained unchanged']
    names += [f'actual_a {j}' for j in range(4)]
    names += [f'gamma {j}' for j in range(4)]
    names += [f'gamma positivity {j}' for j in range(4)]
    selected = [entry for entry in audit['checks'] if entry['name'] in names]
    check('exact nineteen distinct selected names', len(selected) == 19 and {v['name'] for v in selected} == set(names))
    check('complete nineteen records retained', selected == saved['selected_audit_checks'])
    check('nineteen inherited passes', all(v['passed'] is True for v in selected))

    ancestor = ROOT/source['source']
    inherited = json.loads(ancestor.read_text())['evaluation']
    prior = json.loads((ROOT/'scripts/actual-fredholm/audit-433/audit-report.json').read_text())
    replay = json.loads((ROOT/'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json').read_text())
    check(names[0], digest(ancestor) == source['source_sha256'])
    check(names[1], digest(ancestor) == prior['original_sha256'])
    check(names[2], inherited == replay['evaluation'])
    check(names[3], prior['status'] == 'PASS' and prior['failures'] == [])
    check(names[4], inherited['uniform_disk_radius'] == 1600)
    eg = box(inherited['uniform_G_error'])
    check(names[5], 0 < eg[0] <= eg[1] < Q('3.141e-48'))
    check(names[6], source['uniform_G_error'] == inherited['uniform_G_error'])
    provenance_values = []
    for j in range(4):
        error = eg[1]/1600**j
        coeff = plus(box(inherited['coefficients'][j]), (-error, error))
        actual = box(source['actual_a'][j])
        gamma_from_a = times(actual, const(8*4**j*factorial(j)))
        check(f'actual_a {j}', contains(actual, coeff))
        check(f'gamma {j}', contains(box(source['gamma'][j]), gamma_from_a))
        check(f'gamma positivity {j}', gamma_from_a[0] > 0)
        provenance_values.append({'j': j, 'coefficient_error': str(error),
                                  'coefficient_with_Cauchy_error': serial(coeff),
                                  'actual_a': serial(actual), 'gamma_from_actual_a': serial(gamma_from_a)})
    gamma = [box(v) for v in source['gamma'][:4]]
    check('complete gamma decimal provenance', saved['input_gamma_decimal'] == source['gamma'][:4])
    check('complete gamma rational parsing', [serial(v) for v in gamma] == saved['input_gamma_rational'])
    t = [const(1)] + [times(over(gamma[j], gamma[0]), const(factorial(2*j)//factorial(j))) for j in range(1, 4)]
    check('raw moments exact saved reconstruction', [serial(v) for v in t] == saved['raw_moments'])
    symbolic = symbolic_audit()
    check('saved conversion factors', symbolic['conversion_factors'] == saved['conversion_factors'])
    d = minus(t[2], times(t[1], t[1]))
    a = over(minus(t[3], times(t[1], t[2])), d)
    b = minus(times(a, t[1]), t[2])
    discriminant = minus(times(a, a), times(const(4), b))
    for name, value in {'D': d, 'A': a, 'B': b, 'discriminant': discriminant}.items():
        check('saved node polynomial '+name, serial(value) == saved['node_polynomial'][name])
    original_sqrt = box(saved['node_polynomial']['sqrt_discriminant'])
    check('stored sqrt positive', original_sqrt[0] > 0)
    check('stored sqrt lower exact square', original_sqrt[0]**2 <= discriminant[0])
    check('stored sqrt upper exact square', original_sqrt[1]**2 >= discriminant[1])
    sqrt = sqrt_enclosure(discriminant)
    check('stored sqrt encloses independent sqrt', contains(original_sqrt, sqrt))

    def make_nodes(sq):
        return [over(minus(a, sq), const(2)), over(plus(a, sq), const(2))]

    def make_weights(nodes):
        sep = minus(nodes[1], nodes[0])
        return [over(minus(nodes[1], t[1]), sep), over(minus(t[1], nodes[0]), sep)]

    old_nodes, nodes = make_nodes(original_sqrt), make_nodes(sqrt)
    old_weights, weights = make_weights(old_nodes), make_weights(nodes)
    check('saved nodes exact reconstruction', [serial(v) for v in old_nodes] == saved['nodes'])
    check('saved weights exact reconstruction', [serial(v) for v in old_weights] == saved['weights'])
    means = [minus(t[1], old_nodes[0]), minus(old_nodes[1], t[1])]
    check('saved mean-between-nodes bounds', [serial(v) for v in means] == saved['mean_between_nodes'])
    denominators = {'gamma0': gamma[0], 'D': d, '2': const(2), 'v1': old_nodes[0],
                    'v2': old_nodes[1], 'v2_minus_v1': minus(old_nodes[1], old_nodes[0]), '120': const(120)}
    check('all saved denominators reconstructed', {k: serial(v) for k, v in denominators.items()} == saved['denominators'])
    for name, value in {**denominators, 'B': b, 'discriminant': discriminant,
                        'weight1': old_weights[0], 'weight2': old_weights[1],
                        'mean_minus_v1': means[0], 'v2_minus_mean': means[1]}.items():
        check('positive '+name, value[0] > 0)
    check('ordered disjoint node boxes', old_nodes[0][1] < old_nodes[1][0])
    moment_boxes = [plus(times(old_weights[0], power(old_nodes[0], j)),
                         times(old_weights[1], power(old_nodes[1], j))) for j in range(4)]
    residuals = [minus(moment_boxes[j], t[j]) for j in range(4)]
    check('saved moment evaluation boxes', [serial(v) for v in moment_boxes] == saved['moment_evaluation_boxes'])
    check('saved residual boxes (not exactness)', [serial(v) for v in residuals] == saved['moment_residual_boxes_not_exactness_proof'])
    check('interval residual consistency only', all(v[0] <= 0 <= v[1] for v in residuals))

    roots = [box(v) for v in saved['reference_roots']]
    root_values = [[h(v) for v in interval] for interval in roots]
    check('all six stored root endpoint values', [serial(v) for v in root_values] == saved['reference_endpoint_values'])
    for j, (interval, values) in enumerate(zip(roots, root_values)):
        check(f'root {j+1} positive bracket', interval[0] > 0 and interval[0] < interval[1])
        check(f'root {j+1} opposite endpoint signs', values[0]*values[1] < 0)
        check(f'root {j+1} signed orientation', values[0]*(-1 if j != 1 else 1) > 0)
    check('three disjoint brackets exhaust cubic', all(roots[j][1] < roots[j+1][0] for j in range(2)))
    # Existing valid brackets already establish all three simple roots.
    # Refine locally to provide independent scaled enclosures as well.
    refined = []
    for low, high in roots:
        for _ in range(8):
            mid = (low+high)/2
            if h(low)*h(mid) < 0:
                high = mid
            else:
                low = mid
        check('refined strict sign change', h(low)*h(high) < 0)
        refined.append((low, high))
    old_lists = [[over(r, node) for r in roots] for node in old_nodes]
    lists = [[over(r, node) for r in refined] for node in nodes]
    old_gaps = [minus(old_lists[1][j+1], old_lists[0][j]) for j in range(2)]
    gaps = [minus(lists[1][j+1], lists[0][j]) for j in range(2)]
    check('complete saved scaled roots', [[serial(v) for v in row] for row in old_lists] == saved['scaled_root_lists'])
    check('both complete saved gap boxes', [serial(v) for v in old_gaps] == saved['interlacer_gaps_upper_minus_lower'])
    for j in range(2):
        check(f'independent gap {j+1} inside original', contains(old_gaps[j], gaps[j]))
    for name, old, new in [('nodes', old_nodes, nodes), ('weights', old_weights, weights), ('interlacer_gaps', old_gaps, gaps)]:
        display = [box(v) for v in saved['outward_display'][name]]
        check('outward displayed '+name, all(contains(e, v) for e, v in zip(display, old)))
        check('independent reconstruction inside saved '+name, all(contains(e, v) for e, v in zip(old, new)))
    check('all six displayed scaled roots', all(contains(box(saved['outward_display']['scaled_roots'][i][j]), old_lists[i][j]) for i in range(2) for j in range(3)))
    check('first interlacer slot strictly passes', gaps[0][0] >= Q('1.000637'))
    check('second interlacer slot strictly fails', gaps[1][1] <= Q('-195.451439') < 0)
    check('saved failure states slot2 only', saved['criterion_failures'] == ['interlacer slot 2: upper-minus-lower strictly negative'])
    check('saved verification list and outcome', saved['verification_failures'] == [] and saved['outcome'] == 'COMMON_INTERLACING_OBSTRUCTION')
    after = {name: digest(ROOT/name) for name in sorted(original_paths)}
    check('all original artifacts unchanged', before == after)

    evidence.update(input_hashes=before, selected_records=selected,
                    inherited_error=serial(eg), selected_coefficient_provenance=provenance_values,
                    complete_gamma_decimal=source['gamma'][:4], complete_gamma_rational=[serial(v) for v in gamma],
                    raw_moments=[serial(v) for v in t], symbolic=symbolic,
                    node_polynomial={k: serial(v) for k, v in {'D': d, 'A': a, 'B': b, 'discriminant': discriminant}.items()},
                    stored_sqrt=serial(original_sqrt), independent_sqrt=serial(sqrt),
                    positive_denominators={k: serial(v) for k, v in denominators.items()},
                    saved_nodes=[serial(v) for v in old_nodes], independent_nodes=[serial(v) for v in nodes],
                    saved_weights=[serial(v) for v in old_weights], independent_weights=[serial(v) for v in weights],
                    stored_reference_roots=[serial(v) for v in roots], all_six_exact_endpoint_values=[serial(v) for v in root_values],
                    refined_reference_roots=[serial(v) for v in refined], refined_endpoint_values=[[str(h(x)) for x in v] for v in refined],
                    saved_scaled_roots=[[serial(v) for v in row] for row in old_lists],
                    independent_scaled_roots=[[serial(v) for v in row] for row in lists],
                    complete_saved_gaps=[serial(v) for v in old_gaps], independent_gaps=[serial(v) for v in gaps],
                    outward_bounds=saved['outward_display'],
                    requirements={'interlacer_slots': 'both gaps >=0, weak equality allowed',
                                  'denominators_nodes_weights': '>0', 'identity': 'exact cleared algebra, not residual containment'},
                    algebraic_scope='q(v) is raw-nu orthogonal, not Jensen P2; simultaneous negation preserves the convex identity and roots for MSS positive-leading convention.',
                    inherited_qualifications='L778 analytic evaluator and Decimal contracts retained; no independent transcendental backend verification, all-degree signs or RH conclusion.')
    report = {'status': 'PASS' if not failures else 'FAIL', 'checks': checks,
              'failures': failures, 'evidence': evidence, 'program_sha256': digest(Path(__file__)),
              'scope': 'Independent finite audit of L805 only; source coverage reused.'}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print('status:', report['status'], '; checks:', len(checks), '; failures:', failures)
    print('actual outward gaps:', saved['outward_display']['interlacer_gaps'])
    print('required: both >=0; first passes, second strictly fails')
    print('identity: exact symbolic clearings; inherited/backend qualifications retained')
    print('complete audit certificate:', OUT.relative_to(ROOT))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
