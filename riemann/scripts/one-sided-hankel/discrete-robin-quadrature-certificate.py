"""Exact boundary costs for one positive Robin-residue quadrature.

All pass/fail decisions are rational. L681 supplies the residue identity,
derivative bounds, finite-n transfer, and continuous coverage argument.
Only the existing audited series helpers are loaded from the preserved
L673 certificate; its mesh, output and certificate are not executed.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json

directory = Path(__file__).resolve().parent
helper_source = directory / 'positive-cone-contour-certificate.py'
source_text = helper_source.read_text()
boundary = '\npoints = {240:'
assert source_text.count(boundary) == 1
helper_text = source_text.split(boundary)[0]
ns = {'__name__': '__series_helpers__'}
exec(compile(helper_text, str(helper_source), 'exec'), ns)

add, mul = ns['add'], ns['mul']
logq, cmul = ns['logq'], ns['complex_mul']
series, ceil_scaled = ns['series_fixed'], ns['ceil_scaled']
PI, SCALE, SAVE_SCALE = ns['PI'], ns['SCALE'], ns['SAVE_SCALE']
d, U, b = Q(5, 4), Q(121, 64), Q(9, 20)
width = Q(7, 100)
required = -Q(3, 500)
points = {den: ns['circle_points'](den) for den in (300, 50)}
rows, checks, failures = [], [], []


def check(name, passed, actual, required_value):
    checks.append(dict(name=name, passed=bool(passed), actual=str(actual),
                       required=str(required_value)))
    if not passed:
        failures.append(name)


def certify_line(kind, s, y, den, error):
    a = (-d + s, y)
    a2 = a[0]**2 + a[1]**2
    assert Q(29, 25)**2 < a2 < Q(3, 2)**2
    inva = (a[0] / a2, -a[1] / a2)
    constant = mul(logq(d*d/a2), Q(1, 2))
    constant = add(constant, mul(PI, -Q(20, 27)*max(s, Q(0))))
    upper_constant = constant[1] + ns['four_series_error']
    for sign in (-1, 1):
        saved = []
        for ur0, ui in points[den]:
            ur = sign * ur0
            arguments = (cmul((ur, ui), inva), (-ur/d, -ui/d),
                         (-d*ur/U, d*ui/U), cmul(a, (ur/U, -ui/U)))
            val = (series(arguments[0]) - series(arguments[1])
                   + series(arguments[2]) - series(arguments[3]))
            saved.append(ceil_scaled(upper_constant + Q(val, SCALE)))
        sample_max = Q(max(saved), SAVE_SCALE)
        upper = sample_max + error
        row = dict(kind=kind, s=str(s), y=str(y), real_part_sign=sign,
                   v_denominator=den, sample_scale=SAVE_SCALE,
                   sample_upper_numerators=saved,
                   sampled_max_upper=str(sample_max),
                   interpolation_error=str(error), certified_upper=str(upper))
        rows.append(row)
        if upper >= required:
            failures.append(f'{kind} s={s} y={y} sign={sign}')


vertical_error = Q(8, 8)*Q(1, 200)**2 + Q(100, 8)*Q(1, 300)**2
top_error = Q(8, 8)*Q(1, 200)**2 + Q(100, 8)*Q(1, 50)**2
for j in range(91):
    certify_line('right', width, Q(j, 200), 300, vertical_error)
for j in range(-25, 15):
    # s=0 is a node, so no interpolation cell crosses the kink of max(s,0).
    certify_line('top', Q(j, 200), b, 50, top_error)

check('parameter second derivative bound', Q(625, 116)+Q(4096, 1875) < 8,
      Q(625, 116)+Q(4096, 1875), '< 8')
check('angular chart second derivative bound', Q(35359, 435) < 100,
      Q(35359, 435), '< 100')
check('finite-product t derivative', 4+Q(25, 4)+Q(96, 25)+Q(80, 41) < 17,
      4+Q(25, 4)+Q(96, 25)+Q(80, 41), '< 17')
check('top-height first derivative', Q(50, 9)+Q(64, 25) < 9,
      Q(50, 9)+Q(64, 25), '< 9')
check('top finite-n exponent cost', 9+9*Q(27, 20) < 22,
      9+9*Q(27, 20), '< 22')
check('sampling constant C/n', (100+10*PI[1])/27 < 5,
      (100+10*PI[1])/27, '< 5')
check('minimum right-side exponent for n>=15', Q(20, 27)*PI[0]*width*15 > 2,
      Q(20, 27)*PI[0]*width*15, '> 2')
check('e^2>6 by a finite positive Taylor sum',
      sum(Q(2)**k / __import__('math').factorial(k) for k in range(4)) > 6,
      sum(Q(2)**k / __import__('math').factorial(k) for k in range(4)), '> 6')
check('top kernel ratio',
      1+(Q(1, 8)+Q(9, 500))**2/Q(9, 25)**2 < Q(6, 5)**2,
      1+(Q(1, 8)+Q(9, 500))**2/Q(9, 25)**2, '< (6/5)^2')
check('rectangle perimeter contribution', Q(219, 100)*12/(2*3) < 5,
      Q(219, 100)*12/(2*3), '< 5')
check('point and left attenuation stronger than 3/500', Q(1, 67) > Q(3, 500),
      Q(1, 67), '> 3/500')
expected = ({('right', str(width), str(Q(j, 200)), sign)
             for j in range(91) for sign in (-1, 1)} |
            {('top', str(Q(j, 200)), str(b), sign)
             for j in range(-25, 15) for sign in (-1, 1)})
seen = {(r['kind'], r['s'], r['y'], r['real_part_sign']) for r in rows}
check('complete meshes and charts', seen == expected and len(rows) == len(expected),
      len(rows), len(expected))
count = sum(len(r['sample_upper_numerators']) for r in rows)
check('complete sample count', count == 117462, count, 117462)
max_index = max(range(len(rows)), key=lambda j: Q(rows[j]['certified_upper']))
max_row = rows[max_index]
maximum = Q(max_row['certified_upper'])
check('full continuous exponent bound', maximum < required, maximum, required)
certificate = dict(kind='exact rational mesh with analytic interpolation costs',
                   helper_source=helper_source.name,
                   helper_source_sha256=hashlib.sha256(source_text.encode()).hexdigest(),
                   helper_read_boundary=boundary.strip(), rows=rows, checks=checks,
                   sample_count=count, row_count=len(rows), maximum_upper=str(maximum),
                   required_upper=str(required), margin=str(required-maximum),
                   maximum_witness=dict(row_index=max_index,
                                        v_numerator=max_row['sample_upper_numerators'].index(
                                            max(max_row['sample_upper_numerators']))
                                        - max_row['v_denominator']),
                   failures=failures,
                   qualification='L681 supplies all analytic and finite-n arguments; '
                   '3/500 is weaker than the target rate >1/100.')
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Full boundary certificate: {count} samples in {len(rows)} rows')
print(f'Actual upper: {maximum}; required < {required}; margin {required-maximum}')
print(f'Original target rate > 1/100 remains unproved; failures: {failures}')
print(f'Certificate: {out}')
if failures:
    raise SystemExit(1)
