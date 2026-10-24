"""Independent isolated step-453 n=28 replay; imports no producer code or arithmetic."""
import hashlib
import json
from fractions import Fraction

SCALE = 2**256
LEDGER = {}


def tally(key, size=1):
    LEDGER[key] = LEDGER.get(key, 0)+size


def stamp(obj):
    return hashlib.sha256(json.dumps(obj, separators=(',', ':')).encode()).hexdigest()


def encode(r):
    return [r.numerator, r.denominator]


def floor_checked(num, den):
    assert den > 0
    q, r = divmod(abs(num), den)
    ans = q if num >= 0 else -q-(r != 0)
    assert ans*den <= num < (ans+1)*den
    return ans


def ceil_checked(num, den):
    assert den > 0
    q, r = divmod(abs(num), den)
    ans = q+(r != 0) if num >= 0 else -q
    assert (ans-1)*den < num <= ans*den
    return ans


def enclose(num, den=1):
    tally('convert')
    return (floor_checked(num*SCALE, den), ceil_checked(num*SCALE, den))


def plus(a, b):
    tally('add')
    return (a[0]+b[0], a[1]+b[1])


def opposite(a):
    tally('negate')
    return (-a[1], -a[0])


def times(a, b):
    tally('multiply')
    # Determine endpoint extrema by signs, independently of the producer's
    # four-product min/max loop. Signed rounding checks every result.
    al, au = a
    bl, bu = b
    assert al <= au and bl <= bu
    if al >= 0:
        low, high = ((al*bl, au*bu) if bl >= 0 else
                     (au*bl, al*bu) if bu <= 0 else (au*bl, au*bu))
    elif au <= 0:
        low, high = ((al*bu, au*bl) if bl >= 0 else
                     (au*bu, al*bl) if bu <= 0 else (al*bu, al*bl))
    elif bl >= 0:
        low, high = al*bu, au*bu
    elif bu <= 0:
        low, high = au*bl, al*bl
    else:
        low, high = min(al*bu, au*bl), max(al*bl, au*bu)
    return (floor_checked(low, SCALE), ceil_checked(high, SCALE))


def over(a, divisor):
    tally('divide')
    return (floor_checked(a[0], divisor), ceil_checked(a[1], divisor))


def intersect(a, low, high):
    tally('clip')
    left = low if a[0] < low else a[0]
    right = high if a[1] > high else a[1]
    assert left <= right
    return (left, right)


def log_series(numerator, denominator):
    zed = intersect(enclose(numerator, denominator), 0, SCALE//2)
    square = intersect(times(zed, zed), 0, SCALE//4)
    power = zed
    acc = (0, 0)
    rows = []
    for degree in range(1, 256, 2):
        t = over(power, degree)
        acc = plus(acc, t)
        rows.append([power, t, acc])
        if degree < 255:
            power = times(square, power)
    result = (acc[0]*2-1, acc[1]*2+1)
    tally('scale')
    tally('enlarge')
    return result, stamp([zed, square, rows, result])


def exp_series(num, den):
    argument = intersect(enclose(num, den), 0, SCALE//8)
    current = (SCALE, SCALE)
    acc = current
    rows = [[current, acc]]
    degree = 1
    while degree <= 127:
        current = over(times(current, opposite(argument)), degree)
        acc = plus(current, acc)
        rows.append([current, acc])
        degree += 1
    expanded = intersect((acc[0]-1, acc[1]+1), 0, SCALE)
    tally('enlarge')
    result = expanded
    powers = []
    for level in range(16):
        result = intersect(times(result, result), 0, SCALE)
        powers.append(result)
    return result, stamp([argument, rows, expanded, powers])


def product(first, second):
    # Reverse both coefficient traversals and switch the outer factor.
    low = [0]*(len(first)+len(second)-1)
    high = low.copy()
    for j in range(len(second)-1, -1, -1):
        for i in range(len(first)-1, -1, -1):
            l, u = times(second[j], first[i])
            low[i+j] += l
            high[i+j] += u
            tally('add')
            tally('coefficient_pairs')
    return list(zip(low, high))


def verify_parameter(record):
    rational_bounds = []
    for m, saved in zip((5, 239), record['arctangents'], strict=True):
        assert saved['m'] == m and len(saved['terms']) == 25
        partial = Fraction(0)
        terms = []
        for j in range(25):
            term = Fraction(1 if j % 2 == 0 else -1, m**(2*j+1)*(2*j+1))
            terms.append(encode(term))
            if j < 24:
                partial += term
        assert terms == saved['terms']
        bounds = [partial, partial+term]
        assert bounds[0] < bounds[1]
        assert list(map(encode, bounds)) == saved['bounds']
        rational_bounds.append(bounds)
    exact_pi = [16*rational_bounds[0][0]-4*rational_bounds[1][1],
                16*rational_bounds[0][1]-4*rational_bounds[1][0]]
    assert list(map(encode, exact_pi)) == record['pi_exact']
    pi = [enclose(exact_pi[0].numerator, exact_pi[0].denominator)[0],
          enclose(exact_pi[1].numerator, exact_pi[1].denominator)[1]]
    assert pi == record['pi_grid']
    # Independent binary search for the integer square-root witness.
    target = 389*SCALE*SCALE
    lo, hi = 19*SCALE, 20*SCALE
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid*mid <= target:
            lo = mid
        else:
            hi = mid
    assert lo*lo < target < hi*hi and hi == lo+1
    assert [lo, hi] == record['sqrt_grid']
    assert record['sqrt_target'] == target
    assert record['sqrt_squares'] == [lo*lo, hi*hi]
    c = [floor_checked(2*pi[0]*SCALE, hi), ceil_checked(2*pi[1]*SCALE, lo)]
    assert c == record['c_grid']
    midpoint = Fraction(c[0]+c[1], 2*SCALE)
    delta = Fraction(c[1]-c[0], 2*SCALE)
    assert record['midpoint'] == encode(midpoint) and record['delta'] == encode(delta)
    assert Fraction(3, 10) <= Fraction(c[0], SCALE) <= Fraction(c[1], SCALE) <= Fraction(1, 2)
    assert delta <= Fraction(1, 2**50)
    return midpoint.numerator, midpoint.denominator


def run(parameter, records, final, progress):
    num, den = verify_parameter(parameter)
    log_two, hash_two = log_series(1, 3)
    running = (0, 0)
    count_panels = 0
    for index, saved in enumerate(records):
        assert index < 1016
        count_panels += 1
        endpoint = index+8
        exponent = next(k for k in range(7) if 8*2**k <= endpoint < 16*2**k)
        lb, hb = log_series(endpoint-8*2**exponent, endpoint+8*2**exponent)
        la = intersect((lb[0]+exponent*log_two[0], lb[1]+exponent*log_two[1]), 0, 7*SCALE)
        tally('scale')
        tally('add')
        assert 0 < num*endpoint*28 < den*65536
        scalar, hs = exp_series(num*endpoint*28, den*524288)
        assert 0 < num*28 <= den*64
        beta = intersect(enclose(num*28, den*8), 0, SCALE*8)
        rho = intersect(enclose(1, endpoint), 0, SCALE//8)
        reciprocal = [intersect(enclose(8, endpoint), 0, SCALE)]
        e = [(SCALE, SCALE)]
        for degree in range(128):
            e.append(over(times(e[degree], opposite(beta)), degree+1))
        for degree in range(64):
            reciprocal.append(times(reciprocal[degree], opposite(rho)))
        h = [la]
        power = (SCALE, SCALE)
        for degree in range(1, 65):
            power = times(rho, power)
            coefficient = over(power, degree)
            h.append(opposite(coefficient) if degree % 2 == 0 else coefficient)
        first = product(e, reciprocal)
        full = product(first, h)
        assert [len(e), len(reciprocal), len(h), len(first), len(full)] == [129, 65, 65, 193, 257]
        divisions = [over(full[j], j+1) for j in range(257)]
        integral = (0, 0)
        for term in reversed(divisions):
            integral = plus(integral, term)
        contribution = over(times(integral, scalar), 8)
        running = plus(contribution, running)
        reconstructed = {'n': 28, 'index': index, 'endpoints': [[endpoint, 8], [endpoint+1, 8]],
                         'k': exponent, 'log': la, 'exp': scalar,
                         'integrated_polynomial': integral, 'panel_integral': contribution,
                         'running_sum': running,
                         'digests': {'log2': hash_two, 'logb': hb, 'exp': hs,
                                     'E': stamp(e), 'R': stamp(reciprocal), 'H': stamp(h),
                                     'Q': stamp(first), 'P': stamp(full), 'integration': stamp(divisions)}}
        assert json.loads(json.dumps(reconstructed)) == saved, ('panel_mismatch', index)
        if index % 64 == 0:
            progress('replay', count_panels)
    assert count_panels == 1016
    ends = [running[0]-2**72, running[1]+2**72]
    tally('enlarge')
    rad = Fraction(ends[1]-ends[0], 2*SCALE)
    assert ends[0] <= ends[1] and rad < Fraction(1, 2**50) and rad < Fraction(1, 2**183)
    expected = {'grid_denominator': SCALE, 'polynomial_sum': running, 'final_grid': ends,
                'midpoint': encode(Fraction(ends[0]+ends[1], 2*SCALE)), 'radius': encode(rad),
                'required_radius': [1, 2**50], 'stronger_radius': [1, 2**183],
                'complete_panels': 1016, 'n': 28}
    for key, value in expected.items():
        assert json.loads(json.dumps(value)) == final[key], ('final_mismatch', key)
    assert LEDGER['coefficient_pairs'] == 1016*20930
    # Both ledgers include the two parameter conversions and the complete run.
    expected_counts = dict(final['counts'])
    assert expected_counts == LEDGER, ('operation_counts', expected_counts, LEDGER)
    return {'status': 'PASS', 'parameter': 'complete exact reconstruction',
            'panels': count_panels, 'coefficient_pairs': LEDGER['coefficient_pairs'],
            'counts': LEDGER, 'radius': encode(rad), 'all_stage_comparisons': 'PASS',
            'signed_rounding_checks': 'every conversion, multiplication and division',
            'originals_preserved': 'checked by aggregate runner'}
