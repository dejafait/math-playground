"""Separate audit of L151's assembly imports and complete isolated replay.

Imports audited ranks/loci; does not rerun historical mathematical searches.
Only absolute diagnostic paths and their dependent certificate digest are
normalized when comparing the complete relocated outputs.
"""
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import ast
import json
import shutil
import subprocess
import sys

BASE = Path(__file__).resolve().parent
ROOT = BASE.parent.parent


def digest(path):
    h = sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    return json.loads(path.read_bytes())


def normalize(value, root):
    if isinstance(value, str):
        return value.replace(str(root), '<NOTEBOOK>')
    if isinstance(value, list):
        return [normalize(v, root) for v in value]
    if isinstance(value, dict):
        return {k: normalize(v, root) for k, v in value.items()}
    return value


def run():
    out = dict(step_id='2026-10-24-mca-463-l151-critical-audit',
               checks=[], failures=[], inputs={}, canonical_manifests=[],
               runs=[], complete_output_comparisons=[])

    def check(name, value):
        out['checks'].append(dict(name=name, passes=bool(value)))
        if not value:
            raise ValueError(name)

    try:
        check('assertions enabled', __debug__)
        programs = ['new_pair_complete_assembly.py', 'verify_new_pair_complete_assembly.py']
        outputs = ['new-pair-complete-assembly.json', 'new-pair-complete-assembly-replay.json']
        cert, replay = [read(BASE / n) for n in outputs]
        check('saved complete successes', all(a['failures'] == a['uncovered'] == [] and
              all(c['passes'] is True for c in a['checks']) for a in [cert, replay]))
        check('saved program and output bindings', cert['producer_sha256'] == digest(BASE / programs[0]) and
              replay['verifier_sha256'] == digest(BASE / programs[1]) and
              replay['producer_certificate_sha256'] == digest(BASE / outputs[0]))
        check('complete frozen source cardinality', len(cert['source_hashes']) == 567)
        for name, value in cert['source_hashes'].items():
            check('frozen source ' + name, (ROOT / name).resolve().is_relative_to(ROOT) and
                  digest(ROOT / name) == value)
        names = set(cert['source_hashes']) | {'scripts/seven-coordinate/' + n for n in programs + outputs +
                 ['new-pair-complete-assembly-initial-schema-failure.json']}
        out['inputs'] = {n: digest(ROOT / n) for n in sorted(names)}
        for name in programs:
            tree = ast.parse((BASE / name).read_text())
            modules = {node.module if isinstance(node, ast.ImportFrom) else alias.name
                       for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))
                       for alias in node.names}
            check('standalone imports ' + name, modules <=
                  {'collections', 'hashlib', 'itertools', 'pathlib', 'json', 're'})

        # Bind every entry of every canonical manifest, not just output headlines.
        manifests = {}
        for number in range(125, 151):
            audit = read(BASE / f'l{number}-critical-audit.json')
            maps = [audit[k] for k in ['inputs', 'input_sha256', 'audited_input_hashes'] if k in audit]
            check('unique manifest schema ' + str(number), len(maps) == 1 and bool(maps[0]))
            manifest = {}
            for name, value in maps[0].items():
                path = (BASE / name).resolve()
                check('canonical local path ' + str(number) + '/' + name, path.is_relative_to(ROOT))
                relative = str(path.relative_to(ROOT))
                expected = value['sha256'] if isinstance(value, dict) else value
                check('canonical manifest entry ' + str(number) + '/' + name,
                      cert['source_hashes'][relative] == expected == digest(path))
                manifest[relative] = expected
            manifests[number] = manifest
            out['canonical_manifests'].append(dict(lemma=f'L{number}', entries=manifest))
        master = read(BASE / 'new-pair-filter.json')
        check('L125 exact master and every shard audited', all('scripts/seven-coordinate/' + n in manifests[125]
              for n in ['new-pair-filter.json'] + [t['certificate'] for t in master['thirds']]))
        for number, name in [(142, 'l141-survivor-full-rows.json'), (150, 'l149-survivor-full-rows.json')]:
            check('exact capacity audit membership ' + str(number),
                  'scripts/seven-coordinate/' + name in manifests[number])
        check('26 exact audit bindings', len(cert['audit_bindings']) == 26 and
              [a['lemma'] for a in cert['audit_bindings']] == [f'L{n}' for n in range(125, 151)] and
              all(a['sha256'] == digest(BASE / a['path']) and a['manifest_entries'] == len(manifests[n])
                  for n, a in zip(range(125, 151), cert['audit_bindings'])))
        check('historical schema failure retained',
              read(BASE / 'new-pair-complete-assembly-initial-schema-failure.json')['failures'] ==
              [dict(type='KeyError', message="'shard'")])

        with TemporaryDirectory(prefix='l151-audit-', dir=BASE) as temporary:
            isolated = Path(temporary) / 'notebook'
            for name in sorted(names):
                target = isolated / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, target)
            log = BASE / 'l151-critical-audit-replay.log'
            with log.open('w') as stream:
                for name in programs:
                    result = subprocess.run([sys.executable, '-E', '-B',
                        str(isolated / 'scripts/seven-coordinate' / name)], cwd=isolated,
                        text=True, capture_output=True)
                    stream.write(name + '\n' + result.stdout + result.stderr)
                    stream.flush()
                    out['runs'].append(dict(program=name, returncode=result.returncode,
                                            stdout=result.stdout, stderr=result.stderr))
                    check('isolated execution ' + name, result.returncode == 0)
            rebuilt = [read(isolated / 'scripts/seven-coordinate' / n) for n in outputs]
            for old, fresh, name in zip([cert, replay], rebuilt, outputs):
                check('fresh complete successes ' + name, fresh['failures'] == fresh['uncovered'] == [] and
                      all(c['passes'] is True for c in fresh['checks']))
                original_normalized = normalize(old, ROOT)
                fresh_normalized = normalize(fresh, isolated)
                if name == outputs[1]:
                    check('fresh replay binds relocated producer', fresh['producer_certificate_sha256'] ==
                          digest(isolated / 'scripts/seven-coordinate' / outputs[0]))
                    original_normalized['producer_certificate_sha256'] = '<CHECKED-PRODUCER-DIGEST>'
                    fresh_normalized['producer_certificate_sha256'] = '<CHECKED-PRODUCER-DIGEST>'
                equal = original_normalized == fresh_normalized
                out['complete_output_comparisons'].append(dict(output=name, complete_equal=equal,
                    original_sha256=digest(BASE / name),
                    isolated_sha256=digest(isolated / 'scripts/seven-coordinate' / name),
                    normalization='absolute notebook diagnostic paths; replay producer digest checked separately'))
                check('entire relocated output ' + name, equal)
            check('all isolated frozen inputs unchanged', all(digest(isolated / n) == h
                  for n, h in cert['source_hashes'].items()))
        check('every original artifact unchanged', all(digest(ROOT / n) == h for n, h in out['inputs'].items()))
        check('full target counts', cert['summary']['actual_thirds'] == replay['summary']['actual_thirds'] == 382 and
              cert['summary']['actual_occurrences'] == replay['summary']['actual_occurrences'] == 100764 and
              cert['summary']['covered_residuals'] == replay['summary']['residuals_checked'] == 154 and
              len(cert['exchanges']) == 77)
        out['original_artifacts_byte_unchanged'] = True
        out['summary'] = dict(actual_thirds=382, required_thirds=382, actual_occurrences=100764,
            required_occurrences=100764, residual_bindings=154, required_residual_bindings=154,
            exchanged_pairs=77, frozen_sources=567, bound_originals=len(out['inputs']), uncovered=0)
    except Exception as error:
        out['failures'].append(dict(type=type(error).__name__, message=str(error)))
    out['audit_code_sha256'] = digest(Path(__file__))
    target = BASE / 'l151-critical-audit.json'
    target.write_text(json.dumps(out, separators=(',', ':')) + '\n')
    print(json.dumps(out.get('summary', {}), sort_keys=True))
    print('Checks:', len(out['checks']), 'Failures:', len(out['failures']), 'Certificate:', target)
    if out['failures']:
        print(out['failures'][0])
        raise SystemExit(1)


if __name__ == '__main__':
    run()
