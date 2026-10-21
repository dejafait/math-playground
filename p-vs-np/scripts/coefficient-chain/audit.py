"""Step-230 bounded audit; retain complete evidence without rewriting old fixtures."""
import copy
import hashlib
import itertools
import json
from pathlib import Path
import check as c

HERE = Path(__file__).resolve().parent
OUT = HERE / 'output' / 'audit-230'


def save(name, obj):
    path = OUT / (name + '.json')
    path.write_text(json.dumps(obj, separators=(',', ':')) + '\n')
    return str(path.relative_to(HERE.parent.parent))


def span(rows, N):
    result = {tuple([0] * N)}
    for row in rows:
        result |= {tuple(a ^ b for a, b in zip(v, row)) for v in result}
    return sorted(result)


def rejection(name, cert):
    path = save(name, cert)
    try:
        c.check(json.loads((HERE.parent.parent / path).read_text()))
    except (AssertionError, ValueError, StopIteration) as exc:
        return dict(case=name, rejected=True, reason=type(exc).__name__+': '+str(exc), path=path)
    raise AssertionError('accepted ' + name)


def main():
    OUT.mkdir(exist_ok=True)
    historical = json.loads((HERE / 'output' / 'results.json').read_text())
    assert set(historical) == {'passed', 'cases', 'rejections', 'failures'}
    assert historical['passed'] is True and historical['failures'] == []
    checked = []
    for name, report in zip(('empty', 'constants', 'variable', 'mixed'), historical['cases']):
        path = HERE / 'output' / (name + '.json')
        raw = path.read_bytes(); cert = json.loads(raw)
        c.check(cert); c.small_exact(cert)
        # Whole-object equality inspects every archived constructor field.
        assert c.b.construct(cert['source'], cert['depth_factor']) == cert
        assert report == dict(case=name, passed=True,
                              path=str(path.relative_to(HERE.parent.parent)), **cert['ledger'])
        checked.append(dict(case=name, path=str(path.relative_to(HERE.parent.parent)),
                            sha256=hashlib.sha256(raw).hexdigest(), **cert['ledger']))
    assert len(historical['cases']) == 4

    row_cases = [
        (4, [[0,0,1,1], [0,1,0,1], [1,0,0,1], [1,1,1,1], [0,0,0,0], [0,0,1,1]]),
        (3, [[1,1,0], [1,1,1], [1,0,1], [0,1,1]]),
        (3, [[0,0,0], [0,0,0]]), (3, [])]
    rows_evidence = []
    for N, rows in row_cases:
        R = c.b.basis(rows, N)
        assert span(rows, N) == span(R, N)
        assert len(span(R, N)) == 2**len(R)
        coords = [c.b.coordinates(row, R) for row in rows]
        assert c.mm(coords, R, N) == rows
        rows_evidence.append(dict(N=N, candidates=rows, basis=R, coordinates=coords,
                                  full_span=span(rows, N)))
    # Exhaust all ordered lists of up to four rows in F2^N, N <= 3.
    # Only a finite discriminator; the canonical proof covers all N.
    exhaustive = []
    for N in (1, 2, 3):
        vectors = list(itertools.product((0, 1), repeat=N)); count = 0
        for length in range(5):
            for seq in itertools.product(vectors, repeat=length):
                rows = [list(v) for v in seq]; R = c.b.basis(rows, N)
                assert span(rows, N) == span(R, N)
                assert len(span(R, N)) == 2**len(R)
                assert c.mm([c.b.coordinates(row, R) for row in rows], R, N) == rows
                count += 1
        exhaustive.append(dict(N=N, lists_checked=count, max_list_length=4, failures=[]))

    v = lambda i: ['var', i]
    xy = ['mul', v(0), v(1)]
    negative_sources = [
        ('constant_nonzero', ['one'], []), ('variable_nonzero', v(0), ['x']),
        ('boolean_only', ['add', ['mul', v(0), v(0)], v(0)], ['x']),
        ('commutative_only', ['add', xy, ['mul', v(1), v(0)]], ['x','y']),
        ('alias', ['add', v(0), v(1)], ['x','x'])]
    rejects = []
    replayed = []
    for name, tree, letters in negative_sources:
        source = dict(tree=tree, letters=letters, q='q', delete_zero=False)
        path = save('source-'+name, source)
        try:
            c.b.construct(source)
        except c.b.Invalid as exc:
            entry = dict(case=name, rejected=True, reason=str(exc))
            replayed.append(entry); rejects.append(dict(**entry, path=path))
        else:
            raise AssertionError('accepted source '+name)
    base = c.b.construct(dict(tree=['add', xy, xy], letters=['x','y'], q='q', delete_zero=False))
    for name in ('source_row', 'terminal', 'transition', 'closure', 'source_graph'):
        bad = copy.deepcopy(base)
        if name == 'source_row': bad['chain']['levels'][0]['R'][0][0] = 0
        if name == 'terminal': bad['chain']['levels'][-1]['k'] = 1
        if name == 'transition': bad['chain']['levels'][0]['T'][0][0][0][0] ^= 1
        if name == 'closure': bad['K'][0][0] ^= 1
        if name == 'source_graph': bad['edges'].pop()
        rejects.append(rejection('corrupt_'+name, bad))
        replayed.append(dict(case='corrupt_'+name, rejected=True))
    assert replayed == historical['rejections']

    wrong = json.loads((OUT / 'accepted-wrong-U-before-repair.json').read_text())
    rejects.append(rejection('wrong-U-after-repair', wrong))
    original = json.loads((HERE / 'output' / 'variable.json').read_text())
    for key in original['ledger']:
        bad = copy.deepcopy(original)
        if key == 'dimensions': bad['ledger'][key][0] += 1
        else: bad['ledger'][key] += 1
        rejects.append(rejection('ledger-'+key, bad))

    more = []
    comm = ['add', xy, ['mul', v(1), v(0)]]
    for name, source in [
        ('rank-two', dict(tree=['add', comm, comm], letters=['x','y'], q='x', delete_zero=False)),
        ('retained-zero', dict(tree=['zero'], letters=['q'], q='q', delete_zero=False)),
        ('deleted-zero', dict(tree=['zero'], letters=['q'], q='q', delete_zero=True))]:
        cert = c.b.construct(source, depth_factor=1)
        path = save(name, cert); c.check(cert); c.small_exact(cert)
        more.append(dict(case=name, path=path, **cert['ledger']))
    result = dict(passed=True, historical=checked, historical_rejections_replayed=10,
                  pivot_cases=rows_evidence, exhaustive=exhaustive, additional_cases=more,
                  rejections=rejects, failures=[],
                  checker_sha256=hashlib.sha256((HERE/'check.py').read_bytes()).hexdigest())
    path = save('results', result)
    for report in checked+more:
        print(report['case'], 'PASS', 'basis', report['basis_bits'], '<=', report['basis_bits_required_max'],
              'T', report['transition_bits'], '<=', report['transition_bits_required_max'],
              'bytes', report['certificate_bytes'], '<=', report['original_source_byte_bound'])
    print('ordered row lists:', sum(r['lists_checked'] for r in exhaustive),
          'rejections:', len(rejects), 'failures: []', 'full certificate:', path)


if __name__ == '__main__':
    main()
