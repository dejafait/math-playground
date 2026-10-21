#!/usr/bin/env python3
"""Exact witness verification; analytic completeness is imported from L016."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = 27


def val(c):
    if not c:
        return None
    a, b, n = abs(c.numerator), c.denominator, 0
    while a % 3 == 0:
        a //= 3
        n += 1
    while b % 3 == 0:
        b //= 3
        n -= 1
    return n


def field_val(y):
    return min(F(val(c)) + F(r, N) for r, c in enumerate(y) if c)


def scale(y, c):
    return [c*a for a in y]


def add(y, z):
    return [a+b for a, b in zip(y, z)]


def phi(y):
    return 3*y[0] - F(31, 3)*y[1] + 9*y[15] - 9*y[18]


def B(y):
    return -F(3, 496)*phi(y)


def serial(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, list):
        return [serial(a) for a in x]
    if isinstance(x, dict):
        return {k: serial(v) for k, v in x.items()}
    return x


def main():
    source = ROOT / 'lemmas/L016-degree-27-exact-logarithm-membership-fails.md'
    reps = []
    for line in source.read_text().splitlines():
        cells = [s.strip() for s in line.split('|')]
        if len(cells) != 4 or not cells[1].isdigit():
            continue
        assert int(cells[1]) == len(reps)+1
        q = [F(0)]*N
        for item in cells[2].split(','):
            r, c = item.strip().split(':')
            q[int(r)] = F(c)
        reps.append(q)
    assert len(reps) == 13
    basis = [[F(r == s) for r in range(N)] for s in range(N)]
    h = [scale(e, F(3 if s < 14 else 1)) for s, e in enumerate(basis)]
    igens = [scale(j, F(1, 6)) for j in reps+h]
    z = scale(add(reps[1], scale(reps[0], -F(3, 16))), F(1, 6))
    x = scale([3*reps[0][-1]]+reps[0][:-1], F(1, 6))

    def T(y, sign=1):
        return add(y, scale(z, sign*B(y)))

    values = [B(y) for y in igens]
    image, inverse_image = T(x), T(x, -1)
    checks = {
        'direction_in_I_by_integral_combination': val(F(3, 16)) >= 0 and z == add(igens[1], scale(igens[0], -F(3, 16))),
        'B_integral_on_all_40_I_generators': all(a == 0 or val(a) >= 0 for a in values),
        'direction_annihilated_by_B_and_trace': B(z) == 0 and 27*z[0] == 0,
        'both_inverse_compositions_on_full_basis': all(T(T(e), -1) == e and T(T(e, -1)) == e for e in basis),
        'trace_preserved_on_full_basis': all(27*T(e)[0] == 27*e[0] for e in basis),
        'forward_and_inverse_generator_images': all(T(y) == add(y, scale(z, B(y))) and T(y, -1) == add(y, scale(z, -B(y))) for y in igens),
        'witness_in_pi_I': x == scale([3*reps[0][-1]]+reps[0][:-1], F(1, 6)),
        'witness_functional_exact': B(x) == F(1, 54),
        'direction_valuation': field_val(z) == -F(7, 3),
        'witness_image_exact': image == add(x, scale(z, F(1, 54))),
        'witness_image_valuation': field_val(image) == -F(16, 3),
        'strict_radius_81_violation': field_val(image) < -4,
    }
    failures = [name for name, ok in checks.items() if not ok]
    report = dict(
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        checks=checks, failures=failures,
        direction=z, direction_term_valuations=[None if not c else F(val(c))+F(r, N) for r, c in enumerate(z)],
        I_generators=igens, B_on_I_generators=values,
        forward_I_generator_images=[T(y) for y in igens],
        inverse_I_generator_images=[T(y, -1) for y in igens],
        forward_power_basis_images=[T(e) for e in basis],
        inverse_power_basis_images=[T(e, -1) for e in basis],
        witness_input=x, witness_image=image, inverse_witness_image=inverse_image,
        witness_input_valuation=field_val(x), witness_image_valuation=field_val(image),
        actual_witness_radius='3^(16/3)', required_radius=81,
        actual_radius_cubed=3**16, required_radius_cubed=81**3,
        qualifications='Exact envelope witness only; no whole-subgroup radius, actual-ind3 membership or full-pair/native lift established.')
    out = Path(__file__).with_name('trace-compatible-shear.json')
    out.write_text(json.dumps(serial(report), indent=2)+'\n')
    print(f'Trace-compatible shear: 40 lattice generators, 27 full basis vectors; failures={failures}')
    print(f'Image valuation={field_val(image)}; required >= -4; witness radius=3^(16/3) > 81')
    print(f'Cubed radii: actual={3**16}, required={81**3}; certificate={out.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
