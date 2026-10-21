"""Full coordinate matrices; sparse convolution and Laplace determinants."""
from fractions import Fraction as Q
from functools import lru_cache
import copy,sys
from stage_io import R,U,read,save,start,finish

class Rat:
    zero=Q(0);one=Q(1)
    def add(self,a,b):return a+b
    def neg(self,a):return -a
    def mul(self,a,b):return a*b

class Sparse:
    zero=()
    def __init__(self,base,mod):
        self.base=base;self.mod=self.trim(mod);self.n=len(self.mod)-1
        assert self.mod[-1]==base.one
        self.one=(base.one,)
    def trim(self,a):
        a=list(a)
        while a and a[-1]==self.base.zero:a.pop()
        return tuple(a)
    def add(self,a,b):
        return self.trim([self.base.add(a[i] if i<len(a) else self.base.zero,b[i] if i<len(b) else self.base.zero) for i in range(max(len(a),len(b)))])
    def neg(self,a):return self.trim([self.base.neg(v) for v in a])
    def reduce(self,a):
        a=list(a)
        for i in range(len(a)-1,self.n-1,-1):
            v=a[i]
            if v!=self.base.zero:
                for j,c in enumerate(self.mod[:-1]):
                    if c!=self.base.zero:a[i-self.n+j]=self.base.add(a[i-self.n+j],self.base.neg(self.base.mul(v,c)))
        return self.trim(a[:self.n])
    def mul(self,a,b):
        if a==self.zero or b==self.zero:return self.zero
        if a==self.one:return b
        if b==self.one:return a
        d={}
        for i,x in enumerate(a):
            if x!=self.base.zero:
                for j,y in enumerate(b):
                    if y!=self.base.zero:d[i+j]=self.base.add(d.get(i+j,self.base.zero),self.base.mul(x,y))
        return self.reduce([d.get(i,self.base.zero) for i in range(max(d,default=-1)+1)])

t=start();out={'passed':False,'checks':[],'failures':[]}
def need(ok,label):
    if not ok:raise ValueError(label)
    out['checks'].append(label)
try:
    quo=read(U/'quotient-254/quotient.json');dual=read(U/'dual-263/dual.json')
    point=read(U/'certificate.json');fiber=read(U/'incidence-269/fiber.json')
    units=read(U/'incidence-269/units-and-y.json');maps=read(U/'incidence-269/pullbacks.json')
    D=Sparse(Rat(),tuple(map(Q,quo['h'])))
    def d(v):return D.trim(tuple(map(Q,v)))
    k=tuple(d(v) for v in dual['k']);L=Sparse(D,k)
    def l(v):return L.trim(tuple(d(w) for w in v))
    cp=L.reduce((d(quo['target_b']),d(quo['target_a']),D.zero,D.one))
    def pm(a,b):
        z=[D.zero]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):z[i+j]=D.add(z[i+j],D.mul(x,y))
        return z
    q=tuple(d(v) for v in quo['q']);N=tuple(d(v) for v in quo['x_numerator']);q2=pm(q,q)
    F=tuple(L.trim((N[i],D.neg(q2[i]) if i<len(q2) else D.zero)) for i in range(len(N)))
    need(d(fiber['h'])==D.mod and tuple(d(v) for v in fiber['k'])==k and l(fiber['cprime'])==cp,'all_B_inputs')
    need(F==tuple(l(v) for v in fiber['F']) and len(F)==8 and F[-1]==L.one,'entire_reconstructed_monic_F')
    E=Sparse(L,F);B=Sparse(L,(L.neg(cp),L.zero,L.one))
    def e(v):return E.trim(tuple(l(w) for w in v))
    yf=e(units['y_V_factor']);X=(L.zero,L.one)
    def constD(v):return (v,) if v!=D.zero else ()
    def ec(v):return E.reduce(tuple(constD(d([a])) for a in v))
    need(E.mul((cp,),E.mul(yf,yf))==ec([46224,-3024,0,1]),'full_y_factor_source_relation')
    def bflat(a):
        return tuple(a[eps][i][j] if eps<len(a) and i<len(a[eps]) and j<len(a[eps][i]) else Q(0) for eps in range(2) for i in range(3) for j in range(8))
    def iflat(a,b):
        return tuple((a if eps==0 else b)[r][i][j] if r<len(a if eps==0 else b) and i<len((a if eps==0 else b)[r]) and j<len((a if eps==0 else b)[r][i]) else Q(0) for r in range(7) for eps in range(2) for i in range(3) for j in range(8))
    def scal(a,n):return E.trim([L.trim([D.trim([x*n for x in v]) for v in w]) for w in a])
    origx=iflat(scal(E.add(X,E.neg(ec([12]))),Q(1,36)),E.zero)
    origy=iflat(ec([Q(-1,2)]),scal(yf,Q(1,216)))
    need(origx==tuple(map(Q,maps['point_original_x'])) and origy==tuple(map(Q,maps['point_original_y'])),'both_original_coordinate_transports')
    p=E.one;std=[];odd=[]
    for i in range(24):
        std.append(iflat(p,E.zero));odd.append(iflat(E.zero,E.mul(p,yf)));p=E.mul(p,X)
    std+=odd
    need(std==[tuple(map(Q,v)) for v in maps['point_standard_columns']],'entire_48_column_standard_point_basis')
    def transport(cols,mat):
        return [tuple(sum((Q(mat[i][j])*cols[i][n] for i in range(48) if Q(mat[i][j]) and cols[i][n]),Q(0)) for n in range(336)) for j in range(48)]
    power=transport(std,point['matrix'])
    need(power==[tuple(map(Q,v)) for v in maps['point_power_columns']] and transport(power,point['inverse'])==std,'both_complete_48_column_transports')
    save('construction-transports.json',{'point_standard_columns':std,'point_power_columns':power,'point_original_x':origx,'point_original_y':origy})
    out['location']='source unit construction'
    P=Sparse(Rat(),tuple(map(Q,point['f'])))
    pc=P.reduce(tuple(map(Q,[46224,-3024,0,1])))
    az=(P.zero,P.zero);ao=(P.one,P.zero)
    def am(u,v):return (P.add(P.mul(u[0],v[0]),P.mul(pc,P.mul(u[1],v[1]))),P.add(P.mul(u[0],v[1]),P.mul(u[1],v[0])))
    def apow(u,n):
        r=ao
        for _ in range(n):r=am(r,u)
        return r
    def pdiv(a,b):
        a=list(P.trim(a));b=P.trim(b);need(bool(b),'nonzero_Euclidean_divisor')
        quot=[Q(0)]*max(0,len(a)-len(b)+1)
        while len(a)>=len(b):
            j=len(a)-len(b);z=a[-1]/b[-1];quot[j]=z
            for i,c in enumerate(b):a[i+j]-=z*c
            a=list(P.trim(a))
        return P.trim(quot),P.trim(a)
    def pmulfree(a,b):
        v=[Q(0)]*max(0,len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b):v[i+j]+=x*y
        return P.trim(v)
    def pinv(a):
        r0,r1=P.mod,a;s0,s1=(),(Q(1),)
        while r1:
            q,r=pdiv(r0,r1);r0,r1=r1,r;s0,s1=s1,P.add(s0,P.neg(pmulfree(q,s1)))
        need(len(r0)==1 and r0[0]!=0,'unit_Euclidean_gcd')
        result=P.reduce(tuple(x/r0[0] for x in s0))
        need(P.mul(a,result)==P.one,'whole_source_denominator_inverse')
        return result
    def ainverse(u):
        den=P.add(P.mul(u[0],u[0]),P.neg(P.mul(pc,P.mul(u[1],u[1]))));di=pinv(den)
        return (P.mul(u[0],di),P.neg(P.mul(u[1],di)))
    def af(u):return tuple(u[e][i] if i<len(u[e]) else Q(0) for e in range(2) for i in range(24))
    def topower(v):return tuple(sum((Q(point['inverse'][i][j])*v[j] for j in range(48) if v[j] and Q(point['inverse'][i][j])),Q(0)) for i in range(48))
    def frompower(v):return tuple(sum((Q(point['matrix'][i][j])*v[j] for j in range(48) if v[j] and Q(point['matrix'][i][j])),Q(0)) for i in range(48))
    a=((Q(0),Q(1)),P.one);b=(P.one,P.one);ai=ainverse(a);bi=ainverse(b)
    aprime=am(a,apow(b,7));api=am(ai,apow(bi,7))
    elements={'a':a,'b':b,'a_prime':aprime,'scalar2':((Q(2),),P.zero)}
    inverses={'a':ai,'b':bi,'a_prime':api,'scalar2':((Q(1,2),),P.zero)}
    inputs={}
    for label,u in elements.items():
        need(am(u,inverses[label])==ao,'source_unit_'+label)
        v,iv=af(u),af(inverses[label]);tv,tiv=topower(v),topower(iv)
        need(frompower(tv)==v and frompower(tiv)==iv,'input_power_roundtrips_'+label)
        inputs[label]={'standard':v,'inverse_standard':iv,'power':tv,'inverse_power':tiv}
    need(am(a,apow(b,7))==aprime,'source_representative_change')
    save('supplied-inputs.json',{'elements':inputs,'source_basis':'X^i, X^i Y; 0<=i<24','power_basis':'Y^j; 0<=j<48'})
    prejections=[]
    def preject(case,data,fn,expected):
        save('producer-mutant-'+case+'.json',data)
        try:fn(data)
        except ValueError as exc:
            need(str(exc)==expected,'producer_intended_'+case)
            prejections.append({'case':case,'rejected':True,'condition':str(exc),'full_malformed_replay':False,'scope':'named full-data condition only'})
        else:raise ValueError('producer accepted mutant '+case)
    def input_test(rows):
        for label,row in rows.items():
            if any(len(row[k])!=48 for k in ('standard','inverse_standard','power','inverse_power')):raise ValueError('full_source_48_shape')
            v=tuple(map(Q,row['standard']));iv=tuple(map(Q,row['inverse_standard']))
            u=(P.trim(v[:24]),P.trim(v[24:]));ui=(P.trim(iv[:24]),P.trim(iv[24:]))
            if u==az:raise ValueError('zero_is_not_a_supplied_unit')
            if am(u,ui)!=ao:raise ValueError('full_source_unit_inverse_product')
    input_test(inputs)
    bad=copy.deepcopy(inputs);bad['a']['inverse_standard']=list(bad['a']['inverse_standard']);bad['a']['inverse_standard'][0]+=1
    preject('inverse-one-coefficient',bad,input_test,'full_source_unit_inverse_product')
    bad=copy.deepcopy(inputs);bad['a']['standard']=[Q(0)]*48
    preject('zero-supplied-unit',bad,input_test,'zero_is_not_a_supplied_unit')
    bad=copy.deepcopy(inputs);bad['a']['power']=bad['a']['power'][:-1]
    preject('missing-source-coordinate',bad,input_test,'full_source_48_shape')
    save('producer-input-rejections.json',prejections)
    print('All supplied source units and representative identity saved.',flush=True)
    def pairmul(u,v):return (E.add(E.mul(u[0],v[0]),E.mul((cp,),E.mul(u[1],v[1]))),E.add(E.mul(u[0],v[1]),E.mul(u[1],v[0])))
    def ipow(u,n):
        r=(E.one,E.zero)
        for _ in range(n):r=pairmul(r,u)
        return r
    def pull(u):
        def evalp(v):
            r=E.zero
            for c in reversed(v):r=E.add(E.mul(r,X),ec([c]))
            return r
        return (evalp(u[0]),E.mul(evalp(u[1]),yf))
    pulls={};ipulls={}
    for label,u in elements.items():
        pulls[label]=pull(u);ipulls[label]=pull(inverses[label])
        need(pairmul(pulls[label],ipulls[label])==(E.one,E.zero),'full_incidence_unit_'+label)
    need(pairmul(pulls['a'],ipow(pulls['b'],7))==pulls['a_prime'],'incidence_representative_change')
    save('input-pullbacks.json',{label:{'element':iflat(*pulls[label]),'inverse':iflat(*ipulls[label])} for label in elements})
    out['location']='full matrices'
    matrices={}
    for name,(a,b) in list(pulls.items())+[('zero',(E.zero,E.zero))]:
        columns=[];aa=a;bb=b
        for col in range(7):
            columns.append([B.trim((aa[row] if row<len(aa) else L.zero,bb[row] if row<len(bb) else L.zero)) for row in range(7)])
            if col<6:aa=E.mul(aa,X);bb=E.mul(bb,X)
        matrices[name]=[[columns[col][row] for col in range(7)] for row in range(7)]
    full={name:[[bflat(v) for v in row] for row in mat] for name,mat in matrices.items()}
    save('supplied-matrices.json',{'matrices':full,'rational_slots':11760,'F':F,'y_V_factor':yf})
    def matrix_test(data):
        if data!=full:raise ValueError('all_matrix_coefficient_comparison')
    bad=copy.deepcopy(full);bad['a'][0][0]=list(bad['a'][0][0]);bad['a'][0][0][24]+=1
    preject('odd-V-matrix-coefficient',bad,matrix_test,'all_matrix_coefficient_comparison')
    print('Full five matrices saved: 11760 rational slots.',flush=True)
    norms={};unfinished={}
    def determinant(mat,label):
        records={};unfinished[label]=records
        @lru_cache(None)
        def det(cols):
            if not cols:return B.one
            row=7-len(cols);s=B.zero
            for j,col in enumerate(cols):
                if mat[row][col]!=B.zero:
                    term=B.mul(mat[row][col],det(cols[:j]+cols[j+1:]))
                    s=B.add(s,term if j%2==0 else B.neg(term))
            records[','.join(map(str,cols))]=bflat(s)
            return s
        value=det(tuple(range(7)))
        save('laplace-'+label+'.json',{'norm':bflat(value),'ordered_remaining_column_minors':records,'row_rule':'7 - len(columns)','empty_minor':bflat(B.one)})
        del unfinished[label]
        return value
    for name in ('zero','scalar2','a','b','a_prime'):
        out['location']='Laplace '+name;print(out['location'],flush=True)
        norms[name]=determinant(matrices[name],name)
        save('norm-'+name+'.json',{'norm':bflat(norms[name])})
    need(norms['zero']==B.zero and norms['scalar2']==B.trim((L.trim((d([128]),)),)),'scalar_zero_norm_controls')
    def bpow(u,n):
        r=B.one
        for _ in range(n):r=B.mul(r,u)
        return r
    need(B.mul(norms['a'],bpow(norms['b'],7))==norms['a_prime'],'full_norm_representative_change')
    beta=B.trim((L.trim((d([2]),)),));betai=B.trim((L.trim((d([Q(1,2)]),)),))
    need(B.mul(beta,betai)==B.one and bpow(beta,7)==norms['scalar2'],'exact_scalar_root_witness')
    save('supplied-norms.json',{'norms':{k:bflat(v) for k,v in norms.items()},'representative_change':{'lhs':bflat(B.mul(norms['a'],bpow(norms['b'],7))),'rhs':bflat(norms['a_prime'])},'positive_scalar_control':{'beta':bflat(beta),'beta_inv':bflat(betai),'beta7':bflat(bpow(beta,7))},'mixed_root_claim':False})
    nflat={k:bflat(v) for k,v in norms.items()}
    def norm_test(data):
        if data!=nflat:raise ValueError('all_norm_coefficient_comparison')
    bad=copy.deepcopy(nflat);bad['a']=list(bad['a']);bad['a'][0]+=1
    preject('norm-one-coefficient',bad,norm_test,'all_norm_coefficient_comparison')
    save('producer-rejections.json',prejections)
    out.update(passed=True,rational_matrix_slots=11760,norm_slots=240,element_count=5,rejection_count=len(prejections))
except Exception as exc:
    out['failures'].append(type(exc).__name__+': '+str(exc))
    if 'unfinished' in globals() and unfinished:save('unfinished-minors.json',{'location':out.get('location'),'partial_minors':unfinished,'complete_norm_claim':False})
finally:finish('construction',out,t)
sys.exit(0 if out['passed'] else 1)
