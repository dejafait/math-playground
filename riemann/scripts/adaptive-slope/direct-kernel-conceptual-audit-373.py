#!/usr/bin/env python3
"""Independent rational score audit of the existing step372 witnesses.

No candidate generation. Kernel enclosures are checked by the separately
replayed step372 checker; this script uses exact Fraction pairings and a
separate fixed-point exponential to audit every stored score in both
directions. All complete evidence is written beside this script.
"""
from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import comb, factorial, isqrt
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).parent
OUT = HERE / 'direct-kernel-conceptual-audit-373.json'
SCALE = 10**260
ROOT_SCALE = 10**120


def ceildiv(a, b):
    return -(-a // b)


def root(q, scale=ROOT_SCALE):
    assert q >= 0
    k = isqrt(q.numerator * scale * scale // q.denominator)
    assert F(k*k, scale*scale) <= q < F((k+1)**2, scale*scale)
    return F(k, scale), F(k+1, scale)


def exp_positive(bounds):
    """Integer fixed-point enclosure, independent of Decimal exp_ball.

    Divide by 64, use 128 nonnegative Taylor terms plus the uniform
    2/(8^129*129!) tail, and square six times. Every quotient is rounded
    outwards in integer arithmetic. Inputs must lie in [0,8].
    """
    a, b = bounds
    assert 0 <= a <= b <= 8
    lo = (a.numerator*SCALE)//(64*a.denominator)
    hi = ceildiv(b.numerator*SCALE, 64*b.denominator)
    assert hi*8 <= SCALE
    tl = th = sl = sh = SCALE
    for k in range(1, 129):
        tl = tl*lo//(k*SCALE)
        th = ceildiv(th*hi, k*SCALE)
        sl += tl
        sh += th
    sh += ceildiv(2*SCALE, 8**129*factorial(129))
    for _ in range(6):
        sl = sl*sl//SCALE
        sh = ceildiv(sh*sh, SCALE)
    return F(sl, SCALE), F(sh, SCALE)


def interval(v):
    a, b = map(F, v)
    assert a <= b
    return a, b


def times(q, bounds):
    a, b = bounds
    return (q*a, q*b) if q >= 0 else (q*b, q*a)


def pair(weights, column):
    assert len(weights) == len(column)
    rl = rh = il = ih = F(0)
    for (wr, wi), z in zip(weights, column):
        x, y = interval(z['re']), interval(z['im'])
        a, b = times(wr, x), times(-wi, y)
        c, d = times(wr, y), times(wi, x)
        rl += a[0]+b[0]
        rh += a[1]+b[1]
        il += c[0]+d[0]
        ih += c[1]+d[1]
    return (rl, rh), (il, ih)


def modulus(rect):
    lower = upper = F(0)
    for a, b in rect:
        lower += 0 if a <= 0 <= b else min(abs(a), abs(b))**2
        upper += max(abs(a), abs(b))**2
    return root(lower)[0], root(upper)[1]


def enclosed(inner, outer):
    return outer[0] <= inner[0] <= inner[1] <= outer[1]


def record(bounds):
    return [str(x) for x in bounds]


def decimal_display(q):
    with localcontext() as ctx:
        ctx.prec = 16
        return str(Decimal(q.numerator)/Decimal(q.denominator))


def polynomial_check(n):
    older, current = [F(1)], [F(3), F(-1)]
    for j in range(1, n+1):
        nxt = [F(0)]*(len(current)+1)
        for k, a in enumerate(current):
            nxt[k] += (2*j+3)*a
            nxt[k+1] -= a
        for k, a in enumerate(older):
            nxt[k] -= (j+2)*a
        older, current = current, [a/(j+1) for a in nxt]
    current = [a/(n+1) for a in current]
    current[0] -= F(1, n+1)
    binomial = [F((-1)**j*comb(n+3, n+1-j), factorial(j)*(n+1))
                for j in range(n+2)]
    binomial[0] -= F(1, n+1)
    assert current == binomial
    return {'n': n, 'recurrence_equals_binomial_exactly': True,
            'complete_polynomial_coefficients': list(map(str, current))}


report = {'status': 'CHECKING', 'failures': [], 'runs': [],
          'input_sha256': {}, 'polynomial_checks': [],
          'kernel_basis': 'step372 complete-matrix replay and 18 alternate integrals',
          'score_arithmetic': 'exact rational rectangles; integer-root bounds; independent integer fixed-point exponential',
          'required_asymptotic_bound': 'E_n exp(n/64) unbounded on an unbounded integer subsequence for a negative resolution',
          'asymptotic_rate_proved': False, 'optimality_claimed': False}


def load(name):
    data = (HERE/name).read_bytes()
    report['input_sha256'][name] = hashlib.sha256(data).hexdigest()
    return json.loads(data)


def save():
    OUT.write_text(json.dumps(report, indent=2)+'\n')


try:
    replay = load('direct-kernel-paid-leakage-check-372.json')
    assert replay['status'] == 'PASS_FINITE_ONLY' and not replay['failures']
    assert len(replay['runs']) == 2
    assert sum(r['all_kernel_entries_replayed'] for r in replay['runs']) == 5556
    assert sum(r['all_rational_candidates_replayed'] for r in replay['runs']) == 12
    assert all(r['all_assertions_passed'] for r in replay['runs'])
    assert sum(len(r['independent_integral_checks']) for r in replay['runs']) == 18
    assert all(c['overlap'] for r in replay['runs'] for c in r['independent_integral_checks'])
    report['complete_replay_checked'] = {'kernel_entries': 5556, 'witnesses': 12, 'alternate_integrals': 18}
    for n in (16, 32):
        report['polynomial_checks'].append(polynomial_check(n))
        mat = load(f'direct-kernel-paid-leakage-matrix-{n}-372.json')
        cert = load(f'direct-kernel-paid-leakage-{n}-372.json')
        assert mat['n'] == cert['n'] == n
        assert list(map(F, mat['slopes'])) == [F(7,4)+F(l,8*n) for l in range(4*n+1)]
        assert list(map(F, mat['gammas'])) == [F(15,8)+F(j,4*n) for j in range(n+1)]
        columns = mat['kernel_columns']
        assert len(columns) == n+1 and len(cert['results']) == 6
        budget = exp_positive(root(F(n), SCALE))
        scale_exp = exp_positive((F(n,64), F(n,64)))
        results = []
        for index, candidate in enumerate(cert['results']):
            weights = [(F(r),F(i)) for r,i in candidate['rational_weights']]
            assert len(weights) == 4*n+1
            tv_hi = sum(root(r*r+i*i)[1] for r,i in weights)
            assert tv_hi < 1
            tp = pair(weights, mat['target_column'])
            bp = [pair(weights, col) for col in columns]
            assert all(enclosed(v, interval(candidate['target_pairing'][key]))
                       for v,key in zip(tp, ('re','im')))
            assert len(bp) == len(candidate['band_pairings'])
            assert all(enclosed(v, interval(saved[key]))
                       for rect,saved in zip(bp, candidate['band_pairings'])
                       for v,key in zip(rect, ('re','im')))
            action = modulus(tp)
            bands = [modulus(v) for v in bp]
            leakage = max(v[0] for v in bands), max(v[1] for v in bands)
            assert enclosed(action, interval(candidate['target_modulus']))
            assert leakage[1] <= F(candidate['band_modulus_upper'])
            assert enclosed(budget, interval(candidate['budget']))
            score = action[0]-budget[1]*leakage[1], action[1]-budget[0]*leakage[0]
            assert F(candidate['raw_score_lower']) <= score[0]
            assert F(candidate['E_n_lower']) <= max(F(0), score[0])
            assert F(candidate['scaled_lower']) <= max(F(0), score[0])*scale_exp[0]
            if n == 32:
                assert score[1] < 0
            if n == 16 and index == 4:
                assert action[0] > F('0.01053829296')
                assert leakage[1] < F('0.000097692880')
                assert score[0] > F('0.00520444248')
                assert score[0]*scale_exp[0] > F('0.00668263642')
            results.append({'index': index, 'method': candidate['method'],
                            'iterations': candidate['iterations'],
                            'exact_tv_upper': str(tv_hi),
                            'rational_target_pairing': [record(x) for x in tp],
                            'rational_band_pairings': [[record(x) for x in z] for z in bp],
                            'target_modulus': record(action),
                            'band_moduli': [record(x) for x in bands],
                            'leakage': record(leakage), 'raw_score': record(score),
                            'score_sign': 'NEGATIVE' if score[1] < 0 else 'POSITIVE' if score[0] > 0 else 'UNDECIDED',
                            'stored_claims_contained': True})
            print(f'n={n} candidate={index}: score approximately {decimal_display((score[0]+score[1])/2)}; certified sign={results[-1]["score_sign"]}; TV<1; exact bounds in artifact', flush=True)
        best = max(range(6), key=lambda i: max(F(0), F(results[i]['raw_score'][0])))
        assert best == cert['best_index']
        if n == 32:
            maximum = max(F(r['raw_score'][0]) for r in results), max(F(r['raw_score'][1]) for r in results)
            assert F('-0.00566889857') < maximum[0] <= maximum[1] < F('-0.00566889855')
        report['runs'].append({'n': n, 'budget': record(budget),
                               'scaled_exponential': record(scale_exp),
                               'results': results, 'best_index': best})
        save()
    report['status'] = 'PASS_EXISTING_FINITE_CERTIFICATES'
except Exception as exc:
    report['status'] = 'FAIL'
    report['failures'].append(repr(exc))
    save()
    raise
save()
print('Failures: 0. Actual E_16 lower >0.00520444248; all six exact n=32 witness scores <0.')
print('Required unbounded-subsequence rate: UNPROVED; no new numerical candidates.')
print('Full audit certificate:', OUT)
