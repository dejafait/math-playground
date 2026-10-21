"""One-shot exact source-lattice construction, no overorder iteration."""
from pathlib import Path
from fractions import Fraction as Q
import json, hashlib, signal, sys, time, math
sys.set_int_max_str_digits(0)
OUT=Path(__file__).resolve().parent; ROOT=OUT.parents[2]
START=time.monotonic(); CAP=134217728; N=48
REPORT={'status':'INCOMPLETE','phase':'inputs','product_slots':0,'failures':[]}
def need(ok,label):
 if not ok: raise ArithmeticError(label)
def save(name,obj):
 raw=(json.dumps(obj,separators=(',',':'))+'\n').encode()
 need(sum(p.stat().st_size for p in OUT.iterdir() if p.is_file())+len(raw)<=CAP,'byte_cap')
 with (OUT/name).open('xb') as f:f.write(raw)
def read(p):return json.loads((ROOT/p).read_text())
def inventory():
 files=[ROOT/'scripts/seven-torsion/certificate.json']
 for d in ('scripts/seven-torsion/nonmonic-order-283','scripts/residual-prime-289'):
  files.extend(p for p in (ROOT/d).iterdir() if p.is_file())
 return {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}
def hnf(gens,name):
 a=[v[:] for v in gens]; ops=[]; m=len(a)
 def swap(i,j):
  if i!=j:a[i],a[j]=a[j],a[i];ops.append(['s',i,j])
 def add(i,j,q):
  if q:
   a[i]=[x+q*y for x,y in zip(a[i],a[j])];ops.append(['a',i,j,q])
 for r,k in enumerate(range(47,-1,-1)):
  j=next((j for j in range(r,m) if a[j][k]),None)
  need(j is not None,'full_rank_'+name);swap(r,j)
  for i in range(r+1,m):
   while a[i][k]:
    q=a[i][k]//a[r][k];add(i,r,-q)
    if a[i][k]:swap(i,r)
  if a[r][k]<0:a[r]=[-x for x in a[r]];ops.append(['n',r])
  for i in range(r):add(i,r,-(a[i][k]//a[r][k]))
 for i in range(24):swap(i,47-i)
 need(all(not any(v) for v in a[48:]),'all_redundant_generators_zero_'+name)
 basis=a[:48]
 need(all(basis[i][i]>0 and not any(basis[i][i+1:]) for i in range(48)),'triangular_'+name)
 save(name+'.json',{'basis':basis,'operations':ops,'generator_count':m,'rank':48})
 return basis

def mm(a,b):
 cols=list(zip(*b));return [[sum((x*y for x,y in zip(row,col) if x and y),Q(0)) for col in cols] for row in a]
def strings(a):return [[str(x) for x in row] for row in a]
def main():
 before=inventory();save('input-hashes.json',before)
 b=read('scripts/seven-torsion/nonmonic-order-283/basis.json');old=read('scripts/seven-torsion/certificate.json')
 H=b['H'];basis=b['basis'];ded=read('scripts/residual-prime-289/dedekind.json')
 need(H==old['primitive_integer_factors'][0] and len(H)==49 and H[-1]==343,'original_H')
 need(b['source_sha256']==before['scripts/seven-torsion/certificate.json'],'original_hash')
 need(ded['G']==[24,0,1],'fixed_gcd')
 # Full degree-46 coefficient lift of Hbar/G, not a selected field factor.
 work=[x%31 for x in H];U=[0]*47
 for k in range(48,1,-1):
  q=work[k]%31;U[k-2]=q
  work[k]=(work[k]-q)%31;work[k-2]=(work[k-2]-24*q)%31
 need(not any(work) and U[-1]==2,'full_GU_equals_Hbar')
 save('source.json',{'prime':31,'G':[24,0,1],'U':U,'degree_U':46,'B_basis_diagonal':[343]+[1]*47,'power_chain':[[2,1,1],[4,2,2],[8,4,4],[16,8,8],[32,16,16],[40,32,8],[44,40,4],[46,44,2]]})
 def to_poly(v):
  return [sum(v[i]*basis[i][k] for i in range(k,48)) for k in range(48)]
 def product_poly(x,y):
  z=[0]*(len(x)+len(y)-1)
  for i,u in enumerate(x):
   if u:
    for j,v in enumerate(y):
     if v:z[i+j]+=u*v
  for k in range(len(z)-1,47,-1):
   q,r=divmod(z[k],343);need(r==0,'integer_field_reduction')
   if q:
    for j,v in enumerate(H):
     if v:z[k-48+j]-=q*v
  z=z[:48]+[0]*max(0,48-len(z));out=[0]*48
  for k in range(47,0,-1):
   q,r=divmod(z[k],343);need(r==0,'integer_order_coordinates');out[k]=q
   if q:
    for j in range(k+1):
     if basis[k][j]:z[j]-=q*basis[k][j]
  out[0]=z[0];return out
 I=[[int(i==j) for j in range(48)] for i in range(48)]
 B=[row[:] for row in I];B[0][0]=343;powers={1:B}
 for d,l,r in [[2,1,1],[4,2,2],[8,4,4],[16,8,8],[32,16,16],[40,32,8],[44,40,4],[46,44,2]]:
  REPORT['phase']='ideal_power_'+str(d)
  left=list(map(to_poly,powers[l]));right=list(map(to_poly,powers[r]))
  gens=[product_poly(x,y) for x in left for y in right]
  powers[d]=hnf(gens,'power-%02d'%d)
  REPORT['completed_power']=d
  print('completed exact ideal power',d,flush=True)
 REPORT['phase']='source_lattice'
 J=[product_poly(to_poly(v),U) for v in powers[46]]
 save('source-ideal.json',{'basis_B46_times_U':J})
 A=hnf([[31*x for x in row] for row in I]+J,'source-lattice')
 # Rows A are numerator vectors in the old order basis; matrix columns are A^t/31.
 M=[[Q(A[j][i],31) for j in range(48)] for i in range(48)]
 inv=[[Q(0) for j in range(48)] for i in range(48)]
 for j in range(48):
  for i in range(47,-1,-1):inv[i][j]=(Q(i==j)-sum(M[i][k]*inv[k][j] for k in range(i+1,48)))/M[i][i]
 need(mm(M,inv)==I and mm(inv,M)==I,'full_basis_inverse_both')
 need(all(x.denominator==1 for row in inv for x in row),'old_inclusion_integral')
 C=[[int(x) for x in row] for row in inv]
 determinant=math.prod(C[i][i] for i in range(48))
 need(abs(determinant)==961,'exact_index_961')
 toold=mm([[Q(x) for x in row] for row in b['basis_to_L067']],M)
 fromold=mm(inv,[[Q(x) for x in row] for row in b['L067_to_basis']])
 need(mm(toold,fromold)==I and mm(fromold,toold)==I,'L067_transports_both')
 save('basis.json',{'M':strings(M),'inverse':C,'to_L067':strings(toold),'from_L067':strings(fromold),'index':abs(determinant),'inclusion_diagonal':[C[i][i] for i in range(48)],'rank':48})
 REPORT.update(rank=48,index=abs(determinant),phase='new_products')
 polys=list(map(to_poly,A))
 for i in range(48):
  row=[]
  for j in range(48):
   v=product_poly(polys[i],polys[j]);w=[]
   for r in C:
    q,rem=divmod(sum(x*y for x,y in zip(r,v) if x and y),961)
    need(rem==0,'all_new_products_integral');w.append(q)
   row.append(w);REPORT['product_slots']+=48
  save('product-%02d.json'%i,row)
 need(inventory()==before,'all_original_hashes_preserved')
 REPORT.update(status='PASS',phase='complete',source_lattice_equal=True,original_files=len(before))

signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('internal_180_second_cap')))
signal.setitimer(signal.ITIMER_REAL,180)
try:main()
except Exception as e:REPORT.update(status='STOP',failure=type(e).__name__+': '+str(e));REPORT['failures'].append(REPORT['failure'])
finally:
 signal.setitimer(signal.ITIMER_REAL,0)
 REPORT.update(seconds=time.monotonic()-START,required_seconds=180,required_index=961,required_rank=48,required_product_slots=110592,byte_limit=CAP)
 if (OUT/'input-hashes.json').exists():
  try:REPORT['original_hashes_preserved']=inventory()==json.loads((OUT/'input-hashes.json').read_text())
  except Exception as e:REPORT['preservation_error']=str(e)
 save('producer-report.json',REPORT);print(json.dumps(REPORT))
sys.exit(0 if REPORT['status']=='PASS' else 1)
