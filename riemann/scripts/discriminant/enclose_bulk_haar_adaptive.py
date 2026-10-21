"""One capped adaptive refinement of the complete step-188 certificate.

Proof arithmetic is imported from enclose_bulk_haar_integral: integers,
Fraction and isqrt only. Every retained leaf and chosen split is saved.
The old certificate is read and completely checked, never overwritten.
"""
import hashlib
import heapq
import json
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

import enclose_bulk_haar_integral as base

I, SCALE = base.I, base.SCALE
LEAF_CAP = 65536
EVALUATION_CAP = 262144
INITIAL_COUNTS = (4, 4, 4, 512)


def decode(record):
    lo, hi = F(record['lower']), F(record['upper'])
    assert lo <= hi and (lo*SCALE).denominator == (hi*SCALE).denominator == 1
    return I(int(lo*SCALE), int(hi*SCALE), True)


def mass(key):
    denominator = 1
    for count in key[1::2]:
        denominator *= count
    return F(1, denominator)


def children(key, axis):
    result = []
    for side in (0, 1):
        child = list(key)
        child[2*axis] = 2*key[2*axis]+side
        child[2*axis+1] = 2*key[2*axis+1]
        result.append(tuple(child))
    return result


def main():
    directory = Path(__file__).parent
    source_path = directory/'bulk-haar-integral-enclosure-188.json'
    source_bytes = source_path.read_bytes()
    source = json.loads(source_bytes)
    assert all(source['checks'].values())
    assert source['cell_count'] == source['cell_cap'] == 32768
    assert source['prime_coordinates'] == [2, 3, 5]
    g, coefficients = base.source_coefficients(directory)
    assert coefficients == source['coefficients']
    tail = decode(source['full_log_tail'])
    tail_factor = decode(source['full_squared_modulus_tail_factor'])
    assert 0 <= tail.lo <= tail.hi < SCALE
    assert tail_factor.enc() == I((1-tail).square().lo,
                                  (I(1)/(1-tail).square()).hi, True).enc()

    @lru_cache(None)
    def prime_factor(axis, index, count):
        p = (2, 3, 5)[axis]
        angle = I((base.PI*I(F(index, count))).lo,
                  (base.PI*I(F(index+1, count))).hi, True)
        q = I(1)/(p*p*I(p).sqrt())
        return I(1)/(1-2*q*base.trig(angle, True)+q.square())

    response_cache = {}
    for record in source['response_cells']:
        key = tuple(x for index in record['indices'] for x in (index, 4))
        assert key not in response_cache
        response_cache[key] = (decode(record['W']), decode(record['g']))
    assert len(response_cache) == 64

    selector_cache = {}
    for record in source['selector_cells']:
        key = (record['cell'], 512)
        assert key not in selector_cache
        vectors = record['P_times_u']
        selector_cache[key] = (None if vectors is None else
                               [[decode(v) for v in vector] for vector in vectors],
                               record['reason'])
    assert set(selector_cache) == {(k, 512) for k in range(512)}

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

    leaves = {}
    initial_sum_lo = initial_sum_hi = F(0)
    for record in source['cells']:
        indices = (*record['prime_cells'], record['selector_cell'])
        assert all(0 <= index < count for index, count in zip(indices, INITIAL_COUNTS))
        key = tuple(x for index, count in zip(indices, INITIAL_COUNTS) for x in (index, count))
        assert key not in leaves
        value = decode(record['range'])
        leaves[key] = value
        initial_sum_lo += mass(key)*value.lo
        initial_sum_hi += mass(key)*value.hi
    assert len(leaves) == 32768
    initial_interval = decode(source['integral'])
    assert initial_interval.lo <= initial_sum_lo <= initial_sum_hi <= initial_interval.hi
    # Cardinality and valid distinct indices exhaust the initial Cartesian grid.
    assert sum(map(mass, leaves)) == 1
    initial_width = initial_sum_hi-initial_sum_lo
    sum_lo, sum_hi = initial_sum_lo, initial_sum_hi
    queue = [(-mass(key)*(value.hi-value.lo), key) for key, value in leaves.items()]
    heapq.heapify(queue)
    splits = []
    axis_counts = [0]*4
    checkpoints = []
    while len(leaves) < LEAF_CAP and evaluations+8 <= EVALUATION_CAP:
        _, key = heapq.heappop(queue)
        parent = leaves.pop(key)
        m = mass(key)
        choices = []
        for axis in range(4):
            keys = children(key, axis)
            values = [evaluate(child, parent) for child in keys]
            width = sum(v.hi-v.lo for v in values)
            # Prefer the selector in a tie: near a branch, several first
            # subdivisions can be required before any contraction occurs.
            choices.append((width, -axis, keys, values))
        _, neg_axis, keys, values = min(choices, key=lambda v: v[:2])
        axis = -neg_axis
        assert sum(map(mass, keys)) == m
        assert all(v.lo >= parent.lo and v.hi <= parent.hi for v in values)
        sum_lo += m*(F(values[0].lo+values[1].lo, 2)-parent.lo)
        sum_hi += m*(F(values[0].hi+values[1].hi, 2)-parent.hi)
        for child, value in zip(keys, values):
            assert child not in leaves
            leaves[child] = value
            heapq.heappush(queue, (-mass(child)*(value.hi-value.lo), child))
        splits.append({'parent': key, 'axis': axis,
                       'parent_range': parent.enc(),
                       'child_ranges': [v.enc() for v in values]})
        axis_counts[axis] += 1
        if len(splits) % 8192 == 0:
            checkpoint = {'leaves': len(leaves), 'evaluations': evaluations,
                          'integral': {'lower': str(sum_lo/SCALE), 'upper': str(sum_hi/SCALE)}}
            checkpoints.append(checkpoint)
            print('Checkpoint:', checkpoint, flush=True)

    # Independently replay every chosen split as a finite partition, starting
    # from all old cells, and verify all terminal ranges, masses and sums.
    replay = {}
    for record in source['cells']:
        indices = (*record['prime_cells'], record['selector_cell'])
        key = tuple(x for index, count in zip(indices, INITIAL_COUNTS) for x in (index, count))
        replay[key] = decode(record['range'])
    for record in splits:
        key, axis = tuple(record['parent']), record['axis']
        parent = replay.pop(key)
        assert parent.enc() == record['parent_range']
        for child, enc in zip(children(key, axis), record['child_ranges']):
            value = decode(enc)
            assert parent.lo <= value.lo <= value.hi <= parent.hi
            assert child not in replay
            replay[child] = value
    assert set(replay) == set(leaves)
    assert all(replay[k].enc() == v.enc() for k, v in leaves.items())
    assert sum(map(mass, leaves)) == 1
    assert sum(mass(k)*v.lo for k, v in leaves.items()) == sum_lo
    assert sum(mass(k)*v.hi for k, v in leaves.items()) == sum_hi
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
    def enc_fraction(lo, hi):
        return {'lower': str(lo/SCALE), 'upper': str(hi/SCALE)}
    out = {
        'status': 'UNVERIFIED_NONZERO_CANDIDATE' if zero_excluded else 'RIGOROUS_RANGE_ENCLOSURE_CONTAINS_ZERO',
        'target': source['target'], 'method': 'Adaptive dyadic direct range integration, parent intersections',
        'implementation_contract': source['implementation_contract'],
        'input_certificate': source_path.name, 'input_sha256': hashlib.sha256(source_bytes).hexdigest(),
        'leaf_cap': LEAF_CAP, 'evaluation_cap': EVALUATION_CAP,
        'leaf_count': len(leaves), 'candidate_child_evaluations': evaluations,
        'split_count': len(splits), 'axis_split_counts': axis_counts,
        'coefficients': coefficients, 'full_log_tail': tail.enc(),
        'full_squared_modulus_tail_factor': tail_factor.enc(),
        'initial_exact_aggregate': enc_fraction(initial_sum_lo, initial_sum_hi),
        'integral': enc_fraction(sum_lo, sum_hi),
        'width': str((sum_hi-sum_lo)/SCALE),
        'width_ratio_to_initial': str((sum_hi-sum_lo)/initial_width),
        'material_threshold_ratio': '3/4', 'material_narrowing': material,
        'zero_excluded': zero_excluded,
        'strict_contribution': enc_fraction(strict_lo, strict_hi),
        'unresolved_contribution': enc_fraction(unresolved_lo, unresolved_hi),
        'unresolved_product_mass': str(unresolved_mass),
        'checkpoints': checkpoints,
        'checks': {'initial_all_cells_checked': True, 'source_coefficients_unchanged': True,
                   'full_tail_unchanged': True, 'split_tree_replayed': True,
                   'complete_mass_one': True, 'all_leaf_ranges_ordered_and_nested': True,
                   'exact_final_sums_checked': True, 'within_caps': len(leaves) <= LEAF_CAP and evaluations <= EVALUATION_CAP},
        'failures': [] if zero_excluded else ['Final enclosure contains zero; sign/nonvanishing unproved.'],
        'splits': splits,
        'response_cells': [{'key': k, 'W': w.enc(), 'g': gv.enc()} for k, (w, gv) in sorted(response_cache.items())],
        'selector_cells': [{'key': k, 'reason': reason,
                            'P_times_u': None if vectors is None else [[v.enc() for v in vector] for vector in vectors]}
                           for k, (vectors, reason) in sorted(selector_cache.items())],
        'leaves': [{'key': k, 'mass': str(mass(k)), 'range': v.enc()} for k, v in sorted(leaves.items())],
    }
    path = directory/'bulk-haar-adaptive-enclosure-189.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('Actual / required I:', out['integral'], 'required lower>0 or upper<0.')
    print('Width / initial ratio / material threshold:', out['width'], out['width_ratio_to_initial'], '3/4')
    print('Caps / actual:', LEAF_CAP, len(leaves), EVALUATION_CAP, evaluations)
    print('Splits by coordinate:', axis_counts, 'Unresolved mass:', unresolved_mass)
    print('Checks:', out['checks'], 'Failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()
