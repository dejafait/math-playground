"""Independent step-477 two-stage trace/complete archive reception evidence.

Imports no emitter, scalar adapter, filter or correction constructor. Source
recipes are reconstructed before restriction. Full receiving arithmetic and
production acceptance contracts are unchanged.
"""
from pathlib import Path
import hashlib
from parameterized_input import (CAPS, load, require, exact_equal, write_json,
                                request, symbol_map)
from occurrence_input import context
from receive_parameterized import Arithmetic, topo
from receive_occurrence import plan, copied_composition
from verify_constant_translation import typed, normalized, nested_schedule
from verify_path_trimming import counts

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output-477'


def serial(poly):
    return [[list(symbol) for symbol in word]
            for word in sorted(poly, key=lambda w: (len(w), w))]


class MissingEvent(Exception):
    pass


class Reception:
    def __init__(self, req, kdata, hdata):
        self.req, self.kdata, self.hdata = req, kdata, hdata
        self.transport = symbol_map(req['alphabet'], req['dictionary'])
        self.ar = Arithmetic(req)
        self.index = load(OUT / 'trace/index.json')
        self.position = self.block_position = 0
        self.evidence = []
        self.pending = None
        self.statistics = dict(translations=0, booleans=0, commutators=0,
                               nested_calls=0, source_direct_calls=0,
                               occurrence_direct_calls=0, restrictions=0,
                               changed_restrictions=0, max_old_ledger=0,
                               max_new_ledger=0)

    def take(self, kind):
        if self.position == len(self.index):
            raise MissingEvent(dict(expected=kind, position=self.position,
                                    pending=self.pending))
        j = self.position
        item = self.index[j]
        require(item['index'] == j and item['file'] == 'event-%05d.json' % j,
                'complete contiguous event index')
        event = load(OUT / 'trace' / item['file'])
        require(item['kind'] == event['kind'] == kind, 'exact recipe event order')
        self.position += 1
        return j, event

    def save(self, index, kind, **values):
        require(index == len(self.evidence), 'contiguous received event evidence')
        self.evidence.append(dict(index=index, kind=kind, **values))
        write_json(OUT / 'trace-received-prefix.json', dict(
            events=self.evidence, arithmetic=self.ar.counts,
            statistics=self.statistics, caps=CAPS))

    def evaluate(self, g, modes=('free',), original=False):
        if original:
            allowed = {'1'} | {'x'+str(i+1) for i in range(len(self.req['alphabet']))}
            require(all(type(a) is str and a in allowed
                        for _, _, lab in g['edges'] for a in lab),
                    'every original recipe and actual operand original-only')
        h = typed(g, self.transport)
        order = topo(h['vertices'], h['edges'], self.req)
        require(all(type(h[k]) is int and 0 <= h[k] < h['vertices']
                    for k in ('source', 'sink')), 'transported designated endpoints')
        return {m:self.ar.evaluate(h['vertices'], h['edges'], order,
                                  h['source'], h['sink'], m) for m in modes}

    def translation(self, formula):
        j, event = self.take('translation')
        require(exact_equal(event['formula'], formula), 'exact source translation occurrence')
        g = event['graph']
        value = self.evaluate(g, original=True)['free']
        target = self.ar.translation(formula)
        require(value == target, 'complete formal ordered translation')
        self.statistics['translations'] += 1
        self.save(j, 'translation', formula=formula, polynomial=serial(value),
                  target=serial(target), records=g['vertices']+len(g['edges']))
        return g

    def restriction(self, item, expected):
        require(exact_equal(item['original'], expected), 'retained original recipe operand')
        g, z = item['original'], item['trimmed']
        a = self.evaluate(g, original=True)['free']
        b = self.evaluate(z, original=True)['free']
        n, s, t = (g[k] for k in ('vertices', 'source', 'sink'))
        # Independent all-pairs closure, including all length-zero paths.
        reach = [[i == j for j in range(n)] for i in range(n)]
        for u, v, _ in g['edges']:
            reach[u][v] = True
        for k in range(n):
            for u in range(n):
                if reach[u][k]:
                    for v in range(n):
                        reach[u][v] = reach[u][v] or reach[k][v]
        live = [u for u in range(n) if reach[s][u] and reach[u][t]]
        retained = live if reach[s][t] else sorted({s, t})
        edges = [i for i, (u, v, _) in enumerate(g['edges'])
                 if reach[s][u] and reach[v][t]]
        mapping = [retained.index(v) if v in retained else None for v in range(n)]
        require(exact_equal(item['old_to_new'], mapping) and
                exact_equal(item['new_to_old'], retained) and
                exact_equal(item['retained_edge_indices'], edges) and
                item['no_path'] is (not reach[s][t]), 'complete vertex/edge occurrence maps')
        expected_z = dict(vertices=len(retained), source=mapping[s], sink=mapping[t],
                          edges=[[mapping[g['edges'][i][0]], mapping[g['edges'][i][1]],
                                  g['edges'][i][2]] for i in edges])
        require(exact_equal(z, expected_z), 'all labels/order/multiplicities and endpoint transport')
        require(a == b, 'both complete ordered operand polynomials preserved')
        if s == t:
            require(z['vertices'] == 1 and not z['edges'] and b == {()}, 'empty path retained')
        if not reach[s][t]:
            require(not z['edges'] and not b, 'no-path graph retained as zero')
        self.statistics['restrictions'] += 1
        self.statistics['changed_restrictions'] += int(not exact_equal(g, z))
        return a, dict(original_polynomial=serial(a), trimmed_polynomial=serial(b),
                       original_records=n+len(g['edges']),
                       trimmed_records=z['vertices']+len(z['edges']),
                       complete_occurrence_maps_verified=True)

    def commutator(self, f, g, parent, entry):
        j, event = self.take('commutator-input')
        require(event['parent'] == parent and event['entry'] == entry and
                exact_equal([event['f'], event['g']], [f, g]),
                'original pre-restriction ordered recipe provenance')
        values, evidence = [], []
        for key, expected in zip(('f', 'g'), (f, g)):
            value, detail = self.restriction(event['restrictions'][key], expected)
            values.append(value)
            evidence.append(detail)
        old = counts(f, g)
        new = counts(*(event['restrictions'][key]['trimmed'] for key in ('f', 'g')))
        require(exact_equal(old, event['original_ledger']) and
                exact_equal(new, event['trimmed_ledger']), 'independent old/new exact L035 ledgers')
        a, b = values
        target = self.ar.add(self.ar.mul(a, b), self.ar.mul(b, a))
        self.statistics['commutators'] += 1
        self.statistics['max_old_ledger'] = max(old['actual'], self.statistics['max_old_ledger'])
        self.statistics['max_new_ledger'] = max(new['actual'], self.statistics['max_new_ledger'])
        key = ('nested_calls' if parent is not None else 'source_direct_calls'
               if entry == 'm.witness' else 'occurrence_direct_calls')
        self.statistics[key] += 1
        self.save(j, 'commutator-input', parent=parent, entry=entry,
                  operands=evidence, original_ledger=old, trimmed_ledger=new,
                  target=serial(target))
        self.pending = dict(kind='commutator', event=j, ledger=new)
        k, output = self.take('commutator-output')
        require(new['fits'], 'completed call fits unchanged exact preflight')
        require(output['parent'] == j and output['central'] == new['q'] and
                output['graph']['vertices'] == new['vertices'] and
                len(output['graph']['edges']) == new['edges'],
                'actual output/parent/exact-copy pairing')
        polys = self.evaluate(output['graph'], ('free', 'zero', 'axioms'))
        require(not polys['zero'] and polys['axioms'] == target, 'actual commutator identities')
        self.save(k, 'commutator-output', parent=j,
                  polynomials={m:serial(p) for m,p in polys.items()})
        self.pending = None
        return output['graph']

    def boolean(self, g):
        j, event = self.take('boolean-input')
        require(exact_equal(event['graph'], g), 'exact actual translated Boolean operand')
        h = normalized(g)
        a = self.evaluate(g, original=True)['free']
        require(self.evaluate(h, original=True)['free'] == a, 'unchanged all-suffix normalization')
        jobs = nested_schedule(h)
        self.statistics['booleans'] += 1
        self.save(j, 'boolean-input', input=serial(a), required_nested_calls=len(jobs))
        for f, gg in jobs:
            self.commutator(f, gg, j, 'm.witness')
        self.pending = dict(kind='boolean', event=j, completed_nested_calls=len(jobs))
        k, output = self.take('boolean-output')
        require(output['parent'] == j and exact_equal(output['normalized'], h),
                'unchanged complete normalized parent/output binding')
        polys = self.evaluate(output['graph'], ('free', 'zero', 'axioms'))
        target = self.ar.add(self.ar.mul(a, a), a)
        require(not polys['zero'] and polys['axioms'] == target, 'actual Boolean identities')
        self.save(k, 'boolean-output', parent=j, nested_calls=len(jobs),
                  polynomials={m:serial(p) for m,p in polys.items()}, target=serial(target))
        self.pending = None
        return output['graph']

    def block(self, line, role, graph=None, factors=None):
        if self.kdata is None:
            return
        block = self.kdata['blocks'][self.block_position]
        self.block_position += 1
        require(block['line'] == line and block['role'] == role, 'complete source-block sequence')
        lo, hi = block['vertex_range']
        first, last = block['edge_range']
        local = dict(vertices=hi-lo, source=block['entry']-lo, sink=block['exit']-lo,
                     edges=[[u-lo,v-lo,lab] for u,v,lab in self.kdata['graph']['edges'][first:last-2]])
        if factors is not None:
            copied_composition(local, [typed(g, self.transport) for g in factors], 'product')
        else:
            require(exact_equal(local, typed(graph, self.transport)),
                    'complete actual trace graph bound to copied K block')

    def source(self, rows):
        fs = [r['f'] for r in rows]
        for i, r in enumerate(rows):
            tag, f, refs = r['rule'], r['f'], r['refs']
            factors = None
            if tag in ('axiom', 'contraction'):
                seed = self.boolean(self.translation(f[2] if tag == 'axiom' else f))
            elif tag == 'expansion':
                a, b = self.translation(fs[refs[0]]), self.translation(f[1])
                seed = self.commutator(a, b, None, 'm.witness')
            elif tag == 'cut':
                a, b, c = fs[refs[0]][1], fs[refs[0]][2], fs[refs[1]][2]
                bb, cc = self.translation(b), self.translation(c)
                w = self.commutator(bb, cc, None, 'm.witness')
                prefix = self.translation(['not', a])
                factors = [prefix, w]
                seed = None
            else:
                require(tag in ('true', 'not-false', 'association'), 'known source rule')
                seed = dict(vertices=2, source=0, sink=1, edges=[])
            self.block(i, 'seed', seed, factors)
            transitions = ([f[1]] if tag == 'expansion' else
                           ['false'] if tag in ('contraction', 'association') else
                           [fs[refs[1]][2], fs[refs[0]][2]] if tag == 'cut' else [])
            for formula in transitions:
                self.block(i, 'transition', self.translation(formula))
        if self.kdata is not None:
            require(self.block_position == len(self.kdata['blocks']), 'all K blocks bound')

    def occurrence(self, ctx):
        require(self.hdata is not None, 'complete H required for occurrence trace provenance')
        graphs = self.hdata['correction']['graphs']
        inverse = {tuple(v):k for k,v in self.transport.items()}
        def untyped(g):
            return dict(vertices=g['vertices'], source=g['source'], sink=g['sink'],
                        edges=[[u,v,[inverse[tuple(a)] for a in lab]] for u,v,lab in g['edges']])
        for key, spec in plan(ctx):
            if spec['kind'] == 'commutator':
                f, g = [untyped(graphs[k]) for k in spec['inputs']]
                out = self.commutator(f, g, None, 'checked_witness')
                require(exact_equal(typed(out, self.transport), graphs[key]),
                        'complete actual occurrence correction/output binding')


def preservation():
    scope = load(OUT / 'run-scope.json')
    require(exact_equal(scope['caps'], CAPS), 'unchanged scope caps')
    hashes = load(OUT / 'preservation-before.json')
    hashes.update(load(OUT / 'source-hashes.json'))
    hashes.update(scope['source_hashes'])
    for name, digest in hashes.items():
        require(hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest,
                'unchanged source/input bytes: '+name)
    manifest = load(OUT / 'inputs/manifest.json')
    for key in ('source', 'annotations', 'pair', 'proof', 'request'):
        filename = key+('.jsonl' if key == 'proof' else '.json')
        copied = (OUT / 'inputs' / filename).read_bytes()
        original = HERE / ('output-470' if key in ('proof','request') else
                           'output-461/final/empty-clause') / filename
        require(copied == original.read_bytes() and
                hashlib.sha256(copied).hexdigest() == manifest[key],
                'exact unchanged original caller bytes')
    require(load(OUT / 'preservation-after.json')['unchanged'] is True,
            'driver preservation completed')
    return hashes


def main():
    path = OUT / 'integration-reception.json'
    require(not path.exists(), 'refuse existing integration receipt')
    req, raw, rows, checked = request(OUT/'inputs/proof.jsonl', OUT/'inputs/request.json')
    paths = {k:OUT/'inputs'/(k+('.jsonl' if k=='proof' else '.json'))
             for k in ('manifest','source','annotations','pair','proof','request')}
    ctx = context(**{k+'_path':p for k,p in paths.items()})
    kpath, hpath = OUT/'emitted/K.json', OUT/'emitted/H.json'
    kdata = load(kpath) if kpath.exists() else None
    hdata = load(hpath) if hpath.exists() else None
    receiver = Reception(req, kdata, hdata)
    result = dict(accepted=False, complete_KH_received=False, failures=[], caps=CAPS)
    try:
        hashes = preservation()
        receiver.source(rows)
        receiver.occurrence(ctx)
        require(receiver.position == len(receiver.index), 'no missing/extra actual calls/events')
        require(not (OUT/'failure.json').exists(), 'no hidden failed integration stage')
        # The unchanged independent receivers were executed by the run driver.
        # Bind their complete receipts to exactly these parsed K and H archives.
        received = load(OUT/'reception.json')
        require(received['accepted'] is True and received['extractor']['accepted'] is True and
                received['correction']['component_checked'] is True and
                not received['failures'] and not received['extractor']['failures'] and
                not received['correction']['failures'], 'complete independent receiver acceptance')
        require(received['extractor']['certificate_sha256'] ==
                hashlib.sha256(kpath.read_bytes()).hexdigest() and
                received['H_sha256'] == hashlib.sha256(hpath.read_bytes()).hexdigest(),
                'checked complete K/H byte binding')
        require(len(received['extractor']['roots']) == len(rows) and
                len(received['extractor']['blocks']) == len(kdata['blocks']),
                'all source roots and blocks independently received')
        result.update(accepted=True, complete_KH_received=True,
                      complete_trace_received=True, source=checked,
                      statistics=receiver.statistics, trace_arithmetic=receiver.ar.counts,
                      events=len(receiver.evidence), K_blocks=receiver.block_position,
                      K_bounds=received['extractor']['bounds'], H_bounds=received['bounds'],
                      K_arithmetic=received['extractor']['arithmetic'],
                      correction_arithmetic=received['correction']['arithmetic'],
                      H_arithmetic=received['arithmetic'], unchanged_hashes=hashes,
                      evidence='reception.json and trace-received-prefix.json',
                      qualifications=['finite reproduction; critical audit pending',
                                      'empty-clause f=0 does not test nonzero fJ',
                                      'trusted paths and remaining SHA bindings retained'])
    except MissingEvent as error:
        require((OUT/'failure.json').exists(), 'missing output requires recorded failure')
        failure = load(OUT/'failure.json')
        require(receiver.position == len(receiver.index), 'complete saved prefix consumed')
        result.update(complete_trace_prefix_received=True, missing=error.args[0],
                      statistics=receiver.statistics, trace_arithmetic=receiver.ar.counts,
                      events=len(receiver.evidence), failure=failure['failure'],
                      failure_detail=failure['detail'], stage=failure['stage'],
                      unchanged_hashes=hashes,
                      qualifications=['no pending correction or full K/H acceptance'])
    except Exception as error:
        result['failures'].append(repr(error))
        result.update(event=receiver.position, completed_events=len(receiver.evidence),
                      statistics=receiver.statistics, trace_arithmetic=receiver.ar.counts)
        write_json(path.with_suffix('.failure.json'), result)
        raise
    write_json(path, result)
    print(dict(accepted=result['accepted'], complete_KH_received=result['complete_KH_received'],
               events=result['events'], statistics=result['statistics'],
               trace_arithmetic=result['trace_arithmetic'], failures=result['failures'],
               path=str(path)))


if __name__ == '__main__':
    main()
