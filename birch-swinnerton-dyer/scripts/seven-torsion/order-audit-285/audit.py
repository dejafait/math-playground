"""One aggregate audit; all original evidence remains read-only."""
from pathlib import Path
from fractions import Fraction
import hashlib, json, math, shutil, signal, subprocess, sys, time

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
PARENT = ROOT.parent
SOURCE = PARENT / 'nonmonic-order-283'
START = time.monotonic()
CAP = 134217728
STATE = {'status': 'INCOMPLETE', 'phase': 'inventory', 'failures': []}

def need(ok, label):
    if not ok: raise ValueError(label)

def size():
    return sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file())

def save(name, value):
    data = (json.dumps(value, separators=(',', ':'))+'\n').encode()
    need(size()+len(data)+32768 <= CAP, 'new_output_byte_cap')
    with (ROOT/name).open('xb') as f: f.write(data)

def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p): return json.loads(p.read_text())
def stop(*args): raise TimeoutError('aggregate_internal_180_seconds')

def run(args, logname):
    remaining = 180-(time.monotonic()-START)
    need(remaining>0, 'aggregate_time_remaining')
    with (ROOT/logname).open('x') as log:
        result = subprocess.run([sys.executable, '-B']+args, stdout=log,
                                stderr=subprocess.STDOUT, timeout=remaining)
    need(result.returncode==0, 'subprocess_'+logname)
    need(size()<=CAP-32768, 'new_output_byte_cap')

def row_determinant(matrix, label):
    """Exact Gaussian elimination with primitive rows, not Bareiss.

    Row i -> ((p/d) row i - (u/d) row k)/g, d=gcd(p,u).
    Each such operation multiplies the determinant by p/(d*g).
    The product of the final diagonal, divided by all these factors
    and corrected for row swaps, is the original determinant.
    """
    a = [row[:] for row in matrix]
    n = len(a)
    need(all(len(row)==n for row in a), label+'_square')
    steps, sign, factor = [], 1, Fraction(1)
    STATE['phase'] = label
    try:
        for k in range(n):
            candidates = [i for i in range(k,n) if a[i][k]]
            need(bool(candidates), label+'_nonsingular_'+str(k))
            # Unlike the replay, prefer the smallest absolute pivot.
            r = min(candidates, key=lambda i: abs(a[i][k]))
            if r!=k:
                a[k], a[r] = a[r], a[k]
                sign = -sign
            p = a[k][k]
            records = []
            for i in range(k+1,n):
                u = a[i][k]
                if not u: continue
                d = math.gcd(p,u)
                row = [(p//d)*a[i][j]-(u//d)*a[k][j] for j in range(n)]
                g = 0
                for x in row: g = math.gcd(g,x)
                need(g>0 and all(x%g==0 for x in row), label+'_row_content')
                a[i] = [x//g for x in row]
                need(not any(a[i][:k+1]), label+'_eliminated_prefix')
                factor *= Fraction(p,d*g)
                records.append({'row':i,'old_column':u,'gcd_pivot_column':d,
                                'row_content':g,'full_new_row':a[i][:]})
            steps.append({'column':k,'swap_row':r,'pivot':p,'updates':records})
            STATE[label+'_columns'] = k+1
        need(all(a[i][j]==0 for i in range(n) for j in range(i)), label+'_triangular')
        value = Fraction(sign*math.prod(a[i][i] for i in range(n)))/factor
        need(value.denominator==1, label+'_integer_determinant')
        save(label+'.json', {'matrix':matrix,'steps':steps,'echelon':a,
             'swap_sign':sign,'determinant_multiplier':str(factor),
             'determinant':value.numerator,'status':'PASS'})
        return value.numerator
    except Exception:
        save(label+'-partial.json', {'matrix':matrix,'steps':steps,'work':a,
             'swap_sign':sign,'determinant_multiplier':str(factor),'status':'STOP'})
        raise

files = sorted(p for p in SOURCE.iterdir() if p.is_file())
files += [PARENT/'certificate.json', PARENT/'verify_certificate.py',
          PARENT/'audit-241/complete-replay.json']
before = {str(p.relative_to(PARENT)): digest(p) for p in files}
save('original-manifest.json', before)
signal.signal(signal.SIGALRM, stop)
signal.setitimer(signal.ITIMER_REAL, max(0.001,180-(time.monotonic()-START)))
try:
    old = read(PARENT/'audit-241/complete-replay.json')
    need(old['status']=='PASS' and old['sha256']==digest(PARENT/'certificate.json'),
         'audited_L067_certificate_hash')
    STATE['phase'] = 'full_L067_replay'
    run([str(PARENT/'verify_certificate.py'), '--certificate',str(PARENT/'certificate.json'),
         '--report',str(ROOT/'upstream-report.json')], 'upstream.log')
    upstream = read(ROOT/'upstream-report.json')
    need(upstream['status']=='PASS' and upstream['checks_passed']==4852,
         'full_L067_replay_counts')
    STATE['upstream_checks'] = upstream['checks_passed']
    STATE['phase'] = 'full_L077_replay'
    replay = ROOT/'replay'
    replay.mkdir()
    shutil.copyfile(PARENT/'certificate.json', ROOT/'certificate.json')
    names = ['basis.json','trace.json','trace-elimination.json',
             'resultant-elimination.json','discriminant.json','verify_order.py']
    names += ['product-%02d.json'%i for i in range(48)]
    for name in names:
        shutil.copyfile(SOURCE/name,replay/name)
        need(digest(SOURCE/name)==digest(replay/name), 'exact_copy_'+name)
    need(size()<=CAP-32768, 'copy_byte_cap')
    run([str(replay/'verify_order.py')], 'order-replay.log')
    report = read(replay/'verification-report.json')
    need(report['status']=='PASS' and report['basis_elements']==48
         and report['product_slots']==110592 and report['trace_entries']==2304
         and report['trace-elimination_divisions']==35720
         and report['resultant-elimination_divisions']==281295, 'full_L077_counts')
    STATE['order_replay'] = report
    H = read(replay/'basis.json')['H']
    G = read(replay/'trace.json')['gram']
    # Coefficient placement constructed separately from the saved elimination.
    descending = H[::-1]
    derivative = [i*H[i] for i in range(1,len(H))][::-1]
    S = [[0]*i+descending+[0]*(46-i) for i in range(47)]
    S += [[0]*i+derivative+[0]*(47-i) for i in range(48)]
    trace_value = row_determinant(G,'primitive-row-trace')
    resultant_value = row_determinant(S,'primitive-row-resultant')
    disc = read(replay/'discriminant.json')
    need(trace_value==disc['order_discriminant'] and trace_value<0,
         'independent_signed_trace_determinant')
    need(resultant_value==disc['resultant'] and resultant_value==343*trace_value,
         'independent_signed_resultant')
    need(48*47//2==1128 and 1128%2==0 and len(str(abs(trace_value)))==6870,
         'discriminant_convention')
    STATE.update(status='PASS',phase='complete',alternative_determinants=2,
                 signed_equality=True,discriminant_digits=6870)
except Exception as exc:
    STATE.update(status='STOP',failure=type(exc).__name__+': '+str(exc))
    STATE['failures'].append(STATE['failure'])
finally:
    signal.setitimer(signal.ITIMER_REAL,0)
    after = {str(p.relative_to(PARENT)): digest(p) for p in files}
    changed = [name for name in before if before[name]!=after[name]]
    save('preservation.json', {'before':before,'after':after,'changed':changed})
    if changed:
        STATE['status']='STOP'
        STATE['failures'].append('original_bytes_changed')
    STATE.update(seconds=time.monotonic()-START,required_seconds=180,
                 original_files=len(files),originals_unchanged=not changed,
                 bytes_before_report=size(),required_bytes=CAP)
    if STATE['seconds']>180:
        STATE['status']='STOP'
        STATE['failures'].append('aggregate_internal_time_bound')
    save('audit-report.json',STATE)
    print(json.dumps(STATE))
sys.exit(0 if STATE['status']=='PASS' else 1)
