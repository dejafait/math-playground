"""Approved fixed 39-column test; exact arithmetic, no point search."""
from fractions import Fraction as Q
from pathlib import Path
from math import comb
from itertools import permutations
import hashlib
import json
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'eleven-adic-filter-certificate.json'
D = dict(completed=False, failures=[], bindings={}, checks=[], bounds=dict(
    field_coordinates=4, global_columns=39, branch_candidates=1,
    matrix_cap=39, valuation_cap=128, rational_bits_cap=4096,
    field_operations_cap=100000, field_operations=0, max_rational_bits=0,
    max_absolute_valuation=0))


def observe(a):
    if isinstance(a, (list, tuple)):
        for x in a:
            observe(x)
    elif isinstance(a, (int, Q)):
        q = Q(a)
        n = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
        D['bounds']['max_rational_bits'] = max(n, D['bounds']['max_rational_bits'])
        assert n <= 4096, 'rational bit cap'
    return a


def op(a):
    D['bounds']['field_operations'] += 1
    assert D['bounds']['field_operations'] <= 100000, 'field operation cap'
    return observe(a)


def need(name, value):
    D['checks'].append(dict(name=name, passed=bool(value)))
    assert value, name


def read(name, expected=None):
    raw = (ROOT/name).read_bytes()
    h = hashlib.sha256(raw).hexdigest()
    D['bindings'][name] = h
    if expected is not None:
        need('binding '+name, h == expected)
    return json.loads(raw)


def shift(p, t):
    return observe([sum(Q(p[j])*comb(j, i)*t**(j-i)
                        for j in range(i, len(p))) for i in range(len(p))])


def add(a, b):
    return op([a[i]+b[i] for i in range(4)])


def scale(a, t):
    return op([x*t for x in a])


def mul(a, b):
    z = [Q(0)]*7
    for i in range(4):
        for j in range(4):
            z[i+j] += a[i]*b[j]
            observe(z[i+j])
    for j in range(6, 3, -1):
        for i in range(4):
            z[j-4+i] -= z[j]*E[i]
            observe(z[j-4+i])
    return op(z[:4])


def power(a, n):
    r = [Q(1), Q(0), Q(0), Q(0)]
    for _ in range(n):
        r = mul(r, a)
    return r


def norm(a):
    cols = [mul(a, [Q(int(j == i)) for j in range(4)]) for i in range(4)]
    value = Q(0)
    for p in permutations(range(4)):
        t = Q((-1)**sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4)))
        for i in range(4):
            t *= cols[p[i]][i]
            observe(t)
        value += t
        observe(value)
    return value


def vq(x):
    x = Q(x)
    assert x
    a, b, n = x.numerator, x.denominator, 0
    while a % 11 == 0:
        a //= 11
        n += 1
    while b % 11 == 0:
        b //= 11
        n -= 1
    return n


def res(x):
    x = Q(x)
    assert x.denominator % 11
    return x.numerator % 11 * pow(x.denominator, -1, 11) % 11


def bit(t):
    assert t % 11
    return int(t % 11 not in (1, 3, 4, 5, 9))


def bound_v(n):
    D['bounds']['max_absolute_valuation'] = max(abs(n), D['bounds']['max_absolute_valuation'])
    assert abs(n) <= 128, 'valuation cap'


def rational_class(x):
    n = vq(x)
    bound_v(n)
    unit = observe(Q(x)/Q(11)**n)
    t = res(unit)
    return dict(value=Q(x), valuation=n, unit=unit, residue=t, bits=[n % 2, bit(t)])


def field_class(a):
    vals = [None if x == 0 else 4*vq(x)+i for i, x in enumerate(a)]
    n = min(x for x in vals if x is not None)
    bound_v(n)
    i = vals.index(n)
    k = vq(a[i])
    unit_residue = res(a[i]/Q(11)**k) * pow(10, k, 11) % 11
    normalized = mul(a, power(UINV if n >= 0 else U, abs(n)))
    need('normalized integral power coefficients', all(x == 0 or vq(x) >= 0 for x in normalized))
    need('normalized nonzero residue', res(normalized[0]) == unit_residue != 0)
    return dict(u_coefficients=a, term_valuations=vals, minimum_index=i,
                valuation=n, normalized=normalized, residue=unit_residue,
                bits=[n % 2, bit(unit_residue)])


def pair(a, q):
    f, r = field_class(a), rational_class(q)
    bits = r['bits']+f['bits']
    return dict(rational=r, quartic=f, bits=bits,
                mask=sum(b << i for i, b in enumerate(bits)))


def elimination(rows):
    pivots, kernel, trace = {}, [], []
    for j, row in enumerate(rows):
        value, coefficients, additions = row, 1 << j, []
        while value:
            p = value.bit_length()-1
            if p not in pivots:
                pivots[p] = (value, coefficients)
                break
            v, c = pivots[p]
            value ^= v
            coefficients ^= c
            additions.append(p)
        if not value:
            kernel.append(coefficients)
        trace.append(dict(input=row, additions=additions, reduced=value,
                          coefficients=coefficients))
    return dict(rank=len(pivots), pivots={str(k): list(v) for k, v in pivots.items()},
                kernel=kernel, trace=trace)


def main():
    global E, U, UINV
    real = read('real-kummer-certificate.json')
    audit = read('real-kummer-audit.json')
    need('accepted real audit binding', audit['completed'] and not audit['failures'] and
         audit['bindings']['real-kummer-certificate.json'] == D['bindings']['real-kummer-certificate.json'])
    originals = {name: read(name, h) for name, h in real['bindings'].items()}
    model = originals['odd-model-support-certificate.json']
    loc = originals['localized-parity-certificate.json']
    base = originals['quartic-class-certificate.json']
    need('accepted real certificate', real['completed'] and not real['failures'])
    need('exactly 39 witnesses', len(real['witnesses']) == 39)
    need('same complete support', real['S_indices'] == loc['selected_indices'])
    need('prime above 11', base['generators'][1]['p'] == 11 and base['generators'][1]['factor'] == [5, 1])
    g = list(map(Q, model['field']['alpha_polynomial']))
    observe(g)
    observe(real['G'])
    observe([[Q(x) for x in row] for row in real['basis']])
    need('actual g', g == list(map(Q, real['g'])) == [-109375, -32500, 150, 64, 1])
    need('actual G', real['G'] == model['model']['G'])
    E = shift(g, -5)
    D['field'] = dict(g=g, shifted=E, shift='u=alpha+5', prime=base['generators'][1])
    need('fixed Eisenstein gate', E == [49500, -29700, -660, 44, 1] and
         all(x.denominator == 1 and x % 11 == 0 for x in E[:4]) and E[0] % 121 != 0)
    need('rho = 11/u^4 residue', (-int(E[0]/11)) % 11 == 10 and pow(10, -1, 11) == 10)
    U = [Q(0), Q(1), Q(0), Q(0)]
    UINV = [Q(-E[i+1], E[0]) for i in range(4)]
    need('inverse uniformizer identity', mul(U, UINV) == [1, 0, 0, 0])
    eta = shift(model['field']['eta_in_alpha'], -5)
    need('eta transport', mul(eta, [-55, 1, 0, 0]) == [-907500, 0, 0, 0])
    H = list(map(Q, model['model']['H']))
    observe(H)
    h_eta = [Q(0)]*4
    for c in reversed(H):
        h_eta = add(mul(h_eta, eta), [c, 0, 0, 0])
    need('H(eta)=0', h_eta == [0, 0, 0, 0])
    product = [Q(0)]*6
    for i, x in enumerate(H):
        product[i] -= 9075*x
        product[i+1] += x
        observe(product)
    need('full local factor product', product == list(map(Q, real['G'])))
    terms = [observe(c*9075**i) for i, c in enumerate(H)]
    h_r = sum(terms)
    observe(h_r)
    need('distinct branch factors', h_r == 73990352390625 != 0)
    b = add([Q(9075), Q(0), Q(0), Q(0)], scale(eta, -1))
    need('branch norm', norm(b) == h_r)
    branch = pair(b, h_r)
    D['branch'] = dict(H=H, eta_u=eta, H_at_root=h_r, pair=branch,
                       infinity_mask=0, required_dimension=1)
    need('branch complete-image gate', branch['mask'] != 0)
    D['branch']['actual_dimension'] = 1
    D['local_factor_count'] = 2
    D['local_image_span'] = [0, branch['mask']]
    records = []
    for w in real['witnesses']:
        observe([Q(x) for x in w['power_coefficients']])
        observe([Q(w['signed_norm']), Q(w['inverse_norm'])])
        a = shift(w['power_coefficients'], -5)
        n = norm(a)
        need('signed norm '+w['id'], n == Q(w['signed_norm']) != 0 and Q(w['inverse_norm'])*n == 1)
        need('actual basis '+w['id'], [sum(Q(real['basis'][i][j])*w['coefficients'][j]
             for j in range(4)) for i in range(4)] == list(map(Q, w['power_coefficients'])))
        p = pair(a, Q(w['inverse_norm']))
        need('local norm bits '+w['id'], p['rational']['bits'] == [p['quartic']['bits'][0], 0])
        records.append(dict(id=w['id'], source=w, signed_norm=n, pair=p,
                            real_quotient=w['sign_bits'][0] | ((w['sign_bits'][1]^w['sign_bits'][2]) << 1)))
    D['witnesses'] = records
    need('same real image W', set(real['local_rows']) == {0, 24, 30})
    elim = elimination([r['real_quotient'] for r in records])
    D['real_kernel'] = elim
    D['bounds'].update(max_matrix_rows=39, max_matrix_columns=39,
                       coefficient_kernel_vectors=len(elim['kernel']))
    need('complete coefficient kernel', elim['rank'] == 2 and len(elim['kernel']) == 37)
    products = []
    for coefficients in elim['kernel']:
        a, q, signs, localmask, ids = [Q(1), Q(0), Q(0), Q(0)], Q(1), 0, 0, []
        for i, r in enumerate(records):
            if coefficients >> i & 1:
                a = mul(a, r['pair']['quartic']['u_coefficients'])
                q *= r['pair']['rational']['value']
                observe(q)
                signs ^= r['source']['mask']
                localmask ^= r['pair']['mask']
                ids.append(r['id'])
        n = norm(a)
        need('product signed inverse norm', n*q == 1)
        p = pair(a, q)
        need('multiplicative local bits', p['mask'] == localmask)
        need('real compatible product', signs in (0, 24, 30, 6))
        quotient = p['quartic']['bits'][1]
        need('exact local quotient membership', (p['mask'] in D['local_image_span']) == (quotient == 0))
        products.append(dict(coefficients=coefficients, ids=ids, signed_norm=n,
                             real_mask=signs, pair=p, local_quotient=quotient))
    D['products'] = products
    qe = elimination([r['local_quotient'] for r in products])
    D['quotient_elimination'] = qe
    need('positive extra quotient rank', qe['rank'] == 1)
    chosen = next(x for x in products if x['ids'] == ['rational-2'])
    need('explicit positive witness', chosen['real_mask'] == 0 and chosen['local_quotient'] == 1)
    D['obstruction'] = chosen
    D['result'] = dict(required_local_dimension=1, actual_local_dimension=1,
                       global_columns=39, real_coefficient_rank=2,
                       real_kernel_dimension=37, quotient_rank=1,
                       filtered_dimension_constant=8, rank_bound_constant=7,
                       c_upper_bound=2, unconditional_rank_upper_bound=9,
                       sufficient_rank_upper_bound=1, shortfall=8)
    D['completed'] = True


def encode(x):
    if isinstance(x, Q):
        return x.numerator if x.denominator == 1 else str(x)
    raise TypeError(type(x).__name__)


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        D['failures'].append(str(exc))
        D['traceback'] = traceback.format_exc()
    OUT.write_text(json.dumps(D, indent=2, default=encode)+'\n')
    print(json.dumps(dict(completed=D['completed'], result=D.get('result'),
                          bounds=D['bounds'], failures=D['failures'], certificate=str(OUT))))
    if not D['completed']:
        raise SystemExit(1)
