#!/usr/bin/env python3
"""Two bounded malformed/missing-data checks of the new production replay."""
import copy
import json
import traceback
from pathlib import Path

from verify_table import digest, replay

HERE = Path(__file__).resolve().parent


if __name__ == '__main__':
    certificate = HERE/'table_certificate.json'
    data = json.loads(certificate.read_text())
    original_paths = [certificate, HERE/'table_verification.json', HERE/'presentation.json',
                      HERE/'coupled_plan.json', HERE/'exponential_plan.json',
                      HERE/'coupled_plan_verification.json', HERE/'exponential_plan_verification.json',
                      HERE.parent/'nonunitary-cusp/reduced_phase_certificate.json',
                      HERE.parent/'nonunitary-cusp/exact_value_certificate.json']
    original_paths.extend(HERE/p['term_file'] for p in data['primitives'])
    before = {str(p.relative_to(HERE.parent.parent)): digest(p) for p in original_paths}
    destination = HERE/'table-replay-rejections'
    destination.mkdir(exist_ok=True)
    reports = []
    for label in ('missing-phase', 'malformed-partial'):
        altered = copy.deepcopy(data)
        if label == 'missing-phase':
            altered['phases'].pop()
        else:
            altered['phases'][0]['trace'][0]['partial'] = [True, False]
        path = destination/f'{label}.json'
        path.write_text(json.dumps(altered, separators=(',', ':'))+'\n')
        try:
            replay(altered)
            report = {'case': label, 'rejected': False}
        except Exception as exc:
            report = {'case': label, 'rejected': True, 'failure': repr(exc),
                      'traceback': traceback.format_exc()}
        report_path = destination/f'{label}-report.json'
        report_path.write_text(json.dumps(report, indent=2)+'\n')
        reports.append({'case': label, 'rejected': report['rejected'],
                        'altered_certificate': path.relative_to(HERE).as_posix(),
                        'report': report_path.relative_to(HERE).as_posix()})
    after = {str(p.relative_to(HERE.parent.parent)): digest(p) for p in original_paths}
    summary = {'cases': reports, 'originals_preserved': before == after,
               'before_sha256': before, 'after_sha256': after,
               'scope': 'two production-replay rejection tests; separate critical audit pending'}
    (destination/'summary.json').write_text(json.dumps(summary, indent=2)+'\n')
    print('rejections:', reports, 'originals preserved:', before == after,
          'summary: scripts/conductor36-table/table-replay-rejections/summary.json')
    assert all(r['rejected'] for r in reports) and before == after
