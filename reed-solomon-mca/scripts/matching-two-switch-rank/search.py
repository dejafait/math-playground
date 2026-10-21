"""Frozen <=256-pair switch test; reuse the existing polynomial convention."""
from collections import Counter
from itertools import combinations
import importlib.util
import json
from pathlib import Path
from random import Random

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location('prior_rank_search', ROOT / 'scripts/matching-two-rank/search.py')
prior = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prior)
P, H, CP, RP = prior.P, prior.H, prior.CP, prior.RP


def collection(edges):
    return tuple(sorted(tuple(sorted(e)) for e in edges))


def screen(edges, old, selected):
    key = collection(edges)
    masks = [sum(1 << v for v in e) for e in edges]
    reasons = []
    if len(edges) != 16 or len(set(masks)) != 16:
        reasons.append('nonsimple')
    if any(len(e) != len(set(e)) or len(e) != 4 or not set(e) <= set(range(16)) for e in edges):
        reasons.append('edge_size_or_vertices')
    if [sum(v in e for e in edges) for v in range(16)] != [4] * 16:
        reasons.append('degree')
    neighbors = [{j for j in range(16) if j != i and not masks[i] & masks[j]} for i in range(16)]
    if not any(neighbors):
        reasons.append('no_disjoint_pair')
    triple = next(([i, j, k] for i in range(16) for j in sorted(neighbors[i]) if j > i
                   for k in sorted(neighbors[i] & neighbors[j]) if k > j), None)
    if triple is not None:
        reasons.append('disjoint_triple')
    if key in old:
        reasons.append('prior_collection')
    if collection([[(v + 1) % 16 for v in e] for e in edges]) == key:
        reasons.append('translation_invariant')
    if key in selected:
        reasons.append('already_selected')
    return reasons, triple


def make_plan():
    old_plan = json.loads((ROOT / 'scripts/matching-two-rank/plan.json').read_text())
    parents = old_plan['families']
    old = {collection(f['edges']) for f in parents}
    assert len(parents) == len(old) == 63
    baselines = parents[:3]
    assert [f['seed'] for f in baselines] == [[0, 1, 2, 5], [0, 1, 3, 5], [0, 1, 2, 4]]
    selected, fresh, records = set(), [], []
    stopped = False
    for parent in parents:
        for i, j in combinations(range(16), 2):
            a, b = set(parent['edges'][i]), set(parent['edges'][j])
            for x in sorted(a - b):
                for y in sorted(b - a):
                    edges = [e[:] for e in parent['edges']]
                    edges[i], edges[j] = sorted(a - {x} | {y}), sorted(b - {y} | {x})
                    reasons, triple = screen(edges, old, selected)
                    record = {'parent_id': parent['id'], 'edge_indices': [i, j],
                              'exchanged_vertices': [x, y], 'reasons': reasons,
                              'disjoint_triple_witness': triple, 'accepted_id': None}
                    if not reasons:
                        fid = f'switch-{len(fresh):03d}'
                        record['accepted_id'] = fid
                        selected.add(collection(edges))
                        fresh.append({'id': fid, 'edges': edges, 'switch': record.copy(),
                                      'incidence': prior.incidence(edges)})
                    records.append(record)
                    if len(fresh) == 125:
                        stopped = True
                        break
                if stopped:
                    break
            if stopped:
                break
        if stopped:
            break
    cyclic = [pow(8, i, P) for i in range(16)]
    shuffled = H[:]
    Random(20261006059).shuffle(shuffled)
    labels = [('powers-8', cyclic), ('shuffle-20261006059', shuffled)]
    assert all(sorted(lab) == H for _, lab in labels) and cyclic != shuffled
    families = baselines + fresh
    cases = [{'family_id': f['id'], 'labeling_id': name, 'labeling': lab,
              'control': f in baselines[:2], 'fresh': f in fresh}
             for f in families for name, lab in labels]
    assert len(cases) <= 256
    assert len({(collection(f['edges']), tuple(lab)) for f in families for _, lab in labels}) == len(cases)
    counts = Counter(reason for r in records for reason in r['reasons'])
    generation = {'candidate_count': len(records), 'accepted': len(fresh),
                  'rejected': sum(bool(r['reasons']) for r in records),
                  'reason_counts': dict(counts), 'stopped_at_fresh_cap': stopped,
                  'parent_one_switch_enumeration_exhausted': not stopped,
                  'records': records}
    return {'limit': 256, 'modulus': P, 'H': H, 'column_pairs': CP, 'row_pairs': RP,
            'parents': parents, 'families': families, 'cases': cases, 'generation': generation}


def main():
    plan = make_plan()
    # No matrix or rank is formed until the complete plan has been saved.
    (HERE / 'plan.json').write_text(json.dumps(plan, separators=(',', ':')) + '\n')
    gs = {k: v for k, v in plan['generation'].items() if k != 'records'}
    print('Generation: ' + json.dumps(gs, sort_keys=True), flush=True)
    families = {f['id']: f for f in plan['families']}
    blocks, cases, failures, defect = {}, [], [], None
    if not plan['generation']['accepted']:
        failures.append('No fresh qualifying switch family; rank testing stopped')
    for ci, case in enumerate(plan['cases'] if not failures else []):
        keys, matrix = [], []
        for edge in families[case['family_id']]['edges']:
            labels = sorted(case['labeling'][v] for v in edge)
            key = ','.join(map(str, labels))
            if key not in blocks:
                blocks[key] = prior.block(labels)
            keys.append(key)
            matrix.extend(blocks[key]['matrix'])
        indices = prior.selected_rows(matrix)
        selected = [matrix[i] for i in indices]
        reduced, pivots = prior.rref(selected)
        det = prior.determinant([[row[j] for j in pivots] for row in selected])
        rank = len(indices)
        cases.append({'plan_index': ci, 'support_keys': keys, 'rank': rank,
                      'selected_rows': indices, 'minor_columns': pivots, 'minor_determinant': det})
        if not det or len(pivots) != rank:
            failures.append(f'Invalid rank certificate at case {ci}')
        if case['control'] and rank != 28:
            failures.append(f'Failed known rank control at case {ci}')
        if rank < 28:
            kernel = prior.kernels(reduced, pivots)
            assert all(sum(a * b for a, b in zip(row, v)) % P == 0 for row in matrix for v in kernel)
            defect = {'plan_index': ci, 'matrix': matrix, 'kernel_basis': kernel,
                      'selected_reduced': reduced, 'pivot_columns': pivots}
        if defect or failures:
            break
    summary = {'planned': len(plan['cases']), 'limit': 256, 'tested': len(cases),
               'fresh_families': plan['generation']['accepted'],
               'fresh_pairs_tested': sum(plan['cases'][c['plan_index']]['fresh'] for c in cases),
               'required_rank': 28, 'rank_counts': dict(Counter(c['rank'] for c in cases)),
               'defect_index': None if defect is None else defect['plan_index'],
               'controls_passed': sum(plan['cases'][c['plan_index']]['control'] and c['rank'] == 28 for c in cases),
               'failures': failures, 'universal_rank_refuted_pending_independent_check': defect is not None and not failures}
    report = {'summary': summary, 'cases': cases, 'support_blocks': blocks, 'defect': defect}
    (HERE / 'result.json').write_text(json.dumps(report, separators=(',', ':')) + '\n')
    print(json.dumps(summary, sort_keys=True))
    print('Inputs and all candidate outcomes: scripts/matching-two-switch-rank/plan.json')
    print('Full rank certificate: scripts/matching-two-switch-rank/result.json')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
