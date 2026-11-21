"""Complete the unchanged C744b scalar using its audited enclosure input.

Directed interval contract is imported from certify-455.py (preserved).
The analytic tail certificate is proved in C744c; no float evaluation.
All omitted responses are either enclosed individually or paid by the
explicit decreasing rational-series remainder. No all-test sign claim.
"""
import hashlib
import json
import runpy
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'certify-455.py'
BASE = HERE / 'certificate-455.json'
lib = runpy.run_path(str(SOURCE))
I, A, PI = (lib[x] for x in ('I', 'A', 'PI'))
nums, den = lib['NUMERATORS'], lib['DENOMINATOR']
base = json.loads(BASE.read_text())

def saved(x):
    return I(x['lo'], x['hi'])

def mag(x):
    return max(x.lo.copy_abs(), x.hi.copy_abs())

def positive_power(x, p):
    out = I(1)
    for _ in range(p):
        out *= x
    return out

checks = []
def check(label, value):
    checks.append({'check': label, 'passed': bool(value)})
    assert value, label

check('exact unchanged witness', base['witness']['numerators'] == nums and
      base['witness']['denominator'] == den and len(nums) == 64)
check('unchanged a interval', base['constants']['a'] == A.json())
check('ten moments unchanged', len(base['all_physical_moments']) == 10 and
      {(r['cell'], r['sigma']) for r in base['all_physical_moments']} ==
      {(j,s) for j in range(5) for s in (1,-1)})
check('all nine prime powers unchanged', [r['n'] for r in base['prime_terms']] ==
      [2,3,4,5,7,8,9,11,13])
check('old response prefix complete', [r['j'] for r in base['all_response_projections']] == list(range(128)))
check('64 diagonal entries', [r['q'] for r in base['all_h_enclosures']] == list(range(64)))
# Exact rational check that the original total encloses all five saved terms.
term_lo = sum(Fraction(r['lo']) for r in base['terms'].values())
term_hi = sum(Fraction(r['hi']) for r in base['terms'].values())
check('original sum endpoints enclose all five terms',
      Fraction(base['energy']['lo']) <= term_lo and term_hi <= Fraction(base['energy']['hi']))

z = [I(n)/den for n in nums]
k = [q*PI/A for q in range(64)]
k2 = [x.sq() for x in k]
norm = [(I(1)/A).sqrt()] + [(I(2)/A).sqrt()]*63
d = [z[q]*norm[q]*((-1)**q) for q in range(64)]
s0 = sum(d, I(0))
a0 = I(mag(s0))
b1 = sum((I(mag(d[q]))*k2[q] for q in range(64)), I(0))
N = 2048
prefix = I(0)
rows = []
for j in range(128, N):
    c = I(4*j+1)/2
    projection = sum((d[q]*c/(c.sq()+k2[q]) for q in range(64)), I(0))
    projection *= (1-(-2*A*c).exp()).sqrt()
    energy = projection.sq()
    prefix += energy
    rows.append({'j':j, 'projection':projection.json(), 'energy':energy.json()})
cn = I(4*N+1)/2
series = {}
for p in (2,4,6):
    # For decreasing f(j)=c_j^(-p): sum >=N <= f(N)+int_N^infty f.
    series[p] = 1/positive_power(cn,p) + 1/(2*(p-1)*positive_power(cn,p-1))
tail_upper = a0.sq()*series[2] + 2*a0*b1*series[4] + b1.sq()*series[6]
tail = I(0,tail_upper.hi)
restored = prefix+tail
total = saved(base['energy']) + restored
check('every new prefix index', [r['j'] for r in rows] == list(range(128,N)))
check('positive tail upper bound', tail.hi > 0)
check('strict complete positive scalar', total.lo > 0)
result = {
    'status':'CERTIFIED_POSITIVE_COMPLETE_SCALAR',
    'scope':'One closed zero-extension penalized form value; no operator-domain or all-test positivity claim.',
    'inputs':{'certificate':BASE.name,'certificate_sha256':hashlib.sha256(BASE.read_bytes()).hexdigest(),
              'interval_source':SOURCE.name,'interval_source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              'canonical_result':'C744b','source_audit':'C744b step457'},
    'parameters':{'K':5,'penalty':256,'unchanged_dyadic_witness':True,'old_response_end':128,'new_response_end_exclusive':N},
    'witness':base['witness'], 'constants':{'a':A.json()},
    'original_terms':base['terms'], 'original_energy':base['energy'],
    'additional_response_prefix':prefix.json(), 'additional_response_rows':rows,
    'tail_proof_data':{'c_N':cn.json(),'S0':s0.json(),'A0_upper':str(a0.hi),'B1':b1.json(),
                      'series_upper_bounds':{str(p):x.json() for p,x in series.items()},
                      'formula':'A0^2*T2+2*A0*B1*T4+B1^2*T6; Tp=cN^-p+cN^(1-p)/(2*(p-1))'},
    'all_remaining_response_tail':tail.json(), 'complete_restored_response_mass':restored.json(),
    'complete_penalized_energy':total.json(), 'required_threshold':'0; scalar interval must exclude it',
    'checks':checks,'failures':[r['check'] for r in checks if not r['passed']]
}
out = HERE/'complete-response-459.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print('Restored response mass:',restored.json())
print('Remaining response tail: [0,',tail.hi,']')
print('Complete penalized energy:',total.json(),'; required interval excluding 0')
print('Result:',result['status'],'; failures:',result['failures'],'; full certificate:',out)
