#!/usr/bin/env python3
"""Complete independent replay; imports no producer or prior checker."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path

ROOT = Path('scripts/conductor389-kurihara')


def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def row(x, n):
    assert type(x) is list and len(x) == n
    assert all(type(v) is int for v in x)
    return x


def rat(x):
    assert type(x) is str and str(Q(x)) == x
    return Q(x)


def canonical(a, b):
    assert a or b
    if b == 0:
        return [1, 0]
    d = gcd(a, b)*(1 if b > 0 else -1)
    return [a//d, b//d]


def dot(a, b):
    assert len(a) == len(b)
    return sum(x*y for x, y in zip(a, b))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--certificate', type=Path, default=ROOT/'certificate.json')
    parser.add_argument('--terms', type=Path, default=ROOT/'terms.jsonl')
    parser.add_argument('--out', type=Path, default=ROOT/'verification.json')
    parser.add_argument('--replay', type=Path, default=ROOT/'replay.jsonl')
    args = parser.parse_args()
    report = {'checks': {}, 'failures': [], 'completed_terms': 0,
              'external_theorems_verified_by_script': False,
              'verifier_sha256': sha(__file__)}
    def check(name, condition=True):
        assert condition, name
        report['checks'][name] = True
    try:
        report['certificate_sha256'] = sha(args.certificate)
        cert = json.loads(args.certificate.read_text())
        assert cert['failures'] == []
        assert cert['instance'] == {
            'model': [0, 1, 1, -2, 0], 'conductor': 389, 'p': 7, 'm': 1,
            'prime_cap': 500, 'product_cap': 100000, 'period': 'total minimal real',
            'orientation': 'infinity to a/N',
            'selection': 'lexicographically first distinct increasing pair'}
        inputs = [f'scripts/{t}/{n}.json' for t in
                  ('relative-t2', 'twist-five', 'calibrated-symbols')
                  for n in ('certificate', 'verification', 'audit')]
        assert cert['input_sha256'] == {p: sha(p) for p in inputs}
        data = [json.loads(Path(p).read_text()) for p in inputs]
        base, bv, ba, twist, tv, ta, sym, sv, sa = data
        assert not base['failures'] and not sym['failures']
        assert sym['input_sha256'] == {p: sha(p) for p in inputs[:6]}
        for i, reports in [(0, (bv, ba)), (6, (sv, sa))]:
            for r in reports:
                assert r['certificate_sha256'] == sha(inputs[i])
                assert not r['failures'] and r['checks']
                assert all(v is True for v in r['checks'].values())
        assert tv['certificate_sha256'] == ta['certificate_sha256'] == sha(inputs[3])
        assert ta['base_certificate_sha256'] == sha(inputs[0])
        assert not ta['failures'] and rat(ta['q']) == 4
        assert tv['finite_arithmetic_verified'] is True
        assert tv['reports'] and all(r['isolated'] and rat(r['q']) == 4
                                    and not r['failures'] for r in tv['reports'])
        assert twist['attempts'][twist['selected_attempt']]['isolation']['candidates'] == ['4']
        assert base['arithmetic']['model'] == [0, 1, 1, -2, 0]
        assert base['arithmetic']['conductor'] == base['arithmetic']['discriminant'] == 389
        check('audited_L030_L032_inputs_and_normalization_provenance')

        # Trial divisions cover every integer in the congruence class under cap.
        candidates = list(range(8, 501, 7))
        assert len(cert['candidates']) == len(candidates)
        eligible, point_counts = [], []
        for ell, saved in zip(candidates, cert['candidates']):
            assert saved['ell'] == ell
            assert saved['division_trials'] == [[d, ell % d] for d in range(2, isqrt(ell)+1)]
            divisors = [d for d in range(2, ell) if ell % d == 0]
            prime = not divisors
            assert saved['prime'] is prime
            assert saved['coprime'] is (gcd(ell, 2723) == 1)
            if not prime or gcd(ell, 2723) != 1:
                continue
            # Direct equation enumeration, separate from producer's histogram lookup.
            xcounts = []
            yhist = [0]*ell
            for y in range(ell):
                yhist[(y*y+y) % ell] += 1
            for x in range(ell):
                ys = [y for y in range(ell) if
                      (y*y+y-x*x*x-x*x+2*x) % ell == 0]
                xcounts.append(len(ys))
            count = 1+sum(xcounts)
            assert saved['y_histogram'] == yhist
            assert saved['rhs'] == [(x*x*x+x*x-2*x) % ell for x in range(ell)]
            assert saved['x_counts'] == xcounts and saved['point_count'] == count
            assert saved['trace'] == ell+1-count
            assert saved['eligible'] is (count % 7 == 0)
            point_counts.append({'ell': ell, 'point_count': count, 'trace': ell+1-count})
            if count % 7 == 0:
                eligible.append(ell)
        assert cert['eligible'] == eligible
        pairs = [{'pair': [a, b], 'product': a*b, 'within_cap': a*b <= 100000}
                 for a in eligible for b in eligible if a < b]
        assert cert['pairs'] == pairs
        allowed = sorted(r['pair'] for r in pairs if r['within_cap'])
        selected = allowed[0] if allowed else None
        assert cert['selected_pair'] == selected, 'selected pair is not the certified first eligible pair'
        report['eligibility'] = {'candidates': len(candidates), 'point_counts': point_counts,
                                 'eligible': eligible, 'selected_pair': selected,
                                 'prime_cap': 500, 'product_cap': 100000}
        check('complete_prime_counts_eligibility_and_lexicographic_selection')
        if selected is None:
            assert cert['logs'] == []
            assert cert['result'] == {'status': 'NO_ELIGIBLE_PAIR', 'scalar': None, 'terms': 0}
            report['result'] = cert['result']
        else:
            left, right = selected
            N = left*right
            assert N <= 100000 and right <= 500
            assert len(cert['logs']) == 2
            exponents = []
            for ell, saved in zip(selected, cert['logs']):
                assert saved['ell'] == ell
                eta = saved['eta']
                assert type(eta) is int and 1 <= eta < ell
                factors = [q for q in range(2, ell) if (ell-1) % q == 0
                           and all(q % d for d in range(2, isqrt(q)+1))]
                assert all(pow(eta, (ell-1)//q, ell) != 1 for q in factors)
                smaller = []
                for g in range(1, eta):
                    orbit, v = set(), 1
                    for _ in range(ell-1):
                        orbit.add(v)
                        v = v*g % ell
                    assert len(orbit) < ell-1
                    smaller.append({'eta': g, 'distinct_powers': len(orbit)})
                assert saved['smaller_root_tests'] == smaller
                assert len(saved['powers']) == ell-1
                inverse, v = [None]*ell, 1
                for j, power in enumerate(saved['powers']):
                    assert type(power) is int and power == v
                    assert inverse[v] is None
                    inverse[v] = j
                    v = v*eta % ell
                assert v == 1 and sorted(saved['powers']) == list(range(1, ell))
                assert saved['exponents'] == inverse
                assert all(pow(eta, inverse[a], ell) == a for a in range(1, ell))
                exponents.append(inverse)
            check('least_primitive_roots_every_power_and_inverse_log')

            coords = base['presentation']['integral_generator_coordinates']
            assert len(coords) == 390
            for c in coords:
                row(c, 65)
            f = [rat(v) for v in sym['basis_functional']]
            y = [rat(v) for v in sym['integral_generator_values']]
            phi = [rat(v) for v in base['integration_line']['basis_functional']]
            assert len(f) == len(phi) == 65 and len(y) == 390
            assert f == [-v for v in phi] and sym['scale'] == '-1'
            assert all(dot(c, f) == v for c, v in zip(coords, y))
            assert all((2*v).denominator == 1 for v in y)
            assert sym['denominator']['lcm'] == 2
            doubled = [int(2*v) for v in y]
            for r in base['relations']+base['presentation']['saturated_relation_basis']:
                assert dot(row(r, 390), doubled) == 0
            lifts = [[0, -1, 1, i] for i in range(389)]+[[1, 0, 0, 1]]
            assert base['SL2_lifts'] == lifts
            check('all_generator_values_quotient_functional_and_relations')
            terms_hash = sha(args.terms)
            assert cert['terms_sha256'] == terms_hash
            report['terms_sha256'] = terms_hash
            total2, segments, zeros, terms, weighted_exact = 0, 0, 0, 0, Q(0)
            with args.terms.open() as source, args.replay.open('w') as replay:
                for a in range(1, N):
                    if a % left == 0 or a % right == 0:
                        continue
                    line = source.readline()
                    assert line, f'missing term a={a}'
                    term = json.loads(line)
                    assert type(term['a']) is int and term['a'] == a, f'unit ordering a={a}'
                    assert row(term['argument'], 2) == [a, N]
                    cf = term['continued_fraction']
                    assert type(cf) is list and cf and all(type(k) is int for k in cf)
                    r = Q(cf[-1])
                    for k in reversed(cf[:-1]):
                        assert r
                        r = k+1/r
                    assert r == Q(a, N)
                    assert len(term['segments']) == len(cf)
                    raw, previous = [0]*390, [1, 0]
                    for seg in term['segments']:
                        A, B, C, D = row(seg['lift'], 4)
                        assert A*D-B*C == 1
                        assert seg['start'] == previous == canonical(B, D)
                        assert seg['end'] == canonical(A, C)
                        # Exhaustive coset identification independent of inverse lookup.
                        hits = [i for i, (c, d) in enumerate(
                            [(1, j) for j in range(389)]+[(0, 1)])
                            if (C*d-D*c) % 389 == 0]
                        assert len(hits) == 1
                        i = hits[0]
                        assert type(seg['coset']) is int and seg['coset'] == i
                        e, f0, g, h = lifts[i]
                        G, H, I, J = A*h-B*g, B*e-A*f0, C*h-D*g, D*e-C*f0
                        assert row(seg['Gamma0_reduction'], 4) == [G, H, I, J]
                        assert I % 389 == 0 and G*J-H*I == 1
                        assert [G*e+H*g, G*f0+H*h, I*e+J*g, I*f0+J*h] == [A, B, C, D]
                        raw[i] += 1
                        previous = seg['end']
                        segments += 1
                    assert previous == [a, N]
                    assert row(term['raw'], 390) == raw
                    support = [(i, k) for i, k in enumerate(raw) if k]
                    quotient = [sum(k*coords[i][j] for i, k in support) for j in range(65)]
                    assert row(term['coordinates'], 65) == quotient
                    value2 = dot(raw, doubled)
                    value = Q(value2, 2)
                    assert value == rat(term['value']) == dot(quotient, f)
                    logs = [exponents[0][a % left] % 7, exponents[1][a % right] % 7]
                    assert row(term['logs'], 2) == logs
                    symbol = (value2*4) % 7
                    contribution2 = value2*logs[0]*logs[1]
                    contribution = contribution2*4 % 7
                    assert type(term['symbol_mod7']) is int and term['symbol_mod7'] == symbol
                    assert type(term['term']) is int and term['term'] == contribution, f'altered contribution a={a}'
                    total2 += contribution2
                    weighted_exact += value*logs[0]*logs[1]
                    terms += 1
                    zeros += contribution == 0
                    replay.write(json.dumps({'a': a, 'value_twice': value2, 'logs': logs,
                                              'contribution_twice': contribution2,
                                              'prefix_twice': total2}, separators=(',', ':'))+'\n')
                    report['completed_terms'] = terms
                    if terms % 5000 == 0:
                        print('replayed terms', terms, '/', (left-1)*(right-1), flush=True)
                assert source.read() == '', 'extra or duplicate terms'
            assert terms == (left-1)*(right-1)
            assert 2*weighted_exact == total2
            scalar = (total2*4) % 7
            assert scalar == weighted_exact.numerator*pow(weighted_exact.denominator, -1, 7) % 7
            result = {'status': 'ONE_SCALAR_COMPLETE', 'scalar': scalar, 'N': N,
                      'terms': terms, 'required_terms': (left-1)*(right-1),
                      'segments': segments, 'zero_terms': zeros}
            assert cert['result'] == result
            report['result'] = result
            report['independent_sum'] = {'weighted_exact': str(weighted_exact),
                                         'weighted_twice': total2, 'scalar': scalar}
            report['replay_sha256'] = sha(args.replay)
            check('every_unit_path_segment_full_quotient_log_and_uncombined_term')
            check('independent_doubled_integer_and_rational_sums')
            check('stop_after_single_selected_pair')
    except Exception as error:
        report['failures'].append(f'{type(error).__name__}: {error}')
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print('result', report.get('result'), 'failures', report['failures'],
          'report', args.out, flush=True)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
