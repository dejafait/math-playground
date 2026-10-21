#!/usr/bin/env python3
"""Bounded L055 integer-root test, with two exact compressed evaluations.

No giant powers, floating-point arithmetic, rational parity conclusions,
or assumed coprimality of the unreduced numerator/denominator.
"""
from pathlib import Path
from math import isqrt
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
OUT = HERE / 'fixed-witness-integer-certificate.json'
BOUND = 10000
K, N = 397573379, 630138897


def concat(first, second, modulus):
    """First map is applied first: source equation (4)."""
    a, c, q = first
    b, d, r = second
    return (b*a % modulus, (b*c + q*d) % modulus, r*q % modulus)


def repeat(triple, exponent, modulus):
    value = (1, 0, 1)
    base = tuple(x % modulus for x in triple)
    while exponent:
        if exponent & 1:
            value = concat(value, base, modulus)
        base = concat(base, base, modulus)
        exponent //= 2
    return value


def modular_word(j, h, a, modulus):
    # OOEO has integer triple (27,23,16).
    value = repeat((27, 23, 16), j, modulus)
    value = concat(value, repeat((3, 1, 2), h, modulus), modulus)
    return concat(value, repeat((1, 0, 2), a, modulus), modulus)


def closed_offset(j, h, modulus):
    # Let F=23*3^H(27^J-16^J). F is divisible by 11 in Z.
    # Its least residue modulo 11*m is divisible by 11; dividing
    # that residue gives (F/11) mod m, even when m=11.
    lifted_modulus = 11*modulus
    lift = (23*pow(3, h, lifted_modulus) *
            (pow(27, j, lifted_modulus)-pow(16, j, lifted_modulus))) % lifted_modulus
    if lift % 11:
        raise ArithmeticError('lifted integer quotient is not divisible by 11')
    second = (pow(3, h, modulus)-pow(2, h, modulus))*pow(16, j, modulus)
    return (lift//11 + second) % modulus, lift


def sieve(bound):
    flags = [True]*(bound+1)
    flags[0] = flags[1] = False
    for p in range(2, isqrt(bound)+1):
        if flags[p]:
            for multiple in range(p*p, bound+1, p):
                flags[multiple] = False
    return [p for p, flag in enumerate(flags) if flag]


def trial_primes(bound):
    return [n for n in range(2, bound+1)
            if all(n % d for d in range(2, isqrt(n)+1))]


def main():
    source_text = SOURCE.read_text()
    table = [tuple(map(int, row)) for row in
             re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source_text, re.M)]
    failures = []
    checks = 0

    def check(name, actual, required):
        nonlocal checks
        checks += 1
        if actual != required:
            failures.append(dict(name=name, actual=actual, required=required))

    check('literal indices', [r[0] for r in table], list(range(25)))
    # These exact tail statements must still occur in the canonical lemma.
    check('literal short tails', 'For 0<=i<24 set a_i=2;' in source_text, True)
    check('literal closing tail', 'set a_24=166504412=' in source_text, True)
    rows = [dict(i=i, J=j, H=h, a=2 if i < 24 else 166504412,
                 k=3*j+h, length=4*j+h+(2 if i < 24 else 166504412))
            for i, j, h in table]
    check('odd count', sum(row['k'] for row in rows), K)
    check('length', sum(row['length'] for row in rows), N)
    check('even count', N-K, 232565518)
    # Build OOEO separately from its single-letter triples.
    block = (1, 0, 1)
    for letter in ((3, 1, 2), (3, 1, 2), (1, 0, 2), (3, 1, 2)):
        # Modulus is larger than every integer arising here.
        block = concat(block, letter, 1000000)
    check('single-letter block', block, (27, 23, 16))
    primes = sieve(BOUND)
    check('independent complete prime enumeration', primes, trial_primes(BOUND))
    check('prime number', len(primes), 1229)
    check('last prime', primes[-1], 9973)

    prime_records = []
    for p in primes:
        total = (1, 0, 1)
        details = []
        prefix_n = prefix_k = 0
        direct_sum = 0
        for row in rows:
            j, h, a = row['J'], row['H'], row['a']
            triple = modular_word(j, h, a, p)
            c, lift = closed_offset(j, h, p)
            direct_triple = (pow(3, row['k'], p), c, pow(2, row['length'], p))
            check(f'p={p}, row={row["i"]}: full triple', triple, direct_triple)
            total = concat(total, triple, p)
            suffix_k = K-prefix_k-row['k']
            prefix_two = pow(2, prefix_n, p)
            suffix_three = pow(3, suffix_k, p)
            term = c*prefix_two*suffix_three % p
            direct_sum = (direct_sum+term) % p
            details.append(dict(i=row['i'], A=triple[0], C=c, Q=triple[2],
                                lift_mod_11p=lift, prefix_two=prefix_two,
                                suffix_three=suffix_three, contribution=term))
            prefix_n += row['length']
            prefix_k += row['k']
        denominator = (pow(2, N, p)-pow(3, K, p)) % p
        check(f'p={p}: prefix totals', (prefix_k, prefix_n), (K, N))
        check(f'p={p}: independent whole numerator', total[1], direct_sum)
        check(f'p={p}: total A,Q', (total[0], total[2]), (pow(3, K, p), pow(2, N, p)))
        obstruction = denominator == 0 and total[1] != 0
        prime_records.append(dict(p=p, two_N=total[2], three_K=total[0],
                                  denominator=denominator, numerator=total[1],
                                  obstruction=obstruction, words=details))

    candidates = [r for r in prime_records if r['denominator'] == 0]
    obstructions = [r for r in candidates if r['obstruction']]
    common = [r['p'] for r in candidates if not r['obstruction']]
    summary = dict(bound=BOUND, primes_checked=len(primes), largest_prime=primes[-1],
                   checks=checks, failures=len(failures),
                   denominator_prime_divisors=[r['p'] for r in candidates],
                   obstruction_primes=[r['p'] for r in obstructions],
                   common_divisor_primes=common,
                   verdict='NONINTEGRAL' if obstructions else 'NO_VERDICT')
    certificate = dict(source='lemmas/'+SOURCE.name,
                       source_sha256=hashlib.sha256(source_text.encode()).hexdigest(),
                       target='L055 literal 25-word allocation; unshifted n_0',
                       counts=dict(K=K, N=N, L=N-K), parameters=rows,
                       summary=summary, exceptions=[r for r in prime_records if r['p'] in (2, 3, 11)],
                       denominator_cases=candidates, primes=primes,
                       prime_records=prime_records, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required obstruction: denominator == 0 and numerator != 0 modulo p <= 10000.')
    for r in candidates:
        print(f'p={r["p"]}: denominator={r["denominator"]}, numerator={r["numerator"]}, obstruction={r["obstruction"]}')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        print('FAILURES: see /failures in the certificate')
        raise SystemExit(1)


if __name__ == '__main__':
    main()
