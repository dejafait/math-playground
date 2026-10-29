"""Independently reconcile the entire step-513 scalar-helper summary."""
import ast
from collections import Counter
import json
from pathlib import Path
import time

import parameterized_input as p

HERE = Path(__file__).resolve().parent
OUT = HERE/'output-513'


def main():
    start = time.monotonic()
    budget = Counter()
    report = dict(status='IN_PROGRESS', failures=[], actual_internal_cost='UNKNOWN')
    probe = None

    def tick(kind, n=1):
        p.require(sum(budget.values())+n <= 90_000_000, 'reconciliation selected budget')
        budget[kind] += n
        if budget[kind] % 4096 == 0:
            p.require(time.monotonic()-start <= 800, 'reconciliation timer')

    def read(path):
        size = path.stat().st_size
        p.require(size <= p.CAPS['input_bytes'], 'small selected input cap')
        tick('read_bytes', size)
        body = path.read_bytes()
        p.require(len(body) == size, 'read size')
        return body

    def same(a, b):
        tick('complete_comparison_nodes')
        if type(a) is not type(b):
            return False
        if type(a) is dict:
            return a.keys() == b.keys() and all(same(a[k], b[k]) for k in a)
        if type(a) in (list, tuple):
            return len(a) == len(b) and all(same(x, y) for x, y in zip(a, b))
        return a == b

    try:
        p.require(not (OUT/'receipt-check.json').exists() and not (OUT/'check-program.py').exists(), 'exclusive reconciliation')
        (OUT/'check-program.py').write_bytes(Path(__file__).read_bytes())
        probe = json.loads(read(OUT/'source-helpers.json'))
        p.require(probe['status'] == 'SCALAR_HELPER_DELIVERIES_RECEIVED' and not probe['failures'], 'probe success')
        raw = read(HERE/'output-489/inputs/proof.jsonl')
        req_raw = read(HERE/'output-489/inputs/request.json')
        req = ast.literal_eval(req_raw.decode('ascii'))
        header, *rows = [ast.literal_eval(line.decode('ascii')) for line in raw.splitlines()]
        p.require(same(req, json.loads(req_raw)) and same([header]+rows,
                  [json.loads(line) for line in raw.splitlines()]), 'full independent finite decoded inputs')
        m, n, d = len(rows), len(req['alphabet']), len(req['dictionary']['placeholders'])
        p.require((m, n, d) == (212, 6, 21), 'fixed cardinalities')

        containers, json_depth = 0, 0

        def json_walk(value, depth=0):
            nonlocal containers, json_depth
            tick('json_value_nodes')
            if type(value) in (dict, list):
                containers += 1
                json_depth = max(json_depth, depth+1)
                for child in (value.values() if type(value) is dict else value):
                    json_walk(child, depth+1)

        for value in [req, header]+rows:
            json_walk(value)
        leaves, formula_sizes, formula_depths = Counter(), [], []

        def formula(value):
            tick('formula_nodes')
            if type(value) is str:
                leaves[value] += 1
                return 1, 1
            p.require(type(value) is list and ((len(value) == 2 and value[0] == 'not') or
                      (len(value) == 3 and value[0] == 'or')), 'formula syntax')
            children = [formula(child) for child in value[1:]]
            return 1+sum(size for size, _ in children), 1+max(depth for _, depth in children)

        for tree in [req['goal']]+[row['f'] for row in rows]:
            size, depth = formula(tree)
            formula_sizes.append(size)
            formula_depths.append(depth)
        total_nodes, leaf_count = sum(formula_sizes), sum(leaves.values())
        names = leaves+Counter(req['alphabet'])+Counter(x['name'] for x in req['dictionary']['placeholders'])
        integers = [j for row in rows for j in row['refs']]
        expected_sites = {
            'bound <- read_bytes:88':3, 'bound <- read_bytes:91':3,
            'bound <- parse:78':containers, 'bound <- request:138':1,
            'bound <- request:149':1, 'bound <- request:186':m,
            'bound <- name:99':sum(names.values()),
            'bound <- check_tree:105':total_nodes, 'bound <- check_tree:107':total_nodes,
            'name <- request:140':n, 'name <- request:157':d, 'name <- check_tree:109':leaf_count,
            'integer <- <genexpr>:184':len(integers),
            'require <- parse:81':containers, 'require <- parse:82':m+2,
            'require <- no_duplicates:49':sum(len(x) for x in [req,req['dictionary'],header]+req['dictionary']['placeholders']+rows),
            'require <- fields:31':m+d+3,
            'require <- name:98':sum(names.values()),
            'require <- check_tree:112':total_nodes-leaf_count, 'require <- check_tree:110':leaf_count,
            'require <- parse_integer:57':len(integers), 'require <- input_bounds:218':1}
        for line in (131,133,136,143,147,151,168,170,173,176,187,193,196):
            expected_sites['require <- request:'+str(line)] = 1
        for line, count in ((141,n),(158,d),(160,d),(163,d),(167,d),(182,m),(183,m)):
            expected_sites['require <- request:'+str(line)] = count
        bound_count = sum(value for key, value in expected_sites.items() if key.startswith('bound <-'))
        expected_sites['require <- bound:24'] = bound_count
        p.require(same(probe['actual_call_sites'], expected_sites), 'every complete helper caller count')
        expected_calls = dict(bound=bound_count, require=sum(v for k,v in expected_sites.items() if k.startswith('require <-')),
                              name=sum(names.values()), integer=len(integers))
        p.require(same(probe['calls'], expected_calls) and same(probe['returns'], expected_calls), 'all helper calls/returns')
        p.require(same(probe['name_frequencies'], dict(names)) and same(probe['integer_arguments'], integers), 'all name/ref values')
        p.require(same(probe['argument_positions'], dict(bound=bound_count,name=sum(names.values()),integer=len(integers))), 'all ordered oracle positions')

        expected_groups = {}

        def group(resource, stage, count, minimum, maximum):
            expected_groups[resource+' | '+stage] = dict(calls=count, minimum=minimum, maximum=maximum, required=p.CAPS[resource])

        for filename, body, count in (('request.json',req_raw,1),('proof.jsonl',raw,2)):
            path = HERE/'output-489/inputs'/filename
            for prefix in ('file size before read: ', 'bounded read: '):
                group('input_bytes',prefix+str(path),count,len(body),len(body))
        group('json_depth','JSON nesting before parse',containers,1,json_depth)
        group('alphabet','alphabet length',1,n,n)
        group('dictionary_entries','dictionary cardinality before pair allocation',1,d,d)
        group('name_bytes','name bytes',sum(names.values()),min(len(x.encode()) for x in names),max(len(x.encode()) for x in names))
        group('tree_depth','formula tree depth',total_nodes,1,max(formula_depths))
        group('tree_nodes','formula nodes',total_nodes,1,max(formula_sizes))
        group('tree_nodes','aggregate source/request nodes',m,formula_sizes[0]+formula_sizes[1],total_nodes)
        p.require(same(probe['bound_groups'], expected_groups), 'all bound groups with actual/required values')
        p.require(total_nodes == probe['independent_tree_nodes'] == probe['input_bounds']['actual']['tree_nodes'], 'tree totals')
        original = json.loads(read(HERE/'output-502/preflight.json'))
        p.require(same(probe['original_source_observer'], original['source_observer']) and probe['original_source_visits'] == 167322, 'entire original observer')
        expected_charge_keys = {helper+':'+event for helper in expected_calls for event in ('call','line','return')}
        p.require(set(probe['direct_original_charges']) == expected_charge_keys and
                  all(value == 0 for value in probe['direct_original_charges'].values()), 'all helper-event zero deltas')
        p.require(probe['audit_item_event_units'] == sum(probe['audit_budget'].values()) and
                  probe['partial_augmented_source_items'] == 168943 and probe['partial_augmented_original_three_run_items'] == 75868982
                  and probe['dispatches_added_to_original_item_subtotal'] is False, 'disjoint selected measures')
        for name, live in (('preflight_job7_transport.py',HERE/'preflight_job7_transport.py'),
                           ('parameterized_input.py',Path(p.__file__)),
                           ('literal-checker.py',HERE.parent/'parity-four-rule/checker.py'),
                           ('audit-program.py',HERE/'audit_job7_source_helpers.py')):
            p.require(read(OUT/name) == read(live), 'whole program snapshot')
        p.require(same(probe['caps'],p.CAPS) and probe['total_work_bound'] is False and probe['actual_internal_cost'] == 'UNKNOWN', 'retained qualifications')
        report.update(status='PASS', checks='Every site/call/return, bound range, name frequency, reference value, observer field, source snapshot and budget sum reconciled.',
                      helper_calls=expected_calls, json_containers=containers, formula_nodes=total_nodes,
                      formula_leaves=leaf_count, distinct_bound_groups=len(expected_groups))
    except Exception as error:
        import traceback
        report.update(status='FAILED', failures=[dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc())])
    report.update(reconciliation_budget=dict(budget),reconciliation_selected_units=sum(budget.values()),
                  cumulative_selected_units=(probe['audit_item_event_units'] if probe else 0)+sum(budget.values()),
                  required_selected_units=100_000_000,elapsed_seconds=time.monotonic()-start,
                  cumulative_measured_seconds=(probe['elapsed_seconds'] if probe else 0)+time.monotonic()-start,
                  required_seconds=900,cumulative_charged_evidence_bytes=0,required_reserve_bytes=1_000_000,
                  total_internal_cost='UNKNOWN')
    fixed = (probe['program_snapshots_and_receipt_bytes'] if probe else 0)+Path(__file__).stat().st_size+(OUT/'check-program.py').stat().st_size
    while True:
        body = json.dumps(report,separators=(',',':')).encode()
        total = fixed+len(body)
        if report['cumulative_charged_evidence_bytes'] == total:
            break
        report['cumulative_charged_evidence_bytes'] = total
    p.require(report['cumulative_selected_units'] <= 100_000_000 and total <= 1_000_000 and report['cumulative_measured_seconds'] <= 900, 'complete audit ceilings')
    with (OUT/'receipt-check.json').open('xb') as stream:
        stream.write(body)
    print(json.dumps(dict(status=report['status'],actual_units=report['cumulative_selected_units'],required_units=100_000_000,
                          actual_evidence_bytes=total,required_reserve_bytes=1_000_000,failures=report['failures'],path=str(OUT/'receipt-check.json'))))
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
