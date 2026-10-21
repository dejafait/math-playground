"""Exact fixed-mixture checks using L422's audited rational enclosures."""
import json
from fractions import Fraction as F
from pathlib import Path


def main():
    directory = Path(__file__).parent
    source = directory / 'response-modulus-second-moment-certificate.json'
    data = json.loads(source.read_text())
    bounds = data['bounds']

    def interval(record):
        return F(record['lower']), F(record['upper'])

    def divide_positive(a, b):
        assert 0 < b[0] <= b[1]
        return a[0] / b[1], a[1] / b[0]

    def subtract(a, b):
        return a[0] - b[1], a[1] - b[0]

    c = {int(j): interval(v) for j, v in bounds['C'].items()}
    s, t = interval(bounds['S']), interval(bounds['T'])
    b13, b14 = interval(bounds['B13']), interval(bounds['B14'])
    r13, r14 = divide_positive(c[14], c[13]), divide_positive(c[15], c[14])
    denominator = subtract(b14, b13)
    alpha = divide_positive(subtract(b14, t), denominator)
    checks = {
        'source_has_no_failures': data['failures'] == [],
        'all_source_checks_pass': all(data['checks'].values()),
        'C1_below_S': c[1][1] < s[0],
        'S_below_3_over_2': s[1] < F(3, 2),
        'R13_above_3_over_2': r13[0] > F(3, 2),
        'R14_above_3_over_2': r14[0] > F(3, 2),
        'B13_below_T': b13[1] < t[0],
        'T_below_B14': t[1] < b14[0],
        'alpha_above_1_over_3': alpha[0] > F(1, 3),
        'alpha_below_2_over_3': alpha[1] < F(2, 3),
    }
    out = {
        'status': 'EXACT_RATIONAL_SPECIALIZATION_OF_AUDITED_L422',
        'input': str(source.relative_to(directory.parent.parent)),
        'qualification': 'Relies on L422 source bounds; not an independent Euler-tail audit.',
        'bounds': {name: {'lower': str(v[0]), 'upper': str(v[1])}
                   for name, v in [('R13', r13), ('R14', r14), ('alpha', alpha)]},
        'checks': checks,
        'failures': [name for name, passed in checks.items() if not passed],
    }
    path = directory / 'mixed-covariance-weight-certificate.json'
    path.write_text(json.dumps(out, indent=2) + '\n')
    print('Required: C1<S<3/2<R13,R14; B13<T<B14; 1/3<alpha<2/3.')
    for name, value in out['bounds'].items():
        print(name, 'actual rational enclosure:', value)
    print('Checks:', checks, 'Failures:', out['failures'])
    print('Certificate:', path)
    assert not out['failures']


if __name__ == '__main__':
    main()
