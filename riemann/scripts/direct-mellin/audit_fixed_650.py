"""Replay exactly the two existing L829 stages without rewriting their data.

The evaluator and its Decimal contract are reviewed in L829. This checks
every saved integrand range, not merely the sums verified by step648.
There is no additional point, order, precision or subdivision stage.
"""
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
from types import SimpleNamespace

BASE = Path(__file__).resolve().parent
OUT = BASE / 'fixed-laguerre-audit-650.json'
SOURCE = BASE / 'fixed-laguerre-certificate-648.json'


def load(name, filename):
    spec = importlib.util.spec_from_file_location(name, BASE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    cert = json.loads(SOURCE.read_text())
    evaluator = load('fixed648', 'fixed_laguerre_648.py')
    report = dict(status='INCOMPLETE', failures=[], stages=[],
                  source_sha256=sha(SOURCE), evaluator_sha256=sha(BASE/'fixed_laguerre_648.py'),
                  audit_sha256=sha(Path(__file__)), python=sys.version,
                  platform=platform.platform(), libmpdec=evaluator.decimal.__libmpdec_version__,
                  scope='Reviewed evaluator replay of all original cells and constants; same explicit Decimal backend assumption; necessary condition only')
    counts = []

    class CompareWriter:
        def __init__(self, path, mode, encoding):
            assert mode == 'wt' and encoding == 'utf-8'
            self.reader = gzip.open(path, 'rt', encoding=encoding)
            self.count = 0

        def __enter__(self):
            return self

        def write(self, value):
            old = self.reader.readline()
            assert old, 'replay has an extra cell'
            assert json.loads(old) == json.loads(value), f'cell mismatch at {self.count}'
            self.count += 1

        def __exit__(self, exc_type, exc, traceback):
            try:
                if exc_type is None:
                    assert self.reader.readline() == '', 'replay omitted saved cells'
                    counts.append(self.count)
            finally:
                self.reader.close()

    # Intercept the evaluator's output stream: compare each complete cell
    # against its existing record and preserve every step648 artifact.
    evaluator.gzip = SimpleNamespace(open=CompareWriter)
    replay = dict(stages=[])
    try:
        assert not cert['failures']
        assert report['evaluator_sha256'] == cert['program_sha256']
        for name, value in cert['input_sha256'].items():
            assert sha(evaluator.ROOT/name) == value, f'changed input: {name}'
        assert [(s['precision'], s['boxes']) for s in cert['stages']] == list(evaluator.STAGES)
        for index, old in enumerate(cert['stages']):
            path = evaluator.ROOT/old['quadrature']['cells_path']
            assert sha(path) == old['quadrature']['cells_sha256']
            decision = evaluator.run_stage(old['precision'], old['boxes'], replay)
            new = replay['stages'][-1]
            assert new == old, f'full stage mismatch: {index}'
            assert counts[-1] == old['boxes']
            report['stages'].append(dict(precision=old['precision'], boxes=old['boxes'],
                                         all_integrand_ranges_replayed=counts[-1],
                                         full_stage_equal=True, decision=decision,
                                         evaluation=new['evaluation'], bounds=new['bounds']))
            OUT.write_text(json.dumps(report, indent=2)+'\n')
            print('Stage replay:', old['precision'], old['boxes'], decision, flush=True)
        verifier = load('verify648', 'verify_recorded_648.py')
        verifier.OUT = BASE/'recorded-arithmetic-replay-650.json'
        verifier.main()
        exact = json.loads(verifier.OUT.read_text())
        assert exact['status'] == 'PASS' and not exact['failures']
        report['exact_arithmetic_report'] = str(verifier.OUT.relative_to(evaluator.ROOT))
        report['exact_arithmetic_sha256'] = sha(verifier.OUT)
        report['status'] = 'PASS'
    except Exception as exc:
        report['failures'].append(type(exc).__name__+': '+str(exc))
        raise
    finally:
        OUT.write_text(json.dumps(report, indent=2)+'\n')
        print('Audit:', report['status'], 'failures:', report['failures'],
              'report:', OUT.relative_to(evaluator.ROOT), flush=True)
        print('Required scalar > 0; original final enclosure: 0.0548305044439594 to 0.122500470818405', flush=True)


if __name__ == '__main__':
    main()
