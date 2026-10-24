"""Isolated step-449 n=26 producer. All intervals encode endpoints / 2**256."""
import hashlib
import json
from fractions import Fraction
from math import isqrt

D = 1 << 256
COUNTS = {}


def count(key, amount=1):
    COUNTS[key] = COUNTS.get(key, 0) + amount


def digest(value):
    return hashlib.sha256(json.dumps(value, separators=(',', ':')).encode()).hexdigest()


def frac(value):
    return [value.numerator, value.denominator]


def cv(n, d=1):
    count('convert')
    assert d > 0
    return (n * D // d, -((-n * D) // d))


def add(x, y):
    count('add')
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    count('negate')
    return (-x[1], -x[0])


def mul(x, y):
    count('multiply')
    p = (x[0]*y[0], x[0]*y[1], x[1]*y[0], x[1]*y[1])
    return (min(p) // D, -((-max(p)) // D))


def div(x, k):
    count('divide')
    assert k > 0
    return (x[0] // k, -((-x[1]) // k))


def clip(x, lo, hi):
    count('clip')
    ans = (max(x[0], lo), min(x[1], hi))
    assert ans[0] <= ans[1]
    return ans


def logarithm(n, d):
    z = clip(cv(n, d), 0, D//2)
    t = clip(mul(z, z), 0, D//4)
    w = z
    total = (0, 0)
    trace = []
    for r in range(128):
        term = div(w, 2*r+1)
        total = add(total, term)
        trace.append([w, term, total])
        if r != 127:
            w = mul(w, t)
    out = (2*total[0]-1, 2*total[1]+1)
    count('scale')
    count('enlarge')
    return out, digest([z, t, trace, out])


def exponential(n, d):
    w = clip(cv(n, d), 0, D//8)
    v = (D, D)
    total = v
    trace = [[v, total]]
    for r in range(1, 128):
        v = div(mul(neg(w), v), r)
        total = add(total, v)
        trace.append([v, total])
    enlarged = clip((total[0]-1, total[1]+1), 0, D)
    count('enlarge')
    squares = []
    out = enlarged
    for _ in range(16):
        out = clip(mul(out, out), 0, D)
        squares.append(out)
    return out, digest([w, trace, enlarged, squares])


def convolution(left, right):
    out = [(0, 0) for _ in range(len(left)+len(right)-1)]
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            out[i+j] = add(out[i+j], mul(x, y))
            count('coefficient_pairs')
    return out


def parameter():
    arcs = []
    for m in (5, 239):
        terms = [Fraction((-1)**r, (2*r+1)*m**(2*r+1)) for r in range(25)]
        s24 = sum(terms[:24], Fraction())
        s25 = s24 + terms[24]
        assert s24 < s25
        arcs.append({'m': m, 'terms': list(map(frac, terms)),
                     'bounds': [frac(s24), frac(s25)]})
    bounds = [[Fraction(*v) for v in a['bounds']] for a in arcs]
    pl = 16*bounds[0][0] - 4*bounds[1][1]
    pu = 16*bounds[0][1] - 4*bounds[1][0]
    pi_grid = (cv(pl.numerator, pl.denominator)[0], cv(pu.numerator, pu.denominator)[1])
    root_l = isqrt(389*D*D)
    root_u = root_l + (root_l*root_l != 389*D*D)
    assert root_l**2 <= 389*D*D <= root_u**2
    cl = (2*pi_grid[0]*D) // root_u
    cu = -((-2*pi_grid[1]*D) // root_l)
    midpoint = Fraction(cl+cu, 2*D)
    delta = Fraction(cu-cl, 2*D)
    assert Fraction(3, 10) <= Fraction(cl, D) <= Fraction(cu, D) <= Fraction(1, 2)
    assert delta <= Fraction(1, 1 << 50)
    return {'arctangents': arcs, 'pi_exact': [frac(pl), frac(pu)],
            'pi_grid': pi_grid, 'sqrt_grid': [root_l, root_u],
            'sqrt_target': 389*D*D, 'sqrt_squares': [root_l**2, root_u**2],
            'c_grid': [cl, cu], 'midpoint': frac(midpoint), 'delta': frac(delta)}


def run(parameter_record, emit_panel, progress):
    u, v = parameter_record['midpoint']
    log2, log2_hash = logarithm(1, 3)
    total = (0, 0)
    for index in range(1016):
        a8 = index+8
        k = 0
        while a8 >= 16*(1 << k):
            k += 1
        assert 0 <= k <= 6
        lb, lb_hash = logarithm(a8-8*(1 << k), a8+8*(1 << k))
        la = clip((k*log2[0]+lb[0], k*log2[1]+lb[1]), 0, 7*D)
        count('scale')
        count('add')
        assert 0 < 26*u*a8 < v*8*(1 << 16)//8
        scalar, scalar_hash = exponential(26*u*a8, v*8*(1 << 16))
        assert 0 < 26*u <= 64*v
        beta = clip(cv(26*u, 8*v), 0, 8*D)
        rho = clip(cv(1, a8), 0, D//8)
        inva = clip(cv(8, a8), 0, D)
        e = [(D, D)]
        for r in range(1, 129):
            e.append(div(mul(neg(beta), e[-1]), r))
        recip = [inva]
        for _ in range(64):
            recip.append(mul(neg(rho), recip[-1]))
        h = [la]
        power = (D, D)
        for r in range(1, 65):
            power = mul(power, rho)
            term = div(power, r)
            h.append(term if r % 2 else neg(term))
        q = convolution(e, recip)
        p = convolution(q, h)
        integrated = (0, 0)
        divisions = []
        for r in range(257):
            term = div(p[r], r+1)
            integrated = add(integrated, term)
            divisions.append(term)
        panel = div(mul(scalar, integrated), 8)
        total = add(total, panel)
        record = {'n': 26, 'index': index, 'endpoints': [[a8, 8], [a8+1, 8]], 'k': k,
                  'log': la, 'exp': scalar, 'integrated_polynomial': integrated,
                  'panel_integral': panel, 'running_sum': total,
                  'digests': {'log2': log2_hash, 'logb': lb_hash, 'exp': scalar_hash,
                              'E': digest(e), 'R': digest(recip), 'H': digest(h),
                              'Q': digest(q), 'P': digest(p), 'integration': digest(divisions)}}
        emit_panel(record)
        if index % 64 == 0:
            progress('production', index+1)
    enlargement = 1 << 72
    final = [total[0]-enlargement, total[1]+enlargement]
    count('enlarge')
    radius = Fraction(final[1]-final[0], 2*D)
    assert final[0] <= final[1]
    assert radius < Fraction(1, 1 << 50)
    assert radius < Fraction(1, 1 << 183)
    assert COUNTS['coefficient_pairs'] == 1016*(8385+12545)
    return {'grid_denominator': D, 'polynomial_sum': total, 'final_grid': final,
            'midpoint': frac(Fraction(sum(final), 2*D)), 'radius': frac(radius),
            'required_radius': [1, 1 << 50], 'stronger_radius': [1, 1 << 183],
            'counts': COUNTS, 'complete_panels': 1016, 'n': 26}
