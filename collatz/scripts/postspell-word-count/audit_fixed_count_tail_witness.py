#!/usr/bin/env python3
"""Independent L055 audit: literal table, exact unrounded log intervals.

Does not import/run the construction generator. Verifies the complete old
certificate and emits separate evidence; giant factored roots are justified
by the canonical symbolic proof, never by numerical closure approximation.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
source = HERE / 'fixed-count-tail-witness-certificate.json'
old = json.loads(source.read_text())
lemma = (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text()
table = [tuple(map(int, row)) for row in re.findall(r'^\|(\d+)\|(\d+)\|(\d+)\|$', lemma, re.M)]
records = []


def check(name, actual, required, relation='=='):
    passed = {'==': lambda: actual == required,
              '<': lambda: actual < required,
              '<=': lambda: actual <= required}[relation]()
    records.append(dict(name=name, actual=str(actual), required=str(required),
                        relation=relation, passed=passed))


check('literal table indices', [r[0] for r in table], list(range(25)))
K, L, N = 397573379, 232565518, 630138897
S, D = 10**12, 2**192
E, A, T, C = 693147180560, 523248143764, 405465108108, 1011600911678
check('complete original constants', old['constants'],
      dict(S=S, ELO=693147180559, EHI=E, TLO=1098612288668,
           THI=1098612288669, CLO=C, AL=A, BE=T, initial_v=23610000000000))
v, pk, pn = 23610000000000, 0, 0
rows, prefixes = [], []
for i, j, h in table:
    a = 2 if i < 24 else 166504412
    gm, hm = v+C-4*j*E, v+j*A-h*E
    row = dict(i=i, J=j, H=h, a=a, v=v,
               J_guard_margin_scaled=gm, H_guard_margin_scaled=hm,
               odd_exponent=3*j+h, two_exponent=4*j+h+a)
    rows.append(row)
    prefixes.append(dict(i=i, C_three_exponent=pk, C_two_exponent=pn))
    check(f'complete old parameter row {i}', old['parameters'][i], row)
    check(f'J domain {i}', 2, j, '<=')
    check(f'H domain {i}', 3, h, '<=')
    check(f'tail domain {i}', 0, a, '<=')
    check(f'tail congruence {i}', a % 18, 2)
    check(f'independent own J guard {i}', 0, gm, '<')
    check(f'independent own H guard {i}', 0, hm, '<')
    pk, pn = pk+3*j+h, pn+4*j+h+a
    v += j*A+h*T-a*E
check('complete prefix records', old['prefixes'], prefixes)
counts = dict(K=K, N=N, L=L, d=1, K0=K, L0=L,
              sum_J=sum(r['J'] for r in rows),
              sum_H=sum(r['H'] for r in rows),
              sum_a=sum(r['a'] for r in rows))
check('complete count records', old['counts'], counts)
check('odd total', 3*counts['sum_J']+counts['sum_H'], K)
check('even total', counts['sum_J']+counts['sum_a'], L)
check('length total', K+L, N)
check('closing product exponents', (pk, pn), (K, N))
check('primitive count guard with d=1', 225640000, K, '<')
check('positive L0 with d=1', 0, L, '<')


def exact_series(t, m=120):
    """Unrounded atanh series; x-specific rigorous integral upper bound."""
    x = (t-1)/(t+1)
    assert 0 <= x <= F(1, 3)
    total = sum((2*x**(2*j+1)/F(2*j+1) for j in range(m)), F(0))
    rem = 2*x**(2*m+1)/((2*m+1)*(1-x*x))
    return total, total+rem


def old_base(t, label, detail):
    x = (t-1)/(t+1)
    floors = [(D*2*x**(2*j+1)/F(2*j+1)).__floor__() for j in range(96)]
    expected = dict(x=str(x), rounded_summands=floors,
                    rounding_budget=str(F(96, D)),
                    remainder_upper=str(F(9, 4*193*3**193)))
    # Full dictionary equality inspects all 96 entries and every remainder.
    check(label+' complete rounded log evidence', detail, expected)
    lo = F(sum(floors), D)
    return lo, lo+F(96, D)+F(9, 4*193*3**193)

ell = old_base(F(2), 'log2 base', old['log2_detail'])
ell_new = exact_series(F(2))
logs, independent_logs = {}, {}
for name, entry in old['logs'].items():
    t, k = F(name), 0
    reduced = t
    while reduced >= 2:
        reduced /= 2
        k += 1
    check(name+' binary exponent', entry['binary_exponent'], k)
    check(name+' reduced argument', F(entry['reduced_argument']), reduced)
    b = old_base(reduced, name, entry['detail'])
    interval = tuple(b[i]+k*ell[i] for i in (0, 1))
    check(name+' saved lower', F(entry['lower']), interval[0])
    check(name+' saved upper', F(entry['upper']), interval[1])
    bn = exact_series(reduced)
    independent = tuple(bn[i]+k*ell_new[i] for i in (0, 1))
    check(name+' independent lower containment', interval[0], independent[0], '<=')
    check(name+' independent upper containment', independent[1], interval[1], '<')
    logs[name] = interval
    independent_logs[name] = dict(lower=str(independent[0]), upper=str(independent[1]),
                                 terms=120, reduced_argument=str(reduced), binary_exponent=k)
check('all required log arguments', set(logs), {'2', '3', '11/4', '18000000000', '20000000000', str(N), '25'})
l2, u2 = logs['2']; l3, u3 = logs['3']
lo, hi = N*l2-K*u3, N*u2-K*l3
lm, lp = F(10584, 10**14), F(10585, 10**14)
eta0 = F(23, 11)-F(12, 11)*F(16, 27)**8-F(16, 27)**8*F(2, 3)**40
bmax = F(23, 11)*(1+F(2, 10**8))
rootlo, roothi = 2*(1-lp)/lp, bmax/lm
expected = {}


def less(name, a, b):
    a, b = F(a), F(b)
    expected[name] = dict(name=name, actual=str(a), required=str(b), relation='<',
                          margin=str(b-a), passed=a < b)
    check('recomputed '+name, a, b, '<')


less('log2 lower', F(693147180559, S), l2)
less('log2 upper', u2, F(E, S))
less('log3 lower', F(1098612288668, S), l3)
less('log3 upper', u3, F(1098612288669, S))
less('log(11/4) lower', F(C, S), logs['11/4'][0])
less('alpha lower positive', 0, A)
less('beta lower positive', 0, T)
check('alpha from outward constants', A, 3*1098612288668-4*E)
check('beta from outward constants', T, 1098612288668-E)
for r in rows:
    less(f'own J guard {r["i"]}', 4*r['J']*E, r['v']+C)
    less(f'own H guard {r["i"]}', r['H']*E, r['v']+r['J']*A)
less('Lambda positive lower', lm, lo)
less('Lambda upper', hi, lp)
less('Lambda upper below one', lp, 1)
less('length inequality', N, F(8, 5)*K+F(1725, 1034))
less('eta0 above two', 2, eta0)
less('first multiplier above 1e8', 10**8*2**74, 3**64)
less('minimal tail-two multiplier above two', 2, F(27, 16)**2*F(3, 2)**3/4)
less('n0 above 18 billion', 18*10**9, rootlo)
less('s0 below 20 billion', roothi+F(23, 11), 20*10**9)
less('initial lower log height', F(2361, 100), logs['18000000000'][0])
less('initial upper log height below 24', logs['20000000000'][1], 24)
less('seed above 24', 24, F(133, 10)*logs[str(N)][0]+8+logs['25'][0])
less('all junctions above required lower height', F(540, 11), 18*10**9)
check('all 70 checks independently reconstructed', len(expected), 70)
check('complete original strict comparisons', old['checks'], list(expected.values()))
check('complete original compact margins', old['inspection']['strict_margins'],
      [dict(name=r['name'], margin_floor_times_10_18=(F(r['margin'])*10**18).__floor__())
       for r in expected.values()])
rb = dict(eta0=str(eta0), B_upper=str(bmax), lambda_lower=str(lo), lambda_upper=str(hi),
          lambda_lower_used=str(lm), lambda_upper_used=str(lp), n0_lower=str(rootlo),
          n0_upper=str(roothi), certified_n0_lower=18*10**9, certified_s0_upper=20*10**9)
check('complete original root bounds', old['root_bounds'], rb)
ints = dict(word_count=len(rows)==25, J_guards=all(r['J']>=2 for r in rows),
            H_guards=all(r['H']>=3 for r in rows),
            tail_guards=all(r['a']>=0 and r['a']%18==2 for r in rows),
            odd_total=pk==K, even_total=pn-pk==L, length=K+L==N,
            first_24_tails=all(r['a']==2 for r in rows[:24]), d1_scaling=K>225640000 and L>0)
for i in range(24):
    r = rows[i]
    ints[f'lower_recurrence_{i}'] = rows[i+1]['v']==r['v']+r['J']*A+r['H']*T-2*E
ints['product_exponents'] = (pk, pn)==(K, N)
check('complete original integer checks', old['integer_checks'], ints)
check('all 34 independent integer checks hold', all(ints.values()) and len(ints)==34, True)
check('original failures empty', old['failures'], [])
# Also certify the very small Lambda directly with independent unrounded logs.
newlo = N*F(independent_logs['2']['lower'])-K*F(independent_logs['3']['upper'])
newhi = N*F(independent_logs['2']['upper'])-K*F(independent_logs['3']['lower'])
check('independent unrounded Lambda lower', lm, newlo, '<')
check('independent unrounded Lambda upper', newhi, lp, '<')
failures = [r['name'] for r in records if not r['passed']]
summary = dict(checks=len(records), source_rational_checks=len(expected), source_integer_checks=len(ints),
               log_arguments=len(logs), rounded_terms_checked=96*(len(logs)+1),
               lambda_required=[str(lm), str(lp)],
               J_margin_min=min((r['J_guard_margin_scaled'], r['i']) for r in rows),
               H_margin_min=min((r['H_guard_margin_scaled'], r['i']) for r in rows),
               root_required='18000000000<n0<s0<20000000000', failures=failures)
out = HERE / 'fixed-count-tail-witness-audit-certificate.json'
out.write_text(json.dumps(dict(summary=summary, source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                               rows=rows, counts=counts, root_bounds=rb,
                               independent_logs=independent_logs,
                               independent_lambda=dict(lower=str(newlo), upper=str(newhi)),
                               checks=records,
                               symbolic_obligations='See L055 independent critical audit: recurrence, positivity, closure, minimum, guards.'), indent=2)+'\n')
print(json.dumps(summary))
print('Full independent certificate:', out.relative_to(ROOT))
assert not failures, failures
