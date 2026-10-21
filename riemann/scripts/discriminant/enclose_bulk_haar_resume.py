"""Step 190: one capped continuation of the complete step-189 partition.

Integer interval arithmetic and exact rational masses; no sampled proof
decisions. Read-only input certificates, full output partition and split tree.
"""
import hashlib
import heapq
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

import enclose_bulk_haar_integral as base
from enclose_bulk_haar_adaptive import children, decode, mass

I, SCALE = base.I, base.SCALE
LEAF_CAP = 131072
EVALUATION_CAP = 524288


def encoded(lo, hi):
    return {'lower': str(lo/SCALE), 'upper': str(hi/SCALE)}


def check_sums(leaves, interval):
    assert sum(map(mass, leaves)) == 1
    lo = sum(mass(k)*v.lo for k, v in leaves.items())
    hi = sum(mass(k)*v.hi for k, v in leaves.items())
    assert encoded(lo, hi) == interval
    return lo, hi


def replay_splits(leaves, splits):
    for record in splits:
        key, axis = tuple(record['parent']), record['axis']
        assert axis in range(4)
        parent = leaves.pop(key)
        assert parent.enc() == record['parent_range']
        keys = children(key, axis)
        assert sum(map(mass, keys)) == mass(key)
        for key, enc in zip(keys, record['child_ranges'], strict=True):
            value = decode(enc)
            assert parent.lo <= value.lo <= value.hi <= parent.hi
            assert key not in leaves
            leaves[key] = value


def main():
    directory = Path(__file__).parent
    source_path = directory/'bulk-haar-adaptive-enclosure-189.json'
    source_bytes = source_path.read_bytes()
    source = json.loads(source_bytes)
    root_path = directory/source['input_certificate']
    assert root_path.name == 'bulk-haar-integral-enclosure-188.json'
    root_bytes = root_path.read_bytes()
    assert hashlib.sha256(root_bytes).hexdigest() == source['input_sha256']
    root = json.loads(root_bytes)
    assert all(root['checks'].values()) and all(source['checks'].values())
    g, coefficients = base.source_coefficients(directory)
    assert coefficients == root['coefficients'] == source['coefficients']
    assert source['full_log_tail'] == root['full_log_tail']
    assert source['full_squared_modulus_tail_factor'] == root['full_squared_modulus_tail_factor']
    tail = decode(source['full_log_tail'])
    tail_factor = decode(source['full_squared_modulus_tail_factor'])
    assert 0 <= tail.lo <= tail.hi < SCALE
    assert tail_factor.enc() == I((1-tail).square().lo,
                                  (I(1)/(1-tail).square()).hi, True).enc()
    initial = {}
    for record in root['cells']:
        indices = (*record['prime_cells'], record['selector_cell'])
        counts = (4, 4, 4, 512)
        assert all(0 <= a < n for a, n in zip(indices, counts, strict=True))
        key = tuple(v for a, n in zip(indices, counts, strict=True) for v in (a, n))
        assert key not in initial
        initial[key] = decode(record['range'])
    assert len(initial) == 32768 and sum(map(mass, initial)) == 1
    root_lo = sum(mass(k)*v.lo for k, v in initial.items())
    root_hi = sum(mass(k)*v.hi for k, v in initial.items())
    outer = decode(root['integral'])
    assert outer.lo <= root_lo <= root_hi <= outer.hi
    assert encoded(root_lo, root_hi) == source['initial_exact_aggregate']
    replay_splits(initial, source['splits'])
    leaves = {}
    for record in source['leaves']:
        key = tuple(record['key'])
        assert key not in leaves and F(record['mass']) == mass(key)
        leaves[key] = decode(record['range'])
    assert len(leaves) == source['leaf_count'] == 65536
    assert len(source['splits']) == source['split_count'] == 32768
    assert set(initial) == set(leaves)
    assert all(initial[k].enc() == v.enc() for k, v in leaves.items())
    sum_lo, sum_hi = check_sums(leaves, source['integral'])
    initial_lo, initial_hi = sum_lo, sum_hi
    initial_width = sum_hi-sum_lo
    assert str(initial_width/SCALE) == source['width']
    # Keep only the starting leaves for independent replay after refinement.
    del root, source['splits'], source['leaves']
    response_cache = {}
    for record in source['response_cells']:
        key = tuple(record['key'])
        assert key not in response_cache
        response_cache[key] = decode(record['W']), decode(record['g'])
    selector_cache = {}
    for record in source['selector_cells']:
        key = tuple(record['key'])
        assert key not in selector_cache
        vectors = record['P_times_u']
        selector_cache[key] = (None if vectors is None else
                               [[decode(v) for v in vector] for vector in vectors],
                               record['reason'])

    @lru_cache(None)
    def prime_factor(axis, index, count):
        p = (2, 3, 5)[axis]
        angle = I((base.PI*I(F(index, count))).lo,
                  (base.PI*I(F(index+1, count))).hi, True)
        q = I(1)/(p*p*I(p).sqrt())
        return I(1)/(1-2*q*base.trig(angle, True)+q.square())

    def response(key):
        if key not in response_cache:
            w = tail_factor
            for axis in range(3):
                w = w*prime_factor(axis, *key[2*axis:2*axis+2])
            gv = g(w)
            assert gv.lo > 0
            response_cache[key] = w, gv
        return response_cache[key]

    def select(key):
        if key not in selector_cache:
            selector_cache[key] = base.selector(*key)
        return selector_cache[key]

    evaluations = 0

    def evaluate(key, parent):
        nonlocal evaluations
        evaluations += 1
        _, gv = response(key[:6])
        vectors, _ = select(key[6:])
        bound = (1+(3*gv/80).sqrt())/2
        fallback = I(-bound.hi, bound.hi, True)
        value = fallback if vectors is None else sum(
            (base.q_range(gv, v).intersect(fallback) for v in vectors), I(0))/3
        return value.intersect(parent)

    queue = [(-mass(k)*(v.hi-v.lo), k) for k, v in leaves.items()]
    heapq.heapify(queue)
    splits, checkpoints = [], []
    axis_counts = [0]*4
    while len(leaves) < LEAF_CAP and evaluations+8 <= EVALUATION_CAP:
        _, key = heapq.heappop(queue)
        parent = leaves.pop(key)
        m = mass(key)
        choices = []
        for axis in range(4):
            keys = children(key, axis)
            values = [evaluate(child, parent) for child in keys]
            choices.append((sum(v.hi-v.lo for v in values), -axis, keys, values))
        _, neg_axis, keys, values = min(choices, key=lambda v: v[:2])
        axis = -neg_axis
        assert sum(map(mass, keys)) == m
        assert all(v.lo >= parent.lo and v.hi <= parent.hi for v in values)
        sum_lo += m*(F(values[0].lo+values[1].lo, 2)-parent.lo)
        sum_hi += m*(F(values[0].hi+values[1].hi, 2)-parent.hi)
        for child, value in zip(keys, values, strict=True):
            assert child not in leaves
            leaves[child] = value
            heapq.heappush(queue, (-mass(child)*(value.hi-value.lo), child))
        splits.append({'parent': key, 'axis': axis, 'parent_range': parent.enc(),
                       'child_ranges': [v.enc() for v in values]})
        axis_counts[axis] += 1
        if len(splits) % 8192 == 0:
            checkpoint = {'leaves': len(leaves), 'evaluations': evaluations,
                          'integral': encoded(sum_lo, sum_hi)}
            checkpoints.append(checkpoint)
            print('Checkpoint:', checkpoint, flush=True)

    replay_splits(initial, splits)
    assert set(initial) == set(leaves)
    assert all(initial[k].enc() == v.enc() for k, v in leaves.items())
    assert check_sums(leaves, encoded(sum_lo, sum_hi)) == (sum_lo, sum_hi)
    strict_lo = strict_hi = unresolved_lo = unresolved_hi = F(0)
    unresolved_mass = F(0)
    for key, value in leaves.items():
        if select(key[6:])[0] is None:
            unresolved_mass += mass(key)
            unresolved_lo += mass(key)*value.lo
            unresolved_hi += mass(key)*value.hi
        else:
            strict_lo += mass(key)*value.lo
            strict_hi += mass(key)*value.hi
    assert strict_lo+unresolved_lo == sum_lo and strict_hi+unresolved_hi == sum_hi
    zero_excluded = sum_lo > 0 or sum_hi < 0
    material = 4*(sum_hi-sum_lo) <= 3*initial_width
    failures = []
    if not zero_excluded:
        failures.append('Final enclosure contains zero; sign/nonvanishing unproved.')
    if not material:
        failures.append('Final width exceeds 3/4 of the saved step-189 width; stop direct adaptive refinement.')
    out = {
        'status': 'UNVERIFIED_NONZERO_CANDIDATE' if zero_excluded else 'RIGOROUS_RANGE_ENCLOSURE_CONTAINS_ZERO',
        'target': source['target'], 'method': 'Resume dyadic direct range integration with parent intersections',
        'implementation_contract': source['implementation_contract'],
        'input_certificate': source_path.name, 'input_sha256': hashlib.sha256(source_bytes).hexdigest(),
        'root_certificate': root_path.name, 'root_sha256': hashlib.sha256(root_bytes).hexdigest(),
        'leaf_cap': LEAF_CAP, 'evaluation_cap': EVALUATION_CAP,
        'leaf_count': len(leaves), 'candidate_child_evaluations': evaluations,
        'split_count': len(splits), 'axis_split_counts': axis_counts,
        'coefficients': coefficients, 'full_log_tail': tail.enc(),
        'full_squared_modulus_tail_factor': tail_factor.enc(),
        'initial_exact_aggregate': encoded(initial_lo, initial_hi),
        'integral': encoded(sum_lo, sum_hi), 'width': str((sum_hi-sum_lo)/SCALE),
        'width_ratio_to_initial': str((sum_hi-sum_lo)/initial_width),
        'material_threshold_ratio': '3/4', 'material_narrowing': material,
        'zero_excluded': zero_excluded,
        'strict_contribution': encoded(strict_lo, strict_hi),
        'unresolved_contribution': encoded(unresolved_lo, unresolved_hi),
        'unresolved_product_mass': str(unresolved_mass), 'checkpoints': checkpoints,
        'checks': {'source_partition_replayed_from_root': True,
                   'source_exact_aggregate_checked': True, 'source_coefficients_unchanged': True,
                   'full_tail_unchanged': True, 'new_split_tree_replayed': True,
                   'complete_mass_one': True, 'all_leaf_ranges_ordered_and_nested': True,
                   'exact_final_sums_checked': True,
                   'within_caps': len(leaves) <= LEAF_CAP and evaluations <= EVALUATION_CAP},
        'failures': failures, 'splits': splits,
        'response_cells': [{'key': k, 'W': w.enc(), 'g': gv.enc()} for k, (w, gv) in sorted(response_cache.items())],
        'selector_cells': [{'key': k, 'reason': reason,
                            'P_times_u': None if vectors is None else [[v.enc() for v in vector] for vector in vectors]}
                           for k, (vectors, reason) in sorted(selector_cache.items())],
        'leaves': [{'key': k, 'mass': str(mass(k)), 'range': v.enc()} for k, v in sorted(leaves.items())],
    }
    path = directory/'bulk-haar-resumed-enclosure-190.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Actual / required I:', out['integral'], 'required lower>0 or upper<0.')
    print('Width / saved-width ratio / required:', out['width'], out['width_ratio_to_initial'], '<=3/4')
    print('Caps / actual:', LEAF_CAP, len(leaves), EVALUATION_CAP, evaluations)
    print('Splits:', axis_counts, 'Unresolved mass:', unresolved_mass)
    print('Checks:', out['checks'], 'Failures:', failures)
    print('Certificate:', path)


if __name__ == '__main__':
    main()
