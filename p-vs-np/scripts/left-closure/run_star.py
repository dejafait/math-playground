"""Step 205: three-entry selection and variable-after-constant closure.

Test-only exact local proofs use previously paid laws.  The compiler, fixed
library, original-input ledger and full archive checker are unchanged.
"""
import json
import finish_exports as f

h = f.h
b, p, ep = h.b, h.p, h.ep
OUT, ROOT = h.OUT, h.ROOT


def fixture(name, lib):
    assert name == 'star-205'
    q = 'A'
    y = b.atom((0,), p.I(q, q))
    z = b.atom((9,), p.N(p.I(q, q)))
    x = b.atom((3, 0), q)
    a = b.product(x, y)
    views = [b.X(a, y), a, y]
    adjacency = [[0, 1, 1], [0, 0, 0], [0, 0, 0]]
    letters = [[[0, 0, 0], [0, 0, 1], [0, 0, 0]]]
    d = dict(N=3, n=1, q=q, t=2,
             suffixes=[p.text(b.nt(s)) for s in views], letters=[q],
             E0=adjacency, Eb=letters)
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
        prod = b.product(x, b.W(letters[0][v], views, z))
        inner = b.X(const, prod)
        terminal = y if v == 2 else z
        rhs = b.X(terminal, inner)
        if v == 1:
            assert const == z and prod == a
            reduced_inner = a
            j = o.law('zeroL', {'A': a})
        else:
            assert prod == b.product(x, z)
            j = o.p.mp(o.law('prod_zero', {'A': x}),
                       o.law('congR', {'A': prod, 'B': z, 'C': const}))
            j = o.trans(inner, b.X(const, z), const, j,
                        o.law('zeroR', {'A': const}))
            reduced_inner = const
        next_rhs = b.X(terminal, reduced_inner)
        j = o.p.mp(j, o.law('congR',
                           {'A': inner, 'B': reduced_inner, 'C': terminal}))
        final = (o.law('zeroR', {'A': y}) if v == 2 else
                 o.law('zeroL', {'A': reduced_inner}))
        root = o.symm(rhs, views[v],
                      o.trans(rhs, next_rhs, views[v], j, final))
        assert p.text(o.p.rows[root][0]) == ep.e.c.serialize(tables['local'][v])
        path = OUT / (name + '-local-' + str(v) + '.native.jsonl.gz')
        assert not path.exists(), 'preserve existing star inputs'
        h.suite.fixture_write(o, root, path, extra)
        checked = h.c.check(path, ep.e.c.serialize(tables['local'][v]))
        paths.append(path)
        print('complete genuine star local input', v, checked['lines'],
              'records; primitive/endpoint checks PASS', flush=True)
    request = OUT / (name + '.request.json')
    assert not request.exists(), 'preserve existing star request'
    request.write_text(json.dumps(d, indent=2) + '\n')
    return d, paths


def main():
    initial = json.loads((OUT / 'certificate-202.json').read_text())
    cert = dict(step=205, library=initial['library'], constants=initial['constants'],
                cases=[], failures=[], complete=False,
                reused_empty='scripts/left-closure/output/certificate-202.json',
                reused_variable='scripts/left-closure/output/certificate-203-variable.json',
                reused_constant='scripts/left-closure/output/certificate-204-constant.json',
                reused_rejections='scripts/left-closure/output/rejections-202.json',
                preserved_unverified_diamond='scripts/left-closure/output/certificate-203.json')
    h.DEST = OUT / 'certificate-205-star.json'
    assert not h.DEST.exists(), 'preserve existing attempt'
    h.save(cert)
    try:
        lib = f.library(initial)
        h.lc.Closure.write = f.write
        h.audit.syntax = f.ReplaySyntax()
        h.fixture = fixture
        d, paths, obj, record = h.test_case('star-205', lib, cert)
        assert obj.tables['K'] == [[1, 1, 1], [0, 1, 0], [0, 0, 1]]
        assert obj.tables['beta'] == [[1], [0], [1]]
        assert obj.tables['G'] == [[[0, 0, 1], [0, 0, 1], [0, 0, 0]]]
        cert['discriminators'] = dict(nonpower_selection=True,
            variable_after_constant_closure=True, nonzero_constant_closure=True,
            surviving_beta=True, empty_selections=True, repeated_name_q_x=True,
            deep_unused_input=True, two_constant_paths_cancel=False)
        cert['complete'] = True
        h.save(cert)
        for mode in ('native', 'not-or'):
            actual = record['argument_checks'][mode]
            bound = record['uniform_ledger']['formats'][mode]
            print(mode, 'aggregate bytes actual/required',
                  actual['aggregate_bytes'], '/', actual['aggregate_required'],
                  'argument nodes', actual['nodes'], '/', bound['argument_nodes'],
                  'depth', actual['depth'], '/', bound['argument_depth'], flush=True)
        print('structural argument height actual/required',
              record['max_argument_height'], '/', record['uniform_ledger']['H'], flush=True)
        print('PASS three complete star native/image pairs; failures=[];',
              h.DEST.relative_to(ROOT), flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__ + ': ' + str(exc))
        h.save(cert)
        raise


if __name__ == '__main__':
    main()
