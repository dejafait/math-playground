"""Exact bounded rational-root exhaustion, with an independent replay.

Run from the notebook root. No third-party mathematics backend is used.
Every modular trial, raw candidate inspection and evaluation is charged.
The persistent ledger includes previous invocations, including failures.
"""
import hashlib
import itertools
import json
from math import gcd, isqrt, prod
from pathlib import Path

BASE = Path(__file__).resolve().parent
LEDGER = BASE / 'three-isogeny-eligibility-ledger.json'
CERT = BASE / 'three-isogeny-eligibility-certificate.json'
CAPS = {'factor_trials': 10000, 'candidate_work': 200000}
ledger = json.loads(LEDGER.read_text()) if LEDGER.exists() else {
    'caps': CAPS, 'used': dict.fromkeys(CAPS, 0), 'runs': []}
assert ledger['caps'] == CAPS
run = {'status': 'IN_PROGRESS', 'start': ledger['used'].copy(), 'failures': []}
ledger['runs'].append(run)


def save_ledger():
    LEDGER.write_text(json.dumps(ledger, indent=2) + '\n')


def charge(kind, amount=1):
    if ledger['used'][kind] + amount > CAPS[kind]:
        raise RuntimeError('Cumulative cap would be exceeded: ' + kind)
    ledger['used'][kind] += amount


def divisible(n, d):
    charge('factor_trials')
    return n % d == 0


def factor_one(n):
    factors = {}
    d = 2
    while d * d <= n:
        if divisible(n, d):
            factors[d] = factors.get(d, 0) + 1
            n //= d
        else:
            d += 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def factor_two(n):
    # Separate odd-divisor traversal and valuation accumulation.
    out = []
    for d in itertools.chain([2], range(3, isqrt(n) + 1, 2)):
        if d * d > n:
            break
        e = 0
        while divisible(n, d):
            n //= d
            e += 1
        if e:
            out.append((d, e))
    if n != 1:
        out.append((n, 1))
    return dict(out)


def prime_checks(factors):
    # Explicit trial primality certificates; empty trial ranges are valid.
    return [{'p': p, 'trials': [
        [d, not divisible(p, d)] for d in range(2, isqrt(p) + 1)]}
        for p in sorted(factors)]


save_ledger()
try:
    a, b = -2874960, 1739350800
    # At most sqrt(|a|) failed trials plus bit_length(|a|) successes
    # for each of the two factorizations. Check this before either loop.
    factor_bound = 2 * (isqrt(abs(a)) + abs(a).bit_length())
    assert ledger['used']['factor_trials'] + factor_bound <= CAPS['factor_trials']
    f1 = factor_one(abs(a))
    f2 = factor_two(abs(a))
    assert f1 == f2
    assert prod(p ** e for p, e in f1.items()) == abs(a)
    prime_bound = 2 * sum(max(0, isqrt(p) - 1) for p in f1)
    assert ledger['used']['factor_trials'] + prime_bound <= CAPS['factor_trials']
    primality = [prime_checks(f1), prime_checks(f2)]
    assert all(ok for checks in primality for entry in checks for _, ok in entry['trials'])
    # Two traversals: raw inspections plus evaluations <=16*tau.
    # Six additional record passes (table, set construction/comparison,
    # zero filtering, and minimum filtering/reduction) cost <=24*tau.
    # This conservatively charges bookkeeping as well as arithmetic.
    tau = prod(2 * e + 1 for e in f1.values())
    candidate_bound = 40 * tau
    assert ledger['used']['candidate_work'] + candidate_bound <= CAPS['candidate_work']
    save_ledger()

    divisors = [1]
    for p, e in sorted(f1.items()):
        divisors = [d * p ** k for d in divisors for k in range(2 * e + 1)]
    assert len(divisors) == len(set(divisors)) == tau
    records = []
    skipped = 0
    for d in sorted(divisors):
        for sign in (-1, 1):
            m = sign * d
            for n in (1, 3):
                charge('candidate_work')
                if gcd(m, n) != 1:
                    skipped += 1
                    continue
                charge('candidate_work')
                residual = 3*m**4 + 6*a*m*m*n*n + 12*b*m*n**3 - a*a*n**4
                records.append([m, n, residual])

    # Independent organization: exponent tuples, denominator first, reversed
    # signs and Horner evaluation of n^4 * psi_3(m/n). Compare every value.
    charge('candidate_work', len(records))
    table = {(m, n): value for m, n, value in records}
    assert len(table) == len(records)
    replay_keys = set()
    replay_zeros = []
    replay_skipped = 0
    primes = sorted(f2, reverse=True)
    for n in (3, 1):
        for powers in itertools.product(*(range(2*f2[p]+1) for p in primes)):
            magnitude = prod(p**k for p, k in zip(primes, powers))
            for m in (magnitude, -magnitude):
                charge('candidate_work')
                # For the only possible denominators, this is exactly
                # the reduced-fraction condition, independently of gcd.
                if n == 3 and m % 3 == 0:
                    replay_skipped += 1
                    continue
                charge('candidate_work')
                value = (((3*m)*m + 6*a*n*n)*m + 12*b*n**3)*m - a*a*n**4
                assert (m, n) not in replay_keys
                replay_keys.add((m, n))
                assert table[(m, n)] == value
                if value == 0:
                    replay_zeros.append([m, n])
    charge('candidate_work', 2 * len(records))
    assert replay_keys == set(table)
    charge('candidate_work', len(records))
    zeros = [[m, n] for m, n, value in records if value == 0]
    assert sorted(zeros) == sorted(replay_zeros)
    assert skipped == replay_skipped
    discriminant = -16 * (4*a**3 + 27*b*b)
    assert discriminant != 0
    # Charge both the filtering generator and minimum reduction.
    charge('candidate_work', 2 * len(records))
    summary = {
        'model': {'a': a, 'b': b, 'discriminant': discriminant},
        'psi3_descending': [3, 0, 6*a, 12*b, -a*a],
        'factorization_abs_a': sorted(f1.items()),
        'factorization_a_squared': [[p, 2*e] for p, e in sorted(f1.items())],
        'primality_checks': primality,
        'positive_divisors': tau,
        'per_pass': {'raw_candidates': 4*tau, 'skipped_nonreduced': skipped,
                     'evaluated': len(records)},
        'rational_roots': zeros,
        'minimum_absolute_nonzero_residual': min(abs(v) for _, _, v in records if v),
        'all_candidates_replayed': True,
        'all_residuals_agree': True,
        'required_preflight_bounds': {'factor_before_prime_checks': factor_bound,
                                      'prime_checks': prime_bound,
                                      'candidate_work': candidate_bound},
        'cumulative_actual': ledger['used'].copy(), 'caps': CAPS,
        'failures': run['failures']}
    certificate = {'summary': summary, 'all_reduced_candidates_and_residuals': records}
    CERT.write_text(json.dumps(certificate, indent=2) + '\n')
    run.update(status='PASS', end=ledger['used'].copy(),
               certificate_sha256=hashlib.sha256(CERT.read_bytes()).hexdigest())
    save_ledger()
    print(json.dumps(summary, indent=2))
    print('Full certificate:', CERT.relative_to(BASE.parent.parent))
    print('Cumulative ledger:', LEDGER.relative_to(BASE.parent.parent))
except BaseException as error:
    run.update(status='FAIL', end=ledger['used'].copy())
    run['failures'].append(type(error).__name__ + ': ' + str(error))
    save_ledger()
    raise
