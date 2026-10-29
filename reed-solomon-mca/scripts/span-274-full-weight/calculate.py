#!/usr/bin/env python3
"""Coefficient certificate for one saved-kernel scalar obstruction; no ranks."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
HISTORY = [0, 51, 98, 177, 318]
EXPECTED_HASHES = {
    'scripts/pair-free-envelope/cover.json': '4a2093ab88de97fdedf5cf7451bc423d6a974af6fed3ce675e009bf7161b6b75',
    'scripts/pair-free-envelope/verification.json': '88ac33a42b0012575d83fac0dd919417ef1b37ceee14ef28680d6943b97591f9',
    'scripts/pair-free-envelope/verify.py': 'f1c6a45e75f1a9e3c8dc271110a737c61320e536ea11128523f544d701d21c31',
}


def main():
    failures = []

    def check(ok, name):
        if not ok:
            failures.append(name)

    hashes = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in EXPECTED_HASHES}
    check(hashes == EXPECTED_HASHES, 'approved_input_hashes')
    cover = json.loads((ROOT/'scripts/pair-free-envelope/cover.json').read_text())
    prior = json.loads((ROOT/'scripts/pair-free-envelope/verification.json').read_text())
    span, node = cover['spans'][274], cover['nodes'][1006]
    check(cover['modulus'] == 97 and cover['S'] == S and cover['J'] == J, 'parameters')
    check(node['id'] == 1006 and node['span'] == 274 and node['history'] == HISTORY, 'actual_history')
    check(span['generating_history'] == [0,51,98,143,318], 'different_generating_history')
    check(not prior['summary']['failures'] and prior['summary']['certificate_sha256'] == hashes['scripts/pair-free-envelope/cover.json'], 'saved_verification_binding')
    check(prior['spans'][274]['kernel_basis'] == span['kernel_basis'], 'saved_complete_basis')
    # Bind this actual history to previously checked child kernels. Do not recalculate them.
    chain = []
    current = node
    while current['history']:
        parent = cover['nodes'][current['parent']]
        key = {k: current[k] for k in ('parent', 'chosen', 'span')}
        matches = [t for t in prior['transitions'] if all(t[k] == val for k,val in key.items())]
        check(len(matches) == 1, 'saved_transition_'+str(current['id']))
        check(current['history'] == parent['history']+[current['chosen']], 'history_step_'+str(current['id']))
        if matches:
            check(matches[0]['kernel_basis'] == cover['spans'][current['span']]['kernel_basis'], 'child_basis_'+str(current['id']))
        chain.append(dict(node_id=current['id'], history=current['history'], parent_history=parent['history'], saved_transition=matches))
        current = parent
    check(current['id'] == 0 and current['span'] == 0 and len(chain) == 5, 'complete_saved_chain')

    e = [1,0,0,0,0,0,0]
    W = [[0,1,0,0,0,0,0], [0,0,1,79,0,65,95], [0,0,0,0,1,0,0]]
    pairs = list(combinations(range(7), 2))
    factored = [[(e[a]*w[b]-e[b]*w[a]) % 97 for a,b in pairs] for w in W]
    check(factored == span['kernel_basis'], 'all_factor_coefficients')
    check([[w[i] for i in (1,2,4)] for w in W] == [[1,0,0],[0,1,0],[0,0,1]], 'parameter_recovery_coordinates')
    check(all(w[0] == 0 for w in W), 'zero_label_1_coordinate')
    roots = J[2:]

    def g(x):
        value = 1
        for y in roots:
            value = value*(x-y) % 97
        return value

    Q = [[(g(12)*int(a == x)-g(x)*int(a == 12)) % 97 for a in S] for x in [18,22,27,33]]
    check(cover['universe'][0]['I'] == [1,8] and cover['universe'][0]['K'] == [47,50] and Q == cover['universe'][0]['Q'] == prior['reconstructed_universe'][0]['Q'], 'original_row_0')
    qe = [sum(a*b for a,b in zip(row,e)) % 97 for row in Q]
    check(qe == [0]*4 and e[2] == 0 and g(12) != 0, 'recovery_scalar_identity')
    qw_coeff = [[sum(a*b for a,b in zip(row,w)) % 97 for w in W] for row in Q]
    out = dict(input_sha256=hashes, script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               modulus=97, S=S, J=J, history=HISTORY, node=1006, span=274,
               saved_generating_history=span['generating_history'], saved_kernel_basis=span['kernel_basis'],
               saved_completeness_evidence=prior['spans'][274], saved_actual_history_chain=chain,
               common_factor=e, parameter_vectors=W, wedge_coefficients=factored,
               row_0=dict(I=[1,8], K=[47,50], z=12, roots=roots,
                          g_on_S=[g(x) for x in S], Q=Q, Q_common_factor=qe,
                          Q_w_coefficients=qw_coeff, recovery_numerator=e[2], denominator=g(12)),
               summary=dict(outcome='UNIVERSAL_ZERO_SCALAR' if not failures else 'FAILED', failures=failures,
                            factor_coefficients_actual=63, factor_coefficients_required=63,
                            saved_history_transitions_actual=len(chain), saved_history_transitions_required=5,
                            row_0_zero_image_actual=sum(x == 0 for x in qe), row_0_zero_image_required=4,
                            recovery_numerator_actual=e[2], recovery_numerator_required=0,
                            recovery_denominator_actual=g(12), recovery_denominator_required='nonzero',
                            coverage='all nonzero homogeneous parameters over every extension of F_97; rank-zero branch rejected by L109',
                            completeness='reused saved verification, not rerun or separately audited',
                            new_block_rank_tests=0, frontier_obligations_retained=1665, cover_modified=False))
    (HERE/'certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out['summary'],sort_keys=True))
    print('Full certificate: scripts/span-274-full-weight/certificate.json')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
