#!/usr/bin/env python3
"""Separate L173 coefficient/provenance audit; no N, elimination or ranks.

Completeness of saved kernel identities is a premise. Read complete selected
records, but do not execute either the producer or its prior verifier.
"""
from hashlib import sha256
from itertools import combinations
from math import prod
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
EXPECTED_HASHES = {
    'scripts/pair-free-envelope/cover.json': '4a2093ab88de97fdedf5cf7451bc423d6a974af6fed3ce675e009bf7161b6b75',
    'scripts/pair-free-envelope/verification.json': '88ac33a42b0012575d83fac0dd919417ef1b37ceee14ef28680d6943b97591f9',
    'scripts/pair-free-envelope/verify.py': 'f1c6a45e75f1a9e3c8dc271110a737c61320e536ea11128523f544d701d21c31',
}


def main():
    checks = []

    def check(name, actual, required):
        checks.append(dict(name=name, passed=actual == required,
                           actual=actual, required=required))

    hashes = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in EXPECTED_HASHES}
    check('unchanged_premise_files', hashes, EXPECTED_HASHES)
    cover = json.loads((ROOT/'scripts/pair-free-envelope/cover.json').read_text())
    prior = json.loads((ROOT/'scripts/pair-free-envelope/verification.json').read_text())
    cert = json.loads((HERE/'certificate.json').read_text())
    check('prior_cover_hash', prior['summary']['certificate_sha256'], hashes['scripts/pair-free-envelope/cover.json'])
    check('prior_verifier_hash', prior['summary']['verifier_sha256'], hashes['scripts/pair-free-envelope/verify.py'])
    check('prior_failures', prior['summary']['failures'], [])
    check('short_checker_hash', cert['script_sha256'], sha256((HERE/'check.py').read_bytes()).hexdigest())
    check('short_certificate_hashes', cert['input_sha256'], hashes)
    check('field_and_labels', [cover['modulus'], cover['S'], cover['J']], [97, S, J])
    check('short_certificate_parameters', [cert['modulus'], cert['S'], cert['J'], cert['history'], cert['node'], cert['span']], [97, S, J, [0,51,98], 3, 3])
    root = [[int(i == j) for j in range(21)] for i in range(21)]
    check('full_root_441_entries', cover['spans'][0]['kernel_basis'], root)
    check('prior_full_root', prior['spans'][0]['kernel_basis'], root)
    check('root_history_and_span', [cover['nodes'][0]['id'], cover['nodes'][0]['history'], cover['nodes'][0]['span']], [0, [], 0])
    chain = []
    for nid, chosen in enumerate([0,51,98], 1):
        parent, child = cover['nodes'][nid-1:nid+1]
        expected_history = [0,51,98][:nid]
        check('node_'+str(nid), [child['id'], child['parent'], child['chosen'], child['span'], child['history'], parent['history']+[chosen]], [nid, nid-1, chosen, nid, expected_history, expected_history])
        # Select by actual parent and chosen label, not by expected span.
        transitions = [t for t in prior['transitions'] if t['parent'] == nid-1 and t['chosen'] == chosen]
        evaluations = [t for t in cover['evaluated_children'] if t['parent'] == nid-1 and t['chosen'] == chosen]
        expected = dict(parent=nid-1, chosen=chosen, span=nid)
        check('unique_cover_transition_'+str(nid), evaluations, [expected])
        check('unique_whole_saved_transition_'+str(nid), transitions, [dict(**expected, kernel_basis=cover['spans'][nid]['kernel_basis'])])
        check('generating_history_'+str(nid), cover['spans'][nid]['generating_history'], expected_history)
        check('complete_prior_child_'+str(nid), prior['spans'][nid]['kernel_basis'], cover['spans'][nid]['kernel_basis'])
        expected_chain = dict(node_id=nid, parent=nid-1, history=expected_history, saved_transition=transitions)
        check('short_certificate_chain_'+str(nid), cert['saved_actual_history_chain'][nid-1], expected_chain)
        chain.append(dict(parent_node=parent, child_node=child, saved_transition=transitions,
                          full_parent_basis=cover['spans'][parent['span']]['kernel_basis'],
                          full_child_basis=cover['spans'][child['span']]['kernel_basis']))
    check('chain_length', len(cert['saved_actual_history_chain']), 3)
    # In lexicographic pair order, (1,x) occupies coordinate x's index minus 1.
    coordinate_pairs = list(combinations(S, 2))
    expected_basis = [[int(pair == (1,x)) for pair in coordinate_pairs] for x in S[1:]]
    for name, basis in [('cover', cover['spans'][3]['kernel_basis']),
                        ('prior', prior['spans'][3]['kernel_basis']),
                        ('short_saved', cert['saved_basis']),
                        ('short_prior', cert['prior_basis']),
                        ('short_wedges', cert['wedge_coefficients'])]:
        check(name+'_all_126_coefficients', basis, expected_basis)
    check('saved_rank_and_minor_only', [prior['spans'][3]['rank'], prior['spans'][3]['minor_determinant'], cert['saved_rank'], cert['saved_minor_determinant']], [15,16,15,16])
    factors = [[int(i == j) for i in range(7)] for j in range(1,7)]
    check('all_six_parameter_vectors', cert['parameter_vectors'], factors)
    check('common_factor', cert['common_factor'], [1,0,0,0,0,0,0])

    # Independent polynomial path: elementary symmetric sums, no recurrence
    # from the earlier checker and no imported producer routines.
    roots = J[2:]
    polynomial = [((-1)**(7-k)*sum(prod(c) for c in combinations(roots,7-k))) % 97 for k in range(8)]
    values = [sum(a*x**k for k,a in enumerate(polynomial)) % 97 for x in S]
    check('polynomial_coefficients', polynomial, [50,81,21,43,16,83,24,1])
    check('all_original_values', values, [28,72,44,81,42,9,33])
    # Build quotient rows by normalized evaluations and clear denominators.
    # Each row is g(z)*g(x)*(h_x/g(x)-h_z/g(z)).
    zpos = 2
    q = []
    for xpos in range(3,7):
        row = [0]*7
        row[xpos] = pow(values[xpos],-1,97)
        row[zpos] = -pow(values[zpos],-1,97) % 97
        q.append([a*values[xpos]*values[zpos] % 97 for a in row])
    check('all_28_Q_coefficients', q, [[0,0,16,44,0,0,0], [0,0,55,0,44,0,0], [0,0,88,0,0,44,0], [0,0,64,0,0,0,44]])
    for name, rec in [('cover', cover['universe'][0]), ('prior', prior['reconstructed_universe'][0]), ('short', cert['row_0'])]:
        check(name+'_original_row_binding', [rec['I'],rec['K'],rec['Q']], [S[:2], J[:2], q])
    expected_row = dict(I=S[:2], K=J[:2], z=12, roots=roots,
                        polynomial=polynomial, g_product=values, g_horner=values, Q=q,
                        Q_common_factor=[0]*4, Q_w_coefficients=[r[1:] for r in q],
                        numerator=0, denominator=44)
    check('whole_short_row_record', cert['row_0'], expected_row)
    check('short_named_check_count', len(cert['checks']), 27)
    check('short_named_checks_pass', [c['passed'] for c in cert['checks']], [True]*27)
    check('short_report_counts', [cert['summary']['factor_coefficients_actual'], cert['summary']['factor_coefficients_required'], cert['summary']['actual_history_transitions_actual'], cert['summary']['actual_history_transitions_required']], [126,126,3,3])
    failures = [c['name'] for c in checks if not c['passed']]
    summary = dict(outcome='QUALIFIED_AUDIT_PASS' if not failures else 'FAILED',
                   checks_passed=sum(c['passed'] for c in checks), checks_required=len(checks),
                   failures=failures, exterior_coefficients_actual=126, exterior_coefficients_required=126,
                   root_coefficients_actual=441, root_coefficients_required=441,
                   Q_coefficients_actual=28, Q_coefficients_required=28,
                   transitions_actual=len(chain), transitions_required=3,
                   scalar_numerator_actual=0, scalar_numerator_required=0,
                   scalar_denominator_actual=values[2], scalar_denominator_required='nonzero',
                   new_block_rank_tests=0, completeness='explicit saved-elimination premise; not reaudited',
                   cover_modified=False, frontier_obligations_retained=1665)
    output = dict(summary=summary, checks=checks, input_sha256=hashes,
                  script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  short_certificate_sha256=sha256((HERE/'certificate.json').read_bytes()).hexdigest(),
                  complete_root=root, complete_selected_transitions=chain,
                  coordinate_pairs=coordinate_pairs, complete_exterior_basis=expected_basis,
                  independently_reconstructed_row_0=expected_row)
    (HERE/'critical-audit.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Full certificate: scripts/span-3-prefix-scalar/critical-audit.json')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
