#!/usr/bin/env python3
"""One fixed order, bounded powers of five, two exact evaluations."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
OUT = HERE / 'swapped-root-five-adic-cancellation-certificate.json'
K, N, CAP = 397573379, 630138897, 8
TARGET = "Determine whether the reduced denominator of L057's swapped-order root is divisible by 5."


def concat(first, second, modulus):
    a, c, q = first
    b, d, r = second
    return (b*a % modulus, (b*c+q*d) % modulus, r*q % modulus)


def repeat(base, exponent, modulus):
    result = (1, 0, 1)
    while exponent:
        if exponent & 1:
            result = concat(result, base, modulus)
        base = concat(base, base, modulus)
        exponent //= 2
    return result


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

    check('indices', [x[0] for x in table], list(range(25)))
    check('short tails', 'For 0<=i<24 set a_i=2;' in source, True)
    check('last tail', 'set a_24=166504412=' in source, True)
    rows = [dict(i=i, J=j, H=h, a=2 if i < 24 else 166504412,
                 k=3*j+h, D=4*j+h+(2 if i < 24 else 166504412))
            for i, j, h in table]
    check('odd count', sum(r['k'] for r in rows), K)
    check('length', sum(r['D'] for r in rows), N)
    order = list(range(25))
    order[0], order[6] = order[6], order[0]
    check('intact multiplicities', sorted(order), list(range(25)))
    check('closing row', order[-1], 24)
    records = []
    numerator_v = denominator_v = None
    verdict = 'UNDECIDED_CAP'
    for e in range(1, CAP+1):
        modulus = 5**e
        inverse = pow(11, -1, modulus)
        check(f'e={e}: unit inverse', 11*inverse % modulus, 1)
        state = (1, 0, 1)
        prefix_n = prefix_k = weighted = 0
        trace = []
        for position, index in enumerate(order):
            row = rows[index]
            j, h, a = row['J'], row['H'], row['a']
            offset = (23*pow(3, h, modulus)
                      *(pow(27, j, modulus)-pow(16, j, modulus))*inverse
                      +(pow(3, h, modulus)-pow(2, h, modulus))
                      *pow(16, j, modulus)) % modulus
            closed = (pow(3, row['k'], modulus), offset,
                      pow(2, row['D'], modulus))
            # Independent route starts with the single-letter triples.
            block = (1, 0, 1)
            for letter in [(3, 1, 2), (3, 1, 2), (1, 0, 2), (3, 1, 2)]:
                block = concat(block, letter, modulus)
            composed = concat(concat(repeat(block, j, modulus),
                                     repeat((3, 1, 2), h, modulus), modulus),
                              repeat((1, 0, 2), a, modulus), modulus)
            check(f'e={e}: row {index} formulas', list(composed), list(closed))
            suffix_k = K-prefix_k-row['k']
            two, three = pow(2, prefix_n, modulus), pow(3, suffix_k, modulus)
            term = offset*two*three % modulus
            weighted = (weighted+term) % modulus
            previous = state
            state = concat(state, composed, modulus)
            trace.append(dict(position=position, index=index, prefix_N=prefix_n,
                              prefix_K=prefix_k, suffix_K=suffix_k,
                              closed_triple=closed, composed_triple=composed,
                              prefix_two=two, suffix_three=three, term=term,
                              previous_triple=previous, resulting_triple=state))
            prefix_n += row['D']
            prefix_k += row['k']
        delta = (pow(2, N, modulus)-pow(3, K, modulus)) % modulus
        check(f'e={e}: totals', [prefix_k, prefix_n], [K, N])
        check(f'e={e}: numerator evaluations', state[1], weighted)
        check(f'e={e}: powers', [state[0], state[2]],
              [pow(3, K, modulus), pow(2, N, modulus)])
        record = dict(e=e, modulus=modulus, numerator=weighted,
                      denominator=delta, total_triple=state, trace=trace)
        if e == 1:
            check('L057 residues', [weighted, delta], [0, 0])
        if records:
            check(f'e={e}: compatible residues',
                  [weighted % records[-1]['modulus'], delta % records[-1]['modulus']],
                  [records[-1]['numerator'], records[-1]['denominator']])
        records.append(record)
        if weighted != 0 and numerator_v is None:
            numerator_v = e-1
        if delta != 0 and denominator_v is None:
            denominator_v = e-1
        if numerator_v is not None and (denominator_v is None or denominator_v > numerator_v):
            verdict = 'FIVE_SURVIVES_REDUCED_DENOMINATOR'
            break
        if denominator_v is not None and (numerator_v is None or numerator_v >= denominator_v):
            verdict = 'COMPLETE_PRIME_FIVE_CANCELLATION'
            break
    summary = dict(verdict=verdict, actual_exponent=records[-1]['e'],
                   required_cap=CAP, numerator_valuation=numerator_v,
                   denominator_valuation=denominator_v,
                   numerator_divisible_through=(records[-1]['e'] if numerator_v is None else numerator_v),
                   denominator_divisible_through=(records[-1]['e'] if denominator_v is None else denominator_v),
                   checks=len(checks), failures=len(failures))
    certificate = dict(target=TARGET, source='lemmas/'+SOURCE.name,
                       source_sha256=hashlib.sha256(raw).hexdigest(),
                       counts=dict(K=K, N=N), parameters=rows, order=order,
                       records=records, summary=summary, checks=checks, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: decisive valuation comparison; maximum modulus 5^8.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
