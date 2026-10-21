"""Distinct fixed-length rational tower check; no notebook arithmetic imports.

Multiplication uses Horner shifts in each quotient (not sparse convolution).
All equality tests compare entire dense normal forms, including both V parts.
"""
from fractions import Fraction as Q
import json

class Rational:
    zero=Q(0); one=Q(1)
    def add(self,a,b): return a+b
    def neg(self,a): return -a
    def mul(self,a,b): return a*b

class Dense:
    def __init__(self,base,mod):
        self.base=base; self.n=len(mod)-1
        assert mod[-1]==base.one
        self.mod=tuple(mod[:-1]); self.zero=(base.zero,)*self.n
        self.one=(base.one,)+(base.zero,)*(self.n-1)
    def vector(self,a):
        assert len(a)<=self.n
        return tuple(a)+(self.base.zero,)*(self.n-len(a))
    def add(self,a,b): return tuple(self.base.add(x,y) for x,y in zip(a,b))
    def neg(self,a): return tuple(self.base.neg(x) for x in a)
    def shift(self,a):
        r=[self.base.zero]+list(a[:-1]); top=a[-1]
        if top!=self.base.zero:
            for i,c in enumerate(self.mod):
                if c!=self.base.zero:
                    r[i]=self.base.add(r[i],self.base.neg(self.base.mul(top,c)))
        return tuple(r)
    def mul(self,a,b):
        if a==self.zero or b==self.zero: return self.zero
        if a==self.one: return b
        if b==self.one: return a
        r=self.zero
        for c in reversed(b):
            r=self.shift(r)
            if c!=self.base.zero:
                r=self.add(r,tuple(self.base.mul(c,x) if x!=self.base.zero else self.base.zero for x in a))
        return r
    def reduce(self,coeff):
        r=self.zero
        for c in reversed(coeff):
            r=self.shift(r)
            r=(self.base.add(r[0],c),)+r[1:]
        return r

def run(root,save):
    upstream=root.parent
    def read(p): return json.loads(p.read_text())
    src=read(upstream/'certificate.json')
    quo=read(upstream/'quotient-254/quotient.json')
    dual=read(upstream/'dual-263/dual.json')
    fiber=read(root/'fiber.json'); unit=read(root/'units-and-y.json')
    qunit=read(root/'q-unit.json'); maps=read(root/'pullbacks.json')
    checks=[]; residuals={}
    def require(ok,label):
        if not ok: raise ValueError('dense:'+label)
        checks.append(label)
    D=Dense(Rational(),tuple(map(Q,quo['h'])))
    def d(a): return D.vector(tuple(map(Q,a)))
    L=Dense(D,tuple(d(a) for a in dual['k']))
    def l(a): return L.vector(tuple(d(v) for v in a))
    def scalar(a): return L.vector((a,))
    T=L.vector((D.zero,D.one))
    cp=L.reduce((d(quo['target_b']),d(quo['target_a']),D.zero,D.one))
    require(L.mul(cp,l(dual['curve_inverse']))==L.one,'entire_cprime_unit')
    # Independent free D-polynomial arithmetic for F and the W identity.
    def polymul(a,b):
        out=[D.zero]*(len(a)+len(b)-1)
        for i,x in enumerate(a):
            for j,y in enumerate(b): out[i+j]=D.add(out[i+j],D.mul(x,y))
        return out
    q=[d(a) for a in quo['q']]; N=[d(a) for a in quo['x_numerator']]
    M=[d(a) for a in quo['y_multiplier_numerator']]
    q2=polymul(q,q)
    F=[L.vector((N[i],D.neg(q2[i]) if i<len(q2) else D.zero)) for i in range(len(N))]
    require(tuple(F)==tuple(l(v) for v in fiber['F']) and len(F)==8 and F[-1]==L.one,'whole_monic_F')
    E=Dense(L,F)
    def e(a): return E.vector(tuple(l(v) for v in a))
    def lift(a): return E.reduce(tuple(scalar(v) for v in a))
    def constant(v): return E.vector((v,))
    def scale(a,n): return tuple(tuple(tuple(n*x for x in v) for v in w) for w in a)
    def sub(a,b): return E.add(a,E.neg(b))
    X=E.vector((L.zero,L.one)); eq=lift(q); eN=lift(N); eM=lift(M)
    c=lift((d([46224]),d([-3024]),D.zero,D.one))
    H=[d(v) for v in qunit['H']]; W=[d(v) for v in qunit['W']]
    nh=polymul(N,H); qw=polymul(q,W)
    nh[0]=D.add(nh[0],D.neg(D.one))
    size=max(len(nh),len(qw))
    free=tuple(D.add(nh[i] if i<len(nh) else D.zero,D.neg(qw[i] if i<len(qw) else D.zero)) for i in range(size))
    require(all(v==D.zero for v in free),'free_NH_minus_one_equals_qW')
    residuals['free_W']=free
    qi=e(qunit['q_inverse']); mi=e(unit['M_inverse']); di=e(unit['derivative_inverse']); yf=e(unit['y_V_factor'])
    require(qi==e(unit['q_inverse']),'both_saved_q_inverses')
    qsq=E.mul(eq,eq); qcube=E.mul(qsq,eq)
    deriv=E.reduce(tuple(tuple(tuple(Q(i)*x for x in v) for v in F[i]) for i in range(1,8)))
    def zero(label,a):
        residuals[label]=a
        require(a==E.zero,label)
    zero('q_unit',sub(E.mul(eq,qi),E.one))
    zero('M_unit',sub(E.mul(eM,mi),E.one))
    zero('derivative_unit',sub(E.mul(deriv,di),E.one))
    zero('source_curve',sub(E.mul(constant(cp),E.mul(yf,yf)),c))
    zero('x_projection',sub(eN,E.mul(constant(T),qsq)))
    zero('y_projection',sub(E.mul(yf,eM),qcube))
    zero('source_division',lift(tuple(d([v]) for v in src['f'])))
    # Recheck the specialized differential identity, without dividing by T.
    zero('Fprime_q_equals_M',sub(E.mul(deriv,eq),eM))
    print('distinct dense: all units and fiber equations',flush=True)
    def flat(a,b):
        return tuple((a if eps==0 else b)[r][i][j] for r in range(7) for eps in range(2) for i in range(3) for j in range(8))
    def unflat(v):
        require(len(v)==336,'coordinate_length_336')
        return tuple(tuple(tuple(tuple(v[r*48+eps*24+i*8+j] for j in range(8)) for i in range(3)) for r in range(7)) for eps in range(2))
    for n in range(336):
        v=tuple(Q(n==i) for i in range(336))
        require(flat(*unflat(v))==v,'dense_basis_roundtrip_'+str(n))
    p=E.one; std=[]; odd=[]
    for i in range(24):
        std.append(flat(p,E.zero)); odd.append(flat(E.zero,E.mul(p,yf)))
        p=E.shift(p)
    std+=odd
    savedstd=[tuple(map(Q,v)) for v in maps['point_standard_columns']]
    require(std==savedstd,'all_standard_columns')
    power=[]; a=E.one; b=E.zero
    for i in range(48):
        power.append(flat(a,b))
        if i<47: a,b=E.mul(constant(cp),E.mul(b,yf)),E.mul(a,yf)
    require(power==[tuple(map(Q,v)) for v in maps['point_power_columns']],'all_direct_Y_power_columns')
    # Both rational coordinate transports on every column and every coordinate.
    for name,cols,expected in (('matrix',std,power),('inverse',power,std)):
        mat=[[Q(v) for v in row] for row in src[name]]
        for j in range(48):
            image=tuple(sum((mat[i][j]*cols[i][n] for i in range(48) if mat[i][j] and cols[i][n]),Q(0)) for n in range(336))
            require(image==expected[j],name+'_column_'+str(j))
    line=[tuple(Q(n==i) for i in range(336)) for n in range(48)]
    require(line==[tuple(map(Q,v)) for v in maps['line_columns']],'all_line_columns')
    ox=flat(scale(sub(X,lift((d([12]),))),Q(1,36)),E.zero)
    oy=flat(lift((d([Q(-1,2)]),)),scale(yf,Q(1,216)))
    require(ox==tuple(map(Q,maps['point_original_x'])),'original_x_all_coordinates')
    require(oy==tuple(map(Q,maps['point_original_y'])),'original_y_all_coordinates')
    require(std[0]==line[0] and std[0][0]==1,'unital_nonzero_target')
    # Full original-model relation in the even/odd pair algebra.
    xa,xb=unflat(ox); ya,yb=unflat(oy)
    require(xb==E.zero,'original_x_even')
    x2=E.mul(xa,xa)
    ev=E.add(E.add(E.mul(ya,ya),E.mul(constant(cp),E.mul(yb,yb))),ya)
    ev=E.add(sub(sub(ev,E.mul(x2,xa)),x2),scale(xa,2))
    od=E.add(scale(E.mul(ya,yb),2),yb)
    zero('original_curve_even',ev); zero('original_curve_odd',od)
    # Named-condition mutants only: retain the precise limited scope.
    altered=list(oy); altered[24]+=1
    badqi=list(qi); badl=list(badqi[0]); badd=list(badl[0]); badd[0]+=1
    badl[0]=tuple(badd);badqi[0]=tuple(badl);badqi=tuple(badqi)
    rejections=[
      {'case':'dense_q_inverse_plus_one','condition':'q_unit','rejected':E.mul(eq,badqi)!=E.one,'full_malformed_replay':False},
      {'case':'dense_original_y_odd_V_change','condition':'original_y_all_coordinates','rejected':tuple(altered)!=oy,'full_malformed_replay':False},
      {'case':'dense_line_missing_odd_block','condition':'all_line_columns','rejected':line[:24]!=line,'full_malformed_replay':False}]
    require(all(v['rejected'] for v in rejections),'all_distinct_condition_rejections')
    save('dense-mutants.json',{'q_inverse':badqi,'point_original_y':altered,'line_columns':line[:24]})
    save('dense-evidence.json',{'arithmetic':'fixed-length rational Horner quotient multiplication','checks':checks,'residuals':residuals,'point_standard_columns':std,'point_power_columns':power,'line_columns':line,'point_original_x':ox,'point_original_y':oy,'rejections':rejections,'passed':True})
    print('distinct dense: all 336 coordinates, both bases/maps and rejections passed',flush=True)
    return {'passed':True,'conditions':len(checks),'full_coordinates':336,'point_columns_each_basis':48,'line_columns':48,'residuals':list(residuals),'rejections':rejections}
