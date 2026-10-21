"""Bounded distribution reproduction; complete primitive archives and ledgers."""
import argparse
import gzip
import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SLOT = HERE.parent/'balanced-slot'
OUT = HERE/'output'
sys.path.insert(0, str(SLOT))
import compiler as emit
import checker as verify
import endpoints
import audit_archives

def product(a, b): return emit.N(emit.I(a, emit.N(b)))
def xor(a, b): return ('x', a, b)
def prod(a, b): return ('p', a, b)
def native(t):
    if isinstance(t, tuple) and t[0] == 'x': return emit.X(native(t[1]), native(t[2]))
    if isinstance(t, tuple) and t[0] == 'p': return product(native(t[1]), native(t[2]))
    return t
def balanced(ts):
    if len(ts) == 1: return ts[0]
    k = len(ts)//2
    return xor(balanced(ts[:k]), balanced(ts[k:]))
def structural_height(t):
    if isinstance(t, tuple) and t[0] in ('x', 'p'):
        return 1+max(structural_height(t[1]), structural_height(t[2]))
    return 0
def at(t, path):
    for k in path: t = t[k]
    return t
def replace(t, path, value):
    if not path: return value
    k = path[0]
    return (t[0], replace(t[1], path[1:], value), t[2]) if k == 1 else (
            t[0], t[1], replace(t[2], path[1:], value))

def compiler_tree(t):
    if isinstance(t, str): return t
    tag = {'not': 'n', 'imp': 'i'}[t[0]]
    return tuple([tag]+[compiler_tree(v) for v in t[1:]])

def load_template(path):
    # Called only after independent full checking; every record is retained.
    rows = []
    with gzip.open(path, 'rt') as f:
        header = json.loads(next(f))
        for raw in f:
            row = json.loads(raw)
            formula = compiler_tree(verify.parse(row['f'], 'native')[0])
            env = {k: compiler_tree(verify.parse(v, 'native')[0])
                   for k, v in row.get('subs', {}).items()}
            rows.append((formula, row['rule'], row.get('refs', []), env))
    return {'rows': rows, 'goal': compiler_tree(verify.parse(header['goal'], 'native')[0])}

class Templates:
    def __init__(self, p, library): self.p, self.library = p, library
    def use(self, name, env):
        # Fresh request state; no prepopulated external mutable proof cache.
        copied = []
        for f, rule, refs, subs in self.library[name]['rows']:
            if rule == 'mp': j = self.p.mp(*(copied[k] for k in refs))
            else:
                inst = {k: emit.sub(v, env) for k, v in subs.items()}
                j = self.p.ax(rule, inst['A'], inst['B'], inst.get('C'))
            assert self.p.rows[j][0] == emit.sub(f, env)
            copied.append(j)
        return copied[-1]

class Distribution:
    def __init__(self, library, factor, ts):
        self.p = emit.Proof()  # No synthesis helpers or earlier requests here.
        self.laws = Templates(self.p, library)
        self.initial = self.tree = prod(factor, balanced(ts))
        self.eq = self.laws.use('refl', {'A': native(self.tree)})
        self.events = []
    def rewrite(self, path):
        old = self.tree
        local = at(old, path)
        assert local[0] == 'p' and local[2][0] == 'x'
        a, (tag, b, c) = local[1], local[2]
        newsub = xor(prod(a, b), prod(a, c))
        eq = self.laws.use('dist', {'A': native(a), 'B': native(b), 'C': native(c)})
        oldsub = local
        for length in range(len(path), 0, -1):
            parent = at(old, path[:length-1]); side = path[length-1]
            assert parent[0] == 'x'
            sibling = parent[3-side]
            law = self.laws.use('congL' if side == 1 else 'congR',
                {'A': native(oldsub), 'B': native(newsub), 'C': native(sibling)})
            eq = self.p.mp(eq, law)
            oldsub = parent
            newsub = xor(newsub, sibling) if side == 1 else xor(sibling, newsub)
        self.tree = replace(old, path, xor(prod(a, b), prod(a, c)))
        assert newsub == self.tree
        law = self.laws.use('trans', {'A': native(self.initial),
                                   'B': native(old), 'C': native(self.tree)})
        self.eq = self.p.mp(eq, self.p.mp(self.eq, law))
        self.events.append({'path': list(path), 'lifts': len(path),
                            'height': structural_height(self.tree),
                            'before': emit.text(native(old)),
                            'after': emit.text(native(self.tree))})
    def run(self):
        def go(path):
            local = at(self.tree, path)
            if not (isinstance(local[2], tuple) and local[2][0] == 'x'): return
            self.rewrite(path)
            go(path+(1,)); go(path+(2,))
        go(())
        return self.eq

def corruptions(path, expected, mode):
    with gzip.open(path, 'rt') as f: lines = f.read().splitlines()
    rows = [json.loads(s) for s in lines[1:]]
    ax = next(k for k, row in enumerate(rows) if row['rule'] != 'mp')
    mp = next(k for k, row in enumerate(rows) if row['rule'] == 'mp')
    different = next(k for k, row in enumerate(rows) if row['rule'] == 'mp' and
                     any(rows[j]['f'] != rows[row['refs'][0]]['f'] for j in range(k)))
    other = next(j for j in range(different) if
                 rows[j]['f'] != rows[rows[different]['refs'][0]]['f'])
    badsubs = dict(rows[ax]['subs']); badsubs['A'] = 'BAD_SUBSTITUTION'
    changes = [
        ('axiom-substitution', ax, dict(rows[ax], subs=badsubs)),
        ('forward-reference', mp, dict(rows[mp], refs=[0, len(rows)])),
        ('mp-antecedent', different, dict(rows[different], refs=[other, rows[different]['refs'][1]])),
    ]
    result = []
    for label, k, row in changes+[('endpoint', None, None)]:
        copy = list(lines)
        if k is None:
            header = json.loads(copy[0]); header['goal'] = 'BAD_ENDPOINT'
            copy[0] = json.dumps(header, separators=(',', ':'))
        else: copy[k+1] = json.dumps(row, separators=(',', ':'))
        dest = OUT/('corrupt-'+mode+'-'+label+'.jsonl.gz')
        with gzip.open(dest, 'wt') as f: f.write('\n'.join(copy)+'\n')
        try: verify.check(dest, expected)
        except verify.Invalid as err:
            result.append({'path': str(dest.relative_to(HERE.parents[1])),
                           'rejected': True, 'reason': str(err)})
        else: raise AssertionError('corruption accepted: '+label)
    return result

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--case', choices=['all','m2-variable','m4-composite','m8-composite'], default='all')
    args = parser.parse_args()
    OUT.mkdir(exist_ok=True)
    certificate = {'complete': False, 'failures': [], 'library': {}, 'cases': [], 'corruptions': {}}
    certpath = OUT/'certificate-172.json'
    def save(): certpath.write_text(json.dumps(certificate, indent=2)+'\n')
    save()
    try:
        # Regenerate only the two new constant templates. Preserve slot archives.
        a, b, c = 'A', 'B', 'C'
        new_goals = {'dist': emit.E(product(a, emit.X(b,c)), emit.X(product(a,b), product(a,c))),
                     'prod_cong': emit.I(emit.E(b,c), emit.E(product(a,b), product(a,c)))}
        library = {}
        old_goals = audit_archives.fixed_goals()
        for name in ['trans','congL','congR','refl','symm','dist','prod_cong']:
            entry = {}; old = name in old_goals
            if not old:
                p = emit.Proof(); p.build_helpers(); root = p.prove_fixed(new_goals[name])
            for image, mode in [(False,'native'), (True,'not-or')]:
                path = (SLOT/'output' if old else OUT)/(name+'.'+mode+'.jsonl.gz')
                if not old: p.write(root, path, image)
                goal = (old_goals[name] if mode == 'native' else audit_archives.image(old_goals[name])) if old else endpoints.fixed(mode)[name]
                entry[mode] = verify.check(path, goal)
            library[name] = load_template((SLOT/'output' if old else OUT)/(name+'.native.jsonl.gz'))
            certificate['library'][name] = entry; save()
            print('fixed', name, 'native/image checked; lines', entry['native']['lines'], flush=True)
        constants = {'L': max(v['native']['lines'] for v in certificate['library'].values())}
        for mode in ('native','not-or'):
            checks = [v[mode] for v in certificate['library'].values()]
            constants[mode] = {'D': max(v['max_line_depth'] for v in checks),
                               'S': max(v['max_record_nodes'] for v in checks)}
        certificate['constants'] = constants; save()
        print('enlarged selected library constants', constants, flush=True)
        cases = [
            ('m2-variable', 'p_factor', ['p0','p1']),
            ('m4-composite', emit.I('p_factor', emit.N('p_tail')),
             [emit.I('p_repeat','p_suffix')]*2+[emit.Z,emit.I('q','q')]),
            ('m8-composite', emit.N(emit.I('p_factor','p_tail')),
             ['p0',emit.N('p1'),emit.Z,emit.I('q','q'),emit.I('p_repeat','p_suffix'),
              emit.I('p_repeat','p_suffix'),emit.X('p6','p7'),'p8']),
        ]
        for name, factor, ts in cases:
            if args.case not in ('all',name): continue
            dist = Distribution(library, factor, ts); root = dist.run()
            m = len(ts); h = m.bit_length()-1; H = h+1
            J = constants['L']+(m-1)*(h+1)*(constants['L']+2)
            case = {'name': name, 'M': m, 'h': h, 'factor': emit.text(factor),
                    'slots': [emit.text(t) for t in ts], 'events': len(dist.events),
                    'required_events': m-1, 'max_height': max(e['height'] for e in dist.events),
                    'required_height_max': H, 'proofs': {}}
            assert len(dist.events) == m-1 and case['max_height'] <= H
            for image, mode in [(False,'native'),(True,'not-or')]:
                path = OUT/(name+'.'+mode+'.jsonl.gz')
                expected = endpoints.goal(case['factor'], case['slots'], mode)
                emission = dist.p.write(root, path, image)
                measured = verify.check(path, expected)
                assert emission['bytes'] == measured['bytes'] and emission['sha256'] == measured['sha256']
                stats = [verify.parse(emit.text(t, image), mode)[1:] for t in [factor]+ts]
                tmax, dmax = max(t[0] for t in stats), max(t[1] for t in stats)
                names = {'A','B','C'} | set().union(*(emit.variables(t) for t in [factor]+ts))
                B = max(len(n.encode('ascii')) for n in names)
                P = 8*4**(H+1)*(tmax+1); S = constants[mode]['S']
                bounds = {'lines': J, 'depth': constants[mode]['D']+(6 if image else 3)*H+dmax,
                          'record_nodes': S*P,
                          'bytes': (J+2)*((B+4)*S*P+256+64*math.ceil(math.log2(J+2))),
                          'argument_nodes': P, 'term_nodes': tmax, 'term_depth': dmax, 'name_bytes': B}
                bound_tests = {k: measured[field] <= bounds[k] for k, field in
                               [('lines','lines'),('depth','max_line_depth'),
                                ('record_nodes','max_record_nodes'),('bytes','bytes')]}
                bounds['bits'] = 8*bounds['bytes']
                case['proofs'][mode] = {'expected_goal': expected, 'measurement': measured,
                                        'bounds': bounds, 'bound_tests': bound_tests}
                assert all(bound_tests.values()), (name, mode, bound_tests)
                certificate['cases'] = [x for x in certificate['cases'] if x['name'] != name]+[case]
                save()
                print(name, mode, 'accepted; actual/required',
                      {k: [measured[field], bounds[k]] for k, field in
                       [('lines','lines'),('depth','max_line_depth'),('record_nodes','max_record_nodes'),('bytes','bytes')]},
                      'path', measured['path'], flush=True)
            (OUT/(name+'.trace.json')).write_text(json.dumps({'case': case,
                    'events': dist.events}, indent=2)+'\n')
            if name == 'm2-variable':
                for mode in ('native','not-or'):
                    certificate['corruptions'][mode] = corruptions(OUT/(name+'.'+mode+'.jsonl.gz'),
                        endpoints.goal(case['factor'], case['slots'], mode), mode)
                save()
            del dist
        certificate['complete'] = True
        certificate['scope'] = 'Single-factor native/literal-image component only; no ordinary-input completeness or receiver/SAT conclusion.'
        save()
        print('failures none; corruptions rejected', sum(len(v) for v in certificate['corruptions'].values()),
              'certificate', certpath.relative_to(HERE.parents[1]), flush=True)
    except Exception as err:
        certificate['failures'].append(type(err).__name__+': '+str(err)); save(); raise

if __name__ == '__main__': main()
