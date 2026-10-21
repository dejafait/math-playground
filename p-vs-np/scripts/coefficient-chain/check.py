"""Complete independent finite checks plus bounded free-word discriminators."""
import copy
import json
from pathlib import Path
import construct as b

HERE = Path(__file__).resolve().parent
verifier = b.load('coefficient_source_contract', HERE.parent/'actual-tree'/'verify.py')
chain_receiver = b.load('coefficient_chain_receiver', HERE.parent/'backward-zero'/'chain.py')

def mm(A, B, cols):
    return [[sum(a * B[j][w] for j, a in enumerate(row)) % 2 for w in range(cols)] for row in A]

def check(cert):
    assert set(cert) == {'source', 'depth_factor', 'edges', 'adjacency', 'K', 'chain', 'ledger'}
    source, req, chain = cert['source'], cert['adjacency'], cert['chain']
    U, depth = b.actual.validate_input(source, cert['depth_factor'])
    assert len(set(source['letters'])) == len(source['letters'])
    verifier.contract(source, cert['edges'], req)
    N, n = req['N'], req['n']; E = req['E0']
    # Descending DAG recurrence for K, independent of the constructor's powers.
    K = [[int(v == w) for w in range(N)] for v in range(N)]
    for v in range(N-1, -1, -1):
        for j in range(v+1, N):
            if E[v][j]: K[v] = [x ^ y for x, y in zip(K[v], K[j])]
    assert K == cert['K']
    assert chain['beta'] == [[K[v][req['t']]] for v in range(N)]
    assert chain['G'] == [mm(K, g, N) for g in req['Eb']]
    for key in ('N', 'n', 'q', 'letters', 'suffixes'): assert chain[key] == req[key]
    levels = chain['levels']; assert len(levels) == N+1
    assert levels[0]['R'] == [[int(v == 0) for v in range(N)]]
    assert levels[-1] == dict(k=0, R=[], T=[])
    for i, level in enumerate(levels):
        R = level['R']; assert level['k'] == len(R) <= N
        assert len(level['T']) == len(R)
        pivots = [next(v for v, bit in enumerate(r) if bit) for r in R]
        assert pivots == sorted(set(pivots))
        assert not any(any(r[:p]) for r, p in zip(R, pivots))
        assert mm(R, chain['beta'], 1) == [[0] for _ in R]
        if i == N: continue
        nxt = levels[i+1]['R']
        candidates = [row for g in chain['G'] for row in mm(R, g, N)]
        # Independent rank computation, requiring equal spans in both directions.
        assert rank(candidates, N) == len(nxt) == rank(nxt+candidates, N)
        for j, r in enumerate(R):
            assert len(level['T'][j]) == n
            for a, g in enumerate(chain['G']):
                T = level['T'][j][a]
                assert len(T) == 1 and len(T[0]) == len(nxt)
                assert mm([r], g, N) == mm(T, nxt, N)
    chain_receiver.validate(chain)  # exact L064 receiver, no proof compilation
    ledger = cert['ledger']; Q = len(json.dumps(source, separators=(',', ':')).encode('ascii'))
    size = len(json.dumps(cert, separators=(',', ':')).encode('ascii'))
    expected = dict(source_bytes=Q, U=U, depth=depth, depth_factor=cert['depth_factor'],
                    N=N, n=n, levels=len(levels), dimensions=[l['k'] for l in levels],
                    basis_bits=sum(len(l['R'])*N for l in levels),
                    basis_bits_required_max=(N+1)*N*N,
                    transition_bits=sum(len(levels[i]['R'])*n*len(levels[i+1]['R']) for i in range(N)),
                    transition_bits_required_max=n*N**3,
                    original_source_byte_bound=2**30*(Q+2)**(4*cert['depth_factor']+12),
                    certificate_bytes=size)
    assert set(ledger) == set(expected)
    for key, value in expected.items():
        if key == 'dimensions':
            assert isinstance(ledger[key], list) and all(type(k) is int for k in ledger[key])
        else:
            assert type(ledger[key]) is int
        assert ledger[key] == value, 'ledger mismatch: '+key
    assert ledger['basis_bits'] <= ledger['basis_bits_required_max']
    assert ledger['transition_bits'] <= ledger['transition_bits_required_max']
    assert size <= ledger['original_source_byte_bound']
    return True

def rank(rows, N):
    A = [r[:] for r in rows]; k = 0
    for v in range(N):
        pivot = next((j for j in range(k, len(A)) if A[j][v]), None)
        if pivot is None: continue
        A[k], A[pivot] = A[pivot], A[k]
        for j in range(k+1, len(A)):
            if A[j][v]: A[j] = [x ^ y for x, y in zip(A[j], A[k])]
        k += 1
    return k

def words(t):
    if t[0] == 'zero': return set()
    if t[0] == 'one': return {()}
    if t[0] == 'var': return {(t[1],)}
    A, B = words(t[1]), words(t[2])
    if t[0] == 'add': return A ^ B
    out = set()
    for a in A:
        for bb in B:
            w = a+bb
            if w in out: out.remove(w)
            else: out.add(w)
    return out

def small_exact(cert):
    """All reachable word rows for these bounded fixtures only."""
    C = cert['chain']; N = C['N']; rows = C['levels'][0]['R']
    assert not words(cert['source']['tree'])
    for level in C['levels']:
        R = level['R']
        assert rank(rows, N) == len(R) == rank(rows+R, N)
        assert mm(rows, C['beta'], 1) == [[0] for _ in rows]
        rows = [v for g in C['G'] for v in mm(rows, g, N)]
        # Remove duplicate/zero rows only in this finite expansion checker.
        rows = [list(r) for r in sorted(set(tuple(r) for r in rows)) if any(r)]

def main():
    out = HERE/'output'; out.mkdir(exist_ok=True)
    v = lambda i: ['var', i]
    xy = ['mul', v(0), v(1)]
    cases = dict(empty=['zero'], constants=['add', ['one'], ['one']],
                 variable=['add', xy, xy],
                 mixed=['add', ['add', ['one'], v(0)], ['add', v(0), ['one']]])
    reports = []
    for name, tree in cases.items():
        source = dict(tree=tree, letters=[] if name in ('empty','constants') else ['x','y','unused'], q='q', delete_zero=True)
        cert = b.construct(source); check(cert); small_exact(cert)
        path = out/(name+'.json'); path.write_text(json.dumps(cert, separators=(',', ':'))+'\n')
        check(json.loads(path.read_text())); small_exact(json.loads(path.read_text()))
        reports.append(dict(case=name, passed=True, path=str(path.relative_to(HERE.parent.parent)), **cert['ledger']))
    rejects = []
    for name, tree, letters in [
        ('constant_nonzero', ['one'], []), ('variable_nonzero', v(0), ['x']),
        ('boolean_only', ['add', ['mul', v(0), v(0)], v(0)], ['x']),
        ('commutative_only', ['add', xy, ['mul', v(1), v(0)]], ['x','y']),
        ('alias', ['add', v(0), v(1)], ['x','x'])]:
        try: b.construct(dict(tree=tree, letters=letters, q='q', delete_zero=False))
        except b.Invalid as exc: rejects.append(dict(case=name, rejected=True, reason=str(exc)))
        else: raise AssertionError('accepted '+name)
    base = b.construct(dict(tree=cases['variable'], letters=['x','y'], q='q', delete_zero=False))
    for name in ('source_row','terminal','transition','closure','source_graph'):
        bad = copy.deepcopy(base)
        if name == 'source_row': bad['chain']['levels'][0]['R'][0][0] = 0
        if name == 'terminal': bad['chain']['levels'][-1]['k'] = 1
        if name == 'transition': bad['chain']['levels'][0]['T'][0][0][0][0] ^= 1
        if name == 'closure': bad['K'][0][0] ^= 1
        if name == 'source_graph': bad['edges'].pop()
        try: check(bad)
        except (AssertionError, b.Invalid, verifier.c.Invalid): rejects.append(dict(case='corrupt_'+name, rejected=True))
        else: raise AssertionError('accepted corruption '+name)
    summary = dict(passed=True, cases=reports, rejections=rejects, failures=[])
    path = out/'results.json'; path.write_text(json.dumps(summary, indent=2)+'\n')
    for r in reports:
        print(r['case'], 'PASS dimensions=',r['dimensions'], 'basis bits',r['basis_bits'],'<=',r['basis_bits_required_max'], 'T bits',r['transition_bits'],'<=',r['transition_bits_required_max'], 'bytes',r['certificate_bytes'],'<=',r['original_source_byte_bound'],r['path'])
    print('rejections',len(rejects),'failures',summary['failures'],'certificate',path.relative_to(HERE.parent.parent))

if __name__ == '__main__': main()
