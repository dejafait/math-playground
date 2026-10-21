"""Check L054's manuscript and its nonconstant witness by point counting."""
import hashlib
import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).parent


def enc(x):
    return [x.numerator, x.denominator]


def main():
    source = ROOT / 'conditioned-five-shell-audit-results.json'
    raw = source.read_bytes()
    report = json.loads(raw)
    original = json.loads((ROOT / 'conditioned-five-shell-results.json').read_text())
    checks, failures = [], []

    def check(name, truth):
        checks.append({'name': name, 'passed': bool(truth)})
        if not truth:
            failures.append(name)

    check('complete reconstruction passes', report['checks'] == 328
          and report['failures'] == [] and report['verified'])
    check('reconstruction binds constructor', report['source_sha256'] == hashlib.sha256(
        (ROOT / 'conditioned-five-shell-results.json').read_bytes()).hexdigest())
    p = [Q(*z) for z in original['parameters']['p']]
    alpha = p[5]**2/p[68]
    rho = Q(*report['normalization']['rho'])
    check('positive normalization', rho > 0 and p[5] > 0 and p[68] > 0
          and alpha == Q(*report['normalization']['alpha']))
    expected_mult = [[1, 67, 2210, 47838, 764269, 9609743],
                     [1, 955, 455534, 144707330, 34440116295, 6550452053781]]
    check('manuscript factor multiplicities', [z['multiplicities'] for z in original['factors']]
          == expected_mult)
    size = comb(68, 5)*comb(956, 5)
    check('manuscript dimension', size == 68643272053310642688
          == sum(z['multiplicity'] for z in report['modes']))
    signs = []
    for a in range(6):
        row = []
        for b in range(6):
            z = report['modes'][6*a+b]
            value = Q(*z['schur_scaled'])
            expected_sign = -1 if a <= 3 and b <= 2 else 1
            check(f'manuscript mode {a},{b}', z['a'] == a and z['b'] == b
                  and value*expected_sign > 0
                  and z['multiplicity'] == expected_mult[0][a]*expected_mult[1][b])
            row.append(expected_sign)
        signs.append(row)

    # For f_z(Y)=1_{z in Y}-5/956, count the two possible point cases.
    tail_eigen, point_cases = [], []
    for q in range(6):
        valency = comb(5, q)*comb(951, q)
        present = Q(valency)*(Q(5-q, 5)-Q(5, 956))/Q(951, 956)
        absent = Q(valency)*(Q(q, 951)-Q(5, 956))/Q(-5, 956)
        check(f'point cases {q}', present == absent
              == original['factors'][1]['eigenmatrix'][1][q])
        tail_eigen.append(present)
        point_cases.append({'q': q, 'present': enc(present), 'absent': enc(absent)})
    check('point vector sum zero', comb(955, 4)*956 == 5*comb(956, 5))
    terms = []
    for r in range(6):
        for q in range(6):
            entry = p[5] if r+q == 0 else Q(0) if r+q < 5 or (r, q) == (2, 3) else alpha*p[r+q]
            term = entry*comb(5, r)*comb(63, r)*tail_eigen[q]
            terms.append({'r': r, 'q': q, 'entry_over_rho': enc(entry),
                          'contribution_over_rho': enc(term)})
    witness = sum((Q(*z['contribution_over_rho']) for z in terms), Q(0))/alpha
    manuscript = Q(-9407447982070183554138710330070988958007422947593808542631328728863935482584761986056607300265166515267887,
                   58777218163070353667139034661145066715999641701236218891492604409567076435028516765657297701931037908560)
    z = report['modes'][1]
    check('manuscript negative witness', witness == manuscript
          == Q(*z['shell_scaled']) == Q(*z['schur_scaled']) and witness < 0)
    check('witness anchor correction and multiplicity', z['anchor_correction_over_rho'] == [0, 1]
          and z['multiplicity'] == 955)
    check('constant-only anchor correction', all(Q(*z['anchor_correction_over_rho'])
          == (size*p[5]**2 if (z['a'], z['b']) == (0, 0) else 0) for z in report['modes']))
    M = Q(*report['normalization']['objective'])
    tau = Q(65537**28, 2**128)
    check('objective still insufficient', M.__floor__() >= tau.__floor__()+1
          and Q(1383, 1000) < M/tau < Q(1384, 1000))
    out = ROOT / 'conditioned-five-shell-critical-audit-results.json'
    data = {'reconstruction_sha256': hashlib.sha256(raw).hexdigest(), 'checks': checks,
            'failures': failures, 'point_cases': point_cases, 'witness_terms': terms,
            'witness_scaled': enc(witness), 'sign_table': signs,
            'dimension': size, 'objective_floor_minus_T': M.__floor__()-tau.__floor__()-1}
    out.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print(f'Manuscript/point-count checks: {len(checks)}; failures: {len(failures)}')
    print('Modes: 36/36; negative/positive/zero: 12/24/0; PSD requires zero negative modes')
    print('Exact point witness agrees and is negative:', witness == manuscript and witness < 0)
    print('Objective floor >= T:', data['objective_floor_minus_T'] >= 0)
    print('Certificate:', out)
    if failures:
        print('Failures:', failures)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
