#!/usr/bin/env python3
"""Independent exact C998s arithmetic audit; no Gram or large-mode batch."""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial, isqrt
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
ORIGINAL = BASE / 'remote-image-preparation-712.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
OUT = BASE / 'remote-image-preparation-audit-714.json'
old = json.loads(ORIGINAL.read_text())
witness = json.loads(WITNESS.read_text())
checks, failures, replay = [], [], []


def check(label, condition, original=False):
    ok = bool(condition)
    checks.append({'label': label, 'passed': ok})
    if original:
        replay.append({'label': label, 'passed': ok})
    if not ok:
        failures.append(label)


digest = sha256(WITNESS.read_bytes()).hexdigest()
check('unchanged frozen witness', digest ==
      '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a', True)
check('original script pin', old['source_script_sha256'] ==
      sha256((BASE / 'remote-image-preparation-712.py').read_bytes()).hexdigest())
check('original witness pin', old['witness_sha256'] == digest)

coordinates = {}
for name in ('alpha_free', 'beta_free'):
    values = [Q(s) for s in witness[name]]
    rows = [{'n': n, 'parity': n % 2, 'exact_value': str(v),
             'r_bound_case': 'odd denominator comparison' if n % 2 else 'even 2/401 bound'}
            for n, v in enumerate(values, 2)]
    sums = [sum((abs(v) for n, v in enumerate(values, 2) if n % 2 == p), Q())
            for p in (0, 1)]
    total = sums[0] + sums[1]
    check(name + ' all510 exact dyadics', len(values) == 510 and all(
          v.denominator == 1 << (v.denominator.bit_length()-1) for v in values), True)
    check(name + ' nonzero', any(v != 0 for v in values), True)
    check(name + ' complete l1 below3', total < 3, True)
    check(name + ' every coordinate nonzero', all(v != 0 for v in values))
    check(name + ' every completion factor case', all(
          (r['n'] >= 3 and r['n']**2 > 1) if r['parity'] else
          (5*r['n'] >= 10 and Q(2, 401) < Q(1, 200)) for r in rows))
    check(name + ' full recorded coordinate summary', old['coordinates'][name] == dict(
          count=len(values), nonzero=sum(v != 0 for v in values), exact_l1=str(total),
          free_l1_upper='3', raw_l1_upper='6'))
    coordinates[name] = dict(rows=rows, parity_l1=list(map(str, sums)),
                             complete_l1=str(total), raw_l1_strict_upper='6')

# Independent enumeration: factor every candidate integer, not prime generation.
check('complete candidate interval', 1024**2 < 3**13 and 4096**2 > 3**15)
active, candidate_factors = [], []
for n in range(1025, 4096):
    if not (3**13 < n*n < 3**15):
        continue
    rest, factors = n, []
    for d in range(2, isqrt(n)+1):
        if rest % d:
            continue
        exponent = 0
        while rest % d == 0:
            exponent += 1
            rest //= d
        factors.append([d, exponent])
    if rest > 1:
        factors.append([rest, 1])
    product = 1
    for p, exponent in factors:
        product *= p**exponent
    assert product == n
    candidate_factors.append(dict(n=n, factors=factors))
    if len(factors) == 1:
        p, exponent = factors[0]
        active.append(dict(n=n, p=p, exponent=exponent))
check('all334 separation14 prime powers', len(active) == 334, True)
check('zero-delay identity shift retained', dict(n=2187, p=3, exponent=7) in active, True)
check('frozen3125 structural test active', dict(n=3125, p=5, exponent=5) in active
      and 3125 > 3**7, True)
check('all active n between1024 and4096', all(1024 < r['n'] < 4096 for r in active), True)
check('prime mass bound', Q(9, 32) < Q(1, 3) and Q(len(active), 3) < 112, True)
check('complete original prime list equality', active == old['active_prime_powers'])
events = [dict(n=r['n'], kind='entrance' if r['n'] > 2187 else
               'exit' if r['n'] < 2187 else 'identity',
               squared_exit_collision_residual=3125**2-3*r['n']**2,
               entrance_index_difference=r['n']-3125) for r in active]
check('all actual exits distinct from frozen entrance', all(
      row['squared_exit_collision_residual'] != 0 for row in events))
check('only the frozen entrance has the frozen index', sum(
      row['entrance_index_difference'] == 0 for row in events) == 1)
check('universal exit exclusion modulo3', 3125**2 % 3 == 1)

# Local elementary comparisons used by the prose analytic estimates.
e_upper = sum((Q(1, factorial(j)) for j in range(6)), Q()) + Q(1, 720)*Q(7, 6)
check('ell lower via exp1<3', e_upper < 3)
check('ell upper via exp6/5>3', sum((Q(6, 5)**j/factorial(j) for j in range(5)), Q()) > 3)
check('log4096<9', sum((Q(3, 4)**j/factorial(j) for j in range(4)), Q()) > 2)
check('projection exponential upper', 3 < Q(3, 2)**4)
check('kernel geometric ratios', 1+13 > 4 and 1+Q(65, 4) > 16)
kernel_derivative = Q(1, 16)*(Q(5, 2)/Q(3, 4)+Q(1, 2)/Q(3, 4)**2)
check('K derivative geometric comparison', kernel_derivative < 1, True)
check('kernel image supremum and variation', Q(3, 5)*12 < 8 and Q(3, 5)**2*12 < 5)
check('profile derivative bound', 6*2*511*8 == 49056 and 49056 < 50000)
check('Gram determinant rational floor', Q(1, 2)**4/12 == Q(1, 192))

vw = 112*(Q(3, 5)*50000+24)+5
t = 2*192*768
vp = Q(3, 5)*Q(3, 4)*(2*t)
vh = vw+vp
sup = 1352+3*t
check('projection coefficient bound', t == 294912, True)
check('total variation below2^22', vh < 2**22, True)
check('supremum below2^20', sup < 2**20, True)
check('image L2 below768', 113*6 < 768, True)
check('actual Fourier bound below2^24', 4*vh < 2**24)
check('complete S bound below64', Q(46, 5)/Q(1, 5) < 64)
check('digamma remainder uniformly below1', Q(2, 1)/(6*Q(257, 4)**2) < 1)

B, H, N = 2**24, 2**10, 2**136
eps2 = Q(B**2, N-1)
eps = Q(1, 2**43)
dtail = Q((515+136)*B**2, N-1)
stail = 128*H*eps
diagonal = dtail+stail
tg, remote = 30*eps, eps2
check('L2 tail epsilon below2^-43', eps2 < eps**2, True)
check('diagonal logarithmic tail below2^-77', dtail < Q(1, 2**77), True)
check('S cross-and-tail allowance2^-26', stail == Q(1, 2**26), True)
check('diagonal truncation below2^-25', diagonal < Q(1, 2**25), True)
check('Tg pairing truncation below2^-38', tg < Q(1, 2**38), True)
check('remote norm-square tail below2^-87', remote < Q(1, 2**87), True)
check('all ideal truncation errors below1e-6', max(diagonal, tg, remote) < Q(1, 10**6), True)
check('Tg L2 bound below30', Q(471, 100)*6 < 30)
bounds = dict(variation_w=str(vw), projection_coefficient=str(t),
              variation_projection=str(vp), variation_h=str(vh), supremum_h=str(sup),
              cosine_coefficient_constant=B, epsilon_squared=str(eps2), epsilon_upper=str(eps),
              diagonal_log_tail=str(dtail), bounded_S_tail=str(stail),
              full_diagonal_truncation=str(diagonal), Tg_pair_tail=str(tg),
              remote_norm_square_tail=str(remote), required_entry_error='1/1000000')
check('every original bound exactly reproduced', bounds == old['bounds'])
work = dict(retained_modes=N, input_modes=512, prime_shifts=len(active),
            direct_U_shift_primitive_evaluations=len(active)*512*N,
            direct_Tg_shift_primitive_evaluations=16*512*N,
            direct_combined_shift_primitive_evaluations=(len(active)+16)*512*N,
            stored_h_coefficient_slots=N, illustrative_16_bytes_per_slot=16*N,
            full_entry_precision=None, full_entry_work_bound=None, full_batch_executed=False)
check('every original work value exactly reproduced', all(old['work'][k] == v for k, v in work.items()))
check('all24 original checks independently reproduced', len(replay) == 24 and replay == old['checks'])
check('original recorded failures empty', old['failures'] == [])
result = dict(step='714', script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
              original_certificate_sha256=sha256(ORIGINAL.read_bytes()).hexdigest(),
              witness_sha256=digest, checks=checks, failures=failures,
              original_checks_replayed=replay, coordinates=coordinates,
              candidate_factorizations=candidate_factors, active_prime_powers=active,
              all_shift_boundary_checks=events, bounds=bounds, work=work,
              correction=dict(old_exit='15ell-log(m)', actual_exit='log(m)-13ell',
                              actual_collision='3125^2=3m^2', universal_mod3_residue=1),
              qualifications=['Analytic applicability and corrected isolation are prose proofs in C998s Section6.',
                              'All1020 free coordinates and all334 shifts are checked; exact Z bounds are symbolic, not rounded coordinates.',
                              'No retained entries, Gram, inverse, source-response identity or c_star certificate is evaluated.',
                              'Only ideal output truncation is paid; complete finite-entry precision and work remain unpaid.'])
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('Audit checks:', len(checks), '; original replay:', len(replay), '; failures:', failures)
print('Coordinates:', sum(len(v['rows']) for v in coordinates.values()), '; active shifts:', len(active))
print('Corrected exit collision: 3125^2=3m^2; residue modulo3:', 3125**2 % 3)
print('Variation upper:', vh, '; required <', 2**22)
print('Ideal diagonal truncation upper:', float(diagonal), '; required <', 1e-6)
print('Fixed direct U subtask:', work['direct_U_shift_primitive_evaluations'], 'calls; complete finite-entry work: UNPAID')
print('Certificate:', OUT.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
