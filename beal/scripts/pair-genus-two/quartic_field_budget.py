"""Persistent whole-step rational-operation charges, not bit-operation counts."""
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / 'quartic-field-ledger.json'
CAPS = dict(resolvent_root_branches=3, relative_factor_candidates=6,
            root_trials=250000, scalar_operations=500000,
            polynomial_degree=8, integer_bits=4096)


class Budget:
    def __init__(self, fresh=False):
        if fresh:
            if LEDGER.exists():
                raise RuntimeError('Preserve existing ledger; no implicit restart')
            self.data = dict(caps=CAPS, actual={k: 0 for k in CAPS},
                             phases=[], cap_stop=None)
            self.save()
        else:
            self.data = json.loads(LEDGER.read_text())
            assert self.data['caps'] == CAPS

    def save(self):
        LEDGER.write_text(json.dumps(self.data, indent=2) + '\n')

    def charge(self, key='scalar_operations', n=1):
        value = self.data['actual'][key] + n
        if value > CAPS[key]:
            self.data['cap_stop'] = key
            self.save()
            raise RuntimeError('Cap hit: ' + key)
        self.data['actual'][key] = value

    def observe(self, *values):
        for value in values:
            if isinstance(value, (list, tuple, set)):
                self.observe(*value)
                continue
            q = F(value)
            bits = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
            if bits > CAPS['integer_bits']:
                self.data['cap_stop'] = 'integer_bits'
                self.save()
                raise RuntimeError('Integer bit cap')
            self.data['actual']['integer_bits'] = max(
                bits, self.data['actual']['integer_bits'])

    def op(self, kind, a, b):
        self.charge()
        self.observe(a, b)
        if kind == '+':
            out = a + b
        elif kind == '-':
            out = a - b
        elif kind == '*':
            out = a * b
        elif kind == '/':
            out = F(a) / F(b)
        elif kind == '%':
            out = a % b
        elif kind == '//':
            out = a // b
        else:
            raise ValueError(kind)
        self.observe(out)
        return out

    def equal(self, a, b):
        if isinstance(a, (list, tuple, set)) and isinstance(b, (list, tuple, set)):
            if isinstance(a, set):
                a = sorted(a)
            if isinstance(b, set):
                b = sorted(b)
            if not self.equal(len(a), len(b)):
                return False
            return all(self.equal(x, y) for x, y in zip(a, b))
        self.charge()
        self.observe(a, b)
        return a == b

    def polynomial(self, coefficients):
        self.charge()  # processed coefficient row
        self.observe(*coefficients)
        degree = len(coefficients) - 1
        if degree > CAPS['polynomial_degree']:
            self.data['cap_stop'] = 'polynomial_degree'
            self.save()
            raise RuntimeError('Degree cap')
        self.data['actual']['polynomial_degree'] = max(
            degree, self.data['actual']['polynomial_degree'])
        return coefficients

    def phase(self, name):
        self.data['phases'].append(name)
        self.save()

    def summary(self):
        return dict(actual=self.data['actual'], required_caps=CAPS,
                    cap_stop=self.data['cap_stop'])
