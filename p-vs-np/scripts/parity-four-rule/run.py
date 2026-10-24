"""One bounded preparation attempt; run from the active notebook.

Full artifacts stay in output/. No incomplete library is used by a compiler.
"""
import copy
import hashlib
import itertools
import json
from pathlib import Path
import time

import checker
import prepare as gen

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output'
ROOT = HERE.parent.parent


def relative(path):
    return str(path.relative_to(ROOT))


def save(name, value):
    path = OUT / name
    path.write_text(json.dumps(value, indent=2) + '\n')
    return relative(path)


def emitter_fixture_goal(data):
    cs = []
    for literals in data['clauses']:
        terms = [gen.N(s[2:-1]) if s.startswith('(~') and s.endswith(')') else s for s in literals]
        q = 'false'
        if terms:
            q = terms[-1]
            for a in reversed(terms[:-1]):
                q = gen.O(a, q)
        cs.append(q)

    def f(t):
        return cs[t] if type(t) is int else gen.And(f(t[0]), f(t[1]))

    return gen.N(f(data['global_tree']) if cs else 'true')


def checker_self_test():
    n, o = gen.N, gen.O
    a, b = 'A', 'B'
    ax = o(n(a), a)
    rows = [dict(rule='axiom', f=ax, refs=[]),
            dict(rule='true', f='true', refs=[]),
            dict(rule='not-false', f=n('false'), refs=[]),
            dict(rule='expansion', f=o(b, ax), refs=[0]),
            dict(rule='association', f=o(o(b, n(a)), a), refs=[3]),
            dict(rule='expansion', f=o(ax, ax), refs=[0]),
            dict(rule='contraction', f=ax, refs=[5]),
            dict(rule='axiom', f=o(n(n(a)), n(a)), refs=[]),
            dict(rule='cut', f=o(a, n(a)), refs=[0, 7])]
    path = OUT / 'checker-exercise.jsonl'
    gen.write_stream(path, rows, [a, b], rows[-1]['f'])
    base = checker.check(path, rows[-1]['f'])
    original = [json.loads(s) for s in path.read_text().splitlines()]
    results = []
    mutations = [
        ('axiom-argument', 1, 'f', a), ('true-constant', 2, 'f', 'false'),
        ('not-false-constant', 3, 'f', n('true')),
        ('expansion-argument', 4, 'f', o(a, b)),
        ('association-direction', 5, 'f', o(b, ax)),
        ('contraction-argument', 7, 'f', a), ('cut-premise-order', 9, 'refs', [7, 0]),
        ('forward-reference', 4, 'refs', [3]), ('boolean-reference', 4, 'refs', [True]),
        ('out-of-range', 4, 'refs', [999]), ('wrong-earlier-premise', 4, 'refs', [1]),
        ('missing-reference', 9, 'refs', [0]), ('extra-reference', 2, 'refs', [0]),
        ('MP-extra-rule', 9, 'rule', 'mp'), ('assumption-extra-rule', 1, 'rule', 'assume'),
        ('context-extra-rule', 5, 'rule', 'context'), ('bad-syntax', 1, 'f', ['and', a, b]),
        ('header-endpoint', 0, 'goal', 'true'), ('foreign-alphabet', 0, 'alphabet', ['B']),
    ]
    for name, at, key, value in mutations + [('last-endpoint', None, None, None)]:
        changed = copy.deepcopy(original)
        if at is None:
            # This record is itself legal: rejection must be at the final endpoint.
            changed.append(dict(rule='true', f='true', refs=[]))
        else:
            changed[at][key] = value
        bad = OUT / ('corrupt-' + name + '.jsonl')
        bad.write_text(''.join(json.dumps(r, separators=(',', ':')) + '\n' for r in changed))
        try:
            checker.check(bad, rows[-1]['f'])
            results.append(dict(case=name, rejected=False, path=relative(bad)))
        except checker.Invalid as err:
            results.append(dict(case=name, rejected=True, reason=str(err), path=relative(bad)))
    if not all(r['rejected'] for r in results):
        raise AssertionError('checker accepted corruption')
    return dict(valid_exercise=base, exercise_path=relative(path), corruptions=results,
                qualification='Checker exercise only; not a parity/compiler stream.')


def main():
    OUT.mkdir(exist_ok=True)
    # Persist declared bounds before any synthesis.
    save('budget.json', dict(limits=gen.LIMITS, target='L106 section 6 fixed union',
                            tactic='FIFO exact primitive saturation; target subterms and one negation layer as expansion images',
                            stop='first unprepared template; compiler is then NOT_REACHED'))
    tests = checker_self_test()
    save('checker-results.json', tests)
    fixtures = {}
    for label in ['zero-direct', 'zero-unused-rows', 'zero-conjunction', 'three-row']:
        old = HERE.parent / 'parity-source' / 'output' / (label + '-input.json')
        raw = old.read_bytes()
        data = json.loads(raw)
        copied = OUT / (label + '-input.json')
        copied.write_bytes(raw)
        readback = json.loads(copied.read_text())
        expected = checker.fixture_endpoint(readback)
        if expected != emitter_fixture_goal(readback):
            raise AssertionError('independent fixture reconstruction mismatch')
        ep = save(label + '-expected.json', expected)
        fixtures[label] = dict(status='NOT_REACHED', input_path=relative(copied),
                               original_sha256=hashlib.sha256(raw).hexdigest(),
                               exact_expected_path=ep, expected_nodes=checker.nodes(expected),
                               primitive_stream=None,
                               limitation='Input checks only: no L087 provenance or M/Q computation.')
    library = gen.manifest()
    manifest_path = save('library-manifest.json', dict(entries=library, count=len(library),
                         row_count=sum(e['id'].startswith('row-') for e in library),
                         convention='Literal expansions of L097 section 6.1 and L106 section 6.2; no constant simplification.'))
    save('fixture-results.json', fixtures)
    progress = []
    used_records, used_pairs = 0, 0
    started = time.monotonic()
    blocker = None
    for entry in library:
        remaining = dict(records=gen.LIMITS['library_records'] - used_records,
                         pairs=gen.LIMITS['library_cut_pairs'] - used_pairs,
                         seconds=max(0, gen.LIMITS['library_seconds'] - (time.monotonic() - started)))
        rows, result = gen.saturate(entry['target'], remaining)
        used_records += result['records']
        used_pairs += result['stats']['cut_pairs']
        stream = OUT / (entry['id'] + '-preparation.jsonl')
        actual_goal = rows[-1]['f']
        gen.write_stream(stream, rows, entry['slots'], actual_goal)
        check = checker.check(stream, actual_goal)
        result.update(id=entry['id'], target=entry['target'], stream_path=relative(stream),
                      independent_check=check,
                      endpoint_is_requested=actual_goal == entry['target'])
        progress.append(result)
        save('preparation-results.json', progress)
        print(json.dumps(dict(template=entry['id'], status=result['status'], reason=result['reason'],
                              records=result['records'], cut_pairs=result['stats']['cut_pairs'],
                              required='complete exact requested endpoint',
                              checked_records=check['records'], path=relative(stream))), flush=True)
        if result['status'] != 'PREPARED':
            blocker = save('first-unprepared.json', result)
            break
    summary = dict(task='bounded L106 direct source compiler implementation',
                   status='LIBRARY_PREPARATION_BLOCKED' if blocker else 'LIBRARY_PREPARED_COMPILER_NOT_IMPLEMENTED',
                   prepared_templates=sum(r['status'] == 'PREPARED' for r in progress),
                   required_templates=len(library), attempted_templates=len(progress),
                   total_records=used_records, cut_pairs=used_pairs,
                   library_elapsed_seconds=time.monotonic() - started,
                   complete_fixture_streams=0, required_fixture_streams=4,
                   manifest=manifest_path, first_unprepared=blocker,
                   checker_results='scripts/parity-four-rule/output/checker-results.json',
                   fixture_results='scripts/parity-four-rule/output/fixture-results.json',
                   limits=gen.LIMITS,
                   failures=['No complete primitive source compiler or fixture stream verified.'],
                   no_claims=['nonderivability', 'all-size implementation bound', 'H integration', 'SAT separation'])
    summary_path = save('summary.json', summary)
    print(json.dumps(dict(status=summary['status'], prepared=summary['prepared_templates'],
                          required=len(library), complete_fixtures=0, required_fixtures=4,
                          corruptions_rejected=len(tests['corruptions']), path=summary_path)), flush=True)


if __name__ == '__main__':
    main()
