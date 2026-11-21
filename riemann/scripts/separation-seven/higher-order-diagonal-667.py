#!/usr/bin/env python3
"""Fixed K=16,N=8,P=128 inclusion certificate; no residual Gram or sign.

Intervals have integer endpoints in units 2^-128. Only integer arithmetic
is used for the mathematical evaluator. Fractions are used for exact
Bernoulli generation, source-bound verification and report diagnostics.
The canonical proof specifies the scalar-operation overcount.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
from collections import Counter
import json
import numpy as np

B = Path(__file__).resolve().parent
P, K, N, TERMS = 128, 16, 8, 100
S = 1 << P
calls = Counter()
max_bits = 0
checks = []
pins = {}


def observe(*values):
    global max_bits
    max_bits = max(max_bits, *(abs(v).bit_length() for v in values))


def ck(name, value):
    checks.append({'name': name, 'pass': bool(value)})


class I:
    def __init__(self, lo, hi):
        assert lo <= hi
        self.lo, self.hi = lo, hi
        observe(lo, hi)

    @staticmethod
    def rat(a, b=1):
        calls['rational_conversion'] += 1
        assert b > 0
        t = a*S
        observe(a, b, t)
        return I(t//b, -((-t)//b))

    def __add__(self, v):
        calls['addition'] += 1
        return I(self.lo+v.lo, self.hi+v.hi)

    def __neg__(self):
        calls['negation'] += 1
        return I(-self.hi, -self.lo)

    def __sub__(self, v):
        calls['subtraction'] += 1
        return I(self.lo-v.hi, self.hi-v.lo)

    def __mul__(self, v):
        calls['multiplication'] += 1
        t = [self.lo*v.lo, self.lo*v.hi, self.hi*v.lo, self.hi*v.hi]
        observe(*t)
        return I(min(t)//S, -((-max(t))//S))

    def __truediv__(self, v):
        calls['division'] += 1
        assert v.lo > 0 or v.hi < 0
        # General signed quotient: denominators can have either fixed sign.
        lows, highs = [], []
        for a in (self.lo, self.hi):
            for b in (v.lo, v.hi):
                t = a*S
                observe(t, b)
                lows.append(t//b)
                highs.append(-((-t)//b))
        return I(min(lows), max(highs))

    def widen(self, error):
        calls['widening'] += 1
        u = -((-error.numerator*S)//error.denominator)
        observe(error.numerator*S, error.denominator, u)
        return I(self.lo-u, self.hi+u)

    def numerical_radius(self):
        # Error about the midpoint rounded DOWN to the same128-bit grid.
        return Q((self.hi-self.lo+1)//2, S)


one, two, zero = I.rat(1), I.rat(2), I.rat(0)
odd_inverse = [I.rat(1, 2*j+1) for j in range(TERMS)]


def atanh_poly(t):
    t2 = t*t
    v = odd_inverse[-1]
    for j in range(TERMS-2, -1, -1):
        v = v*t2+odd_inverse[j]
    return two*t*v


def atan_inv(d):
    x = I.rat(1, d)
    minus_x2 = -(x*x)
    v = odd_inverse[-1]
    for j in range(TERMS-2, -1, -1):
        v = v*minus_x2+odd_inverse[j]
    # Absolute alternating-series remainder, valid at the exact 1/d.
    return (x*v).widen(Q(1, (2*TERMS+1)*d**(2*TERMS+1)))


pi = I.rat(16)*atan_inv(5)-I.rat(4)*atan_inv(239)
log2 = atanh_poly(I.rat(1, 3)).widen(Q(1, 2**190))
log3 = atanh_poly(I.rat(1, 2)).widen(Q(1, 2**190))
ell = log3/two
ck('ell in (1/2,3/5), pi in (3,4)',
   ell.lo > S//2 and ell.hi*5 < 3*S and pi.lo > 3*S and pi.hi < 4*S)


def log_interval(x):
    assert x.lo > 0
    y, exponent = x, 0
    # All calls here have x>=1. Range is verified, not presumed.
    while y.hi > 2*S:
        calls['range_reduction_iteration'] += 1
        y = y/two
        exponent += 1
    assert y.lo*2 >= S and y.hi <= 2*S
    t = (y-one)/(y+one)
    assert max(abs(t.lo), abs(t.hi))*3 <= S+3
    # Exact reduced input lies in [1/2,2]; hence |t_exact|<=1/3.
    return atanh_poly(t).widen(Q(1, 2**190))+I.rat(exponent)*log2


logpi = log_interval(pi)
# Rational Bernoulli generation, not a special-function routine.
# sum_{j=0}^m binom(m+1,j) B_j = 0 for m>=1.
bernoulli_work = 0


def reduced(num, den):
    global bernoulli_work
    # Explicit Euclid: each pass has <=8 scalar ops including control.
    bernoulli_work += 64
    observe(num, den)
    a, b = abs(num), den
    while b:
        a, b = b, a % b
        bernoulli_work += 8
    return num//a, den//a


bernoulli_pairs = [(1, 1)]
for m in range(1, 2*N+1):
    c, acc = 1, (0, 1)
    for j in range(m):
        u, v = bernoulli_pairs[j]
        acc = reduced(acc[0]*v+c*u*acc[1], acc[1]*v)
        c = c*(m+1-j)//(j+1)
        bernoulli_work += 64  # uncounted integer ops, indices, cache/control
        observe(c)
    bernoulli_pairs.append(reduced(-acc[0], acc[1]*(m+1)))
bernoulli = [Q(a, b) for a, b in bernoulli_pairs]  # report/checker only
ck('B16 convention and value', bernoulli[16] == Q(-3617, 510))
coeff = []
for j in range(1, N):
    a, b = bernoulli_pairs[2*j]
    a, b = reduced(a, b*(2*j))
    coeff.append(I.rat(a, b))
# Re(w)>0 gives sec(arg(w)/2)<sqrt(2); 2^9>2^(17/2).
analytic = Q(2**9)*abs(bernoulli[16])/16/Q(65, 4)**16
ck('uniform exact-argument analytic remainder <=2^-45', analytic <= Q(1, 2**45))
ck('all elementary log tails below chosen 2^-190',
   Q(2, 201)*Q(1, 2)**201/(1-Q(1, 2)**2) < Q(1, 2**190))


def cmul(u, v):
    return (u[0]*v[0]-u[1]*v[1], u[0]*v[1]+u[1]*v[0])


diagonal, frequencies, modes = [], [], []
for n in range(256):
    k = I.rat(n)*pi/ell
    frequencies.append(k)
    y = k/two
    x = I.rat(4*K+1, 4)
    norm = x*x+y*y
    inv = (x/norm, -(y/norm))
    inv2 = cmul(inv, inv)
    power = inv2
    correction = zero
    for j in range(1, N):
        correction = correction+coeff[j-1]*power[0]
        if j < N-1:
            power = cmul(power, inv2)
    value = log_interval(norm)/two-inv[0]/two-correction
    for j in range(K):
        a = I.rat(4*j+1, 4)
        value = value-a/(a*a+y*y)
    value = value-logpi
    diagonal.append(value)
    ck(f'mode{n} nonanalytic error <=2^-47', value.numerical_radius() <= Q(1, 2**47))
    modes.append({'n': n, 'h_center_numerator_over_S': (value.lo+value.hi)//2,
                  'numerical_interval_endpoints_over_S': [value.lo, value.hi],
                  'nonanalytic_error': value.numerical_radius(),
                  'analytic_error_upper': analytic,
                  'total_error_upper': analytic+value.numerical_radius()})

# A finite integer bisection is charged for sqrt(2), used only by neutral Z.
lo, hi = S, 2*S
for _ in range(P+1):
    calls['sqrt_bisection_iteration'] += 1
    mid = (lo+hi)//2
    observe(mid*mid, 2*S*S)
    if mid*mid <= 2*S*S:
        lo = mid
    else:
        hi = mid
sqrt2 = I(lo, hi)
ck('sqrt2 dyadic enclosure <= one ulp', lo*lo <= 2*S*S <= hi*hi and hi-lo <= 1)
quarter = I.rat(1, 4)
ratios = []
for n in range(2, 256):
    p = n % 2
    r = (quarter+frequencies[p]*frequencies[p])/(quarter+frequencies[n]*frequencies[n])
    ratios.append((sqrt2*r) if p == 0 else r)
    ck(f'exact completion ratio{n} in (0,1)', 0 < ratios[-1].lo <= ratios[-1].hi < S)


def load_json(name):
    data = (B/name).read_bytes()
    pins[name] = sha256(data).hexdigest()
    return json.loads(data)


data654 = load_json('jump-log-h1-bounds-654.json')
audit655 = load_json('jump-log-h1-audit-655.json')
ck('655 pins complete654 and reports no failures',
   audit655['input_sha256']['jump-log-h1-bounds-654.json'] == pins['jump-log-h1-bounds-654.json']
   and audit655['failures'] == [])
archive = B/'frozen-reference-proposal-652.npz'
pins[archive.name] = sha256(archive.read_bytes()).hexdigest()
ck('unchanged pinned652', pins[archive.name] ==
   '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
with np.load(archive, allow_pickle=False) as a:
    raw = a['free_middle_dyadics'].copy()
ck('all762 exact dyadics agree with audited654', raw.shape == (254, 3) and
   all(Q(*float(raw[n, j]).as_integer_ratio()) ==
       Q(int(data654['exact_free_middle_columns'][j][n]['numerator']),
         int(data654['exact_free_middle_columns'][j][n]['denominator']))
       for j in range(3) for n in range(254)))
dq_columns = []
analytic_interval = I.rat(analytic.numerator, analytic.denominator)
for col in range(3):
    completed = [zero, zero]
    free = []
    for n in range(2, 256):
        a, b = float(raw[n-2, col]).as_integer_ratio()
        v = I.rat(a, b)
        ck(f'exact free dyadic{n}column{col} representable at128', v.lo*b == a*S == v.hi*b)
        free.append(v)
        p = n % 2
        completed[p] = completed[p]-ratios[n-2]*v
    completed += free
    numerical = [diagonal[n]*completed[n] for n in range(256)]
    # Each numeric interval includes all errors OTHER than analytic digamma R.
    total_radii = []
    for n, v in enumerate(numerical):
        calls['Dq_error_radius_assembly'] += 1
        amplitude = I(0, max(abs(completed[n].lo), abs(completed[n].hi)))
        radius = ((v.hi-v.lo+1)//2)+(analytic_interval*amplitude).hi
        total_radii.append(Q(radius, S))  # exact output dyadic, report only
    dq_columns.append({'column': col,
        'completed_q_intervals_over_S': [[v.lo, v.hi] for v in completed],
        'Dq_numeric_intervals_over_S': [[v.lo, v.hi] for v in numerical],
        'Dq_centers_over_S': [(v.lo+v.hi)//2 for v in numerical],
        'Dq_total_error_radii': total_radii})

max_error = max(v.numerical_radius() for v in diagonal)
interval_calls = sum(calls.values())
# Each interval call, including its loop/index/cache overhead, expands to
# <=64 allowed real/integer operations/assignments at this fixed precision.
# Additional reserve below covers input/output/precision setup and control;
# scalar neutral completion and Dq assembly are already counted above.
setup_reserve = {'literal_constants_and_exact_tail_construction': 20000,
                 'all762_input_dyadic_decodes_and_copies': 100000,
                 'cache_writes_and_output_centers': 100000,
                 'unabsorbed_loop_index_branch_and_precision_management': 100000,
                 'additional_conservative_padding': 680000}
work = 64*interval_calls+bernoulli_work+1000000
ck('complete setup work <=10000000', work <= 10000000)
ck('evaluator operand/register cap <=16384bits', max_bits <= 16384)
report = {'result': 'CERTIFIED' if all(c['pass'] for c in checks) else 'FAILED',
    'design': {'K': K, 'first_omitted_Bernoulli_index': N, 'fractional_bits': P,
               'elementary_series_terms': TERMS},
    'analytic': {'uniform_bound': analytic, 'required_bound': Q(1, 2**45),
                 'exact_Bernoulli_numbers_B0_to_B16': bernoulli},
    'arithmetic': {'max_nonanalytic_error': max_error, 'required_bound': Q(1, 2**47),
                   'pi_interval_over_S': [pi.lo, pi.hi],
                   'ell_interval_over_S': [ell.lo, ell.hi],
                   'logpi_interval_over_S': [logpi.lo, logpi.hi],
                   'sqrt2_interval_over_S': [sqrt2.lo, sqrt2.hi]},
    'work': {'interval_calls_by_kind': dict(calls), 'interval_calls': interval_calls,
             'per_call_upper_bound': 64, 'Bernoulli_generation_upper': bernoulli_work,
             'additional_setup_reserve': 1000000, 'complete_setup_upper': work,
             'additional_setup_reserve_breakdown': setup_reserve,
             'required_upper': 10000000, 'observed_max_register_bits': max_bits,
             'register_cap_bits': 16384},
    'modes': modes, 'Dq_columns': dq_columns,
    'checks': checks, 'failures': [c['name'] for c in checks if not c['pass']],
    'input_sha256': pins, 'script_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
    'not_certified': ['residual Gram', 'quadrature work', 'inverse debt size',
                      'signed S3', 'original source/core/c_* contracts', 'RH']}


def encode(x):
    if isinstance(x, Q):
        return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    if isinstance(x, list):
        return [encode(v) for v in x]
    return x


out = B/'higher-order-diagonal-667.json'
out.write_text(json.dumps(encode(report), indent=2)+'\n')
print(f"result={report['result']} checks={len(checks)} failures={report['failures']}")
print(f'analytic <= {float(analytic):.8g}, required <= {2**-45:.8g}')
print(f'other error <= {float(max_error):.8g}, required <= {2**-47:.8g}')
print(f'complete setup <= {work}, required <= 10000000; max register={max_bits}bits')
print(out.relative_to(B.parent.parent))
if report['failures']:
    raise SystemExit(1)
