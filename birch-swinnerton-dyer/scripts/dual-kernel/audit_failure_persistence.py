#!/usr/bin/env python3
"""Exercise a real fixed-path assertion and preserve pre/post repair evidence."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(phase):
    spec = importlib.util.spec_from_file_location('audited_dual_checker', ROOT/'verify_certificate.py')
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    out = ROOT/'critical-audit'/phase
    out.mkdir(parents=True, exist_ok=True)
    c = json.loads(Path('scripts/relative-t2/certificate.json').read_bytes())
    # Keep shape, arithmetic, operators, minor, and segment counts unchanged.
    # Only a claimed Gamma0 matrix entry is corrupted, so the shape audit
    # passes but the complete geometric assertion must reject it.
    changed = None
    for i, path in enumerate(c['basepaths']):
        for key in ('start_chain', 'end_chain'):
            if path[key]['segments']:
                seg = path[key]['segments'][0]
                before = seg['Gamma0_reduction'][:]
                seg['Gamma0_reduction'][0] += 1
                changed = {'path_index': i, 'chain': key, 'segment_index': 0,
                           'before': before, 'after': seg['Gamma0_reduction'][:]}
                break
        if changed:
            break
    sr = (json.dumps(c, separators=(',', ':'))+'\n').encode()
    structural = out/'corrupted-structural.json'
    structural.write_bytes(sr)
    cert = json.loads((ROOT/'conductor389-certificate.json').read_bytes())
    cert['bindings']['structural_sha256'] = hashlib.sha256(sr).hexdigest()
    cp = out/'bound-corrupted-dual.json'
    cp.write_text(json.dumps(cert, separators=(',', ':'))+'\n')
    report_path = out/'verification.json'
    subordinate = out/'verification-structure/fixed-verification.json'
    subordinate.parent.mkdir(exist_ok=True)
    old = (ROOT/'conductor389-verification-structure/fixed-verification.json').read_bytes()
    subordinate.write_bytes(old)
    report = verifier.verify(cp, structural, ROOT/'conductor389-arithmetic.json', report_path)
    after = json.loads(subordinate.read_bytes())
    summary = {'phase': phase, 'mutation': changed,
               'checker_sha256': hashlib.sha256((ROOT/'verify_certificate.py').read_bytes()).hexdigest(),
               'outer_rejected': bool(report['failures']), 'outer_failures': report['failures'],
               'subordinate_failures': after['failures'],
               'stale_success_retained': subordinate.read_bytes() == old,
               'subordinate_bound_to_corruption': after.get('certificate_sha256') == hashlib.sha256(sr).hexdigest(),
               'required': 'outer and subordinate reject; subordinate bound to actual failed bytes',
               'report': str(report_path), 'subordinate_report': str(subordinate)}
    (out/'persistence.json').write_text(json.dumps(summary, indent=2)+'\n')
    print('outer rejected', summary['outer_rejected'], '; stale success retained', summary['stale_success_retained'],
          '; subordinate failures', summary['subordinate_failures'], '; evidence', out/'persistence.json')
    if phase == 'before-repair':
        if not summary['outer_rejected'] or not summary['stale_success_retained']:
            raise SystemExit('expected original persistence defect not reproduced')
    elif not (summary['outer_rejected'] and summary['subordinate_failures'] and
              summary['subordinate_bound_to_corruption'] and not summary['stale_success_retained']):
        raise SystemExit('failure persistence contract not repaired')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=['before-repair', 'after-repair'])
    run(p.parse_args().phase)
