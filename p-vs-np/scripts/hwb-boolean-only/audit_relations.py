#!/usr/bin/env python3
"""Replay complete L029 diagnostics without changing the earlier certificate."""
import hashlib
import json
from pathlib import Path

from check_relations import run


def main():
    source = Path(__file__).with_name('relations-results.json')
    original_bytes = source.read_bytes()
    saved = json.loads(original_bytes)
    cases = []
    failures = []
    for index, n in enumerate((2, 3)):
        # Normalize tuples and integer dictionary keys to their JSON encodings.
        regenerated = json.loads(json.dumps(run(n)))
        matches = regenerated == saved['cases'][index]
        checks = {
            'entire_saved_case_matches': matches,
            'all_relations_and_bridges_pass': not regenerated['failures'],
            'representative_syntactic_degree': regenerated['max_d'] <= n + 1,
            'relation_syntactic_degree': regenerated['max_h'] <= 3 * n,
            'all_atomic_widths': all(max(d['widths']) <= n + 2
                                     for d in regenerated['diagrams']),
            'all_gate_kinds_covered': {r['kind'] for r in regenerated['relations']}
                == {'z0', 'u', 'v', 'w', 't', 'd', 'h', 'accumulator'},
            'encoding_within_common_dag_ceiling': regenerated['actual_padded_encoding_bits']
                <= regenerated['common_dag_copy_ceiling_bits'],
            'bridge_deletion_detected': regenerated['mutation_rejections'] > 0,
            'no_clause_placeholder_nodes': all(g[0] in {'const', 'var', 'bool', 'comm', 'add', 'mul'}
                                               for g in regenerated['dag_nodes']),
        }
        failures.extend([n, name] for name, ok in checks.items() if not ok)
        cases.append({'n': n, 'checks': checks, 'complete_replayed_certificate': regenerated})
        print(f"n={n}: full saved comparison={matches}, "
              f"relations={regenerated['checked_relations']}, "
              f"bridges={regenerated['checked_signed_bridges']}, "
              f"d={regenerated['max_d']}/{n + 1}, h={regenerated['max_h']}/{3 * n}, "
              f"encoding={regenerated['actual_padded_encoding_bits']}/"
              f"{regenerated['common_dag_copy_ceiling_bits']}, "
              f"mutation rejections={regenerated['mutation_rejections']}")
    if source.read_bytes() != original_bytes:
        failures.append(['source_certificate_changed'])
    if len(saved['cases']) != len(cases):
        failures.append(['saved_case_count'])
    output = Path(__file__).with_name('audit-results.json')
    output.write_text(json.dumps({
        'scope': 'Complete finite replay only; n=2,3 are outside the theorem family. '
                 'The all-n informal audit is recorded in L029.',
        'source_certificate': str(source.relative_to(Path.cwd())),
        'source_sha256': hashlib.sha256(original_bytes).hexdigest(),
        'cases': cases,
        'failures': failures,
    }, indent=2) + '\n')
    print('Failures:', failures)
    print('Full audit certificate:', output.relative_to(Path.cwd()))
    assert not failures, failures


if __name__ == '__main__':
    main()
