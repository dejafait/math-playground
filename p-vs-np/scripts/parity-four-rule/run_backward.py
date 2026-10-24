"""Step-447 bounded test. Preserves every earlier output directory."""
import hashlib
import json
from pathlib import Path
import time

import backward
import checker
import prepare
import run as old_run

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'output-goal-directed-447'


def save(name, value):
    path = OUT / name
    path.write_text(json.dumps(value, indent=2) + '\n')
    return str(path.relative_to(ROOT))


def main():
    OUT.mkdir(exist_ok=True)
    save('budget.json', dict(limits=backward.LIMITS,
                            tactic='Goal-directed backward primitive AND/OR search; Boolean pruning; fixed subterm pivots',
                            stop='first unprepared template; no cap increases or FIFO fallback',
                            target='L106 section 6 source-only compiler',
                            required=dict(library=72, complete_fixtures=4)))
    old_run.OUT = OUT
    tests = old_run.checker_self_test()
    save('checker-results.json', tests)
    library = prepare.manifest()
    manifest = save('library-manifest.json', dict(count=len(library), entries=library))
    saved = json.loads((HERE / 'output' / 'first-unprepared.json').read_text())
    assert checker.tree(saved['target']) == library[1]['target']
    fixtures = {}
    for label in ['zero-direct', 'zero-unused-rows', 'zero-conjunction', 'three-row']:
        raw = (HERE.parent / 'parity-source' / 'output' / (label + '-input.json')).read_bytes()
        path = OUT / (label + '-input.json')
        path.write_bytes(raw)
        data = json.loads(path.read_text())
        expected = checker.fixture_endpoint(data)
        assert expected == old_run.emitter_fixture_goal(data)
        fixtures[label] = dict(status='NOT_REACHED', input_sha256=hashlib.sha256(raw).hexdigest(),
                               input_path=str(path.relative_to(ROOT)), expected=expected,
                               qualification='Input/endpoint check only; no primitive fixture stream.')
    fixture_path = save('fixture-results.json', fixtures)
    results = []
    start = time.monotonic()
    states = 0
    for entry in library:
        rows, report = backward.synthesize(entry['target'],
                         backward.LIMITS['library_seconds'] - (time.monotonic() - start),
                         backward.LIMITS['library_states'] - states)
        states += report['stats']['states']
        path = OUT / (entry['id'] + '-preparation.jsonl')
        actual = rows[-1]['f']
        prepare.write_stream(path, rows, entry['slots'], actual)
        report.update(id=entry['id'], independent_check=checker.check(path, actual),
                      path=str(path.relative_to(ROOT)), endpoint_is_requested=actual == entry['target'])
        results.append(report)
        save('preparation-results.json', results)
        print(json.dumps(dict(id=entry['id'], status=report['status'], reason=report['reason'],
                              records=report['records'], states=report['stats']['states'],
                              seconds=round(report['seconds'], 3),
                              required='complete exact primitive endpoint', path=report['path'])), flush=True)
        if report['status'] != 'PREPARED':
            save('first-unprepared.json', report)
            break
    summary = dict(status='LIBRARY_PREPARATION_BLOCKED' if results[-1]['status'] != 'PREPARED'
                          else 'LIBRARY_PREPARED_COMPILER_NOT_IMPLEMENTED',
                   prepared_templates=sum(r['status'] == 'PREPARED' for r in results),
                   required_templates=len(library), complete_fixture_streams=0,
                   required_fixture_streams=4, attempted_templates=len(results),
                   total_states=states, total_records=sum(r['records'] for r in results),
                   elapsed_seconds=time.monotonic() - start,
                   corruptions_rejected=sum(r['rejected'] for r in tests['corruptions']),
                   manifest=manifest, fixture_results=fixture_path,
                   preparation_results='scripts/parity-four-rule/output-goal-directed-447/preparation-results.json',
                   failure='No complete fixture compiler or stream verified.',
                   route='Park concrete preparation if blocked under this second tactic.',
                   no_claims=['nonderivability', 'all-size implementation bound', 'H integration', 'SAT transfer'])
    path = save('summary.json', summary)
    print(json.dumps(dict(status=summary['status'], prepared=summary['prepared_templates'],
                          required=summary['required_templates'], complete_fixtures=0,
                          required_fixtures=4, corruptions_rejected=summary['corruptions_rejected'],
                          path=path)), flush=True)


if __name__ == '__main__':
    main()
