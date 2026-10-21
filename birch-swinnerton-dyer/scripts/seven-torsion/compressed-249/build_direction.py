from fractions import Fraction as F
from pathlib import Path
import hashlib,json,signal,sys,time
R=Path(__file__).resolve().parent; U=R.parent
sys.path.insert(0,str(U))
import build_certificate as P
start=time.monotonic(); signal.alarm(180)
def enc(x):
    if isinstance(x,F):return str(x)
    if isinstance(x,list):return [enc(z) for z in x]
    if isinstance(x,dict):return {k:enc(v) for k,v in x.items()}
    return x
def save(name,c):
    s=json.dumps(enc(c),separators=(',',':'))+'\n'
    assert sum(p.stat().st_size for p in R.rglob('*') if p.is_file())+len(s.encode())<=128*1024*1024
    (R/name).write_text(s)
def mm(A,B):
    cols=list(zip(*B))
    return [[sum((z*w for z,w in zip(row,col) if z and w),F(0)) for col in cols] for row in A]
def read(M):return [[F(z) for z in row] for row in M]
manifest={str(p.relative_to(U)):hashlib.sha256(p.read_bytes()).hexdigest() for p in U.rglob('*') if p.is_file() and R not in p.parents and '__pycache__' not in p.parts}
save('original-manifest.json',manifest)
up=json.loads((U/'certificate.json').read_text()); act=json.loads((U/'scalar-actions-243/actions.json').read_text())
f=list(map(F,up['f']))
def red(v):return P.divmodq(v,f)[1]
def mul(v,w):return red(P.mul(v,w))
def fixed(v):return v+[F(0)]*(24-len(v))
z=[F(0)]
for i in [1,2,3]:
    assert not any(map(F,act['maps'][str(i)]['X'][1]))
    z=P.add(z,list(map(F,act['maps'][str(i)]['X'][0])))
powers=[[F(1)]]
for i in range(8):powers.append(mul(powers[-1],z))
cols=[]
for k in range(3):
    for j in range(8):cols.append(fixed(red([F(0)]*k+powers[j])))
M=list(map(list,zip(*cols))); N=P.inverse(M)
assert N is not None
assert mm(M,N)==mm(N,M)==[[F(i==j) for j in range(24)] for i in range(24)]
v=P.mv(N,fixed(powers[8])); assert not any(v[8:])
h=[-q for q in v[:8]]+[F(1)]
x3=[F(0)]*3+[F(1)]; cubic_v=P.mv(N,fixed(x3))
# U^3 = sum_{k<3,j<8} cubic_v[j+8*k] Z^j U^k.
cubic=[[-v for v in cubic_v[8*k:8*k+8]] for k in range(3)]+[[F(1)]]
A2=read(act['maps']['2']['B_action']);A4=read(act['maps']['4']['B_action'])
Re=[[(F(i==j)+A2[i][j]+A4[i][j])/3 for j in range(24)] for i in range(24)]
E=[row[:8] for row in M]; K=mm(N,Re)[:8]
assert mm(E,K)==Re and mm(K,E)==[[F(i==j) for j in range(8)] for i in range(8)]
EB=E+[[F(0)]*8 for _ in range(24)]
KB=[row+[F(0)]*24 for row in K]
RB=mm(EB,KB)
power=read(up['matrix']); inv=read(up['inverse'])
ET=mm(inv,EB); KT=mm(KB,power); RT=mm(ET,KT)
cert={'schema':'389-direction-v1','upstream_hash':hashlib.sha256((U/'certificate.json').read_bytes()).hexdigest(),
      'action_hash':hashlib.sha256((U/'scalar-actions-243/actions.json').read_bytes()).hexdigest(),
      'z':z,'h':h,'powers':powers,'mixed_basis_order':'Z^j X^k; j fastest, 0<=j<8, 0<=k<3',
      'mixed_matrix':M,'mixed_inverse':N,'cubic':cubic,'E_B':EB,'K_B':KB,'R_B':RB,'E_T':ET,'K_T':KT,'R_T':RT,
      'dimension':8,'cover_degree':6,'seconds':time.monotonic()-start}
save('direction.json',cert)
signal.alarm(0)
print(json.dumps({'status':'PRODUCED_UNVERIFIED','actual_dimension':8,'required_dimension':8,'mixed_rank':24,'required_rank':24,'seconds':cert['seconds'],'path':str(R/'direction.json')}))

