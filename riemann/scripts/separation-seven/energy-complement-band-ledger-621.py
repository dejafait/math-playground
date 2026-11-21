#!/usr/bin/env python3
"""Complete arithmetic ledger for projected band621; not an independent conceptual audit."""
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
c=json.loads((P/'energy-complement-band-621.json').read_text());q=np.load(P/'energy-complement-band-621.npz')
ck(c['script_sha256']==sha(P/'energy-complement-band-621.py'),'executed source hash')
ck(c['archive']['sha256']==sha(P/'energy-complement-band-621.npz'),'full archive hash')
ck(c['failures']==[],'primary certificate failures empty')
ck(all(x['passed'] for x in c['checks']),'all primary checks pass')
for name,h in c['input_hashes'].items():ck(sha(P/name)==h,'input preserved '+name)
Z,Y,G,A,B=[q[n] for n in ('Z','Y','G','A','B')]
with np.load(P/'original-galerkin-586.npz') as t:M,T,Ts,U=[t[n] for n in ('local_matrix','t_entries','ts_entries','u_entries')]
E=1024;F=1022
C0,V,ZT=[q[n] for n in ("C0","V","ZT")]
ck(Z.shape==(1024,F) and Y.shape==(F,E),'full family dimensions')
ck(np.array_equal(V[:510],-C0) and np.array_equal(V[510:],np.eye(512)),'free band map exact sparsity')
ck(nf(ZT-Z@V).hi<Decimal('1e-10'),'entire projected input product rebuild')
AA=Z.T@M@Z;BB=Z.T@np.hstack((T@ZT,Ts@ZT))
EE=np.block([[ZT.T@M@ZT,-ZT.T@U.T@ZT],[-ZT.T@U@ZT,ZT.T@M@ZT]])-BB.T@Y-Y.T@BB+Y.T@AA@Y
for name,a,b in [('A',A,AA),('B',B,BB),('G',G,Z@Y),('trial',q['trial'],EE)]:ck(nf(a-b).hi<Decimal('1e-9'),'full rebuild '+name)
for name,a,cap in [('Z',Z,32),('Y',Y,16),('G',G,16),('A',A,200),('B',B,100),('M',M,1000),('T',T,100),('Ts',Ts,100),('U',U,100),('boundary',q['tail_boundary'],100),('head_rhs',q['head_residual'],1),('head_solution',q['head_solution'],1),('V',V,23),('C0',C0,1),('ZT',ZT,23)]:ck(nf(a).hi<cap,'magnitude '+name)
# Same dot-product/Frobenius bounds as audit596, with every enlarged dimension.
budgets={
'A':gam(4096)*32**2*1000+I('1e-9'),
'B':2*gam(4096)*32**2*100+I('1e-9'),
'U':gam(4096)*32**2*100+I('1e-9'),
'energy':20*gam(4096)*(32**2*1000+100*16+200*16**2)+I('1e-7'),
'elimination_equation':gam(2048)*200+I('1e-8'),
'projected_map':gam(2048)*32*23+I('1e-8'),
'row_maps':gam(2048)*(2*257*32+1921*16)+I('1e-8'),
'boundary':gam(4096)*100**2+I('1e-7'),
'head_product_nuclear':I(E).sqrt()*gam(1024)+I('1e-8'),
'finite_gram_trace':gam(65536)*4+gam(E*E)*10+gam(4096)*I(E).sqrt()*4+I('1e-5')+I('1e-6'),
'H_assembly':gam(16)*401+I('1e-10')}
limits={'elimination_equation':'1e-6','projected_map':'1e-6','A':'1e-6','B':'2e-6','U':'1e-6','energy':'4e-5','row_maps':'1e-6','boundary':'1e-5','head_product_nuclear':'1e-6','finite_gram_trace':'1e-4','H_assembly':'1e-8'}
for n,a in budgets.items():ck(a.hi<Decimal(limits[n]),'paid arithmetic '+n)
ck(gam(65536*1024+10).hi<Decimal('1e-8'),'full radius arithmetic inflation')
ck(gam(E*E+10).hi<Decimal('1e-8'),'joint norm arithmetic inflation')
factors={}
for name,target in [('galerkin_floor',A-.77*np.eye(F)),('predictor_norm',.61**2*np.eye(F)-Y@Y.T),('elimination_norm',.052**2*np.eye(510)-C0@C0.T),('local_operator_norm',100*np.eye(F)-(M@Z).T@(M@Z))]:
    f=q['factor_'+name];r=nf(target-f@f.T);err=r+gam(4096)*100000+I('2e-7')
    ck(nf(f).hi**2<100000,'factor cap '+name);ck(err.hi<Decimal('1e-6'),'full factor reconstruction '+name)
    factors[name]=dict(reconstruction_error=err.json(),required='1e-6')
ck((I('.610001')*I('.610001')-I('.61')*I('.61')-I('1e-6')).lo>(gam(4096)*16**2+I('1e-9')).hi,'predictor inflation pays Gram')
ck((I('.05201')*I('.05201')-I('.052')*I('.052')-I('1e-6')).lo>(gam(4096)+I('1e-9')).hi,'elimination norm inflation pays Gram')
ck((I('10.000001')*I('10.000001')-100-I('1e-6')).lo>(gam(4096)*100000+I('1e-8')).hi,'LZ inflation pays Gram')
blocks=c['ledger']['row_blocks']
ck(len(blocks)==126 and all(b['first']==1024+512*j and b['last']==1535+512*j for j,b in enumerate(blocks)),'every finite higher row partition')
# Reconstruct the ENTIRE final positive factor, not a minimum eigenvalue.
low=q['comparison_lower'];ff=q['factor_projected_zero_comparison']
err=nf(low-.001*np.eye(E)-ff@ff.T)+gam(4096)*100000+I('2e-7')
ck(err.hi<Decimal('1e-6'),'full final factor error<1e-6')
ck(nf(ff).hi**2<100000,'full final factor norm cap')
# Confirm actual-exact reference head assembly and its factor too.
with np.load(P/'complete-covariance-532.npz') as d:
 H=d['m0']-.00024*np.eye(512)-(100/307)*(d['cov00']+.0046*np.eye(512))
rf=q['factor_reference_floor'];re=nf(H-.24*np.eye(512)-rf@rf.T)+gam(4096)*100000+I('2e-7')
ck(re.hi<Decimal('1e-6'),'full reference floor factor reconstruction')
# All six boundary rows rebuilt after forming projected endpoint maps.
idx=np.arange(1024);d=np.ones(1024);d[0]=1/np.sqrt(2)
vp=d;va=d*np.where(idx%2==0,1.,-1.);ve=d*(idx%2==0);vo=d*(idx%2==1)
bd=np.zeros((6,E));bd[0,:512]=va@ZT;bd[1,:512]=vp@ZT;bd[2,512:]=vp@ZT;bd[3,512:]=va@ZT;bd[4]=ve@G;bd[5]=vo@G
ck(nf(bd-q['tail_boundary']).hi<Decimal('1e-10'),'full projected six-row boundary rebuild')
# Lower endpoints / weights are covered by the unchanged C999q596 import.
# They are reused unchanged; no new transcendental entry claims.
report=dict(result='PASS_UNDER_RETAINED_CONTRACTS' if not fail else 'LEDGER_INCOMPLETE',failures=fail,checks=checks,arithmetic={n:dict(actual_upper=a.json(),required=limits[n]) for n,a in budgets.items()},factor_checks=factors,final_factor_error=err.json(),certified_free_coefficient_floor='.000999' if not fail else None,reference_factor_error=re.json(),certificate_sha256=sha(P/'energy-complement-band-621.json'),script_sha256=sha(Path(__file__)),qualification='Local arithmetic verification only. Separate conceptual audit pending; all analytic, core, IEEE754/Decimal and unreplayed c_star qualifications remain.')
out=P/'energy-complement-band-ledger-621.json';out.write_text(json.dumps(report,indent=2)+'\n')
print('Result',report['result'],'failures',fail)
for n,a in budgets.items():print(n,'actual upper',hi(a),'required',limits[n])
print('Full final factor error upper',err.hi,'required <1e-6; certified coefficient floor .000999 > zero')
print('Full certificate',out)
