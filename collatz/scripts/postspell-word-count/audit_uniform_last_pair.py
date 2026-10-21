#!/usr/bin/env python3
"""Independent finite audit of L068; symbolic interval proof is in L068.

Does not import or execute the construction program. All certificate
operands are reconstructed, not accepted from stored success flags.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
SOURCE = HERE / 'uniform-last-pair-certificate.json'
old = json.loads(SOURCE.read_text())
pairs = [
    (8, 40), (15, 72), (28, 134), (52, 249), (98, 467),
    (184, 877), (347, 1650), (653, 3106), (1230, 5849),
    (2317, 11018), (4365, 20756), (8224, 39104),
    (15494, 73672), (29191, 138802), (54998, 261511),
    (103621, 492705), (195229, 928293), (367827, 1748976),
    (693015, 3295208), (1305695, 6208431), (2460032, 11697176),
    (4634896, 22038409), (8732512, 41522114),
    (16452748, 78230965), (30998279, 32670621),
]
checks = []


def check(name, ok, **evidence):
    checks.append(dict(name=name, passed=bool(ok), **evidence))


def equal(name, actual, expected):
    check(name, actual == expected, actual=actual, expected=expected)


def less(name, actual, required):
    check(name, actual < required, actual=actual, required=required,
          difference=required-actual)


literal = [tuple(map(int, r)) for r in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$',
    (ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md').read_text(), re.M)]
equal('complete independent table versus L055', literal,
      [(i, j, h) for i, (j, h) in enumerate(pairs)])
S = 10**12
TMAX = 9250245
K, N = 397573379, 630138897
lm, lp = Q(10584, 10**14), Q(10585, 10**14)
el, eu = Q(693147180559, S), Q(693147180560, S)
tl, tu = Q(1098612288668, S), Q(1098612288669, S)
dl, du = Q(1011600911678, S), Q(1011600911679, S)

# Direct unrounded series: x=(z-1)/(z+1), not the original binary
# reduction. The exact integral remainder is bounded by
# 2*x^(2m+1)/((2m+1)*(1-x*x)) after m terms.
logs = {}


def log_interval(z, name):
    x = (z-1)/(z+1)
    assert 0 < x <= Q(1, 2)
    terms = [2*x**(2*k+1)/(2*k+1) for k in range(160)]
    lower = sum(terms, Q(0))
    remainder = 2*x**321/(321*(1-x*x))
    logs[name] = dict(argument=z, x=x, terms=terms, lower=lower,
                      remainder=remainder, upper=lower+remainder)
    return lower, lower+remainder


l2, u2 = log_interval(Q(2), 'log2')
l3, u3 = log_interval(Q(3), 'log3')
ld, ud = log_interval(Q(11, 4), 'log11over4')
lv, uv = log_interval(Q(18*10**9, 2**34), 'reduced_log18billion')
for name, low, high, gridlow, gridhigh in [
    ('log2', l2, u2, el, eu), ('log3', l3, u3, tl, tu),
    ('log11over4', ld, ud, dl, du),
]:
    less(name+' lower grid', gridlow, low)
    less(name+' upper grid', high, gridhigh)
less('log18billion exceeds 23.61', Q(2361, 100), lv+34*l2)
lambda_low, lambda_high = N*l2-K*u3, N*u2-K*l3
less('Lambda lower including full cancellation', lm, lambda_low)
less('Lambda upper including full cancellation', lambda_high, lp)
equal('original constants', old['constants'], dict(
    S=S, EL=int(el*S), EU=int(eu*S), TL=int(tl*S), TU=int(tu*S),
    CU=int(du*S), AU=int((3*tu-4*el)*S), BU=int((tu-el)*S),
    lambda_lower=str(lm), lambda_upper=str(lp)))

eta = Q(23, 11)-Q(16, 27)**8*(Q(12, 11)+Q(2, 3)**40)
equal('written eta0', eta, Q(7122556955297586891012225981605,
                            3433683820292512484657849089281))
domain = 2*(1-lp)/lp
bmax = Q(23, 11)*(1+Q(2, 10**8))
norm = bmax/lm+bmax+Q(23, 11)
equal('written domain bound', domain, Q(39999999995766, 2117))
equal('written normalized upper', norm, Q(435606069410390910013, 22050000000))
equal('stored domain bound', Q(old['uniform_domain']['unshifted_lower']), domain)
equal('stored required domain', Q(old['uniform_domain']['required_shifted']), Q(540, 11))
less('shifted lower domain follows from unshifted bound', Q(540, 11), domain+Q(23, 11))
less('unchanged prefix multiplier baseline', 2, Q(19683, 8192))
finite_geometric = sum((Q(1, 10**8*2**k) for k in range(24)), Q(0))
less('complete finite inverse-prefix bound', Q(23, 11)*(1+finite_geometric), bmax)

# Reconstruct the entire t=2 record by direct prefix summation.
rows = [dict(i=i, J=j, H=h, a=38 if i == 23 else
             (166504376 if i == 24 else 2)) for i, (j, h) in enumerate(pairs)]
prefixes = []
for i in range(25):
    p = sum(3*r['J']+r['H'] for r in rows[:i])
    q = sum(4*r['J']+r['H']+r['a'] for r in rows[:i])
    prefixes.append(dict(i=i, three_exponent=p, two_exponent=q,
                         log_s_upper_scaled=int((24+p*tu-q*el)*S)))
p, q = prefixes[24]['three_exponent'], prefixes[24]['two_exponent']
equal('written row24 incoming exponents', [p, q], [271907921, 306970784])
qguard = q+4*pairs[24][0]
equal('written total negative log2 coefficient', qguard, 430963900)
margin = Q(24)+p*tu-qguard*el+du
equal('written boundary margin', margin, Q(-474883782659, 125000000000))
direct_margin = Q(24)+p*u3-qguard*l2+ud
less('independent upper margin below stored upper', direct_margin, margin)
expected_t2 = dict(rows=rows, prefixes=prefixes,
    closing_exponents=dict(three=sum(3*j+h for j, h in pairs),
        two=sum(4*r['J']+r['H']+r['a'] for r in rows)),
    B_upper=str(bmax), normalized_shifted_upper=str(norm), rejected_guard=24,
    log_s24_upper_scaled=prefixes[24]['log_s_upper_scaled'],
    margin_upper_scaled=int(margin*S), margin_upper=str(margin))
for key, value in expected_t2.items():
    equal('complete t2/'+key, old['t2'][key], value)

terms = [Q(1)]
for k in range(1, 41):
    terms.append(terms[-1]*24/k)
equal('all 41 exponential terms', [Q(v) for v in old['exp24_terms']], terms)
exp_sum = sum(terms, Q(0))
expected_operands = [
    (Q(2), eta), (Q(0), lm), (lp, Q(1)), (Q(18*10**9), domain),
    (Q(540, 11), Q(18*10**9)), (Q(10**8), Q(3**64, 2**74)),
    (Q(2), Q(3**117, 2**170)), (norm, Q(20*10**9)),
    (Q(20*10**9), exp_sum), (margin, Q(0)), (margin, Q(-379, 100)),
]
equal('original rational check count', len(old['checks']), len(expected_operands))
for i, ((a, b), saved) in enumerate(zip(expected_operands, old['checks'])):
    equal('original rational operands '+str(i),
          [Q(saved['actual']), Q(saved['required']), Q(saved['difference']), saved['passed']],
          [a, b, b-a, a < b])
    less('independent rational inequality '+str(i), a, b)

expected_table = dict(
    literal_indices=[r['i'] for r in rows] == list(range(25)),
    all_J_at_least_8_H_at_least_40=all(j >= 8 and h >= 40 for j, h in pairs),
    row24_eta_comparison=pairs[24][0] >= 8 and pairs[24][1] >= 40,
    first23_unchanged_tails=all(r['a'] == 2 for r in rows[:23]),
    t2_growing_baseline=all(r['J'] >= 15 and r['H'] >= 72 and r['a'] <= 38 for r in rows[1:24]),
    odd_total=sum(3*j+h for j, h in pairs) == K,
    even_total=sum(r['J']+r['a'] for r in rows) == N-K,
    total_exponent=sum(4*r['J']+r['H']+r['a'] for r in rows) == N,
    total_tail_budget=sum(r['a'] for r in rows) == 166504460,
    endpoint_tail23=2+18*TMAX == 166504412,
    endpoint_tail24=166504412-18*TMAX == 2,
    tail_congruences=all(r['a'] >= 2 and r['a'] % 18 == 2 for r in rows),
    closing_exponents=expected_t2['closing_exponents'] == dict(three=K, two=N))
equal('all original table checks', old['table_checks'], expected_table)
for name, value in expected_table.items():
    check('recomputed '+name, value)

equal('failed optional probe preserved', old['diagnostic_probes'], [dict(
    name='initial unnecessary margin<-4 request', actual=str(margin), requested='-4',
    passed=margin < -4,
    qualification='Failed stronger bound preserved; classification requires only margin<0')])
check('optional probe really fails', not margin < -4, actual=margin, requested=-4)
equal('original failures empty', old['failures'], [])
equal('coverage partition', old['interval_classification'], [
    dict(first=0, last=1, domain='PASS', J='PASS_BY_L055_L064'),
    dict(first=2, last=TMAX, domain='PASS', J='FAIL_ROW24_BY_MONOTONICITY')])
equal('partition size', 2+(TMAX-2+1), 9250246)

# Applicability check for the two imported survivors: every own-input
# lower margin is recomputed with the actual incoming tail sum.
survivors = []
for t in [0, 1]:
    tails = [2]*23+[2+18*t, 166504412-18*t]
    equal('survivor complete exponent '+str(t),
          sum(4*j+h+a for (j, h), a in zip(pairs, tails)), N)
    for i, (j, h) in enumerate(pairs):
        pk = sum(3*jj+hh for jj, hh in pairs[:i])
        pn = sum(4*jj+hh+aa for (jj, hh), aa in zip(pairs[:i], tails[:i]))
        lower = Q(2361, 100)+pk*tl-(pn+4*j)*eu+dl
        independent = lv+34*l2+pk*l3-(pn+4*j)*u2+ld
        less('t%d row%d imported passing guard' % (t, i), 0, lower)
        less('t%d row%d independent lower' % (t, i), lower, independent)
        survivors.append(dict(t=t, i=i, three=pk, two=pn,
                              lower=lower, independent_lower=independent))

failures = [r['name'] for r in checks if not r['passed']]
summary = dict(verdict='NO_DEFECT' if not failures else 'DEFECT',
    checks=len(checks), failures=failures, original_rational_checks=11,
    original_table_checks=13, table_rows=25, prefix_records=25,
    exponential_terms=41, independent_log_terms=160,
    uniform_unshifted_lower=domain, required_shifted_domain=Q(540, 11),
    normalized_shifted_upper=norm, normalized_required_upper=20*10**9,
    row24_boundary_upper=margin, required_margin_upper=Q(-379, 100),
    optional_margin_below_minus4=False,
    survivor_minima={str(t): min(r['lower'] for r in survivors if r['t'] == t)
                     for t in [0, 1]},
    lambda_claimed_interval=[lm, lp],
    coverage='t=0,1 pass; integers 2..9250245 fail row24 by the audited symbolic proof')
result = dict(summary=summary, original_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    checks=checks, independent_logs=logs, lambda_interval=[lambda_low, lambda_high],
    t2=expected_t2, independent_boundary_upper=direct_margin,
    exponential_terms=terms, exponential_sum=exp_sum, survivor_checks=survivors,
    symbolic_scope='L068 audit section verifies full closure, uniqueness, monotonicity and all-parameter domain; finite arithmetic alone is not that proof.')
out = HERE / 'uniform-last-pair-audit-certificate.json'
out.write_text(json.dumps(result, default=str, indent=2)+'\n')
print('Independent audit:', len(checks), 'checks; failures:', failures)
print('Uniform unshifted lower:', domain, '; shifted domain required: 540/11')
print('t=2 normalized upper:', norm, '; required < 20000000000')
print('t=2 row24 margin <', margin, '; required < -379/100; optional <-4 fails')
print('Minimum imported J lower margins:', summary['survivor_minima'])
print('Certificate:', out)
assert not failures
