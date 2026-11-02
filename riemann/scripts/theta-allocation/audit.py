"""Instrumented replay of L609's single existing certificate; no search.

Inclusion proofs are in L609. This records runtime evidence, not a formal
verification of Decimal or an independent numerical integration algorithm.
"""
import decimal
import hashlib
import importlib.util
import json
import platform
from pathlib import Path
import sys
import time


def main():
    directory = Path(__file__).resolve().parent
    original_path = directory / 'certificate.json'
    before_bytes = original_path.read_bytes()
    saved_path = directory / 'certificate-before-independent-audit.json'
    if saved_path.exists():
        assert json.loads(saved_path.read_bytes()) == json.loads(before_bytes), 'preserve earlier audit evidence'
    else:
        saved_path.write_bytes(before_bytes)
    before_bytes = saved_path.read_bytes()
    before = json.loads(before_bytes)
    spec = importlib.util.spec_from_file_location('l609_certificate', directory / 'certify.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # Module-level pi and tail calculations have already set sticky flags;
    # do not clear them before checking the whole run.
    telemetry = {'intervals_constructed': 0, 'zero_straddling_intervals': 0,
                 'smallest_nonzero_adjusted_exponent': None,
                 'largest_nonzero_adjusted_exponent': None,
                 'division_calls': 0, 'smallest_denominator_magnitude': None,
                 'exponential_calls': 0, 'exponential_input_min': None,
                 'exponential_input_max': None,
                 'kernel_calls_by_order': [0, 0, 0]}
    init = module.I.__init__
    divide = module.I.__truediv__
    exp = module.I.exp
    kernel = module.kernel

    def record_init(self, lo, hi=None):
        init(self, lo, hi)
        telemetry['intervals_constructed'] += 1
        if self.lo <= 0 <= self.hi:
            telemetry['zero_straddling_intervals'] += 1
        for value in (self.lo, self.hi):
            if value:
                adjusted = value.adjusted()
                low = telemetry['smallest_nonzero_adjusted_exponent']
                high = telemetry['largest_nonzero_adjusted_exponent']
                if low is None or adjusted < low:
                    telemetry['smallest_nonzero_adjusted_exponent'] = adjusted
                if high is None or adjusted > high:
                    telemetry['largest_nonzero_adjusted_exponent'] = adjusted

    def record_divide(self, other):
        other = module.cv(other)
        assert other.lo > 0 or other.hi < 0
        separation = min(other.lo.copy_abs(), other.hi.copy_abs())
        telemetry['division_calls'] += 1
        previous = telemetry['smallest_denominator_magnitude']
        if previous is None or separation < previous:
            telemetry['smallest_denominator_magnitude'] = separation
        return divide(self, other)

    def record_exp(self):
        telemetry['exponential_calls'] += 1
        previous = telemetry['exponential_input_min']
        if previous is None or self.lo < previous:
            telemetry['exponential_input_min'] = self.lo
        previous = telemetry['exponential_input_max']
        if previous is None or self.hi > previous:
            telemetry['exponential_input_max'] = self.hi
        return exp(self)

    def record_kernel(u, order=0):
        telemetry['kernel_calls_by_order'][order] += 1
        return kernel(u, order)

    module.I.__init__ = record_init
    module.I.__truediv__ = record_divide
    module.I.exp = record_exp
    module.kernel = record_kernel
    assert module.POLYS == [(0, -12, 8), (0, -30, 60, -16),
                           (0, -75, 330, -224, 32)]
    started = time.monotonic()
    module.main()
    elapsed = time.monotonic() - started
    after_bytes = original_path.read_bytes()
    after = json.loads(after_bytes)
    flags = {name: {signal.__name__: value for signal, value in ctx.flags.items()}
             for name, ctx in [('DN', module.DN), ('UP', module.UP), ('RN', module.RN)]}
    failures = []
    if before != after:
        failures.append('replay differs from preserved complete certificate')
    for name, signals in flags.items():
        for signal, raised in signals.items():
            if raised and signal not in ('Inexact', 'Rounded'):
                failures.append(f'{name}: unexpected arithmetic signal {signal}')
    if telemetry['kernel_calls_by_order'] != [18432, 1, 2048]:
        failures.append('unexpected cell/derivative evaluation counts')
    enclosures = after['enclosures']
    for key in ('k_a', 'Z'):
        if decimal.Decimal(enclosures[key][0]) <= 0:
            failures.append(f'{key} lower bound is not positive')
    if decimal.Decimal(enclosures['G'][1]) >= 0:
        failures.append('normalized G upper bound is not strictly negative')
    normalized = module.I(*enclosures['G'])
    report = {
        'status': 'AUDIT_REPLAY_PASS' if not failures else 'AUDIT_REPLAY_FAILED',
        'scope': 'existing x=11, a=7/16 certificate only; no new candidate',
        'independent_replay_runs': 1,
        'historical_run_counter_scope': 'Original calculation counter retained verbatim; it excludes this independent audit replay.',
        'runtime': {'python': sys.version, 'implementation': platform.python_implementation(),
                    'decimal_module': decimal.__file__,
                    'decimal_class_module': decimal.Decimal.__module__,
                    'decimal_version': decimal.__version__,
                    'libmpdec_version': decimal.__libmpdec_version__,
                    'c_backend_identity': decimal.Decimal is __import__('_decimal').Decimal,
                    'contexts': {name: str(ctx) for name, ctx in
                                 [('DN', module.DN), ('UP', module.UP), ('RN', module.RN)]},
                    'signals': flags, 'elapsed_seconds': elapsed},
        'telemetry': {key: str(value) if isinstance(value, decimal.Decimal) else value
                      for key, value in telemetry.items()},
        'complete_certificate_identical': before == after,
        'complete_certificate_byte_identical': before_bytes == after_bytes,
        'original_sha256': hashlib.sha256(before_bytes).hexdigest(),
        'replayed_sha256': hashlib.sha256(after_bytes).hexdigest(),
        'executable_sha256': hashlib.sha256((directory / 'certify.py').read_bytes()).hexdigest(),
        'preserved_certificate': saved_path.name,
        'complete_replayed_certificate': after,
        'normalized_G_radius_upper': str(normalized.radius()),
        'required_upper_bound': '0', 'actual_upper_bound': enclosures['G'][1],
        'failures': failures}
    report_path = directory / 'independent-audit.json'
    report_path.write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({key: report[key] for key in
                      ['status', 'complete_certificate_identical', 'actual_upper_bound',
                       'required_upper_bound', 'normalized_G_radius_upper', 'failures']}, indent=2))
    print(f'Full audit certificate: {report_path}')
    assert not failures, failures


if __name__ == '__main__':
    main()
