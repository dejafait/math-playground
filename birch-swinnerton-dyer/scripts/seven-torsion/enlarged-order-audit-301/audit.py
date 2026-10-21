"""One bounded audit: unchanged replay plus full inverse/left-inverse checks.
No producer imports, no new order, no prime search, no stopped power inputs.
"""
from pathlib import Path
import hashlib, json, subprocess, sys, time
D=Path(__file__).resolve().parent
ROOT=D.parents[2]
OLD=D.parent/'enlarged-order-test-299'
START=time.monotonic()
CAP=134217728
N=48
P=31
E=[[int(i==j) for j in range(N)] for i in range(N)]
REPORT={'status':'STOP','phase':'inputs','failures':[]}
BEFORE={}
sys.set_int_max_str_digits(0)

def need(ok,label):
    if not ok:raise ArithmeticError(label)

def size():return sum(p.stat().st_size for p in D.iterdir() if p.is_file())

def guard():
    need(time.monotonic()-START<180,'aggregate_internal_180_second_cap')
    need(size()+65536<CAP,'aggregate_byte_cap')

def save(name,value):
    raw=(json.dumps(value,separators=(',',':'))+'\n').encode()
    need(size()+len(raw)+65536<CAP,'aggregate_write_byte_cap')
    with (D/name).open('xb') as f:f.write(raw)

def read(path):return json.loads(path.read_text())

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def mm(a,b):
    """Exact integer product; checks all output slots, omitting zero summands only."""
    need(bool(b) and all(len(row)==len(b) for row in a),'product_inner_shapes')
    w=len(b[0]);need(all(len(row)==w for row in b),'product_right_shape')
    out=[[0]*w for _ in a]
    for i,row in enumerate(a):
        for j,x in enumerate(row):
            if x:
                for k,y in enumerate(b[j]):
                    if y:out[i][k]+=x*y
    return [[x%P for x in row] for row in out]

def square_inverse(a):
    # Fresh reverse-column Gauss--Jordan, without the saved row-operation data.
    work=[[x%P for x in row]+e[:] for row,e in zip(a,E)]
    selected=[]
    for c in range(N-1,-1,-1):
        pivot=next((r for r in range(c,-1,-1) if work[r][c]),None)
        need(pivot is not None,'fresh_inverse_nonzero_pivot')
        selected.append({'column':c,'row':pivot,'value':work[pivot][c]})
        work[c],work[pivot]=work[pivot],work[c]
        q=pow(work[c][c],-1,P)
        work[c]=[x*q%P for x in work[c]]
        for r in range(N):
            if r!=c:
                q=work[r][c]
                if q:work[r]=[(x-q*y)%P for x,y in zip(work[r],work[c])]
    need([row[:N] for row in work]==E,'fresh_inverse_terminal_identity')
    return [row[N:] for row in work],selected

def main():
    global BEFORE
    upstream=read(OLD/'input-hashes.json')
    need(len(upstream)==294,'full_294_input_inventory')
    BEFORE={p:digest(ROOT/p) for p in upstream}
    need(BEFORE==upstream,'unchanged_original_upstream_inventory')
    original_files=sorted(p for p in OLD.iterdir() if p.is_file())
    for f in original_files:BEFORE[str(f.relative_to(ROOT))]=digest(f)
    need(len(original_files)==70 and len(BEFORE)==364,'complete_original_step299_inventory')
    save('original-hashes.json',BEFORE)
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
    save('copy-manifest.json',{'changes':[], 'files':copied,'count':len(copied),
        'note':'Same sibling depth; unchanged verifier arithmetic and input paths; only copied output directory is fresh.'})
    REPORT['phase']='fresh_full_unchanged_replay'
    with (D/'verify.log').open('x') as log:
        replay=subprocess.run([sys.executable,'-B',str(D/'verify.py')],
            stdout=log,stderr=subprocess.STDOUT,timeout=180-(time.monotonic()-START))
    need(replay.returncode==0,'fresh_replay_failed_no_retry')
    v=read(D/'verification-report.json')
    need(v['status']=='PASS' and not v['failures'] and v['input_product_slots']==110592
        and v['action_slots']==110592 and v['row_operations']==54651
        and v['frobenius_rank']==v['action_rank']==48
        and v['radical_dimension']==v['action_kernel_dimension']==0
        and v['index']==1 and v['decision']=='31_MAXIMAL','all_complete_replay_counts_and_decision')
    REPORT['replay']=v
    guard();REPORT['phase']='independent_full_inverse_certificates'
    ib=read(D/'input-basis.json');identity=ib['identity']
    need(len(identity)==48 and all(type(x) is int for x in identity),'actual_integer_identity_shape')
    # Explicit specialization of L078's displayed basis, independent of copied identity.
    r0=[1,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28,4,5,14]
    expected=[31,0]+[-r0[i//2] if i%2==0 else 0 for i in range(2,N)]
    need(identity==expected,'actual_identity_from_displayed_L078_basis')
    for name in ('radical-lattice','numerator-lattice'):
        c=read(D/(name+'.json'))
        full31=[[31*x for x in row] for row in E]
        need(c['basis']==c['S']==full31 and c['C']==c['D']==E
             and c['kernel_reduction']['matrix']==[] and c['kernel_reduction']['kernel']==E,
             name+'_entire_empty_kernel_lattice_coefficients')
    f=read(D/'frobenius.json')
    F2=f['second']
    inv,steps=square_inverse(F2)
    left=mm(inv,F2);right=mm(F2,inv)
    need(left==right==E,'both_full_inverse_products')
    im=[sum(F2[i][j]*identity[j] for j in range(N))%31 for i in range(N)]
    need(im==[x%31 for x in identity],'frobenius_squared_actual_identity_fixed')
    save('frobenius-inverse.json',{'modulus':P,'matrix':F2,'inverse':inv,
        'left_product':left,'right_product':right,'reverse_column_pivots':steps,
        'actual_identity':identity,'identity_image':im,'checked_product_slots':4608})
    actions=[read(D/('action-%02d.json'%i)) for i in range(N)]
    stack=[[actions[i][k][j]%P for i in range(N)] for j in range(N) for k in range(N)]
    need(stack==read(D/'action-kernel.json')['matrix'],'independently_reconstructed_entire_action_stack')
    # Evaluation at 31*1 in J=31I coordinates. L[k,(j,l)]=delta_kl*identity[j].
    L=[[identity[j]%P if k==l else 0 for j in range(N) for l in range(N)] for k in range(N)]
    result=mm(L,stack)
    need(result==E,'entire_left_inverse_product')
    unit_action=[[sum(identity[i]*actions[i][k][j] for i in range(N))%P
                  for j in range(N)] for k in range(N)]
    need(unit_action==E,'actual_identity_acts_on_entire_radical_quotient')
    save('action-left-inverse.json',{'modulus':P,'action_matrix':stack,'left_inverse':L,
        'full_product':result,'actual_identity':identity,'identity_action':unit_action,
        'checked_product_slots':2304,'checked_action_entries':110592,
        'evaluation_vector_in_J_basis':identity,'left_inverse_shape':[48,2304]})
    residues=[x%31 for i in range(N) for row in read(ROOT/('scripts/seven-torsion/radical-overorder-295/product-%02d.json'%i)) for x in row]
    need(len(residues)==110592 and min(residues)>=0 and max(residues)<=30,'all_residue_ranges')
    bound=48**2*30**3
    need(bound==62208000 and bound<2**63,'producer_int64_bound')
    dc=read(D/'decision.json')
    need(dc['index']==1 and dc['M']==[[str(x) for x in row] for row in E]
         and dc['inverse']==dc['equality_forward']==dc['equality_reverse']==E,
         'all_equality_and_multiplier_coefficients')
    REPORT.update(status='PASS',phase='complete',copied_files=len(copied),
        original_files=len(BEFORE),frobenius_inverse_product_slots=4608,
        action_left_inverse_product_slots=2304,action_entries=110592,
        actual_identity=identity,radical_preimage='31R',numerator_preimage='31R',
        decision='31_MAXIMAL',index=1,producer_contraction_bound=bound,
        producer_required_bound=2**63,residue_range=[min(residues),max(residues)])
    guard()

try:main()
except Exception as e:REPORT.update(status='STOP',failures=[type(e).__name__+': '+str(e)])
finally:
    if BEFORE:
        after={p:digest(ROOT/p) for p in BEFORE}
        preserved=after==BEFORE
        save('audit-preservation.json',{'before':BEFORE,'after':after,'equal':preserved,'count':len(BEFORE)})
        if not preserved:REPORT['status']='STOP';REPORT['failures'].append('original_bytes_changed')
    REPORT.update(seconds=time.monotonic()-START,internal_limit=180,external_limit=181,
                  byte_limit=CAP,bytes_before_report=size())
    if REPORT['seconds']>=180:REPORT['status']='STOP';REPORT['failures'].append('internal_time_cap')
    save('audit-report.json',REPORT)
    print(json.dumps({k:REPORT[k] for k in ('status','phase','seconds','bytes_before_report','byte_limit','original_files','failures') if k in REPORT}))
sys.exit(0 if REPORT['status']=='PASS' else 1)
