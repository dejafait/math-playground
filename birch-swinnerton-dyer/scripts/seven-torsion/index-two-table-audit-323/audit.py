"""One fresh L084 replay and distinct exact-elimination certificate."""
from pathlib import Path
from fractions import Fraction as Q
import hashlib, json, subprocess, sys, time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent
ROOT=D.parents[2]
SRC=D.parent
OLD=SRC/'index-two-table-321'
CAP=134217728
START=time.monotonic()
N=48
I=[[Q(i==j) for j in range(N)] for i in range(N)]
REPORT={'status':'STOP','failures':[]}
def require(ok,label):
    if not ok: raise ValueError(label)
def load(p): return json.loads(p.read_text())
def save(name,obj):
    raw=(json.dumps(obj,default=str,separators=(',',':'))+'\n').encode()
    require(sum(p.stat().st_size for p in D.iterdir() if p.is_file())+len(raw)+65536<CAP,'byte_cap')
    with (D/name).open('xb') as f: f.write(raw)
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():
    paths=set(ROOT/p for p in load(OLD/'input-hashes.json'))
    paths.update(p for p in OLD.iterdir() if p.is_file())
    return {str(p.relative_to(ROOT)):digest(p) for p in sorted(paths)}
def rational(a): return [[Q(x) for x in row] for row in a]
def multiply(a,b):
    cols=list(zip(*b))
    return [[sum((x*y for x,y in zip(row,col)),Q(0)) for col in cols] for row in a]
def eliminate(a,rhs):
    """Full rational Gauss--Jordan; retain every reversible row operation."""
    rows=[list(row)+list(v) for row,v in zip(a,rhs)]
    det=Q(1); ops=[]
    for col in range(N):
        pivot=next((r for r in range(col,N) if rows[r][col]),None)
        require(pivot is not None,'full_rank_pivot_'+str(col))
        if pivot!=col:
            rows[pivot],rows[col]=rows[col],rows[pivot]
            det=-det; ops.append(['swap',pivot,col])
        factor=rows[col][col]; det*=factor
        rows[col]=[v/factor for v in rows[col]]
        ops.append(['scale',col,1/factor])
        for r in range(N):
            if r==col or not rows[r][col]: continue
            factor=-rows[r][col]
            rows[r]=[v+factor*w for v,w in zip(rows[r],rows[col])]
            ops.append(['add',r,col,factor])
    require([row[:N] for row in rows]==I,'whole_terminal_identity')
    return [row[N:] for row in rows],det,ops
def main():
    before=inventory(); save('original-hashes.json',before)
    require(all(before[p]==h for p,h in load(OLD/'input-hashes.json').items()),'upstream_hashes')
    names=['verify.py','input-hashes.json','basis.json']+['product-%02d.json'%i for i in range(N)]
    copies={}
    for name in names:
        with (D/name).open('xb') as f: f.write((OLD/name).read_bytes())
        require(digest(D/name)==digest(OLD/name),'byte_unchanged_copy_'+name)
        copies[name]={'source':str((OLD/name).relative_to(ROOT)),'sha256':digest(D/name)}
    save('copy-manifest.json',copies)
    with (D/'replay.log').open('x') as log:
        result=subprocess.run([sys.executable,'-B',str(D/'verify.py')],stdout=log,stderr=subprocess.STDOUT)
    require(result.returncode==0,'fresh_replay_exit')
    replay=load(D/'verification-report.json')
    for key,value in {'status':'PASS','product_slots':110592,'product_identities':2304,
                      'remainder_coefficients':218880,'transport_entries':13824,
                      'inverse_products':6,'identity_actions':96,'index':2,'failures':[]}.items():
        require(replay[key]==value,'replay_complete_'+key)
    h=load(SRC/'nonmonic-order-283/basis.json')['H']
    b=[[Q(0) for _ in range(N)] for _ in range(N)]; b[0][0]=Q(1)
    for col in range(1,N):
        for row in range(col+1): b[row][col]=Q(h[N-col+row])
    old=load(SRC/'radical-overorder-295/basis.json')
    a=[[Q(x,31) for x in row] for row in old['numerator']]
    oldpower=multiply(b,a)
    newpower=[[x/(2 if col==47 else 1) for col,x in enumerate(row)] for row in oldpower]
    got=load(D/'basis.json')
    require(newpower==rational(got['basis_to_power']),'independent_power_columns')
    # Solve simultaneously for inverse, old-lattice inclusion and actual identity.
    rhs=[I[r]+oldpower[r]+[Q(r==0)] for r in range(N)]
    solved,detnew,ops=eliminate(newpower,rhs)
    inv=[row[:N] for row in solved]
    inclusion=[row[N:2*N] for row in solved]
    identity=[row[-1] for row in solved]
    oldinv,detold,oldops=eliminate(oldpower,I)
    require(multiply(newpower,inv)==I and multiply(inv,newpower)==I,'both_recomputed_power_inverses')
    require(multiply(oldpower,oldinv)==I and multiply(oldinv,oldpower)==I,'both_recomputed_old_inverses')
    require(inv==rational(got['power_to_basis']),'entire_saved_power_inverse')
    require(all(x.denominator==1 for row in inclusion for x in row),'integral_inclusion')
    require(multiply(newpower,inclusion)==oldpower,'full_inclusion_equation')
    require(inclusion==rational(got['old_inclusion']),'entire_saved_inclusion')
    incinv,detinc,incops=eliminate(inclusion,I)
    require(multiply(inclusion,incinv)==I and multiply(incinv,inclusion)==I,'both_inclusion_inverses')
    require(abs(detinc)==abs(detold/detnew)==2,'independent_determinant_ratio_index_two')
    require(all(x.denominator==1 for x in identity) and identity==list(map(Q,got['identity'])),'actual_identity_coordinates')
    require(multiply(newpower,[[x] for x in identity])==[[Q(r==0)] for r in range(N)],'identity_equals_one')
    # Obtain the b-transport by solving against the reconstructed original basis.
    inb,detb,bops=eliminate(b,newpower)
    binv,detinb,inbops=eliminate(inb,I)
    require(inb==rational(got['basis_in_b']) and binv==rational(got['b_to_basis']),'independent_b_transports')
    require(multiply(inb,binv)==I and multiply(binv,inb)==I,'both_b_inverses')
    original=load(SRC/'certificate.json')
    twocoords=multiply(rational(original['matrix']),newpower)
    twoinv,dettwo,twoops=eliminate(twocoords,I)
    require(twocoords==rational(got['to_L067']) and twoinv==rational(got['from_L067']),'independent_two_coordinate_transports')
    require(multiply(twocoords,twoinv)==I and multiply(twoinv,twocoords)==I,'both_two_coordinate_inverses')
    save('exact-elimination-certificate.json',{
        'method':'rational Gauss-Jordan; matrices act on columns',
        'original_basis':b,'old_power_basis':oldpower,'new_power_basis':newpower,
        'new_rhs':rhs,'new_solution':solved,'new_operations':ops,'new_determinant':detnew,
        'old_inverse':oldinv,'old_operations':oldops,'old_determinant':detold,
        'inclusion':inclusion,'inclusion_inverse':incinv,'inclusion_operations':incops,
        'inclusion_determinant':detinc,'determinant_ratio':detold/detnew,'index':2,
        'identity':identity,'b_operations':bops,'b_determinant':detb,
        'basis_in_b':inb,'b_to_basis':binv,'in_b_operations':inbops,'in_b_determinant':detinb,
        'two_coordinate_basis':twocoords,'two_coordinate_inverse':twoinv,
        'two_coordinate_operations':twoops,'two_coordinate_determinant':dettwo,
        'all_full_matrix_checks':True,'failures':[]})
    after=inventory(); require(before==after,'all_originals_preserved')
    save('audit-preservation.json',{'equal':True,'original_files':len(before),'after':after})
    REPORT.update(status='PASS',original_files=len(before),copied_files=len(names),
                  product_slots=110592,product_identities=2304,transport_entries=13824,
                  replay_inverse_products=6,identity_actions=96,index=2,
                  exact_elimination_systems=6,exact_elimination_full_matrix_checks=True)
try: main()
except Exception as e: REPORT['failures']=[type(e).__name__+': '+str(e)]
finally:
    REPORT.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=CAP)
    save('audit-report.json',REPORT)
    print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
