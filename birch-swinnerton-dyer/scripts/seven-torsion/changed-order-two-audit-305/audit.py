"""One fixed audit: unchanged replay, distinct ranks, global lattices, witness.
No producer imports; no new order table, correction or prime.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, subprocess, sys, time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent
ROOT=D.parents[2]
OLD=D.parent/'changed-order-two-303'
START=time.monotonic()
CAP=134217728
N=48
E=[[int(i==j) for j in range(N)] for i in range(N)]
REPORT={'status':'STOP','phase':'inputs','failures':[]}
BEFORE={}

def need(ok,label):
    if not ok:raise ArithmeticError(label)

def size():return sum(p.stat().st_size for p in D.iterdir() if p.is_file())
def guard():
    need(time.monotonic()-START<180,'internal_180_second_cap')
    need(size()+65536<CAP,'aggregate_byte_cap')
def save(name,value):
    raw=(json.dumps(value,separators=(',',':'))+'\n').encode()
    need(size()+len(raw)+65536<CAP,'write_byte_cap')
    with (D/name).open('xb') as f:f.write(raw)
def read(p):return json.loads(p.read_text())
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def tr(a):return [list(r) for r in zip(*a)]
def mm(a,b):
    need(bool(b) and all(len(r)==len(b) for r in a),'inner_shapes')
    w=len(b[0]);need(all(len(r)==w for r in b),'right_shape')
    out=[[0]*w for _ in a]
    for i,row in enumerate(a):
        for j,x in enumerate(row):
            if x:
                for k,y in enumerate(b[j]):
                    if y:out[i][k]+=x*y
    return out
def mod(a):return [[x%2 for x in r] for r in a]
def inverse_mod2(a):
    n=len(a);eye=[[int(i==j) for j in range(n)] for i in range(n)]
    w=[row[:]+e for row,e in zip(a,eye)]
    for c in range(n-1,-1,-1):
        p=next((r for r in range(c,-1,-1) if w[r][c]),None)
        need(p is not None,'fresh_minor_pivot')
        w[c],w[p]=w[p],w[c]
        for r in range(n):
            if r!=c and w[r][c]:w[r]=[x^y for x,y in zip(w[r],w[c])]
    need([r[:n] for r in w]==eye,'fresh_minor_terminal_identity')
    inv=[r[n:] for r in w]
    need(mod(mm(a,inv))==mod(mm(inv,a))==eye,'both_full_minor_inverse_products')
    return inv

def lattice_check(name,free):
    # Independently generate all standard lifts and all 2e_i. No saved
    # elimination operations or saved generation matrices enter this construction.
    rows=[E[i] for i in free]
    S=tr(rows+[[2*x for x in r] for r in E])
    diag=[1 if i in free else 2 for i in range(N)]
    J=[[diag[i]*E[i][j] for j in range(N)] for i in range(N)]
    inv=[[F(E[i][j],diag[i]) for j in range(N)] for i in range(N)]
    selected=[free.index(i) if i in free else len(free)+i for i in range(N)]
    C=[[int(i==selected[j]) for j in range(N)] for i in range(len(free)+N)]
    B=[]
    for i in range(N):
        need(all(x%diag[i]==0 for x in S[i]),name+'_every_reverse_coefficient_integral')
        B.append([x//diag[i] for x in S[i]])
    need(mm(S,C)==J and mm(J,B)==S,name+'_both_integral_generations')
    need(mm(J,inv)==mm(inv,J)==E,name+'_both_full_rational_inverses')
    saved=read(D/(name+'.json'))
    need(saved['S']==S and saved['basis']==J and saved['C']==C and saved['D']==B
         and [[F(x) for x in r] for r in saved['inverse']]==inv,
         name+'_all_independent_lattice_coefficients_match')
    return {'free_coordinates':free,'S':S,'basis':J,'C':C,'D':B,
            'inverse':[[str(x) for x in r] for r in inv]}

def main():
    global BEFORE
    upstream=read(OLD/'input-hashes.json')
    need(len(upstream)==434,'complete_upstream_inventory')
    BEFORE={p:digest(ROOT/p) for p in upstream}
    need(BEFORE==upstream,'unchanged_upstream_before')
    originals=sorted(p for p in OLD.iterdir() if p.is_file())
    for p in originals:BEFORE[str(p.relative_to(ROOT))]=digest(p)
    save('original-hashes.json',BEFORE)
    REPORT.update(upstream_files=434,step303_files=len(originals),original_files=len(BEFORE))
    names=['verify.py','input-hashes.json','input-basis.json','frobenius.json',
           'radical-lattice.json','action-kernel.json','numerator-lattice.json','decision.json']
    names+=['action-%02d.json'%i for i in range(N)]
    copied={}
    for name in names:
        guard();raw=(OLD/name).read_bytes()
        need(size()+len(raw)+65536<CAP,'copy_byte_cap')
        with (D/name).open('xb') as f:f.write(raw)
        need(digest(D/name)==digest(OLD/name),'byte_identical_'+name)
        copied[name]=digest(D/name)
    save('copy-manifest.json',{'changes':[],'files':copied,'count':len(copied)})
    REPORT['phase']='fresh_complete_unchanged_replay'
    with (D/'verify.log').open('x') as log:
        vrun=subprocess.run([sys.executable,'-B',str(D/'verify.py')],stdout=log,
            stderr=subprocess.STDOUT,timeout=180-(time.monotonic()-START))
    need(vrun.returncode==0,'fresh_verifier_failed_no_retry')
    v=read(D/'verification-report.json')
    need(v['status']=='PASS' and not v['failures'] and v['input_product_slots']==110592
         and v['action_slots']==110592 and v['row_operations']==1735
         and v['frobenius_slots']==13824 and v['frobenius_iterates']==6
         and v['frobenius_rank']==1 and v['action_rank']==47
         and v['radical_dimension']==47 and v['action_kernel_dimension']==1
         and v['index']==2 and v['decision']=='NOT_2_MAXIMAL','full_replay_obligations')
    REPORT['replay']=v
    guard();REPORT['phase']='distinct_rank_certificates'
    ib=read(D/'input-basis.json');identity=ib['identity']
    r0=[1,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28,4,5,14]
    expected=[31,0]+[-r0[i//2] if i%2==0 else 0 for i in range(2,N)]
    need(identity==expected,'actual_identity_from_L078_displayed_basis')
    fc=read(D/'frobenius.json');F6=fc['iterates'][5]
    u=[[F6[i][0]] for i in range(N)];vrow=[E[0]]
    fact=mm(u,vrow)
    pivot=next((i for i in range(N) if u[i][0]),None)
    need(pivot is not None and F6[pivot][0]==1 and fact==F6,'entire_rank_one_factorization_and_minor')
    # The factorization and nonzero entry identify kernel exactly x_0=0.
    need(mod(mm(F6,tr(E[1:])))==[[0]*47 for _ in range(N)],'whole_frobenius_kernel')
    need([sum(F6[i][j]*identity[j] for j in range(N))%2 for i in range(N)]
         ==[x%2 for x in identity],'sixth_frobenius_fixes_actual_identity')
    save('frobenius-rank-one.json',{'matrix':F6,'column':u,'row':vrow,
         'full_product':fact,'nonzero_minor':[pivot,0,1],'kernel':E[1:],
         'factorization_slots':2304,'kernel_product_slots':2256})
    actions=[read(D/('action-%02d.json'%i)) for i in range(N)]
    stack=[[actions[i][k][j]%2 for i in range(N)] for j in range(N) for k in range(N)]
    need(stack==read(D/'action-kernel.json')['matrix'],'entire_reconstructed_stack')
    need(all(row[47]==0 for row in stack),'entire_nonzero_kernel_vector')
    # Fresh bit-vector independence selection on ORIGINAL rows, scanning backwards.
    # No original or replay elimination operations are used.
    basis={};selected=[]
    for ix in range(len(stack)-1,-1,-1):
        z=sum(stack[ix][j]<<j for j in range(47))
        while z:
            p=z.bit_length()-1
            if p in basis:z^=basis[p]
            else:
                basis[p]=z;selected.append(ix);break
        if len(selected)==47:break
    need(len(selected)==47,'fresh_47_original_independent_rows')
    minor=[stack[i][:47] for i in selected]
    inv=inverse_mod2(minor)
    kernel=E[47]
    result=mm(stack,tr([kernel]))
    need(result==[[0] for _ in stack],'full_action_kernel_product')
    save('action-minor.json',{'modulus':2,'matrix':stack,'selected_rows':selected,
         'selected_columns':list(range(47)),'minor':minor,'inverse':inv,
         'left_product':mod(mm(inv,minor)),'right_product':mod(mm(minor,inv)),
         'kernel':[kernel],'kernel_product':result,'minor_product_slots':4418,
         'stack_entries':110592,'kernel_product_slots':2304})
    guard();REPORT['phase']='independent_global_preimages_and_strict_witness'
    rad=lattice_check('radical-lattice',list(range(1,48)))
    num=lattice_check('numerator-lattice',[47])
    dc=read(D/'decision.json')
    mult=[[F(E[i][j],2 if i==47 else 1) for j in range(N)] for i in range(N)]
    inclusion=[[E[i][j]*(2 if i==47 else 1) for j in range(N)] for i in range(N)]
    need([[F(x) for x in r] for r in dc['M']]==mult and dc['inverse']==inclusion
         and dc['numerator']==num['basis'],'entire_multiplier_and_inclusion')
    need(mm(mult,inclusion)==mm(inclusion,mult)==E,'full_multiplier_inverse_products')
    need(dc['determinant_diagonal']==[1]*47+[2] and dc['determinant']==dc['index']==2,
         'independent_diagonal_index')
    need(dc['identity_in_multiplier']==[sum(inclusion[i][j]*identity[j] for j in range(N))
         for i in range(N)],'actual_identity_multiplier_coordinates')
    w=dc['strict_witness']
    need(w['column']==47 and w['numerator']==E[47] and E[47][47]%2==1,
         'strict_old_basis_nonmembership')
    need(all(type(x) is int for row in w['radical_action'] for x in row),'full_integer_witness')
    B=[[F(x,2) for x in row] for row in actions[47]]
    need(all(x.denominator==1 for row in B for x in row) and B==w['radical_action'],
         'all_2304_witness_action_slots')
    need(ib['scale']==31 and [F(ib['M'][i][47]) for i in range(N)]==E[47],
         'm47_equals_original_b47_scale_not_prime')
    save('independent-lattices-witness.json',{'radical':rad,'numerator':num,
         'multiplier':[[str(x) for x in row] for row in mult],'inclusion':inclusion,
         'actual_identity':identity,'index':2,'strict_witness':w,
         'witness_action_slots':2304,'original_scale':31,'testing_prime':2})
    REPORT.update(status='PASS',phase='complete',copied_files=len(copied),
         frobenius_rank=1,action_rank=47,radical_preimage='diag(2,1,...,1) Z^48',
         numerator_preimage='diag(2,...,2,1) Z^48',strict_witness='m47/2=b47/2',
         strict_witness_slots=2304,minor_product_slots=4418,
         decision='NOT_2_MAXIMAL',index=2,producer_contraction_bound=2304,
         producer_required_bound=2**63)
    guard()

try:main()
except Exception as e:REPORT.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
finally:
    if BEFORE:
        after={p:digest(ROOT/p) for p in BEFORE}
        save('audit-preservation.json',{'before':BEFORE,'after':after,'equal':after==BEFORE,'count':len(BEFORE)})
        if after!=BEFORE:REPORT['status']='STOP';REPORT['failures'].append('original_bytes_changed')
    REPORT.update(seconds=time.monotonic()-START,internal_limit=180,external_limit=181,
         byte_limit=CAP,bytes_before_report=size())
    if REPORT['seconds']>=180:REPORT['status']='STOP';REPORT['failures'].append('internal_time_cap')
    save('audit-report.json',REPORT)
    print(json.dumps({k:REPORT[k] for k in ('status','phase','seconds','bytes_before_report',
         'byte_limit','original_files','failures') if k in REPORT}))
sys.exit(0 if REPORT['status']=='PASS' else 1)
