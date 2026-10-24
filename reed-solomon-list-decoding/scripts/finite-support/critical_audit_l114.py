"""Replay complete consumed L105 evidence; retain the L112/L113 joint audit.

All historical artifacts are immutable. Only the old verifier's in-memory
wall-clock start is refreshed; its mathematical inputs and checks are unchanged.
The replay elapsed time is not a new measurement of constructor-plus-verifier
time. No search, constructor, solve, box refinement or PSD test is performed.
"""
import hashlib
import importlib.util
import json
from pathlib import Path
import time
from types import SimpleNamespace

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'l114-critical-audit.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(name):
    return json.loads((B / name).read_text())


def module(name):
    spec = importlib.util.spec_from_file_location('audit_' + name, B / name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    start = time.monotonic()
    report = dict(stage='in_progress', checks=0, failures=[],
                  code_sha256=sha(Path(__file__)))

    def save():
        report['seconds'] = time.monotonic() - start
        OUT.write_text(json.dumps(report, indent=2) + '\n')

    def ck(label, condition):
        report['checks'] += 1
        if not condition:
            report['failures'].append(label)
            raise AssertionError(label)

    names = ['fixed-pair-row-capacity-results.json',
             'fixed-pair-row-capacity-verification.json',
             'fixed-pair-row-capacity-verify.py',
             'fixed_product_lower_implication.py',
             'fixed-product-lower-implication.json',
             'delsarte-lp-results.json', 'positive-factor-enclosure.json.gz',
             'enclosed-root-all-capacities-verification.json',
             'l112-l113-critical-audit.json']
    report['input_sha256'] = {
        str((B / name).relative_to(ROOT)): sha(B / name) for name in names}
    save()
    try:
        replay = module('fixed-pair-row-capacity-verify.py')
        replay.OUT = B / 'l105-l114-critical-reverification.json'

        def replay_loads(text):
            data = json.loads(text)
            if 'coefficient_entries' in data and 'started' in data:
                report['clock_adaptation'] = dict(
                    original_started=data['started'], replay_started=time.time(),
                    scope='In-memory timestamp only; all mathematical data unchanged. '
                          'Elapsed/cap now measures verifier replay only.')
                data['started'] = report['clock_adaptation']['replay_started']
            return data

        replay.json = SimpleNamespace(loads=replay_loads, dumps=json.dumps)
        replay.main()
        old = read('fixed-pair-row-capacity-verification.json')
        new = read('l105-l114-critical-reverification.json')
        operational = {'peak_live_bytes', 'total_elapsed_seconds'}
        ck('complete_replay_mathematical_equality',
           {k: v for k, v in old.items() if k not in operational} ==
           {k: v for k, v in new.items() if k not in operational})
        ck('complete_replay_pass', new['verified'] and not new['failures'])
        ck('complete_orbits_and_presentations',
           new['entries'] == 1500625 and new['visits'] == 9003750)
        ck('all_special_entries', new['repeated_entries'] == 205 and
           new['forbidden_entries'] == 10232)
        ck('replay_constructor_binding', new['construction_sha256'] ==
           sha(B / 'fixed-pair-row-capacity-results.json'))

        binding = module('fixed_product_lower_implication.py')
        binding.OUT = B / 'l114-critical-binding-reverification.json'
        binding.main()
        before = read('fixed-product-lower-implication.json')
        after = read('l114-critical-binding-reverification.json')
        ck('complete_binding_replay_equality', before == after)
        ck('all_bindings_pass', after['stage'] == 'verified' and not after['failures'])
        data = read('fixed-pair-row-capacity-results.json')
        q, P = data['denominator'], data['pair_numerators']
        ck('strict_permitted_pair_positivity', all(0 < P[i] <= q for i in range(5, 69)))
        ck('fixed_N_greater_than_two', data['N'] == 65537**28 // 2**128 + 1 > 2)
        rows = []
        for i in range(5, 69):
            r = new['rows'][i]
            residual = r['lower_numerator'] - 2 * P[i]
            ck('reconstructed_minimum_' + str(i), r['i'] == i and residual == 0)
            ck('two_repetitions_' + str(i), data['rows'][i]['repetitions'] ==
               [[0, 0, 0, 1], [i, i, i, 1]])
            rows.append(dict(i=i, pair_numerator=P[i], denominator=q,
                             reconstructed_minimum_numerator=r['lower_numerator'],
                             distinct_lower_sum_numerator=residual, required=0))
        report['rows'] = rows
        report['complete_replay_checks'] = new['checks']
        report['binding_replay_checks'] = after['checks']
        report['original_entries'] = new['entries']
        report['presentations'] = new['visits']
        report['raw_interval_check'] = (
            'Complete replay reconstructs all six raw inequalities before checking '
            'lower<=0<=upper for forbidden entries and before the zero override; '
            'Boolean entries are likewise checked before their override. '
            'Permitted distinct entries are not overridden.')
        report['scope'] = (
            'L114 lower implication and consumed L105 interval/minimum evidence. '
            'Reuse retained L112/L113 joint review; no new root/upper audit or PSD claim. '
            'L105 unrelated upper-attainment proof is not critically reviewed here.')
        for path, expected in report['input_sha256'].items():
            ck('unchanged_input:' + path, sha(ROOT / path) == expected)
        report['replay_sha256'] = {name: sha(B / name) for name in (
            'l105-l114-critical-reverification.json',
            'l114-critical-binding-reverification.json')}
        report['stage'] = 'verified'
    except Exception as exc:
        report['stage'] = 'failed'
        report['failures'].append(repr(exc))
        save()
        raise
    save()
    print('L114 audit:', report['stage'], '; additional checks:', report['checks'],
          '; failures:', len(report['failures']))
    print('64 reconstructed distinct lower sums: 0; required: 0.')
    print('Full certificate:', OUT)


if __name__ == '__main__':
    main()
