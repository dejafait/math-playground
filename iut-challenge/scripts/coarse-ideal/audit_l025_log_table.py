#!/usr/bin/env python3
"""Exact finite evidence for L025; analytic completeness is proved in L016."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def valuation(x):
    if not x:
        return None  # infinity
    a, b, result = abs(x.numerator), x.denominator, 0
    while a % 3 == 0:
        a //= 3
        result += 1
    while b % 3 == 0:
        b //= 3
        result -= 1
    return result


def main():
    lemma = ROOT / 'lemmas/L016-degree-27-exact-logarithm-membership-fails.md'
    rows = []
    for line in lemma.read_text().splitlines():
        cells = [s.strip() for s in line.split('|')]
        if len(cells) != 4 or not cells[1].isdigit():
            continue
        assert int(cells[1]) == len(rows) + 1
        q = [F(0)] * 27
        seen = set()
        for pair in cells[2].split(','):
            r, value = pair.strip().split(':')
            r = int(r)
            assert 0 <= r < 27 and r not in seen
            seen.add(r)
            q[r] = F(value)
        rows.append(q)
    assert len(rows) == 13
    records, failures = [], []
    for j, q in enumerate(rows, 1):
        sums = [F(0)] * 27
        for k in range(1, 243):
            quotient, r = divmod(j*k, 27)
            sums[r] += F((-1)**(k+1) * 3**quotient, k)
        for r in range(27):
            error = sums[r] - q[r]
            actual, required = valuation(error), int(r < 14)
            ok = actual is None or actual >= required
            records.append(dict(j=j, r=r, finite_sum=str(sums[r]),
                                representative=str(q[r]), error=str(error),
                                actual_valuation=actual, required_valuation=required,
                                passed=ok))
            if not ok:
                failures.append(f'congruence j={j}, r={r}')
    q4, q13 = [F(0)]*27, [F(0)]*27
    for r in (4, 8):
        q4[r] = F(1)
    for r in (9, 12, 24):
        q4[r] = F(1, 3)
    q13[12] = q13[13] = F(1)
    coefficients = [q[13] for q in rows]
    checks = dict(
        P13_complete_table=coefficients == [F(1)] + [F(0)]*11 + [F(1)],
        q4_exact=rows[3] == q4, q13_exact=rows[12] == q13,
        q4_trace_zero=rows[3][0] == 0, q13_trace_zero=rows[12][0] == 0,
        q4_nonintegral_coefficient=valuation(rows[3][9]) == -1,
        tail_base_above_H=3**5-27*5 >= 14,
        tail_block_increment_positive=2*3**5-27 > 0,
        deep_log_exp_threshold=F(14, 27) > F(1, 2))
    failures += [name for name, ok in checks.items() if not ok]
    report = dict(input_sha256=hashlib.sha256(lemma.read_bytes()).hexdigest(),
                  finite_congruences=records, checks=checks, failures=failures,
                  P13_representatives=[str(c) for c in coefficients],
                  q4=[str(c) for c in rows[3]], q13=[str(c) for c in rows[12]],
                  q4_pi9_coefficient_actual_valuation=-1,
                  D_coefficient_required_valuation=0,
                  tail_base_actual=108, tail_base_required=14,
                  scope='Finite L025 inputs only; all-unit coverage, infinite tails, source action, irreducibility and homothety require the canonical proofs.')
    output = Path(__file__).with_name('l025-log-table-audit.json')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Checked {len(records)} exact printed-table congruences; failures={failures}')
    print('q4 pi^9 coefficient valuation: actual=-1, D requires >=0; tail base: actual=108, required>=14')
    print(f'Certificate: {output.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
