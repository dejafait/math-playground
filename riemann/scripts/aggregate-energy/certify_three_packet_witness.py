#!/usr/bin/env python3
"""Exact rational certificate for L615's three-packet counterexample.

No floating-point transcendental evaluation enters the certificate.
The elementary series comparison and kernel identities are proved in L615;
this checks full ordered-label accounting and all rational thresholds.
Run from riemann: python3 scripts/aggregate-energy/certify_three_packet_witness.py
"""
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def main():
    h = Q(1, 10)
    packets = [(-1, Q(0), 2), (0, h, 1), (1, Q(0), 2)]
    labels = [(Q(x), sign * depth)
              for x, depth, multiplicity in packets
              for sign in (-1, 1) for _ in range(multiplicity)]
    differences = Counter((x - xx, y - yy)
                          for x, y in labels for xx, yy in labels)
    grouped = Counter()
    failures = []

    def require(name, condition):
        if not condition:
            failures.append(name)

    for (dx, dy), count in differences.items():
        if dx == 0 and dy == 0:
            category = 'K(0)^2=1'
        elif dx == 0 and abs(dy) == 2*h:
            category = 'K(2ih)^2=H(2h)'
        elif abs(dx) == 2 and dy == 0:
            category = 'K(2)^2=0'
        elif abs(dx) == 1 and abs(dy) == h:
            # Evenness K(-z)=K(z) normalizes the real part to +1.
            category = 'K(1+ih)^2' if dx*dy > 0 else 'K(1-ih)^2'
        else:
            category = 'UNEXPECTED'
            failures.append(f'unexpected difference: {dx}, {dy}')
        grouped[category] += count

    expected = {'K(0)^2=1': 34, 'K(2ih)^2=H(2h)': 2,
                'K(2)^2=0': 32, 'K(1+ih)^2': 16,
                'K(1-ih)^2': 16}
    M = sum(x == xx for x, y in labels for xx, yy in labels)
    require('exact packet constraints',
            all(-2 <= x <= 2 and 0 <= d <= 2 and m in (1, 2)
                for x, d, m in packets) and
            all(packets[j][0] < packets[j+1][0] for j in range(2)))
    require('full ordered pair total', sum(differences.values()) == 100)
    require('ordered energy categories', dict(grouped) == expected)
    require('horizontal second moment', M == 36)

    # Archimedes pi < 22/7 and (22/7)^2 < 10 imply pi^2 < 10.
    # a_(k+1)/a_k = 4/((2k+4)(2k+3)) <= 1/3 for every k>=0;
    # hence (sinh y/y)^2 <= 1/(1-y^2/3). See the full proof in L615.
    pi_upper = Q(22, 7)
    require('Archimedean upper square', pi_upper**2 < 10)
    y_square_upper = Q(10, 25)
    geometric_ratio_upper = y_square_upper / 3
    require('geometric ratio range', 0 < geometric_ratio_upper < 1)
    H_upper = 1 / (1 - geometric_ratio_upper)
    F_upper = -h*h*(1-h*h)/(1+h*h)**2
    residual_upper = 2*(H_upper-1) + 32*F_upper
    require('H upper bound value', H_upper == Q(15, 13))
    require('F upper bound value', F_upper == Q(-99, 10201))
    require('residual upper bound value', residual_upper == Q(-380, 132613))
    require('strict negative threshold', residual_upper < 0)

    output = {
        'kind': 'exact rational checks supporting the analytic proof in L615',
        'target': 'E>=M for the approved three-packet family',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'packets': [{'x': str(x), 'depth': str(d), 'per_label_multiplicity': m}
                    for x, d, m in packets],
        'label_count': len(labels), 'ordered_pair_count': sum(differences.values()),
        'ordered_differences': [{'dx': str(dx), 'dy': str(dy), 'count': count}
                                for (dx, dy), count in sorted(differences.items())],
        'energy_categories': dict(sorted(grouped.items())),
        'M': M,
        'bounds': {'pi_upper_standard_input': str(pi_upper),
                   'y_square_strict_upper': str(y_square_upper),
                   'geometric_ratio_strict_upper': str(geometric_ratio_upper),
                   'H_strict_upper': str(H_upper), 'F_upper': str(F_upper),
                   'E_minus_M_strict_upper': str(residual_upper),
                   'E_strict_upper': str(M + residual_upper)},
        'required': 'one exact allowed family with real E-M<0',
        'failures': failures,
        'limitations': ['analytic identities and infinite-series comparison are proved in L615',
                        'not an independent proof audit or formal runtime verification',
                        'not a zeta-zero configuration or an RH counterexample']}
    path = Path(__file__).with_name('three-packet-witness.json')
    path.write_text(json.dumps(output, indent=2) + '\n')
    print(f'Ordered labels={len(labels)}, pairs={sum(differences.values())}, M={M}')
    print(f'Actual certified bound: E-M < {residual_upper}; required: E-M < 0')
    print(f'Failures: {len(failures)}; full certificate: {path}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
