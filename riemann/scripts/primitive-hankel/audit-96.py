#!/usr/bin/env python3
"""Preserving replay of L876's existing audit; no new mathematical test."""
import hashlib
import json
from pathlib import Path


def main():
    directory = Path(__file__).resolve().parent
    names = (
        'coefficient-test-24.py', 'coefficient-test-24.json',
        'audit-26.py', 'audit-26.json', 'coefficient-replay-26.json',
        'audit-31.py', 'audit-31.json', 'coefficient-replay-31.json',
    )
    before = {name: (directory / name).read_bytes() for name in names}
    source = before['audit-26.py'].decode()
    for old, new in (
        ("'coefficient-replay-26.json'", "'coefficient-replay-96.json'"),
        ("'audit-26.json'", "'audit-96.json'"),
    ):
        assert source.count(old) == 1
        source = source.replace(old, new)
    namespace = {'__name__': 'l876_preserving_repeat', '__file__': __file__}
    exec(compile(source, str(directory / 'audit-26.py'), 'exec'), namespace)
    exit_code = namespace['main']()
    output = directory / 'audit-96.json'
    result = json.loads(output.read_text())
    result['repeated_audit'] = True
    result['preserved_inputs_sha256'] = {
        name: hashlib.sha256(data).hexdigest() for name, data in before.items()
    }
    result['preserved_input_checks'] = {
        name: (directory / name).read_bytes() == data
        for name, data in before.items()
    }
    for name, passed in result['preserved_input_checks'].items():
        if not passed:
            result['failures'].append('Prior evidence changed: ' + name)
    result['decision'] = ('AUDIT_CHECK_FAILURE' if result['failures']
                          else 'REPEATED_AUDIT_CHECKS_PASS')
    result['qualification'] += '; step26 and step31 already verified this result; no new evidence or mathematical advance'
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({key: result[key] for key in (
        'decision', 'residual', 'required_threshold',
        'claimed_strict_bounds', 'failures',
    )}))
    print('Certificate:', output)
    return bool(exit_code or result['failures'])


if __name__ == '__main__':
    raise SystemExit(main())
