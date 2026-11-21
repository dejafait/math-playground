"""Exact saved-data consistency checks, not an independent evaluator audit."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parent
path = BASE/'filon-586.json'
r = json.loads(path.read_text())
checks = {}


def pair(v):
    a, b = map(F, v)
    assert a <= b
    return a, b


def contains(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def mul(a, b):
    vals = [x*y for x in a for y in b]
    return min(vals), max(vals)


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


checks['fixed_caps'] = r['caps'] == dict(u_panels=1024, u_end=3, n_max=4, x_cells=67, x_width='0.5', retries=0)
checks['u_node_grid'] = len(r['nodes']) == 2049 and all(pair(n['u']) == (F(3*k, 2048),)*2 for k, n in enumerate(r['nodes']))
checks['x_closed_cover'] = len(r['cells']) == 67 and all(pair(c['x']) == (F(k+13, 2), F(k+14, 2)) for k, c in enumerate(r['cells']))
checks['panel_cover'] = len(r['panels']) == 1024 and all(pair(p['u']) == (F(3*k, 1024), F(3*(k+1), 1024)) for k, p in enumerate(r['panels']))
h = F(3, 2048)
checks['panel_errors_outward'] = all(
    pair(p['integrated_remainder'][f][j])[1] >= max(map(abs, pair(p['third_derivative'][f][j])))*h*h*h*h/3
    for p in r['panels'] for f in range(2) for j in range(3))
checks['total_errors_outward'] = all(
    pair(r['interpolation_errors'][f][j])[1] >= sum(pair(p['integrated_remainder'][f][j])[1] for p in r['panels'])
    for f in range(2) for j in range(3))
checks['all_finite_sums_outward'] = all(
    contains(pair(c['finite_sums'][f][j]),
             (sum(F(p[f][j][0]) for p in c['panel_integrals']),
              sum(F(p[f][j][1]) for p in c['panel_integrals'])))
    for c in r['cells'] for f in range(2) for j in range(3))
checks['full_errors_added'] = all(
    contains(pair(c['F' if f == 0 else 'S'][j]),
             (F(c['finite_sums'][f][j][0])-F(r['interpolation_errors'][f][j][1])-F(r['u_tail'][1])-(F(r['n_tail'][1]) if f == 0 else 0),
              F(c['finite_sums'][f][j][1])+F(r['interpolation_errors'][f][j][1])+F(r['u_tail'][1])+(F(r['n_tail'][1]) if f == 0 else 0)))
    for c in r['cells'] for f in range(2) for j in range(3))
checks['normalization_and_W_Wp_outward'] = all(
    all(contains(pair(c['G'][j]), mul(pair(r['normalization']), pair(c['S'][j]))) for j in range(3))
    and contains(pair(c['W']), sub(mul(pair(c['F'][0]), pair(c['G'][1])), mul(pair(c['G'][0]), pair(c['F'][1]))))
    and contains(pair(c['Wp']), sub(mul(pair(c['F'][0]), pair(c['G'][2])), mul(pair(c['G'][0]), pair(c['F'][2]))))
    for c in r['cells'])
exclusions = []
for k, c in enumerate(r['cells']):
    fs, gs, w = pair(c['F'][0]), pair(c['G'][0]), pair(c['W'])
    expected = ('same_sign_event_exclusion' if (fs[0] > 0 and gs[0] > 0) or (fs[1] < 0 and gs[1] < 0)
                else 'W_event_exclusion' if w[0] > 0 or w[1] < 0 else 'unresolved')
    assert c['kind'] == expected and c['unresolved'] == (expected == 'unresolved')
    if expected != 'unresolved':
        exclusions.append(dict(index=k, x=c['x'], kind=expected,
                               F=c['F'][0], G=c['G'][0], W=c['W']))
checks['complete_classification_and_unresolved_cover'] = (exclusions == r['exclusions']
    and r['unresolved_cover'] == [c['x'] for c in r['cells'] if c['unresolved']])
checks['seven_originally_unresolved_cells'] = len(exclusions) == 7 and all(
    c['comparison579']['kind'] == 'unresolved' for c in r['cells'])
checks['actual_argument_range'] = contains((F(0), F(120)), pair(r['trig_argument_range']))
checks['saved_inputs_unchanged'] = all(hashlib.sha256((BASE.parent.parent/p).read_bytes()).hexdigest() == s
                                       for p, s in {**r['provenance'], **r['input_sha256']}.items())
summary = dict(actual_new_exclusions=7, required_new_exclusions=1,
               same_sign_cell=['6.5', '7'], F_lower_greater_than='0.14439', G_lower_greater_than='0.01447',
               W_cells=['7', '10'], negative_W_distance_greater_than='0.00012224',
               unresolved_cells=60, unresolved_region=['10', '40'], independent_audit='pending')
checks['stated_strict_margins'] = (F(exclusions[0]['F'][0]) > F('0.14439')
    and F(exclusions[0]['G'][0]) > F('0.01447')
    and all(F(c['W'][1]) < -F('0.00012224') for c in exclusions[1:]))
failures = [k for k, v in checks.items() if not v]
out = BASE/'check-filon-586.json'
out.write_text(json.dumps(dict(scope='exact saved arithmetic relations; no exp/trig/jet replay or independent source audit',
                              certificate_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                              checks=checks, failures=failures, summary=summary), indent=2)+'\n')
print(json.dumps(dict(summary=summary, checks_passed=sum(checks.values()), checks_required=len(checks),
                      failures=failures, certificate=str(out))))
raise SystemExit(bool(failures))
