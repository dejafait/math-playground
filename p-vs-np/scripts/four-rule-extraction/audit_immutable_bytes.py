"""Step 468: independent boundary/provenance review and read-only archive replay.

Run from the notebook root with PYTHONDONTWRITEBYTECODE=1.
Existing evidence is read in full; fresh artifacts go only to output-468.
"""
import ast
import collections
import contextlib
import copy
import hashlib
import json
import platform
from pathlib import Path

import parameterized_input as p
import test_immutable_bytes as h
import test_parameterized as driver
import occurrence_input as occurrence

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SAVED = HERE/'output-466'
OUT = HERE/'output-468'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path):
    return json.loads(path.read_bytes())


def write(name, value):
    p.write_json(OUT/name, value)


def relocate(x):
    if type(x) is str:
        return x.replace('output-466', 'output-468')
    if type(x) is list:
        return [relocate(v) for v in x]
    if type(x) is dict:
        return {k: relocate(v) for k, v in x.items()}
    return x


def ast_equal(a, b):
    assert ast.dump(a) == ast.dump(b)


def module_review():
    pinned = load(HERE/'output-464/dependency-preservation.json')['code_checks']
    results = {}
    changed = {'scripts/parity-four-rule/checker.py': 'checker-before.py',
               'scripts/four-rule-extraction/parameterized_input.py': 'parameterized_input-before.py'}
    for name, evidence in pinned.items():
        path = SAVED/changed[name] if name in changed else ROOT/name
        actual = digest(path)
        assert actual == evidence['actual'] == evidence['recorded']
        results[name] = dict(path=str(path.relative_to(ROOT)), sha256=actual)
    for name, recorded in load(SAVED/'verification.json')['scripts'].items():
        assert digest(ROOT/name) == recorded
    old = ast.parse((SAVED/'checker-before.py').read_text())
    new = ast.parse(h.CHECKER.read_text())
    old_check = next(x for x in old.body if isinstance(x, ast.FunctionDef) and x.name == 'check')
    new_check = next(x for x in new.body if isinstance(x, ast.FunctionDef) and x.name == 'check')
    # Verify wrapper operations separately, including normalization before open.
    expected = ast.parse('''def check(path, expected):
    expected = tree(json.loads(json.dumps(expected)))
    with Path(path).open('rb') as stream:
        return _check_stream(stream, expected)
''').body[0]
    wrapper = copy.deepcopy(new_check)
    wrapper.body = wrapper.body[1:]  # Only the documented docstring.
    assert isinstance(new_check.body[0], ast.Expr) and isinstance(new_check.body[0].value, ast.Constant)
    ast_equal(wrapper, expected)
    ast_equal(old_check.body[0], expected.body[0])
    # Restore the old check and remove only the two new functions and io import.
    restored = copy.deepcopy(new)
    restored.body = [old_check if isinstance(x, ast.FunctionDef) and x.name == 'check' else x
                     for x in restored.body
                     if not (isinstance(x, ast.FunctionDef) and x.name in ('check_bytes','_check_stream'))
                     and not (isinstance(x, ast.Import) and ast.dump(x) == ast.dump(ast.parse('import io').body[0]))]
    ast_equal(restored, old)
    engine = h.equivalent_engine()
    occurrence_hashes = load(HERE/'output-464/verified/verification.json')['source_hashes']
    for name, evidence in occurrence_hashes.items():
        assert digest(HERE/name) == evidence['actual'] == evidence['snapshot'] == evidence['recorded']
    return dict(pinned_baselines_and_dependencies=results, occurrence_hashes=occurrence_hashes,
                full_unchanged_module_ast=True, legacy_wrapper_ast=True, engine=engine)


def independent_receipts(checks):
    out = []
    for item in checks['fixtures'] + checks['framing']:
        if not item['immutable_bytes']['accepted']:
            continue
        raw = (HERE/item['path']).read_bytes()
        # Use explicit LF segmentation, not the checker's iteration or splitlines.
        lines = raw.split(b'\n')
        if lines[-1] == b'':
            lines.pop()
        header, *rows = [json.loads(line) for line in lines]
        def size(tree):
            return 1 if isinstance(tree, str) else 1 + sum(size(c) for c in tree[1:])
        expected = dict(accepted=True, records=len(rows),
                        rule_counts=dict(collections.Counter(r['rule'] for r in rows)),
                        formula_nodes=sum(size(r['f']) for r in rows), bytes=len(raw),
                        sha256=hashlib.sha256(raw).hexdigest())
        assert p.exact_equal(expected, item['immutable_bytes']['receipt'])
        out.append(dict(path=item['path'], independently_reconstructed=expected))
    return out


def replay():
    driver.OUT = OUT/'replay'
    driver.OUT.mkdir()
    with (OUT/'replay.log').open('w') as log, contextlib.redirect_stdout(log):
        driver.main()
    summary = load(driver.OUT/'summary.json')
    old_summary = load(SAVED/'regression-comparison.json')['summary']
    assert p.exact_equal(summary, old_summary)
    for name in ('mutation-results.json', 'regressions.json', 'accepted-cases.json'):
        assert p.exact_equal(load(driver.OUT/name), relocate(load(SAVED/'replay'/name)))
    compared = []
    for item in load(driver.OUT/'accepted-cases.json'):
        name = item['name']
        for file in ('source.jsonl','request.json','certificate.json'):
            assert (driver.OUT/name/file).read_bytes() == (SAVED/'replay'/name/file).read_bytes()
            assert (driver.OUT/name/file).read_bytes() == (HERE/'output-457'/name/file).read_bytes()
        for file in ('construction.json','reception.json'):
            assert p.exact_equal(load(driver.OUT/name/file), relocate(load(SAVED/'replay'/name/file)))
        receipt = load(driver.OUT/name/'reception.json')
        compared.append(dict(name=name, roots=len(receipt['roots']), blocks=len(receipt['blocks']),
                             complete_receipt_equal=True, certificate_bytes_equal=True))
    return dict(summary=summary, complete_comparisons=compared)


def retained_authorization(races):
    old = load(HERE/'output-459/authorization-checks.json')['checks']
    white = next(x for x in races if x['test']=='whitespace')
    assert not white['result']['accepted'] and white['result']['reason']==old[0]['reason']
    assert len(white['reads'])==old[0]['reads']==2
    assert white['reads'][0]['sha256']==old[0]['original_sha256']
    assert white['reads'][1]['sha256']==old[0]['second_read_sha256']
    foreign = h.verdict(lambda:h.receiver.receive(HERE/'output-457/singleton/certificate.json',
                       HERE/'output-457/old-nonzero/source.jsonl',HERE/'output-457/old-nonzero/request.json'))
    assert foreign == dict(accepted=False, exception='Rejected', reason=old[1]['reason'])
    assert p.exact_equal(foreign, load(SAVED/'regression-comparison.json')['foreign_caller'])
    # A focused bind_K unit exercise is not positive occurrence reception.
    base = HERE/'output-457/old-nonzero'
    raw = (base/'source.jsonl').read_bytes()
    req = load(base/'request.json')
    ctx = dict(raw=dict(proof=raw.decode()),manifest=dict(proof=hashlib.sha256(raw).hexdigest()),request=req)
    cert = load(base/'certificate.json')
    occurrence.bind_K(cert,ctx)
    mutations = []
    for name, field, replacement in [
        ('K-binding-changed-proof-text','source_text',cert['source_text']+'\n'),
        ('K-binding-changed-proof-digest','source_sha256','0'*64),
        ('K-binding-changed-dictionary-order','dictionary',dict(cert['dictionary'],
            placeholders=list(reversed(cert['dictionary']['placeholders']))))]:
        candidate = copy.deepcopy(cert)
        candidate[field] = replacement
        result = h.verdict(lambda:occurrence.bind_K(candidate,ctx))
        assert not result['accepted'] and result['exception']=='Rejected'
        mutations.append(dict(name=name, result=result))
    result = h.verdict(lambda:occurrence.bind_K(load(HERE/'output-457/singleton/certificate.json'),ctx))
    mutations.append(dict(name='K-binding-actual-other-caller', result=result))
    retained = {x['name']:x for x in load(HERE/'output-464/verified/verification.json')['rejections']}
    for item in mutations:
        assert item['result']==dict(accepted=False,exception='Rejected',reason=retained[item['name']]['reason'])
    return dict(step459_checks=old,foreign_caller=foreign,bind_K_units=mutations,
                qualification='Generic-fixture bind_K unit checks only; no positive occurrence composition.')


def main():
    OUT.mkdir(exist_ok=False)
    # Read exactly the archived manifest's paths, plus the archive under review.
    prior = load(SAVED/'archives-before.json')
    for name, expected in prior.items():
        assert digest(Path(name)) == expected
    protected = {str(path):digest(path) for path in SAVED.rglob('*') if path.is_file()}
    protected.update(prior)
    write('archives-before.json', protected)
    for file in ('checker-before.py','parameterized_input-before.py'):
        (OUT/file).write_bytes((SAVED/file).read_bytes())
    h.OUT = OUT
    write('module-review.json', module_review())
    old = h.module('step468_old',SAVED/'checker-before.py')
    new = h.module('step468_new',h.CHECKER)
    checks = h.checker_tests(old,new)
    write('checker-tests.json',checks)
    assert p.exact_equal(checks,relocate(load(SAVED/'checker-tests.json')))
    write('independent-receipts.json',independent_receipts(checks))
    races = h.guarded_reads()
    write('guarded-reads.json',races)
    assert p.exact_equal(races,load(SAVED/'guarded-reads.json'))
    write('authorization.json',retained_authorization(races))
    replay_result = replay()
    write('regression-comparison.json',replay_result)
    after = {name:digest(Path(name)) for name in protected}
    assert protected == after
    write('archive-preservation.json',dict(files=len(after),unchanged=True,hashes=after))
    result = dict(accepted=True,failures=[],python=platform.python_version(),
                  fixtures=len(checks['fixtures']),framing_cases=len(checks['framing']),
                  primitive_endpoint_rejections=len(checks['primitive_rejections']),
                  cap_type_rejections=len(checks['preparse_cap_and_type_rejections']),
                  guarded_read_cases=len(races),bind_K_rejections=4,
                  replay_accepted=6,replay_roots=35,replay_rejections=47,
                  protected_files=len(after),source_bytes_actual_max=824,source_bytes_required=p.CAPS['input_bytes'],
                  read_requested=2000001,oversize_returned=2000001,oversize_limit=2000000,
                  script_sha256=digest(Path(__file__)),
                  limitations=['Finite reviewed boundary only; no total interpreter/latency bound',
                               'Trusted paths and remaining SHA assumptions; no post-read change detection',
                               'No positive occurrence proof/composition, proof-existence or SAT conclusion'])
    write('verification.json',result)
    print(json.dumps(dict(result,evidence=str(OUT/'verification.json'))))


if __name__=='__main__':
    try:
        main()
    except Exception as error:
        if OUT.exists():
            write('failure.json',dict(accepted=False,failure=repr(error)))
        raise
