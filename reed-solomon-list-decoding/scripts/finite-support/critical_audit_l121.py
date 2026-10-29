"""Bind and replay the complete L121 certificate without changing old artifacts."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path

import verify_fixed_triple_fourth_capacity as verifier

B = Path(__file__).resolve().parent
ROOT = B.parent.parent
OUT = B / 'l121-critical-audit.json'
REPLAY = B / 'l121-critical-audit-replay.json'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--reuse-replay', action='store_true')
    args = parser.parse_args()
    report = dict(stage='in_progress', checks=0, failures=[], input_sha256={},
                  code_sha256=digest(Path(__file__)))

    def save():
        OUT.write_text(json.dumps(report, indent=2) + '\n')

    def check(label, ok):
        report['checks'] += 1
        if not ok:
            report['failures'].append(label)
            report['stage'] = 'failed'
            save()
            raise AssertionError(label)

    def bind(path):
        report['input_sha256'][str(path.relative_to(ROOT))] = digest(path)

    save()
    if not args.reuse_replay:
        verifier.OUT = REPLAY
        verifier.main()
    source = B / 'fixed-triple-fourth-capacity.json.gz'
    with gzip.open(source, 'rt') as stream:
        constructor = json.load(stream)
    original = json.loads((B / 'fixed-triple-fourth-capacity-verification.json').read_text())
    replay = json.loads(REPLAY.read_text())
    check('constructor_code_binding', constructor['code_sha256'] ==
          digest(B / 'fixed_triple_fourth_capacity.py'))
    check('verifier_code_binding', original['code_sha256'] == replay['code_sha256'] ==
          digest(B / 'verify_fixed_triple_fourth_capacity.py'))
    check('complete_replay_equals_original', replay == original)
    check('complete_constructor_binding', replay['constructor_sha256'] == digest(source))
    check('complete_summary_equality', constructor['summary'] == replay['summary'])
    check('complete_input_binding_equality', constructor['input_sha256'] == replay['input_sha256'])
    check('replayed_verdict', replay['stage'] == 'verified' and replay['failures'] == [] and
          replay['checks'] == 117635)
    check('constructor_verdict', constructor['stage'] == 'complete' and
          constructor['failures'] == [] and constructor['checks'] == 396970)
    for name, expected in constructor['input_sha256'].items():
        check('current_input:' + name, digest(ROOT / name) == expected)
        bind(ROOT / name)
    for name in ['l112-l113-critical-audit.json', 'l114-critical-audit.json']:
        audit = json.loads((B / name).read_text())
        check('retained_audit:' + name, audit['stage'] == 'verified' and audit['failures'] == [])
        for path, expected in audit['input_sha256'].items():
            check('retained_audit_input:' + path, digest(ROOT / path) == expected)
            bind(ROOT / path)
    for path in [source, REPLAY, B / 'fixed-triple-fourth-capacity-verification.json',
                 B / 'fixed_triple_fourth_capacity.py',
                 B / 'verify_fixed_triple_fourth_capacity.py']:
        bind(path)
    report.update(stage='verified', replay_checks=replay['checks'],
                  complete_original_report_equal=True, summary=replay['summary'],
                  ratio_integer_bracket=replay['ratio_integer_bracket'],
                  root_triple_bounds=replay['root_triple_bounds'],
                  scope='Complete L121 local certificate replay and input bindings; root existence is an audited input, not reproved.')
    save()
    print('Additional binding checks:', report['checks'], '; failures:', len(report['failures']))
    print('Complete replay checks:', replay['checks'], '; original report equality: True')
    print('Capacity/required strictly in (93301984669,93301984670); pass threshold: 1')
    print('Certificate:', OUT, '; replay:', REPLAY)


if __name__ == '__main__':
    main()
