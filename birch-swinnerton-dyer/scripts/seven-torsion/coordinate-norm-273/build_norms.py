"""Full coordinate matrices; sparse convolution and Laplace determinants."""
from fractions import Fraction as Q
from functools import lru_cache
import sys
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
    matrices={}
    for name,a,b in [('X',X,E.zero),('Y',E.zero,yf)]:
        columns=[];aa=a;bb=b
        for col in range(7):
            columns.append([B.trim((aa[row] if row<len(aa) else L.zero,bb[row] if row<len(bb) else L.zero)) for row in range(7)])
            if col<6:aa=E.mul(aa,X);bb=E.mul(bb,X)
        matrices[name]=[[columns[col][row] for col in range(7)] for row in range(7)]
    full={name:[[bflat(v) for v in row] for row in mat] for name,mat in matrices.items()}
    save('coordinate-matrices.json',{'entry_basis':'Z^j T^i V^e; j fastest; 8*3*2=48','column_basis':['1','X','X^2','X^3','X^4','X^5','X^6'],'matrices':full,'rational_slots':4704,'F':F,'y_V_factor':yf})
    print('Both 7-by-7 matrices saved: 4704 rational slots; complete transports pass.',flush=True)
    def determinant(mat,label):
        records={}
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
        return value
    norms={}
    for name,mat in matrices.items():
        print('Laplace determinant '+name,flush=True)
        norms[name]=determinant(mat,name)
    controls={}
    for v in (0,2):
        a=(L.trim((d([v]),)),) if v else B.zero
        scalar=[[a if i==j else B.zero for j in range(7)] for i in range(7)]
        value=determinant(scalar,'scalar-'+str(v))
        expected=(L.trim((d([v**7]),)),) if v else B.zero
        need(value==expected,'rank_seven_scalar_convention_'+str(v))
        controls[str(v)]={'matrix':[[bflat(x) for x in row] for row in scalar],'norm':bflat(value)}
    save('coordinate-norms.json',{'norms':{k:bflat(v) for k,v in norms.items()},'scalar_controls':controls})
    out.update(passed=True,rational_matrix_slots=4704,norm_slots=96,coordinate_count=2)
except Exception as exc:out['failures'].append(type(exc).__name__+': '+str(exc))
finally:finish('construction',out,t)
sys.exit(0 if out['passed'] else 1)
