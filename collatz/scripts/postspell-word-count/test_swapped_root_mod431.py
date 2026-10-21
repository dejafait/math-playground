#!/usr/bin/env python3
"""Evaluate only the approved swapped-order unshifted root at modulus 431."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
OUT = HERE / 'swapped-root-mod431-certificate.json'
K, N, M = 397573379, 630138897, 431
TARGET = "Test whether modulo 431 excludes integer realization of L057's fixed swapped-order root."


def concat(first, later):
    a, c, q = first
    b, d, r = later
    return (b*a % M, (b*c+q*d) % M, r*q % M)


def power(base, exponent):
    # After each bit, value is base raised to the consumed binary prefix.
    value = (1, 0, 1)
    for bit in bin(exponent)[2:]:
        value = concat(value, value)
        if bit == '1':
            value = concat(value, base)
    return value


def main():
    raw = SOURCE.read_bytes()
    source = raw.decode()
    table = [tuple(map(int, row)) for row in
             re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
    checks, failures = [], []

    def check(name, actual, required):
        record = dict(name=name, actual=actual, required=required)
        checks.append(record)
        if actual != required:
            failures.append(record)

    check('indices', [r[0] for r in table], list(range(25)))
    check('tail prescription', ['For 0<=i<24 set a_i=2;' in source,
                               'set a_24=166504412=' in source], [True, True])
    rows = [dict(i=i, J=j, H=h, a=2 if i < 24 else 166504412,
                 k=3*j+h, D=4*j+h+(2 if i < 24 else 166504412))
            for i, j, h in table]
    check('allocation sums', [sum(r['J'] for r in rows),
                             sum(r['H'] for r in rows),
                             sum(r['a'] for r in rows)],
          [66061058, 199390205, 166504460])
    check('counts', [sum(r['k'] for r in rows), sum(r['D'] for r in rows)], [K, N])
    order = list(range(25))
    order[0], order[6] = order[6], order[0]
    check('intact multiplicities', sorted(order), list(range(25)))
    check('closing tail', rows[order[-1]]['a'], 166504412)

    block = (1, 0, 1)
    for letter in [(3, 1, 2), (3, 1, 2), (1, 0, 2), (3, 1, 2)]:
        block = concat(block, letter)
    check('OOEO', list(block), [27, 23, 16])
    state = (1, 0, 1)
    prefix_n = prefix_k = term_sum = 0
    trace = []
    for position, index in enumerate(order):
        row = rows[index]
        j, h, tail = row['J'], row['H'], row['a']
        # If T is divisible by 11, (T mod 11M)/11 represents T/11 mod M.
        lifted = (pow(27, j, 11*M)-pow(16, j, 11*M)) % (11*M)
        check(f'row {index}: lifted exact division', lifted % 11, 0)
        c = (23*pow(3, h, M)*(lifted//11)
             +(pow(3, h, M)-pow(2, h, M))*pow(16, j, M)) % M
        closed = (pow(3, row['k'], M), c, pow(2, row['D'], M))
        composed = concat(concat(power(block, j), power((3, 1, 2), h)),
                          power((1, 0, 2), tail))
        check(f'row {index}: closed versus division-free', list(closed), list(composed))
        # Recompute each prefix and suffix as full finite sums, independently
        # of the running exponents, before using their powers.
        t = sum(rows[i]['D'] for i in order[:position])
        u = sum(rows[i]['k'] for i in order[position+1:])
        check(f'position {position}: exponents', [prefix_n, K-prefix_k-row['k']], [t, u])
        two, three = pow(2, t, M), pow(3, u, M)
        term = c*two*three % M
        term_sum += term
        previous = state
        state = concat(state, composed)
        prefix_n += row['D']
        prefix_k += row['k']
        check(f'position {position}: partial powers', [state[0], state[2]],
              [pow(3, prefix_k, M), pow(2, prefix_n, M)])
        trace.append(dict(position=position, index=index, prefix_N=t, suffix_K=u,
                          lifted_difference=lifted, lifted_quotient=lifted//11,
                          closed_triple=list(closed), composed_triple=list(composed),
                          prefix_two=two, suffix_three=three, term=term,
                          previous_triple=list(previous), resulting_triple=list(state)))
    two_total, three_total = pow(2, N, M), pow(3, K, M)
    delta = (two_total-three_total) % M
    numerator = term_sum % M
    check('total exponents', [prefix_k, prefix_n], [K, N])
    check('weighted versus chronological numerator', numerator, state[1])
    check('denominator reproduced', delta, 0)
    summary = dict(modulus=M, numerator=numerator, denominator=delta,
                   two_total=two_total, three_total=three_total, term_sum=term_sum,
                   checks=len(checks), failures=len(failures),
                   verdict=('REPAIR_REQUIRED' if failures else
                            'NONINTEGRAL' if delta == 0 and numerator != 0 else
                            'COMMON_ZERO_STOP'))
    evidence = dict(target=TARGET, source='lemmas/'+SOURCE.name,
                    source_sha256=hashlib.sha256(raw).hexdigest(),
                    counts=dict(K=K, N=N), order=order, parameters=rows,
                    trace=trace, summary=summary, checks=checks, failures=failures)
    OUT.write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: denominator = 0 and numerator != 0 modulo 431; exactly 25 intact rows.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
