#!/usr/bin/env python3
"""Independent exact arithmetic audit of the fixed L053 certificate.

No generator imports. Read every operand; check all stored rounded terms;
independently use 144 unrounded terms with argument-specific remainders.
Only r=24 is tested. Regeneration takes place in a temporary directory.
"""
from fractions import Fraction as Q
from pathlib import Path
from tempfile import TemporaryDirectory
import hashlib
import json
import shutil
import subprocess
import sys

# Exact, locally generated rational certificates can exceed the default limit.
sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'twenty-four-height-certificate.json'
raw = SOURCE.read_bytes()
saved = json.loads(raw)
checks, base_evidence, independent_evidence = [], {}, {}


def check(name, actual, required, relation='='):
    passed = actual == required if relation == '=' else actual < required
    checks.append(dict(name=name, actual=actual, required=required,
                       relation=relation, passed=passed))


def base(label, v, row):
    x = (v-1)/(v+1)
    check(label+' schema', sorted(row), sorted(['x', 'rounded_summands',
          'rounding_budget', 'remainder_upper']))
    check(label+' x', Q(row['x']), x)
    check(label+' domain', 0 <= x <= Q(1, 3), True)
    check(label+' term count', len(row['rounded_summands']), 96)
    term, evidence = 2*x, []
    for j, value in enumerate(row['rounded_summands']):
        exact = term*2**192
        check(f'{label} rounded term {j}',
              type(value) is int and value <= exact < value+1, True)
        evidence.append(dict(index=j, exact_term=term, rounded=value))
        term *= x*x*Q(2*j+1, 2*j+3)
    budget, remainder = Q(96, 2**192), Q(9, 4*193*3**193)
    check(label+' rounding budget', Q(row['rounding_budget']), budget)
    check(label+' remainder', Q(row['remainder_upper']), remainder)
    base_evidence[label] = evidence
    lo = Q(sum(row['rounded_summands']), 2**192)
    return lo, lo+budget+remainder


def series(v):
    x = (v-1)/(v+1)
    assert 0 <= x <= Q(1, 3)
    # Horner evaluation of the unrounded polynomial, unlike the generator.
    polynomial = Q(0)
    for j in reversed(range(144)):
        polynomial = Q(1, 2*j+1)+x*x*polynomial
    lo = 2*x*polynomial
    error = 2*x**289/(289*(1-x*x))
    return lo, lo+error, dict(x=x, terms=144, polynomial=polynomial,
                            lower=lo, remainder_upper=error)


ell0, ell1 = base('base log2', Q(2), saved['precision']['log2_detail'])
check('precision', [saved['precision']['bits'], saved['precision']['terms']], [192, 96])
il2, iu2, independent_evidence['base log2'] = series(Q(2))
original, independent = {}, {}
for key, row in saved['logs'].items():
    t = Q(key)
    # Normalize with increasing powers, independently of repeated division.
    k = 0
    while Q(2**(k+1)) <= t:
        k += 1
    v = t/Q(2**k)
    check(key+' log schema', sorted(row), sorted(['binary_exponent',
          'reduced_argument', 'lower', 'upper', 'detail']))
    check(key+' exponent', row['binary_exponent'], k)
    check(key+' reduced argument', Q(row['reduced_argument']), v)
    lo, hi = base(key, v, row['detail'])
    original[key] = (lo+k*ell0, hi+k*ell1)
    check(key+' saved lower', Q(row['lower']), original[key][0])
    check(key+' saved upper', Q(row['upper']), original[key][1])
    ilo, ihi, detail = series(v)
    independent[key] = (ilo+k*il2, ihi+k*iu2)
    detail.update(binary_exponent=k, reduced_argument=v,
                  complete_lower=independent[key][0], complete_upper=independent[key][1])
    independent_evidence[key] = detail
    check(key+' independent lower contained', original[key][0], independent[key][0], '<')
    check(key+' independent upper contained', independent[key][1], original[key][1], '<')


def expected_values(logs):
    l2, u2 = logs['2']
    l3, u3 = logs['3']
    lc, uc = logs['11/4']
    rho, count = Q(189, 100), Q(14, 5)
    R23 = (rho**23-1)/(rho-1)
    R24 = (rho**24-1)/(rho-1)
    A, B, M = Q(288982400), Q(282464002), 6900000000
    p, q, inverse = 9809721694, 6189245291, 397573379
    eps_lo, eps_hi = q*l3-p*u2, q*u3-p*l2
    D0 = Q(2208*q+23, 11)
    Kcap, splitcap = count*4850000*29, count*31*2570001
    tail = Q(529, 11)/(Q(27, 10)**30-Q(23, 11))
    comparisons = [
        ('R23', R23, Q(2570000)), ('R24', R24, Q(4850000)),
        ('log24 exponential comparison', Q(24), Q(27, 10)**4),
        ('length remainder', Q(1656, 1034), Q(2)),
        ('logM', logs[str(M)][1], Q(227, 10)),
        ('whole-ray derivative', A, Q(M)),
        ('whole-ray value', A*Q(227, 10)+B, Q(M)),
        ('epsilon positive', Q(0), eps_lo),
        ('epsilon upper', eps_hi, Q(958, 10**13)),
        ('log2 lower', Q(6931, 10000), l2),
        ('quarter-log separation', Q(1, 4), Q(6931, 10000)-Q(2*M, 3)*Q(958, 10**13)),
        ('minimum height below 28', D0, Q(163, 60)**28),
        ('K coarse upper', Kcap, Q(394000000)),
        ('minimum height above 15', count*4850000*16, Q(225640000)),
        ('two small heights impossible', splitcap, Q(225640000)),
        ('other 23 reciprocal terms', tail, Q(1, 10**11)),
        ('minimum real height exceeds million', Q(10**6), Q(27, 10)**15),
        ('endpoint positive shift error', Q(92, 11*10**6), Q(1, 100000))]
    caps = {}
    for z, height in [(32, Q(21)), (63, Q(98, 5))]:
        lam = (z*Q(6931, 10000)-394000000*Q(958, 10**13))/q
        denom = lam-Q(1, 10**11)
        D = Q(23, 11)+Q(23, 11)/denom
        caps[str(z)] = dict(lambda_lower=str(lam), mass_denominator=str(denom),
                            s0_upper=str(D), h0_upper=str(height))
        comparisons.extend([(f'z={z} mass denominator positive', Q(0), denom),
                            (f'z={z} minimum log-height', logs[str(D)][1], height)])
    comparisons.extend([
        ('z=32 count contradiction', count*4850000*22, Q(343857546)),
        ('compact log2 lower for floors', Q(693147180559, 10**12), l2),
        ('compact log3 upper for floors', u3, Q(1098612288669, 10**12)),
        ('compact c upper for floors', uc, Q(1011600911679, 10**12)),
        ('positive alpha lower', Q(0), 3*l3-4*u2),
        ('positive beta lower', Q(0), l3-u2),
        ('z>=63 total odd-count contradiction', Q(224363706), Q(225640000))])
    operands = dict(R23=str(R23), R24=str(R24), A=str(A), B=str(B), M=M,
                    p=p, q=q, epsilon_lower=str(eps_lo), epsilon_upper=str(eps_hi),
                    D0=str(D0), K_cap=str(Kcap), two_small_cap=str(splitcap),
                    tail_upper=str(tail), inverse=inverse,
                    modular_identity=630138897*q-inverse*p, floor_scale=10**12,
                    E=693147180559, T=1098612288669, C=1011600911679,
                    alpha_upper=str(Q(523248143771, 10**12)),
                    beta_upper=str(Q(405465108110, 10**12)))
    return comparisons, operands, caps


comparisons, operands, caps = expected_values(original)
check('complete operand schema', sorted(saved['operands']), sorted(operands))
for key, value in operands.items():
    check('operand '+key, saved['operands'][key], value)
check('complete height caps', saved['height_caps'], caps)
check('all log arguments', sorted(saved['logs']), sorted(['2', '3', '11/4',
      '6900000000']+[v['s0_upper'] for v in caps.values()]))
check('sign count', len(saved['checks']), 29)
for row, (name, actual, required) in zip(saved['checks'], comparisons):
    check(name+' complete saved comparison', row, dict(name=name,
          actual=str(actual), required=str(required), relation='<',
          margin=str(required-actual), passed=actual < required))
    check(name+' rational sign', actual, required, '<')
for name, actual, required in expected_values(independent)[0]:
    check(name+' independent sign', actual, required, '<')

# Independently rearrange the delicate residual via log(3/2).
lv, uv, detail = series(Q(3, 2))
ep0 = (6189245291-9809721694)*iu2+6189245291*lv
ep1 = (6189245291-9809721694)*il2+6189245291*uv
independent_evidence['rearranged epsilon'] = dict(lower=ep0, upper=ep1, log_three_halves=detail)
check('rearranged epsilon positive', Q(0), ep0, '<')
check('rearranged epsilon upper', ep1, Q(958, 10**13), '<')
check('Bezout identity', 630138897*6189245291-397573379*9809721694, 1)
residues = []
for z in range(1, 63):
    quotient, residue = divmod(397573379*z, 6189245291)
    residues.append(dict(z=z, K=residue))
    expected_quotient = 0 if z <= 15 else 1 if z <= 31 else 2 if z <= 46 else 3
    check(f'z={z} quotient range', quotient, expected_quotient)
    check(f'z={z} full residue', saved['residues'][z-1], residues[-1])
check('residue count', len(saved['residues']), 62)
check('survivors', saved['survivors'], [dict(z=32, K=343857546)])
check('independent survivors', [r for r in residues if 225640000 < r['K'] < 394000000],
      [dict(z=32, K=343857546)])
rho = Q(189, 100)
splits = []
for j in range(1, 24):
    split = (rho**j+rho**(24-j)-2)/(rho-1)
    extremum = 1+(rho**23-1)/(rho-1)
    check(f'split {j} extremum', split <= extremum, True)
    splits.append(dict(j=j, sum=split, extremum=extremum))

# Reconstruct all integer divisions using divmod and check every full row.
v, E, C, a, b, S = 19600000000000, 693147180559, 1011600911679, 523248143771, 405465108110, 10**12
greedy, total = [], 0
check('floor row count', len(saved['greedy']), 24)
for i in range(24):
    jnum = v+C
    J, jr = divmod(jnum, 4*E)
    hnum = v+J*a
    H, hr = divmod(hnum, E)
    nv = v+J*a+H*b-2*E+10**7
    row = dict(i=i, U_numerator=v, U=str(Q(v, S)), J_argument=str(Q(jnum, 4*E)), J=J,
               H_argument=str(Q(hnum, E)), H=H, odd_count_upper=3*J+H,
               next_U=str(Q(nv, S)), next_numerator=nv)
    check(f'floor row {i} complete', saved['greedy'][i], row)
    check(f'floor row {i} positive operands', min(v, jnum, hnum, nv, a, b) > 0, True)
    check(f'floor row {i} J remainder', 0 <= jr < 4*E, True)
    check(f'floor row {i} H remainder', 0 <= hr < E, True)
    check(f'floor row {i} minimum parameters', J >= 2 and H >= 3, True)
    greedy.append(dict(**row, J_remainder=jr, J_divisor=4*E,
                       H_remainder=hr, H_divisor=E))
    total += 3*J+H
    v = nv
check('saved total', saved['greedy_total'], total)
check('total as claimed', total, 224363706)
check('count threshold', total, 225640000, '<')
published_pairs = [(7, 33), (13, 60), (23, 111), (43, 206), (81, 386),
    (152, 724), (286, 1362), (539, 2563), (1015, 4827), (1912, 9092),
    (3602, 17127), (6786, 32267), (12785, 60791), (24087, 114532),
    (45382, 215785), (85502, 406554), (161093, 765978), (303511, 1443161),
    (571838, 2719027), (1077389, 5122862), (2029885, 9651877),
    (3824465, 18184902), (7205596, 34261800), (13575916, 64551955)]
check('complete L053 printed parameter table', [(r['J'], r['H']) for r in greedy],
      published_pairs)

# Stored decimal inspection is checked for faithful outward rounding, not used as proof.
def interval(t):
    unit = 10**12
    n = (Q(t)*unit).__floor__()
    return [str(Q(n, unit)), str(Q(n+1, unit))]

expected_inspection = dict(checks=[dict(name=name, actual=interval(actual),
    required=interval(required), margin_lower=str(Q(((required-actual)*10**12).__floor__(), 10**12)),
    passed=actual < required) for name, actual, required in comparisons],
    greedy=[dict(i=r['i'], U_numerator=r['U_numerator'], J=r['J'], H=r['H'],
        J_argument=interval(r['J_argument']), H_argument=interval(r['H_argument']),
        odd_count_upper=r['odd_count_upper']) for r in saved['greedy']])
check('complete inspection values', saved['inspection'], expected_inspection)
check('source target', saved['target'], 'L051 (1)-(4) at r=24')
check('source failures', saved['failures'], [])
check('source complete schema', sorted(saved), sorted(['target', 'precision', 'logs',
      'operands', 'residues', 'survivors', 'height_caps', 'greedy', 'greedy_total', 'checks',
      'inspection', 'failures']))

# Recheck the L052 analytic coefficient enclosures used at every occurrence.
check('log2 coarse lower', Q(6931, 10000), independent['2'][0], '<')
check('log3 coarse upper', independent['3'][1], Q(10987, 10000), '<')
check('c coarse upper', independent['11/4'][1], Q(41, 40), '<')
check('delta upper', Q(10987, 6931), Q(793, 500), '<')
check('odd count height coefficient', Q(19395, 6931), Q(14, 5), '<')
check('odd count additive coefficient', Q(77039, 55448), Q(7, 5), '<')
check('transfer height coefficient', Q(1886547, 1000000), Q(189, 100), '<')
check('transfer additive coefficient', Q(12322427, 40000000), Q(31, 100), '<')
check('e partial sum', sum((Q(1, k) for k in [1, 1, 2, 6, 24, 120]), Q(0)), Q(163, 60))
check('whole ray exact value', 6900000000-Q(227, 10)*288982400-282464002, Q(57635518))
check('separation exact value', Q(6931, 10000)-4600000000*Q(958, 10**13), Q(12621, 50000))

with TemporaryDirectory() as temp:
    generator = Path(temp)/'certify_twenty_four_heights.py'
    shutil.copyfile(ROOT/generator.name, generator)
    proc = subprocess.run([sys.executable, str(generator)], capture_output=True, text=True)
    check('regeneration exit', proc.returncode, 0)
    regenerated = generator.with_name(SOURCE.name).read_bytes()
    check('regeneration identical', regenerated == raw, True)
check('original preserved', SOURCE.read_bytes() == raw, True)

def serialize(value):
    if isinstance(value, Q):
        return str(value)
    if isinstance(value, dict):
        return {k: serialize(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [serialize(v) for v in value]
    return value

failures = [c['name'] for c in checks if not c['passed']]
output = ROOT/'twenty-four-height-audit-certificate.json'
result = dict(target='L053 audit under L051 (1)-(4) at r=24',
              original_sha256=hashlib.sha256(raw).hexdigest(),
              checks=checks, failures=failures, rounding_evidence=base_evidence,
              independent_evidence=independent_evidence, operands=operands,
              splits=splits, residues=residues, greedy=greedy,
              total=total, required_lower_bound=225640000,
              threshold_margin=225640000-total)
output.write_text(json.dumps(serialize(result), indent=2)+'\n')
print(f'Audit checks: {len(checks)}; failures: {failures}')
print('N<6900000000; whole-ray margin 57635518; K<393820000')
print('z=32: K<298760000 versus K=343857546')
print(f'z>=63: K<={total}; required K>225640000; margin {225640000-total}')
print(f'Index 18 J remainder: {greedy[18]["J_remainder"]}/{greedy[18]["J_divisor"]}')
print(f'Index 18 H remainder: {greedy[18]["H_remainder"]}/{greedy[18]["H_divisor"]}')
print(f'Original SHA-256: {result["original_sha256"]}')
print(f'Certificate: {output}')
if failures:
    raise SystemExit(1)
