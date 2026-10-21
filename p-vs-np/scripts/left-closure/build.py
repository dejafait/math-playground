"""Paid closure assembly from complete local packages; no suffix constructor."""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'backward-zero'))
import build as b
spec = importlib.util.spec_from_file_location('closure_endpoints',HERE/'endpoints.py')
ep = importlib.util.module_from_spec(spec); spec.loader.exec_module(ep)
p,c = b.p,b.checker


class Closure(b.Store):
    def __init__(self,d,paths,library):
        self.data=d; self.tables=ep.request(d)
        if len(paths) != d['N']: raise c.Invalid('all local proof occurrences required')
        if set(library) != set(b.ep.fixed())|{'close_cancel'}:
            raise c.Invalid('fixed closure library required')
        # Exact fixed-library endpoints, never arbitrary caller tautologies.
        for name,goal in dict(b.ep.fixed(),close_cancel=ep.cancellation()).items():
            if library[name]['rows'][-1][0] != b.aggregate.native(goal):
                raise c.Invalid('fixed closure library endpoint')
        self.packages=[b.aggregate.load(path,ep.e.c.serialize(goal))
            for path,goal in zip(paths,self.tables['local'])]
        super().__init__(library,d['q'])
        self.local_roots=[self.retain(pkg,'local-'+str(v))
            for v,pkg in enumerate(self.packages)]
        self.imported_end=len(self.p.rows); self.coordinate_roots=[]; self.traces=[]

    def row(self,v):
        d=self.data; z=b.atom((9,),p.N(p.I(d['q'],d['q'])))
        y=b.atom((0,),p.I(d['q'],d['q']))
        S=[b.atom((1,w),b.aggregate.native(ep.e.c.parse(s,'native')[0]))
           for w,s in enumerate(d['suffixes'])]
        xs=[b.atom((3,j),s) for j,s in enumerate(d['letters'])]
        local_right=[b.X(y if w==d['t'] else z,b.X(b.W(d['E0'][w],S,z),
            b.Bal([b.product(xs[j],b.W(d['Eb'][j][w],S,z)) for j in range(d['n'])],z)))
            for w in range(d['N'])]
        selected=[w for w,bit in enumerate(self.tables['K'][v]) if bit]
        a,rhs,proof=b.combine(self,[S[w] for w in selected],
            [local_right[w] for w in selected],[self.local_roots[w] for w in selected],z)
        closed=b.X(y if self.tables['beta'][v][0] else z,
            b.Bal([b.product(xs[j],b.W(self.tables['G'][j][v],S,z))
                   for j in range(d['n'])],z))
        target=b.X(a,b.X(S[v],closed))
        compare,traces=b.compare(self,rhs,target,z)
        premise=self.trans(a,rhs,target,proof,compare)
        self.root=self.p.mp(premise,self.law('close_cancel',{'A':a,'B':S[v],'C':closed}))
        if p.text(self.p.rows[self.root][0]) != ep.e.c.serialize(self.tables['closed'][v]):
            raise c.Invalid('closure exact coordinate endpoint')
        if self.root != len(self.p.rows)-1: raise c.Invalid('coordinate final root')
        self.coordinate_roots.append(self.root); self.traces.extend(traces)
        return self.root


def thresholds(d,packages,constants,term_stats,library_names):
    """Changed all-size ledger, original inputs only; all N full exports paid."""
    N=d['N']; h=(1+N+d['n']).bit_length()
    V=1<<(3*h+6); H=9*h+30
    operations=10000*N*V**2*(H+1)**2
    generated=(constants['L']+1)*operations
    I=sum(len(a['rows']) for a in packages); J=I+generated
    frame=256+64*(J+1).bit_length()
    result=dict(h=h,V=V,H=H,elementary_operations=operations,generated_records=generated,
        imported_records=I,lines=J,aggregate_lines=N*J,formats={})
    for mode,factor in [('native',3),('not-or',6)]:
        t,depth,names=term_stats[mode]
        K=sum(a['node_sums'][mode] for a in packages)
        delta=max([a['depths'][mode] for a in packages]+[0])
        B=max([1,names,library_names]+[a['name_bytes'] for a in packages])
        D,S=constants[mode]['D'],constants[mode]['S']
        P=8*4**(H+1)*(t+1)
        size=(B+4)*(K+(generated+1)*S*P)+(J+2)*frame
        result['formats'][mode]=dict(lines=J,depth=max(delta,D+factor*H+depth),
            record_nodes=max(K,S*P),bytes=size,bits=8*size,aggregate_bytes=N*size,
            aggregate_bits=8*N*size,argument_nodes=P,argument_depth=factor*H+depth,
            input_term_nodes=t,input_term_depth=depth,imported_nodes=K,
            imported_depth=delta,payload_bytes=B)
    return result
