#!/usr/bin/env python3
"""Four bounded L056 altered-evidence tests, with preserved original bytes.

Each case uses the full unchanged verifier; changed term-file hashes are
updated so rejection must reach arithmetic/completeness, not just hashing.
All changes occur in new case directories. No original artifact is written.
"""
import copy
import json
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path

import verify_table

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE/'table-critical-audit'


def dump(path, data):
    path.write_text(json.dumps(data, separators=(',', ':'))+'\n')


def run():
    original = json.loads((HERE/'table_certificate.json').read_text())
    results = []
    cases = ('missing-final-term', 'well-formed-final-partial', 'zero-row-quotient', 'last-source-relation')
    for label in cases:
        folder = OUT/'rejections'/label/'scripts'/'conductor36-table'
        folder.mkdir(parents=True, exist_ok=False)
        (folder.parent/'nonunitary-cusp').symlink_to(HERE.parent/'nonunitary-cusp', target_is_directory=True)
        for name in ('presentation.json', 'coupled_plan.json', 'exponential_plan.json'):
            (folder/name).symlink_to(HERE/name)
        terms = folder/'table-data'
        terms.mkdir()
        for p in original['primitives']:
            (folder/p['term_file']).symlink_to(HERE/p['term_file'])
        changed = copy.deepcopy(original)
        if label in ('missing-final-term', 'well-formed-final-partial'):
            path = folder/changed['primitives'][0]['term_file']
            lines = path.read_text().splitlines()
            assert len(lines) == 4860
            path.unlink()  # New case's symlink only; original target stays intact.
            if label == 'missing-final-term':
                lines.pop()
                expected = 'missing terms'
            else:
                term = json.loads(lines[-1])
                assert term[0] == 4860
                term[5] = [v+1 for v in term[5]]
                assert term[5][0] <= term[5][1]
                lines[-1] = json.dumps(term, separators=(',', ':'))
                expected = 'finite operation mismatch'
            path.write_text('\n'.join(lines)+'\n')
            changed['primitives'][0]['term_sha256'] = sha256(path.read_bytes()).hexdigest()
        elif label == 'zero-row-quotient':
            assert changed['generators'][28]['scaled_integer'] == 0
            changed['generators'][28]['quotient_endpoints'][0] = str(
                Q(changed['generators'][28]['quotient_endpoints'][0])+Q(1, 2**96))
            expected = "row['quotient_endpoints'] == list(map(str, quotients))"
        else:
            changed['relations']['source_images'][-1] = '1/24'
            expected = "data['relations'] == relation_checks"
        certificate = folder/'table_certificate.json'
        dump(certificate, changed)
        old_here = verify_table.HERE
        verify_table.HERE = folder
        try:
            verify_table.replay(changed)
            report = {'case': label, 'rejected': False, 'failures': ['altered certificate accepted']}
        except Exception as exc:
            trace = traceback.format_exc()
            report = {'case': label, 'rejected': True, 'exception': repr(exc),
                'traceback': trace, 'expected_failure': expected, 'expected_failure_reached': expected in trace,
                'altered_certificate': str(certificate.relative_to(ROOT)),
                'certificate_sha256': sha256(certificate.read_bytes()).hexdigest()}
        finally:
            verify_table.HERE = old_here
        report_path = folder.parent.parent/'report.json'
        dump(report_path, report)
        results.append({'case': label, 'rejected': report['rejected'],
            'expected_failure_reached': report.get('expected_failure_reached', False),
            'report': str(report_path.relative_to(ROOT))})
        print('altered evidence:', results[-1], flush=True)
    before = json.loads((OUT/'preservation-before.json').read_text())
    after = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in before}
    dump(OUT/'preservation-after-rejections.json', after)
    summary = {'cases': results, 'actual_rejections': sum(r['rejected'] for r in results),
        'required_rejections': len(cases), 'originals_preserved': before == after,
        'original_count': len(before), 'failures': [r for r in results if not (
            r['rejected'] and r['expected_failure_reached'])]}
    dump(OUT/'rejection-report.json', summary)
    print('rejections:', summary['actual_rejections'], '/', summary['required_rejections'],
          'originals preserved:', before == after, 'failures:', summary['failures'],
          'report: scripts/conductor36-table/table-critical-audit/rejection-report.json', flush=True)
    assert before == after and not summary['failures']


if __name__ == '__main__':
    run()
