#!/usr/bin/env python3
"""Check every saved partial-cover entry, without importing its producer.

Reuse the independent audited polynomial construction/elimination of L169's
verifier. Do not extend any untested suffix or evaluate pending children.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import importlib.util
import json

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location('independent_l169', HERE.parent/'block-closure-capacity/verify.py')
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


def main():
    data = json.loads((HERE/'cover.json').read_text())
    failures, span_checks, node_checks, transition_checks = [], [], [], []
    counts = Counter()
    actual_tests = 0

    def check(ok, name, detail=None):
        counts[name] += 1
        if not ok:
            failures.append(dict(check=name, detail=detail))

    records = v.reconstructed_universe()
    check(len(records) == len(data['universe']) == 756, 'universe_size')
    check(data['modulus'] == 97 and data['S'] == v.S and data['J'] == v.J
          and data['fixed_labels'] == [], 'pair_free_parameters')
    for r,s in zip(records, data['universe']):
        check(all(r[k] == s[k] for k in s), 'original_block', r['label'])
        check(len(v.gauss(r['N'], 21)[1]) == 6, 'block_rank_six', r['label'])
        actual_tests += 1
    for path,digest in data['inputs_sha256'].items():
        check(sha256((ROOT/path).read_bytes()).hexdigest() == digest, 'input_hash', path)
    check(sha256((HERE/'run.py').read_bytes()).hexdigest() == data['script_sha256'], 'producer_hash')
    blocks = np.array([r['N'] for r in records], dtype=np.int64)
    sets = [set(r['support']) for r in records]
    keys = set()
    for sid,span in enumerate(data['spans']):
        history = span['generating_history']
        stack = [row for a in history for row in records[a]['N']]
        reduced,pivots,selected = v.gauss(stack, 21)
        free_vectors = []
        for j in range(21):
            if j not in pivots:
                vector = [0]*21
                vector[j] = 1
                for i,p in enumerate(pivots):
                    vector[p] = -reduced[i][j] % 97
                free_vectors.append(vector)
        basis = v.gauss(free_vectors, 21)[0]
        actual_tests += len(history)
        check(span['id'] == sid and span['kernel_basis'] == basis, 'entire_span_kernel', sid)
        check(span['rank'] == len(pivots) == 21-len(basis) < 21, 'span_rank', sid)
        minor = [[stack[i][j] for j in pivots] for i in selected]
        determinant = v.det(minor)
        check(determinant != 0, 'original_rank_minor', sid)
        key = tuple(map(tuple,basis))
        check(key not in keys, 'distinct_span', sid)
        keys.add(key)
        inc = []
        for a in range(len(span['extension_rank_increments'])):
            inc.append(len(v.gauss(blocks[a] @ np.array(basis,dtype=np.int64).T % 97, len(basis))[1]))
            actual_tests += 1
        check(len(inc) <= 756 and inc == span['extension_rank_increments'], 'entire_tested_prefix', sid)
        closure = [a for a,r in enumerate(inc) if r == 0] if len(inc) == 756 else None
        check(span['closure'] == closure, 'closure_or_unfinished', sid)
        span_checks.append(dict(id=sid, generating_history=history, kernel_basis=basis,
                                rank=len(pivots), minor_rows=selected, minor_columns=pivots,
                                minor=minor, minor_determinant=determinant,
                                extension_rank_increments=inc, closure=closure))
    check(data['spans'][0]['generating_history'] == [] and data['spans'][0]['rank'] == 0,
          'empty_root_span')
    for e in data['evaluated_children']:
        parent = data['nodes'][e['parent']]
        basis = np.array(data['spans'][parent['span']]['kernel_basis'], dtype=np.int64)
        residual = blocks[e['chosen']] @ basis.T % 97
        coeff = v.kernel(residual, len(basis))
        # v.kernel returns a canonical basis in the coefficient space.
        child = v.gauss(np.array(coeff,dtype=np.int64) @ basis % 97, 21)[0]
        actual_tests += 1
        check(child == data['spans'][e['span']]['kernel_basis'], 'entire_child_kernel', e)
        transition_checks.append(dict(**e, kernel_basis=child))

    all_states = data['nodes'] + data['frontier'] + ([data['witness']] if data['witness'] else [])
    states = {}
    for state in all_states:
        history = state['history']
        key = tuple(history)
        check(key not in states, 'unique_history', history)
        states[key] = state
        check(history == sorted(set(history)) and all(0 <= a < 756 for a in history), 'ordered_labels', history)
        check(state['last_added'] == (history[-1] if history else -1), 'last_added', history)
        check(all(len(sets[a] & sets[b]) <= 1 for a,b in combinations(history, 2)), 'linearity', history)
        degrees = [sum(h in sets[a] for a in history) for h in v.H]
        check(max(degrees,default=0) <= 4, 'integer_degrees', history)
        if not history:
            check(state['parent'] is None and state['chosen'] is None and state['span'] == 0, 'root_state')
        else:
            parent = data['nodes'][state['parent']]
            check(parent['decision'] == 'branch' and history == parent['history']+[state['chosen']]
                  and state['chosen'] in parent['candidates'], 'parent_history', history)
    check(() in states, 'root_present')
    for span in data['spans']:
        state = states.get(tuple(span['generating_history']))
        check(state is not None and state['span'] == span['id'], 'every_generated_span_retained', span['id'])
    expected_evaluated = []
    for nid,node in enumerate(data['nodes']):
        check(node['id'] == nid, 'node_id', nid)
        if node['parent'] is not None:
            check(node['parent'] < nid, 'earlier_parent', nid)
        span = data['spans'][node['span']]
        inc = span['extension_rank_increments']
        check(len(inc) == 756, 'processed_node_full_scan', nid)
        degrees = [sum(h in sets[a] for a in node['history']) for h in v.H]
        candidates = [a for a in range(node['last_added']+1,756)
                      if span['rank']+inc[a] < 21
                      and all(len(sets[a] & sets[b]) <= 1 for b in node['history'])
                      and all(degrees[v.H.index(h)] < 4 for h in sets[a])]
        check(node['degrees'] == degrees and node['candidates'] == candidates, 'entire_candidate_list', nid)
        dual = node['capacity_certificate']
        q = dual['denominator']
        coverage = []
        if dual['kind'] == 'candidate_count':
            numerator = len(candidates)
            check(q == 1, 'count_denominator', nid)
        else:
            check(dual['kind'] == 'coordinate_pair_dual' and q in (1,2), 'dual_type', nid)
            coords = dual['coordinates']
            check(len(coords) == len(set(coords)) and set(coords) <= set(v.H), 'dual_coordinates', nid)
            side = dual['group_side']
            check(side in ('I','K'), 'dual_group_side', nid)
            groups = {tuple(g['pair']):g['numerator'] for g in dual['group_numerators']}
            available = {tuple(records[a][side]) for a in candidates}
            check(len(groups) == len(dual['group_numerators']) and set(groups) <= available
                  and all(isinstance(t,int) and t >= 0 for t in groups.values()), 'dual_groups', nid)
            numerator = sum(4-degrees[v.H.index(h)] for h in coords)+sum(groups.values())
            for a in candidates:
                amount = len(sets[a] & set(coords))+groups.get(tuple(records[a][side]),0)
                coverage.append([a,amount])
                check(amount >= q, 'every_dual_column', [nid,a])
        upper = len(node['history'])+numerator//q
        check(numerator == dual['numerator'] and upper == node['total_upper_bound'], 'exact_objective', nid)
        check((node['decision'] == 'capacity' and upper <= 11) or
              (node['decision'] == 'branch' and upper > 11), 'sound_node_decision', nid)
        if node['decision'] == 'branch':
            check([c['chosen'] for c in node['children']] == candidates, 'complete_child_list', nid)
            for c in node['children']:
                history = tuple(node['history']+[c['chosen']])
                state = states.get(history)
                check(state is not None and state['parent'] == nid and state['span'] == c['span'],
                      'every_child_processed_or_retained', [nid,c['chosen']])
        node_checks.append(dict(id=nid, degrees=degrees, candidates=candidates,
                                dual=dual, column_coverage=coverage, upper=upper, decision=node['decision']))
    for state in all_states:
        if state['history']:
            if state['span'] is not None:
                expected_evaluated.append(dict(parent=state['parent'], chosen=state['chosen'], span=state['span']))
            else:
                check(state in data['frontier'], 'uncomputed_child_is_pending', state['history'])
    order = lambda e:(e['parent'],e['chosen'])
    check(sorted(expected_evaluated,key=order) == sorted(data['evaluated_children'],key=order), 'all_evaluated_children')
    summary = data['summary']
    prod = sum(len(s['extension_rank_increments']) for s in data['spans'])+len(data['evaluated_children'])
    check(prod == summary['producer_block_tests'], 'producer_counter')
    check(actual_tests == summary['reserved_verifier_block_tests'], 'verification_counter')
    check(prod+actual_tests == summary['combined_committed_block_tests'] <= 1000000, 'shared_test_cap')
    check(len(data['spans']) == summary['span_count'] <= 10000, 'span_counter_cap')
    check(len(data['nodes']) == summary['node_count'] and len(data['frontier']) == summary['frontier_count'], 'history_counters')
    check(summary['decisions'] == dict(Counter(n['decision'] for n in data['nodes'])), 'decision_counters')
    check(summary['rank_counts'] == {str(k):n for k,n in sorted(Counter(s['rank'] for s in data['spans']).items())},
          'rank_histogram')
    check(summary['largest_leaf_upper_bound'] == max((n['total_upper_bound'] for n in data['nodes']
                                                    if n['decision'] == 'capacity'),default=None), 'largest_leaf_bound')
    check(summary['complete'] == (not data['frontier'] and data['witness'] is None), 'completion_flag')
    check(summary['witness_found'] == (data['witness'] is not None), 'witness_flag')
    if data['witness']:
        check(len(data['witness']['history']) == 12 and data['spans'][data['witness']['span']]['rank'] < 21,
              'exact_twelve_witness')
    if summary['stop_reason'] == 'block_test_cap_with_verification_reservation':
        current = data['frontier'][-1]
        next_cost = 2+(len(current['history']) if current['span'] is None else 0)
        check(prod+actual_tests+next_cost > 1000000, 'reservation_stop_is_necessary')
    result = dict(checks=dict(counts), failures=failures, actual_verifier_block_tests=actual_tests,
                  producer_block_tests=prod, combined_actual_block_tests=prod+actual_tests,
                  required_total_capacity=11, partial_only=bool(data['frontier']),
                  span_count=len(data['spans']), node_count=len(data['nodes']),
                  frontier_count=len(data['frontier']), witness_found=data['witness'] is not None,
                  history_lengths=dict(sorted(Counter(len(n['history']) for n in data['nodes']).items())),
                  frontier_lengths=dict(sorted(Counter(len(n['history']) for n in data['frontier']).items())),
                  evaluated_zero_increment_children=sum(data['spans'][e['span']]['rank'] ==
                      data['spans'][data['nodes'][e['parent']]['span']]['rank'] for e in data['evaluated_children']),
                  pending_root_label_count=sum(s['parent'] == 0 for s in data['frontier']),
                  certificate_sha256=sha256((HERE/'cover.json').read_bytes()).hexdigest(),
                  verifier_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                  reused_verifier_sha256=sha256((HERE.parent/'block-closure-capacity/verify.py').read_bytes()).hexdigest())
    out = dict(summary=result, reconstructed_universe=records, spans=span_checks,
               nodes=node_checks, transitions=transition_checks, frontier=data['frontier'],
               witness=data['witness'])
    (HERE/'verification.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(result,sort_keys=True))
    print('Full verification: scripts/pair-free-envelope/verification.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
