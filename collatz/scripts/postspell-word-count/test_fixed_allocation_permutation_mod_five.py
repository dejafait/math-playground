#!/usr/bin/env python3
"""Bounded intact-triple swaps; two complete modulo-five evaluations."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
OUT = HERE / 'fixed-allocation-permutation-mod-five-certificate.json'
P = 5
K, N = 397573379, 630138897


def concat(first, second):
    a, c, q = first
    b, d, r = second
    return b*a % P, (b*c + q*d) % P, r*q % P


def repeat(base, exponent):
    value = (1, 0, 1)
    while exponent:
        if exponent & 1:
            value = concat(value, base)
        base = concat(base, base)
        exponent //= 2
    return value


def main():
    source = SOURCE.read_bytes()
    source_text = source.decode()
    table = [tuple(map(int, row)) for row in
             re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source_text, re.M)]
    failures = []
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, actual=actual, required=required))
        if actual != required:
            failures.append(checks[-1])

    check('indices', [row[0] for row in table], list(range(25)))
    check('short-tail source statement', 'For 0<=i<24 set a_i=2;' in source_text, True)
    check('large-tail source statement', 'set a_24=166504412=' in source_text, True)
    rows = []
    for i, j, h in table:
        a = 2 if i < 24 else 166504412
        k, length = 3*j+h, 4*j+h+a
        triple = concat(concat(repeat((27 % P, 23 % P, 16 % P), j),
                               repeat((3, 1, 2), h)), repeat((1, 0, 2), a))
        # 11 is 1 mod 5, so the exact quotient reduces without an inverse.
        offset = (3*pow(3, h, P)*(pow(2, j, P)-1)
                  + pow(3, h, P)-pow(2, h, P)) % P
        direct = (pow(3, k, P), offset, pow(2, length, P))
        check(f'word {i}: compressed / closed formula', triple, direct)
        rows.append(dict(i=i, J=j, H=h, a=a, k=k, length=length,
                         A=triple[0], C=triple[1], Q=triple[2]))
    check('total odd count', sum(row['k'] for row in rows), K)
    check('total length', sum(row['length'] for row in rows), N)
    denominator = (pow(2, N, P)-pow(3, K, P)) % P
    check('denominator residue', denominator, 0)

    def evaluate(order):
        check('intact-index multiplicities', sorted(order), list(range(25)))
        state = (1, 0, 1)
        prefix_n = prefix_k = direct_sum = 0
        trace = []
        for position, index in enumerate(order):
            row = rows[index]
            suffix_k = K-prefix_k-row['k']
            two = pow(2, prefix_n, P)
            three = pow(3, suffix_k, P)
            term = row['C']*two*three % P
            direct_sum = (direct_sum+term) % P
            previous = state
            state = concat(state, (row['A'], row['C'], row['Q']))
            trace.append(dict(position=position, index=index,
                              prefix_N=prefix_n, prefix_K=prefix_k,
                              suffix_K=suffix_k, prefix_two=two,
                              suffix_three=three, contribution=term,
                              previous_triple=previous, resulting_triple=state))
            prefix_n += row['length']
            prefix_k += row['k']
        check('order totals', [prefix_k, prefix_n], [K, N])
        check('two whole-numerator evaluations', state[1], direct_sum)
        check('whole slope and denominator power', [state[0], state[2]],
              [pow(3, K, P), pow(2, N, P)])
        return dict(order=order, numerator=state[1], weighted_sum=direct_sum,
                    contribution_sum=sum(record['contribution'] for record in trace),
                    total_triple=state, trace=trace)

    literal = evaluate(list(range(25)))
    check('literal numerator matches L056', literal['numerator'], 4)
    tested = []
    witness = None
    for i in range(25):
        for j in range(i+1, 25):
            order = list(range(25))
            order[i], order[j] = order[j], order[i]
            result = evaluate(order)
            tested.append(dict(swap=[i, j], numerator=result['numerator']))
            if result['numerator'] == 0:
                witness = result
                witness['swap'] = [i, j]
                break
        if witness is not None:
            break
    verdict = 'UNIFORM_PRIME_FIVE_EXCLUSION_FAILS' if witness else 'BOUNDED_SEARCH_NO_VERDICT'
    summary = dict(verdict=verdict, modulus=P, maximum_swaps=300,
                   swaps_tested=len(tested), checks=len(checks), failures=len(failures),
                   denominator=denominator,
                   witness_numerator=None if witness is None else witness['numerator'],
                   witness_swap=None if witness is None else witness['swap'])
    certificate = dict(target="Decide whether modulo 5 excludes every permutation of L055's 25 fixed word triples.",
                       source='lemmas/'+SOURCE.name,
                       source_sha256=hashlib.sha256(source).hexdigest(),
                       counts=dict(K=K, N=N), parameters=rows, literal=literal,
                       tested_swaps=tested, witness=witness, summary=summary,
                       checks=checks, failures=failures)
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required stop: an intact-triple permutation with numerator = denominator = 0 mod 5.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
