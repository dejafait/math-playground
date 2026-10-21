#!/usr/bin/env python3
"""Exact residual-pair identity audits; no enumeration of the large fibers."""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import comb
import json


def moments(values, q):
    return tuple(sum(pow(x, j, q) for x in values) % q for j in (1, 2, 3))


def audit(q, domain, a):
    subsets = list(combinations(domain, a))
    data = [(frozenset(s), moments(s, q)) for s in subsets]
    incidence = Counter()
    projected = Counter()
    for _, s in data:
        for z in range(q):
            v = tuple((s[j-1] + pow(z, j, q)) % q for j in (1, 2, 3))
            incidence[v] += 1
            projected[v[:2]] += 1
    j3 = sum(c*c for c in incidence.values())
    j2 = sum(c*c for c in projected.values())
    counts = Counter()
    by_distance = defaultdict(Counter)
    quadratic_checks = 0
    for sset, s in data:
        for tset, t in data:
            d1, d2, d3 = ((y-x) % q for x, y in zip(s, t))
            l = len(sset-tset)
            row = by_distance[l]
            row['pairs'] += 1
            if d1 == d2 == 0:
                counts['E2'] += 1
                row['E2'] += 1
                if d3 == 0:
                    counts['E3'] += 1
                    row['E3'] += 1
            if d1:
                counts['B'] += 1
                row['B'] += 1
                z = ((d1 + d2*pow(d1, -1, q))*pow(2, -1, q)) % q
                w = (z-d1) % q
                cubic = (4*d1*d3-3*d2*d2-d1**4) % q == 0
                assert cubic == ((z**3-w**3-d3) % q == 0)
                if cubic:
                    counts['N'] += 1
                    row['N'] += 1
            # Independent full residual enumeration for each subset pair.
            direct2 = direct3 = 0
            for z, w in product(range(q), repeat=2):
                if (z-w-d1) % q == (z*z-w*w-d2) % q == 0:
                    direct2 += 1
                    if (z**3-w**3-d3) % q == 0:
                        direct3 += 1
            assert direct2 == (q if d1 == d2 == 0 else int(d1 != 0))
            assert direct3 == (q if d1 == d2 == d3 == 0 else
                              int(d1 != 0 and (4*d1*d3-3*d2*d2-d1**4) % q == 0))
            # Remove each marked root; audit the polynomial identity at every y.
            for marked in tset:
                aa = (d1-marked) % q
                bb = (d2-marked**2) % q
                cc = (d3-marked**3) % q
                coeff = ((aa**4+3*bb*bb-4*aa*cc) % q,
                         (4*(aa**3-cc)) % q,
                         (6*(aa*aa+bb)) % q)
                roots = 0
                for y in range(q):
                    lhs = ((aa+y)**4 + 3*(bb+y*y)**2 -
                           4*(aa+y)*(cc+y**3)) % q
                    rhs = sum(coef*pow(y, i, q) for i, coef in enumerate(coeff)) % q
                    assert lhs == rhs
                    roots += int(lhs == 0)
                degenerate = bb == (-aa*aa) % q and cc == aa**3 % q
                assert (coeff == (0, 0, 0)) == degenerate
                assert roots == q if degenerate else roots <= 2
                quadratic_checks += 1
    assert j3 == q*counts['E3']+counts['N']
    assert j2 == q*counts['E2']+counts['B']
    k = Fraction(q*counts['E3']-counts['E2']) + counts['N']-Fraction(counts['B'], q)
    assert k == j3-Fraction(j2, q) and k >= 0
    assert q*counts['E3'] >= counts['E2']
    c = len(data)
    assert by_distance[0]['E3'] == by_distance[0]['E2'] == c
    assert by_distance[0]['N'] == by_distance[0]['B'] == 0
    if a >= 1:
        n1 = c*a*(len(domain)-a)
        assert by_distance[1]['pairs'] == by_distance[1]['N'] == by_distance[1]['B'] == n1
        assert by_distance[1]['E2'] == by_distance[1]['E3'] == 0
    if a >= 2:
        assert by_distance[2]['N'] == by_distance[2]['E2'] == by_distance[2]['E3'] == 0
    return {'Q': q, 'n': len(domain), 'A': a, 'J3': j3, 'J2': j2,
            'counts': dict(counts), 'energy': str(k),
            'counts_by_half_symmetric_difference': {str(l): dict(row) for l, row in sorted(by_distance.items())},
            'quadratic_identity_checks': quadratic_checks,
            'direct_residual_enumeration_passed': True}


def fixed_comparison():
    q, n, a = 65537, 1024, 66
    c = comb(n, a)
    threshold = Fraction(q**28, 2**128)
    margin = threshold-Fraction(c, q*q)-Fraction(513*(q-1), q*q)*comb(579, a)
    required = Fraction(q, q-1)*margin*margin
    # Lower bound on the root-count UPPER allowance, not on actual energy:
    # Q E3-E2 >= 0, D >= 0 and B <= C^2.
    allowance_floor = (Fraction(2, n-a+1)-Fraction(1, q))*c*c
    ratio = allowance_floor/required
    assert 614*10**12 < ratio < 615*10**12
    near_pairs = c*(1+a*(n-a)+comb(a, 2)*comb(n-a, 2))
    assert Fraction(near_pairs, c*c) < Fraction(1, 10**95)
    low_positive = (q-1)*c+Fraction(q-1, q)*c*a*(n-a)
    assert low_positive/required < Fraction(1, 10**80)
    return {'Q': q, 'n': n, 'A': a,
            'root_count_allowance_floor_to_required_energy_bracket': ['6.14e14', '6.15e14'],
            'allowance_floor_is_not_a_bound_for_actual_energy': True,
            'half_symmetric_difference_at_most_two_pair_fraction_upper': '1e-95',
            'known_positive_near_diagonal_energy_to_required_upper': '1e-80',
            'required_energy': str(required),
            'larger_symmetric_difference_collision_counts_estimated': False,
            'actual_large_fibers_enumerated': False,
            'full_code_grid_bound_changed': False}


if __name__ == '__main__':
    small = [audit(13, tuple(sorted(pow(4, j, 13) for j in range(6))), 3),
             audit(17, tuple(sorted(pow(2, j, 17) for j in range(8))), 4)]
    print(json.dumps({'all_checks_passed': True, 'fixed_instance': fixed_comparison(),
                      'small_domain_audits': small}, indent=2))
