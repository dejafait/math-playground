#!/usr/bin/env python3
"""Independent coordinate/Horner verification; imports no producer code."""
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def main():
    data = json.loads((HERE/'certificate.json').read_text())
    failures, checks = [], []

    def check(ok, name):
        checks.append(dict(name=name, passed=bool(ok)))
        if not ok:
            failures.append(name)

    S, J = [1,8,12,18,22,27,33], [47,50,64,70,75,79,85,89,96]
    check(data['modulus'] == 97 and data['S'] == S and data['J'] == J and data['history'] == [0,51,98,177,318], 'fixed_parameters')
    for p,digest in data['input_sha256'].items():
        check(sha256((ROOT/p).read_bytes()).hexdigest() == digest, 'input_hash_'+p)
    cover = json.loads((ROOT/'scripts/pair-free-envelope/cover.json').read_text())
    prior = json.loads((ROOT/'scripts/pair-free-envelope/verification.json').read_text())
    check(not prior['summary']['failures'] and prior['summary']['certificate_sha256'] == data['input_sha256']['scripts/pair-free-envelope/cover.json'], 'prior_verification_binding')
    check(data['saved_completeness_evidence'] == prior['spans'][274] and data['saved_kernel_basis'] == prior['spans'][274]['kernel_basis'] == cover['spans'][274]['kernel_basis'], 'prior_complete_basis_binding')
    chain = data['saved_actual_history_chain']
    check(len(chain) == 5 and chain[0]['node_id'] == 1006, 'five_step_chain')
    expected_id = 1006
    for part in chain:
        node = cover['nodes'][expected_id]
        parent = cover['nodes'][node['parent']]
        check(part['node_id'] == expected_id and part['history'] == node['history'] == parent['history']+[node['chosen']] and part['parent_history'] == parent['history'], 'chain_history_'+str(expected_id))
        matches = [t for t in prior['transitions'] if (t['parent'],t['chosen'],t['span']) == (node['parent'],node['chosen'],node['span'])]
        check(len(matches) == 1 and part['saved_transition'] == matches and matches[0]['kernel_basis'] == cover['spans'][node['span']]['kernel_basis'], 'saved_child_kernel_'+str(expected_id))
        expected_id = node['parent']
    check(expected_id == 0 and cover['nodes'][0]['history'] == [] and cover['nodes'][0]['span'] == 0, 'empty_root')
    # Independently specify sparse factors by label and check each exterior coefficient.
    expected = [{8:1}, {12:1,18:79,27:65,33:95}, {22:1}]
    reconstructed = [[(w.get(b,0) if a == 1 else 0) for a,b in combinations(S,2)] for w in expected]
    check(reconstructed == data['saved_kernel_basis'] == data['wedge_coefficients'], 'all_63_factor_coefficients')
    check(data['parameter_vectors'] == [[w.get(a,0) for a in S] for w in expected] and data['common_factor'] == [1,0,0,0,0,0,0], 'all_factor_vectors')
    check([[w.get(a,0) for w in expected] for a in (8,12,22)] == [[1,0,0],[0,1,0],[0,0,1]], 'nonzero_parameters_give_independence')
    poly = [1]
    for y in [64,70,75,79,85,89,96]:
        nxt = [0]*(len(poly)+1)
        for i,c in enumerate(poly):
            nxt[i] = (nxt[i]-y*c) % 97
            nxt[i+1] = (nxt[i+1]+c) % 97
        poly = nxt

    def value(x):
        out = 0
        for c in reversed(poly):
            out = (out*x+c) % 97
        return out

    Q = [[(value(12)*(a == x)-value(x)*(a == 12)) % 97 for a in S] for x in (18,22,27,33)]
    row = data['row_0']
    check(row['I'] == [1,8] and row['K'] == [47,50] and row['z'] == 12 and row['roots'] == J[2:] and row['g_on_S'] == [value(x) for x in S], 'original_polynomial')
    check(Q == row['Q'] == cover['universe'][0]['Q'] == prior['reconstructed_universe'][0]['Q'], 'all_original_Q_coefficients')
    check([r[0] for r in Q] == row['Q_common_factor'] == [0]*4, 'common_factor_is_killed')
    qw = [[sum(c*w.get(a,0) for a,c in zip(S,r)) % 97 for w in expected] for r in Q]
    check(qw == row['Q_w_coefficients'], 'all_Q_w_coefficients')
    check(row['recovery_numerator'] == 0 and row['denominator'] == value(12) != 0, 'scalar_zero_with_nonzero_denominator')
    summary = dict(failures=failures, checks_actual=len(checks), checks_required=len(checks),
                   factor_coefficients_actual=63, factor_coefficients_required=63,
                   row_0_denominator_actual=value(12), row_0_denominator_required='nonzero',
                   scalar_numerator_actual=0, scalar_numerator_required=0,
                   new_block_rank_tests=0, separate_critical_audit=False)
    out = dict(summary=summary, checks=checks, reconstructed_basis=reconstructed,
               polynomial_coefficients=poly, Q=Q, Q_w_coefficients=qw,
               certificate_sha256=sha256((HERE/'certificate.json').read_bytes()).hexdigest(),
               verifier_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    (HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Full verification: scripts/span-274-full-weight/verification.json')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
