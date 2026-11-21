#!/usr/bin/env python3
"""Inspect every saved575 block, ledger, prime record and artifact pin.

This checks complete saved evidence; it is not an independent entry replay
or conceptual audit of C999m Sections12-16.
"""
import hashlib
import importlib.util
import json
from decimal import Context, Decimal, ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN
from pathlib import Path
import numpy as np

BASE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('iv_check575', BASE/'complete-schur-531.py')
iv = importlib.util.module_from_spec(spec)
spec.loader.exec_module(iv)
iv.DOWN = Context(prec=80, rounding=ROUND_FLOOR)
iv.UP = Context(prec=80, rounding=ROUND_CEILING)
iv.NEAR = Context(prec=80, rounding=ROUND_HALF_EVEN)
I = iv.I
record = json.loads((BASE/'signed-mixed-direct-action-575.json').read_text())
checks, failures = [], []

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

def interval(data):
    return I(data['lo'], data['hi'])

check(len(record['checks']) == 1111 and not record['failures']
      and all(c['passed'] for c in record['checks']), 'all1111 production flags')
check(sha(BASE/'signed-mixed-direct-action-575.py') == record['source_sha256'], 'source pin')
for name, digest in record['input_hashes'].items():
    check(sha(BASE/name) == digest, 'input pin '+name)
for name, artifact in record['archives'].items():
    check(sha(BASE/name) == artifact['sha256'], 'complete artifact pin '+name)
u = I(1)/2**53
gamma = lambda n: n*u/(1-n*u)
f = {name: I(value) for name,value in record['full_factor_norms'].items()}
ev = I('1e-14')*I('1.320001')+gamma(1024)*(f['z']*f['y']+f['xhat']+1)
check(ev.json() == record['scalars']['raw_predictor_center_error'], 'entire raw-predictor ledger')
rows = np.load(BASE/'signed-mixed-direct-center-575.npy', mmap_mode='r')
check(rows.shape == (2,65536,1020), 'complete direct-center shape')
total = I(0)
for number, block in enumerate(record['blocks']):
    first, last = block['first'], block['last']
    e = {name: I(value) for name,value in block['radius_fro'].items()}
    c = {name: I(value) for name,value in block['center_fro'].items()}
    entry = (2*e['L']+e['U']+e['Ustar'])*I('1.008')+(e['T']+e['Tstar'])*(f['vcenter']+ev)
    basis = (2*c['L']+c['U']+c['Ustar'])*I('1e-14')+(c['T']+c['Tstar'])*ev
    rounding = gamma(4096)*((2*c['L']+c['U']+c['Ustar'])*f['z']+(c['T']+c['Tstar'])*f['vcenter']+1)
    q = entry+basis+rounding
    check(first == 512*number and last == first+511 and block['entries_per_operator'] == 512**2
          and entry.json() == block['entry_error'] and basis.json() == block['basis_and_raw_predictor_error']
          and rounding.json() == block['complete_product_rounding'] and q.json() == block['combined_pair_error'],
          'entire block error ledger '+str(first))
    values = [np.array(rows[side,first:last+1]) for side in range(2)]
    digest = hashlib.sha256(values[0].tobytes()+values[1].tobytes()).hexdigest()
    check(all(np.all(np.isfinite(a)) for a in values) and digest == block['center_pair_sha256'],
          'every saved direct-center row '+str(first))
    if number:
        weight = interval(block['first_weight'])
        check(weight.lo > Decimal('6.14'), 'positive weight '+str(first))
        total += q*q/weight
    else:
        q0 = q
check(len(record['blocks']) == 128, 'all128 output blocks')
raw = total.sqrt()
low = (4/(3*I('6.14')*511**3)).sqrt()*q0
mixed = (raw+low)/I('.000999').sqrt()
check(raw.json() == record['scalars']['weighted_raw_tail_error']
      and low.json() == record['scalars']['weighted_low_error']
      and mixed.json() == record['scalars']['normalized_direct_error'], 'complete directed sum and low correction')
primes = record['complete_prime_records']
groups = {str(s): {str(sign): sum(p['separation'] == s and p['sign'] == sign for p in primes)
                   for sign in [-1,0,1]} for s in [7,14]}
check(len(primes) == 350 and sum(groups['7'].values()) == 16
      and groups['14'] == {'-1':206,'0':1,'1':127}, 'all prime delay cases')
check(mixed.hi < Decimal('.000001'), 'achieved bound permits reservation .000001')
remaining = I('.004204')-I('.001556')-I('.000002')-I('.000001')
check(remaining.lo == Decimal('.002645'), 'unchanged total budget leaves .002645')
out = dict(scope=__doc__, production_checks=len(record['checks']), checks=checks, failures=failures,
           complete_block_count=len(record['blocks']), complete_prime_groups=groups,
           normalized_direct_error=mixed.json(), required_direct_upper='.00001',
           valid_tighter_reservation='.000001', remaining_inverse_action_allowance=remaining.json(),
           input_certificate_sha256=sha(BASE/'signed-mixed-direct-action-575.json'),
           source_sha256=sha(Path(__file__)))
path = BASE/'signed-mixed-direct-action-check-575.json'
path.write_text(json.dumps(out,indent=2)+'\n')
print('Complete evidence checks:',len(checks),'failures:',failures)
print('Actual normalized direct upper:',mixed.hi,'; required .00001; reservation .000001; remaining .002645')
print('Evidence:',path.relative_to(BASE.parent.parent))
