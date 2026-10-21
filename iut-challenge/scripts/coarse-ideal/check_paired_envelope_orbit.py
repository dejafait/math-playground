#!/usr/bin/env python3
"""Exact finite evidence for L026; analytic/group inputs remain canonical proofs."""
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
        q = [F(0)] * 27
        for pair in cells[2].split(','):
            r, c = pair.strip().split(':')
            q[int(r)] = F(c)
        rows.append(q)
    assert len(rows) == 13
    q1, q2 = rows[:2]
    scaled_generators = [[3*c for c in q1]] + rows[1:]
    bound = -F(4, 3)
    coordinate_checks = []
    for j, q in enumerate(scaled_generators, 1):
        for r, c in enumerate(q):
            actual = None if not c else F(valuation(c)) + F(r, 27)
            coordinate_checks.append(dict(j=j, r=r, coefficient=str(c),
                                          actual=None if actual is None else str(actual),
                                          required=str(bound),
                                          passed=actual is None or actual >= bound))
    m = [3*a-16*b for a, b in zip(q1, q2)]
    x = [q1[26]/2] + [c/6 for c in q1[:26]]  # pi*q1/6
    phi = lambda y: 3*y[0]-F(31, 3)*y[1]+9*y[15]-9*y[18]
    separator = phi([27*c for c in x])
    constant_numerators = [9*q[0] for q in rows]
    checks = dict(
        trace_relation_mod3=constant_numerators[0] == 16 and
        all(c.denominator == 1 and c.numerator % 3 == 0
            for c in constant_numerators[1:]),
        x_trace_zero=x[0] == 0,
        m_trace_zero=m[0] == 0,
        separator_exact=separator == -F(248, 3),
        separator_nonintegral=valuation(separator) == -1,
        m_pi18_exact=m[18] == -F(13, 9),
        m_field_value=field_value(m) == bound,
        ideal_scale=81+1-54 == 28 and 28 >= 14,
        span_value=bound-4 == -F(16, 3),
        strict_escape=bound-4 < -4)
    failures = [f'coordinate {c["j"]}:{c["r"]}'
                for c in coordinate_checks if not c['passed']]
    failures += [name for name, passed in checks.items() if not passed]
    report = dict(input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  checks=checks, failures=failures, coordinate_checks=coordinate_checks,
                  trace_numerators=[str(c) for c in constant_numerators],
                  x=[str(c) for c in x], m=[str(c) for c in m],
                  separator=str(separator), separator_actual_valuation=valuation(separator),
                  separator_required_valuation=0,
                  M_minimum_actual=str(field_value(m)), M_minimum_bound=str(bound),
                  orbit_minimum_actual=str(bound-4), container_required='-4',
                  ideal_exponent_actual=28, ideal_exponent_required=14,
                  scope='Finite arithmetic only. Full J, N fullness, exact finite-word span, '
                        'homothety, and passage to an orbit point require L026 proof.')
    output = Path(__file__).with_name('paired-envelope-orbit.json')
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(f'Checked {len(coordinate_checks)} exact coordinate bounds; failures={failures}')
    print(f'Separator valuation: actual={valuation(separator)}, membership requires >=0')
    print(f'M minimum: actual={field_value(m)}, bound={bound}; ideal exponent: actual=28, required>=14')
    print(f'Orbit minimum after proved scale: actual={bound-4}, container requires >=-4')
    print(f'Certificate: {output.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
