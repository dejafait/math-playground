#!/usr/bin/env python3
"""Complete fixed-instance replay; does not import the producer.

Uses independent exhaustive point counts and Fraction endpoint arithmetic.
External homology/period theorems and optimality qualification are in L043.
"""
import json
import subprocess
import sys
from fractions import Fraction as F
from hashlib import sha256
from math import factorial, gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
ROOT = BASE.parent.parent


def replay(data, checks):
    def need(label, condition):
        if not condition:
            raise ValueError(label)
        checks.append(label)

    need('schema', data['schema'] == 'conductor-eleven-full-absolute-v1')
    paths = [BASE/'structural-certificate.json', BASE/'dual-certificate.json', BASE/'arithmetic-input.json']
    need('complete byte bindings', data['inputs'] == {p.name: sha256(p.read_bytes()).hexdigest() for p in paths})
    structural, dual, arithmetic = [json.loads(p.read_text()) for p in paths]
    need('source scope and qualifications', data['source_scope'] == {
        'model': [0, -1, 1, -10, -20], 'N': 11, 'optimal_label': '11a1',
        'absolute_Manin_constant': 1, 'components': 1,
        'published_optimality_qualification': 'L040; complete isogeny class and two-period comparison'})
    need('arithmetic instance', arithmetic['model'] == data['source_scope']['model'] and arithmetic['conductor'] == 11)
    upstream = HERE/'upstream-replay'
    upstream.mkdir(exist_ok=True)
    result = subprocess.run([sys.executable, str(ROOT/'scripts/dual-kernel/verify_certificate.py'),
                             str(paths[1]), '--structural', str(paths[0]), '--arithmetic', str(paths[2]),
                             '--out', str(upstream/'dual-verification.json')], capture_output=True, text=True)
    (upstream/'replay.txt').write_text(result.stdout+result.stderr)
    report = json.loads((upstream/'dual-verification.json').read_text())
    need('fresh complete structural and dual replay', result.returncode == 0 and report['failures'] == [])
    need('fresh dual byte binding', report['certificate_sha256'] == data['inputs']['dual-certificate.json'])
    p = structural['presentation']
    need('entire integral relative module dimension', (p['s'], p['r'], p['d']) == (12, 9, 3))
    Pi, Q, K = [p[k]['entries'] for k in ('Pi', 'Q', 'K')]

    def mul(a, b):
        need('multiplication shapes', len(a[0]) == len(b))
        return [[sum(row[k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for row in a]

    def transpose(a):
        return [[a[i][j] for i in range(len(a))] for j in range(len(a[0]))]

    b = data['boundary']
    need('two cusp classes with canonical order', b['cusp_order'] == ['zero', 'infinity'])
    need('complete endpoint witnesses', len(b['endpoint_witnesses']) == 12)
    raw = []
    for i, pair in enumerate(structural['endpoints']):
        flags = []
        need('both endpoint witnesses', len(b['endpoint_witnesses'][i]) == 2)
        for j, (num, den) in enumerate(pair):
            need('reduced endpoint', den >= 0 and gcd(num, den) == 1)
            w = b['endpoint_witnesses'][i][j]
            flag = int(den % 11 == 0)
            tp, tq = ((1, 0) if flag else (0, 1))
            u = w['unit']
            need('cusp identity', w['cusp'] == [num, den] and w['class'] == flag)
            need('complete cusp-equivalence unit witness', type(u) is int and 1 <= u < 11
                 and (tq-u*den) % 11 == 0 and (u*tp-num) % gcd(den, 11) == 0)
            flags.append(flag)
        raw.append(flags[1]-flags[0])
    need('all raw boundaries', raw == [1, -1]+[0]*10 and b['raw_reduced'] == raw)
    need('full boundary target, not just scalar', b['raw_full'] == [[-v for v in raw], raw])
    source_images = mul([raw], transpose(structural['A']['entries']))
    saturated_images = mul([raw], K)
    need('all 24 source relations descend', b['source_images'] == source_images == [[0]*24])
    need('all 9 saturated relations descend', b['saturated_images'] == saturated_images == [[0]*9])
    B = mul([raw], Q)[0]
    need('integral quotient boundary', b['quotient_reduced'] == B == [0, 0, -1])
    need('full quotient boundary', b['quotient_full'] == [[-v for v in B], B])
    need('boundary on all 12 integral generators', mul([B], Pi) == [raw])
    k = data['kernel']
    T, Ti = k['unimodular_transform'], k['inverse']
    need('integral transform shapes', len(T) == len(Ti) == 3 and all(len(row) == 3 for row in T+Ti)
         and all(type(v) is int for row in T+Ti for v in row))
    identity = [[int(i == j) for j in range(3)] for i in range(3)]
    need('both unimodular inverse products', mul(T, Ti) == mul(Ti, T) == identity)
    need('full integral boundary normal form', k['boundary_after_transform'] == mul([B], T) == [[1, 0, 0]])
    basis = [[row[j] for row in T] for j in (1, 2)]
    need('entire integral kernel basis', k['basis_columns'] == basis == [[1, 0, 0], [0, 1, 0]])
    need('complete raw kernel lifts', k['raw_basis_columns'] == [[row[j] for row in Q] for j in (0, 1)])
    need('kernel lifts map correctly', [mul(Pi, [[v] for v in col]) for col in k['raw_basis_columns']]
         == [[[v] for v in col] for col in basis])
    phi = list(map(F, dual['line']['v']))
    need('certified full relative line', phi == [F(5, 2), F(5), F(1)])
    image = [sum(a*v for a, v in zip(phi, col)) for col in basis]
    need('all absolute basis functional values', list(map(F, k['functional_values'])) == image)
    den = k['common_denominator']
    integers = [v*den for v in image]
    need('integer image after denominator clearing', den == 2 and integers == list(map(F, k['integer_values'])) == [5, 10])
    gg = gcd(*k['integer_values'])
    need('full image gcd and complete Bezout', k['gcd'] == gg == 5
         and all(v % gg == 0 for v in k['integer_values'])
         and len(k['bezout']) == 2 and sum(a*v for a, v in zip(k['bezout'], integers)) == gg)
    g = F(gg, den)
    need('positive rational image generator', F(k['positive_image_generator']) == g)
    need('primitive functional on full kernel', list(map(F, k['primitive_values'])) == [v/g for v in image] == [1, 2])
    cycle = data['cycle']
    rawcycle = [0]*12
    rawcycle[3] = -1
    need('oriented cycle is reversed generator 3', cycle['raw'] == rawcycle
         and cycle['path'] == list(reversed(structural['endpoints'][3])) == [[0, 1], [-1, 2]])
    xy = [row[0] for row in mul(Pi, [[v] for v in rawcycle])]
    phicycle = sum(a*v for a, v in zip(phi, xy))
    need('absolute cycle coordinates and functional', cycle['coordinates'] == xy == [0, -1, 0]
         and sum(a*v for a, v in zip(B, xy)) == 0 and F(cycle['phi']) == phicycle == -5)
    aa, bb, cc, dd = cycle['matrix']
    need('direct Gamma0 matrix and orientation', cycle['matrix'] == [-5, -1, 11, 2]
         and aa*dd-bb*cc == 1 and cc > 0 and cc % 11 == 0 and F(bb, dd) == F(-1, 2))
    ar, ai = map(F, cycle['alpha'])
    nr, ni, dr, di = aa*ar+bb, aa*ai, cc*ar+dd, cc*ai
    mapped = [(nr*dr+ni*di)/(dr*dr+di*di), (ni*dr-nr*di)/(dr*dr+di*di)]
    need('exact upper half-plane endpoints', [ar, ai] == [F(-2, 11), F(1, 11)]
         and list(map(F, cycle['M_alpha'])) == mapped == [F(-5, 11), F(1, 11)])
    f = data['fourier']
    need('bounded schedule', (f['bits'], f['T'], f['atan_count'], f['exp_count'], f['cos_degree']) == (48, 64, 32, 40, 24))
    D, nmax = 1 << f['bits'], f['T']
    need('scale and positive height', f['scale'] == D and F(f['height']) == ai)

    def exact(x):
        need('outward interval shape', len(x) == 2 and all(type(v) is int for v in x) and x[0] <= x[1])
        return [F(v, D) for v in x]

    def outer(lo, hi):
        need('ordered exact endpoints', lo <= hi)
        return [(lo*D).__floor__(), -((-hi*D).__floor__())]

    def product(x, y):
        ends = [a*b for a in exact(x) for b in exact(y)]
        return outer(min(ends), max(ends))

    def times(x, v):
        return outer(*sorted(a*v for a in exact(x)))

    ab = []
    for inv in (5, 239):
        s = sum((F((-1)**j, (2*j+1)*inv**(2*j+1)) for j in range(f['atan_count'])), F(0))
        ab.append(sorted([s, s+F((-1)**f['atan_count'], (2*f['atan_count']+1)*inv**(2*f['atan_count']+1))]))
    need('complete alternating atan bounds', f['atan_brackets'] == [[str(v) for v in row] for row in ab])
    tangent2 = 2*F(1, 5)/(1-F(1, 25))
    tangent4 = 2*tangent2/(1-tangent2*tangent2)
    need('Machin algebra', (tangent4-F(1, 239))/(1+tangent4*F(1, 239)) == 1)
    pi_exact = [16*ab[0][0]-4*ab[1][1], 16*ab[0][1]-4*ab[1][0]]
    need('pi exact enclosure and outward rounding', f['pi_exact'] == list(map(str, pi_exact)) and f['pi'] == outer(*pi_exact))
    h = times(f['pi'], F(2, 11))
    need('exponential argument', h == f['h'])
    ex = []
    for x in exact(h):
        need('decreasing alternating exponential series', 0 < x < 1)
        s = sum(((-x)**j/factorial(j) for j in range(f['exp_count']+1)), F(0))
        ex.append(sorted([s, s+(-x)**(f['exp_count']+1)/factorial(f['exp_count']+1)]))
    rex = [ex[1][0], ex[0][1]]
    r = f['r']
    need('complete exponential endpoints and rounding', f['exp_exact'] == list(map(str, rex)) and r == outer(*rex) and 0 < r[0] <= r[1] < D)
    need('every cosine residue', len(f['cosines']) == 6)
    for j, row in enumerate(f['cosines']):
        need('cosine residue label', row['j'] == j)
        if j == 0:
            need('exact zero-angle cosine', row == {'j': 0, 'interval': [D, D]})
            continue
        theta = sorted(2*F(j, 11)*v for v in exact(f['pi']))
        midpoint, radius = sum(theta)/2, (theta[1]-theta[0])/2
        poly = sum((F((-1)**k)*midpoint**(2*k)/factorial(2*k) for k in range(f['cos_degree']+1)), F(0))
        err = abs(midpoint)**(2*f['cos_degree']+2)/factorial(2*f['cos_degree']+2)+radius
        need('full cosine polynomial and Taylor/Lipschitz errors', row['theta'] == list(map(str, theta))
             and F(row['midpoint']) == midpoint and F(row['radius']) == radius
             and F(row['polynomial']) == poly and F(row['error']) == err
             and row['interval'] == outer(poly-err, poly+err))
    primes = [p for p in range(2, nmax+1) if all(p % j for j in range(2, isqrt(p)+1))]
    need('all prime coefficient inputs', [row['p'] for row in f['point_counts']] == primes)
    aps = {}
    for row in f['point_counts']:
        ell = row['p']
        # Independent exhaustive y enumeration, rather than producer Euler criterion.
        xs = [sum((y*y+y-x*x*x+x*x+10*x+20) % ell == 0 for y in range(ell)) for x in range(ell)]
        if ell == 2:
            pairs = [[x, y] for x in range(ell) for y in range(ell) if (y*y+y-x*x*x+x*x+10*x+20) % ell == 0]
            need('all F2 pairs', row['pairs'] == pairs)
        else:
            need('complete discriminant character count', row['characters'] == [v-1 for v in xs])
        aps[ell] = ell-sum(xs)
        need('full affine count and good/nodal trace', row['affine'] == sum(xs) and row['a_p'] == aps[ell])
    need('actual multiplicative Euler factor', aps[11] == 1)
    coeffs, factors = [0, 1], []
    for n in range(2, nmax+1):
        rem, val, fs = n, 1, []
        for ell in primes:
            if rem % ell:
                continue
            k = 0
            while rem % ell == 0:
                rem //= ell
                k += 1
            powers = [1, aps[ell]]
            for _ in range(2, k+1):
                powers.append(aps[ell]*powers[-1]-(0 if ell == 11 else ell)*powers[-2])
            val *= powers[k]
            fs.append([ell, k, powers])
        need('complete integer factorization', rem == 1)
        coeffs.append(val)
        factors.append([n, fs])
    need('all Fourier coefficients and prime power recurrences', coeffs == f['coefficients'] and factors == f['factorizations']
         and all(abs(coeffs[n]) <= n for n in range(1, nmax+1)))
    need('all finite terms', len(f['terms']) == nmax)
    power, partial = [D, D], [0, 0]

    def cosine_residue(k):
        k %= 11
        return f['cosines'][min(k, 11-k)]['interval']

    for n, row in enumerate(f['terms'], 1):
        power = product(power, r)
        x, y = cosine_residue(aa*n), cosine_residue(-dd*n)
        diff = [x[0]-y[1], x[1]-y[0]]
        term = times(product(power, diff), F(coeffs[n], n))
        partial = [partial[0]+term[0], partial[1]+term[1]]
        need('complete oriented term '+str(n), row == {'n': n, 'power': power, 'difference': diff, 'term': term, 'partial': partial})
    nxt = product(power, r)
    tail_exact = 2*F(nxt[1], D)/(1-F(r[1], D))
    tail = -((-tail_exact*D).__floor__())
    need('Wuthrich full two-series geometric tail', f['next_power'] == nxt and f['tail_upper'] == tail and F(tail, D) >= tail_exact)
    period = [partial[0]-tail, partial[1]+tail]
    need('strict independently oriented period enclosure', f['period_interval'] == period and period[1] < 0)
    normalization = data['normalization']
    sign = (-1 if period[1] < 0 else 1)*(-1 if phicycle < 0 else 1)
    scalar = F(sign)/(2*g)
    values = [scalar*sum(a*v for a, v in zip(phi, col)) for col in p['generator_coordinates']]
    common = 1
    for v in values:
        common = common*v.denominator//gcd(common, v.denominator)
    need('signed total-period scale, not least real projection', normalization['beta_sign'] == sign == 1
         and F(normalization['beta_over_total_period']) == scalar == F(1, 5))
    need('all 12 normalized integral generator values', list(map(F, normalization['generator_values'])) == values and len(values) == 12)
    need('all denominator primes retained', common == normalization['common_denominator'] == 10
         and normalization['denominator_primes'] == [2, 5] and normalization['C_for_p_ge_5_not_5'] == 0)
    need('all normalized source and saturated relations', mul([values], transpose(structural['A']['entries'])) == [[0]*24]
         and mul([values], K) == [[0]*9])
    need('no producer failures', data['failures'] == [])
    return {'kernel_rank_actual': 2, 'kernel_rank_required': 2, 'image': str(g),
            'primitive_image': 'Z', 'period_interval': period, 'scale': D,
            'required_orientation': 'upper endpoint < 0', 'terms_actual': nmax, 'terms_required': 64,
            'coefficients_actual': len(coeffs)-1, 'coefficients_required': 64,
            'generator_values_actual': len(values), 'generator_values_required': 12,
            'normalizing_scalar': str(scalar), 'all_generator_denominator': common,
            'tail_upper': tail, 'upstream_report': 'upstream-replay/dual-verification.json'}


if __name__ == '__main__':
    path, out = HERE/'certificate.json', HERE/'verification.json'
    checks, failures, summary = [], [], None
    try:
        summary = replay(json.loads(path.read_text()), checks)
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    report = {'certificate_sha256': sha256(path.read_bytes()).hexdigest(),
              'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
              'summary': summary, 'checks_passed': len(checks), 'checks': checks, 'failures': failures}
    out.write_text(json.dumps(report, indent=2)+'\n')
    print('Complete absolute-cycle replay:', summary, '; failures:', failures, '; report:', out)
    if failures:
        raise SystemExit(1)
