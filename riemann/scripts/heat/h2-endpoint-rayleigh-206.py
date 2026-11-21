"""One fixed Rayleigh test; exact saved intervals and complete directional tail.

Run from the active notebook. No quadrature, optimization or zero census.
Analytic inclusion is conditional on the canonical L917/L919 inputs.
"""
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'low-time-h2-uniform-195.json'
OUT = HERE / 'h2-endpoint-rayleigh-206.json'


def interval(record):
    return Q(record['lower']), Q(record['upper'])


def scale(a, w):
    values = (w * a[0], w * a[1])
    return min(values), max(values)


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def saved(a):
    return {'lower': str(a[0]), 'upper': str(a[1])}


def outward(a, digits=12):
    base = 10 ** digits
    lo = (a[0] * base).__floor__()
    hi = (a[1] * base).__ceil__()
    def decimal(n):
        return ('-' if n < 0 else '') + str(abs(n) // base) + '.' + str(abs(n) % base).zfill(digits)
    return {'lower': decimal(lo), 'upper': decimal(hi)}


def main():
    raw = SOURCE.read_bytes()
    source = json.loads(raw)
    panel = source['panels'][0]
    c, diagonal = (1, -2, 1), (1, 200, 40000)
    d = tuple(x * y for x, y in zip(c, diagonal))
    norm2 = sum(x * x for x in c)
    weights = {k: sum(d[i] * d[j] for i in range(3) for j in range(3) if i+j+2 == k)
               for k in range(2, 7)}
    expected = {2: 1, 3: -800, 4: 240000, 5: -32000000, 6: 1600000000}
    checks = []
    def check(name, passed):
        checks.append({'name': name, 'passed': bool(passed)})
    check('fixed scaling and norm', d == (1, -400, 40000) and norm2 == 6)
    check('five algebraic contraction weights', weights == expected)
    check('closed panel contains zero', interval(panel['lambda']) == (Q(0), Q(1, 5120)))
    check('positive saved mass', interval(panel['moments']['0'])[0] > 0)
    for name, rounding in [('DOWN', 'ROUND_FLOOR'), ('UP', 'ROUND_CEILING'), ('NEAR', 'ROUND_HALF_EVEN')]:
        context = source['arithmetic'][name]
        check(name + ' inherited contract', context['precision'] == 100 and context['rounding'] == rounding
              and all(context['traps'][key] for key in ('DivisionByZero','InvalidOperation','Overflow','Underflow','Subnormal'))
              and not any(context['exceptional_flags'].values()))

    terms = []
    numerator = (Q(0), Q(0))
    for k, w in weights.items():
        value = interval(panel['S'][str(k)])
        check('ordered S' + str(k), value[0] <= value[1])
        term = scale(value, w)
        numerator = add(numerator, term)
        terms.append({'index': k, 'weight': w, 'input': panel['S'][str(k)], 'contribution': saved(term)})
    matrix_replay = (Q(0), Q(0))
    for i in range(3):
        for j in range(3):
            matrix_replay = add(matrix_replay, scale(interval(panel['S'][str(i+j+2)]), d[i]*d[j]))
    # For each anti-diagonal these weights have the same sign, hence equality.
    check('independent nine-entry contraction equals five-term contraction', matrix_replay == numerator)
    full = scale(numerator, Q(1, norm2))

    tails = []
    tail_numerator = Q(0)
    for k, w in weights.items():
        p = 2 * k
        jp = Q(4*p, 5*(p-1)) * Q(100) ** (1-p) * (5 + Q(1, p-1))
        term = abs(w) * jp
        tail_numerator += term
        tails.append({'p': p, 'absolute_weight': abs(w), 'power_sum_bound': str(jp), 'weighted_bound': str(term)})
        check('positive integrated bound p=' + str(p), jp > 0)
    tail = tail_numerator / norm2
    head = full[0] - tail, full[1] + tail
    threshold = Q(5691, 10**9)
    decisive = head[1] <= threshold
    straddles = head[0] <= threshold < head[1]
    check('exact directional constant', tail == Q(178794260431, 175872436523437500))
    check('reported full enclosure', Q('-0.000044222946') <= full[0] <= full[1] <= Q('0.000045398584'))
    check('reported directional bound', tail < Q('0.000001016614'))
    check('reported head enclosure', Q('-0.000045239559') <= head[0] <= head[1] <= Q('0.000046415197'))
    check('threshold comparison is inconclusive', not decisive and straddles)
    failures = [r['name'] for r in checks if not r['passed']]
    certificate = {
        'step': 206,
        'source': {'path': str(SOURCE.relative_to(HERE.parent.parent)), 'sha256': hashlib.sha256(raw).hexdigest(), 'panel': 0},
        'fixed': {'lambda': '0', 'R': 100, 'D': list(diagonal), 'c': list(c), 'Dc': list(d), 'norm_squared': norm2},
        'coefficient_contraction': terms,
        'full_numerator': saved(numerator), 'full_quotient': saved(full),
        'directional_tail': {'powers': tails, 'numerator_bound': str(tail_numerator), 'quotient_bound': str(tail)},
        'head_quotient': saved(head),
        'comparison': {'required_upper_at_most': str(threshold), 'upper_minus_threshold': str(head[1]-threshold),
                       'decisive_obstruction': decisive, 'interval_straddles_threshold': straddles,
                       'decision': 'obstruction_to_strict_head_margin' if decisive else 'inconclusive_stop_without_refinement'},
        'checks': checks, 'failures': failures,
        'summary': {'check_count': len(checks), 'failure_count': len(failures), 'full_quotient_outward': outward(full),
                    'directional_tail_outward': outward((Q(0), tail)), 'head_quotient_outward': outward(head),
                    'required_threshold': '0.000005691', 'decision': 'decisive' if decisive else 'inconclusive'},
        'qualifications': ['L917 enclosure and Decimal-library assumptions inherited',
                           'exact Fraction arithmetic in this calculation',
                           'complete complex-zero tail with multiplicities and boundary zeros retained in head',
                           'no claim of head feasibility, H2 sign or RH']}
    OUT.write_text(json.dumps(certificate, indent=2) + '\n')
    print(json.dumps(certificate['summary'], indent=2))
    print('Certificate:', OUT.relative_to(HERE.parent.parent))
    print('Failures:', failures)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
