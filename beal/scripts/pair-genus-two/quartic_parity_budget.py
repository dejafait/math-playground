"""Persistent scalar accounting and source instrumentation, no mathematics.

Count numeric binary/unary operations, comparisons, rational construction,
and sum additions in both instrumented programs. Loop machinery, indexing,
container operations, serialization, Fraction normalization and Python's
internal bit operations are excluded. Powers are scalar operations, not bit
operation counts. Explicit enumeration/closure counters have separate caps.
"""
import ast
import json
import operator
import traceback
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER = ROOT / 'quartic-parity-ledger.json'
CAPS = dict(scalar_operations=20000000, membership_tests=200000,
            dimension=4, integer_bits=4096)
OPS = {k: getattr(operator, v) for k, v in dict(Add='add', Sub='sub',
       Mult='mul', Div='truediv', FloorDiv='floordiv', Mod='mod',
       Pow='pow', BitAnd='and_', BitOr='or_', BitXor='xor', LShift='lshift',
       RShift='rshift').items()}
CMPS = {k: getattr(operator, v) for k, v in dict(Eq='eq', NotEq='ne',
        Lt='lt', LtE='le', Gt='gt', GtE='ge', Is='is_', IsNot='is_not',
        In='contains', NotIn='contains').items()}

class Budget:
    def __init__(self):
        if LEDGER.exists():
            self.data = json.loads(LEDGER.read_text())
            assert self.data['caps'] == CAPS
            if self.data['cap_stop']:
                raise RuntimeError('Previous cap stop is final')
        else:
            self.data = dict(caps=CAPS, actual={k: 0 for k in CAPS},
                             phases=[], failures=[], cap_stop=None)
            self.data['actual']['dimension'] = 4
            self.save()
        self.next_save = self.data['actual']['scalar_operations'] + 100000

    def save(self):
        LEDGER.write_text(json.dumps(self.data, indent=2) + '\n')

    def charge(self, key='scalar_operations', n=1):
        self.data['actual'][key] += n
        if self.data['actual'][key] > CAPS[key]:
            self.data['cap_stop'] = key
            self.save()
            raise RuntimeError('Cap exceeded: ' + key)
        if key == 'scalar_operations' and self.data['actual'][key] >= self.next_save:
            self.next_save += 100000
            self.save()

    def observe(self, x):
        if isinstance(x, (int, Fraction)):
            q = Fraction(x)
            bits = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
            self.data['actual']['integer_bits'] = max(bits, self.data['actual']['integer_bits'])
            if bits > CAPS['integer_bits']:
                self.data['cap_stop'] = 'integer_bits'
                self.save()
                raise RuntimeError('4096-bit cap exceeded')

    def op(self, key, x, y):
        numeric = isinstance(x, (int, Fraction)) and isinstance(y, (int, Fraction))
        if numeric:
            self.charge()
            self.observe(x)
            self.observe(y)
        z = OPS[key](x, y)
        if numeric:
            self.observe(z)
        return z

    def cmp(self, key, x, y):
        if key in ('Eq', 'NotEq') and isinstance(x, (list, tuple)) and isinstance(y, (list, tuple)):
            same = self.cmp('Eq', len(x), len(y)) and all(self.cmp('Eq', a, c) for a, c in zip(x, y))
            return same if key == 'Eq' else not same
        if isinstance(x, (int, Fraction)) and isinstance(y, (int, Fraction)):
            self.charge()
            self.observe(x)
            self.observe(y)
        if key in ('In', 'NotIn'):
            z = operator.contains(y, x)
            return z if key == 'In' else not z
        return CMPS[key](x, y)

    def rational(self, *args):
        self.charge()
        z = Fraction(*args)
        self.observe(z)
        return z

    def scalar_sum(self, values, start=0):
        for x in values:
            start = self.op('Add', start, x)
        return start

    def phase(self, name):
        self.data['phases'].append(name)
        self.save()

    def summary(self):
        return dict(actual=self.data['actual'], required_caps=CAPS,
                    failures=self.data['failures'], cap_stop=self.data['cap_stop'])

class Instrument(ast.NodeTransformer):
    def call(self, method, *args):
        return ast.Call(ast.Attribute(ast.Name('b', ast.Load()), method, ast.Load()), list(args), [])

    def visit_BinOp(self, node):
        self.generic_visit(node)
        return ast.copy_location(self.call('op', ast.Constant(type(node.op).__name__), node.left, node.right), node)

    def visit_UnaryOp(self, node):
        self.generic_visit(node)
        if isinstance(node.op, ast.USub):
            return ast.copy_location(self.call('op', ast.Constant('Sub'), ast.Constant(0), node.operand), node)
        return node

    def visit_Compare(self, node):
        self.generic_visit(node)
        terms = [self.call('cmp', ast.Constant(type(op).__name__), left, right)
                 for left, op, right in zip([node.left] + node.comparators, node.ops, node.comparators)]
        return ast.copy_location(terms[0] if len(terms) == 1 else ast.BoolOp(ast.And(), terms), node)

    def visit_Call(self, node):
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id in ('sum', 'Q'):
            node.func = ast.Attribute(ast.Name('b', ast.Load()),
                                      'scalar_sum' if node.func.id == 'sum' else 'rational', ast.Load())
        return node

def run(path):
    budget = Budget()
    budget.phase(Path(path).name + ': start')
    tree = Instrument().visit(ast.parse(Path(path).read_text(), filename=path))
    ast.fix_missing_locations(tree)
    env = dict(__name__='__main__', __file__=path, __instrumented__=True, b=budget)
    try:
        exec(compile(tree, path, 'exec'), env)
    except Exception as exc:
        budget.data['failures'].append(dict(program=Path(path).name, error=repr(exc)))
        budget.save()
        traceback.print_exc()
        raise
    finally:
        budget.save()
