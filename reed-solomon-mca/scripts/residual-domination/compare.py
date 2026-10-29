#!/usr/bin/env python3
"""Offline comparison only: cached integer ranks, no matrix operations."""
from collections import defaultdict
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
LIMIT = 100000


def main():
    paths = ['scripts/pair-free-envelope/cover.json',
             'scripts/pair-free-envelope/verification.json',
             'drafts/literature/2026-10-28-residual-domination-offline-test-review.md']
    hashes = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    data = json.loads((ROOT/paths[0]).read_text())
    prior = json.loads((ROOT/paths[1]).read_text())
    failures = []

    def check(ok, name, detail=None):
        if not ok:
            failures.append(dict(check=name, detail=detail))

    check(prior['summary']['failures'] == [], 'prior_failures')
    check(prior['summary']['certificate_sha256'] == hashes[paths[0]], 'prior_cover_hash')
    check(data['modulus'] == 97 and data['fixed_labels'] == [], 'model')
    h = data['S']+data['J']
    check(h == [1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96], 'coordinates')
    expected = [(list(i),list(k)) for i in combinations(h[:7],2) for k in combinations(h[7:],2)]
    records = data['universe']
    check(len(records) == len(expected) == 756, 'universe_size')
    for a,(i,k) in enumerate(expected):
        check(records[a]['label'] == a and records[a]['I'] == i and records[a]['K'] == k
              and records[a]['support'] == sorted(i+k), 'incidence', a)
        check(all(records[a][key] == prior['reconstructed_universe'][a][key]
                  for key in ('label','I','K','support')), 'prior_incidence', a)
    masks = [sum(1 << h.index(x) for x in r['support']) for r in records]
    all_bits = (1 << 756)-1
    compatible = [sum(1 << b for b in range(756) if (mask & masks[b]).bit_count() <= 1)
                  for mask in masks]
    coord_bits = [sum(1 << a for a,m in enumerate(masks) if m >> j & 1) for j in range(16)]
    envelopes, span_keys = {}, {}
    for span in data['spans']:
        sid = span['id']
        key = tuple(map(tuple,span['kernel_basis']))
        check(key not in span_keys, 'unique_canonical_span', sid)
        span_keys[key] = sid
        increments = span['extension_rank_increments']
        if len(increments) == 756:
            envelopes[sid] = sum(1 << a for a,r in enumerate(increments) if span['rank']+r < 21)
    nodes = data['nodes']
    groups = defaultdict(list)
    bits, checks = [], []
    check(len(nodes) == len(prior['nodes']), 'prior_node_count')
    for nid,node in enumerate(nodes):
        hist = node['history']
        check(node['id'] == nid and hist == sorted(set(hist)), 'node_history', nid)
        check(node['last_added'] == (hist[-1] if hist else -1), 'last_label', nid)
        check(node['span'] in envelopes, 'complete_span_scan', nid)
        deg = [sum(masks[a] >> j & 1 for a in hist) for j in range(16)]
        check(max(deg) <= 4 and all((masks[a]&masks[b]).bit_count() <= 1
                                  for a,b in combinations(hist,2)), 'feasible_history', nid)
        check(deg == node['degrees'] == prior['nodes'][nid]['degrees'], 'degrees', nid)
        cand = envelopes[node['span']] & (all_bits ^ ((1 << (node['last_added']+1))-1))
        for a in hist:
            cand &= compatible[a]
        for j,d in enumerate(deg):
            if d == 4:
                cand &= all_bits ^ coord_bits[j]
        labels = [a for a in range(756) if cand >> a & 1]
        check(labels == node['candidates'] == prior['nodes'][nid]['candidates'], 'complete_B', nid)
        bits.append(cand)
        checks.append(dict(id=nid, candidates=labels, residual_degrees=[4-d for d in deg]))
        groups[(node['span'],len(hist),tuple(4-d for d in deg))].append(nid)
    group_list = [dict(span=s, cardinality=c, residual_degrees=list(d), nodes=ids)
                  for (s,c,d),ids in groups.items()]
    group_list.sort(key=lambda g:g['nodes'][0])
    eligible = sum(len(g['nodes'])*(len(g['nodes'])-1)//2 for g in group_list)
    later = {}
    for g in group_list:
        ids = g['nodes']
        for j,nid in enumerate(ids):
            later[nid] = (ids,j+1)
    pairs, arrows = [], []
    for a in range(len(nodes)):
        ids,start = later[a]
        for b in ids[start:]:
            if len(pairs) == LIMIT:
                break
            ab, ba = bits[a] & ~bits[b] == 0, bits[b] & ~bits[a] == 0
            pairs.append(dict(a=a,b=b,a_subset_b=ab,b_subset_a=ba))
            # Strict inclusion increases |B|; equality goes toward lower ID.
            if ab and not ba:
                arrows.append([a,b])
            if ba:
                arrows.append([b,a])
        if len(pairs) == LIMIT:
            break
    potential = lambda a:(-bits[a].bit_count(),a)
    chosen = {}
    for source,target in arrows:
        check(potential(target) < potential(source), 'acyclic_arrow', [source,target])
        if source not in chosen or potential(target) < potential(chosen[source]):
            chosen[source] = target
    policy = []
    for source in sorted(chosen):
        end = source
        while end in chosen:
            end = chosen[end]
        policy.append(dict(source=source, target=chosen[source], retained=end,
                           retained_decision=nodes[end]['decision'],
                           obligation='Existing capacity certificate' if nodes[end]['decision']=='capacity'
                           else 'Entire residual branch search remains required; original frontier untouched'))
    summary = dict(total_nodes=len(nodes), total_groups=len(groups),
                   multi_node_groups=sum(len(g['nodes'])>1 for g in group_list),
                   eligible_unordered_pairs=eligible, tested_unordered_pairs=len(pairs), pair_limit=LIMIT,
                   all_eligible_covered=len(pairs)==eligible, budget_exhausted=len(pairs)<eligible,
                   inclusion_directions=sum(p['a_subset_b']+p['b_subset_a'] for p in pairs),
                   equal_candidate_pairs=sum(p['a_subset_b'] and p['b_subset_a'] for p in pairs),
                   strict_inclusion_pairs=sum(p['a_subset_b'] != p['b_subset_a'] for p in pairs),
                   policy_sources=len(policy), distinct_retained=len({p['retained'] for p in policy}),
                   required_nontrivial_relations=1, new_block_rank_tests=0,
                   original_frontier_count=len(data['frontier']), cover_modified=False,
                   uniform_capacity_proved=False, failures=failures)
    out = dict(summary=summary, input_sha256=hashes,
               script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
               node_checks=checks, groups=group_list, pairs=pairs, acyclic_arrows=arrows, policy=policy)
    (HERE/'comparison.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(summary,sort_keys=True))
    print('Full certificate: scripts/residual-domination/comparison.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
