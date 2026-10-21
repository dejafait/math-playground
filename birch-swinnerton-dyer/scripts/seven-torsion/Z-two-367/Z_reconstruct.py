"""Separate exact forward elimination; no producer/verifier helper imports."""
from pathlib import Path
from fractions import Fraction as F
import json, sys, time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent; S=D.parent
N=48; I=[[F(i==j) for j in range(N)] for i in range(N)]
def need(ok,label):
    if not ok: raise ArithmeticError(label)
def load(p): return json.loads(p.read_text())
def rat(a): return [[F(x) for x in r] for r in a]
def mul(a,b):
    out=[[F(0) for _ in b[0]] for _ in a]
    for r,row in enumerate(a):
        for k,x in enumerate(row):
            if x:
                for c,y in enumerate(b[k]):
                    if y: out[r][c]+=x*y
    return out
def save(name,data):
    with (D/name).open('x') as f: json.dump(data,f,default=str,separators=(',',':')); f.write('\n')
def solve(a,b):
    """Unnormalized forward elimination followed by back substitution."""
    u=[r[:] for r in a]; v=[r[:] for r in b]; ops=[]; pivots=[]; sign=1
    for k in range(N):
        p=next(r for r in range(k,N) if u[r][k])
        if p!=k:
            u[k],u[p]=u[p],u[k]; v[k],v[p]=v[p],v[k]
            ops.append(['swap',k,p]); sign=-sign
        pivots.append(u[k][k])
        for r in range(k+1,N):
            if not u[r][k]: continue
            q=u[r][k]/u[k][k]; ops.append(['subtract',r,k,q])
            u[r]=[x-q*y for x,y in zip(u[r],u[k])]
            v[r]=[x-q*y for x,y in zip(v[r],v[k])]
    x=[[F(0) for _ in b[0]] for _ in range(N)]
    for r in range(N-1,-1,-1):
        for c in range(len(b[0])):
            x[r][c]=(v[r][c]-sum((u[r][k]*x[k][c] for k in range(r+1,N)),F(0)))/u[r][r]
    det=F(sign)
    for p in pivots: det*=p
    need(mul(a,x)==b,'all_solution_residuals')
    return {'a':a,'rhs':b,'upper':u,'transformed_rhs':v,'solution':x,
            'operations':ops,'pivots':pivots,'swap_sign':sign,'determinant':det}
def reread(c):
    a=rat(c['a']); b=rat(c['rhs']); u=[r[:] for r in a]; v=[r[:] for r in b]; sign=1
    for op in c['operations']:
        if op[0]=='swap':
            _,r,k=op; u[r],u[k]=u[k],u[r]; v[r],v[k]=v[k],v[r]; sign=-sign
        else:
            _,r,k,q=op; q=F(q)
            need(u[k][k]!=0 and u[r][k]==q*u[k][k],'persisted_elimination_factor')
            u[r]=[x-q*y for x,y in zip(u[r],u[k])]
            v[r]=[x-q*y for x,y in zip(v[r],v[k])]
    need(u==rat(c['upper']) and v==rat(c['transformed_rhs']),'all_persisted_row_operations')
    need(all(u[r][k]==0 for r in range(N) for k in range(r)),'complete_upper_triangle')
    pivots=[u[r][r] for r in range(N)]; need(all(pivots),'all_nonzero_pivots')
    need(pivots==list(map(F,c['pivots'])) and sign==c['swap_sign'],'all_pivots_and_sign')
    det=F(sign)
    for p in pivots: det*=p
    need(det==F(c['determinant']),'persisted_determinant')
    x=rat(c['solution']); need(mul(a,x)==b and mul(u,x)==v,'all_persisted_solution_entries')
    if b==I: need(mul(x,a)==I,'persisted_reverse_inverse')
    return x,det
def main():
    h=load(S/'nonmonic-order-283/basis.json')['H']
    need(len(h)==49 and h[-1]==343 and all(type(z) is int for z in h),'original_H')
    b=[[F(0) for _ in range(N)] for _ in range(N)]; b[0][0]=F(1)
    for j in range(1,N):
        for i in range(j+1): b[i][j]=F(h[48-j+i])
    even=[1,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28,4,5,14]
    odd=[1,9,19,16,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28]
    a=[r[:] for r in I]
    for i in range(N):
        a[i][0]=F(even[i//2] if i%2==0 else 0,31)
        a[i][1]=F(odd[i//2] if i%2 else 0,31)
    m=mul(b,a)
    n=[[x/(2 if j==47 else 1) for j,x in enumerate(r)] for r in m]
    s=[[x/(2 if j>=46 else 1) for j,x in enumerate(r)] for r in n]
    u=[[x/(2 if j>=45 else 1) for j,x in enumerate(r)] for r in s]
    v=[[x/(2 if j>=44 else 1) for j,x in enumerate(r)] for r in u]
    w=[[x/(2 if j>=43 else 1) for j,x in enumerate(r)] for r in v]

    import math
    z=[[x/(2 if j>=42 else 1) for j,x in enumerate(row)] for row in w]
    cert={}
    cert['power']=solve(z,[I[i]+w[i]+[F(i==0)] for i in range(N)])
    x=cert['power']['solution'];inv=[r[:48] for r in x];inc=[r[48:96] for r in x];unit=[r[96] for r in x]
    cert['old_power']=solve(w,[I[i]+[F(i==0)] for i in range(N)])
    oldinv=[r[:48] for r in cert['old_power']['solution']]
    oldunit=[r[48] for r in cert['old_power']['solution']]
    cert['inclusion']=solve(inc,I);invinc=cert['inclusion']['solution']
    cert['b_coordinates']=solve(b,z);B=cert['b_coordinates']['solution']
    cert['b_inverse']=solve(B,I)
    original=load(S/'certificate.json');p=rat(original['matrix']);pz=mul(p,z)
    need(h==original['primitive_integer_factors'][0]
        and [F(x,343) for x in h]==list(map(F,original['h'])),'whole_original_polynomial')
    cert['two_coordinates']=solve(pz,I)
    got=load(D/'z-basis.json');old=load(D/'w-basis.json')
    dec=load(D/'decision-359.json');aud=load(D/'Z-independent-multiplier.json')
    need(dec==load(D/'decision-361.json'),'whole_original_audited_decision')
    for f,r,mat,back in [('basis_to_power','power_to_basis',z,inv),
        ('basis_in_b','b_to_basis',B,cert['b_inverse']['solution']),
        ('to_L067','from_L067',pz,cert['two_coordinates']['solution'])]:
        need(mat==rat(got[f]) and back==rat(got[r]),'all_Z_transports_'+f)
        need(mul(mat,back)==I and mul(back,mat)==I,'both_Z_inverses_'+f)
    need(w==rat(old['basis_to_power']) and oldinv==rat(old['power_to_basis'])
        and mul(w,oldinv)==I and mul(oldinv,w)==I and oldunit==old['identity']==aud['identity'],
        'direct_W_inverse_and_unit')
    need(all(x.denominator==1 for row in inc for x in row),'integral_W_inclusion')
    need(inc==rat(got['old_inclusion'])==rat(dec['inverse'])==rat(aud['inclusion']),'whole_inclusion')
    need(invinc==rat(got['basis_in_w'])==rat(dec['M'])==rat(aud['basis']),'whole_multiplier')
    q=[[2*x for x in row] for row in invinc]
    need(q==dec['numerator']==aud['numerator']==load(D/'Z-numerator-359.json')['basis']
        ==load(D/'Z-numerator-361.json')['basis']==load(D/'Z-independent-preimage.json')['basis'],
        'whole_numerator')
    need(mul(z,inc)==w and mul(w,invinc)==z and mul(inc,invinc)==I and mul(invinc,inc)==I,
        'both_lattice_equations')
    audited=mul(w,rat(aud['basis']))
    forward=mul(inv,audited);reverse=mul(rat(aud['inclusion']),mul(oldinv,z))
    need(all(x.denominator==1 for mat in (forward,reverse) for row in mat for x in row)
        and mul(z,forward)==audited and mul(audited,reverse)==z
        and mul(forward,reverse)==I and mul(reverse,forward)==I,'both_integral_Z_containments')
    need(abs(cert['inclusion']['determinant'])==64==got['index']==dec['index']==aud['determinant'],'index_64')
    need(aud['index_orientation']=='[(I:I):W] = absolute determinant of W basis in (I:I)','orientation')
    need(cert['old_power']['determinant']/cert['power']['determinant']==cert['inclusion']['determinant'],
        'determinant_ratio')
    need(unit==list(map(F,got['identity']))==list(map(F,dec['identity_in_multiplier']))
        ==list(map(F,aud['identity_in_multiplier'])) and all(x.denominator==1 for x in unit)
        and mul(z,[[x] for x in unit])==[[F(i==0)] for i in range(N)],'actual_constant_one')
    scaled={}
    for label,scale,mat in [('m',31,m),('n',62,n),('s',124,s),('u',248,u),('v',496,v),('w',992,w),('z',1984,z)]:
        need(math.lcm(*(x.denominator for row in mat for x in row))==scale,'entire_denominator_lcm_'+label)
        scaled[label]=[[scale*mat[r][j] for r in range(N)] for j in range(N)]
        need(all(x.denominator==1 for row in scaled[label] for x in row),'scaled_integrality_'+label)
    mb=load(S/'radical-overorder-295/basis.json');nb=load(S/'index-two-table-321/basis.json')
    sb=load(D/'basis.json');ub=load(D/'u-basis.json');vb=load(D/'v-basis.json')
    need(a==rat(mb['M']) and scaled['m']==list(map(list,zip(*mul(b,rat(mb['numerator']))))),'original_m_coordinates')
    for label,obj in [('n',nb),('s',sb),('u',ub),('v',vb),('w',old),('z',got)]:
        need(scaled[label]==obj['scaled_polynomials'],'all_scaled_slots_'+label)
        need(obj['original_scale']==31 and obj['enlargement_denominator']==2,'scale_origin_'+label)
    need(nb['scale']==sb['input_scale']==62 and sb['scale']==ub['input_scale']==124
        and ub['scale']==vb['input_scale']==248 and vb['scale']==old['input_scale']==496
        and old['scale']==got['input_scale']==992 and got['scale']==1984
        and ub['prior_scales']==[31,62,124] and vb['prior_scales']==[31,62,124,248]
        and old['prior_scales']==[31,62,124,248,496] and got['prior_scales']==[31,62,124,248,496,992],
        'complete_scale_metadata')
    complete={'systems':cert,'reconstructed':{'b':b,'a':a,'m':m,'n':n,'s':s,'u':u,'v':v,'w':w,'z':z,
        'L067_map':p,'two_coordinates':pz},'scaled':scaled,'identity':unit,'old_identity':oldunit,
        'inclusion':inc,'inverse_inclusion':invinc,'audited_Z':audited,
        'forward_integral_comparison':forward,'reverse_integral_comparison':reverse}
    save('Z-exact-lattice-certificate.json',complete)
    persisted=load(D/'Z-exact-lattice-certificate.json')
    need(persisted==json.loads(json.dumps(complete,default=str)),'entire_Z_certificate_roundtrip')
    for c in persisted['systems'].values():reread(c)
    original365=load(S/'Z-table-audit-365/Z-exact-lattice-certificate.json')
    need(original365==persisted,'entire_original365_Z_certificate')
    for c in original365['systems'].values():reread(c)
    for prefix,un in [('w-',oldunit),('z-',unit)]:
        table=[load(D/(prefix+'product-%02d.json'%i)) for i in range(N)]
        for i in range(N):
            need([sum(un[j]*table[j][i][k] for j in range(N)) for k in range(N)]==I[i]
                and [sum(un[j]*table[i][j][k] for j in range(N)) for k in range(N)]==I[i],
                'all_direct_unit_actions_'+prefix+str(i))
    save('Z-solve-report.json',{'status':'PASS','failures':[],'elimination_systems':6,
        'transport_entries':13824,'inclusion_entries':4608,'inverse_products':8,'scaled_slots':16128,
        'index':64,'scale':1984,'solved_identity_actions':192,'both_integral_Z_containments':True,
        'complete_certificate_reread':True,'all_scales_derived_from_full_denominator_lcm':True})
if __name__=='__main__':main()
