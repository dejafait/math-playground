"""Step 489: one audited opposing-units caller, unchanged selected constructors."""
import sys
from pathlib import Path
import receive_positive_occurrence as driver
import parameterized_input as inputs
from empty_central_translation import install
from receive_selected_commutator import install_evidence_budget

TARGET = 'Test full nonzero-fJ reception on the audited opposing-units endpoint under the unchanged extraction and evidence caps.'
OUT = Path(__file__).resolve().parent / 'output-489'


def source_pins():
    """Match reused implementations to their previously audited saved versions."""
    old = inputs.load(driver.HERE / 'output-481/run-scope.json')['source_hashes']
    old.update(inputs.load(driver.HERE / 'output-483/audited-dependency-preservation.json'))
    checked = {}
    for name, expected in old.items():
        if not name.endswith('.py'):
            continue
        path = driver.ROOT / name if name.startswith('scripts/') else driver.HERE / name
        inputs.require(driver.digest(path.read_bytes()) == expected,
                       'previously audited source unchanged: ' + name)
        checked[driver.relative(path)] = expected
    for name in ('run_opposing_occurrence.py', 'verify_opposing_occurrence.py'):
        path = driver.HERE / name
        checked[driver.relative(path)] = driver.digest(path.read_bytes())
    for name in ('output-485/proof.jsonl', 'output-485/request.json',
                 'output-487/verified/verification.json', 'output-487/verified/binding.json'):
        path = driver.HERE / name
        checked[driver.relative(path)] = driver.digest(path.read_bytes())
    return checked


def main():
    driver.BASE = driver.HERE / 'output-461/final/opposing-units'
    driver.SUPPLIED = driver.HERE / 'output-485'
    driver.OUT = OUT
    hashes = source_pins()
    adapter = install(OUT / 'trace')
    original = inputs.write_json
    aliases = [name for name, module in list(sys.modules.items())
               if module is not None and getattr(module, 'write_json', None) is original]
    writer = install_evidence_budget(OUT)
    inputs.require(all(getattr(sys.modules[name], 'write_json') is writer for name in aliases),
                   'all observed writer aliases rebound')
    raw_emit = driver.emit_occurrence.emit

    def emit(**kw):
        # Driver creates the fresh output and immutable caller copies first.
        inputs.write_json(OUT / 'run-scope.json', dict(
            target=TARGET, source_hashes=hashes, caps=inputs.CAPS,
            caller_base=driver.relative(driver.BASE), supplied=driver.relative(driver.SUPPLIED),
            changed_operation='explicit opposing-units fixed caller and output provenance only',
            selected_constructor='empty_central_translation.EmptyCentral',
            entries=['m.witness', 'checked_witness'], constructors_unchanged=True,
            receivers_unchanged=True, caller_bytes_unchanged=True,
            writer_aliases=aliases, all_observed_writer_aliases_rebound=True,
            qualifications=['lexical paths; trusted caller paths and remaining SHA',
                            'not total work, memory, temporary storage or guaranteed recovery']))
        return raw_emit(**kw)

    driver.emit_occurrence.emit = emit
    driver.main()
    inputs.write_json(OUT / 'trace-summary.json', dict(events=len(adapter.events)))
    inputs.require(all(driver.digest((driver.ROOT / name).read_bytes()) == expected
                       for name, expected in hashes.items()), 'pinned sources unchanged after run')


if __name__ == '__main__':
    main()
