#!/usr/bin/env python3
"""C919o audit: independent base bounds plus complete preserved-source replay.

Shares the explicitly trusted Decimal backend; does not verify that backend.
All original2236 sources/artifacts are read-only. Full results are saved.
"""
import decimal
from decimal import Decimal as D
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'joint_kernel_audit_2238.json'
REPLAY = ROOT / 'audit2238-replay'
started = time.monotonic()
counts, failures, records = {}, [], []


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(category, ok, where):
    counts[category] = counts.get(category, 0) + 1
    if not ok:
        failures.append(dict(category=category, where=where))


def read(name, root=ROOT):
    return json.loads((root / name).read_text())


def contains(saved, a, b):
    if isinstance(saved, dict):
        saved = [saved['lower'], saved['upper']]
    return F(saved[0]) <= F(a) <= F(b) <= F(saved[1])


ctx = {}
for key, rounding in [('lo', decimal.ROUND_FLOOR),
                      ('hi', decimal.ROUND_CEILING),
                      ('near', decimal.ROUND_HALF_EVEN)]:
    cc = decimal.Context(prec=110, rounding=rounding, Emin=-999999, Emax=999999)
    for sig in cc.traps:
        cc.traps[sig] = sig not in (decimal.Inexact, decimal.Rounded)
    cc.clear_flags()
    ctx[key] = cc
lo, hi, near = (ctx[k] for k in ('lo', 'hi', 'near'))


def rd(q, context):
    q = F(q)
    return context.divide(D(q.numerator), D(q.denominator))


def prod(*vals):
    out = D(1)
    for v in vals:
        assert v >= 0
        out = hi.multiply(out, v)
    return out


def total(vals):
    out = D(0)
    for v in vals:
        assert v >= 0
        out = hi.add(out, v)
    return out


def exp_lo(v):
    return lo.next_minus(near.exp(v))


def exp_hi(v):
    return hi.next_plus(near.exp(v))


p = read('joint_kernel_preflight_2236.json')
n = read('joint_kernel_nodes_2236.json')
c = read('joint_kernel_2236.json')
oldcheck = read('joint_kernel_inspection_2236.json')

# Exact alternating arctangent sums and remainder intervals.
def atan(q, count):
    terms = [F(1, (2*k+1)*q**(2*k+1)) for k in range(count+1)]
    value = sum(((-1)**k*terms[k] for k in range(count)), F(0))
    other = value + (-1)**count*terms[count]
    return min(value, other), max(value, other)


a, b = atan(5, 80), atan(239, 25)
pil, pir = 16*a[0]-4*b[1], 16*a[1]-4*b[0]
check('pi', [F(z) for z in p['constants']['exact_pi_bounds']] == [pil, pir], 'exact Machin bounds')
check('pi', contains(p['constants']['pi'], pil, pir), 'outward conversion')
check('pi', 3 < pil < pir < F(22, 7) and pir**2 < 10, 'tail constants')
pl, pr = rd(pil, lo), rd(pir, hi)
itail = prod(D(15000000), exp_hi(D(-75)))
stail = prod(rd(F(200,768), hi), exp_hi(D(-384)))
check('tail', F(p['constants']['index_factor']) >= F(itail), 'index factor')
check('tail', F(p['constants']['space_tail']) >= F(stail), 'spatial tail')
records.append(dict(kind='constants', index_upper=str(itail), space_upper=str(stail)))

# Independently organized positive Bell recurrence, not copied closed formulas.
for k, row in enumerate(p['space']):
    l, r = rd(F(k,256), lo), rd(F(k+1,256), hi)
    el, er = exp_lo(lo.multiply(D(2),l)), exp_hi(hi.multiply(D(2),r))
    envelope = [D(0)]*5
    for nn in range(1,5):
        al, ar = lo.multiply(pl,D(nn*nn)), hi.multiply(pr,D(nn*nn))
        vl, vr = lo.multiply(al,el), hi.multiply(ar,er)
        for slope, prefactor in [(D('4.5'),prod(D(8),ar,ar)),
                                 (D('2.5'),prod(D(12),ar))]:
            e0 = prod(prefactor,exp_hi(hi.subtract(prod(slope,r),vl)))
            ad = [total([slope,prod(D(2),vr)]),prod(D(4),vr),
                  prod(D(8),vr),prod(D(16),vr)]
            bell = [D(1)]
            for order in range(4):
                bell.append(total(prod(D(comb(order,j)),bell[order-j],ad[j])
                                  for j in range(order+1)))
            envelope = [total([old,prod(e0,bv)]) for old,bv in zip(envelope,bell)]
    for j in range(5):
        check('base_envelope', F(row['E'][j]) >= F(envelope[j]), [k,j])
    records.append(dict(kind='base_envelope', cell=k, upper=list(map(str,envelope))))

# Exact polynomial and remainder reconstruction for the two small-angle steps.
for q, center in enumerate([F(57,4),F(43,2)]):
    theta = center/F(16384)
    cosine = sum(((-1)**j*theta**(2*j)/factorial(2*j) for j in range(16)),F(0))
    sine = sum(((-1)**j*theta**(2*j+1)/factorial(2*j+1) for j in range(16)),F(0))
    rem = theta**32/factorial(32)
    saved = n['trig_steps'][q]
    check('trig_step', 0 < theta < F(1,500), q)
    check('trig_step', F(saved[2]) >= rem, [q,'remainder'])
    check('trig_step', contains(saved[0],cosine-rem,cosine+rem), [q,'cosine'])
    check('trig_step', contains(saved[1],sine-rem,sine+rem), [q,'sine'])
    records.append(dict(kind='trig_step', family=q, angle=str(theta), remainder=str(rem)))

for context, cc in ctx.items():
    check('reconstruction_runtime', all(not flag for sig,flag in cc.flags.items()
          if sig not in (decimal.Inexact,decimal.Rounded)), context)

# Preserve byte-identical sources in a dedicated directory. Their __file__
# changes only the output directory; no evaluator or inspector code is edited.
REPLAY.mkdir(exist_ok=True)
provenance = []
for name in ['joint_kernel_2236.py','inspect_joint_kernel_2236.py']:
    destination = REPLAY/name
    if destination.exists():
        raise RuntimeError('Replay destination already exists: '+str(destination))
    shutil.copyfile(ROOT/name,destination)
    provenance.append(dict(source=name,copy=str(destination.relative_to(ROOT)),
                           source_sha256=digest(ROOT/name),copy_sha256=digest(destination)))
(REPLAY/'provenance.json').write_text(json.dumps(dict(sources=provenance,
    transformation='None: byte-identical copies, __file__ selects the new output directory.'),indent=2)+'\n')

def save(status):
    result = dict(status=status,counts=counts,checks=sum(counts.values()),failures=failures,
        reconstruction=records,precision=110,contexts={k:str(v) for k,v in ctx.items()},
        original_artifact_hashes={name:digest(ROOT/name) for name in [
            'joint_kernel_preflight_2236.json','joint_kernel_nodes_2236.json',
            'joint_kernel_2236.json','joint_kernel_inspection_2236.json']},
        original_source_hashes={name:digest(ROOT/name) for name in [
            'joint_kernel_2236.py','inspect_joint_kernel_2236.py']},
        replay_provenance=provenance,minimum=c['uniform_margin']['lower'],
        claimed_lower='69/10000000000',required='1/10000000000',
        qualification='Reviewed mathematical argument and source; independent 110-digit base-envelope and exact step reconstruction; byte-identical evaluator/node replay and full exact-rational inspector reconstruction. Shared CPython/Fraction/libmpdec contracts; no backend verification.',
        elapsed_seconds=time.monotonic()-started)
    OUT.write_text(json.dumps(result,indent=2)+'\n')


save('BASE_CHECKED_REPLAY_PENDING')
print('Base reconstruction:',sum(counts.values()),'checks; failures:',len(failures),flush=True)
for name in ['joint_kernel_2236.py','inspect_joint_kernel_2236.py']:
    proc=subprocess.run([sys.executable,str(REPLAY/name)],stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT,text=True)
    (REPLAY/(name+'.log')).write_text(proc.stdout)
    check('replay_exit',proc.returncode == 0,name)
    print('Replay completed:',name,'exit:',proc.returncode,flush=True)
    if proc.returncode:
        save('FAIL')
        raise SystemExit(1)

rp=read('joint_kernel_preflight_2236.json',REPLAY)
rn=read('joint_kernel_nodes_2236.json',REPLAY)
rc=read('joint_kernel_2236.json',REPLAY)
ri=read('joint_kernel_inspection_2236.json',REPLAY)
# Compare every field other than explicitly listed run-specific values.
for label,old,new,omitted in [
    ('preflight',p,rp,{'runtime'}),('nodes',n,rn,{'runtime'}),
    ('certificate',c,rc,{'runtime','preflight_sha256','nodes_sha256'}),
    ('inspection',oldcheck,ri,{'elapsed_seconds','certificate_sha256'})]:
    check('complete_replay',set(old)==set(new),label+' keys')
    for key in sorted(set(old)|set(new)):
        if key not in omitted:
            check('complete_replay',old.get(key)==new.get(key),label+'/'+key)
    if 'runtime' in old:
        check('runtime',set(old['runtime'])==set(new['runtime']),label+' runtime keys')
        for key in old['runtime']:
            if key != 'elapsed_seconds':
                check('runtime',old['runtime'][key]==new['runtime'][key],label+'/'+key)
        check('runtime',not old['runtime']['unexpected_signals'] and
              not new['runtime']['unexpected_signals'],label+' signals')

for root, cert, inspection in [(ROOT,c,oldcheck),(REPLAY,rc,ri)]:
    for key,name in [('preflight_sha256',cert['preflight']),('nodes_sha256',cert['nodes']),
                     ('script_sha256','joint_kernel_2236.py')]:
        check('hash',cert[key]==digest(root/name),str(root/name))
    check('hash',inspection['certificate_sha256']==digest(root/'joint_kernel_2236.json'),
          str(root/'joint_kernel_2236.json'))
    check('hash',inspection['inspection_sha256']==digest(root/'inspect_joint_kernel_2236.py'),
          str(root/'inspect_joint_kernel_2236.py'))
    check('full_inspection',inspection['status']=='PASS' and not inspection['failures'] and
          inspection['checks']==sum(inspection['categories'].values())==464918,str(root))
    check('margin',F(inspection['minimum'])==F(cert['uniform_margin']['lower'])>
          F(69,10**10)>F(1,10**10),str(root))
check('full_inspection',ri['records_consumed']==dict(spatial=1024,suffix=256,
      node_snapshots=256,u=256,joint=131072),'all records')
save('PASS' if not failures else 'FAIL')
print('Result:','PASS' if not failures else 'FAIL','audit checks:',sum(counts.values()),
      'full rational checks:',ri['checks'],'failures:',len(failures),flush=True)
print('Actual lower:',c['uniform_margin']['lower'],'claimed > 6.9e-9; required > 1e-10',flush=True)
print('Certificate:',OUT,flush=True)
