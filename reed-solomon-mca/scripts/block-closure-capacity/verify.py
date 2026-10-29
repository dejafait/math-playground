#!/usr/bin/env python3
"""Independent reconstruction and complete replay of the fixed-pair cover.

Does not import the producer. Builds supports as four-subsets, evaluates
expanded polynomials, and uses normalized quotient maps before comparing
every actual block. Checks the entire certificate, not a preview/sample.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
P = 97
S = [1, 8, 12, 18, 22, 27, 33]
J = [47, 50, 64, 70, 75, 79, 85, 89, 96]
H = S + J


def gauss(rows, width):
    a = [[int(x) % P for x in row] for row in rows]
    origins = list(range(len(a)))
    pivots, selected = [], []
    for j in range(width):
        k = len(pivots)
        pivot = next((i for i in range(k, len(a)) if a[i][j] != 0), None)
        if pivot is None:
            continue
        a[k], a[pivot] = a[pivot], a[k]
        origins[k], origins[pivot] = origins[pivot], origins[k]
        selected.append(origins[k])
        scale = pow(a[k][j], P-2, P)
        a[k] = [scale*x % P for x in a[k]]
        for i in range(len(a)):
            if i == k:
                continue
            multiple = a[i][j]
            if multiple:
                a[i] = [(x-multiple*y) % P for x, y in zip(a[i], a[k])]
        pivots.append(j)
    return a[:len(pivots)], pivots, selected


def kernel(rows, width):
    a, pivots, _ = gauss(rows, width)
    result = []
    for j in range(width):
        if j in pivots:
            continue
        row = [0]*width
        row[j] = 1
        for i, p in enumerate(pivots):
            row[p] = -a[i][j] % P
        result.append(row)
    return gauss(result, width)[0]


def det(rows):
    a = [r[:] for r in rows]
    answer = 1
    for j in range(len(a)):
        k = next((i for i in range(j, len(a)) if a[i][j]), None)
        if k is None:
            return 0
        if k != j:
            a[k], a[j] = a[j], a[k]
            answer = -answer
        answer = answer*a[j][j] % P
        for i in range(j+1, len(a)):
            coefficient = a[i][j]*pow(a[j][j], P-2, P) % P
            a[i] = [(x-coefficient*y) % P for x, y in zip(a[i], a[j])]
    return answer % P


def reconstructed_universe():
    pairs = []
    for support in combinations(H, 4):
        i = sorted(set(support) & set(S))
        k = sorted(set(support) & set(J))
        if len(i) == len(k) == 2:
            pairs.append((i, k))
    pairs.sort()
    result = []
    for label, (i, k) in enumerate(pairs):
        coeff = [1]
        for y in sorted(set(J)-set(k)):
            new = [0]*(len(coeff)+1)
            for j, c in enumerate(coeff):
                new[j] = (new[j]-y*c) % P
                new[j+1] = (new[j+1]+c) % P
            coeff = new
        values = []
        for x in S:
            value = 0
            for c in reversed(coeff):
                value = (value*x+c) % P
            values.append(value)
        observed = sorted(set(S)-set(i))
        z = S.index(observed[0])
        inverse = pow(values[z], P-2, P)
        q = []
        for x in observed[1:]:
            row = [0]*7
            row[S.index(x)] = 1
            row[z] = -values[S.index(x)]*inverse % P
            q.append(row)
        normalized = []
        for a, b in combinations(range(4), 2):
            normalized.append([(q[a][u]*q[b][v]-q[a][v]*q[b][u]) % P
                               for u, v in combinations(range(7), 2)])
        actual = [[entry*values[z]**2 % P for entry in row] for row in normalized]
        result.append(dict(label=label, I=i, K=k, support=sorted(i+k),
                           pivot=observed[0], covector_labels=observed[1:],
                           polynomial_coefficients=coeff, g_on_S=values,
                           normalized_Q=q, normalized_N=normalized,
                           Q=[[x*values[z] % P for x in row] for row in q], N=actual))
    return result


def main():
    source = HERE/'pilot.json'
    data = json.loads(source.read_text())
    failures = []
    checks = Counter()

    def check(ok, name, detail=None):
        checks[name] += 1
        if not ok:
            failures.append(dict(check=name, detail=detail))

    records = reconstructed_universe()
    check(len(records) == 756 and len(data['universe']) == 756, 'universe_count')
    check(data['modulus'] == P and data['S'] == S and data['J'] == J, 'field_partition')
    check(data['column_pairs'] == list(map(list, combinations(S, 2))), 'column_order')
    for actual, stored in zip(records, data['universe']):
        for key in ('label', 'I', 'K', 'support', 'pivot', 'covector_labels', 'g_on_S', 'Q', 'N'):
            check(actual[key] == stored[key], 'all_original_block_fields', [actual['label'], key])
        check(len(gauss(actual['N'], 21)[1]) == 6, 'single_block_rank', actual['label'])
        check(all(actual['g_on_S']), 'nonzero_polynomial_values', actual['label'])
    fixed = [237, 570]
    check(data['fixed_labels'] == fixed, 'fixed_ids')
    check([records[a]['support'] for a in fixed] == [[8, 12, 70, 75], [18, 22, 79, 85]], 'fixed_supports')
    for name, digest in data['inputs_sha256'].items():
        check(sha256((ROOT/name).read_bytes()).hexdigest() == digest, 'input_sha256', name)
    check(data['script_sha256'] == sha256((HERE/'pilot.py').read_bytes()).hexdigest(), 'producer_sha256')

    normalized = np.array([r['normalized_N'] for r in records], dtype=np.int64)
    masks = [sum(1 << H.index(x) for x in r['support']) for r in records]
    spans = data['spans']
    span_records = []
    keys = set()
    for sid, span in enumerate(spans):
        check(sid == span['id'], 'span_identity', sid)
        history = span['generating_history']
        stack = [row for a in history for row in records[a]['N']]
        reduced, pivots, selected = gauss(stack, 21)
        basis = kernel(stack, 21)
        check(basis == span['kernel_basis'], 'full_kernel_basis', sid)
        check(len(pivots) == span['rank'] == 21-len(basis) < 21, 'full_span_rank', sid)
        check(all(sum(x*y for x, y in zip(row, vector)) % P == 0
                  for row in stack for vector in basis), 'entire_kernel_residual', sid)
        minor = [[stack[i][j] for j in pivots] for i in selected]
        determinant = det(minor)
        check(determinant != 0, 'full_rank_minor', sid)
        key = tuple(map(tuple, basis))
        check(key not in keys, 'distinct_spans', sid)
        keys.add(key)
        products = normalized @ np.array(basis, dtype=np.int64).T % P
        increments = [len(gauss(matrix, len(basis))[1]) for matrix in products]
        check(increments == span['extension_rank_increments'], 'all_756_extension_ranks', sid)
        closure = [a for a, increment in enumerate(increments) if increment == 0]
        check(closure == span['closure'], 'complete_closure', sid)
        span_records.append(dict(id=sid, generating_history=history, rank=len(pivots),
                                 kernel_basis=basis, minor_rows=selected, minor_columns=pivots,
                                 minor=minor, minor_determinant=determinant,
                                 extension_rank_increments=increments, closure=closure))

    # The full tree, with no merging of histories even for equal spans.
    nodes = data['nodes']
    histories = set()
    actual_children = {i: [] for i in range(len(nodes))}
    node_records = []
    checked_edges = set()
    for nid, node in enumerate(nodes):
        history = node['history']
        sid = node['span']
        span = spans[sid]
        check(node['id'] == nid and tuple(history) not in histories, 'unique_history_identity', nid)
        histories.add(tuple(history))
        check(history[:2] == fixed and history[2:] == sorted(set(history[2:]))
              and len(set(history)) == len(history), 'ordered_added_history', nid)
        check(node['last_added'] == (history[-1] if len(history) > 2 else -1), 'last_added', nid)
        check(2 <= len(history) <= 11, 'no_unexamined_twelve_row_history', nid)
        degrees = [sum(bool(masks[a] >> h & 1) for a in history) for h in range(16)]
        check(degrees == node['degrees'] and max(degrees) <= 4, 'integer_history_degrees', nid)
        check(all((masks[a] & masks[b]).bit_count() <= 1 for a, b in combinations(history, 2)),
              'history_pair_linearity', nid)
        if nid == 0:
            check(node['parent'] is None and node['chosen'] is None and history == fixed,
                  'root', nid)
            check(span['kernel_basis'] == kernel([row for a in fixed for row in records[a]['N']], 21),
                  'root_span')
        else:
            parent = node['parent']
            a = node['chosen']
            check(isinstance(parent, int) and 0 <= parent < nid, 'earlier_parent', nid)
            pn = nodes[parent]
            check(pn['decision'] == 'branch' and history == pn['history']+[a], 'parent_history', nid)
            actual_children[parent].append(dict(chosen=a, span=sid))
            edge = (pn['span'], a, sid)
            if edge not in checked_edges:
                checked_edges.add(edge)
                pk = np.array(spans[pn['span']]['kernel_basis'], dtype=np.int64)
                residual = normalized[a] @ pk.T % P
                coefs = kernel(residual.tolist(), len(pk))
                child_basis = gauss(np.array(coefs, dtype=np.int64) @ pk % P, 21)[0]
                check(child_basis == span['kernel_basis'], 'full_child_kernel_transition', edge)
        increments = span['extension_rank_increments']
        candidates = []
        for a, record in enumerate(records):
            if a <= node['last_added'] or a in history:
                continue
            if span['rank'] + increments[a] >= 21:
                continue
            if any((masks[a] & masks[b]).bit_count() > 1 for b in history):
                continue
            if any(degrees[H.index(x)] == 4 for x in record['support']):
                continue
            candidates.append(a)
        check(candidates == node['candidates'], 'complete_envelope_candidates', nid)
        dual = node['capacity_certificate']
        q = dual['denominator']
        if dual['kind'] == 'candidate_count':
            numerator = len(candidates)
            check(q == 1 and dual['numerator'] == numerator, 'exact_cardinality_certificate', nid)
            minimum = 1 if candidates else None
        else:
            check(dual['kind'] == 'coordinate_pair_dual' and q in (1, 2), 'dual_kind', nid)
            coords = dual['coordinates']
            check(len(coords) == len(set(coords)) and set(coords) <= set(H), 'coordinate_weights', nid)
            side = dual['group_side']
            check(side in ('I', 'K'), 'pair_group_side', nid)
            groups = {tuple(r['pair']): r['numerator'] for r in dual['group_numerators']}
            check(len(groups) == len(dual['group_numerators']) and all(v >= 0 for v in groups.values()),
                  'nonnegative_pair_weights', nid)
            coverages = [len(set(coords) & set(records[a]['support'])) + groups.get(tuple(records[a][side]), 0)
                         for a in candidates]
            minimum = min(coverages, default=None)
            check(all(c >= q for c in coverages), 'every_dual_column', nid)
            numerator = sum(4-degrees[H.index(x)] for x in coords)+sum(groups.values())
            check(numerator == dual['numerator'], 'exact_dual_objective', nid)
        bound = len(history) + numerator//q
        check(bound == node['total_upper_bound'], 'exact_total_bound', nid)
        if node['decision'] == 'capacity':
            check(bound <= 11 and not node.get('children'), 'terminal_bound', nid)
        else:
            check(node['decision'] == 'branch' and bound > 11, 'branch_decision', nid)
            check([c['chosen'] for c in node['children']] == candidates, 'all_branch_choices', nid)
        node_records.append(dict(id=nid, span=sid, candidate_count=len(candidates),
                                 minimum_dual_coverage_numerator=minimum, denominator=q,
                                 total_upper_bound=bound, decision=node['decision']))
    for nid, node in enumerate(nodes):
        check(actual_children[nid] == node.get('children', []), 'entire_child_cover', nid)
    check(data['frontier'] == [] and data['witness'] is None, 'no_pending_frontier')
    summary = dict(verified_complete_cover=not failures,
                   actual_total_upper_bound=max(n['total_upper_bound'] for n in nodes if n['decision'] == 'capacity'),
                   required_total_upper_bound=11, span_count=len(spans), node_count=len(nodes),
                   block_extension_checks=756*len(spans), single_block_rank_checks=756,
                   distinct_child_transition_checks=len(checked_edges),
                   decisions=dict(Counter(n['decision'] for n in nodes)),
                   history_size_counts=dict(sorted(Counter(len(n['history']) for n in nodes).items())),
                   rank_counts=dict(sorted(Counter(s['rank'] for s in spans).items())),
                   leaf_bound_counts=dict(sorted(Counter(n['total_upper_bound'] for n in nodes if n['decision'] == 'capacity').items())),
                   all_check_count=sum(checks.values()), failure_count=len(failures))
    ps = data['summary']
    for field, actual in (('span_count', len(spans)), ('node_count', len(nodes)),
                          ('block_tests', 756*len(spans)), ('frontier_count', 0),
                          ('complete', True), ('stop_reason', 'complete_cover'),
                          ('largest_leaf_upper_bound', summary['actual_total_upper_bound'])):
        check(ps[field] == actual, 'producer_summary', field)
    check(ps['span_count'] <= ps['span_limit'] == 10000 and
          ps['block_tests'] <= ps['block_test_limit'] == 1000000, 'exploration_caps')
    summary['verified_complete_cover'] = not failures
    summary['failure_count'] = len(failures)
    summary['all_check_count'] = sum(checks.values())
    out = dict(certificate_sha256=sha256(source.read_bytes()).hexdigest(),
               verifier_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               reconstructed_blocks=records, spans=span_records, nodes=node_records,
               check_counts=dict(checks), failures=failures, summary=summary)
    dest = HERE/'verification.json'
    dest.write_text(json.dumps(out, separators=(',', ':'))+'\n')
    print(json.dumps(summary, sort_keys=True))
    print('Full independent verification: '+str(dest.relative_to(ROOT)))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
