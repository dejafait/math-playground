#!/usr/bin/env python3
"""Replay L876 without overwriting production evidence; audit with Fractions.

The analytic and code audit is canonical in L876. These checks certify
the stored scalar deductions and rational margins, not the analytic proof.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
import hashlib
import io
import json
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent
    source = directory / 'coefficient-test-24.py'
    original_path = source.with_suffix('.json')
    original_bytes = original_path.read_bytes()
    original = json.loads(original_bytes)
    source_bytes = source.read_bytes()
    replay_path = directory / 'coefficient-replay-26.json'
    namespace = {'__name__': 'l876_audit_replay',
                 '__file__': str(replay_path.with_suffix('.py'))}
    exec(compile(source_bytes, str(source), 'exec'), namespace)
    with redirect_stdout(io.StringIO()):
        exit_code = namespace['main']()
    replay = json.loads(replay_path.read_text())
    checks = {}
    def check(name, condition):
        checks[name] = bool(condition)

    check('replay_exit_success', exit_code == 0)
    check('original_certificate_preserved', original_path.read_bytes() == original_bytes)
    check('complete_replay_equals_original', replay == original)
    e = replay['enclosures']
    def interval(name):
        return tuple(F(v) for v in e[name])
    m0, m2, m4, t, j = map(interval, ('M0', 'M2', 'M4', 'TrA', 'J'))
    s1, s2, c, t2, residual = map(interval, ('S1', 'S2', 'c', 'TrA2', 'residual'))
    check('all_recorded_scalar_intervals_positive_ordered',
          all(0 < F(v[0]) <= F(v[1]) for v in e.values() if isinstance(v, list)))
    check('S1_rational_enclosure',
          s1[0] <= m2[0]/(2*m0[1]) <= m2[1]/(2*m0[0]) <= s1[1])
    numerator = (3*m2[0]**2-m0[1]*m4[1], 3*m2[1]**2-m0[0]*m4[0])
    check('S2_positive_numerator', numerator[0] > 0)
    check('S2_rational_enclosure',
          s2[0] <= numerator[0]/(12*m0[1]**2)
          <= numerator[1]/(12*m0[0]**2) <= s2[1])
    check('c_rational_enclosure', c[0] <= s1[0]/t[1] <= s1[1]/t[0] <= c[1])
    check('TrA2_rational_enclosure', t2[0] <= j[0]**4 <= t[1]**2 <= t2[1])
    purity = F(e['purity_lower'])
    check('purity_lower_direction', F('0.480229') < purity <= j[0]**4/t[1]**2)
    check('residual_rational_enclosure',
          residual[0] <= s1[0]**2*purity-s2[1]
          <= s1[1]**2-s2[0] <= residual[1])
    check('strict_claimed_residual_bounds',
          F('0.00021317') < residual[0] <= residual[1] < F('0.00050451'))

    displayed = {
        'M0': ('0.4965499282', '0.4976918892'),
        'M2': ('0.0229231967', '0.0230208067'),
        'M4': ('0.0029544576', '0.0029712878'),
        'TrA': ('0.0802855244', '0.0806857625'),
        'J': ('0.2364616436', '0.2371348528'),
        'S1': ('0.02302950', '0.02318076'),
        'S2': ('0.0000328469', '0.0000415166'),
    }
    for key, bounds in displayed.items():
        lo, hi = interval(key)
        check('displayed_' + key + '_outward', F(bounds[0]) < lo <= hi < F(bounds[1]))
    simple_lo = F('0.02302950')**2*F('0.480229')-F('0.0000415166')
    simple_hi = F('0.02318076')**2-F('0.0000328469')
    check('displayed_lower_fraction_exact', simple_lo == F(852706518689149, 4000000000000000000))
    check('displayed_upper_fraction_exact', simple_hi == F(315312958861, 625000000000000))
    check('displayed_rational_margins_strict',
          F('0.00021317') < simple_lo < simple_hi < F('0.00050451'))

    # Independent exact alternating sums: do not use production atan_bounds.
    def atan(q, count):
        terms = [F(1 if k % 2 == 0 else -1, (2*k+1)*q**(2*k+1))
                 for k in range(count+1)]
        s = sum(terms[:-1], F(0))
        return min(s, s+terms[-1]), max(s, s+terms[-1])
    a, b = atan(5, 55), atan(239, 18)
    pi = tuple(F(v) for v in replay['constants']['pi'])
    check('pi_exact_alternating_enclosure', pi[0] <= 16*a[0]-4*b[1] <= 16*a[1]-4*b[0] <= pi[1])

    compact = replay['integration']['compact_moment_integrals']
    tails = replay['integration']['moment_tail_bounds']
    tail_caps = {'0': '2.258e-63', '2': '9.161e-63', '4': '3.718e-62'}
    for key in ('0', '2', '4'):
        low, high = interval('M' + key)
        base_low, base_high = map(F, compact[key])
        tail_low, tail_high = map(F, tails[key])
        check('moment_' + key + '_tail_added_outward',
              low == base_low and high >= base_high + tail_high)
        check('moment_' + key + '_tail_cap', 0 < tail_low <= tail_high < F(tail_caps[key]))
    tt = tuple(F(v) for v in replay['integration']['TrA_tail_bound'])
    check('trace_tail_cap', 0 < tt[0] <= tt[1] < F('3.581e-124'))
    parameters = replay['parameters']
    check('mesh_and_trial_corners', parameters == {
        'mesh_denominator': 2000, 'cells': 4000, 'endpoint': 2,
        'trial_b': '3/10', 'retained_n': [1, 2]})
    check('no_certificate_failures', replay['failures'] == [])
    failures = [name for name, passed in checks.items() if not passed]
    result = {
        'scope': 'L876 fixed operator only; proof and interval-code inspection recorded in canonical lemma',
        'source_sha256': hashlib.sha256(source_bytes).hexdigest(),
        'original_certificate_sha256': hashlib.sha256(original_bytes).hexdigest(),
        'replay_certificate': str(replay_path.relative_to(directory.parent.parent)),
        'checks': checks,
        'exact_simple_bounds': [str(simple_lo), str(simple_hi)],
        'exact_simple_margins': [str(simple_lo-F('0.00021317')), str(F('0.00050451')-simple_hi)],
        'residual': e['residual'], 'required_threshold': '0',
        'claimed_strict_bounds': ['0.00021317', '0.00050451'],
        'failures': failures,
        'decision': 'AUDIT_CHECKS_PASS' if not failures else 'AUDIT_CHECK_FAILURE',
        'qualification': 'Replay and rational checks complement, and do not replace, analytic and implementation audit; no RH conclusion',
    }
    output = directory / 'audit-26.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ('decision', 'residual', 'required_threshold', 'claimed_strict_bounds', 'failures')}))
    print('Certificates:', replay_path, output)
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
