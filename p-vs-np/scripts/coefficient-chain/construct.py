"""Exact-length L055 coefficient tables; no propositional proof generation."""
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj

actual = load('coefficient_actual', HERE.parent/'actual-tree'/'build.py')
Invalid = actual.c.Invalid

def product(row, matrix):
    return [sum(x * matrix[v][w] for v, x in enumerate(row)) % 2
            for w in range(len(row))]

def basis(rows, N):
    """Ordered echelon basis, with no all-word enumeration or cumulative rows."""
    pivots = {}
    for original in rows:
        row = original[:]
        for p in sorted(pivots):
            if row[p]: row = [x ^ y for x, y in zip(row, pivots[p])]
        if any(row): pivots[next(i for i, x in enumerate(row) if x)] = row
    return [pivots[p] for p in sorted(pivots)]

def coordinates(row, R):
    residue = row[:]; out = []
    for r in R:
        pivot = next(i for i, x in enumerate(r) if x)
        bit = residue[pivot]; out.append(bit)
        if bit: residue = [x ^ y for x, y in zip(residue, r)]
    if any(residue): raise Invalid('basis does not span candidate')
    return out

def construct(source, depth_factor=4):
    actual.validate_input(source, depth_factor)
    if len(set(source['letters'])) != len(source['letters']):
        raise Invalid('pairwise-distinct letter names required')
    obj = actual.construct(source, depth_factor)
    req = obj['request']; N, n = req['N'], req['n']
    closed = actual.ep.request(req)
    G, beta = closed['G'], closed['beta']
    R = [[int(v == 0) for v in range(N)]]
    levels = []
    for i in range(N):
        if any(sum(x * y[0] for x, y in zip(r, beta)) % 2 for r in R):
            raise Invalid('source is not formally zero: coefficient annihilation failed at level '+str(i))
        products = [[product(r, g) for g in G] for r in R]
        nxt = basis([v for row in products for v in row], N)
        T = [[[coordinates(v, nxt)] for v in row] for row in products]
        levels.append(dict(k=len(R), R=R, T=T)); R = nxt
    if R: raise Invalid('strict triangular terminal space must be empty')
    levels.append(dict(k=0, R=[], T=[]))
    chain = {key: req[key] for key in ('N', 'n', 'q', 'suffixes', 'letters')}
    chain.update(beta=beta, G=G, levels=levels)
    U, depth = actual.validate_input(source, depth_factor)
    Q = len(json.dumps(source, separators=(',', ':'), ensure_ascii=True).encode('ascii'))
    basis_bits = sum(level['k'] * N for level in levels)
    transition_bits = sum(levels[i]['k'] * n * levels[i+1]['k'] for i in range(N))
    ledger = dict(source_bytes=Q, U=U, depth=depth, depth_factor=depth_factor,
                  N=N, n=n, levels=len(levels), dimensions=[l['k'] for l in levels],
                  basis_bits=basis_bits, basis_bits_required_max=(N+1)*N*N,
                  transition_bits=transition_bits, transition_bits_required_max=n*N**3,
                  original_source_byte_bound=2**30*(Q+2)**(4*depth_factor+12))
    result = dict(source=source, depth_factor=depth_factor, edges=obj['edges'],
                  adjacency=req, K=closed['K'], chain=chain, ledger=ledger)
    ledger['certificate_bytes'] = len(json.dumps(result, separators=(',', ':')).encode('ascii'))
    # The final count includes this integer field itself; iterate to a fixed point.
    while True:
        size = len(json.dumps(result, separators=(',', ':')).encode('ascii'))
        if size == ledger['certificate_bytes']: break
        ledger['certificate_bytes'] = size
    if size > ledger['original_source_byte_bound']: raise Invalid('source byte ledger exceeded')
    return result
