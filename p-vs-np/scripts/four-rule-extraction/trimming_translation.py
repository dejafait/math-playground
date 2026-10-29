"""Step 477: restrict only the two original operands before each L035 call.

Both public call entries delegate to the same retained checked constructor,
without recursively wrapping it. No polynomial evaluation selects a rewrite.
"""
from constant_translation import Translation, e
from trim_saved_operands import trim, ledger


class Trimming(Translation):
    def __init__(self, folder):
        super().__init__(folder)
        self.checked_constructor = e.checked_witness

    def call(self, entry, f, g, **kw):
        # Never let deletion hide a forbidden original input symbol.
        e.original_only(f)
        e.original_only(g)
        restrictions = dict(f=trim(f), g=trim(g))
        a, b = (restrictions[k]['trimmed'] for k in ('f', 'g'))
        index = self.save('commutator-input', parent=self.boolean, entry=entry,
                          f=f, g=g, restrictions=restrictions,
                          original_ledger=ledger(f, g), trimmed_ledger=ledger(a, b))
        # This preserves checked_witness's exact-copy and original-only guards.
        out, central = self.checked_constructor(a, b, **kw)
        self.save('commutator-output', parent=index, graph=out, central=central)
        return out, central

    def witness(self, f, g, **kw):
        return self.call('m.witness', f, g, **kw)

    def occurrence_witness(self, f, g, **kw):
        return self.call('checked_witness', f, g, **kw)


def install(folder):
    adapter = Trimming(folder)
    e.translation = adapter.translation
    e.b.construct = adapter.construct
    e.m.witness = adapter.witness
    e.checked_witness = adapter.occurrence_witness
    return adapter
