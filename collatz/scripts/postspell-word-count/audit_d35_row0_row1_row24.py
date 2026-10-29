#!/usr/bin/env python3
"""Independent L105 finite audit; uniformity and closure are proved in L105.

Does not import or execute the construction program. L104's audited log
enclosure is an input after exact matching, not a new log computation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SOURCE = HERE / 'd35-row0-row1-row24-certificate.json'
original = json.loads(SOURCE.read_text())
# Independent transcription of L055, checked against its canonical table.
J = [8,15,28,52,98,184,347,653,1230,2317,4365,8224,15494,
     29191,54998,103621,195229,367827,693015,1305695,2460032,
     4634896,8732512,16452748,30998279]
H = [40,72,134,249,467,877,1650,3106,5849,11018,20756,39104,
     73672,138802,261511,492705,928293,1748976,3295208,6208431,
     11697176,22038409,41522114,78230965,32670621]
table = [tuple(map(int, x)) for x in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(), re.M)]
checks = []


def check(label, actual, required, relation='='):
    passed = {'=': lambda: actual == required,
              '<': lambda: actual < required,
              '>': lambda: actual > required,
              '>=': lambda: actual >= required}[relation]()
    checks.append(dict(label=label, actual=actual, required=required,
                       relation=relation, passed=passed))


check('independent literal table', list(zip(range(25), J, H)), table)
H[0] -= 35
H[24] += 35
B, kappa = 9250245, F(23, 11)
budgets = [[0, 0, 0] for _ in J]
budgets[0], budgets[1], budgets[24] = [0, 1, 0], [0, 0, 1], [B, -1, -1]
tails = [[2 + 18*b[0], 18*b[1], 18*b[2]] for b in budgets]
p = [3*j+h for j, h in zip(J, H)]
q = [[4*j+h+a[0], a[1], a[2]] for j, h, a in zip(J, H, tails)]
K = sum(p)
N = [sum(v[d] for v in q) for d in range(3)]
check('J total', sum(J), 66061058)
check('H total', sum(H), 199390205)
check('tail total', [sum(a[d] for a in tails) for d in range(3)], [166504460, 0, 0])
check('L104 K exactly matched', K, 397573379)
check('L104 N exactly matched including parameter cancellation', N, [630138897, 0, 0])
check('original K', original['K'], K)
check('original N', original['N_affine'], N)
for i in range(25):
    expected = dict(i=i, J=J[i], H=H[i], b=budgets[i], a=tails[i], p=p[i], q=q[i])
    check(f'complete row {i}', original['rows'][i], expected)
    check(f'eta positivity J {i}', J[i], 0, '>')
    check(f'eta positivity H {i}', H[i], 0, '>')

order = list(range(2, 25)) + [0, 1]
prefixes = []
for k in range(26):
    # Sum the indicated subset independently, not an accumulated stored prefix.
    before = order[:k]
    pref = dict(input_row=order[k] if k < 25 else 2,
                p=sum(p[i] for i in before),
                q=[sum(q[i][d] for i in before) for d in range(3)])
    prefixes.append(pref)
    if k < 25:
        check(f'complete saved prefix {k}', original['cut2_prefixes'][k], pref)
    if k <= 22:
        check(f'prefix {k} uses only ordinary rows', all(2 <= i <= 23 for i in before), True)
        check(f'prefix {k} parameter independence', pref['q'][1:], [0, 0])
check('prefix23 exact powers', prefixes[23], dict(input_row=0, p=397573233, q=[630138724,-18,-18]))
check('prefix24 exact powers', prefixes[24], dict(input_row=1, p=397573262, q=[630138763,0,-18]))
check('complete product', prefixes[25], dict(input_row=2, p=K, q=N))
for k, remaining in [(23, [0,1]), (24, [1])]:
    check(f'prefix{k} complement p', prefixes[k]['p'] + sum(p[i] for i in remaining), K)
    check(f'prefix{k} complement q', [prefixes[k]['q'][d]+sum(q[i][d] for i in remaining) for d in range(3)], N)
for i in range(2,24):
    check(f'ordinary row {i} tail', tails[i], [2,0,0])
    check(f'ordinary row {i} H floor', H[i], 6, '>=')
check('ordinary multiplier lower floor', F(729,256), 2, '>')
check('c0 symbolic denominator', q[0], [39,18,0])
check('c1 symbolic denominator', q[1], [134,0,18])
check('c0 numerator exponent', p[0], 29)
check('c1 numerator exponent', p[1], 117)

# Boundary bookkeeping only; the written coefficient argument proves uniformity.
vertices = []
for m,u in [(1,1),(1,B-1),(B-1,1)]:
    bs = [b[0]+b[1]*m+b[2]*u for b in budgets]
    av = [2+18*b for b in bs]
    vertices.append(dict(m=m,u=u,budgets=bs,tails=av))
    check(f'nonnegative budgets at {m},{u}', min(bs), 0, '>=')
    check(f'budget total at {m},{u}', sum(bs), B)
check('complete saved vertex records', original['domain_vertices'], vertices)
check('whole closing-edge tail coefficients after u=B-m',
      [tails[24][0]+tails[24][2]*B, tails[24][1]-tails[24][2]], [2,0])

lo, hi = F(10584,10**14), F(10585,10**14)
check('imported lower operand', F(original['imported_L104_enclosure']['lower']), lo)
check('imported upper operand', F(original['imported_L104_enclosure']['upper']), hi)
check('positive denominator input', lo, 0, '>')
check('exponential domain', hi, F(1,2), '<')
check('exponential majorant', 1/(1-hi), 2, '<')
c0, c1 = F(3**29,2**57), F(3**117,2**152)
check('c0 integer comparison', 1000*3**29, 2**57, '<')
check('c1 integer comparison', 3**117, 2**186, '<')
geom = F(2)-F(1,2**22)
check('finite geometric sum', sum(F(1,2**k) for k in range(23)), geom)
bcap = kappa*(2+F(2**35,1000)+2**35)
scap = bcap/lo+kappa
guard = F(4*2**(4*J[2]),11)
bounds = dict(c0_maximum=c0,c1_maximum=c1,geometric_sum=geom,
              prefix23_upper=F(2**35,1000),prefix24_upper=2**35,
              B2_upper=bcap,s2_upper=scap,coarse_cap=10**21,
              row2_J_required=guard,guard_gap=guard-10**21)
for key, value in bounds.items():
    check(f'complete bound operand {key}', F(original['bounds'][key]), value)
check('canonical B2 numerator', bcap, F(98883032061558,1375))
check('canonical s2 cap', scap, F(3296101068718600000010143,4851))
check('s2 cap below required comparison threshold', scap, 10**21, '<')
check('own-input J2', J[2], 28)
check('guard above comparison threshold', guard, 10**21, '>')
check('canonical guard operand', guard, F(20769187434139310514121985316880384,11))
# Arithmetic replay ignores all original pass flags. Its scope is finite
# arithmetic consistency; independent rows/prefixes/bounds were checked above.
for i, item in enumerate(original['checks']):
    a,b = F(item['actual']), F(item['required'])
    check(f'original comparison {i}: {item["name"]}', a,b,item['relation'])
    check(f'original difference {i}', F(item['difference']), a-b)
failures = [c['label'] for c in checks if not c['passed']]
result = dict(scope='L105 full integer triangle; symbolic proof required for uniformity and closure',
              source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              changed_table=[dict(i=i,J=J[i],H=H[i],b=budgets[i],a=tails[i],p=p[i],q=q[i]) for i in range(25)],
              K=K,N_affine=N,cut2_prefixes_including_closure=prefixes,
              imported_L104_interval=dict(lower=lo,upper=hi,logs_recomputed=False),
              bounds=bounds,checks=checks,
              summary=dict(verdict='RETAIN L105' if not failures else 'AUDIT FAILED',
                           checks=len(checks),failures=failures,parameter_samples_for_uniformity=0),
              limitations='No formal verification, other guards, actual-word transfer or universal descent.')
out = HERE / 'd35-row0-row1-row24-audit-certificate.json'
out.write_text(json.dumps(result,default=str,indent=2)+'\n')
print(f'{result["summary"]["verdict"]}: checks={len(checks)}, failures={failures}')
print(f'K={K}; N={N}; all25 prefixes and exact closing product matched')
print(f'Uniform s2 < {scap} < {10**21}; own-input guard requires >= {guard}')
print(f'Certificate: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
