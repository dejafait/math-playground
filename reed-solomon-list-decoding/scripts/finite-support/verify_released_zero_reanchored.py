#!/usr/bin/env python3
"""Read and check every saved matrix/minor by closed Schur formulas.

Does not import the constructor or reuse its determinant routine.
This arithmetic verification is not a separate critical proof review.
"""
import hashlib
import itertools
import json
import re
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NOTEBOOK = ROOT.parent.parent
SOURCE = ROOT / 'released-zero-reanchored-results.json'
OUT = ROOT / 'released-zero-reanchored-verification.json'


def enc(z):
    z = Q(z)
    return [z.numerator, z.denominator]


def main():
    saved = json.loads(SOURCE.read_text())
    manuscript = (NOTEBOOK / 'lemmas/L056-released-zero-five-shell-nonexclusion.md').read_text()
    z = {(int(r), int(q)): Q(value) for r, q, value in
         re.findall(r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$', manuscript, re.M)}
    lp = json.loads((ROOT / 'delsarte-lp-results.json').read_text())
    p = [Q(1)] + [Q(0)]*4 + [Q(v['numerator'], v['denominator']) /
        (2*comb(68, i)*comb(956, i)) for i, v in zip(range(5, 69), lp['exact']['primal'])]
    failures, checks, minor_count = [], 0, 0

    def check(name, condition, detail=None):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append({'check': name, 'detail': detail})

    def verify_matrix(record, expected, tag):
        nonlocal minor_count
        check('matrix', record['matrix_over_rho'] == [[enc(v) for v in row] for row in expected], tag)
        # Complete closed formulas, with the 3x3 determinant given by Schur.
        if len(expected) == 1:
            values = {(0,): Q(1)}
        elif len(expected) == 2:
            b = expected[0][1]
            values = {(0,): Q(1), (1,): b, (0, 1): b*(1-b)}
        else:
            a, b, c = expected[0][1], expected[0][2], expected[1][2]
            values = {(0,): Q(1), (1,): a, (2,): b,
                      (0, 1): a*(1-a), (0, 2): b*(1-b), (1, 2): a*b-c*c,
                      (0, 1, 2): a*(1-a)*b*(1-b)-(c-a*b)**2}
        minors = record['principal_minors_over_rho']
        check('all_minor_subsets', {tuple(m['indices']) for m in minors} == set(values)
              and len(minors) == len(values), tag)
        for m in minors:
            value = values[tuple(m['indices'])]
            check('minor_value', m['value'] == enc(value), [tag, m['indices']])
            check('minor_nonnegative', value >= 0, [tag, m['indices']])
            if 'sign' in m:
                check('minor_sign', m['sign'] == (value > 0)-(value < 0), [tag, m['indices']])
            minor_count += 1

    check('pairs', saved['normalization']['p'] == list(map(enc, p)))
    rho = (Q(comb(1024, 64), comb(68, 64))+1)/(2*comb(1024, 68))
    check('rho', saved['normalization']['rho'] == enc(rho) and rho > 0)
    check('relations', [r['relation'] for r in saved['records']] ==
          [[r, q] for r in range(6) for q in range(6)])
    for record in saved['records']:
        r, q = record['relation']
        y = (p[5] if r == q == 0 else p[5]*z.get((r, q), Q(0)) /
             (comb(5, r)*comb(63, r)*comb(5, q)*comb(951, q)))
        check('triple', record['triple_over_rho'] == enc(y), [r, q])
        check('all_permutations', [m['order'] for m in record['matrices']] ==
              [list(o) for o in itertools.permutations(range(3))], [r, q])
        pair_dist = {(0, 1): 5, (0, 2): 5, (1, 2): r+q}
        for m in record['matrices']:
            a, b, c = m['order']
            dist = [pair_dist[tuple(sorted(pair))] for pair in ((a, b), (a, c), (b, c))]
            check('distances', m['distances'] == dist, [r, q, m['order']])
            expected = [[Q(1), p[5]], [p[5], p[5]]] if r == q == 0 else [
                [Q(1), p[dist[0]], p[dist[1]]],
                [p[dist[0]], p[dist[0]], y], [p[dist[1]], y, p[dist[1]]]]
            verify_matrix(m, expected, [r, q, m['order']])
    check('Boolean_distances', sorted(set(m['distance'] for m in saved['Boolean_closure'])) == list(range(11)))
    check('Boolean_count', len(saved['Boolean_closure']) == 31)
    for m in saved['Boolean_closure']:
        b = p[m['distance']]
        expected = [[Q(1)]] if m['distance'] == 0 else [[Q(1), b], [b, b]]
        verify_matrix(m, expected, ['Boolean', m['distance'], m['equality_pattern']])
    check('full_minor_count', minor_count == 1579)
    check('constructor_input_errors', saved['input_errors'] == [])
    report = {'certificate_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'checks': checks, 'minors_verified': minor_count,
              'failures': failures, 'verified': not failures}
    OUT.write_text(json.dumps(report, separators=(',', ':'))+'\n')
    print('Full exact serialized-minor verification:', minor_count, '/1579;', checks, 'checks')
    print('Failures:', len(failures), '; verified:', report['verified'], '; report:', OUT)
    assert not failures, failures


if __name__ == '__main__':
    main()
