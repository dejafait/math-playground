"""Exact saved-data audit; no evaluator import, execution or census replay.

The analytic/source proof is canonical in L816, step588. In particular this
does not numerically regenerate exp, trig, kernel jets or panel integrals.
"""
from collections import Counter
from decimal import Decimal
from fractions import Fraction as F
from pathlib import Path
import ast
import hashlib
import json

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(name):
    return json.loads((BASE/name).read_text())


def pair(v):
    assert len(v) == 2 and all(Decimal(s).is_finite() for s in v)
    a, b = map(F, v)
    assert a <= b
    return a, b


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def div(a, b):
    assert not b[0] <= 0 <= b[1]
    return mul(a, (1/b[1], 1/b[0]))


def pt(x):
    return F(x), F(x)


def scale(a, x):
    return mul(a, pt(x))


def contains(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def intersection(a, b):
    v = max(a[0], b[0]), min(a[1], b[1])
    assert v[0] <= v[1]
    return v


r = read('filon-586.json')
old = read('census-579.json')
prior = read('check-filon-586.json')
repair, audit = read('exact-machin-583.json'), read('audit-584.json')
checks, counts, failures, cell_details = {}, Counter(), [], []


def check(name, ok, location=''):
    checks[name] = checks.get(name, True) and bool(ok)
    counts[name] += 1
    if not ok:
        failures.append(dict(check=name, location=location))


check('fixed_caps', r['caps'] == dict(u_panels=1024, u_end=3, n_max=4,
                                    x_cells=67, x_width='0.5', retries=0))
check('saved_hashes', all(sha(ROOT/p) == digest for p, digest in
                        {**r['provenance'], **r['input_sha256']}.items()))
check('prior_checker_bound_to_output', prior['certificate_sha256'] == sha(BASE/'filon-586.json')
      and len(prior['checks']) == 14 and all(prior['checks'].values()) and not prior['failures'])
check('qualified_input_chain', all(repair['checks'].values()) and not repair['failures']
      and all(audit['checks'].values()) and not audit['failures']
      and repair['provenance']['saved_certificate_sha256'] == sha(BASE/'census-579.json')
      and all(sha(BASE/p) == digest for p, digest in audit['input_hashes'].items()))
check('pi_c_and_tails_match_audited_inputs',
      r['pi'] == old['pi'] == repair['saved_pi']
      and r['normalization'] == old['normalization']
      and r['n_tail'] == old['n_tail_all_j'] and r['u_tail'] == old['u_tail_all_j'])
normal = pair(r['normalization'])
check('normalization_contains_full_quotient', pair(old['S0'])[0] > 0
      and normal[0] > 0 and contains(normal, div(pair(old['F0']), pair(old['S0']))))
tree = ast.parse((BASE/'filon-586.py').read_text())
check('no_power_syntax_or_power_method', not any(
    isinstance(n, ast.BinOp) and isinstance(n.op, ast.Pow)
    or isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute)
    and n.func.attr in ('power', '__pow__') for n in ast.walk(tree)))

h = F(3, 2048)
check('array_lengths', len(r['nodes']) == 2049 and len(r['panels']) == 1024
      and len(r['cells']) == 67)
for i, node in enumerate(r['nodes']):
    u = F(3*i, 2048)
    check('node_grid_and_amplitudes', pair(node['u']) == pt(u)
          and len(node['values']) == 2 and all(len(v) == 3 for v in node['values']), str(i))
    for family in range(2):
        v = [pair(a) for a in node['values'][family]]
        for j in (1, 2):
            check('node_moment_factors', contains(v[j], scale(v[0], u**j)), f'{i}/{family}/{j}')

error_sum = [F(0)]*6
for i, panel in enumerate(r['panels']):
    check('panel_grid_midpoint', pair(panel['u']) == (2*i*h, (2*i+2)*h)
          and pair(panel['mid']) == pt((2*i+1)*h), str(i))
    for family in range(2):
        for j in range(3):
            loc = f'{i}/{family}/{j}'
            left, center, right = [pair(r['nodes'][2*i+k]['values'][family][j]) for k in range(3)]
            exact = [center, scale(sub(right, left), 1/(2*h)),
                     scale(sub(add(right, left), scale(center, 2)), 1/(2*h*h))]
            check('all_coefficients_outward', all(contains(pair(v), e) for v, e in
                  zip(panel['coefficients'][family][j], exact)), loc)
            third = pair(panel['third_derivative'][family][j])
            bound = max(map(abs, third))*h**4/3
            error = pair(panel['integrated_remainder'][family][j])
            check('all_panel_errors_outward', error[0] >= 0 and contains(error, pt(bound)), loc)
            error_sum[3*family+j] += error[1]
errors = [[pair(v) for v in a] for a in r['interpolation_errors']]
for family in range(2):
    for j in range(3):
        check('total_errors_outward', errors[family][j][0] >= 0
              and errors[family][j][1] >= error_sum[3*family+j], f'{family}/{j}')

exclusions, unresolved, arguments = [], [], []
nt, ut = pair(r['n_tail']), pair(r['u_tail'])
for i, cell in enumerate(r['cells']):
    x = pair(cell['x'])
    check('closed_cell_and_old_evidence', x == (F(i+13, 2), F(i+14, 2))
          and cell['x'] == old['cells'][i+13]['x']
          and old['cells'][i+13]['kind'] == 'unresolved'
          and all(cell['comparison579'][key] == old['cells'][i+13][key]
                  for key in ('kind', 'F', 'G', 'W', 'Wp')), str(i))
    md = cell['moments']
    z, co, si = [pair(md[key]) for key in ('z', 'cos', 'sin')]
    check('moment_domain', z == scale(x, h) and 0 < z[0] <= z[1] < 1 and co[0] > 0, str(i))
    arguments.append(z)
    raw = [div(scale(si, 2), x), div(scale(sub(si, mul(z, co)), 2), mul(x, x)),
           div(scale(add(mul(sub(mul(z, z), pt(2)), si), scale(mul(z, co), 2)), 2),
               mul(mul(x, x), x))]
    crude = [(2*h*co[0], 2*h), (F(0), 2*x[1]*h**3/3),
             (2*h**3*co[0]/3, 2*h**3/3)]
    for k in range(3):
        a, b, c = [pair(md[key][k]) for key in ('exact_formula_intervals', 'integral_bounds', 'final')]
        check('raw_moment_formula_inclusion', contains(a, raw[k]), f'{i}/{k}')
        check('crude_moment_bound_inclusion', contains(b, crude[k]), f'{i}/{k}')
        check('moment_intersection_exact', c == intersection(a, b), f'{i}/{k}')
    check('panel_integral_count', len(cell['panel_integrals']) == 1024, str(i))
    totals = [[(F(0), F(0)) for _ in range(3)] for _ in range(2)]
    for p, integral in enumerate(cell['panel_integrals']):
        assert len(integral) == 2 and all(len(a) == 3 for a in integral)
        arguments.append(scale(x, (2*p+1)*h))
        for family in range(2):
            for j in range(3):
                totals[family][j] = add(totals[family][j], pair(integral[family][j]))
    for family in range(2):
        for j in range(3):
            finite = pair(cell['finite_sums'][family][j])
            check('all_finite_sums_outward', contains(finite, totals[family][j]), f'{i}/{family}/{j}')
            error = errors[family][j][1] + ut[1] + (nt[1] if family == 0 else 0)
            full = pair(cell['F' if family == 0 else 'S'][j])
            check('all_errors_added', contains(full, (finite[0]-error, finite[1]+error)), f'{i}/{family}/{j}')
            if family == 1:
                check('all_normalizations_outward', contains(pair(cell['G'][j]), mul(normal, full)), f'{i}/{j}')
    f, g = [[pair(v) for v in cell[key]] for key in ('F', 'G')]
    w, wp = pair(cell['W']), pair(cell['Wp'])
    check('all_W_Wp_outward', contains(w, sub(mul(f[0], g[1]), mul(g[0], f[1])))
          and contains(wp, sub(mul(f[0], g[2]), mul(g[0], f[2]))), str(i))
    kind = ('same_sign_event_exclusion' if f[0][0] > 0 and g[0][0] > 0 or f[0][1] < 0 and g[0][1] < 0
            else 'W_event_exclusion' if w[0] > 0 or w[1] < 0 else 'unresolved')
    check('all_classifications', cell['kind'] == kind and cell['unresolved'] == (kind == 'unresolved'), str(i))
    cell_details.append(dict(index=i, x=cell['x'], kind=kind, F=cell['F'], G=cell['G'], W=cell['W'], Wp=cell['Wp']))
    if kind == 'unresolved':
        unresolved.append(cell['x'])
    else:
        exclusions.append(dict(index=i, x=cell['x'], kind=kind, F=cell['F'][0], G=cell['G'][0], W=cell['W']))

arg_range = min(v[0] for v in arguments), max(v[1] for v in arguments)
check('all_actual_arguments_and_reduction', pair(r['trig_argument_range']) == arg_range
      and F(0) <= arg_range[0] <= arg_range[1] <= 120 and arg_range[1]/256 < 1)
check('full_exclusion_unresolved_lists', exclusions == r['exclusions'] and unresolved == r['unresolved_cover']
      and [c['index'] for c in exclusions] == list(range(7)) and len(unresolved) == 60
      and [pair(v) for v in unresolved] == [(F(k, 2), F(k+1, 2)) for k in range(20, 80)])
check('counts_and_coverage', r['coverage'] is True and r['counts'] == Counter(c['kind'] for c in cell_details)
      and r['actual_new_exclusions'] == 7 and r['required_new_exclusions'] == 1)
margin = min(-F(c['W'][1]) for c in exclusions[1:])
check('strict_margins', F(exclusions[0]['F'][0]) > F('0.14439')
      and F(exclusions[0]['G'][0]) > F('0.01447') and margin > F('0.00012224'))
error_caps = [['7.747e-8', '3.420e-8', '1.482e-8'], ['1.031e-8', '4.801e-9', '2.430e-9']]
check('reported_error_caps', all(errors[f][j][1] < F(error_caps[f][j]) for f in range(2) for j in range(3)))

summary = dict(conclusion='FAIL' if failures else 'PASS', check_groups_passed=sum(checks.values()),
               check_groups_required=len(checks), exclusions=7, required_new_exclusions=1,
               actual_bounds=['F > 0.14439 and G > 0.01447 on [6.5,7]',
                              'W < -0.00012224 on each of the six cells [7,10]'],
               required_bounds='strict same-sign F,G or nonzero W on the entire closed cell',
               unresolved_cells=60, unresolved_region=['10', '40'])
out = BASE/'audit-588.json'
out.write_text(json.dumps(dict(step='588', scope=__doc__, summary=summary,
    input_hashes={n:sha(BASE/n) for n in ('filon-586.py', 'filon-586.json', 'check-filon-586.py',
      'check-filon-586.json', 'census-579.json', 'audit-581.json', 'exact-machin-583.json', 'audit-584.json')},
    this_script_sha256=sha(Path(__file__)), checks=checks, comparison_counts=counts,
    failures=failures, exclusions=exclusions, unresolved_cover=unresolved, cells=cell_details,
    interpolation_errors=r['interpolation_errors'], actual_argument_range=r['trig_argument_range'],
    limitations=['Analytic and source inclusion proof is in L816 step588.',
                 'Correct original execution and the stated backend contracts remain hypotheses.',
                 'No transcendental, jet, panel-integral or census replay.',
                 'No event, orientation, global reference theorem, infinity or RH conclusion.']), indent=2)+'\n')
print(json.dumps(dict(summary=summary, failures=failures, certificate=str(out.relative_to(ROOT)))))
raise SystemExit(bool(failures))
