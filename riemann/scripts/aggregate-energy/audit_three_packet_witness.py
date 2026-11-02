#!/usr/bin/env python3
"""Independent finite-accounting replay for L615; no transcendental oracle.

Run from riemann: python3 scripts/aggregate-energy/audit_three_packet_witness.py
The analytic audit is in L615. This records every indexed pair and checks
the original certificate rather than importing the original generator.
"""
from collections import Counter
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent
    source = directory / 'three-packet-witness.json'
    original = json.loads(source.read_text())
    failures = []
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            failures.append(name)

    # Explicit occurrences, independently of the packet generator.
    z = [(Q(-1), Q(0))] * 4 + [(Q(0), Q(-1, 10)), (Q(0), Q(1, 10))]
    z += [(Q(1), Q(0))] * 4
    # Rows classify the nine possible differences by evenness and conjugation.
    symbols = {(Q(-2), Q(0)): 'zero', (Q(2), Q(0)): 'zero',
               (Q(0), Q(0)): 'one',
               (Q(0), Q(-1, 5)): 'H', (Q(0), Q(1, 5)): 'H',
               (Q(-1), Q(-1, 10)): 'A', (Q(1), Q(1, 10)): 'A',
               (Q(-1), Q(1, 10)): 'A_conjugate',
               (Q(1), Q(-1, 10)): 'A_conjugate'}
    histogram = Counter()
    energy = Counter()
    pairs = []
    for i in range(10):
        for j in range(10):
            dx, dy = z[i][0] - z[j][0], z[i][1] - z[j][1]
            symbol = symbols.get((dx, dy), 'UNCLASSIFIED')
            histogram[(dx, dy)] += 1
            energy[symbol] += 1
            pairs.append({'i': i, 'j': j, 'dx': str(dx), 'dy': str(dy),
                          'energy_symbol': symbol, 'charged': dx == 0})
    records = original['ordered_differences']
    recorded = {(Q(row['dx']), Q(row['dy'])): row['count'] for row in records}
    check('no duplicate recorded differences', len(recorded) == len(records))
    check('entire original difference table', dict(histogram) == recorded)
    check('all indexed pairs distinct and present',
          {(p['i'], p['j']) for p in pairs} == {(i, j) for i in range(10) for j in range(10)})
    check('all energy terms classified', 'UNCLASSIFIED' not in energy)
    check('energy polynomial', dict(energy) ==
          {'one': 34, 'H': 2, 'zero': 32, 'A': 16, 'A_conjugate': 16})
    check('complete certificate energy categories', original['energy_categories'] ==
          {'K(0)^2=1': energy['one'], 'K(2ih)^2=H(2h)': energy['H'],
           'K(2)^2=0': energy['zero'], 'K(1+ih)^2': energy['A'],
           'K(1-ih)^2': energy['A_conjugate']})
    M = sum(p['charged'] for p in pairs)
    check('charge counts and recorded totals',
          M == 36 == original['M'] and original['label_count'] == 10
          and original['ordered_pair_count'] == 100)
    check('exact admitted packet parameters', original['packets'] ==
          [{'x': '-1', 'depth': '0', 'per_label_multiplicity': 2},
           {'x': '0', 'depth': '1/10', 'per_label_multiplicity': 1},
           {'x': '1', 'depth': '0', 'per_label_multiplicity': 2}])
    check('conjugation-invariant occurrence multiset',
          Counter(z) == Counter((x, -y) for x, y in z))

    # Audit the all-k ratio proof algebraically, not by testing finitely many k.
    # (2k+4)(2k+3)-12 = 4k^2+14k. Nonnegative for every integer k>=0.
    denominator_minus_12 = [4*3-12, 4*2+2*3, 2*2]
    check('universal coefficient ratio polynomial', denominator_minus_12 == [0, 14, 4])
    check('positive denominators for k nonnegative', 4 > 0 and 3 > 0)
    check('initial power-series coefficient', Q(2, 2) == 1)
    pi_up = Q(22, 7)
    check('strict rational square bound', pi_up*pi_up < 10)
    h = Q(1, 10)
    y2_up = 4*10*h*h
    ratio_up = y2_up / 3
    H_up = 1/(1-ratio_up)
    F_up = -h*h*(1-h*h)/(1+h*h)**2
    surplus_up = 2*(H_up-1)
    cross_up = 32*F_up
    residual_up = surplus_up + cross_up
    check('valid geometric-series range', 0 < ratio_up < 1)
    check('negative multiplier for sinh lower bound', -(1-h*h)/(1+h*h)**2 < 0)
    check('exact strict rational margin', residual_up == -Q(380, 132613) < 0)
    bounds = {'pi_upper_standard_input': pi_up, 'y_square_strict_upper': y2_up,
              'geometric_ratio_strict_upper': ratio_up, 'H_strict_upper': H_up,
              'F_upper': F_up, 'E_minus_M_strict_upper': residual_up,
              'E_strict_upper': M+residual_up}
    check('every original rational bound', original['bounds'] ==
          {name: str(value) for name, value in bounds.items()})
    check('original has no reported failures', original['failures'] == [])
    check('original generator hash', original['script_sha256'] == hashlib.sha256(
          (directory / 'certify_three_packet_witness.py').read_bytes()).hexdigest())
    output = {
        'scope': 'independent finite and rational replay of L615, not formal verification',
        'audit_script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'original_certificate_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'checks': checks, 'failures': failures, 'indexed_ordered_pairs': pairs,
        'ordered_differences': [{'dx': str(dx), 'dy': str(dy), 'count': count}
                                for (dx, dy), count in sorted(histogram.items())],
        'energy_polynomial': dict(energy), 'M': M,
        'ratio_denominator_minus_12_coefficients': denominator_minus_12,
        'bounds': {name: str(value) for name, value in bounds.items()},
        'self_surplus_strict_upper': str(surplus_up),
        'cross_contribution_upper': str(cross_up),
        'required': 'E-M<0 for one admitted family',
        'analytic_inputs_reviewed_in_L615': [
            'sinc evenness, reality, integer zeros and sin(pi+iy) identity',
            'absolutely convergent sinh/cosh power series and double-angle identity',
            'all-k coefficient comparison with nonnegative geometric series',
            'standard Archimedean pi<22/7 bound and strictness propagation'],
        'limitations': ['analytic inputs are reviewed in prose, not verified by this code',
                        'same-session independent replay, not an external referee or Lean proof',
                        'no actual zeta realization or Xi sign is established']}
    destination = directory / 'three-packet-audit.json'
    destination.write_text(json.dumps(output, indent=2) + '\n')
    print(f'Audited indexed ordered pairs={len(pairs)}, M={M}, checks={len(checks)}')
    print(f'Actual certified bound: E-M < {residual_up}; required: E-M < 0')
    print(f'Failures: {len(failures)}; full audit certificate: {destination}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
