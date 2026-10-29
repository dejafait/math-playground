"""Independent full receiver of step 475; no filter/emitter/constructor imports.

Checks path support by Boolean transitive closure, complete occurrence maps,
backward free-word arithmetic, old event values, provenance and exact ledger.
"""
from collections import Counter
from pathlib import Path
import hashlib
from parameterized_input import (CAPS, load, request, symbol_map, require,
                                exact_equal, write_json, bound)
from receive_parameterized import Arithmetic, topo
from verify_constant_translation import typed, normalized, nested_schedule

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = HERE / 'output-473'
OUT = HERE / 'output-475'


def serial(poly):
    return [[list(symbol) for symbol in word]
            for word in sorted(poly, key=lambda w: (len(w), w))]


def counts(f, g):
    p = len(f['edges']) * len(g['edges'])
    a, b = (Counter(x for _, _, lab in h['edges'] for x in lab if x != '1')
            for h in (f, g))
    q = sum(a.values())*sum(b.values()) - sum(v*b[x] for x, v in a.items())
    nv = 2 + 2*p*(f['vertices'] + g['vertices'])
    ne = 2*p*(len(f['edges']) + len(g['edges'])) + 4*p + q
    return dict(p=p, q=q, vertices=nv, edges=ne, actual=nv+ne,
                required=CAPS['records'], fits=nv+ne <= CAPS['records'])


def main():
    path = OUT / 'reception.json'
    require(not path.exists(), 'refuse existing step-475 reception')
    receipt = dict(accepted=False, failures=[], scope='finite operand replacement only')
    try:
        cert = load(OUT / 'trimmed-pair.json')
        req, raw, rows, checked = request(OLD / 'inputs/proof.jsonl', OLD / 'inputs/request.json')
        transport = symbol_map(req['alphabet'], req['dictionary'])
        ar = Arithmetic(req)
        require(exact_equal(cert['caps'], CAPS), 'unchanged caps')
        require(exact_equal(cert['alphabet'], req['alphabet']) and
                exact_equal(cert['dictionary'], req['dictionary']), 'complete names/dictionary')
        require(len(rows) == 31 and cert['original_source_roots'] == list(range(1, 32)),
                'unchanged caller source-root table')
        event = load(OLD / 'trace/event-00201.json')
        frame = load(OLD / 'failure-frame-7.json')
        stop = load(OLD / 'stop-check.json')
        parent = load(OLD / 'trace/event-00196.json')
        require(event['parent'] == 196 and parent['kind'] == 'boolean-input', 'parent binding')
        h = normalized(parent['graph'])
        jobs = nested_schedule(h)
        for j, i in enumerate((197, 199, 201)):
            actual = load(OLD / ('trace/event-%05d.json' % i))
            require(actual['parent'] == 196 and
                    exact_equal([actual['f'], actual['g']], list(jobs[j])),
                    'exact ordered L036 nested recipe')
        old_receipt = load(OLD / 'trace-received-prefix.json')['events'][201]
        require(old_receipt['index'] == 201 and old_receipt['parent'] == 196,
                'full prior polynomial receipt binding')

        def evaluate(g):
            require(all(a == '1' or a in {'x'+str(i+1) for i in range(len(req['alphabet']))}
                        for _, _, lab in g['edges'] for a in lab), 'original-only labels')
            z = typed(g, transport)
            order = topo(z['vertices'], z['edges'], req)
            require(all(type(z[k]) is int and 0 <= z[k] < z['vertices']
                        for k in ('source', 'sink')), 'designated endpoints')
            return ar.evaluate(z['vertices'], z['edges'], order, z['source'], z['sink'], 'free')

        def receive_item(item):
            g, z = item['original'], item['trimmed']
            a, b = evaluate(g), evaluate(z)
            n, s, t = g['vertices'], g['source'], g['sink']
            # Independent all-pairs closure, including length-zero reachability.
            reach = [[i == j for j in range(n)] for i in range(n)]
            for u, v, _ in g['edges']:
                reach[u][v] = True
            for k in range(n):
                for u in range(n):
                    if reach[u][k]:
                        for v in range(n):
                            reach[u][v] = reach[u][v] or reach[k][v]
            live = [u for u in range(n) if reach[s][u] and reach[u][t]]
            indices = [i for i, (u, v, _) in enumerate(g['edges'])
                       if reach[s][u] and reach[v][t]]
            retained = live if reach[s][t] else sorted({s, t})
            mapping = [retained.index(v) if v in retained else None for v in range(n)]
            require(exact_equal(item['old_to_new'], mapping) and
                    exact_equal(item['new_to_old'], retained) and
                    exact_equal(item['retained_edge_indices'], indices) and
                    item['no_path'] is (not reach[s][t]), 'complete occurrence/root maps')
            expected = dict(vertices=len(retained), source=mapping[s], sink=mapping[t],
                            edges=[[mapping[g['edges'][i][0]], mapping[g['edges'][i][1]],
                                    g['edges'][i][2]] for i in indices])
            require(exact_equal(z, expected), 'exact retained labels/order/multiplicities')
            require(a == b, 'complete ordered-polynomial preservation')
            if s == t:
                require(z['vertices'] == 1 and not z['edges'] and b == {()}, 'empty path')
            if not reach[s][t]:
                require(not z['edges'] and not b, 'no-path zero graph')
            return dict(accepted=True, original_records=n+len(g['edges']),
                        trimmed_records=z['vertices']+len(z['edges']),
                        original_polynomial=serial(a), trimmed_polynomial=serial(b),
                        original_vertices=n, original_edges=len(g['edges']),
                        trimmed_vertices=z['vertices'], trimmed_edges=len(z['edges']),
                        structural_path_map_verified=True), a

        evidence, polys = {}, []
        for j, k in enumerate(('f', 'g')):
            item = cert['operands'][k]
            require(exact_equal(item['original'], event[k]) and
                    exact_equal(event[k], frame[k]), 'all original operand records')
            evidence[k], value = receive_item(item)
            require(exact_equal(serial(value), old_receipt['operands'][j]),
                    'full event-201 polynomial comparison')
            polys.append(value)
        fixtures = {k: receive_item(x)[0] for k, x in cert['fixtures'].items()}
        require(set(fixtures) == {'nonextremal-ordered-parallel-zero',
                'interior-coincident-empty-path', 'no-path-distinct-roots',
                'edgeless-coincident', 'constant-parallel-cancellation',
                'affine-duplicate-labels'}, 'boundary fixture coverage')
        original = counts(event['f'], event['g'])
        trimmed = counts(*(cert['operands'][k]['trimmed'] for k in ('f', 'g')))
        require(exact_equal(original, cert['original_ledger']) and
                exact_equal(trimmed, cert['trimmed_ledger']), 'independent exact L035 ledger')
        require(all(original[k] == frame[k] == stop['ledger'][k]
                    for k in ('p', 'q', 'vertices', 'edges') if k in frame), 'failure ledger binding')
        require(original['vertices'] == frame['nv'] and original['edges'] == frame['ne'] and
                original['actual'] == stop['ledger']['actual'] == 10_500_818,
                'complete original stop ledger')
        bound(trimmed['actual'], 'records', 'unchanged L035 preflight on filtered operands')
        # This target concerns operands, not the zero commutator alone.
        commutator = ar.add(ar.mul(polys[0], polys[1]), ar.mul(polys[1], polys[0]))
        require(exact_equal(serial(commutator), old_receipt['target']), 'prior target corroboration')
        manifest = load(OLD / 'inputs/manifest.json')
        for k in ('source', 'annotations', 'pair', 'proof', 'request'):
            filename = k + ('.jsonl' if k == 'proof' else '.json')
            origin = HERE / ('output-470' if k in ('proof', 'request') else
                             'output-461/final/empty-clause') / filename
            copied = (OLD / 'inputs' / filename).read_bytes()
            require(copied == origin.read_bytes() and
                    hashlib.sha256(copied).hexdigest() == manifest[k], 'exact caller bytes')
        for p, digest in cert['input_hashes'].items():
            require(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == digest,
                    'preserved bytes: ' + p)
        require(not (OUT / 'K.json').exists() and not (OUT / 'H.json').exists(), 'no integration')
        receipt.update(accepted=True, operands=evidence, fixtures=fixtures,
                       original_ledger=original, trimmed_ledger=trimmed,
                       arithmetic=ar.counts, caps=CAPS, full_event_201_match=True,
                       parent_196_recipe_match=True, caller_bytes_preserved=True,
                       checked_source=checked, complete_KH_received=False,
                       input_hashes=cert['input_hashes'])
    except Exception as exc:
        receipt['failures'].append(repr(exc))
        write_json(path, receipt)
        raise
    write_json(path, receipt)
    print(dict(accepted=receipt['accepted'], actual=trimmed['actual'],
               required=CAPS['records'], operands={k: dict(
                   records=v['trimmed_records'], words=len(v['trimmed_polynomial']))
                   for k, v in evidence.items()}, failures=receipt['failures'], path=str(path)))


if __name__ == '__main__':
    main()
