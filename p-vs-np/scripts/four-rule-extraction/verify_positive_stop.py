"""Independent structural/count check of the step-471 saved resource stop.

No emitter, receiver arithmetic, or graph constructor is imported. Complete
saved graphs are read; no polynomial correctness of an unfinished K is claimed.
"""
import hashlib
import json
from collections import deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
OUT = HERE / 'output-471'


def read(name):
    return json.loads((OUT / name).read_bytes())


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def graph(g, typed, n, nd):
    nv, edges = g['vertices'], g['edges']
    assert type(nv) is int and 0 < nv <= 2_000_000
    assert nv + len(edges) <= 2_000_000
    assert all(type(g[k]) is int and 0 <= g[k] < nv for k in ('source', 'sink'))
    adj, ind = [[] for _ in range(nv)], [0] * nv
    entries = 0
    for u, v, label in edges:
        assert type(u) is int and type(v) is int and 0 <= u < nv and 0 <= v < nv
        assert type(label) is list and len(label) <= 1024
        entries += len(label)
        for symbol in label:
            if typed:
                assert symbol == ['one'] or (
                    type(symbol) is list and len(symbol) == 2 and
                    type(symbol[1]) is int and symbol[0] in ('original', 'placeholder') and
                    0 <= symbol[1] < (n if symbol[0] == 'original' else nd))
            else:
                assert type(symbol) is str and (symbol == '1' or
                    symbol in {'x' + str(i + 1) for i in range(n)} or
                    symbol in {'b:' + str(i + 1) for i in range(n)} or
                    symbol in {'t:' + str(i + 1) + ':' + str(j + 1)
                               for i in range(n) for j in range(i + 1, n)})
        adj[u].append(v)
        ind[v] += 1
    assert entries <= 2_000_000
    queue = deque(i for i in range(nv) if ind[i] == 0)
    visited = 0
    while queue:
        u = queue.popleft()
        visited += 1
        for v in adj[u]:
            ind[v] -= 1
            if ind[v] == 0:
                queue.append(v)
    assert visited == nv
    return dict(vertices=nv, edges=len(edges), records=nv + len(edges),
                label_entries=entries, acyclic=True, required_records=2_000_000)


def main():
    result_path = OUT / 'stop-check.json'
    assert not result_path.exists()
    failed, outer, attach = read('failure.json'), read('failure-frame-2.json'), read('failure-frame-3.json')
    req = read('inputs/request.json')
    rows = [json.loads(line) for line in (OUT / 'inputs/proof.jsonl').read_bytes().splitlines()]
    n, nd = len(req['alphabet']), len(req['dictionary']['placeholders'])
    assert outer['i'] == attach['i'] == 7 and outer['r'] == rows[8]
    assert outer['r']['rule'] == 'cut' and outer['r']['refs'] == [5, 6]
    assert attach['kind'] == 'prefixed-commutator' and attach['parent'] is None
    assert outer['out'] == attach['out'] and outer['seed'] == attach['g']
    prefix = graph(outer['out'], True, n, nd)
    pending = graph(attach['g'], False, n, nd)
    blocks = outer['blocks']
    vertex, edge = len(rows), 0  # source plus all 31 retained line vertices
    completed_lines = []
    for block in blocks:
        lo, hi = block['vertex_range']
        first, last = block['edge_range']
        assert lo == vertex and first == edge and lo < hi <= prefix['vertices']
        assert first + 2 <= last <= prefix['edges']
        s, t = block['entry'], block['exit']
        assert lo <= s < hi and lo <= t < hi
        for u, v, _ in outer['out']['edges'][first:last - 2]:
            assert lo <= u < hi and lo <= v < hi
        parent = block['parent']
        assert outer['out']['edges'][last - 2:last] == [
            [0 if parent is None else parent + 1, s, [['one']]],
            [t, block['line'] + 1, [['one']]]]
        assert 0 <= block['line'] < 7
        completed_lines.append(block['line'])
        vertex, edge = hi, last
    assert vertex == prefix['vertices'] and edge == prefix['edges']
    assert set(completed_lines) == set(range(7))
    actual = prefix['records'] + pending['records'] + 2
    assert failed['detail'] == [dict(stage='outer graph preflight', actual=actual,
                                    required=2_000_000, resource='records')]
    assert actual == 2_008_364 > 2_000_000
    assert not (OUT / 'emitted/K.json').exists() and not (OUT / 'emitted/H.json').exists()
    preservation = read('preservation-before.json')
    assert all(sha(ROOT / p) == h for p, h in preservation.items())
    sources = read('source-hashes.json')
    assert all(sha(ROOT / p) == h for p, h in sources.items())
    # Actual imported marked-edge module, omitted by the driver's conservative
    # existence filter for its mistaken candidate path. Pin it explicitly here.
    marked = ROOT / 'scripts/alternative-abp-commutator/check_marked_edges.py'
    supplementary = {str(marked.relative_to(ROOT)): sha(marked)}
    manifest = read('inputs/manifest.json')
    for key in ('source', 'annotations', 'pair', 'proof', 'request'):
        copied = OUT / 'inputs' / (key + ('.jsonl' if key == 'proof' else '.json'))
        origin = HERE / ('output-470' if key in ('proof', 'request') else
                         'output-461/final/empty-clause') / copied.name
        assert copied.read_bytes() == origin.read_bytes()
        assert manifest[key] == sha(copied)
    result = dict(verified_resource_stop=True, prefix=prefix, pending_seed=pending,
                  retained_blocks=len(blocks), completed_source_lines=list(range(7)),
                  failed_source_line_zero_based=7, failed_source_rule='cut',
                  next_attachment=dict(actual=actual, required=2_000_000,
                                       excess=actual - 2_000_000, connectors=2),
                  input_files_unchanged=len(preservation), source_hashes_unchanged=len(sources),
                  supplementary_source_hashes=supplementary,
                  evidence=['failure-frame-2.json', 'failure-frame-3.json', 'failure.json'],
                  scope='Full graph counts/labels/topology/partitions and retained bytes checked; no partial-K polynomial verification or complete K/H acceptance.',
                  failures=[])
    result_path.write_text(json.dumps(result, separators=(',', ':')))
    print(dict(verified_resource_stop=True, actual=actual, required=2_000_000,
               prefix=prefix['records'], pending_seed=pending['records'],
               path=str(result_path.relative_to(ROOT))))


if __name__ == '__main__':
    main()
