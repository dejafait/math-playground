#!/usr/bin/env python3
"""Independent finite C874c audit: partitions, formal log, integer Bareiss."""
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
import hashlib
import json
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
ORIGINAL = HERE / 'contact-ordinary-moment-2132.json'
OUTPUT = HERE / 'contact-ordinary-moment-audit-2134.json'


def coefficient(n, s):
    # Enumerate all multiplicities r_k with sum k*r_k=n directly.
    def visit(k, remaining):
        if k == 8:
            return Q(remaining == 0)
        return sum(((-s[k-1] / k)**r / factorial(r)
                    * visit(k+1, remaining-k*r)
                    for r in range(remaining//k+1)), Q(0))
    return visit(1, n)


def convolution(a, b):
    return [sum((a[i]*b[n-i] for i in range(n+1)), Q(0))
            for n in range(8)]


def bareiss(matrix):
    a = [row[:] for row in matrix]
    previous, sign = 1, 1
    for k in range(len(a)-1):
        if not a[k][k]:
            row = next((r for r in range(k+1, len(a)) if a[r][k]), None)
            if row is None:
                return 0
            a[k], a[row] = a[row], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, len(a)):
            for j in range(k+1, len(a)):
                numerator = pivot*a[i][j] - a[i][k]*a[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError('Bareiss nonexact division')
                a[i][j] = quotient
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def encode(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, list):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    return value


def main():
    initial = ORIGINAL.read_bytes()
    old = json.loads(initial)
    failures, cases = [], []

    def check(label, condition):
        if not condition:
            failures.append(label)
        return bool(condition)

    text = (ROOT / 'lemmas/C874c-ordinary-degree-seven-contact-compatibility.md').read_text()
    rows = [line.split('|')[1:-1] for line in text.splitlines()
            if line.startswith('| ')]
    printed_moments = [row for row in rows if row[0].strip().isdigit()]
    printed_minors = {row[0].strip(): [int(x.strip()) for x in row[1:]]
                      for row in rows if row[0].strip() in
                      ('first / A_3', 'first / B_3', 'second / A_3', 'second / B_3')}
    check('printed moment table has all eight rows', len(printed_moments) == 8)
    check('printed minor table has all four rows', len(printed_minors) == 4)
    check('original case count', len(old['cases']) == 2)

    for index, second in enumerate((2, 3)):
        name = ('rank_one', 'rank_two')[index]
        s = list(map(Q, [16, second, 2, 2, 2, 2, 2]))
        a = [coefficient(n, s) for n in range(8)]
        rational_moments = [(-1)**j*factorial(2*j)*a[j] for j in range(8)]
        check(name+'/integral moments', all(m.denominator == 1 for m in rational_moments))
        m = [int(x) for x in rational_moments]
        # log(1+v)=sum (-1)^(r+1)*v^r/r mod y^8; not the old recurrence.
        v = [Q(0)] + a[1:]
        power, logarithm = [Q(1)] + [Q(0)]*7, [Q(0)]*8
        for r in range(1, 8):
            power = convolution(power, v)
            logarithm = [x + Q((-1)**(r+1), r)*y
                         for x, y in zip(logarithm, power)]
        recovered = [-n*logarithm[n] for n in range(1, 8)]
        checks = {}
        saved = old['cases'][index]
        for key, value in (
            ('S_1_through_S_7', s), ('coefficients_a_0_through_a_7', a),
            ('factor_product_coefficients', a), ('moments_m_0_through_m_7', rational_moments),
            ('recovered_S_1_through_S_7', recovered)):
            checks[key] = check(name+'/'+key, encode(value) == saved[key])
        checks['formal_log_prefix'] = check(name+'/formal log', recovered == s)
        checks['normalization'] = check(name+'/normalization', m[0] == 1 and s[0] == 16)
        checks['printed_moments'] = check(name+'/printed moments',
            len(printed_moments) == 8 and
            all(int(row[0]) == j and int(row[index+1]) == m[j]
                for j, row in enumerate(printed_moments)))
        matrices = {}
        for label, shift in (('A_3', 0), ('B_3', 1)):
            matrix = [[m[i+j+shift] for j in range(4)] for i in range(4)]
            minors = [bareiss([row[:n] for row in matrix[:n]]) for n in range(1, 5)]
            expected = saved['matrices'][label]
            prefix = ('first', 'second')[index] + ' / ' + label
            matched = check(name+'/'+label+'/matrix',
                            matrix == [[int(x) for x in row] for row in expected['matrix']])
            matched_minors = check(name+'/'+label+'/minors',
                                   minors == list(map(int, expected['leading_minors'])))
            printed = check(name+'/'+label+'/printed minors', minors == printed_minors.get(prefix))
            symmetric = check(name+'/'+label+'/symmetry',
                              all(matrix[i][j] == matrix[j][i] for i in range(4) for j in range(4)))
            signs = [check(name+'/'+label+f'/minor{n+1}>0', d > 0) for n, d in enumerate(minors)]
            matrices[label] = dict(matrix=matrix, leading_minors=minors,
                required_each_minor='>0', strict_sign_checks=signs,
                original_matrix_matches=matched, original_minors_match=matched_minors,
                canonical_table_matches=printed, symmetric=symmetric)
        cases.append(dict(name=name, S_1_through_S_7=s, coefficients=a,
                          logarithm_coefficients=logarithm, recovered_prefix=recovered,
                          moments=m, comparisons=checks, matrices=matrices))

    replay = subprocess.run([sys.executable, str(HERE/'contact_ordinary_moment_2132.py')],
                            capture_output=True, text=True)
    check('original replay exit zero', replay.returncode == 0)
    check('original replay byte identical', initial == ORIGINAL.read_bytes())
    check('original failures empty', old['failures'] == [])
    report = dict(step='2134', scope='C874c degree-seven audit only; S_8 unprescribed',
        methods='partition coefficients; finite log powers; fraction-free integer Bareiss',
        original_sha256=hashlib.sha256(initial).hexdigest(), cases=cases,
        original_replay_exit=replay.returncode, original_replay_stdout=replay.stdout,
        original_replay_stderr=replay.stderr, original_replay_byte_identical=initial == ORIGINAL.read_bytes(),
        required_minor_count=16, verified_strict_minor_count=sum(
            sum(e['strict_sign_checks']) for c in cases for e in c['matrices'].values()),
        all_checks_pass=not failures, failures=failures)
    OUTPUT.write_text(json.dumps(encode(report), indent=2)+'\n')
    for case in cases:
        for label, evidence in case['matrices'].items():
            print(f"{case['name']}/{label}: {evidence['leading_minors']}; required each >0")
    print(f"strict minors={report['verified_strict_minor_count']}/16; failures={failures}; certificate={OUTPUT}")
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
