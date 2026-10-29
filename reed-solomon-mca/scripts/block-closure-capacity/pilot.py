#!/usr/bin/env python3
"""Bounded exact deficient-span/envelope search; full histories are retained.

No solver, symmetry reduction, decomposability assumption or coding converse.
The block-test counter counts each tested (span, whole block) once; cached
results can be reused by different selection histories without merging them.
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
PAIRS = list(combinations(range(7), 2))
INV = [0] + [pow(i, -1, P) for i in range(1, P)]
MAX_SPANS = 10000
MAX_TESTS = 1000000


def rref(matrix, width):
    a = [list(map(int, row)) for row in matrix]
    pivots = []
    for j in range(width):
        k = len(pivots)
        pos = next((i for i in range(k, len(a)) if a[i][j] % P), None)
        if pos is None:
            continue
        a[k], a[pos] = a[pos], a[k]
        a[k] = [(v * INV[a[k][j] % P]) % P for v in a[k]]
        for i in range(len(a)):
            if i != k and a[i][j] % P:
                t = a[i][j] % P
                a[i] = [(v - t*w) % P for v, w in zip(a[i], a[k])]
        pivots.append(j)
        if len(pivots) == len(a):
            break
    return a[:len(pivots)], pivots


def nullspace(matrix, width):
    a, pivots = rref(matrix, width)
    out = []
    for j in range(width):
        if j not in pivots:
            v = [0] * width
            v[j] = 1
            for i, col in enumerate(pivots):
                v[col] = -a[i][j] % P
            out.append(v)
    return out


def residual_rank(matrix):
    # Forward elimination only; separate from the canonical-kernel routine.
    a = [list(map(int, row)) for row in matrix]
    if not a:
        return 0
    rank = 0
    for j in range(len(a[0])):
        pos = next((i for i in range(rank, len(a)) if a[i][j]), None)
        if pos is None:
            continue
        a[rank], a[pos] = a[pos], a[rank]
        inv = INV[a[rank][j]]
        for i in range(rank+1, len(a)):
            if a[i][j]:
                t = a[i][j] * inv % P
                for k in range(j+1, len(a[0])):
                    a[i][k] = (a[i][k] - t*a[rank][k]) % P
                a[i][j] = 0
        rank += 1
        if rank == min(len(a), len(a[0])):
            break
    return rank


def universe():
    records = []
    for i_pair in combinations(S, 2):
        for k_pair in combinations(J, 2):
            g = []
            for x in S:
                value = 1
                for y in J:
                    if y not in k_pair:
                        value = value * (x-y) % P
                g.append(value)
            observed = [i for i, x in enumerate(S) if x not in i_pair]
            z = observed[0]
            q = [[(g[z]*(a == x)-g[x]*(a == z)) % P for a in range(7)]
                 for x in observed[1:]]
            n = [[(q[i][a]*q[j][b]-q[i][b]*q[j][a]) % P for a, b in PAIRS]
                 for i, j in combinations(range(4), 2)]
            records.append(dict(label=len(records), I=list(i_pair), K=list(k_pair),
                                support=sorted(i_pair+k_pair), pivot=S[z],
                                covector_labels=[S[x] for x in observed[1:]],
                                g_on_S=g, Q=q, N=n))
    return records


def best_capacity(candidates, degrees, records):
    """Exact duals using coordinates and disjoint pair-groups, or edge count.

    Each I group and each K group has capacity one by pairwise linearity.
    For a tested coordinate subset T and q in {1,2}, a group receives
    numerator max(0,q-min_{a in group}|a intersect T|). Every column then
    has coverage >=q. All weights and costs are integers divided by q.
    """
    best = dict(kind='candidate_count', numerator=len(candidates), denominator=1)
    if not candidates:
        return best
    by_side = {}
    for side in ('I', 'K'):
        groups = {}
        for a in candidates:
            groups.setdefault(tuple(records[a][side]), []).append(a)
        by_side[side] = groups
    support_bits = {a: sum(1 << H.index(x) for x in records[a]['support']) for a in candidates}
    for coord_side in (S, J):
        for mask in range(1 << len(coord_side)):
            coords = [x for k, x in enumerate(coord_side) if mask >> k & 1]
            bitmask = sum(1 << H.index(x) for x in coords)
            cost = sum(4-degrees[H.index(x)] for x in coords)
            hits = {a: (support_bits[a] & bitmask).bit_count() for a in candidates}
            for side, groups in by_side.items():
                minima = [(pair, min(hits[a] for a in group)) for pair, group in groups.items()]
                for q in (1, 2):
                    numerator = cost + sum(max(0, q-h) for _, h in minima)
                    if numerator * best['denominator'] < best['numerator'] * q:
                        best = dict(kind='coordinate_pair_dual', coordinates=coords,
                                    group_side=side, denominator=q, numerator=numerator,
                                    group_numerators=[dict(pair=list(pair), numerator=q-h)
                                                      for pair, h in minima if h < q])
    return best


def main():
    started = time.monotonic()
    records = universe()
    blocks = np.array([r['N'] for r in records], dtype=np.int64)
    masks = [sum(1 << H.index(x) for x in r['support']) for r in records]
    fixed = [next(r['label'] for r in records if r['I'] == i and r['K'] == k)
             for i, k in (([8, 12], [70, 75]), ([18, 22], [79, 85]))]
    compatible = [[b for b in range(756) if (masks[a] & masks[b]).bit_count() <= 1]
                  for a in range(756)]
    compatible_sets = list(map(set, compatible))
    initial_kernel, _ = rref(nullspace([row for a in fixed for row in records[a]['N']], 21), 21)
    spans = []
    span_keys = {}
    nodes = []
    frontier = []
    tests = 0
    witness = None
    stop_reason = None
    failures = []

    def intern(kernel, generating_history):
        key = bytes(x for row in kernel for x in row)
        if key in span_keys:
            return span_keys[key]
        if len(spans) >= MAX_SPANS:
            return None
        sid = len(spans)
        span_keys[key] = sid
        spans.append(dict(id=sid, generating_history=generating_history[:],
                          rank=21-len(kernel), kernel_basis=kernel,
                          extension_rank_increments=[], closure=None))
        return sid

    root_span = intern(initial_kernel, fixed)
    frontier.append(dict(history=fixed, last_added=-1, span=root_span,
                         parent=None, chosen=None))

    def save(final=False):
        summary = dict(complete=not frontier and witness is None and not failures,
                       stop_reason=stop_reason, span_count=len(spans),
                       node_count=len(nodes), block_tests=tests,
                       span_limit=MAX_SPANS, block_test_limit=MAX_TESTS,
                       frontier_count=len(frontier), witness_found=witness is not None,
                       required_total_capacity=11,
                       largest_leaf_upper_bound=max((n['total_upper_bound'] for n in nodes
                                                     if n.get('decision') == 'capacity'), default=None),
                       decisions=dict(Counter(n.get('decision', 'incomplete') for n in nodes)),
                       rank_counts=dict(sorted(Counter(s['rank'] for s in spans).items())),
                       elapsed_seconds=round(time.monotonic()-started, 3), failures=failures)
        out = dict(modulus=P, S=S, J=J, fixed_labels=fixed,
                   universe=records, column_pairs=[[S[a], S[b]] for a, b in PAIRS],
                   method='all-block deficient-extension envelope; separate ordered histories',
                   inputs_sha256={p: sha256((ROOT/p).read_bytes()).hexdigest() for p in (
                       'lemmas/L109-seven-coordinate-parameter-free-support-filter.md',
                       'lemmas/L167-completed-family-marked-extraction-counterexample.md',
                       'drafts/literature/2026-10-28-block-closure-capacity-pilot-review.md')},
                   script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
                   spans=spans, nodes=nodes, frontier=frontier, witness=witness, summary=summary)
        path = HERE / 'pilot.json'
        tmp = HERE / 'pilot.tmp'
        tmp.write_text(json.dumps(out, separators=(',', ':'))+'\n')
        tmp.replace(path)
        if final:
            print(json.dumps(summary, sort_keys=True), flush=True)
            print('Complete evidence and pending frontier: '+str(path.relative_to(ROOT)), flush=True)

    while frontier:
        state = frontier.pop()
        sid = state['span']
        span = spans[sid]
        history = state['history']
        if len(history) >= 12:
            witness = dict(history=history, span=sid)
            stop_reason = 'twelve_support_deficient_witness'
            break
        increments = span['extension_rank_increments']
        if len(increments) < 756:
            products = blocks @ np.array(span['kernel_basis'], dtype=np.int64).T % P
            for a in range(len(increments), 756):
                if tests >= MAX_TESTS:
                    stop_reason = 'block_test_limit'
                    break
                increments.append(residual_rank(products[a]))
                tests += 1
            if len(increments) < 756:
                frontier.append(state)
                break
            span['closure'] = [a for a, r in enumerate(increments) if r == 0]
        degrees = [sum(bool(masks[a] >> h & 1) for a in history) for h in range(16)]
        if max(degrees) > 4 or any(b not in compatible_sets[a] for a, b in combinations(history, 2)):
            failures.append(dict(kind='invalid_history', history=history))
            frontier.append(state)
            break
        candidates = [a for a in range(state['last_added']+1, 756)
                      if a not in history and span['rank']+increments[a] < 21
                      and all(a in compatible_sets[b] for b in history)
                      and all(degrees[h] < 4 for h in range(16) if masks[a] >> h & 1)]
        dual = best_capacity(candidates, degrees, records)
        upper = len(history) + dual['numerator']//dual['denominator']
        nid = len(nodes)
        node = dict(id=nid, **state, degrees=degrees, candidates=candidates,
                    capacity_certificate=dual, total_upper_bound=upper)
        nodes.append(node)
        if upper <= 11:
            node['decision'] = 'capacity'
        else:
            node['decision'] = 'branch'
            node['children'] = []
            new_states = []
            kernel = np.array(span['kernel_basis'], dtype=np.int64)
            for a in candidates:
                if len(spans) >= MAX_SPANS:
                    stop_reason = 'span_limit'
                    child_state = dict(history=history+[a], last_added=a, span=None,
                                       parent=nid, chosen=a, needs_kernel=True)
                    new_states.append(child_state)
                    node['children'].append(dict(chosen=a, span=None))
                    continue
                residual = blocks[a] @ kernel.T % P
                coefficient_kernel = nullspace(residual, len(kernel))
                child_kernel, _ = rref((np.array(coefficient_kernel, dtype=np.int64) @ kernel % P).tolist(), 21)
                child_history = history+[a]
                child_sid = intern(child_kernel, child_history)
                child_state = dict(history=child_history, last_added=a, span=child_sid,
                                   parent=nid, chosen=a)
                assert child_sid is not None
                new_states.append(child_state)
                node['children'].append(dict(chosen=a, span=child_sid))
            # Reverse insertion gives an increasing-label depth-first traversal.
            frontier.extend(reversed(new_states))
            if stop_reason:
                break
        if len(nodes) % 50 == 0:
            print(f'Visited {len(nodes)} histories; spans {len(spans)}; '
                  f'block tests {tests}; pending {len(frontier)}.', flush=True)
            save()
    if stop_reason is None:
        stop_reason = 'complete_cover' if not frontier else 'unfinished'
    save(final=True)


if __name__ == '__main__':
    main()
