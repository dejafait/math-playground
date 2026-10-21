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
    need(len(h)==49 and h[-1]==343,'full_original_H_degree_leading')
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
    got=load(D/'u-basis.json'); old=load(D/'basis.json')
    prior=load(S/'index-two-table-321/basis.json')
    dec=load(D/'decision-335.json'); aud=load(D/'fixed-independent-multiplier.json')
    need(dec==load(D/'decision-337.json'),'entire_audited_multiplier_input')
    cert={}; cert['power']=solve(u,[I[i]+s[i]+[F(i==0)] for i in range(N)])
    x=cert['power']['solution']; inv=[r[:48] for r in x]; inc=[r[48:96] for r in x]; identity=[r[96] for r in x]
    need(mul(inv,u)==I,'full_power_reverse_inverse')
    cert['old_power']=solve(s,[I[i]+[F(i==0)] for i in range(N)])
    oldinv=[r[:48] for r in cert['old_power']['solution']]
    oldidentity=[r[48] for r in cert['old_power']['solution']]
    need(oldinv==rat(old['power_to_basis']) and s==rat(old['basis_to_power'])
         and mul(oldinv,s)==I and oldidentity==old['identity']==aud['identity'],'full_old_inverse_and_identity')
    cert['inclusion']=solve(inc,I)
    cert['b_coordinates']=solve(b,u); B=cert['b_coordinates']['solution']
    cert['b_inverse']=solve(B,I)
    original=load(S/'certificate.json'); p=rat(original['matrix']); pu=mul(p,u)
    cert['two_coordinates']=solve(pu,I)
    for f,r,mat,back in [('basis_to_power','power_to_basis',u,inv),
                        ('basis_in_b','b_to_basis',B,cert['b_inverse']['solution']),
                        ('to_L067','from_L067',pu,cert['two_coordinates']['solution'])]:
        need(mat==rat(got[f]) and back==rat(got[r]),'all_saved_transport_entries_'+f)
        need(mul(mat,back)==I and mul(back,mat)==I,'both_full_inverse_products_'+f)
    invinc=cert['inclusion']['solution']
    need(all(x.denominator==1 for r in inc for x in r),'entire_integral_inclusion')
    need(inc==rat(got['old_inclusion'])==rat(dec['inverse'])==rat(aud['inclusion']),'full_old_inclusion')
    need(invinc==rat(got['basis_in_s'])==rat(dec['M'])==rat(aud['basis']),'entire_multiplier_lattice')
    q=[[2*x for x in r] for r in invinc]
    need(q==dec['numerator']==aud['numerator']==load(D/'fixed-numerator-lattice.json')['basis'],'entire_numerator_lattice')
    need(mul(u,inc)==s and mul(inc,invinc)==I and mul(invinc,inc)==I,'both_lattice_containments')
    need(abs(cert['inclusion']['determinant'])==8==got['index']==dec['index']==aud['determinant'],'exact_inclusion_determinant')
    need(cert['old_power']['determinant']/cert['power']['determinant']==cert['inclusion']['determinant'],'determinant_ratio')
    need(identity==list(map(F,got['identity']))==list(map(F,dec['identity_in_multiplier']))==list(map(F,aud['identity_in_multiplier'])),'entire_saved_identity')
    need(all(x.denominator==1 for x in identity) and mul(u,[[x] for x in identity])==[[F(i==0)] for i in range(N)],'actual_integral_identity')
    scaled={}
    for label,scale,mat in [('m',31,m),('n',62,n),('s',124,s),('u',248,u)]:
        scaled[label]=[[scale*mat[r][j] for r in range(N)] for j in range(N)]
        need(all(x.denominator==1 for row in scaled[label] for x in row),'all_scaled_integrality_'+label)
    need(scaled['n']==prior['scaled_polynomials'] and scaled['s']==old['scaled_polynomials'] and scaled['u']==got['scaled_polynomials'],'all_saved_scaled_polynomials')
    need(prior['original_scale']==old['original_scale']==got['original_scale']==31
         and prior['scale']==old['input_scale']==62 and old['scale']==got['input_scale']==124
         and got['scale']==248 and got['prior_scales']==[31,62,124]
         and prior['enlargement_denominator']==old['enlargement_denominator']==got['enlargement_denominator']==2,'all_scale_metadata')
    reconstructed={'b':b,'a':a,'m':m,'n':n,'s':s,'u':u,'two_coordinates':pu}
    complete={'systems':cert,'reconstructed':reconstructed,'scaled':scaled,'identity':identity,
              'old_identity':oldidentity,'inclusion':inc,'inverse_inclusion':invinc}
    save('exact-lattice-certificate.json',complete)
    reread_cert=load(D/'exact-lattice-certificate.json')
    need(reread_cert==json.loads(json.dumps(complete,default=str)),'complete_certificate_reread')
    for c in reread_cert['systems'].values(): reread(c)
    # Identity actions are checked anew using solved vectors, on both full tables.
    for prefix,unit in [('',oldidentity),('u-',identity)]:
        table=[load(D/(prefix+'product-%02d.json'%i)) for i in range(N)]
        for i in range(N):
            need([sum(unit[j]*table[j][i][k] for j in range(N)) for k in range(N)]==I[i]
                 and [sum(unit[j]*table[i][j][k] for j in range(N)) for k in range(N)]==I[i],
                 'solved_identity_both_table_actions_'+prefix+str(i))
    save('independent-report.json',{'status':'PASS','failures':[],'elimination_systems':6,
         'transport_entries':13824,'inclusion_entries':4608,'scaled_slots':9216,'index':8,
         'identity_entries':96,'solved_identity_actions':192,'complete_certificate_reread':True})
if __name__=='__main__': main()
