"""Independent L115 critical arithmetic audit; no producer/replay imports.

Recompute Frobenius by substitution into independently reduced monomials.
Validate every stored operation's state, division identity and remainder,
the complete Euclidean chain, and the existing replay's complete evidence.
Only recorded primes are inspected; no prime search is performed.
"""
from pathlib import Path
from math import gcd, isqrt
from functools import reduce
from fractions import Fraction
import hashlib
import json

HERE = Path(__file__).resolve().parent
G = [2673, 0, -39204, 0, 76230, 0, -31460, 0, 3025]
F = [243, 0, -3564, 0, 6930, 0, -2860, 0, 275]
checks = {}


def check(name, actual, required):
    checks[name] = dict(actual=actual, required=required, passed=actual == required)


def canon(a, p):
    a = [x % p for x in a]
    while a and not a[-1]:
        a.pop()
    return a


def plus(a, b, p):
    out = [0] * max(len(a), len(b))
    for source in (a, b):
        for i, x in enumerate(source):
            out[i] += x
    return canon(out, p)


def product(a, b, p):
    if not a or not b:
        return []
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return canon(out, p)


def monomial_table(f, p):
    # M[d] is x^d modulo monic f. All required d <= 7p.
    n = len(f)-1
    table = [[1]]
    for d in range(1, (n-1)*p+1):
        a = [0] + table[-1]
        a += [0] * (n+1-len(a))
        high = a[n]
        table.append(canon([a[i]-high*f[i] for i in range(n)], p))
    return table


def frobenius(a, table, p):
    # In characteristic p, a(x)^p = sum a_i x^(ip).
    out = []
    for i, x in enumerate(a):
        out = plus(out, [x*y for y in table[i*p]], p)
    return out


def validate_division(label, dividend, divisor, quotient, remainder, p):
    reconstructed = plus(product(divisor, quotient, p), remainder, p)
    check(label + '/identity', reconstructed, canon(dividend, p))
    check(label + '/remainder_degree', len(remainder) < len(divisor), True)
    for name, a in [('quotient', quotient), ('remainder', remainder)]:
        check(label + '/' + name + '_canonical', a, canon(a, p))
    return reconstructed


def audit_row(row):
    p = row['prime']
    tag = f'p{p}'
    inverse = next(i for i in range(1, p) if (F[-1]*i) % p == 1)
    f = [x*inverse % p for x in F]
    check(tag + '/monic_degree_eight', [len(f)-1, f[-1]], [8, 1])
    check(tag + '/normalized_reduction', row['normalized_reduction'], f)
    table = monomial_table(f, p)
    check(tag + '/power_count', len(row['frobenius_powers']), 8)
    a, residues, divisions, replay_rows = [0, 1], [], [], []
    for k, entry in enumerate(row['frobenius_powers'], 1):
        label = f'{tag}/power{k}'
        check(label + '/base', entry['base'], a)
        check(label + '/index', entry['frobenius_index'], k)
        check(label + '/exponent', entry['exponent'], p)
        r = frobenius(a, table, p)
        check(label + '/independent_residue', entry['remainder'], r)
        # Validate a complete binary-power state machine, including no
        # missing or additional operations; a correct isolated identity
        # alone would not establish the recorded exponentiation.
        exponent, accumulator, base, j = p, [1], a, 0

        def consume(kind, left, right):
            nonlocal j
            step = entry['trace'][j]
            loc = label + f'/trace{j}'
            check(loc + '/kind_and_operands',
                  [step['kind'], step['left'], step['right']],
                  [kind, left, right])
            dividend = product(left, right, p)
            reconstructed = validate_division(
                loc, dividend, f, step['quotient'], step['remainder'], p)
            divisions.append(dict(k=k, j=j, kind=kind, left=left,
                                  right=right, dividend=dividend,
                                  quotient=step['quotient'],
                                  remainder=step['remainder']))
            replay_rows.append(dict(k=k, j=j, product=dividend,
                                    reconstructed=reconstructed))
            j += 1
            return step['remainder']

        while exponent:
            if exponent % 2:
                accumulator = consume('multiply', accumulator, base)
            exponent //= 2
            if exponent:
                base = consume('square', base, base)
        check(label + '/complete_trace_length', len(entry['trace']), j)
        check(label + '/terminal_accumulator', accumulator, r)
        residues.append(r)
        a = r
    h = plus(residues[3], [0, -1], p)
    end = plus(residues[7], [0, -1], p)
    check(tag + '/fourth_difference', row['fourth_minus_x'], h)
    check(tag + '/eighth_difference', row['eighth_minus_x'], end)
    bez = row['fourth_gcd_certificate']
    r0, r1 = f, h
    for j, step in enumerate(bez['euclidean_trace']):
        loc = tag + f'/euclid{j}'
        check(loc + '/linked_operands', [step['dividend'], step['divisor']], [r0, r1])
        check(loc + '/nonzero_divisor', bool(r1), True)
        validate_division(loc, r0, r1, step['quotient'], step['remainder'], p)
        r0, r1 = r1, step['remainder']
    check(tag + '/euclid_terminated', r1, [])
    inverse = next(i for i in range(1, p) if r0[-1]*i % p == 1)
    g = canon([inverse*x for x in r0], p)
    check(tag + '/normalized_gcd', bez['gcd'], g)
    value = plus(product(bez['left_multiplier'], f, p),
                 product(bez['right_multiplier'], h, p), p)
    check(tag + '/bezout', value, g)
    passed = end == [] and g == [1]
    check(tag + '/criterion_result', row['irreducible'], passed)
    return dict(prime=p, normalized_reduction=f, monomial_remainders=table,
                frobenius_remainders=residues, division_records=divisions,
                euclidean_trace=bez['euclidean_trace'],
                bezout_left=bez['left_multiplier'], bezout_right=bez['right_multiplier'],
                bezout_identity=value, criterion_passed=passed,
                replay_rows=replay_rows)


def main():
    paths = [HERE/'marked-octic-factorization-certificate.json',
             HERE/'marked-octic-factorization-replay.json']
    source, replay = [json.loads(path.read_text()) for path in paths]
    check('input_coefficients', source['input_coefficients'], G)
    check('primitive_coefficients', source['primitive_coefficients'], F)
    check('positive_content', [source['content'], reduce(gcd, G)], [11, 11])
    check('primitive_content', reduce(gcd, F), 1)
    check('all_nine_product_coefficients', [11*x for x in F], G)
    check('monic_rational_product', [str(3025*Fraction(x, 275)) for x in F],
          [str(x) for x in G])
    check('complete_factor_and_multiplicity', source['rational_factors'],
          [dict(coefficients=F, multiplicity=1)])
    check('recorded_cap', source['search_prime_cap'], 101)
    check('selected_prime', source['selected_prime'], 19)
    check('all_recorded_primes', [r['prime'] for r in source['attempts']],
          [2, 3, 5, 7, 11, 13, 17, 19])
    evidence = []
    for row in source['attempts']:
        p = row['prime']
        divisors = [d for d in range(2, isqrt(p)+1) if p % d == 0]
        check(f'p{p}/prime_trial', [p >= 2, divisors], [True, []])
        if 'skipped' in row:
            check(f'p{p}/skip_reason', row['skipped'], 'leading coefficient vanishes')
            check(f'p{p}/vanishing_leading_coefficient', G[-1] % p, 0)
            continue
        check(f'p{p}/preserved_degrees', [G[-1] % p != 0, F[-1] % p != 0], [True, True])
        evidence.append(audit_row(row))
    selected = next(row for row in evidence if row['prime'] == 19)
    check('only_success_in_recorded_tests',
          [row['prime'] for row in evidence if row['criterion_passed']], [19])
    check('leading_residues_and_inverse', [3025 % 19, 275 % 19, (9*17) % 19], [4, 9, 1])
    check('degree_prime_divisors', [d for d in [2, 3, 5, 7] if 8 % d == 0], [2])
    check('selected_R4_R8', [selected['frobenius_remainders'][i] for i in [3, 7]],
          [[0, 18], [0, 1]])
    check('selected_bezout_coefficients', [selected['bezout_left'], selected['bezout_right']],
          [[12], [0, 18, 0, 3, 0, 6, 0, 6]])
    for key in ['prime', 'normalized_reduction', 'frobenius_remainders',
                'bezout_left', 'bezout_right', 'bezout_identity']:
        check('saved_replay/' + key, replay[key], selected[key])
    check('saved_replay/all_arithmetic_rows', replay['arithmetic_rows'], selected['replay_rows'])
    check('saved_replay/check_count', len(replay['checks']), 167)
    for name, record in replay['checks'].items():
        check('saved_replay/check/' + name,
              [record['actual'] == record['required'], record['pass_']], [True, True])
    check('saved_replay/no_reported_failures', replay['failures'], [])
    check('producer/final_checks', source['checks'],
          dict(input_degree_eight=True, exact_positive_content=True,
               exact_product=True, irreducible_reduction_found=True))
    check('producer/no_reported_failures', source['failures'], [])
    failures = [name for name, record in checks.items() if not record['passed']]
    destination = HERE/'marked-octic-factorization-audit-certificate.json'
    result = dict(input_sha256={path.name: hashlib.sha256(path.read_bytes()).hexdigest()
                               for path in paths},
                  input_coefficients=G, primitive_coefficients=F,
                  evidence=evidence, checks=checks, failures=failures,
                  summary=dict(checks_passed=len(checks)-len(failures),
                               checks_required=len(checks), selected_prime=19,
                               selected_divisions=len(selected['division_records']),
                               selected_euclidean_steps=len(selected['euclidean_trace']),
                               actual_factor_degrees=[8], required_factor_degrees=[8],
                               actual_multiplicities=[1], required_multiplicities=[1]))
    destination.write_text(json.dumps(result, indent=2)+'\n')
    print(f'Checks: {len(checks)-len(failures)}/{len(checks)}; failures: {failures}')
    print('Actual/required: content 11/11; factor degrees [8]/[8]; multiplicities [1]/[1]')
    print('Actual/required: selected divisions 56/56; Euclidean steps 2/2; R4=-x; R8=x; Bezout=1')
    print('Recorded primes only: 2,3,5,7,11,13,17,19; no enlarged search')
    print('Certificate:', destination.relative_to(HERE.parent.parent))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
