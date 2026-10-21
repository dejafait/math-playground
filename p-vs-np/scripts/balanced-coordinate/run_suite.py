"""One bounded implementation test; complete artifacts, compact actual/bound output."""
import argparse
import gzip
import json
import math
from pathlib import Path
import aggregate
import endpoints
primitive, checker = aggregate.primitive, aggregate.checker
HERE = Path(__file__).resolve().parent
OUT = HERE/'output'
SLOT = HERE.parent/'balanced-slot'/'output'

def save(path,obj): path.write_text(json.dumps(obj,indent=2)+'\n')
def raw_records(path):
    with gzip.open(path,'rt') as f:
        header = json.loads(next(f)); rows = [json.loads(s) for s in f]
    return header,rows
def write_records(path,header,rows):
    with gzip.open(path,'wt') as f:
        for row in [header]+rows: f.write(json.dumps(row,separators=(',',':'))+'\n')

def package(path, law, env, u, v, pad, library):
    rows = []
    if pad:
        deep = 'A'
        for _ in range(pad): deep = primitive.N(deep)
        rows.append({'f':primitive.text(primitive.I(deep,primitive.I('q',deep))),
                     'rule':'ax1','subs':{'A':primitive.text(deep),'B':'q'}})
    offset = len(rows)
    for f,rule,refs,subs in library[law]['rows']:
        row = {'f':primitive.text(primitive.sub(f,env)),'rule':rule}
        if rule == 'mp': row['refs'] = [k+offset for k in refs]
        else: row['subs'] = {k:primitive.text(primitive.sub(t,env)) for k,t in subs.items()}
        rows.append(row)
    write_records(path,{'format':'native','goal':endpoints.coordinate(u,v)},rows)
    return checker.check(path,endpoints.coordinate(u,v))

def main():
    parser = argparse.ArgumentParser(); parser.add_argument('--case',default='all',choices=['all','m2','m4','m8'])
    args = parser.parse_args(); OUT.mkdir(exist_ok=True)
    cert = {'complete':False,'failures':[],'library':{},'cases':[],'corruptions':[]}
    certpath = OUT/'certificate-176.json'; save(certpath,cert)
    try:
        library = {}
        for name in ['congL','congR','trans','refl','comm','double_neg_bridge']:
            expected = primitive.text(primitive.schemas()[name])
            library[name] = aggregate.load(SLOT/(name+'.native.jsonl.gz'),expected)
            cert['library'][name] = library[name]['measurement']; save(certpath,cert)
        L = 3470
        constants = {'native':{'D':18,'S':2456,'c':3},'not-or':{'D':25,'S':3492,'c':6}}
        cert['constants'] = {'L':L,**constants}
        # Fully check selected image templates too, against independent translation.
        for name in ['congL','congR','trans']:
            native_goal = checker.parse(primitive.text(primitive.schemas()[name]),'native')[0]
            expected = checker.serialize(endpoints.image(native_goal))
            measured = checker.check(SLOT/(name+'.not-or.jsonl.gz'),expected)
            cert['library'][name+'-image'] = measured
            assert measured['max_line_depth'] <= constants['not-or']['D']
            assert measured['max_record_nodes'] <= constants['not-or']['S']
            assert library[name]['measurement']['lines'] <= L
            assert library[name]['measurement']['max_line_depth'] <= constants['native']['D']
            assert library[name]['measurement']['max_record_nodes'] <= constants['native']['S']
        # Tests contain variable collisions, constants, mixed lengths and nontrivial equalities.
        n,i,x = primitive.N,primitive.I,primitive.X
        specs = {
            'm2':[('comm',{'A':'A','B':'q'},x('A','q'),x('q','A'),0),
                  ('double_neg_bridge',{'A':'B'},'B',n(n('B')),24)],
            'm4':[('refl',{'A':primitive.Z},primitive.Z,primitive.Z,0),
                  ('comm',{'A':'A','B':'B'},x('A','B'),x('B','A'),0),
                  ('double_neg_bridge',{'A':i('q','q')},i('q','q'),n(n(i('q','q'))),12),
                  ('refl',{'A':'A'},'A','A',0)],
            'm8':[('double_neg_bridge',{'A':'C'},'C',n(n('C')),0)]+
                  [('refl',{'A':a},a,a,30 if k==5 else 0) for k,a in enumerate(['q','A','A','B','B','q','C'])]
        }
        for name,spec in specs.items():
            if args.case not in ('all',name): continue
            us = [primitive.text(s[2]) for s in spec]; vs = [primitive.text(s[3]) for s in spec]
            paths = []
            for k,(law,env,u,v,pad) in enumerate(spec):
                path = OUT/(name+'-coordinate-'+str(k)+'.native.jsonl.gz')
                package(path,law,env,us[k],vs[k],pad,library); paths.append(path)
            combination = aggregate.Combination(us,vs,paths,library); combination.run()
            m = len(us); h = m.bit_length()-1
            N = sum(len(p['rows']) for p in combination.packages)
            G = (m-1)*(3*L+4); J = N+G
            case = {'name':name,'U':us,'V':vs,'M':m,'h':h,'N':N,'G':G,'J':J,
                    'input_bytes':sum(p['measurement']['bytes'] for p in combination.packages),
                    'input_paths':[str(p.relative_to(HERE.parents[1])) for p in paths],
                    'inputs':[dict(p['measurement'],depths=p['depths'],node_sums=p['node_sums'],name_bytes=p['name_bytes']) for p in combination.packages],
                    'imports':combination.imports,'events':combination.events,'proofs':{}}
            assert len(combination.events) == m-1
            # Exact unpruned retention/relocation is checked against every supplied record.
            for entry,p in zip(combination.imports,combination.packages):
                for k,(f,rule,refs,subs) in enumerate(p['rows']):
                    out = combination.p.rows[entry['start']+k]
                    assert out[0] == f and out[1] == rule and out[3] == (subs if rule!='mp' else None)
                    assert tuple(out[2]) == tuple(entry['start']+r for r in refs)
            for image,mode in [(False,'native'),(True,'not-or')]:
                path = OUT/(name+'.'+mode+'.jsonl.gz'); written = combination.write(path,image)
                expected = endpoints.goal(us,vs,mode); measured = checker.check(path,expected)
                assert measured['sha256'] == written['sha256'] and measured['bytes'] == written['bytes']
                terms = [checker.parse(s,'native')[0] for s in us+vs]
                if image: terms = [endpoints.image(t) for t in terms]
                ts = [endpoints.stats(t) for t in terms]
                t,d = max(s[0] for s in ts),max(s[1] for s in ts)
                B = max([1]+[s[2] for s in ts]+[p['name_bytes'] for p in combination.packages])
                K = sum(p['node_sums'][mode] for p in combination.packages)
                delta = max(p['depths'][mode] for p in combination.packages)
                P = 8*4**(h+1)*(t+1); S,D,c = (constants[mode][key] for key in ['S','D','c'])
                framing = 256+64*math.ceil(math.log2(J+2))
                bounds = {'lines':J,'depth':max(delta,D+c*h+d),
                          'record_nodes':max(K,S*P),
                          'bytes':(B+4)*(K+(G+1)*S*P)+(J+2)*framing}
                bounds['bits'] = 8*bounds['bytes']
                tests = {key:measured[field] <= bounds[key] for key,field in
                         [('lines','lines'),('depth','max_line_depth'),('record_nodes','max_record_nodes'),('bytes','bytes')]}
                # Inspect every actual growing argument, rather than using a preview.
                arg_stats = [endpoints.stats(checker.parse(s,'native')[0] if not image else
                            endpoints.image(checker.parse(s,'native')[0])) for event in combination.events for s in event['arguments']]
                argmax = {'nodes':max(s[0] for s in arg_stats),'depth':max(s[1] for s in arg_stats)}
                tests['argument_nodes'] = argmax['nodes'] <= P
                tests['argument_depth'] = argmax['depth'] <= c*h+d
                assert all(tests.values()),tests
                case['proofs'][mode] = {'expected_goal':expected,'measurement':dict(measured,storage_bytes=written['storage_bytes']),
                                       'parameters':{'t':t,'d':d,'B':B,'K':K,'delta':delta,'P':P},
                                       'bounds':bounds,'tests':tests,'arguments':argmax}
                print(name,mode,'lines',measured['lines'],'/',J,'depth',measured['max_line_depth'],'/',bounds['depth'],
                      'bytes',measured['bytes'],'/',bounds['bytes'],'all checks passed',flush=True)
            cert['cases'].append(case); save(certpath,cert)
            if name == 'm2':
                header,rows = raw_records(paths[1]); mp = next(k for k,r in enumerate(rows) if r['rule']=='mp')
                wrongmp = next(k for k,r in enumerate(rows) if r['rule']=='mp' and
                              any(rows[j]['f'] != rows[r['refs'][0]]['f'] for j in range(k)))
                other = next(j for j in range(wrongmp) if rows[j]['f'] != rows[rows[wrongmp]['refs'][0]]['f'])
                changes = [('endpoint',None,dict(header,goal='BAD_ENDPOINT')),
                           ('axiom-substitution',0,dict(rows[0],subs=dict(rows[0]['subs'],A='BAD_SUBSTITUTION'))),
                           ('forward-reference',mp,dict(rows[mp],refs=[0,len(rows)])),
                           ('mp-antecedent',wrongmp,dict(rows[wrongmp],refs=[other,rows[wrongmp]['refs'][1]])),
                           ('premise-rule',0,{'f':rows[0]['f'],'rule':'assume'}),
                           ('image-input',None,dict(header,format='not-or'))]
                for label,k,replacement in changes:
                    hh = dict(header); rr = list(rows)
                    if k is None: hh = replacement
                    else: rr[k] = replacement
                    bad = OUT/('corrupt-'+label+'.native.jsonl.gz'); write_records(bad,hh,rr)
                    try: aggregate.Combination(us,vs,[paths[0],bad],library)
                    except (checker.Invalid,ValueError) as err:
                        cert['corruptions'].append({'case':label,'path':str(bad.relative_to(HERE.parents[1])),
                                                    'rejected':True,'reason':str(err)})
                    else: raise AssertionError('corruption accepted: '+label)
                for label,badpaths,badvs in [('missing-proof',paths[:1],vs),('different-request',paths,['q']+vs[1:])]:
                    try: aggregate.Combination(us,badvs,badpaths,library)
                    except checker.Invalid as err:
                        cert['corruptions'].append({'case':label,'rejected':True,'reason':str(err)})
                    else: raise AssertionError('bad request accepted: '+label)
                save(certpath,cert); print('eight supplied-input rejection checks passed',flush=True)
        cert['complete'] = True; save(certpath,cert)
        print('complete certificate',certpath.relative_to(HERE.parents[1]),'failures',len(cert['failures']),flush=True)
    except Exception as err:
        cert['failures'].append(repr(err)); save(certpath,cert); raise

if __name__ == '__main__': main()
