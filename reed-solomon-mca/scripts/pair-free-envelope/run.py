#!/usr/bin/env python3
"""One capped pair-free cover; preserve every pending history and partial scan."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import importlib.util
import json
import time

import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location('audited_pilot', HERE.parent/'block-closure-capacity/pilot.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
LIMIT = 1000000
SPAN_LIMIT = 10000


def main():
    start = time.monotonic()
    records = m.universe()
    blocks = np.array([r['N'] for r in records], dtype=np.int64)
    masks = [sum(1 << m.H.index(x) for x in r['support']) for r in records]
    compatible = [set(b for b in range(756) if (x & masks[b]).bit_count() <= 1) for x in masks]
    spans, nodes, evaluated_children = [], [], []
    keys = {}
    producer_tests, reserve = 0, 756
    witness = None
    stop = None

    def intern(k, history):
        nonlocal reserve
        key = bytes(x for row in k for x in row)
        if key in keys:
            return keys[key]
        sid = len(spans)
        keys[key] = sid
        reserve += len(history)
        spans.append(dict(id=sid, generating_history=history[:], kernel_basis=k,
                          rank=21-len(k), extension_rank_increments=[], closure=None))
        return sid

    identity = [[int(i == j) for j in range(21)] for i in range(21)]
    intern(identity, [])
    frontier = [dict(history=[], last_added=-1, span=0, parent=None, chosen=None)]

    def save(final=False):
        summary = dict(complete=not frontier and witness is None,
                       stop_reason=stop, span_count=len(spans), node_count=len(nodes),
                       producer_block_tests=producer_tests, reserved_verifier_block_tests=reserve,
                       combined_committed_block_tests=producer_tests+reserve,
                       block_test_limit=LIMIT, span_limit=SPAN_LIMIT,
                       frontier_count=len(frontier), witness_found=witness is not None,
                       required_total_capacity=11,
                       largest_leaf_upper_bound=max((n['total_upper_bound'] for n in nodes
                                                      if n['decision'] == 'capacity'), default=None),
                       decisions=dict(Counter(n['decision'] for n in nodes)),
                       rank_counts=dict(sorted(Counter(s['rank'] for s in spans).items())),
                       elapsed_seconds=round(time.monotonic()-start, 3))
        paths = ['lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
                 'lemmas/L169-fixed-pair-deficient-envelope-capacity.md',
                 'drafts/literature/2026-10-28-pair-free-envelope-cover-review.md',
                 'drafts/2026-10-28-pair-free-envelope-working.md',
                 'scripts/block-closure-capacity/pilot.py']
        out = dict(modulus=97, S=m.S, J=m.J, fixed_labels=[], universe=records,
                   inputs_sha256={p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
                   script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                   spans=spans, nodes=nodes, frontier=frontier,
                   evaluated_children=evaluated_children, witness=witness, summary=summary)
        temp = HERE/'cover.tmp'
        temp.write_text(json.dumps(out, separators=(',', ':'))+'\n')
        temp.replace(HERE/'cover.json')
        if final:
            print(json.dumps(summary, sort_keys=True), flush=True)
            print('Full evidence: scripts/pair-free-envelope/cover.json', flush=True)

    # Initial checkpoint precedes the potentially long calculation.
    save()
    while frontier:
        state = frontier.pop()
        history = state['history']
        if state['span'] is None:
            # Every unevaluated child is retained until both its test and its
            # independent replay/new-span stack checks fit in the budget.
            if producer_tests+reserve+2+len(history) > LIMIT:
                frontier.append(state)
                stop = 'block_test_cap_with_verification_reservation'
                break
            parent = nodes[state['parent']]
            k = np.array(spans[parent['span']]['kernel_basis'], dtype=np.int64)
            residual = blocks[state['chosen']] @ k.T % 97
            coeff = m.nullspace(residual, len(k))
            child_kernel, _ = m.rref((np.array(coeff, dtype=np.int64) @ k % 97).tolist(), 21)
            producer_tests += 1
            reserve += 1
            sid = intern(child_kernel, history)
            state['span'] = sid
            parent['children'][parent['candidates'].index(state['chosen'])]['span'] = sid
            evaluated_children.append(dict(parent=state['parent'], chosen=state['chosen'], span=sid))
            if len(spans) >= SPAN_LIMIT:
                frontier.append(state)
                stop = 'span_limit'
                break
        sid = state['span']
        span = spans[sid]
        if len(history) == 12:
            witness = dict(**state)
            stop = 'twelve_support_deficient_witness'
            break
        inc = span['extension_rank_increments']
        if len(inc) < 756:
            k = np.array(span['kernel_basis'], dtype=np.int64)
            # Form only counted restrictions, avoiding uncounted suffix tests.
            for a in range(len(inc), 756):
                if producer_tests+reserve+2 > LIMIT:
                    stop = 'block_test_cap_with_verification_reservation'
                    break
                inc.append(m.residual_rank(blocks[a] @ k.T % 97))
                producer_tests += 1
                reserve += 1
            if len(inc) < 756:
                frontier.append(state)
                break
            span['closure'] = [a for a, r in enumerate(inc) if r == 0]
        degrees = [sum(bool(masks[a] >> h & 1) for a in history) for h in range(16)]
        assert max(degrees, default=0) <= 4
        assert all(b in compatible[a] for a,b in m.combinations(history, 2))
        candidates = [a for a in range(state['last_added']+1, 756)
                      if span['rank']+inc[a] < 21
                      and all(a in compatible[b] for b in history)
                      and all(degrees[h] < 4 for h in range(16) if masks[a] >> h & 1)]
        dual = (dict(kind='candidate_count', numerator=len(candidates), denominator=1)
                if len(history)+len(candidates) <= 11 else m.best_capacity(candidates, degrees, records))
        upper = len(history)+dual['numerator']//dual['denominator']
        nid = len(nodes)
        node = dict(id=nid, **state, degrees=degrees, candidates=candidates,
                    capacity_certificate=dual, total_upper_bound=upper,
                    decision='capacity' if upper <= 11 else 'branch')
        nodes.append(node)
        if upper > 11:
            node['children'] = [dict(chosen=a, span=None) for a in candidates]
            frontier.extend(dict(history=history+[a], last_added=a, span=None, parent=nid, chosen=a)
                            for a in reversed(candidates))
        if len(nodes) % 100 == 0:
            print(f'Histories {len(nodes)}; spans {len(spans)}; committed tests '
                  f'{producer_tests+reserve}; frontier {len(frontier)}.', flush=True)
            save()
    if stop is None:
        stop = 'complete_cover'
    save(True)


if __name__ == '__main__':
    main()
