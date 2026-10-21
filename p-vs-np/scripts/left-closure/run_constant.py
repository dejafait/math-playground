"""Step 204: isolated constant-path parity, complete prefixes and full replay.

Reuse the unchanged closure compiler and paid laws.  These literal local test
inputs are constructed here; no general suffix or recurrence finder is given.
"""
import json
import finish_exports as f

h = f.h
b, p, ep = h.b, h.p, h.ep
OUT, ROOT = h.OUT, h.ROOT


def fixture(name, lib):
    assert name == 'constant-204'
    q = 'A'
    y = b.atom((0,), p.I(q, q))
    z = b.atom((9,), p.N(p.I(q, q)))
    views = [z, y, y]
    adjacency = [[0, 1, 1], [0, 0, 1], [0, 0, 0]]
    d = dict(N=3, n=0, q=q, t=2,
             suffixes=[p.text(b.nt(s)) for s in views], letters=[],
             E0=adjacency, Eb=[])
    tables = ep.request(d)
    paths = []
    for v in range(3):
        o = b.Store(lib, q)
        extra = []
        if v == 0:
            deep = 'unused'
            for _ in range(35):
                deep = p.N(deep)
            extra = [o.p.ax('ax1', deep, q)]
        const = b.W(adjacency[v], views, z)
        inner = b.X(const, z)
        terminal = y if v == 2 else z
        rhs = b.X(terminal, inner)
        if v == 0:
            assert const == b.X(y, y)
            # Cancel the two actual suffix occurrences before deleting zeros.
            j = o.p.mp(o.law('cancel', {'A': y}),
                       o.law('congL', {'A': const, 'B': z, 'C': z}))
            j = o.trans(inner, b.X(z, z), z, j,
                        o.law('zeroR', {'A': z}))
            reduced_inner = z
        else:
            reduced_inner = const
            j = o.law('zeroR', {'A': const})
        next_rhs = b.X(terminal, reduced_inner)
        j = o.p.mp(j, o.law('congR',
                           {'A': inner, 'B': reduced_inner, 'C': terminal}))
        final = (o.law('zeroR', {'A': terminal}) if v == 2 else
                 o.law('zeroL', {'A': reduced_inner}))
        root = o.symm(rhs, views[v],
                      o.trans(rhs, next_rhs, views[v], j, final))
        assert p.text(o.p.rows[root][0]) == ep.e.c.serialize(tables['local'][v])
        path = OUT / (name + '-local-' + str(v) + '.native.jsonl.gz')
        h.suite.fixture_write(o, root, path, extra)
        h.c.check(path, ep.e.c.serialize(tables['local'][v]))
        paths.append(path)
        print('complete genuine constant local input', v, 'checked', flush=True)
    (OUT / (name + '.request.json')).write_text(json.dumps(d, indent=2) + '\n')
    return d, paths


def main():
    initial = json.loads((OUT / 'certificate-202.json').read_text())
    cert = dict(step=204, library=initial['library'], constants=initial['constants'],
                cases=[], failures=[], complete=False,
                reused_empty='scripts/left-closure/output/certificate-202.json',
                reused_variable='scripts/left-closure/output/certificate-203-variable.json',
                reused_rejections='scripts/left-closure/output/rejections-202.json',
                preserved_unverified_diamond='scripts/left-closure/output/certificate-203.json')
    h.DEST = OUT / 'certificate-204-constant.json'
    h.save(cert)
    try:
        lib = f.library(initial)
        h.lc.Closure.write = f.write
        h.audit.syntax = f.ReplaySyntax()
        h.fixture = fixture
        d, paths, obj, record = h.test_case('constant-204', lib, cert)
        assert obj.tables['K'] == [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
        assert obj.tables['beta'] == [[0], [1], [1]]
        assert obj.tables['G'] == []
        cert['discriminators'] = dict(nonzero_constant_closure=True,
            two_constant_paths_cancel=True, surviving_beta=True,
            empty_letter_list=True, empty_selections=True,
            repeated_suffixes=True, deep_unused_input=True,
            nonpower_selection=False, variable_after_constant_closure=False)
        cert['complete'] = True
        h.save(cert)
        print('PASS three complete constant-cancellation native/image pairs;',
              h.DEST.relative_to(ROOT), flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__ + ': ' + str(exc))
        h.save(cert)
        raise


if __name__ == '__main__':
    main()
