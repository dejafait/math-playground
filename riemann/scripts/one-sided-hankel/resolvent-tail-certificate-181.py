"""Exact finite certificate for the limiting logarithmic derivative in L716.

The analytic proof, including the moment formula, mesh/remainder bounds
and eventual passage to finite n, is in the canonical lemma. No floating
point value participates in a check. Full rows and rational coefficients
are saved, not just sampled maxima.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

S = 1 << 120
K = 80
U, p, q = F(121, 64), F(3, 10), F(2, 5)
alpha, A = F(11, 8), F(27, 10)
J0 = 1/(2*U)

def ceildiv(a, b):
    return -((-a)//b)

def fixed(x):
    x = F(x)
    return (x.numerator*S//x.denominator,
            ceildiv(x.numerator*S, x.denominator))

def add(a, b):
    return a[0]+b[0], a[1]+b[1]

def neg(a):
    return -a[1], -a[0]

def mul(a, b):
    corners = [x*y for x in a for y in b]
    return min(corners)//S, ceildiv(max(corners), S)

def cmul(a, b):
    return (add(mul(a[0], b[0]), neg(mul(a[1], b[1]))),
            add(mul(a[0], b[1]), mul(a[1], b[0])))

def exp_minus(x):
    assert 0 <= x <= 1
    # Decreasing alternating series: odd truncation below, even above.
    even = sum(((-x)**j/F(factorial(j)) for j in range(41)), F(0))
    odd = even+(-x)**41/F(factorial(41))
    return fixed(odd)[0], fixed(even)[1]

def trig(x):
    assert 0 <= x <= 1
    cs = sum(((-1)**j*x**(2*j)/F(factorial(2*j)) for j in range(21)), F(0))
    sn = sum(((-1)**j*x**(2*j+1)/F(factorial(2*j+1)) for j in range(21)), F(0))
    return ((fixed(cs-x**42/F(factorial(42)))[0], fixed(cs)[1]),
            (fixed(sn-x**43/F(factorial(43)))[0], fixed(sn)[1]))

def log_interval(x):
    assert x >= 1
    r = (x-1)/(x+1)
    partial = 2*sum((r**(2*j+1)/F(2*j+1) for j in range(12)), F(0))
    remainder = 2*r**25/(25*(1-r*r))
    return partial, partial+remainder

def enc(x):
    x = F(x)
    return {'numerator': x.numerator, 'denominator': x.denominator,
            'decimal_preview': float(x)}

def interval(a):
    return [enc(F(a[0], S)), enc(F(a[1], S))]

checks = {}
def check(name, actual, relation, required):
    actual, required = F(actual), F(required)
    passed = {'<': actual < required, '>': actual > required,
              '<=': actual <= required, '>=': actual >= required}[relation]
    checks[name] = {'actual': enc(actual), 'relation': relation,
                    'required': enc(required), 'passed': passed}

E0 = exp_minus(J0)
power = fixed(1)
moments = []
moment_rows = []
for k in range(1, K+1):
    # exp(sum_(l>=1) e_l*w^l), by the exact derivative recurrence.
    e = [F(0)]+[F(k*(-1)**(l+1), l+2)/U**(l+1) for l in range(1, k)]
    h = [F(1)]
    for m in range(1, k):
        h.append(sum((l*e[l]*h[m-l] for l in range(1, m+1)), F(0))/m)
    c = sum((comb(k, k-1-m)*h[m] for m in range(k)), F(0))/k
    power = mul(power, E0)
    moment = mul(fixed(c), power)
    moments.append(moment)
    moment_rows.append({'k': k, 'rational_coefficient': enc(c),
                        'moment_enclosure': interval(moment)})

check('moment_lower', min(F(m[0], S) for m in moments), '>', 0)
check('moment_upper', max(F(m[1], S) for m in moments), '<', 1)

log1, log2 = log_interval(F(9, 5)), log_interval(F(201, 121))
omega = [A*(log1[j]-F(4, 5)+F(121, 100)*log2[j]) for j in (0, 1)]
check('whole_bump_x_above_two_fifths', (omega[0]-F(1, 3000))/A, '>', F(2, 5))
check('whole_bump_x_below_six_fifths', (omega[1]+F(1, 3000))/A, '<', F(6, 5))
check('compact_radius', F(exp_minus(p*F(2, 5))[1], S), '<', F(9, 10))
check('large_x_radius', F(exp_minus(p*F(6, 5))[1], S), '<', F(7, 10))

tail = 5*F(9, 10)**(K+1)
lipschitz = F(45, 2)
mesh_error = lipschitz/F(1000)  # Mesh spacing 1/500, nearest distance 1/1000.
rows = []
for j in range(401):
    x = F(2, 5)+F(j, 500)
    radius = exp_minus(p*x)
    cosine, sine = trig(q*x)
    z = mul(radius, cosine), neg(mul(radius, sine))
    zk = fixed(1), fixed(0)
    total = fixed(0)
    for moment in moments:
        zk = cmul(zk, z)
        real_uzk = add(mul(fixed(p), zk[0]), neg(mul(fixed(q), zk[1])))
        total = add(total, mul(moment, real_uzk))
    upper = F(total[1], S)+tail+mesh_error
    rows.append({'x': enc(x), 'partial_sum': interval(total),
                 'upper_in_nearest_cell': enc(upper)})

worst = max(rows, key=lambda row: F(row['upper_in_nearest_cell']['numerator'],
                                  row['upper_in_nearest_cell']['denominator']))
upper = F(worst['upper_in_nearest_cell']['numerator'],
          worst['upper_in_nearest_cell']['denominator'])
check('entire_compact_G_upper', upper, '<', F(4, 3))
check('large_x_G_upper', F(7, 6), '<', F(4, 3))
check('eventual_integrable_margin', alpha-F(65, 48), '>=', F(1, 48))

path = Path(__file__).with_suffix('.json')
result = {'purpose': __doc__, 'arithmetic': 'Exact rational and outward fixed-point intervals',
          'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'parameters': {'scale': S, 'moment_cutoff': K, 'grid_points': len(rows),
                         'grid_spacing': enc(F(1, 500)), 'omega_enclosure': [enc(x) for x in omega]},
          'analytic_bounds': {'series_tail': enc(tail), 'G_lipschitz': enc(lipschitz),
                              'nearest_grid_error': enc(mesh_error)},
          'moment_rows': moment_rows, 'grid_rows': rows, 'worst_cell': worst,
          'checks': checks, 'failures': [name for name, row in checks.items() if not row['passed']],
          'qualifications': ['Analytic argument and exact moment identity are in L716',
                             'Finite-n onset is existential, from audited L715',
                             'No signed bump integral or Xi positivity claim']}
path.write_text(json.dumps(result, indent=2)+'\n')
for name, row in checks.items():
    print(f"{name}: actual {row['actual']['decimal_preview']:.12g} "
          f"{row['relation']} required {row['required']['decimal_preview']:.12g}; pass={row['passed']}")
print(f"Failures: {result['failures']}; full certificate: {path}")
if result['failures']:
    raise SystemExit(1)
