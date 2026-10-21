#!/usr/bin/env python3
"""Independent complete operand audit of L051; no new count search."""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import subprocess
import sys

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
SOURCE = ROOT / 'fixed-pair-range-certificate.json'
OUTPUT = ROOT / 'fixed-pair-range-audit-certificate.json'
before = SOURCE.read_bytes()
c = json.loads(before)
checks, evidence, expected_signs = [], {}, []


def check(name, condition):
    checks.append(dict(name=name, passed=bool(condition)))


def bounds(obj):
    return Q(obj['lower']), Q(obj['upper'])


def floor(t):
    return t.numerator // t.denominator


# Independent unrounded Horner polynomial and argument-dependent remainder.
# log v = 2*x*sum_{j<112} (x*x)^j/(2*j+1) + positive remainder,
# bounded above by 2*x^225/(225*(1-x*x)); x=0 is exact.
def series(v):
    x = (v-1)/(v+1)
    assert 0 <= x <= Q(1, 3)
    acc = Q(0)
    for j in reversed(range(112)):
        acc = Q(1, 2*j+1) + x*x*acc
    low = 2*x*acc
    return low, low + 2*x**225/(225*(1-x*x))


il2, iu2 = series(Q(2))
ell, eu = bounds(c['log2'])
S, m = 2**192, 96
E = Q(9, 4*193*3**193)


def verify_rounded(v, detail):
    x = (v-1)/(v+1)
    term, total = 2*x, 0
    for j in range(m):
        total += floor(S*term/(2*j+1))
        term *= x*x
    expected = dict(x=str(x), rounded_partial_integer=total,
                    rounding_budget=str(Q(m, S)),
                    integral_remainder_upper=str(E))
    return expected == detail, Q(total, S), Q(total+m, S)+E


ok, lo, hi = verify_rounded(Q(2), c['log2']['detail'])
check('log2 complete rounded operands', ok and (lo, hi) == (ell, eu))
check('independent log2 enclosure inside saved enclosure', ell < il2 <= iu2 < eu)
independent_logs = {'2': dict(lower=str(il2), upper=str(iu2))}
for key, item in c['logarithms'].items():
    t = Q(key)
    # Deliberately normalize by repeated halving, not bit-length arithmetic.
    v, k = t, 0
    while v >= 2:
        v /= 2
        k += 1
    ok, vl, vu = verify_rounded(v, item['detail'])
    check('complete rounded log '+key,
          ok and t >= 1 and 1 <= v < 2 and item['argument'] == key
          and item['binary_exponent'] == k and Q(item['reduced_argument']) == v
          and bounds(item) == (vl+k*ell, vu+k*eu))
    a, b = series(v)
    a, b = a+k*il2, b+k*iu2
    sl, su = bounds(item)
    check('independent enclosure '+key, sl <= a <= b < su)
    independent_logs[key] = dict(lower=str(a), upper=str(b))

p, q = 9809721694, 6189245291
l3, u3 = bounds(c['logarithms']['3'])
eps, epsu = q*l3-p*eu, q*u3-p*ell
check('fixed constants and residual operands',
      (c['bits'], c['terms'], c['p'], c['q'], c['primitive_threshold'])
      == (192, 96, p, q, 225640000)
      and Q(c['epsilon_lower']) == eps and Q(c['epsilon_upper']) == epsu)
# Independent cancellation through log(3/2) and the negative coefficient q-p.
l32, u32 = series(Q(3, 2))
ieps, iepsu = (q-p)*iu2+q*l32, (q-p)*il2+q*u32
check('independent positive residual and outward cancellation',
      0 < eps < ieps <= iepsu < epsu and Q(9, 10**11) < ieps < iepsu < Q(1, 10**10))
evidence['independent_epsilon'] = dict(lower=str(ieps), upper=str(iepsu))


def sign(name, val):
    margin = Q(floor(val*10**12), 10**12)
    expected_signs.append(dict(name=name, actual=str(margin), relation='>',
                               required='0', passed=margin > 0))
    check(name, margin > 0)


sign('epsilon positive', eps)
sign('log2 exceeds 2/3', ell-Q(2, 3))
expected_M = [4878,11017,23657,49490,102015,208393,423153,855531,
              1723967,3464527,6946364,13899373,27762044,55360636,
              110231529,219188637,435294295,863456373,1710903708,
              3386647505,6697335032]
check('all and only counts 3 through 23', [v['r'] for v in c['rows']] == list(range(3,24)))
needed_logs = {'3'}
row_evidence = []
for r, row, M in zip(range(3,24), c['rows'], expected_M):
    start = len(expected_signs)
    # Closed form independent of the generator's finite sum.
    R = Q(48**r-25**r, 23*25**(r-1))
    A = Q(399,5)*R
    lr, ur = bounds(c['logarithms'][str(r)])
    B, Bu = (54+6*lr)*R+Q(69*r,1034), (54+6*ur)*R+Q(69*r,1034)
    lm, um = bounds(c['logarithms'][str(M)])
    lp, up = bounds(c['logarithms'][str(M-1)])
    fm, fmu = M-A*um-Bu, M-A*lm-B
    fp, fpu = M-1-A*up-Bu, M-1-A*lp-B
    gl, gu = ell-2*M*epsu, eu-2*M*eps
    D = Q(69*r*q+23,11)
    ld, ud = bounds(c['logarithms'][str(D)])
    tl, tu = Q(15,4)*R*(1+ld), Q(15,4)*R*(1+ud)
    operands = dict(R=R, A=A, B_lower=B, B_upper=Bu,
                    F_M_lower=fm, F_M_upper=fmu, guard_lower=gl,
                    guard_upper=gu, D=D, T_lower=tl, T_upper=tu)
    check(f'r={r}: all complete row operands',
          all(Q(row[k]) == v for k,v in operands.items())
          and row['least_integer_ceiling'] == M
          and row['previous'] == dict(integer=M-1, F_lower=str(fp), F_upper=str(fpu)))
    check(f'r={r}: previous integer also on increasing ray', M-1 > A)
    sign(f'r={r}: M>A', M-A)
    sign(f'r={r}: F(M)>0', fm)
    sign(f'r={r}: F(M-1)<0', -fpu)
    if r < 23:
        sign(f'r={r}: half-log guard holds', gl)
        sign(f'r={r}: T below primitive threshold', 225640000-tu)
    else:
        sign(f'r={r}: half-log guard fails', -gu)
        sign(f'r={r}: T above primitive threshold', tl-225640000)
    check(f'r={r}: predicates and exact saved checks',
          row['half_log_guard_pass'] == (r < 23)
          and row['odd_count_pass'] == (r < 23)
          and row['success'] == (r < 23)
          and row['checks'] == expected_signs[start:])
    # An independent, tighter interval recomputes every decisive sign too.
    ir, iur = bounds(independent_logs[str(r)])
    im, ium = bounds(independent_logs[str(M)])
    ip, iup = bounds(independent_logs[str(M-1)])
    idl, idu = bounds(independent_logs[str(D)])
    ib, ibu = (54+6*ir)*R+Q(69*r,1034), (54+6*iur)*R+Q(69*r,1034)
    independent = dict(F_M_lower=M-A*ium-ibu, F_previous_upper=M-1-A*ip-ib,
                       guard_lower=il2-2*M*iepsu, guard_upper=iu2-2*M*ieps,
                       T_lower=Q(15,4)*R*(1+idl), T_upper=Q(15,4)*R*(1+idu))
    check(f'r={r}: independently enclosed decisive signs',
          independent['F_M_lower'] > 0 and independent['F_previous_upper'] < 0
          and ((independent['guard_lower'] > 0 and independent['T_upper'] < 225640000)
               if r < 23 else
               (independent['guard_upper'] < 0 and independent['T_lower'] > 225640000)))
    needed_logs.update(map(str, (r, M, M-1, D)))
    row_evidence.append(dict(r=r, M=M, previous_ray_margin=str(M-1-A),
                            operands={k:str(v) for k,v in operands.items()},
                            independent={k:str(v) for k,v in independent.items()}))
check('all stored log arguments exactly required', set(c['logarithms']) == needed_logs)
check('all 107 saved sign checks exactly reproduced', c['checks'] == expected_signs and len(expected_signs) == 107)
check('range/failure summaries', c['successful_range'] == [3,22] and c['first_failure'] == 23 and c['failures'] == [])
r22, r23 = c['rows'][-2:]
check('all displayed r22 rational bounds',
      Q(r22['F_M_lower']) > Q('0.542833173111')
      and Q(r22['previous']['F_upper']) < -Q('0.413407377843')
      and Q(r22['guard_lower']) > Q('0.044804922744')
      and Q(r22['T_upper']) < 198293520)
check('all displayed r23 rational bounds',
      Q(r23['F_M_lower']) > Q('0.708478495879')
      and Q(r23['previous']['F_upper']) < -Q('0.249035961741')
      and Q(r23['guard_upper']) < -Q('0.588995501718')
      and Q(r23['T_lower']) > 381318038)
run = subprocess.run([sys.executable, str(ROOT/'certify_fixed_pair_range.py')],
                     capture_output=True, text=True)
check('original generator succeeds and reproduces bytes', run.returncode == 0 and SOURCE.read_bytes() == before)
failures = [v for v in checks if not v['passed']]
result = dict(scope='L051 fixed-scope independent audit, r=3 through 23 only',
              source_sha256=hashlib.sha256(before).hexdigest(),
              independent_method='112 unrounded Horner terms with argument-dependent integral remainder',
              checks=checks, failures=failures, log_enclosures=independent_logs,
              evidence=evidence, rows=row_evidence, exact_sign_checks=expected_signs,
              original_generator_stdout=run.stdout, original_generator_stderr=run.stderr)
OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
print(f'Audit checks={len(checks)}; failures={len(failures)}; log arguments={len(c["logarithms"])}; rows={len(row_evidence)}; saved signs={len(expected_signs)}')
for row in (r22,r23):
    print(f'r={row["r"]}: M={row["least_integer_ceiling"]}; half-log guard={row["half_log_guard_pass"]}; T interval=({floor(Q(row["T_lower"])*100)/100}, {(floor(Q(row["T_upper"])*100)+1)/100}); required T<=225640000')
print('Source SHA256:', result['source_sha256'])
print('Failures:', failures)
print('Full certificate:', OUTPUT)
raise SystemExit(bool(failures))
