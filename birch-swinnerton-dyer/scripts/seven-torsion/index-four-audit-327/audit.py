"""Independent full rank/lattice supplement; no producer/verifier imports."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, subprocess, sys, time
sys.set_int_max_str_digits(0)
D = Path(__file__).resolve().parent
ROOT = D.parents[2]
OLD = D.parent/'index-two-order-two-325'
START = time.monotonic()
CAP = 134217728
N = 48
I = [[int(i==j) for j in range(N)] for i in range(N)]
report = {'status':'INCOMPLETE', 'phase':'initial_inventory', 'failures':[]}
def need(ok, label):
    if not ok: raise ArithmeticError(label)
def read(path):
    return json.loads(path.read_text())
def save(name, value):
    raw = (json.dumps(value, separators=(',', ':'))+'\n').encode()
    need(sum(p.stat().st_size for p in D.rglob('*') if p.is_file())+len(raw)+65536 < CAP, 'combined_byte_reserve')
    with (D/name).open('xb') as f: f.write(raw)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def tr(a): return [list(r) for r in zip(*a)]
def mm(a,b):
    cols = tr(b)
    return [[sum(x*y for x,y in zip(row,col) if x and y) for col in cols] for row in a]
def rat(a): return [[F(x) for x in r] for r in a]
def strings(a): return [[str(x) for x in r] for r in a]
def bits(row):
    need(all(type(x) is int and x in (0,1) for x in row), 'binary_entries')
    return sum(x<<j for j,x in enumerate(row))
def unpack(v,w): return [(v>>j)&1 for j in range(w)]
def bm(a,b):
    # Row-vector linear combinations, all coefficients represented exactly.
    width = len(b[0]); packed = [bits(row) for row in b]; out = []
    for row in a:
        need(len(row)==len(b), 'binary_product_shape')
        value = 0
        for j,x in enumerate(row):
            need(x in (0,1), 'binary_multiplier')
            if x: value ^= packed[j]
        out.append(unpack(value,width))
    return out
def rank(rows,width):
    piv = {}
    for row in rows:
        need(len(row)==width, 'rank_width')
        value = bits(row)
        while value:
            k = value.bit_length()-1
            if k in piv: value ^= piv[k]
            else:
                piv[k] = value; break
    return len(piv)
def spans(saved, own, width, label):
    # Both independent systems have the same full span, not just cardinality.
    need(rank(saved,width)==len(saved)==len(own)==rank(own,width), label+'_independent')
    need(rank(saved+own,width)==len(own), label+'_both_span_containments')
def inverse_binary(a):
    n = len(a)
    need(all(len(row)==n for row in a), 'square_binary_inverse')
    rows = [bits(row) | (1<<(n+i)) for i,row in enumerate(a)]
    for c in range(n):
        s = next((r for r in range(c,n) if (rows[r]>>c)&1), None)
        need(s is not None, 'independent_selected_rows_nonsingular')
        rows[c],rows[s] = rows[s],rows[c]
        for r in range(n):
            if r!=c and ((rows[r]>>c)&1): rows[r] ^= rows[c]
    need(all((row&((1<<n)-1))==(1<<i) for i,row in enumerate(rows)), 'inverse_all_terminal_entries')
    inv = [unpack(row>>n,n) for row in rows]
    identity = [[int(i==j) for j in range(n)] for i in range(n)]
    need(bm(a,inv)==identity and bm(inv,a)==identity, 'binary_inverse_both_products')
    return inv

def preimage(label, own_kernel, diag):
    cert = read(D/(label+'-lattice.json'))
    G = tr(own_kernel+[[2*x for x in row] for row in I])
    L = [[diag[i]*int(i==j) for j in range(N)] for i in range(N)]
    Linv = [[F(int(i==j),diag[i]) for j in range(N)] for i in range(N)]
    V = []
    for i in range(N):
        row = []
        for x in G[i]:
            q,r = divmod(x,diag[i]); need(r==0,label+'_all_G_in_L'); row.append(q)
        V.append(row)
    U = [[0]*N for _ in range(len(G[0]))]
    for j in range(N):
        target = [L[i][j] for i in range(N)]
        selected = next((k for k,col in enumerate(tr(G)) if col==target),None)
        need(selected is not None,label+'_all_L_in_G')
        U[selected][j] = 1
    need(mm(G,U)==L and mm(L,V)==G,label+'_two_sided_global_generation')
    need(mm(L,Linv)==I and mm(Linv,L)==I,label+'_both_independent_inverse_products')
    B = cert['basis']; BI = rat(cert['inverse'])
    forward = mm(Linv,B); reverse = mm(BI,L)
    need(all(x.denominator==1 for a in (forward,reverse) for row in a for x in row),label+'_saved_basis_both_integral_containments')
    need(mm(L,forward)==B and mm(B,reverse)==L,label+'_saved_basis_both_generation_identities')
    need(mm(forward,reverse)==I and mm(reverse,forward)==I,label+'_basis_comparison_inverse_products')
    need(B==L,label+'_displayed_basis')
    save(label+'-independent-preimage.json', {'kernel_rows':own_kernel,'generators':G,
        'basis':L,'G_to_basis':U,'basis_to_G':V,'inverse':strings(Linv),
        'saved_basis_in_displayed':strings(forward),'displayed_basis_in_saved':strings(reverse),
        'all_integer_containments':True})
    return L,Linv

def main():
    upstream = read(OLD/'input-hashes.json')
    need(len(upstream)==568,'full_568_input_inventory')
    paths = set(upstream)
    paths.update(str(p.relative_to(ROOT)) for p in OLD.iterdir() if p.is_file())
    paths.add('lemmas/L085-conductor389-index-two-order-not-2-maximal.md')
    paths.add('drafts/literature/2026-10-18-index-two-order-two-critical-audit.md')
    before = {name:sha(ROOT/name) for name in sorted(paths)}
    need(all(before[name]==value for name,value in upstream.items()),'unchanged_production_inputs')
    save('original-hashes.json',before)
    names = ['verify.py','input-hashes.json','input-basis.json','frobenius.json',
        'radical-lattice.json','action-kernel.json','numerator-lattice.json','decision.json']
    names += ['action-%02d.json'%i for i in range(N)]
    manifest = []
    for name in names:
        src = OLD/name; data = src.read_bytes()
        need(sum(p.stat().st_size for p in D.iterdir() if p.is_file())+len(data)+65536<CAP,'copy_byte_reserve')
        with (D/name).open('xb') as f: f.write(data)
        need(sha(D/name)==before[str(src.relative_to(ROOT))],'byte_unchanged_copy_'+name)
        manifest.append({'source':str(src.relative_to(ROOT)),'destination':name,'sha256':sha(D/name)})
    save('copy-manifest.json',manifest)
    report['phase']='fresh_complete_replay'
    with (D/'replay.log').open('x') as log:
        child = subprocess.run([sys.executable,'-B',str(D/'verify.py')],stdout=log,stderr=subprocess.STDOUT)
    need(child.returncode==0,'fresh_verifier_exit')
    replay = read(D/'verification-report.json')
    need(replay['status']=='PASS' and not replay['failures'],'fresh_verifier_report')
    required = {'input_product_slots':110592,'product_slots':110592,'product_identities':2304,
        'remainder_coefficients':218880,'action_slots':110592,'frobenius_slots':13824,
        'frobenius_iterates':6,'frobenius_rank':1,'radical_dimension':47,
        'action_rank':46,'action_kernel_dimension':2,'index':4,'identity_actions':96,
        'transport_entries':13824,'inverse_products':6,'original_files':568,'row_operations':1662}
    need(all(replay[k]==v for k,v in required.items()),'all_fresh_replay_obligation_counts')
    need(replay['decision']=='NOT_2_MAXIMAL','fresh_strict_verdict')

    report['phase']='independent_full_rank_certificates'
    fc = read(D/'frobenius.json'); A = fc['iterates'][5]
    need(len(A)==N and all(len(row)==N for row in A),'full_sixth_matrix')
    pivot = next((j for j in range(N) if any(A[i][j] for i in range(N))),None)
    need(pivot is not None,'frobenius_nonzero_column')
    c = [[A[i][pivot]] for i in range(N)]
    row_index = next(i for i in range(N) if c[i][0])
    coeff = [A[row_index][:]]
    need(c[row_index][0]==1 and bm(c,coeff)==A,'complete_frobenius_rank_one_factorization')
    need(coeff==[I[0]],'frobenius_displayed_kernel_equation')
    fk = I[1:]
    need(bm(A,tr(fk))==[[0]*47 for _ in range(N)],'entire_frobenius_kernel')
    spans(fc['elimination']['kernel'],fk,N,'frobenius_saved_kernel')
    save('frobenius-independent-rank.json',{'matrix':A,'column':c,'coefficient_row':coeff,
        'nonzero_row':row_index,'pivot_column':pivot,'kernel_rows':fk,'rank':1,
        'factorization_entries':2304})

    actions = [read(D/('action-%02d.json'%i)) for i in range(N)]
    stack = [[actions[i][k][j]%2 for i in range(N)] for j in range(N) for k in range(N)]
    ac = read(D/'action-kernel.json')
    need(stack==ac['matrix'],'independently_reassembled_entire_action_stack')
    C = [row[:46] for row in stack]
    selected = []; echelon = {}
    # Select independent rows using reverse-pivot XOR, no stored operations.
    for i,row in enumerate(C):
        value = bits(row)
        while value:
            k = value.bit_length()-1
            if k in echelon: value ^= echelon[k]
            else:
                echelon[k]=value; selected.append(i); break
        if len(selected)==46: break
    need(len(selected)==46,'independent_46_rows')
    square = [C[i] for i in selected]; inv = inverse_binary(square)
    left = [[0]*2304 for _ in range(46)]
    for i in range(46):
        for j,pos in enumerate(selected): left[i][pos]=inv[i][j]
    small_identity = [[int(i==j) for j in range(46)] for i in range(46)]
    need(bm(left,C)==small_identity,'full_46_by_2304_left_inverse')
    factor = bm(left,stack)
    need(bm(C,factor)==stack,'all_110592_action_factorization_entries')
    need(factor==[I[i] for i in range(46)],'complete_action_kernel_equations')
    ak = I[46:]
    need(bm(stack,tr(ak))==[[0,0] for _ in range(2304)],'entire_two_dimensional_kernel_containment')
    spans(ac['kernel'],ak,N,'action_saved_kernel')
    save('action-independent-rank.json',{'matrix':stack,'chosen_columns':list(range(46)),
        'columns':C,'selected_rows':selected,'selected_square_inverse':inv,
        'left_inverse':left,'factor':factor,'kernel_rows':ak,'rank':46,
        'factorization_entries':110592,'left_inverse_entries':2116})

    report['phase']='independent_complete_preimages_and_strictness'
    J,JI = preimage('radical',fk,[2]+[1]*47)
    Q,QI = preimage('numerator',ak,[2]*46+[1]*2)
    mult = [[F(x,2) for x in row] for row in Q]
    inclusion = [[2*x for x in row] for row in QI]
    need(all(x.denominator==1 for row in inclusion for x in row),'integer_full_order_inclusion')
    inclusion = [[int(x) for x in row] for row in inclusion]
    need(mm(mult,inclusion)==I and mm(inclusion,mult)==I,'independent_multiplier_inverse_products')
    expected = [[int(i==j)*(2 if i>=46 else 1) for j in range(N)] for i in range(N)]
    need(inclusion==expected,'all_diagonal_and_offdiagonal_inclusion_entries')
    det = math.prod(inclusion[i][i] for i in range(N))
    need(det==4,'independent_inclusion_determinant')
    dc = read(D/'decision.json'); ib = read(D/'input-basis.json'); u = ib['identity']
    need(rat(dc['M'])==mult and dc['inverse']==inclusion and dc['numerator']==Q,'entire_displayed_multiplier')
    need(dc['index']==dc['determinant']==det,'index_orientation')
    identity_poly = mm(tr(ib['scaled_polynomials']),tr([u]))
    need(identity_poly==[[62*int(i==0)] for i in range(N)],'actual_identity_in_original_power_basis')
    im = mm(inclusion,tr([u]))
    need(mm(mult,im)==tr([u]) and tr(im)[0]==dc['identity_in_multiplier'],'actual_identity_in_multiplier')
    table_row = read(D.parent/'index-two-table-321/product-46.json')
    # Reconstruct the complete witness action from the table and independent J.
    witness_action = [[F(x,2) for x in row] for row in mm(JI,mm(tr(table_row),J))]
    need(all(isinstance(x,F) and x.denominator==1 for row in witness_action for x in row),'strict_witness_all_integral_actions')
    witness_action = [[int(x) for x in row] for row in witness_action]
    need([[2*x for x in row] for row in witness_action]==actions[46],'entire_witness_matches_replayed_action')
    w = dc['strict_witness']
    need(w['numerator']==I[46] and w['column']==46 and w['radical_action']==witness_action,'complete_saved_strict_witness')
    need(F(1,2).denominator!=1 and mult[46][46]==F(1,2),'strict_old_lattice_nonmembership')
    save('independent-multiplier.json',{'basis':strings(mult),'inclusion':inclusion,
        'determinant':det,'index_orientation':'[S:R+] = |det(R+ basis in S)|',
        'actual_identity':u,'identity_in_multiplier':tr(im)[0],
        'strict_numerator':I[46],'strict_denominator':2,'full_radical_action':witness_action,
        'strict_action_entries':2304})

    report['phase']='final_preservation'
    after = {name:sha(ROOT/name) for name in sorted(paths)}
    need(after==before,'all_original_files_preserved')
    need(all(sha(D/x['destination'])==x['sha256'] for x in manifest),'all_fixed_copies_preserved')
    save('audit-preservation.json',{'before':before,'after':after,'equal':True,
        'original_files':len(before),'fixed_copies_preserved':len(manifest)})
    report.update(status='PASS',phase='complete',original_files=len(before),fixed_copies=len(manifest),
        replay_counts=required,frobenius_rank=1,action_rank=46,index=4,
        decision='NOT_2_MAXIMAL',independent_preimages=2,full_strict_action_entries=2304,
        frobenius_factorization_entries=2304,action_factorization_entries=110592,
        action_left_inverse_product_entries=2116)

try:
    main()
except Exception as exc:
    report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
finally:
    report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=CAP)
    save('audit-report.json',report)
    print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
