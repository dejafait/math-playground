#!/usr/bin/env python3
"""Check fixed coefficient/provenance identities; never form N or compute ranks."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
EXPECTED = {
    'scripts/pair-free-envelope/cover.json': '4a2093ab88de97fdedf5cf7451bc423d6a974af6fed3ce675e009bf7161b6b75',
    'scripts/pair-free-envelope/verification.json': '88ac33a42b0012575d83fac0dd919417ef1b37ceee14ef28680d6943b97591f9',
    'scripts/pair-free-envelope/verify.py': 'f1c6a45e75f1a9e3c8dc271110a737c61320e536ea11128523f544d701d21c31',
}


def main():
    checks = []

    def check(ok, name):
        checks.append(dict(name=name, passed=bool(ok)))

    hashes = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in EXPECTED}
    check(hashes == EXPECTED, 'approved_input_hashes')
    cover = json.loads((ROOT/'scripts/pair-free-envelope/cover.json').read_text())
    prior = json.loads((ROOT/'scripts/pair-free-envelope/verification.json').read_text())
    check(cover['modulus'] == 97 and cover['S'] == S and cover['J'] == J, 'fixed_parameters')
    check(not prior['summary']['failures'], 'saved_verification_no_failures')
    check(prior['summary']['certificate_sha256'] == hashes['scripts/pair-free-envelope/cover.json'], 'saved_verification_binding')
    check(cover['nodes'][0]['history'] == [] and cover['nodes'][0]['span'] == 0, 'empty_root')
    check(cover['spans'][0]['kernel_basis'] == [[int(i == j) for j in range(21)] for i in range(21)], 'full_exterior_root')
    chain = []
    for parent_id, node_id, chosen, history in [(0,1,0,[0]), (1,2,51,[0,51]), (2,3,98,[0,51,98])]:
        parent, node = cover['nodes'][parent_id], cover['nodes'][node_id]
        check(node['id'] == node_id and node['parent'] == parent_id and node['chosen'] == chosen
              and node['span'] == node_id and node['history'] == history
              and history == parent['history']+[chosen], 'actual_transition_'+str(node_id))
        matches = [t for t in prior['transitions'] if (t['parent'],t['chosen'],t['span']) == (parent_id,chosen,node_id)]
        check(len(matches) == 1, 'unique_saved_transition_'+str(node_id))
        check(len(matches) == 1 and matches[0]['kernel_basis'] == cover['spans'][node_id]['kernel_basis'], 'whole_child_basis_'+str(node_id))
        chain.append(dict(node_id=node_id, parent=parent_id, history=history, saved_transition=matches))

    basis = cover['spans'][3]['kernel_basis']
    check(cover['spans'][3]['generating_history'] == [0,51,98], 'generating_history')
    check(basis == prior['spans'][3]['kernel_basis'], 'prior_complete_basis_binding')
    pairs = list(combinations(range(7), 2))
    e = [1,0,0,0,0,0,0]
    factors = [[int(i == j) for i in range(7)] for j in range(1,7)]
    wedges = [[(e[a]*w[b]-e[b]*w[a]) % 97 for a,b in pairs] for w in factors]
    coefficient_matches = sum(a == b for u,v in zip(basis,wedges) for a,b in zip(u,v))
    check(basis == wedges and len(basis) == 6, 'all_126_wedge_coefficients')
    check(all(w[0] == 0 for w in factors) and [w[1:] for w in factors] == [[int(i == j) for i in range(6)] for j in range(6)], 'homogeneous_parameter_recovery')

    # Direct products and expanded-polynomial Horner evaluation are independent
    # arithmetic paths for every original coefficient actually used below.
    I, K = list(combinations(S,2))[0], list(combinations(J,2))[0]
    O = [x for x in S if x not in I]
    roots = [x for x in J if x not in K]
    g_product = []
    for x in S:
        value = 1
        for y in roots:
            value = value*(x-y) % 97
        g_product.append(value)
    polynomial = [1]
    for y in roots:
        nxt = [0]*(len(polynomial)+1)
        for i,a in enumerate(polynomial):
            nxt[i] = (nxt[i]-y*a) % 97
            nxt[i+1] = (nxt[i+1]+a) % 97
        polynomial = nxt
    g_horner = []
    for x in S:
        value = 0
        for a in reversed(polynomial):
            value = (value*x+a) % 97
        g_horner.append(value)
    check(polynomial == [50,81,21,43,16,83,24,1], 'expanded_original_polynomial')
    check(g_product == g_horner == [28,72,44,81,42,9,33], 'independent_evaluations')
    z = min(O)
    values = dict(zip(S,g_product))
    Q = [[(values[z]*int(a == x)-values[x]*int(a == z)) % 97 for a in S] for x in O if x != z]
    expected_Q = [[0,0,16,44,0,0,0], [0,0,55,0,44,0,0], [0,0,88,0,0,44,0], [0,0,64,0,0,0,44]]
    check(I == (1,8) and K == (47,50) and z == 12, 'original_row_label')
    for label,record in [('cover',cover['universe'][0]), ('prior',prior['reconstructed_universe'][0])]:
        check(record['I'] == list(I) and record['K'] == list(K) and record['Q'] == Q == expected_Q, label+'_row_0_binding')
    qe = [sum(a*b for a,b in zip(row,e)) % 97 for row in Q]
    qw = [[sum(a*b for a,b in zip(row,w)) % 97 for w in factors] for row in Q]
    check(qe == [0]*4, 'common_factor_killed')
    check(qw == [row[1:] for row in expected_Q], 'whole_symbolic_row_image')
    check(e[S.index(z)] == 0 and values[z] == 44, 'zero_numerator_nonzero_denominator')
    failures = [c['name'] for c in checks if not c['passed']]
    summary = dict(outcome='UNIVERSAL_ZERO_SCALAR' if not failures else 'FAILED',
                   failures=failures, checks_passed=sum(c['passed'] for c in checks), checks_required=len(checks),
                   factor_coefficients_actual=coefficient_matches, factor_coefficients_required=126,
                   actual_history_transitions_actual=len(chain), actual_history_transitions_required=3,
                   numerator_actual=e[2], numerator_required=0, denominator_actual=values[z], denominator_required='nonzero',
                   new_block_rank_tests=0, cover_modified=False, frontier_obligations_retained=1665,
                   completeness='reused saved elimination, not reaudited', separate_critical_audit=False)
    out = dict(summary=summary, checks=checks, input_sha256=hashes,
               script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(), modulus=97, S=S, J=J,
               history=[0,51,98], node=3, span=3, saved_actual_history_chain=chain,
               saved_basis=basis, prior_basis=prior['spans'][3]['kernel_basis'],
               saved_rank=prior['spans'][3]['rank'], saved_minor_determinant=prior['spans'][3]['minor_determinant'],
               common_factor=e, parameter_vectors=factors, wedge_coefficients=wedges,
               row_0=dict(I=list(I), K=list(K), z=z, roots=roots, polynomial=polynomial,
                          g_product=g_product, g_horner=g_horner, Q=Q, Q_common_factor=qe,
                          Q_w_coefficients=qw, numerator=e[2], denominator=values[z]))
    (HERE/'certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Full certificate: scripts/span-3-prefix-scalar/certificate.json')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
