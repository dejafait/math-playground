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
    g=[[x/(2 if j>=46 else 1) for j,x in enumerate(r)] for r in n]
    got=load(D/'basis.json'); prior=load(S/'index-two-table-321/basis.json')
    dec=load(S/'index-two-order-two-325/decision.json')
    need(dec==load(S/'index-four-audit-327/decision.json'),'entire_audited_multiplier_input')
    rhs=[I[i]+n[i]+[F(i==0)] for i in range(N)]
    cert={}; cert['power']=solve(g,rhs)
    x=cert['power']['solution']; inv=[r[:48] for r in x]; inc=[r[48:96] for r in x]; identity=[r[96] for r in x]
    need(mul(inv,g)==I,'full_power_reverse_inverse')
    cert['old_power']=solve(n,I); cert['inclusion']=solve(inc,I)
    cert['b_coordinates']=solve(b,g); B=cert['b_coordinates']['solution']
    cert['b_inverse']=solve(B,I)
    original=load(S/'certificate.json'); p=rat(original['matrix']); pg=mul(p,g)
    cert['two_coordinates']=solve(pg,I)
    for f,r,mat,back in [('basis_to_power','power_to_basis',g,inv),
                        ('basis_in_b','b_to_basis',B,cert['b_inverse']['solution']),
                        ('to_L067','from_L067',pg,cert['two_coordinates']['solution'])]:
        need(mat==rat(got[f]) and back==rat(got[r]),'all_saved_transport_entries_'+f)
        need(mul(mat,back)==I and mul(back,mat)==I,'both_full_inverse_products_'+f)
    invinc=cert['inclusion']['solution']
    need(all(x.denominator==1 for r in inc for x in r),'entire_integral_inclusion')
    need(inc==rat(got['old_inclusion'])==rat(dec['inverse']),'full_old_inclusion')
    need(invinc==rat(got['basis_in_n'])==rat(dec['M']),'entire_multiplier_lattice')
    need(mul(g,inc)==n and mul(inc,invinc)==I and mul(invinc,inc)==I,'both_lattice_containments')
    need(abs(cert['inclusion']['determinant'])==4==got['index'],'exact_inclusion_determinant')
    need(cert['old_power']['determinant']/cert['power']['determinant']==cert['inclusion']['determinant'],'determinant_ratio')
    need(identity==list(map(F,got['identity']))==list(map(F,dec['identity_in_multiplier'])),'entire_saved_identity')
    need(all(x.denominator==1 for x in identity) and mul(g,[[x] for x in identity])==[[F(i==0)] for i in range(N)],'actual_integral_identity')
    scaled={}
    for label,scale,mat in [('m',31,m),('n',62,n),('s',124,g)]:
        scaled[label]=[[scale*mat[r][j] for r in range(N)] for j in range(N)]
        need(all(x.denominator==1 for row in scaled[label] for x in row),'all_scaled_integrality_'+label)
    need(scaled['n']==prior['scaled_polynomials'] and scaled['s']==got['scaled_polynomials'],'all_saved_scaled_polynomials')
    need(prior['original_scale']==got['original_scale']==31 and prior['scale']==got['input_scale']==62 and got['scale']==124 and got['enlargement_denominator']==2,'all_scale_metadata')
    save('exact-lattice-certificate.json',{'systems':cert,'reconstructed':{'b':b,'a':a,'m':m,'n':n,'s':g,'two_coordinates':pg},'scaled':scaled,'identity':identity,'inclusion':inc,'inverse_inclusion':invinc})
    reread_cert=load(D/'exact-lattice-certificate.json')
    need(reread_cert==json.loads(json.dumps({'systems':cert,'reconstructed':{'b':b,'a':a,'m':m,'n':n,'s':g,'two_coordinates':pg},'scaled':scaled,'identity':identity,'inclusion':inc,'inverse_inclusion':invinc},default=str)),'complete_certificate_reread')
    for c in reread_cert['systems'].values(): reread(c)
    save('independent-report.json',{'status':'PASS','failures':[],'elimination_systems':6,'transport_entries':13824,'inclusion_entries':4608,'scaled_slots':6912,'index':4,'identity_entries':48,'complete_certificate_reread':True})
if __name__=='__main__': main()
