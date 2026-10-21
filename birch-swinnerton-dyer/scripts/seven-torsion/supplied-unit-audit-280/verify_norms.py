"""Independent fixed-length Horner tower arithmetic and Bär recurrence.

Imports only I/O/limits from stage_io, no producer or old arithmetic.
"""
from fractions import Fraction as Q
import copy,sys
from stage_io import R,U,read,save,start,finish

class Rational:
    zero=Q(0);one=Q(1)
    def add(self,a,b):return a+b
    def neg(self,a):return -a
    def mul(self,a,b):return a*b

class Horner:
    def __init__(self,base,mod):
        self.base=base;self.n=len(mod)-1
        assert mod[-1]==base.one
        self.mod=tuple(mod[:-1]);self.zero=(base.zero,)*self.n
        self.one=(base.one,)+(base.zero,)*(self.n-1)
    def vector(self,a):
        assert len(a)<=self.n
        return tuple(a)+(self.base.zero,)*(self.n-len(a))
    def add(self,a,b):return tuple(self.base.add(x,y) for x,y in zip(a,b))
    def neg(self,a):return tuple(self.base.neg(x) for x in a)
    def shift(self,a):
        r=[self.base.zero]+list(a[:-1]);top=a[-1]
        if top!=self.base.zero:
            for i,c in enumerate(self.mod):
                if c!=self.base.zero:r[i]=self.base.add(r[i],self.base.neg(self.base.mul(top,c)))
        return tuple(r)
    def mul(self,a,b):
        if a==self.zero or b==self.zero:return self.zero
        if a==self.one:return b
        if b==self.one:return a
        r=self.zero
        for c in reversed(b):
            r=self.shift(r)
            if c!=self.base.zero:r=self.add(r,tuple(self.base.mul(c,x) if x!=self.base.zero else self.base.zero for x in a))
        return r
    def reduce(self,coeff):
        r=self.zero
        for c in reversed(coeff):
            r=self.shift(r);r=(self.base.add(r[0],c),)+r[1:]
        return r

t=start();out={'passed':False,'checks':[],'failures':[]}
def need(ok,label):
    if not ok:raise ValueError(label)
    out['checks'].append(label)
try:
    quo=read(U/'quotient-254/quotient.json');dual=read(U/'dual-263/dual.json')
    point=read(U/'certificate.json');fiber=read(U/'incidence-269/fiber.json')
    units=read(U/'incidence-269/units-and-y.json');maps=read(U/'incidence-269/pullbacks.json')
    produced=read(R/'supplied-matrices.json');savednorm=read(R/'supplied-norms.json')
    D=Horner(Rational(),tuple(map(Q,quo['h'])))
    def d(a):return D.vector(tuple(map(Q,a)))
    L=Horner(D,tuple(d(a) for a in dual['k']))
    def l(a):return L.vector(tuple(d(v) for v in a))
    cp=L.reduce((d(quo['target_b']),d(quo['target_a']),D.zero,D.one))
    need(L.mul(cp,l(dual['curve_inverse']))==L.one,'full_cprime_unit')
    def pm(a,b):
        v=[D.zero]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):v[i+j]=D.add(v[i+j],D.mul(x,y))
        return v
    q=[d(v) for v in quo['q']];N=[d(v) for v in quo['x_numerator']]
    M=[d(v) for v in quo['y_multiplier_numerator']];qq=pm(q,q)
    F=tuple(L.vector((N[i],D.neg(qq[i]) if i<len(qq) else D.zero)) for i in range(len(N)))
    need(tuple(F)==tuple(l(v) for v in fiber['F'])==tuple(l(v) for v in produced['F']) and len(F)==8 and F[-1]==L.one,'all_full_F_coefficients')
    need(tuple(map(Q,fiber['h']))==tuple(map(Q,quo['h'])) and tuple(l([v]) for v in fiber['k'])==tuple(l([v]) for v in dual['k']) and l(fiber['cprime'])==cp,'all_full_B_coefficients')
    E=Horner(L,F)
    def e(a):return E.vector(tuple(l(v) for v in a))
    def lift(a):return E.reduce(tuple(L.vector((v,)) for v in a))
    def constant(a):return E.vector((a,))
    def escale(a,n):return tuple(tuple(tuple(x*n for x in v) for v in w) for w in a)
    X=E.vector((L.zero,L.one));eq=lift(q);mi=e(units['M_inverse'])
    need(E.mul(lift(M),mi)==E.one,'whole_M_inverse')
    yf=E.mul(E.mul(E.mul(eq,eq),eq),mi)
    need(yf==e(units['y_V_factor'])==e(produced['y_V_factor']),'independently_reconstructed_full_y_factor')
    need(E.mul(constant(cp),E.mul(yf,yf))==lift((d([46224]),d([-3024]),D.zero,D.one)),'full_source_relation')
    # Explicit B pair retains even and odd components, no selected factor.
    bz=(L.zero,L.zero);bo=(L.one,L.zero)
    def ba(a,b):return (L.add(a[0],b[0]),L.add(a[1],b[1]))
    def bn(a):return (L.neg(a[0]),L.neg(a[1]))
    def bm(a,b):
        if a==bz or b==bz:return bz
        if a==bo:return b
        if b==bo:return a
        ac=L.mul(a[0],b[0]);bd=L.mul(a[1],b[1])
        return (L.add(ac,L.mul(cp,bd)),L.add(L.mul(a[0],b[1]),L.mul(a[1],b[0])))
    def bs(a,n):return tuple(tuple(tuple(n*x for x in v) for v in w) for w in a)
    def bf(a):return tuple(a[eps][i][j] for eps in range(2) for i in range(3) for j in range(8))
    def iff(a,b):return tuple((a if eps==0 else b)[r][i][j] for r in range(7) for eps in range(2) for i in range(3) for j in range(8))
    def unf(v):
        assert len(v)==336
        return tuple(tuple(tuple(tuple(v[r*48+eps*24+i*8+j] for j in range(8)) for i in range(3)) for r in range(7)) for eps in range(2))
    for i in range(336):
        v=tuple(Q(i==j) for j in range(336))
        need(iff(*unf(v))==v,'basis_roundtrip_'+str(i))
    p=E.one;std=[];odd=[]
    for j in range(24):
        std.append(iff(p,E.zero));odd.append(iff(E.zero,E.mul(p,yf)));p=E.shift(p)
    std+=odd
    power=[];a=E.one;b=E.zero
    for j in range(48):
        power.append(iff(a,b))
        if j<47:a,b=E.mul(constant(cp),E.mul(b,yf)),E.mul(a,yf)
    oldtrans=read(R/'construction-transports.json')
    for key,cols in [('point_standard_columns',std),('point_power_columns',power)]:
        need(cols==[tuple(map(Q,v)) for v in maps[key]]==[tuple(map(Q,v)) for v in oldtrans[key]],'every_entry_'+key)
    for key,cols,wanted in [('matrix',std,power),('inverse',power,std)]:
        mat=[[Q(v) for v in row] for row in point[key]]
        for j in range(48):
            v=tuple(sum((mat[i][j]*cols[i][n] for i in range(48) if mat[i][j] and cols[i][n]),Q(0)) for n in range(336))
            need(v==wanted[j],'full_transport_'+key+'_'+str(j))
    ox=iff(escale(E.add(X,E.neg(lift((d([12]),)))),Q(1,36)),E.zero)
    oy=iff(lift((d([Q(-1,2)]),)),escale(yf,Q(1,216)))
    for key,v in [('point_original_x',ox),('point_original_y',oy)]:
        need(v==tuple(map(Q,maps[key]))==tuple(map(Q,oldtrans[key])),'all_coordinates_'+key)
    line=[tuple(Q(i==j) for i in range(336)) for j in range(48)]
    need(line==[tuple(map(Q,v)) for v in maps['line_columns']],'all_48_line_inclusions')
    save('verification-transports.json',{'point_standard_columns':std,'point_power_columns':power,'point_original_x':ox,'point_original_y':oy,'line_columns':line,'basis_roundtrips':336,'transport_columns':96})
    out['location']='independent full source units'
    P=Horner(Rational(),tuple(map(Q,point['f'])))
    pc=P.reduce(tuple(map(Q,[46224,-3024,0,1])))
    az=(P.zero,P.zero);ao=(P.one,P.zero)
    def am(u,v):return (P.add(P.mul(u[0],v[0]),P.mul(pc,P.mul(u[1],v[1]))),P.add(P.mul(u[0],v[1]),P.mul(u[1],v[0])))
    def apow(u,n):
        r=ao
        while n:
            if n%2:r=am(r,u)
            n//=2
            if n:u=am(u,u)
        return r
    def af(u):return u[0]+u[1]
    def au(v):
        if len(v)!=48:raise ValueError('full_source_48_shape')
        w=tuple(map(Q,v));return (w[:24],w[24:])
    def convert(v,mat):return tuple(sum((Q(mat[i][j])*v[j] for j in range(48) if v[j] and Q(mat[i][j])),Q(0)) for i in range(48))
    supplied=read(R/'supplied-inputs.json')['elements'];labels=('a','b','a_prime','scalar2')
    need(set(supplied)==set(labels),'exact_supplied_unit_labels')
    a=(P.vector((Q(0),Q(1))),P.one);b=(P.one,P.one)
    wanted={'a':a,'b':b,'a_prime':am(a,apow(b,7)),'scalar2':(P.vector((Q(2),)),P.zero)}
    def input_test(rows):
        if set(rows)!=set(labels):raise ValueError('supplied_input_labels')
        for label in labels:
            row=rows[label]
            for key in ('standard','inverse_standard','power','inverse_power'):
                if len(row[key])!=48:raise ValueError('full_source_48_shape')
            u=au(row['standard']);ui=au(row['inverse_standard'])
            if u==az:raise ValueError('zero_is_not_a_supplied_unit')
            if am(u,ui)!=ao:raise ValueError('full_source_unit_inverse_product')
            if u!=wanted[label]:raise ValueError('exact_mixed_input_value')
            for key,dest in (('power','standard'),('inverse_power','inverse_standard')):
                v=tuple(map(Q,row[key]));w=tuple(map(Q,row[dest]))
                if convert(v,point['matrix'])!=w or convert(w,point['inverse'])!=v:raise ValueError('all_input_basis_transports')
    input_test(supplied);need(True,'all_full_source_inputs_inverses_and_transports')
    rejections=[]
    def reject(case,data,fn,expected):
        save('mutant-'+case+'.json',data)
        try:fn(data)
        except ValueError as exc:
            need(str(exc)==expected,'intended_'+case)
            rejections.append({'case':case,'rejected':True,'condition':str(exc),'full_malformed_replay':False,'scope':'named full-data condition only'})
        else:raise ValueError('accepted mutant '+case)
    bad=copy.deepcopy(supplied);bad['a']['inverse_standard'][0]=str(Q(bad['a']['inverse_standard'][0])+1)
    reject('inverse-one-coefficient',bad,input_test,'full_source_unit_inverse_product')
    bad=copy.deepcopy(supplied);bad['a']['standard']=['0']*48
    reject('zero-supplied-unit',bad,input_test,'zero_is_not_a_supplied_unit')
    bad=copy.deepcopy(supplied);bad['a']['power']=bad['a']['power'][:-1]
    reject('missing-source-coordinate',bad,input_test,'full_source_48_shape')
    def im(u,v):return (E.add(E.mul(u[0],v[0]),E.mul(constant(cp),E.mul(u[1],v[1]))),E.add(E.mul(u[0],v[1]),E.mul(u[1],v[0])))
    def ipow(u,n):
        r=(E.one,E.zero)
        while n:
            if n%2:r=im(r,u)
            n//=2
            if n:u=im(u,u)
        return r
    def pull(u):
        def evalp(v):
            r=E.zero
            for z in reversed(v):
                r=E.shift(r);r=E.add(r,constant(L.vector((d([z]),))))
            return r
        return (evalp(u[0]),E.mul(evalp(u[1]),yf))
    pulls={};invpulls={};oldpull=read(R/'input-pullbacks.json')
    for label in labels:
        row=supplied[label];pulls[label]=pull(au(row['standard']));invpulls[label]=pull(au(row['inverse_standard']))
        need(im(pulls[label],invpulls[label])==(E.one,E.zero),'all_incidence_inverse_coefficients_'+label)
        for key,v in (('element',pulls[label]),('inverse',invpulls[label])):
            need(iff(*v)==tuple(map(Q,oldpull[label][key])),'all_336_pullback_coefficients_'+label+'_'+key)
    need(am(au(supplied['a']['standard']),apow(au(supplied['b']['standard']),7))==au(supplied['a_prime']['standard']),'full_source_representative_change')
    need(im(pulls['a'],ipow(pulls['b'],7))==pulls['a_prime'],'full_incidence_representative_change')
    save('independent-inputs.json',{'elements':{label:{'element':iff(*pulls[label]),'inverse':iff(*invpulls[label]),'inverse_product':iff(*im(pulls[label],invpulls[label]))} for label in labels},'source_products':{label:af(am(au(supplied[label]['standard']),au(supplied[label]['inverse_standard']))) for label in labels}})
    matrices={}
    for name,(a,b) in list(pulls.items())+[('zero',(E.zero,E.zero))]:
        cols=[]
        for j in range(7):
            cols.append([(a[i],b[i]) for i in range(7)])
            if j<6:a,b=E.shift(a),E.shift(b)
        matrices[name]=[[cols[j][i] for j in range(7)] for i in range(7)]
    flat={name:[[bf(v) for v in row] for row in mat] for name,mat in matrices.items()}
    def matrix_test(data):
        if set(data)!=set(matrices) or any(len(data[k])!=7 or any(len(row)!=7 or any(len(v)!=48 for v in row) for row in data[k]) for k in data):raise ValueError('full_matrix_48_shape')
        if {k:[[tuple(map(Q,v)) for v in row] for row in mat] for k,mat in data.items()}!=flat:raise ValueError('all_matrix_coefficient_comparison')
    matrix_test(produced['matrices']);need(produced['rational_slots']==11760,'all_11760_matrix_slots')
    save('independent-matrices.json',{'matrices':flat,'rational_slots':11760})
    bad=copy.deepcopy(produced['matrices']);bad['a'][0][0][24]=str(Q(bad['a'][0][0][24])+1)
    reject('odd-V-matrix-coefficient',bad,matrix_test,'all_matrix_coefficient_comparison')
    print('Independent full source units, pullbacks and 11760 matrix slots pass.',flush=True)
    def mm(a,b):
        c=[[bz for _ in range(7)] for _ in range(7)]
        for i in range(7):
            for k in range(7):
                if a[i][k]!=bz:
                    for j in range(7):
                        if b[k][j]!=bz:c[i][j]=ba(c[i][j],bm(a[i][k],b[k][j]))
        return c
    def mf(a):return [[bf(v) for v in row] for row in a]
    def faddeev(a,label):
        n=[[bo if i==j else bz for j in range(7)] for i in range(7)]
        coeff=[bo];records=[]
        for k in range(1,8):
            product=mm(a,n);trace=bz
            for i in range(7):trace=ba(trace,product[i][i])
            ck=bs(trace,Q(-1,k));nnext=[row[:] for row in product]
            for i in range(7):nnext[i][i]=ba(nnext[i][i],ck)
            coeff.append(ck)
            record={'k':k,'N_k':mf(n),'A_N_k':mf(product),'trace':bf(trace),'c_k':bf(ck),'N_next':mf(nnext)}
            path='faddeev-'+label+'-'+str(k)+'.json';save(path,record);records.append(path)
            n=nnext
            print('Faddeev '+label+' k='+str(k),flush=True)
        need(all(v==bz for row in n for v in row),'terminal_zero_'+label)
        norm=bn(coeff[-1])
        save('faddeev-'+label+'-result.json',{'characteristic_coefficients':[bf(v) for v in coeff],'norm':bf(norm),'terminal_zero_matrix':mf(n),'recurrence_records':records})
        return norm
    norms={}
    for name in ('zero','scalar2','a','b','a_prime'):
        out['location']='Faddeev '+name
        norms[name]=faddeev(matrices[name],name)
        lap=read(R/('laplace-'+name+'.json'))
        need(tuple(map(Q,lap['norm']))==bf(norms[name])==tuple(map(Q,savednorm['norms'][name])),'all_48_determinant_coefficients_'+name)
    need(norms['zero']==bz and norms['scalar2']==bs(bo,128),'independent_zero_scalar_norms')
    def bp(u,n):
        r=bo
        while n:
            if n%2:r=bm(r,u)
            n//=2
            if n:u=bm(u,u)
        return r
    representative=bm(norms['a'],bp(norms['b'],7))
    need(representative==norms['a_prime'],'all_norm_representative_change_coefficients')
    for key in ('lhs','rhs'):need(tuple(map(Q,savednorm['representative_change'][key]))==bf(representative),'saved_full_representative_'+key)
    def bu(v):
        if len(v)!=48:raise ValueError('full_B_shape')
        w=tuple(map(Q,v));return tuple(tuple(tuple(w[e*24+i*8+j] for j in range(8)) for i in range(3)) for e in range(2))
    root=savednorm['positive_scalar_control'];beta=bu(root['beta']);betai=bu(root['beta_inv'])
    need(beta==bs(bo,2) and betai==bs(bo,Q(1,2)) and bm(beta,betai)==bo and bp(beta,7)==norms['scalar2'] and tuple(map(Q,root['beta7']))==bf(bp(beta,7)),'full_positive_scalar_root_and_inverse')
    def norm_test(data):
        if set(data)!=set(norms) or any(len(data[k])!=48 or tuple(map(Q,data[k]))!=bf(norms[k]) for k in data):raise ValueError('all_norm_coefficient_comparison')
    norm_test(savednorm['norms']);bad=copy.deepcopy(savednorm['norms']);bad['a'][0]=str(Q(bad['a'][0])+1)
    reject('norm-one-coefficient',bad,norm_test,'all_norm_coefficient_comparison')
    save('rejections.json',rejections)
    save('verification-summary.json',{'norms':{k:bf(v) for k,v in norms.items()},'all_matrix_coefficients_equal':True,'all_norm_coefficients_equal':True,'representative_change':{'lhs':bf(representative),'rhs':bf(norms['a_prime'])},'positive_scalar_control':root,'rejections':rejections,'mixed_root_claim':False})
    out.update(passed=True,rational_matrix_slots=11760,norm_slots=240,element_count=5,rejection_count=len(rejections))
except Exception as exc:out['failures'].append(type(exc).__name__+': '+str(exc))
finally:finish('verification',out,t)
sys.exit(0 if out['passed'] else 1)
