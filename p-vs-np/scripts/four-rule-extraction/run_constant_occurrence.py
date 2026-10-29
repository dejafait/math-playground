"""One fresh fixed-cap run; reuse step-471 caller/failure retention driver."""
from pathlib import Path
import receive_positive_occurrence as driver
from constant_translation import install
from parameterized_input import write_json

TARGET = 'Implement a bounded constant-aware original-only translation for the retained 31-record occurrence proof, preserving exact ordered polynomials, caller data and existing caps.'


def main():
    driver.OUT = Path(__file__).resolve().parent / 'output-473'
    # The reused driver refuses to overwrite OUT and creates it before emission.
    adapter = install(driver.OUT / 'trace')
    paths = [Path(__file__), Path(__file__).with_name('constant_translation.py'),
             driver.HERE.parent / 'alternative-abp-commutator/check_marked_edges.py']
    hashes = {driver.relative(p): driver.digest(p.read_bytes()) for p in paths}
    driver.main()
    write_json(driver.OUT / 'run-scope.json', dict(
        target=TARGET, source_hashes=hashes, events=len(adapter.events),
        changed_operation='only original-only formula translation',
        constructors_unchanged=True, caps_unchanged=True,
        reused_driver='receive_positive_occurrence.py',
        note='The reused preflight records its original receiver target; this file records this run target.'))
    assert all(driver.digest((driver.ROOT / p).read_bytes()) == h for p,h in hashes.items())


if __name__ == '__main__':
    main()
