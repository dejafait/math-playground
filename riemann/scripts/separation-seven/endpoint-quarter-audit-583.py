#!/usr/bin/env python3
"""Audit frozen C999n; never rerun selection or overwrite prior evidence.

Full entry replay, integer prime enumeration, exact dyadic scalar products,
exact rational reference checks and directed final bounds. Analytic entry
accuracy retains C744v/w's stated contracts; array agreement alone is not
an analytic error certificate. No inverse, eigensolver or FFT is executed.
"""
import contextlib
import hashlib
import io
import json
import math
from decimal import Decimal
from fractions import Fraction as Q
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
OUT = BASE / 'endpoint-quarter-audit-583.json'
checks, details = [], {}


def check(ok, label):
    checks.append(dict(label=label, passed=bool(ok)))
    if not ok:
        raise AssertionError(label)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def execute_prefix(name, marker):
    path = BASE / name
    source = path.read_text()
    check(source.count(marker) == 1, 'unique non-writing replay boundary ' + name)
    env = {'__file__': str(path), '__name__': 'audit583_replay'}
    capture = io.StringIO()
    with contextlib.redirect_stdout(capture):
        exec(compile(source.split(marker)[0], str(path), 'exec'), env)
    details[name + '_stdout'] = capture.getvalue()
    return env


def dyadic_vector(v):
    ratios = [float(x).as_integer_ratio() for x in v]
    den = max(d for _, d in ratios)
    return [n * (den // d) for n, d in ratios], den


def exact_dot(x, matrix, y):
    # Every float is used as its exact binary rational, with integer sums.
    xn, xd = dyadic_vector(x)
    yn, yd = dyadic_vector(y)
    value = Q(0)
    for xi, row in zip(xn, matrix):
        mn, md = dyadic_vector(row)
        value += Q(xi * sum(m * yj for m, yj in zip(mn, yn)), xd * md * yd)
    return value


def main():
    old_path = BASE / 'endpoint-complement-certificate-581.json'
    old = json.loads(old_path.read_text())
    pins = {p: digest(BASE / p) for p in [
        'endpoint-complement-locator-581.npz', 'endpoint-complement-locator-581.json',
        'endpoint-complement-locator-581.py', 'endpoint-complement-certificate-581.py',
        'endpoint-complement-certificate-581.json', 'complete-covariance-532.npz',
        'response-prefix-stop-546.json', 'residual-certificate-532.py',
        'complete-schur-531.py']}
    check(old['script_sha256'] == pins['endpoint-complement-certificate-581.py'],
          'original verifier source pin')
    # Stop before any file write. This executes the complete scalar certificate.
    r = execute_prefix('endpoint-complement-certificate-581.py', "out=BASE/'endpoint-complement-certificate-581.json'")
    check(r['result'] == old, 'complete original certificate replay equality')
    checks.extend(r['checks'])
    I, a = r['I'], r['a']

    def qi(value):
        return I(value.numerator) / value.denominator

    def contains(interval, value):
        return Q(interval.lo) <= value <= Q(interval.hi)

    # Reconstruct all operator entries, stopping before Z, eigenvectors or files.
    p = execute_prefix('endpoint-complement-locator-581.py', '# Exact object Z')
    data = r['data']
    idx = np.r_[0, 1, np.arange(512, 1024)]
    check(np.array_equal(idx, data['physical_index_set']), 'every physical index')
    expected_shapes = dict(local_matrix=(514,514), t_entries=(1024,514),
        ts_entries=(1024,514), u_entries=(514,514), reference_head=(512,512),
        diagonal=(1024,), raw_f_center=(514,), raw_h_center=(514,),
        free_numerators=(1024,), trial_numerators=(1024,))
    for key, shape in expected_shapes.items():
        check(data[key].shape == shape, 'complete shape ' + key)
    for key, value in dict(local_matrix=p['L'], t_entries=p['T'],
                          ts_entries=p['Ts'], u_entries=p['U'][idx],
                          diagonal=p['D']).items():
        check(np.array_equal(value, data[key]), 'every reconstructed entry ' + key)
    details['entry_counts'] = {key: int(data[key].size) for key in
        ['local_matrix','t_entries','ts_entries','u_entries','diagonal']}
    for key in ['free_numerators','trial_numerators']:
        check(data[key].dtype.kind == 'i' and np.max(np.abs(data[key])) < 2**53,
              'exact int64 to binary64 conversion ' + key)
        check(np.count_nonzero(data[key]) == 1024, 'all1024 nonzero ' + key)
    check(np.array_equal(data['raw_f_center'][2:], data['free_numerators'][:512]/2**40)
          and np.array_equal(data['raw_h_center'][2:], data['free_numerators'][512:]/2**40),
          'all free physical coefficients are unchanged dyadics')

    # A separate prime-base enumeration with exact integer boundaries.
    prime_list = []
    for prime in range(2, 3784):
        if any(prime % d == 0 for d in range(2, math.isqrt(prime)+1)):
            continue
        v = prime
        while v*v < 3**15:
            if v*v > 3**13:
                prime_list.append((v, prime))
            v *= prime
    prime_list.sort()
    check(prime_list == p['powers'] and len(prime_list) == 334,
          'independent exact enumeration of all334 remote powers')
    check([(v,pp) for v,pp in prime_list if v*v == 3**14] == [(2187,3)],
          'unique exact zero remote delay')
    near = []
    for (v, prime), dc, wc in zip(prime_list, p['delays'], p['weights']):
        di = I(0) if v == 2187 else 14*r['ell']-I(v).ln()
        wi = I(prime).ln()/I(v).sqrt()
        check(r['absmax'](di-r['exact'](dc)) < Decimal('1e-16') and
              r['absmax'](wi-r['exact'](wc)) < Decimal('1e-16'),
              'actual generator constants ' + str(v))
        check(r['absmax'](di) < r['ell'].lo, 'strict overlap ' + str(v))
        check(v == 2187 or di.lo*di.hi > 0, 'delay sign separated from zero ' + str(v))
        near.append(dict(n=v, prime=prime, delay=di.json(), weight=wi.json()))
    details['remote_constants'] = near
    identity = p['shift'](0.)
    expected = np.zeros((1024,514)); expected[idx,np.arange(514)] = 1.
    check(np.array_equal(identity, expected), 'all exact zero-shift identity entries')
    # Adjoint comparisons are diagnostic formula checks, not analytic accuracy.
    details['adjoint_center_discrepancies'] = {
        'T': float(np.max(np.abs(p['T'][idx]-p['Ts'][idx].T))),
        'U': float(np.max(np.abs(p['U'][idx]-p['Us'][idx].T)))}
    for name,value in details['adjoint_center_discrepancies'].items():
        check(value < 1e-12, 'complete adjoint center check ' + name)

    pi, ell = r['pi'], r['ell']
    kmax = 1023*pi/ell
    gap = pi/ell
    ratio = Q(1023**2+1022**2, 1023**2-1022**2)
    check(ratio < 1024, 'exact maximal unequal-index cancellation ratio')
    rmax = I(2).sqrt()/(6*I('64.25')*I('64.25'))
    cj = I('131072.5')
    diag_error = 1/(cj*cj)+2*kmax*kmax*(1/(6*cj*cj*cj)+1/(cj*cj*cj*cj))
    off_error = 4*rmax/gap
    response_tail = I(8)/(3**64)/(1-I(1)/3)/(I('128.5')*I('128.5'))
    # Row/column-integral bound for c>=16.5 at separation7.
    continuous_tail = I(1)/(3**49*I(3).sqrt()*I('16.5')*(1-I(1)/729))
    shift_argument = I(4)*1025*I('1e-14')*r['wsum']
    local_cap = rmax + 8*diag_error + off_error + I('1e-7') + response_tail
    reference_tail_cap = (rmax+I('1e-7'))/2
    u = I(1)/2**53
    gamma = 1024*u/(1-1024*u)
    dot_cap = 400*(2*gamma+gamma*gamma)
    ledger = dict(kmax=kmax, minimum_frequency_gap=gap, rmax=rmax,
        diagonal_before_normalization=diag_error, off_diagonal_error=off_error,
        exponential_response_tail=response_tail, cross_continuous_tail=continuous_tail,
        prime_argument_error=shift_argument, local_entry_cap=local_cap,
        reference_tail_cap=reference_tail_cap, two_dot_cap=dot_cap)
    for label,value,bound in [
        ('frequency gap',I('5.7')/gap,1),
        ('rmax',rmax,'.000058'), ('diagonal error',diag_error,'6e-9'),
        ('response tail',response_tail,'1e-30'),
        ('continuous tail',continuous_tail,'1e-24'),
        ('prime argument',shift_argument,'2.2e-9'),
        ('local entry',local_cap,'.001'),
        ('reference tail',reference_tail_cap,'.00005'),
        ('two dot errors',dot_cap,'1e-8')]:
        check(value.hi < Decimal(bound), 'directed uniform ledger ' + label)
    details['analytic_ledger'] = {name:value.json() for name,value in ledger.items()}

    # Check the full rational definition of H, not merely its floating replay.
    with np.load(BASE/'complete-covariance-532.npz') as z:
        mh,ch = z['m0'].copy(),z['cov00'].copy()
    H = data['reference_head']
    max_herr = Q(0)
    for i in range(512):
        for j in range(512):
            exact_h = Q(float(mh[i,j])) - Q(100,307)*Q(float(ch[i,j]))
            if i == j:
                exact_h -= Q(3,12500)+Q(100,307)*Q(23,5000)
            max_herr = max(max_herr, abs(Q(float(H[i,j]))-exact_h))
    check(max_herr < Q(1,10**10), 'all262144 exact rational head assembly errors')
    details['reference_head_max_exact_error'] = qi(max_herr).json()

    f,h,t = data['raw_f_center'],data['raw_h_center'],r['tc']
    products = {}
    for name,x,m,y in [('fLf',f,data['local_matrix'],f),
                       ('hLh',h,data['local_matrix'],h),
                       ('hUf',h,data['u_entries'],f),
                       ('tTf',t,data['t_entries'],f),
                       ('tTsh',t,data['ts_entries'],h),
                       ('tHt',t[:512],H,t[:512])]:
        products[name] = exact_dot(x,m,y)
        check(contains(r['dot_center'](x,m,y), products[name]),
              'original dot enclosure contains exact integer product ' + name)
    details['exact_dyadic_products'] = {name:dict(
        numerator=str(value.numerator), denominator=str(value.denominator),
        enclosure=qi(value).json()) for name,value in products.items()}
    # Independent exact rational head energy from original m0/cov00.
    head_exact = exact_dot(t[:512],mh,t[:512])-Q(100,307)*exact_dot(t[:512],ch,t[:512])
    head_exact -= (Q(3,12500)+Q(100,307)*Q(23,5000))*sum((Q(float(x))**2 for x in t[:512]),Q(0))
    tail_exact = sum((Q(float(data['diagonal'][n]))*Q(float(t[n]))**2/2
                      for n in range(512,1024)),Q(0))
    endpoint = r['inflate'](qi(products['fLf']+products['hLh']-2*products['hUf']),r['endpoint_error'])
    pairing = r['inflate'](qi(products['tTf']+products['tTsh']),r['pair_error'])
    # Retain the existing (larger) allowance, although head assembly is now exact.
    energy = r['inflate'](qi(head_exact+tail_exact),r['ref_error'])
    check(energy.lo > 0 and pairing.lo > 0, 'independent positive denominator and pairing')
    quotient = r['square'](pairing)/energy
    result = endpoint-quotient-r['wnorm']/4
    check(result.hi < Decimal('-.11797'), 'independent upper strictly below-.11797 and0')
    details['independent_bounds'] = {name:value.json() for name,value in dict(
        endpoint=endpoint,pairing=pairing,reference_energy=energy,
        inverse_lower_quotient=quotient,weighted_free_norm_squared=r['wnorm'],
        difference_upper_expression=result).items()}
    details['neutral_low_intervals'] = {'f':[x.json() for x in r['f'][:2]],
                                       'h':[x.json() for x in r['h'][:2]]}
    details['full_neutral_ratios'] = [x.json() for x in r['r']]
    details['full_tail_weights'] = [x.json() for x in r['weights']]
    details['l1_bounds'] = {name:r[name].json() for name in ['lf','lh','lt','df','dh']}
    for name,threshold in [('lf','1.442'),('lh','1.442'),('lt','.987')]:
        check(r[name].hi < Decimal(threshold), 'full coefficient bound ' + name)
    for name,old_digest in pins.items():
        check(digest(BASE/name) == old_digest, 'prior artifact preserved ' + name)
    details['input_hashes'] = pins
    return str(result.hi)


upper = None
try:
    upper = main()
except Exception as error:
    details['exception'] = repr(error)
    if not any(not c['passed'] for c in checks):
        checks.append(dict(label='audit execution',passed=False))
finally:
    failures = [c['label'] for c in checks if not c['passed']]
    OUT.write_text(json.dumps(dict(
        audit_passed=not failures, checks=checks, failures=failures,
        actual_upper=upper, required_upper_strictly_below='0',
        scope='frozen C999n; conditional analytic/IEEE754/Decimal computational audit',
        limitation='No actual triple sign; no RH conclusion; no new source theorem; array equality alone is not analytic verification.',
        script_sha256=digest(Path(__file__)), details=details),indent=2)+'\n')
    print(f'Audit passed={not failures}; checks={len(checks)}; failures={failures}')
    print(f'Actual upper={upper}; required<0; certificate={OUT.relative_to(BASE.parent.parent)}')
if failures:
    raise SystemExit(1)
