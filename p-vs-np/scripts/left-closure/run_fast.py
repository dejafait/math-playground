"""Same compiler, smaller paid local test inputs; preserve initial evidence."""
import json
import shutil
import run as h

b,p,c,ep,lc=h.b,h.p,h.c,h.ep,h.lc
OUT=h.OUT; ROOT=h.ROOT


def fixture(name,lib):
    assert name=='diamond-small-input'
    q='A'; y=b.atom((0,),p.I(q,q)); z=b.atom((9,),p.N(p.I(q,q)))
    x=b.atom((3,0),q); a=b.atom((2,0,3),b.P(q,b.nt(y)))
    views=[a,b.X(y,a),y,y]
    E0=[[0,1,1,0],[0,0,0,1],[0,0,0,1],[0,0,0,0]]
    Eb=[[[0,0,0,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]]]
    d=dict(N=4,n=1,q=q,t=3,suffixes=[p.text(b.nt(s)) for s in views],
           letters=[q],E0=E0,Eb=Eb)
    goals=ep.request(d)['local']; paths=[]
    for v in range(4):
        o=b.Store(lib,q); extra=[]
        if v==0:
            deep='unused'
            for _ in range(35):deep=p.N(deep)
            extra=[o.p.ax('ax1',deep,'A')]
        const=b.W(E0[v],views,z)
        if v==0:
            # Five exact paid steps: (Y XOR a) XOR Y -> a.
            t1=b.X(y,b.X(a,y)); t2=b.X(y,b.X(y,a))
            t3=b.X(b.X(y,y),a); t4=b.X(z,a)
            j=o.law('assoc',{'A':y,'B':a,'C':y})
            comm=o.law('comm',{'A':a,'B':y})
            j2=o.p.mp(comm,o.law('congR',{'A':b.X(a,y),'B':b.X(y,a),'C':y}))
            j=o.trans(const,t1,t2,j,j2)
            j2=o.symm(t3,t2,o.law('assoc',{'A':y,'B':y,'C':a}))
            j=o.trans(const,t2,t3,j,j2)
            j2=o.p.mp(o.law('cancel',{'A':y}),
                o.law('congL',{'A':b.X(y,y),'B':z,'C':a}))
            j=o.trans(const,t3,t4,j,j2)
            jc=o.trans(const,t4,a,j,o.law('zeroL',{'A':a}));small_const=a
        else:
            small_const=const;jc=o.refl(const)
        var=b.product(x,b.W(Eb[0][v],views,z))
        if v==1:
            assert b.nt(var)==b.nt(a)
            small_var=a;jv=o.refl(a)
        else:
            assert var==b.product(x,z)
            small_var=z;jv=o.law('prod_zero',{'A':x})
        old=b.X(const,var); mid=b.X(small_const,small_var)
        j=o.congr(const,small_const,var,small_var,jc,jv)
        if small_var==z:
            inner=small_const
            j=o.trans(old,mid,inner,j,o.law('zeroR',{'A':small_const}))
        else:inner=mid
        B=y if v==3 else z; rhs=b.X(B,old); next_rhs=b.X(B,inner)
        lift=o.p.mp(j,o.law('congR',{'A':old,'B':inner,'C':B}))
        if inner==z:
            reduced=B;last=o.law('zeroR',{'A':B})
        else:
            assert B==z
            reduced=inner;last=o.law('zeroL',{'A':inner})
        assert b.nt(reduced)==b.nt(views[v])
        root=o.symm(rhs,views[v],o.trans(rhs,next_rhs,views[v],lift,last))
        assert p.text(o.p.rows[root][0])==ep.e.c.serialize(goals[v])
        path=OUT/(name+'-local-'+str(v)+'.native.jsonl.gz')
        h.suite.fixture_write(o,root,path,extra)
        c.check(path,ep.e.c.serialize(goals[v]));paths.append(path)
        print('small genuine local input',v,'checked',flush=True)
    (OUT/(name+'.request.json')).write_text(json.dumps(d,indent=2)+'\n')
    return d,paths


def main():
    initial=json.loads((OUT/'certificate-202.json').read_text())
    assert len(initial['cases'])==1 and initial['cases'][0]['complete']
    if not (OUT/'certificate-202-interrupted.json').exists():
        shutil.copyfile(OUT/'certificate-202.json',OUT/'certificate-202-interrupted.json')
    cert=dict(step=202,library=initial['library'],constants=initial['constants'],
        cases=initial['cases'],rejections=[],failures=[],complete=False,
        interrupted_initial_fixture='diamond-local-0.native.jsonl.gz',
        initial_run='run-202.log',initial_certificate='certificate-202-interrupted.json')
    h.DEST=OUT/'certificate-202-fast.json';h.save(cert)
    # Reuse unchanged checked fixed strings; never reuse a populated proof store.
    lib={}
    for name,goal in dict(b.ep.fixed(),close_cancel=ep.cancellation()).items():
        path=ROOT/cert['library'][name]['native']['path'] if 'path' in cert['library'][name]['native'] else None
        if path is None:
            if name=='close_cancel': path=OUT/'close_cancel.native.jsonl.gz'
            elif name in ('zeroR','zeroL','prod_zero'):
                path=OUT.parent.parent/'backward-zero'/'output'/(name+'.native.jsonl.gz')
            else:
                location='balanced-distribution' if name in ('dist','prod_cong') else 'balanced-slot'
                path=OUT.parent.parent/location/'output'/(name+'.native.jsonl.gz')
        lib[name]=b.aggregate.load(path,ep.e.c.serialize(goal))
        assert lib[name]['measurement']['sha256']==cert['library'][name]['native']['sha256']
    h.fixture=fixture
    try:
        d,paths,obj,record=h.test_case('diamond-small-input',lib,cert)
        assert obj.tables['beta']==[[0],[1],[1],[1]]
        assert obj.tables['G'][0][0][3]==1 and sum(obj.tables['K'][0])==3
        h.rejections(d,paths,lib,record,cert)
        cert['complete']=True;h.save(cert)
        print('PASS six complete export pairs, five rejections;',h.DEST.relative_to(ROOT),flush=True)
    except BaseException as exc:
        cert['failures'].append(type(exc).__name__+': '+str(exc));h.save(cert);raise

if __name__=='__main__':main()
