"""Persistent whole-attempt charges; no claim about internal elementary steps."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / 'degree-three-branch-ledger.json'
CAPS = dict(prime_visits=25, divisor_trials=250000, work_units=1000000,
            polynomial_degree=12, integer_bits=4096)


class Budget:
    def __init__(self, fresh=False):
        if fresh:
            if LEDGER.exists():
                raise RuntimeError('Preserve existing ledger; no implicit restart')
            self.data = dict(caps=CAPS, actual=dict(prime_visits=0,
                divisor_trials=0, work_units=0, polynomial_degree=0,
                integer_bits=0), phases=[], cap_stop=None)
            self.save()
        else:
            self.data = json.loads(LEDGER.read_text())
            assert self.data['caps'] == CAPS

    def save(self):
        LEDGER.write_text(json.dumps(self.data, indent=2) + '\n')

    def charge(self, kind='work_units', n=1):
        a = self.data['actual']
        if a[kind] + n > CAPS[kind]:
            self.data['cap_stop'] = kind
            self.save()
            raise RuntimeError('Cap stop: ' + kind)
        a[kind] += n
        self.save()

    def scalar(self, *values):
        self.charge()
        for x in values:
            bits = abs(int(x)).bit_length()
            if bits > CAPS['integer_bits']:
                raise RuntimeError('Integer bit cap')
            self.data['actual']['integer_bits'] = max(
                self.data['actual']['integer_bits'], bits)
        self.save()

    def polynomial(self, coeffs):
        # Observing an input/output is a processed row as well as a size check.
        self.charge()
        degree = len(coeffs) - 1
        if degree > CAPS['polynomial_degree']:
            raise RuntimeError('Polynomial degree cap')
        self.data['actual']['polynomial_degree'] = max(
            self.data['actual']['polynomial_degree'], degree)
        self.scalar(*coeffs)

    def phase(self, name):
        self.data['phases'].append(name)
        self.save()

    def summary(self):
        return dict(actual=self.data['actual'], required_caps=CAPS,
                    cap_stop=self.data['cap_stop'])
