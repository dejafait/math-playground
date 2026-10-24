#!/usr/bin/env python3
"""L123 independent audit. No producer, replay or local implementation imports.

L122's already audited finite square-class tables are mathematical inputs.
Full rows, linked determinant evidence and exact transports are checked;
all-place support and the scope of the conclusion are reviewed in L123.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from pathlib import Path
from hashlib import sha256
import json

BASE = Path(__file__).parent
FILES = ['marked-octic-small-global-witness-certificate.json',
         'marked-octic-small-global-witness-replay.json',
         'marked-octic-two-adic-image-certificate.json']
C, R, L = [json.loads((BASE / p).read_text()) for p in FILES]
OUT = BASE / 'marked-octic-small-global-witness-audit-certificate.json'
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
    out = [Q(0)]*(2*n-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    for d in range(2*n-2, n-1, -1):
        q = out[d]/f[n]
        for j in range(n+1):
            out[d-n+j] -= q*f[j]
    return out[:n]


F = list(map(Q, [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]))
E = [Q(a, 9150625) for a in [22130658, -74245842, 91279980, -48315300, 9150625]]
one = [Q(1), Q(0), Q(0), Q(0)]
pi = [Q(0), Q(1), Q(0), Q(0)]
ipi = [-E[i]/E[0] for i in range(1, 5)]


def lm(a, b):
    return mul(a, b, E)


def scale(a, c):
    return [c*x for x in a]


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def vp(q):
    q = Q(q)
    n, d = abs(q.numerator), q.denominator
    return (n & -n).bit_length() - (d & -d).bit_length()


def val(a):
    return min(4*vp(c)+i for i, c in enumerate(a) if c)


def inverse(a):
    # Solve multiplication by a against 1, with exact rational row reduction.
    cols = [lm(a, [Q(i == j) for i in range(4)]) for j in range(4)]
    m = [[cols[j][i] for j in range(4)]+[Q(i == 0)] for i in range(4)]
    for j in range(4):
        k = next(k for k in range(j, 4) if m[k][j])
        m[j], m[k] = m[k], m[j]
        m[j] = [x/m[j][j] for x in m[j]]
        for k in range(4):
            if k != j:
                q = m[k][j]
                m[k] = [x-q*y for x, y in zip(m[k], m[j])]
    return [row[-1] for row in m]


cosets = {tuple(row['residue']): row['label'] for row in L['residue_ring']['complete_unit_cosets']}
table = L['residue_ring']['unit_multiplication_table']
scalars = L['scalar_labels']


def label(a):
    w = val(a)
    z = a[:]
    for _ in range(abs(w)):
        z = lm(z, ipi if w >= 0 else pi)
    residue = [q.numerator*pow(q.denominator, -1, m) % m for q, m in zip(z, [8, 4, 4, 4])]
    return dict(valuation=w, normalized_residue=residue, label=32*(w % 2)+cosets[tuple(residue)])


def classmul(a, b):
    return 32*((a//32) ^ (b//32))+table[a % 32][b % 32]


def orbit(pair):
    return sorted([[classmul(pair[0], s), classmul(pair[1], s)] for s in scalars])


def norm_evidence(a):
    n = 8
    cols = [mul(a, [Q(i == j) for i in range(n)], F) for j in range(n)]
    matrix = [[cols[j][i] for j in range(n)] for i in range(n)]
    terms = []
    for perm in permutations(range(n)):
        z = Q((-1)**sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n)))
        for i in range(n):
            z *= matrix[i][perm[i]]
            if not z:
                break
        if z:
            terms.append(dict(permutation=list(perm), signed_product=str(z)))
    det = sum((Q(t['signed_product']) for t in terms), Q(0))
    m, trace = [row[:] for row in matrix], []
    for j in range(n):
        k = next(k for k in range(j, n) if m[k][j])
        m[j], m[k] = m[k], m[j]
        p = m[j][j]
        trace.append(dict(column=j, swapped_row=k, pivot=str(p)))
        for k in range(j+1, n):
            q = m[k][j]/p
            m[k] = [x-q*y for x, y in zip(m[k], m[j])]
    return dict(matrix=matrix, elimination=trace, norm=det), terms


check('whole polynomial and coefficient', [int(11*x) for x in F], L['input']['G'])
check('whole degree support input', C['input'], dict(F=list(map(int, F)), leading_coefficient_G=3025,
      degree=8, support=[2, 3, 5, 11], integral_generator='u=275 theta',
      integral_equation=[int(F[i]*275**(7-i)) for i in range(8)]+[1]))
check('local input hash', C['local_input'], dict(path=FILES[2], sha256=sha256((BASE/FILES[2]).read_bytes()).hexdigest()))
check('exact quartic input', E, L['field']['monic_E'])
check('theta transport', L['field']['actual_theta_transports'], ['alpha', '-alpha'])
check('uniformizer inverse', lm(pi, ipi), one)
r = list(map(Q, [468, -1126, Q(2585, 3), Q(-5500, 27)]))
check('exact r input', r, L['field']['r'])
check('exact r identity', lm(r, r), scale(add(pi, scale(one, -1)), 2))
alpha = add(one, scale(r, 2))
target = add(one, scale(r, 4))
residuals = []
for _ in range(3):
    error = add(lm(alpha, alpha), scale(target, -1))
    residuals.append(val(error))
    if len(residuals) < 3:
        alpha = add(alpha, scale(lm(error, inverse(scale(alpha, 2))), -1))
check('Newton residuals and exact approximation', [residuals, alpha], [[12, 16, 24], L['field']['alpha_approximation']])
check('Hensel root precision', [L['field']['alpha_error_lower_bound'], L['input']['strict_threshold']], [20, 8])
gens = [[Q(0), Q(1)]+[Q(0)]*6, [Q(1), Q(-1)]+[Q(0)]*6, [Q(1), Q(1)]+[Q(0)]*6]
lgens = [[alpha, scale(alpha, -1)], [add(one, scale(alpha, -1)), add(one, alpha)],
         [add(one, alpha), add(one, scale(alpha, -1))]]
generator_rows = []
for j, (name, pair) in enumerate(zip(['theta', '1-theta', '1+theta'], lgens)):
    nr, _ = norm_evidence(gens[j])
    check(name+' norm certificate', nr, C['generator_norms'][j])
    comps = [label(a) for a in pair]
    margins = [20-c['valuation'] for c in comps]
    row = dict(name=name, approximate_components=pair, components=comps,
               relative_error_lower_bounds=margins, required_strictly_above=8)
    check(name+' complete localization', row, C['local_generators'][j])
    check(name+' strict precision', min(margins) > 8, True)
    generator_rows.append(row)

expected_rows, determinant_terms = [], []
for k, abc in enumerate(product(range(2), repeat=3)):
    a, b, c = abc
    global_element = [Q(1)]+[Q(0)]*7
    local_pair = [one[:], one[:]]
    class_pair = [0, 0]
    for j, bit in enumerate(abc):
        if bit:
            global_element = mul(global_element, gens[j], F)
            local_pair = [lm(local_pair[i], lgens[j][i]) for i in range(2)]
            class_pair = [classmul(class_pair[i], generator_rows[j]['components'][i]['label']) for i in range(2)]
    local_labels = [label(z)['label'] for z in local_pair]
    check(str(abc)+' direct product versus certified generator classes', local_labels, class_pair)
    nr, terms = norm_evidence(global_element)
    determinant_terms.append(dict(exponents=list(abc), nonzero_determinant_terms=terms))
    exps = {'2':10*(b+c), '3':5*a, '5':-2*(a+b+c), '11':-(a+b+c)}
    norm = Q(1)
    for p, e in exps.items():
        norm *= Q(int(p))**e
    check(str(abc)+' determinant versus exact norm formula', nr['norm'], norm)
    eligible = all(e % 2 == 0 for e in exps.values())
    degree = max(i for i, q in enumerate(global_element) if q)
    integral = [q*275**(degree-i) for i, q in enumerate(global_element[:degree+1])]
    check(str(abc)+' cleared integrality', all(q.denominator == 1 for q in integral), True)
    orb = orbit(local_labels)
    row = dict(exponents=list(abc), coordinates=global_element, clearing_denominator=275**degree,
               integral_u_coordinates=integral, norm_evidence=nr,
               norm_factorization=dict(sign=1, exponents=exps, numerator_remainder=1,
                                      denominator_remainder=1, square=eligible),
               supported=True, global_norm_admissible=eligible, raw_local_labels=local_labels,
               common_scalar_orbit=orb, quotient=orb[0],
               in_two_adic_point_image=(orb[0] in L['point_image']) if eligible else None)
    expected_rows.append(row)
    check(str(abc)+' complete producer row', row, C['rows'][k])

check('complete eight rows', len(C['rows']), 8)
check('all replay determinant terms', determinant_terms, R['full_determinant_terms'])
delta = scale(r, -4)
check('exact witness producer evidence', dict(expression='1-theta^2=-4r in both factors',
      components=delta, square_evidence=label(delta)), C['exact_diagonal_delta'])
normalized = delta[:]
for _ in range(10):
    normalized = lm(normalized, ipi)
check('complete replay normalized coefficients', normalized, R['witness_normalized_coefficients'])
check('witness valuation residue and label', label(delta), dict(valuation=10, normalized_residue=[1, 2, 3, 3], label=25))
check('replay residue', R['witness_residue'], [1, 2, 3, 3])
check('replay complete scalar orbit', R['witness_scalar_orbit'], orbit([25, 25]))
check('scalar labels', sorted(scalars), [0, 5, 8, 12, 15, 19, 22, 29])
check('witness canonical label', orbit([25, 25])[0], [1, 1])
check('full point image', L['point_image'], [[0, 0], [0, 5], [0, 8], [0, 22], [2, 6]])
check('leading coefficient retained', Q(1024, 275)**2/Q(3025), Q(1024, 15125)**2)
collisions = [[expected_rows[i]['exponents'], row['exponents']]
              for j, row in enumerate(expected_rows) for i in range(j)
              if expected_rows[i]['quotient'] == row['quotient']]
check('complete collisions', collisions, C['local_collisions'])
check('no collisions', collisions, [])
rejected = [row['exponents'] for row in expected_rows
            if row['global_norm_admissible'] and not row['in_two_adic_point_image']]
check('rejected rows', rejected, C['rejected_exponent_vectors'])
check('complete counts', C['counts'], dict(rows=8, support_certified=8, norm_admissible=2, rejected=1))
for name, source, count in [('producer', C, 48), ('replay', R, 40)]:
    check(name+' reported check count', len(source['checks']), count)
    check(name+' saved comparison consistency', all(x['passed'] == (x['actual'] == x['required']) for x in source['checks']), True)
    check(name+' saved failures', source['failures'], [x['name'] for x in source['checks'] if not x['passed']])
    check(name+' saved checks pass', source['failures'], [])

failures = [x['name'] for x in checks if not x['passed']]
certificate = dict(inputs=[dict(path=p, sha256=sha256((BASE/p).read_bytes()).hexdigest()) for p in FILES],
                   checks=checks, failures=failures, full_rows=expected_rows,
                   full_determinant_terms=determinant_terms, generator_rows=generator_rows,
                   witness_normalized_coefficients=normalized,
                   limitations=['Uses audited L122 finite tables', 'No other-place survival test',
                                'No global class completeness or point determination'])
OUT.write_text(json.dumps(clean(certificate), indent=2)+'\n')
print(json.dumps(dict(checks=len(checks), failures=failures, rows=8, required_rows=8,
                     norm_admissible=2, rejected=1, collisions=len(collisions),
                     minimum_relative_precision=14, required_strictly_above=8,
                     residue_precision=9, required_residue_precision=9, path=str(OUT))))
for row in expected_rows:
    print(''.join(map(str, row['exponents'])), 'norm='+str(row['norm_evidence']['norm']),
          'norm_admissible='+str(row['global_norm_admissible']), 'quotient='+str(row['quotient']))
if failures:
    raise SystemExit(1)
