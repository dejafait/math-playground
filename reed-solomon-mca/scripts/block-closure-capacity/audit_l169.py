#!/usr/bin/env python3
"""Separate L169 audit; read both saved certificates without rewriting either.

No imports from pilot.py or verify.py. Incremental row insertion and backward
substitution replace their Gauss-Jordan routines. Every history is checked
against its original stack, independently of parent/span-transition caching.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
H = S + J
FIXED = [237, 570]
INV = [0] + [pow(x, -1, P) for x in range(1, P)]


def echelon(rows):
    basis = {}
    for row in rows:
        v = [int(x) % P for x in row]
        for j in sorted(basis):
            if v[j]:
                c = v[j]
                v = [(x-c*y) % P for x, y in zip(v, basis[j])]
        pivot = next((j for j, x in enumerate(v) if x), None)
        if pivot is not None:
            c = INV[v[pivot]]
            basis[pivot] = [c*x % P for x in v]
    return basis


def canonical(rows):
    b = echelon(rows)
    pivots = sorted(b)
    for j in reversed(pivots):
        for i in pivots:
            if i < j and b[i][j]:
                c = b[i][j]
                b[i] = [(x-c*y) % P for x, y in zip(b[i], b[j])]
    return [b[j] for j in pivots]


def nullspace(rows, width):
    b = echelon(rows)
    out = []
    for free in range(width):
        if free in b:
            continue
        v = [0]*width
        v[free] = 1
        for pivot in sorted(b, reverse=True):
            v[pivot] = -sum(x*y for x, y in zip(b[pivot], v)) % P
        out.append(v)
    return canonical(out)


def determinant(rows):
    a = [row[:] for row in rows]
    result = 1
    for j in range(len(a)):
        pivot = next((i for i in range(j, len(a)) if a[i][j] % P), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            result = -result
        value = a[j][j] % P
        result = result*value % P
        for i in range(j+1, len(a)):
            c = a[i][j]*INV[value] % P
            a[i] = [(x-c*y) % P for x, y in zip(a[i], a[j])]
    return result % P


def reconstruct():
    records, expanded = [], []
    for ip in combinations(S, 2):
        for kp in combinations(J, 2):
            roots = [y for y in J if y not in kp]
            values = []
            for x in S:
                v = 1
                for y in roots:
                    v = v*(x-y) % P
                values.append(v)
            # Elementary symmetric coefficients: independent of Horner construction.
            coeff = [sum((-1)**(7-d)*np_prod(t) for t in combinations(roots, 7-d)) % P
                     for d in range(8)]
            observed = [x for x in S if x not in ip]
            z = observed[0]
            gz = values[S.index(z)]
            q = [[(gz*(h == x)-values[S.index(x)]*(h == z)) % P for h in S]
                 for x in observed[1:]]
            n = [[(u[a]*v[b]-u[b]*v[a]) % P for a, b in combinations(range(7), 2)]
                 for u, v in combinations(q, 2)]
            r = dict(label=len(records), I=list(ip), K=list(kp), support=sorted(ip+kp),
                     pivot=z, covector_labels=observed[1:], g_on_S=values, Q=q, N=n)
            records.append(r)
            expanded.append(dict(**r, polynomial_coefficients=coeff,
                                 normalized_Q=[[x*INV[gz] % P for x in row] for row in q],
                                 normalized_N=[[x*INV[gz]**2 % P for x in row] for row in n]))
    return records, expanded


def np_prod(values):
    result = 1
    for x in values:
        result *= x
    return result


def main():
    started = time.monotonic()
    pilot_path, verification_path = HERE/'pilot.json', HERE/'verification.json'
    data = json.loads(pilot_path.read_text())
    old = json.loads(verification_path.read_text())
    checks, failures = Counter(), []

    def check(ok, name, detail=None):
        checks[name] += 1
        if not ok:
            failures.append(dict(check=name, detail=detail))

    records, expanded = reconstruct()
    check(data['universe'] == records, 'all_producer_block_fields')
    check(old['reconstructed_blocks'] == expanded, 'all_verifier_block_fields')
    check(data['modulus'] == P and data['S'] == S and data['J'] == J
          and data['fixed_labels'] == FIXED, 'exact_parameters')
    check(data['column_pairs'] == list(map(list, combinations(S, 2))), 'column_order')
    check([records[a]['support'] for a in FIXED] == [[8, 12, 70, 75], [18, 22, 79, 85]],
          'mandatory_supports')
    for r in records:
        check(len(echelon(r['N'])) == 6 and all(r['g_on_S']), 'whole_block_rank', r['label'])
    for path, digest in data['inputs_sha256'].items():
        check(sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'input_hash', path)
    check(data['script_sha256'] == sha256((HERE/'pilot.py').read_bytes()).hexdigest(), 'producer_hash')
    check(old['verifier_sha256'] == sha256((HERE/'verify.py').read_bytes()).hexdigest(), 'verifier_hash')
    check(old['certificate_sha256'] == sha256(pilot_path.read_bytes()).hexdigest(), 'saved_certificate_hash')
    check(old['failures'] == [] and data['summary']['failures'] == [], 'saved_failure_lists')
    check(len(data['spans']) == len(old['spans']) == 300, 'span_counts')
    blocks = np.array([r['N'] for r in records], dtype=np.int64)
    support_sets = [set(r['support']) for r in records]
    audited_spans, kernel_keys = [], set()
    for sid, span in enumerate(data['spans']):
        stack = [row for a in span['generating_history'] for row in records[a]['N']]
        basis = nullspace(stack, 21)
        rank = len(echelon(stack))
        check(span['id'] == sid and basis == span['kernel_basis']
              and rank == span['rank'] == 21-len(basis) < 21, 'complete_span', sid)
        key = tuple(map(tuple, basis))
        check(key not in kernel_keys, 'distinct_span', sid)
        kernel_keys.add(key)
        check(all(sum(x*y for x, y in zip(v, row)) % P == 0 for v in basis for row in stack),
              'span_kernel_residuals', sid)
        products = blocks @ np.array(basis, dtype=np.int64).T % P
        increments = [len(echelon(matrix)) for matrix in products]
        closure = [a for a, inc in enumerate(increments) if inc == 0]
        check(increments == span['extension_rank_increments'] and closure == span['closure'],
              'all_extension_ranks_and_closure', sid)
        v = old['spans'][sid]
        for field in ('id', 'generating_history', 'rank', 'kernel_basis', 'extension_rank_increments', 'closure'):
            check(v[field] == span[field], 'saved_verified_span_field', [sid, field])
        rows, cols = v['minor_rows'], v['minor_columns']
        check(len(rows) == len(set(rows)) == len(cols) == len(set(cols)) == rank
              and all(0 <= i < len(stack) for i in rows) and all(0 <= j < 21 for j in cols),
              'minor_shape_indices', sid)
        minor = [[stack[i][j] for j in cols] for i in rows]
        residue = determinant(minor)
        check(v['minor'] == minor and v['minor_determinant'] == residue != 0, 'original_nonzero_minor', sid)
        audited_spans.append(dict(id=sid, generating_history=span['generating_history'], rank=rank,
                                  kernel_basis=basis, extension_rank_increments=increments, closure=closure,
                                  minor_rows=rows, minor_columns=cols, minor=minor, minor_determinant=residue))

    nodes = data['nodes']
    check(len(nodes) == len(old['nodes']) == 12508, 'history_counts')
    seen, children = set(), [[] for _ in nodes]
    audited_nodes, transitions = [], set()
    for nid, node in enumerate(nodes):
        hist, sid = node['history'], node['span']
        span = audited_spans[sid]
        check(node['id'] == nid and tuple(hist) not in seen and hist[:2] == FIXED
              and len(set(hist)) == len(hist) and hist[2:] == sorted(hist[2:])
              and 2 <= len(hist) <= 11 and all(0 <= a < 756 for a in hist), 'history_identity_order', nid)
        seen.add(tuple(hist))
        # Direct original-stack check at EVERY history; do not infer this from cached edges.
        stack = [row for a in hist for row in records[a]['N']]
        direct_kernel = nullspace(stack, 21)
        direct_rank = len(echelon(stack))
        check(direct_kernel == span['kernel_basis'] and direct_rank == span['rank'], 'direct_history_stack', nid)
        degrees = [sum(h in support_sets[a] for a in hist) for h in H]
        check(node['degrees'] == degrees and all(0 <= d <= 4 for d in degrees), 'integer_degrees', nid)
        check(all(len(support_sets[a] & support_sets[b]) <= 1 for a, b in combinations(hist, 2)),
              'pairwise_linearity', nid)
        last = hist[-1] if len(hist) > 2 else -1
        check(last == node['last_added'], 'only_nonmandatory_ordered', nid)
        if nid == 0:
            check(hist == FIXED and node['parent'] is None and node['chosen'] is None, 'unique_root')
        else:
            parent, chosen = node['parent'], node['chosen']
            check(type(parent) is int and 0 <= parent < nid, 'strict_ancestry', nid)
            pn = nodes[parent]
            check(pn['decision'] == 'branch' and hist == pn['history']+[chosen], 'exact_parent_history', nid)
            children[parent].append(dict(chosen=chosen, span=sid))
            transitions.add((pn['span'], chosen, sid))
        candidates = [a for a in range(last+1, 756) if a not in hist
                      and span['rank']+span['extension_rank_increments'][a] < 21
                      and all(len(support_sets[a] & support_sets[b]) <= 1 for b in hist)
                      and all(degrees[H.index(h)] < 4 for h in support_sets[a])]
        check(candidates == node['candidates'], 'complete_candidate_envelope', nid)
        dual = node['capacity_certificate']
        q = dual['denominator']
        check(type(q) is int and q > 0 and type(dual['numerator']) is int, 'exact_rational_types', nid)
        if dual['kind'] == 'candidate_count':
            numerator, coverages = len(candidates), [1]*len(candidates)
            check(q == 1, 'cardinality_denominator', nid)
        else:
            coords, side = dual['coordinates'], dual['group_side']
            check(dual['kind'] == 'coordinate_pair_dual' and q in (1, 2)
                  and len(set(coords)) == len(coords) and set(coords) <= set(H)
                  and side in ('I', 'K'), 'dual_shape', nid)
            groups = {tuple(g['pair']): g['numerator'] for g in dual['group_numerators']}
            valid_pairs = set(combinations(S if side == 'I' else J, 2))
            check(len(groups) == len(dual['group_numerators']) and set(groups) <= valid_pairs
                  and all(type(t) is int and t >= 0 for t in groups.values()), 'genuine_pair_group_weights', nid)
            coverages = [len(support_sets[a] & set(coords))+groups.get(tuple(records[a][side]), 0)
                         for a in candidates]
            check(all(c >= q for c in coverages), 'every_exact_dual_inequality', nid)
            numerator = sum(4-degrees[H.index(h)] for h in coords)+sum(groups.values())
        bound = len(hist)+numerator//q
        check(numerator == dual['numerator'] and bound == node['total_upper_bound'], 'exact_objective_and_floor', nid)
        if node['decision'] == 'capacity':
            check(bound <= 11 and node.get('children', []) == [], 'terminal_exclusion', nid)
        else:
            check(node['decision'] == 'branch' and bound > 11
                  and [c['chosen'] for c in node['children']] == candidates, 'full_branch_labels', nid)
        expected = dict(id=nid, span=sid, candidate_count=len(candidates),
                        minimum_dual_coverage_numerator=min(coverages, default=None), denominator=q,
                        total_upper_bound=bound, decision=node['decision'])
        check(old['nodes'][nid] == expected, 'entire_saved_verifier_node', nid)
        audited_nodes.append(dict(**expected, history=hist, direct_rank=direct_rank,
                                  degrees=degrees, candidates=candidates, dual=dual,
                                  column_coverage_numerators=coverages, parent=node['parent'],
                                  chosen=node['chosen'], children=node.get('children', [])))
        if (nid+1) % 4000 == 0:
            print(f'Audited {nid+1}/{len(nodes)} complete history stacks and capacity records.', flush=True)
    for nid, node in enumerate(nodes):
        check(children[nid] == node.get('children', []), 'all_children_reached_exactly', nid)
    check(data['frontier'] == [] and data['witness'] is None, 'no_unfinished_search')
    decisions = dict(Counter(n['decision'] for n in nodes))
    ranks = dict(sorted(Counter(str(s['rank']) for s in audited_spans).items()))
    sizes = dict(sorted(Counter(str(len(n['history'])) for n in nodes).items()))
    leaves = dict(sorted(Counter(str(n['total_upper_bound']) for n in nodes if n['decision'] == 'capacity').items()))
    maximum = max(n['total_upper_bound'] for n in nodes if n['decision'] == 'capacity')
    expected_summary = dict(verified_complete_cover=True, actual_total_upper_bound=maximum,
                            required_total_upper_bound=11, span_count=300, node_count=12508,
                            block_extension_checks=226800, single_block_rank_checks=756,
                            distinct_child_transition_checks=len(transitions), decisions=decisions,
                            history_size_counts=sizes, rank_counts=ranks, leaf_bound_counts=leaves,
                            all_check_count=sum(old['check_counts'].values()), failure_count=0)
    check(old['summary'] == expected_summary, 'entire_saved_verifier_summary')
    for key, value in dict(complete=True, stop_reason='complete_cover', span_count=300, node_count=12508,
                           block_tests=226800, span_limit=10000, block_test_limit=1000000,
                           frontier_count=0, witness_found=False, required_total_capacity=11,
                           largest_leaf_upper_bound=maximum, decisions=decisions, rank_counts=ranks,
                           failures=[]).items():
        check(data['summary'][key] == value, 'producer_summary', key)
    summary = dict(accepted=not failures, failure_count=len(failures), check_count=sum(checks.values()),
                   original_blocks=756, complete_spans=300, extension_rank_checks=226800,
                   direct_history_stack_checks=len(nodes), distinct_transitions=len(transitions),
                   decisions=decisions, history_size_counts=sizes, rank_counts=ranks,
                   leaf_bound_counts=leaves, actual_largest_terminal_bound=maximum,
                   required_largest_terminal_bound=11, excluded_support_count=12,
                   maximum_numpy_dot_product_bound=21*96*96,
                   elapsed_seconds=round(time.monotonic()-started, 3))
    paths = ['scripts/block-closure-capacity/pilot.py', 'scripts/block-closure-capacity/verify.py',
             'scripts/block-closure-capacity/pilot.json', 'scripts/block-closure-capacity/verification.json',
             'lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
             'lemmas/L167-completed-family-marked-extraction-counterexample.md',
             'drafts/literature/2026-10-28-l169-critical-audit-review.md']
    output = dict(inputs_sha256={p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
                  audit_script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  reconstructed_blocks=expanded, spans=audited_spans, nodes=audited_nodes,
                  check_counts=dict(checks), failures=failures, summary=summary)
    target = HERE/'l169-critical-audit.json'
    target.write_text(json.dumps(output, separators=(',', ':'))+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Full critical-audit evidence: '+str(target.relative_to(ROOT)))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
