"""Complete checked package import, fresh append-only balanced aggregation."""
import gzip
import hashlib
import json
import re
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'balanced-slot'))
import compiler as primitive
import checker
import endpoints

def native(t):
    if isinstance(t, str):
        if re.fullmatch(r'[A-Za-z0-9_]+', t) is None:
            raise checker.Invalid('non-ASCII variable payload')
        return t
    return tuple([{'not':'n', 'imp':'i'}[t[0]]]+[native(a) for a in t[1:]])

def unique_object(pairs):
    out = {}
    for k, v in pairs:
        if k in out: raise checker.Invalid('duplicate JSON field')
        out[k] = v
    return out

def load(path, expected):
    """Check full stream, then retain/hash the same complete records."""
    measured = checker.check(path, expected)
    rows = []; digest = hashlib.sha256(); node_sums = {'native':0, 'not-or':0}
    depths = {'native':0, 'not-or':0}; name_bytes = 1
    with (gzip.open(path, 'rb') if str(path).endswith('.gz') else Path(path).open('rb')) as stream:
        raw = stream.readline(); digest.update(raw)
        header = json.loads(raw, object_pairs_hook=unique_object)
        if set(header) != {'format','goal'} or header['format'] != 'native':
            raise checker.Invalid('complete native proof header required')
        if header['goal'] != expected:
            raise checker.Invalid('requested endpoint mismatch on copy')
        native(checker.parse(header['goal'], 'native')[0])
        for raw in stream:
            digest.update(raw); row = json.loads(raw, object_pairs_hook=unique_object)
            if row.get('rule') == 'mp':
                refs = row.get('refs', [])
                if set(row) != {'f','rule','refs'} or len(refs) != 2 or any(
                        type(k) is not int or k < 0 or k >= len(rows) for k in refs):
                    raise checker.Invalid('invalid copied MP record/reference')
            elif row.get('rule') not in ('ax1','ax2','ax3') or set(row) != {'f','rule','subs'}:
                raise checker.Invalid('invalid copied primitive axiom record')
            f = checker.parse(row['f'], 'native')[0]
            subs = {k: checker.parse(v, 'native')[0] for k,v in row.get('subs', {}).items()}
            fields = [f]+list(subs.values())
            for t in fields:
                native(t)
                for mode, tree in [('native',t), ('not-or',endpoints.image(t))]:
                    count, depth, payload = endpoints.stats(tree)
                    node_sums[mode] += count; depths[mode] = max(depths[mode],depth)
                    name_bytes = max(name_bytes,payload)
            rows.append((native(f), row['rule'], row.get('refs',[]),
                         {k:native(v) for k,v in subs.items()}))
    if digest.hexdigest() != measured['sha256'] or len(rows) != measured['lines']:
        raise checker.Invalid('package changed after validation')
    if not rows or rows[-1][0] != native(checker.parse(expected,'native')[0]):
        raise checker.Invalid('copied final line differs from requested endpoint')
    return {'rows': rows, 'measurement': measured, 'node_sums':node_sums,
            'depths':depths, 'name_bytes':name_bytes}

class AppendProof(primitive.Proof):
    def add(self, f, rule, refs=(), env=None, deps=frozenset()):
        if deps or rule not in ('ax1','ax2','ax3','mp'):
            raise checker.Invalid('only assumption-free primitive records')
        j = len(self.rows)
        self.rows.append((f,rule,refs,env,deps))
        return j

class Combination:
    def __init__(self, us, vs, paths, library):
        endpoints.goal(us,vs)  # Validate perfect size and syntax independently.
        if len(paths) != len(us): raise checker.Invalid('one complete proof per coordinate required')
        self.us = [native(checker.parse(u,'native')[0]) for u in us]
        self.vs = [native(checker.parse(v,'native')[0]) for v in vs]
        # All packages validated before the fresh proof store is populated.
        self.packages = [load(path,endpoints.coordinate(u,v)) for u,v,path in zip(us,vs,paths)]
        self.p = AppendProof(); self.library = library; self.imports = []; self.events = []
        self.leaves = []
        for package in self.packages:
            start = len(self.p.rows)
            root = self.copy(package['rows'], {})
            self.imports.append({'start':start, 'lines':len(package['rows']), 'root':root})
            self.leaves.append(root)

    def copy(self, rows, env):
        relocated = []
        for f,rule,refs,subs in rows:
            if rule == 'mp':
                j = self.p.mp(*(relocated[k] for k in refs))
            else:
                e = {k:primitive.sub(v,env) for k,v in subs.items()}
                j = self.p.ax(rule,e['A'],e['B'],e.get('C'))
            if self.p.rows[j][0] != primitive.sub(f,env):
                raise checker.Invalid('copied conclusion differs')
            relocated.append(j)
        return relocated[-1]

    def use(self, name, env): return self.copy(self.library[name]['rows'],env)

    def run(self):
        def go(lo,hi):
            if hi-lo == 1: return self.us[lo],self.vs[lo],self.leaves[lo]
            mid = (lo+hi)//2
            a,b,left = go(lo,mid); c,d,right = go(mid,hi)
            first = self.p.mp(left,self.use('congL',{'A':a,'B':b,'C':c}))
            second = self.p.mp(right,self.use('congR',{'A':c,'B':d,'C':b}))
            u,v,w = primitive.X(a,c),primitive.X(b,c),primitive.X(b,d)
            trans = self.use('trans',{'A':u,'B':v,'C':w})
            root = self.p.mp(second,self.p.mp(first,trans))
            self.events.append({'range':[lo,hi], 'left':left,'right':right,'root':root,
                                'arguments':[primitive.text(t) for t in [a,b,c,d,u,v,w]]})
            return u,w,root
        u,v,self.root = go(0,len(self.us))
        assert self.p.rows[self.root][0] == primitive.E(u,v)
        assert self.root == len(self.p.rows)-1
        return self.root

    def write(self,path,image=False):
        digest = hashlib.sha256(); size = 0
        with gzip.open(path,'wb',compresslevel=6) as stream:
            def put(row):
                nonlocal size
                raw = (json.dumps(row,separators=(',',':'))+'\n').encode('ascii')
                size += len(raw); digest.update(raw); stream.write(raw)
            put({'format':'not-or' if image else 'native',
                 'goal':primitive.text(self.p.rows[self.root][0],image)})
            for f,rule,refs,subs,deps in self.p.rows:
                row = {'f':primitive.text(f,image),'rule':rule}
                if rule == 'mp': row['refs'] = list(refs)
                else: row['subs'] = {k:primitive.text(v,image) for k,v in subs.items()}
                put(row)
        return {'lines':len(self.p.rows),'bytes':size,'sha256':digest.hexdigest(),
                'storage_bytes':Path(path).stat().st_size}
