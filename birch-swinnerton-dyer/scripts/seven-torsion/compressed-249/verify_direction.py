"""Independent full direction replay, importing only old verifier arithmetic."""
from fractions import Fraction as F
from pathlib import Path
import argparse,hashlib,json,signal,sys,time
R=Path(__file__).resolve().parent;U=R.parent
sys.path.insert(0,str(U))
import verify_certificate as V
def mm(A,B):
    return [[sum((a*b for a,b in zip(row,col) if a and b),F(0)) for col in zip(*B)] for row in A]
def matrix(x):return [[F(z) for z in row] for row in x]
def run(path,action_path=None):
    start=time.monotonic();signal.alarm(180); checks=[]
    def need(ok,label):
        if not ok:raise ValueError(label)
        checks.append(label)
    action_path=action_path or U/'scalar-actions-243/actions.json'
    c=json.loads(path.read_text());up=json.loads((U/'certificate.json').read_text());act=json.loads(action_path.read_text())
    need(c['schema']=='389-direction-v1','schema')
    need(c['upstream_hash']==hashlib.sha256((U/'certificate.json').read_bytes()).hexdigest() and c['action_hash']==hashlib.sha256(action_path.read_bytes()).hexdigest(),'both_input_hashes')
    f=list(map(F,up['f'])); z=V.clean(list(map(F,c['z'])))
    expected=[]
    for i in [1,2,3]:
        need(not any(map(F,act['maps'][str(i)]['X'][1])),'even_scalar_'+str(i))
        expected=V.plus(expected,list(map(F,act['maps'][str(i)]['X'][0])))
    need(z==expected,'geometric_orbit_sum')
    def mul(a,b):return V.remainder(V.times(a,b),f)
    powers=[[F(1)]]
    for i in range(8):powers.append(mul(powers[-1],z))
    need([V.clean(list(map(F,p))) for p in c['powers']]==powers,'all_nine_powers')
    cols=[V.fixed(V.remainder([F(0)]*k+powers[j],f),24) for k in range(3) for j in range(8)]
    M=matrix(c['mixed_matrix']);N=matrix(c['mixed_inverse'])
    need(M==list(map(list,zip(*cols))),'all_24_mixed_basis_columns')
    I=[[F(i==j) for j in range(24)] for i in range(24)]
    need(mm(M,N)==I and mm(N,M)==I,'both_complete_mixed_inverse_products')
    h=list(map(F,c['h']));need(len(h)==9 and h[-1]==1,'degree_eight_monic')
    need(not V.evalmod(h,z,f),'full_h_annihilation')
    cubic=[list(map(F,p)) for p in c['cubic']]
    need(len(cubic)==4 and cubic[-1]==[1],'cubic_monic')
    cv=[]
    for k,pol in enumerate(cubic):
        v=V.evalmod(pol,z,f);cv=V.plus(cv,V.remainder([F(0)]*k+v,f))
    need(not cv,'entire_cubic_identity')
    EB=matrix(c['E_B']);KB=matrix(c['K_B']);RB=matrix(c['R_B'])
    ET=matrix(c['E_T']);KT=matrix(c['K_T']);RT=matrix(c['R_T'])
    need(len(EB)==48 and all(len(row)==8 for row in EB) and len(KB)==8 and all(len(row)==48 for row in KB),'complete_inclusion_retraction_shapes')
    need(EB==[row[:8] for row in M]+[[F(0)]*8 for _ in range(24)],'entire_B_inclusion')
    need(mm(EB,KB)==RB,'entire_B_projection_factorization')
    need(mm(KB,EB)==[[F(i==j) for j in range(8)] for i in range(8)],'B_inverse_on_full_image')
    mean=[[sum((F(act['maps'][str(a)]['B_action'][i][j]) for a in range(1,7)),F(0))/6 for j in range(48)] for i in range(48)]
    need(RB==mean,'all_2304_Reynolds_entries_six_scalars')
    for a in range(1,7):need(mm(matrix(act['maps'][str(a)]['B_action']),EB)==EB,'all_fixed_basis_columns_scalar_'+str(a))
    oldM=matrix(up['matrix']);oldN=matrix(up['inverse'])
    need(mm(oldM,ET)==EB and mm(oldN,EB)==ET,'both_entire_inclusion_transports')
    need(mm(KB,oldM)==KT and mm(KT,oldN)==KB,'both_entire_retraction_transports')
    need(mm(ET,KT)==RT and mm(KT,ET)==[[F(i==j) for j in range(8)] for i in range(8)],'entire_T_image_inverses')
    need(mm(mm(oldN,RB),oldM)==RT,'entire_projection_transport')
    # All products of the eight direction basis elements; exact Q[Z]/h reduction.
    for i in range(8):
        for j in range(8):
            pol=[F(0)]*(i+j)+[F(1)]
            need(V.evalmod(V.remainder(pol,h),z,f)==mul(powers[i],powers[j]),'direction_product_'+str(i)+'_'+str(j))
    need(c['dimension']==8 and c['cover_degree']==6,'actual_required_dimensions')
    signal.alarm(0)
    return {'passed':True,'checks':checks,'failures':[],'dimension':8,'required_dimension':8,'mixed_rank':24,'required_mixed_rank':24,'seconds':time.monotonic()-start,'scope':'direction algebra only; no incidence relation or norm'}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--certificate',type=Path,default=R/'direction.json');ap.add_argument('--report',type=Path,default=R/'direction-replay.json');args=ap.parse_args()
    try:report=run(args.certificate)
    except Exception as e:report={'passed':False,'failures':[str(e)]}
    args.report.write_text(json.dumps(report,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='checks'}))
    sys.exit(0 if report['passed'] else 1)
