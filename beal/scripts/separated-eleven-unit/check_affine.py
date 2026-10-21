"""Bounded exact affine test in the fixed D=Q[k,t]; no unit completeness claim."""
import json
from itertools import product
from math import gcd
from pathlib import Path

BASE = Path(__file__).resolve().parent
M = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]
F = [1, 1, -1, 1]


def mul(a, b, modulus):
    degree = len(modulus)-1
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    for j in range(len(out)-1, degree-1, -1):
        lead = out[j]
        for i in range(degree+1):
            out[j-degree+i] -= lead*modulus[i]
    return (out[:degree]+[0]*degree)[:degree]


def determinant(matrix):
    a = [row[:] for row in matrix]
    sign, previous = 1, 1
    for k in range(len(a)-1):
        if a[k][k] == 0:
            pivot = next((j for j in range(k+1, len(a)) if a[j][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def norm(a, modulus):
    degree = len(modulus)-1
    columns = [mul(a, [0]*j+[1], modulus) for j in range(degree)]
    return determinant([[columns[j][i] for j in range(degree)]
                        for i in range(degree)])


def relative_norm(a, b, c):
    # N_D/K(d+ct)=d^3+c*d^2+c^2*d-c^3, d=a+bk.
    return [a**3+c*a*a+c*c*a-c**3,
            3*a*a*b+2*c*a*b+c*c*b,
            3*a*b*b+c*b*b, b**3]


def other_tower_norm(a, b, c):
    # N_D/F(a+bk+ct)=b^12*m(-(a+ct)/b), exact homogenized Horner.
    d = [-a, -c, 0]
    value, power = [1, 0, 0], 1
    for coefficient in M[-2::-1]:
        power *= b
        value = mul(value, d, F)
        value[0] += coefficient*power
    return value, norm(value, F)


def strip(n):
    assert n != 0
    remainder, exponents = abs(n), []
    for p in (2, 11):
        exponent = 0
        while remainder % p == 0:
            remainder //= p
            exponent += 1
        exponents.append(exponent)
    return remainder, exponents


def main():
    rows, hits, failures, skipped = [], [], [], 0
    for a, b, c in product(range(-32, 33), range(1, 5),
                           (-4, -3, -2, -1, 1, 2, 3, 4)):
        if gcd(gcd(a, b), abs(c)) != 1:
            skipped += 1
            continue
        relative = relative_norm(a, b, c)
        absolute = norm(relative, M)
        other_relative, other_absolute = other_tower_norm(a, b, c)
        if absolute != other_absolute or absolute == 0:
            failures.append([a, b, c])
        remainder, exponents = strip(absolute)
        # This residue flag is only a prospective local test, not a witness.
        prospective = [int((a+b*k+3*c) % 11 == 0) for k in (8, 2)]
        row = dict(abc=[a, b, c], relative_norm_k_ascending=relative,
                   absolute_norm=absolute,
                   other_relative_norm_t_ascending=other_relative,
                   other_absolute_norm=other_absolute,
                   exponents_2_11=exponents, outside_support_factor=remainder,
                   prospective_ramified_parities=prospective)
        rows.append(row)
        if remainder == 1:
            hits.append(row)
    checks = dict(raw_count=len(rows)+skipped == 2080,
                  unique_candidates=len({tuple(r['abc']) for r in rows}) == len(rows),
                  all_tower_norms_agree=not failures,
                  all_norms_nonzero=all(r['absolute_norm'] != 0 for r in rows),
                  all_factorizations_reconstruct=all(
                      r['outside_support_factor'] * 2**r['exponents_2_11'][0]
                      * 11**r['exponents_2_11'][1] == abs(r['absolute_norm'])
                      for r in rows))
    summary = dict(raw_cap=2080, actual_raw=len(rows)+skipped,
                   primitive_candidates=len(rows), gcd_skipped=skipped,
                   exact_tower_comparisons=len(rows), support_hits=len(hits),
                   prospective_separating_candidates=sum(
                       r['prospective_ramified_parities'][0] !=
                       r['prospective_ramified_parities'][1] for r in rows),
                   failures=failures, checks=checks,
                   required_separating_witnesses=1,
                   certified_separating_witnesses=0)
    certificate = dict(field_k_ascending=M, field_t_ascending=F,
                       summary=summary, support_hits=hits, all_tests=rows,
                       qualification='Finite family only; hits still require '
                       'supported-inverse, norm-correction and valuation proof.')
    path = BASE/'affine-certificate.json'
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(summary, indent=2))
    print('Certificate:', path.relative_to(BASE.parent.parent))
    if failures or not all(checks.values()):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
