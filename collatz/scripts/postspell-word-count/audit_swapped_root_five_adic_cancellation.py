#!/usr/bin/env python3
"""Independent exhaustive residue-map audit, only moduli 5 and 25."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
CLAIM = ROOT / 'lemmas/L058-swapped-root-complete-prime-five-cancellation.md'
ORIGINAL = HERE / 'swapped-root-five-adic-cancellation-certificate.json'
OUT = HERE / 'swapped-root-five-adic-cancellation-audit-certificate.json'


def main():
    source = SOURCE.read_bytes()
    rows = []
    for line in source.decode().splitlines():
        if line.startswith('|'):
            cells = [x.strip() for x in line.strip('|').split('|')]
            if len(cells) == 3 and all(x.isdecimal() for x in cells):
                i, j, h = map(int, cells)
                a = 2 if i < 24 else 166504412
                rows.append(dict(i=i, J=j, H=h, a=a, k=3*j+h, D=4*j+h+a))
    K, N = sum(r['k'] for r in rows), sum(r['D'] for r in rows)
    order = [6, 1, 2, 3, 4, 5, 0] + list(range(7, 25))
    tests, failures, details, original_checks = [], [], [], []

    def test(name, actual, required):
        rec = dict(name=name, actual=actual, required=required)
        tests.append(rec)
        if actual != required:
            failures.append(rec)

    def oldcheck(name, actual, required):
        original_checks.append(dict(name=name, actual=actual, required=required))
        test('recomputed original: '+name, actual, required)

    oldcheck('indices', [r['i'] for r in rows], list(range(25)))
    oldcheck('short tails', 'For 0<=i<24 set a_i=2;' in source.decode(), True)
    oldcheck('last tail', 'set a_24=166504412=' in source.decode(), True)
    oldcheck('odd count', K, 397573379)
    oldcheck('length', N, 630138897)
    oldcheck('intact multiplicities', sorted(order), list(range(25)))
    oldcheck('closing row', order[-1], 24)
    records = []
    for e, m in [(1, 5), (2, 25)]:
        # Composition on complete value tables, no affine-triple powering.
        def after(f, g):
            return [g[y] for y in f]

        def iterate(f, exponent):
            test(f'm={m} permutation', sorted(f), list(range(m)))
            out = []
            for x in range(m):
                orbit = [x]
                y = f[x]
                while y != x:
                    if y in orbit:
                        raise AssertionError('noncyclic permutation orbit')
                    orbit.append(y)
                    y = f[y]
                out.append(orbit[exponent % len(orbit)])
            return out

        # Small integer multiplications produce unit-power tables independently.
        def power(base, exponent, modulus=m):
            orbit, v = [1], base % modulus
            while v != 1:
                if v in orbit:
                    raise AssertionError('base is not a unit')
                orbit.append(v)
                v = v*base % modulus
            return orbit[exponent % len(orbit)]

        identity = list(range(m))
        inverse_two = (m+1)//2
        odd = [(3*x+1)*inverse_two % m for x in identity]
        even = [x*inverse_two % m for x in identity]
        block = identity
        for letter in [odd, odd, even, odd]:
            block = after(block, letter)
        inverse_eleven = next(x for x in range(m) if 11*x % m == 1)
        oldcheck(f'e={e}: unit inverse', 11*inverse_eleven % m, 1)

        def triple(f, length):
            q = power(2, length)
            a, c = q*(f[1]-f[0]) % m, q*f[0] % m
            test(f'm={m} full affine map, length={length}',
                 [q*y % m for y in f], [(a*x+c) % m for x in identity])
            return [a, c, q]

        state, trace, extra = identity, [], []
        for pos, index in enumerate(order):
            r = rows[index]
            j, h, a = r['J'], r['H'], r['a']
            word = after(after(iterate(block, j), iterate(odd, h)), iterate(even, a))
            composed = triple(word, r['D'])
            # Exact quotient from a lifted modulus, independently of inverse 11.
            lifted = (23*power(3, h, 11*m)
                      *(power(27, j, 11*m)-power(16, j, 11*m))) % (11*m)
            test(f'm={m}, row={index}: quotient integrality', lifted % 11, 0)
            offset = (lifted//11+(power(3, h)-power(2, h))*power(16, j)) % m
            closed = [power(3, r['k']), offset, power(2, r['D'])]
            oldcheck(f'e={e}: row {index} formulas', composed, closed)
            prefix_n = sum(rows[i]['D'] for i in order[:pos])
            prefix_k = sum(rows[i]['k'] for i in order[:pos])
            suffix_k = sum(rows[i]['k'] for i in order[pos+1:])
            two, three = power(2, prefix_n), power(3, suffix_k)
            previous = triple(state, prefix_n)
            state = after(state, word)
            resulting = triple(state, prefix_n+r['D'])
            trace.append(dict(position=pos, index=index, prefix_N=prefix_n,
                              prefix_K=prefix_k, suffix_K=suffix_k,
                              closed_triple=closed, composed_triple=composed,
                              prefix_two=two, suffix_three=three,
                              term=offset*two*three % m,
                              previous_triple=previous, resulting_triple=resulting))
            extra.append(dict(index=index, map=word, accumulated_map=state,
                              lifted_residue=lifted, quotient=lifted//11))
        total = triple(state, N)
        weighted = sum(t['term'] for t in trace) % m
        delta = (power(2, N)-power(3, K)) % m
        oldcheck(f'e={e}: totals', [sum(rows[i]['k'] for i in order),
                                  sum(rows[i]['D'] for i in order)], [K, N])
        oldcheck(f'e={e}: numerator evaluations', total[1], weighted)
        oldcheck(f'e={e}: powers', [total[0], total[2]], [power(3, K), power(2, N)])
        if e == 1:
            oldcheck('L057 residues', [weighted, delta], [0, 0])
        else:
            oldcheck('e=2: compatible residues', [weighted % 5, delta % 5],
                     [records[0]['numerator'], records[0]['denominator']])
        records.append(dict(e=e, modulus=m, numerator=weighted, denominator=delta,
                            total_triple=total, trace=trace))
        details.append(dict(modulus=m, rows=extra))

    printed = []
    for line in CLAIM.read_text().splitlines():
        if line.startswith('|'):
            cells = [x.strip() for x in line.strip('|').split('|')]
            if len(cells) == 6 and all(x.isdecimal() for x in cells):
                printed.append(list(map(int, cells)))
    computed = [[t['position'], t['index'], t['closed_triple'][1],
                 t['prefix_two'], t['suffix_three'], t['term']] for t in records[1]['trace']]
    test('complete written table', computed, printed)
    test('written representative sum', sum(r[-1] for r in computed), 265)
    test('modulo 25 decisive residues', [records[1]['numerator'], records[1]['denominator']], [15, 5])
    test('written sample exponents',
         [[records[1]['trace'][j]['prefix_N'], records[1]['trace'][j]['suffix_K']] for j in [1, 6, 24]],
         [[3040, 397570571], [6357, 397567694], [306970748, 0]])
    test('last length', rows[24]['D'], 323168149)
    test('denominator power reduction', [N % 20, K % 20], [17, 19])
    expected_summary = dict(verdict='COMPLETE_PRIME_FIVE_CANCELLATION', actual_exponent=2,
                            required_cap=8, numerator_valuation=1, denominator_valuation=1,
                            numerator_divisible_through=1, denominator_divisible_through=1,
                            checks=len(original_checks), failures=0)
    expected = dict(target="Determine whether the reduced denominator of L057's swapped-order root is divisible by 5.",
                    source='lemmas/'+SOURCE.name, source_sha256=hashlib.sha256(source).hexdigest(),
                    counts=dict(K=K, N=N), parameters=rows, order=order,
                    records=records, summary=expected_summary, checks=original_checks, failures=[])
    original = json.loads(ORIGINAL.read_text())
    test('original key set', sorted(original), sorted(expected))
    for key in expected:
        test('complete original field: '+key, original.get(key), expected[key])
    summary = dict(checks=len(tests), failures=len(failures), moduli=[5, 25],
                   actual_residues=[records[1]['numerator'], records[1]['denominator']],
                   required_residues=[15, 5], numerator_valuation=1, denominator_valuation=1,
                   written_rows=len(computed), original_comparisons=len(original_checks))
    output = dict(summary=summary, source_sha256=hashlib.sha256(source).hexdigest(),
                  original_sha256=hashlib.sha256(ORIGINAL.read_bytes()).hexdigest(),
                  parameters=rows, order=order, records=records, map_evidence=details,
                  written_table=computed, checks=tests, failures=failures)
    OUT.write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Required: every original field and printed entry equal; only moduli 5 and 25.')
    print('Failures:', len(failures))
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
