#!/usr/bin/env python3
"""Independent exhaustive L038 replay; never imports the builder.

Matrix shapes survive empty rows/columns. Paths are checked geometrically,
not by sharing or trusting the builder's continued-fraction algorithm.
Failures and partial check counts are persisted even when replay aborts.
"""
import argparse
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path


class ReplayError(Exception):
    pass


class Checker:
    def __init__(self):
        self.checks = []
        self.counts = {'orbit_assignments': 0, 'cosets': 0, 'relations': 0,
                       'relation_lookups': 0, 'paths': 0, 'segments': 0,
                       'row_operations': 0, 'column_operations': 0,
                       'inverse_row_operations': 0, 'inverse_column_operations': 0,
                       'source_relation_images': 0, 'saturated_kernel_images': 0,
                       'reconstructed_generator_images': 0}
        self.required = {}
        self.context = 'startup'

    def check(self, name, condition):
        label = self.context+': '+name
        if not condition:
            raise ReplayError(label)
        self.checks.append(label)

    def integer(self, x):
        self.check('strict integer', type(x) is int)
        return x

    def vector(self, x, length):
        self.check('vector length', type(x) is list and len(x) == length)
        for v in x:
            self.integer(v)
        return x

    def matrix(self, x, rows, cols):
        self.check('matrix schema', type(x) is dict and set(x) == {'rows', 'cols', 'entries'})
        self.integer(x['rows'])
        self.integer(x['cols'])
        self.check('explicit matrix shape', x['rows'] == rows and x['cols'] == cols)
        self.check('matrix row count', type(x['entries']) is list and len(x['entries']) == rows)
        return M(rows, cols, [self.vector(row, cols) for row in x['entries']])


class M:
    def __init__(self, nr, nc, data=None):
        self.nr, self.nc = nr, nc
        data = [[0]*nc for _ in range(nr)] if data is None else data
        if len(data) != nr or any(len(row) != nc for row in data):
            raise ReplayError('internal shape mismatch')
        self.data = tuple(tuple(row) for row in data)

    def __eq__(self, other):
        return (self.nr, self.nc, self.data) == (other.nr, other.nc, other.data)

    def t(self):
        return M(self.nc, self.nr,
                 [[self.data[i][j] for i in range(self.nr)] for j in range(self.nc)])

    def __matmul__(self, other):
        if self.nc != other.nr:
            raise ReplayError('incompatible multiplication shapes')
        out = [[0]*other.nc for _ in range(self.nr)]
        for i, row in enumerate(self.data):
            for k, x in enumerate(row):
                if x:
                    for j in range(other.nc):
                        out[i][j] += x*other.data[k][j]
        return M(self.nr, other.nc, out)

    def __add__(self, other):
        if (self.nr, self.nc) != (other.nr, other.nc):
            raise ReplayError('incompatible addition shapes')
        return M(self.nr, self.nc, [[self.data[i][j]+other.data[i][j]
                                   for j in range(self.nc)] for i in range(self.nr)])


def identity(n):
    return M(n, n, [[int(i == j) for j in range(n)] for i in range(n)])


def elementary(ch, op, n, backwards=False):
    ch.check('operation syntax', type(op) is list and len(op) in (3, 4))
    typ = op[0]
    ch.check('operation name', typ in ('swap', 'add', 'neg'))
    i, j = ch.integer(op[1]), ch.integer(op[2])
    ch.check('operation indices', 0 <= i < n and 0 <= j < n)
    ch.check('operation arity', len(op) == (4 if typ == 'add' else 3))
    ch.check('elementary operation condition', i == j if typ == 'neg' else i != j)
    entries = [list(row) for row in identity(n).data]
    if typ == 'swap':
        entries[i], entries[j] = entries[j], entries[i]
    elif typ == 'neg':
        entries[i][i] = -1
    else:
        coefficient = ch.integer(op[3])
        entries[i][j] = -coefficient if backwards else coefficient
    return M(n, n, entries)


def mat2(a, b):
    # Independent 2-by-2 product through indexed rows/columns.
    rows, cols = ((a[0], a[1]), (a[2], a[3])), ((b[0], b[2]), (b[1], b[3]))
    return [sum(rows[i][k]*cols[j][k] for k in range(2)) for i in range(2) for j in range(2)]


def normalized(p, q):
    if p == q == 0:
        raise ReplayError('zero projective cusp')
    if not q:
        return [1, 0]
    sign = 1 if q > 0 else -1
    factor = gcd(p, q)
    return [sign*p//factor, sign*q//factor]


def image(h, pt):
    return normalized(h[0]*pt[0]+h[1]*pt[1], h[2]*pt[0]+h[3]*pt[1])


def replay(ch, cert, n, primes):
    ch.check('schema', cert['schema'] == 'L038-relative-v1')
    ch.integer(cert['inputs']['N'])
    ch.vector(cert['inputs']['P'], len(primes))
    ch.check('external input binding', cert['inputs'] == {'N': n, 'P': primes})
    ch.check('input domain', n > 0 and primes == sorted(set(primes)) and
             all(p >= 2 and n % p and all(p % q for q in range(2, isqrt(p)+1)) for p in primes))
    c = cert['cosets']
    if n == 1:
        units, reps, primitive, orbit_indices = [], [[0, 0]], [], {(0, 0): 0}
    else:
        units = [u for u in range(n) if gcd(u, n) == 1]
        primitive = [(a, b) for a in range(n) for b in range(n) if gcd(gcd(a, b), n) == 1]
        unseen, reps, orbit_indices = set(primitive), [], {}
        while unseen:
            a, b = min(unseen)
            orbit = {(u*a % n, u*b % n) for u in units}
            ch.check('unit orbit free size', len(orbit) == len(units))
            ch.check('orbit domain', orbit <= unseen)
            i = len(reps)
            reps.append([a, b])
            for pair in orbit:
                orbit_indices[pair] = i
            unseen -= orbit
        ch.check('all primitive pairs partitioned', set(orbit_indices) == set(primitive))
    s = len(reps)
    ch.required.update(orbit_assignments=len(primitive), cosets=s, relations=2*s,
                       relation_lookups=3*s, paths=s*(2+sum(p+1 for p in primes)))
    ch.context = 'coset completeness'
    ch.vector(c['units'], len(units))
    ch.check('all units', c['units'] == units)
    ch.check('representative count', type(c['representatives']) is list and len(c['representatives']) == s)
    for rep in c['representatives']:
        ch.vector(rep, 2)
    ch.check('complete orbit representatives', c['representatives'] == reps)
    ch.check('assignment count', type(c['assignments']) is list and len(c['assignments']) == len(primitive))
    for assignment, pair in zip(c['assignments'], primitive):
        ch.vector(assignment['pair'], 2)
        i, u = ch.integer(assignment['coset']), ch.integer(assignment['unit'])
        ch.check('assignment complete and congruent', assignment['pair'] == list(pair) and
                 i == orbit_indices[pair] and u in units and
                 [(u*x) % n for x in reps[i]] == list(pair))
        ch.counts['orbit_assignments'] += 1
    ch.check('lift count', type(c['lifts']) is list and len(c['lifts']) == s)
    lifts = c['lifts']
    for i, h in enumerate(lifts):
        a, b, cc, dd = ch.vector(h, 4)
        ch.check('SL2 coprime lift', a*dd-b*cc == 1 and gcd(cc, dd) == 1 and
                 [cc % n, dd % n] == reps[i])
        ch.counts['cosets'] += 1
    if n == 1:
        ch.check('level one identity lift', lifts == [[1, 0, 0, 1]])

    def lookup(witness, expected_h=None):
        h = ch.vector(witness['h'], 4)
        a, b, cc, dd = h
        ch.check('lookup determinant', a*dd-b*cc == 1)
        if expected_h is not None:
            ch.check('lookup right action', h == expected_h)
        residue = [cc % n, dd % n]
        ch.vector(witness['residue'], 2)
        i, u = ch.integer(witness['coset']), ch.integer(witness['unit'])
        ch.check('lookup residue/index', witness['residue'] == residue and
                 0 <= i < s and orbit_indices.get(tuple(residue)) == i)
        ch.check('lookup unit witness', u == 0 if n == 1 else
                 u in units and [(u*x) % n for x in reps[i]] == residue)
        aa, bb, ccc, ddd = lifts[i]
        gamma = mat2(h, [ddd, -bb, -ccc, aa])
        ch.vector(witness['gamma'], 4)
        ch.check('h times inverse lift in Gamma0', witness['gamma'] == gamma and
                 gamma[0]*gamma[3]-gamma[1]*gamma[2] == 1 and gamma[2] % n == 0)
        return i

    ch.context = 'complete Manin relations'
    convention = {'S': [0, -1, 1, 0], 'R3': [1, -1, 1, 0]}
    for key in convention:
        ch.vector(cert['relation_convention'][key], 4)
    ch.check('S and R3 convention', cert['relation_convention'] == convention)
    S, R = convention['S'], convention['R3']
    ch.check('action count', type(cert['actions']) is list and len(cert['actions']) == s)
    rows = []
    for i in range(s):
        ch.check('all three lookups', type(cert['actions'][i]) is list and len(cert['actions'][i]) == 3)
        indices = [lookup(cert['actions'][i][j], mat2(lifts[i], h))
                   for j, h in enumerate((S, R, mat2(R, R)))]
        ch.counts['relation_lookups'] += 3
        for summands in ((i, indices[0]), (i, indices[1], indices[2])):
            row = [0]*s
            for index in summands:
                row[index] += 1
            rows.append(row)
            ch.counts['relations'] += 1
    A = ch.matrix(cert['A'], 2*s, s)
    ch.check('all relations including multiplicity', A == M(2*s, s, rows))
    pr = cert['presentation']
    r, d = ch.integer(pr['r']), ch.integer(pr['d'])
    ch.integer(pr['s'])
    ch.check('presentation dimensions', pr['s'] == s and 0 <= r <= s and d == s-r)
    ch.vector(pr['diagonal'], r)
    ch.check('positive nonzero pivots', all(x > 0 for x in pr['diagonal']))
    D = ch.matrix(pr['D'], 2*s, s)
    expected = M(2*s, s, [[pr['diagonal'][i] if i == j and i < r else 0
                           for j in range(s)] for i in range(2*s)])
    ch.check('entire diagonal and zero tail', D == expected)
    ch.check('operation lists', type(pr['row_operations']) is list and type(pr['column_operations']) is list)
    rops, cops = pr['row_operations'], pr['column_operations']
    ch.required.update(row_operations=len(rops), column_operations=len(cops),
                       inverse_row_operations=len(rops), inverse_column_operations=len(cops))
    ch.context = 'unimodular replay'
    work, U, W = A, identity(2*s), identity(s)
    for op in rops:
        E = elementary(ch, op, 2*s)
        work, U = E@work, E@U
        ch.counts['row_operations'] += 1
    for op in cops:
        E = elementary(ch, op, s).t()
        work, W = work@E, W@E
        ch.counts['column_operations'] += 1
    ch.check('full forward diagonal replay', work == D)
    Ui, Wi = identity(2*s), identity(s)
    for op in reversed(cops):
        E = elementary(ch, op, s, backwards=True).t()
        work, Wi = work@E, Wi@E
        ch.counts['inverse_column_operations'] += 1
    for op in reversed(rops):
        E = elementary(ch, op, 2*s, backwards=True)
        work, Ui = E@work, E@Ui
        ch.counts['inverse_row_operations'] += 1
    ch.check('full reverse relation replay', work == A)
    for key, transform in (('U', U), ('U_inverse', Ui), ('W', W), ('W_inverse', Wi)):
        ch.check(key+' reconstructed', ch.matrix(pr[key], transform.nr, transform.nc) == transform)
    ch.check('row inverse products both ways', U@Ui == Ui@U == identity(2*s))
    ch.check('column inverse products both ways', W@Wi == Wi@W == identity(s))
    ch.check('full UAW identity', U@A@W == D)
    ch.context = 'integral saturation'
    K, Q, Pi, head = (ch.matrix(pr[key], nr, nc) for key, nr, nc in
                      (('K', s, r), ('Q', s, d), ('Pi', d, s), ('head', r, s)))
    wt, wit = W.t(), Wi.t()
    ch.check('K full saturation basis', K == M(s, r, [row[:r] for row in wit.data]))
    ch.check('Q full quotient section', Q == M(s, d, [row[r:] for row in wit.data]))
    ch.check('Pi all quotient coordinates', Pi == M(d, s, wt.data[r:]))
    ch.check('head all kernel coordinates', head == M(r, s, wt.data[:r]))
    ch.check('PiQ identity', Pi@Q == identity(d))
    ch.check('PiK zero', Pi@K == M(d, r))
    ch.check('PiAt all source relations zero', Pi@A.t() == M(d, 2*s))
    ch.check('complete integral decomposition', K@head+Q@Pi == identity(s))
    ch.integer(pr['removed_torsion_order'])
    ch.check('all torsion removed', pr['removed_torsion_order'] == prod(pr['diagonal']))
    ch.check('all generator coordinate count', type(pr['generator_coordinates']) is list and
             len(pr['generator_coordinates']) == s)
    coordinates = [[Pi.data[j][i] for j in range(d)] for i in range(s)]
    for coord in pr['generator_coordinates']:
        ch.vector(coord, d)
    ch.check('every generator integral coordinates', coordinates == pr['generator_coordinates'])
    if n == 1:
        ch.check('level one audited expected case', A == M(2, 1, [[2], [3]]) and
                 (s, r, d, pr['removed_torsion_order']) == (1, 1, 0, 1))

    def check_cusp(pt):
        ch.vector(pt, 2)
        ch.check('reduced cusp with positive denominator', normalized(*pt) == pt)
        return pt

    def chain(witness, target):
        ch.check('chain target', check_cusp(witness['target']) == target)
        ch.check('segment list', type(witness['segments']) is list)
        ch.check('terms list', type(witness['terms']) is list)
        ch.vector(witness['terms'], len(witness['terms']))
        ch.check('one term per finite segment', len(witness['terms']) == len(witness['segments']))
        if target == [1, 0]:
            ch.check('infinity chain empty', witness['segments'] == [] and witness['terms'] == [])
        else:
            ch.check('finite chain nonempty', len(witness['segments']) >= 1)
        counts, previous = [0]*s, [1, 0]
        # Terms are additionally verified against the convergent recurrence;
        # geometric adjacency and telescoping alone certify the path class.
        pm2, qm2, pm1, qm1 = 0, 1, 1, 0
        for number, seg in enumerate(witness['segments']):
            start, end = check_cusp(seg['start']), check_cusp(seg['end'])
            ch.check('chain adjacency', start == previous)
            ch.check('unimodular neighboring endpoints', abs(end[0]*start[1]-start[0]*end[1]) == 1)
            i = lookup(seg['lookup'])
            h = seg['lookup']['h']
            ch.check('segment orientation and endpoints', image(h, [0, 1]) == start and image(h, [1, 0]) == end)
            term = witness['terms'][number]
            pp, qq = term*pm1+pm2, term*qm1+qm2
            ch.check('full continued fraction recurrence', normalized(pp, qq) == end)
            pm2, qm2, pm1, qm1 = pm1, qm1, pp, qq
            counts[i] += 1
            previous = end
            ch.counts['segments'] += 1
        ch.check('chain ends at target', previous == target)
        return counts

    def path(witness, start, end):
        ch.check('path endpoints', check_cusp(witness['start']) == start and check_cusp(witness['end']) == end)
        first, last = chain(witness['start_chain'], start), chain(witness['end_chain'], end)
        raw = [last[i]-first[i] for i in range(s)]
        ch.vector(witness['raw'], s)
        ch.check('complete oriented raw sum', witness['raw'] == raw)
        coord = [sum(Pi.data[j][i]*raw[i] for i in range(s)) for j in range(d)]
        ch.vector(witness['coordinates'], d)
        ch.check('all path coordinates', witness['coordinates'] == coord)
        ch.counts['paths'] += 1
        return raw, coord

    ch.context = 'original generator paths'
    endpoints = [[image(h, [0, 1]), image(h, [1, 0])] for h in lifts]
    ch.check('endpoint list length', type(cert['endpoints']) is list and len(cert['endpoints']) == s)
    for pair in cert['endpoints']:
        ch.check('endpoint pair length', type(pair) is list and len(pair) == 2)
        for pt in pair:
            check_cusp(pt)
    ch.check('all original lift endpoints', cert['endpoints'] == endpoints)
    ch.check('basepath count', type(cert['basepaths']) is list and len(cert['basepaths']) == s)
    for i in range(s):
        _, coord = path(cert['basepaths'][i], *endpoints[i])
        ch.check('original path equals generator coordinates', coord == coordinates[i])
    maps = {'J': [[-1, 0, 0, 1]]}
    for p in primes:
        maps['T'+str(p)] = [[p, 0, 0, 1]]+[[1, t, 0, p] for t in range(p)]
    ch.check('complete operator names', type(cert['operators']) is dict and set(cert['operators']) == set(maps))
    ch.required.update(source_relation_images=len(maps)*2*s,
                       saturated_kernel_images=len(maps)*r,
                       reconstructed_generator_images=len(maps)*s)
    Bs = {}
    for name, transforms in maps.items():
        ch.context = name+' entire operator'
        operator = cert['operators'][name]
        ch.check('endpoint map count', type(operator['endpoint_maps']) is list and
                 len(operator['endpoint_maps']) == len(transforms))
        for h in operator['endpoint_maps']:
            ch.vector(h, 4)
        ch.check('all required endpoint maps', operator['endpoint_maps'] == transforms)
        paths = operator['paths']
        ch.check('all generator image paths', type(paths) is list and len(paths) == s)
        columns = []
        for i in range(s):
            ch.check('all prime plus one terms', type(paths[i]) is list and len(paths[i]) == len(transforms))
            raw = [0]*s
            for term, h in enumerate(transforms):
                a, b = endpoints[i]
                values, _ = path(paths[i][term], image(h, a), image(h, b))
                for k in range(s):
                    raw[k] += values[k]
            columns.append(raw)
        Z = M(s, s, columns).t()
        ch.check('complete raw operator matrix', ch.matrix(operator['Z'], s, s) == Z)
        Y = Pi@Z
        ch.check('all generator coordinate images', ch.matrix(operator['Y'], d, s) == Y)
        source, saturated = Y@A.t(), Y@K
        ch.check('recorded source relation images', ch.matrix(operator['source_images'], d, 2*s) == source)
        ch.check('every source relation killed', source == M(d, 2*s))
        ch.counts['source_relation_images'] += 2*s
        ch.check('recorded saturated kernel images', ch.matrix(operator['saturated_images'], d, r) == saturated)
        ch.check('every saturated kernel column killed', saturated == M(d, r))
        ch.counts['saturated_kernel_images'] += r
        B = Y@Q
        ch.check('basis matrix YQ', ch.matrix(operator['B'], d, d) == B)
        ch.check('full BPi reconstruction', B@Pi == Y)
        ch.counts['reconstructed_generator_images'] += s
        Bs[name] = B
    ch.context = 'completion'
    ch.check('reflection involution supplementary', Bs['J']@Bs['J'] == identity(d))
    for p in primes:
        H, J = Bs['T'+str(p)], Bs['J']
        ch.check('reflection Hecke commute supplementary', J@H == H@J)
    for key, required in ch.required.items():
        ch.check('complete domain '+key, ch.counts[key] == required)
    return {'s': s, 'r': r, 'd': d, 'removed_torsion_order': pr['removed_torsion_order'],
            'operator_shapes': {name: [b.nr, b.nc] for name, b in Bs.items()}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('certificate', type=Path)
    parser.add_argument('--level', type=int, required=True)
    parser.add_argument('--primes', type=int, nargs='*', default=[])
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    ch, failures, summary = Checker(), [], None
    source_hash = None
    try:
        raw = args.certificate.read_bytes()
        source_hash = hashlib.sha256(raw).hexdigest()
        cert = json.loads(raw)
        summary = replay(ch, cert, args.level, sorted(args.primes))
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    report = {'certificate': str(args.certificate), 'sha256': source_hash,
              'inputs': {'N': args.level, 'P': sorted(args.primes)},
              'summary': summary, 'actual': ch.counts, 'required': ch.required,
              'checks_passed': len(ch.checks), 'checks': ch.checks, 'failures': failures}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(f"replay N={args.level}: summary={summary}; failures={len(failures)}; report={args.out}")
    for key in ch.required:
        print(f"  {key}: actual={ch.counts[key]}, required={ch.required[key]}")
    print(f"  segments: {ch.counts['segments']}; checks passed: {len(ch.checks)}")
    if failures:
        print('  '+failures[0])
        raise SystemExit(1)


if __name__ == '__main__':
    main()
