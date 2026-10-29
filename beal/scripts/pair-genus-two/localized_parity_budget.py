"""Persistent fixed-test bounds. Counts row/witness XORs, not scalar work."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PATH = ROOT / 'localized-parity-ledger.json'
CAPS = dict(row_xors=20000, witness_xors=20000, mask_bits=256, input_rows=189)

class Budget:
    def __init__(self):
        self.data = json.loads(PATH.read_text()) if PATH.exists() else dict(
            caps=CAPS, actual={k: 0 for k in CAPS}, failures=[], cap_stop=None)
        assert self.data['caps'] == CAPS and self.data['cap_stop'] is None
        self.save()

    def save(self):
        PATH.write_text(json.dumps(self.data, indent=2) + '\n')

    def observe(self, key, value):
        self.data['actual'][key] = max(self.data['actual'][key], value)
        if value > CAPS[key]:
            self.data['cap_stop'] = key
            self.save()
            raise RuntimeError('Fixed-test bound exceeded: ' + key)

    def xor(self, x, y, witness=False):
        key = 'witness_xors' if witness else 'row_xors'
        self.observe(key, self.data['actual'][key] + 1)
        z = x ^ y
        self.observe('mask_bits', max(x.bit_length(), y.bit_length(), z.bit_length()))
        return z

    def fail(self, exc):
        self.data['failures'].append(repr(exc))
        self.save()
