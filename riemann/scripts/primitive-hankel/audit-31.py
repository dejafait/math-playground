#!/usr/bin/env python3
"""Preserving replay of the already completed L876 audit, step31.

Only output names in audit-26.py are changed. No new mathematical test
or integration algorithm is introduced; conceptual inspection is in L876.
"""
import hashlib
import json
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent
    preserved = [directory / name for name in (
        'coefficient-test-24.py', 'coefficient-test-24.json',
        'audit-26.py', 'audit-26.json', 'coefficient-replay-26.json',
    )]
    before = {p.name: p.read_bytes() for p in preserved}
    audit_source = before['audit-26.py'].decode()
    for old, new in (
        ("'coefficient-replay-26.json'", "'coefficient-replay-31.json'"),
        ("'audit-26.json'", "'audit-31.json'"),
    ):
        assert audit_source.count(old) == 1
        audit_source = audit_source.replace(old, new)
    namespace = {'__name__': 'l876_preserving_repeat', '__file__': __file__}
    exec(compile(audit_source, str(directory / 'audit-26.py'), 'exec'), namespace)
    exit_code = namespace['main']()
    result_path = directory / 'audit-31.json'
    result = json.loads(result_path.read_text())
    result['repeated_audit'] = True
    result['preserved_inputs_sha256'] = {
        name: hashlib.sha256(data).hexdigest() for name, data in before.items()
    }
    for p in preserved:
        if p.read_bytes() != before[p.name]:
            result['failures'].append('Prior evidence changed: ' + p.name)
    result['decision'] = ('AUDIT_CHECK_FAILURE' if result['failures']
                          else 'REPEATED_AUDIT_CHECKS_PASS')
    result_path.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in (
        'decision', 'residual', 'required_threshold',
        'claimed_strict_bounds', 'failures',
    )}))
    print('Certificate:', result_path)
    return bool(exit_code or result['failures'])


if __name__ == '__main__':
    raise SystemExit(main())
