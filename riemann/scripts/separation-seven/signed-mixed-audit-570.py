#!/usr/bin/env python3
"""C999m conceptual-audit evidence. Read originals; write only step570.

Full factor/Gram replay and directed scalar/resonance audit, under the
inherited binary64/Decimal contracts. No FFT or quarter certification.
"""
import hashlib
import importlib.util
import json
import math
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
N, J, K, E = 512, 32768, 65536, 1020
names = ['signed-mixed-output-tail-565', 'signed-mixed-remote-input-tail-566',
         'signed-mixed-predictor-error-567', 'signed-mixed-local-trial-input-568',
         'signed-mixed-inverse-input-569']
records = [json.loads((BASE/(s+'.json')).read_text()) for s in names]
checks, failures, factors, scalar_results, resonance_results = [], [], {}, {}, {}

def check(ok, label):
    checks.append({'label': label, 'passed': bool(ok)})
    if not ok:
        failures.append(label)

def sha(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda: f.read(8*1024*1024), b''):
            h.update(block)
    return h.hexdigest()

pins = {}
for name, rec in zip(names, records):
    for ext in ['.py', '.json', '.npz']:
        pins[name+ext] = sha(BASE/(name+ext))
    check(not rec['failures'] and all(t['passed'] for t in rec['checks']),
          name+' complete original check list')
    expected = rec.get('source_sha256', rec.get('script_sha256'))
    check(pins[name+'.py'] == expected, name+' source pin')
    for filename, expected in rec['input_hashes'].items():
        check(sha(BASE/filename) == expected, name+' input '+filename)
    archive = rec.get('archive')
    expected = (archive['sha256'] if isinstance(archive, dict) else
                rec.get('archive_sha256'))
    if expected:
        check(pins[name+'.npz'] == expected, name+' archive pin')
    for filename, artifact in rec.get('artifacts', {}).items():
        check(sha(BASE/filename) == artifact['sha256'], name+' artifact '+filename)

with np.load(BASE/'neutral-head-covariance-559.npz') as a:
    mc, z, y, solution = a['comparison_lower'], a['z'], a['predictor_free'], a['head_solution']
    inherited_boundary, inherited_tail = a['boundary_functionals'], a['tail_covariance_upper']
with np.load(BASE/'complete-covariance-532.npz') as a:
    m0, chat = a['m0'], a['cov00']
check(np.array_equal(mc, mc.T), 'exact comparison symmetry')

def fro(a):
    return float(np.linalg.norm(a))

def factor_check(label, target, factor):
    residual, f2 = fro(target-factor@factor.T), fro(factor)**2
    maximum = max(float(np.max(np.abs(a))) for a in [target, factor])
    factors[label] = dict(residual_fro=residual, factor_squared_fro=f2,
                          maximum_entry=maximum, required_residual='1e-7',
                          restored_margin='1e-6')
    check(residual < 1e-7 and f2 < 100000 and maximum < 400,
          label+' complete reconstruction and magnitude ledger')

with np.load(BASE/(names[0]+'.npz')) as a:
    check(np.array_equal(a['comparison'], mc) and np.array_equal(a['tail_covariance'], inherited_tail),
          '565 exact input arrays')
    target = .02*mc-(inherited_tail+inherited_tail.T)/2-1e-6*np.eye(E)
    factor_check('565 output', target, a['factor'])

with np.load(BASE/(names[1]+'.npz')) as a:
    check(np.array_equal(a['comparison'], mc) and
          np.array_equal(a['boundary_rows'], inherited_boundary[:4]), '566 exact input arrays')
    for j, row in enumerate(a['boundary_rows']):
        factor_check('566 boundary '+str(j), mc-np.outer(row,row)/144-1e-6*np.eye(E),
                     a['boundary_factor_'+str(j)])

with np.load(BASE/(names[2]+'.npz')) as a:
    check(np.array_equal(a['head_form_center'], m0) and np.array_equal(a['covariance_center'], chat)
          and np.array_equal(a['neutral_basis'], z), '567 exact input arrays')
    h = m0-.00024*np.eye(N)-(100/307)*(chat+.0046*np.eye(N))
    check(np.array_equal(h, a['reference_center']), '567 same rational-reference center')
    defect = a['proposed_head_defect']
    solve_residual = fro((h-m0)@z-h@defect)
    check(solve_residual < 1e-9 and fro(defect) < .01732, '567 complete defect equation')
    factor_check('567 covariance', .172*np.eye(N)-chat-1e-6*np.eye(N), a['covariance_upper_factor'])

with np.load(BASE/(names[3]+'.npz')) as a:
    check(np.array_equal(a['comparison'], mc), '568 exact comparison')
    dd = np.ones(N); dd[0] = 1/np.sqrt(2)
    even, odd = dd*(np.arange(N)%2 == 0), dd*(np.arange(N)%2 == 1)
    local = np.zeros((4,E)); local[:2,:510] = np.vstack((np.sqrt(2)*(even@z), odd@z))
    local[2:,510:] = local[:2,:510]
    g = z@y
    trial = np.vstack((dd@g, (dd*((-1.)**np.arange(N)))@g))
    check(np.array_equal(local, a['local_boundary_rows']) and np.array_equal(trial,a['trial_boundary_rows'])
          and np.array_equal(g,a['raw_trial_center']), '568 complete boundary map replay')
    for label, rows, q in [('local',local,12), ('trial_plus',trial[:1],6), ('trial_minus',trial[1:],6)]:
        factor_check('568 '+label, mc-rows.T@rows/(q*q)-1e-6*np.eye(E), a[label+'_factor'])

# Replay all finite inverse rows, all weighted Grams and both boundary rows.
# The source/formula audit uses the inherited direct-residual byte digest;
# this replay does not regenerate that expensive residual calculation.
v = np.load(BASE/'signed-mixed-inverse-centers-569.npy', mmap_mode='r')
check(v.shape == (K,E) and np.array_equal(v[:N],solution), '569 complete inverse includes audited head')
qdef = {'boundary_plus':5., 'boundary_minus':5., 'low_norm':.35,
        'moment1':.011, 'moment2':.006, 'band_norm':.007}
grams = {key:np.zeros((E,E)) for key in qdef}
boundary = np.zeros((2,E)); nf2 = {key:0. for key in qdef}
for start in range(0,K,N):
    w = np.array(v[start:start+N]); ns = np.arange(start,start+N)
    if start < J:
        d = np.ones(N); d[ns==0] = 1/np.sqrt(2)
        boundary[0] += d@w; boundary[1] += (d*((-1.)**ns))@w
        for key, power in [('low_norm',0),('moment1',1),('moment2',2)]:
            scaled = ((ns/(J-1))**power)[:,None]*w/qdef[key]
            grams[key] += scaled.T@scaled; nf2[key] += fro(scaled)**2
    else:
        scaled = w/qdef['band_norm']
        grams['band_norm'] += scaled.T@scaled; nf2['band_norm'] += fro(scaled)**2
for key, row in zip(['boundary_plus','boundary_minus'],boundary):
    scaled = row/qdef[key]; grams[key] = np.outer(scaled,scaled); nf2[key] = fro(scaled)**2
with np.load(BASE/(names[4]+'.npz')) as a:
    check(np.array_equal(a['comparison'],mc) and np.array_equal(boundary,a['boundary_rows']),
          '569 complete comparison and boundary replay')
    for key in qdef:
        check(np.array_equal(grams[key],a[key+'_normalized_gram']), '569 entire Gram replay '+key)
        factor_check('569 '+key, mc-grams[key]-1e-6*np.eye(E), a[key+'_factor'])
    check(a['hcenter'].shape==(K-N,) and np.isfinite(a['hcenter']).all()
          and float(a['hcenter'].min())>6.14, '569 every saved diagonal center')
check(max(nf2.values()) < 10000 and fro(v[:J]) < 1 and fro(v[J:]) < .1
      and fro(boundary) < 100, '569 complete finite magnitude ledger')
head = json.loads((BASE/'neutral-head-covariance-559.json').read_text())
check(records[4]['full_residual_digest']==head['finite']['regenerated_combined_residual_sha256'],
      '569 inherited complete direct residual digest')
print('All 15 full factor reconstructions and complete inverse Grams inspected',flush=True)

# Higher-precision directed recomputation, including every resonance pair.
spec = importlib.util.spec_from_file_location('iv570',BASE/'complete-schur-531.py')
iv = importlib.util.module_from_spec(spec); spec.loader.exec_module(iv)
iv.DOWN=Context(prec=110,rounding=ROUND_FLOOR)
iv.UP=Context(prec=110,rounding=ROUND_CEILING)
iv.NEAR=Context(prec=110,rounding=ROUND_HALF_EVEN)
I=iv.I
def sq(a): return a*a
def atan(q):
    a=I(1)/q; power=a; total=I(0)
    for j in range(120):
        total+=((-1)**j)*power/(2*j+1); power*=a*a
    return total+I(power.hi.copy_negate(),power.hi)/241
pi,ell=16*atan(5)-4*atan(239),I(3).ln()/2
mu,zbound,ybound,dK=I('.000999'),I('1.008'),I('1.320001'),I('10.9963070613268')
zeta=(1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
lowcoef=(4/(3*dK*(K-1)**3)).sqrt()
u=I(1)/2**53
def gamma(n): return n*u/(1-n*u)
fe=I('1e-7')+gamma(2048)*100000+I('2e-7')
ge=gamma(2*K)*10000+I('1e-8')
check(fe.hi < Decimal('1e-6') and (fe+ge).hi < Decimal('1e-6'), 'both complete factor error margins')
scalar_results['factor_error']=fe.json(); scalar_results['inverse_factor_error']=(fe+ge).json()

def absiv(x):
    assert x.lo>0 or x.hi<0
    return x if x.lo>0 else -x

def resonance(separation, rec):
    # Independent prime sieve, then enumerate exactly the strict integer window.
    top=math.isqrt(3**(separation+1))+1
    sieve=[True]*(top+1); sieve[:2]=[False,False]
    for p in range(2,math.isqrt(top)+1):
        if sieve[p]:
            for n in range(p*p,top+1,p): sieve[n]=False
    pairs=[]
    for p in range(2,top+1):
        if not sieve[p]: continue
        n=p
        while n*n<3**(separation+1):
            if n*n>3**(separation-1): pairs.append((n,p))
            n*=p
    pairs.sort()
    key='n' if separation==14 else 'q'
    check(pairs==[(p[key],p['prime']) for p in rec['primes']],str(separation)+' complete prime enumeration')
    groups={'positive':[],'negative':[]}; total=I(0)
    for n,p in pairs:
        w=I(p).ln()/I(n).sqrt(); total+=w
        if n*n==3**separation: continue
        delta=separation*ell-I(n).ln(); beta=absiv(delta)/ell
        assert 0<beta.lo<=beta.hi<1
        groups['positive' if delta.lo>0 else 'negative'].append((n,w,beta))
    bounds={}; detail={}
    for sign,rows in groups.items():
        diag,osc=I(0),I(0); inspected=[]
        saved=rec['all_pair_resonance_bounds'][sign]; index=0
        for j,(n,a,b) in enumerate(rows):
            diag+=a*a
            for m,c,d in rows[j:]:
                plus=b+d; gap=min(plus.lo,(2-plus).lo)
                assert gap>0
                diff=None if n==m else absiv(b-d).lo
                term=a*a/I(gap) if n==m else 2*a*c*(1/I(gap)+1/I(diff))
                old=saved[index]; index+=1
                check(Decimal(old['gap_sum_lower']) <= gap and
                      (diff is None or Decimal(old['gap_difference_lower']) <= diff),
                      f'{separation} {sign} {n},{m} complete resonance lower bounds')
                check(Decimal(old['oscillatory_numerator_upper']) >= term.hi,
                      f'{separation} {sign} {n},{m} oscillatory upper bound')
                osc+=term
                inspected.append(dict(n=n,m=m,gap_sum_lower=str(gap),
                    gap_difference_lower=None if diff is None else str(diff),upper=str(term.hi)))
        check(index==len(saved),f'{separation} {sign} all pairs inspected')
        bound=diag/(2*(K-1))+osc/(2*K*K)
        field='complete_weighted_sine_square_upper' if separation==14 else 'complete_sine_square_upper'
        check(bound.hi<=Decimal(rec['sine_tails'][sign][field]['hi']),f'{separation} {sign} complete sine bound')
        bounds[sign]=bound
        detail[sign]=dict(pair_count=index,bound=bound.json(),pairs=inspected)
    resonance_results[str(separation)]=detail
    return bounds,total

v14,a14=resonance(14,records[1]); v7,a7=resonance(7,records[3])
jrem=(2/pi)/(1-I((N-1)**2)/(K*K))*(I(sum(n**4 for n in range(1,N))).sqrt()/
       (I(5).sqrt()*I(K-1)*I(K-1)*I(K-1).sqrt())+
       I(sum(n*n for n in range(1,N))).sqrt()/(I(3).sqrt()*I(K-1)*I(K-1).sqrt()))
k7=1/(I(2187)*I(3).sqrt()*I('2.5')*(1-I(1)/729))
k14=1/(I(3**16)*I(3).sqrt().sqrt()*I('2.5')*(1-I(1)/3**13))
out=zeta*I(2).sqrt()*I('4.71')*(2/dK).sqrt()*(I('.02').sqrt()+
    (2/dK).sqrt()*I('.062501906')*zbound*I('.000612')/mu.sqrt())
remote=(((2/pi)*I(2).sqrt()*(12+I('1e-7')/mu.sqrt())*
    (v14['positive'].sqrt()+v14['negative'].sqrt())+(a14*jrem+k14)*zbound/mu.sqrt())/
    dK.sqrt()+lowcoef*I('29.813203120')*zbound/mu.sqrt())
eh=((I('1e-8')+I('.00024'))*zbound+I('1e-14')+I('1e-7')+I('1e-8')*I('.0174'))/I('.239999')
edef=(sq(I('.0174')+eh)+sq((2/I('6.14'))*zbound*I('.1766').sqrt())).sqrt()
pred=zeta*I(2).sqrt()*I('4.71')*edef*I('.000612')/mu.sqrt()
b=4*ell*(1+I('1.5')/I(3).sqrt().sqrt())/(pi*pi)
srem=(sum((sq(4*n+16*ell/(pi*pi)) for n in range(N)),I(0)).sqrt()/
    (I(3).sqrt()*I(K-1)*I(K-1).sqrt()))
lt=(((1+b/K)*(12+I('1e-7')/mu.sqrt())/I(K-1).sqrt()+srem*zbound/mu.sqrt()+
    (2/pi)*I(2).sqrt()*(6+I('1e-7')/mu.sqrt())*(v7['positive'].sqrt()+v7['negative'].sqrt())+
    I(2).sqrt()*(a7*jrem+k7)*zbound*ybound/mu.sqrt())/dK.sqrt()+
    lowcoef*(I('6.191')+I(2).sqrt()*I('4.71')*zbound*ybound)/mu.sqrt())
dJ=(I(J)/(2*ell)).ln()-2*ell*ell/(9*J*J)
ehead=(I(head['finite']['residual_head_error']['hi'])+I(head['finite']['head_solve_error']['hi']))/I('.239999')
def inv_err(count,d):
    count=I(count)
    dr=I(2).sqrt()*(count*N).sqrt()*I('2.1e-7')*zbound+(
        I('.000000181')+(count*N).sqrt()*I('1e-7'))*zbound*ybound+I('1e-7')
    return 2*dr/d+6*I('1e-6')/(d*(d-I('1e-6')))+I('1e-7')
elo,eband,eta=inv_err(J-N,I('6.14')),inv_err(K-J,dJ),I('1e-7')
qb=5+(I(N).sqrt()*ehead+I(J-N).sqrt()*elo+eta)/mu.sqrt()
q0=I('.35')+((ehead*ehead+elo*elo).sqrt()+eta)/mu.sqrt()
q1=I('.011')+(I(N-1)/(J-1)*ehead+elo+eta)/mu.sqrt()
q2=I('.006')+(I((N-1)**2)/(J-1)**2*ehead+elo+eta)/mu.sqrt()
qband=I('.007')+(eband+eta)/mu.sqrt()
lead=(2/pi)*I(2).sqrt()*qb*(v7['positive'].sqrt()+v7['negative'].sqrt())
rem=(2/pi)*I(2).sqrt()*a7*I(J).sqrt()/(1-I((J-1)**2)/(K*K))*(
    (J-1)**2*q2/(I(5).sqrt()*I(K-1)*I(K-1)*I(K-1).sqrt())+
    (J-1)*q1/(I(3).sqrt()*I(K-1)*I(K-1).sqrt()))
inv=((lead+rem+I(2).sqrt()*k7*q0+I(2).sqrt()*I('4.71')*qband)/dK.sqrt()+
    lowcoef*I(2).sqrt()*I('4.71')*(q0*q0+qband*qband).sqrt())
for label,value,threshold in [('output',out,'.163'),('remote_input',remote,'.112'),
                              ('predictor',pred,'.008'),('local_trial_input',lt,'.058'),
                              ('inverse_input',inv,'.08')]:
    scalar_results[label]=value.json()
    check(value.hi<Decimal(threshold),label+' complete directed bound <'+threshold)

# Audit the already stated scalar ledger; this does not test the locator.
threshold=sq(I('.5')-I('.163')-I('.008'))-sq(I('.112')+I('.058')+I('.08'))
check(threshold.lo<=Decimal('.045741')<=threshold.hi,'equation40 sufficient finite threshold')
scalar_results['required_finite_covariance']=threshold.json()
result=dict(scope='C999m Sections1-10 conceptual audit; inherited analytic/core/c_star/execution contracts',
    task_type='proof_audit',reasoning_class='conceptual_audit',input_hashes=pins,
    script_sha256=sha(Path(__file__)),factors=factors,scalars=scalar_results,
    resonance_replay=resonance_results,inverse_gram_squared_fro=nf2,
    checks=checks,failures=failures,full_quarter_test_decided=False,
    limitations=['No fresh direct residual regeneration; complete digest and pinned source inherited from559/561/569',
                'FFT locator and finite signed entry/basis/head-solve arithmetic remain unpaid',
                'No joint-tail matrix order, complementary coercivity or actual-Xi conclusion'])
outpath=BASE/'signed-mixed-audit-570.json'
outpath.write_text(json.dumps(result,indent=2)+'\n')
print('Audit570 checks:',len(checks),'failures:',len(failures))
for k in ['output','remote_input','predictor','local_trial_input','inverse_input']:
    print(k,scalar_results[k]['hi'])
print('Required finite covariance with rounded allowances: <=.045741; not certified')
print('Failures:',failures[:10],'; full certificate:',outpath.relative_to(BASE.parent.parent))
assert not failures
