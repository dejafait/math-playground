#!/usr/bin/env python3
"""Independent L124 audit; imports no producer, replay or local implementation.

L118's isolating intervals and L122's audited finite square-class tables are
inputs. Exact rational arithmetic checks complete evidence, not previews.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path
import json

BASE = Path(__file__).parent
FILES = ['marked-octic-bounded-linear-certificate.json',
         'marked-octic-bounded-linear-replay.json',
         'marked-octic-two-adic-image-certificate.json']
C, R, L = [json.loads((BASE / p).read_text()) for p in FILES]
OUT = BASE / 'marked-octic-bounded-linear-audit-certificate.json'
F = list(map(Q, [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]))
E = [Q(x, 9150625) for x in [22130658, -74245842, 91279980, -48315300, 9150625]]
S = [2, 3, 5, 11]
checks = []


def clean(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, dict):
        return {str(k): clean(v) for k, v in x.items()}
    if isinstance(x, (tuple, list)):
        return [clean(v) for v in x]
    return x


def check(name, actual, required):
    a, b = clean(actual), clean(required)
    checks.append(dict(name=name, actual=a, required=b, passed=a == b))


def mul(a, b, f):
    n = len(f)-1
    z = [Q(0)]*(2*n-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            z[i+j] += x*y
    for k in range(2*n-2, n-1, -1):
        q = z[k]/f[-1]
        for i in range(n+1):
            z[k-n+i] -= q*f[i]
    return z[:n]


def matrix(a, f):
    n = len(f)-1
    cols = [mul(a, [Q(i == j) for i in range(n)], f) for j in range(n)]
    return [[cols[j][i] for j in range(n)] for i in range(n)]


def determinant(m):
    # Exterior-power subset expansion: independent of saved elimination.
    n, stages = len(m), [{0: Q(1)}]
    for i in range(n):
        nxt = {}
        for used, value in stages[-1].items():
            for j in range(n):
                if not (used >> j & 1) and m[i][j]:
                    key = used | (1 << j)
                    term = value*m[i][j]*(-1)**((used >> (j+1)).bit_count())
                    nxt[key] = nxt.get(key, Q(0))+term
        stages.append(nxt)
    return stages[-1].get((1 << n)-1, Q(0)), stages


def norm_evidence(a):
    m = matrix(a, F)
    value, stages = determinant(m)
    work, trace = [r[:] for r in m], []
    for j in range(8):
        k = next(k for k in range(j, 8) if work[k][j])
        work[j], work[k] = work[k], work[j]
        pivot = work[j][j]
        trace.append(dict(column=j, swapped_row=k, pivot=pivot))
        for k in range(j+1, 8):
            q = work[k][j]/pivot
            work[k] = [x-q*y for x, y in zip(work[k], work[j])]
    return dict(matrix=m, elimination=trace, norm=value), stages


def factor(x):
    assert x
    n, d, exponents = abs(x.numerator), x.denominator, {}
    for p in S:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        while d % p == 0:
            d //= p
            e -= 1
        exponents[p] = e
    square = x > 0 and isqrt(x.numerator)**2 == x.numerator and isqrt(x.denominator)**2 == x.denominator
    return dict(sign=1 if x > 0 else -1, exponents=exponents,
                numerator_remainder=n, denominator_remainder=d, square=square)


def ev(f, x):
    z = Q(0)
    for c in reversed(f):
        z = z*x+c
    return z


def vp(x):
    n, d = abs(x.numerator), x.denominator
    assert n
    return (n & -n).bit_length()-(d & -d).bit_length()


def val(a):
    return min(4*vp(x)+i for i, x in enumerate(a) if x)


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def scale(a, s):
    return [x*s for x in a]


def lm(a, b):
    return mul(a, b, E)


one = list(map(Q, [1, 0, 0, 0]))
pi = list(map(Q, [0, 1, 0, 0]))
ipi = [-E[i]/E[0] for i in range(1, 5)]


def inverse(a):
    m = [row+[Q(i == 0)] for i, row in enumerate(matrix(a, E))]
    for j in range(4):
        k = next(k for k in range(j, 4) if m[k][j])
        m[j], m[k] = m[k], m[j]
        m[j] = [x/m[j][j] for x in m[j]]
        for k in range(4):
            if k != j:
                q = m[k][j]
                m[k] = [x-q*y for x, y in zip(m[k], m[j])]
    return [r[-1] for r in m]


cosets = {tuple(r['residue']): r['label'] for r in L['residue_ring']['complete_unit_cosets']}
table = L['residue_ring']['unit_multiplication_table']
scalars = L['scalar_labels']


def label(a):
    w, z = val(a), a[:]
    for _ in range(abs(w)):
        z = lm(z, ipi if w >= 0 else pi)
    residue = [x.numerator*pow(x.denominator, -1, m) % m for x, m in zip(z, [8, 4, 4, 4])]
    return dict(valuation=w, normalized_residue=residue, label=32*(w % 2)+cosets[tuple(residue)])


def cm(a, b):
    return 32*((a//32) ^ (b//32))+table[a % 32][b % 32]


def orbit(pair):
    return sorted((cm(pair[0], s), cm(pair[1], s)) for s in scalars)


def canonical(bits):
    return bits ^ (255 if bits & 1 else 0)


check('complete prescribed input', C['input'], dict(F=list(map(int, F)), leading_coefficient_G=3025,
      support=S, bounds=dict(a_min=-16, a_max=16, b_min=1, b_max=16, gcd=1)))
check('local input hash', C['local_input'], dict(path=FILES[2], sha256=sha256((BASE/FILES[2]).read_bytes()).hexdigest()))
check('actual full local polynomial', L['input']['G'], [int(11*x) for x in F])
check('actual field and theta', [L['field']['monic_E'], L['field']['actual_theta_transports']], [E, ['alpha', '-alpha']])
check('uniformizer inverse', lm(pi, ipi), one)
integral_equation = [int(F[i]*275**(7-i)) for i in range(8)]+[1]
check('L123 monic equation', integral_equation, [28902481402587890625, 0, -5605329726562500, 0, 144122343750, 0, -786500, 0, 1])
r = list(map(Q, [468, -1126, Q(2585, 3), Q(-5500, 27)]))
check('exact r and identity', [r, lm(r, r)], [L['field']['r'], scale(add(pi, scale(one, -1)), 2)])
alpha, target, newton = add(one, scale(r, 2)), add(one, scale(r, 4)), []
for i in range(3):
    err = add(lm(alpha, alpha), scale(target, -1))
    newton.append(dict(approximation=alpha, residual_valuation=val(err), derivative_valuation=val(scale(alpha, 2))))
    if i < 2:
        alpha = add(alpha, scale(lm(err, inverse(scale(alpha, 2))), -1))
check('all Newton bounds', [[x['residual_valuation'], x['derivative_valuation']] for x in newton], [[12, 4], [16, 4], [24, 4]])
check('actual approximation and precision', [alpha, L['field']['alpha_error_lower_bound'], L['input']['strict_threshold']], [L['field']['alpha_approximation'], 20, 8])
check('alpha plus/minus one valuations', [val(add(alpha, scale(one, -1))), val(add(alpha, one))], [6, 4])
check('complete scalar labels', sorted(scalars), [0, 5, 8, 12, 15, 19, 22, 29])
real_image = {0, 252, 240, 192}
point_image = {(0, 0), (0, 5), (0, 8), (0, 22), (2, 6)}
check('real and dyadic point sets', [C['real_image_codes'], C['dyadic_point_image'], L['point_image']],
      [sorted(real_image), sorted(point_image), sorted(point_image)])

pairs = [(a, b) for a in range(-16, 17) for b in range(1, 17) if gcd(a, b) == 1]
check('exhaustive pair domain', [(x['a'], x['b']) for x in C['pair_decisions']], pairs)
check('replay exhaustive pair domain', [x['pair'] for x in R['norm_recomputations']], pairs)
norms, pair_records, eligible = {}, [], []
for i, (a, b) in enumerate(pairs):
    nr, stages = norm_evidence(list(map(Q, [a, -b]+[0]*6)))
    n, fac = nr['norm'], factor(nr['norm'])
    h = sum(int(c)*a**j*b**(8-j) for j, c in enumerate(F))
    allowed = fac['numerator_remainder'] == fac['denominator_remainder'] == 1
    nd = dict(homogeneous_F=h, norm=n, sign=fac['sign'], support_exponents=list(fac['exponents'].values()),
              numerator_remainder=fac['numerator_remainder'], denominator_remainder=fac['denominator_remainder'], eligible=allowed)
    check('full norm formula '+str(i), n, Q(h, 275))
    check('complete eligibility evidence '+str(i), C['pair_decisions'][i], dict(a=a, b=b, norm_data=nd))
    check('complete replay norm evidence '+str(i), R['norm_recomputations'][i],
          dict(pair=(a, b), multiplication_determinant=nr, factorization=fac, eligible=allowed))
    if allowed:
        eligible.append((a, b))
    norms[(a, b)] = nd
    pair_records.append(dict(pair=(a, b), norm_evidence=nr, determinant_stages=stages, norm_data=nd))
check('exact eligibility count and list', [len(pairs), eligible], [319, [(-3, 1), (-1, 1), (0, 1), (1, 1), (3, 1)]])
check('generator order', [x['pair'] for x in C['generators']], eligible)

intervals = [(Q(5, 2), Q(3)), (Q(3, 2), Q(2)), (Q(3, 4), Q(1)), (Q(1, 4), Q(1, 2)),
             (Q(-1, 2), Q(-1, 4)), (Q(-1), Q(-3, 4)), (Q(-2), Q(-3, 2)), (Q(-3), Q(-5, 2))]
root_records = [dict(index=i+1, initial_interval=(lo, hi), bisections=[], interval=(lo, hi),
                     F_endpoint_values=(ev(F, lo), ev(F, hi))) for i, (lo, hi) in enumerate(intervals)]
check('complete strict root evidence', C['roots'], root_records)
check('root exhaustion', all(ev(F, lo)*ev(F, hi) < 0 for lo, hi in intervals) and
      all(intervals[i+1][1] < intervals[i][0] for i in range(7)), True)
generators, local_generators = [], []
for i, (a, b) in enumerate(eligible):
    bits, signs = 0, []
    for j, (lo, hi) in enumerate(intervals):
        left, right = a-b*hi, a-b*lo
        assert left >= 0 or right <= 0
        negative = right <= 0
        bits |= int(negative) << j
        signs.append(dict(strict_value_interval=(left, right), negative=negative))
    components = [add(scale(one, a), scale(alpha, -b)), add(scale(one, a), scale(alpha, b))]
    evidence = []
    for x in components:
        row = label(x)
        row.update(approximation=x, absolute_error_lower_bound=20+4*vp(Q(b)),
                   relative_error_lower_bound=20+4*vp(Q(b))-row['valuation'])
        evidence.append(row)
    nd, pair = norms[(a, b)], tuple(x['label'] for x in evidence)
    norm_bits = int(nd['sign'] < 0) | sum((e % 2) << (j+1) for j, e in enumerate(nd['support_exponents']))
    gen = dict(index=i, pair=(a, b), norm_data=nd, norm_bits=norm_bits, ordered_sign_bits=bits,
               sign_evidence=signs, real_code=canonical(bits), components=evidence,
               raw_dyadic_labels=pair, dyadic_quotient=orbit(pair)[0])
    check('every generator arithmetic field '+str(i), gen,
          {key: C['generators'][i][key] for key in gen})
    check('replay generator '+str(i), R['generators'][i], dict(pair=(a, b), norm=nd['norm'], signs=bits, local_pair=pair))
    check('strict generator bounds '+str(i), all(x['relative_error_lower_bound'] > 8 for x in evidence), True)
    generators.append(gen)
    local_generators.append(components)

# Check the entire stored coordinate interface, but obtain the joint image
# below by direct products, independently of echelon codes.
codes = {int(k): v for k, v in C['field_coordinates']['labels_to_codes'].items()}
check('complete field coordinate bijection', [sorted(codes), sorted(codes.values())], [list(range(64)), list(range(64))])
check('all 4096 field products respect coordinates', all(codes[cm(a, b)] == codes[a] ^ codes[b]
      for a in range(64) for b in range(64)), True)
check('field basis', [codes[x] for x in C['field_coordinates']['basis']], [1 << i for i in range(6)])
sb = {}
scalar_rows = []


def reduce_code(x, basis):
    for p in sorted(basis, reverse=True):
        if x >> p & 1:
            x ^= basis[p]
    return x


for s in scalars:
    raw = codes[s] | (codes[s] << 6)
    reduced = reduce_code(raw, sb)
    if reduced:
        sb[reduced.bit_length()-1] = reduced
    scalar_rows.append(dict(label=s, raw_code=raw, reduced_at_insertion=reduced))
check('complete common-scalar reduction evidence', C['common_scalars'], dict(rows=scalar_rows, echelon_basis=sb))
lookup = {}
for a in range(64):
    for b in range(64):
        code = reduce_code(codes[a] | (codes[b] << 6), sb)
        q = orbit((a, b))[0]
        assert code not in lookup or lookup[code] == q
        lookup[code] = q
check('entire scalar quotient lookup', lookup, C['local_code_to_canonical_pair'])
for i, g in enumerate(generators):
    a, b = g['raw_dyadic_labels']
    d = reduce_code(codes[a] | (codes[b] << 6), sb)
    joint = g['norm_bits'] | (g['real_code'] << 5) | (d << 13)
    g.update(dyadic_code=d, joint_code=joint)
    check('generator encoded image '+str(i), g, C['generators'][i])

products, product_evidence, collisions = [], [], {}
for mask in range(32):
    a, loc, n, bits, pair = [Q(1)]+[Q(0)]*7, [one, one], Q(1), 0, (0, 0)
    for i, g in enumerate(generators):
        if mask >> i & 1:
            aa, bb = eligible[i]
            a = mul(a, list(map(Q, [aa, -bb]+[0]*6)), F)
            loc = [lm(loc[j], local_generators[i][j]) for j in range(2)]
            n *= g['norm_data']['norm']
            bits ^= g['ordered_sign_bits']
            pair = tuple(cm(pair[j], g['raw_dyadic_labels'][j]) for j in range(2))
    nr, stages = norm_evidence(a)
    check('direct product norm '+str(mask), nr['norm'], n)
    labels = [label(x) for x in loc]
    check('direct product labels '+str(mask), [x['label'] for x in labels], pair)
    fac = factor(n)
    nc = int(n < 0) | sum((e % 2) << (j+1) for j, e in enumerate(fac['exponents'].values()))
    triple = (nc, canonical(bits), orbit(pair)[0])
    row = dict(mask=mask, norm=n, ordered_sign_bits=bits, raw_local_pair=pair, triple=triple,
               norm_admissible=fac['square'], real_survives=triple[1] in real_image, dyadic_survives=triple[2] in point_image)
    check('complete product replay '+str(mask), row, R['all_32_products'][mask])
    products.append(row)
    product_evidence.append(dict(mask=mask, coordinates=a, norm_evidence=nr, determinant_stages=stages,
                                 local_approximations=loc, local_labels=labels, scalar_orbit=orbit(pair)))
    collisions.setdefault(triple, []).append(mask)
joint = sorted(collisions)
check('complete replay joint image', joint, R['complete_joint_triples'])
decoded = lambda code: (code & 31, (code >> 5) & 255, lookup[code >> 13])
check('complete producer joint image', joint, sorted(decoded(x['code']) for x in C['complete_joint_image']))
for x in C['complete_joint_image']:
    check('complete image representative '+str(x['code']), products[x['witness_mask']]['triple'], decoded(x['code']))
check('all collisions', sorted(collisions.values()), [[m, m ^ 17] for m in range(16)])
check('joint-zero masks', collisions[(0, 0, (0, 0))], [0, 17])
check('saved joint-zero relations', C['joint_zero_relations'], [17])
jb, elimination = {}, []
for g in generators:
    v, witness, trace = g['joint_code'], 1 << g['index'], []
    for pivot in sorted(jb, reverse=True):
        if v >> pivot & 1:
            trace.append(pivot)
            v ^= jb[pivot]['value']
            witness ^= jb[pivot]['witness']
    if v:
        jb[v.bit_length()-1] = dict(value=v, witness=witness)
    elimination.append(dict(generator=g['index'], pivot_trace=trace, remainder=v, witness=witness))
check('full elimination and basis', [elimination, jb], [C['elimination'], C['joint_basis']])
norm_rows = [x for x in joint if x[0] == 0]
real_rows = [x for x in norm_rows if x[1] in real_image]
removed = [x for x in real_rows if x[2] not in point_image]
survivors = [x for x in real_rows if x[2] in point_image]
counts = dict(pairs=319, eligible=5, ineligible=314, joint_rank=len(jb), joint_image=len(joint),
              norm_admissible=len(norm_rows), real_survivors=len(real_rows),
              dyadic_removed_after_real=len(removed), dyadic_survivors_after_real=len(survivors))
check('all exact counts', counts, C['counts'])
check('actual versus required counts', list(counts.values()), [319, 5, 314, 4, 16, 4, 2, 1, 1])
for key, rows in [('norm_admissible_image', norm_rows), ('real_surviving_image', real_rows),
                  ('removed_after_real', removed), ('surviving_both', survivors)]:
    actual = []
    for x in C[key]:
        tr = decoded(x['joint_code'])
        check(key+' representative '+str(x['joint_code']), [tr, products[x['witness_mask']]['triple'],
              (x['joint_code'] & 31, x['real_code'], tuple(x['dyadic_quotient']))], [tr, tr, tr])
        check(key+' dyadic code '+str(x['joint_code']), lookup[x['dyadic_code']], tr[2])
        actual.append(tr)
    check('complete filtered list '+key, sorted(actual), rows)

w = product_evidence[5]
direct = [add(lm(alpha, alpha), scale(alpha, 3)), add(lm(alpha, alpha), scale(alpha, -3))]
components = [label(x) for x in direct]
check('direct quadratic approximations', direct, w['local_approximations'])
check('direct quadratic error multipliers are units', [val(add(scale(alpha, 2), scale(one, s))) for s in [3, -3]], [0, 0])
dw = dict(expression='theta(theta+3)', coordinates=[0, 3, 1]+[0]*5, norm_evidence=w['norm_evidence'],
          norm_square_root=Q(7776, 275), norm_divided_by_3025_square_root=Q(7776, 15125),
          ordered_signs='++++----', real_class='----++++', components=components,
          absolute_error_lower_bound=20, relative_error_lower_bounds=[20-x['valuation'] for x in components],
          common_scalar_orbit=orbit(tuple(x['label'] for x in components)), quotient=(2, 24))
check('entire direct witness evidence', dw, R['direct_witness'])
check('saved witness product', R['witness'], products[5])
check('witness norm and coefficient retained', [products[5]['norm'], products[5]['norm']/3025], [Q(7776, 275)**2, Q(7776, 15125)**2])
check('witness threshold', [products[5]['triple'], products[5]['norm_admissible'], products[5]['real_survives'], products[5]['dyadic_survives']],
      [(0, 240, (2, 24)), True, True, False])
check('witness complete scalar orbit', dw['common_scalar_orbit'], [(2, 24), (4, 6), (6, 4), (10, 31), (17, 18), (18, 17), (24, 2), (31, 10)])
precision = dict(actual_minimum=min(x['relative_error_lower_bound'] for g in generators for x in g['components']), required_strictly_above=8)
check('complete precision claim', precision, C['precision'])
check('strict bounds', [precision['actual_minimum'] > 8, min(dw['relative_error_lower_bounds']) > 8, 9 > 8], [True, True, True])
check('identity survives both point tests', [products[0]['norm_admissible'], products[0]['real_survives'], products[0]['dyadic_survives']], [True, True, True])
for name, report in [('producer', C), ('replay', R)]:
    bad = [x['name'] for x in report['checks'] if x['actual'] != x['required']]
    check(name+' complete saved comparison consistency', all(x['passed'] == (x['actual'] == x['required']) for x in report['checks']), True)
    check(name+' saved failures', [bad, report['failures']], [[], []])

failures = [x['name'] for x in checks if not x['passed']]
certificate = dict(inputs=[dict(path=p, sha256=sha256((BASE/p).read_bytes()).hexdigest()) for p in FILES],
                   integral_equation=integral_equation, newton=newton, pairs=pair_records, roots=root_records,
                   generators=generators, products=products, direct_product_evidence=product_evidence,
                   collisions=[dict(triple=k, masks=v) for k, v in sorted(collisions.items())],
                   direct_witness=dw, counts=counts, precision=precision, checks=checks, failures=failures,
                   qualification='Audit of L124 only. Joint collisions are not global relations; no supported-group or point completeness.')
OUT.write_text(json.dumps(clean(certificate), indent=2)+'\n')
print(json.dumps(dict(checks=len(checks), failures=failures, counts=counts, precision=precision,
                      witness_relative_bounds=dw['relative_error_lower_bounds'], square_residue_precision=9,
                      required_strictly_above=8, path=str(OUT))))
if failures:
    raise SystemExit(1)
