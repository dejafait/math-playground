#!/usr/bin/env python3
"""Replay the already independent audit2063 without overwriting its evidence."""
import hashlib
import json
from pathlib import Path
import runpy

HERE = Path(__file__).resolve().parent
OUT = HERE / 'actual-scalar-q6-replay-2193.json'
INPUTS = [HERE / name for name in (
    'actual_scalar_q6_2061.py', 'actual-scalar-q6-2061.json',
    'actual_scalar_q6_audit_2063.py', 'actual-scalar-q6-audit-2063.json',
    'tilted-boundary-metric-2010.json')]


def hashes():
    return {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in INPUTS}


def main():
    before = hashes()
    result = {'status': 'STARTED', 'input_hashes_before': before,
              'scope': 'Duplicate audit replay; no new mathematical advance',
              'fixed_grid_digits': 60, 'required_distinct_real_count': 4}
    try:
        # run_name is deliberately not __main__: the old output is never written.
        module = runpy.run_path(str(HERE / 'actual_scalar_q6_audit_2063.py'))
        module['run']()
        fresh = module['report']
        historical = json.loads((HERE / 'actual-scalar-q6-audit-2063.json').read_text())
        result['full_audit_report'] = fresh
        result['historical_report_equal'] = fresh == historical
        result['input_hashes_after'] = hashes()
        result['inputs_unchanged'] = before == result['input_hashes_after']
        result['failures'] = [k for k, v in fresh['checks'].items() if not v]
        if fresh['status'] != 'AUDIT_PASSED' or result['failures']:
            raise AssertionError('independent audit did not pass')
        if not result['historical_report_equal'] or not result['inputs_unchanged']:
            raise AssertionError('historical evidence or input disagreement')
        result.update(status='REPLAY_PASSED',
                      actual_distinct_real_count=fresh['actual_distinct_real_count'],
                      variations=fresh['variations'], threshold_passed=fresh['threshold_passed'])
    except Exception as exc:
        result.update(status='REPLAY_FAILED', error=repr(exc))
        if 'module' in locals():
            result['full_audit_report'] = module['report']
        result['input_hashes_after'] = hashes()
        result['inputs_unchanged'] = before == result['input_hashes_after']
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result.get(k) for k in (
        'status', 'actual_distinct_real_count', 'required_distinct_real_count',
        'variations', 'threshold_passed', 'historical_report_equal',
        'inputs_unchanged', 'failures', 'error')}))
    print('Certificate:', OUT.relative_to(HERE.parent.parent))
    raise SystemExit(0 if result['status'] == 'REPLAY_PASSED' else 1)


if __name__ == '__main__':
    main()
