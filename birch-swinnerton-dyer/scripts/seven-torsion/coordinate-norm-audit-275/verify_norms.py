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
    produced=read(R/'coordinate-matrices.json');savednorm=read(R/'coordinate-norms.json')
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
    matrices={}
    for name,a,b in [('X',X,E.zero),('Y',E.zero,yf)]:
        cols=[]
        for j in range(7):
            cols.append([(a[i],b[i]) for i in range(7)])
            if j<6:a,b=E.shift(a),E.shift(b)
        matrices[name]=[[cols[j][i] for j in range(7)] for i in range(7)]
    flat={name:[[bf(v) for v in row] for row in mat] for name,mat in matrices.items()}
    def shape_test(data):
        if set(data)!=set(('X','Y')) or any(len(data[k])!=7 or any(len(row)!=7 or any(len(v)!=48 for v in row) for row in data[k]) for k in data):raise ValueError('full_48_coefficient_basis_shape')
    def matrix_test(data):
        shape_test(data)
        if {k:[[tuple(map(Q,v)) for v in row] for row in mat] for k,mat in data.items()}!=flat:raise ValueError('full_matrix_coefficient_comparison')
    matrix_test(produced['matrices']);need(produced['rational_slots']==4704,'all_4704_matrix_slots')
    save('independent-matrices.json',{'matrices':flat,'rational_slots':4704,'all_entries_equal':True})
    print('Independent full tower, all transports and 4704 matrix slots pass.',flush=True)
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
    for name in ('X','Y'):
        norms[name]=faddeev(matrices[name],name)
        lap=read(R/('laplace-'+name+'.json'))
        need(tuple(map(Q,lap['norm']))==bf(norms[name])==tuple(map(Q,savednorm['norms'][name])),'full_48_coefficient_determinant_'+name)
    controls={}
    for v in (0,2):
        entry=(L.vector((d([v]),)),L.zero)
        mat=[[entry if i==j else bz for j in range(7)] for i in range(7)]
        norm=faddeev(mat,'scalar-'+str(v));expected=(L.vector((d([v**7]),)),L.zero)
        need(norm==expected,'independent_scalar_norm_'+str(v))
        old=savednorm['scalar_controls'][str(v)]
        need(mf(mat)==[[tuple(map(Q,x)) for x in row] for row in old['matrix']] and bf(norm)==tuple(map(Q,old['norm'])),'full_saved_scalar_control_'+str(v))
        controls[str(v)]=bf(norm)
    def norm_test(data):
        if set(data)!=set(norms) or any(len(data[k])!=48 or tuple(map(Q,data[k]))!=bf(norms[k]) for k in data):raise ValueError('full_determinant_coefficient_comparison')
    norm_test(savednorm['norms'])
    rejections=[]
    def reject(case,data,fn,expected):
        save('mutant-'+case+'.json',data)
        try:fn(data)
        except ValueError as exc:
            need(str(exc)==expected,'intended_'+case)
            rejections.append({'case':case,'rejected':True,'condition':str(exc),'full_malformed_replay':False,'scope':'named full-data condition only'})
        else:raise ValueError('accepted mutant '+case)
    bad=copy.deepcopy(produced['matrices']);bad['X'][0][0][24]=str(Q(bad['X'][0][0][24])+1)
    reject('matrix-one-coefficient',bad,matrix_test,'full_matrix_coefficient_comparison')
    bad=copy.deepcopy(savednorm['norms']);bad['Y'][0]=str(Q(bad['Y'][0])+1)
    reject('norm-one-coefficient',bad,norm_test,'full_determinant_coefficient_comparison')
    bad={k:[[v[:24] for v in row] for row in mat] for k,mat in produced['matrices'].items()}
    reject('missing-odd-V-block',bad,shape_test,'full_48_coefficient_basis_shape')
    save('rejections.json',rejections)
    save('verification-summary.json',{'norms':{k:bf(v) for k,v in norms.items()},'all_4704_matrix_coefficients_equal':True,'both_48_coefficient_norms_equal':True,'all_full_transports_equal':True,'all_terminal_matrices_zero':True,'scalar_controls':controls,'rejections':rejections})
    out.update(passed=True,rational_matrix_slots=4704,norm_slots=96,coordinate_count=2,rejection_count=3)
except Exception as exc:out['failures'].append(type(exc).__name__+': '+str(exc))
finally:finish('verification',out,t)
sys.exit(0 if out['passed'] else 1)
