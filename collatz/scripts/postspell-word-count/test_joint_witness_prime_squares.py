#!/usr/bin/env python3
"""One fixed order, exactly 5^2 and 431^2; full dual-method evidence."""
from pathlib import Path
from math import isqrt
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'joint-witness-prime-square-certificate.json'
TARGET = "Test L060's fixed two-transposition root modulo 25 and 185761 for a strict numerator/denominator valuation mismatch."
K, N = 397573379, 630138897
ORDER = [8, 1, 2, 3, 4, 5, 6, 12, 0, 9, 10, 11, 7, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


def concat(first, later, m):
    a, c, q = first
    b, d, r = later
    return b*a % m, (b*c + q*d) % m, r*q % m


def power(base, exponent, m):
    # Left-to-right binary powering: consume a bit by doubling the current
    # represented exponent, then adding one if the bit is set.
    value = (1, 0, 1)
    for bit in bin(exponent)[2:]:
        value = concat(value, value, m)
        if bit == '1':
            value = concat(value, base, m)
    return value


def main():
    checks, failures = [], []

    def check(name, actual, required):
        item = dict(name=name, actual=actual, required=required)
        checks.append(item)
        if actual != required:
            failures.append(item)

    inputs = {}
    for lemma in ('L055', 'L056', 'L057', 'L060'):
        matches = list((ROOT / 'lemmas').glob(lemma+'-*.md'))
        check(lemma+' unique canonical file', len(matches), 1)
        path = matches[0]
        raw = path.read_bytes()
        inputs[lemma] = dict(path=str(path.relative_to(ROOT)),
                             sha256=hashlib.sha256(raw).hexdigest())
        if lemma == 'L055':
            source = raw.decode()
    table = [tuple(map(int, r)) for r in
             re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', source, re.M)]
    check('complete input indices', [r[0] for r in table], list(range(25)))
    check('canonical tail prescriptions',
          ['For 0<=i<24 set a_i=2;' in source, 'set a_24=166504412=' in source],
          [True, True])
    rows = [dict(i=i, J=j, H=h, a=2 if i < 24 else 166504412,
                 k=3*j+h, D=4*j+h+(2 if i < 24 else 166504412))
            for i, j, h in table]
    check('positive parameter domain', all(r['J'] >= 2 and r['H'] >= 3 and r['a'] >= 2 for r in rows), True)
    counts = dict(sum_J=sum(r['J'] for r in rows), sum_H=sum(r['H'] for r in rows),
                  sum_a=sum(r['a'] for r in rows), K=sum(r['k'] for r in rows),
                  N=sum(r['D'] for r in rows))
    check('complete allocation counts', list(counts.values()),
          [66061058, 199390205, 166504460, K, N])
    derived_order = list(range(25))
    for a, b in ((0, 8), (7, 12)):
        derived_order[a], derived_order[b] = derived_order[b], derived_order[a]
    check('exact two-transposition order', derived_order, ORDER)
    check('intact permutation', sorted(ORDER), list(range(25)))
    check('fixed large-tail final row', [ORDER[-1], rows[ORDER[-1]]['a']], [24, 166504412])

    # These are proof inputs, not a claim to numerically evaluate huge integers.
    # L055's audited positive log difference proves Delta>0. L056's formula
    # has two positive summands for J,H>0; each positive weight gives Phi>0.
    nonzero = dict(delta='Delta>0 by L055: N log(2)-K log(3)>10584/10^14>0; totals unchanged.',
                   numerator='Phi>0 by L056 positive integral offsets and L057 positive chronological weights.',
                   justification='Each J,H>0, 27>16 and 3>2; 11 divides 27^J-16^J. All weights are positive.')
    primality, evaluations = {}, {}
    for p in (5, 431):
        trials = [dict(divisor=d, remainder=p % d) for d in range(2, isqrt(p)+1)]
        prime = p >= 2 and all(t['remainder'] for t in trials)
        check(f'p={p}: complete trial-divisor primality', prime, True)
        primality[str(p)] = dict(base=p, floor_sqrt=isqrt(p), trials=trials, prime=prime)
        m = p*p
        block = (1, 0, 1)
        for letter in ((3, 1, 2), (3, 1, 2), (1, 0, 2), (3, 1, 2)):
            block = concat(block, letter, m)
        check(f'm={m}: OOEO block', list(block), [27 % m, 23 % m, 16 % m])
        words = []
        for r in rows:
            j, h, tail = r['J'], r['H'], r['a']
            lifted = (pow(27, j, 11*m)-pow(16, j, 11*m)) % (11*m)
            check(f'm={m} row={r["i"]}: lifted difference divisible by 11', lifted % 11, 0)
            c = (23*pow(3, h, m)*(lifted//11)
                 +(pow(3, h, m)-pow(2, h, m))*pow(16, j, m)) % m
            closed = (pow(3, r['k'], m), c, pow(2, r['D'], m))
            composed = concat(concat(power(block, j, m), power((3, 1, 2), h, m), m),
                              power((1, 0, 2), tail, m), m)
            check(f'm={m} row={r["i"]}: independent word triple', list(composed), list(closed))
            words.append(dict(index=r['i'], lifted_modulus=11*m, lifted_difference=lifted,
                              lifted_quotient=lifted//11, closed_triple=list(closed),
                              composed_triple=list(composed)))
        state, term_sum, t, prefix_k, trace = (1, 0, 1), 0, 0, 0, []
        for position, i in enumerate(ORDER):
            r = rows[i]
            u = K-prefix_k-r['k']
            check(f'm={m} position={position}: suffix exponent', u,
                  sum(rows[v]['k'] for v in ORDER[position+1:]))
            two, three = pow(2, t, m), pow(3, u, m)
            term = words[i]['closed_triple'][1]*two*three % m
            previous = state
            state = concat(state, words[i]['composed_triple'], m)
            term_sum += term
            trace.append(dict(position=position, index=i, prefix_N=t, suffix_K=u,
                              prefix_two=two, suffix_three=three, term=term,
                              previous_triple=list(previous), resulting_triple=list(state)))
            t += r['D']
            prefix_k += r['k']
            check(f'm={m} position={position}: composed prefix powers', [state[0], state[2]],
                  [pow(3, prefix_k, m), pow(2, t, m)])
        two_total, three_total = pow(2, N, m), pow(3, K, m)
        phi, delta = term_sum % m, (two_total-three_total) % m
        check(f'm={m}: complete dual-method numerator', state[1], phi)
        check(f'm={m}: final total exponents', [prefix_k, t], [K, N])
        check(f'm={m}: full composed triple', list(state), [three_total, phi, two_total])
        check(f'm={m}: inherited common zeros', [phi % p, delta % p], [0, 0])
        # Only precision two is evaluated; zero residues are lower bounds.
        numerator_v = '>=2' if phi == 0 else '=1'
        denominator_v = '>=2' if delta == 0 else '=1'
        if phi != 0 and delta == 0:
            verdict = 'STRICT_DENOMINATOR_EXCESS_NONINTEGRAL'
        elif delta != 0:
            verdict = 'DENOMINATOR_PRIME_CANCELS'
        else:
            verdict = 'INCONCLUSIVE_AT_SQUARE_PRECISION'
        evaluations[str(m)] = dict(base=p, modulus=m, words=words, trace=trace,
                                   term_sum=term_sum, phi=phi, two_total=two_total,
                                   three_total=three_total, delta=delta,
                                   final_triple=list(state), numerator_valuation=numerator_v,
                                   denominator_valuation=denominator_v, verdict=verdict)
    decisive = [v['base'] for v in evaluations.values()
                if v['verdict'] == 'STRICT_DENOMINATOR_EXCESS_NONINTEGRAL']
    summary = dict(verdict='REPAIR_REQUIRED' if failures else 'NONINTEGRAL' if decisive else 'NO_STRICT_DENOMINATOR_EXCESS_CERTIFIED',
                   decisive_primes=decisive, actual_precision=2, required_precision=2,
                   moduli=[25, 185761], rows_per_modulus=25, checks=len(checks), failures=len(failures),
                   residues={m: {k: v[k] for k in ('phi', 'two_total', 'three_total', 'delta',
                                                  'numerator_valuation', 'denominator_valuation', 'verdict')}
                             for m, v in evaluations.items()})
    OUT.write_text(json.dumps(dict(target=TARGET, inputs=inputs, parameters=rows, counts=counts,
                                    order=ORDER, swaps=[[0, 8], [7, 12]], nonzero=nonzero,
                                    primality=primality, evaluations=evaluations,
                                    checks=checks, failures=failures, summary=summary), indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: a strict denominator valuation excess for this fixed order; stop at both squares regardless.')
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
