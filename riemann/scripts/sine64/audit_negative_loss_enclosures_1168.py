"""Independent tighter rational enclosures for ALL saved C750n cells.

No import from the generator and no floating elementary functions. This
uses a different grid, direct term recurrences (not Horner), monotone
endpoint logs, and exact rational square-root endpoint bounds. Analytic
justification, including Machin's real branch, is in canonical C750n.
"""
from fractions import Fraction as F
from math import factorial, isqrt
from pathlib import Path
import json

G = 10**70


def ceil_fraction(x):
    return -((-x.numerator)//x.denominator)


def box(lo, hi=None):
    lo, hi = F(lo), F(lo if hi is None else hi)
    return (lo.numerator*G//lo.denominator, ceil_fraction(hi*G))


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def neg(x):
    return (-x[1], -x[0])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    z = [a*b for a in x for b in y]
    return (min(z)//G, -((-max(z))//G))


def div(x, y):
    assert y[0]*y[1] > 0
    z = [F(a*G, b) for a in x for b in y]
    return (min(z).numerator//min(z).denominator, ceil_fraction(max(z)))


def times(x, q):
    return mul(x, box(q))


def sqrt_integer(n):
    a = isqrt(n*G*G)
    return (a, a+(a*a != n*G*G))


def atan_inverse(n, count):
    a = sum((F((-1)**j, (2*j+1)*n**(2*j+1)) for j in range(count)), F())
    e = F(1, (2*count+1)*n**(2*count+1))
    return box(a-e, a+e)


PI = sub(times(atan_inverse(5, 65), 16), times(atan_inverse(239, 20), 4))


def log_endpoint(x):
    """Monotone real log at one exact rational endpoint."""
    x = F(x)
    assert x > 0
    k = 0
    while x >= 2:
        x /= 2
        k += 1
    while x < 1:
        x *= 2
        k -= 1
    assert 1 <= x < 2
    q = box((x-1)/(x+1))
    q2 = mul(q, q)
    term, acc = q, box(0)
    for j in range(90):
        acc = add(acc, times(term, F(2, 2*j+1)))
        term = mul(term, q2)
    rem = F(2)*F(1, 3)**181/(181*(1-F(1, 9)))
    ans = add(acc, box(0, rem))
    return add(ans, times(LOG2, k)) if k else ans


# Separate endpoint computation for log2 avoids a recursive definition.
q = box(F(1, 3))
q2 = mul(q, q)
term, LOG2 = q, box(0)
for j in range(90):
    LOG2 = add(LOG2, times(term, F(2, 2*j+1)))
    term = mul(term, q2)
LOG2 = add(LOG2, box(0, F(2)*F(1, 3)**181/(181*(1-F(1, 9)))))


def log_box(x):
    return (log_endpoint(F(x[0], G))[0], log_endpoint(F(x[1], G))[1])


def trig(x, kind):
    if kind != 'sinc':
        # Any integer works; the independent domain assertion is essential.
        k = (x[0]+x[1])//(4*PI[0])
        x = sub(x, times(PI, 2*k))
    assert max(abs(v) for v in x) <= 7*G
    # This reduction can give [0,2pi], so use the larger domain |x|<=7.
    # 50 terms give substantially tighter bounds than the original |x|<=4.
    x2 = mul(x, x)
    term = x if kind == 'sin' else box(1)
    acc = term
    for j in range(1, 50):
        if kind in ('sin', 'sinc'):
            denom = (2*j)*(2*j+1)
        else:
            denom = (2*j-1)*(2*j)
        term = times(mul(term, x2), F(-1, denom))
        acc = add(acc, term)
    if kind == 'sin':
        rem = F(7**101, factorial(101))
    elif kind == 'cos':
        rem = F(7**100, factorial(100))
    else:
        rem = F(7**100, factorial(101))
    return add(acc, box(-rem, rem))


def record(x):
    return {'lo': str(x[0]), 'hi': str(x[1]), 'scale': str(G)}


def contained(x, old):
    s = int(old['scale'])
    return int(old['lo'])*G <= x[0]*s and x[1]*s <= int(old['hi'])*G


def main():
    root = Path(__file__).parent
    source = root/'negative-loss-witness-1166.json'
    saved = json.loads(source.read_text())
    checks = {}
    parameters = saved['parameters']
    L = log_box(box(101))
    b = times(L, F(1, 2))
    powers = {}
    for n in range(2, 101):
        # Independent smallest-divisor factorization of each integer.
        p = next((d for d in range(2, n+1) if n % d == 0))
        r = n
        while r % p == 0:
            r //= p
        if r == 1:
            powers[n] = p
    checks['exact_prime_power_list'] = [(r['n'], r['p']) for r in saved['prime_powers']] == list(powers.items())
    checks['35_terms'] = len(powers) == 35
    terms, term_records = [], []
    A, D = box(0), box(1)
    for old, (n, p) in zip(saved['prime_powers'], powers.items()):
        c = div(times(log_box(box(p)), 2), sqrt_integer(n))
        ell = log_box(box(n))
        ok = contained(c, old['c']) and contained(ell, old['log_n'])
        terms.append((c, ell))
        term_records.append({'n': n, 'p': p, 'c': record(c), 'log_n': record(ell), 'contained': ok})
        A, D = add(A, c), add(D, mul(c, ell))
    checks['all_coefficient_enclosures'] = all(r['contained'] for r in term_records)
    params = {'pi': PI, 'L': L, 'b': b, 'A': A, 'D': D, 'beta0': box(F(199999, 100000))}
    checks['all_parameter_enclosures'] = all(contained(v, parameters[k]) for k, v in params.items())
    checks['b_range'] = 2*G < b[0] <= b[1] < F(5, 2)*G
    checks['derivative_bound'] = D[1] < 109*G
    checks['machin_tangent_identity'] = (F(120,119)-F(1,239))/(1+F(120,119*239)) == 1
    checks['machin_angle_range'] = 4*F(5,26)-F(1,239) > 0 and F(4,5) < 1
    cells = []
    assert len(saved['cells']) == 2000
    for k, old in enumerate(saved['cells']):
        t = box(F(77)+F(2*k+1, 2000))
        p = box(0)
        for c, ell in terms:
            p = add(p, mul(c, trig(mul(t, ell), 'cos')))
        v = add(sub(sub(params['beta0'], log_box(div(t, times(PI, 2)))), div(box(2), mul(t, t))), p)
        u = sub(mul(b, t), times(PI, F(115, 2)))
        z = add(mul(b, t), times(PI, F(115, 2)))
        transform = add(trig(u, 'sinc'), div(trig(z, 'sin'), z))
        tests = {'consecutive_index': old['k'] == k,
                 'v_contained': contained(v, old['v']),
                 'G_contained': contained(transform, old['transform_scaled'])}
        cells.append({'k': k, 'v': record(v), 'G': record(transform), 'checks': tests})
    checks['all_2000_primitive_cells'] = all(all(r['checks'].values()) for r in cells)
    failures = [k for k, v in checks.items() if not v]
    out = {'scope': 'Independent transcendental interval containment; assembly verified separately1166.',
           'method': '10^-70 grid, 90-term monotone log, direct 50-term trig recurrence on [-7,7].',
           'parameters': {k: record(v) for k, v in params.items()},
           'terms': term_records, 'cells': cells, 'checks': checks, 'failures': failures,
           'actual_lower': saved['complete_lower_integral'],
           'required': 'norm < beta < 2; saved lower must exceed 27/10'}
    target = root/'negative-loss-enclosure-audit-1168.json'
    target.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Independent enclosure audit: {len(cells)} cells, {len(terms)} joint terms; failures={failures}')
    print('Actual saved lower: '+str(F(int(saved['complete_lower_integral']['lo']), int(saved['scale'])))+'; comparison >27/10; required norm <beta<2.')
    print('Full certificate: '+str(target.relative_to(Path.cwd())))
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
