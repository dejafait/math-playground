"""Independent backward replay of L036's finite evidence; not a proof.

Preserves the old certificate and writes complete audit data separately.
The constructor is reused, but neither its evaluator nor its ledger is trusted.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import runpy


def add(*polys):
    counts = Counter()
    for p in polys:
        counts.update(p)
    return {w: 1 for w, c in counts.items() if c % 2}


def mul(p, q):
    counts = Counter()
    for a in p:
        for b in q:
            counts[a + b] += 1
    return {w: 1 for w, c in counts.items() if c % 2}


def serial(p):
    return [list(w) for w in sorted(p, key=lambda w: (len(w), w))]


def evaluate(g, mode):
    """All vertex-to-sink polynomials; path marks ignore F2 cancellation."""
    nv = g['vertices']
    adj, indegree = [[] for _ in range(nv)], [0] * nv
    for u, v, lab in g['edges']:
        assert 0 <= u < nv and 0 <= v < nv
        adj[u].append((v, lab))
        indegree[v] += 1
    ready = [u for u in range(nv) if not indegree[u]]
    order = []
    while ready:
        u = ready.pop()
        order.append(u)
        for v, _ in adj[u]:
            indegree[v] -= 1
            if not indegree[v]:
                ready.append(v)
    assert len(order) == nv, 'cycle'
    values, marks = [{} for _ in range(nv)], [set() for _ in range(nv)]
    for u in reversed(order):
        parts = [{(): 1}] if u == g['sink'] else []
        if u == g['sink']:
            marks[u].add(0)
        for v, lab in adj[u]:
            terms = []
            for a in lab:
                if a == '1':
                    terms.append({(): 1})
                elif a.startswith(('b:', 't:')):
                    if mode == 'free':
                        terms.append({(a,): 1})
                    elif mode == 'axioms':
                        if a.startswith('b:'):
                            x = 'x' + a[2:]
                            terms.append({(x, x): 1, (x,): 1})
                        else:
                            _, i, j = a.split(':')
                            x, y = 'x' + i, 'x' + j
                            terms.append({(x, y): 1, (y, x): 1})
                else:
                    terms.append({(a,): 1})
            parts.append(mul(add(*terms), values[v]))
            # Output labels are all single symbols. Count actual graph paths.
            placeholder = any(a.startswith(('b:', 't:')) for a in lab)
            if placeholder:
                assert len(lab) == 1
            marks[u].update(c + int(placeholder) for c in marks[v])
        values[u] = add(*parts)
    return values, marks


def w_counts(vf, lf, vg, lg):
    p = len(lf) * len(lg)
    q = sum(a != '1' and b != '1' and a != b for a in lf for b in lg)
    return 2 + 2 * p * (vf + vg), 2 * p * (len(lf) + len(lg)) + 4 * p + q


def expected_blocks(h):
    v, m = h['vertices'], len(h['edges'])
    labels = [lab[0] for _, _, lab in h['edges']]
    blocks = []
    for u in range(v):
        outgoing = [lab[0] for z, _, lab in h['edges'] if z == u]
        for a in outgoing:
            if a != '1':
                blocks.append(dict(vertex=u, kind='edge_boolean', vertices=2*v+4, edges=2*m+5))
            wn, wm = w_counts(2, [a], v, labels)
            blocks.append(dict(vertex=u, kind='product_commutator', vertices=wn+v+4, edges=wm+m+5))
        for i, a in enumerate(outgoing):
            for b in outgoing[i+1:]:
                wn, wm = w_counts(v+1, labels+[a], v+1, labels+[b])
                blocks.append(dict(vertex=u, kind='sum_commutator', vertices=wn, edges=wm))
    return blocks


def main():
    here = Path(__file__).parent
    constructor = runpy.run_path(str(here / 'check_suffix_graph.py'))['construct']
    original = here / 'suffix-graph-results.json'
    original_bytes = original.read_bytes()
    old = json.loads(original_bytes)
    cases, failures = [], []
    detected = Counter()
    for saved in old['cases']:
        name, g = saved['name'], saved['input']
        n = len(saved['full_output']['alphabet'])
        w, h, ledger = constructor(g)
        w = json.loads(json.dumps(w))
        h = json.loads(json.dumps(h))
        f, _ = evaluate(g, 'free')
        normalized, _ = evaluate(h, 'free')
        free, marks = evaluate(w, 'free')
        zero, _ = evaluate(w, 'zero')
        sub, _ = evaluate(w, 'axioms')
        s = g['source']
        target = add(mul(f[s], f[s]), f[s])
        polynomials = dict(f=serial(f[s]), free=serial(free[s]), zero=serial(zero[s]),
                           substituted=serial(sub[s]), target=serial(target))
        blocks = expected_blocks(h)
        q = h['vertices'] + len(h['edges']) + n + 2
        nv = h['vertices'] + 1 + sum(b['vertices'] for b in blocks)
        ne = len(h['edges']) + sum(b['edges'] + 2 for b in blocks)
        axioms = {f'b:{i}': [[f'x{i}', f'x{i}'], [f'x{i}']] for i in range(1, n+1)}
        axioms.update({f't:{i}:{j}': [[f'x{i}', f'x{j}'], [f'x{j}', f'x{i}']]
                       for i in range(1, n+1) for j in range(i+1, n+1)})
        full = dict(alphabet=[f'x{i}' for i in range(1, n+1)], axioms=axioms, graph=w)
        bounds = dict(Q=q, vertices_actual=w['vertices'], vertices_required=nv,
                      edges_actual=len(w['edges']), edges_required=ne,
                      records_actual=nv+ne, records_upper=50*q**5,
                      full_json_bits=8*len(json.dumps(full, separators=(',', ':')).encode()))
        checks = dict(full_output_replayed=full == saved['full_output'],
                      normalized_graph_replayed=h == saved['normalized'],
                      all_suffixes_preserved=f == normalized,
                      all_propagation_identities=all(sub[u] == add(mul(f[u], f[u]), f[u])
                                                     and not zero[u] for u in range(g['vertices'])),
                      all_propagation_paths=all(marks[u] <= {1} for u in range(g['vertices'])),
                      all_polynomials_replayed=polynomials == saved['polynomials'],
                      path_counts_replayed=sorted(marks[s]) == saved['path_placeholder_counts'],
                      independent_blocks=blocks == ledger == saved['blocks'],
                      independent_bounds=bounds == saved['bounds'],
                      exact_counts=w['vertices'] == nv and len(w['edges']) == ne,
                      branch_bound=len(blocks) <= (len(h['edges'])+1)**2,
                      each_block_bound=all(b['vertices']+b['edges']+2 <= 16*q**3 for b in blocks),
                      record_bound=nv+ne <= 50*q**5)
        mutations = {}
        for kind in ('omit_product_commutator', 'omit_sum_commutator'):
            bad, _, _ = constructor(g, kind)
            value = evaluate(bad, 'axioms')[0][s]
            result = dict(detected=value != target, substituted=serial(value))
            detected[kind] += result['detected']
            mutations[kind] = result
        checks['mutations_replayed'] = mutations == saved['mutations']
        if not all(checks.values()):
            failures.append(dict(name=name, failed=[k for k, v in checks.items() if not v]))
        cases.append(dict(name=name, checks=checks, bounds=bounds, blocks=blocks,
                          input=g, normalized=h, full_output=full, polynomials=polynomials,
                          all_input_suffixes=[serial(p) for p in f],
                          all_propagation_substituted=[serial(p) for p in sub[:g['vertices']]],
                          all_propagation_path_counts=[sorted(c) for c in marks[:g['vertices']]],
                          mutations=mutations))
    assert original.read_bytes() == original_bytes, 'original certificate changed'
    summary = dict(cases=len(cases), failures=failures, mutations_detected=dict(detected),
                   original_sha256=hashlib.sha256(original_bytes).hexdigest(),
                   max_records=max(c['bounds']['records_actual'] for c in cases),
                   required_record_bound='50 Q^5; each attached block <= 16 Q^3',
                   all_checks_pass=not failures)
    out = here / 'suffix-graph-audit-results.json'
    out.write_text(json.dumps(dict(scope='Finite replay, not the all-input proof.',
                                   summary=summary, cases=cases), indent=2)+'\n')
    print(json.dumps(summary))
    print('Full graphs, polynomials, failures, actual/required bounds:', out)
    assert not failures, failures


if __name__ == '__main__':
    main()
