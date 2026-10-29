#!/usr/bin/env python3
"""Independent exact audit of L103, without executing its constructor.

Finite evidence supports the quantified proof; no allocation sampling.
The assessed positive-real log remainder and exponential series are inputs.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
certificate = HERE / 'd35-earlier-recipients-certificate.json'
raw = certificate.read_bytes()
saved = json.loads(raw)
table_path = ROOT / 'lemmas/L055-fixed-count-twenty-five-word-real-witness.md'
lemma_path = ROOT / 'lemmas/L103-d35-conditional-earlier-support-exclusion.md'
# Independent transcription of the canonical table, before either H change.
J = [8, 15, 28, 52, 98, 184, 347, 653, 1230, 2317, 4365, 8224,
     15494, 29191, 54998, 103621, 195229, 367827, 693015, 1305695,
     2460032, 4634896, 8732512, 16452748, 30998279]
H_original = [40, 72, 134, 249, 467, 877, 1650, 3106, 5849, 11018,
              20756, 39104, 73672, 138802, 261511, 492705, 928293,
              1748976, 3295208, 6208431, 11697176, 22038409,
              41522114, 78230965, 32670621]
H = H_original.copy()
H[0] -= 35
H[-1] += 35
rows = [[i, J[i], H[i]] for i in range(25)]
B, kap, U, T = 9250245, F(23, 11), F(20_000_000_000), F(24)
ell, q, w = [F(n, 10**12) for n in
             (693147180559, 1098612288669, 1011600911679)]
lam = F(10584, 10**14)
E = F(24*23, 4*2**(4*J[1])-23)
R = kap/(lam-E)+kap
A = [sum(3*J[k]+H[k] for k in range(i)) for i in range(26)]
D = [sum(4*J[k]+H[k]+2 for k in range(i)) for i in range(26)]
K, N = A[-1], D[-1]+18*B
terms = [F(1)]
for k in range(1, 41):
    terms.append(terms[-1]*T/k)
exp_lower = sum(terms)
prefix_upper = kap-(F(12, 11)*F(3, 2)**5+1)/4
recipient_q = F(12, 11)*F(3, 2)**72+1
Q0 = F(12, 11)*F(3, 2)**5+1
offsets = []
for i in range(22):
    floor = min(H[i], 72)
    lower = F(12, 11)*F(3, 2)**floor+1
    offsets.append(dict(i=i, H_floor=floor, Q_lower=lower,
                        tail2_upper=kap-lower/4, tail20_upper=kap-lower/2**20))
margins = []
for j in range(1, 22):
    c = D[j+1]+18+4*J[j+1]
    m = c*ell-T-w-A[j+1]*q
    margins.append(dict(j=j, next_input=j+1, A=A[j+1], D=D[j+1],
                        next_J=J[j+1], log2_coefficient=c,
                        margin=m, scaled_margin=m*10**12))
minimum = min(margins, key=lambda m: m['margin'])

failures, comparisons, proof_checks = [], [], []


def verify(name, condition, evidence=None):
    proof_checks.append(dict(name=name, passed=bool(condition), evidence=evidence))
    if not condition:
        failures.append(name)


def compare(path, actual, expected):
    """Check every relevant leaf and every container's exact keys/length."""
    if isinstance(expected, dict):
        verify(path+' keys', isinstance(actual, dict) and actual.keys() == expected.keys())
        if isinstance(actual, dict):
            for key, value in expected.items():
                compare(path+'/'+key, actual.get(key), value)
    elif isinstance(expected, list):
        verify(path+' length', isinstance(actual, list) and len(actual) == len(expected))
        if isinstance(actual, list):
            for i, value in enumerate(expected):
                compare(path+'/'+str(i), actual[i] if i < len(actual) else None, value)
    else:
        encoded = str(expected) if isinstance(expected, F) else expected
        comparisons.append(dict(path=path, actual=actual, expected=encoded,
                                passed=actual == encoded))
        if actual != encoded:
            failures.append(path)


transcription = [[i, J[i], H_original[i]] for i in range(25)]
canonical = [list(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|$', table_path.read_text(), re.M)]
compare('canonical table', canonical, transcription)

# Reapply the inspected rational remainder at different operands and length
# from the constructor's imported analytic data. log3=log2+log(3/2).
logs = {}
for label, x in [('2', F(2)), ('3/2', F(3, 2)), ('11/4', F(11, 4))]:
    z = (x-1)/(x+1)
    power, series = z, []
    for k in range(120):
        series.append(2*power/(2*k+1))
        power *= z*z
    remainder = 2*power/(241*(1-z*z))
    lower = sum(series)
    logs[label] = dict(x=x, z=z, terms=series, remainder=remainder,
                       lower=lower, upper=lower+remainder)
    verify('log domain '+label, 0 < z < 1 and remainder > 0)
log2lo, log2hi = logs['2']['lower'], logs['2']['upper']
log3lo = log2lo+logs['3/2']['lower']
log3hi = log2hi+logs['3/2']['upper']
lambda_lo = (N-K)*log2lo-K*logs['3/2']['upper']
lambda_hi = (N-K)*log2hi-K*logs['3/2']['lower']
verify('strict ell lower', 0 < ell < log2lo, [ell, log2lo])
verify('strict q upper', log3hi < q, [log3hi, q])
verify('strict w upper', logs['11/4']['upper'] < w, [logs['11/4']['upper'], w])
verify('strict positive Lambda lower', 0 < lam < lambda_lo < lambda_hi,
       [lam, lambda_lo, lambda_hi])
verify('invariant sums', (sum(J), sum(H), 50+18*B, K, N) ==
       (66061058, 199390205, 166504460, 397573379, 630138897))
verify('cap positivity and exp threshold', 0 < lam-E and kap < R < U < exp_lower,
       [lam-E, R, U, exp_lower])
verify('printed cap', R == F(1325859730438202850942226985830949,
                             67113790726173775832193))
verify('printed exp sum', exp_lower == F(202750314819830504045671593478515759301,
                                       7661655986496068058455078125))
verify('prefix and recipient distinct domains', min(H[:21]) == 5 and min(H[1:22]) == 72)
verify('printed separated offset constants', prefix_upper == F(-81, 352) and
       recipient_q == F(67585198634830509743348335148655587, 12986507827891524337664)
       and Q0 == F(817, 88))
verify('failed row0 tail20 test preserved', Q0 < kap*2**20 < recipient_q)
verify('all first-recipient margins', len(margins) == 21 and
       all(m['margin'] > F(47, 2) for m in margins))
verify('claimed minimum', minimum['j'] == 4 and
       minimum['margin'] == F(734806653733, 31250000000))
printed = [list(map(int, row)) for row in re.findall(
    r'^\|(\d+)\|(\d+)\|(\d+)\|(\d+)\|$', lemma_path.read_text(), re.M)]
compare('printed complete margin table', printed,
        [[m['j'], m['A'], m['D'], int(m['scaled_margin'])] for m in margins])

# Reconstruct the mathematical meaning of every constructor comparison.
# Equalities with prior L084 data must equal independently rebuilt quantities;
# a constructor pass flag is never treated as evidence.
checks = {}


def expect(name, actual, relation, required):
    a, b = F(actual), F(required)
    passed = {'=': a == b, '<': a < b, '>': a > b, '>=': a >= b}[relation]
    if name in checks:
        failures.append('duplicate expected comparison '+name)
    checks[name] = dict(name=name, actual=a, relation=relation, required=b,
                        difference=a-b, passed=passed)
    if not passed:
        failures.append('independent inequality '+name)


for key, value in dict(U=U, T=T, ell=ell, u=q, v=w).items():
    expect('L084 S constant '+key, value, '=', value)
expect('positive budget', B, '>', 0)
for i in range(25):
    expect(f'row{i} J domain', J[i], '>=', 2)
    expect(f'row{i} H domain', H[i], '>=', 3)
    if i:
        expect(f'row{i} increasing J', J[i], '>', J[i-1])
expect('J1 for residual', J[1], '=', 15)
expect('positive cap residual', lam-E, '>', 0)
expect('cap', R, '<', U)
expect('cap matches L084 independent datum', R, '=', R)
expect('U below exp24 lower sum', U, '<', exp_lower)
expect('prefix H floor', min(H[:21]), '=', 5)
expect('uniform prefix tail2 offset', prefix_upper, '<', 0)
expect('recipient H floor', min(H[1:22]), '=', 72)
expect('uniform recipient Q lower', recipient_q, '>', kap*2**20)
expect('failed full-package row0 tail20 datum retained', Q0, '<', kap*2**20)
for o in offsets:
    i, f, v = o['i'], o['H_floor'], o['Q_lower']
    expect(f'row{i} O index', i, '=', i)
    expect(f'row{i} O floor', f, '=', f)
    expect(f'row{i} O offset', o['tail2_upper'], '=', o['tail2_upper'])
    if i <= 20:
        expect(f'prefix row{i} negative tail2 offset upper', o['tail2_upper'], '<', 0)
    if i:
        expect(f'recipient{i} S index', i, '=', i)
        expect(f'recipient{i} S floor', f, '=', f)
        expect(f'recipient{i} S Q', v, '=', v)
        expect(f'recipient{i} negative tail20 offset upper', o['tail20_upper'], '<', 0)
for i in range(25):
    expect(f'incoming{i} A matches L084', A[i], '=', A[i])
    expect(f'incoming{i} D matches L084', D[i], '=', D[i])
for m in margins:
    i = m['j']
    for key in ('j', 'A', 'D', 'margin'):
        expect(f'recipient{i} matches L084 {key}', m[key], '=', m[key])
    old_a = sum(3*J[k]+H_original[k] for k in range(i+1))
    old_d = sum(4*J[k]+H_original[k]+2 for k in range(i+1))
    expect(f'recipient{i} A shift', A[i+1]-old_a, '=', -35)
    expect(f'recipient{i} D shift', D[i+1]-old_d, '=', -35)
    expect(f'recipient{i} positive A', m['A'], '>', 0)
    expect(f'recipient{i} positive log2 coefficient', m['log2_coefficient'], '>', 0)
    expect(f'recipient{i} rejection', m['margin'], '>', F(47, 2))
expect('total K', K, '=', 397573379)
expect('total N', N, '=', 630138897)
saved_names = [c['name'] for c in saved['checks']]
verify('complete unique comparison names', len(saved_names) == len(set(saved_names)) ==
       len(checks) == 502 and set(saved_names) == set(checks))
for c in saved['checks']:
    if c['name'] in checks:
        compare('checks/'+c['name'], c, checks[c['name']])

core = dict(rows=rows, B=B,
    constants=dict(kappa=kap, U=U, T=T, ell=ell, log3_upper=q,
                   logv_upper=w, lambda_lower=lam, E=E, R=R),
    uniform_offsets=dict(prefix_H_floor=5, prefix_tail2_upper=prefix_upper,
        recipient_H_floor=72, recipient_Q_lower=recipient_q,
        required_Q=kap*2**20, failed_row0_Q=Q0),
    offsets=offsets, prefixes=[dict(i=i, A=A[i], D=D[i]) for i in range(25)],
    margins=margins, exponential_terms=terms, exp24_lower=exp_lower,
    summary=dict(checks=502, recipients=21, minimum_j=4,
        minimum_margin=minimum['margin'], required_margin=F(47, 2),
        failures=[], passed=True, parameter_samples=0))
for key, value in core.items():
    compare(key, saved[key], value)
source_records = []
for path in [table_path, HERE/'h-transfer-family-certificate.json']:
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(65536), b''):
            digest.update(chunk)
    source_records.append(dict(path=str(path.relative_to(ROOT)), sha256=digest.hexdigest()))
compare('sources', saved['sources'], source_records)

out = HERE/'d35-earlier-recipients-audit-certificate.json'
result = dict(scope='L103 conditional d35 full-simplex critical audit; b0=0 assumed',
    construction_sha256=hashlib.sha256(raw).hexdigest(),
    independent_data=core, analytic=dict(logs=logs, lambda_lower=lambda_lo,
        lambda_upper=lambda_hi), reconstructed_checks=list(checks.values()),
    leaf_comparisons=comparisons, proof_checks=proof_checks,
    summary=dict(leaf_comparisons=len(comparisons), proof_checks=len(proof_checks),
        constructor_comparisons=len(checks), failures=failures,
        minimum_j=minimum['j'], minimum_margin=minimum['margin'],
        required_margin=F(47, 2), cap=R, cap_upper=U,
        lambda_floor_1e14=(lambda_lo*10**14).__floor__(),
        lambda_ceil_1e14=-(-lambda_hi*10**14).__floor__(), parameter_samples=0,
        passed=not failures),
    limitations='Quantified coverage is justified in L103, not by sampling; no '
        'row0 elimination, assembly, realization or universal descent claimed.')
out.write_text(json.dumps(result, indent=2, default=str)+'\n')
print(f'Constructor comparisons: {len(checks)}; leaf comparisons: {len(comparisons)}; '
      f'proof/container checks: {len(proof_checks)}; failures: {failures}')
print(f'Lambda interval times 10^14 inside '
      f"({result['summary']['lambda_floor_1e14']},{result['summary']['lambda_ceil_1e14']}); "
      'required lower >10584')
print(f'Cap R={R}; required <{U}; exp24 lower >{exp_lower.__floor__()}')
print(f'Prefix offset={prefix_upper}<0; recipient Q={recipient_q}>{kap*2**20}')
print(f"Minimum M({minimum['j']})={minimum['margin']}; required >47/2; samples=0")
print(f'Full evidence: {out.relative_to(ROOT)}')
if failures:
    raise SystemExit(1)
