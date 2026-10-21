"""Step 206: fixed-library replay and combination-count audit, no exports.

The counting adapter executes the real combination traversal but creates no
primitive proof. The all-size proof remains in L065; finite checks are diagnostics.
"""
import json
import run as h

DEST = h.OUT / 'audit-206.json'


class Count:
    def __init__(self):
        self.operations = 0
        self.internal = 0
        self.padding = 0

    def refl(self, a):
        self.operations += 1
        self.padding += 1

    def congr(self, a, b, c, d, ab, cd):
        self.operations += 7  # three fixed laws and four external MPs
        self.internal += 1


def main():
    assert not DEST.exists(), 'preserve previous audit'
    result = dict(step=206, complete=False, failures=[], library={}, combinations=[],
                  limitation='No coordinate archive replay; counting adapter is not a proof emitter.')
    def save():
        DEST.write_text(json.dumps(result, indent=2) + '\n')
    save()
    try:
        for name, goal in dict(h.b.ep.fixed(), close_cancel=h.ep.cancellation()).items():
            if name == 'close_cancel':
                folder = h.OUT
            elif name in ('zeroR', 'zeroL', 'prod_zero'):
                folder = h.HERE.parent / 'backward-zero' / 'output'
            else:
                folder = h.HERE.parent / ('balanced-distribution' if name in
                    ('dist', 'prod_cong') else 'balanced-slot') / 'output'
            checked = h.audit.scan(folder / (name + '.native.jsonl.gz'),
                h.ep.e.c.serialize(goal), folder / (name + '.not-or.jsonl.gz'))
            result['library'][name] = checked['measurements']
        constants = dict(L=max(r['native']['lines'] for r in result['library'].values()))
        for mode in ('native', 'not-or'):
            constants[mode] = dict(
                D=max(r[mode]['max_line_depth'] for r in result['library'].values()),
                S=max(r[mode]['max_record_nodes'] for r in result['library'].values()))
        required = dict(L=3470, native=dict(D=19, S=2456),
                        **{'not-or':dict(D=27, S=3492)})
        result['constants'] = dict(actual=constants, required=required)
        assert constants == required
        z = h.b.atom((9,), h.p.N(h.p.I('q', 'q')))
        for m in range(1, 130):
            old = [h.b.atom((1, i), 's'+str(i)) for i in range(m)]
            new = [h.b.X(t, z) for t in old]
            o = Count()
            a, b, _ = h.b.combine(o, old, new, [None]*m, z)
            M = 1 << (m-1).bit_length()
            exact = 7*(M-1)+(M-m)
            N = max(2, m)
            assert a == h.b.Bal(old,z) and b == h.b.Bal(new,z)
            assert o.operations == exact and exact <= 16*N
            assert o.internal == M-1 and o.padding == M-m
            result['combinations'].append(dict(selected=m, capacity=M, visits=2*M-1,
                operations=o.operations, exact_required=exact, bound=16*N,
                old_visit_claim=2*N-1, old_visit_claim_holds=2*M-1<=2*N-1))
        result['first_visit_counterexample'] = next(r for r in result['combinations']
            if not r['old_visit_claim_holds'])
        result['complete'] = True
    except BaseException as error:
        result['failures'].append(type(error).__name__+': '+str(error))
        raise
    finally:
        save()
        print('Fixed laws:', len(result['library']), 'pairs; combinations:',
              len(result['combinations']), '; complete:', result['complete'],
              '; failures:', result['failures'])
        print('Constants actual/required:', result.get('constants'))
        print('First old visit-bound failure:', result.get('first_visit_counterexample'))
        print('Certificate:', DEST.relative_to(h.ROOT))


if __name__ == '__main__':
    main()
