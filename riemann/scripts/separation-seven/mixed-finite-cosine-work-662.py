#!/usr/bin/env python3
"""Exact early cost test only; never evaluates a point or a query batch."""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import numpy as np

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
checks = []


def check(name, value):
    checks.append({'name': name, 'pass': bool(value)})


def rat(x):
    return {'numerator': str(x.numerator), 'denominator': str(x.denominator)}


def main():
    pins = {}
    for name in ('frozen-reference-proposal-652.npz',
                 'jump-log-h1-bounds-654.json', 'jump-log-h1-audit-655.json',
                 'finite-cosine-point-660.json'):
        pins[name] = sha256((B/name).read_bytes()).hexdigest()
    check('unchanged652 archive', pins['frozen-reference-proposal-652.npz'] ==
          '2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6')
    old = json.loads((B/'jump-log-h1-bounds-654.json').read_text())
    audit = json.loads((B/'jump-log-h1-audit-655.json').read_text())
    check('655 pins entire654', audit['input_sha256']['jump-log-h1-bounds-654.json'] ==
          pins['jump-log-h1-bounds-654.json'])
    check('all recorded655 checks, not a preview', len(audit['checks']) == 41 and
          all(c['pass'] for c in audit['checks']) and audit['failures'] == [])
    with np.load(B/'frozen-reference-proposal-652.npz', allow_pickle=False) as data:
        free = data['free_middle_dyadics']
        check('free array shape', free.shape == (254, 3) and np.isfinite(free).all())
        for j in range(3):
            exact = [Q(*float(free[i,j]).as_integer_ratio()) for i in range(254)]
            recorded = [Q(int(x['numerator']), int(x['denominator']))
                        for x in old['exact_free_middle_columns'][j]]
            check(f'all254 dyadics column{j} match654', exact == recorded)
            check(f'all41 witness modes nonzero column{j}',
                  all(exact[n-2] != 0 for n in range(41,82)))

    # An exact witness interval, not sampled point evaluations. If the planned
    # argument error is <1/8, every computed first argument lies in (30,64).
    witness = []
    for n in range(41,82):
        lo = Q(3*n,4)-Q(1,8)
        hi = Q(n,2)*Q(22,7)*Q(513,1024)+Q(1,8)
        check(f'mode{n} entire witness interval inside small branch', 30 < lo < hi < 64)
        witness.append({'mode':n, 'computed_argument_lower':rat(lo),
                        'computed_argument_upper':rat(hi)})
    epsilon = Q(1,2**80)
    # Full selected load-bearing evidence: every possible omitted cosine
    # term N<=60 fails even the necessary first-term condition at z=30.
    terms = []
    for N in range(61):
        val = Q(30**(2*N),factorial(2*N))
        margin = val-epsilon
        check(f'first omitted cosine term N={N} exceeds2^-80 at30', margin > 0)
        terms.append({'N':N, 'term_at30':rat(val), 'excess_over_allowance':rat(margin)})
    # These planning rationals are NOT oracle calls. Their full numerators
    # and denominators are saved, and all exact comparisons are performed.
    max_evidence_bits = max(abs(int(v)).bit_length() for row in terms
                            for key in ('term_at30','excess_over_allowance')
                            for v in row[key].values())
    per_query = 41*2*60*2
    batch = 11174*per_query
    ceiling = 100_000_000
    check('uniform service floor exceeds ceiling without setup', batch > ceiling)
    cases = [{'threshold':h,'fraction_bits':p,
              'witness_modes':list(range(41,82)), 'minimum_terms':61,
              'mandatory_operations_per_query_lower':per_query,
              'uniform_service_batch_lower':batch,
              'decision':'STOP_PRESCRIBED_UNIFORM_SERVICE'}
             for h in (64,128,256) for p in (256,512,1024)]
    check('all nine allowed threshold/precision cases stopped', len(cases)==9 and
          all(c['uniform_service_batch_lower']>ceiling for c in cases))
    report = {
        'result':'MIXED_SIMULTANEOUS_SERIES_UNIFORM_WORK_STOP',
        'assessment':'drafts/literature/2026-11-12-mixed-finite-cosine-test-review-661.md',
        'checks':checks, 'failures':[x['name'] for x in checks if not x['pass']],
        'prescription':{
            'primitive_truncation_allowance':'2^-80',
            'small_branch':'two unconditional factorial recurrences A,B; N terms; cosine geometric absolute-tail certificate must include first omitted z^(2N)/(2N)!',
            'large_branch':'finite DLMF f,g first-omitted-term bounds; not reached by this lower test',
            'argument_accuracy_requirement':'absolute error<1/8 for first arguments on witness interval; a necessary design condition, not an implemented enclosure',
            'work_unit':'integer addition/subtraction, multiplication, division, shift or comparison; registers<=16384 bits',
            'cache_or_mode_pruning':False,
            'query_service':'any11174 admissible point codes; worst-case uniform budget, not a fixed quadrature-node-list lower bound'},
        'normalized_witness_interval':{'lower':rat(Q(1,2)), 'upper':rat(Q(513,1024))},
        'all41_witness_arguments':witness,
        'all61_excluded_truncations':terms,
        'all_threshold_precision_cases':cases,
        'work':{'minimum_updates_per_argument':120,'operations_per_update':2,
                'per_query_lower':per_query,'query_count':11174,'batch_lower':batch,
                'ceiling':ceiling,'excess':batch-ceiling,
                'setup_and_other_modes_charged_in_lower':False},
        'planning_evidence_max_bits':max_evidence_bits,
        'not_established':['whole-density error<=2^-53','Euler-constant enclosure',
            'mixed branch constant assembly','complete arithmetic/register upper bounds',
            'cost of a prescribed nonrepeating outer-node list','residual or inverse norms','signs'],
        'point_or_norm_batch_executed':False,
        'input_sha256':pins,
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest()}
    dest = B/'mixed-finite-cosine-work-662.json'
    dest.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'result':report['result'],'checks':len(checks),
        'failures':report['failures'],'uniform_batch_work_lower':batch,
        'required_work_ceiling':ceiling,'whole_error_required':'2^-53',
        'whole_error_established':False,'point_or_norm_batch_executed':False,
        'certificate':str(dest.relative_to(ROOT))},indent=2))
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
