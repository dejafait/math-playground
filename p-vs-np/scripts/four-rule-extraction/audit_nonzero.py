"""Step 455: preserve and critically replay the fixed step-453 evidence only.

Arithmetic independence is the inspected forward/backward pair; rebuilding
uses the constructor and does not constitute independent algebraic evidence.
"""
import contextlib
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import shutil

HERE = Path(__file__).resolve().parent
NOTEBOOK = HERE.parents[1]
OLD = HERE / 'output-453'
OUT = HERE / 'output-455'
CAPS = dict(records=2_000_000, certificate_bytes=200_000_000,
            polynomial_words=1_000_000, word_length=256,
            multiplication_pairs=100_000_000, stored_words=20_000_000)


def demand(ok, message):
    if not ok:
        raise AssertionError(message)


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def read(p):
    return json.loads(p.read_bytes())


def typed(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'))


def write(name, value):
    (OUT / name).write_text(json.dumps(value, indent=2) + '\n')


def main():
    OUT.mkdir(exist_ok=True)
    previous = read(OLD / 'verification.json')
    paths = {NOTEBOOK / p for p in read(OLD / 'preserved-input-hashes.json')}
    paths.update(p for p in OLD.rglob('*') if p.is_file())
    paths.update(NOTEBOOK / p for p in previous['code_sha256'])
    paths.add(HERE / 'nonzero-source.jsonl')
    before = {str(p.relative_to(NOTEBOOK)): digest(p) for p in sorted(paths)}
    write('preserved-input-hashes.json', before)
    for p, sha in previous['code_sha256'].items():
        demand(digest(NOTEBOOK / p) == sha, 'retained program hash ' + p)
    for p, sha in read(OLD / 'preserved-input-hashes.json').items():
        demand(digest(NOTEBOOK / p) == sha, 'older archive hash ' + p)
    demand(digest(OLD / 'certificate.json') == previous['certificate_sha256'],
           'retained certificate hash')
    demand((OLD / 'source.jsonl').read_bytes() ==
           (HERE / 'nonzero-source.jsonl').read_bytes(), 'complete fixed source copy')

    r = module('audit455_receiver', HERE / 'receive_nonzero.py')
    demand(r.CAPS == CAPS, 'receiver caps')
    replayed = r.receive(OLD / 'certificate.json', OLD / 'source.jsonl')
    saved = read(OLD / 'reception.json')
    demand(typed({k: v for k, v in replayed.items() if k != 'arithmetic'}) ==
           typed({k: v for k, v in saved.items() if k != 'arithmetic'}),
           'entire saved backward reception')
    c = module('audit455_forward', HERE / 'check_nonzero.py')
    c.counters(replayed['arithmetic'], saved['arithmetic'])
    write('backward-reception.json', replayed)

    e = module('audit455_emitter', HERE / 'emit_nonzero.py')
    demand(e.CAPS == CAPS == c.CAPS, 'constructor and forward caps')
    e.OUT = OUT / 'rebuilt'
    log = io.StringIO()
    with contextlib.redirect_stdout(log):
        e.main()
    for name in ('certificate.json', 'source.jsonl'):
        demand((e.OUT / name).read_bytes() == (OLD / name).read_bytes(),
               'byte-identical rebuild ' + name)

    # Run the inspected forward arithmetic and all diagnostics in new files.
    c.OUT = OUT / 'replay'
    c.OUT.mkdir(exist_ok=True)
    for name in ('certificate.json', 'source.jsonl', 'reception.json',
                 'preserved-input-hashes.json'):
        shutil.copyfile(OLD / name, c.OUT / name)
    scratch = dict(max_unreduced_counter_words=0, max_unreduced_word_length=0)
    original_reduced = c.reduced

    def measured_reduced(counter):
        scratch['max_unreduced_counter_words'] = max(
            scratch['max_unreduced_counter_words'], len(counter))
        scratch['max_unreduced_word_length'] = max(
            scratch['max_unreduced_word_length'], max(map(len, counter), default=0))
        demand(scratch['max_unreduced_counter_words'] <= CAPS['polynomial_words'],
               'unreduced scratch word cap')
        demand(scratch['max_unreduced_word_length'] <= CAPS['word_length'],
               'unreduced scratch length cap')
        return original_reduced(counter)

    c.reduced = measured_reduced
    with contextlib.redirect_stdout(log):
        c.main()
    for name in ('independent-polynomials.json', 'contributions.json'):
        demand(typed(read(c.OUT / name)) == typed(read(OLD / name)),
               'complete forward evidence ' + name)
    new_report = read(c.OUT / 'verification.json')
    demand(new_report['actual'] == previous['actual'], 'all six actual counts')
    demand(new_report['required'] == previous['required'] == CAPS, 'all six required caps')
    demand(new_report['construction'] == previous['construction'], 'construction counters')

    original_tests = read(OLD / 'mutation-results.json')
    new_tests = read(c.OUT / 'mutation-results.json')
    for group, pathkey in (('certificate_tests', 'certificate_path'), ('source_tests', 'path')):
        demand(len(original_tests[group]) == len(new_tests[group]), 'mutation count ' + group)
        for old, new in zip(original_tests[group], new_tests[group]):
            demand(typed({k: v for k, v in old.items() if k != pathkey}) ==
                   typed({k: v for k, v in new.items() if k != pathkey}),
                   'complete mutation verdict/difference ' + old['case'])
            p, q = NOTEBOOK / old[pathkey], NOTEBOOK / new[pathkey]
            demand(digest(p) == old['sha256'] == digest(q), 'complete mutation bytes ' + old['case'])

    cert = read(OLD / 'certificate.json')
    # Check the complete edit sets, including unchanged metadata and connectors.
    internal_edits = {}
    for name, indexes, symbol, block in (
        ('delete-selected-cut-seed', [9179, 9268], 'tau:A:B', 12),
        ('delete-selected-sigma-B', [29], 'sigma:B', 1)):
        damaged = read(OLD / 'mutations' / (name + '.json'))
        differences = c.changed(cert, damaged)
        expected = [dict(pointer=f'/graph/edges/{i}/2', before=[symbol], after=[])
                    for i in indexes]
        demand(differences == expected, 'only intended internal edits ' + name)
        first, last = cert['blocks'][block]['edge_range']
        demand(all(first <= i < last - 2 for i in indexes), 'internal edge bounds')
        internal_edits[name] = differences
    write('internal-edit-audit.json', internal_edits)

    # Preserve and distinguish the old connector-disable probe. It is not a
    # substitute for the two internal-label deletion receptions above.
    connector_path = OLD / 'connector-diagnostic' / 'connector-disabled-cut.json'
    connector = read(connector_path)
    connector_changes = c.changed(cert, connector)
    try:
        r.receive(connector_path, OLD / 'source.jsonl')
        raise AssertionError('connector mutation accepted')
    except r.Rejected as err:
        connector_reason = str(err)
    demand(connector_reason == 'exact block connectors', 'connector syntax distinction')
    c.stats = dict(multiplication_pairs=0, max_polynomial_words=0,
                   max_word_length=0, max_stored_words=0)
    g = connector['graph']
    connector_polys = {m: c.serial(c.forward(g['vertices'], g['edges'], 0, m)[g['sink']])
                       for m in c.MODES}
    demand(connector_polys['axioms'] != saved['roots'][8]['target'],
           'connector damaged final identity')
    write('connector-replay.json', dict(changes=connector_changes, reason=connector_reason,
          final_polynomials=connector_polys, arithmetic=c.stats, caps=CAPS))

    demand(all(digest(NOTEBOOK / p) == sha for p, sha in before.items()),
           'all originals preserved byte for byte')
    report = dict(accepted=True, roots=9, blocks=15, nonzero_contributions=2,
                  byte_identical_rebuild=True, expected_certificate_rejections=24,
                  expected_source_rejections=14, neutral_acceptances=1,
                  actual=new_report['actual'], required=CAPS,
                  backward_arithmetic=replayed['arithmetic'],
                  forward_arithmetic=new_report['actual'],
                  construction=e.CONSTRUCTION, unreduced_scratch=scratch,
                  connector_arithmetic=c.stats, preserved_files=len(before),
                  certificate_sha256=digest(OLD / 'certificate.json'),
                  code_sha256={**previous['code_sha256'],
                               str(Path(__file__).relative_to(NOTEBOOK)): digest(Path(__file__))},
                  failures=[], limitations=['fixed finite fixture only',
                  'source checker shared; literal rules separately inspected',
                  'rebuild authenticates constructor counters, not independent mathematics',
                  'all-size executable efficiency and short-proof availability not established'])
    write('audit.json', report)
    (OUT / 'replay-log.txt').write_text(log.getvalue())
    print(json.dumps({k: report[k] for k in ('accepted', 'roots', 'blocks',
          'nonzero_contributions', 'expected_certificate_rejections',
          'expected_source_rejections', 'neutral_acceptances', 'failures')}))
    print('Actual/required:', typed(dict(actual=report['actual'], required=CAPS)))
    print('Unreduced scratch:', typed(scratch))
    print('Complete audit:', OUT / 'audit.json')


if __name__ == '__main__':
    try:
        main()
    except Exception as err:
        OUT.mkdir(exist_ok=True)
        write('audit-failure.json', dict(failure=repr(err), caps=CAPS))
        raise
