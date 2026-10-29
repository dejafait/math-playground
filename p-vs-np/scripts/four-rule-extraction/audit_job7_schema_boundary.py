"""Step 516: tiny probes of unchanged graph and metadata checks.

No preflight main, archives, coordinate search or production mutation.
Extract existing postcheck ASTs; do not invent a transport receiver.
"""
import ast
from copy import deepcopy
import json
from pathlib import Path
import sys
import time

sys.dont_write_bytecode = True
import preflight_job7_transport as m

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-516-repaired'
VISIT_LIMIT = 100_000_000
SECONDS_LIMIT = 900
RESERVE = 1_000_000


def main():
    started = time.monotonic()
    m.p.require(not OUT.exists(), 'fresh output required')
    source = (HERE / 'preflight_job7_transport.py').read_text()
    tree = ast.parse(source)
    main_node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    product_check = next(n for n in ast.walk(main_node) if isinstance(n, ast.For) and n.lineno == 543)
    local = next(n for n in ast.walk(main_node) if isinstance(n, ast.FunctionDef) and n.name == 'local')
    gadget_check = [n for n in local.body if 596 <= n.lineno and n.end_lineno <= 614]
    comparison_check = next(n for n in ast.walk(main_node) if isinstance(n, ast.For) and n.lineno == 633)
    m.p.require(len(gadget_check) == 4, 'exact local postcheck selection')
    selections = {'product': [product_check], 'gadget': gadget_check,
                  'comparison': [comparison_check]}
    blocks = {k: compile(ast.Module(body=v, type_ignores=[]), '<original-'+k+'-postcheck>', 'exec')
              for k, v in selections.items()}
    excerpts = {k: [{'first_line': n.lineno, 'last_line': n.end_lineno,
                     'source': ast.get_source_segment(source, n)} for n in v]
                for k, v in selections.items()}
    cases = []
    visits = 0
    symbols = {'1': ['one'], 'x1': ['original', 0]}

    def trial(name, expected, fixture, action):
        nonlocal visits
        m.R = m.Run()
        m.R.stage = 'tiny schema probe'
        try:
            result = action()
            accepted, error = True, None
        except m.p.Rejected as err:
            accepted, error, result = False, str(err), None
        visits += m.R.visits
        cases.append(dict(name=name, expected_accept=expected, accepted=accepted,
                          matches_expectation=accepted == expected, fixture=fixture,
                          result=result, rejection=error, selected_item_visits=m.R.visits))

    base = m.graph(edges=[[0, 1, ['x1']]])
    graph_cases = [('graph-valid-singleton', base, True)]
    for name, key, value in [('graph-extra-field', 'unexpected', 0),
                             ('graph-boolean-vertex-count', 'vertices', True),
                             ('graph-boolean-source', 'source', False),
                             ('graph-float-sink', 'sink', 1.0),
                             ('graph-negative-source', 'source', -1),
                             ('graph-boolean-edge-endpoint', 'edges', [[False, 1, ['x1']]]),
                             ('graph-unknown-token', 'edges', [[0, 1, ['x2']]]),
                             ('graph-nonstring-token', 'edges', [[0, 1, [True]]]),
                             ('graph-cycle', 'edges', [[0, 1, ['1']], [1, 0, ['1']]])]:
        g = deepcopy(base)
        g[key] = value
        graph_cases.append((name, g, False))
    graph_cases += [('graph-empty-affine-label', m.graph(edges=[[0, 1, []]]), True),
                    ('graph-multiple-affine-entries', m.graph(edges=[[0, 1, ['1', 'x1']]]), True),
                    ('graph-coincident-roots', m.graph(n=1, s=0, t=0), True)]
    for name, g, expected in graph_cases:
        trial(name, expected, g, lambda g=g: m.validate(g, symbols, True))

    # Construct tiny fixtures with the existing primitives, then mutate only
    # metadata presented to the unchanged selected postcheck.
    m.R = m.Run()
    a, b = deepcopy(base), m.graph(edges=[[0, 1, ['1']]])
    fg, fgmaps = m.product([a, b])
    gf, gfmaps = m.product([b, a])
    fixture_setup_visits = m.R.visits
    for name, mutation, expected in [('product-valid', None, True),
                                     ('product-boolean-range-start', 'bool', True),
                                     ('product-extra-map-field', 'extra', True),
                                     ('product-range-extra-element', 'length', False)]:
        maps = deepcopy(fgmaps)
        if mutation == 'bool': maps[0]['edge_range'][0] = False
        if mutation == 'extra': maps[0]['unexpected'] = 0
        if mutation == 'length': maps[0]['edge_range'].append(0)
        fixture = dict(a=a, b=b, fg=fg, gf=gf, fgmaps=maps, gfmaps=gfmaps)
        trial(name, expected, fixture,
              lambda fixture=fixture: exec(blocks['product'], dict(fixture, R=m.R, p=m.p)))

    attrs = [dict(input_edge=0, token='x1', vertex_range=[2, 2], edge_range=[0, 1])]
    for name, mutation, expected in [('gadget-valid', None, True),
                                     ('gadget-boolean-input-edge', 'bool', True),
                                     ('gadget-extra-field-and-range-suffix', 'extra', True),
                                     ('gadget-wrong-range-end', 'wrong', False)]:
        items = deepcopy(attrs)
        if mutation == 'bool': items[0]['input_edge'] = False
        if mutation == 'extra':
            items[0]['unexpected'] = 0
            items[0]['edge_range'].append(99)
        if mutation == 'wrong': items[0]['edge_range'][1] = 2
        fixture = dict(z=base, out=base, attrs=items, mode='free', symbols=symbols)
        trial(name, expected, fixture,
              lambda fixture=fixture: exec(blocks['gadget'], dict(fixture, R=m.R, p=m.p)))

    m.R = m.Run()
    union = m.graph(0, [], 0, 0)
    maps2 = [m.copy(union, a), m.copy(union, b)]
    fixture_setup_visits += m.R.visits
    for name, mutation in [('comparison-valid', None), ('comparison-missing-second-map', 'short'),
                           ('comparison-bogus-unused-range-ends', 'ends')]:
        maps = deepcopy(maps2)
        if mutation == 'short': maps.pop()
        if mutation == 'ends':
            maps[0]['vertex_range'][1] = None
            maps[0]['edge_range'][1] = 'unchecked'
        fixture = dict(left=a, right=b, out=union, maps2=maps)
        trial(name, True, fixture,
              lambda fixture=fixture: exec(blocks['comparison'], dict(fixture, R=m.R, p=m.p)))

    # The exact comparator used on imported maps rejects both examples.
    trial('exact-map-comparator-rejects-boolean', False, [0, False],
          lambda: m.p.require(m.R.eq([0], [False]), 'type-sensitive map comparison'))
    elapsed = time.monotonic() - started
    failures = [c['name'] for c in cases if not c['matches_expectation']]
    report = dict(status='PASS' if not failures else 'FAIL', cases=cases, failures=failures,
                  selected_source_blocks=excerpts, selected_item_visits=visits,
                  fixture_setup_visits=fixture_setup_visits, required_item_visits=VISIT_LIMIT,
                  elapsed_seconds=elapsed, required_seconds=SECONDS_LIMIT,
                  full_preflight_executed=False, archives_read=False,
                  initial_failure=dict(path='output-516/failure.json', selected_item_visits=0,
                                       fixture_setup_visits=0, elapsed_seconds='UNKNOWN',
                                       other_work='UNKNOWN; stopped before fixture setup'),
                  complete_administrative_ledger=False, production_changed=False,
                  limitation='These are existing subchecks, not a full transport acceptance path. '
                  'Accepted malformed metadata is unreachable under the unchanged constructor invariants. '
                  'Selected visits exclude interpreter, parsing, AST, serialization and I/O work.')
    raw = json.dumps(report, ensure_ascii=True, separators=(',', ':'), allow_nan=False).encode()
    program = Path(__file__).read_bytes()
    failure_bytes = sum(p.stat().st_size for p in (HERE / 'output-516').iterdir() if p.is_file())
    evidence_bytes = len(raw) + len(program) + failure_bytes
    m.p.require(evidence_bytes <= RESERVE and evidence_bytes <= m.p.CAPS['certificate_bytes'], 'evidence reserve')
    m.p.require(visits + fixture_setup_visits <= VISIT_LIMIT and elapsed <= SECONDS_LIMIT, 'tiny probe limits')
    OUT.mkdir()
    (OUT / 'audit_job7_schema_boundary.py').write_bytes(program)
    (OUT / 'schema-boundary.json').write_bytes(raw)
    print(json.dumps(dict(status=report['status'], cases=len(cases), failures=failures,
                          selected_and_fixture_visits=visits + fixture_setup_visits,
                          required_item_visits=VISIT_LIMIT, saved_bytes=evidence_bytes,
                          required_reserve_bytes=RESERVE, required_evidence_bytes=m.p.CAPS['certificate_bytes'],
                          elapsed_seconds=elapsed, required_seconds=SECONDS_LIMIT,
                          path=str(OUT / 'schema-boundary.json'))))
    return 0 if not failures else 1


if __name__ == '__main__':
    raise SystemExit(main())
