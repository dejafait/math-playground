"""Shared persistent accounting only; contains no field/lattice algorithms.

The two arithmetic scripts have numeric binary operations, comparisons,
sum and modular pow expanded through this API. Container operations and
control bookkeeping are excluded. Fraction normalization and bit operations
are not claimed as elementary scalar charges.
"""
import json
from fractions import Fraction
from pathlib import Path
import operator

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / 'quartic-order-ledger.json'
CAPS = dict(factor_trials=250000, strict_enlargements=128,
            scalar_operations=2000000, field_dimension=4, integer_bits=4096)
OPS = {'+': operator.add, '-': operator.sub, '*': operator.mul,
       '/': operator.truediv, '//': operator.floordiv, '%': operator.mod,
       '**': operator.pow, '>>': operator.rshift, '<<': operator.lshift,
       '&': operator.and_, '|': operator.or_}
CMPS = {'==': operator.eq, '!=': operator.ne, '<': operator.lt,
        '<=': operator.le, '>': operator.gt, '>=': operator.ge,
        'in': lambda a, b: a in b, 'not in': lambda a, b: a not in b,
        'is': operator.is_, 'is not': operator.is_not}


class Budget:
    def __init__(self):
        if LEDGER.exists():
            self.data = json.loads(LEDGER.read_text())
            assert self.data['caps'] == CAPS
            if self.data['cap_stop']:
                raise RuntimeError('Earlier cap stop is final for this attempt')
        else:
            self.data = dict(caps=CAPS, actual={k: 0 for k in CAPS},
                             phases=[], failures=[], cap_stop=None)
            self.data['actual']['field_dimension'] = 4
            self.save()

    def save(self):
        LEDGER.write_text(json.dumps(self.data, indent=2) + '\n')

    def charge(self, key='scalar_operations', n=1):
        if self.data['actual'][key] + n > CAPS[key]:
            self.data['cap_stop'] = key
            self.save()
            raise RuntimeError('Cap hit: ' + key)
        self.data['actual'][key] += n

    def observe(self, value):
        if isinstance(value, dict):
            for v in value.values():
                self.observe(v)
        elif isinstance(value, (list, tuple)):
            for v in value:
                self.observe(v)
        elif isinstance(value, (int, Fraction)):
            q = Fraction(value)
            bits = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
            if bits > CAPS['integer_bits']:
                self.data['cap_stop'] = 'integer_bits'
                self.save()
                raise RuntimeError('4096-bit cap hit')
            self.data['actual']['integer_bits'] = max(bits, self.data['actual']['integer_bits'])

    def op(self, symbol, a, b):
        numeric = isinstance(a, (int, Fraction)) and isinstance(b, (int, Fraction))
        if numeric:
            self.charge()
            self.observe(a)
            self.observe(b)
        value = OPS[symbol](a, b)
        if numeric:
            self.observe(value)
        return value

    def rational(self, numerator=0, denominator=None):
        if denominator is not None:
            self.charge()
            self.observe(numerator)
            self.observe(denominator)
            value = Fraction(numerator, denominator)
        else:
            value = Fraction(numerator)
        self.observe(value)
        return value

    def cmp(self, symbol, a, b):
        if symbol in ('==', '!=') and isinstance(a, (list, tuple)) and isinstance(b, (list, tuple)):
            same = self.cmp('==', len(a), len(b))
            if same:
                same = all(self.cmp('==', x, y) for x, y in zip(a, b))
            return same if symbol == '==' else not same
        if isinstance(a, (int, Fraction)) and isinstance(b, (int, Fraction)):
            self.charge()
            self.observe(a)
            self.observe(b)
        return CMPS[symbol](a, b)

    def scalar_sum(self, values, start=0):
        for value in values:
            start = self.op('+', start, value)
        return start

    def modpow(self, a, exponent, modulus):
        # Negative exponent is used only for prime-field inverse.
        if exponent == -1:
            old_r, r, old_s, s = modulus, a % modulus, 0, 1
            self.charge(n=2)
            while r:
                q = self.op('//', old_r, r)
                old_r, r = r, self.op('-', old_r, self.op('*', q, r))
                old_s, s = s, self.op('-', old_s, self.op('*', q, s))
            if not self.cmp('==', old_r, 1):
                raise ValueError('Nonunit modular inverse')
            return self.op('%', old_s, modulus)
        result = 1
        a = self.op('%', a, modulus)
        while exponent:
            if self.op('&', exponent, 1):
                result = self.op('%', self.op('*', result, a), modulus)
            exponent = self.op('>>', exponent, 1)
            if exponent:
                a = self.op('%', self.op('*', a, a), modulus)
        return result

    def phase(self, name):
        self.data['phases'].append(name)
        self.save()

    def failure(self, detail):
        self.data['failures'].append(detail)
        self.save()

    def summary(self):
        return dict(actual=self.data['actual'], required_caps=CAPS,
                    cap_stop=self.data['cap_stop'], failures=self.data['failures'])
