"""Independent exact audit of every step-165 certificate factor and bound."""
import json
from fractions import Fraction as Q
from math import comb, isqrt
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'response-modulus-second-moment-certificate.json'
OUTPUT = HERE / 'response-modulus-second-moment-audit-certificate.json'
D = 10**18
failures = []
roundings = 0


def check(name, condition):
    if not condition:
        failures.append(name)


def rounded(lo, hi):
    global roundings
    lower = Q((lo * D).__floor__(), D)
    upper = Q((hi * D).__ceil__(), D)
    check('outward rounding', lower <= lo <= hi <= upper)
    roundings += 1
    return lower, upper


def add(a, b):
    return rounded(a[0] + b[0], a[1] + b[1])


def subtract(a, b):
    return rounded(a[0] - b[1], a[1] - b[0])


def multiply(a, b):
    products = [x * y for x in a for y in b]
    return rounded(min(products), max(products))


division_records = []


def divide(a, b):
    check('positive divisor', b[0] > 0)
    division_records.append([str(x) for x in b])
    return multiply(a, (1 / b[1], 1 / b[0]))


def saved_interval(record):
    return Q(record['lower']), Q(record['upper'])


def encode(interval):
    return {'lower': str(interval[0]), 'upper': str(interval[1])}


def main():
    source = json.loads(SOURCE.read_text())
    check('cutoff', source['prime_cutoff'] == 200)
    check('order', source['local_order'] == 40)
    check('denominator', source['denominator'] == D)
    # Trial division is independent of the generator's sieve.
    primes = [n for n in range(2, 201)
              if all(n % d for d in range(2, isqrt(n) + 1))]
    check('complete ordered prime list', source['primes'] == primes)
    check('exact local j keys', set(source['C_local_factors']) ==
          {'1', '2', '13', '14', '15', '16'})
    moments, local_records, tails = {}, [], {}
    for j in (1, 2, 13, 14, 15, 16):
        records = source['C_local_factors'][str(j)]
        check(f'C{j} prime ordering', [r['p'] for r in records] == primes)
        product = (Q(1), Q(1))
        for p, record in zip(primes, records):
            # Direct binomial coefficients, not the generator's recurrence.
            terms = [Q(comb(j + e - 1, e)**2, p**(5 * e))
                     for e in range(41)]
            finite = sum(terms, Q(0))
            first_omitted = Q(comb(j + 40, 41)**2, p**205)
            ratio = Q((j + 40)**2, 41**2 * p**5)
            check(f'local ratio {j},{p}', 0 < ratio < 1)
            tail = first_omitted / (1 - ratio)
            interval = rounded(finite, finite + tail)
            check(f'local factor {j},{p}', saved_interval(record['factor']) == interval)
            local_records.append({'j': j, 'p': p, 'finite_sum': str(finite),
                                  'tail_upper': str(tail), 'interval': encode(interval),
                                  'saved_matches': saved_interval(record['factor']) == interval})
            product = multiply(product, interval)
        tail_log = Q(j*j, 4 * 200**4) / (1 - Q(j*j, 201**5))
        tails[f'C{j}'] = tail_log
        moments[j] = multiply(product, (Q(1), 1 / (1 - tail_log)))

    zetas = {}
    for s in (3, 5, 6):
        product = (Q(1), Q(1))
        for p in primes:
            factor = Q(p**s, p**s - 1)
            product = multiply(product, (factor, factor))
        tail_log = Q(1, (s - 1) * 200**(s - 1)) / (1 - Q(1, 201**s))
        tails[f'zeta{s}'] = tail_log
        zetas[s] = multiply(product, (Q(1), 1 / (1 - tail_log)))
    s_value = divide(multiply(zetas[5], multiply(zetas[3], zetas[3])), zetas[6])
    t_value = (Q(1), Q(1))
    t_records = []
    for p in primes:
        u, v = Q(1, p**3), Q(1, p**5)
        # Common-minimum/excess decomposition, distinct from rational numerator form.
        factor = (1 + v) / (1 - v)**3 * (1 + u) / (1 - u)
        factor += 2 * u / ((1 - u)**2 * (1 - v)**2)
        check(f'T majorant {p}', 1 <= factor <= (1-u)**(-4) * (1-v)**(-4))
        t_records.append({'p': p, 'factor': str(factor)})
        t_value = multiply(t_value, (factor, factor))
    tails['T'] = Q(2, 200**2) / (1-Q(1, 201**3)) + Q(1, 200**4) / (1-Q(1, 201**5))
    t_value = multiply(t_value, (Q(1), 1 / (1 - tails['T'])))
    check('tail key coverage', set(tails) == set(source['log_tail_upper_bounds']))
    for name, value in tails.items():
        check(f'tail {name}', 0 < value < 1 and
              Q(source['log_tail_upper_bounds'][name]) == value)
    b_values = {}
    for k in (13, 14):
        ratio = divide(moments[k+1], moments[k])
        theta = divide(subtract(s_value, moments[1]), subtract(ratio, moments[1]))
        b_values[k] = add(moments[2], multiply(theta,
                         subtract(divide(moments[k+2], moments[k]), moments[2])))
    expected = {'S': s_value, 'T': t_value, 'B13': b_values[13], 'B14': b_values[14]}
    for name, interval in expected.items():
        check(f'global bound {name}', saved_interval(source['bounds'][name]) == interval)
    check('moment bound keys', set(source['bounds']['C']) == {str(j) for j in moments})
    for j, interval in moments.items():
        check(f'global C{j}', saved_interval(source['bounds']['C'][str(j)]) == interval)
    checks = {
        'B13_below_2236_over_1000': b_values[13][1] < Q(2236, 1000),
        'T_above_2237_over_1000': t_value[0] > Q(2237, 1000),
        'T_below_4475_over_2000': t_value[1] < Q(4475, 2000),
        'B14_above_4477_over_2000': b_values[14][0] > Q(4477, 2000),
        'S_above_C1': s_value[0] > moments[1][1],
        'C2_above_C1_squared': moments[2][0] > moments[1][1]**2,
    }
    check('all saved checks recomputed', source['checks'] == checks and all(checks.values()))
    check('saved failures empty', source['failures'] == [])
    gaps = {'T_minus_B13': t_value[0] - b_values[13][1],
            'B14_minus_T': b_values[14][0] - t_value[1]}
    for name, gap in gaps.items():
        check(name, gap > Q(1, 1000))
    out = {'status': 'PASS' if not failures else 'FAIL', 'source': SOURCE.name,
           'prime_count': len(primes), 'primes': primes, 'local_factor_count': len(local_records),
           'local_factor_checks': local_records, 'T_local_factors': t_records,
           'rounding_checks': roundings, 'division_denominators': division_records,
           'tail_log_bounds': {k: str(v) for k, v in tails.items()},
           'bounds': {k: encode(v) for k, v in expected.items()},
           'moment_bounds': {j: encode(v) for j, v in moments.items()},
           'checks': checks, 'gap_lower_bounds': {k: str(v) for k, v in gaps.items()},
           'required_gap': '1/1000', 'failures': failures}
    OUTPUT.write_text(json.dumps(out, indent=2) + '\n')
    print(f"{out['status']}: {len(primes)} primes, {len(local_records)} local C factors, "
          f"{len(t_records)} T factors, {len(tails)} full tails, {roundings} outward roundings")
    print('Gap lower bounds:', out['gap_lower_bounds'], 'required: > 1/1000')
    print('Failures:', failures)
    print('Full audit certificate:', OUTPUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
