#!/usr/bin/env python3
"""Exactly two L079 survivors, modulus 25; no parameter/factor search."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'redistributed-h-survivors-mod25-certificate.json'
TARGET = 'Evaluate the complete unshifted affine numerator and denominator modulo 25 for both L079 survivors t=0,1, testing whether a factor 5 survives reduction.'
M, K, N, B = 25, 397573379, 630138897, 9250245


def concat(first, second):
    a, f, q = first
    b, g, r = second
    return (b*a % M, (b*f+q*g) % M, r*q % M)


def repeat(base, exponent):
    result = (1, 0, 1)
    while exponent:
        if exponent & 1:
            result = concat(result, base)
        base = concat(base, base)
        exponent //= 2
    return result


def main():
    sources, texts = {}, {}
    for name in ['L055-fixed-count-twenty-five-word-real-witness.md',
                 'L078-variable-table-finite-survivor-divisibility-criterion.md',
                 'L079-redistributed-h-table-data-certificate.md']:
        raw = (ROOT / 'lemmas' / name).read_bytes()
        sources['lemmas/'+name] = hashlib.sha256(raw).hexdigest()
        texts[name[:4]] = raw.decode()
    table = [tuple(map(int, row)) for row in
             re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', texts['L055'], re.M)]
    checks, failures = [], []

    def check(name, actual, required):
        entry = dict(name=name, actual=actual, required=required)
        checks.append(entry)
        if actual != required:
            failures.append(entry)

    check('full original indices', [r[0] for r in table], list(range(25)))
    check('original boundary H', [table[0][2], table[24][2]], [40, 32670621])
    check('L079 replacements stated',
          'H_0=40 by 39 and H_24=32670621 by 32670622' in texts['L079'], True)
    check('unit inverse 11', 11*16 % M, 1)
    odd, even = (3, 1, 2), (1, 0, 2)
    block = (1, 0, 1)
    for letter in [odd, odd, even, odd]:
        block = concat(block, letter)
    check('OOEO triple', list(block), [2, 23, 16])
    cases = []
    for t in [0, 1]:
        rows = []
        for i, j, old_h in table:
            h = 39 if i == 0 else 32670622 if i == 24 else old_h
            beta = t if i == 23 else B-t if i == 24 else 0
            a = 2+18*beta
            rows.append(dict(i=i, J=j, H=h, beta=beta, a=a,
                             k=3*j+h, d=4*j+h+a))
        check(f't={t} counts',
              [sum(r[key] for r in rows) for key in ['J', 'H', 'beta', 'a', 'k', 'd']],
              [66061058, 199390205, B, 166504460, K, N])
        check(f't={t} tail qualifications', all(r['a'] >= 2 and r['a'] % 18 == 2 for r in rows), True)
        trace, state, weighted = [], (1, 0, 1), 0
        for row in rows:
            i, j, h, a = row['i'], row['J'], row['H'], row['a']
            prefix_n = sum(r['d'] for r in rows[:i])
            suffix_k = sum(r['k'] for r in rows[i+1:])
            offset = (23*pow(3, h, M)*(pow(27, j, M)-pow(16, j, M))*16
                      +(pow(3, h, M)-pow(2, h, M))*pow(16, j, M)) % M
            closed = (pow(3, row['k'], M), offset, pow(2, row['d'], M))
            composed = concat(concat(repeat(block, j), repeat(odd, h)), repeat(even, a))
            check(f't={t} row {i} triple', list(composed), list(closed))
            two, three = pow(2, prefix_n, M), pow(3, suffix_k, M)
            term = offset*two*three % M
            weighted = (weighted+term) % M
            before = state
            state = concat(state, composed)
            trace.append(dict(**row, prefix_N=prefix_n, suffix_K=suffix_k,
                              offset=offset, prefix_two=two, suffix_three=three,
                              contribution=term, closed_triple=closed,
                              composed_triple=composed, before_triple=before,
                              after_triple=state))
        # Evaluate both denominator powers afresh for each allocation.
        power2, power3 = pow(2, sum(r['d'] for r in rows), M), pow(3, sum(r['k'] for r in rows), M)
        delta = (power2-power3) % M
        check(f't={t} numerator agreement', state[1], weighted)
        check(f't={t} composed denominator powers', [state[2], state[0]], [power2, power3])
        # Independent period-20 evaluation of both count powers.
        check(f't={t} denominator period check',
              [pow(2, 20, M), pow(3, 20, M), N % 20, K % 20, power2, power3, delta],
              [1, 1, 17, 19, 22, 17, 5])
        numerator_v = 0 if weighted % 5 else 1 if weighted else None
        verdict = ('FIVE_SURVIVES_REDUCED_DENOMINATOR' if weighted % 5
                   else 'COMPLETE_PRIME_FIVE_CANCELLATION')
        summary = dict(t=t, modulus=M, required_modulus=25, numerator=weighted,
                       denominator=delta, numerator_valuation=numerator_v,
                       numerator_valuation_lower_bound=2 if weighted == 0 else numerator_v,
                       denominator_valuation=1, verdict=verdict,
                       contribution_sum=sum(r['contribution'] for r in trace),
                       total_triple=state)
        cases.append(dict(t=t, trace=trace, summary=summary))
    certificate = dict(target=TARGET, sources=sources, counts=dict(K=K, N=N),
                       cases=cases, checks=checks, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    for case in cases:
        print(json.dumps(case['summary'], sort_keys=True))
    print(f'Checks: {len(checks)}; failures: {len(failures)}; actual/required modulus: 25/25.')
    print('Required: all 50 row triples and both complete numerators agree; denominator valuation exactly 1.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        print(json.dumps(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
