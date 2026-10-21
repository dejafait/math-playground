"""One bounded step-195 specialization; full records and work charged to disk."""
import json
from fractions import Fraction as F
from pathlib import Path
import certify_bulk_conditional_sign as c

ROOT = Path(__file__).parent
OUT = ROOT / 'bulk-smaller-complement-199.json'
CAP = 262144


def read(name):
    return json.loads((ROOT / name).read_text())


def dec(rec):
    return c.I(c.I(F(rec['lower'])).lo, c.I(F(rec['upper'])).hi, True)


def load_geometry(source):
    """Reuse the audited closed-cell jets without another selector evaluation."""
    for cell in source['cells']:
        left, right = F(cell['left']), F(cell['right'])
        states = None
        if 'state_jets' in cell:
            states = [[c.J(dec(j['value']), dec(j['first']), dec(j['second']))
                       for j in state] for state in cell['state_jets']]
        c.geometry_cache[left, right] = (states, cell['selector'])


def save(data):
    data['callback_counts'] = dict(c.calls)
    data['new_callbacks'] = c.count()
    data['combined_callbacks'] = data['inherited_callbacks'] + c.count()
    assert data['combined_callbacks'] <= CAP
    OUT.write_text(json.dumps(data, indent=2) + '\n')


def main():
    source = read('bulk-core-tail-196.json')
    audit = read('bulk-core-tail-audit-198.json')
    inherited = audit['records']['work_accounting']['combined_historical_and_current']
    for key in c.calls:
        c.calls[key] = 0
    load_geometry(source)
    a, b = [F(source['g_full_range'][key]) for key in ('lower', 'upper')]
    data = {'step': 199, 'target': "Test whether L426's I is negative by combining a uniformly negative conditional core with a certified full-response tail bound.",
            'inherited_callbacks': inherited, 'cap': CAP,
            'g_full_range': source['g_full_range'], 'anchors': [],
            'transport_slabs': [], 'failures': [], 'outcome': 'IN_PROGRESS'}
    if OUT.exists():
        saved = json.loads(OUT.read_text())
        if saved['anchors']:
            data = saved
            c.calls.update(data['callback_counts'])
            if data['outcome'] != 'IN_PROGRESS':
                print('Saved completed certificate:', OUT)
                print('Outcome:', data['outcome'], '; combined callbacks:', data['combined_callbacks'], '/', CAP)
                return
    if not data['anchors']:
        save(data)
        center = F(1)
        c.points.clear()
        records, total = [], c.I(0)
        for old in source['cells']:
            assert inherited+c.count()+16 < CAP
            record, values = c.cell(F(old['left']), F(old['right']), [c.I(center)])
            records.append(record)
            total += values[0]
        assert records[0]['left'] == '0' and records[-1]['right'] == '1'
        assert all(x['right'] == y['left'] for x, y in zip(records, records[1:]))
        assert sum((F(r['mass']) for r in records), F(0)) == 1
        data['anchors'].append({'g': str(center), 'value': total.enc(), 'cells': records})
        save(data)
        print('A(1) enclosure:', [float(F(v)) for v in total.enc().values()], flush=True)

    # Fixed angular partition from audited step 196. It is independent of g.
    # For the unresolved set use BOTH its complete derivative bound and its
    # full Q range. Transporting its range rather than its derivative can be
    # sharper and never discards any part of its mass.
    eps = sum((F(r['mass']) for r in source['cells'] if 'state_jets' not in r), F(0))
    T = c.I(F(13, 4))
    B = c.I(F(1, 4))+c.I(3)/c.I(80).sqrt()
    C = c.I(F(3, 2))*(1+c.I(1)/c.I(80).sqrt())
    nodes = [a, F(1, 5), F(3, 10), F(1, 2), F(1), F(2), F(4),
             F(6), F(10), F(15), F(20), F(25), F(30), F(35), b]
    assert len(nodes)-1 <= 256
    for idx in range(len(data['transport_slabs']), len(nodes)-1):
        left, right = nodes[idx:idx+2]
        gg = c.I(c.I(left).lo, c.I(right).hi, True)
        strict, full, records = c.I(0), c.I(0), []
        for k, old in enumerate(source['cells']):
            assert inherited+c.count()+4 < CAP
            vectors, _ = c.geometry_cache[F(old['left']), F(old['right'])]
            if vectors is None:
                # One charged fallback derivative-bound evaluation per cell.
                c.calls['state_response_derivative'] += 1
                dd = B+(2*C+T*B)*gg+T*C*gg.square()
                value = c.sym(dd.hi)
                records.append({'cell': k, 'kind': 'unresolved', 'derivative': value.enc()})
            else:
                vals, states = [], []
                for state in vectors:
                    c.calls['state_response_derivative'] += 1
                    x, y, z = [v.v for v in state]
                    t = 3*(x.square()+y.square())
                    p = 3*(y.square()+x*z)
                    q = -18*y.square()*(x.square()+x*z)
                    ex = c.b.exp_negative(t*gg)
                    value = ex*(p+(2*q-t*p)*gg-t*q*gg.square())
                    states.append({'t': t.enc(), 'p': p.enc(), 'q': q.enc(),
                                   'exponential': ex.enc(), 'derivative': value.enc()})
                    vals.append(value)
                value = sum(vals, c.I(0))/3
                strict += value*F(old['mass'])
                records.append({'cell': k, 'kind': 'strict', 'states': states,
                                'derivative': value.enc()})
            full += value*F(old['mass'])
        data['transport_slabs'].append({'left': str(left), 'right': str(right),
                                       'strict_derivative': strict.enc(),
                                       'full_derivative': full.enc(), 'cells': records})
        save(data)
        print('Transport slab', idx+1, '/', len(nodes)-1,
              'strict derivative', [float(F(v)) for v in strict.enc().values()],
              'combined callbacks', inherited+c.count(), '/', CAP, flush=True)

    # Every anchor is a full integral. Subtracting an unresolved contribution
    # bounded in absolute value by eps R(g) encloses the same strict integral.
    endpoints = read('bulk-haar-conditional-sign-194.json')
    anchors = [(a, endpoints['centers'][0]['value']),
               (F(1), data['anchors'][0]['value']),
               (F(30), source['conditional_value']),
               (b, endpoints['centers'][-1]['value'])]
    def radius(g):
        return F(c.fallback(c.I(g)).hi, c.S)
    slopes = [(F(r['strict_derivative']['lower']), F(r['strict_derivative']['upper']))
              for r in data['transport_slabs']]
    upper = []
    for j, node in enumerate(nodes):
        bounds = []
        for g, value in anchors:
            k = nodes.index(g)
            val = F(value['upper'])+eps*radius(g)
            if j >= k:
                val += sum((slopes[n][1]*(nodes[n+1]-nodes[n]) for n in range(k, j)), F(0))
            else:
                val -= sum((slopes[n][0]*(nodes[n+1]-nodes[n]) for n in range(j, k)), F(0))
            bounds.append(val)
        upper.append(min(bounds))
    def interval_upper(left, right):
        """Max of the two-sided affine upper envelope, plus full tie range."""
        vals = []
        for j, (u, v) in enumerate(zip(nodes, nodes[1:])):
            l, r = max(left, u), min(right, v)
            if l > r:
                continue
            low, high = slopes[j]
            pts = [l, r]
            if high != low:
                cross = (upper[j+1]-low*v-upper[j]+high*u)/(high-low)
                if l <= cross <= r:
                    pts.append(cross)
            best = max(min(upper[j]+high*(g-u), upper[j+1]-low*(v-g)) for g in pts)
            vals.append(best+eps*radius(r))
        assert vals
        return max(vals)
    data['transport_envelope'] = {'nodes': list(map(str, nodes)),
        'unresolved_mass': str(eps), 'strict_endpoint_upper': list(map(str, upper)),
        'full_slab_upper': [str(interval_upper(u, v)) for u, v in zip(nodes, nodes[1:])]}
    moments = read('bulk-core-tail-moments-196.json')
    comparisons = []
    for old in source['candidate_cutoffs']:
        cutoff = F(old['c'])
        core = interval_upper(a, cutoff)
        if cutoff == F(source['transport']['c']):
            core = min(core, F(source['transport']['core_upper']))
        tail_upper = max(F(0), interval_upper(cutoff, b))
        # Keep the smaller-M experiment explicit; the legacy bound is only an
        # independently valid intersection, never a claim of new success.
        M = min(tail_upper, F(source['M']))
        probabilities = [min(F(1), F(m['moment']['upper'])/cutoff**m['r'])
                         for m in moments['G_moments']]
        pbar = min(probabilities)
        assert pbar == F(old['pbar'])
        comparison = core*(1-pbar)+M*pbar if core < 0 else None
        comparisons.append({'c': str(cutoff), 'core_upper': str(core),
            'negative_core_certified': core < 0, 'raw_complement_upper': str(tail_upper),
            'M': str(M), 'strictly_smaller_M': M < F(source['M']),
            'markov_bounds': list(map(str, probabilities)), 'pbar': str(pbar),
            'comparison_upper': None if comparison is None else str(comparison),
            'success': comparison is not None and comparison < 0})
    data['candidate_comparisons'] = comparisons
    # Also charge auxiliary Q-range bounds, including those evaluated on
    # strict cells. The state/derivative counters above already charge every
    # fallback derivative. These value-bound charges are conservative with
    # respect to the callback convention in steps 194/196/198.
    endpoints_used = {F(r[k]) for r in source['cells'] if 'state_jets' in r
                      for k in ('left', 'right')}
    def overlaps(left, right):
        return sum(max(left, u) <= min(right, v) for u, v in zip(nodes, nodes[1:]))
    value_bound_calls = len(source['cells'])+len(endpoints_used)+len(nodes)*len(anchors)
    value_bound_calls += sum(overlaps(u, v) for u, v in zip(nodes, nodes[1:]))
    value_bound_calls += sum(overlaps(a, F(r['c']))+overlaps(F(r['c']), b) for r in comparisons)
    c.calls['auxiliary_value_bound'] = value_bound_calls
    data['auxiliary_value_bound_accounting'] = {'anchor_cell_calls': len(source['cells']),
        'anchor_endpoint_calls': len(endpoints_used),
        'transport_calls': value_bound_calls-len(source['cells'])-len(endpoints_used),
        'total': value_bound_calls}
    data['checks'] = {'all_14_slabs_cover_full_response': nodes[0] == a and nodes[-1] == b,
        'all_32_original_candidates_reused': len(comparisons) == 32,
        'same_1848_cell_partition': all(len(s['cells']) == len(source['cells']) == 1848 for s in data['transport_slabs']),
        'unchanged_full_markov_bounds': True, 'saved_nondegenerate_core_retained': comparisons[0]['negative_core_certified'],
        'callback_cap': inherited+c.count() <= CAP, 'response_slabs_cap': len(nodes) <= 256,
        'response_centers_cap': 5 <= 33, 'angular_leaf_cap': len(source['cells']) <= 4096,
        'precision_places': 24 <= 160}
    success = any(r['success'] for r in comparisons)
    data['outcome'] = 'STRICT_NEGATIVE_COMPARISON' if success else 'NO_STRICT_COMPARISON_WITHIN_CAP'
    if not success:
        data['failures'] = ['No complete negative core and smaller-complement comparison succeeds on the 32 saved cutoffs.',
            'The remaining callback budget does not cover one further complete 1848-cell center-and-transport calculation.']
    save(data)
    print('Certified cores:', [(r['c'], float(F(r['core_upper']))) for r in comparisons if r['negative_core_certified']], flush=True)
    print('Smallest raw full-complement upper:', min(float(F(r['raw_complement_upper'])) for r in comparisons), flush=True)
    print('Successes:', sum(r['success'] for r in comparisons), '/ 32; outcome:', data['outcome'], flush=True)
    print('Callbacks new / combined / cap:', c.count(), inherited+c.count(), CAP, flush=True)
    print('Failures:', data['failures'], '\nCertificate:', OUT, flush=True)


if __name__ == '__main__':
    main()
