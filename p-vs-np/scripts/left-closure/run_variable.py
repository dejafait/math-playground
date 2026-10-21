"""Smaller complete variable-edge discriminator; preserve diamond evidence."""
import json
import finish_exports as f

h = f.h
b, p, ep = h.b, h.p, h.ep
OUT, ROOT = h.OUT, h.ROOT


def fixture(name, lib):
    assert name == 'variable-203'
    q = 'A'
    y = b.atom((0,), p.I(q, q))
    z = b.atom((9,), p.N(p.I(q, q)))
    x = b.atom((3, 0), q)
    a = b.product(x, y)
    views = [a, y]
    d = dict(N=2, n=1, q=q, t=1,
             suffixes=[p.text(b.nt(s)) for s in views], letters=[q],
             E0=[[0, 0], [0, 0]], Eb=[[[0, 1], [0, 0]]])
    tables = ep.request(d)
    paths = []
    for v in range(2):
        o = b.Store(lib, q)
        extra = []
        if v == 0:
            deep = 'unused'
            for _ in range(35):
                deep = p.N(deep)
            extra = [o.p.ax('ax1', deep, q)]
            inner = b.X(z, a)
            rhs = b.X(z, inner)
            j = o.trans(rhs, inner, a,
                        o.law('zeroL', {'A': inner}),
                        o.law('zeroL', {'A': a}))
            root = o.symm(rhs, a, j)
        else:
            prod = b.product(x, z)
            inner = b.X(z, prod)
            rhs = b.X(y, inner)
            j = o.p.mp(o.law('prod_zero', {'A': x}),
                       o.law('congR', {'A': prod, 'B': z, 'C': z}))
            j = o.trans(inner, b.X(z, z), z, j, o.law('zeroL', {'A': z}))
            j = o.p.mp(j, o.law('congR', {'A': inner, 'B': z, 'C': y}))
            j = o.trans(rhs, b.X(y, z), y, j, o.law('zeroR', {'A': y}))
            root = o.symm(rhs, y, j)
        assert p.text(o.p.rows[root][0]) == ep.e.c.serialize(tables['local'][v])
        path = OUT / (name + '-local-' + str(v) + '.native.jsonl.gz')
        h.suite.fixture_write(o, root, path, extra)
        h.c.check(path, ep.e.c.serialize(tables['local'][v]))
        paths.append(path)
        print('complete genuine variable local input', v, 'checked', flush=True)
    (OUT / (name + '.request.json')).write_text(json.dumps(d, indent=2) + '\n')
    return d, paths


def main():
    initial = json.loads((OUT / 'certificate-202.json').read_text())
    cert = dict(step=203, library=initial['library'], constants=initial['constants'],
                cases=[], failures=[], complete=False,
                preserved_unverified_diamond='scripts/left-closure/output/certificate-203.json',
                reused_empty='scripts/left-closure/output/certificate-202.json',
                reused_rejections='scripts/left-closure/output/rejections-202.json')
    h.DEST = OUT / 'certificate-203-variable.json'
    h.save(cert)
    try:
        lib = f.library(initial)
        h.lc.Closure.write = f.write
        h.audit.syntax = f.ReplaySyntax()
        h.fixture = fixture
        d, paths, obj, record = h.test_case('variable-203', lib, cert)
        assert obj.tables['beta'] == [[0], [1]]
        assert obj.tables['G'][0] == [[0, 1], [0, 0]]
        cert['complete'] = True
        h.save(cert)
        print('PASS two complete variable-edge native/image pairs;', h.DEST.relative_to(ROOT), flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__ + ': ' + str(exc))
        h.save(cert)
        raise


if __name__ == '__main__':
    main()
