#!/usr/bin/env python3
"""Fixed rational isolation from audited L051; no analytic recomputation.

The degree-one/Manin/cusp-torsion applicability proof is in L052.
This certificate records all selected finite counts and denominator rows.
No expected rational value is an input.
"""
import json
from fractions import Fraction as Q
from hashlib import sha256
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'reduced_phase_certificate.json'
OUTPUT = HERE / 'exact_value_certificate.json'


def ceil(q):
    return -((-q).__floor__())


def build():
    raw = SOURCE.read_bytes()
    source = json.loads(raw)
    assert source['schema'] == 'nonunitary-36-reduced-phase-v2'
    assert source['arithmetic']['model'] == [0, 0, 0, 0, 1]
    assert source['arithmetic']['N'] == 36
    scale = source['scale']
    endpoints = source['result']['normalized']
    lo, hi = [Q(n, scale) for n in endpoints]
    assert lo < hi
    rows = []
    for p in (7, 13):
        divisors = list(range(2, isqrt(p) + 1))
        assert all(p % d for d in divisors)
        assert p > 2 and p % 6 == 1 and (-432) % p != 0
        splitting_roots = [z for z in range(p) if (z*z-z+1) % p == 0]
        assert len(splitting_roots) == 2
        assert all((2*z-1) % p != 0 for z in splitting_roots)
        entries = []
        for x in range(p):
            rhs = (x**3 + 1) % p
            ys = [y for y in range(p) if y*y % p == rhs]
            entries.append({'x': x, 'rhs': rhs, 'ys': ys})
        total = 1 + sum(len(row['ys']) for row in entries)
        rows.append({'p': p, 'trial_divisors': divisors,
                     'cyclotomic_roots': splitting_roots,
                     'delta_mod_p': (-432) % p, 'entries': entries,
                     'infinity_points': 1, 'total': total})
    T = gcd(*(row['total'] for row in rows))
    # The canonical applicability proof gives 2*T*F in Z, hence B=2*T.
    K = 2*T
    enumeration, candidates = [], []
    for q in range(1, K + 1):
        lower, upper = ceil(q*lo), (q*hi).__floor__()
        reduced = [a for a in range(lower, upper + 1) if gcd(abs(a), q) == 1]
        enumeration.append({'denominator': q, 'lower_numerator': lower,
                            'upper_numerator': upper,
                            'reduced_numerators': reduced})
        candidates.extend(str(Q(a, q)) for a in reduced)
    integer_lower, integer_upper = ceil(K*lo), (K*hi).__floor__()
    passed = len(candidates) == 1 and integer_lower == integer_upper
    result = {'passed': passed, 'candidate_count': len(candidates),
              'candidates': candidates,
              'scaled_integer_lower': integer_lower,
              'scaled_integer_upper': integer_upper,
              'width': str(hi-lo), 'lattice_spacing': str(Q(1, K)),
              'required_candidate_count': 1}
    if passed:
        recovered = Q(candidates[0])
        assert recovered == Q(integer_lower, K) and lo <= recovered <= hi
        result.update(recovered=str(recovered),
                      lower_margin=str(recovered-lo),
                      upper_margin=str(hi-recovered),
                      left_neighbor_excluded_by=str(lo-Q(integer_lower-1, K)),
                      right_neighbor_excluded_by=str(Q(integer_lower+1, K)-hi))
    cert = {'schema': 'nonunitary-36-exact-recovery-v1',
            'input_certificate_sha256': sha256(raw).hexdigest(),
            'input_lemma': 'L051', 'model': [0, 0, 0, 0, 1],
            'conductor': 36, 'discriminant': -432,
            'path': ['1/6', 'infinity'], 'period': 'total minimal real',
            'scale': scale, 'interval_numerators': endpoints,
            'delta': 6, 'absolute_differential_scalar': 1,
            'point_counts': rows, 'torsion_annihilator': T,
            'clearing_integer': K, 'denominator_bound': K,
            'enumeration': enumeration, 'result': result}
    OUTPUT.write_text(json.dumps(cert, indent=2) + '\n')
    assert SOURCE.read_bytes() == raw
    print(json.dumps({'passed': passed, 'counts': [r['total'] for r in rows],
                      'clearing_integer': K, 'candidate_count': len(candidates),
                      'recovered': result.get('recovered'),
                      'actual_width': result['width'],
                      'lattice_spacing': result['lattice_spacing'],
                      'failures': [] if passed else ['non-isolation'],
                      'certificate': str(OUTPUT.relative_to(HERE.parent.parent))}))
    return passed


if __name__ == '__main__':
    raise SystemExit(0 if build() else 1)
