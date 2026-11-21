"""Exact-rational consistency checks of the step459 interval certificate.

Checks aggregation and rational-tail arithmetic, not an independent
verification of elementary-function enclosures or the form-domain proof.
"""
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
path = HERE/'complete-response-459.json'
c = json.loads(path.read_text())
checks = []

def bounds(x):
    return F(x['lo']), F(x['hi'])

def check(label, condition):
    checks.append({'check':label, 'passed':bool(condition)})

def contains(x, pair):
    lo,hi = bounds(x)
    return lo <= pair[0] <= pair[1] <= hi

def total(xs):
    pairs = [bounds(x) for x in xs]
    return sum((x[0] for x in pairs),F(0)), sum((x[1] for x in pairs),F(0))

def square(x):
    lo,hi = bounds(x)
    return F(0) if lo<=0<=hi else min(lo*lo,hi*hi), max(lo*lo,hi*hi)

base_path = HERE/c['inputs']['certificate']
base = json.loads(base_path.read_text())
check('input certificate hash', hashlib.sha256(base_path.read_bytes()).hexdigest() == c['inputs']['certificate_sha256'])
check('interval source hash', hashlib.sha256((HERE/c['inputs']['interval_source']).read_bytes()).hexdigest() == c['inputs']['interval_source_sha256'])
check('unchanged original terms', c['original_terms'] == base['terms'])
check('unchanged original energy', c['original_energy'] == base['energy'])
check('unchanged witness', c['witness'] == base['witness'])
rows = c['additional_response_rows']
N = c['parameters']['new_response_end_exclusive']
check('complete additional prefix indices', [r['j'] for r in rows] == list(range(128,N)))
for r in rows:
    check('projection square j='+str(r['j']), contains(r['energy'],square(r['projection'])))
check('additional prefix sum', contains(c['additional_response_prefix'],total([r['energy'] for r in rows])))
d = c['tail_proof_data']
cn = F(2*N)+F(1,2)
check('exact c_N', bounds(d['c_N']) == (cn,cn))
sl,sh = bounds(d['S0'])
a0 = F(d['A0_upper']); b1 = bounds(d['B1'])[1]
check('A0 pays whole S0 interval', a0 >= max(abs(sl),abs(sh)))
check('nonnegative B1', bounds(d['B1'])[0] >= 0)
u = {p:cn**(-p)+cn**(1-p)/(2*(p-1)) for p in (2,4,6)}
for p in u:
    check('rational tail series p='+str(p),contains(d['series_upper_bounds'][str(p)],(u[p],u[p])))
upper = a0*a0*u[2]+2*a0*b1*u[4]+b1*b1*u[6]
check('whole rational tail paid', bounds(c['all_remaining_response_tail'])[0] == 0 and bounds(c['all_remaining_response_tail'])[1] >= upper)
check('restored mass aggregation',contains(c['complete_restored_response_mass'],total([c['additional_response_prefix'],c['all_remaining_response_tail']])))
check('complete scalar aggregation',contains(c['complete_penalized_energy'],total([c['original_energy'],c['complete_restored_response_mass']])))
lo,hi = bounds(c['complete_penalized_energy'])
check('strict complete scalar thresholds',F('2.0418e-7') < lo <= hi < F('2.1169e-7'))
rl,rh = bounds(c['complete_restored_response_mass'])
check('strict restored mass thresholds',F('2.2785e-7') < rl <= rh < F('2.3458e-7'))
failures = [r['check'] for r in checks if not r['passed']]
report = {'status':'PASS' if not failures else 'FAIL',
          'scope':'Exact-rational consistency; separate conceptual and algorithm audit pending.',
          'certificate':path.name,'certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
          'check_count':len(checks),'checks':checks,'failures':failures,
          'complete_penalized_energy':c['complete_penalized_energy'],
          'required_bounds':['2.0418e-7','2.1169e-7'],
          'tail_upper_exact_from_saved_majorants':str(upper)}
out = HERE/'complete-response-checks-459.json'
out.write_text(json.dumps(report,indent=2)+'\n')
print(report['status'],len(checks),'checks; failures:',failures)
print('Complete scalar:',c['complete_penalized_energy'],'; required:',report['required_bounds'])
print('Full consistency certificate:',out)
assert not failures
