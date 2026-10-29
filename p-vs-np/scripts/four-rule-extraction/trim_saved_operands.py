"""Step 475: isolated path filtering of the exact saved pair; no integration.

No polynomial evaluator, scalar recognition or correction constructor is used.
The independent receiver is verify_path_trimming.py.
"""
from pathlib import Path
import hashlib
from parameterized_input import CAPS, load, require, write_json

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OLD = HERE / 'output-473'
OUT = HERE / 'output-475'
TARGET = ('Test source-to-sink path trimming on the two saved record-22 L035 '
          'operands, requiring exact ordered-polynomial preservation and an '
          'L035 preflight of at most 2,000,000 records.')


def trim(g):
    nv, edges, s, t = (g[k] for k in ('vertices', 'edges', 'source', 'sink'))
    forward, backward = [[] for _ in range(nv)], [[] for _ in range(nv)]
    for u, v, _ in edges:
        forward[u].append(v)
        backward[v].append(u)

    def visit(start, adjacency):
        seen, todo = {start}, [start]
        while todo:
            for v in adjacency[todo.pop()]:
                if v not in seen:
                    seen.add(v)
                    todo.append(v)
        return seen

    live = visit(s, forward) & visit(t, backward)
    no_path = t not in live
    retained = sorted(live if not no_path else {s, t})
    old_to_new = [None] * nv
    for j, v in enumerate(retained):
        old_to_new[v] = j
    indices = [i for i, (u, v, _) in enumerate(edges)
               if not no_path and u in live and v in live]
    out = dict(vertices=len(retained), source=old_to_new[s], sink=old_to_new[t],
               edges=[[old_to_new[edges[i][0]], old_to_new[edges[i][1]],
                       list(edges[i][2])] for i in indices])
    return dict(original=g, trimmed=out, old_to_new=old_to_new,
                new_to_old=retained, retained_edge_indices=indices, no_path=no_path)


def ledger(f, g):
    p = len(f['edges']) * len(g['edges'])
    q = sum(x != '1' and y != '1' and x != y
            for _, _, a in f['edges'] for _, _, b in g['edges']
            for x in a for y in b)
    nv = 2 + 2*p*(f['vertices'] + g['vertices'])
    ne = 2*p*(len(f['edges']) + len(g['edges'])) + 4*p + q
    return dict(p=p, q=q, vertices=nv, edges=ne, actual=nv+ne,
                required=CAPS['records'], fits=nv+ne <= CAPS['records'])


def fixtures():
    def graph(n, s, t, edges):
        return dict(vertices=n, source=s, sink=t, edges=edges)
    return {
        'nonextremal-ordered-parallel-zero': graph(7, 2, 4, [
            [0, 2, ['x4']], [2, 3, ['x2']], [2, 3, ['x2']],
            [2, 3, ['x1']], [3, 4, ['x2']], [2, 4, []],
            [4, 5, ['x3']], [6, 5, ['1']]]),
        'interior-coincident-empty-path': graph(5, 2, 2, [
            [0, 1, ['1']], [1, 2, ['x1']], [2, 3, ['x2']], [3, 4, ['1']]]),
        'no-path-distinct-roots': graph(5, 1, 3, [
            [0, 1, ['1']], [1, 2, ['x1']], [3, 4, ['x2']]]),
        'edgeless-coincident': graph(1, 0, 0, []),
        'constant-parallel-cancellation': graph(4, 3, 0, [
            [3, 1, ['1']], [3, 1, ['1']], [1, 0, ['1']]]),
        'affine-duplicate-labels': graph(4, 2, 0, [
            [2, 3, ['1', 'x1', 'x1', 'x2']], [3, 0, ['x1']],
            [1, 0, ['x3']]])}


def main():
    require(not OUT.exists(), 'refuse existing step-475 output')
    files = [OLD / p for p in (
        'trace/event-00201.json', 'trace/event-00196.json',
        'trace/event-00197.json', 'trace/event-00199.json',
        'failure-frame-7.json', 'stop-check.json', 'trace-received-prefix.json',
        'inputs/manifest.json', 'inputs/source.json', 'inputs/annotations.json',
        'inputs/pair.json', 'inputs/proof.jsonl', 'inputs/request.json')]
    files += [HERE / p for p in (
        'output-470/proof.jsonl', 'output-470/request.json',
        'output-461/final/empty-clause/source.json',
        'output-461/final/empty-clause/annotations.json',
        'output-461/final/empty-clause/pair.json',
        'emit_parameterized.py', 'parameterized_input.py', 'receive_parameterized.py',
        'constant_translation.py', 'trim_saved_operands.py', 'verify_path_trimming.py')]
    files += [HERE.parent / 'alternative-abp-commutator/check_marked_edges.py',
              HERE.parent / 'affine-abp-boolean/check_suffix_graph.py']
    hashes = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in files}
    event = load(OLD / 'trace/event-00201.json')
    req = load(OLD / 'inputs/request.json')
    OUT.mkdir()
    # Persist full operands before reception; interruption preserves all work.
    cert = dict(target=TARGET, scope='isolated pair only; no constructor invocation',
                caps=CAPS, alphabet=req['alphabet'], dictionary=req['dictionary'],
                original_source_roots=list(range(1, 32)), input_hashes=hashes,
                operands={k: trim(event[k]) for k in ('f', 'g')},
                fixtures={k: trim(g) for k, g in fixtures().items()})
    f, g = (cert['operands'][k]['trimmed'] for k in ('f', 'g'))
    cert['original_ledger'] = ledger(event['f'], event['g'])
    cert['trimmed_ledger'] = ledger(f, g)
    write_json(OUT / 'trimmed-pair.json', cert)
    print(dict(saved=True, operands={k: dict(vertices=x['trimmed']['vertices'],
               edges=len(x['trimmed']['edges'])) for k, x in cert['operands'].items()},
               actual=cert['trimmed_ledger']['actual'], required=CAPS['records'],
               path=str(OUT / 'trimmed-pair.json')))


if __name__ == '__main__':
    main()
