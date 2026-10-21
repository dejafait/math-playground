#!/usr/bin/env python3
"""Bounded sensitivity checks for the implementation's load-bearing contracts.

Does not constitute the later critical audit. Full mutation specifications
and failure evidence are saved, using the unchanged full input certificates.
"""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path('scripts/general-relative')
spec = importlib.util.spec_from_file_location('independent_replay', ROOT/'verify_certificate.py')
verifier = importlib.util.module_from_spec(spec)
spec.loader.exec_module(verifier)


def replace(cert, path, value):
    parent = cert
    for key in path[:-1]:
        parent = parent[key]
    parent[path[-1]] = value


def main():
    cases = [
        (1, 'empty shape loss', ['presentation', 'Pi', 'cols'], 0),
        (1, 'bool in row log', ['presentation', 'row_operations', 0, 3], True),
        (15, 'missing primitive pair', ['cosets', 'assignments'], 'DROP_LAST'),
        (15, 'wrong relation multiplicity', ['A', 'entries', 0, 0], 99),
        (15, 'missing Hecke summand', ['operators', 'T2', 'paths', 0], 'DROP_LAST'),
        (15, 'reversed segment orientation', ['basepaths', 0, 'end_chain', 'segments', 0, 'start'], [0, 1]),
        (15, 'wrong saturated image', ['operators', 'T2', 'saturated_images', 'entries', 0, 0], 1),
        (15, 'out of bounds operation', ['presentation', 'row_operations', 0, 1], 48),
    ]
    results = []
    for n, name, pointer, value in cases:
        source = ROOT/f'N{n}-certificate.json'
        cert = json.loads(source.read_text())
        mutated = copy.deepcopy(cert)
        if value == 'DROP_LAST':
            original = mutated
            for key in pointer:
                original = original[key]
            value = original[:-1]
        replace(mutated, pointer, value)
        checker = verifier.Checker()
        failure = None
        try:
            verifier.replay(checker, mutated, n, [2])
        except verifier.ReplayError as error:
            failure = str(error)
        results.append({'case': name, 'source': str(source), 'pointer': pointer,
                        'replacement': value, 'expected': 'ReplayError',
                        'actual_failure': failure, 'rejected': failure is not None,
                        'checks_passed_before_rejection': len(checker.checks)})
    report = {'cases': results, 'actual_rejections': sum(r['rejected'] for r in results),
              'required_rejections': len(results),
              'failures': [r['case'] for r in results if not r['rejected']]}
    output = ROOT/'rejection-checks.json'
    output.write_text(json.dumps(report, indent=2)+'\n')
    print(f"checker sensitivity: rejected {report['actual_rejections']}/{len(results)}; "
          f"failures={len(report['failures'])}; artifact={output}")
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
