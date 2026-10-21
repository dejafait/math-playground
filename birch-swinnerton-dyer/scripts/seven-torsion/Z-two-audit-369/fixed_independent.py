"""Independent full rank/lattice supplement; no producer/verifier imports."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, subprocess, sys, time
sys.set_int_max_str_digits(0)
D = Path(__file__).resolve().parent
ROOT = D.parents[2]
OLD = D.parent/'W-two-359'
START = time.monotonic()
CAP = 134217728
N = 48
I = [[int(i==j) for j in range(N)] for i in range(N)]
report = {'status':'INCOMPLETE', 'phase':'initial_inventory', 'failures':[]}
def need(ok, label):
    if not ok: raise ArithmeticError(label)
def read(path):
    if path.parent==D and (path.name in ['frobenius.json', 'radical-lattice.json', 'numerator-lattice.json', 'action-kernel.json', 'decision.json', 'input-basis.json'] or __import__('re').fullmatch(r'action-[0-9]{2}\.json',path.name)):
        path=path.with_name('test-'+path.name)
    return json.loads(path.read_text())
def save(name, value):
    raw = (json.dumps(value, separators=(',', ':'))+'\n').encode()
    need(sum(p.stat().st_size for p in D.rglob('*') if p.is_file())+len(raw)+65536 < CAP, 'combined_byte_reserve')
    with (D/name).open('xb') as f: f.write(raw)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def tr(a): return [list(r) for r in zip(*a)]
def mm(a,b):
    cols = tr(b)
    return [[sum(x*y for x,y in zip(row,col) if x and y) for col in cols] for row in a]
def rat(a): return [[F(x) for x in r] for r in a]
def strings(a): return [[str(x) for x in r] for r in a]
def bits(row):
    need(all(type(x) is int and x in (0,1) for x in row), 'binary_entries')
    return sum(x<<j for j,x in enumerate(row))
def unpack(v,w): return [(v>>j)&1 for j in range(w)]
def bm(a,b):
    # Row-vector linear combinations, all coefficients represented exactly.
    width = len(b[0]); packed = [bits(row) for row in b]; out = []
    for row in a:
        need(len(row)==len(b), 'binary_product_shape')
        value = 0
        for j,x in enumerate(row):
            need(x in (0,1), 'binary_multiplier')
            if x: value ^= packed[j]
        out.append(unpack(value,width))
    return out
def rank(rows,width):
    piv = {}
    for row in rows:
        need(len(row)==width, 'rank_width')
        value = bits(row)
        while value:
            k = value.bit_length()-1
            if k in piv: value ^= piv[k]
            else:
                piv[k] = value; break
    return len(piv)
def spans(saved, own, width, label):
    # Both independent systems have the same full span, not just cardinality.
    need(rank(saved,width)==len(saved)==len(own)==rank(own,width), label+'_independent')
    need(rank(saved+own,width)==len(own), label+'_both_span_containments')
def inverse_binary(a):
    n = len(a)
    need(all(len(row)==n for row in a), 'square_binary_inverse')
    rows = [bits(row) | (1<<(n+i)) for i,row in enumerate(a)]
    for c in range(n):
        s = next((r for r in range(c,n) if (rows[r]>>c)&1), None)
        need(s is not None, 'independent_selected_rows_nonsingular')
        rows[c],rows[s] = rows[s],rows[c]
        for r in range(n):
            if r!=c and ((rows[r]>>c)&1): rows[r] ^= rows[c]
    need(all((row&((1<<n)-1))==(1<<i) for i,row in enumerate(rows)), 'inverse_all_terminal_entries')
    inv = [unpack(row>>n,n) for row in rows]
    identity = [[int(i==j) for j in range(n)] for i in range(n)]
    need(bm(a,inv)==identity and bm(inv,a)==identity, 'binary_inverse_both_products')
    return inv

