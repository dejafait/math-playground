"""Independent complete quotient-fiber replay; no producer arithmetic imports."""
from fractions import Fraction as Q
from pathlib import Path
import json,hashlib,time,signal,sys,copy
R=Path(__file__).resolve().parent;U=R.parent
start=time.monotonic();out={'passed':False,'checks':[],'failures':[],'required_seconds':180}
def enc(v):
    if isinstance(v,Q):return str(v)
    if isinstance(v,(tuple,list)):return [enc(x) for x in v]
    if isinstance(v,dict):return {str(k):enc(x) for k,x in v.items()}
    return v
def save(n,v):
    s=json.dumps(enc(v),separators=(',',':'))+'\n'
    assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())<=134217728,'combined 128-MiB cap'
    p=R/n;p.parent.mkdir(parents=True,exist_ok=True)
    with p.open('x') as f:f.write(s)
def check(v,n):
    if not v:raise ValueError(n)
    out['checks'].append(n)
def alarm(*_):raise TimeoutError('180-second replay cap')
signal.signal(signal.SIGALRM,alarm);signal.alarm(180)
# Each quotient below uses a separate independently implemented sparse convolution.
class Rat:
    zero=Q(0);one=Q(1)
    def add(self,a,b):return a+b
    def neg(self,a):return -a
    def mul(self,a,b):return a*b
class Monic:
    zero=()
    def __init__(self,base,mod):
        self.base=base;self.mod=self.clean(mod);self.n=len(self.mod)-1
        if self.mod[-1]!=base.one:raise ValueError('nonmonic modulus')
        self.one=(base.one,)
    def clean(self,a):
        a=list(a)
        while a and a[-1]==self.base.zero:a.pop()
        return tuple(a)
    def add(self,a,b):
        return self.clean([self.base.add(a[i] if i<len(a) else self.base.zero,b[i] if i<len(b) else self.base.zero) for i in range(max(len(a),len(b)))])
    def neg(self,a):return self.clean([self.base.neg(x) for x in a])
    def reduce(self,a):
        a=list(a)
        for i in range(len(a)-1,self.n-1,-1):
            if a[i]!=self.base.zero:
                v=a[i]
                for j,c in enumerate(self.mod[:-1]):
                    if c!=self.base.zero:a[i-self.n+j]=self.base.add(a[i-self.n+j],self.base.neg(self.base.mul(v,c)))
        return self.clean(a[:self.n])
    def mul(self,a,b):
        d={}
        for i,c in enumerate(a):
            if c!=self.base.zero:
                for j,e in enumerate(b):
                    if e!=self.base.zero:d[i+j]=self.base.add(d.get(i+j,self.base.zero),self.base.mul(c,e))
        return self.reduce([d.get(i,self.base.zero) for i in range(max(d,default=-1)+1)])
    def power(self,a,n):
        r=self.one
        while n:
            if n%2:r=self.mul(r,a)
            n//=2
            if n:a=self.mul(a,a)
        return r
    def eval(self,coeff,x):
        r=self.zero
        for c in reversed(coeff):r=self.add(self.mul(r,x),(c,) if c!=self.base.zero else ())
        return r
try:
    point=json.loads((U/'certificate.json').read_text());old=json.loads((U/'quotient-254/quotient.json').read_text());dual=json.loads((U/'dual-263/dual.json').read_text())
    fiber=json.loads((R/'fiber.json').read_text());qunit=json.loads((R/'q-unit.json').read_text());units=json.loads((R/'units-and-y.json').read_text());maps=json.loads((R/'pullbacks.json').read_text())
    paths={'point':'certificate.json','direction':'compressed-249/direction.json','quotient':'quotient-254/quotient.json','dual':'dual-263/dual.json'}
    check(all(hashlib.sha256((U/p).read_bytes()).hexdigest()==fiber['input_hashes'][n] for n,p in paths.items()),'all_input_hashes')
    rat=Rat();D=Monic(rat,tuple(map(Q,old['h'])))
    def d(a):return D.clean(tuple(map(Q,a)))
    def dscale(a,n):return D.clean([v*n for v in a])
    def poly(p):return tuple(d(a) for a in p)
    q=poly(old['q']);k=poly(dual['k']);N=poly(old['x_numerator']);M=poly(old['y_multiplier_numerator'])
    L=Monic(D,k);T=(D.zero,D.one)
    cp=L.reduce((d(old['target_b']),d(old['target_a']),D.zero,D.one))
    cpI=L.clean(poly(dual['curve_inverse']))
    check(L.mul(cp,cpI)==L.one,'entire_B_cubic_unit')
    def dp_mul(a,b):
        v=[D.zero]*(len(a)+len(b)-1)
        for i,c in enumerate(a):
            for j,e in enumerate(b):v[i+j]=D.add(v[i+j],D.mul(c,e))
        return v
    qq=dp_mul(q,q)
    F=tuple(L.clean((N[i] if i<len(N) else D.zero,D.neg(qq[i]) if i<len(qq) else D.zero)) for i in range(max(len(N),len(qq))))
    def readL(v):return L.clean(poly(v))
    check(d(fiber['h'])==D.mod and poly(fiber['k'])==k and readL(fiber['cprime'])==cp,'all_tower_input_coefficients')
    check(tuple(readL(v) for v in fiber['F'])==F and len(F)==8 and F[-1]==L.one,'entire_specialized_fiber_monic_coefficients')
    E=Monic(L,F);X=(L.zero,L.one)
    def lift(a):return E.reduce(tuple((v,) if v!=D.zero else () for v in a))
    def constL(v):return (v,) if v!=L.zero else ()
    def readE(v):return E.clean(tuple(readL(w) for w in v))
    def scale(a,n):return E.clean([L.clean([dscale(c,n) for c in w]) for w in a])
    def sub(a,b):return E.add(a,E.neg(b))
    eq=lift(q);eM=lift(M);eN=lift(N);ec=lift((d([46224]),d([-3024]),D.zero,D.one))
    # Reconstruct the denominator inverse using only audited full-kernel units.
    K=Monic(D,q);I=K.clean(poly(old['qprime_inverse_mod_q']));J=K.clean(poly(old['c_inverse_mod_q']))
    H=tuple(dscale(v,Q(1,4)) for v in K.mul(J,K.mul(I,I)))
    nh=dp_mul(N,H);nh[0]=D.add(nh[0],D.neg(D.one))
    W=[D.zero]*max(1,len(nh)-len(q)+1)
    rem=list(nh)
    for i in range(len(rem)-1,len(q)-2,-1):
        v=rem[i];W[i-len(q)+1]=v
        for j,c in enumerate(q):rem[i-len(q)+1+j]=D.add(rem[i-len(q)+1+j],D.neg(D.mul(v,c)))
    check(all(v==D.zero for v in rem),'independent_exact_NH_minus_one_division')
    qi=sub(E.mul(constL(T),E.mul(eq,lift(H))),lift(W))
    def unit_test(data):
        check(E.mul(eq,readE(data['q_inverse']))==E.one,'full_q_inverse_product')
    unit_test(qunit)
    check(poly(qunit['H'])==H and K.clean(poly(qunit['W']))==K.clean(W) and readE(qunit['q_inverse'])==qi,'all_q_witness_coefficients')
    # W is a free polynomial, so compare the unreduced full W as well.
    def trimD(a):
        a=list(a)
        while a and a[-1]==D.zero:a.pop()
        return tuple(a)
    check(trimD(poly(qunit['W']))==trimD(W),'entire_free_W_not_just_residue')
    qi3=E.power(qi,3)
    mi=E.mul(E.mul(ec,eM),E.mul(constL(cpI),E.mul(qi3,qi3)))
    di=E.mul(eq,mi);yf=E.mul(E.power(eq,3),mi)
    check(readE(units['M_inverse'])==mi and readE(units['derivative_inverse'])==di and readE(units['y_V_factor'])==yf and readE(units['q_inverse'])==qi,'every_saved_unit_and_y_coefficient')
    derivative=E.reduce(tuple(L.clean([dscale(v,i) for v in F[i]]) for i in range(1,8)))
    check(E.mul(eM,mi)==E.one,'full_M_inverse_product')
    check(E.mul(derivative,di)==E.one,'full_derivative_inverse_product')
    check(E.mul(constL(cp),E.mul(yf,yf))==ec,'source_curve_every_component_both_signs')
    check(E.mul(yf,eM)==E.power(eq,3),'full_y_quotient_equation')
    check(sub(eN,E.mul(constL(T),E.power(eq,2)))==E.zero,'full_x_quotient_equation')
    check(lift(tuple(d([v]) for v in point['f']))==E.zero,'entire_L067_source_division_polynomial')
    print('all fiber equations and units replayed',flush=True)
    # Full 336-coordinate flattening, inverse and the even/odd V multiplication.
    def flatten(a,b):
        return tuple((a if e==0 else b)[r][i][j] if r<len(a if e==0 else b) and i<len((a if e==0 else b)[r]) and j<len((a if e==0 else b)[r][i]) else Q(0) for r in range(7) for e in range(2) for i in range(3) for j in range(8))
    def unflatten(v):
        return tuple(E.clean([L.clean([D.clean([v[r*48+e*24+i*8+j] for j in range(8)]) for i in range(3)]) for r in range(7)]) for e in range(2))
    check(fiber['rank_B']==7 and fiber['dimension_Q']==336 and fiber['B_basis']==['1','X','X^2','X^3','X^4','X^5','X^6'],'complete_monic_basis_sizes')
    for n in range(336):
        v=tuple(Q(i==n) for i in range(336));check(flatten(*unflatten(v))==v,'basis_transport_'+str(n))
    def pairmul(a,b):
        return (E.add(E.mul(a[0],b[0]),E.mul(constL(cp),E.mul(a[1],b[1]))),E.add(E.mul(a[0],b[1]),E.mul(a[1],b[0])))
    xx=(X,E.zero);yy=(E.zero,yf)
    check(pairmul(yy,yy)==(ec,E.zero),'two_coordinate_pair_ring_source_relation')
    pows=[E.one]
    for _ in range(23):pows.append(E.mul(pows[-1],X))
    std=[flatten(p,E.zero) for p in pows]+[flatten(E.zero,E.mul(p,yf)) for p in pows]
    def cols(v):return [tuple(map(Q,c)) for c in v]
    check(cols(maps['point_standard_columns'])==std,'all_48_standard_source_columns_336_coordinates')
    mat=[[Q(v) for v in row] for row in point['matrix']];inv=[[Q(v) for v in row] for row in point['inverse']]
    def transport(c,m):
        return [tuple(sum((m[i][j]*c[i][n] for i in range(48) if m[i][j] and c[i][n]),Q(0)) for n in range(336)) for j in range(48)]
    power=transport(std,mat)
    check(cols(maps['point_power_columns'])==power and transport(power,inv)==std,'both_full_point_basis_transports')
    line=[]
    for n in range(48):line.append(tuple(Q(i==n) for i in range(336)))
    def line_test(data):check(cols(data['line_columns'])==line,'all_48_line_columns_including_both_sign_components')
    line_test(maps)
    origx=flatten(scale(sub(X,lift((d([12]),))),Q(1,36)),E.zero)
    origy=flatten(lift((d([Q(-1,2)]),)),scale(yf,Q(1,216)))
    def point_test(data):check(tuple(map(Q,data['point_original_x']))==origx and tuple(map(Q,data['point_original_y']))==origy,'both_original_point_coordinate_maps')
    point_test(maps)
    check(maps['full_ranks']=={'point':48,'line':48} and std[0]==line[0] and any(std[0]),'unital_field_source_and_full_constant_basis_ranks')
    # Source-generator equations give algebra homomorphisms. Check the entire
    # separating Y power basis also by pair-ring multiplication, independently
    # of transporting its saved matrix.
    current=(E.one,E.zero)
    for j in range(48):
        check(flatten(*current)==power[j],'power_basis_multiplication_'+str(j))
        if j<47:current=pairmul(current,yy)
    print('all maps and full bases replayed',flush=True)
    save('complete-replay-evidence.json',{'F':F,'q_inverse':qi,'M_inverse':mi,'derivative_inverse':di,'y_V_factor':yf,'point_standard_columns':std,'point_power_columns':power,'line_columns':line,'point_original_x':origx,'point_original_y':origy,'all_coefficient_equalities':True,'basis_transport_count':336,'source_power_products':48,'residuals':{'q_unit':E.add(E.mul(eq,qi),E.neg(E.one)),'M_unit':E.add(E.mul(eM,mi),E.neg(E.one)),'derivative_unit':E.add(E.mul(derivative,di),E.neg(E.one)),'curve':E.add(E.mul(constL(cp),E.mul(yf,yf)),E.neg(ec)),'x_map':sub(eN,E.mul(constL(T),E.power(eq,2))),'y_map':sub(E.mul(yf,eM),E.power(eq,3))}})
    rejections=[]
    def reject(name,data,fn,expected,scope):
        save('rejections/'+name+'.json',data)
        before=len(out['checks'])
        try:fn(data)
        except ValueError as e:
            check(str(e)==expected,'intended_rejection_'+name)
            rejections.append({'case':name,'rejected':True,'failure':str(e),'scope':scope,'full_malformed_replay':False,'passed_prefix':out['checks'][before:-1]})
        else:raise ValueError('accepted altered '+name)
    bad=copy.deepcopy(qunit);bad['q_inverse'][0][0][0]=str(Q(bad['q_inverse'][0][0][0])+1)
    reject('corrupt-q-unit',bad,unit_test,'full_q_inverse_product','full-domain denominator unit condition only')
    bad=copy.deepcopy(maps);bad['point_original_y'][0]=str(Q(bad['point_original_y'][0])+1)
    reject('wrong-point-map',bad,point_test,'both_original_point_coordinate_maps','complete two-coordinate original-model map comparison only')
    bad=copy.deepcopy(maps);bad['line_columns']=bad['line_columns'][:24]
    reject('missing-sign-columns',bad,line_test,'all_48_line_columns_including_both_sign_components','complete line pullback columns; removes the entire odd-V block, not a geometric sign selector')
    save('rejections.json',rejections)
    original=json.loads((R/'originals.json').read_text())
    changed=[p for p,h in original.items() if not (U/p).is_file() or hashlib.sha256((U/p).read_bytes()).hexdigest()!=h]
    check(not changed,'all_inventoried_original_bytes_preserved')
    save('preservation.json',{'count':len(original),'changed_or_missing':changed,'passed':not changed})
    out.update(passed=True,phase='complete independent replay',dimension_Q=336,required_dimension_Q=336,rank_B=7,required_rank_B=7,rejection_count=3,preserved_files=len(original))
except Exception as e:out['failures']=[type(e).__name__+': '+str(e)]
finally:
    signal.alarm(0);out['seconds']=time.monotonic()-start;save('replay-report.json',out)
print(json.dumps({k:v for k,v in out.items() if k!='checks'}));sys.exit(0 if out['passed'] else 1)
