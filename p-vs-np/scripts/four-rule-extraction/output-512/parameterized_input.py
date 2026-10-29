"""Strict caller-owned input contract; no graph constructors or algebra evaluator."""
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CAPS = dict(records=2_000_000, certificate_bytes=200_000_000,
            polynomial_words=1_000_000, word_length=256,
            multiplication_pairs=100_000_000, stored_words=20_000_000,
            input_bytes=2_000_000, tree_depth=64, json_depth=160,
            tree_nodes=100_000, source_lines=10_000, alphabet=256,
            dictionary_entries=32_896, label_entries=2_000_000,
            label_width=1024, name_bytes=4096)

class Rejected(ValueError):
    pass

def require(ok, message):
    if not ok:
        raise Rejected(message)

def bound(actual, key, stage):
    require(actual <= CAPS[key], dict(stage=stage, actual=actual,
                                    required=CAPS[key], resource=key))

def integer(x):
    return type(x) is int

def fields(x, keys):
    require(type(x) is dict and set(x) == set(keys.split()), 'schema fields: '+keys)

def typed(x):
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=True)

def exact_equal(a,b):
    """Type-sensitive comparison without allocating another serialized candidate."""
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return a.keys()==b.keys() and all(exact_equal(a[k],b[k]) for k in a)
    if type(a) is list:
        return len(a)==len(b) and all(exact_equal(x,y) for x,y in zip(a,b))
    return a==b

def no_duplicates(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'duplicate JSON key: '+k)
        out[k] = v
    return out

def reject_number(s):
    raise Rejected('noninteger JSON number: '+s[:40])

def parse_integer(s):
    require(len(s) <= 12, 'JSON integer digit cap')
    return int(s)

def parse(raw):
    # Check nesting before json.loads creates recursive containers; quoted brackets
    # and escaped quotes do not change the nesting count.
    if type(raw) is bytes:
        raw = raw.decode('utf-8')
    depth, quoted, escaped = 0, False, False
    for c in raw:
        if quoted:
            if escaped:
                escaped = False
            elif c == '\\':
                escaped = True
            elif c == '"':
                quoted = False
        elif c == '"':
            quoted = True
        elif c in '[{':
            depth += 1
            bound(depth, 'json_depth', 'JSON nesting before parse')
        elif c in ']}':
            depth -= 1
            require(depth >= 0, 'JSON nesting')
    require(depth == 0 and not quoted, 'JSON closing syntax')
    return json.loads(raw, object_pairs_hook=no_duplicates, parse_float=reject_number,
                      parse_int=parse_integer, parse_constant=reject_number)

def read_bytes(path, key):
    path = Path(path)
    bound(path.stat().st_size, key, 'file size before read: '+str(path))
    with path.open('rb') as stream:
        raw = stream.read(CAPS[key]+1)
    bound(len(raw), key, 'bounded read: '+str(path))
    return raw

def load(path, key='certificate_bytes'):
    return parse(read_bytes(path, key))

def name(x):
    require(type(x) is str and bool(x), 'name string')
    bound(len(x.encode()), 'name_bytes', 'name bytes')

def check_tree(t, alphabet):
    stack, nodes = [(t, 1)], 0
    while stack:
        x, depth = stack.pop()
        bound(depth, 'tree_depth', 'formula tree depth')
        nodes += 1
        bound(nodes, 'tree_nodes', 'formula nodes')
        if type(x) is str:
            name(x)
            require(x in ('true','false') or x in alphabet, 'foreign formula name')
        else:
            require(type(x) is list and len(x) in (2,3) and
                    ((len(x)==2 and x[0]=='not') or (len(x)==3 and x[0]=='or')),
                    'ordered formula syntax')
            stack.extend((c,depth+1) for c in x[1:])
    return nodes

def symbol_map(alphabet, dictionary):
    # Constructor-only token names have no relation to display names.
    out = {'1':['one']}
    out.update({'x'+str(i+1):['original',i] for i in range(len(alphabet))})
    for j, p in enumerate(dictionary['placeholders']):
        ids = [alphabet.index(x)+1 for x in p['originals']]
        token = 'b:'+str(ids[0]) if p['kind']=='boolean' else 't:'+':'.join(map(str,ids))
        out[token] = ['placeholder',j]
    return out

def request(source_path, request_path):
    req = load(request_path, 'input_bytes')
    fields(req, 'format source_sha256 goal alphabet dictionary')
    require(req['format']=='L108-request-v1', 'request format')
    sha = req['source_sha256']
    require(type(sha) is str and len(sha)==64 and all(c in '0123456789abcdef' for c in sha),
            'caller source digest schema')
    alphabet = req['alphabet']
    require(type(alphabet) is list, 'ordered alphabet')
    n = len(alphabet)
    bound(n, 'alphabet', 'alphabet length')
    for x in alphabet:
        name(x)
        require(x not in ('true','false') and all(c.isalnum() or c=='_' for c in x),
                'checker-legal original name')
    require(len(set(alphabet))==n, 'distinct original names')
    nodes = check_tree(req['goal'], set(alphabet))
    d = req['dictionary']
    fields(d, 'alphabet placeholders')
    require(typed(d['alphabet'])==typed(alphabet), 'dictionary alphabet order')
    count = n*(n+1)//2
    bound(count, 'dictionary_entries', 'dictionary cardinality before pair allocation')
    ps = d['placeholders']
    require(type(ps) is list and len(ps)==count, 'complete dictionary cardinality')
    expected = {('boolean', (x,)) for x in alphabet}
    expected.update(('commutator',(x,y)) for i,x in enumerate(alphabet) for y in alphabet[i+1:])
    seen, names = set(), set()
    for p in ps:
        fields(p, 'name kind originals polynomial')
        name(p['name'])
        require(p['name'] not in names, 'independent placeholder names')
        names.add(p['name'])
        require(type(p['kind']) is str and type(p['originals']) is list and
                all(type(x) is str for x in p['originals']), 'dictionary entry types')
        key = (p['kind'],tuple(p['originals']))
        require(key in expected and key not in seen, 'dictionary association/uniqueness')
        seen.add(key)
        a = p['originals']
        polynomial = [[a[0],a[0]],[a[0]]] if p['kind']=='boolean' else [[a[0],a[1]],[a[1],a[0]]]
        require(typed(p['polynomial'])==typed(polynomial), 'exact ordered dictionary polynomial')
    require(seen==expected, 'complete dictionary coverage')
    raw = read_bytes(source_path, 'input_bytes')
    require(hashlib.sha256(raw).hexdigest()==sha, 'caller source digest')
    # Duplicate rejection and every strict type/depth check precede checker.check_bytes.
    lines = raw.splitlines()
    require(2 <= len(lines) <= CAPS['source_lines']+1, 'nonempty bounded source lines')
    header, *records = [parse(line) for line in lines]
    fields(header, 'format alphabet goal')
    require(header['format']=='literal-four-rule-v1' and
            typed(header['alphabet'])==typed(alphabet) and typed(header['goal'])==typed(req['goal']),
            'caller exact source header')
    needed = {'axiom':0,'true':0,'not-false':0,'expansion':1,'contraction':1,'association':1,'cut':2}
    for i,r in enumerate(records):
        fields(r, 'rule f refs')
        require(type(r['rule']) is str and r['rule'] in needed, 'source rule tag')
        require(type(r['refs']) is list and len(r['refs'])==needed[r['rule']] and
                all(integer(j) and 0<=j<i for j in r['refs']), 'strict backward source references')
        nodes += check_tree(r['f'],set(alphabet))
        bound(nodes, 'tree_nodes', 'aggregate source/request nodes')
    require(typed(records[-1]['f'])==typed(req['goal']), 'caller exact final endpoint')
    spec = importlib.util.spec_from_file_location('parameterized_literal_checker', HERE.parent/'parity-four-rule/checker.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    # Preserve changed-second-open rejection, but never parse replacement bytes.
    second_raw = read_bytes(source_path, 'input_bytes')
    require(second_raw == raw, 'source changed during checking')
    checked = checker.check_bytes(raw, req['goal'], CAPS['input_bytes'])
    # Bind the exact immutable bytes checked to the original caller digest.
    require(checked['sha256']==sha, 'source changed during checking')
    return req, raw, records, checked

def input_bounds(req, raw, records, request_path):
    def size_depth(t):
        stack, count, depth = [(t,1)], 0, 0
        while stack:
            x,d = stack.pop()
            count += 1
            depth = max(depth,d)
            if type(x) is list:
                stack.extend((c,d+1) for c in x[1:])
        return count,depth
    trees=[req['goal']]+[x['f'] for x in records]
    sizes=[size_depth(t) for t in trees]
    names=req['alphabet']+[p['name'] for p in req['dictionary']['placeholders']]
    actual=dict(source_bytes=len(raw),request_bytes=Path(request_path).stat().st_size,
                tree_depth=max(x[1] for x in sizes),tree_nodes=sum(x[0] for x in sizes),
                source_lines=len(records),alphabet=len(req['alphabet']),
                dictionary_entries=len(req['dictionary']['placeholders']),
                name_bytes=max((len(x.encode()) for x in names),default=0))
    required={k:(CAPS['input_bytes'] if k in ('source_bytes','request_bytes') else CAPS[k]) for k in actual}
    require(all(actual[k]<=required[k] for k in actual), 'complete input metrics bounds')
    return dict(actual=actual,required=required)

def write_json(path, value, key='certificate_bytes'):
    # Stream to a capped temporary file; do not first allocate a whole JSON string.
    path = Path(path)
    tmp = path.with_suffix(path.suffix+'.partial')
    size = 0
    try:
        with tmp.open('wb') as stream:
            for chunk in json.JSONEncoder(separators=(',',':')).iterencode(value):
                b = chunk.encode()
                size += len(b)
                bound(size, key, 'streamed output bytes: '+str(path))
                stream.write(b)
            bound(size+1, key, 'streamed output newline: '+str(path))
            stream.write(b'\n')
        tmp.replace(path)
    except Exception:
        # Keep an explicit partial artifact on failure.
        raise
    return size+1
