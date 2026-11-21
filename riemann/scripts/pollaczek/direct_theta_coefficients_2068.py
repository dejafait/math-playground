#!/usr/bin/env python3
"""Bounded Romik (1.7)/(3.3) certificate; proof in C530a. No packages."""
import decimal
from decimal import Decimal as D
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import platform
import sys

PREC, X, N, PANELS = 60, 16, 4, 2**18
ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / 'direct-theta-coefficients-2068.json'
counts = dict(basic=0, exp=0, sqrt=0, sqrt_square_checks=0, nodes=0)
contexts = {}
for key, rounding in [('lo', decimal.ROUND_FLOOR),
                      ('hi', decimal.ROUND_CEILING),
                      ('near', decimal.ROUND_HALF_EVEN)]:
    c = decimal.Context(prec=PREC, rounding=rounding,
                        Emin=-999999, Emax=999999, capitals=1, clamp=0)
    for sig in c.traps:
        c.traps[sig] = sig not in (decimal.Inexact, decimal.Rounded)
    c.clear_flags()
    contexts[key] = c
lo, hi, near = (contexts[k] for k in ('lo', 'hi', 'near'))


def basic(c, name, x, y):
    counts['basic'] += 1
    return getattr(c, name)(x, y)


def point(n):
    return (D(n), D(n))


def frac(q):
    q = F(q)
    return (basic(lo, 'divide', D(q.numerator), D(q.denominator)),
            basic(hi, 'divide', D(q.numerator), D(q.denominator)))


def add(a, b):
    return (basic(lo, 'add', a[0], b[0]), basic(hi, 'add', a[1], b[1]))


def sub(a, b):
    return (basic(lo, 'subtract', a[0], b[1]),
            basic(hi, 'subtract', a[1], b[0]))


def mul(a, b):
    # Every use in this certificate has nonnegative factors.
    assert a[0] >= 0 and b[0] >= 0
    return (basic(lo, 'multiply', a[0], b[0]),
            basic(hi, 'multiply', a[1], b[1]))


def div(a, b):
    assert a[0] >= 0 and b[0] > 0
    return (basic(lo, 'divide', a[0], b[1]),
            basic(hi, 'divide', a[1], b[0]))


def exp_interval(a):
    # Decimal exp is correctly rounded HALF_EVEN, irrespective of mode.
    counts['exp'] += 2
    lower = near.exp(a[0])
    upper = near.exp(a[1])
    return (lo.next_minus(lower), hi.next_plus(upper))


def sqrt_point(a):
    assert a > 0
    counts['sqrt'] += 1
    q = near.sqrt(a)
    l, u = lo.next_minus(q), hi.next_plus(q)
    # Exact Python-integer square comparisons, independent of Decimal sqrt.
    ln, ld = l.as_integer_ratio()
    un, ud = u.as_integer_ratio()
    an, ad = a.as_integer_ratio()
    assert ln*ln*ad <= an*ld*ld
    assert un*un*ad >= an*ud*ud
    counts['sqrt_square_checks'] += 2
    return (l, u)


def atan_bounds(q, terms):
    s = sum(((-1)**r * F(1, (2*r+1)*q**(2*r+1))
             for r in range(terms)), F(0))
    t = F((-1)**terms, (2*terms+1)*q**(2*terms+1))
    return min(s, s+t), max(s, s+t)


def serial_interval(a):
    return dict(lower=str(a[0]), upper=str(a[1]))


def sf(q):
    return str(F(q))


# Machin's identity, with exact alternating rational remainders.
a5, a239 = atan_bounds(5, 80), atan_bounds(239, 25)
pi_rational = (16*a5[0]-4*a239[1], 16*a5[1]-4*a239[0])
assert F(3) < pi_rational[0] < pi_rational[1] < F(22, 7)
pi = (frac(pi_rational[0])[0], frac(pi_rational[1])[1])
assert sum((F(3)**r/F(factorial(r)) for r in range(9)), F(0)) > 20
sqrt2 = sqrt_point(D(2))
normalizer = mul(point(4), sqrt2)
assert normalizer[1] < 6
assert exp_interval(point(0))[0] <= 1 <= exp_interval(point(0))[1]
assert D(2) < exp_interval(point(1))[0] < exp_interval(point(1))[1] < D(3)

# Exact analytic error budgets, uniform on the complete [1,16].
G = []
for r in range(5):
    total = F(0)
    for n in range(1, N+1):
        A = F(22*n*n, 7)
        p = A**r*(2*A*A+3*A)
        if r >= 1:
            p += r*A**(r-1)*(4*A*A+3*A)
        if r >= 2:
            p += comb(r, 2)*A**(r-2)*4*A*A
        total += p/F(20)**(n*n)
    G.append(total)
V = [F(1, 2)]
for r in range(1, 5):
    V.append(V[-1]*F(2*r+1, 4))
tail_index = F(4000, 20**25)
tail_spatial = F(240, 20**16)*(F(X*X, 3)+F(2*X, 9)+F(2, 27))
threshold = F(1, 2**40)
assert X <= 64 and N <= 32 and PANELS <= 2**18 and PREC <= 100
assert PANELS % 2 == 0
budgets = []
for k in (0, 2, 4, 6):
    W = V[:]
    for _ in range(k):
        W = [sum((F(comb(r, s))*W[r-s]*F(factorial(s), 2**s)
                  for s in range(r+1)), F(0)) for r in range(5)]
    M = 6*sum((F(comb(4, r))*G[r]*W[4-r] for r in range(5)), F(0))
    error = F((X-1)**5, 180*PANELS**4)*M
    assert 2*error+tail_index+tail_spatial < threshold
    budgets.append((k, W, M, error))

print('Analytic bounds ready: X=16, N=4, panels=262144, digits=60.', flush=True)
sums = [point(0) for _ in range(4)]
rates = [mul(pi, point(n*n)) for n in range(1, N+1)]
# 1/2^18 = 5^18 * 10^-18, so all nodes are exactly represented.
mesh_unit = D(5**18).scaleb(-18)
assert F(mesh_unit) == F(1, PANELS)
for i in range(PANELS+1):
    x = basic(near, 'multiply', D(PANELS+15*i), mesh_unit)
    # This product has <=26 significant digits, hence is exact at PREC=60.
    assert F(x) == F(PANELS+15*i, PANELS)
    xp1 = basic(near, 'add', x, D(1))
    root = sqrt_point(xp1)
    u = div(point(basic(near, 'subtract', x, D(1))), point(xp1))
    u2 = mul(u, u)
    omega = point(0)
    for rate in rates:
        ax = mul(rate, point(x))
        p = sub(mul(point(2), mul(ax, ax)), mul(point(3), ax))
        assert p[0] > 0
        ex = exp_interval((ax[1].copy_negate(), ax[0].copy_negate()))
        omega = add(omega, mul(p, ex))
    f = div(mul(normalizer, omega), mul(point(xp1), root))
    weight = point(1 if i in (0, PANELS) else (4 if i % 2 else 2))
    for j in range(4):
        sums[j] = add(sums[j], mul(weight, f))
        if j != 3:
            f = mul(f, u2)
    counts['nodes'] += 1
    if i and i % 65536 == 0:
        print(f'Integrated {i}/{PANELS} panels.', flush=True)

rows = []
failures = []
for j, (k, W, M, error) in enumerate(budgets):
    Q = mul(frac(F(X-1, 3*PANELS)), sums[j])
    arithmetic_width = F(Q[1])-F(Q[0])
    # Missing theta and spatial tails are nonnegative; Simpson error is signed.
    lower = basic(lo, 'subtract', Q[0], frac(error)[1])
    upper = basic(hi, 'add', Q[1], frac(error+tail_index+tail_spatial)[1])
    width = F(upper)-F(lower)
    positive = D(0) < lower < upper and lower.is_finite() and upper.is_finite()
    passed = positive and width <= threshold
    if not passed:
        failures.append(f'c{k}: positivity/finite/width test failed')
    rows.append(dict(coefficient=f'c{k}', quadrature=serial_interval(Q),
                     arithmetic_and_constants_width=sf(arithmetic_width),
                     weight_derivative_bounds=list(map(sf, W)),
                     fourth_derivative_bound=sf(M), simpson_error=sf(error),
                     theta_index_error=sf(tail_index), spatial_error=sf(tail_spatial),
                     enclosure=serial_interval((lower, upper)),
                     width=sf(width), positive_finite=positive, passed=passed))
    print(f'c{k}: [{lower}, {upper}]', flush=True)
    print(f'  width={float(width):.9e}; required<={float(threshold):.9e}; pass={passed}', flush=True)

flags = {key: {sig.__name__: bool(value) for sig, value in ctx.flags.items()}
         for key, ctx in contexts.items()}
unexpected = [(key, name) for key, mapping in flags.items()
              for name, value in mapping.items()
              if value and name not in ('Inexact', 'Rounded')]
if unexpected:
    failures.append('Unexpected Decimal signals: '+str(unexpected))
certificate = dict(
    status='PASS' if not failures else 'FAIL', target='c0,c2,c4,c6 widths <= 2^-40',
    parameters=dict(X=X, N=N, panels=PANELS, digits=PREC),
    required_width=sf(threshold), coefficients=rows, failures=failures,
    analytic_common=dict(G=list(map(sf, G)), V=list(map(sf, V)),
                         theta_index_error=sf(tail_index), spatial_error=sf(tail_spatial)),
    constants=dict(pi=serial_interval(pi), pi_exact_machin_bounds=list(map(sf, pi_rational)),
                   atan_terms=dict(q5=80, q239=25), sqrt2=serial_interval(sqrt2)),
    runtime=dict(python=sys.version, implementation=platform.python_implementation(),
                 decimal_module=decimal.__file__, libmpdec=decimal.__libmpdec_version__,
                 contexts={key: str(ctx) for key, ctx in contexts.items()}, flags=flags,
                 counts=counts, unexpected_signals=unexpected,
                 trust_assumption='Correct CPython integer/Fraction and libmpdec basic operations and correctly-rounded exp; finite runtime checks are not a backend proof.'),
    source='Romik arXiv:1902.06330v3 (1.7)/(3.3); DLMF 3.5.6-8, 8.2.2/8.4.8/8.4.11',
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
OUTPUT.write_text(json.dumps(certificate, indent=2)+'\n')
print('Failures:', failures, flush=True)
print('Certificate:', OUTPUT, flush=True)
if failures:
    raise SystemExit(1)
