#!/usr/bin/env python3
"""Bounded intended-error fixtures; retain originals and exact failing prefixes."""
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path('scripts/conductor389-kurihara')
OUT = ROOT/'rejections'


def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def main():
    OUT.mkdir(exist_ok=True)
    originals = [ROOT/n for n in ('certificate.json', 'terms.jsonl', 'verification.json', 'replay.jsonl')]
    before = {str(p): sha(p) for p in originals}
    cert = json.loads((ROOT/'certificate.json').read_text())
    with (ROOT/'terms.jsonl').open() as f:
        prefix = [json.loads(f.readline()) for _ in range(3)]
    bad_term = copy.deepcopy(prefix)
    bad_term[0]['term'] = (bad_term[0]['term']+1) % 7
    cases = [('missing-second-term', [prefix[0], prefix[2]], 'unit ordering a=2'),
             ('duplicate-first-term', [prefix[0], prefix[0], prefix[2]], 'unit ordering a=2'),
             ('altered-contribution', bad_term, 'altered contribution a=1'),
             ('ineligible-pair', prefix, 'selected pair is not the certified first eligible pair')]
    reports, failures = [], []
    for name, rows, expected in cases:
        fixture = OUT/(name+'-terms.jsonl')
        fixture.write_text(''.join(json.dumps(r, separators=(',', ':'))+'\n' for r in rows))
        c = copy.deepcopy(cert)
        c['terms_sha256'] = sha(fixture)
        if name == 'ineligible-pair':
            c['selected_pair'] = [29, 113]
        cp = OUT/(name+'-certificate.json')
        cp.write_text(json.dumps(c, indent=2)+'\n')
        rp = OUT/(name+'-report.json')
        run = subprocess.run([sys.executable, str(ROOT/'verify_certificate.py'),
                              '--certificate', str(cp), '--terms', str(fixture),
                              '--out', str(rp), '--replay', str(OUT/(name+'-replay.jsonl'))],
                             capture_output=True, text=True)
        (OUT/(name+'-stdout.txt')).write_text(run.stdout+run.stderr)
        report = json.loads(rp.read_text())
        rejected = run.returncode != 0 and report['failures'] == ['AssertionError: '+expected]
        reports.append({'case': name, 'rejected_for_intended_reason': rejected,
                        'expected': expected, 'report': str(rp),
                        'fixture_terms': len(rows),
                        'qualification': 'retained prefix; intended failure precedes omitted suffix'})
        if not rejected:
            failures.append(name)
    unchanged = {str(p): sha(p) for p in originals} == before
    if not unchanged:
        failures.append('originals changed')
    (ROOT/'rejection-checks.json').write_text(json.dumps({
        'cases': reports, 'original_sha256': before,
        'originals_unchanged': unchanged, 'failures': failures}, indent=2)+'\n')
    print('intended rejections', sum(r['rejected_for_intended_reason'] for r in reports),
          '/', len(cases), 'originals unchanged', unchanged, 'failures', failures,
          'report', ROOT/'rejection-checks.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
