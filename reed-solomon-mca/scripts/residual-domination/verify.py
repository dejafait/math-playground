#!/usr/bin/env python3
"""Independent finite incidence/set verifier; never constructs or ranks a matrix."""
from collections import Counter, defaultdict
from hashlib import sha256
from heapq import merge
from itertools import combinations, islice
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent


def main():
    raw = (ROOT/'scripts/pair-free-envelope/cover.json').read_bytes()
    data = json.loads(raw)
    prior_raw = (ROOT/'scripts/pair-free-envelope/verification.json').read_bytes()
    prior = json.loads(prior_raw)
    out_raw = (HERE/'comparison.json').read_bytes()
    proposed = json.loads(out_raw)
    failures, counts = [], Counter()

    def check(ok, name, detail=None):
        counts[name] += 1
        if not ok:
            failures.append(dict(check=name, detail=detail))

    check(prior['summary']['failures'] == [], 'prior_no_failures')
    check(prior['summary']['certificate_sha256'] == sha256(raw).hexdigest(), 'prior_cover_digest')
    check(prior['summary']['verifier_sha256'] ==
          sha256((ROOT/'scripts/pair-free-envelope/verify.py').read_bytes()).hexdigest(), 'prior_verifier_digest')
    check(prior['summary']['reused_verifier_sha256'] ==
          sha256((ROOT/'scripts/block-closure-capacity/verify.py').read_bytes()).hexdigest(), 'prior_reused_verifier_digest')
    for p,digest in proposed['input_sha256'].items():
        check(sha256((ROOT/p).read_bytes()).hexdigest() == digest, 'input_digest', p)
    check(proposed['script_sha256'] == sha256((HERE/'compare.py').read_bytes()).hexdigest(), 'producer_digest')
    check(data['modulus'] == 97 and data['fixed_labels'] == [] and data['S'] == [1,8,12,18,22,27,33]
          and data['J'] == [47,50,64,70,75,79,85,89,96], 'fixed_parameters')
    h = data['S']+data['J']
    supports = sorted((sorted(s) for s in combinations(h,4)
                       if len(set(s)&set(h[:7])) == 2),
                      key=lambda s:(sorted(set(s)&set(h[:7])),sorted(set(s)&set(h[7:]))))
    sets = list(map(frozenset,supports))
    check(len(sets) == len(data['universe']) == len(prior['reconstructed_universe']) == 756, 'support_count')
    coord_labels, pair_labels = defaultdict(set), defaultdict(set)
    for a,s in enumerate(sets):
        check(data['universe'][a]['label'] == prior['reconstructed_universe'][a]['label'] == a
              and data['universe'][a]['support'] == prior['reconstructed_universe'][a]['support'] == supports[a],
              'original_incidence', a)
        for x in s:
            coord_labels[x].add(a)
        for pair in combinations(sorted(s),2):
            pair_labels[pair].add(a)
    kernels, allowed = {}, {}
    check(len(data['spans']) == len(prior['spans']), 'span_count')
    for sid,span in enumerate(data['spans']):
        checked = prior['spans'][sid]
        for field in ('id','kernel_basis','rank','extension_rank_increments','closure'):
            check(span[field] == checked[field], 'cached_span_field', [sid,field])
        key = tuple(map(tuple,span['kernel_basis']))
        check(span['id'] == sid and key not in kernels, 'span_identity', sid)
        kernels[key] = sid
        inc = span['extension_rank_increments']
        if len(inc) == 756:
            allowed[sid] = {a for a,r in enumerate(inc) if r < 21-span['rank']}
    groups, candidates, node_checks = defaultdict(list), [], []
    nodes = data['nodes']
    check(len(nodes) == len(prior['nodes']) == len(proposed['node_checks']), 'node_count')
    for i,node in enumerate(nodes):
        hist = node['history']
        check(node['id'] == i and all(a < b for a,b in zip(hist,hist[1:]))
              and node['last_added'] == max(hist,default=-1), 'increasing_history', i)
        degree = Counter(x for a in hist for x in sets[a])
        check(all(d <= 4 for d in degree.values())
              and all(len(sets[a]&sets[b]) < 2 for a,b in combinations(hist,2)), 'feasible_history', i)
        check(node['span'] in allowed, 'fully_materialized', i)
        forbidden = set(range(node['last_added']+1))
        for a in hist:
            for pair in combinations(sorted(sets[a]),2):
                forbidden.update(pair_labels[pair])
        for x in h:
            if degree[x] == 4:
                forbidden.update(coord_labels[x])
        cand = allowed[node['span']]-forbidden
        ordered = sorted(cand)
        residual = [4-degree[x] for x in h]
        check([degree[x] for x in h] == node['degrees'] == prior['nodes'][i]['degrees'], 'integer_degrees', i)
        check(ordered == node['candidates'] == prior['nodes'][i]['candidates'], 'complete_candidate_set', i)
        evidence = dict(id=i,candidates=ordered,residual_degrees=residual)
        check(evidence == proposed['node_checks'][i], 'producer_node_evidence', i)
        candidates.append(cand)
        node_checks.append(evidence)
        key = (tuple(map(tuple,data['spans'][node['span']]['kernel_basis'])),len(hist),tuple(residual))
        groups[key].append(i)
    group_records = [dict(span=kernels[key[0]],cardinality=key[1],residual_degrees=list(key[2]),nodes=ids)
                     for key,ids in groups.items()]
    group_records.sort(key=lambda g:min(g['nodes']))
    check(group_records == proposed['groups'], 'entire_partition')
    eligible = sum(len(ids)*(len(ids)-1)//2 for ids in groups.values())
    ordered_pairs = merge(*(combinations(ids,2) for ids in groups.values() if len(ids)>1))
    results, arrows = [], []
    for a,b in islice(ordered_pairs,100000):
        ab,ba = candidates[a].issubset(candidates[b]),candidates[b].issubset(candidates[a])
        results.append(dict(a=a,b=b,a_subset_b=ab,b_subset_a=ba))
        if ab and not ba:
            arrows.append([a,b])
        if ba:
            arrows.append([b,a])
    check(results == proposed['pairs'], 'entire_pair_prefix_and_both_directions')
    check(arrows == proposed['acyclic_arrows'], 'entire_proposed_arrow_list')
    chosen = {}
    for source,target in arrows:
        a,b = nodes[source],nodes[target]
        check(a['span'] == b['span'] and len(a['history']) == len(b['history'])
              and a['degrees'] == b['degrees'] and a['history'] != b['history']
              and candidates[source] <= candidates[target], 'all_domination_hypotheses', [source,target])
        check((len(candidates[target]) > len(candidates[source])) or
              (candidates[target] == candidates[source] and target < source), 'strict_potential', [source,target])
        previous = chosen.get(source)
        if previous is None or (-len(candidates[target]),target) < (-len(candidates[previous]),previous):
            chosen[source] = target
    policy, chain_failures = [], []
    for source in sorted(chosen):
        terminal, seen = source,set()
        while terminal in chosen and terminal not in seen:
            seen.add(terminal)
            terminal = chosen[terminal]
        if terminal in seen:
            chain_failures.append(source)
        check(candidates[source] <= candidates[terminal] and terminal not in chosen,
              'retained_representative', source)
        policy.append(dict(source=source,target=chosen[source],retained=terminal,
                           retained_decision=nodes[terminal]['decision'],
                           obligation='Existing capacity certificate' if nodes[terminal]['decision']=='capacity'
                           else 'Entire residual branch search remains required; original frontier untouched'))
    check(not chain_failures, 'no_policy_cycles')
    check(policy == proposed['policy'], 'entire_policy_and_obligations')
    expected = dict(total_nodes=len(nodes), total_groups=len(groups),
                    multi_node_groups=sum(len(ids)>1 for ids in groups.values()),
                    eligible_unordered_pairs=eligible, tested_unordered_pairs=len(results),pair_limit=100000,
                    all_eligible_covered=len(results)==eligible,budget_exhausted=len(results)<eligible,
                    inclusion_directions=sum(p['a_subset_b']+p['b_subset_a'] for p in results),
                    equal_candidate_pairs=sum(p['a_subset_b'] and p['b_subset_a'] for p in results),
                    strict_inclusion_pairs=sum(p['a_subset_b'] != p['b_subset_a'] for p in results),
                    policy_sources=len(policy),distinct_retained=len({p['retained'] for p in policy}),
                    required_nontrivial_relations=1,new_block_rank_tests=0,
                    original_frontier_count=len(data['frontier']),cover_modified=False,
                    uniform_capacity_proved=False,failures=[])
    check(proposed['summary'] == expected, 'entire_producer_summary')
    check(expected['inclusion_directions'] >= 1, 'continuation_threshold')
    # Both frozen inputs must still have their pre-test bytes.
    check(sha256((ROOT/'scripts/pair-free-envelope/cover.json').read_bytes()).hexdigest() == sha256(raw).hexdigest(),
          'cover_unmodified')
    check(sha256((ROOT/'scripts/pair-free-envelope/verification.json').read_bytes()).hexdigest() == sha256(prior_raw).hexdigest(),
          'prior_verification_unmodified')
    branch_arrows = [[s,t] for s,t in arrows if nodes[s]['decision']=='branch']
    first_strict = next((p for p in results if p['a_subset_b'] != p['b_subset_a']),None)
    example_ids = [] if first_strict is None else [first_strict['a'],first_strict['b']]
    examples = [dict(id=i,history=nodes[i]['history'],span=nodes[i]['span'],
                     degrees=nodes[i]['degrees'],candidates=sorted(candidates[i]),decision=nodes[i]['decision'])
                for i in example_ids]
    branch_examples = [dict(id=i,history=nodes[i]['history'],span=nodes[i]['span'],
                            degrees=nodes[i]['degrees'],candidates=sorted(candidates[i]),decision=nodes[i]['decision'])
                       for i in (branch_arrows[0] if branch_arrows else [])]
    summary = dict(**{k:v for k,v in expected.items() if k!='failures'},
                   verified_arrows=len(arrows),branch_source_arrows=len(branch_arrows),
                   branch_to_branch_arrows=sum(nodes[t]['decision']=='branch' for s,t in branch_arrows),
                   checks=dict(counts),failures=failures,
                   comparison_sha256=sha256(out_raw).hexdigest(),
                   verifier_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    certificate = dict(summary=summary,input_sha256=proposed['input_sha256'],
                       node_checks=node_checks,groups=group_records,pairs=results,
                       verified_arrows=arrows,policy=policy,first_strict_pair=first_strict,
                       strict_pair_nodes=examples,first_branch_arrow=branch_arrows[0] if branch_arrows else None,
                       branch_arrow_nodes=branch_examples)
    (HERE/'verification.json').write_text(json.dumps(certificate,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='checks'},sort_keys=True))
    print('Full independent certificate: scripts/residual-domination/verification.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
