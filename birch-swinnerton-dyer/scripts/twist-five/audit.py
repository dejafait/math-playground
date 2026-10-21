#!/usr/bin/env python3
"""Fixed-certificate audit by exact powers without intermediate rounding.

Complements verify.py; does not replace its point counts or period replay.
Source applicability is justified in L031, not by these computations.
"""
import hashlib
import json
from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    raw = (HERE / 'certificate.json').read_bytes()
    cert = json.loads(raw)
    assert len(cert['attempts']) == 1 and cert['selected_attempt'] == 0
    a = cert['attempts'][0]
    assert (a['bits'], a['T']) == (48, 256)
    D = 2**48
    assert a['scale'] == D
    base_path = HERE.parent / 'relative-t2' / 'certificate.json'
    base_raw = base_path.read_bytes()
    base = json.loads(base_raw)['arithmetic']
    assert base['model'] == [0, 1, 1, -2, 0]
    b2, b4, b6, b8 = 4, -4, 1, -3
    c4, c6 = b2*b2-24*b4, -b2**3+36*b2*b4-216*b6
    delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    assert (c4, c6, delta) == (112, -856, 389)
    assert base['b'] == [b2, b4, b6, b8]
    assert (base['c4'], base['c6'], base['discriminant']) == (c4, c6, delta)
    assert c4**3-c6*c6 == 1728*delta and gcd(c4, delta) == 1
    trials = [[k, delta % k] for k in range(2, isqrt(delta)+1)]
    assert base['primality_trial'] == trials and all(r for _, r in trials)
    assert base['conductor'] == delta
    for name in ('verification.json', 'audit.json'):
        inherited = json.loads((base_path.parent / name).read_text())
        assert inherited['certificate_sha256'] == hashlib.sha256(base_raw).hexdigest()
        assert inherited['failures'] == [] and all(inherited['checks'].values())

    # Direct rational powers avoid all intermediate dyadic rounding.
    lo, hi = [Q(x, D) for x in a['exponential']['r']]
    assert 0 < lo <= hi < 1
    lower = upper = Q(0)
    witnesses = []

    def slacks(interval, exact_lo, exact_hi):
        left = exact_lo-Q(interval[0], D)
        right = Q(interval[1], D)-exact_hi
        assert left >= 0 and right >= 0
        # Floors are certified nonnegative lower bounds, in units of 1/D.
        return [(left*D).__floor__(), (right*D).__floor__()]

    assert len(a['series']['powers']) == len(a['series']['partials']) == 256
    assert len(a['coefficients']) == 257
    for n in range(1, 257):
        pl, pu = lo**n, hi**n
        power_slack = slacks(a['series']['powers'][n-1], pl, pu)
        weight = Q(2*(0, 1, -1, -1, 1)[n % 5]*a['coefficients'][n], n)
        tl, tu = sorted((weight*pl, weight*pu))
        lower += tl
        upper += tu
        partial_slack = slacks(a['series']['partials'][n-1], lower, upper)
        witnesses.append({'n': n, 'power_slack_floor_D': power_slack,
                          'partial_slack_floor_D': partial_slack})
    tail = 2*hi**257/(1-hi)
    assert Q(a['series']['tail_upper'], D) >= tail
    L_slack = slacks(a['series']['L_interval'], lower-tail, upper+tail)
    qlo, qhi = a['isolation']['ratio']
    assert qlo < 4*D < qhi
    assert 4*(qhi-qlo) < D
    assert a['isolation']['denominator_ranges'] == [[1, 4, 4], [2, 8, 8]]
    assert a['isolation']['candidates'] == ['4']
    report = {
        'certificate_sha256': hashlib.sha256(raw).hexdigest(),
        'base_certificate_sha256': hashlib.sha256(base_raw).hexdigest(),
        'method': 'direct exact rational endpoint powers and sums, no intermediate rounding',
        'base_arithmetic_and_prior_report_hashes_checked': True,
        'all_power_and_partial_witnesses': witnesses,
        'tail_slack_floor_D': ((Q(a['series']['tail_upper'], D)-tail)*D).__floor__(),
        'L_interval_slack_floor_D': L_slack,
        'ratio': [qlo, qhi], 'scale': D,
        'width': str(Q(qhi-qlo, D)), 'required_width': '1/4',
        'q': '4', 'failures': [], 'external_theorems_verified_by_script': False,
    }
    out = HERE / 'audit.json'
    out.write_text(json.dumps(report, indent=2)+'\n')
    print(f"direct audit: 256 powers and partial sums; width={report['width']} "
          "required<1/4; q=4; failures=[]")
    print('certificate:', out.relative_to(HERE.parents[1]))


if __name__ == '__main__':
    main()
