#!/usr/bin/env python3
"""Independent L036 saved-certificate audit; no builder imports.

Every matrix entry and elementary operation is checked over Q. The analytic
identification of the pinned logarithm basis remains audited L031.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'projected-envelope-independent-audit.json'
PIN = 'ad5ea1741a5cc54d5413ab679fd4fba387e8a2aafc8d9c7c2b6d31e799159102'
report = {'checks': {}, 'failures': [], 'operation_checks': []}


def check(name, ok):
    report['checks'][name] = bool(ok)
    if not ok:
        raise ValueError(name)


def matrix(raw, rows, cols, integer=False):
    if len(raw) != rows or any(len(row) != cols for row in raw):
        raise ValueError('matrix dimensions')
    if integer and any(type(x) is not int for row in raw for x in row):
        raise ValueError('integer matrix required')
    return [[Q(x) for x in row] for row in raw]


def product(a, b):
    if any(len(row) != len(b) for row in a):
        raise ValueError('product dimensions')
    out = [[Q(0)] * len(b[0]) for _ in a]
    sparse = [[(j, x) for j, x in enumerate(row) if x] for row in b]
    for i, row in enumerate(a):
        for k, x in enumerate(row):
            if x:
                for j, y in sparse[k]:
                    out[i][j] += x*y
    return out


def identity(n):
    return [[Q(i == j) for j in range(n)] for i in range(n)]


def v3(x):
    x = Q(x)
    if x == 0:
        raise ValueError('zero has no finite valuation')
    result = 0
    n, d = abs(x.numerator), x.denominator
    while n % 3 == 0:
        n //= 3
        result += 1
    while d % 3 == 0:
        d //= 3
        result -= 1
    return result


def operate(m, op, inverse=False):
    kind, i, j, *rest = op
    if kind.startswith('swap'):
        c = None
    else:
        c = Q(rest[0]) * (-1 if inverse else 1)
    if kind == 'swap_row':
        m[i], m[j] = m[j], m[i]
    elif kind == 'swap_col':
        for row in m:
            row[i], row[j] = row[j], row[i]
    elif kind == 'add_row':
        for k in range(len(m[0])):
            m[i][k] += c*m[j][k]
    elif kind == 'add_col':
        for row in m:
            row[i] += c*row[j]
    else:
        raise ValueError('unknown operation')


def main():
    names = ['enlarged-basis.json', 'projected-container-homothety.json',
             'projected-envelope-span.json']
    report['input_sha256'] = {name: sha256((BASE/name).read_bytes()).hexdigest()
                              for name in names}
    jd, md, td = [json.loads((BASE/name).read_text()) for name in names]
    hashes = report['input_sha256']
    check('pinned_J', hashes[names[0]] == PIN == td['source_sha256'] == md['source_sha256'])
    check('pinned_M', hashes[names[1]] == td['M_source_sha256'])
    b = matrix(jd['integer_basis_matrix'], 108, 108, True)
    check('J_full_rank', all(b[i][i] for i in range(108)) and
          all(b[i][j] == 0 for i in range(108) for j in range(i)))
    check('J_determinant_valuation', sum(v3(b[i][i]) for i in range(108))-216 == 4)

    # Explicit multiplication matrix, separately from the builder's row shift.
    pi = [[Q(0)]*108 for _ in range(108)]
    for a in range(4):
        for r in range(26):
            pi[4*(r+1)+a][4*r+a] = 1
        pi[a][104+a] = 3
    pib = product(pi, b)
    check('complete_pi_times_B', pib == matrix(td['pi_times_integer_basis'], 108, 108, True))
    tau = [[Q(4), Q(-1), Q(-1), Q(-1)] + [Q(0)]*104]
    check('complete_field_trace', tau[0] == td['trace_row_divided_by_27'] == md['trace_row_divided_by_27'])
    bases = {}
    for label, source, ambient, gcd_expected, field in [
        ('M', md, b, 1, 'M_basis_times_9'),
        ('T', td, pib, 27, 'T_basis_times_54')]:
        t = product(tau, ambient)
        trace_field = 'trace_on_integer_J_basis' if label == 'M' else 'trace_on_pi_integer_basis'
        check(label+'_full_trace', t[0] == source[trace_field])
        g = 0
        for x in t[0]:
            if x.denominator != 1:
                raise ValueError('nonintegral trace numerator')
            g = gcd(g, x.numerator)
        check(label+'_trace_gcd', g == source['trace_gcd'] == gcd_expected)
        a = matrix(source['kernel_transform'], 108, 108, True)
        ai = matrix(source['inverse_kernel_transform'], 108, 108, True)
        check(label+'_left_inverse', product(ai, a) == identity(108))
        check(label+'_right_inverse', product(a, ai) == identity(108))
        check(label+'_full_transformed_trace', product(t, a) == [[Q(g)]+[Q(0)]*107])
        basis = product(ambient, [row[1:] for row in a])
        check(label+'_full_kernel_basis', basis == matrix(source[field], 108, 107, True))
        check(label+'_zero_trace', product(tau, basis) == [[Q(0)]*107])
        bases[label] = basis
    check('identical_M_in_T_certificate', bases['M'] == matrix(td['M_basis_times_9'], 108, 107, True))
    r = matrix(td['relative_T_in_M'], 107, 107)
    check('all_11556_relative_entries', product(bases['M'], r) ==
          [[x/6 for x in row] for row in bases['T']])
    rr = [row[:] for row in r]
    for index, op in enumerate(td['smith_operations']):
        kind, i, j, *rest = op
        valid = (type(i) is int and type(j) is int and 0 <= i < 107
                 and 0 <= j < 107 and i != j)
        if kind in ('swap_row', 'swap_col'):
            valid = valid and not rest
            cv = None
        elif kind in ('add_row', 'add_col'):
            valid = valid and len(rest) == 1
            c = Q(rest[0])
            cv = v3(c) if c else None
            valid = valid and (cv is None or cv >= 0)
        else:
            valid = False
            cv = None
        report['operation_checks'].append({'index': index, 'valid': bool(valid),
                                           'coefficient_valuation': cv})
        if not valid:
            raise ValueError('noninvertible Smith operation '+str(index))
        operate(rr, op)
    diagonal = [Q(x) for x in td['smith_diagonal']]
    check('107_nonzero_diagonal_entries', len(diagonal) == 107 and all(diagonal))
    check('full_diagonal_and_off_diagonal_identity', rr ==
          [[diagonal[i] if i == j else Q(0) for j in range(107)] for i in range(107)])
    for op in reversed(td['smith_operations']):
        operate(rr, op, inverse=True)
    check('inverse_replay_recovers_all_R_entries', rr == r)
    exponents = list(map(v3, diagonal))
    expected = [-4]*4+[-3]*8+[-2]*24+[-1]*32+[0]*28+[1]*8+[2]*3
    counts = {str(e): n for e, n in sorted(Counter(exponents).items())}
    check('complete_ordered_exponents', exponents == td['smith_exponents'] == expected)
    check('complete_multiplicities', counts == td['exponent_multiplicities'])
    check('projected_minimum_interval', exponents[:2] == td['projected_minimum_interval'] == [-4, -4])
    check('saved_projected_minimum', td['uniform_projected_minimum'] == -4)
    report.update(trace_gcd_T=27, smith_operation_count=len(td['smith_operations']),
                  smith_exponents=exponents, smith_diagonal=list(map(str, diagonal)),
                  exponent_multiplicities=counts, actual_projected_minimum_interval=exponents[:2],
                  required_for_uniform_minimum='first two exponents equal',
                  expected_span='3^(-4)P, conditional on the audited quotient/group proof',
                  analytic_input='Audited L031 complete logarithm and infinite tails')


try:
    main()
except Exception as error:
    report['failures'].append(str(error))
finally:
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key: report.get(key) for key in
          ['failures', 'trace_gcd_T', 'smith_operation_count', 'exponent_multiplicities',
           'actual_projected_minimum_interval', 'required_for_uniform_minimum']} |
          {'evidence': str(OUT.relative_to(BASE.parents[1]))}))
if report['failures']:
    raise SystemExit(1)
