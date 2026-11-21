"""Replay unchanged C028v evidence, preserving every1925/1928 certificate.

No new matching test, quadrature, sites, masses or enclosure narrowing.
Proof/derivative semantics are justified in C028v's separate audit section.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import io
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = Path(__file__).with_suffix('.json')
TARGET = "Audit C028v's positive two-site update divisor and fixed-collar variance enclosure failure against its complete proof, producer/checker and unchanged1928 certificates, retaining L917/L037's conditional input contracts."
REVIEW = 'drafts/literature/2026-11-20-positive-update-audit-review-1928.md'


def load(filename):
    path = HERE / filename
    spec = spec_from_file_location(path.stem.replace('-', '_'), path)
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read(path):
    return json.loads(path.read_bytes())


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def interval(record):
    lo, hi = F(record['lower']), F(record['upper'])
    assert lo <= hi
    return lo, hi


def maximum_id(obj):
    if isinstance(obj, dict):
        if 'trace_id' in obj:
            return obj['trace_id']
        return max((maximum_id(v) for v in obj.values()), default=-1)
    if isinstance(obj, list):
        return max(map(maximum_id, obj), default=-1)
    return -1


def main():
    originals = [HERE / name for name in (
        'two-site-positive-update-1928.json', 'two-site-positive-update-check-1928.json',
        'two-site-actual-collar-1925.json', 'two-site-actual-collar-check-1925.json',
        'low-time-h2-uniform-195.json', 'low-time-h2-audit-197.json')]
    original_hashes = {str(p.relative_to(ROOT)): digest(p) for p in originals}
    old, old_check, prior, prior_check, source, audit = map(read, originals)
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)

    # The frozen approved target remains reproducible after the checkpoint moves.
    assessment = (ROOT / REVIEW).read_text()
    target = next(s[8:] for s in assessment.splitlines() if s.startswith('TARGET: '))
    check('exact approved assessment target match', TARGET == target)
    check('approved source gate ready', 'DECISION: SPECIALIZE' in assessment.splitlines())
    for label, saved in [('producer1928', old), ('checker1928', old_check),
                         ('producer1925', prior), ('checker1925', prior_check), ('audit197', audit)]:
        check('complete unchanged input register ' + label, all(
            digest(ROOT / name) == h for name, h in saved['input_sha256'].items()))
    check('accepted audit197', audit['status'] == 'passed' and audit['failures'] == [])
    check('all original checkers passed', all(x['status'] == 'passed' and x['failures'] == []
                                            for x in (old_check, prior_check)))
    selected = {str(k): source['panels'][0]['moments'][str(k)] for k in (0, 2, 4, 6, 8)}
    check('all complete raw copies including I8',
          old['selected_inputs'] == prior['selected_inputs'] == selected == {
              k: audit['panels'][0]['moments'][k] for k in selected})
    check('closed panel contains lambda zero', interval(source['panels'][0]['lambda']) ==
          (F(0), F(1, 5120)))
    check('positive normalization input', interval(selected['0'])[0] > 0)

    producer = load('two-site-positive-update-1928.py')
    producer.OUT = HERE / 'two-site-positive-update-replay-1930.json'
    with redirect_stdout(io.StringIO()):
        producer.main()
    new = read(producer.OUT)
    check('all producer fields exactly reproduce', old == new)
    check('producer byte for byte reproduction', digest(originals[0]) == digest(producer.OUT))
    checker = load('two-site-positive-update-check-1928.py')
    checker.CERT = producer.OUT
    checker.OUT = HERE / 'two-site-positive-update-check-replay-1930.json'
    with redirect_stdout(io.StringIO()):
        checker.main()
    replay_check = read(checker.OUT)
    check('checker field names', old_check.keys() == replay_check.keys())
    for key in old_check:
        if key != 'input_sha256':
            check('complete checker field ' + key, old_check[key] == replay_check[key])
    expected_register = old_check['input_sha256'].copy()
    expected_register[str(producer.OUT.relative_to(ROOT))] = expected_register.pop(
        str(originals[0].relative_to(ROOT)))
    check('checker only changes certificate path', replay_check['input_sha256'] == expected_register)
    check('replay checker input hashes', all(digest(ROOT / n) == h
          for n, h in replay_check['input_sha256'].items()))
    previous_checker = load('two-site-actual-collar-check-1925.py')
    previous_checker.OUT = HERE / 'two-site-actual-collar-check-replay-1930.json'
    with redirect_stdout(io.StringIO()):
        previous_checker.main()
    replay_prior = read(previous_checker.OUT)
    check('full1925 checker exactly reproduces', prior_check == replay_prior)
    check('all full replays passed', replay_check['failures'] == replay_prior['failures'] == []
          and replay_check['status'] == replay_prior['status'] == 'passed')
    check('all3560 nodes and99 divisors checked', len(new['trace']) == replay_check['trace_nodes'] == 3560
          and len(new['divisors']) == replay_check['divisor_count'] == 99)
    check('all11019 independent checks reproduced', replay_check['checks'] == 11019)

    bounds = {}
    norm_outer = [(F(1), F(1)), (F(46209, 10**6), F(46212, 10**6)),
                  (F(3824, 10**6), F(3825, 10**6)), (F(436, 10**6), F(437, 10**6))]
    for j, record in enumerate(new['base']['norms']):
        lo, hi = interval(record)
        lower, upper = norm_outer[j]
        check('norm bound ' + str(j), lo == hi == 1 if j == 0 else lower < lo <= hi < upper)
        bounds['h' + str(j)] = {'actual': record,
            'required_outer': {'lower': str(lower), 'upper': str(upper)}}
    d_record = new['collar']['update_divisor']['value']
    v_record = new['collar']['predivision_variance']['value']
    d, v = interval(d_record), interval(v_record)
    check('printed complete determinant endpoints', d == (
        F(57353061649999427835432132832043829802624813700995013, 10**50),
        F(7356944911507680245224346931478959249122343572937320367, 10**50)))
    check('printed complete variance endpoints', v == (
        F(-1118463952817667705569661925865477998273697991324198801, 5*10**49),
        F(137107526243041901040766657432250636331662276054171621, 4*10**48)))
    check('strict printed determinant bound', F(573530616, 10**6) < d[0] <= d[1] <
          F(73569449116, 10**6))
    check('strict printed variance endpoint bounds', F(-22369279057, 10**6) < v[0] < 0 < v[1] <
          F(34276881561, 10**6))
    bounds['collar_update_divisor'] = {'actual': d_record, 'required_lower': '0', 'paid': d[0] > 0}
    bounds['collar_variance'] = {'actual': v_record, 'required_lower': '0', 'paid': v[0] > 0}
    check('every full divisor strictly positive', all(interval(row['interval'])[0] > 0
                                                   for row in new['divisors']))
    boundaries = [maximum_id(new[key]) for key in ('base', 'actual', 'point')]
    counts = dict.fromkeys(('base', 'actual', 'point', 'collar'), 0)
    full_divisors = []
    for row in new['trace']:
        if row['operation'] == 'reciprocal':
            stage = next((name for name, end in zip(('base', 'actual', 'point'), boundaries)
                          if row['id'] <= end), 'collar')
            counts[stage] += 1
            full_divisors.append({'reciprocal_node': row['id'], 'stage': stage,
                                 'input': new['trace'][row['inputs'][0]]})
    check('complete executed divisor stages', counts == {'base': 8, 'actual': 5, 'point': 46, 'collar': 40})
    check('exact prescribed domain', new['fixed_box'] == [['-1/4', '1/4'], ['3/4', '5/4']])
    check('trace ends at full unnormalized variance derivative',
          new['collar']['predivision_variance']['db']['trace_id'] == len(new['trace']) - 1)
    check('collar contains no normalized observables', not any(k in new['collar']
          for k in ('g', 'k', 'jacobian', 'range', 'K')))
    check('both signs stop before normalized residual and Krawczyk',
          set(new['orientations']) == {'1', '-1'} and all(
              x == {'krawczyk_evaluated': False, 'range_exclusion_evaluated': False,
                    'status': 'inconclusive_unpaid_variance',
                    'blocked': 'variance lower bound not positive'}
              for x in new['orientations'].values()))
    check('all original evidence preserved', all(digest(ROOT / p) == h
                                              for p, h in original_hashes.items()))
    failures = [name for name, passed in checks.items() if not passed]
    paths = originals + [Path(__file__), producer.OUT, checker.OUT, previous_checker.OUT,
        HERE / 'two-site-positive-update-1928.py', HERE / 'two-site-positive-update-check-1928.py',
        HERE / 'two-site-actual-collar-1925.py', HERE / 'two-site-actual-collar-check-1925.py',
        HERE / 'two-site-theta-jacobian-1921.py', HERE / 'two-site-theta-jacobian-check-1921.py']
    report = {'status': 'passed' if not failures else 'failed', 'checks': checks, 'failures': failures,
        'actual_required_bounds': bounds, 'trace_nodes': len(new['trace']),
        'divisor_count': len(full_divisors), 'divisor_stages': counts, 'all_full_divisors': full_divisors,
        'independent1928_checks': replay_check['checks'], 'independent1925_checks': replay_prior['checks'],
        'mathematical_threshold_failures': ['collar variance lower endpoint is not positive'],
        'original_sha256': original_hashes,
        'input_sha256': {str(p.relative_to(ROOT)): digest(p) for p in paths},
        'qualification': 'Conditional finite audit acceptance; inherited L917 containment and Decimal correctness assumed; no matching or nonmatching inference'}
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'checks': len(checks), 'failures': failures,
        'trace_nodes': report['trace_nodes'], 'divisor_count': report['divisor_count'],
        'divisor_stages': counts, 'actual_bounds': {'Delta': ['573.530616', '73569.449116'],
                                                'variance': ['-22369.279057', '34276.881561']},
        'required': 'positive lower endpoints for all divisors and variance before normalization',
        'mathematical_threshold_failures': report['mathematical_threshold_failures'],
        'certificate': str(OUT.relative_to(ROOT))}))
    assert not failures


if __name__ == '__main__':
    main()
