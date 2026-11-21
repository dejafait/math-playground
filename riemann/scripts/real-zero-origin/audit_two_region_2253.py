#!/usr/bin/env python3
"""Independent implementation of missing2251 layers; see C919r audit2253.

Fixed meshes/degrees/cutoffs. Higher precision is verification, not retuning.
All evidence is saved; the mathematical/backend qualifications are explicit.
"""
import decimal as dec
from decimal import Decimal as D
from fractions import Fraction as F
from math import factorial as fac, comb
from pathlib import Path
import hashlib
import json
import platform
import time

ROOT = Path(__file__).resolve().parent
PREF = ROOT / 'two_region_preflight_2251.json'
CERT = ROOT / 'two_region_2251.json'
OUT = ROOT / 'two_region_audit_2253.json'
started = time.monotonic()
p, c = json.loads(PREF.read_text()), json.loads(CERT.read_text())
contexts = [dec.Context(prec=110, rounding=r, Emin=-999999, Emax=999999)
            for r in [dec.ROUND_FLOOR, dec.ROUND_CEILING, dec.ROUND_HALF_EVEN]]
for context in contexts:
    for signal in context.traps:
        context.traps[signal] = signal not in (dec.Inexact, dec.Rounded)
    context.clear_flags()
dn, up, rn = contexts
failures, checks = [], 0
evidence = {}


def check(ok, label):
    global checks
    checks += 1
    if not ok:
        failures.append(label)


def interval(q):
    q = F(q)
    return (dn.divide(D(q.numerator), D(q.denominator)),
            up.divide(D(q.numerator), D(q.denominator)))


def plus(a, b):
    return dn.add(a[0], b[0]), up.add(a[1], b[1])


def minus(a):
    return a[1].copy_negate(), a[0].copy_negate()


def times(a, b):
    return (min(dn.multiply(x, y) for x in a for y in b),
            max(up.multiply(x, y) for x in a for y in b))


def positive_times(a, b):
    assert a[0] >= 0 and b[0] >= 0
    return dn.multiply(a[0], b[0]), up.multiply(a[1], b[1])


def exponential(a):
    return dn.next_minus(rn.exp(a[0])), up.next_plus(rn.exp(a[1]))


def pow_upper(a, k):
    assert a >= 0
    z = D(1)
    for _ in range(k):
        z = up.multiply(z, a)
    return z


def sum_upper(values):
    z = D(0)
    for v in values:
        z = up.add(z, v)
    return z


def enclose(a, radius):
    return dn.subtract(a[0], radius), up.add(a[1], radius)


def saved(a):
    return D(a['lower']), D(a['upper'])


def pack(a):
    return dict(lower=str(a[0]), upper=str(a[1]))


def includes(a, b):
    return a[0] <= b[0] <= b[1] <= a[1]


def atan(q, terms):
    a = sum((F((-1)**k, (2*k+1)*q**(2*k+1)) for k in range(terms)), F(0))
    b = a + F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(a, b), max(a, b)


def machin(n, m):
    a, b = atan(5, n), atan(239, m)
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


oldpi = machin(80, 25)
check(list(map(F, p['constants']['exact_pi_bounds'])) == list(oldpi), 'original exact Machin bounds')
check(F(3) < oldpi[0] < oldpi[1] < F(22, 7) and oldpi[1]**2 < 10, 'pi inequalities')
check(F(saved(p['constants']['pi'])[0]) <= oldpi[0] and
      F(saved(p['constants']['pi'])[1]) >= oldpi[1], 'original Decimal pi enclosure')
newpi = machin(100, 35)
pi = interval(newpi[0])[0], interval(newpi[1])[1]
check(includes(saved(p['constants']['pi']), pi), 'higher precision pi inclusion')
centers = [F(0)] + [F(2*i+1, 32) for i in range(1, 16)]
expected = dict(U=4, N=4, panels=16384, precision=80, x_center='57/4',
                x_degree=8, x_cells=32, u_degree=16, u_subcells=32,
                centers=list(map(str, centers)), spatial_cells=1280,
                required_J='0.01', required_I='1E-12')
check(p['parameters'] == c['parameters'] == expected, 'exact fixed settings')
check(len(p['centers']) == len(c['centers']) == 16, 'all centers')
check(len(p['spatial_cells']) == 1280, 'all spatial envelopes')
check(c['preflight_sha256'] == hashlib.sha256(PREF.read_bytes()).hexdigest(), 'preflight hash')
check(c['script_sha256'] == hashlib.sha256((ROOT/'two_region_2251.py').read_bytes()).hexdigest(), 'evaluator hash')

# Independently form the derivative operator using polynomial derivative,
# scalar multiplication, and shift; compare all exact rational coefficients.
polynomials = [[F(0), F(-12), F(8)]]
for m in range(17):
    a = polynomials[-1]
    derivative = [F(k)*a[k] for k in range(1, len(a))]
    b = [q/2 for q in a] + [F(0)]
    for k, q in enumerate(a):
        b[k+1] -= 2*q
    for k, q in enumerate(derivative):
        b[k+1] += 2*q
    polynomials.append(b)
check(polynomials == [[F(q) for q in a] for a in p['derivative_polynomials']], 'all exact derivative polynomials')
A = [sum((abs(q)*(4*k)**k for k, q in enumerate(a)), F(0)) for a in polynomials]
check(A == list(map(F, p['derivative_A'])), 'all A constants')
ip = [positive_times(interval(2*a), exponential(interval(F(-225, 4))))[1] for a in A]
sp = [positive_times(interval(2*a), exponential(interval(-512)))[1] for a in A]
for m in range(18):
    check(D(p['index_prefactors'][m]) >= ip[m], f'index prefactor{m}')
    check(D(p['spatial_prefactors'][m]) >= sp[m], f'spatial prefactor{m}')


def index_tail(m, j):
    return up.multiply(ip[m], interval(F(fac(j), 112**(j+1)))[1])


def spatial_tail(m, j):
    q = sum((F(comb(j, k)*4**(j-k)*fac(k), 1024**(k+1)) for k in range(j+1)), F(0))
    return up.multiply(sp[m], interval(q)[1])


rates = [positive_times(pi, interval(n*n)) for n in range(1, 5)]
absolute_coefficients = [[interval(abs(q))[1] for q in a] for a in polynomials]
signed_coefficients = [[interval(q) for q in a] for a in polynomials]


def positive_horner(aa, v):
    z = D(0)
    for a in reversed(aa):
        z = up.add(up.multiply(z, v), a)
    return z


eb = []
for k, row in enumerate(p['spatial_cells']):
    left, right = F(k, 256), F(k+1, 256)
    check((F(row['left']), F(row['right']), row['index']) == (left, right, k), f'spatial identity{k}')
    eleft, eright = exponential(interval(2*left)), exponential(interval(2*right))
    bounds = [D(0)]*18
    for rate in rates:
        vlo, vhi = dn.multiply(rate[0], eleft[0]), up.multiply(rate[1], eright[1])
        argument = up.subtract(interval(right/2)[1], vlo)
        weight = exponential((argument, argument))[1]
        for m in range(18):
            bounds[m] = up.add(bounds[m], up.multiply(weight, positive_horner(absolute_coefficients[m], vhi)))
    check(len(row['bounds']) == 18, f'orders{k}')
    for m in range(18):
        check(D(row['bounds'][m]) >= bounds[m], f'whole-cell bound{k}/{m}')
    eb.append(bounds)
evidence['spatial_bounds'] = [[str(z) for z in row] for row in eb]

compact9 = sum_upper(up.multiply(interval(F(1, 256))[1],
                                 up.multiply(interval(F(k+1, 256)**9)[1], eb[k][0])) for k in range(1024))
compact17 = sum_upper(up.multiply(interval(F(1, 256))[1], eb[k][17]) for k in range(1024))
for key, m, j, compact in [('moment9', 0, 9, compact9), ('derivative17', 17, 0, compact17)]:
    parts = dict(compact=compact, index=index_tail(m, j), spatial=spatial_tail(m, j))
    parts['total'] = sum_upper(parts.values())
    for name, value in parts.items():
        check(D(p[key][name]) >= value, f'{key}/{name}')
    evidence[key] = {name: str(value) for name, value in parts.items()}

errors, jets = [], []
for ci, center in enumerate(centers):
    maxima, witnesses = [D(0)]*9, [None]*9
    first = int(256*center)
    # Multinomial Leibniz formula, independently of the evaluator's nested sums.
    terms = [[(a, b, interval(F(fac(4), fac(a)*fac(b)*fac(4-a-b))*
                              F(57, 4)**(4-a-b)/fac(j-a))[1])
              for a in range(min(4, j)+1) for b in range(5-a)] for j in range(9)]
    for k in range(first, first+1024):
        powers = [interval((F(k+1, 256)-center)**q)[1] for q in range(9)]
        for j in range(9):
            val = sum_upper(up.multiply(constant, up.multiply(powers[j-a], eb[k][b]))
                            for a, b, constant in terms[j])
            if val > maxima[j]:
                maxima[j], witnesses[j] = val, k
    erows = []
    for j in range(9):
        values = dict(fourth=maxima[j],
                      simpson=up.multiply(interval(F(4**5, 180*16384**4))[1], maxima[j]),
                      index=up.divide(index_tail(0, j), D(fac(j))),
                      spatial=up.divide(spatial_tail(0, j), D(fac(j))))
        values['total'] = sum_upper(values[name] for name in ('simpson', 'index', 'spatial'))
        for name, value in values.items():
            check(D(p['centers'][ci]['errors'][j][name]) >= value, f'coefficient bound{ci}/{j}/{name}')
        erows.append(dict(j=j, maximizer=witnesses[j], **{name: str(value) for name, value in values.items()}))
    errors.append(dict(center=str(center), errors=erows))
    sums = [interval(0) for _ in range(16)]
    for rate in rates:
        v = positive_times(rate, exponential(interval(2*center)))
        weight = positive_times(exponential(interval(center/2)), exponential(minus(v)))
        powers = [interval(1)]
        for _ in range(19):
            powers.append(positive_times(powers[-1], v))
        for m in range(16):
            value = interval(0)
            for k, coefficient in enumerate(signed_coefficients[m]):
                value = plus(value, times(coefficient, powers[k]))
            sums[m] = plus(sums[m], times(weight, value))
    decay = exponential(interval(-112*center))[1]
    sums = [enclose(value, up.multiply(ip[m], decay)) for m, value in enumerate(sums)]
    for m in range(16):
        check(includes(saved(p['centers'][ci]['jets'][m]), sums[m]), f'signed kernel jet{ci}/{m}')
    jets.append(list(map(pack, sums)))
evidence['centers'] = errors
evidence['kernel_jets'] = jets
print('Preflight recomputed:', checks, 'checks;', len(failures), 'failures', flush=True)

# Exact rational trigonometric polynomials and the full Lagrange remainder.
d = F(57, 4)*F(4, 16384)
cs = sum(((-1)**k*d**(2*k)/fac(2*k) for k in range(16)), F(0))
ss = sum(((-1)**k*d**(2*k+1)/fac(2*k+1) for k in range(16)), F(0))
rem = d**32/fac(32)
stepc = interval(cs-rem)[0], interval(cs+rem)[1]
steps = interval(ss-rem)[0], interval(ss+rem)[1]
check(includes(saved(c['trigonometric']['step_cosine']), stepc), 'step cosine')
check(includes(saved(c['trigonometric']['step_sine']), steps), 'step sine')
check(F(c['trigonometric']['remainder']) >= rem, 'step remainder')
cosine, sine = interval(1), interval(0)
trigs = []
for i in range(16385):
    trigs.append((cosine, sine))
    if i < 16384:
        cosine, sine = (plus(times(cosine, stepc), minus(times(sine, steps))),
                        plus(times(sine, stepc), times(cosine, steps)))
evidence['trigonometric'] = dict(step_cosine=pack(stepc), step_sine=pack(steps),
                                 final_cosine=pack(cosine), final_sine=pack(sine))

node_count, replay = 0, []
for ci, center in enumerate(centers):
    sums = [[interval(0) for _ in range(9)] for _ in range(2)]
    for i, (ct, st) in enumerate(trigs):
        tq, sq = F(i, 4096), center+F(i, 4096)
        e2s, eshalf = exponential(interval(2*sq)), exponential(interval(sq/2))
        kernel = interval(0)
        for rate in rates:
            v = positive_times(rate, e2s)
            polynomial = plus(positive_times(interval(8), positive_times(v, v)),
                              minus(positive_times(interval(12), v)))
            assert polynomial[0] > 0
            kernel = plus(kernel, positive_times(polynomial, positive_times(eshalf, exponential(minus(v)))))
        weight = 1 if i in (0, 16384) else 2+2*(i % 2)
        node = positive_times(interval(weight), kernel)
        phases = [[ct, minus(st), minus(ct), st], [st, ct, minus(st), minus(ct)]]
        moment = F(1)
        for j in range(9):
            w = positive_times(interval(moment), node)
            for family in range(2):
                sums[family][j] = plus(sums[family][j], times(w, phases[family][j % 4]))
            moment *= tq/F(j+1)
        node_count += 1
    result = dict(center=str(center))
    for family, name in enumerate(('cosine', 'sine')):
        rows = []
        for j in range(9):
            quadrature = times(interval(F(1, 12288)), sums[family][j])
            check(includes(saved(c['centers'][ci][name][j]['quadrature']), quadrature), f'quadrature inclusion{ci}/{name}/{j}')
            enclosure = enclose(quadrature, D(errors[ci]['errors'][j]['total']))
            check(includes(saved(c['centers'][ci][name][j]['enclosure']), enclosure), f'full coefficient inclusion{ci}/{name}/{j}')
            rows.append(dict(j=j, quadrature=pack(quadrature), enclosure=pack(enclosure)))
        result[name] = rows
    replay.append(result)
    print('Independent quadrature center:', center, 'failures:', len(failures), flush=True)
check(node_count == 262160, 'complete node count')
evidence['quadrature'] = replay
flags = [{signal.__name__: bool(value) for signal, value in context.flags.items()} for context in contexts]
check(all(not value or signal in ('Inexact', 'Rounded') for record in flags for signal, value in record.items()), 'new arithmetic signals')
for artifact in (p, c):
    check(artifact['failures'] == [] and artifact['runtime']['unexpected_signals'] == [], 'original runtime pass')
    for record in artifact['runtime']['flags'].values():
        check(all(not value or signal in ('Inexact', 'Rounded') for signal, value in record.items()), 'original flags')
result = dict(status='PASS' if not failures else 'FAIL', checks=checks, failures=failures,
              original_bounds=c['uniform'], required={'J': '0.01', 'I': '1e-12'},
              counts=dict(spatial_bounds=1280*18, jets=16*16, error_records=16*9,
                          quadrature_intervals=16*18, nodes=node_count),
              precision=110, evidence=evidence, flags=flags,
              runtime=dict(python=platform.python_version(), libmpdec=dec.__libmpdec_version__,
                           elapsed_seconds=time.monotonic()-started),
              hashes={path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                      for path in [PREF, CERT, Path(__file__)]},
              qualification='Independent implementation, same explicit CPython/Fraction/libmpdec contracts; no backend verification. Complete exact cell reconstruction is separate. Analytic proof is in C919r audit2253.')
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('Audit:', result['status'], 'checks:', checks, 'failures:', len(failures), flush=True)
print('Actual lower bounds:', {name: record['lower'] for name, record in c['uniform'].items()},
      'required:', result['required'], 'full certificate:', OUT, flush=True)
