#!/usr/bin/env python3
"""Recompute all finite evidence used in the L030 audit from printed L016.

This does not certify infinite series or local-field theorems; see L030.
No lattice diagonalization or stored success flag is used as proof.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valuation(x):
    x = Q(x)
    if not x:
        return None
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % 3 == 0:
        n //= 3
        v += 1
    while d % 3 == 0:
        d //= 3
        v -= 1
    return v


def main():
    failures, checks = [], {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)

    lemma = ROOT / 'lemmas/L016-degree-27-exact-logarithm-membership-fails.md'
    old = json.loads((ROOT / 'scripts/coarse-ideal/degree-27-membership.json').read_text())
    previous = json.loads(Path(__file__).with_name('scalar-transport.json').read_text())
    rows = []
    for line in lemma.read_text().splitlines():
        cells = [s.strip() for s in line.split('|')]
        if len(cells) != 4 or not cells[1].isdigit():
            continue
        assert int(cells[1]) == len(rows) + 1
        q, seen = [Q(0)] * 27, set()
        for entry in cells[2].split(','):
            r, value = entry.strip().split(':')
            r = int(r)
            assert 0 <= r < 27 and r not in seen
            seen.add(r)
            q[r] = Q(value)
        rows.append(q)
    assert len(rows) == 13
    check('old_table_matches_printed_table', rows == [[Q(x) for x in r] for r in old['logarithm_representatives']])
    records, sums_all = [], []
    for j, q in enumerate(rows, 1):
        sums = [Q(0)] * 27
        for k in range(1, 243):
            m, r = divmod(j * k, 27)
            sums[r] += Q(3 ** m, k) * (1 if k % 2 else -1)
        sums_all.append(sums)
        for r in range(27):
            error = sums[r] - q[r]
            actual, required = valuation(error), int(r < 14)
            ok = actual is None or actual >= required
            records.append(dict(j=j, r=r, finite_sum=str(sums[r]),
                                representative=str(q[r]), error=str(error),
                                actual_valuation=actual, required_valuation=required,
                                passed=ok))
            check(f'old_congruence_{j}_{r}', ok)
    check('all_old_exact_sums_match_recomputation', sums_all == [[Q(x) for x in r] for r in old['finite_sums']])
    H = [[Q(3 if r < 14 else 1) if c == r else Q(0) for c in range(27)] for r in range(27)]
    check('old_H_basis_matches_definition', H == [[Q(x) for x in r] for r in old['H_basis']])

    def phi(c):
        return 3*c[0] - Q(31, 3)*c[1] + 9*c[15] - 9*c[18]

    qvals, hvals = list(map(phi, rows)), list(map(phi, H))
    check('all_thirteen_separator_values', qvals == list(map(Q, [0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0])))
    expected_h = [Q(0)]*27
    expected_h[0], expected_h[1], expected_h[15], expected_h[18] = Q(9), Q(-31), Q(9), Q(-9)
    check('all_twenty_seven_H_values', hvals == expected_h)
    check('previous_q_values', qvals == list(map(Q, previous['old_representative_separator_values'])))
    check('previous_H_values', hvals == list(map(Q, previous['deep_ideal_separator_values'])))
    terms, total, rest = [], [Q(0)]*20, [Q(0)]*20
    for k in range(1, 243):
        m, r = divmod(k, 27)
        c = [Q(0)]*27
        c[r] = Q(3**m, k) * (1 if k % 2 else -1)
        value = phi(c)
        v = valuation(value)
        required = -1 if k in (1, 27) else 0
        check(f'witness_term_{k}', v is None or v >= required)
        if r == 0:
            predicted = m - 2 - valuation(m)
        elif r == 1:
            predicted = m - 1
        elif r == 15:
            predicted = m + 1
        elif r == 18:
            predicted = m
        else:
            predicted = None
        check(f'case_formula_{k}', v == predicted)
        terms.append(dict(k=k, field_coordinate=r, scalar=str(value),
                          valuation=v, special=k in (1, 27)))
        total[k % 20] += value
        if k not in (1, 27):
            rest[k % 20] += value
    check('all_previous_term_records_exact', terms == previous['finite_log_terms'])
    leading = [Q(0)]*20
    leading[1], leading[7] = Q(-31, 3), Q(1, 3)
    check('exact_polynomial_decomposition', total == [x+y for x, y in zip(leading, rest)])
    for name, values in [('finite_separator_polynomial_mod_zeta20', total), ('leading_polynomial', leading), ('integral_remainder_polynomial', rest)]:
        check('previous_'+name, values == list(map(Q, previous[name])))
    check('all_remainder_coefficients_integral', all(valuation(x) is None or valuation(x) >= 0 for x in rest))
    check('tail_base_bound', 3**5 - 27*5 == 108 >= 14)
    check('tail_increment', 2*3**5 - 27 > 0)
    check('strict_log_exp_threshold', Q(14, 27) > Q(1, 2))
    check('order_three_mod_twenty', [pow(3, i, 20) for i in range(1, 5)] == [3, 9, 7, 1])
    check('residue_noncancellation_exponent', 26 % 20 != 0)
    report = dict(input_lemma_sha256=hashlib.sha256(lemma.read_bytes()).hexdigest(),
                  old_congruences=records, q_separator_values=list(map(str, qvals)),
                  H_separator_values=list(map(str, hvals)), finite_log_terms=terms,
                  leading_polynomial=list(map(str, leading)), integral_remainder=list(map(str, rest)),
                  checks=checks, failures=failures,
                  actual_separator_valuation=-1, required_span_valuation=0,
                  tail_actual=108, tail_required=14,
                  scope='All relevant finite data recomputed; all-unit, infinite-series and order-lifting proofs audited in L030.')
    out = Path(__file__).with_name('scalar-transport-audit.json')
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Old congruences: {len(records)}; generator values: {len(qvals)+len(hvals)}; finite witness terms: {len(terms)}')
    print(f'Failures: {failures}; separator actual=-1, span requires >=0; tail actual=108, requires >=14')
    print(f'Full certificate: {out.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
