"""Independent complete replay using sparse polynomial dictionaries.
Imports no producer. Reconstructs full generators and replays unimodular
operations, with both integral generation directions explicitly checked.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib,signal,sys,time,math
sys.set_int_max_str_digits(0)
D=Path(__file__).resolve().parent;ROOT=D.parents[2];START=time.monotonic();N=48
R={'status':'INCOMPLETE','phase':'inputs','product_slots':0,'old_product_slots':0,'ideal_product_slots':0,'failures':[]}
def check(x,label):
 if not x:raise ValueError(label)
def load(p):return json.loads(p.read_text())
def save(p,x):
 raw=(json.dumps(x,separators=(',',':'))+'\n').encode()
 check(sum(f.stat().st_size for f in D.iterdir() if f.is_file())+len(raw)<=134217728,'combined_output_cap')
 with (D/p).open('xb') as f:f.write(raw)
def hashes():
 return {p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in load(D/'input-hashes.json')}
def matrix(a):return [[F(x) for x in row] for row in a]
def mulmat(a,b):
 z=[[F(0) for _ in range(len(b[0]))] for _ in a]
 for i,row in enumerate(a):
  for k,x in enumerate(row):
   if x:
    for j,y in enumerate(b[k]):
     if y:z[i][j]+=x*y
 return z
def replay(gens,e,name):
 check(e['generator_count']==len(gens) and e['rank']==48,'generator_shape_'+name)
 a=[x[:] for x in gens]
 for op in e['operations']:
  kind=op[0];i=op[1];check(type(i) is int and 0<=i<len(a),'op_index')
  if kind=='s':
   j=op[2];check(0<=j<len(a) and i!=j,'swap_indices');a[i],a[j]=a[j],a[i]
  elif kind=='a':
   j,c=op[2:];check(0<=j<len(a) and i!=j and type(c) is int,'add_indices_integer')
   for k in range(48):a[i][k]+=c*a[j][k]
  elif kind=='n':a[i]=[-x for x in a[i]]
  else:raise ValueError('unknown_operation')
 check(a[:48]==e['basis'] and not any(x for row in a[48:] for x in row),'complete_reduction_'+name)
 check(all(len(row)==48 and row[i]>0 and not any(row[i+1:]) for i,row in enumerate(e['basis'])),'triangular_basis_'+name)
 # Reverse every operation as an explicit generation witness back to all inputs.
 for op in reversed(e['operations']):
  kind=op[0];i=op[1]
  if kind=='s':j=op[2];a[i],a[j]=a[j],a[i]
  elif kind=='n':a[i]=[-x for x in a[i]]
  else:
   j,c=op[2:]
   for k in range(48):a[i][k]-=c*a[j][k]
 check(a==gens,'reverse_full_integral_generation_'+name)
 R['reversible_operations']=R.get('reversible_operations',0)+len(e['operations'])
 return e['basis']
def main():
 before=load(D/'input-hashes.json');check(hashes()==before,'all_original_inputs_match')
 orig=load(ROOT/'scripts/seven-torsion/certificate.json');b=load(ROOT/'scripts/seven-torsion/nonmonic-order-283/basis.json');s=load(D/'source.json')
 H=b['H'];check(len(H)==49 and H[-1]==343 and H==orig['primitive_integer_factors'][0],'full_primitive_H')
 check([F(v,343) for v in H]==list(map(F,orig['h'])) and math.gcd(*H)==1,'original_h_content')
 expected=[[1]+[0]*47]+[[H[48-i+k] if k<=i else 0 for k in range(48)] for i in range(1,48)]
 check(b['basis']==expected,'every_original_basis_polynomial')
 bp=list(map(list,zip(*expected)));pb=matrix(b['power_to_basis']);I=[[int(i==j) for j in range(48)] for i in range(48)]
 check(b['basis_to_power']==bp and mulmat(bp,pb)==I and mulmat(pb,bp)==I,'original_basis_both_inverses')
 check(mulmat(matrix(orig['matrix']),bp)==matrix(b['basis_to_L067']) and mulmat(pb,matrix(orig['inverse']))==matrix(b['L067_to_basis']),'both_original_transports')
 U=s['U'];check(s['prime']==31 and s['G']==[24,0,1] and s['degree_U']==46 and len(U)==47 and U[-1]==2,'full_homogeneous_degrees_top_unit')
 check(s['B_basis_diagonal']==[343]+[1]*47,'original_denominator_ideal')
 for k in range(49):check(((U[k] if k<47 else 0)*24+(U[k-2] if k>=2 else 0)-H[k])%31==0,'all_GU_coefficients')
 check(load(ROOT/'scripts/residual-prime-289/dedekind.json')['G']==s['G'],'audited_gcd')
 hp={i:c for i,c in enumerate(H) if c};base=[{i:c for i,c in enumerate(row) if c} for row in expected]
 def poly(v):
  z={}
  for i,c in enumerate(v):
   if c:
    for k,x in base[i].items():z[k]=z.get(k,0)+c*x
  return {k:x for k,x in z.items() if x}
 def multiply(x,y):
  z={}
  for i,c in x.items():
   for j,d in y.items():z[i+j]=z.get(i+j,0)+c*d
  return z
 def reduce(z):
  z=z.copy()
  for k in range(max(z,default=0),47,-1):
   if z.get(k,0):
    q,r=divmod(z[k],343);check(r==0,'sparse_exact_H_division')
    for j,c in hp.items():z[k-48+j]=z.get(k-48+j,0)-q*c
  return {k:c for k,c in z.items() if c}
 def coords(z):
  z=reduce(z);v=[0]*48
  for k in range(47,0,-1):
   q,r=divmod(z.get(k,0),343);check(r==0,'sparse_exact_basis_division');v[k]=q
   if q:
    for j,c in base[k].items():z[j]=z.get(j,0)-q*c
  v[0]=z.get(0,0);check(all(not c for k,c in z.items() if k),'no_remaining_coordinate');return v
 # Retain all original product slots as complete independently checked input.
 R['phase']='original_products'
 for i in range(48):
  rows=load(ROOT/('scripts/seven-torsion/nonmonic-order-283/product-%02d.json'%i))
  check(len(rows)==48 and all(len(v)==48 for v in rows),'old_full_shape')
  for j,v in enumerate(rows):
   check(all(type(c) is int for c in v),'old_integer_slots')
   check(reduce(multiply(base[i],base[j]))==poly(v),'every_old_product_identity')
   R['old_product_slots']+=48
 B=[row[:] for row in I];B[0][0]=343;powers={1:B}
 chain=[[2,1,1],[4,2,2],[8,4,4],[16,8,8],[32,16,16],[40,32,8],[44,40,4],[46,44,2]]
 check(s['power_chain']==chain,'fixed_chain')
 for d,l,r in chain:
  R['phase']='independent_ideal_power_'+str(d)
  left=[poly(v) for v in powers[l]];right=[poly(v) for v in powers[r]]
  gens=[]
  for x in left:
   for y in right:gens.append(coords(multiply(x,y)));R['ideal_product_slots']+=48
  powers[d]=replay(gens,load(D/('power-%02d.json'%d)),str(d))
  R['completed_power']=d
  print('independently replayed exact ideal power',d,flush=True)
 R['phase']='source_lattice_equality'
 up={i:c for i,c in enumerate(U) if c}
 J=[coords(multiply(poly(v),up)) for v in powers[46]]
 check(load(D/'source-ideal.json')['basis_B46_times_U']==J,'all_source_ideal_generators')
 A=replay([[31*x for x in row] for row in I]+J,load(D/'source-lattice.json'),'source_lattice')
 certificate=load(D/'basis.json');M=matrix(certificate['M']);C=certificate['inverse']
 check(M==[[F(A[j][i],31) for j in range(48)] for i in range(48)],'exact_source_lattice_basis')
 check(all(x.denominator==1 for row in M for x in [31*y for y in row]),'31M_integral')
 check(len(C)==48 and all(len(row)==48 and all(type(x) is int for x in row) for row in C),'full_integral_old_inclusion')
 check(mulmat(M,C)==I and mulmat(C,M)==I,'both_new_basis_inverse_identities')
 check(all(not C[i][j] for i in range(48) for j in range(i)),'inclusion_upper_triangular')
 diagonal=[C[i][i] for i in range(48)];index=abs(math.prod(diagonal))
 check(index==961 and certificate['index']==index and certificate['inclusion_diagonal']==diagonal,'full_exact_triangular_determinant')
 check(certificate['rank']==48 and all(M[i][i] for i in range(48)),'rank48_and_strict_inclusion')
 # Columns of C put every old basis vector (including 1) in the new lattice.
 check(mulmat(M,C)==I,'all_old_vectors_and_identity_in_new_lattice')
 toold=matrix(certificate['to_L067']);fromold=matrix(certificate['from_L067'])
 check(mulmat(matrix(b['basis_to_L067']),M)==toold and mulmat(C,matrix(b['L067_to_basis']))==fromold,'both_full_L067_transports')
 check(mulmat(toold,fromold)==I and mulmat(fromold,toold)==I,'both_full_L067_inverse_identities')
 R.update(rank=48,index=index,source_lattice_equal=True,phase='every_new_product')
 np=[poly(row) for row in A]
 for i in range(48):
  rows=load(D/('product-%02d.json'%i));check(len(rows)==48 and all(len(v)==48 for v in rows),'new_product_all_slots_shape')
  for j,v in enumerate(rows):
   check(all(type(x) is int for x in v),'new_product_integral_slots')
   # Numerator identity: Ni*Nj = 31 sum_k c_ijk Nk modulo the entire H.
   z=multiply(np[i],np[j])
   for k,c in enumerate(v):
    if c:
     for degree,x in np[k].items():z[degree]=z.get(degree,0)-31*c*x
   check(not reduce(z),'complete_new_product_polynomial_identity_'+str((i,j)))
   R['product_slots']+=48
 check(hashes()==before,'all_original_hashes_preserved')
 R.update(status='PASS',phase='complete',original_files=len(before),original_hashes_preserved=True)
signal.signal(signal.SIGALRM,lambda *_:(_ for _ in ()).throw(TimeoutError('internal_180_second_cap')))
signal.setitimer(signal.ITIMER_REAL,180)
try:main()
except Exception as e:R.update(status='STOP',failure=type(e).__name__+': '+str(e));R['failures'].append(R['failure'])
finally:
 signal.setitimer(signal.ITIMER_REAL,0)
 R.update(seconds=time.monotonic()-START,required_seconds=180,required_rank=48,required_index=961,required_product_slots=110592,required_old_product_slots=110592,required_ideal_product_slots=884736,byte_limit=134217728)
 try:R['original_hashes_preserved']=hashes()==load(D/'input-hashes.json')
 except Exception as e:R['preservation_error']=str(e)
 save('verification-report.json',R);print(json.dumps(R))
sys.exit(0 if R['status']=='PASS' else 1)
