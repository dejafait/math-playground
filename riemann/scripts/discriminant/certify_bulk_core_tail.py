"""Step 196: one capped core/tail test with the approved global M option.

Complete finite partition and transport evidence is saved, never sampled.
"""
import heapq
import json
from fractions import Fraction as F
from pathlib import Path
import certify_bulk_conditional_sign as c


def main():
    p = Path(__file__).parent
    source = json.loads((p/'bulk-haar-conditional-sign-194.json').read_text())
    previous = json.loads((p/'bulk-core-tail-preliminary-196.json').read_text())
    failed = json.loads((p/'bulk-core-tail-failed-196.json').read_text())
    for k in c.calls:
        c.calls[k] = 0
    c.calls['failed_execution_callbacks'] = failed['state_response_derivative_callbacks']
    c.calls['state_response_derivative'] = previous['state_response_derivative_callbacks']
    a, b = [F(source['g_full_range'][k]) for k in ('lower', 'upper')]
    point = F(30)
    gs = [c.I(point)]
    leaves, heap, serial = {}, [], 0
    def add(left, right):
        nonlocal serial
        record, vals = c.cell(left, right, gs)
        leaves[serial] = (record, vals[0])
        heapq.heappush(heap, (-(vals[0].hi-vals[0].lo), serial))
        serial += 1
    for r in source['cells']:
        add(F(r['left']), F(r['right']))
    def aggregate():
        return c.I(sum(v.lo for _, v in leaves.values()),
                   sum(v.hi for _, v in leaves.values()), True)
    result = aggregate()
    # A positive value rules out any negative core reaching this point.
    while result.lo <= 0 and len(leaves) < 4096 and c.count()+64 <= 65536:
        _, idx = heapq.heappop(heap)
        r, _ = leaves.pop(idx)
        left, right = F(r['left']), F(r['right'])
        mid = (left+right)/2
        add(left, mid)
        add(mid, right)
        result = aggregate()
    records = sorted((r for r, _ in leaves.values()), key=lambda r: F(r['left']))
    assert records[0]['left'] == '0' and records[-1]['right'] == '1'
    assert all(x['right'] == y['left'] for x, y in zip(records, records[1:]))
    assert sum((F(r['mass']) for r in records), F(0)) == 1
    # Global entire-g derivative bound from L426 (18), retaining exp(-tg)<=1.
    T = c.I(F(13, 4))
    B = c.I(F(1, 4))+c.I(3)/c.I(80).sqrt()
    C = c.I(F(3, 2))*(1+c.I(1)/c.I(80).sqrt())
    h = F(1, 100000)
    end = a+h
    d = B+(2*C+T*B)*end+T*C*end**2
    c.calls['state_response_derivative'] += 1  # one universal bound evaluation
    old = source['centers'][0]['value']
    anchor_upper = F(old['upper'])
    derivative_bound = F(d.hi, c.S)
    core_upper = anchor_upper+derivative_bound*h
    assert core_upper < 0
    delta = -core_upper
    M = F(c.fallback(c.I(b)).hi, c.S)
    # Exactly one core transport slab [a,a+h].
    transport = {'a': str(a), 'c': str(end), 'anchor': old,
                 'sup_abs_derivative': str(derivative_bound),
                 'core_upper': str(core_upper), 'delta': str(delta)}
    moments = json.loads((p/'bulk-core-tail-moments-196.json').read_text())
    # 32 fixed rational candidates, all within the enclosing interval.
    cutoffs = [end]+[F(j) for j in range(1, 31)]+[(F(30)+b)/2]
    assert len(cutoffs) == 32 and all(a < x < b for x in cutoffs)
    candidates = []
    for x in cutoffs:
        bounds = [min(F(1), F(m['moment']['upper'])/x**m['r']) for m in moments['G_moments']]
        prob = min(bounds)
        upper = -delta*(1-prob)+M*prob if x == end else None
        candidates.append({'c': str(x), 'markov_bounds': list(map(str, bounds)),
                           'pbar': str(prob), 'negative_core_certified': x == end,
                           'comparison_upper': None if upper is None else str(upper),
                           'strict_negative_comparison': upper is not None and upper < 0})
    # Optimistic obstruction for this GLOBAL-M implementation, not for smaller M.
    # A(a)>=l implies every eligible delta<=-l. If A(30)>0, c<30.
    delta_max = -F(old['lower'])
    floor = min(F(1), *[F(m['moment']['upper'])/point**m['r'] for m in moments['G_moments']])
    optimistic = -delta_max*(1-floor)+M*floor
    obstruction = result.lo > 0 and optimistic > 0
    out = {'step': 196, 'target': "L426 fixed I, global-complement M core/tail specialization",
           'g_full_range': source['g_full_range'], 'conditional_point': str(point),
           'conditional_value': result.enc(), 'cells': records, 'transport': transport,
           'M': str(M), 'candidate_cutoffs': candidates,
           'global_M_obstruction': {'positive_conditional_point': result.lo > 0,
               'delta_upper_for_any_negative_core': str(delta_max),
               'computed_pbar_lower_for_c_below_point': str(floor),
               'optimistic_comparison_lower': str(optimistic), 'certified': obstruction},
           'callback_counts': c.calls, 'callback_total': c.count(),
           'centers': [str(a), str(point)], 'transport_slabs': 1,
           'checks': {'partition': True, 'nondegenerate_core_before_feasibility_cap': c.count() <= 65536,
               'core_strict_negative': core_upper < 0, 'all_full_positive_moments_retained': True,
               'total_callback_cap': c.count() <= 262144, 'leaf_cap': len(records) <= 4096,
               'cutoff_cap': len(candidates) <= 32, 'centers_and_slabs_caps': True},
           'outcome': 'GLOBAL_M_IMPLEMENTATION_RULED_OUT' if obstruction else 'INCONCLUSIVE',
           'failures': ['The approved global M cannot yield a negative comparison.' if obstruction else
                        'No strict negative comparison; the conditional point or comparison obstruction is unresolved.']}
    path = p/'bulk-core-tail-196.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print('A(30):', [float(F(result.enc()[k])) for k in ('lower', 'upper')])
    print('Core [a,c], delta, global M:', float(a), float(end), float(delta), float(M))
    print('Optimistic pbar floor / comparison lower:', float(floor), float(optimistic))
    print('Callbacks actual / feasibility / total caps:', c.count(), 65536, 262144)
    print('Leaves actual / cap:', len(records), 4096)
    print('Outcome:', out['outcome'], '; failures:', out['failures'])
    print('Certificate:', path)


if __name__ == '__main__':
    main()
