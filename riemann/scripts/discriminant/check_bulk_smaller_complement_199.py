"""Complete record/aggregate consistency check, not an independent jet replay.

Reuses audited interval/jet contracts. No selector, state Q or response
derivative is re-evaluated. Every auxiliary Q-range evaluation is charged.
"""
import json
from fractions import Fraction as F
from pathlib import Path
import enclose_bulk_haar_integral as base

ROOT = Path(__file__).parent


def read(name):
    return json.loads((ROOT/name).read_text())


def iv(rec):
    return F(rec['lower']), F(rec['upper'])


def contains(outer, inner):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def total(records, field, masses):
    return tuple(sum((iv(r[field])[k]*m for r, m in zip(records, masses)), F(0)) for k in (0, 1))


def main():
    path = ROOT/'bulk-smaller-complement-199.json'
    d = read(path.name)
    src = read('bulk-core-tail-196.json')
    old = read('bulk-haar-conditional-sign-194.json')
    audit = read('bulk-core-tail-audit-198.json')
    moments = read('bulk-core-tail-moments-196.json')
    checks = {}
    cells = src['cells']
    assert cells[0]['left'] == '0' and cells[-1]['right'] == '1'
    assert all(x['right'] == y['left'] for x, y in zip(cells, cells[1:]))
    masses = [F(r['mass']) for r in cells]
    assert all(m == F(r['right'])-F(r['left']) > 0 for m, r in zip(masses, cells))
    assert sum(masses) == 1
    strict_ids = [i for i, r in enumerate(cells) if 'state_jets' in r]
    eps = sum(m for i, m in enumerate(masses) if i not in strict_ids)
    assert len(cells) == 1848 and len(strict_ids) == 1824 and eps == F(3, 65536)
    checks['complete_audited_angular_partition_retained'] = True
    anchor = d['anchors'][0]
    assert anchor['g'] == '1' and len(anchor['cells']) == len(cells)
    for r, oldr in zip(anchor['cells'], cells):
        for field in ('left', 'right', 'mass', 'selector'):
            assert r[field] == oldr[field]
        assert r.get('state_jets') == oldr.get('state_jets')
        assert len(r['values']) == 1
    vals = [r['values'][0] for r in anchor['cells']]
    sums = tuple(sum((iv(r['integral'])[k] for r in vals), F(0)) for k in (0, 1))
    assert sums == iv(anchor['value'])
    assert -F(83, 10000) < sums[0] <= sums[1] < -F(68, 10000)
    checks['all_anchor_cells_and_exact_aggregate'] = True
    nodes = list(map(F, d['transport_envelope']['nodes']))
    a, b = iv(d['g_full_range'])
    assert nodes == [a, F(1, 5), F(3, 10), F(1, 2), F(1), F(2), F(4),
                     F(6), F(10), F(15), F(20), F(25), F(30), F(35), b]
    assert len(d['transport_slabs']) == 14
    for j, slab in enumerate(d['transport_slabs']):
        assert (F(slab['left']), F(slab['right'])) == tuple(nodes[j:j+2])
        records = slab['cells']
        assert len(records) == len(cells)
        for i, rec in enumerate(records):
            assert rec['cell'] == i
            if i in strict_ids:
                assert rec['kind'] == 'strict' and len(rec['states']) == 3
                for state in rec['states']:
                    assert 0 <= iv(state['t'])[0] <= iv(state['t'])[1]
                    assert 0 <= iv(state['exponential'])[0] <= iv(state['exponential'])[1] <= 1
                mean = tuple(sum(iv(s['derivative'])[k] for s in rec['states'])/3 for k in (0, 1))
                assert contains(iv(rec['derivative']), mean)
            else:
                assert rec['kind'] == 'unresolved' and iv(rec['derivative'])[0] == -iv(rec['derivative'])[1]
        assert contains(iv(slab['full_derivative']), total(records, 'derivative', masses))
        assert contains(iv(slab['strict_derivative']), total([records[i] for i in strict_ids], 'derivative', [masses[i] for i in strict_ids]))
    checks['all_25872_slab_cell_records_and_state_averages'] = True
    # 14*1848 = 25872 cell records, with 14*1824*3 = 76608
    # individual strict-state derivatives and 336 fallback derivatives.
    checks['all_transport_slabs_full_mass'] = True
    value_calls = 0
    def radius(g):
        nonlocal value_calls
        value_calls += 1
        val = (1+(base.I(3)*g/80).sqrt())/2
        return F(val.hi, base.SCALE)
    anchors = [(a, old['centers'][0]['value']), (F(1), anchor['value']),
               (F(30), src['conditional_value']), (b, old['centers'][-1]['value'])]
    slopes = [iv(s['strict_derivative']) for s in d['transport_slabs']]
    endpoint_upper = []
    for j, node in enumerate(nodes):
        candidates = []
        for g, value in anchors:
            k = nodes.index(g)
            bound = F(value['upper'])+eps*radius(g)
            if j >= k:
                bound += sum((slopes[n][1]*(nodes[n+1]-nodes[n]) for n in range(k, j)), F(0))
            else:
                bound -= sum((slopes[n][0]*(nodes[n+1]-nodes[n]) for n in range(j, k)), F(0))
            candidates.append(bound)
        endpoint_upper.append(min(candidates))
    assert list(map(str, endpoint_upper)) == d['transport_envelope']['strict_endpoint_upper']
    def upper(left, right):
        maxima = []
        for j, (u, v) in enumerate(zip(nodes, nodes[1:])):
            l, r = max(left, u), min(right, v)
            if l > r:
                continue
            low, high = slopes[j]
            points = [l, r]
            if high != low:
                cross = (endpoint_upper[j+1]-low*v-endpoint_upper[j]+high*u)/(high-low)
                if l <= cross <= r:
                    points.append(cross)
            maxima.append(max(min(endpoint_upper[j]+high*(g-u), endpoint_upper[j+1]-low*(v-g)) for g in points)+eps*radius(r))
        return max(maxima)
    assert [str(upper(u, v)) for u, v in zip(nodes, nodes[1:])] == d['transport_envelope']['full_slab_upper']
    checks['every_two_sided_transport_bound_recomputed'] = True
    assert len(d['candidate_comparisons']) == len(src['candidate_cutoffs']) == 32
    for rec, oldrec in zip(d['candidate_comparisons'], src['candidate_cutoffs']):
        cutoff = F(rec['c'])
        assert rec['c'] == oldrec['c']
        core = upper(a, cutoff)
        if cutoff == F(src['transport']['c']):
            core = min(core, F(src['transport']['core_upper']))
        Mraw = max(F(0), upper(cutoff, b))
        M = min(Mraw, F(src['M']))
        probs = [min(F(1), F(m['moment']['upper'])/cutoff**m['r']) for m in moments['G_moments']]
        pbar = min(probs)
        comp = core*(1-pbar)+M*pbar if core < 0 else None
        assert str(core) == rec['core_upper'] and str(Mraw) == rec['raw_complement_upper']
        assert str(M) == rec['M'] and str(pbar) == rec['pbar'] == oldrec['pbar']
        assert list(map(str, probs)) == rec['markov_bounds']
        assert (core < 0) == rec['negative_core_certified']
        assert rec['comparison_upper'] == (str(comp) if comp is not None else None)
        assert not rec['success'] and (comp is None or comp >= 0)
    first = d['candidate_comparisons'][0]
    M0 = F(first['M'])
    assert F(105, 100) < M0 < F(106, 100) < F(src['M'])
    assert first['pbar'] == '1'
    assert sum(r['negative_core_certified'] for r in d['candidate_comparisons']) == 1
    assert F(d['candidate_comparisons'][1]['core_upper']) > F(5, 100)
    checks['all_32_full_comparisons_and_failure_margins'] = True
    # Reconstruct the generator's complete auxiliary bound count from its
    # finite loop structure. This adds the initial execution's previously
    # uncharged auxiliary values; no original record is discarded.
    endpoints_used = {F(r[k]) for r in cells if 'state_jets' in r for k in ('left', 'right')}
    auxiliary = len(cells)+len(endpoints_used)+value_calls
    if 'auxiliary_value_bound' not in d['callback_counts']:
        d['callback_counts']['auxiliary_value_bound'] = auxiliary
        d['new_callbacks'] += auxiliary
        d['combined_callbacks'] += auxiliary
        d['auxiliary_value_bound_accounting'] = {'anchor_cell_calls': len(cells),
            'anchor_endpoint_calls': len(endpoints_used), 'transport_calls': value_calls,
            'total': auxiliary, 'qualification': 'Charged after initial execution; includes auxiliary bounds even on strict cells.'}
        path.write_text(json.dumps(d, indent=2)+'\n')
    assert d['callback_counts']['auxiliary_value_bound'] == auxiliary
    assert d['callback_counts']['state_response_derivative'] == 14*(3*len(strict_ids)+24) == 76944
    assert d['new_callbacks'] == sum(d['callback_counts'].values())
    assert d['inherited_callbacks'] == audit['records']['work_accounting']['combined_historical_and_current'] == 166413
    combined = d['combined_callbacks']+value_calls
    assert combined <= 262144
    assert 262144-combined < 3*len(strict_ids)+24
    checks['complete_work_accounting_including_this_check'] = True
    out = {'checks': checks, 'failures': [], 'qualification': 'Complete record/aggregate consistency check under inherited contracts; not an independent interval-jet or exponential replay.',
        'generator_combined_callbacks': d['combined_callbacks'], 'check_auxiliary_value_callbacks': value_calls,
        'complete_combined_callbacks': combined, 'cap': 262144,
        'anchor_value': anchor['value'], 'retained_core_comparison': first,
        'all_core_upper_positive_at_c_ge_one': all(F(r['core_upper']) > 0 for r in d['candidate_comparisons'][1:]),
        'state_derivative_records': 14*len(strict_ids)*3, 'fallback_derivative_records': 14*24}
    output = ROOT/'bulk-smaller-complement-check-199.json'
    output.write_text(json.dumps(out, indent=2)+'\n')
    print('Consistency checks passed:', len(checks), '/', len(checks), '; failures:', out['failures'])
    print('A(1):', [float(x) for x in sums])
    print('Retained core M / pbar / comparison:', float(M0), first['pbar'], float(F(first['comparison_upper'])))
    print('Callbacks including check / cap:', combined, '/', 262144)
    print('Full-response derivative records:', out['state_derivative_records'], '+ fallback:', out['fallback_derivative_records'])
    print('Certificate:', output)


if __name__ == '__main__':
    main()
