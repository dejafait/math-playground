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
    # All six system inputs above/below are canonical definitions, not saved inverses.
    cert={}; cert['power']=solve(w,[I[i]+v[i]+[F(i==0)] for i in range(N)])
    x=cert['power']['solution']; inv=[r[:48] for r in x]; inc=[r[48:96] for r in x]; unit=[r[96] for r in x]
    cert['old_power']=solve(v,[I[i]+[F(i==0)] for i in range(N)])
    oldinv=[r[:48] for r in cert['old_power']['solution']]; oldunit=[r[48] for r in cert['old_power']['solution']]
    cert['inclusion']=solve(inc,I)
    cert['b_coordinates']=solve(b,w); B=cert['b_coordinates']['solution']
    cert['b_inverse']=solve(B,I)
    original=load(S/'certificate.json'); p=rat(original['matrix']); pw=mul(p,w)
    need(h==original['primitive_integer_factors'][0] and [F(z,343) for z in h]==list(map(F,original['h'])),'whole_original_polynomial')
    cert['two_coordinates']=solve(pw,I)
    got=load(D/'w-basis.json'); old=load(D/'v-basis.json')
    dec=load(D/'decision-351.json'); aud=load(D/'W-independent-multiplier.json')
    need(dec==load(D/'decision-353.json'),'whole_original_audited_decision')
    for f,r,mat,back in [('basis_to_power','power_to_basis',w,inv),
        ('basis_in_b','b_to_basis',B,cert['b_inverse']['solution']),
        ('to_L067','from_L067',pw,cert['two_coordinates']['solution'])]:
        need(mat==rat(got[f]) and back==rat(got[r]),'all_W_transports_'+f)
        need(mul(mat,back)==I and mul(back,mat)==I,'both_W_inverses_'+f)
    need(v==rat(old['basis_to_power']) and oldinv==rat(old['power_to_basis'])
        and mul(oldinv,v)==I and mul(v,oldinv)==I and oldunit==old['identity']==aud['identity'],'direct_V_inverse_and_unit')
    invinc=cert['inclusion']['solution']
    need(all(z.denominator==1 for row in inc for z in row),'integral_V_inclusion')
    need(inc==rat(got['old_inclusion'])==rat(dec['inverse'])==rat(aud['inclusion']),'whole_inclusion')
    need(invinc==rat(got['basis_in_v'])==rat(dec['M'])==rat(aud['basis']),'whole_multiplier')
    q=[[2*z for z in row] for row in invinc]
    need(q==dec['numerator']==aud['numerator']==load(D/'W-numerator-351.json')['basis']
        ==load(D/'W-numerator-353.json')['basis']==load(D/'W-independent-preimage.json')['basis'],'whole_numerator')
    need(mul(w,inc)==v and mul(v,invinc)==w and mul(inc,invinc)==I and mul(invinc,inc)==I,'both_lattice_equations')
    audited=mul(v,rat(aud['basis'])); forward=mul(inv,audited); reverse=mul(rat(aud['inclusion']),mul(oldinv,w))
    need(all(z.denominator==1 for mat in (forward,reverse) for row in mat for z in row)
        and mul(w,forward)==audited and mul(audited,reverse)==w
        and mul(forward,reverse)==I and mul(reverse,forward)==I,'both_integral_W_containments')
    need(abs(cert['inclusion']['determinant'])==32==got['index']==dec['index']==aud['determinant'],'index_32')
    need(aud['index_orientation']=='[(I:I):V] = absolute determinant of V basis in (I:I)','orientation')
    need(cert['old_power']['determinant']/cert['power']['determinant']==cert['inclusion']['determinant'],'determinant_ratio')
    need(unit==list(map(F,got['identity']))==list(map(F,dec['identity_in_multiplier']))
        ==list(map(F,aud['identity_in_multiplier'])) and all(z.denominator==1 for z in unit)
        and mul(w,[[z] for z in unit])==[[F(i==0)] for i in range(N)],'actual_constant_one')
    scaled={}
    for label,scale,mat in [('m',31,m),('n',62,n),('s',124,s),('u',248,u),('v',496,v),('w',992,w)]:
        scaled[label]=[[scale*mat[r][j] for r in range(N)] for j in range(N)]
        need(all(z.denominator==1 for row in scaled[label] for z in row),'scaled_integrality_'+label)
    mb=load(S/'radical-overorder-295/basis.json'); nb=load(S/'index-two-table-321/basis.json')
    sb=load(D/'basis.json'); ub=load(D/'u-basis.json')
    need(a==rat(mb['M']) and scaled['m']==list(map(list,zip(*mul(b,rat(mb['numerator']))))),'original_m_coordinates')
    for label,obj in [('n',nb),('s',sb),('u',ub),('v',old),('w',got)]:
        need(scaled[label]==obj['scaled_polynomials'],'all_scaled_slots_'+label)
        need(obj['original_scale']==31 and obj['enlargement_denominator']==2,'scale_origin_'+label)
    need(nb['scale']==sb['input_scale']==62 and sb['scale']==ub['input_scale']==124
        and ub['scale']==old['input_scale']==248 and old['scale']==got['input_scale']==496 and got['scale']==992
        and ub['prior_scales']==[31,62,124] and old['prior_scales']==[31,62,124,248]
        and got['prior_scales']==[31,62,124,248,496],'complete_scale_metadata')
    complete={'systems':cert,'reconstructed':{'b':b,'a':a,'m':m,'n':n,'s':s,'u':u,'v':v,'w':w,'L067_map':p,'two_coordinates':pw},
        'scaled':scaled,'identity':unit,'old_identity':oldunit,'inclusion':inc,'inverse_inclusion':invinc,
        'audited_W':audited,'forward_integral_comparison':forward,'reverse_integral_comparison':reverse}
    save('W-exact-lattice-certificate.json',complete)
    persisted=load(D/'W-exact-lattice-certificate.json')
    need(persisted==json.loads(json.dumps(complete,default=str)),'entire_W_certificate_roundtrip')
    for c in persisted['systems'].values(): reread(c)
    original357=load(S/'W-table-audit-357/W-exact-lattice-certificate.json')
    need(original357==persisted,'entire_original357_W_certificate')
    for c in original357['systems'].values(): reread(c)
    original359=load(S/'W-two-359/W-exact-lattice-certificate.json')
    need(original359==persisted,'entire_original359_W_certificate')
    for c in original359['systems'].values(): reread(c)
    original361=load(S/'W-two-audit-361/W-exact-lattice-certificate.json')
    need(original361==persisted,'entire_original361_W_certificate')
    for c in original361['systems'].values(): reread(c)
    # Bind and replay the production's complete V solve copy, separately from W.
    prod=load(S/'index-thirty-two-table-355/exact-lattice-certificate.json')
    fresh=load(D/'exact-lattice-certificate.json')
    need(prod==fresh,'whole_step355_V_solve_copy')
    for c in prod['systems'].values(): reread(c)
    for folder in ['W-table-audit-357','W-two-359','W-two-audit-361']:
        vc=load(S/folder/'exact-lattice-certificate.json')
        need(vc==fresh,'entire_original_V_copy_'+folder)
        for c in vc['systems'].values(): reread(c)
    for prefix,unit_vector in [('v-',oldunit),('w-',unit)]:
        table=[load(D/(prefix+'product-%02d.json'%i)) for i in range(N)]
        for i in range(N):
            need([sum(unit_vector[j]*table[j][i][k] for j in range(N)) for k in range(N)]==I[i]
                and [sum(unit_vector[j]*table[i][j][k] for j in range(N)) for k in range(N)]==I[i],'direct_solved_unit_actions_'+prefix+str(i))
    save('W-solve-report.json',{'status':'PASS','failures':[],'elimination_systems':6,'transport_entries':13824,
        'inclusion_entries':4608,'scaled_slots':13824,'index':32,'scale':992,'solved_identity_actions':192,
        'complete_certificate_reread':True,'both_integral_W_containments':True,'whole_step355_V_solves_replayed':True})
if __name__=='__main__': main()
