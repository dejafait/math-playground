#!/usr/bin/env python3
"""Compare complete paired-reachable replay certificates; receive path bindings."""

import argparse
import json
from pathlib import Path


def load(path):
    return json.loads(path.read_text())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--old', type=Path, required=True)
    parser.add_argument('--new', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    old_path = args.old / 'paired-reachable.json'
    new_path = args.new / 'paired-reachable.json'
    old, new = load(old_path), load(new_path)
    old_audit = load(args.old / 'audit.json')
    new_audit = load(args.new / 'audit.json')
    checks = {
        'complete_constructor_value_equality': old == new,
        'old_audit_source_binding': old_audit.get('source_certificate') == str(old_path),
        'new_audit_source_binding': new_audit.get('source_certificate') == str(new_path),
        'complete_audit_value_equality_except_received_path':
            {k: v for k, v in old_audit.items() if k != 'source_certificate'} ==
            {k: v for k, v in new_audit.items() if k != 'source_certificate'},
        'all_failure_lists_empty': all(
            value.get('failures') == [] for value in (old, new, old_audit, new_audit)),
    }
    totals = {
        'coordinate_subsets_actual_required': [sum(new['subsets_examined_by_weight']), 12951],
        'all_codewords_actual_required': [len(new['all_K_rows']), 512],
        'dimension_actual_required': [new['dimension'], 9],
        'projection_rank_actual_required': [new['r_projection_rank'], 4],
        'minimum_basis_support_actual_required': [new['minimum_basis_support'], 38],
    }
    for name, (actual, required) in totals.items():
        checks[name] = actual == required
    failures = [name for name, passed in checks.items() if not passed]
    receipt = {
        'old_constructor': str(old_path), 'new_constructor': str(new_path),
        'old_audit': str(args.old / 'audit.json'),
        'new_audit': str(args.new / 'audit.json'),
        'comparison': 'Complete decoded nested-value equality; only the separately checked audit input-path field differs.',
        'checks': checks, 'actual_required': totals,
        'complete_threshold_ranks': new['all_threshold_ranks'],
        'failures': failures,
        'qualification': 'Finite replay comparison; the all-k obstruction requires L127 mathematical audit.',
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2) + '\n')
    print(f'Complete equality checks passed: {sum(checks.values())}/{len(checks)}.')
    for name, pair in totals.items():
        print(f'{name}: {pair[0]}/{pair[1]}')
    print(f'Failures: {failures}; full receipt: {args.output}')
    raise SystemExit(bool(failures))


if __name__ == '__main__':
    main()
