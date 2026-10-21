#!/usr/bin/env python3
"""Finite arithmetic for L027; source actions and orbit attainment are proofs."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from audit_l025_log_table import valuation

ROOT = Path(__file__).resolve().parents[2]


def field_value(vector):
    return min(F(valuation(c)) + F(r, 27)
               for r, c in enumerate(vector) if c)


def main():
    source = ROOT / 'lemmas/L016-degree-27-exact-logarithm-membership-fails.md'
    rows = []
    for line in source.read_text().splitlines():
        cells = [c.strip() for c in line.split('|')]
        if len(cells) != 4 or not cells[1].isdigit():
            continue
        assert int(cells[1]) == len(rows) + 1
        vector = [F(0)] * 27
        for pair in cells[2].split(','):
            r, c = pair.strip().split(':')
            vector[int(r)] = F(c)
        rows.append(vector)
    assert len(rows) == 13
    q1, q2 = rows[:2]
    m = [3*a-16*b for a, b in zip(q1, q2)]
    pi_vector = [F(r == 1) for r in range(27)]
    phi = lambda y: 3*y[0]-F(31, 3)*y[1]+9*y[15]-9*y[18]
    ideal_exponents = [27+r for r in range(1, 27)]
    branch_vectors = dict(ideal=[c/3 for c in m],
                          logarithm=[c/9 for c in m])
    minima = {name: field_value(v) for name, v in branch_vectors.items()}
    checks = dict(
        ideal_branch_pi_trace_zero=pi_vector[0] == 0,
        ideal_branch_pi_value=field_value(pi_vector) == F(1, 27),
        three_D_in_H=min(ideal_exponents) >= 14,
        pi_separator_exact=phi(pi_vector) == -F(31, 3),
        pi_separator_nonintegral=valuation(phi(pi_vector)) == -1,
        logarithm_span_scalar=F(18, 81) == F(2, 9),
        scalar_unit=valuation(F(2)) == 0,
        literal_input_scalar=F(18, 6) == 3,
        m_trace_zero=m[0] == 0,
        m_minimum=field_value(m) == -F(4, 3),
        ideal_span_minimum=minima['ideal'] == -F(7, 3),
        logarithm_span_minimum=minima['logarithm'] == -F(10, 3),
        logarithm_orbit_shift=-F(16, 3)+valuation(F(18)) == -F(10, 3),
        union_minimum=min(minima.values()) == -F(10, 3),
        union_within_required_container=min(minima.values()) > -4)
    failures = [name for name, passed in checks.items() if not passed]
    report = dict(input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  checks=checks, failures=failures,
                  ideal_exponents=ideal_exponents,
                  ideal_exponent_actual=min(ideal_exponents), ideal_exponent_required=14,
                  pi_vector=[str(c) for c in pi_vector],
                  separator=str(phi(pi_vector)), separator_actual_valuation=-1,
                  separator_membership_required=0,
                  M_minimum_vector=[str(c) for c in m],
                  branch_span_minimum_vectors={k: [str(c) for c in v]
                                               for k, v in branch_vectors.items()},
                  branch_minima={k: str(v) for k, v in minima.items()},
                  union_minimum_actual=str(min(minima.values())), container_required='-4',
                  union_radius_exact='3^(10/3)', coarse_radius_exact='3^4 = 81',
                  scope='Finite arithmetic only. Complete J, exact branch modules, '
                        'homothety and actual finite-word attainment require L027 and its inputs.')
    output = Path(__file__).with_name('paired-literal-trace-zero-orbit.json')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Exact arithmetic checks={len(checks)}; failures={failures}')
    print(f'3D ideal exponent: actual={min(ideal_exponents)}, required>=14')
    print(f'pi separator: actual=-31/3, valuation=-1; J membership requires>=0')
    print(f'Branch minima: ideal={minima["ideal"]}, logarithm={minima["logarithm"]}')
    print(f'Union minimum: actual={min(minima.values())}, container requires>=-4')
    print('Attained radius after proof: 3^(10/3); required radius=81')
    print(f'Certificate: {output.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
