#!/usr/bin/env python3
"""Exact certificates for the weighted-energy upper test, not large fibers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, isqrt
import json


def stirling_cycle_counts(a):
    counts = [1]
    for length in range(1, a + 1):
        row = [0] * (length + 1)
        for cycles in range(1, length + 1):
            row[cycles] = counts[cycles - 1] + (length - 1) * (
                counts[cycles] if cycles < len(counts) else 0)
        counts = row
    assert sum(counts) == factorial(a)
    return counts


def fixed_certificate():
    q, n, a, w, r = 65537, 1024, 66, 770, 769
    counts = stirling_cycle_counts(a)
    moments = [None, n, 2*n*n-n, 6*n**3-9*n*n+4*n]
    roots = [None] + [isqrt(value)+1 for value in moments[1:]]
    assert roots[1:] == [33, 1448, 80207]
    assert all((root-1)**2 <= value < root**2
               for root, value in zip(roots[1:], moments[1:]))
    numerator = sum(counts[c] * w**max(0, c-3) * roots[min(c, 3)]
                    for c in range(1, a+1))
    cubic_cap = Fraction(r*numerator, factorial(a))
    # All c>=3 terms factor as sqrt(moment_6)/w^3 times the cycle polynomial.
    d3 = comb(w+a-1, a)
    assert sum(counts[c]*w**c for c in range(a+1)) == factorial(a)*d3
    main = Fraction(r*roots[3], w**3)*d3
    corrections = Fraction(r, factorial(a))*(
        counts[1]*(roots[1]-Fraction(roots[3],w*w)) +
        counts[2]*(roots[2]-Fraction(roots[3],w)))
    assert cubic_cap == main+corrections and corrections > 0
    total = comb(n,a)
    mean = Fraction(total,q*q)
    quadratic_cap = Fraction(513*(q-1),q*q)*comb(579,a)
    upper = mean+quadratic_cap+cubic_cap
    threshold = Fraction(q**28,2**128)
    margin = threshold-mean-quadratic_cap
    assert margin > 0
    assert Fraction(56273,1000) < cubic_cap/threshold < Fraction(56274,1000)
    assert Fraction(56385,1000) < upper/threshold < Fraction(56386,1000)
    assert 56*threshold < upper < 57*threshold
    support = Fraction(comb(n,64),comb(a,64))
    assert upper < support and 1050 < support/threshold < 1051
    assert 63**2 < cubic_cap*cubic_cap/(margin*margin) < 64**2
    required_energy = Fraction(q,q-1)*margin*margin
    precision = required_energy/Fraction(total*total,q)
    assert Fraction(2208,10**16) < precision < Fraction(2209,10**16)
    return {
        'Q':q, 'n':n, 'A':a, 'ambient_extension_degree':28,
        'exact_low_moments':moments[1:], 'integer_root_caps':roots[1:],
        'cubic_error_cap':str(cubic_cap), 'uniform_upper':str(upper),
        'uniform_integer_upper':str(upper.numerator//upper.denominator),
        'upper_threshold_ratio_bracket':['56.385','56.386'],
        'previous_support_ratio_bracket':[1050,1051],
        'threshold':str(threshold),
        'sufficient_cubic_collision_energy_threshold':str(required_energy),
        'margin_squared_over_mean_collision_bracket':['2.208e-13','2.209e-13'],
        'upper_below_threshold':False,
        'improves_previous_support_upper':True,
        'actual_large_fibers_enumerated':False,
        'full_code_grid_bound_changed':False,
    }


def moments(values, p):
    return tuple(sum(pow(x,j,p) for x in values)%p for j in (1,2,3))


def small_audit():
    p,n,a = 17,8,4
    domain = tuple(sorted(pow(2,j,p) for j in range(n)))
    assert len(set(domain)) == n
    low = []
    for s in (1,2,3):
        distribution = Counter(moments(values,p) for values in product(domain,repeat=s))
        energy = sum(value*value for value in distribution.values())
        expected = {1:n,2:2*n*n-n,3:6*n**3-9*n*n+4*n}[s]
        assert energy == expected
        low.append(energy)
    # Import the already audited signed group-ring sieve implementation.
    from verify_cubic_cofactor_upper import cycle_lengths, convolve
    signed = Counter()
    cycle_distributions = {j:Counter(tuple(j*t%p for t in moments((x,),p))
                                     for x in domain) for j in range(1,a+1)}
    for permutation in permutations(range(a)):
        lengths = cycle_lengths(permutation)
        distribution = Counter({(0,0,0):1})
        for length in lengths:
            distribution = convolve(distribution,cycle_distributions[length],p)
        sign = (-1)**(a-len(lengths))
        for key,value in distribution.items():
            signed[key] += sign*value
    subsets = Counter(moments(values,p) for values in combinations(domain,a))
    assert all(signed[key] == factorial(a)*subsets[key] for key in signed.keys()|subsets.keys())
    curve = Counter(moments((z,),p) for z in range(p))
    incidence = convolve(subsets,curve,p)
    assert convolve(signed,curve,p) == Counter({key:factorial(a)*value
                                               for key,value in incidence.items()})
    j3 = sum(value*value for value in incidence.values())
    projected = Counter()
    for v,count in incidence.items():
        projected[v[:2]] += count
    j2 = sum(value*value for value in projected.values())
    assert j2 >= sum(incidence.values())**2 // (p*p)
    # Independent cyclotomic computation of sum_{u3!=0}|F_A R|^2:
    # coefficients encode powers of zeta_p exactly; Phi_p removes constants.
    coeff = [0]*p
    for u in product(range(p),range(p),range(1,p)):
        phases = Counter()
        for v,count in incidence.items():
            phases[sum(x*y for x,y in zip(u,v))%p] += count
        for left,left_count in phases.items():
            for right,right_count in phases.items():
                coeff[(left-right)%p] += left_count*right_count
    expected = p**3*j3-p**2*j2
    assert expected >= 0
    assert all(coeff[0]-value == expected for value in coeff[1:])
    return {'Q':p,'n':n,'A':a,'low_moment_collision_counts':low,
            'signed_sieve_and_cofactor_convolution_passed':True,
            'J3':j3,'J2':j2,'exact_cubic_weighted_fourier_norm':expected,
            'normalized_cubic_energy':str(Fraction(expected,p**3)),
            'cyclotomic_energy_identity_passed':True}


if __name__ == '__main__':
    print(json.dumps({'all_checks_passed':True,'fixed_instance':fixed_certificate(),
                      'small_domain_audit':small_audit()},indent=2))
