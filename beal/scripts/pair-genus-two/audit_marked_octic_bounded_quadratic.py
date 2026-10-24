#!/usr/bin/env python3
"""L125 critical-audit arithmetic. Reads all rows; no notebook module imports.

Producer/replay are preserved. Local image theorems are L118/L119/L122
inputs, not re-proved by this finite instance audit.
"""
from fractions import Fraction as Q
from itertools import product
from math import isqrt
from pathlib import Path
import hashlib
import json


def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, (list, tuple)):
        return [encode(y) for y in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def vp(x, p):
    x = Q(x)
    if not x:
        return 10**9
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % p == 0:
        n //= p
        v += 1
    while d % p == 0:
        d //= p
        v -= 1
    return v


def ev(c, x):
    y = Q(0)
    for a in c[::-1]:
        y = y*x+a
    return y


def convolution(a, b):
    c = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def reduce(c, f):
    c = list(map(Q, c))
    n = len(f)-1
    c += [Q(0)]*max(0, n-len(c))
    for k in range(len(c)-1, n-1, -1):
        z = c[k]/f[n]
        for j in range(n+1):
            c[k-n+j] -= z*f[j]
    return c[:n]


def determinant(a):
    a = [r[:] for r in a]
    out, trace = Q(1), []
    for j in range(len(a)):
        p = next(i for i in range(j, len(a)) if a[i][j])
        if p != j:
            a[p], a[j] = a[j], a[p]
            out = -out
        z = a[j][j]
        out *= z
        trace.append(dict(column=j, pivot_row=p, pivot=z))
        for i in range(j+1, len(a)):
            factor = a[i][j]/z
            a[i] = [x-factor*y for x, y in zip(a[i], a[j])]
    return out, trace


F = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
E = list(map(Q, [22130658, -74245842, 91279980, -48315300, 9150625]))
ONE = [Q(1), Q(0), Q(0), Q(0)]
PI = [Q(0), Q(1), Q(0), Q(0)]


def mul(a, b):
    return reduce(convolution(a, b), E)


def add(a, b):
    return [x+y for x, y in zip(a, b)]


def scale(a, b):
    return [x*b for x in a]


def power(a, n):
    out = ONE
    while n:
        if n % 2:
            out = mul(out, a)
        n //= 2
        a = mul(a, a)
    return out


def val(a):
    return min(4*vp(c, 2)+i for i, c in enumerate(a))


def residue(a):
    return tuple(c.numerator*pow(c.denominator, -1, m) % m
                 for c, m in zip(a, (8, 4, 4, 4)))


def main():
    base = Path(__file__).parent
    names = ['marked-octic-bounded-quadratic-certificate.json',
             'marked-octic-bounded-quadratic-replay.json',
             'marked-octic-two-adic-image-certificate.json']
    c, replay, dy = [json.loads((base/n).read_text()) for n in names]
    hashes = {n: hashlib.sha256((base/n).read_bytes()).hexdigest() for n in names}
    checks = []

    def check(name, actual, required):
        actual, required = encode(actual), encode(required)
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    check('exact input', c['input'], dict(F=F, bounds=[-8, 8], support=[2, 3, 5, 11], leading_coefficient=3025))
    check('unchanged dyadic certificate', c['local_input'], dict(path=names[2], sha256=hashes[names[2]]))
    box = [[a, b] for a in range(-8, 9) for b in range(-8, 9)]
    check('producer complete ordered box', [[r['a'], r['b']] for r in c['rows']], box)
    check('replay complete ordered box', [r['pair'] for r in replay['norms']], box)
    eligible, square, norm_records = [], [], []
    for row, old in zip(c['rows'], replay['norms']):
        a, b = row['a'], row['b']
        tag = f'({a},{b})'
        columns = [reduce([Q(0)]*i+[Q(b), Q(a), Q(1)], F) for i in range(8)]
        matrix = [list(r) for r in zip(*columns)]
        norm, pivots = determinant(matrix)
        check('full replay determinant record '+tag, old,
              dict(pair=[a, b], matrix=matrix, elimination=pivots, norm=norm))
        quotient, remainder = list(map(Q, row['division_quotient'])), list(map(Q, row['remainder']))
        coefficients = convolution([b, a, 1], quotient)
        for j, d in enumerate(remainder):
            coefficients[j] += d
        check('all nine division coefficients '+tag, coefficients, list(map(Q, F)))
        d, z = remainder
        check('resultant norm with multiplicity '+tag, (d*d-a*z*d+b*z*z)/275**2, norm)
        check('producer norm '+tag, row['norm'], norm)
        n, den = abs(norm.numerator), norm.denominator
        exponents = [vp(norm, p) for p in (2, 3, 5, 11)]
        for p in (2, 3, 5, 11):
            while n % p == 0:
                n //= p
            while den % p == 0:
                den //= p
        allowed = n == den == 1
        check('entire support record '+tag, row['support'], dict(exponents=exponents,
              numerator_remainder=n, denominator_remainder=den, eligible=allowed))
        ns = norm > 0 and isqrt(norm.numerator)**2 == norm.numerator and isqrt(norm.denominator)**2 == norm.denominator
        root = Q(isqrt(norm.numerator), isqrt(norm.denominator)) if ns else None
        check('square decision and root '+tag, [row['norm_square'], row['norm_square_root']], [ns, root])
        if allowed:
            eligible.append([a, b])
            check('support parity agrees with square test '+tag, ns, norm > 0 and all(v % 2 == 0 for v in exponents))
        if allowed and ns:
            square.append([a, b])
        norm_records.append(dict(pair=[a, b], norm=norm, support_remainder=[n, den], eligible=allowed, norm_square=ns))
    check('thirteen eligible', c['eligible_pairs'], eligible)
    check('all seven local rows', [r['pair'] for r in c['tested']], square)
    check('all seven replay rows', [r['pair'] for r in replay['local_replay']], square)

    # Independent quotient-ring arithmetic reconstructs all unit labels.
    units = [(a, b, d, e) for a in (1, 3, 5, 7) for b, d, e in product(range(4), repeat=3)]
    squares = {residue(mul(u, u)) for u in units}
    unseen, groups = set(units), []
    while unseen:
        representative = min(unseen)
        group = {residue(mul(representative, s)) for s in squares}
        check('disjoint complete unit coset '+str(len(groups)), group <= unseen and len(group) == 8, True)
        groups.append(sorted(group))
        unseen -= group
    labels = {u: i for i, group in enumerate(groups) for u in group}
    check('unit counts', [len(units), len(squares), len(groups), len(labels)], [256, 8, 32, 256])
    check('every imported unit label', dy['residue_ring']['complete_unit_cosets'],
          [dict(residue=list(u), label=labels[u]) for u in sorted(units)])
    # pi inverse follows directly from the constant term of E.
    pi_inverse = [-E[i+1]/E[0] for i in range(4)]
    check('exact uniformizer inverse', mul(PI, pi_inverse), ONE)

    def label(x):
        w = val(x)
        normalized = mul(x, power(pi_inverse if w >= 0 else PI, abs(w)))
        res = residue(normalized)
        return dict(valuation=w, normalized_residue=list(res), label=32*(w % 2)+labels[res])

    def lm(x, y):
        return 32*((x//32) ^ (y//32))+labels[residue(mul(groups[x % 32][0], groups[y % 32][0]))]

    scalar_labels = [label(scale(ONE, Q(s)))['label'] for s in (1, 5, 2, 10, -1, -5, -2, -10)]
    check('ordered theorem scalar labels', scalar_labels, [0, 22, 12, 29, 5, 8, 19, 15])
    check('single common scalar image', dy['scalar_labels'], sorted(scalar_labels))
    r = list(map(Q, [468, -1126, Q(2585, 3), Q(-5500, 27)]))
    target = add(ONE, scale(r, 4))
    alpha0 = list(map(Q, dy['field']['alpha_approximation']))
    check('same exact alpha square target', dy['field']['alpha_square_target'], target)
    residual = add(mul(alpha0, alpha0), scale(target, -1))
    check('actual residual and derivative valuations', [val(residual), val(scale(alpha0, 2))], [24, 4])
    beta = add(ONE, scale(r, 2))
    check('approximant in original Hensel ball', val(add(alpha0, scale(beta, -1))), 8)
    check('alpha0 is a unit', val(alpha0), 0)
    # Strong Hensel: same root, error 24-4=20; alpha+alpha0 has value 4.
    intervals = [(Q(5, 2), Q(11, 4)), (Q(3, 2), Q(2)), (Q(3, 4), Q(7, 8)), (Q(1, 4), Q(1, 2)),
                 (Q(-1, 2), Q(-1, 4)), (Q(-7, 8), Q(-3, 4)), (Q(-2), Q(-3, 2)), (Q(-11, 4), Q(-5, 2))]
    for j, (root, interval) in enumerate(zip(c['roots'], intervals)):
        lo, hi = interval
        check('exact refined interval '+str(j), root['interval'], interval)
        check('exact endpoint values '+str(j), root['endpoint_values'], [ev(F, lo), ev(F, hi)])
        check('strict sign change '+str(j), ev(F, lo)*ev(F, hi) < 0, True)
        for bisect in root['bisections']:
            check('exact bisection '+str(j), bisect['F_value'], ev(F, Q(bisect['midpoint'])))
    check('eight separate intervals', len(c['roots']), 8)

    H = [3025, -31460, 76230, -39204, 2673]
    hp = [(i+1)*H[i+1] for i in range(4)]
    transport = c['five_transport']
    check('actual five transport polynomial and precision', [transport['H'], transport['precision']], [H, 8])
    check('simple Hensel derivative', int(ev(hp, 3)) % 5, 1)
    for step in transport['r0_hensel']:
        check('full r0 Hensel residual '+str(step['depth']), step['residual'], ev(H, step['root']))
        check('r0 precision '+str(step['depth']), [int(ev(H, step['root'])) % 5**step['depth'], step['root'] % 5], [0, 3])
    M = 5**8
    r0, s = transport['r0_approximation'], transport['s_approximation']
    rad = 3*pow(r0, -1, M) % M
    check('r0 precision eight', int(ev(H, r0)) % M, 0)
    check('full radicand', transport['sqrt_radicand'], rad)
    for step in transport['s_hensel']:
        check('principal root precision '+str(step['depth']), [(step['root']**2-rad) % 5**step['depth'], step['root'] % 5], [0, 1])
    check('final principal square root', [(s*s-rad) % M, s % 5], [0, 1])
    point2 = [[0, 0], [0, 5], [0, 8], [0, 22], [2, 6]]
    check('actual dyadic point set', dy['point_image'], point2)
    records = []
    margins2, margins5, ramified_margins = [], [], []
    for row, old in zip(c['tested'], replay['local_replay']):
        a, b = row['pair']
        tag = str(row['pair'])
        norm_row = c['rows'][(a+8)*17+b+8]
        check('local row exact norm and root '+tag, [row['norm'], row['norm_square_root']],
              [norm_row['norm'], norm_row['norm_square_root']])
        real, bits = [], 0
        for j, (lo, hi) in enumerate(intervals):
            values = [ev([b, a, 1], lo), ev([b, a, 1], hi)]
            if lo <= Q(-a, 2) <= hi:
                values.append(Q(4*b-a*a, 4))
            bounds = [min(values), max(values)]
            check('strict real bounds '+tag+str(j), bounds[0] > 0 or bounds[1] < 0, True)
            negative = bounds[1] < 0
            bits |= int(negative) << j
            real.append(dict(value_bounds=bounds, negative=negative))
        code = bits ^ (255 if bits & 1 else 0)
        check('complete real record '+tag, [row['real_evidence'], row['real_signs'], row['real_code'], row['passes_real']],
              [real, ''.join('-' if bits >> j & 1 else '+' for j in range(8)), code, code in (0, 252, 240, 192)])
        components = []
        for j, sign in enumerate((1, -1)):
            approx = add(add(mul(alpha0, alpha0), scale(alpha0, sign*a)), scale(ONE, b))
            bound = 20+min(4, 4*vp(a, 2))
            lab = label(approx)
            check('entire producer dyadic component '+tag+str(j), row['dyadic_components'][j],
                  dict(approximation=approx, **lab, absolute_error_lower_bound=bound, relative_error_lower_bound=bound-lab['valuation']))
            replay_approx = add(add(target, scale(alpha0, sign*a)), scale(ONE, b))
            lab2 = label(replay_approx)
            margin = 20+4*vp(a, 2)-lab2['valuation'] if a else None
            check('entire replay dyadic component '+tag+str(j), old['dyadic'][j],
                  dict(exact_square_approximation=replay_approx, **lab2, relative_error_lower_bound=margin, error_zero=not a))
            check('matching exact classes '+tag+str(j), lab['label'], lab2['label'])
            check('both strict dyadic bounds '+tag+str(j), bound-lab['valuation'] > 8 and (margin is None or margin > 8), True)
            margins2.append(bound-lab['valuation'])
            components.append(lab)
        orbit = sorted([lm(components[0]['label'], t), lm(components[1]['label'], t)] for t in scalar_labels)
        check('full dyadic orbit and actual image '+tag, [row['dyadic_orbit'], row['dyadic_quotient'], row['passes_two']],
              [orbit, min(orbit), min(orbit) in point2])
        for j, e in enumerate((4, 2)):
            terms = ([e*vp(a, 5)+1] if a else [])+([e*vp(b, 5)+2] if b else [])
            lower = min(terms) if terms else None
            check('full ramified record '+tag+str(j), row['five_ramified_components'][j],
                  dict(e=e, value_valuation=-2, principal_error_lower_bound=lower,
                       principal_error_identically_zero=not terms, square_class_bits=[0, 0]))
            check('strict ramified bound or identity '+tag+str(j), lower is None or lower > 0, True)
            if lower is not None:
                ramified_margins.append(lower)
        x, y = Q(1, r0)+b, Q(a*s, 3)
        w = min(vp(x, 5), vp(y, 5))
        normalized = [x/Q(5)**w, y/Q(5)**w]
        residues = [z.numerator*pow(z.denominator, -1, 5) % 5 for z in normalized]
        nr = (residues[0]**2-3*residues[1]**2) % 5
        check('entire U record '+tag, row['five_U'], dict(approximation=[x, y], valuation=w, normalized_residue=residues,
              residue_norm=nr, square_class_bits=[w % 2, int(nr in (2, 3))], absolute_error_lower_bound=8, relative_error_lower_bound=8-w))
        check('exact U square and strict bound '+tag, w % 2 == 0 and nr in (1, 4) and 8-w > 0, True)
        margins5.append(8-w)
        # Verify replay's higher-precision roots and full normalized evaluation.
        ur = old['U']
        rr, ss = ur['r0'], ur['s']
        modulus = 5**10
        check('replay exact root balls '+tag, [int(ev(H, rr)) % modulus, rr % 5, (ss*ss-3*pow(rr, -1, modulus)) % modulus, ss % 5], [0, 3, 0, 1])
        xx, yy = Q(1, rr)+b, Q(a*ss, 3)
        ww = min(vp(xx, 5), vp(yy, 5))
        residues2 = [(z/Q(5)**ww).numerator*pow((z/Q(5)**ww).denominator, -1, 5) % 5 for z in (xx, yy)]
        check('entire replay U record '+tag, ur, dict(r0=rr, s=ss, valuation=ww, residue=residues2,
              residue_norm=(residues2[0]**2-3*residues2[1]**2) % 5))
        check('matching normalized U values '+tag, [ww, residues2], [w, residues])
        five_orbit = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 0]]
        check('full five-adic common scalar orbit '+tag, [row['five_raw'], row['five_orbit'], row['five_canonical'], row['passes_five']],
              [[0]*6, five_orbit, '000000', True])
        records.append(dict(pair=[a, b], real_signs=row['real_signs'], dyadic=components, orbit=orbit,
                            U_valuation=w, U_residue=residues, passes=[code in (0, 252, 240, 192), min(orbit) in point2, True]))
    counts = dict(total=len(norm_records), eligible=len(eligible), norm_square=len(square),
                  real_survivors=sum(r['passes'][0] for r in records),
                  real_two_survivors=sum(all(r['passes'][:2]) for r in records),
                  removed_at_five=sum(all(r['passes'][:2]) and not r['passes'][2] for r in records))
    check('producer complete counts', c['counts'], counts)
    check('replay complete counts', replay['counts'], counts)
    check('claimed counts', counts, dict(total=289, eligible=13, norm_square=7, real_survivors=6, real_two_survivors=4, removed_at_five=0))
    check('producer removed list', c['removed'], [])
    check('producer precision', c['precision'], dict(two_minimum=min(margins2), two_required_strictly_above=8,
          five_U_minimum=min(margins5), five_required_strictly_above=0))
    check('all original failure fields', [c['failures'], replay['failures']], [[], []])
    # Review every stored replay comparison, not its summary success flag.
    for i, comparison in enumerate(replay['checks']):
        check('stored replay comparison '+str(i), [comparison['actual'] == comparison['required'], comparison['passed']], [True, True])
    failures = [r['name'] for r in checks if not r['passed']]
    bounds = dict(two=dict(actual=min(margins2), required_strictly_above=8),
                  U=dict(actual=min(margins5), required_strictly_above=0),
                  ramified=dict(actual=min(ramified_margins), required_strictly_above=0))
    output = base/'marked-octic-bounded-quadratic-audit-certificate.json'
    output.write_text(json.dumps(encode(dict(source_sha256=hashes, counts=counts, bounds=bounds,
        all_norm_decisions=norm_records, local_rows=records, comparisons=checks, failures=failures,
        limitations='Only L125 individual family; local image theorems imported; no product closure or point completeness.')), indent=2)+'\n')
    print(json.dumps(dict(result='PASS' if not failures else 'FAIL', comparisons=len(checks), counts=counts,
                         bounds=bounds, failures=failures, certificate=str(output.relative_to(Path.cwd())))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
