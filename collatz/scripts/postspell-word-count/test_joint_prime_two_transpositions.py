#!/usr/bin/env python3
"""Approved intact-order test at moduli 5 and 431; stop at a common zero.

All evidence is written to disk. No integer itinerary or guards are inferred.
"""
from pathlib import Path
from itertools import combinations
from math import comb
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
OUT = HERE / 'joint-prime-two-transposition-certificate.json'
TARGET = "Test joint modulo-5 and modulo-431 nonvanishing for all orders obtained from L055's literal order by at most two transpositions among indices 0 through 23."
K, N = 397573379, 630138897
MODULI = (5, 431)


def concat(first, later, modulus):
    a, c, q = first
    b, d, r = later
    return b*a % modulus, (b*c + q*d) % modulus, r*q % modulus


def power(base, exponent, modulus):
    value = (1, 0, 1)
    for bit in bin(exponent)[2:]:
        value = concat(value, value, modulus)
        if bit == '1':
            value = concat(value, base, modulus)
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

    check('literal indices', [r[0] for r in table], list(range(25)))
    check('tail prescriptions', ['For 0<=i<24 set a_i=2;' in source,
                                'set a_24=166504412=' in source], [True, True])
    rows = [dict(i=i, J=j, H=h, a=2 if i < 24 else 166504412,
                 k=3*j+h, D=4*j+h+(2 if i < 24 else 166504412))
            for i, j, h in table]
    check('allocation sums', [sum(r['J'] for r in rows), sum(r['H'] for r in rows),
                              sum(r['a'] for r in rows)],
          [66061058, 199390205, 166504460])
    check('total exponents', [sum(r['k'] for r in rows), sum(r['D'] for r in rows)], [K, N])

    triples, words, denominator = {}, {}, {}
    for m in MODULI:
        block = (1, 0, 1)
        for letter in ((3, 1, 2), (3, 1, 2), (1, 0, 2), (3, 1, 2)):
            block = concat(block, letter, m)
        check(f'm={m}: OOEO', list(block), [27 % m, 23 % m, 16 % m])
        triples[m], words[m] = [], []
        for r in rows:
            j, h, tail = r['J'], r['H'], r['a']
            lifted = (pow(27, j, 11*m)-pow(16, j, 11*m)) % (11*m)
            check(f'm={m} row={r["i"]}: lifted quotient', lifted % 11, 0)
            c = (23*pow(3, h, m)*(lifted//11)
                 +(pow(3, h, m)-pow(2, h, m))*pow(16, j, m)) % m
            closed = (pow(3, r['k'], m), c, pow(2, r['D'], m))
            composed = concat(concat(power(block, j, m), power((3, 1, 2), h, m), m),
                              power((1, 0, 2), tail, m), m)
            check(f'm={m} row={r["i"]}: two evaluations', list(composed), list(closed))
            triples[m].append(composed)
            words[m].append(dict(index=r['i'], lifted_difference=lifted,
                                 lifted_quotient=lifted//11, closed_triple=list(closed),
                                 composed_triple=list(composed)))
        two, three = pow(2, N, m), pow(3, K, m)
        denominator[m] = dict(two_total=two, three_total=three, delta=(two-three) % m)
        check(f'm={m}: denominator zero', denominator[m]['delta'], 0)

    # The search evaluator uses division-free triples. The independent sum
    # uses the closed-offset triples, suffix A products and prefix Q products.
    def evaluate(order, m):
        state = (1, 0, 1)
        for i in order:
            state = concat(state, triples[m][i], m)
        suffix = [1]*26
        for p in range(24, -1, -1):
            suffix[p] = suffix[p+1]*words[m][order[p]]['closed_triple'][0] % m
        total, prefix = 0, 1
        for p, i in enumerate(order):
            _, c, q = words[m][i]['closed_triple']
            total = (total + c*prefix*suffix[p+1]) % m
            prefix = prefix*q % m
        return state, total

    identity = tuple(range(25))
    for name, order, required in [('literal', identity, [4, 240]),
                                  ('L057 swap', tuple([6, 1, 2, 3, 4, 5, 0]+list(range(7, 25))), [0, 240])]:
        check(f'{name}: known residues', [evaluate(order, m)[0][1] for m in MODULI], required)

    swaps = list(combinations(range(24), 2))
    sequences_required = 1+len(swaps)+len(swaps)**2
    # Cycle types with transposition distance <=2: identity, a transposition,
    # a three-cycle, or two disjoint transpositions. This count is an optional
    # independent exhaustive-coverage check, not needed for a witness stop.
    unique_required = 1+comb(24, 2)+2*comb(24, 3)+3*comb(24, 4)

    def sequences():
        yield ()
        for s in swaps:
            yield (s,)
        for s in swaps:
            for t in swaps:
                yield (s, t)

    seen, records = set(), []
    processed = duplicates = evaluations = comparison_failures = 0
    witness = None
    for sequence in sequences():
        processed += 1
        order = list(identity)
        for a, b in sequence:
            order[a], order[b] = order[b], order[a]
        order = tuple(order)
        if order in seen:
            duplicates += 1
            continue
        seen.add(order)
        residues = []
        for m in MODULI:
            state, weighted = evaluate(order, m)
            evaluations += 1
            if state != (denominator[m]['three_total'], weighted, denominator[m]['two_total']):
                comparison_failures += 1
                failures.append(dict(name='per-order independent comparison', order=order,
                                     modulus=m, actual=state, weighted=weighted))
            residues.append(state[1])
        records.append(dict(sequence=sequence, order=order, residues=residues))
        if residues == [0, 0] and not failures:
            witness = records[-1]
            break

    traces = {}
    if witness:
        order = witness['order']
        check('witness intact multiplicities', sorted(order), list(range(25)))
        check('witness final index', order[-1], 24)
        check('witness closing tail', rows[order[-1]]['a'], 166504412)
        for m in MODULI:
            state, term_sum, trace = (1, 0, 1), 0, []
            for p, i in enumerate(order):
                t = sum(rows[v]['D'] for v in order[:p])
                u = sum(rows[v]['k'] for v in order[p+1:])
                two, three = pow(2, t, m), pow(3, u, m)
                closed = words[m][i]['closed_triple']
                term = closed[1]*two*three % m
                previous = state
                state = concat(state, triples[m][i], m)
                term_sum += term
                trace.append(dict(position=p, index=i, prefix_N=t, suffix_K=u,
                                  **{k: v for k, v in words[m][i].items() if k != 'index'},
                                  prefix_two=two, suffix_three=three, term=term,
                                  previous_triple=list(previous), resulting_triple=list(state)))
                check(f'm={m} position={p}: partial powers', [state[0], state[2]],
                      [pow(3, sum(rows[v]['k'] for v in order[:p+1]), m),
                       pow(2, sum(rows[v]['D'] for v in order[:p+1]), m)])
            check(f'm={m}: witness independent weighted zero', [term_sum % m, state[1]], [0, 0])
            traces[m] = dict(trace=trace, term_sum=term_sum, final_triple=list(state),
                             **denominator[m])
    else:
        check('exhaustive sequence count', processed, sequences_required)
        check('exhaustive unique count', len(seen), unique_required)

    summary = dict(verdict='REPAIR_REQUIRED' if failures else 'COMMON_ZERO_STOP' if witness else 'EXHAUSTIVE_NONVANISHING',
                   moduli=MODULI, sequences_actual=processed, sequences_required=sequences_required,
                   unique_orders_actual=len(seen), unique_orders_required_for_exhaustion=unique_required,
                   duplicate_sequences=duplicates, evaluations=evaluations,
                   per_order_comparison_failures=comparison_failures, checks=len(checks), failures=len(failures),
                   exhaustive=witness is None)
    evidence = dict(target=TARGET, source='lemmas/'+SOURCE.name,
                    source_sha256=hashlib.sha256(raw).hexdigest(), parameters=rows, counts=dict(K=K, N=N),
                    word_evidence=words, denominator=denominator, summary=summary,
                    witness=witness, witness_evidence=traces, search_records=records, checks=checks, failures=failures)
    OUT.write_text(json.dumps(evidence, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: one certified common-zero order, or all 76453 sequences / 36203 distinct orders with no common zero.')
    if witness:
        print('Witness swaps:', witness['sequence'])
        print('Witness order:', witness['order'])
        print('Witness residues:', witness['residues'])
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
