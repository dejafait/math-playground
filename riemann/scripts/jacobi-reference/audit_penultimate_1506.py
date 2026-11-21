"""Independent exact-rational enclosure audit of the complete 1504 certificate.

No original arithmetic implementation is imported. All saved determinant
states are checked by the last-column recurrence, with no rounding. The
input Decimal evaluator remains subject to L778's previously stated contracts.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
import platform

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'scripts/jacobi-reference/audit-penultimate-1506.json'
CERT = ROOT / 'scripts/jacobi-reference/penultimate-cost-1504.json'


def point(x):
    return (Q(x), Q(x))


def pair(xs):
    a, b = map(Q, xs)
    assert a <= b
    return a, b


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    vals = [x*y for x in a for y in b]
    return min(vals), max(vals)


def scale(a, q):
    return mul(a, point(q))


def div(a, b):
    assert b[0] > 0 or b[1] < 0
    return mul(a, (1/b[1], 1/b[0]))


def power(a, n):
    out = point(1)
    for _ in range(n):
        out = mul(out, a)
    return out


def isum(xs):
    out = point(0)
    for x in xs:
        out = add(out, x)
    return out


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def serialized(a):
    return [str(x) for x in a]


def main():
    report = dict(step=1506, status='INCOMPLETE', failures=[], checks=[],
                  enclosure_checks=[], determinant_states_checked=0,
                  arithmetic='Unrounded exact Fraction endpoint arithmetic',
                  python=platform.python_version(), program_sha256=sha(Path(__file__)),
                  scope='Complete certificate1504; no new transcendental evaluator or backend attestation')
    inputs = [CERT, ROOT / 'scripts/jacobi-reference/penultimate_cost_1504.py']

    def check(name, condition):
        report['checks'].append(dict(name=name, passed=bool(condition)))
        if not condition:
            raise AssertionError(name)

    def enclosed(name, saved, expected):
        actual = pair(saved)
        ok = actual[0] <= expected[0] <= expected[1] <= actual[1]
        report['enclosure_checks'].append(dict(
            field=name, saved=saved, required=serialized(expected), passed=ok))
        check('enclosure: ' + name, ok)
        return actual

    try:
        cert = json.loads(CERT.read_text())
        inputs += [ROOT / p for p in cert['input_hashes']]
        hashes = {str(p.relative_to(ROOT)): sha(p) for p in inputs}
        report['input_hashes'] = hashes
        check('certificate status', cert['status'] == 'MATCHING_FEASIBLE_AND_RETAINED_COST_OBSTRUCTED')
        check('all 21 recorded checks passed', len(cert['checks']) == 21 and all(c['passed'] is True for c in cert['checks']))
        check('no recorded failure', cert['failures'] == [])
        check('original program hash', sha(inputs[1]) == cert['program_sha256'])
        for p, expected in cert['input_hashes'].items():
            check('input hash: ' + p, hashes[p] == expected)
        src = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
        prior = json.loads((ROOT / 'scripts/actual-fredholm/audit-433/audit-report.json').read_text())
        replay = json.loads((ROOT / 'scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json').read_text())
        ev = json.loads(src.read_text())['evaluation']
        check('L778 recorded source hash', sha(src) == prior['original_sha256'])
        check('L778 prior audit PASS', prior['status'] == 'PASS' and prior['failures'] == [])
        check('entire evaluation equals prior replay', ev == replay['evaluation'])
        check('disk radius', ev['uniform_disk_radius'] == 1600)
        check('full analytic error copied', ev['uniform_G_error'] == cert['uniform_G_error'])
        error = pair(ev['uniform_G_error'])
        check('full analytic error threshold', 0 < error[0] <= error[1] < Q('3.141e-48'))
        check('all six P0 coefficients copied', len(cert['source_P0_coefficients']) == 6 and cert['source_P0_coefficients'] == ev['coefficients'][:6])
        lengths = {'cauchy_error_bounds': 6, 'actual_G_coefficients': 6,
                   'F_ordinary_coefficients': 6, 'actual_b': 6,
                   'logarithm_coefficients': 5, 'E_descending': 7,
                   'J_descending': 4, 'sylvester_matrix': 9}
        for name, n in lengths.items():
            check('length: ' + name, len(cert[name]) == n)
        aa = []
        for j in range(6):
            eps = error[1] / 1600**j
            enclosed(f'cauchy_error_bounds/{j}', cert['cauchy_error_bounds'][j], (Q(0), eps))
            aa.append(enclosed(f'actual_G_coefficients/{j}', cert['actual_G_coefficients'][j],
                               add(pair(ev['coefficients'][j]), (-eps, eps))))
            check('positive actual A_' + str(j), aa[j][0] > 0)
        ff = [enclosed('F_ordinary_coefficients/0', cert['F_ordinary_coefficients'][0], point(1))]
        for j in range(1, 6):
            ff.append(enclosed(f'F_ordinary_coefficients/{j}', cert['F_ordinary_coefficients'][j],
                               scale(div(aa[j], aa[0]), 4**j)))
        for j in range(6):
            enclosed(f'actual_b/{j}', cert['actual_b'][j], scale(ff[j], math.factorial(j)))
        logs = [point(0)]
        sums = {}
        check('reciprocal-sum indices', set(cert['reciprocal_sums']) == {str(n) for n in range(1, 6)})
        for n in range(1, 6):
            expected = sub(ff[n], scale(isum(scale(mul(logs[k], ff[n-k]), k)
                                             for k in range(1, n)), Q(1, n)))
            logs.append(enclosed(f'logarithm_coefficients/{n-1}', cert['logarithm_coefficients'][n-1], expected))
            sums[n] = enclosed(f'reciprocal_sums/{n}', cert['reciprocal_sums'][str(n)],
                               scale(logs[n], (-1)**(n+1)*n))
        v, t, q, h = [sums[n] for n in range(2, 6)]
        for n in range(2, 6):
            check('positive S_' + str(n), sums[n][0] > 0)
        feas = enclosed('feasibility_margin', cert['feasibility_margin'],
                        sub(power(scale(v, Q(9, 10)), 3), power(t, 2)))
        check('feasibility strictly positive', feas[0] > 0)
        check('scale exactly 1/200', Q(cert['scale']) == Q(1, 200))
        T, Qn, H = [enclosed('normalized_sums/' + name, cert['normalized_sums'][name],
                              scale(value, 200**n))
                    for name, value, n in [('T', t, 3), ('Q', q, 4), ('H', h, 5)]]
        expected_E = [point(1), point(0), point(0), scale(T, -8), scale(Qn, 9), point(0), scale(power(T, 2), -2)]
        expected_J = [T, scale(Qn, -3), scale(H, 3), neg(power(T, 2))]
        E = [enclosed(f'E_descending/{j}', a, b) for j, (a, b) in enumerate(zip(cert['E_descending'], expected_E))]
        J = [enclosed(f'J_descending/{j}', a, b) for j, (a, b) in enumerate(zip(cert['J_descending'], expected_J))]
        matrix = []
        for i, row in enumerate(cert['sylvester_matrix']):
            check('matrix row width ' + str(i), len(row) == 9)
            poly, shift = (E, i) if i < 3 else (J, i-3)
            expected_row = [point(0)]*shift + poly + [point(0)]*(9-shift-len(poly))
            matrix.append([enclosed(f'sylvester_matrix/{i}/{j}', a, b)
                           for j, (a, b) in enumerate(zip(row, expected_row))])
        states = cert['determinant_states']
        check('exactly every mask 0 through 511', set(states) == {str(i) for i in range(512)})
        verified = {0: enclosed('determinant_states/0', states['0'], point(1))}
        for mask in range(1, 512):
            row = mask.bit_count()-1
            contributions = []
            for col in range(9):
                if mask & (1 << col):
                    previous = mask ^ (1 << col)
                    sign = (-1)**sum(bool(previous & (1 << k)) for k in range(col+1, 9))
                    contributions.append(scale(mul(verified[previous], matrix[row][col]), sign))
            verified[mask] = enclosed('determinant_states/' + str(mask), states[str(mask)], isum(contributions))
        report['determinant_states_checked'] = len(verified)
        det = enclosed('determinant', cert['determinant'], verified[511])
        check('determinant strictly negative', det[1] < 0)
        coarse = {'S_2': (v, '3.7172599285269686e-5', '3.7172599285269687e-5'),
                  'S_3': (t, '1.4417393140097327e-7', '1.4417393140097329e-7'),
                  'S_4': (q, '6.6303168025299086e-10', '6.6303168025299088e-10'),
                  'S_5': (h, '3.2136641506166011e-12', '3.2136641506166013e-12'),
                  'feasibility': (feas, '1.6659e-14', '1.6660e-14'),
                  'determinant': (det, '-21.518952570', '-21.518952569')}
        report['actual_and_required_bounds'] = {}
        for label, (bounds, lo, hi) in coarse.items():
            check('strict published enclosure: ' + label, Q(lo) < bounds[0] <= bounds[1] < Q(hi))
            report['actual_and_required_bounds'][label] = dict(actual=serialized(bounds), required_open=[lo, hi])
        for path in inputs:
            check('input unchanged: ' + str(path.relative_to(ROOT)), sha(path) == hashes[str(path.relative_to(ROOT))])
        report['status'] = 'PASS'
    except Exception as exc:
        report['status'] = 'FAIL'
        report['failures'].append(type(exc).__name__ + ': ' + str(exc))
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    print('Result:', report['status'])
    print('Exact enclosure checks:', len(report['enclosure_checks']))
    print('Determinant states checked / required:', report['determinant_states_checked'], '/ 512')
    print('Actual strict bounds: feasibility in (1.6659e-14,1.6660e-14); determinant in (-21.518952570,-21.518952569)' if report['status'] == 'PASS' else 'Bounds not certified')
    print('Required: feasibility > 0 and determinant != 0; asymptotic argument requires separate conceptual review')
    print('Failures:', report['failures'])
    print('Full evidence:', OUT.relative_to(ROOT))
    return 0 if report['status'] == 'PASS' else 1


if __name__ == '__main__':
    raise SystemExit(main())
