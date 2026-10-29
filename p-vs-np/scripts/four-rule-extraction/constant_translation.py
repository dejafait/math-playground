"""Step 473 adapter: scalar-only folding of original formula operands.

The production emitter and both correction constructors are unchanged. Events
retain complete graphs for a separate verifier; no polynomial evaluator is used
to choose a rewrite. Call install once in a fresh process/output directory.
"""
from pathlib import Path
import emit_parameterized as e
from parameterized_input import write_json


class Translation:
    def __init__(self, folder):
        self.folder = Path(folder)
        self.events = []
        self.boolean = None
        self.raw_construct = e.b.construct
        self.raw_witness = e.m.witness

    def save(self, kind, **values):
        self.folder.mkdir(parents=True, exist_ok=True)
        index = len(self.events)
        path = self.folder / ('event-%05d.json' % index)
        write_json(path, dict(kind=kind, **values))
        self.events.append(dict(index=index, kind=kind, file=path.name))
        # Save after each complete event, including before lengthy constructors.
        write_json(self.folder / 'index.json', self.events)
        return index

    def simplify(self, t):
        if type(t) is str:
            return ['scalar', int(t == 'false')] if t in ('true', 'false') else ['original', e.ALPHABET.index(t)]
        a = self.simplify(t[1])
        if t[0] == 'not':
            return ['scalar', 1 ^ a[1]] if a[0] == 'scalar' else ['one-plus', a]
        b = self.simplify(t[2])
        if a == ['scalar', 0] or b == ['scalar', 0]:
            return ['scalar', 0]
        if a == ['scalar', 1]:
            return b
        if b == ['scalar', 1]:
            return a
        return ['product', a, b]

    def build(self, t):
        if t[0] == 'scalar':
            return e.m.graph(2, [] if t[1] == 0 else [(0, 1, ['1'])])
        if t[0] == 'original':
            return e.m.graph(2, [(0, 1, ['x' + str(t[1]+1)])])
        if t[0] == 'product':
            return e.b.product([self.build(t[1]), self.build(t[2])])
        h = self.build(t[1])
        out = e.m.graph(2, [(0, 1, ['1'])], sink=1)
        s, z = e.b.copy_into(out, h)
        out['edges'].extend([[0, s, ['1']], [z, 1, ['1']]])
        return out

    def translation(self, t):
        reduced = self.simplify(t)
        graph = self.build(reduced)
        self.save('translation', formula=t, reduced=reduced, graph=graph)
        return graph

    def construct(self, graph):
        previous = self.boolean
        index = self.save('boolean-input', graph=graph)
        self.boolean = index
        try:
            out, normalized, ledger = self.raw_construct(graph)
            self.save('boolean-output', parent=index, graph=out,
                      normalized=normalized, ledger=ledger)
            return out, normalized, ledger
        finally:
            self.boolean = previous

    def witness(self, f, g, **kw):
        index = self.save('commutator-input', parent=self.boolean, f=f, g=g)
        out, central = self.raw_witness(f, g, **kw)
        self.save('commutator-output', parent=index, graph=out, central=central)
        return out, central


def install(folder):
    adapter = Translation(folder)
    e.translation = adapter.translation
    e.b.construct = adapter.construct
    e.m.witness = adapter.witness
    return adapter
