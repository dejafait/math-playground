#!/usr/bin/env python3
"""Independent complete replay, using Fraction endpoint arithmetic.

Does not import certify.py. External theorem applicability is in L040;
this verifies the finite arithmetic evidence, not the source theorems.
"""
import json
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ceilq(x):
    return -((-x.numerator)//x.denominator)


def run(data):
    D = 1 << data['bits']
    assert data['scale'] == D
    T = data['T']
    assert T in (128, 256, 512)
    checks = []

    def exact(interval):
        assert len(interval) == 2 and all(type(t) is int for t in interval)
        assert interval[0] <= interval[1]
        return [F(t, D) for t in interval]

    def outer(lo, hi):
        assert lo <= hi
        return [(lo*D).__floor__(), ceilq(hi*D)]

    def endpoints(x, y, op):
        vals = [op(a, b) for a in exact(x) for b in exact(y)]
        return outer(min(vals), max(vals))

    def product(x, y):
        return endpoints(x, y, lambda a, b: a*b)

    def quotient(x, y):
        assert y[0] > 0
        return endpoints(x, y, lambda a, b: a/b)

    def times(x, t):
        v = sorted([a*t for a in exact(x)])
        return outer(*v)

    def root(x):
        assert x[0] >= 0
        lo, hi = isqrt(x[0]*D), isqrt(x[1]*D)
        if hi*hi != x[1]*D:
            hi += 1
        assert lo*lo <= x[0]*D < (lo+1)*(lo+1)
        assert (hi-1)*(hi-1) < x[1]*D <= hi*hi or hi == 0
        return [lo, hi]

    assert data['source_inputs'] == {
        'model': [0, -1, 1, -10, -20], 'N': 11, 'Delta': -11**5,
        'optimal_table_label': '11a1', 'torsion_order': 5, 'components': 1,
        'Manin_constant': 1, 'twist': 5, 'Pal_minimalization_factor': 1, 'B': 10}
    assert gcd(11**5, 5) == 1 and 5 % 4 == 1
    checks.append('exact instance and source specialization parameters')
    J = data['pi']['atan_terms']
    atan = []
    for inv in (5, 239):
        s = sum((F((-1)**k, (2*k+1)*inv**(2*k+1)) for k in range(J)), F(0))
        t = s+F((-1)**J, (2*J+1)*inv**(2*J+1))
        atan.append(sorted([s, t]))
    assert [[str(x) for x in ab] for ab in atan] == data['pi']['atan_brackets']
    pi = [16*atan[0][0]-4*atan[1][1], 16*atan[0][1]-4*atan[1][0]]
    assert [str(t) for t in pi] == data['pi']['exact_bracket']
    assert data['pi']['interval'] == outer(*pi)
    t2 = 2*F(1, 5)/(1-F(1, 25))
    t4 = 2*t2/(1-t2*t2)
    assert (t4-F(1, 239))/(1+t4*F(1, 239)) == 1
    checks.append('Machin algebra and complete alternating pi bounds')
    assert root([11*D, 11*D]) == data['sqrt11']
    h = quotient(times(data['pi']['interval'], F(2)), times(data['sqrt11'], F(5)))
    assert h == data['h']
    K = data['exponential']['Taylor_degree']
    expends = []
    for x in exact(h):
        assert 0 < x < 1
        s = sum(((-x)**k/F(factorial(k))
                 for k in range(K+1)), F(0))
        t = s+(-x)**(K+1)/F(factorial(K+1))
        expends.append(sorted([s, t]))
    ex = [expends[1][0], expends[0][1]]
    assert [str(t) for t in ex] == data['exponential']['exact_bracket']
    r = data['exponential']['r']
    assert r == outer(*ex) and 0 < r[0] <= r[1] < D
    checks.append('sqrt11 and all exponential Taylor/rounding bounds')

    def prime(p):
        return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))

    counts = data['point_counts']
    assert [row['p'] for row in counts] == [p for p in range(2, T+1) if prime(p)]
    for row in counts+[data['nodal_count']]:
        p = row['p']
        # Deliberately independent exhaustive y-count instead of Euler's criterion.
        counts_x = [sum((y*y+y-x*x*x+x*x+10*x+20) % p == 0 for y in range(p))
                    for x in range(p)]
        if p == 2:
            pairs = [[x, y] for x in range(p) for y in range(p)
                     if (y*y+y-x*x*x+x*x+10*x+20) % p == 0]
            assert pairs == row['pairs']
        else:
            assert [n-1 for n in counts_x] == row['discriminant_characters']
        assert sum(counts_x) == row['affine']
        assert sum(counts_x)+1 == row['total']
        assert p-sum(counts_x) == row['a_p']
    assert data['nodal_count']['p'] == 11 and data['nodal_count']['a_p'] == 1
    assert data['epsilon_N'] == -1 and data['chi_minus_N'] == 1
    assert data['twist_root_number'] == 1
    checks.append('every prime point count and exact Fricke-sign branch')
    ap = {row['p']: row['a_p'] for row in counts}
    coeffs = [0, 1]
    factor_records = []
    for n in range(2, T+1):
        m, val, fs = n, 1, []
        for p in range(2, n+1):
            if not prime(p) or m % p:
                continue
            k = 0
            while m % p == 0:
                k += 1
                m //= p
            terms = [1, ap[p]]
            for _ in range(2, k+1):
                terms.append(ap[p]*terms[-1]-(0 if p == 11 else p)*terms[-2])
            fs.append([p, k, terms])
            val *= terms[-1]
        assert m == 1
        factor_records.append([n, fs])
        coeffs.append(val)
    assert coeffs == data['coefficients']
    assert factor_records == data['factorizations_and_prime_powers']
    assert all(abs(coeffs[n]) <= n for n in range(1, T+1))
    power, partial = [D, D], [0, 0]
    for n in range(1, T+1):
        power = product(power, r)
        assert power == data['series']['powers'][n-1]
        chi = (0, 1, -1, -1, 1)[n % 5]
        term = times(power, F(2*chi*coeffs[n], n))
        partial = [partial[0]+term[0], partial[1]+term[1]]
        assert partial == data['series']['partials'][n-1]
    assert len(data['series']['powers']) == len(data['series']['partials']) == T
    nxt = product(power, r)
    assert nxt == data['series']['next_power']
    tail = quotient(times(nxt, F(2)), [D-r[1], D-r[0]])[1]
    assert tail == data['series']['tail_upper']
    assert F(tail, D) >= 2*F(nxt[1], D)/(1-F(r[1], D))
    L = [partial[0]-tail, partial[1]+tail]
    assert L == data['series']['L_interval']
    checks.append('all Euler coefficients, signed finite sums and full geometric tail')

    def poly(x):
        return 4*x**3-4*x**2-40*x-79

    lo, hi = 4*D, 5*D
    assert poly(F(lo, D)) == -47 and poly(F(hi, D)) == 121
    for mid, sign in data['period']['root_bisections']:
        assert mid == (lo+hi)//2
        v = poly(F(mid, D))
        assert sign == (1 if v > 0 else -1 if v < 0 else 0)
        if sign == 0:
            lo = hi = mid
        elif poly(F(lo, D))*v < 0:
            hi = mid
        else:
            lo = mid
    assert [lo, hi] == data['period']['real_root'] and hi-lo <= 1
    assert lo == hi or poly(F(lo, D))*poly(F(hi, D)) < 0
    rr = [lo, hi]
    # Endpoint-Fraction replay of every Vieta/square-root operation.
    square = product(rr, rr)
    v3 = times(square, F(3))
    v2 = times(rr, F(2))
    vsq = times([v3[0]-v2[1]-41*D, v3[1]-v2[0]-41*D], F(1, 4))
    dr = times(rr, F(3))
    d = times([dr[0]-D, dr[1]-D], F(1, 2))
    assert vsq[0] > 0 and d[0] > 0
    dd = product(d, d)
    R = root([dd[0]+vsq[0], dd[1]+vsq[1]])
    assert vsq == data['period']['v_squared']
    assert d == data['period']['d'] and R == data['period']['R']
    A, G = root(R), root(times([R[0]+d[0], R[1]+d[1]], F(1, 2)))
    assert data['period']['agm_steps'][0] == [A, G]
    for step in data['period']['agm_steps'][1:]:
        avg = outer((F(A[0], D)+F(G[0], D))/2,
                    (F(A[1], D)+F(G[1], D))/2)
        geo = root(product(A, G))
        A, G = avg, geo
        assert step == [A, G]
    assert len(data['period']['agm_steps']) == 13
    agm = [min(A[0], G[0]), max(A[1], G[1])]
    assert agm == data['period']['agm_bracket'] and agm[0] > 0
    omega = quotient(data['pi']['interval'], agm)
    total = omega[:]
    twist = quotient(total, root([5*D, 5*D]))
    assert omega == data['period']['omega_plus']
    assert total == data['period']['omega_total']
    assert twist == data['period']['omega_twist']
    checks.append('complete root bisections, finite AGM bracket and total-period factors')
    ratio = quotient(L, twist)
    iso = data['isolation']
    assert ratio == iso['ratio']
    width = F(ratio[1]-ratio[0], D)
    assert str(width) == iso['width'] and iso['required_width'] == '1/100'
    choices, ranges = set(), []
    for b in range(1, 11):
        lo, hi = ceilq(F(b*ratio[0], D)), (b*ratio[1])//D
        ranges.append([b, lo, hi])
        for a in range(lo, hi+1):
            if gcd(a, b) == 1:
                choices.add(F(a, b))
    assert ranges == iso['denominator_ranges']
    assert [str(t) for t in sorted(choices)] == iso['candidates']
    isolated = len(choices) == 1 and width < F(1, 100)
    assert isolated == iso['isolated']
    assert data['failures'] == ([] if isolated else ['rational isolation not certified'])
    checks.append('exhaustive denominator<=10 existence and uniqueness test')
    return {'bits': data['bits'], 'T': T, 'checks': checks,
            'ratio': ratio, 'width': str(width), 'required_width': '1/100',
            'isolated': isolated, 'q': str(next(iter(choices))) if isolated else None,
            'failures': data['failures']}


def main():
    path = HERE/'certificate.json'
    cert = json.loads(path.read_text())
    assert 1 <= len(cert['attempts']) <= 3
    schedule = [(48, 128), (64, 256), (96, 512)]
    for i, attempt in enumerate(cert['attempts']):
        assert (attempt['bits'], attempt['T']) == schedule[i]
    reports = [run(attempt) for attempt in cert['attempts']]
    assert cert['selected_attempt'] == len(reports)-1
    assert all(not r['isolated'] for r in reports[:-1])
    report = {'certificate_sha256': sha256(path.read_bytes()).hexdigest(),
              'reports': reports, 'finite_arithmetic_verified': True,
              'external_theorems_verified_by_script': False}
    out = HERE/'verification.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    for r in reports:
        print(f"verified {len(r['checks'])} full checks: q={r['q']} width={r['width']} "
              f"required<1/100 failures={r['failures']}")
    print('verification:', out.relative_to(HERE.parents[2]))


if __name__ == '__main__':
    main()
