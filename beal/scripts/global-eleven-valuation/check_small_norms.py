"""Bounded exact norm search, not a complete S-unit computation.

Run from beal. Every tested polynomial and norm is saved; only a summary
is printed. No maximal-order, ideal-class, or exclusion certificate results.
"""
import json
from itertools import product
from pathlib import Path

BASE = Path(__file__).resolve().parent
M = [-380, -774, -1062, -456, 258, 468, 104, -126, -6, 6, -6, 0, 1]


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
                a[i][j] = numerator // previous
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def multiplication_norm(g):
    """Independent determinant on Q[X]/(M), basis 1,...,X^11."""
    columns = []
    for j in range(12):
        p = [0]*j+g[:]
        while len(p) > 12:
            coefficient = p[-1]
            shift = len(p)-13
            for i, coefficient_m in enumerate(M):
                p[shift+i] -= coefficient*coefficient_m
            p.pop()
        columns.append(p+[0]*(12-len(p)))
    return determinant([[columns[j][i] for j in range(12)] for i in range(12)])


def linear_norm(c):
    r = 0
    for coefficient in reversed(M):
        r = -c*r+coefficient
    return r


def quadratic_norm(a, b, c):
    # a^12 M mod (aX^2+bX+c) = uX+v. The resultant is
    # (a v^2-buv+c u^2)/a^13, since deg(M)=12.
    u, v, ap = 0, 1, 1
    for coefficient in M[-2::-1]:
        ap *= a
        u, v = a*v-b*u, coefficient*ap-c*u
    numerator = a*v*v-b*u*v+c*u*u
    assert numerator % (a**13) == 0
    return numerator // (a**13)


def cubic_norm(a, b, c):
    # R=M mod (X^3+aX^2+bX+c); determinant of multiplication
    # by R in this three-dimensional algebra equals Res(M,g).
    u, v, w = 0, 0, 0
    for coefficient in reversed(M):
        u, v, w = coefficient-c*w, u-b*w, v-a*w
    columns = []
    for _ in range(3):
        columns.append((u, v, w))
        u, v, w = -c*w, u-b*w, v-a*w
    return determinant([[columns[j][i] for j in range(3)] for i in range(3)])


def strip_support(n):
    n = abs(n)
    if not n:
        return None, [0, 0]
    exponents = []
    for prime in (5, 11):
        exponent = 0
        while n % prime == 0:
            n //= prime
            exponent += 1
        exponents.append(exponent)
    return n, exponents


def main():
    rows, hits = [], []

    def record(g, norm, family):
        remainder, exponents = strip_support(norm)
        row = {'g_ascending': g, 'norm': norm, 'family': family,
               'outside_5_11_factor': remainder, 'exponents_5_11': exponents}
        rows.append(row)
        if remainder == 1:
            hits.append(row)

    for c in range(-30, 31):
        record([c, 1], linear_norm(c), 'linear')
    # Includes and extends the preliminary monic-quadratic box [-30,30]^2.
    for a in range(1, 7):
        for b, c in product(range(-60, 61), repeat=2):
            record([c, b, a], quadratic_norm(a, b, c), 'quadratic')
    for a, b, c in product(range(-12, 13), repeat=3):
        record([c, b, a, 1], cubic_norm(a, b, c), 'cubic')

    # Determinant identities justify all norms. These selected exact checks
    # detect implementation/sign/scaling errors; they are not ideal data.
    selected = [[-8, 1], [30, 1], [-60, 60, 6], [0, 0, 1],
                [13, -21, 4], [-12, 12, -12, 1], [0, 0, 0, 1],
                [7, -4, 9, 1]]
    audits = []
    for g in selected:
        if len(g) == 2:
            computed = linear_norm(g[0])
        elif len(g) == 3:
            computed = quadratic_norm(g[2], g[1], g[0])
        else:
            computed = cubic_norm(g[2], g[1], g[0])
        independent = multiplication_norm(g)
        audits.append({'g_ascending': g, 'norm': computed,
                       'multiplication_determinant': independent,
                       'equal': computed == independent})
    required_count = 61+6*121**2+25**3
    checks = {'complete_box_counts': len(rows) == required_count,
              'selected_independent_norms': all(a['equal'] for a in audits),
              'no_zero_norms': all(row['norm'] for row in rows)}
    certificate = {'field_polynomial_ascending': M,
                   'bounds': {'linear_c': [-30, 30], 'quadratic_a': [1, 6],
                              'quadratic_b_c': [-60, 60], 'cubic_a_b_c': [-12, 12],
                              'actual_count': len(rows), 'required_count': required_count},
                   'checks': checks, 'independent_norm_checks': audits,
                   'hits': hits, 'all_tests': rows,
                   'limitations': 'Bounded search only; no class-group certificate, '
                                  'exact global image, or absence proof.'}
    path = BASE/'small-norm-certificate.json'
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    failures = [name for name, passed in checks.items() if not passed]
    print(f'Tests actual={len(rows)}, required={required_count}; support-only hits={len(hits)}')
    print(f'Checks={sum(checks.values())}/{len(checks)}; failures={failures}')
    print(f'Required projection threshold: certified exact image; actual=UNRESOLVED')
    print(f'Certificate: {path.relative_to(BASE.parent.parent)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
