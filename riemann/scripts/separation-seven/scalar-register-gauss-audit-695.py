#!/usr/bin/env python3
"""Source-directed replay of694; intercept all writes to existing artifacts.

All numerical/control statements are the original AST. Only the transcript
sink and terminal serialization are replaced. This is a correspondence
check, not a second independently implemented inclusion proof. The complete
independent rational checks are692/694, bound here by hashes.
"""
import ast
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import gzip
import json

HERE = Path(__file__).resolve()
BASE = HERE.parent
SOURCE = BASE / 'scalar-register-gauss-694.py'
CERT = SOURCE.with_suffix('.json')
TRACE = SOURCE.with_suffix('.trace.jsonl.gz')
OUT = HERE.with_suffix('.json')
counts = Counter()
failures = []
report = {'result': 'INCOMPLETE', 'failures': failures}


def ck(value, name):
    counts[name] += 1
    if not value:
        failures.append(name)
        raise AssertionError(name)


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def zi(value):
    return int(value['odd_hex'], 16) << value['shift']


def rf(value):
    return Fraction(zi(value['num']), zi(value['den']))


class Sink:
    def __init__(self):
        self.stream = gzip.open(TRACE, 'rt')
        self.lines = 0
        self.inventory = Counter()
        self.previous = None
        self.closed = False
        self.cost = 0

    def write(self, text):
        # Every emit/mark/output writes exactly one JSON line.
        ck(text.count('\n') == 1 and text.endswith('\n'), 'one complete emitted event')
        actual = json.loads(text)
        expected_line = self.stream.readline()
        ck(bool(expected_line), 'saved transcript event exists')
        expected = json.loads(expected_line)
        ck(actual == expected, 'entire source event equals saved event')
        self.lines += 1
        op = actual[0]
        self.inventory[op] += 1
        if op == '/':
            ck(self.previous == ['compare', '!=', actual[3], 1, True],
               'every division immediately follows its counted nonzero guard')
        self.cost += 2 if op in ('+', '-', '*', '/') else int(op in ('literal', 'copy', 'compare'))
        self.previous = actual

    def close(self):
        ck(self.stream.readline() == '', 'source consumes entire saved transcript')
        self.stream.close()
        self.closed = True


try:
    data = json.loads(CERT.read_text())
    replay_path = BASE / 'scalar-register-gauss-replay-694.json'
    replay = json.loads(replay_path.read_text())
    old_path = BASE / 'certified-gauss-adaptive-692.json'
    old = json.loads(old_path.read_text())
    oldreplay_path = BASE / 'certified-gauss-adaptive-replay-692.json'
    oldreplay = json.loads(oldreplay_path.read_text())
    ck(data['script_sha256'] == digest(SOURCE), '694 source hash matches constructed certificate')
    ck(data['trace_sha256'] == digest(TRACE) == replay['trace_sha256'], '694 trace bound to full replay')
    ck(replay['source_sha256'] == digest(CERT), '694 complete certificate bound to replay')
    ck(replay['script_sha256'] == digest(BASE / 'scalar-register-gauss-replay-694.py'), '694 replay source unchanged')
    ck(replay['failures'] == [] and replay['result'] == 'PASS_FULL_TRANSCRIPT_AND_ALL_EXACT_TRACE_VALUES', '694 full rational replay passed')
    ck(replay['old_accuracy_source_sha256'] == digest(old_path), '694 binds692 accuracy certificate')
    ck(replay['old_accuracy_replay_sha256'] == digest(oldreplay_path), '694 binds692 full replay')
    ck(oldreplay['source_certificate_sha256'] == digest(old_path), '692 accuracy source binding')
    ck(oldreplay['script_sha256'] == digest(BASE / 'certified-gauss-adaptive-replay-692.py'), '692 replay source unchanged')
    ck(oldreplay['failures'] == [] and oldreplay['result'] == 'PASS_COMPLETE_RECORDED_TRACE', '692 full accuracy replay passed')

    tree = ast.parse(SOURCE.read_text(), filename=str(SOURCE))
    engine = next(node for node in tree.body if isinstance(node, ast.ClassDef) and node.name == 'Engine')
    init = next(node for node in engine.body if isinstance(node, ast.FunctionDef) and node.name == '__init__')
    sink_assignment = init.body[0]
    ck(ast.unparse(sink_assignment) == "self.file = gzip.open(TRACE, 'wt')", 'only transcript creation replaced')
    sink_assignment.value = ast.Name(id='_audit_sink', ctx=ast.Load())
    # Preserve all program logic and in-memory report formation through324.
    # Lines325 onward only hash/serialize/print the already formed report.
    kept = [node for node in tree.body if node.lineno <= 324]
    ck(ast.unparse(kept[-1]) == "report['guard_counts'] = dict(E.guards)", 'serialization cutoff after full service')
    removed = [node for node in tree.body if node.lineno > 324]
    report['excluded_terminal_source'] = [ast.unparse(node) for node in removed]
    tree.body = kept
    ast.fix_missing_locations(tree)
    sink = Sink()
    namespace = {'__file__': str(SOURCE), '__name__': '__audit__', '_audit_sink': sink}
    exec(compile(tree, str(SOURCE), 'exec'), namespace)
    ck(sink.closed, 'source closed intercepted stream')
    regenerated = namespace['report']
    expected = {key: value for key, value in data.items() if key not in ('script_sha256', 'trace_sha256')}
    ck(regenerated == expected, 'entire regenerated report equals original694')
    ck(regenerated['rows'] == old['rows'], 'entire regenerated mathematical trace equals692')
    ck(dict(sink.inventory) == replay['instruction_inventory'], 'independent event inventory agrees')
    ck(sink.lines == replay['transcript_lines'], 'every instruction marker and output consumed')
    ck(sink.cost == regenerated['scalar_work']['complete_register_cost'] == 3290939, 'source-directed scalar cost exact')
    ck(sink.cost <= 5000000, 'complete setup cap')
    pairs = 0
    max_nr = max_wr = Fraction(0)
    degrees = []
    for row in regenerated['rows']:
        degrees.append(row['degree'])
        entries = []
        for root in row['positive_roots']:
            entries += [root['final'], {'node': root['negative_node'], 'weight': root['negative_weight']}]
        entries.append(row['zero_node'])
        ck(len(entries) == row['degree'], 'complete degree output list')
        for entry in entries:
            bounds = []
            for kind in ('node', 'weight'):
                lo, hi = map(rf, entry[kind])
                ck(lo <= hi, 'each output interval ordered')
                radius = (hi-lo)/2
                ck(radius <= Fraction(1, 2**512), 'each separate output radius passes')
                bounds.append(radius)
            max_nr = max(max_nr, bounds[0]); max_wr = max(max_wr, bounds[1])
            pairs += 1
    ck(degrees == [63,81,117] and pairs == 261, 'all degrees and261 pairs')
    ck(Fraction(1,2**552) < max_nr <= Fraction(1,2**551), 'complete maximum node dyadic bracket')
    ck(Fraction(1,2**543) < max_wr <= Fraction(1,2**542), 'complete maximum weight dyadic bracket')
    report.update(result='PASS_SOURCE_CORRESPONDENCE_AND_SCALAR_THRESHOLDS',
                  complete_source_events=sink.lines, instruction_inventory=dict(sink.inventory),
                  scalar_work=sink.cost, required_upper=5000000, headroom=5000000-sink.cost,
                  output_pairs=pairs, maximum_node_radius_upper='2^-551',
                  maximum_weight_radius_upper='2^-542', required_separate_radius='2^-512',
                  original_artifact_writes=0,
                  qualification='Full source correspondence; relies on the separately inspected692/694 complete rational replays and canonical analytic/control-flow proofs in C998o. Not a bit-complexity assertion.')
except Exception as exc:
    if not failures:
        failures.append(type(exc).__name__ + ': ' + str(exc))
    report['result'] = 'FAIL'
report.update(check_counts=dict(counts), total_checks=sum(counts.values()),
              source_sha256=digest(SOURCE), certificate_sha256=digest(CERT),
              trace_sha256=digest(TRACE), script_sha256=digest(HERE))
OUT.write_text(json.dumps(report, indent=2)+'\n')
print(report['result'])
print('Checks:', report['total_checks'], '; failures:', failures)
print('Scalar work:', report.get('scalar_work'), '; required <=5000000; separate radii <=2^-512')
print('Outputs:', report.get('output_pairs'), '; actual radius bounds:', report.get('maximum_node_radius_upper'), report.get('maximum_weight_radius_upper'))
print('Full audit:', OUT.relative_to(HERE.parents[2]))
if failures:
    raise SystemExit(1)
