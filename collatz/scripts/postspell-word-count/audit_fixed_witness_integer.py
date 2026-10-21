#!/usr/bin/env python3
"""Independent bounded audit of every saved L056 modular record.

No import of the generator. Matrices act on homogeneous column vectors;
the chronological last map multiplies on the left. All evidence is saved.
"""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'fixed-witness-integer-audit-certificate.json'
K, N = 397573379, 630138897
IDENTITY = [[1, 0], [0, 1]]
O, E = [[3, 1], [0, 2]], [[1, 0], [0, 2]]


def multiply(a, b, modulus):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) % modulus
             for j in range(2)] for i in range(2)]


def power(a, exponent, modulus):
    # Left-to-right binary powering; invariant is a**(bits consumed).
    result = IDENTITY
    for bit in bin(exponent)[2:]:
        result = multiply(result, result, modulus)
        if bit == '1':
            result = multiply(result, a, modulus)
    return result


def main():
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required,
                           passed=actual == required))

    source_path = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
    source = source_path.read_text()
    proof = (ROOT / 'lemmas/L056-fixed-witness-prime-five-nonintegrality.md').read_text()
    saved = json.loads((HERE / 'fixed-witness-integer-certificate.json').read_text())
    written = json.loads((HERE / 'fixed-witness-written-table-check.json').read_text())
    literal = []
    for line in source.splitlines():
        fields = line.strip('|').split('|')
        if len(fields) == 3 and all(s.isdigit() for s in fields):
            literal.append(list(map(int, fields)))
    check('indices', [r[0] for r in literal], list(range(25)))
    check('tails specified', 'For 0<=i<24 set a_i=2;' in source and
          'set a_24=166504412=' in source, True)
    rows = [dict(i=i, J=j, H=h, a=2 if i < 24 else 166504412,
                 k=3*j+h, length=4*j+h+(2 if i < 24 else 166504412))
            for i, j, h in literal]
    check('complete source parameters', saved['parameters'], rows)
    check('source hash', saved['source_sha256'], hashlib.sha256(source.encode()).hexdigest())
    check('counts', [sum(r['k'] for r in rows), sum(r['length'] for r in rows)], [K, N])
    check('saved counts', saved['counts'], dict(K=K, N=N, L=N-K))

    # Inductively, every composite n has a previously found prime divisor
    # at most sqrt(n). This enumerates the complete fixed interval.
    primes = []
    for candidate in range(2, 10001):
        composite = False
        for divisor in primes:
            if divisor*divisor > candidate:
                break
            if candidate % divisor == 0:
                composite = True
                break
        if not composite:
            primes.append(candidate)
    check('complete prime list', saved['primes'], primes)
    check('prime count and maximum', [len(primes), primes[-1]], [1229, 9973])

    records = []
    for p in primes:
        block = IDENTITY
        for letter in [O, O, E, O]:
            block = multiply(letter, block, p)
        check(f'{p}: OOEO matrix', block, [[27 % p, 23 % p], [0, 16 % p]])
        product = IDENTITY
        words = []
        for i, row in enumerate(rows):
            j, h, a = row['J'], row['H'], row['a']
            word = multiply(power(E, a, p),
                            multiply(power(O, h, p), power(block, j, p), p), p)
            product = multiply(word, product, p)
            lift = 23*pow(3, h, 11*p)*(pow(27, j, 11*p)-pow(16, j, 11*p)) % (11*p)
            check(f'{p}/{i}: lift divisible', lift % 11, 0)
            offset = (lift//11+(pow(3, h, p)-pow(2, h, p))*pow(16, j, p)) % p
            check(f'{p}/{i}: closed-offset matrix', word,
                  [[pow(3, row['k'], p), offset], [0, pow(2, row['length'], p)]])
            before = pow(2, sum(r['length'] for r in rows[:i]), p)
            after = pow(3, sum(r['k'] for r in rows[i+1:]), p)
            words.append(dict(i=i, A=word[0][0], C=word[0][1], Q=word[1][1],
                              lift_mod_11p=lift, prefix_two=before, suffix_three=after,
                              contribution=word[0][1]*before*after % p))
        denominator = (pow(2, N, p)-pow(3, K, p)) % p
        check(f'{p}: whole matrix', product,
              [[pow(3, K, p), sum(w['contribution'] for w in words) % p], [0, pow(2, N, p)]])
        records.append(dict(p=p, two_N=product[1][1], three_K=product[0][0],
                            denominator=denominator, numerator=product[0][1],
                            obstruction=denominator == 0 and product[0][1] != 0, words=words))
    check('record count', len(saved['prime_records']), len(records))
    for i, record in enumerate(records):
        check(f"{record['p']}: complete saved record", saved['prime_records'][i], record)
    cases = [r for r in records if r['denominator'] == 0]
    exceptions = [r for r in records if r['p'] in (2, 3, 11)]
    check('complete denominator records', saved['denominator_cases'], cases)
    check('complete exceptional records', saved['exceptions'], exceptions)
    check('saved failures', saved['failures'], [])
    expected_summary = dict(bound=10000, primes_checked=1229, largest_prime=9973,
                            checks=10+1229*28, failures=0,
                            denominator_prime_divisors=[r['p'] for r in cases],
                            obstruction_primes=[r['p'] for r in cases if r['obstruction']],
                            common_divisor_primes=[r['p'] for r in cases if not r['obstruction']],
                            verdict='NONINTEGRAL')
    check('entire generator summary', saved['summary'], expected_summary)

    printed = [list(map(int, m)) for m in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$', proof, re.M)]
    direct = []
    two, three = [1, 2, 4, 3], [1, 3, 4, 2]
    for i, row in enumerate(rows):
        c = (3*three[row['H'] % 4]*(two[row['J'] % 4]-1)
             +three[row['H'] % 4]-two[row['H'] % 4]) % 5
        before = two[sum(r['length'] for r in rows[:i]) % 4]
        after = three[sum(r['k'] for r in rows[i+1:]) % 4]
        direct.append([i, c, before, after, c*before*after % 5])
    check('every printed term', printed, direct)
    five = next(r for r in records if r['p'] == 5)
    check('matrix terms equal period-four terms',
          [[w['i'], w['C'], w['prefix_two'], w['suffix_three'], w['contribution']]
           for w in five['words']], direct)
    check('saved printed table', written['printed'], printed)
    check('saved direct table', written['direct'], direct)
    check('integer contribution sum', sum(r[-1] for r in direct), 44)
    check('prime-five denominator', (two[N % 4]-three[K % 4]) % 5, 0)
    expected_checks = [
        dict(name='all 25 written proof rows equal direct period-four calculation', passed=printed == direct),
        dict(name='all 25 direct rows equal full certificate rows', passed=direct == written['direct']),
        dict(name='contribution sum exactly 44', actual=sum(r[-1] for r in direct), required=44, passed=True),
        dict(name='denominator zero via periods', actual=(two[N % 4]-three[K % 4]) % 5, required=0, passed=True)]
    check('saved table check records', written['checks'], expected_checks)
    check('saved table failures', written['failures'], [])
    failures = [c for c in checks if not c['passed']]
    summary = dict(primes=len(primes), word_records=len(primes)*25,
                   checks=len(checks), failures=len(failures),
                   denominator_numerator=[[r['p'], r['denominator'], r['numerator']] for r in cases],
                   prime_five_contribution_sum=sum(r[-1] for r in direct))
    evidence = dict(summary=summary, source_sha256=hashlib.sha256(source.encode()).hexdigest(),
                    prime_records=records, period_four_table=direct, checks=checks, failures=failures)
    OUT.write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: all saved records agree; no failures; at p=5 denominator=0, numerator=4.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
