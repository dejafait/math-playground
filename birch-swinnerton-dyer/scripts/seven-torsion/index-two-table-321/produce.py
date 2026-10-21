"""One bounded production: rational basis transports and all structure constants."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, sys, time
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent
R=D.parents[2]; S=R/'scripts/seven-torsion'
START=time.monotonic(); CAP=134217728; N=48
U=[[int(i==j) for j in range(N)] for i in range(N)]
REPORT={'status':'INCOMPLETE','phase':'inputs','product_slots':0,'failures':[]}
def need(ok,label):
    if not ok: raise ArithmeticError(label)
def read(p): return json.loads(p.read_text())
def save(name,x):
    raw=(json.dumps(x,separators=(',',':'))+'\n').encode()
    need(sum(p.stat().st_size for p in D.iterdir() if p.is_file())+len(raw)+65536<=CAP,'artifact_cap')
    with (D/name).open('xb') as f: f.write(raw)
def mm(a,b):
    cols=list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col) if x and y) for col in cols] for row in a]
def rat(a): return [[F(x) for x in row] for row in a]
def strs(a): return [[str(x) for x in row] for row in a]
def tr(a): return [list(x) for x in zip(*a)]
def hashes():
    paths=[S/'certificate.json']
    for name in ('nonmonic-order-283','radical-overorder-295','radical-overorder-audit-297',
                 'changed-order-two-303','changed-order-two-audit-305'):
        paths.extend(p for p in (S/name).iterdir() if p.is_file())
    return {str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(paths)}
def main():
    before=hashes(); save('input-hashes.json',before)
    original=read(S/'certificate.json'); b=read(S/'nonmonic-order-283/basis.json')
    old=read(S/'radical-overorder-295/basis.json'); decision=read(S/'changed-order-two-303/decision.json')
    H=b['H']; need(len(H)==49 and H[-1]==343 and math.gcd(*H)==1,'primitive_H')
    need(H==original['primitive_integer_factors'][0] and [F(x,343) for x in H]==list(map(F,original['h'])),'H_equals_343h')
    bases=[U[0]]+[[H[48-i+j] if j<=i else 0 for j in range(N)] for i in range(1,N)]
    bp=tr(bases); pb=rat(b['power_to_basis'])
    need(b['basis']==bases and b['basis_to_power']==bp and mm(bp,pb)==U and mm(pb,bp)==U,'original_full_basis')
    to=rat(b['basis_to_L067']); fr=rat(b['L067_to_basis'])
    need(mm(rat(original['matrix']),bp)==to and mm(pb,rat(original['inverse']))==fr,'original_transports')
    M=rat(old['M']); C=rat(old['inverse'])
    need(mm(M,C)==U and mm(C,M)==U and [[31*x for x in row] for row in M]==old['numerator'],'old_basis')
    need(mm(to,M)==rat(old['to_L067']) and mm(C,fr)==rat(old['from_L067']),'old_transports')
    Q=[[int(i==j)*(1 if i==47 else 2) for j in range(N)] for i in range(N)]
    mult=[[F(x,2) for x in row] for row in Q]
    T=[[int(i==j)*(2 if i==47 else 1) for j in range(N)] for i in range(N)]
    need(decision['numerator']==Q and rat(decision['M'])==mult and decision['inverse']==T
         and decision['index']==2 and decision['decision']=='NOT_2_MAXIMAL','entire_L080_lattice')
    need(mm(mult,T)==U and mm(T,mult)==U,'multiplier_inverse')
    B=mm(M,mult); B_inv=mm(T,C)
    power=mm(bp,B); power_inv=mm(B_inv,pb)
    coord=mm(to,B); coord_inv=mm(B_inv,fr)
    for a,z in ((B,B_inv),(power,power_inv),(coord,coord_inv)):
        need(mm(a,z)==U and mm(z,a)==U,'full_two_way_transports')
    identity=[B_inv[i][0] for i in range(N)]
    need(all(x.denominator==1 for x in identity),'identity_integral')
    identity=list(map(int,identity))
    need(identity==decision['identity_in_multiplier'] and mm(B,tr([identity]))==tr([U[0]]),'actual_identity')
    scaled=[[62*power[i][j] for i in range(N)] for j in range(N)]
    need(all(x.denominator==1 for row in scaled for x in row),'scaled_polynomials_integral')
    scaled=[[int(x) for x in row] for row in scaled]
    save('basis.json',{'H':H,'scale':62,'original_scale':31,'enlargement_denominator':2,
         'basis_in_b':strs(B),'b_to_basis':strs(B_inv),'basis_to_power':strs(power),
         'power_to_basis':strs(power_inv),'to_L067':strs(coord),'from_L067':strs(coord_inv),
         'basis_in_m':strs(mult),'old_inclusion':T,'index':2,'identity':identity,
         'scaled_polynomials':scaled,'rank':48})
    REPORT['phase']='all_transported_products'; table=[]
    for i in range(N):
        source=read(S/'radical-overorder-295'/('product-%02d.json'%i))
        need(len(source)==N and all(len(v)==N and all(type(x) is int for x in v) for v in source),'full_old_table_shape')
        row=[]
        for j,v in enumerate(source):
            denominator=(2 if i==47 else 1)*(2 if j==47 else 1)
            actual=[]
            for k,x in enumerate(v):
                q,r=divmod(x*(2 if k==47 else 1),denominator)
                need(r==0,'nonintegral_product_'+str((i,j,k)))
                actual.append(q); REPORT['product_slots']+=1
            row.append(actual)
        save('product-%02d.json'%i,row); table.append(row)
    for i in range(N):
        need([sum(identity[j]*table[j][i][k] for j in range(N)) for k in range(N)]==U[i],'left_identity')
        need([sum(identity[j]*table[i][j][k] for j in range(N)) for k in range(N)]==U[i],'right_identity')
    after=hashes(); need(after==before,'originals_preserved')
    save('preservation-producer.json',{'equal':True,'original_files':len(before),'after':after})
    REPORT.update(status='PASS',phase='complete',basis_elements=48,transport_matrices=6,
                  inverse_pairs=3,identity_actions=96,index=2,original_files=len(before))
try: main()
except Exception as e: REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e),failures=[str(e)])
finally:
    REPORT.update(seconds=time.monotonic()-START,required_product_slots=110592,stage_limit_seconds=180,artifact_limit_bytes=CAP)
    save('producer-report.json',REPORT); print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
