"""One fresh step-481 supplied-proof integration under all original caps."""
from pathlib import Path
import receive_positive_occurrence as driver
from empty_central_translation import install
from parameterized_input import CAPS, write_json
from receive_selected_commutator import install_evidence_budget

TARGET = ('Integrate literal-empty-central branch omission into every L035 call of the retained step-470/461 extraction, preserving all caps and requiring complete K/H reception.')


def main():
    driver.OUT = Path(__file__).resolve().parent / 'output-481'
    adapter = install(driver.OUT / 'trace')
    install_evidence_budget(driver.OUT)
    names = ('run_empty_central_occurrence.py', 'empty_central_translation.py',
             'verify_empty_central_occurrence.py', 'receive_selected_commutator.py',
             'trimming_translation.py',
             'verify_trimmed_occurrence.py', 'trim_saved_operands.py',
             'constant_translation.py', 'verify_constant_translation.py',
             'receive_positive_occurrence.py', 'emit_parameterized.py',
             'receive_parameterized.py', 'parameterized_input.py',
             'emit_occurrence.py', 'receive_occurrence.py', 'occurrence_input.py')
    paths = [driver.HERE / name for name in names]
    paths += [driver.HERE.parent / name for name in (
        'alternative-abp-commutator/check_marked_edges.py',
        'affine-abp-boolean/check_suffix_graph.py', 'parity-four-rule/checker.py')]
    paths += [driver.HERE / name for name in (
        'output-475/trimmed-pair.json', 'output-475/reception.json',
        'output-473/trace/event-00201.json',
        'output-479/inputs.json', 'output-479/inventory.json',
        'output-479/candidate.json', 'output-479/reference.json',
        'output-479/reception.json', 'output-477/stop-check.json',
        'output-477/integration-reception.json')]
    hashes = {driver.relative(p): driver.digest(p.read_bytes()) for p in paths}
    raw_emit = driver.emit_occurrence.emit

    def emit(**kw):
        write_json(driver.OUT / 'run-scope.json', dict(
            target=TARGET, source_hashes=hashes, caps=CAPS,
            changed_operation='path restriction then literal-empty-central omission before every L035 call',
            entries=['m.witness', 'checked_witness'],
            scalar_translation_unchanged=True, Boolean_constructor_unchanged=True, L035_constructor_changed=True,
            receivers_unchanged=True, caller_bytes_unchanged=True,
            reused_driver='receive_positive_occurrence.py'))
        return raw_emit(**kw)

    driver.emit_occurrence.emit = emit
    driver.main()
    write_json(driver.OUT / 'trace-summary.json', dict(events=len(adapter.events)))
    assert all(driver.digest((driver.ROOT / p).read_bytes()) == h for p,h in hashes.items())


if __name__ == '__main__':
    main()
