#!/usr/bin/env python3
"""Full census/arithmetic audit and isolated replay of fixed test2258."""
import ast
import contextlib
from fractions import Fraction as R
import hashlib
import io
import json
from math import comb
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'quartic_first_zero_2258.py'
ORIGINAL = HERE / 'quartic_first_zero_2258.json'
REPLAY = HERE / 'quartic_first_zero_replay_2259.json'
OUTPUT = HERE / 'quartic_first_zero_audit_2259.json'
LOG = HERE / 'quartic_first_zero_replay_2259.log'
checks, failures = [], []


def check(name, condition):
    checks.append({'check': name, 'passed': bool(condition)})
    if not condition:
        failures.append(name)


def read_interval(value):
    a, b = R(value['lower']), R(value['upper'])
    check('interval endpoints ordered', a <= b)
    return a, b


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def product(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def difference(a, b):
    return a[0]-b[1], a[1]-b[0]


def derivative(p):
    return {i-1: i*a for i, a in p.items() if i and a}


def next_polynomial(p):
    q = derivative(p)
    for i, a in p.items():
        for k, v in ((1, -2), (3, -4)):
            q[i+k] = q.get(i+k, 0) + a*v
    return {i: a for i, a in q.items() if a}


def weight(i):
    k = (i+3)//4
    return max(R(1), R(k, 2)**k) if k else R(1)


source_bytes = SOURCE.read_bytes()
original_bytes = ORIGINAL.read_bytes()
c = json.loads(original_bytes)
check('original source hash', c['script_sha256'] == hashlib.sha256(source_bytes).hexdigest())
check('original status and empty failures', c['status'] == 'NONPOSITIVE_CURVATURE' and not c['failures'])
setup = c['setup']
check('fixed setup', setup == {
    'kernel': 'exp(-u^4-u^2)', 'u': 1, 'cap': 8, 'mesh': '1/32',
    'panels': 2048, 'finite_interval': '[0,4]', 'shift_interval': '[1,4]',
    'bisections_max': 10, 'trig_degree': 25, 'trig_remainder_order': 26})

# Independent sparse polynomial arithmetic for the complete C4 majorants.
p = {0: 1}
bk, btk = [], []
previous_bound = R(0)
for j in range(5):
    dense = c['bounds']['K_derivative_polynomials'][j]
    check(f'polynomial P{j}', p == {i: a for i, a in enumerate(dense) if a})
    b = sum((abs(a)*weight(i) for i, a in p.items()), R(0))
    tb = sum((abs(a)*weight(i+1) for i, a in p.items()), R(0)) + j*previous_bound
    bk.append(b)
    btk.append(tb)
    previous_bound = b
    p = next_polynomial(p)
check('all K derivative bounds', list(map(R, c['bounds']['BK'])) == bk == list(map(R, (1, 6, 42, 508, 5228))))
check('all tK derivative bounds', list(map(R, c['bounds']['BtK'])) == btk == list(map(R, (1, 7, 54, 634, 12316))))
d4 = sum(comb(4, j)*8**(4-j)*bk[j] for j in range(5))
d4t = sum(comb(4, j)*8**(4-j)*btk[j] for j in range(5))
check('complete fourth derivative bounds', d4 == R(c['bounds']['D4']) == 53996 and d4t == R(c['bounds']['D4t']) == 71772)
h = R(1, 512)
for name, length, bound, display in (
        ('simpson_F', 4, d4, '1.746101e-8'),
        ('simpson_Fprime', 4, d4t, '2.320934e-8'),
        ('simpson_shift', 3, d4, '1.309576e-8')):
    check(name + ' exact error and displayed upper', length*h**4*bound/180 <= R(c['bounds'][name]) < R(display))

# Complete census, with continuity, interpolation and derivative certificates.
cells = c['census']
check('148 cells', len(cells) == 148)
margins = []
for i, cell in enumerate(cells):
    left, right = R(cell['left']), R(cell['right'])
    fl, fr = read_interval(cell['F_left']), read_interval(cell['F_right'])
    check(f'cell{i} endpoints', (left, right) == (R(i, 32), R(i+1, 32)))
    if i:
        check(f'cell{i} shared endpoint', cell['F_left'] == cells[i-1]['F_right'])
    interp = R(cell['interpolation_lower'])
    check(f'cell{i} outward interpolation', interp <= min(fl[0], fr[0])-R(1, 8192))
    if i < 147:
        check(f'cell{i} strictly positive', cell['result'] == 'POSITIVE_BY_INTERPOLATION' and interp > 0)
        margins.append(interp)
    else:
        fp = read_interval(cell['Fprime_midpoint'])
        du = R(cell['Fprime_cell_upper'])
        check('crossing signs and label', cell['result'] == 'UNIQUE_FIRST_ZERO_CELL' and fl[0] > 0 > fr[1])
        check('whole crossing cell strict decrease', fp[1]+R(1, 64) <= du < 0)
        check('displayed crossing margins', fl[0] > R('0.00044030') and fr[1] < R('-0.00146124'))
        check('displayed derivative bounds', fp[1] < R('-0.06084930249') and du < R('-0.04522430249'))
check('displayed interpolation margin', min(margins) > R('0.00031823'))

lo, hi = R(cells[-1]['left']), R(cells[-1]['right'])
endpoint_intervals = {lo: cells[-1]['F_left'], hi: cells[-1]['F_right']}
check('ten bisections', len(c['bisection']) == 10)
for i, item in enumerate(c['bisection']):
    mid, value = R(item['point']), read_interval(item['F'])
    check(f'bisection{i} midpoint', mid == (lo+hi)/2)
    if item['sign'] == 'positive':
        check(f'bisection{i} positive sign', value[0] > 0)
        lo = mid
    elif item['sign'] == 'negative':
        check(f'bisection{i} negative sign', value[1] < 0)
        hi = mid
    else:
        check(f'bisection{i} resolved sign', False)
    endpoint_intervals[mid] = item['F']
root = c['root']
check('final first simple root', (lo, hi) == (R(root['lower']), R(root['upper'])) == (R(150761, 32768), R(75381, 16384)) and root['simple'] is True and 0 < lo < hi < 8)
check('final endpoint evidence', endpoint_intervals[lo] == root['F_lower'] and endpoint_intervals[hi] == root['F_upper'])
check('displayed root signs', read_interval(root['F_lower'])[0] > R('9.8579158e-7') and read_interval(root['F_upper'])[1] < R('-8.5631636e-7'))
check('root center and radius', (R(root['center']), R(root['radius'])) == ((lo+hi)/2, (hi-lo)/2) == (R(301523, 65536), R(1, 65536)))

# Only OUT is redirected in a parsed copy. All original math executes intact.
tree = ast.parse(source_bytes, filename=str(SOURCE))
redirected = 0
for node in tree.body:
    if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'OUT' for t in node.targets):
        node.value = ast.Call(func=ast.Name(id='Path', ctx=ast.Load()), args=[ast.Constant(str(REPLAY))], keywords=[])
        redirected += 1
check('only unique OUT assignment redirected', redirected == 1)
ast.fix_missing_locations(tree)
namespace = {'__file__': str(SOURCE), '__name__': '__main__'}
log = io.StringIO()
with contextlib.redirect_stdout(log):
    exec(compile(tree, str(SOURCE), 'exec'), namespace)
LOG.write_text(log.getvalue())
replay = json.loads(REPLAY.read_text())
for key in c:
    if key != 'runtime':
        check('complete replay equality: ' + key, c[key] == replay[key])
check('original certificate preserved', ORIGINAL.read_bytes() == original_bytes)
check('original source preserved', SOURCE.read_bytes() == source_bytes)

# Inspect the actual replay's intermediate interval endpoints using exact
# rationals; this is additional checking, not a different integration scheme.
def ns_interval(name):
    return tuple(R(str(v)) for v in namespace[name])

def check_outward(name, actual, intended):
    check(name, contains(actual, intended))

exp272 = tuple(R(str(v)) for v in namespace['expq'](-272))
check('tail F complete tangent bound', exp272[1]/264 <= R(c['bounds']['tail_F']) < R('2.821e-121'))
check('tail Fprime complete tangent bound', exp272[1]*(R(4, 264)+R(1, 264**2)) <= R(c['bounds']['tail_Fprime']) < R('1.130e-120'))
check('all trig increments within Taylor scope', 8*h == R(1, 64))
check('positive even panel counts and complete shifted range', 2048*h == 4 and (2048-512)*h == 3 and 512*h == 1 and 2048 % 2 == (2048-512) % 2 == 0)
radius = R(root['radius'])
for field, sine in (('A_sine', True), ('B_cosine', False)):
    raw = namespace['integrate'](R(root['center']), start=512, sine=sine)
    raw = tuple(R(str(v)) for v in raw)
    check_outward(field + ' full root-radius inflation', read_interval(c['curvature'][field]), (raw[0]-radius/2, raw[1]+radius/2))
cv = c['curvature']
xx, aa, bb = (lo, hi), read_interval(cv['A_sine']), read_interval(cv['B_cosine'])
g, gp, gpp, delta = (read_interval(cv[f]) for f in ('G', 'Gprime', 'Gsecond', 'Delta'))
xx2 = product(xx, xx)
check_outward('G product', g, product(xx, aa))
gp_unsigned = product(xx2, bb)
check_outward('Gprime product', gp, (-gp_unsigned[1], -gp_unsigned[0]))
k1 = tuple(R(str(v)) for v in namespace['expq'](-2))
check_outward('Gsecond ODE enclosure', gpp, product(xx2, difference(k1, g)))
check_outward('Delta complete outward enclosure', delta, difference(product(g, gpp), product(gp, gp)))
for name, value, lower, upper in (
        ('G', g, '0.03370892', '0.03377948'),
        ('Gprime', gp, '-0.29928826', '-0.29896072'),
        ('Gsecond', gpp, '2.14972505', '2.15124695'),
        ('Delta detailed', delta, '-0.017108533136863', '-0.016709525820705'),
        ('Delta conclusion', delta, '-0.017109', '-0.016709')):
    check('displayed ' + name, R(lower) < value[0] <= value[1] < R(upper))
check('negative determinant and positive inverse at1', g[0] > 0 and delta[1] < 0)

report = {
    'status': 'PASS' if not failures else 'FAIL',
    'scope': 'C919s fixed quartic first zero and curvature at u=1 only',
    'original_source_sha256': hashlib.sha256(source_bytes).hexdigest(),
    'original_certificate_sha256': hashlib.sha256(original_bytes).hexdigest(),
    'replay_runtime': replay['runtime'],
    'backend_qualification': 'CPython integers/Fraction and libmpdec rounding/exp/neighbor contracts remain assumptions; same-code replay is not independent verification of them',
    'analytic_review': 'See C919s Proof, Audit2259 subsection; no generic curvature theorem checked',
    'census_cells_checked': len(cells), 'signed_bisections_checked': len(c['bisection']),
    'checks': checks, 'failures': failures,
    'result': {'root': root, 'Delta': cv['Delta'], 'required_for_refutation': 'Delta.lower>0', 'actual': 'Delta.upper<0'},
    'artifacts': {'replay': REPLAY.name, 'replay_log': LOG.name},
}
OUTPUT.write_text(json.dumps(report, indent=2)+'\n')
print('audit:', report['status'], '; checks:', len(checks), '; cells:', len(cells), '; bisections:', len(c['bisection']))
print('root:', lo, hi, '; required: first positive root in(0,8)')
print('Delta:', cv['Delta']['lower'], cv['Delta']['upper'], '; refutation requires lower>0')
print('failures:', failures)
print('certificate:', OUTPUT)
print('replay:', REPLAY)
if failures:
    raise SystemExit(1)
