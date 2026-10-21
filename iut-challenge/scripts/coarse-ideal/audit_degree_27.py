#!/usr/bin/env python3
"""Independent audit of the printed L016 table and L017 compact witness.

Uses neither stored lattice transformations nor either previous checker.
Infinite-log coverage and whole-group saturation remain analytic obligations.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
N = 27


def valuation(x):
    x = F(x)
    if not x:
        return None
    a, b, v = abs(x.numerator), x.denominator, 0
    while a % 3 == 0:
        a //= 3
        v += 1
    while b % 3 == 0:
        b //= 3
        v -= 1
    return v


def at_least(x, threshold):
    return not x or valuation(x) >= threshold


def field_val(x):
    return min(F(valuation(c)) + F(r, N) for r, c in enumerate(x) if c)


def mul_pi(x):
    return [3*x[-1]] + x[:-1]


def scale(x, a):
    return [a*c for c in x]


def phi(x):
    return 3*x[0] - F(31, 3)*x[1] + 9*x[15] - 9*x[18]


def serialize(x):
    if isinstance(x, F):
        return str(x)
    if isinstance(x, (list, tuple)):
        return [serialize(y) for y in x]
    if isinstance(x, dict):
        return {k: serialize(v) for k, v in x.items()}
    return x


def main():
    lemma = ROOT / 'lemmas/L016-degree-27-exact-logarithm-membership-fails.md'
    printed = []
    for line in lemma.read_text().splitlines():
        cells = [s.strip() for s in line.split('|')]
        if len(cells) != 4 or not cells[1].isdigit():
            continue
        assert int(cells[1]) == len(printed) + 1
        q = [F(0)]*N
        seen = set()
        for pair in cells[2].split(','):
            r, value = pair.strip().split(':')
            r = int(r)
            assert r not in seen and 0 <= r < N
            seen.add(r)
            q[r] = F(value)
        printed.append(q)
    assert len(printed) == 13
    depths = [int(r < 14) for r in range(N)]
    errors = []
    for j, q in enumerate(printed, 1):
        exact = [F(0)]*N
        for k in range(1, 243):
            degree = j*k
            exact[degree % N] += F((-1)**(k+1), k)*3**(degree//N)
        errors.append([a-b for a, b in zip(exact, q)])
    checks = {'all_351_printed_congruences': all(
        at_least(c, d) for row in errors for c, d in zip(row, depths))}
    h_basis = [[F(3**depths[r] if r == c else 0) for r in range(N)]
               for c in range(N)]
    generators = printed + h_basis
    checks['all_generator_outer_bounds'] = all(field_val(x) >= -2 for x in generators)
    checks['separator_integral_on_all_generators'] = all(at_least(phi(x), 0) for x in generators)
    q = printed[0]
    checks['primitive_ideal_input'] = valuation(phi(scale(mul_pi([F(1)]+[F(0)]*26), 2))) == -1
    checks['log_content_separator'] = phi(scale(mul_pi(q), 18)) == F(-992, 3)
    checks['log_branch_upper_inclusion'] = all(
        all(at_least(c, d) for c, d in zip(scale(mul_pi(x), 54), depths))
        for x in generators)
    checks['ideal_branch_upper_inclusion'] = all(
        all(at_least(c, d) for c, d in zip(
            scale(mul_pi([F(r == s) for r in range(N)]), 6), depths))
        for s in range(N))
    w, z = scale(mul_pi(q), 9), scale(q, F(1, 6))
    delta = [a-b for a, b in zip(w, z)]

    def A(x):
        return F(27, 8)*x[0]

    def B(x):
        return -F(3, 496)*phi(x)

    def g(x):
        return [a+(A(x)-B(x))*d for a, d in zip(x, delta)]

    checks['splitting_values'] = [A(z), A(w), B(z), B(w)] == [1, 0, 0, 1]
    checks['integral_functionals_on_I_generators'] = all(
        at_least(f(scale(x, F(1, 6))), 0) for x in generators for f in (A, B))
    checks['involution_on_power_basis'] = all(
        g(g([F(r == c) for r in range(N)])) == [F(r == c) for r in range(N)]
        for c in range(N))
    attained = g(mul_pi(q))
    checks['exact_attained_image'] = attained == scale(q, F(1, 54))
    checks['sharp_valuation'] = field_val(attained) == -5
    tails = [g(mul_pi(h)) for h in h_basis]
    checks['all_tail_generators_above_sharp_image'] = all(field_val(t) >= -2 for t in tails)
    failures = [name for name, ok in checks.items() if not ok]
    report = dict(checks=checks, failures=failures,
                  input_lemma_sha256=hashlib.sha256(lemma.read_bytes()).hexdigest(),
                  printed_representatives=printed,
                  exact_finite_sum_minus_printed_representative=errors,
                  separator_values=[phi(x) for x in generators],
                  splitting_values=[A(z), A(w), B(z), B(w)],
                  attained_image=attained,
                  tail_images=tails,
                  tail_image_valuations=[field_val(t) for t in tails],
                  actual_radius=243, required_radius=81,
                  scope='Independent finite audit only; analytic completeness and saturation checked in L017 audit prose')
    out = Path(__file__).with_name('degree-27-audit.json')
    out.write_text(json.dumps(serialize(report), indent=2)+'\n')
    print(f'Independent audit: 351 printed congruences, 40 lattice generators, 27 tail images; failures={failures}')
    print(f'Actual radius=243; required radius=81; certificate={out.relative_to(ROOT)}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
