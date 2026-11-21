#!/usr/bin/env python3
"""Exact replay of every scalar interval used by C999, under its stated floor.

Reads the full648 certificate without rewriting it. Independent endpoint
formulae check all interval inclusions, display rounding and six thresholds.
This does not replay C999k's inherited head factor or solve an inverse.
"""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json


def main():
    source = Path(__file__).with_name('endpoint-reference-648.json')
    raw = source.read_bytes()
    old = json.loads(raw)
    checks = []

    def check(name, value):
        checks.append({'name': name, 'pass': bool(value)})

    intervals = {}
    for name, item in old['intervals'].items():
        lo, hi = F(item['lo']), F(item['hi'])
        intervals[name] = lo, hi
        check(name + ': ordered exact rational endpoints', lo <= hi)
        check(name + ': outward decimal display',
              F(item['display_lo']) <= lo <= hi <= F(item['display_hi']))

    def contains(name, lo, hi):
        saved_lo, saved_hi = intervals[name]
        check(name + ': complete enclosure', saved_lo <= lo <= hi <= saved_hi)

    # Independent tighter positive-series enclosure (120 rather than100 terms).
    n = 120
    partial = sum((F(1, (2*j+1)*2**(2*j)) for j in range(n)), F(0))
    tail = F(1, (2*n+1)*2**(2*n)) * F(4, 3)
    contains('a', partial/4, (partial+tail)/4)
    al, ah = intervals['a']
    rl, rh = intervals['root_3_1_8']
    check('root: exact eighth powers straddle3', 1 < rl < rh and rl**8 < 3 < rh**8)

    # For r>1, r(1-r^-2)(1-r^-4) is positive and increasing.
    def denominator(r):
        return r*(1-r**-2)*(1-r**-4)

    contains('Ca', 4*al/denominator(rh), 4*ah/denominator(rl))
    cl, ch = intervals['Ca']
    h, delta = F(303, 16), F(1, 100)
    contains('m_rule', 2*h*al*al/delta, 2*h*ah*ah/delta)
    contains('tail_J13', cl/rh**52, ch/rl**52)
    contains('tail_J14', cl/rh**56, ch/rl**56)
    tl, th = intervals['tail_J14']
    contains('eta', h*al*al/286+tl, h*ah*ah/286+th)
    el, eh = intervals['eta']
    inherited = F(239999, 10**6)
    beta = F(219999, 10**6)
    contains('inherited_floor_minus_delta_minus_eta',
             inherited-delta-eh, inherited-delta-el)

    check('fixed parameters retained', old['parameters'] == {'m': 286, 'J': 14, 'delta': '1/100'})
    ml, mh = intervals['m_rule']
    check('minimal m: 285 < rule < 286', 285 < ml <= mh < 286)
    check('minimal J: 13 fails and14 pays',
          intervals['tail_J13'][0] > delta/2 and th < delta/2)
    check('eta below stated decimal and .01', eh < F('.009308749378074894') < delta)
    check('strict improved floor',
          inherited-delta-eh > F('.220690250621925106') > beta)
    check('coarse floor from two delta losses', inherited-2*delta == beta > 0)
    check('inverse norm threshold', 1/beta < F('4.546'))
    check('six original checks and no failures',
          len(old['checks']) == 6 and all(c['pass'] for c in old['checks']) and old['failures'] == [])
    check('input preserved', source.read_bytes() == raw)
    failures = [c['name'] for c in checks if not c['pass']]
    result = {
        'step': '2026-11-12-fixed-endpoint-conceptual-audit-650',
        'source': str(source.relative_to(Path.cwd())),
        'source_sha256': sha256(raw).hexdigest(),
        'method': 'complete Fraction endpoint verification; independent120-term log enclosure',
        'qualification': 'C999k .239999 floor assumed under its original contracts, not replayed',
        'checks': checks, 'failures': failures,
        'summary': {
            'checks_passed': len(checks)-len(failures), 'checks_total': len(checks),
            'm_rule': old['summary']['m_rule_interval'], 'm_required': '(285,286)',
            'tail_J13_lower': old['summary']['tail_J13_lower'],
            'tail_J14_upper': old['summary']['tail_J14_upper'], 'tail_required': '.005',
            'eta_upper': old['summary']['eta_upper'], 'eta_required': '.01',
            'floor_lower': old['summary']['floor_lower'], 'coarse_floor': '.219999',
            'inverse_norm_upper': '4.546', 'failures': failures},
    }
    output = Path(__file__).with_suffix('.json')
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['summary'], sort_keys=True))
    print('certificate:', output.relative_to(Path.cwd()))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
