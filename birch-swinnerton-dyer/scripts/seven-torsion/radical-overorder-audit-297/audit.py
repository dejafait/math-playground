"""One fixed L078 audit; original files read-only; no retry or enlargement."""
from pathlib import Path
from fractions import Fraction as F
import hashlib, json, math, shutil, signal, subprocess, sys, time

D = Path(__file__).resolve().parent
ROOT = D.parents[2]
OLD = D.parent / 'radical-overorder-295'
START = time.monotonic()
CAP = 134217728
REPORT = {'status': 'INCOMPLETE', 'failures': []}
sys.set_int_max_str_digits(0)

def need(ok, label):
    if not ok:
        raise ArithmeticError(label)

def size():
    return sum(p.stat().st_size for p in D.iterdir() if p.is_file())

def save(name, value):
    raw = (json.dumps(value, separators=(',', ':')) + '\n').encode()
    need(size() + len(raw) + 65536 <= CAP, 'aggregate_byte_cap')
    with (D / name).open('xb') as f:
        f.write(raw)

def read(name):
    return json.loads((D / name).read_text())

def hashes(paths):
    return {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in sorted(paths)}

def matmul(a, b):
    columns = list(zip(*b))
    return [[sum(x*y for x, y in zip(row, col) if x and y)
             for col in columns] for row in a]

def full_rank_witness(matrix, kernel, columns, label):
    # Find independent ORIGINAL rows without reading any saved row operations.
    echelon = []
    selected = []
    for index, row in enumerate(matrix):
        v = [x % 31 for x in row]
        for pivot, earlier in echelon:
            q = v[pivot]
            v = [(x-q*y) % 31 for x, y in zip(v, earlier)]
        pivot = next((i for i, x in enumerate(v) if x), None)
        if pivot is not None:
            q = pow(v[pivot], -1, 31)
            echelon.append((pivot, [x*q % 31 for x in v]))
            selected.append(index)
    need(len(selected) == len(columns) == 46, label+'_rank46')
    minor = [[matrix[i][j] % 31 for j in columns] for i in selected]
    a = [r[:] for r in minor]
    determinant = 1
    steps = []
    for k in range(46):
        s = next(i for i in range(k, 46) if a[i][k])
        if s != k:
            a[k], a[s] = a[s], a[k]
            determinant = -determinant
        pivot = a[k][k]
        determinant = determinant * pivot % 31
        multipliers = []
        for i in range(k+1, 46):
            q = a[i][k] * pow(pivot, -1, 31) % 31
            multipliers.append(q)
            a[i] = [(x-q*y) % 31 for x, y in zip(a[i], a[k])]
        steps.append({'column': k, 'swap_row': s, 'pivot': pivot,
                      'multipliers': multipliers})
    need(determinant != 0, label+'_nonzero_minor')
    need(kernel[0][0] == kernel[1][1] == 1 and
         kernel[0][1] == kernel[1][0] == 0, label+'_kernel_independence')
    need(all(sum(x*y for x, y in zip(row, v)) % 31 == 0
             for row in matrix for v in kernel), label+'_full_kernel_containment')
    save(label+'-minor.json', {'rows': selected, 'columns': columns,
         'matrix': minor, 'steps': steps, 'upper_triangular': a,
         'determinant_mod31': determinant, 'kernel': kernel,
         'rows_tested': len(matrix), 'rank': 46, 'nullity': 2})
    return determinant

def main():
    inputs = json.loads((OLD / 'input-hashes.json').read_text())
    paths = {ROOT / name for name in inputs}
    paths.update(p for p in OLD.iterdir() if p.is_file())
    before = hashes(paths)
    need(all(before[k] == v for k, v in inputs.items()), 'original_upstream_hashes')
    save('original-manifest.json', before)
    names = ['verify.py', 'input-hashes.json', 'source.json', 'frobenius.json',
             'radical-lattice.json', 'action-kernel.json', 'numerator-lattice.json', 'basis.json']
    names += ['%s-%02d.json' % (kind, i) for kind in ('action', 'product') for i in range(48)]
    for name in names:
        need(not (D / name).exists(), 'fresh_evidence_only')
        need(size() + (OLD / name).stat().st_size + 65536 <= CAP, 'copy_byte_cap')
        shutil.copyfile(OLD / name, D / name)
        need((D / name).read_bytes() == (OLD / name).read_bytes(), 'byte_identical_replay_copy')
    # Same directory depth: verifier is entirely unchanged, including ROOT/HERE.
    result = subprocess.run([sys.executable, '-B', str(D / 'verify.py')],
                            capture_output=True, text=True,
                            timeout=max(0.01, 179.5-(time.monotonic()-START)))
    save('replay-process.json', {'returncode': result.returncode,
                                'stdout': result.stdout, 'stderr': result.stderr})
    replay = read('verification-report.json')
    need(result.returncode == 0 and replay['status'] == 'PASS', 'full_fresh_replay')
    for name in ('old_product_slots', 'action_slots', 'new_product_slots'):
        need(replay[name] == 110592, 'complete_'+name)

    evens = [1,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28,4,5,14]
    odds = [1,9,19,16,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28]
    r0 = [evens[i//2] if i % 2 == 0 else 0 for i in range(48)]
    r1 = [odds[i//2] if i % 2 else 0 for i in range(48)]
    unit = [[int(i == j) for j in range(48)] for i in range(48)]
    J = [[r0[i], r1[i]] + [31*int(i == j) for j in range(2, 48)] for i in range(48)]
    S = [[r0[i], r1[i]] + [31*int(i == j) for j in range(48)] for i in range(48)]
    chosen = [0, 1] + list(range(4, 50))
    forward = [[int(i == chosen[j]) for j in range(48)] for i in range(50)]
    inclusion = [[31*int(i == j) if i < 2 else
                  (-r0[i] if j == 0 else -r1[i] if j == 1 else int(i == j))
                  for j in range(48)] for i in range(48)]
    reverse = [[int(i == 0), int(i == 1)] + inclusion[i] for i in range(48)]
    inverse = [[F(x, 31) for x in row] for row in inclusion]
    need(matmul(S, forward) == J and matmul(J, reverse) == S,
         'independent_both_generator_identities')
    need(matmul(J, inverse) == unit and matmul(inverse, J) == unit,
         'independent_full_radical_inverse')
    for name in ('radical-lattice', 'numerator-lattice'):
        a = read(name+'.json')
        need(a['kernel_reduction']['rref'] == [r0, r1], name+'_displayed_full_kernel')
        need(a['basis'] == J and a['S'] == S and a['C'] == forward and a['D'] == reverse,
             name+'_all_direct_integer_generator_coefficients')
        need([[F(x) for x in row] for row in a['inverse']] == inverse,
             name+'_every_inverse_coefficient')
    b = read('basis.json')
    M = [[F(x, 31) for x in row] for row in J]
    need([[F(x) for x in row] for row in b['M']] == M and b['inverse'] == inclusion,
         'entire_displayed_basis_and_inclusion')
    need(matmul(M, inclusion) == unit and matmul(inclusion, M) == unit,
         'new_inverse_orientation')
    need([inclusion[i][i] for i in range(48)] == [31,31]+[1]*46 and
         all(inclusion[i][j] == 0 for i in range(48) for j in range(i+1,48)),
         'full_triangular_index961')
    f = read('frobenius.json')
    fd = full_rank_witness(f['second'], [r0,r1], f['elimination']['pivots'], 'frobenius')
    actions = [read('action-%02d.json' % i) for i in range(48)]
    stack = [[a[k][j] % 31 for a in actions] for j in range(48) for k in range(48)]
    ad = full_rank_witness(stack, [r0,r1], read('action-kernel.json')['pivots'], 'action')
    need(48*48*30**3 == 62208000 < 2**63, 'producer_int64_bound')
    save('independent-basis.json', {'r0': r0, 'r1': r1, 'J': J, 'S': S,
         'forward': forward, 'reverse': reverse, 'inclusion': inclusion,
         'index': 961, 'frobenius_minor_mod31': fd, 'action_minor_mod31': ad,
         'int64_actual_upper_bound': 62208000, 'int64_required_strict_bound': 2**63})
    REPORT.update(status='PASS', original_files=len(before), copied_files=len(names),
                  replay=replay, independent_index=961,
                  independent_rank46_minor_mod31={'frobenius':fd, 'action':ad},
                  integral_preimages_checked=2, basis_and_inverse_slots=2304,
                  int64_bound=62208000, required_int64_strict_bound=2**63)

def stop(*unused):
    raise TimeoutError('aggregate_internal_180_seconds')

signal.signal(signal.SIGALRM, stop)
signal.setitimer(signal.ITIMER_REAL, 180)
try:
    main()
except Exception as e:
    REPORT.update(status='STOP', failures=[type(e).__name__+': '+str(e)])
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    if (D/'original-manifest.json').exists():
        before = read('original-manifest.json')
        after = hashes([ROOT/name for name in before])
        changed = [name for name in before if before[name] != after[name]]
        save('audit-preservation.json', {'before':before, 'after':after, 'changed':changed})
        REPORT['original_files_unchanged'] = not changed
        if changed:
            REPORT.update(status='STOP', failures=REPORT['failures']+['original_files_changed'])
    REPORT.update(seconds=time.monotonic()-START, internal_limit=180, byte_limit=CAP)
    save('audit-report.json', REPORT)
    print(json.dumps({'status':REPORT['status'], 'seconds':REPORT['seconds'],
          'required_seconds':180, 'bytes':size(), 'required_bytes':CAP,
          'index':REPORT.get('independent_index'), 'required_index':961,
          'slots':REPORT.get('replay',{}).get('new_product_slots'), 'required_slots_each':110592,
          'failures':REPORT['failures'], 'report':str((D/'audit-report.json').relative_to(ROOT))}))
sys.exit(0 if REPORT['status']=='PASS' else 1)
