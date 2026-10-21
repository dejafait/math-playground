#!/usr/bin/env python3
"""Exact finite verification of the approved two-factor fixed-involution test.

Analytic logarithm coverage, tensor identifications and source applicability
are proved/cited in L020; this certificate does not establish them by sampling.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

from audit_degree_27 import at_least, field_val, mul_pi, phi, scale, serialize

ROOT = Path(__file__).resolve().parents[2]
N = 27


def main():
    source = ROOT / 'lemmas/L016-degree-27-exact-logarithm-membership-fails.md'
    reps = []
    for line in source.read_text().splitlines():
        cells = [cell.strip() for cell in line.split('|')]
        if len(cells) != 4 or not cells[1].isdigit():
            continue
        assert int(cells[1]) == len(reps) + 1
        qj = [F(0)] * N
        for item in cells[2].split(','):
            r, c = item.strip().split(':')
            qj[int(r)] = F(c)
        reps.append(qj)
    assert len(reps) == 13
    basis = [[F(r == s) for r in range(N)] for s in range(N)]
    h_basis = [scale(b, 3 if s < 14 else 1) for s, b in enumerate(basis)]
    j_gens = reps + h_basis
    q = reps[0]
    w, z = scale(mul_pi(q), 9), scale(q, F(1, 6))
    delta = [a-b for a, b in zip(w, z)]

    def A(y):
        return F(27, 8) * y[0]

    def B(y):
        return -F(3, 496) * phi(y)

    def g(y):
        return [c+(A(y)-B(y))*d for c, d in zip(y, delta)]

    ideal_inputs = [mul_pi(b) for b in basis]
    log_inputs = [scale(mul_pi(j), 3) for j in j_gens]
    ideal_images = [g(y) for y in ideal_inputs]
    log_images = [g(y) for y in log_inputs]
    tail_images = [g(scale(mul_pi(h), 3)) for h in h_basis]
    different_valuations = [F(107, 27), F(0)]
    beta_valuation = sum(different_valuations) - max(different_valuations)
    ramification_product = 27
    scalar_valuation = F(1, 27)
    exponent = scalar_valuation - beta_valuation
    floor_exponent = exponent.numerator // exponent.denominator
    required_radius = F(ramification_product, 1) / F(1, 3) * F(3) ** (-floor_exponent)
    infinite_tail_lower = min(map(field_val, tail_images))
    ideal_witness = ideal_images[0]
    log_witness = g(scale(mul_pi(q), 3))
    checks = {
        'second_shell_unit_generator': at_least(F(1, 2), 0) and at_least(F(2), 0),
        'beta_required_valuation_zero': beta_valuation == 0,
        'coarse_required_radius_81': required_radius == 81,
        'splitting_values': [A(z), A(w), B(z), B(w)] == [1, 0, 0, 1],
        'functionals_integral_on_shell_generators': all(
            at_least(f(scale(j, F(1, 6))), 0) for j in j_gens for f in (A, B)),
        'involution_on_all_power_basis_vectors': all(g(g(b)) == b for b in basis),
        'all_27_ideal_images_enclosed': all(field_val(y) >= -3 for y in ideal_images),
        'all_40_log_images_enclosed': all(field_val(y) >= -4 for y in log_images),
        'ideal_extreme_attained': field_val(ideal_witness) == -3,
        'log_image_exactly_q_over_18': log_witness == scale(q, F(1, 18)),
        'log_extreme_attained': field_val(log_witness) == -4,
        'all_27_infinite_tail_images_above_extreme': infinite_tail_lower >= -1,
        'rational_scaling_on_log_generators': all(
            g(scale(mul_pi(j), 3)) == scale(g(mul_pi(j)), 3) for j in j_gens),
    }
    failures = [name for name, passed in checks.items() if not passed]
    report = {
        'scope': 'Finite exact fixed-map verification; analytic and tensor proof obligations remain in L020.',
        'input_lemma_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'checks': checks, 'failures': failures,
        'different_valuations': different_valuations,
        'beta_valuation': beta_valuation, 'scalar_valuation': scalar_valuation,
        'floor_exponent': floor_exponent,
        'actual_radius': 81, 'required_radius': required_radius,
        'ideal_branch_radius': 27, 'log_branch_radius': 81,
        'ideal_inputs': ideal_inputs, 'ideal_images': ideal_images,
        'ideal_image_valuations': list(map(field_val, ideal_images)),
        'log_inputs': log_inputs, 'log_images': log_images,
        'log_image_valuations': list(map(field_val, log_images)),
        'ideal_witness_image': ideal_witness, 'log_witness_image': log_witness,
        'tail_images': tail_images, 'tail_image_valuations': list(map(field_val, tail_images)),
        'infinite_tail_lower_valuation': infinite_tail_lower,
    }
    out = Path(__file__).with_name('two-factor-degree-27.json')
    out.write_text(json.dumps(serialize(report), indent=2) + '\n')
    print(f'Two-factor test: 27 ideal, 40 logarithm and 27 tail generators; failures={failures}')
    print(f'Actual radius=81; required radius={required_radius}; ideal radius=27; tail valuation >= {infinite_tail_lower}')
    print(f'Certificate: {out.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
