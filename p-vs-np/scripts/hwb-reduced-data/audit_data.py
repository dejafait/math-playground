#!/usr/bin/env python3
"""L028 finite audit; full saved-data replay and an in-family Boolean test.

The all-n argument remains in L028. This does not test OBDD hardness or
replace the formal proof with finite evaluations.
"""
import json
from pathlib import Path

import check_data as data


def json_form(value):
    return json.loads(json.dumps(value))


def main():
    directory = Path(__file__).parent
    saved = json.loads((directory / 'data-results.json').read_text())
    replay = []
    for index, certificate in enumerate(saved['certificates']):
        summary, regenerated = data.check(certificate['n'])
        # Compare complete arrays/words/assignments, not their previews.
        assert json_form(regenerated) == certificate
        assert json_form(summary) == saved['summary'][index]
        replay.append(summary)

    n = 10
    proof, circuit, positive, signed, relations, deltas, prefixes = data.build_data(n)
    abstract = []
    associations = {}

    def add(kind, root, variable=None, operands=()):
        label = len(abstract) + 1
        assert all(1 <= operand < label for operand in operands)
        abstract.append(dict(label=label, kind=kind, root=root,
                             variable=variable, operands=list(operands)))
        return label

    add('constant', circuit.zero)
    add('constant', circuit.one)
    for variable in range(1, n + 1):
        assert circuit.nodes[positive[variable]] == ['var', variable]
        associations[variable] = add('original', positive[variable], variable)
        associations[-variable] = add('signed', signed[variable], -variable,
                                      (associations[variable],))
    for variable, left, right in proof['gates']:
        associations[variable] = add('reduced_and', positive[variable], variable,
                                      (associations[left], associations[right]))
        associations[-variable] = add('signed', signed[variable], -variable,
                                       (associations[variable],))
        left_root = positive[left] if left > 0 else signed[-left]
        right_root = positive[right] if right > 0 else signed[-right]
        assert circuit.nodes[relations[variable]] == ['mul', deltas[variable], circuit.j]
        delta_record = circuit.nodes[deltas[variable]]
        assert delta_record[:2] == ['add', positive[variable]]
        assert circuit.nodes[delta_record[2]] == ['mul', left_root, right_root]
    for variable in positive:
        assert circuit.nodes[signed[variable]] == ['add', circuit.one, positive[variable]]
    assert len(abstract) == 2*n + 4*proof['circuit_gate_count'] + 2
    assignments = data.check_assignments(proof, circuit, positive, signed)
    assert len(assignments) == 2**n

    bad_proof, bad_circuit, bad_positive, bad_signed, *_ = data.build_data(n, corrupt_cutoff=True)
    try:
        data.check_assignments(bad_proof, bad_circuit, bad_positive, bad_signed)
    except AssertionError as error:
        corruption = str(error)
    else:
        raise AssertionError('late accumulator cutoff passed the in-family test')

    summary = dict(saved_certificates_replayed=len(replay),
                   saved_formal_relations_replayed=sum(r['formal_relations_checked'] for r in replay),
                   in_family_n=n, assignments_checked=len(assignments),
                   signed_extensions_per_assignment=2*len(proof['gates']),
                   abstract_nodes_checked=len(abstract),
                   ordered_relation_associations_checked=len(relations),
                   cutoff_corruption_failure=corruption, failures=[])
    output = directory / 'audit-results.json'
    output.write_text(json.dumps(dict(summary=summary, replay_bounds=replay,
                                      in_family_certificate=dict(
                                          nodes=circuit.nodes, positive_roots=positive,
                                          signed_roots=signed, relation_roots=relations,
                                          delta_roots=deltas, abstract_nodes=abstract,
                                          actual_signed_and_definitions=proof['gates'],
                                          accumulator_prefixes=prefixes,
                                          assignments=assignments)), indent=2) + '\n')
    print(f"Full replay: {len(replay)} saved certificates, "
          f"{summary['saved_formal_relations_replayed']} free-word relations; failures=[]")
    print(f"n={n}: assignments={len(assignments)}/{2**n}, "
          f"abstract nodes={len(abstract)}, relations={len(relations)}; failures=[]")
    for row in replay:
        print(f"n={row['n']}: gates={row['gates']}/{row['gate_bound']}, "
              f"degree={row['representative_degree_actual']}/{row['d']}, "
              f"H degree={row['witness_degree_actual']}/{row['h']}, "
              f"E={row['E_padded_bits']}/{row['E_bound_bits']} bits")
    print(f'Late-cutoff corruption rejected: {corruption}; certificate: {output}')


if __name__ == '__main__':
    main()
