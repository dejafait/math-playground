#!/usr/bin/env python3
"""Full integral intersection and relative-factor certificate; analytic input L031.

Run from notebook root, then --verify to replay saved evidence.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from projected_container_homothety import identity, kernel, mul, serialize, smith, triangular_solve, val

BASE = Path(__file__).resolve().parent
SOURCE = BASE / 'enlarged-basis.json'
M_SOURCE = BASE / 'projected-container-homothety.json'
OUT = BASE / 'projected-envelope-span.json'
VERIFICATION = BASE / 'projected-envelope-span-verification.json'


def pi_times(b):
    out = [[0]*108 for _ in range(108)]
    for r in range(27):
        for a in range(4):
            out[4*((r+1) % 27)+a] = [x*(3 if r == 26 else 1) for x in b[4*r+a]]
    return out


def build():
    b = json.loads(SOURCE.read_text())['integer_basis_matrix']
    md = json.loads(M_SOURCE.read_text())
    pb = pi_times(b)
    tau = [4, -1, -1, -1]+[0]*104
    t = mul([tau], pb)[0]
    a, ai, g = kernel(t)
    tb54 = mul(pb, [row[1:] for row in a])
    jc = triangular_solve(b, [[Q(x, 6) for x in row] for row in tb54])
    coords = mul(md['inverse_kernel_transform'], jc)
    assert not any(coords[0])
    r = coords[1:]
    diagonal, ops = smith(r)
    exponents = [val(x) for x in diagonal]
    return serialize(dict(
        source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        M_source_sha256=hashlib.sha256(M_SOURCE.read_bytes()).hexdigest(),
        trace_row_divided_by_27=tau, pi_times_integer_basis=pb,
        trace_on_pi_integer_basis=t, kernel_transform=a,
        inverse_kernel_transform=ai, trace_gcd=g, T_basis_times_54=tb54,
        M_basis_times_9=md['M_basis_times_9'], relative_T_in_M=r,
        smith_operations=ops, smith_diagonal=diagonal,
        smith_exponents=exponents,
        exponent_multiplicities={str(e): n for e, n in sorted(Counter(exponents).items())},
        projected_minimum_interval=exponents[:2],
        uniform_projected_minimum=exponents[0] if exponents[0] == exponents[1] else None))


def verify(d):
    checks = {}
    def check(name, ok):
        checks[name] = bool(ok)
    b = json.loads(SOURCE.read_text())['integer_basis_matrix']
    md = json.loads(M_SOURCE.read_text())
    check('pinned_complete_J', d['source_sha256'] == hashlib.sha256(SOURCE.read_bytes()).hexdigest())
    check('pinned_complete_M', d['M_source_sha256'] == hashlib.sha256(M_SOURCE.read_bytes()).hexdigest())
    pb = pi_times(b)
    check('all_pi_multiplication_entries', pb == d['pi_times_integer_basis'])
    a, ai = d['kernel_transform'], d['inverse_kernel_transform']
    check('full_integer_kernel_shapes', all(len(m) == 108 and all(len(row) == 108 for row in m)
          and all(type(x) is int for row in m for x in row) for m in (a, ai)))
    check('both_unimodular_inverse_identities', mul(a, ai) == identity(108) and mul(ai, a) == identity(108))
    tau = [4, -1, -1, -1]+[0]*104
    t = mul([tau], pb)[0]
    check('full_trace_kernel', d['trace_row_divided_by_27'] == tau and
          t == d['trace_on_pi_integer_basis'] and d['trace_gcd'] != 0 and
          mul([t], a)[0] == [d['trace_gcd']]+[0]*107)
    tb = mul(pb, [row[1:] for row in a])
    check('full_T_basis', tb == d['T_basis_times_54'])
    mb = md['M_basis_times_9']
    check('full_M_basis', mb == d['M_basis_times_9'])
    r = [[Q(x) for x in row] for row in d['relative_T_in_M']]
    check('relative_matrix_shape', len(r) == 107 and all(len(row) == 107 for row in r))
    check('all_relative_identity_entries', mul(mb, r) == [[Q(x, 6) for x in row] for row in tb])
    rr = [row[:] for row in r]
    integral = True
    for op in d['smith_operations']:
        kind, i, j, *rest = op
        integral &= 0 <= i < 107 and 0 <= j < 107 and i != j
        if kind in ('swap_row', 'swap_col'):
            integral &= not rest
            if kind == 'swap_row':
                rr[i], rr[j] = rr[j], rr[i]
            else:
                for row in rr:
                    row[i], row[j] = row[j], row[i]
        elif kind in ('add_row', 'add_col'):
            integral &= len(rest) == 1
            q = Q(rest[0])
            integral &= val(q) is None or val(q) >= 0
            if kind == 'add_row':
                rr[i] = [x+q*y for x, y in zip(rr[i], rr[j])]
            else:
                for row in rr:
                    row[i] += q*row[j]
        else:
            raise ValueError(kind)
    diagonal = list(map(Q, d['smith_diagonal']))
    check('all_operations_Z3_invertible', integral)
    check('complete_diagonal_identity', rr == [[diagonal[i] if i == j else Q(0)
          for j in range(107)] for i in range(107)])
    exponents = [val(x) for x in diagonal]
    check('107_nonzero_ordered_factors', len(exponents) == 107 and None not in exponents
          and exponents == sorted(exponents) == d['smith_exponents'])
    check('full_multiplicities', d['exponent_multiplicities'] ==
          {str(e): n for e, n in sorted(Counter(exponents).items())})
    check('quotient_minimum_interval', d['projected_minimum_interval'] == exponents[:2])
    check('uniform_minimum_verdict', d['uniform_projected_minimum'] ==
          (exponents[0] if exponents[0] == exponents[1] else None))
    failures = [name for name, ok in checks.items() if not ok]
    VERIFICATION.write_text(json.dumps(dict(checks=checks, failures=failures,
        exponent_multiplicities=d['exponent_multiplicities'],
        projected_minimum_interval=exponents[:2],
        uniform_projected_minimum=d['uniform_projected_minimum']), indent=2)+'\n')
    print(json.dumps(dict(failures=failures, exponent_multiplicities=d['exponent_multiplicities'],
        actual_projected_minimum_interval=exponents[:2],
        required_for_uniformity='equal first two exponents',
        certificate=str(OUT.relative_to(BASE.parents[1])),
        verification=str(VERIFICATION.relative_to(BASE.parents[1])))))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify', action='store_true')
    args = parser.parse_args()
    if not args.verify:
        OUT.write_text(json.dumps(build(), indent=2)+'\n')
    verify(json.loads(OUT.read_text()))
