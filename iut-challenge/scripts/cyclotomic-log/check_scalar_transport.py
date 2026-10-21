#!/usr/bin/env python3
"""Exact finite checks for L030; infinite-series and residue proofs are in L030."""
from fractions import Fraction as Q
import json
from pathlib import Path


def val(x):
    x = Q(x)
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


def at_least(x, bound):
    v = val(x)
    return v is None or v >= bound


def main():
    here = Path(__file__).resolve().parent
    old_path = here.parent / 'coarse-ideal' / 'degree-27-membership.json'
    old = json.loads(old_path.read_text())
    phi = [Q(0)] * 27
    phi[0], phi[1], phi[15], phi[18] = Q(3), Q(-31, 3), Q(9), Q(-9)
    dot = lambda row: sum((a * Q(b) for a, b in zip(phi, row)), Q(0))
    qvals = [dot(row) for row in old['logarithm_representatives']]
    hvals = [dot(row) for row in old['H_basis']]
    assert qvals == list(map(Q, [0, 0, 4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0]))
    assert all(at_least(x, 0) for x in qvals + hvals)
    old_congruences = []
    for sums, reps in zip(old['finite_sums'], old['logarithm_representatives']):
        for r, (s, q) in enumerate(zip(sums, reps)):
            old_congruences.append(at_least(Q(s) - Q(q), 1 if r < 14 else 0))
    assert len(old_congruences) == 351 and all(old_congruences)

    terms, total, rest = [], [Q(0)] * 20, [Q(0)] * 20
    for k in range(1, 243):
        m, r = divmod(k, 27)
        coefficient = phi[r] * Q((-1) ** (k + 1) * 3 ** m, k)
        terms.append(dict(k=k, field_coordinate=r, scalar=str(coefficient),
                          valuation=val(coefficient), special=k in (1, 27)))
        total[k % 20] += coefficient
        if k not in (1, 27):
            assert at_least(coefficient, 0)
            rest[k % 20] += coefficient
    leading = [Q(0)] * 20
    leading[1], leading[7] = Q(-31, 3), Q(1, 3)
    assert total == [a + b for a, b in zip(leading, rest)]
    assert all(at_least(c, 0) for c in rest)
    assert 3 ** 5 - 27 * 5 == 108 >= 14
    assert 2 * 3 ** 5 - 27 > 0
    assert 26 % 20 != 0
    result = dict(
        theorem='L030', old_input='L016',
        field='U(pi), U=Q_3(zeta_20), pi^27=3',
        old_representative_separator_values=list(map(str, qvals)),
        deep_ideal_separator_values=list(map(str, hvals)),
        old_representative_congruences=old_congruences,
        finite_log_terms=terms,
        finite_separator_polynomial_mod_zeta20=list(map(str, total)),
        leading_polynomial=list(map(str, leading)),
        integral_remainder_polynomial=list(map(str, rest)),
        infinite_tail=dict(cutoff_exclusive=243, integer_valuation_bound=108,
                           required_deep_ideal_bound=14,
                           proof='L030: uniform blocks and phi(pi^14 O_L) subset O_U'),
        residue=dict(zeta_order=20, difference_exponent=26,
                     divisible_by_order=False,
                     proof='L030: prime-to-3 order is retained by reduction'),
        actual_separator_valuation=-1, required_scalar_span_valuation=0,
        identity_holds=False, finite_check_failures=0,
        limitations='No complete new log lattice, IUT admissibility, action or radius claim')
    output = here / 'scalar-transport.json'
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(dict(identity_holds=False, actual_separator_valuation=-1,
                          required_scalar_span_valuation=0,
                          old_generator_checks=len(qvals) + len(hvals),
                          finite_log_term_checks=len(terms), finite_check_failures=0,
                          tail_bound=108, required_tail_bound=14,
                          certificate=str(output.relative_to(here.parent.parent)))))


if __name__ == '__main__':
    main()
