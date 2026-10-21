#!/usr/bin/env python3
"""Exact fixed-model evidence for L039; named arithmetic inputs are in L039.

This produces a full arithmetic certificate and the conditional generic
adapter input. It does not implement Tate's general algorithm or certify BSD.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def main():
    root = Path(__file__).resolve().parent
    failures = []
    checks = {}

    def need(label, condition):
        checks[label] = bool(condition)
        if not condition:
            failures.append(label)

    model = [0, -1, 1, -10, -20]
    a1, a2, a3, a4, a6 = model
    b2 = a1*a1 + 4*a2
    b4 = a1*a3 + 2*a4
    b6 = a3*a3 + 4*a6
    b8 = a1*a1*a6 + 4*a2*a6 - a1*a3*a4 + a2*a3*a3 - a4*a4
    c4 = b2*b2 - 24*b4
    c6 = -b2**3 + 36*b2*b4 - 216*b6
    delta = -b2*b2*b8 - 8*b4**3 - 27*b6*b6 + 9*b2*b4*b6
    need('complete invariant values', (b2, b4, b6, b8, c4, c6, delta) ==
         (-4, -20, -79, -21, 496, 20008, -161051))
    need('invariant identity', c4**3-c6**2 == 1728*delta)
    trials = [{'divisor': q, 'remainder': 11 % q} for q in (2, 3)]
    need('all prime trials through floor sqrt 11', all(t['remainder'] for t in trials))
    need('complete discriminant factorization', delta == -11**5)
    need('minimality valuation threshold', 0 <= 5 < 12)
    need('multiplicative c4 unit', c4 % 11 != 0)
    j = Fraction(c4**3, delta)
    need('nonintegral j excludes rational CM', j.denominator == 11**5 and j.denominator > 1)
    pairs = []
    for x in range(2):
        for y in range(2):
            lhs = (y*y + a1*x*y + a3*y) % 2
            rhs = (x**3 + a2*x*x + a4*x + a6) % 2
            pairs.append({'x': x, 'y': y, 'lhs': lhs, 'rhs': rhs, 'on_curve': lhs == rhs})
    affine = sum(pair['on_curve'] for pair in pairs)
    count = affine + 1
    need('all four affine pairs lie on curve', affine == 4)
    need('smooth good reduction at 2', delta % 2 == 1)
    need('affine y derivative at 2 is one', a1 % 2 == 0 and a3 % 2 == 1)
    x0, y0, z0 = 0, 1, 0
    infinity_fz = y0*y0 + a1*x0*y0 + 2*a3*y0*z0 - a2*x0*x0 - 2*a4*x0*z0 - 3*a6*z0*z0
    need('infinity derivative F_Z is one', infinity_fz % 2 == 1)
    trace = 3-count
    need('complete point count and trace', count == 5 and trace == -2)
    arithmetic = {
        'schema': 'supplied-elliptic-arithmetic-v1', 'model': model,
        'conductor': 11, 'certification': 'SUPPLIED_CONDITIONAL',
        'provenance': {
            'minimal_model': 'L039 independent invariants: Delta=-11^5, every valuation below 12; Cremona Sections 3.1--3.2',
            'nonCM': 'L039 nonintegral rational j; Cremona Section 3.9 rational CM list',
            'exact_conductor': 'L039 complete Delta factorization, c4 unit at 11, multiplicative Tate exit, good elsewhere',
            'newform': 'L039 BCDT Theorem A, exact conductor-level normalized rational weight-two newform'},
        'traces': [{'prime': 2, 'trace': trace, 'provenance': 'L039 all four affine F2 pairs plus unique infinity; smooth reduction'}]}
    adapter_path = root/'arithmetic-input.json'
    # Preserve unsupported generic claims as conditional; L039 supplies proof separately.
    if not failures:
        adapter_path.write_text(json.dumps(arithmetic, indent=2)+'\n')
    certificate = {
        'schema': 'L039-fixed-arithmetic-v1', 'model': model,
        'invariants': dict(zip(('b2', 'b4', 'b6', 'b8', 'c4', 'c6', 'Delta'),
                               (b2, b4, b6, b8, c4, c6, delta))),
        'prime_trials': trials, 'discriminant_factorization': {'sign': -1, 'factors': [[11, 5]]},
        'local_cases': {'11': {'v_Delta': 5, 'minimality_required_upper_bound': 12,
                              'c4_mod_11': c4 % 11, 'type': 'I_5', 'conductor_exponent': 1},
                        'all_other_primes': 'v_Delta=0; good; conductor exponent zero'},
        'j': str(j), 'F2': {'all_affine_pairs': pairs, 'infinity': [0, 1, 0],
                           'infinity_FZ': infinity_fz, 'point_count': count, 'trace': trace},
        'adapter_input_sha256': hashlib.sha256(adapter_path.read_bytes()).hexdigest() if not failures else None,
        'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'qualification': 'Arithmetic implications use cited named results in L039; no general Tate implementation or BSD claim.',
        'checks': checks, 'failures': failures}
    path = root/'arithmetic-certificate.json'
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print('arithmetic: Delta=', delta, '; v_11 actual/required=', 5, '/<12;',
          'c4 mod 11=', c4 % 11, '; #E(F2)=', count, '; a2=', trace,
          '; checks=', len(checks), '; failures=', failures,
          '; certificate=', path, '; adapter input=', adapter_path)
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
