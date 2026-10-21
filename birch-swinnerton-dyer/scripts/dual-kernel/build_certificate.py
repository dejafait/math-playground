#!/usr/bin/env python3
"""Produce a finite rational witness, conditional on the structural input.
The separate checker validates structure, arithmetic provenance and all evidence.
"""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


def encode(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, list):
        return [encode(y) for y in x]
    if isinstance(x, dict):
        return {k: encode(v) for k, v in x.items()}
    return x


def mat(a, nr, nc):
    return {'rows': nr, 'cols': nc, 'entries': encode(a)}


def elimination(source, d):
    a = [[Q(x) for x in row] for row in source]
    ids, selected, pivots, ops = list(range(len(a))), [], [], []
    for j in range(d):
        k = len(pivots)
        found = next((i for i in range(k, len(a)) if a[i][j]), None)
        if found is None:
            continue
        if found != k:
            a[k], a[found] = a[found], a[k]
            ids[k], ids[found] = ids[found], ids[k]
            ops.append(['swap', k, found])
        selected.append(ids[k])
        t = 1/a[k][j]
        if t != 1:
            a[k] = [t*x for x in a[k]]
            ops.append(['scale', k, str(t)])
        for i in range(len(a)):
            if i != k and a[i][j]:
                t = -a[i][j]
                a[i] = [a[i][h]+t*a[k][h] for h in range(d)]
                ops.append(['add', i, k, str(t)])
        pivots.append(j)
    free = [j for j in range(d) if j not in pivots]
    basis = []
    for j in free:
        v = [Q(0)]*d
        v[j] = Q(1)
        for i, p in enumerate(pivots):
            v[p] = -a[i][j]
        basis.append(v)
    return a, pivots, basis, ops, selected


def determinant(a):
    a = [[Q(x) for x in row] for row in a]
    result = Q(1)
    for j in range(len(a)):
        i = next((i for i in range(j, len(a)) if a[i][j]), None)
        if i is None:
            return Q(0)
        if i != j:
            a[j], a[i] = a[i], a[j]
            result = -result
        t = a[j][j]
        result *= t
        for i in range(j+1, len(a)):
            f = a[i][j]/t
            for k in range(j+1, len(a)):
                a[i][k] -= f*a[j][k]
    return result


def build(structural, arithmetic, adapter):
    p = structural['presentation']
    primes = [e['prime'] for e in arithmetic['traces']]
    if adapter == 'L030-fixed-v1':
        d, s = p['dimension'], len(structural['projective_cosets'])
        coords = p['integral_generator_coordinates']
        matrices = {'J': structural['matrices']['J'], 'T2': structural['matrices']['H2']}
    else:
        d, s = p['d'], p['s']
        coords = p['generator_coordinates']
        matrices = {k: v['B']['entries'] for k, v in structural['operators'].items()}
    b = []
    for name, eigenvalue in [('J', 1)]+[('T'+str(e['prime']), e['trace']) for e in arithmetic['traces']]:
        h = matrices[name]
        b.extend([[Q(h[j][i])-eigenvalue*int(i == j) for j in range(d)] for i in range(d)])
    reduced, pivots, basis, ops, selected = elimination(b, d)
    line = None
    if d > 0 and len(basis) == 1:
        v = basis[0]
        rows, cols = selected, pivots
        minor = [[b[i][j] for j in cols] for i in rows]
        line = {'v': encode(v), 'residuals': encode([sum(row[k]*v[k] for k in range(d)) for row in b]),
                'minor': {'row_indices': rows, 'column_indices': cols,
                          'matrix': mat(minor, d-1, d-1), 'determinant': str(determinant(minor))}}
    values = [[sum(Q(coords[i][j])*v[j] for j in range(d)) for i in range(s)] for v in basis]
    return {'schema': 'full-relative-dual-v1',
            'structural_adapter': adapter, 'arithmetic': arithmetic,
            'domain': {'d': d, 's': s, 'P': primes, 'blocks': ['J']+['T'+str(p) for p in primes]},
            'B': mat(b, len(b), d), 'rref': mat(reduced, len(b), d),
            'row_operations': ops, 'pivots': pivots, 'rank': len(pivots), 'nullity': len(basis),
            'kernel_basis': mat(basis, len(basis), d),
            'generator_values': mat(values, len(basis), s), 'line': line,
            'result': 'LINE_WITNESS' if line is not None else 'INCONCLUSIVE',
            'qualification': 'No Neron normalization, q, coefficient or BSD claim; generic arithmetic is supplied conditional input.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--structural', type=Path, required=True)
    parser.add_argument('--arithmetic', type=Path, required=True)
    parser.add_argument('--adapter', choices=['L030-fixed-v1', 'L038-relative-v1'], required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    try:
        sr, ar = args.structural.read_bytes(), args.arithmetic.read_bytes()
        result = build(json.loads(sr), json.loads(ar), args.adapter)
        result['bindings'] = {'structural_sha256': hashlib.sha256(sr).hexdigest(),
                              'arithmetic_sha256': hashlib.sha256(ar).hexdigest()}
        args.out.write_text(json.dumps(result, separators=(',', ':'))+'\n')
        print('produced', result['result'], 'rank actual/line-required', result['rank'], '/', result['domain']['d']-1,
              'nullity actual/line-required', result['nullity'], '/1; unverified; certificate', args.out)
    except Exception as error:
        failure = args.out.with_suffix('.build-failure.json')
        failure.write_text(json.dumps({'failures': [type(error).__name__+': '+str(error)]}, indent=2)+'\n')
        print('build failure', error, 'report', failure)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
