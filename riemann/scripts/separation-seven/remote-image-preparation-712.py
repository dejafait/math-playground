#!/usr/bin/env python3
"""Exact small checks for C998s; no Gram entries or large arrays are computed."""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parent
OUT = BASE / 'remote-image-preparation-712.json'
WITNESS = BASE / 'defect-window-fixed-pair-707-witness.json'
checks, failures = [], []


def check(label, condition):
    ok = bool(condition)
    checks.append(dict(label=label, passed=ok))
    if not ok:
        failures.append(label)


frozen = json.loads(WITNESS.read_text())
digest = sha256(WITNESS.read_bytes()).hexdigest()
check('unchanged frozen witness', digest ==
      '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a')
coordinates = {}
for key in ('alpha_free', 'beta_free'):
    v = [Q(s) for s in frozen[key]]
    l1 = sum(map(abs, v), Q())
    check(key + ' all510 exact dyadics', len(v) == 510 and all(
          q.denominator & (q.denominator - 1) == 0 for q in v))
    check(key + ' nonzero', any(v))
    check(key + ' complete l1 below3', l1 < 3)
    coordinates[key] = dict(count=len(v), nonzero=sum(q != 0 for q in v),
                            exact_l1=str(l1), free_l1_upper='3',
                            raw_l1_upper='6')

# Exact prime-power enumeration, without a prime or floating-log oracle.
primes, active = [], []
for p in range(2, 4096):
    if any(p % q == 0 for q in primes if q*q <= p):
        continue
    primes.append(p)
    n, exponent = p, 1
    while n < 4096:
        if 3**13 < n*n < 3**15:
            active.append(dict(n=n, p=p, exponent=exponent))
        n *= p
        exponent += 1
active.sort(key=lambda a: a['n'])
check('all334 separation14 prime powers', len(active) == 334)
check('zero-delay identity shift retained', any(a['n'] == 2187 for a in active))
check('frozen3125 structural test active',
      dict(n=3125, p=5, exponent=5) in active and 3125 > 2187)
check('all active n between1024 and4096', all(1024 < a['n'] < 4096 for a in active))
check('prime mass bound', Q(9, 32) < Q(1, 3) and Q(334, 3) < 112)

# Prose establishes ell in(1/2,3/5), all r_n<1, K/derivative<1,
# det(G)>1/192, and ||e_+||,||e_-||<1. These are not software proofs.
v_shift = Q(3, 5)*50000 + 24
v_w = 112*v_shift + 5
t_bound = 384*768
v_projection = Q(3, 5)*Q(3, 4)*2*t_bound
v_h = v_w + v_projection
sup_h = 1352 + Q(3, 2)*2*t_bound
check('K derivative geometric comparison',
      (Q(5, 2)/Q(3, 4) + Q(1, 2)/Q(3, 4)**2)/16 < 1)
check('projection coefficient bound', t_bound == 294912)
check('total variation below2^22', v_h < 2**22)
check('supremum below2^20', sup_h < 2**20)
check('image L2 below768', 113*6 < 768)

B, H, N = 2**24, 2**10, 2**136
eps2 = Q(B*B, N-1)
eps_upper = Q(1, 2**43)
d_tail = Q(651*B*B, N-1)  # log(N-1)<136, integral constant515.
s_tail = 128*H*eps_upper
diagonal_tail = d_tail+s_tail
tg_tail = 30*eps_upper
remote_tail = eps2
check('L2 tail epsilon below2^-43', eps2 < eps_upper**2)
check('diagonal logarithmic tail below2^-77', d_tail < Q(1, 2**77))
check('S cross-and-tail allowance2^-26', s_tail == Q(1, 2**26))
check('diagonal truncation below2^-25', diagonal_tail < Q(1, 2**25))
check('Tg pairing truncation below2^-38', tg_tail < Q(1, 2**38))
check('remote norm-square tail below2^-87', remote_tail < Q(1, 2**87))
check('all ideal truncation errors below1e-6',
      max(diagonal_tail, tg_tail, remote_tail) < Q(1, 10**6))

work = dict(retained_modes=N, input_modes=512, prime_shifts=334,
            direct_U_shift_primitive_evaluations=334*512*N,
            direct_Tg_shift_primitive_evaluations=16*512*N,
            direct_combined_shift_primitive_evaluations=350*512*N,
            stored_h_coefficient_slots=N,
            illustrative_16_bytes_per_slot=16*N,
            full_entry_precision=None, full_entry_work_bound=None,
            full_batch_executed=False,
            scope='Exact counts of the specified direct truncated-coefficient subtask only; not necessary complexity bounds or a complete entry plan.')
result = dict(step='712', source_script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
              witness_sha256=digest, checks=checks, failures=failures,
              coordinates=coordinates, active_prime_powers=active,
              bounds=dict(variation_w=str(v_w), projection_coefficient=str(t_bound),
                          variation_projection=str(v_projection), variation_h=str(v_h),
                          supremum_h=str(sup_h), cosine_coefficient_constant=B,
                          epsilon_squared=str(eps2), epsilon_upper=str(eps_upper),
                          diagonal_log_tail=str(d_tail), bounded_S_tail=str(s_tail),
                          full_diagonal_truncation=str(diagonal_tail), Tg_pair_tail=str(tg_tail),
                          remote_norm_square_tail=str(remote_tail), required_entry_error='1/1000000'),
              work=work,
              qualifications=['C998s contains the analytic/domain and non-head proof; it is not independently audited.',
                              'All inherited analytic-response, neutral-core, arithmetic and c_star qualifications persist.',
                              'Only truncation errors are bounded. Finite continuous-response, moments, all S entries, D evaluation and arithmetic are unpaid.',
                              'No complete1e-6 entry certificate, signed Gram, S3 or RH conclusion.'])
OUT.write_text(json.dumps(result, indent=2)+'\n')
print('Exact preparation checks:', len(checks), '; failures:', failures)
print('Var(h) upper:', v_h, '; required <', 2**22)
print('Ideal diagonal truncation upper:', float(diagonal_tail), '; entry target:', 1e-6)
print('Chosen retained modes:', N)
print('Direct U shift primitive evaluations:', work['direct_U_shift_primitive_evaluations'])
print('Complete entry precision/work: UNPAID; full batch executed: false')
print('Certificate:', OUT.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
