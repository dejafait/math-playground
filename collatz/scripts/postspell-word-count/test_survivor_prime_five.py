#!/usr/bin/env python3
"""L065 literal changed tails: one modulus, two complete exact evaluations."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
TARGET = "Determine whether prime 5 survives in the reduced denominator of L065's exact j=23 unshifted cyclic root by comparing its numerator and denominator modulo 25."
OUT = HERE / 'survivor-prime-five-certificate.json'
K, N, M = 397573379, 630138897, 25


def concat(first, second):
    a, c, q = first
    b, d, r = second
    return (b*a % M, (b*c+q*d) % M, r*q % M)


def repeat(base, exponent):
    result = (1, 0, 1)
    while exponent:
        if exponent & 1:
            result = concat(result, base)
        base = concat(base, base)
        exponent //= 2
    return result


def main():
    sources = {}
    texts = {}
    for name in ['L055-fixed-count-twenty-five-word-real-witness.md',
                 'L064-single-tail-redistribution-j-guard-classification.md',
                 'L065-single-tail-survivor-remaining-real-guards.md']:
        raw = (ROOT / 'lemmas' / name).read_bytes()
        sources['lemmas/'+name] = hashlib.sha256(raw).hexdigest()
        texts[name[:4]] = raw.decode()
    table = [tuple(map(int, row)) for row in
             re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', texts['L055'], re.M)]
    checks, failures = [], []

    def check(name, actual, required):
        record = dict(name=name, actual=actual, required=required)
        checks.append(record)
        if actual != required:
            failures.append(record)

    check('indices', [r[0] for r in table], list(range(25)))
    check('L065 changed-tail statement',
          'with a_23=20, a_24=166504394 and a_i=2 at every other index.' in texts['L065'], True)
    rows = []
    for i, j, h in table:
        a = 20 if i == 23 else 166504394 if i == 24 else 2
        rows.append(dict(i=i, J=j, H=h, a=a, k=3*j+h, D=4*j+h+a))
    check('J sum', sum(r['J'] for r in rows), 66061058)
    check('H sum', sum(r['H'] for r in rows), 199390205)
    check('tail sum', sum(r['a'] for r in rows), 166504460)
    check('K sum', sum(r['k'] for r in rows), K)
    check('N sum', sum(r['D'] for r in rows), N)
    check('positive J,H', all(r['J'] > 0 and r['H'] > 0 for r in rows), True)
    inv = pow(11, -1, M)
    check('unit inverse 11', [inv, 11*inv % M], [16, 1])
    block = (1, 0, 1)
    for letter in [(3, 1, 2), (3, 1, 2), (1, 0, 2), (3, 1, 2)]:
        block = concat(block, letter)
    check('OOEO triple', list(block), [27 % M, 23, 16])
    trace = []
    state = (1, 0, 1)
    weighted = 0
    for row in rows:
        i, j, h, a = row['i'], row['J'], row['H'], row['a']
        # Prefix and suffix exponents are direct full sums.
        t = sum(r['D'] for r in rows[:i])
        u = sum(r['k'] for r in rows[i+1:])
        offset = (23*pow(3, h, M)*(pow(27, j, M)-pow(16, j, M))*inv
                  +(pow(3, h, M)-pow(2, h, M))*pow(16, j, M)) % M
        closed = (pow(3, row['k'], M), offset, pow(2, row['D'], M))
        composed = concat(concat(repeat(block, j), repeat((3, 1, 2), h)),
                          repeat((1, 0, 2), a))
        check(f'row {i}: two triples', list(composed), list(closed))
        two, three = pow(2, t, M), pow(3, u, M)
        term = offset*two*three % M
        weighted = (weighted+term) % M
        before = state
        state = concat(state, composed)
        trace.append(dict(**row, prefix_N=t, suffix_K=u, offset=offset,
                          prefix_two=two, suffix_three=three, contribution=term,
                          closed_triple=closed, composed_triple=composed,
                          before_triple=before, after_triple=state))
    power2, power3 = pow(2, N, M), pow(3, K, M)
    delta = (power2-power3) % M
    check('numerator evaluations', state[1], weighted)
    check('whole count powers', [state[0], state[2]], [power3, power2])
    check('denominator powers', [N % 20, K % 20, power2, power3, delta],
          [17, 19, 22, 17, 5])
    numerator_v = 0 if weighted % 5 else 1 if weighted else None
    verdict = ('FIVE_SURVIVES_REDUCED_DENOMINATOR' if weighted % 5
               else 'COMPLETE_PRIME_FIVE_CANCELLATION')
    summary = dict(modulus=M, required_modulus=25, numerator=weighted,
                   denominator=delta, numerator_valuation=numerator_v,
                   numerator_valuation_lower_bound=2 if weighted == 0 else numerator_v,
                   denominator_valuation=1, verdict=verdict,
                   contribution_sum=sum(r['contribution'] for r in trace),
                   total_triple=state, checks=len(checks), failures=len(failures))
    certificate = dict(target=TARGET, sources=sources, counts=dict(K=K, N=N),
                       parameters=rows, trace=trace, summary=summary,
                       checks=checks, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: all 25 contributions agree with division-free composition; Delta has exact valuation 1. Stop at modulus 25.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
