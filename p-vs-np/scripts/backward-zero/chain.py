"""One fresh finite-chain store; no external row packages or cache input."""
import build as b

ep,p,c=b.ep,b.p,b.checker


def base_request(data):
    return {key:data[key] for key in ('N','n','q','suffixes','letters','beta','G')}


def row_request(data,i,j):
    level,nxt=data['levels'][i:i+2]
    return dict(base_request(data),k=nxt['k'],r=[level['R'][j]],
                R_next=nxt['R'],T=level['T'][j])


def validate(data):
    if not isinstance(data,dict) or set(data)!={'N','n','q','suffixes','letters','beta','G','levels'}:
        raise c.Invalid('chain fields')
    if any(type(data[key]) is not int for key in ('N','n')) or data['N']<2 or data['n']<0:
        raise c.Invalid('fixed chain dimensions')
    # Check all fixed syntax/matrices even when every level is empty.
    fixed=dict(base_request(data),k=0,r=[[0]*data['N']],R_next=[],
               T=[[[]] for _ in range(data['n'])])
    coordinates=ep.strings(fixed)['coordinates']
    levels=data['levels']
    if not isinstance(levels,list) or not levels:
        raise c.Invalid('explicit nonempty level list required')
    for i,level in enumerate(levels):
        if not isinstance(level,dict) or set(level)!={'k','R','T'}:
            raise c.Invalid('level fields')
        k=level['k']
        if type(k) is not int or not 0<=k<=data['N']:
            raise c.Invalid('level dimension')
        ep._matrix(level['R'],k,data['N'],'chain R')
        if not isinstance(level['T'],list) or len(level['T'])!=k:
            raise c.Invalid('one indexed T per row required')
        if i==len(levels)-1 and k!=0:
            raise c.Invalid('terminal table must be empty')
    for i,level in enumerate(levels[:-1]):
        for j in range(level['k']): ep.request(row_request(data,i,j))
    return coordinates


class RowHandle:
    """Runtime ownership token only, never a propositional inference rule."""
    def __init__(self,owner,i,j,root):
        self.owner,self.i,self.j,self.root=owner,i,j,root


class ChainStore(b.Store):
    def __init__(self,data,coordinate_paths,library):
        coordinates=validate(data)
        if len(coordinate_paths)!=data['N']:
            raise c.Invalid('complete coordinate occurrence count')
        packages=[b.aggregate.load(path,goal) for path,goal in zip(coordinate_paths,coordinates)]
        super().__init__(library,data['q'])
        self.data=data; self.packages=packages; self.handles={}; self.rows=[]
        self.coordinate_roots=[self.retain(pkg,'coordinate-'+str(v)) for v,pkg in enumerate(packages)]
        self.imported_end=len(self.p.rows)
        # With no requested rows this is the final imported coordinate, not
        # an invented terminal zero conclusion.
        self.root=self.coordinate_roots[-1]

    def resolve(self,i,j,handle):
        if not isinstance(handle,RowHandle) or handle.owner is not self:
            raise c.Invalid('wrong chain state')
        if self.handles.get((i,j)) is not handle or (handle.i,handle.j)!=(i,j):
            raise c.Invalid('wrong indexed row provenance')
        root=handle.root
        if type(root) is not int or not 0<=root<len(self.p.rows):
            raise c.Invalid('chain root not strictly earlier')
        q=self.data['q']; z=ep.neg(ep.imp(q,q))
        S=[ep.c.parse(s,'native')[0] for s in self.data['suffixes']]
        goal=ep.eq(ep.choose(self.data['levels'][i]['R'][j],S,z),z)
        if p.text(self.p.rows[root][0])!=ep.c.serialize(goal):
            raise c.Invalid('chain row exact endpoint')
        return root

    def run(self):
        for i in range(len(self.data['levels'])-2,-1,-1):
            for j in range(self.data['levels'][i]['k']):
                roots=[self.resolve(i+1,k,self.handles[(i+1,k)])
                       for k in range(self.data['levels'][i+1]['k'])]
                result=b.emit_transition(self,row_request(self.data,i,j),self.coordinate_roots,roots)
                handle=RowHandle(self,i,j,self.root)
                self.handles[(i,j)]=handle
                self.resolve(i,j,handle)
                result.update(level=i,row=j,next_roots=roots)
                self.rows.append(result)
        return self


def compile_chain(data,coordinate_paths,library):
    return ChainStore(data,coordinate_paths,library).run()


def thresholds(data,packages,constants,term_stats,library_name_bytes):
    """Original-input-only bound; never receives derived packages/statistics."""
    m=sum(level['k'] for level in data['levels'][:-1])
    D=2+data['N']+data['n']+max(level['k'] for level in data['levels'])
    h=(D-1).bit_length(); V=1<<(3*h+4); H=9*h+20
    elementary=10000*V**2*(H+1)**2
    G=m*(constants['L']+1)*elementary
    I=sum(len(pkg['rows']) for pkg in packages); J=I+G
    framing=256+64*(J+1).bit_length()
    # One root-location record per indexed row: i,j,start,end,four roots.
    # The test certificate's optional traces are evidence, not proof output.
    location_framing=512+128*(J+len(data['levels'])+m+2).bit_length()
    metadata=(m+len(data['levels'])+data['N']+2)*location_framing
    result={'row_count':m,'dimension':D,'h':h,'V':V,'H':H,
            'elementary_per_row':elementary,'generated_records':G,
            'imported_records':I,'lines':J,'metadata_bytes':metadata,'formats':{}}
    for mode,factor in [('native',3),('not-or',6)]:
        t,depth,names=term_stats[mode]
        K=sum(pkg['node_sums'][mode] for pkg in packages)
        delta=max([pkg['depths'][mode] for pkg in packages]+[0])
        B=max([1,names,library_name_bytes]+[pkg['name_bytes'] for pkg in packages])
        Dj,Sj=constants[mode]['D'],constants[mode]['S']
        Pj=8*4**(H+1)*(t+1)
        # For m=0 the proof header is a coordinate-import conclusion.
        header=max(K,Sj*Pj)
        size=(B+4)*(K+G*Sj*Pj+header)+(J+2)*framing
        result['formats'][mode]={'lines':J,'depth':max(delta,Dj+factor*H+depth),
            'record_nodes':max(K,Sj*Pj),'bytes':size,'bits':8*size,
            'proof_and_locations_bytes':size+metadata,'argument_nodes':Pj,
            'argument_depth':factor*H+depth,'imported_nodes':K,
            'basis':'L062 fixed-suffix per-row geometry; original imports only; global references'}
    return result
