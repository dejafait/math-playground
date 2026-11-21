#!/usr/bin/env python3
"""C999v: complete fixed621 audit, with independent integer scalar bounds.

Reuse C999q596's audited unchanged entry radii/weights after exact pins,
formula and range checks. Replay every changed row and matrix separately.
Original analytic, IEEE754/Decimal, core and c_star contracts remain.
"""
import ast
import hashlib
import importlib.util
import json
from decimal import Decimal
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

P = Path(__file__).resolve().parent
N, J, K, F, E = 512, 1024, 65536, 1022, 1024
spec = importlib.util.spec_from_file_location('integer557for623', P/'fixed-block-metric-audit-557.py')
helper = importlib.util.module_from_spec(spec)
spec.loader.exec_module(helper)
Q, SCALE, sq, ln = helper.Q, helper.SCALE, helper.sq, helper.ln
checks, failures, evidence = [], [], {}


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def read(name): return json.loads((P/name).read_text())
def exact(x): return Q(Fr(float(x)))
def fro(x): return exact(np.linalg.norm(x))*Q('1.000000001')+Q('1e-100')
def gamma(n): return Q(Fr(n, 2**53))/(1-Q(Fr(n, 2**53)))
def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok: failures.append(label)
def cap(q, limit, label): check(0 <= q.lo <= q.hi < Q(limit).lo, label)
def bound(name, q, limit):
    cap(q, limit, name)
    evidence.setdefault('bounds', {})[name] = dict(value=q.json(), required_less_than=limit)
def uf(q):
    f = np.nextafter(float(Fr(q.hi, SCALE)), np.inf)
    check(Fr(float(f)) >= Fr(q.hi, SCALE), 'upward scalar conversion')
    return f
def function_ast(name, function):
    nodes = ast.parse((P/name).read_text()).body
    return ast.dump(next(n for n in nodes if isinstance(n, ast.FunctionDef) and n.name == function), include_attributes=False)


def main():
    old = read('energy-complement-band-621.json')
    rep = read('energy-complement-band-replay-623.json')
    ledger = read('energy-complement-band-ledger-621.json')
    prior = read('tail-galerkin-family-audit-596.json')
    raw = read('tail-galerkin-family-certificate-594.json')
    names = set(old['input_hashes']) | set(prior['evidence']['input_hashes'])
    names |= {'energy-complement-band-621.'+x for x in ('py', 'json', 'npz')}
    names |= {'energy-complement-band-ledger-621.'+x for x in ('py', 'json')}
    names |= {'tail-galerkin-family-audit-596.py', 'tail-galerkin-family-audit-596.json'}
    pins = {n: sha(P/n) for n in names}
    for label, record in [('621', old), ('replay623', rep), ('ledger621', ledger), ('audit596', prior)]:
        check(record['failures'] == [] and all(x['passed'] for x in record['checks']), label+' all checks and failure list')
    for n, h in old['input_hashes'].items(): check(pins[n] == h, '621 input pin '+n)
    for n, h in prior['evidence']['input_hashes'].items(): check(pins[n] == h, '596 imported pin '+n)
    for record, name in [(old, 'energy-complement-band-621'), (ledger, 'energy-complement-band-ledger-621'), (prior, 'tail-galerkin-family-audit-596')]:
        check(record['script_sha256'] == pins[name+'.py'], 'generator pin '+name)
    check(old['archive']['sha256'] == pins['energy-complement-band-621.npz'], '621 complete archive pin')
    check(ledger['certificate_sha256'] == pins['energy-complement-band-621.json'], 'ledger621 certificate pin')
    check(rep['script_sha256'] == sha(P/'energy-complement-band-replay-623.py'), 'replay source pin')
    check(rep['archive']['sha256'] == sha(P/'energy-complement-band-replay-623.npz'), 'replay full archive pin')
    with np.load(P/'energy-complement-band-621.npz') as f: ar = {k: f[k].copy() for k in f.files}
    with np.load(P/'energy-complement-band-replay-623.npz') as f:
        check(set(f.files) == set(ar), 'every replay array present')
        for k, v in ar.items(): check(np.isfinite(v).all() and np.array_equal(v, f[k]), 'entire replay array '+k)
    check(old['ledger']['complete_residual_sha256'] == rep['ledger']['complete_residual_sha256'], 'all higher residual rows replay')
    blocks = old['ledger']['row_blocks']
    check(blocks == rep['ledger']['row_blocks'], 'all changed block records replay')
    check([(b['first'], b['last']) for b in blocks] == [(n, n+511) for n in range(J, K, N)], 'all126 higher blocks partition outputs')
    # Reuse the completed596 entry/weight verification, not a preview or an
    # old endpoint covariance. The exact scalar formula and ranges agree.
    check(function_ast('energy-complement-band-621.py', 'response_error') == function_ast('tail-galerkin-family-certificate-594.py', 'response_error'), 'identical audited radius formula')
    for key, prior_key in [('local_square_error_fro', 'square_upper'), ('local_all_output_error_fro', 'rectangle_upper')]:
        check(Fr(prior['evidence']['radius_total'][prior_key]['hi']) <= Fr(old['bounds'][key]['hi']), 'audited independent radius below621 upper '+key)
    check(all(b['local_error_fro_squared'] == c['local_error_fro_squared'] for b, c in zip(blocks, raw['ledger']['row_blocks'])), 'all126 unchanged radius sums')
    with np.load(P/'tail-galerkin-family-certificate-594.npz') as f:
        check(np.array_equal(ar['local_error_radius_square'], f['local_error_radius_square']), 'all square radii identical to audited594')
        check(np.array_equal(ar['Z'], f['Z']), 'entire neutral basis identical to audited594')
    check(old['ledger']['neutral_ratio_intervals'] == raw['ledger']['neutral_ratio_intervals'], 'all1022 audited exact-neutral intervals')
    evidence['reused_entry_coverage'] = dict(entries=K*J, weights=K-N, source='C999q Section8/audit596', radius_total=prior['evidence']['radius_total'])
    with np.load(P/'original-galerkin-586.npz') as f: M, T, Ts, U = [f[k].copy() for k in ('local_matrix', 't_entries', 'ts_entries', 'u_entries')]
    with np.load(P/'complete-covariance-532.npz') as f: m0, cov00 = f['m0'].copy(), f['cov00'].copy()
    H = m0-.00024*np.eye(N)-(100/307)*(cov00+.0046*np.eye(N))
    Z, V, C, X, A, B, Y, G = [ar[k] for k in ('Z', 'V', 'C0', 'ZT', 'A', 'B', 'Y', 'G')]
    check(Z.shape == (J, F) and X.shape == (J, N) and Y.shape == (F, E) and C.shape == (510,512), 'all projected dimensions')
    check(np.array_equal(V[:510], -C) and np.array_equal(V[510:], np.eye(N)), 'dyadic free map exact sparsity')
    check(np.array_equal(T, Ts.T), 'complete forcing adjoint orientation')
    aa=Z.T@M@Z; bb=Z.T@np.hstack((T@X, Ts@X)); gg=Z@Y
    trial=np.block([[X.T@M@X, -X.T@U.T@X], [-X.T@U@X, X.T@M@X]])-bb.T@Y-Y.T@bb+Y.T@aa@Y
    for label, x in [('X', X-Z@V), ('A', A-aa), ('B', B-bb), ('G', G-gg), ('trial', ar['trial']-trial)]: cap(fro(x), '1e-9', 'entire assembly '+label)
    rho=np.hstack((T@X, Ts@X))-M@G
    check(np.array_equal(rho[:N], ar['head_residual']), 'all head residual entries including actual Dg')
    lowers=read('fixed-block-metric-555.json')['middle']['diagonal_lower_endpoints']
    weights=np.array([float(np.nextafter(float(2/Decimal(s)), np.inf)) for s in lowers])
    check(len(weights) == K-N, 'all audited unchanged inverse weights')
    initial=rho[N:].T@(weights[:N, None]*rho[N:])
    trace_rebuild=float(np.trace(initial))+sum(b['weighted_residual_fro_squared'] for b in blocks)
    check(abs(float(np.trace(ar['finite_covariance']))-trace_rebuild)<1e-10, 'complete finite trace includes512:1023 and all126 higher blocks')
    factors={}
    targets={'galerkin_floor': A-.77*np.eye(F), 'elimination_norm': .052**2*np.eye(510)-C@C.T, 'predictor_norm': .61**2*np.eye(F)-Y@Y.T, 'local_operator_norm': 100*np.eye(F)-(M@Z).T@(M@Z), 'reference_floor': H-.24*np.eye(N), 'projected_zero_comparison': ar['comparison_lower']-.001*np.eye(E)}
    for name, target in targets.items():
        ff=ar['factor_'+name]; rr=fro(target-ff@ff.T)
        cap(sq(fro(ff)), '100000', 'factor magnitude '+name)
        check(np.max(np.abs(target))<1000, 'factor target magnitude '+name)
        er=rr+gamma(4096)*100000+Q('2e-7')
        cap(er, '1e-6', 'every factor reconstruction '+name)
        factors[name]=dict(total_error=er.json(), required_less_than='1e-6')
    evidence['factors']=factors
    z,c,v,y=Q('1.008'),Q('.05201'),Q('1.002'),Q('.610001')
    p,m=z*v,z*y
    ea=Q(old['bounds']['local_square_error_fro']['hi']); eall=Q(old['bounds']['local_all_output_error_fro']['hi'])
    etaA=sq(z)*ea+Q('1e-6'); etaB=Q(2).sqrt()*sq(z)*J*Q('1e-6')+Q('2e-6'); etaU=sq(z)*J*Q('1e-6')+Q('1e-6')
    re=fro(A[:510,:510]@C-A[:510,510:])+Q('1e-6')
    e=(re+etaA*(1+c))/Q('.779')
    cap((1+sq(c)).sqrt(), '1.002', 'full free-map norm')
    q=2*v*e+sq(e)
    et=etaA*(sq(v)+sq(y))+2*etaB*v*y+etaU*sq(v)+Q('4e-5')+42*q+14*e*y
    sol=ar['head_solution']; rh=ar['head_residual']
    he=fro(rh)*(fro(rh-H@sol)+Q('1e-8')*fro(sol)+Q('1e-6'))/Q('.239999')+Q('1e-6')
    dp=Q(2*N*J).sqrt()*Q('1e-6')*p+ea*m+Q('1e-6')
    dm=Q(2*(K-N)*J).sqrt()*Q('1e-6')*p+eall*m+Q('1e-6')
    df=(sq(dp)/Q('.239999')+2*sq(dm)/Q('6.14')).sqrt()
    trace=exact(np.trace(ar['head_covariance']+ar['finite_covariance']))+Q('1e-4')
    ef=2*trace.sqrt()*df+sq(df)+Q('1e-4')
    half=Q(Fr(1,2)); ell=sum((half**(2*j+1)/(2*j+1) for j in range(200)),Q())
    ell+=Q.ends(0,(half**401/(401*(1-half*half))).hi)
    pi=16*helper.arith.atan(5)-4*helper.arith.atan(239)
    ap,am=Q(),Q()
    # These16 powers are the inspected complete C744v list.
    for n, prime in [(29,29),(31,31),(32,2),(37,37),(41,41),(43,43),(47,47),(49,7),(53,53),(59,59),(61,61),(64,2),(67,67),(71,71),(73,73),(79,79)]:
        delay=7*ell-ln(Q(n)); wt=ln(Q(prime))/Q(n).sqrt()
        check(delay.lo>0 or delay.hi<0, 'strict delay sign '+str(n))
        if delay.lo>0: ap+=wt
        else: am+=wt
    wb=4*ell*(1+Q('1.5')/Q(3).sqrt().sqrt())/sq(pi)
    jr=(2/pi)/(1-Q((J-1)**2)/(K*K))*(Q(sum(n**4 for n in range(1,J))).sqrt()/Q(5*(K-1)**5).sqrt()+Q(sum(n*n for n in range(1,J))).sqrt()/Q(3*(K-1)**3).sqrt())
    sr=sum((sq(4*n+16*ell/sq(pi)) for n in range(J)),Q()).sqrt()/Q(3*(K-1)**3).sqrt()
    kap=1/(2187*Q(3).sqrt()*Q('2.5')*(1-Q(1)/729))
    tr=Q(2).sqrt()*p*((ap+am)*jr+kap)+sr*m
    dk=ln(K/(2*ell))-2*sq(ell)/(9*K*K)
    tw=[2*ap/pi/Q(K-1).sqrt(),2*am/pi/Q(K-1).sqrt()]*2+[Q(2).sqrt()*(1+wb/K)/Q(K-1).sqrt(),(1+wb/K)/Q(K-1).sqrt()]
    for j, w in enumerate(tw):
        s=old['ledger']['tail_weights'][j]
        check(Fr(s['lo'])<=Fr(w.lo,SCALE)<=Fr(w.hi,SCALE)<=Fr(s['hi']), 'entire tail weight '+str(j))
    idx=np.arange(J);d=np.ones(J);d[0]=1/np.sqrt(2);par=np.where(idx%2==0,1.,-1.)
    bd=np.zeros((6,E));bd[0,:N]=(d*par)@X;bd[1,:N]=d@X;bd[2,N:]=d@X;bd[3,N:]=(d*par)@X;bd[4]=(d*(idx%2==0))@G;bd[5]=(d*(idx%2==1))@G
    check(np.array_equal(bd,ar['tail_boundary']), 'all six projected boundary rows')
    leading=uf(sum(tw,Q()))*(bd.T@(np.array([uf(w) for w in tw])[:,None]*bd))
    tail=uf(2/dk)*(1.1*leading+uf(11*sq(tr))*np.eye(E))+1e-5*np.eye(E)
    cap(fro(tail-ar['tail_covariance_upper']), '1e-12', 'entire infinite tail majorant assembly')
    rebuilt=ar['head_covariance']+ar['finite_covariance']+ar['tail_covariance_upper']
    rebuilt=(rebuilt+rebuilt.T)/2+uf(ef)*np.eye(E)
    cap(fro(rebuilt-ar['full_covariance_upper']), '1e-12', 'complete covariance assembly')
    ct=fro(ar['full_covariance_upper'])+Q('1e-5')
    de=Q(2).sqrt()*Q('4.71')*z*e/Q('.239999').sqrt(); ec=2*ct.sqrt()*de+sq(de)
    vals=[('exact_elimination_error',e,'.000408451801'),('trial_error',et,'.041175449134'),('head_action_nuclear_error',he,'.000001074705'),('weighted_residual_error',df,'.007386577394'),('finite_trace',trace,'2.682234845453'),('finite_covariance_error',ef,'.024349339903'),('complete_tail_remainder',tr,'.006323211217'),('full_covariance_operator_bound',ct,'1.662542686651'),('weighted_elimination_error',de,'.005597995380'),('exact_elimination_covariance_error',ec,'.014467406040')]
    for name,val,limit in vals: bound(name,val,limit)
    for name,val in [('trial_error',et),('finite_covariance_error',ef),('exact_elimination_covariance_error',ec)]:
        check(Fr(val.hi,SCALE)<=Fr(old['bounds'][name]['hi'])+Fr('1e-14'), 'independent scalar agreement within assembly slack '+name)
    check(dk.lo>Q('10.9963070613268').hi,'all infinite diagonal weights covered')
    cap(z*(Q('10.000001')+ea*z+Q('1e-6')), '11', 'complete finite A operator bound')
    cap(sq(z)*30,'31','remote block bound');cap(Q(2).sqrt()*sq(z)*Q('4.71'),'7','two-orientation block bound')
    debt=Q(old['bounds']['trial_error']['hi'])+Q(old['bounds']['exact_elimination_covariance_error']['hi'])+Q('1e-5')
    low=(ar['trial']+ar['trial'].T)/2-ar['full_covariance_upper']-uf(debt)*np.eye(E);low=(low+low.T)/2
    cap(fro(low-ar['comparison_lower']),'1e-12','entire final lower comparison assembly')
    check(np.count_nonzero(ar['quarter_metric_upper'])==0,'zero threshold only')
    for name,a,limit in [('Z',Z,32),('V',V,23),('X',X,23),('C',C,1),('Y',Y,16),('G',G,16),('M',M,1000),('T',T,100),('Ts',Ts,100),('U',U,100),('A',A,200),('B',B,100),('boundary',bd,100),('head_rhs',rh,1),('head_solution',sol,1),('m0',m0,400),('cov00',cov00,1)]: cap(fro(a),str(limit),'full magnitude '+name)
    cap((2*ell+2*pi)/Q('.24'),'60','full response norm');cap(ap+am+kap,'8','both full forcing norms')
    budgets={'A':(gamma(4096)*32**2*1000+Q('1e-9'),'1e-6'),'B':(2*gamma(4096)*32**2*100+Q('1e-9'),'2e-6'),'U':(gamma(4096)*32**2*100+Q('1e-9'),'1e-6'),'trial':(20*gamma(4096)*(32**2*1000+100*16+200*16**2)+Q('1e-7'),'4e-5'),'elimination_equation':(gamma(2048)*200+Q('1e-8'),'1e-6'),'projected_map':(gamma(2048)*32*23+Q('1e-8'),'1e-6'),'row_maps':(gamma(2048)*(2*257*32+1921*16)+Q('1e-8'),'1e-6'),'boundary':(gamma(4096)*100**2+Q('1e-7'),'1e-5'),'head_product_nuclear':(Q(E).sqrt()*gamma(1024)+Q('1e-8'),'1e-6'),'finite_gram_trace':(gamma(K)*4+gamma(E*E)*10+gamma(4096)*Q(E).sqrt()*4+he+Q('1e-6'),'1e-4'),'H_assembly':(gamma(16)*401+Q('1e-10'),'1e-8')}
    evidence['arithmetic']={name:dict(upper=val.json(),required_less_than=limit) for name,(val,limit) in budgets.items()}
    for name,(val,limit) in budgets.items(): cap(val,limit,'paid arithmetic '+name)
    check((sq(y)-Q('.61')**2-Q('1e-6')).lo>(gamma(4096)*256+Q('1e-9')).hi,'predictor norm enlargement pays Gram')
    check((sq(c)-Q('.052')**2-Q('1e-6')).lo>(gamma(4096)+Q('1e-9')).hi,'elimination norm enlargement pays Gram')
    check((Q('10.000001')**2-100-Q('1e-6')).lo>(gamma(4096)*100000+Q('1e-8')).hi,'local operator enlargement pays Gram')
    cap(gamma(K*J+10),'1e-8','full radius summation inflation');cap(gamma(E*E+10),'1e-9','matrix norm inflation')
    evidence['full_array_count']=len(ar);evidence['complete_residual_digest']=old['ledger']['complete_residual_sha256']
    first=read('energy-complement-band-audit-first-pass-623.json')
    check(first['failures']==['unchanged audited complete radius local_square_error_fro'], 'preserved first checker overstrict scalar-equality failure')
    check(first['script_sha256']==sha(P/'energy-complement-band-audit-first-pass-623.py'), 'preserved executed first checker bytes')
    evidence['first_checker_failure']=dict(failures=first['failures'], square_radius621=old['bounds']['local_square_error_fro'], square_radius594=raw['bounds']['local_square_error_fro'], resolution='Identical complete radius arrays have slightly different floating norm reductions. The mathematical reuse condition is domination of the independent596 radius upper bound, checked above, not equality of rounded norm reports. No source or mathematical parameter changed.')
    evidence['pins']=pins
    for n,h in pins.items(): check(sha(P/n)==h,'original preserved '+n)


try: main()
except Exception as exc: failures.append(type(exc).__name__+': '+str(exc))
out=P/'energy-complement-band-audit-623.json'
report=dict(result='PASS_UNDER_RETAINED_CONTRACTS' if not failures else 'INCONCLUSIVE',scope='C999v fixed exact energy projection and complete zero-threshold comparison',script_sha256=sha(Path(__file__)),checks=checks,failures=failures,evidence=evidence,certified_coefficient_floor='.000999' if not failures else None,qualifications=['Analytic-response and IEEE754/Decimal contracts retained','Whole neutral core and original c_star not independently validated','Only this energy-orthogonal band; mixed/global signs open'])
out.write_text(json.dumps(report,indent=2)+'\n')
print('Result',report['result'],'checks',len(checks),'failures',failures)
for name in ('exact_elimination_error','trial_error','finite_covariance_error','complete_tail_remainder','exact_elimination_covariance_error'):
    x=evidence.get('bounds',{}).get(name)
    if x: print(name,'actual upper',float(Fr(x['value']['hi'])),'required <',x['required_less_than'])
print('Required zero threshold; certified coefficient floor',report['certified_coefficient_floor'])
print('Full certificate',out.relative_to(P.parent.parent))
