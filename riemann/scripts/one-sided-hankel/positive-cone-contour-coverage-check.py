"""Complete mesh/data consistency check, not an independent analytic audit."""
import ast
from fractions import Fraction as Q
import json
from pathlib import Path

root = Path(__file__).parent
certificate = json.loads((root/'positive-cone-contour-certificate.json').read_text())
failures = []


def check(condition, label):
    if not condition:
        failures.append(label)


def functions(path):
    tree = ast.parse(path.read_text())
    return {node.name: ast.dump(node, include_attributes=False)
            for node in tree.body if isinstance(node, ast.FunctionDef)}


old = functions(root/'angular-anchor-contour-certificate.py')
new = functions(root/'positive-cone-contour-certificate.py')
helpers = ['add', 'neg', 'mul', 'log_unit', 'logq', 'atan_small', 'atanq',
           'primitive', 'kernel', 'floor_scaled', 'ceil_scaled',
           'complex_mul', 'series_fixed', 'circle_points']
for name in helpers:
    check(old[name] == new[name], f'changed inherited helper: {name}')

expected = set()
for s in (-Q(3, 50), Q(3, 50)):
    for k in range(51):
        for sign in (-1, 1):
            expected.add(('vertical', s, Q(k, 100), sign, 240))
for k in range(7):
    for sign in (-1, 1):
        expected.add(('horizontal', -Q(3, 50)+Q(k, 50), Q(1, 2), sign, 30))

actual = set()
maximum = None
maximum_row = None
count = 0
for index, row in enumerate(certificate['rows']):
    identity = (row['kind'], Q(row['s']), Q(row['y']), row['real_part_sign'],
                row['v_denominator'])
    check(identity not in actual, f'duplicate row: {index}')
    actual.add(identity)
    saved = row['sample_upper_numerators']
    check(len(saved) == 2*row['v_denominator']+1, f'row {index}: missing chart points')
    check(all(isinstance(value, int) for value in saved), f'row {index}: noninteger sample')
    count += len(saved)
    sampled = Q(max(saved), row['sample_scale'])
    error = (Q(17, 8)*Q(1, 100)**2+Q(100, 8)*Q(1, 240)**2
             if row['kind'] == 'vertical'
             else Q(18, 8)*Q(1, 50)**2+Q(100, 8)*Q(1, 30)**2)
    upper = sampled+error
    check(sampled == Q(row['sampled_max_upper']), f'row {index}: sampled maximum')
    check(error == Q(row['interpolation_error']), f'row {index}: interpolation error')
    check(upper == Q(row['certified_upper']), f'row {index}: combined upper')
    check(all(Q(value, row['sample_scale'])+error < -Q(1, 200)
              for value in saved), f'row {index}: rate threshold')
    if maximum is None or upper > maximum:
        maximum, maximum_row = upper, index

check(actual == expected, 'complete contour/chart grid')
check(count == certificate['sample_count'] == 98978, 'sample count')
check(maximum == Q(certificate['maximum_upper']), 'global maximum')
check(-Q(1, 200)-maximum == Q(certificate['strict_margin']), 'strict margin')
check(maximum_row == certificate['maximum_witness']['row_index'], 'maximum row')
for item in certificate['checks']:
    check(Q(item['actual']) < Q(item['required']) and item['passed'], item['name'])
check(not certificate['failures'], 'certificate failure list')

# Independently retain both enclosure endpoints at one load-bearing point.
# Execute only the definition prefix, before any contour sampling loop.
namespace = {}
definition_prefix = (root/'positive-cone-contour-certificate.py').read_text().split(
    '# Tensor-product linear interpolation errors:')[0]
exec(compile(definition_prefix, 'positive-cone-certificate-definitions', 'exec'), namespace)
add, mul = namespace['add'], namespace['mul']
s, y = Q(3, 50), Q(1, 25)
ur, ui = -Q(6391, 6409), Q(480, 6409)
a = (-Q(5, 4)+s, y)
a2 = a[0]*a[0]+a[1]*a[1]
constant = add(mul(namespace['logq'](Q(25, 16)/a2), Q(1, 2)),
               namespace['kernel'](s, y))
constant = add(constant, mul(namespace['C_INTERVAL'], -s))
quadratic = -Q(3, 5)*(s*s-y*y)
constant = add(constant, (quadratic, quadratic))
cmul, sf = namespace['complex_mul'], namespace['series_fixed']
z1 = cmul((ur, ui), (a[0]/a2, -a[1]/a2))
z2 = (-ur/Q(5, 4), -ui/Q(5, 4))
z3 = (-Q(5, 4)*ur/Q(121, 64), Q(5, 4)*ui/Q(121, 64))
z4 = cmul(a, (ur/Q(121, 64), -ui/Q(121, 64)))
approximation = Q(sf(z1)-sf(z2)+sf(z3)-sf(z4), namespace['SCALE'])
lower = constant[0]+approximation-namespace['four_series_error']
upper = constant[1]+approximation+namespace['four_series_error']
save_scale = 10**12
lower_saved = Q(namespace['floor_scaled'](lower, save_scale), save_scale)
upper_saved = Q(namespace['ceil_scaled'](upper, save_scale), save_scale)
check(lower_saved > -Q(1, 100), 'fixed-contour point excludes rate 1/100')
point = dict(s=str(s), y=str(y), u_real=str(ur), u_imag=str(ui),
             exponent_lower=str(lower_saved), exponent_upper=str(upper_saved),
             target_upper='-1/100',
             meaning='This absolute contour exponent cannot be <=-1/100 everywhere; this is not a lower bound on kappa.')

out = Path(__file__).with_suffix('.json')
report = dict(
    scope='Complete exact saved-data/mesh check and inherited helper comparison; no independent source or analytic audit',
    rows=len(actual), samples=count, inherited_helpers=helpers,
    maximum=str(maximum), required='-1/200',
    strict_margin=str(-Q(1, 200)-maximum), fixed_contour_point=point,
    failures=failures)
out.write_text(json.dumps(report, indent=2)+'\n')
print(f'Checked all {len(actual)} rows and {count} sample bounds; inherited helpers unchanged.')
print(f'Actual upper: {maximum}; required < -1/200; failures: {failures}; report: {out}')
print(f'Fixed-contour point exponent: [{lower_saved}, {upper_saved}], above target -1/100.')
if failures:
    raise SystemExit(1)
