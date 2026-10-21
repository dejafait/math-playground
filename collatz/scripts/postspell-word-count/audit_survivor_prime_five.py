#!/usr/bin/env python3
"""Independent L066 audit: literal changed-tail tuple, modulo 25 only."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'survivor-prime-five-audit-certificate.json'
ORIGINAL = HERE / 'survivor-prime-five-certificate.json'
M = 25
K, N = 397573379, 630138897
IDENTITY = [[1, 0], [0, 1]]


def multiply(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) % M
             for j in range(2)] for i in range(2)]


def matrix_power(base, exponent):
    # After each left-to-right bit, acc = base**(the processed prefix).
    acc = IDENTITY
    for bit in bin(exponent)[2:]:
        acc = multiply(acc, acc)
        if bit == '1':
            acc = multiply(acc, base)
    return acc


def unit_power(base, exponent, modulus):
    # Discover and use the complete finite unit power cycle, without pow().
    residues = [1]
    value = base % modulus
    while value != 1:
        if len(residues) > modulus:
            raise ValueError('unit cycle did not close')
        residues.append(value)
        value = value*base % modulus
    return residues[exponent % len(residues)]


def triple(matrix):
    return [matrix[0][0], matrix[0][1], matrix[1][1]]


def main():
    old_raw = ORIGINAL.read_bytes()
    old = json.loads(old_raw)
    lemma = ROOT / 'lemmas/L066-single-tail-survivor-prime-five-nonintegrality.md'
    text = lemma.read_text()
    source_names = [
        'L055-fixed-count-twenty-five-word-real-witness.md',
        'L064-single-tail-redistribution-j-guard-classification.md',
        'L065-single-tail-survivor-remaining-real-guards.md',
    ]
    sources = {f'lemmas/{name}': hashlib.sha256(
        (ROOT / 'lemmas' / name).read_bytes()).hexdigest() for name in source_names}
    checks, failures = [], []

    def check(name, actual, required):
        rec = dict(name=name, actual=actual, required=required)
        checks.append(rec)
        if actual != required:
            failures.append(rec)

    check('all original source hashes', old['sources'], sources)
    input_text = (ROOT / 'lemmas' / source_names[0]).read_text()
    table = []
    for line in input_text.splitlines():
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) == 3 and all(c.isdecimal() for c in cells):
            table.append(list(map(int, cells)))
    check('complete source table indices', [r[0] for r in table], list(range(25)))
    survivor_text = (ROOT / 'lemmas' / source_names[2]).read_text()
    tail_statement = 'with a_23=20, a_24=166504394 and a_i=2 at every other index.'
    check('canonical tail statement', tail_statement in survivor_text, True)
    rows = [dict(i=i, J=j, H=h, a=(20 if i == 23 else 166504394 if i == 24 else 2))
            for i, j, h in table]
    for r in rows:
        r.update(k=3*r['J']+r['H'], D=4*r['J']+r['H']+r['a'])
    sums = {key: sum(r[key] for r in rows) for key in ['J', 'H', 'a', 'k', 'D']}
    check('all count sums', sums,
          dict(J=66061058, H=199390205, a=166504460, k=K, D=N))
    check('positive parameters', all(r['J'] > 0 and r['H'] > 0 for r in rows), True)
    check('changed D values', [rows[23]['D'], rows[24]['D']], [144041977, 323168131])
    odd, even = [[3, 1], [0, 2]], [[1, 0], [0, 2]]
    block = multiply(odd, multiply(even, multiply(odd, odd)))
    check('chronological OOEO matrix', block, [[2, 23], [0, 16]])
    trace, evidence = [], []
    state = IDENTITY
    prefix = 0
    suffix = K
    for r in rows:
        i, j, h, a = (r[key] for key in ['i', 'J', 'H', 'a'])
        suffix -= r['k']
        lifted = (23*unit_power(3, h, 275)*(
            unit_power(27, j, 275)-unit_power(16, j, 275))) % 275
        check(f'row {i}: lifted division remainder', lifted % 11, 0)
        offset = (lifted//11 + (unit_power(3, h, M)-unit_power(2, h, M))
                  * unit_power(16, j, M)) % M
        word = multiply(matrix_power(even, a), multiply(
            matrix_power(odd, h), matrix_power(block, j)))
        compressed = [unit_power(3, r['k'], M), offset, unit_power(2, r['D'], M)]
        check(f'row {i}: independent matrix and lifted offset', triple(word), compressed)
        check(f'row {i}: homogeneous lower-left entry', word[1][0], 0)
        two, three = unit_power(2, prefix, M), unit_power(3, suffix, M)
        before = triple(state)
        state = multiply(word, state)
        record = dict(**r, prefix_N=prefix, suffix_K=suffix, offset=offset,
                      prefix_two=two, suffix_three=three, contribution=offset*two*three % M,
                      closed_triple=compressed, composed_triple=triple(word),
                      before_triple=before, after_triple=triple(state))
        trace.append(record)
        evidence.append(dict(i=i, lifted_modulus=275, lifted_numerator=lifted,
                             exact_quotient=lifted//11, word_matrix=word,
                             accumulated_matrix=state))
        check(f'row {i}: complete original trace', old['trace'][i], record)
        prefix += r['D']
    check('all original trace records', old['trace'], trace)
    check('final prefix and suffix', [prefix, suffix], [N, 0])
    check('last prefix', trace[24]['prefix_N'], 306970766)
    written_table = [list(map(int, groups)) for groups in re.findall(
        r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$', text, re.M)]
    expected_table = [[r[key] for key in ['i', 'offset', 'prefix_two', 'suffix_three', 'contribution']]
                      for r in trace]
    check('complete written table', written_table, expected_table)
    power2, power3 = unit_power(2, N, M), unit_power(3, K, M)
    total = sum(r['contribution'] for r in trace)
    check('sum and total matrix', [total, triple(state)], [296, [17, 21, 22]])
    check('weighted numerator versus matrix', total % M, state[0][1])
    check('denominator powers', [N % 20, K % 20, power2, power3, (power2-power3) % M],
          [17, 19, 22, 17, 5])
    check('unit inverse 11', 11*16 % M, 1)
    check('claimed periods', [unit_power(2, 20, M), unit_power(3, 20, M)], [1, 1])
    # Reconstruct every original check record from independently calculated data.
    old_checks = []

    def expected_check(name, actual, required):
        old_checks.append(dict(name=name, actual=actual, required=required))

    expected_check('indices', [r['i'] for r in rows], list(range(25)))
    expected_check('L065 changed-tail statement', tail_statement in survivor_text, True)
    for label, key, required in [('J', 'J', 66061058), ('H', 'H', 199390205),
                                 ('tail', 'a', 166504460), ('K', 'k', K), ('N', 'D', N)]:
        expected_check(label+' sum', sums[key], required)
    expected_check('positive J,H', all(r['J'] > 0 and r['H'] > 0 for r in rows), True)
    expected_check('unit inverse 11', [16, 11*16 % M], [16, 1])
    expected_check('OOEO triple', triple(block), [2, 23, 16])
    for r in trace:
        expected_check(f"row {r['i']}: two triples", r['composed_triple'], r['closed_triple'])
    expected_check('numerator evaluations', state[0][1], total % M)
    expected_check('whole count powers', [state[0][0], state[1][1]], [power3, power2])
    expected_check('denominator powers', [N % 20, K % 20, power2, power3, (power2-power3) % M],
                   [17, 19, 22, 17, 5])
    expected_summary = dict(modulus=M, required_modulus=25, numerator=total % M,
        denominator=(power2-power3) % M, numerator_valuation=0,
        numerator_valuation_lower_bound=0, denominator_valuation=1,
        verdict='FIVE_SURVIVES_REDUCED_DENOMINATOR', contribution_sum=total,
        total_triple=triple(state), checks=len(old_checks), failures=0)
    expected = dict(target="Determine whether prime 5 survives in the reduced denominator of L065's exact j=23 unshifted cyclic root by comparing its numerator and denominator modulo 25.",
                    sources=sources, counts=dict(K=K, N=N), parameters=rows,
                    trace=trace, summary=expected_summary, checks=old_checks, failures=[])
    check('original top-level keys', sorted(old), sorted(expected))
    for key in expected:
        check('complete original field: '+key, old[key], expected[key])
    summary = dict(verdict='NO_DEFECT' if not failures else 'AUDIT_FAILED',
                   modulus=M, required_modulus=25, numerator=total % M,
                   denominator=(power2-power3) % M, rows=len(trace),
                   checks=len(checks), failures=len(failures))
    certificate = dict(summary=summary, sources=sources,
        audited_certificate_sha256=hashlib.sha256(old_raw).hexdigest(),
        audited_generator_sha256=hashlib.sha256((HERE/'test_survivor_prime_five.py').read_bytes()).hexdigest(),
        trace=trace, independent_evidence=evidence, written_table=written_table,
        reconstructed_original_checks=old_checks, checks=checks, failures=failures,
        written_obligations='L066 audit section checks coordinate equality, original binary invariant, positive Delta/Phi and valuation applicability; arithmetic verdict alone does not prove these.')
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Actual/required: 25/25 rows, modulus 25/25; Phi=21, Delta=5; failures='+str(len(failures)))
    print('Certificate: scripts/postspell-word-count/'+OUT.name)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
