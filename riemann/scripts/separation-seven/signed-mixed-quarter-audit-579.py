#!/usr/bin/env python3
"""Bounded audit replay of C999m Sections12-17, preserving all inputs.

Replays complete571/572/573 calculations up to their first artifact write,
checks complete574 ledgers and difference arrays, and reruns the complete
575/576 evidence inspections without overwriting their evidence. This is
not an independent65536-square entry/product replay. Conceptual justification
and retained contracts are recorded in C999m Section18.
"""
import hashlib
import json
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
checks, failures, results, pins = [], [], {}, {}

def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        failures.append(label)

def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(8*1024*1024), b''):
            h.update(block)
    return h.hexdigest()

def read(stem):
    path = BASE/(stem+'.json')
    pins[path.name] = sha(path)
    rec = json.loads(path.read_text())
    check(not rec['failures'] and all(c['passed'] for c in rec['checks']), stem+' complete original checks')
    skey = 'script_sha256' if 'script_sha256' in rec else 'source_sha256'
    check(sha(BASE/(stem+'.py')) == rec[skey], stem+' source pin')
    for name, digest in rec['input_hashes'].items():
        check(sha(BASE/name) == digest, stem+' input '+name)
    archives = rec.get('archives', {})
    if 'archive' in rec:
        archives = {Path(rec['archive']['path']).name: rec['archive']}
    for name, item in archives.items():
        check(sha(BASE/name) == item['sha256'], stem+' full archive '+name)
    return rec

def execute_prefix(name, stop):
    path = BASE/name
    source = path.read_text()
    assert source.count(stop) == 1
    ns = {'__file__': str(path), '__name__': 'replay579'}
    exec(compile(source.split(stop)[0], str(path), 'exec'), ns)
    for item in ns['checks']:
        check(item['passed'], name+': '+item['label'])
    return ns

def arrays_equal(actual, saved, names, label):
    for a, b in names:
        check(np.array_equal(actual[a], saved[b]), label+' complete '+b)

stems = ['signed-mixed-joint-input-571','signed-mixed-finite-center-572',
         'signed-mixed-head-defect-573','signed-mixed-complement-inverse-574',
         'signed-mixed-direct-action-575','signed-mixed-inverse-action-576']
records = {i: read(stem) for i, stem in zip(range(571,577), stems)}
print('Pinned complete571-576 inputs; failures:',failures,flush=True)

n = execute_prefix(stems[0]+'.py', "archive = BASE/'signed-mixed-joint-input-571.npz'")
with np.load(BASE/(stems[0]+'.npz')) as a:
    arrays_equal(n,a,[('mc','comparison'),('qhat','majorant_center'),('target','target'),
                     ('combined','combined_boundary_rows')],'571')
    for key, gram in n['grams'].items():
        check(np.array_equal(gram,a[key+'_gram']),'571 full Gram '+key)
    factor=a['factor']
    residual=float(np.linalg.norm(n['target']-factor@factor.T))
    check(residual<1e-7 and float(np.sum(factor*factor))<100000,'571 saved full factor reconstruction')
results['571'] = dict(tail=n['tail'].json(), factor_error=n['factor_error'].json(),
                     saved_factor_residual=residual, grams=len(n['grams']))
check(n['tail'].hi<n['Decimal']('.151'),'571 complete input norm <.151')
print('571 complete majorant replay passed:',not failures,flush=True)
del n

n = execute_prefix(stems[1]+'.py', "archive = BASE/'signed-mixed-finite-center-572.npz'")
with np.load(BASE/(stems[1]+'.npz')) as a:
    arrays_equal(n,a,[('mc','comparison'),('gram','center_covariance'),('rhat','neutral_ratio_center'),
        ('weights','upward_inverse_sqrt_weight'),('dlo','d_lower'),('dhi','d_upper'),
        ('rlo','r_lower'),('rhi','r_upper')],'572')
    factor=a['factor']
    residual=float(np.linalg.norm(n['target']-factor@factor.T))
    check(residual<1e-7 and float(np.sum(factor*factor))<100000,'572 saved complete factor reconstruction')
check(n['digest'].hexdigest()==records[572]['combined_weighted_rows_sha256'],'572 every weighted row replay')
results['572'] = dict(scalar_rows=len(n['rhat']),gram_blocks=2*len(n['blocks']),
    row_error=n['row_error'].json(),factor_error=n['total_error'].json(),saved_factor_residual=residual)
print('572 complete coordinate/Gram replay passed:',not failures,flush=True)
del n

n = execute_prefix(stems[2]+'.py', "archive=BASE/'signed-mixed-head-defect-573.npz'")
with np.load(BASE/(stems[2]+'.npz')) as a:
    for key,obj in [('m',n['mm']),('t',n['tt']),('h',n['hh'])]:
        check(np.array_equal(obj.lo,a[key+'_lower']) and np.array_equal(obj.hi,a[key+'_upper']),
              '573 every '+key+' enclosure entry replay')
    arrays_equal(n,a,[('m','m_center'),('t','t_center'),('h','h_center'),('rho','exact_proxy_head_residual_center'),
                     ('defect','defect'),('xhat','head_solution')],'573')
    correction=a['correction']
    correction_residual=n['fro_upper'](n['defect']-n['h']@correction)
    check(correction_residual<1e-16,'573 saved complete correction residual')
    target=n['mc']-(correction/.0005).T@(correction/.0005)-1e-6*np.eye(1020)
    factor=a['factor']
    residual=n['fro_upper'](target-factor@factor.T)
    check(residual<1e-7 and n['fro_upper'](factor)**2<100000,'573 saved full correction factor')
check(n['mixed_head'].hi<n['Decimal']('.001556'),'573 complete head error <.001556')
results['573'] = dict(head_enclosure_entries=3*512**2,head_error=n['mixed_head'].json(),
    defect_error=n['defect_error'].json(),saved_correction_residual=correction_residual,saved_factor_residual=residual)
I, fro, Decimal = n['I'], n['fro_upper'], n['Decimal']
print('573 complete head-entry/defect replay passed:',not failures,flush=True)
del n

# Independently reassemble every574 block error and inspect every difference.
rec=records[574]
iv=lambda a:I(a['lo'],a['hi'])
u=I(1)/2**53
gamma=lambda k:k*u/(1-k*u)
f={key:I(value) for key,value in rec['complete_factor_norms'].items()}
dif=np.load(BASE/'signed-mixed-complement-inverse-difference-574.npy',mmap_mode='r')
total=I(0)
for j,b in enumerate(rec['blocks']):
    first,last=b['first'],b['last']
    check(first==512*(j+1) and last==first+511 and b['full_entry_count_each']==512**2,'574 full block coverage '+str(j))
    r={key:I(value) for key,value in b['matrix_radius_fro'].items()}
    c={key:I(value) for key,value in b['matrix_center_fro'].items()}
    entry=(r['T']+r['Tstar'])*I('1.008')+r['local']*I('1.008')*I('1.320001')
    basis=(c['T']+c['Tstar']+r['T']+r['Tstar']+(c['local']+r['local'])*I('1.320001'))*I('1e-14')
    ar=gamma(4096)*((c['T']+c['Tstar'])*f['z']+c['local']*f['z']*f['y']+1)
    am,ae=iv(b['inverse_max']),iv(b['inverse_radius_max'])
    err=am*(entry+basis+ar)+ae*c['residual']+gamma(8)*(am*c['residual']+c['old_inverse']+1)
    q=I(b['inverse_center_difference_fro'])+err
    check(entry.json()==b['exact_residual_entry_error'] and basis.json()==b['exact_basis_error']
          and ar.json()==b['complete_product_rounding'] and err.json()==b['complete_inverse_center_error']
          and q.json()==b['exact_block_difference_bound'],'574 entire block arithmetic '+str(j))
    values=np.array(dif[first-512:last+1-512])
    check(np.all(np.isfinite(values)) and fro(values)<=b['inverse_center_difference_fro']
          and hashlib.sha256(values.tobytes()).hexdigest()==b['combined_difference_sha256'],
          '574 every saved difference '+str(j))
    total+=q*q
zeta=(1/I('6.14')+4/(3*I('6.14')*511**3)).sqrt()
mixed=zeta*I(2).sqrt()*I('4.71')*total.sqrt()/I('.000999').sqrt()
check(len(rec['blocks'])==127 and mixed.hi<Decimal('.000002'),'574 complete complementary error <.000002')
check(mixed.json()==rec['scalars']['normalized_mixed_contribution'],'574 complete scalar result reproduced')
results['574']=dict(blocks=len(rec['blocks']),raw_error=total.sqrt().json(),mixed_error=mixed.json())
print('574 complete block/error evidence passed:',not failures,flush=True)

for number,name,stop in [
    (575,'check-signed-mixed-direct-action-575.py','out = dict(scope=__doc__'),
    (576,'check-signed-mixed-inverse-action-576.py',"out=dict(scope='complete evidence inspection")]:
    n=execute_prefix(name,stop)
    if number==575:
        results[str(number)]=dict(blocks=len(n['record']['blocks']),mixed_error=n['mixed'].json())
    else:
        results[str(number)]=dict(matrix_blocks=len(n['record']['matrix_blocks']),
            difference_blocks=len(n['record']['difference_blocks']),action_error=n['eta'].json(),
            finite=n['finite'].json(),whole=n['whole'].json(),covariance=(n['whole']*n['whole']).json())
    print(number,'complete saved-evidence replay passed:',not failures,flush=True)

out=dict(scope=__doc__,checks=checks,failures=failures,results=results,input_certificates=pins,
         source_sha256=sha(Path(__file__)),
         limitations=['No independent complete574-576 interval-entry/product replay',
             'Complete production sources reviewed conceptually in C999m Section18',
             'Inherited execution/analytic/whole-core/c_* contracts retained',
             'No endpoint-complement coercivity or RH conclusion'])
path=BASE/'signed-mixed-quarter-audit-579.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('Audit checks:',len(checks),'failures:',failures,flush=True)
print('Full mixed norm:',results['576']['whole']['hi'],'required <.5',flush=True)
print('Certificate:',path.relative_to(BASE.parent.parent),flush=True)
assert not failures
