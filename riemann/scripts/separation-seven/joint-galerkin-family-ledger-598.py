#!/usr/bin/env python3
"""Check the failed joint lower-enclosure ledger; no exact target sign claim."""
import hashlib,json,importlib.util
from pathlib import Path
from decimal import Decimal
import numpy as np
P=Path(__file__).resolve().parent
s=importlib.util.spec_from_file_location('intervals598',P/'complete-schur-531.py');v=importlib.util.module_from_spec(s);s.loader.exec_module(v);I=v.I
fail=[];checks=[]
def ck(ok,why):
    checks.append(dict(check=why,passed=bool(ok)))
    if not ok:fail.append(why)
def nf(a):return I(Decimal(float(np.linalg.norm(a))))*I('1.00000001')+I('1e-290')
def gam(n):return I(n)/(I(2**53)-I(n))
def hi(x):return float(x.hi)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((P/'joint-galerkin-family-certificate-598.json').read_text());q=np.load(P/'joint-galerkin-family-certificate-598.npz')
ck(c['script_sha256']==sha(P/'joint-galerkin-family-certificate-598.py'),'executed source hash')
ck(c['archive']['sha256']==sha(P/'joint-galerkin-family-certificate-598.npz'),'full archive hash')
ck(c['failures']==['quarter_comparison factor unavailable'],'exactly the final legacy-named factor failed')
ck(all(x['passed'] or x['label']=='quarter_comparison factor unavailable' for x in c['checks']),'all other original checks pass')
for name,h in c['input_hashes'].items():ck(sha(P/name)==h,'input preserved '+name)
Z,Y,G,A,B=[q[n] for n in ('Z','Y','G','A','B')]
with np.load(P/'original-galerkin-586.npz') as t:M,T,Ts,U=[t[n] for n in ('local_matrix','t_entries','ts_entries','u_entries')]
E=2044;F=1022
ck(Z.shape==(1024,F) and Y.shape==(F,E),'full family dimensions')
ck(np.array_equal(q['ZT'],Z),'one entire endpoint Z at both orientations')
AA=Z.T@M@Z;BB=Z.T@np.hstack((T@Z,Ts@Z))
EE=np.block([[Z.T@M@Z,-Z.T@U.T@Z],[-Z.T@U@Z,Z.T@M@Z]])-BB.T@Y-Y.T@BB+Y.T@AA@Y
for name,a,b in [('A',A,AA),('B',B,BB),('G',G,Z@Y),('trial',q['trial'],EE)]:ck(nf(a-b).hi<Decimal('1e-9'),'full rebuild '+name)
for name,a,cap in [('Z',Z,32),('Y',Y,16),('G',G,16),('A',A,200),('B',B,100),('M',M,1000),('T',T,100),('Ts',Ts,100),('U',U,100),('boundary',q['tail_boundary'],100),('head_rhs',q['head_residual'],1),('head_solution',q['head_solution'],1)]:ck(nf(a).hi<cap,'magnitude '+name)
# Same dot-product/Frobenius bounds as audit596, with every enlarged dimension.
budgets={
'A':gam(4096)*32**2*1000+I('1e-9'),
'B':2*gam(4096)*32**2*100+I('1e-9'),
'U':gam(4096)*32**2*100+I('1e-9'),
'energy':20*gam(4096)*(32**2*1000+100*16+200*16**2)+I('1e-7'),
'row_maps':gam(2048)*(2*257*32+1921*16)+I('1e-8'),
'boundary':gam(4096)*100**2+I('1e-7'),
'head_product_nuclear':I(E).sqrt()*gam(1024)+I('1e-8'),
'finite_gram_trace':gam(65536)*4+gam(E*E)*10+gam(4096)*I(E).sqrt()*4+I('1e-5')+I('1e-6'),
'H_assembly':gam(16)*401+I('1e-10')}
limits={'A':'1e-6','B':'2e-6','U':'1e-6','energy':'4e-5','row_maps':'1e-6','boundary':'1e-5','head_product_nuclear':'1e-6','finite_gram_trace':'1e-4','H_assembly':'1e-8'}
for n,a in budgets.items():ck(a.hi<Decimal(limits[n]),'paid arithmetic '+n)
ck(gam(65536*1024+10).hi<Decimal('1e-8'),'full radius arithmetic inflation')
ck(gam(E*E+10).hi<Decimal('1e-8'),'joint norm arithmetic inflation')
factors={}
for name,target in [('galerkin_floor',A-.77*np.eye(F)),('predictor_norm',1.4**2*np.eye(F)-Y@Y.T),('local_operator_norm',100*np.eye(F)-(M@Z).T@(M@Z))]:
    f=q['factor_'+name];r=nf(target-f@f.T);err=r+gam(4096)*100000+I('2e-7')
    ck(nf(f).hi**2<100000,'factor cap '+name);ck(err.hi<Decimal('1e-6'),'full factor reconstruction '+name)
    factors[name]=dict(reconstruction_error=err.json(),required='1e-6')
ck((I('1.400001')*I('1.400001')-I('1.4')*I('1.4')-I('1e-6')).lo>(gam(4096)*16**2+I('1e-9')).hi,'predictor inflation pays Gram')
ck((I('10.000001')*I('10.000001')-100-I('1e-6')).lo>(gam(4096)*100000+I('1e-8')).hi,'LZ inflation pays Gram')
blocks=c['ledger']['row_blocks']
ck(len(blocks)==126 and all(b['first']==1024+512*j and b['last']==1535+512*j for j,b in enumerate(blocks)),'every finite higher row partition')
# A direction only for the saved LOWER certificate, not for the actual F.
low=q['comparison_lower'];values,vectors=np.linalg.eigh(low);x=vectors[:,0]
a=float(x@(low@x));err=gam(4096)*nf(low)*nf(x)*nf(x)+I('1e-8')
upper=I(Decimal(a))+I(-err.hi,err.hi)
ck(upper.hi<Decimal('-.15'),'lower certificate itself has a negative direction; no target violation inferred')
p=P/'joint-galerkin-family-lower-direction-598.npz';np.savez_compressed(p,free_direction=x)
report=dict(result='LOWER_ENCLOSURE_INCONCLUSIVE' if not fail else 'LEDGER_INCOMPLETE',failures=fail,checks=checks,arithmetic={n:dict(actual_upper=a.json(),required=limits[n]) for n,a in budgets.items()},factor_checks=factors,saved_lower_certificate_rayleigh=upper.json(),direction_archive_sha256=sha(p),certificate_sha256=sha(P/'joint-galerkin-family-certificate-598.json'),script_sha256=sha(Path(__file__)),qualification='No exact target sign certified; final factor failure retained; this is not a separate conceptual audit of analytic assumptions.')
out=P/'joint-galerkin-family-ledger-598.json';out.write_text(json.dumps(report,indent=2)+'\n')
print('Result',report['result'],'failures',fail)
for n,a in budgets.items():print(n,'actual upper',hi(a),'required',limits[n])
print('Saved LOWER certificate Rayleigh upper',upper.hi,'required target lower .000999; actual target undecided')
print('Full certificate',out,'direction',p)
