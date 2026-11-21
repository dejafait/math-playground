#!/usr/bin/env python3
"""Exact fixed-S1 joint C874b compatibility through m8; no parameter sweep."""
from fractions import Fraction as Q
from itertools import permutations
from math import factorial
from pathlib import Path
import json

DEGREE = 8
HERE = Path(__file__).resolve().parent
OUTPUT = HERE / 'contact-joint-eighth-2136.json'


def multiply(a, b):
    return [sum((a[j]*b[n-j] for j in range(n+1)), Q(0))
            for n in range(DEGREE+1)]


def determinant(matrix):
    a = [list(map(Q, row)) for row in matrix]
    value = Q(1)
    for k in range(len(a)):
        pivot = next((i for i in range(k, len(a)) if a[i][k]), None)
        if pivot is None:
            return Q(0)
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            value = -value
        p = a[k][k]
        value *= p
        for i in range(k+1, len(a)):
            ratio = a[i][k]/p
            for j in range(k+1, len(a)):
                a[i][j] -= ratio*a[k][j]
            a[i][k] = Q(0)
    return value


def leibniz(matrix):
    value = Q(0)
    for p in permutations(range(len(matrix))):
        inversions = sum(p[i] > p[j] for i in range(len(p))
                         for j in range(i+1, len(p)))
        term = Q((-1)**inversions)
        for i, j in enumerate(p):
            term *= matrix[i][j]
        value += term
    return value


def solve(matrix, column):
    a = [list(map(Q, row)) + [Q(v)] for row, v in zip(matrix, column)]
    for k in range(len(a)):
        pivot = next(i for i in range(k, len(a)) if a[i][k])
        a[k], a[pivot] = a[pivot], a[k]
        p = a[k][k]
        a[k] = [x/p for x in a[k]]
        for i in range(len(a)):
            if i != k:
                ratio = a[i][k]
                a[i] = [x-ratio*y for x, y in zip(a[i], a[k])]
    return [row[-1] for row in a]


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, list):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    return value


def main():
    old = json.loads((HERE/'contact-ordinary-moment-2132.json').read_text())
    audited = json.loads((HERE/'contact-ordinary-moment-audit-2134.json').read_text())
    failures, cases = [], []

    def check(label, condition):
        if not condition:
            failures.append(label)
        return bool(condition)

    check('prior independent audit passed', audited['all_checks_pass'] and not audited['failures'])
    for index, second in enumerate((2, 3)):
        name = ('rank_one', 'rank_two')[index]
        s = [Q(0), Q(16), Q(second)] + [Q(2)]*6
        a = [Q(1)]
        for n in range(1, DEGREE+1):
            a.append(-sum((s[k]*a[n-k] for k in range(1, n+1)), Q(0))/n)
        product = [Q(1)] + [Q(0)]*DEGREE
        for k in range(1, DEGREE+1):
            factor = [Q(0)]*(DEGREE+1)
            for r in range(DEGREE//k+1):
                factor[k*r] = (-s[k]/k)**r/factorial(r)
            product = multiply(product, factor)
        check(name+'/independent exponential coefficients', a == product)
        m = [(-1)**j*factorial(2*j)*a[j] for j in range(DEGREE+1)]
        check(name+'/normalization', m[0] == 1 and s[1] == 16)
        check(name+'/lower moments match original',
              encode(m[:8]) == old['cases'][index]['moments_m_0_through_m_7'])
        check(name+'/lower moments match independent audit',
              m[:8] == list(map(Q, audited['cases'][index]['moments'])))

        # Independent formal logarithm, rather than the inverse recurrence.
        v = [Q(0)] + a[1:]
        power, logarithm = [Q(1)] + [Q(0)]*DEGREE, [Q(0)]*(DEGREE+1)
        for r in range(1, DEGREE+1):
            power = multiply(power, v)
            logarithm = [x + Q((-1)**(r+1), r)*y
                         for x, y in zip(logarithm, power)]
        recovered = [-k*logarithm[k] for k in range(1, DEGREE+1)]
        check(name+'/all eight prescribed logarithmic coefficients', recovered == s[1:])

        matrices = {}
        for label, size, shift in (('A_4', 5, 0), ('B_3', 4, 1)):
            matrix = [[m[i+j+shift] for j in range(size)] for i in range(size)]
            minors, agreement = [], []
            for n in range(1, size+1):
                corner = [row[:n] for row in matrix[:n]]
                d = determinant(corner)
                agreement.append(check(f'{name}/{label}/{n}/determinants', d == leibniz(corner)))
                minors.append(d)
            pd = all(d > 0 for d in minors)
            # A failed strict test is NOT a PSD incompatibility certificate.
            check(name+'/'+label+'/strict PD branch sufficient', pd)
            matrices[label] = dict(matrix=matrix, leading_minors=minors,
                required_strict_lower_bound='0', determinant_crosschecks=agreement,
                positive_definite_by_Sylvester=pd)
        column = m[5:9]
        if matrices['B_3']['positive_definite_by_Sylvester']:
            b = matrices['B_3']['matrix']
            solution = solve(b, column)
            residual = [sum((b[i][j]*solution[j] for j in range(4)), Q(0))-column[i]
                        for i in range(4)]
            range_ok = check(name+'/even theorem range residual', residual == [Q(0)]*4)
        else:
            solution, residual, range_ok = [], [], False
        cases.append(dict(name=name, S_1_through_S_8=s[1:], coefficients=a,
            independent_product_coefficients=product, moments=m,
            logarithm_coefficients=logarithm, recovered_S_1_through_S_8=recovered,
            lower_moments_match_audited_C874c=m[:8] == list(map(Q, audited['cases'][index]['moments'])),
            matrices=matrices, even_range_column=column, range_solution=solution,
            range_residual=residual, range_condition_certified=range_ok,
            even_criterion_satisfied=range_ok and all(
                x['positive_definite_by_Sylvester'] for x in matrices.values())))
    report = dict(step='2136', arithmetic='exact fractions.Fraction',
        target='both fixed C874b prefixes through S_8 at S_1=16 only',
        theorem='Curto-Fialkow 1991 Theorem5.3 pp626-627, k=4',
        cases=cases, failures=failures, all_checks_pass=not failures,
        all_joint_criteria_satisfied=all(c['even_criterion_satisfied'] for c in cases),
        scope='finite ordinary representation plus auxiliary contact; no theta or trajectory realization')
    OUTPUT.write_text(json.dumps(encode(report), indent=2)+'\n')
    for c in cases:
        print(f"{c['name']}: m_8={c['moments'][8]}; recovered S_8={c['recovered_S_1_through_S_8'][7]}")
        for label, evidence in c['matrices'].items():
            print(f"  {label}: minors={list(map(str, evidence['leading_minors']))}; required each >0")
        print(f"  range residual={list(map(str, c['range_residual']))}; required zero")
    print(f"joint criteria={report['all_joint_criteria_satisfied']}; failures={failures}; certificate={OUTPUT}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
