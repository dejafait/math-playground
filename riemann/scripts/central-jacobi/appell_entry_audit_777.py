"""Independent finite C040a audit; no imported local arithmetic or evaluator.

Tuple intervals use exact Fraction endpoint extrema and direct endpoint
division, then outward integer rounding to 10^-110. Only P_(2,0) is tested.
The original step775 program/certificate and all inherited files are read-only.
"""
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / 'scripts/central-jacobi/appell-entry-audit-777.json'
UNIT = 10**110
checks = []
failures = []
report = {'scope': 'Independent finite C040a audit under inherited L778 contracts',
          'arithmetic': 'Exact Fraction tuple extrema; direct division; outward 10^-110 grid',
          'checks': checks, 'failures': failures}


def check(label, condition):
    checks.append({'name': label, 'passed': bool(condition)})
    if not condition:
        failures.append(label)


def interval(lo, hi=None):
    lo, hi = Fraction(lo), Fraction(lo if hi is None else hi)
    assert lo <= hi
    return lo, hi


def outward(lo, hi):
    assert lo <= hi
    # // on integers is mathematical floor, including negative inputs.
    low_scaled, high_scaled = lo * UNIT, hi * UNIT
    low = low_scaled.numerator // low_scaled.denominator
    high = -((-high_scaled.numerator) // high_scaled.denominator)
    return Fraction(low, UNIT), Fraction(high, UNIT)


def add(a, b):
    return outward(a[0] + b[0], a[1] + b[1])


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    corners = [x * y for x in a for y in b]
    return outward(min(corners), max(corners))


def scale(n, a):
    return mul(interval(n), a)


def div(a, b):
    assert b[0] > 0 or b[1] < 0, 'division interval meets zero'
    corners = [x / y for x in a for y in b]
    return outward(min(corners), max(corners))


def total(values):
    answer = interval(0)
    for value in values:
        answer = add(answer, value)
    return answer


def pair(a):
    return [str(x) for x in a]


def encloses(label, saved, computed):
    lo, hi = interval(*saved)
    check(label, lo <= computed[0] <= computed[1] <= hi)


def load(path):
    return json.loads((ROOT / path).read_text())


def sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def decimal_bounds(a, places=24):
    unit = 10**places
    low, high = a[0] * unit, a[1] * unit
    integers = [low.numerator // low.denominator,
                -((-high.numerator) // high.denominator)]
    return [('' if n >= 0 else '-') + str(abs(n) // unit) + '.' +
            str(abs(n) % unit).zfill(places) for n in integers]


def audit():
    original_path = 'scripts/central-jacobi/appell-production-entry-775.json'
    source_path = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    prior433_path = 'scripts/actual-fredholm/audit-433/audit-report.json'
    prior478_path = 'scripts/central-jacobi/audit-478/audit-report.json'
    replay_path = 'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json'
    model_path = 'scripts/central-jacobi/fixed-model-certificate-476.json'
    saved = load(original_path)
    paths = set(saved['input_hashes']) | {
        original_path, 'scripts/central-jacobi/fixed_model_476.py',
        'scripts/actual-fredholm/fixed_pair_431.py',
        'scripts/actual-fredholm/check_saved_431.py'}
    before = {p: sha(p) for p in sorted(paths)}
    report['input_hashes'] = before
    report['audit_program_sha256'] = sha('scripts/central-jacobi/appell_entry_audit_777.py')
    for p, expected in saved['input_hashes'].items():
        check('step775 hash unchanged: ' + p, before[p] == expected)
    a433, a478 = load(prior433_path), load(prior478_path)
    model = load(model_path)
    ev = load(source_path)['evaluation']
    check('complete evaluation equals audited step433 replay',
          ev == load(replay_path)['evaluation'])
    check('source hash matches step433', before[source_path] == a433['original_sha256'])
    check('source hash matches L791 source', before[source_path] == model['source_sha256'])
    check('evaluator program matches step433',
          before['scripts/actual-fredholm/fixed_pair_431.py'] == a433['source_sha256'])
    check('saved-data checker matches step433',
          before['scripts/actual-fredholm/check_saved_431.py'] == a433['checker_sha256'])
    for p, expected in a478['original_hashes'].items():
        check('step478 provenance: ' + p, before[p] == expected)
    for label, old in [('433', a433), ('478', a478), ('775', saved)]:
        check('saved audit/certificate ' + label + ' PASS/no failures',
              old['status'] == 'PASS' and old['failures'] == [])
    check('all step478 checks passed', all(x['passed'] for x in a478['checks']))
    check('all step775 checks passed', all(x['passed'] for x in saved['checks']))
    check('complete evaluation comparison recorded in step433',
          'Exact equality of ALL recomputed fields: evaluation' in a433['checks'])
    check('step433 context names and flags', set(a433['context_flags']) == {'DN', 'UP', 'RN'}
          and all(set(x) <= {'Inexact', 'Rounded'} for x in a433['context_flags'].values()))
    check('radius is 1600', ev['uniform_disk_radius'] == 1600)
    check('coefficient indices0-5 present', len(ev['coefficients']) >= 6)
    eg = interval(*ev['uniform_G_error'])
    check('positive error and claimed bound', 0 < eg[0] <= eg[1] < Fraction('3.141e-48'))
    encloses('step775 unchanged error endpoints', saved['uniform_G_error'], eg)
    if failures:
        return

    coefficients = []
    report['coefficient_inputs'] = []
    for j in range(6):
        raw = interval(*ev['coefficients'][j])
        error = eg[1] / 1600**j
        actual = add(raw, interval(-error, error))
        source = saved['coefficient_inputs'][j]
        check('source coefficient index ' + str(j), source['j'] == j and
              source['polynomial_coefficient'] == ev['coefficients'][j])
        check('exact Cauchy error ' + str(j), Fraction(source['Cauchy_error_upper']) == error)
        encloses('saved actual coefficient ' + str(j), source['actual_a'], actual)
        check('actual coefficient positive ' + str(j), actual[0] > 0)
        if j < 5:
            encloses('audited L791 coefficient ' + str(j), model['actual_a'][j], actual)
        coefficients.append(actual)
        report['coefficient_inputs'].append({'j': j, 'raw': pair(raw),
              'Cauchy_error_upper': str(error), 'actual': pair(actual)})

    # L776/L021 theta scaling; exact e0 avoids correlated self-division.
    e = [interval(1)] + [div(scale(4**j, coefficients[j]), coefficients[0])
                         for j in range(1, 6)]
    check('exact e0', e[0] == interval(1) and interval(*saved['e'][0]) == interval(1))
    for j in range(6):
        encloses('saved e_' + str(j), saved['e'][j], e[j])

    sums = [interval(0)]
    for k in range(1, 6):
        terms = [mul(scale((-1)**(j-1), e[j]), sums[k-j])
                 for j in range(1, k)]
        sums.append(add(total(terms), scale((-1)**(k-1) * k, e[k])))
        encloses('saved S_' + str(k), saved['S'][str(k)], sums[k])
    check('a0 denominator positive', coefficients[0][0] > 0)
    check('S2 denominator positive', sums[2][0] > 0)
    if failures:
        return
    m = [interval(1)] + [div(sums[j+2], sums[2]) for j in range(1, 4)]
    for j in range(4):
        encloses('saved m_' + str(j), saved['m'][j], m[j])

    entry = add(sub(m[3], mul(scale(3, m[1]), m[2])),
                mul(mul(scale(2, m[1]), m[1]), m[1]))
    # Independently use the explicit row2 inverse, not step775's inverse loop.
    row = [sub(mul(scale(2, m[1]), m[1]), m[2]), scale(-2, m[1]), interval(1)]
    matrix = total(mul(row[j], m[j+1]) for j in range(3))
    numerator = add(sub(mul(mul(sums[5], sums[2]), sums[2]),
                        mul(mul(scale(3, sums[3]), sums[4]), sums[2])),
                    mul(mul(scale(2, sums[3]), sums[3]), sums[3]))
    denominator = mul(mul(sums[2], sums[2]), sums[2])
    check('numerator quotient denominator positive', denominator[0] > 0)
    quotient = div(numerator, denominator)
    for label, value in [('P20', entry), ('P20_matrix', matrix),
                         ('power_sum_numerator', numerator), ('P20_quotient', quotient)]:
        encloses('original exact enclosure contains independent ' + label, saved[label], value)
        check('strict negative ' + label, value[1] < 0)
        report[label] = pair(value)
    for j in range(3):
        encloses('saved inverse row2 index ' + str(j), saved['inverse_row2'][j], row[j])

    claimed_entry = ['-0.000000004398201602576945', '-0.000000004398201602576944']
    claimed_s2 = ['0.000037172599285269686164', '0.000037172599285269686165']
    encloses('canonical displayed P20 enclosure', claimed_entry, entry)
    encloses('canonical displayed S2 enclosure', claimed_s2, sums[2])
    check('original displayed P20 equals canonical claim',
          saved['summary']['P20_outward_24_places'] == claimed_entry)
    check('original displayed S2 equals canonical claim',
          saved['summary']['S2_outward_24_places'] == claimed_s2)
    report.update(e=[pair(v) for v in e], S={str(k): pair(sums[k]) for k in range(1, 6)},
                  m=[pair(v) for v in m], inverse_row2=[pair(v) for v in row],
                  quotient_denominator=pair(denominator), uniform_G_error=pair(eg))
    report['summary'] = {'P20_outward_24_places': decimal_bounds(entry),
        'S2_outward_24_places': decimal_bounds(sums[2]), 'required_upper': '0',
        'all_three_entry_upper_endpoints_negative': all(x[1] < 0 for x in [entry, matrix, quotient]),
        'all_original_exact_enclosures_contain_independent_images': not failures,
        'qualification': 'Only this Appell production-TP construction; L778 contracts retained; RH open'}
    for p, expected in before.items():
        check('original preserved: ' + p, sha(p) == expected)


if __name__ == '__main__':
    try:
        audit()
    except Exception as exc:
        failures.append(type(exc).__name__ + ': ' + str(exc))
    report['status'] = 'FAIL' if failures else 'PASS'
    OUTPUT.write_text(json.dumps(report, indent=2) + '\n')
    print('status:', report['status'], 'checks:', len(checks), 'failures:', failures)
    print('actual/required:', report.get('summary', {}))
    print('full certificate:', OUTPUT.relative_to(ROOT))
    raise SystemExit(bool(failures))
