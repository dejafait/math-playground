"""One fresh step-477 supplied-proof integration under all original caps."""
from pathlib import Path
import receive_positive_occurrence as driver
from trimming_translation import install
from parameterized_input import CAPS, write_json

TARGET = ('Integrate source-to-sink trimming before each L035 call in the '
          'scalar-aware supplied-proof run and independently receive complete '
          'K/H under unchanged caps.')


def main():
    driver.OUT = Path(__file__).resolve().parent / 'output-477'
    adapter = install(driver.OUT / 'trace')
    names = ('run_trimmed_occurrence.py', 'trimming_translation.py',
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
        'output-473/trace/event-00201.json')]
    hashes = {driver.relative(p): driver.digest(p.read_bytes()) for p in paths}
    raw_emit = driver.emit_occurrence.emit

    def emit(**kw):
        write_json(driver.OUT / 'run-scope.json', dict(
            target=TARGET, source_hashes=hashes, caps=CAPS,
            changed_operation='path restriction of both operands before every L035 call',
            entries=['m.witness', 'checked_witness'],
            scalar_translation_unchanged=True, constructors_unchanged=True,
            receivers_unchanged=True, caller_bytes_unchanged=True,
            reused_driver='receive_positive_occurrence.py'))
        return raw_emit(**kw)

    driver.emit_occurrence.emit = emit
    driver.main()
    write_json(driver.OUT / 'trace-summary.json', dict(events=len(adapter.events)))
    assert all(driver.digest((driver.ROOT / p).read_bytes()) == h for p,h in hashes.items())


if __name__ == '__main__':
    main()
