"""Verify generation and full certificates; import no search code."""
from collections import Counter
from itertools import combinations
import importlib.util
import json
from pathlib import Path
from random import Random

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
spec = importlib.util.spec_from_file_location('prior_independent_verifier', ROOT / 'scripts/matching-two-rank/verify.py')
ind = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ind)
P, CP, RP = ind.P, ind.CP, ind.RP


def edge_set(edges):
    return frozenset(frozenset(e) for e in edges)


def check_generation(plan):
    previous = json.loads((ROOT / 'scripts/matching-two-rank/plan.json').read_text())
    assert plan['parents'] == previous['families']
    parents = {f['id']: f for f in plan['parents']}
    old = {edge_set(f['edges']) for f in parents.values()}
    assert len(old) == len(parents) == 63
    fresh = plan['families'][3:]
    assert plan['families'][:3] == plan['parents'][:3]
    assert [f['seed'] for f in plan['families'][:3]] == [[0, 1, 2, 5], [0, 1, 3, 5], [0, 1, 2, 4]]
    # Independently generate the prescribed switch order, consuming only
    # the saved bounded prefix and checking every accept/reject decision.
    def switches():
        for parent in plan['parents']:
            for i in range(16):
                for j in range(i + 1, 16):
                    a, b = set(parent['edges'][i]), set(parent['edges'][j])
                    for x in sorted(a.difference(b)):
                        for y in sorted(b.difference(a)):
                            yield parent['id'], i, j, x, y
    sequence = switches()
    accepted, rejected, selected, reason_counts = [], 0, set(), Counter()
    for rec in plan['generation']['records']:
        pid, i, j, x, y = next(sequence)
        assert (pid, [i, j], [x, y]) == (rec['parent_id'], rec['edge_indices'], rec['exchanged_vertices'])
        edges = [set(e) for e in parents[pid]['edges']]
        assert x in edges[i] - edges[j] and y in edges[j] - edges[i]
        edges[i].remove(x)
        edges[i].add(y)
        edges[j].remove(y)
        edges[j].add(x)
        key = edge_set(edges)
        reasons = []
        if len(edges) != 16 or len(key) != 16:
            reasons.append('nonsimple')
        if any(len(e) != 4 or not e <= set(range(16)) for e in edges):
            reasons.append('edge_size_or_vertices')
        if [sum(v in e for e in edges) for v in range(16)] != [4] * 16:
            reasons.append('degree')
        if not any(edges[i].isdisjoint(edges[j]) for i, j in combinations(range(16), 2)):
            reasons.append('no_disjoint_pair')
        triple = next((list(c) for c in combinations(range(16), 3)
                       if all(edges[a].isdisjoint(edges[b]) for a, b in combinations(c, 2))), None)
        if triple is not None:
            reasons.append('disjoint_triple')
        if key in old:
            reasons.append('prior_collection')
        if edge_set([{(v + 1) % 16 for v in e} for e in edges]) == key:
            reasons.append('translation_invariant')
        if key in selected:
            reasons.append('already_selected')
        assert reasons == rec['reasons'] and triple == rec['disjoint_triple_witness']
        reason_counts.update(reasons)
        if reasons:
            assert rec['accepted_id'] is None
            rejected += 1
        else:
            idx = len(accepted)
            assert rec['accepted_id'] == fresh[idx]['id'] == f'switch-{idx:03d}'
            assert [sorted(e) for e in edges] == fresh[idx]['edges']
            assert rec == fresh[idx]['switch']
            accepted.append(rec['accepted_id'])
            selected.add(key)
    generation = plan['generation']
    assert len(accepted) == len(selected) == len(fresh) == generation['accepted'] <= 125
    assert rejected == generation['rejected']
    assert len(accepted) + rejected == generation['candidate_count'] == len(generation['records'])
    assert dict(reason_counts) == generation['reason_counts']
    assert generation['stopped_at_fresh_cap'] == (len(fresh) == 125)
    assert generation['parent_one_switch_enumeration_exhausted'] == (len(fresh) < 125)
    if len(fresh) < 125:
        assert next(sequence, None) is None
    assert not generation['records'][-1]['reasons'] if len(fresh) == 125 else True
    return {'candidates_checked': len(generation['records']), 'rejections_checked': rejected,
            'fresh_families_checked': len(fresh), 'parent_counts': dict(Counter(f['switch']['parent_id'] for f in fresh)),
            'reason_counts': dict(reason_counts), 'translation_noninvariance_checked': True,
            'fresh_collections_distinct_from_prior_checked': True}


def main():
    plan = json.loads((HERE / 'plan.json').read_text())
    result = json.loads((HERE / 'result.json').read_text())
    gs = check_generation(plan)
    assert plan['modulus'] == P
    assert plan['column_pairs'] == [list(p) for p in CP]
    assert plan['row_pairs'] == [list(p) for p in RP]
    H = [x for x in range(1, P) if pow(x, 16, P) == 1]
    assert plan['H'] == H and len(H) == 16
    assert pow(8, 16, P) == 1 and pow(8, 8, P) != 1
    shuffled = H[:]
    Random(20261006059).shuffle(shuffled)
    labels = [('powers-8', [pow(8, i, P) for i in range(16)]), ('shuffle-20261006059', shuffled)]
    expected = [{'family_id': f['id'], 'labeling_id': name, 'labeling': lab,
                 'control': fi < 2, 'fresh': fi >= 3}
                for fi, f in enumerate(plan['families']) for name, lab in labels]
    assert expected == plan['cases']
    assert len(expected) == 2 * len(plan['families']) <= plan['limit'] == 256
    families = {f['id']: f for f in plan['families']}
    assert len({(edge_set(families[c['family_id']]['edges']), tuple(c['labeling'])) for c in expected}) == len(expected)
    for f in families.values():
        edges = [set(e) for e in f['edges']]
        assert len(edges) == len(edge_set(edges)) == 16
        assert all(len(e) == 4 and e <= set(range(16)) for e in edges)
        degrees = [sum(v in e for e in edges) for v in range(16)]
        assert degrees == f['incidence']['degrees'] == [4] * 16
        pairs = [list(c) for c in combinations(range(16), 2) if edges[c[0]].isdisjoint(edges[c[1]])]
        triples = [list(c) for c in combinations(range(16), 3)
                   if all(edges[i].isdisjoint(edges[j]) for i, j in combinations(c, 2))]
        assert pairs == f['incidence']['disjoint_pairs'] and pairs
        assert triples == f['incidence']['disjoint_triples'] == []
        assert f['incidence']['admissible']
    moment_blocks = {}
    for key, saved in result['support_blocks'].items():
        lab = list(map(int, key.split(',')))
        assert saved['labels'] == lab and len(lab) == len(set(lab)) == 4 and set(lab) <= set(H)
        rows = ind.exact_polynomial_rows(lab)
        assert rows == saved['annihilator']
        matrix = ind.wedge(rows)
        assert matrix == saved['matrix']
        moment_rows = ind.moment_annihilator(lab)
        assert ind.reduce_rows(rows)[0] == ind.reduce_rows(moment_rows)[0]
        moment_blocks[key] = ind.wedge(moment_rows)
        assert ind.reduce_rows(matrix)[0] == ind.reduce_rows(moment_blocks[key])[0]
        assert len(ind.reduce_rows(matrix)[1]) == 6
    checked = []
    for ci, saved in enumerate(result['cases']):
        assert saved['plan_index'] == ci
        case = expected[ci]
        assert sorted(case['labeling']) == H
        keys = [','.join(map(str, sorted(case['labeling'][v] for v in e)))
                for e in families[case['family_id']]['edges']]
        assert saved['support_keys'] == keys
        matrix = [row for k in keys for row in result['support_blocks'][k]['matrix']]
        independent = [row for k in keys for row in moment_blocks[k]]
        assert len(matrix) == len(independent) == 96 and all(len(row) == 28 for row in matrix + independent)
        rank = len(ind.reduce_rows(independent)[1])
        assert rank == saved['rank'] == len(ind.reduce_rows(matrix)[1])
        indices, cols = saved['selected_rows'], saved['minor_columns']
        assert len(indices) == len(set(indices)) == len(cols) == len(set(cols)) == rank
        assert all(0 <= i < 96 for i in indices) and all(0 <= j < 28 for j in cols)
        det = ind.column_determinant([[matrix[i][j] for j in cols] for i in indices])
        assert det == saved['minor_determinant'] != 0
        if case['control']:
            assert rank == 28
        if rank < 28:
            defect = result['defect']
            assert ci == len(result['cases']) - 1 == defect['plan_index']
            assert defect['matrix'] == matrix
            kernel = defect['kernel_basis']
            assert len(kernel) == 28 - rank == len(ind.reduce_rows(kernel)[1])
            assert all(len(v) == 28 and any(v) for v in kernel)
            assert all(sum(a * b for a, b in zip(row, v)) % P == 0
                       for row in matrix + independent for v in kernel)
        checked.append({'plan_index': ci, 'rank': rank, 'minor_determinant': det,
                        'independent_moment_rank': rank})
    summary = result['summary']
    assert summary['planned'] == len(expected) and summary['tested'] == len(checked)
    assert summary['required_rank'] == 28 and summary['limit'] == 256
    assert summary['rank_counts'] == {str(k): v for k, v in Counter(c['rank'] for c in checked).items()}
    assert summary['controls_passed'] == sum(expected[c['plan_index']]['control'] for c in checked)
    assert summary['fresh_pairs_tested'] == sum(expected[c['plan_index']]['fresh'] for c in checked)
    assert not summary['failures']
    if result['defect'] is None:
        assert len(checked) == len(expected) and all(c['rank'] == 28 for c in checked)
        assert summary['defect_index'] is None and not summary['universal_rank_refuted_pending_independent_check']
    else:
        assert summary['defect_index'] == result['defect']['plan_index']
    vs = {**gs, 'families_checked': len(families), 'pairs_checked': len(checked),
          'fresh_pairs_checked': summary['fresh_pairs_tested'], 'blocks_checked': len(moment_blocks),
          'all_saved_entries_checked': True, 'matrix_entries_checked': 96 * 28 * len(checked),
          'required_rank': 28, 'actual_ranks': sorted({c['rank'] for c in checked}),
          'failures': [], 'universal_theorem_proved': False}
    (HERE / 'verification.json').write_text(json.dumps({'summary': vs, 'cases': checked}, separators=(',', ':')) + '\n')
    print(json.dumps(vs, sort_keys=True))
    print('Independent verification: scripts/matching-two-switch-rank/verification.json')


if __name__ == '__main__':
    main()
