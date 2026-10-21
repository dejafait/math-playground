"""Independent exact finite left-closure receiving contract."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location('closure_zero_endpoints',
    Path(__file__).resolve().parent.parent/'backward-zero'/'endpoints.py')
e = importlib.util.module_from_spec(spec); spec.loader.exec_module(e)
c = e.c


def multiply(a, b, N):
    return [[sum(a[v][j]*b[j][w] for j in range(N)) % 2
             for w in range(N)] for v in range(N)]


def request(d):
    if not isinstance(d, dict) or set(d) != {'N','n','q','t','suffixes','letters','E0','Eb'}:
        raise c.Invalid('closure fields')
    N,n,t = d['N'],d['n'],d['t']
    if any(type(a) is not int for a in (N,n,t)) or N < 2 or n < 0 or not 0 <= t < N:
        raise c.Invalid('closure dimensions/terminal')
    # Reuse only fixed term/name validation, with zero rows and matrices.
    zero = [[0]*N for _ in range(N)]
    e.request(dict(N=N,n=n,k=0,q=d['q'],suffixes=d['suffixes'],letters=d['letters'],
        beta=[[0] for _ in range(N)],G=[zero for _ in range(n)],r=[[0]*N],
        R_next=[],T=[[[]] for _ in range(n)]))
    if not isinstance(d['Eb'],list) or len(d['Eb']) != n:
        raise c.Invalid('closure letter matrices')
    for matrix in [d['E0']]+d['Eb']:
        e._matrix(matrix,N,N,'closure adjacency')
        if any(matrix[v][w] for v in range(N) for w in range(v+1)):
            raise c.Invalid('closure adjacency must be strictly upper triangular')
    identity = [[int(v == w) for w in range(N)] for v in range(N)]
    power = identity; K = [row[:] for row in identity]
    for _ in range(1,N):
        power = multiply(power,d['E0'],N)
        K = [[(K[v][w]+power[v][w]) % 2 for w in range(N)] for v in range(N)]
    if any(any(row) for row in multiply(power,d['E0'],N)):
        raise c.Invalid('finite nilpotence check')
    KE = multiply(K,d['E0'],N)
    if KE != [[(K[v][w]+identity[v][w]) % 2 for w in range(N)] for v in range(N)]:
        raise c.Invalid('finite closure equation')
    beta = [[K[v][t]] for v in range(N)]
    G = [multiply(K,matrix,N) for matrix in d['Eb']]
    S = [c.parse(s,'native')[0] for s in d['suffixes']]
    xs = d['letters']; y = e.imp(d['q'],d['q']); z = e.neg(y)
    right = [e.xor(y if v == t else z,e.xor(e.choose(d['E0'][v],S,z),
        e.bal([e.prod(xs[b],e.choose(d['Eb'][b][v],S,z)) for b in range(n)],z)))
        for v in range(N)]
    local = [e.eq(S[v],right[v]) for v in range(N)]
    closed = e.request(dict(N=N,n=n,k=0,q=d['q'],suffixes=d['suffixes'],
        letters=xs,beta=beta,G=G,r=[[0]*N],R_next=[],T=[[[]] for _ in range(n)]))['coordinates']
    return dict(K=K,beta=beta,G=G,local=local,closed=closed)


def cancellation():
    a,b,c = 'A','B','C'
    return e.imp(e.eq(a,e.xor(a,e.xor(b,c))),e.eq(b,c))
