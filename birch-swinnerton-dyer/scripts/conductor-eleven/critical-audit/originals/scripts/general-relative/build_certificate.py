#!/usr/bin/env python3
"""L038 structural witnesses only; exact positive N and finite good-prime P.

Run from the notebook root. Standard inputs/qualifications: canonical L038.
No elliptic arithmetic, eigenline, normalization or BSD assertion.
"""
import argparse
import json
from math import gcd, isqrt, prod
from pathlib import Path


def matrix(rows, cols, entries=None):
    a = entries if entries is not None else [[0]*cols for _ in range(rows)]
    assert len(a) == rows and all(len(row) == cols for row in a)
    assert all(type(x) is int for row in a for x in row)
    return {'rows': rows, 'cols': cols, 'entries': a}


def eye(n):
    return matrix(n, n, [[int(i == j) for j in range(n)] for i in range(n)])


def transpose(a):
    return matrix(a['cols'], a['rows'],
                  [[a['entries'][i][j] for i in range(a['rows'])]
                   for j in range(a['cols'])])


def mul(a, b):
    assert a['cols'] == b['rows']
    return matrix(a['rows'], b['cols'],
                  [[sum(a['entries'][i][k]*b['entries'][k][j]
                        for k in range(a['cols'])) for j in range(b['cols'])]
                   for i in range(a['rows'])])


def add(a, b):
    assert (a['rows'], a['cols']) == (b['rows'], b['cols'])
    return matrix(a['rows'], a['cols'],
                  [[a['entries'][i][j]+b['entries'][i][j]
                    for j in range(a['cols'])] for i in range(a['rows'])])


def rowop(a, op):
    typ, i, j, *tail = op
    rows = a['entries']
    if typ == 'swap':
        rows[i], rows[j] = rows[j], rows[i]
    elif typ == 'add':
        rows[i] = [rows[i][k]+tail[0]*rows[j][k] for k in range(a['cols'])]
    else:
        assert typ == 'neg' and i == j
        rows[i] = [-v for v in rows[i]]


def colop(a, op):
    typ, i, j, *tail = op
    for row in a['entries']:
        if typ == 'swap':
            row[i], row[j] = row[j], row[i]
        elif typ == 'add':
            row[i] += tail[0]*row[j]
        else:
            assert typ == 'neg' and i == j
            row[i] = -row[i]


def inverse(op):
    return op[:3]+[-op[3]] if op[0] == 'add' else op[:]


def diagonalize(a):
    b = matrix(a['rows'], a['cols'], [row[:] for row in a['entries']])
    n, m = b['rows'], b['cols']
    rops, cops = [], []

    def rr(op):
        rowop(b, op)
        rops.append(op)

    def cc(op):
        colop(b, op)
        cops.append(op)

    k = 0
    while k < min(n, m):
        candidates = [(abs(b['entries'][i][j]), i, j)
                      for i in range(k, n) for j in range(k, m)
                      if b['entries'][i][j]]
        if not candidates:
            break
        _, i, j = min(candidates)
        if i != k:
            rr(['swap', k, i])
        if j != k:
            cc(['swap', k, j])
        while True:
            restart = False
            for i in range(k+1, n):
                if b['entries'][i][k]:
                    q = b['entries'][i][k]//b['entries'][k][k]
                    if q:
                        rr(['add', i, k, -q])
                    if b['entries'][i][k]:
                        rr(['swap', k, i])
                        restart = True
                        break
            if restart:
                continue
            for j in range(k+1, m):
                if b['entries'][k][j]:
                    q = b['entries'][k][j]//b['entries'][k][k]
                    if q:
                        cc(['add', j, k, -q])
                    if b['entries'][k][j]:
                        cc(['swap', k, j])
                        restart = True
                        break
            if not restart:
                break
        if b['entries'][k][k] < 0:
            rr(['neg', k, k])
        k += 1
    u, ui, w, wi = eye(n), eye(n), eye(m), eye(m)
    for op in rops:
        rowop(u, op)
    for op in reversed(rops):
        rowop(ui, inverse(op))
    for op in cops:
        colop(w, op)
    for op in reversed(cops):
        colop(wi, inverse(op))
    assert mul(mul(u, a), w) == b
    assert mul(u, ui) == mul(ui, u) == eye(n)
    assert mul(w, wi) == mul(wi, w) == eye(m)
    return k, b, rops, cops, u, ui, w, wi


def mm(a, b):
    return [a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]]


def egcd(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a//b
        a, b = b, a-q*b
        x, xx, y, yy = xx, x-q*xx, yy, y-q*yy
    assert a == 1
    return x, y


def lift(pair, n):
    c0, d0 = pair
    c = c0 or n
    factors, rest = [], c
    q = 2
    while q*q <= rest:
        if rest % q == 0:
            factors.append(q)
            while rest % q == 0:
                rest //= q
        q += 1
    if rest > 1:
        factors.append(rest)
    k, modulus = 0, 1
    for q in factors:
        if n % q:
            excluded = -d0*pow(n, -1, q) % q
            allowed = int(excluded == 0)
            k += modulus*((allowed-k)*pow(modulus, -1, q) % q)
            modulus *= q
    d = d0+k*n
    x, y = egcd(c, d)
    return [y, -x, c, d]


def cusp(p, q):
    assert p or q
    if q == 0:
        return [1, 0]
    h = gcd(p, q)
    p, q = p//h, q//h
    return [p, q] if q > 0 else [-p, -q]


def transform(a, point):
    p, q = point
    return cusp(a[0]*p+a[1]*q, a[2]*p+a[3]*q)


def prime(p):
    return p >= 2 and all(p % q for q in range(2, isqrt(p)+1))


def build(n, primes):
    if type(n) is not int or n <= 0:
        raise ValueError('N must be a positive integer')
    if len(primes) != len(set(primes)) or any(type(p) is not int or not prime(p)
                                            or n % p == 0 for p in primes):
        raise ValueError('P must be a finite set of good primes')
    primes = sorted(primes)
    assignments, reps, units, lookup_table = [], [], [], {}
    if n == 1:
        reps, lifts = [[0, 0]], [[1, 0, 0, 1]]
    else:
        units = [u for u in range(n) if gcd(u, n) == 1]
        for c in range(n):
            for d in range(n):
                if gcd(gcd(c, d), n) != 1:
                    continue
                pair = (c, d)
                if pair not in lookup_table:
                    i = len(reps)
                    reps.append([c, d])
                    for u in units:
                        lookup_table[(u*c % n, u*d % n)] = (i, u)
                i, u = lookup_table[pair]
                assignments.append({'pair': [c, d], 'coset': i, 'unit': u})
        lifts = [lift(p, n) for p in reps]
    s = len(reps)

    def lookup(h):
        residue = [h[2] % n, h[3] % n]
        i, u = (0, 0) if n == 1 else lookup_table[tuple(residue)]
        a, b, c, d = lifts[i]
        gamma = mm(h, [d, -b, -c, a])
        assert gamma[0]*gamma[3]-gamma[1]*gamma[2] == 1 and gamma[2] % n == 0
        return {'h': h, 'residue': residue, 'coset': i, 'unit': u, 'gamma': gamma}

    S, R = [0, -1, 1, 0], [1, -1, 1, 0]
    actions, rows = [], []
    for i, g in enumerate(lifts):
        witnesses = [lookup(mm(g, h)) for h in (S, R, mm(R, R))]
        actions.append(witnesses)
        for indices in ([i, witnesses[0]['coset']],
                        [i, witnesses[1]['coset'], witnesses[2]['coset']]):
            row = [0]*s
            for j in indices:
                row[j] += 1
            rows.append(row)
    A = matrix(2*s, s, rows)
    r, D, rops, cops, U, Ui, W, Wi = diagonalize(A)
    d = s-r
    Wt, Wit = transpose(W), transpose(Wi)
    K = matrix(s, r, [row[:r] for row in Wit['entries']])
    Q = matrix(s, d, [row[r:] for row in Wit['entries']])
    Pi = matrix(d, s, Wt['entries'][r:])
    head = matrix(r, s, Wt['entries'][:r])
    assert mul(Pi, Q) == eye(d)
    assert mul(Pi, K) == matrix(d, r)
    assert mul(Pi, transpose(A)) == matrix(d, 2*s)
    assert add(mul(K, head), mul(Q, Pi)) == eye(s)
    coordinates = [[Pi['entries'][j][i] for j in range(d)] for i in range(s)]

    def chain(target):
        p, q = target
        terms, segments = [], []
        if q == 0:
            return {'target': target, 'terms': terms, 'segments': segments}
        a, b = p, q
        while b:
            t = a//b
            terms.append(t)
            a, b = b, a-t*b
        pm2, qm2, pm1, qm1 = 0, 1, 1, 0
        for t in terms:
            pp, qq = t*pm1+pm2, t*qm1+qm2
            det = pp*qm1-pm1*qq
            assert abs(det) == 1
            h = [det*pp, pm1, det*qq, qm1]
            segments.append({'start': cusp(pm1, qm1), 'end': cusp(pp, qq),
                             'lookup': lookup(h)})
            pm2, qm2, pm1, qm1 = pm1, qm1, pp, qq
        assert cusp(pm1, qm1) == target
        return {'target': target, 'terms': terms, 'segments': segments}

    def path(start, end):
        first, last = chain(start), chain(end)
        raw = [0]*s
        for sign, ch in ((-1, first), (1, last)):
            for seg in ch['segments']:
                raw[seg['lookup']['coset']] += sign
        coord = [sum(Pi['entries'][j][i]*raw[i] for i in range(s)) for j in range(d)]
        return {'start': start, 'end': end, 'start_chain': first,
                'end_chain': last, 'raw': raw, 'coordinates': coord}

    endpoints = [[cusp(g[1], g[3]), cusp(g[0], g[2])] for g in lifts]
    base = [path(*pair) for pair in endpoints]
    assert [p['coordinates'] for p in base] == coordinates
    operators = {}
    maps = {'J': [[-1, 0, 0, 1]]}
    for p in primes:
        maps['T'+str(p)] = [[p, 0, 0, 1]]+[[1, t, 0, p] for t in range(p)]
    for name, transforms in maps.items():
        paths = [[path(transform(h, a), transform(h, b)) for h in transforms]
                 for a, b in endpoints]
        raw_columns = [[sum(term['raw'][j] for term in terms) for j in range(s)]
                       for terms in paths]
        Z = transpose(matrix(s, s, raw_columns))
        Y = mul(Pi, Z)
        source_images, saturated_images = mul(Y, transpose(A)), mul(Y, K)
        B = mul(Y, Q)
        assert source_images == matrix(d, 2*s)
        assert saturated_images == matrix(d, r)
        assert mul(B, Pi) == Y
        operators[name] = {'endpoint_maps': transforms, 'paths': paths, 'Z': Z,
                           'Y': Y, 'source_images': source_images,
                           'saturated_images': saturated_images, 'B': B}
    assert mul(operators['J']['B'], operators['J']['B']) == eye(d)
    for p in primes:
        j, h = operators['J']['B'], operators['T'+str(p)]['B']
        assert mul(j, h) == mul(h, j)
    diag = [D['entries'][i][i] for i in range(r)]
    return {'schema': 'L038-relative-v1', 'inputs': {'N': n, 'P': primes},
            'cosets': {'representatives': reps, 'units': units,
                       'assignments': assignments, 'lifts': lifts},
            'relation_convention': {'S': S, 'R3': R}, 'actions': actions, 'A': A,
            'presentation': {'s': s, 'r': r, 'd': d, 'D': D, 'diagonal': diag,
                             'row_operations': rops, 'column_operations': cops,
                             'U': U, 'U_inverse': Ui, 'W': W, 'W_inverse': Wi,
                             'K': K, 'Q': Q, 'Pi': Pi, 'head': head,
                             'generator_coordinates': coordinates,
                             'removed_torsion_order': prod(diag)},
            'endpoints': endpoints, 'basepaths': base, 'operators': operators}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--level', type=int, required=True)
    parser.add_argument('--primes', type=int, nargs='*', default=[])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    try:
        cert = build(args.level, args.primes)
        args.out.write_text(json.dumps(cert, indent=2)+'\n')
    except Exception as error:
        args.out.with_suffix('.build-failure.json').write_text(json.dumps(
            {'inputs': {'N': args.level, 'P': args.primes},
             'failures': [type(error).__name__+': '+str(error)]}, indent=2)+'\n')
        raise
    pr = cert['presentation']
    print(f"built N={args.level}, P={cert['inputs']['P']}: s={pr['s']} r={pr['r']} "
          f"d={pr['d']}; removed torsion={pr['removed_torsion_order']}; "
          f"artifact={args.out}")


if __name__ == '__main__':
    main()
