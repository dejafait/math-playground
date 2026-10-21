#!/usr/bin/env python3
"""Exact complete trace-kernel/Smith certificate. Analytic input: L031.

Run from notebook root; --verify checks the saved complete certificate.
"""
from fractions import Fraction as Q
from pathlib import Path
import argparse
import hashlib
import json

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'enlarged-basis.json'
OUT = BASE / 'projected-container-homothety.json'

def val(x):
    x = Q(x)
    if not x:
        return None
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % 3 == 0:
        a //= 3
        v += 1
    while b % 3 == 0:
        b //= 3
        v -= 1
    return v

def identity(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]

def mul(a, b):
    cols = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col) if x and y)
             for col in cols] for row in a]

def egcd(a, b):
    r, s, u, v = a, b, 1, 0
    w, z = 0, 1
    while s:
        q = r // s
        r, s, u, v, w, z = s, r-q*s, w, z, u-q*w, v-q*z
    if r < 0:
        r, u, v = -r, -u, -v
    assert u*a + v*b == r
    return r, u, v

def kernel(t):
    n = len(t)
    a, ai, row = identity(n), identity(n), list(t)
    for j in range(1, n):
        if not row[j]:
            continue
        x, y = row[0], row[j]
        g, u, v = egcd(x, y)
        w, z = -y//g, x//g
        for r in a:
            h, k = r[0], r[j]
            r[0], r[j] = u*h+v*k, w*h+z*k
        h, k = ai[0][:], ai[j][:]
        ai[0] = [z*p-w*q for p, q in zip(h, k)]
        ai[j] = [-v*p+u*q for p, q in zip(h, k)]
        row[0], row[j] = g, 0
    assert row[0]
    return a, ai, row[0]

def triangular_solve(b, c):
    n, m = len(b), len(c[0])
    x = [[Q(0)]*m for _ in range(n)]
    for i in range(n-1, -1, -1):
        for j in range(m):
            x[i][j] = (Q(c[i][j]) - sum(b[i][k]*x[k][j]
                         for k in range(i+1, n) if b[i][k])) / b[i][i]
    return x

def smith(r):
    d = [row[:] for row in r]
    n, ops = len(d), []
    for k in range(n):
        _, i, j = min((val(d[i][j]), i, j) for i in range(k, n)
                     for j in range(k, n) if d[i][j])
        if i != k:
            d[k], d[i] = d[i], d[k]
            ops.append(['swap_row', k, i])
        if j != k:
            for row in d:
                row[k], row[j] = row[j], row[k]
            ops.append(['swap_col', k, j])
        for i in range(k+1, n):
            if d[i][k]:
                q = d[i][k]/d[k][k]
                assert val(q) >= 0
                d[i] = [x-q*y for x, y in zip(d[i], d[k])]
                ops.append(['add_row', i, k, str(-q)])
        for j in range(k+1, n):
            if d[k][j]:
                q = d[k][j]/d[k][k]
                assert val(q) >= 0
                for row in d:
                    row[j] -= q*row[k]
                ops.append(['add_col', j, k, str(-q)])
    return [d[i][i] for i in range(n)], ops

def serialize(x):
    if isinstance(x, Q):
        return str(x)
    if isinstance(x, list):
        return [serialize(v) for v in x]
    if isinstance(x, dict):
        return {k: serialize(v) for k, v in x.items()}
    return x

def build():
    b = json.loads(SOURCE.read_text())['integer_basis_matrix']
    tau = [4, -1, -1, -1]+[0]*104
    t = mul([tau], b)[0]
    a, ai, g = kernel(t)
    # Exact C basis: (e_0+4e_a), a=1,2,3, then e_4,...,e_107.
    c = [[0]*107 for _ in range(108)]
    for j in range(3):
        c[0][j], c[j+1][j] = 1, 4
    for i in range(4, 108):
        c[i][i-1] = 1
    mc = [row[1:] for row in a]
    mb9 = mul(b, mc)
    jc = triangular_solve(b, [[9*x for x in row] for row in c])
    coords = mul(ai, jc)
    assert not any(coords[0])
    r = coords[1:]
    diagonal, ops = smith(r)
    exponents = [val(x) for x in diagonal]
    assert exponents == sorted(exponents)
    return serialize(dict(source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        trace_row_divided_by_27=tau, trace_on_integer_J_basis=t,
        kernel_transform=a, inverse_kernel_transform=ai, trace_gcd=g,
        C_basis=c, M_basis_times_9=mb9, relative_C_in_M=r,
        smith_operations=ops, smith_diagonal=diagonal, smith_exponents=exponents,
        exponent_multiplicities={str(e): exponents.count(e) for e in sorted(set(exponents))},
        required_scalar_lower=exponents[-2], required_scalar_upper=exponents[1],
        scalar_interval_empty=exponents[-2] > exponents[1]))

def verify(d):
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)
    b = json.loads(SOURCE.read_text())['integer_basis_matrix']
    check('unchanged_L031_source', d['source_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest())
    a, ai = d['kernel_transform'], d['inverse_kernel_transform']
    check('complete_kernel_transform_shapes', all(len(m) == 108 and
          all(len(row) == 108 for row in m) for m in (a, ai)))
    check('integer_unimodular_kernel_transform',
          all(type(x) is int for m in (a, ai) for row in m for x in row)
          and mul(a, ai) == identity(108) and mul(ai, a) == identity(108))
    tau = [4, -1, -1, -1]+[0]*104
    check('trace_row', d['trace_row_divided_by_27'] == tau)
    t = mul([tau], b)[0]
    check('full_trace_kernel', t == d['trace_on_integer_J_basis'] and
          mul([t], a)[0] == [d['trace_gcd']]+[0]*107 and d['trace_gcd'] != 0)
    c = [[0]*107 for _ in range(108)]
    for j in range(3):
        c[0][j], c[j+1][j] = 1, 4
    for i in range(4, 108):
        c[i][i-1] = 1
    check('complete_C_basis', c == d['C_basis'] and not any(mul([tau], c)[0]))
    mb = mul(b, [row[1:] for row in a])
    r = [[Q(x) for x in row] for row in d['relative_C_in_M']]
    check('complete_relative_matrix_shape', len(r) == 107 and
          all(len(row) == 107 for row in r))
    check('complete_M_basis', mb == d['M_basis_times_9'])
    check('exact_relative_matrix', mul(mb, r) == [[9*x for x in row] for row in c])
    # Replay every recorded operation, checking each elementary operation is
    # invertible over Z_3. No builder Smith function is called here.
    rr = [row[:] for row in r]
    integral = True
    for op in d['smith_operations']:
        kind, i, j, *rest = op
        integral &= 0 <= i < 107 and 0 <= j < 107 and i != j
        if kind == 'swap_row':
            rr[i], rr[j] = rr[j], rr[i]
        elif kind == 'swap_col':
            for row in rr:
                row[i], row[j] = row[j], row[i]
        elif kind == 'add_row':
            q = Q(rest[0])
            integral &= val(q) is None or val(q) >= 0
            rr[i] = [x+q*y for x, y in zip(rr[i], rr[j])]
        elif kind == 'add_col':
            q = Q(rest[0])
            integral &= val(q) is None or val(q) >= 0
            for row in rr:
                row[i] += q*row[j]
        else:
            raise ValueError(kind)
    diagonal = list(map(Q, d['smith_diagonal']))
    check('every_Smith_operation_is_Z3_invertible', integral)
    check('full_diagonal_identity', rr == [[diagonal[i] if i == j else Q(0)
                                         for j in range(107)] for i in range(107)])
    exponents = [val(x) for x in diagonal]
    check('all_107_nonzero_ordered_factors', len(exponents) == 107 and
          None not in exponents and exponents == sorted(exponents) == d['smith_exponents'])
    check('complete_multiplicities', d['exponent_multiplicities'] ==
          {str(e): exponents.count(e) for e in sorted(set(exponents))})
    check('interlacing_required_interval', d['required_scalar_lower'] == exponents[-2]
          and d['required_scalar_upper'] == exponents[1]
          and d['scalar_interval_empty'] == (exponents[-2] > exponents[1]))
    failures = [name for name, ok in checks.items() if not ok]
    evidence = dict(checks=checks, failures=failures, required_scalar_lower=exponents[-2],
                    required_scalar_upper=exponents[1], exponents=exponents)
    path = BASE / 'projected-container-homothety-verification.json'
    path.write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps(dict(failures=failures, exponent_multiplicities=d['exponent_multiplicities'],
          required_scalar_lower=exponents[-2], required_scalar_upper=exponents[1],
          certificate=str(OUT.relative_to(BASE.parents[1])),
          verification=str(path.relative_to(BASE.parents[1])))))
    if failures:
        raise SystemExit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    if not args.verify:
        OUT.write_text(json.dumps(build(), indent=2)+'\n')
    verify(json.loads(OUT.read_text()))
