"""Restricted, caller-pinned L087 occurrence input. No proof or algebra synthesis.

Source clause/CNF trees use ordered positional integer leaves. Only canonical
three-state dense tester numbering is received; arbitrary isomorphic diagrams
are deliberately outside this serialization. Whole caller bytes are retained.
"""
import hashlib
from pathlib import Path
from parameterized_input import (CAPS, require, bound, fields, integer, name,
                                parse, read_bytes, exact_equal, check_tree)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def ordered_tree(t, leaves, tag, empty):
    """Receive the actual bracketing; exactly one leaf per position, in order."""
    seen = []
    def walk(x, depth):
        bound(depth, 'tree_depth', 'source positional tree')
        bound(len(seen), 'tree_nodes', 'source positional leaves')
        if integer(x):
            require(0 <= x < len(leaves), 'positional leaf index')
            seen.append(x)
            return leaves[x]
        require(type(x) is list and len(x)==3 and x[0]==tag,
                'positional tree connective')
        return [tag, walk(x[1],depth+1), walk(x[2],depth+1)]
    if not leaves:
        require(type(t) is str and t==empty, 'exact empty positional tree')
        return empty
    result = walk(t,1)
    require(seen == list(range(len(leaves))), 'complete ordered positional leaves')
    return result


def fold(xs, tag, empty):
    # Explicit right association; all occurrences remain written on serialization.
    if not xs:
        return empty
    out = xs[-1]
    for x in reversed(xs[:-1]):
        out = [tag,x,out]
    return out


def expand(t, depth=1):
    bound(depth,'tree_depth','AND expansion input depth')
    if type(t) is str:
        return t
    if t[0]=='and':
        return ['not',['or',['not',expand(t[1],depth+1)],
                            ['not',expand(t[2],depth+1)]]]
    return [t[0]]+[expand(x,depth+1) for x in t[1:]]


def complement(t):
    # Simultaneous substitution at OLD leaves, never recurse into inserted NOT.
    if type(t) is str:
        return t if t in ('true','false') else ['not',t]
    return [t[0]]+[complement(x) for x in t[1:]]


def pair_spec(clauses, names, groups):
    """The two specified L087 transition machines, with all unreachable states."""
    flat = [x for row in names for x in row]
    q = len(flat)
    result = {}
    for kind in ('D','E'):
        order = flat if kind=='D' else [x for group in groups for x in group]
        schedule = {}
        batches = list(zip(clauses,names)) if kind=='D' else [(None,g) for g in groups]
        for clause, batch in batches:
            for j,x in enumerate(batch):
                schedule[x] = (j==0,j==len(batch)-1,
                               clause[j]['negative'] if kind=='D' else False)
        edges = []
        for i,x in enumerate(order):
            first,last,negative = schedule[x]
            for state in range(3):  # failure, live-zero, live-one
                for bit in (0,1):
                    if state==0:
                        target = 0
                    elif kind=='D':
                        value = (0 if first else state-1) | (bit ^ int(negative))
                        target = (1 if value else 0) if last else value+1
                    else:
                        target = bit+1 if first else state if state-1==bit else 0
                    dest = 3*q+int(target!=0) if i==q-1 else 3*(i+1)+target
                    edges.append([3*i+state,bit,dest])
        root = 0 if kind=='D' and any(not row for row in clauses) else 1
        result[kind] = dict(order=order,vertices=3*q+2,root=root,
                            zero=3*q,one=3*q+1,transitions=edges)
    return result


def dictionary(req, alphabet):
    fields(req,'format source_sha256 goal alphabet dictionary')
    require(req['format']=='L108-request-v1','generic request format')
    require(exact_equal(req['alphabet'],alphabet),'occurrence alphabet order')
    d = req['dictionary']
    fields(d,'alphabet placeholders')
    require(exact_equal(d['alphabet'],alphabet),'dictionary occurrence alphabet')
    n = len(alphabet)
    bound(n*(n+1)//2,'dictionary_entries','occurrence dictionary preflight')
    ps = d['placeholders']
    require(type(ps) is list and len(ps)==n*(n+1)//2,'occurrence dictionary count')
    expected = {('boolean',(x,)) for x in alphabet}
    expected.update(('commutator',(x,y)) for i,x in enumerate(alphabet) for y in alphabet[i+1:])
    seen, display = set(), set()
    for p in ps:
        fields(p,'name kind originals polynomial')
        name(p['name'])
        require(p['name'] not in display,'placeholder display names distinct')
        display.add(p['name'])
        require(type(p['kind']) is str and type(p['originals']) is list and
                all(type(x) is str for x in p['originals']),'dictionary types')
        key = (p['kind'],tuple(p['originals']))
        require(key in expected and key not in seen,'dictionary ordered association')
        seen.add(key)
        a = p['originals']
        poly = [[a[0],a[0]],[a[0]]] if p['kind']=='boolean' else [[a[0],a[1]],[a[1],a[0]]]
        require(exact_equal(p['polynomial'],poly),'dictionary exact polynomial')
    require(seen==expected,'complete occurrence dictionary')


def context(manifest_path, source_path, annotations_path, pair_path, proof_path, request_path):
    paths = dict(source=source_path,annotations=annotations_path,pair=pair_path,
                 proof=proof_path,request=request_path)
    manifest_raw = read_bytes(manifest_path,'input_bytes')
    manifest = parse(manifest_raw)
    fields(manifest,'format source annotations pair proof request')
    require(manifest['format']=='L097-occurrence-caller-v1','occurrence manifest format')
    raw = {k:read_bytes(p,'input_bytes') for k,p in paths.items()}
    for k in paths:
        require(type(manifest[k]) is str and manifest[k]==sha(raw[k]),'caller digest: '+k)
    f,a,p,req = [parse(raw[k]) for k in ('source','annotations','pair','request')]
    fields(f,'format clauses tree')
    require(f['format']=='ordered-width-three-v1' and type(f['clauses']) is list,'source CNF format')
    bound(len(f['clauses']),'source_lines','source clause count')
    fields(a,'format gadget names alphabet')
    require(a['format']=='L087-occurrences-v1','annotation format')
    require(type(a['gadget']) is list and len(a['gadget'])==2 and
            len(set(a['gadget']))==2,'two distinct fresh gadget names')
    for x in a['gadget']:
        name(x)
    clauses,old_names,trees = [],set(),[]
    for row in f['clauses']:
        fields(row,'literals tree')
        ls = row['literals']
        require(type(ls) is list and len(ls)<=3,'width-three literal list')
        for lit in ls:
            fields(lit,'variable negative')
            name(lit['variable'])
            require(type(lit['negative']) is bool,'literal sign bool')
            old_names.add(lit['variable'])
        clauses.append(ls)
        trees.append(row['tree'])
    require(not (set(a['gadget']) & old_names),'fresh gadget source variables')
    u,v = a['gadget']
    clauses += [[dict(variable=u,negative=False),dict(variable=v,negative=False)],
                [dict(variable=u,negative=True),dict(variable=v,negative=True)]]
    names = a['names']
    require(type(names) is list and len(names)==len(clauses),'all occurrence rows including gadget')
    for row,ls in zip(names,clauses):
        require(type(row) is list and len(row)==len(ls),'one occurrence per literal position')
        for x in row:
            name(x)
    flat = [x for row in names for x in row]
    bound(len(flat),'alphabet','occurrence count before dictionary/state allocation')
    require(len(set(flat))==len(flat),'distinct occurrence names')
    alphabet = a['alphabet']
    require(type(alphabet) is list and all(type(x) is str for x in alphabet) and
            len(alphabet)==len(flat) and set(alphabet)==set(flat),'complete occurrence alphabet')
    for x in alphabet:
        require(x not in ('true','false') and all(c.isalnum() or c=='_' for c in x),'checker-legal occurrence name')
    dictionary(req,alphabet)
    require(req['source_sha256']==manifest['proof'],'proof/request digest binding')
    by_old = {x:[] for x in sorted(old_names)+[u,v]}
    for row,ls in zip(names,clauses):
        for y,lit in zip(row,ls):
            by_old[lit['variable']].append(y)
    groups = list(by_old.values())
    fields(p,'format D E')
    require(p['format']=='L087-canonical-pair-v1','pair format')
    for tester in (p['D'],p['E']):
        fields(tester,'order vertices root zero one transitions')
        require(type(tester['transitions']) is list and len(tester['transitions'])==6*len(flat),
                'dense transition count before expected pair allocation')
    expected = pair_spec(clauses,names,groups)
    require(exact_equal(p['D'],expected['D']) and exact_equal(p['E'],expected['E']),
            'actual canonical tester provenance')
    split = []
    for i,(row,ls) in enumerate(zip(names,clauses)):
        lits = [['not',y] if lit['negative'] else y for y,lit in zip(row,ls)]
        tree = trees[i] if i<len(trees) else ['or',0,1]
        split.append(ordered_tree(tree,lits,'or','false'))
    c = ordered_tree(f['tree'],split[:-2],'and','true')
    # Preserve F's actual conjunction tree, then append the two gadget clauses.
    c = (['and',['and',c,split[-2]],split[-1]] if f['clauses'] else
         ['and',split[-2],split[-1]])
    us = [['or',fold([['not',x] for x in g],'and','true'),fold(g,'and','true')] for g in groups]
    ordinary_u = fold(us,'and','true')
    goal = complement(expand(['not',['and',c,ordinary_u]]))
    nodes = check_tree(goal,set(alphabet))
    require(exact_equal(req['goal'],goal),'exact complemented occurrence endpoint')
    return dict(source=f,annotations=a,pair=p,request=req,groups=groups,C=c,U=ordinary_u,
                goal=goal,raw={k:b.decode() for k,b in raw.items()},manifest=manifest,
                input_metrics=dict(bytes={k:len(b) for k,b in raw.items()},manifest_bytes=len(manifest_raw),
                                   Q_bytes=2+len(manifest_raw)+sum(map(len,raw.values())),
                                   occurrences=len(flat),endpoint_nodes=nodes),
                proof_validated=False)
