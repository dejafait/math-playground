#!/usr/bin/env python3
"""Replay the approved finite audit, retaining all original evidence."""
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path('scripts/dual-kernel')
OUT = ROOT/'critical-audit'


def load(name):
    spec = importlib.util.spec_from_file_location('audit_'+name, ROOT/name)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    failures, checks = [], {}

    def need(name, value):
        checks[name] = bool(value)
        if not value:
            failures.append(name)

    try:
        old = json.loads((OUT/'originals/manifest.json').read_text())
        need('all seven original snapshots preserved', all(
            sha(OUT/'originals'/Path(p).name) == h for p, h in old['files'].items()))
        need('only documented checker repair changed original seven files', all(
            p == str(ROOT/'verify_certificate.py') or sha(Path(p)) == h
            for p, h in old['files'].items()))
        need('complete rebuilt certificate byte equality',
             (OUT/'rebuilt-certificate.json').read_bytes() == (ROOT/'conductor389-certificate.json').read_bytes())
        v = load('verify_certificate.py')
        replay = v.verify(ROOT/'conductor389-certificate.json', Path('scripts/relative-t2/certificate.json'),
                          ROOT/'conductor389-arithmetic.json', OUT/'verification.json')
        previous = json.loads((ROOT/'conductor389-verification.json').read_text())
        need('full replay accepted', not replay['failures'])
        need('all linear check labels equal original', replay['checks'] == previous['checks'])
        need('summary exact expected equality', replay['summary'] == previous['summary'] == old['summary'])
        need('all full subordinate reports equal original', all(
            json.loads(Path(new['report']).read_text()) == json.loads(Path(prior['report']).read_text())
            for new, prior in zip(replay['structural_replays'], previous['structural_replays']))
             and len(replay['structural_replays']) == len(previous['structural_replays']) == 2)
        # Route only outputs/fixture copies to a fresh directory. Actual verifier
        # and producer modules retain their original __file__ and adapter paths.
        rejection = load('check_rejection.py')
        dest = OUT/'rejections'
        dest.mkdir(exist_ok=True)
        for filename in ('conductor389-arithmetic.json', 'conductor389-certificate.json'):
            (dest/filename).write_bytes((ROOT/filename).read_bytes())
        rejection.ROOT = dest
        rejection.module = load
        rejection.main()
        rr = json.loads((dest/'rejection-checks.json').read_text())
        need('complete 22 rejections and four fixtures equal originals', rr == json.loads((ROOT/'rejection-checks.json').read_text()))
        need('all required rejection and fixture cases pass', rr['actual_rejections'] == rr['required_rejections'] == 22
             and len(rr['synthetic_fixtures']) == 4 and not rr['failures'])
        for phase in ('before-repair', 'after-repair'):
            evidence = json.loads((OUT/phase/'persistence.json').read_text())
            if phase == 'before-repair':
                need('original persistence defect reproduced', evidence['outer_rejected'] and evidence['stale_success_retained'])
            else:
                need('failure persistence repair verified', evidence['outer_rejected'] and evidence['subordinate_failures']
                     and evidence['subordinate_bound_to_corruption'] and not evidence['stale_success_retained'])
    except Exception as error:
        failures.append(type(error).__name__+': '+str(error))
    finally:
        files = [ROOT/x for x in ('build_certificate.py', 'verify_certificate.py', 'check_rejection.py',
                                 'audit_failure_persistence.py', 'run_critical_audit.py', 'conductor389-arithmetic.json',
                                 'conductor389-certificate.json')]
        files += [Path('scripts/relative-t2')/x for x in ('certificate.json', 'verify_certificate.py', 'audit_certificate.py')]
        files += [Path('scripts/general-relative/verify_certificate.py')]
        files += [OUT/x for x in ('verification.json', 'preservation.json', 'before-repair/persistence.json',
                                 'after-repair/persistence.json', 'rejections/rejection-checks.json')]
        report = {'checks': checks, 'failures': failures,
                  'files': {str(p): sha(p) for p in files if p.exists()},
                  'summary': locals().get('replay', {}).get('summary'),
                  'qualification': 'Bounded fixed replay and inspected adapters; generic arithmetic remains conditional; no universal soundness theorem.'}
        (OUT/'manifest.json').write_text(json.dumps(report, indent=2)+'\n')
        print('audit checks actual/required', sum(checks.values()), '/', len(checks),
              '; failures', failures, '; evidence', OUT/'manifest.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
