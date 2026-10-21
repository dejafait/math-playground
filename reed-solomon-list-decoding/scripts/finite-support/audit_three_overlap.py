#!/usr/bin/env python3
"""Independent full reconstruction of L033; no imports from its producer."""
import hashlib
import itertools
import json
from pathlib import Path

P = 65537
HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'three-overlap-results.json'
OUT = HERE / 'three-overlap-audit-results.json'
FAILURES = []
CHECKS = []
MATCHED_LEAVES = 0


def check(condition, label):
    CHECKS.append({'label': label, 'passed': bool(condition)})
    if not condition:
        FAILURES.append(label)


def root_coefficients(roots):
    """Newton identities, independent of repeated linear-factor multiplication."""
    n = len(roots)
    powers = [0] + [sum(pow(x, j, P) for x in roots) % P
                    for j in range(1, n + 1)]
    elementary = [1]
    for k in range(1, n + 1):
        elementary.append(sum((-1)**(j-1) * elementary[k-j] * powers[j]
                              for j in range(1, k+1)) * pow(k, -1, P) % P)
    return [(-1)**(n-i) * elementary[n-i] % P for i in range(n+1)]


def evaluate(coefficients, x):
    return sum(c * pow(x, j, P) for j, c in enumerate(coefficients)) % P


def eliminate(matrix):
    """Exact Gaussian elimination; record each elementary row operation."""
    a = [list(row) for row in matrix]
    rows, columns = len(a), len(a[0])
    rank, determinant, operations, pivots = 0, 1, [], []
    for col in range(columns):
        pivot_row = next((r for r in range(rank, rows) if a[r][col]), None)
        if pivot_row is None:
            continue
        if pivot_row != rank:
            a[rank], a[pivot_row] = a[pivot_row], a[rank]
            determinant = -determinant % P
            operations.append(['swap', rank, pivot_row])
        pivot = a[rank][col]
        determinant = determinant * pivot % P
        inverse = pow(pivot, -1, P)
        a[rank] = [v * inverse % P for v in a[rank]]
        operations.append(['scale', rank, inverse])
        for r in range(rows):
            if r != rank and a[r][col]:
                factor = a[r][col]
                a[r] = [(v - factor*w) % P for v, w in zip(a[r], a[rank])]
                operations.append(['subtract', r, rank, factor])
        pivots.append(col)
        rank += 1
        if rank == rows:
            break
    return dict(rank=rank, rref=a, pivots=pivots, operations=operations,
                determinant=(determinant if rank == rows else 0)
                if rows == columns else None)


def compare(expected, recorded, path=''):
    """Compare every type, key, list position and scalar; no preview checking."""
    global MATCHED_LEAVES
    if type(expected) is not type(recorded):
        FAILURES.append(path + ': type mismatch')
        return
    if isinstance(expected, dict):
        if expected.keys() != recorded.keys():
            FAILURES.append(path + ': key mismatch')
        for key in expected.keys() & recorded.keys():
            compare(expected[key], recorded[key], path + '/' + key)
    elif isinstance(expected, list):
        if len(expected) != len(recorded):
            FAILURES.append(path + ': length mismatch')
        for i, (a, b) in enumerate(zip(expected, recorded)):
            compare(a, b, path + '/' + str(i))
    elif expected != recorded:
        FAILURES.append(path + ': value mismatch')
    else:
        MATCHED_LEAVES += 1


def reconstruct_case(domain, triples, realized):
    name = 'realized' if realized else 'forbidden'
    flat = [x for triple in triples for x in triple]
    unused = [x for x in domain if x not in flat]
    core = unused[:60]
    private = [unused[60+2*i:62+2*i] for i in range(3)]
    parts = [core] + triples + private
    check(list(map(len, parts)) == [60, 3, 3, 3, 2, 2, 2], name+': part sizes')
    check(len(set(sum(parts, []))) == 75, name+': seven disjoint parts')
    check(set(sum(parts, [])) <= set(domain), name+': all parts in H')
    supports = [core+triples[0]+triples[2]+private[0],
                core+triples[0]+triples[1]+private[1],
                core+triples[1]+triples[2]+private[2]]
    sets = list(map(set, supports))
    check(all(len(s) == 68 for s in sets), name+': support sizes')
    check(set.intersection(*sets) == set(core), name+': triple intersection')
    pairs = [(0, 1), (1, 2), (2, 0)]
    check(all(sets[i] & sets[j] == set(core + triple)
              for (i, j), triple in zip(pairs, triples)), name+': pair intersections')
    cubics = [root_coefficients(t) for t in triples]
    check(all(evaluate(cubic, x) == 0 for cubic, triple in zip(cubics, triples)
              for x in triple), name+': cubic roots')
    matrix = [list(row) for row in zip(*cubics)]
    elimination = eliminate(matrix)
    minor_certificates = [{'rows': list(rows), 'elimination': eliminate([matrix[i] for i in rows])}
                          for rows in itertools.combinations(range(4), 3)]
    minors = [{'rows': c['rows'], 'value': c['elimination']['determinant']}
              for c in minor_certificates]
    pair_ranks = [eliminate([[row[i], row[j]] for row in matrix])['rank']
                  for i, j in itertools.combinations(range(3), 2)]
    check(pair_ranks == [2, 2, 2], name+': pairwise column independence')
    check(elimination['rank'] == (2 if realized else 3), name+': required rank')
    check(all(m['value'] == 0 for m in minors) if realized else
          all(m['value'] != 0 for m in minors), name+': all four maximal minors')
    small = dict(triples=triples, subgroup_membership_powers=[pow(x, 1024, P) for x in flat],
                 cubics=cubics, matrix=matrix, minors=minors, rank=elimination['rank'])
    result = dict(small=small, core=core, private=private, supports=supports)
    audit = dict(matrix_elimination=elimination, minor_certificates=minor_certificates,
                 pair_ranks=pair_ranks)
    if realized:
        d = [f[0] for f in cubics]
        z = [(d[1]-d[2]) % P, (d[2]-d[0]) % P, (d[0]-d[1]) % P]
        check(all(z), 'realized: three distinctions in kernel')
        check(all(sum(v*w for v, w in zip(row, z)) % P == 0 for row in matrix),
              'realized: all four kernel equations')
        check(elimination['pivots'] == [0, 1], 'realized: first two pivot columns')
        normalized = [(-elimination['rref'][0][2]) % P,
                      (-elimination['rref'][1][2]) % P, 1]
        check([v*z[2] % P for v in normalized] == z, 'realized: independently solved kernel')
        G = root_coefficients(core)
        f = [[0], [(-z[0]*c) % P for c in root_coefficients(core+triples[0])],
             [(z[2]*c) % P for c in root_coefficients(core+triples[2])]]
        degrees = [max((j for j, c in enumerate(poly) if c), default=-1) for poly in f]
        check(degrees == [-1, 63, 63], 'realized: strict message degrees')
        differences = []
        for edge, (i, j) in enumerate(pairs):
            difference = [((f[i][k] if k < len(f[i]) else 0) -
                           (f[j][k] if k < len(f[j]) else 0)) % P for k in range(64)]
            check(difference == [z[edge]*c % P for c in root_coefficients(core+triples[edge])],
                  'realized: full cyclic polynomial identity '+str(edge))
            differences.append(difference)
        values = [[evaluate(poly, x) for x in domain] for poly in f]
        center = []
        compatibility = []
        for pos, x in enumerate(domain):
            prescribed = [values[i][pos] for i in range(3) if x in sets[i]]
            compatibility.append(len(set(prescribed)) <= 1)
            center.append(prescribed[0] if prescribed else 0)
        check(all(compatibility), 'realized: all 1024 center prescriptions compatible')
        agreements = [[x for pos, x in enumerate(domain) if values[i][pos] == center[pos]]
                      for i in range(3)]
        equalities = [[x for pos, x in enumerate(domain) if values[i][pos] == values[j][pos]]
                      for i, j in pairs]
        check(all(sets[i] <= set(agreements[i]) for i in range(3)), 'realized: selected agreements')
        check(all(set(eq) == set(core+triple) for eq, triple in zip(equalities, triples)),
              'realized: full pair equality sets')
        check(list(map(len, agreements)) == [1017, 68, 68], 'realized: full agreement counts')
        check(all(values[i] != values[j] for i, j in pairs), 'realized: distinct evaluated codewords')
        small.update(kernel=z, agreement_counts=list(map(len, agreements)),
                     pair_equality_counts=list(map(len, equalities)), message_degrees=degrees)
        result.update(core_polynomial=G, messages=f, message_evaluations=values,
                      center=center, full_agreements=agreements, pair_equalities=equalities)
        audit.update(normalized_kernel=normalized, cyclic_differences=differences,
                     pointwise_center_compatibility=compatibility)
    else:
        h = domain[1]
        A, B = (1+h+h*h) % P, (h+h*h+h**3) % P
        xs = [1, pow(h, 3, P), pow(h, 6, P)]
        vandermonde = -A*B
        for i, j in itertools.combinations(range(3), 2):
            vandermonde = vandermonde*(xs[j]-xs[i]) % P
        check(A != 0 and B != 0 and len(set(xs)) == 3, 'forbidden: Vandermonde factors nonzero')
        check((h-1)*A % P == (pow(h, 3, P)-1) % P, 'forbidden: geometric-sum identity')
        check(cubics == [[-pow(h, 3, P)*pow(x, 3, P) % P, B*x*x % P, -A*x % P, 1]
                          for x in xs], 'forbidden: scaled-triple cubic formula')
        descending = eliminate([matrix[i] for i in [3, 2, 1]])['determinant']
        check(descending == vandermonde == -minors[-1]['value'] % P,
              'forbidden: Vandermonde value and opposite row orientation')
        audit.update(A=A, B=B, xs=xs, descending_minor=descending,
                     vandermonde_product=vandermonde)
    return result, audit


def main():
    raw = SOURCE.read_bytes()
    old = json.loads(raw)
    check(all(P % d for d in range(2, 257)), 'prime characteristic trial divisors through sqrt')
    h = pow(3, 64, P)
    check(h == 19139 and pow(h, 1024, P) == 1 and pow(h, 512, P) == P-1,
          'generator has exact order 1024')
    domain = [1]
    for _ in range(1023):
        domain.append(domain[-1]*h % P)
    roots = [x for x in range(P) if pow(x, 1024, P) == 1]
    check(len(set(domain)) == 1024 and set(domain) == set(roots), 'entire subgroup equals all roots in E')
    realized = [[1, 25417, 40120], [8306, 27221, 30011], [14177, 16349, 35012]]
    forbidden = [[domain[3*r+j] for j in range(3)] for r in range(3)]
    cases, audit_cases = {}, {}
    for name, triples, real in [('realized', realized, True), ('forbidden', forbidden, False)]:
        cases[name], audit_cases[name] = reconstruct_case(domain, triples, real)
    reconstructed = dict(field=P, generator=h, domain=domain, cases=cases, failures=[],
                         required_agreements=68, established_list_lower_bound=3,
                         threshold_numerator=P**28, threshold_denominator=2**128)
    compare(reconstructed, old)
    check(3*2**128 < P**28, 'three-message witness is strictly below unsafe threshold')
    certificate = dict(source='scripts/finite-support/three-overlap-results.json',
                       source_sha256=hashlib.sha256(raw).hexdigest(),
                       reconstruction_method='Newton identities; Gaussian elimination; direct power-sum evaluation',
                       matched_scalar_leaves=MATCHED_LEAVES, checks=CHECKS,
                       full_reconstruction=reconstructed, audit_cases=audit_cases,
                       summary=dict(ranks={n: c['small']['rank'] for n, c in cases.items()},
                                    all_minor_values={n: [v['value'] for v in c['small']['minors']]
                                                      for n, c in cases.items()},
                                    actual_agreements=cases['realized']['small']['agreement_counts'],
                                    required_agreements=68, achieved_list=3,
                                    unsafe_requires='list > 65537^28 / 2^128'),
                       failures=FAILURES)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Ranks: realized='+str(cases['realized']['small']['rank'])+
          ' (required 2), forbidden='+str(cases['forbidden']['small']['rank'])+' (required 3).')
    print('All source scalar leaves compared: '+str(MATCHED_LEAVES))
    print('Actual agreements='+str(certificate['summary']['actual_agreements'])+'; required=68.')
    print('Achieved list=3; unsafe requires >65537^28/2^128; no boundary improvement.')
    print('Checks='+str(len(CHECKS))+'; failures='+str(FAILURES))
    print('Full certificate: scripts/finite-support/'+OUT.name)
    if FAILURES:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
