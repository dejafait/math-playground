"""Fresh complete-record guarded context lifting, using checked fixed strings."""
import sys
from pathlib import Path
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE.parent/'balanced-coordinate'))
import aggregate
import context_endpoints as endpoint
primitive,checker=aggregate.primitive,aggregate.checker

def conjunction(a,b): return primitive.N(primitive.I(a,primitive.N(b)))

class Lift(aggregate.Combination):
    def __init__(self,g,u,v,context,path,library):
        endpoint.request(g,u,v,context)
        if path is None: raise checker.Invalid('complete proof required')
        self.g=aggregate.native(endpoint.validate_term(g))
        self.u=aggregate.native(endpoint.validate_term(u)); self.v=aggregate.native(endpoint.validate_term(v))
        self.context=context
        self.package=aggregate.load(path,endpoint.coordinate(g,u,v))
        self.p=aggregate.AppendProof(); self.library=library; self.events=[]
        self.import_root=self.copy(self.package['rows'],{})
        self.root=self.import_root

    def run(self):
        def fixed(node):
            if 'term' in node: return aggregate.native(endpoint.validate_term(node['term']))
            op=primitive.X if node['op']=='xor' else conjunction
            return op(fixed(node['left']),fixed(node['right']))
        def marked(node):
            if 'mark' in node: return True
            if 'term' in node: return False
            return marked(node['left']) or marked(node['right'])
        def go(node):
            if 'mark' in node: return self.u,self.v,self.import_root
            position='left' if marked(node['left']) else 'right'
            sibling='right' if position=='left' else 'left'
            a,b,prior=go(node[position]); c=fixed(node[sibling])
            name=node['op']+'-'+position
            law=self.use(name,{'A':a,'B':b,'C':c,'G':self.g})
            root=self.p.mp(prior,law)
            op=primitive.X if node['op']=='xor' else conjunction
            uu,vv=(op(a,c),op(b,c)) if position=='left' else (op(c,a),op(c,b))
            assert self.p.rows[root][0]==primitive.I(self.g,primitive.E(uu,vv))
            self.events.append({'template':name,'prior':prior,'law':law,'root':root,
                                'arguments':{k:primitive.text(t) for k,t in
                                             [('A',a),('B',b),('C',c),('G',self.g)]}})
            return uu,vv,root
        _,_,self.root=go(self.context)
        assert self.root==len(self.p.rows)-1
        assert primitive.text(self.p.rows[self.root][0])==endpoint.goal(
            primitive.text(self.g),primitive.text(self.u),primitive.text(self.v),self.context)
        return self.root
