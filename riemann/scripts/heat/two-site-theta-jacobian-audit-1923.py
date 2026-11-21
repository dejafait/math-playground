"""Replay the assessed C028t audit without overwriting its saved evidence.

The inspected producer supplies expression semantics; its independent checker
supplies the full arithmetic and symbolic replay. This wrapper reproduces both,
compares all mathematical fields with1921, verifies every printed theorem bound
using Fraction endpoints, and preserves complete audit certificates.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import io
import json

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = Path(__file__).with_suffix('.json')


def load(name):
    path = HERE / name
    spec = spec_from_file_location(path.stem.replace('-', '_'), path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def interval(record):
    lo, hi = F(record['lower']), F(record['upper'])
    assert lo <= hi
    return lo, hi


def main():
    original = HERE / 'two-site-theta-jacobian-1921.json'
    original_check = HERE / 'two-site-theta-jacobian-check-1921.json'
    producer = load('two-site-theta-jacobian-1921.py')
    producer.OUT = HERE / 'two-site-theta-jacobian-replay-1923.json'
    with redirect_stdout(io.StringIO()):
        producer.main()
    checker = load('two-site-theta-jacobian-check-1921.py')
    checker.CERT = producer.OUT
    checker.OUT = HERE / 'two-site-theta-jacobian-check-replay-1923.json'
    with redirect_stdout(io.StringIO()):
        checker.main()
    old = json.loads(original.read_bytes())
    new = json.loads(producer.OUT.read_bytes())
    old_check = json.loads(original_check.read_bytes())
    new_check = json.loads(checker.OUT.read_bytes())
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    # Only runtime version and the deliberately changed summary output path
    # are not mathematical fields. The entire remaining producer object agrees.
    check('producer field names', old.keys() == new.keys())
    for key in old:
        if key not in ('python', 'summary'):
            check('producer complete field ' + key, old[key] == new[key])
    check('summary field names', old['summary'].keys() == new['summary'].keys())
    for key in old['summary']:
        if key != 'certificate':
            check('summary field ' + key, old['summary'][key] == new['summary'][key])
    check('checker field names', old_check.keys() == new_check.keys())
    for key in old_check:
        if key not in ('input_sha256', 'producer_input_hashes'):
            check('checker complete field ' + key, old_check[key] == new_check[key])
    check('original checker provenance', all(
        sha256((ROOT / path).read_bytes()).hexdigest() == digest
        for path, digest in old_check['input_sha256'].items()))
    check('replayed checker producer provenance',
          all(new_check['producer_input_hashes'].values()))

    result = new['results']
    specifications = {
        'gram_determinant': (result['gram_determinant']['value'], F(386, 10**6), F(387, 10**6)),
        'variance': (result['variance']['value'], F(2688, 10**4), F(2692, 10**4)),
        'rank_numerator': (result['rank_numerator'], F(-439, 10**6), F(-255, 10**6)),
        'determinant': (result['determinant'], F(-603, 1000), F(-349, 1000)),
        'independent_rank_numerator': (new_check['independent_rank_numerator'], F(-378, 10**6), F(-317, 10**6)),
    }
    bounds = {}
    for name, (record, lower, upper) in specifications.items():
        lo, hi = interval(record)
        check('strict quoted bound ' + name, lower < lo <= hi < upper)
        bounds[name] = {'actual': {'lower': str(lo), 'upper': str(hi)},
                        'required_outer': {'lower': str(lower), 'upper': str(upper)}}
    check('printed complete determinant endpoint equality',
          interval(result['determinant']) == (
              F(-60260542634616891377496411143313853498905414870639, 10**50),
              F(-6989618220286959911416477650126957777667399682899, 2*10**49)))
    check('closed panel contains zero', interval(new['selected_inputs']['lambda']) == (F(0), F(1, 5120)))
    base = new['base_probability_moments']
    check('base zeroth moment exactly one', interval(base['0']) == (F(1), F(1)))
    check('all odd base moments exactly zero', all(
        interval(base[str(k)]) == (F(0), F(0)) for k in (1, 3, 5, 7)))
    check('empirical division exactly four', new['empirical_divisor'] == 4)
    check('all twelve divisors strictly positive', len(new['divisors']) == 12 and all(
        interval(row['interval'])[0] > 0 for row in new['divisors']))
    counts = {}
    for row in new['divisors']:
        key = str(row['trace_id'])
        counts[key] = counts.get(key, 0) + 1
    check('divisor multiplicities', counts == {'0': 3, '140': 4, '1607': 2, '1611': 2, '1626': 1})
    check('all traces checked', new_check['trace_records_checked'] == len(new['trace']) == 1633)
    check('all symbolic components checked', len(new_check['polynomial_checks']) == 15 and all(
        row['all_coefficients_equal'] for row in new_check['polynomial_checks']))
    check('both certificates have no failures', new['failures'] == new_check['failures'] == [])
    failures = [name for name, value in checks.items() if not value]
    paths = (original, original_check, producer.SOURCE, producer.PRIOR,
             HERE / 'two-site-theta-jacobian-1921.py',
             HERE / 'two-site-theta-jacobian-check-1921.py',
             producer.OUT, checker.OUT, Path(__file__))
    report = {
        'status': 'passed' if not failures else 'failed',
        'qualification': 'C028t fixed reference audit only; inherited L917/L037 containment and Decimal correctness remain conditional',
        'checks': checks, 'bounds': bounds, 'positive_divisor_multiplicities': counts,
        'trace_records': len(new['trace']), 'symbolic_components': 15,
        'producer_replay': str(producer.OUT.relative_to(ROOT)),
        'checker_replay': str(checker.OUT.relative_to(ROOT)),
        'input_sha256': {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths},
        'failures': failures,
    }
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'checks': len(checks),
                      'traces': report['trace_records'], 'symbolic_components': 15,
                      'divisors': sum(counts.values()),
                      'actual_determinant': bounds['determinant']['actual'],
                      'required_outer': bounds['determinant']['required_outer'],
                      'failures': failures, 'certificate': str(OUT.relative_to(ROOT)),
                      'producer_replay': report['producer_replay'],
                      'checker_replay': report['checker_replay']}))
    assert not failures


if __name__ == '__main__':
    main()
