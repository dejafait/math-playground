"""Step 505: exhaustive inline-comprehension subaudit of the fixed source phase.

No graph generation, word receiver or coordinate search. Original code and
receipts are read-only. A source-class correction is not a complete ledger.
"""
import ast
from collections import Counter
import json
from pathlib import Path
import sys
import time

import parameterized_input as p
import preflight_job7_transport as original

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output-505'
LIMIT, SECONDS, RESERVE = 100_000_000, 900, 1_000_000


def main():
    p.require(not OUT.exists(), 'fresh output only; preserve every previous run')
    OUT.mkdir()
    start = time.monotonic()
    budget = Counter()
    report = dict(status='IN_PROGRESS', item_limit=LIMIT, seconds_limit=SECONDS,
                  reserve_bytes=RESERVE, graph_regeneration=False,
                  word_expansion=False, coordinate_search=False)
    r = original.Run()
    original.R = r
    r.stage = 'fixed source phase only'
    entries, calls, completions = {}, set(), Counter()
    events, charges, frame_calls = Counter(), Counter(), Counter()
    sources = {p.__file__: Path(p.__file__).read_text(),
               str(HERE.parent / 'parity-four-rule/checker.py'):
                   (HERE.parent / 'parity-four-rule/checker.py').read_text()}
    source = HERE / 'output-489/inputs/proof.jsonl'
    request = HERE / 'output-489/inputs/request.json'

    def tick(kind, n=1):
        total = sum(budget.values())
        p.require(total+n <= LIMIT, 'audit event/item limit before next event')
        budget[kind] += n
        if (total+n) % 4096 == 0:
            p.require(time.monotonic()-start < SECONDS, 'audit time limit')

    def walk(x):
        tick('independent_json_items')
        if type(x) is dict:
            for k, v in x.items():
                walk(k); walk(v)
        elif type(x) in (list, tuple):
            for v in x:
                walk(v)

    def equal(a, b):
        tick('independent_comparison_items')
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            if a.keys() != b.keys():
                return False
            for k in a:
                if not equal(a[k], b[k]):
                    return False
            return True
        if type(a) in (list, tuple):
            if len(a) != len(b):
                return False
            for x, y in zip(a, b):
                if not equal(x, y):
                    return False
            return True
        return a == b

    def size_depth(t):
        work = [(t, 1)]
        n, depth = 0, 0
        while work:
            tick('independent_tree_nodes')
            x, d = work.pop()
            n += 1
            depth = max(depth, d)
            if type(x) is list:
                for child in x[1:]:
                    tick('independent_tree_links')
                    work.append((child, d+1))
        return n, depth

    try:
        p.require(p.CAPS == original.EXPECTED_CAPS, 'all original caps unchanged')
        raw = p.read_bytes(source, 'input_bytes')
        req_raw = p.read_bytes(request, 'input_bytes')
        req = p.parse(req_raw)
        rows = []
        for line in raw.splitlines():
            tick('independent_source_lines')
            rows.append(p.parse(line))
        walk(req); walk(rows)
        records = rows[1:]
        trees = [req['goal']]
        for row in records:
            tick('independent_tree_selection')
            trees.append(row['f'])
        sizes = []
        for t in trees:
            tick('independent_tree_sizes')
            sizes.append(size_depth(t))
        names = list(req['alphabet'])
        for entry in req['dictionary']['placeholders']:
            tick('independent_placeholder_names')
            names.append(entry['name'])
        boolean_expected = set()
        for x in req['alphabet']:
            tick('independent_boolean_entries')
            boolean_expected.add(('boolean', (x,)))

        # Pin the complete seven expressions and containing functions. Every
        # function actually entered in either local module is checked below.
        specs = [
            ('parameterized_input.py', 'request', 152, 153, 'expected',
             "{('boolean', (x,)) for x in alphabet}", len(req['alphabet']), boolean_expected),
            ('parameterized_input.py', 'request', 174, 175, 'records',
             '[parse(line) for line in lines]', len(rows), records),
            ('parameterized_input.py', 'input_bounds', 209, 210, 'trees',
             "[x['f'] for x in records]", len(records), trees),
            ('parameterized_input.py', 'input_bounds', 210, 211, 'sizes',
             '[size_depth(t) for t in trees]', len(trees), sizes),
            ('parameterized_input.py', 'input_bounds', 211, 212, 'names',
             "[p['name'] for p in req['dictionary']['placeholders']]",
             len(req['dictionary']['placeholders']), names),
            ('parameterized_input.py', 'input_bounds', 217, 218, 'required',
             "{k: CAPS['input_bytes'] if k in ('source_bytes', 'request_bytes') else CAPS[k] for k in actual}",
             8, None),
            ('checker.py', '_check_stream', 90, 91, 'p', '[fs[j] for j in refs]',
             sum(len(row['refs']) for row in records), None)]
        ast_inventory = []
        for path, text in sources.items():
            module = ast.parse(text)
            functions = [x for x in ast.walk(module) if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef))]
            for node in ast.walk(module):
                tick('ast_nodes')
                if isinstance(node, (ast.ListComp, ast.SetComp, ast.DictComp)):
                    owners = [f for f in functions if f.lineno <= node.lineno <= f.end_lineno]
                    owner = min(owners, key=lambda f: f.end_lineno-f.lineno)
                    ast_inventory.append(dict(file=Path(path).name, function=owner.name,
                                              line=node.lineno, expression=ast.unparse(node)))
        for file, function, line, after, variable, expression, count, expected in specs:
            matches = [x for x in ast_inventory if (x['file'],x['function'],x['line']) == (file,function,line)]
            p.require(len(matches) == 1 and matches[0]['expression'] == expression,
                      'pin exact comprehension AST and owning function')
            entries[(file, function, line)] = dict(file=file,function=function,line=line,
                after=after,variable=variable,expression=expression,item_visits=count,
                expected=expected,invocations=212 if file=='checker.py' else 1)

        checked_record_ids = []

        def observer(frame, event, arg):
            tick('trace_events')
            before = r.visits
            original.observe_source(frame,event,arg)
            delta = r.visits-before
            filename, name, line = frame.f_code.co_filename, frame.f_code.co_name, frame.f_lineno
            if filename in sources:
                file = Path(filename).name
                if event == 'call':
                    calls.add((file, name))
                    if name in ('<listcomp>', '<setcomp>', '<dictcomp>'):
                        frame_calls[name] += 1
                key = (file,name,line)
                if key in entries:
                    charges[key] += delta
                    if event == 'line':
                        events[key] += 1
                if event == 'line':
                    for k, item in entries.items():
                        if (file,name,line) != (item['file'],item['function'],item['after']):
                            continue
                        # The following statement may itself be an inlined
                        # comprehension, revisiting its line after our first
                        # completed-output inspection. Line counts below still
                        # independently check each original invocation count.
                        if item['line'] != 90 and completions[k]:
                            continue
                        tick('completed_collections')
                        loc = frame.f_locals
                        value = loc[item['variable']]
                        if item['line'] == 90:
                            i = loc['i']
                            p.require(i == len(checked_record_ids), 'all source records in order')
                            p.require(equal(loc['refs'],records[i]['refs']), 'exact original reference list')
                            p.require(len(value) == len(loc['refs']), 'complete reference-list output')
                            for j, v in zip(loc['refs'],value):
                                tick('checked_reference_selections')
                                p.require(v is loc['fs'][j], 'selected actual immutable formula object')
                            checked_record_ids.append(i)
                        elif item['line'] == 217:
                            expected = {}
                            p.require(set(loc['actual']) == {'source_bytes','request_bytes','tree_depth',
                                'tree_nodes','source_lines','alphabet','dictionary_entries','name_bytes'},
                                'exact metric keys')
                            for k2 in loc['actual']:
                                tick('independent_bound_entries')
                                expected[k2] = p.CAPS['input_bytes'] if k2 in ('source_bytes','request_bytes') else p.CAPS[k2]
                            # Exact count is eight; derived from the checked complete map.
                            item['item_visits'] = len(expected)
                            p.require(equal(value, expected), 'every required-bound map entry')
                        elif item['line'] == 152:
                            tick('checked_set_members',len(value))
                            p.require(value == item['expected'], 'complete Boolean expected set')
                        else:
                            p.require(equal(value,item['expected']), 'complete collection matches independent inputs')
                            if item['line'] == 174:
                                p.require(equal(loc['header'],rows[0]), 'complete parsed source header')
                        completions[k] += 1
            return observer

        sys.settrace(observer)
        try:
            actual_req, actual_raw, actual_records, checked = p.request(source,request)
            bounds = p.input_bounds(actual_req,actual_raw,actual_records,request)
        finally:
            sys.settrace(None)
        p.require(equal(actual_req,req) and actual_raw==raw and equal(actual_records,records),
                  'complete literal input correspondence')
        p.require(p.read_bytes(source,'input_bytes')==raw and p.read_bytes(request,'input_bytes')==req_raw,
                  'unchanged immutable input bytes')
        p.require(checked['accepted'] and checked['records']==212, 'full unchanged literal check')
        p.require(not frame_calls, 'no noninlined list/set/dict comprehension frames')
        entered_comps = [x for x in ast_inventory if (x['file'],x['function']) in calls]
        p.require({(x['file'],x['function'],x['line']) for x in entered_comps} == set(entries),
                  'all inline comprehensions in all entered local functions covered')
        table=[]
        for key, item in entries.items():
            p.require(completions[key]==item['invocations'], 'every comprehension output checked')
            p.require(events[key]==item['item_visits']+item['invocations'], 'all actual inline iteration line events')
            p.require(charges[key]==0, 'zero original charges on comprehension lines')
            table.append({k:v for k,v in item.items() if k!='expected'} | dict(
                completed_outputs=completions[key],line_events=events[key],original_charges=charges[key]))
        old_raw=p.read_bytes(HERE/'output-502/preflight.json','certificate_bytes')
        old=json.loads(old_raw,object_pairs_hook=p.no_duplicates,parse_constant=p.reject_number)
        walk(old)
        p.require(equal(dict(r.source_observer),old['source_observer']), 'entire unchanged original source observer')
        omitted=sum(x['item_visits'] for x in table)
        report.update(status='INLINE_CLASS_RECONCILED', caps=p.CAPS, literal_check=checked,
            input_bounds=bounds, complete_comprehension_table=table,
            entered_local_functions=[list(x) for x in sorted(calls)],
            full_local_ast_inventory=ast_inventory, noninlined_comprehension_frames=dict(frame_calls),
            completed_source_record_ids=checked_record_ids, original_source_observer=dict(r.source_observer),
            original_source_visits=r.visits, omitted_inline_item_visits=omitted,
            already_recorded_step504_visits=212, additional_omitted_visits=omitted-212,
            source_ledger_plus_inline_class=r.visits+omitted,
            old_three_run_reported_total=75_385_009,
            old_total_plus_inline_class=75_385_009+omitted,
            corrected_complete_total='UNKNOWN', transport_and_equalities='NOT_AUDITED',
            conclusion='Complete correction for this inline-comprehension class only; other source/supplement/failed work and transport audit remain unfinished.')
    except Exception as err:
        report.update(status='AUDIT_UNFINISHED', error=dict(type=type(err).__name__,message=str(err)),
            partial_line_events={str(k):v for k,v in events.items()},
            partial_completions={str(k):v for k,v in completions.items()})
    finally:
        sys.settrace(None)
    report.update(runtime=sys.version,elapsed_seconds=time.monotonic()-start,
        audit_budget=dict(budget),audit_event_item_upper=sum(budget.values()),
        budget_scope='trace events, AST nodes, explicit independent JSON/tree/comparison/collection items; not total Python work',
        extra_work='bounded input/source AST/JSON byte scans, source loading and receipt encoding; no exact interpreter-memory bound',
        input_scan_bytes=dict(source=source.stat().st_size,request=request.stat().st_size,
                              local_source_text=sum(len(x.encode()) for x in sources.values())),
        failed_and_supplement_work='NOT_RECONCILED; original helper failure and both supplements retained unchanged',
        receipt_policy='one exclusive sized write; no payload/temp/replacement files',
        failures=[] if report['status']=='INLINE_CLASS_RECONCILED' else [report.get('error')])
    raw=json.dumps(report,ensure_ascii=True,separators=(',',':')).encode()
    size=len(raw)+Path(__file__).stat().st_size
    p.require(size<RESERVE and size<p.CAPS['certificate_bytes'], 'program and complete receipt fit original reserve')
    p.require(time.monotonic()-start<SECONDS, 'bounded audit time')
    output=OUT/'source-comprehensions.json'
    with output.open('xb') as stream:
        stream.write(raw)
    print(json.dumps(dict(status=report['status'],omitted_inline_item_visits=report.get('omitted_inline_item_visits'),
        additional_omitted_visits=report.get('additional_omitted_visits'),
        audit_event_item_upper=sum(budget.values()),required_item_limit=LIMIT,
        artifact_bytes=size,required_reserve_bytes=RESERVE,failures=report['failures'],path=str(output))))


if __name__=='__main__':
    main()
