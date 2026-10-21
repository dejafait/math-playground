"""Independent full rank/lattice supplement; no producer/verifier imports."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, subprocess, sys, time
sys.set_int_max_str_digits(0)
D = Path(__file__).resolve().parent
ROOT = D.parents[2]
OLD = D.parent/'W-two-359'
START = time.monotonic()
CAP = 134217728
N = 48
I = [[int(i==j) for j in range(N)] for i in range(N)]
report = {'status':'INCOMPLETE', 'phase':'initial_inventory', 'failures':[]}
def need(ok, label):
    if not ok: raise ArithmeticError(label)
def read(path):
    if path.parent==D and (path.name in ['frobenius.json', 'radical-lattice.json', 'numerator-lattice.json', 'action-kernel.json', 'decision.json', 'input-basis.json'] or __import__('re').fullmatch(r'action-[0-9]{2}\.json',path.name)):
        path=path.with_name('test-'+path.name)
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

def full_rank(label, M, r, saved_kernel):
    height=len(M)
    need(height in (48,2304) and all(len(row)==48 for row in M),'full_matrix_shape_'+label)
    C=[row[:r] for row in M]
    selected=[]; echelon={}
    for i,row in enumerate(C):
        v=bits(row)
        while v:
            k=v.bit_length()-1
            if k in echelon:v^=echelon[k]
            else:
                echelon[k]=v;selected.append(i);break
        if len(selected)==r:break
    need(len(selected)==r,'selected_rows_full_rank_'+label)
    inv=inverse_binary([C[i] for i in selected])
    L=[[0]*height for _ in range(r)]
    for i in range(r):
        for j,pos in enumerate(selected):L[i][pos]=inv[i][j]
    B=bm(L,M)
    K=tr(I[r:]);P=I[r:]
    cert={'matrix':M,'columns':C,'factor':B,'left_inverse':L,
          'selected_rows':selected,'selected_inverse':inv,'rank':r,
          'kernel':K,'kernel_projection':P,'kernel_rows':I[r:]}
    save(label+'-full-rank.json',cert)
    got=read(D/(label+'-full-rank.json'))
    need(got==cert,'entire_certificate_round_trip_'+label)
    # Recheck every persisted shape, binary entry and load-bearing equation.
    shapes={'matrix':(height,48),'columns':(height,r),'factor':(r,48),
            'left_inverse':(r,height),'kernel':(48,48-r),
            'kernel_projection':(48-r,48),'kernel_rows':(48-r,48),
            'selected_inverse':(r,r)}
    for key,(h,w) in shapes.items():
        a=got[key]
        need(len(a)==h and all(len(row)==w for row in a),'persisted_shape_'+key)
        for row in a:bits(row)
    c,b,l,k,p=map(got.get,['columns','factor','left_inverse','kernel','kernel_projection'])
    need(got['matrix']==M and c==[row[:r] for row in M],'persisted_full_matrix_and_columns')
    need(bm(c,b)==M,'persisted_entire_upper_rank_factorization')
    need(bm(l,c)==[[int(i==j) for j in range(r)] for i in range(r)],'persisted_entire_left_inverse')
    need(b==I[:r] and got['rank']==r,'displayed_full_kernel_equations')
    need(bm(M,k)==[[0]*(48-r) for _ in range(height)],'persisted_entire_kernel_equations')
    need(bm(p,k)==[[int(i==j) for j in range(48-r)] for i in range(48-r)],'persisted_kernel_left_inverse')
    need(k==tr(got['kernel_rows']) and got['kernel_rows']==I[r:]
         and r+len(got['kernel_rows'])==48,'rank_nullity_and_displayed_full_kernel')
    spans(saved_kernel,got['kernel_rows'],48,label+'_saved_full_kernel')
    return got['kernel_rows']

def reread_preimage(label,kernel,diag):
    L,LI=preimage(label,kernel,diag)
    e=read(D/(label+'-independent-preimage.json'))
    G=tr(kernel+[[2*x for x in row] for row in I])
    need(e['kernel_rows']==kernel and e['generators']==G and e['basis']==L,'persisted_preimage_inputs_'+label)
    U=e['G_to_basis'];V=e['basis_to_G'];inv=rat(e['inverse'])
    for a,h,w in [(G,48,len(kernel)+48),(L,48,48),(U,len(kernel)+48,48),(V,48,len(kernel)+48)]:
        need(len(a)==h and all(len(row)==w for row in a),'persisted_integer_shape_'+label)
        need(all(type(x) is int for row in a for x in row),'persisted_integer_entries_'+label)
    need(mm(G,U)==L and mm(L,V)==G,'persisted_both_integer_generations_'+label)
    need(inv==LI and mm(L,inv)==I and mm(inv,L)==I,'persisted_both_preimage_inverses_'+label)
    saved=read(D/(label+'-lattice.json'));SB=saved['basis']
    forward=rat(e['saved_basis_in_displayed']);back=rat(e['displayed_basis_in_saved'])
    need(all(x.denominator==1 for a in (forward,back) for row in a for x in row),'persisted_both_integral_comparisons')
    need(mm(L,forward)==SB and mm(SB,back)==L and mm(forward,back)==I
         and mm(back,forward)==I,'persisted_both_saved_preimage_comparisons')
    return L,LI

def main():
    table=[read(D/('w-product-%02d.json'%i)) for i in range(48)]
    for row in table:
        need(len(row)==48 and all(len(v)==48 and all(type(x) is int for x in v) for v in row),'entire_validated_table')
    # Characteristic two in the commutative validated order: cross terms cancel.
    first=tr([[x%2 for x in table[i][i]] for i in range(48)])
    terminal=first
    for _ in range(5):terminal=bm(first,terminal)
    fc=read(D/'frobenius.json')
    need(terminal==fc['iterates'][5],'independent_terminal_frobenius_from_full_table')
    fk=full_rank('frobenius',terminal,1,fc['elimination']['kernel'])
    J,JI=reread_preimage('radical',fk,[2]+[1]*47)
    actions=[]
    for i in range(48):
        # Independent exact basis conversion, with both full coordinate identities.
        act=mm(JI,mm(tr(table[i]),J))
        need(all(F(x).denominator==1 for row in act for x in row),'independent_full_integral_action')
        act=[[int(x) for x in row] for row in act]
        need(mm(J,act)==mm(tr(table[i]),J) and act==read(D/('action-%02d.json'%i)),
             'independent_every_action_entry_'+str(i))
        actions.append(act)
    stack=[[actions[i][k][j]%2 for i in range(48)] for j in range(48) for k in range(48)]
    ac=read(D/'action-kernel.json')
    need(ac['matrix']==stack,'entire_independent_action_stack')
    ak=full_rank('action',stack,42,ac['kernel'])
    Q,QI=reread_preimage('numerator',ak,[2]*42+[1]*6)
    mult=[[F(x,2) for x in row] for row in Q]
    T=[[2*x for x in row] for row in QI]
    need(all(x.denominator==1 for row in T for x in row),'independent_integral_old_order_inclusion')
    T=[[int(x) for x in row] for row in T]
    need(T==[[int(i==j)*(2 if i>=42 else 1) for j in range(48)] for i in range(48)],'all_inclusion_entries')
    need(mm(mult,T)==I and mm(T,mult)==I,'independent_full_multiplier_inverse')
    det=math.prod(T[i][i] for i in range(48));need(det==64,'independent_index_thirty_two')
    dc=read(D/'decision.json');ib=read(D/'input-basis.json');u=ib['identity']
    need(rat(dc['M'])==mult and dc['inverse']==T and dc['numerator']==Q
         and dc['index']==dc['determinant']==det and dc['decision']=='NOT_2_MAXIMAL','entire_saved_multiplier')
    need(mm(tr(ib['scaled_polynomials']),tr([u]))==[[992*int(i==0)] for i in range(48)],'actual_unit_in_original_field')
    im=tr(mm(T,tr([u])))[0]
    need(im==dc['identity_in_multiplier'] and mm(mult,tr([im]))==tr([u]),'actual_unit_in_multiplier')
    witness=[[F(x,2) for x in row] for row in actions[42]]
    need(all(x.denominator==1 for row in witness for x in row),'all_strict_witness_actions_integral')
    witness=[[int(x) for x in row] for row in witness]
    w=dc['strict_witness']
    need(w['numerator']==I[42] and w['column']==42 and w['radical_action']==witness
         and mult[42][42]==F(1,2),'full_strict_witness_and_nonmembership')
    certificate={'basis':strings(mult),'numerator':Q,'inclusion':T,'determinant':det,
        'index_orientation':'[(I:I):W] = absolute determinant of W basis in (I:I)',
        'identity':u,'identity_in_multiplier':im,'strict_numerator':I[42],
        'strict_denominator':2,'strict_action':witness}
    save('independent-multiplier.json',certificate)
    e=read(D/'independent-multiplier.json');need(e==certificate,'whole_multiplier_round_trip')
    m=rat(e['basis']);t=e['inclusion']
    need(mm(m,t)==I and mm(t,m)==I and [[2*x for x in row] for row in m]==e['numerator'],
         'persisted_multiplier_inverse_and_N_over_two')
    need(t==T and e['determinant']==math.prod(t[i][i] for i in range(48))==64,'persisted_full_index_orientation')
    need(mm(m,tr([e['identity_in_multiplier']]))==tr([u]),'persisted_actual_identity')
    need(e['strict_numerator']==I[42] and e['strict_denominator']==2 and m[42][42]==F(1,2)
         and [[2*x for x in row] for row in e['strict_action']]==actions[42]
         and all(type(x) is int for row in e['strict_action'] for x in row),'persisted_strict_full_action')
    report.update(status='PASS',phase='complete',frobenius_rank=1,action_rank=42,index=64,
        radical_kernel_dimension=47,action_kernel_dimension=6,independent_preimages=2,
        action_entries=110592,frobenius_factorization_entries=2304,action_factorization_entries=110592,
        action_left_inverse_entries=96768,selected_inverse_entries=1764,full_strict_action_entries=2304,
        all_load_bearing_certificates_reread=True)
try:main()
except Exception as exc:report.update(status='STOP',failures=[type(exc).__name__+': '+str(exc)])
finally:
    report.update(seconds=time.monotonic()-START,required_seconds=180,required_bytes=CAP)
    save('independent-report.json',report);print(json.dumps(report))
sys.exit(0 if report['status']=='PASS' else 1)
