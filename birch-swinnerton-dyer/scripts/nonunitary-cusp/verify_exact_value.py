#!/usr/bin/env python3
"""Independent complete finite recovery replay; no producer imports.

Imports L051's audited analytic interval, not a fresh analytic proof.
Recounts by square histograms and enumerates the complete rectangular
range of numerators independently of the producer's ceiling schedule.
"""
import json
from fractions import Fraction
from hashlib import sha256
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve().parent


def replay(data):
    source_path = HERE / 'reduced_phase_certificate.json'
    source_bytes = source_path.read_bytes()
    source = json.loads(source_bytes)
    assert data['schema'] == 'nonunitary-36-exact-recovery-v1'
    assert data['input_certificate_sha256'] == sha256(source_bytes).hexdigest()
    assert source['schema'] == 'nonunitary-36-reduced-phase-v2'
    assert data['input_lemma'] == 'L051'
    assert data['model'] == source['arithmetic']['model'] == [0, 0, 0, 0, 1]
    assert data['conductor'] == source['arithmetic']['N'] == 36
    assert data['discriminant'] == -16*27 == -432
    assert source['arithmetic']['components'] == 1
    assert data['path'] == ['1/6', 'infinity']
    assert data['period'] == 'total minimal real'
    assert data['delta']**2 == data['conductor'] and data['delta'] == 6
    assert data['absolute_differential_scalar'] == 1
    # This scalar is a theorem specialization proved in L052, not numeric evidence.
    D = data['scale']
    assert D == source['scale'] == 2**96
    assert data['interval_numerators'] == source['result']['normalized'] == [
        -6602346876266374004306815782, -6602346876111015594619213162]
    lo, hi = [Fraction(n, D) for n in data['interval_numerators']]
    assert -1 < lo < hi < 0
    rows = data['point_counts']
    assert [row['p'] for row in rows] == [7, 13]
    totals = []
    affine_checks = 0
    for row in rows:
        p = row['p']
        assert p > 2 and all(p % d != 0 for d in range(2, p))
        assert row['trial_divisors'] == [d for d in range(2, p) if d*d <= p]
        assert p % 6 == 1 and row['delta_mod_p'] == -432 % p != 0
        roots = [z for z in range(p) if (z*z-z+1) % p == 0]
        assert row['cyclotomic_roots'] == roots and len(set(roots)) == 2
        assert all((2*z-1) % p for z in roots)
        histogram = [[] for _ in range(p)]
        for y in range(p):
            histogram[y*y % p].append(y)
        assert len(row['entries']) == p and row['infinity_points'] == 1
        numbers = []
        for x, entry in enumerate(row['entries']):
            rhs = (x*x*x+1) % p
            assert entry == {'x': x, 'rhs': rhs, 'ys': histogram[rhs]}
            numbers.append(len(histogram[rhs]))
            affine_checks += 1
        total = 1+sum(numbers)
        assert row['total'] == total
        totals.append(total)
    T = gcd(totals[0], totals[1])
    K = 2*T
    assert data['torsion_annihilator'] == T
    assert data['clearing_integer'] == data['denominator_bound'] == K
    assert len(data['enumeration']) == K
    candidates = []
    numerator_checks = 0
    for q, row in enumerate(data['enumeration'], start=1):
        # Since J is inside (-1,0), every possible numerator is in [-q,q].
        admissible = []
        for a in range(-q, q+1):
            numerator_checks += 1
            if lo*q <= a <= hi*q and gcd(abs(a), q) == 1:
                admissible.append(a)
                candidates.append(str(Fraction(a, q)))
        lower = row['lower_numerator']
        upper = row['upper_numerator']
        assert lower-1 < q*lo <= lower and upper <= q*hi < upper+1
        assert row == {'denominator': q, 'lower_numerator': lower,
                       'upper_numerator': upper, 'reduced_numerators': admissible}
    result = data['result']
    assert result['candidate_count'] == len(candidates)
    assert result['candidates'] == candidates
    assert result['required_candidate_count'] == 1
    assert Fraction(result['width']) == hi-lo
    assert Fraction(result['lattice_spacing']) == Fraction(1, K)
    lower, upper = result['scaled_integer_lower'], result['scaled_integer_upper']
    assert lower-1 < K*lo <= lower and upper <= K*hi < upper+1
    passed = len(candidates) == 1 and lower == upper
    assert result['passed'] == passed
    assert passed, 'non-isolation; no exact value certified'
    value = Fraction(candidates[0])
    assert Fraction(result['recovered']) == value == Fraction(lower, K)
    margins = {'lower_margin': value-lo, 'upper_margin': hi-value,
               'left_neighbor_excluded_by': lo-Fraction(lower-1, K),
               'right_neighbor_excluded_by': Fraction(lower+1, K)-hi}
    for name, margin in margins.items():
        assert Fraction(result[name]) == margin > 0
    assert source_path.read_bytes() == source_bytes
    return {'passed': True, 'counts': totals, 'clearing_integer': K,
            'candidate_count': len(candidates), 'recovered': str(value),
            'affine_x_checks': affine_checks, 'numerator_checks': numerator_checks,
            'denominator_rows': K, 'actual_width': str(hi-lo),
            'lattice_spacing': str(Fraction(1, K)), 'failures': [],
            'scope': 'complete finite recovery; audited L051 interval imported'}


if __name__ == '__main__':
    certificate = HERE / 'exact_value_certificate.json'
    report_path = HERE / 'exact_value_verification.json'
    try:
        raw = certificate.read_bytes()
        report = replay(json.loads(raw))
        report['certificate_sha256'] = sha256(raw).hexdigest()
    except Exception as exc:
        report = {'passed': False, 'failures': [type(exc).__name__ + ': ' + str(exc)]}
    report_path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({**report, 'report': str(report_path.relative_to(HERE.parent.parent))}))
    raise SystemExit(0 if report['passed'] else 1)
