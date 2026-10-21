#!/usr/bin/env python3
"""Approved finite L027 specialization; exact arithmetic and complete paths."""
import hashlib
import json
from fractions import Fraction as Q
from math import comb, gcd
from pathlib import Path

ROOT = Path('scripts/conductor-eleven/quadratic-seven')
BASE = Path('scripts/conductor-eleven')
CAL = BASE/'calibrated-symbols'


def bindings():
    symbols = json.loads((CAL/'certificate.json').read_text())
    audit = json.loads((CAL/'critical-audit/audit.json').read_text())
    hashes = dict(symbols['input_sha256'])
    hashes.update({str(CAL/name): value for name, value in audit['original_sha256'].items()})
    hashes[str(CAL/'critical-audit/alternative-paths.json')] = audit['alternative_sha256']
    for name in ('audit.json', 'pre-replay-manifest.json'):
        p = CAL/'critical-audit'/name
        hashes[str(p)] = sha(p)
    assert not audit['failures'] and all(audit['checks'].values())
    assert audit['original_inputs_unchanged'] and audit['prior_inputs_unchanged']
    assert all(sha(p) == h for p, h in hashes.items())
    return hashes


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def vp(x):
    x = Q(x)
    if not x:
        return 'infinity'
    def order(k):
        e = 0
        while k % 7 == 0:
            k //= 7
            e += 1
        return e
    return order(x.numerator)-order(x.denominator)


def canonical(p, q):
    if q == 0:
        assert p
        return [1, 0]
    x = Q(p, q)
    return [x.numerator, x.denominator]


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    cert = {'input_sha256': {},
            'instance': {'model': [0, -1, 1, -10, -20], 'p': 7, 'level': 11,
                         'C': 0, 'gamma': 8, 'branch': 'primitive untwisted trivial',
                         'period': 'total minimal real'},
            'paths': {}, 'attempts': [], 'failures': []}
    def save():
        (ROOT/'certificate.json').write_text(json.dumps(cert, indent=2)+'\n')
    try:
        cert['input_sha256'] = bindings()
        save()
        base = json.loads((BASE/'structural-certificate.json').read_text())
        dual = json.loads((BASE/'dual-certificate.json').read_text())
        arithmetic = json.loads((BASE/'arithmetic-certificate.json').read_text())
        calibrated = json.loads((CAL/'certificate.json').read_text())
        assert arithmetic['invariants']['Delta'] == -11**5
        assert dual['arithmetic']['model'] == [0, -1, 1, -10, -20]
        assert base['inputs'] == {'N': 11, 'P': [2]}
        assert calibrated['scale'] == '1/5' and calibrated['denominator']['lcm'] == 10
        coords = base['presentation']['generator_coordinates']
        lifts = base['cosets']['lifts']
        reps = base['cosets']['representatives']
        values = [Q(v) for v in calibrated['integral_generator_values']]
        functional = [Q(v) for v in calibrated['basis_functional']]
        assert len(coords) == len(lifts) == len(values) == 12 and len(functional) == 3
        assert all(len(row) == 3 for row in coords)
        assert all(Q(sum(a*b for a, b in zip(row, functional))) == value
                   for row, value in zip(coords, values))
        assert all(vp(v) == 'infinity' or vp(v) >= 0 for v in values)

        # Production uses completing the square; replay exhausts all 49 pairs.
        rows = []
        for x in range(7):
            rhs = (x**3-x*x-10*x-20) % 7
            disc = (1+4*rhs) % 7
            legendre = 0 if not disc else (1 if pow(disc, 3, 7) == 1 else -1)
            ys = [((z-1)*4) % 7 for z in range(7) if z*z % 7 == disc]
            rows.append({'x': x, 'rhs': rhs, 'disc': disc, 'legendre': legendre,
                         'ys': sorted(ys), 'count': 1+legendre})
        points = 1+sum(row['count'] for row in rows)
        t = 8-points
        cert['ordinary'] = {'rows': rows, 'point_at_infinity': [0, 1, 0],
                            'point_count': points, 't': t, 'discriminant_mod_p': (-11**5) % 7,
                            'good': gcd(-11**5, 7) == 1, 'ordinary': t % 7 != 0}
        print('point count', points, 't', t, 'good', cert['ordinary']['good'],
              'ordinary', cert['ordinary']['ordinary'], flush=True)
        save()
        assert cert['ordinary']['good'] and cert['ordinary']['ordinary']

        def path(r):
            key = str(r)
            if key in cert['paths']:
                return key, Q(cert['paths'][key]['value'])
            a, b = r.numerator, r.denominator
            digits, numerator, denominator = [], a, b
            while denominator:
                digit = numerator//denominator
                digits.append(digit)
                numerator, denominator = denominator, numerator-digit*denominator
            p0, q0, p1, q1 = 0, 1, 1, 0
            raw, segments = [0]*12, []
            for digit in digits:
                p2, q2 = digit*p1+p0, digit*q1+q0
                det = p2*q1-p1*q2
                assert abs(det) == 1
                h = [det*p2, p1, det*q2, q1]
                A, B, C, D = h
                rep = [1, D*pow(C % 11, -1, 11) % 11] if C % 11 else [0, 1]
                i = reps.index(rep)
                e, f, g, k = lifts[i]
                gamma = [A*k-B*g, -A*f+B*e, C*k-D*g, -C*f+D*e]
                assert gamma[2] % 11 == 0
                segments.append({'start': canonical(p1, q1), 'end': canonical(p2, q2),
                                 'lift': h, 'coset': i, 'Gamma0_reduction': gamma})
                raw[i] += 1
                p0, q0, p1, q1 = p1, q1, p2, q2
            assert canonical(p1, q1) == [a, b]
            quotient = [sum(raw[i]*coords[i][j] for i in range(12)) for j in range(3)]
            value = sum(Q(a)*b for a, b in zip(quotient, functional))
            assert value == sum(Q(a)*b for a, b in zip(raw, values))
            cert['paths'][key] = {'argument': [a, b], 'continued_fraction': digits,
                                  'segments': segments, 'raw': raw,
                                  'coordinates': quotient, 'value': str(value)}
            return key, value

        for n in (2, 3, 4):
            M, modulus = n+1, 7**n
            roots = []
            for d in range(1, 7):
                w = pow(d, 7**(n-1), modulus)
                assert 1 <= w < modulus and w % 7 == d and pow(w, 6, modulus) == 1
                roots.append({'d': d, 'w': w, 'sixth_residual': w**6-1,
                              'residual_valuation': vp(w**6-1), 'derivative_mod_p': 6*w**5 % 7})
            u = t % 7
            for k in range(1, M):
                choices = [u+h*7**k for h in range(7)
                           if ((u+h*7**k)**2-t*(u+h*7**k)+7) % (7**(k+1)) == 0]
                assert len(choices) == 1
                u = choices[0]
            residual = u*u-t*u+7
            attempt = {'n': n, 'M': M, 'N': min(n-1, M), 'teichmuller': roots,
                       'unit_root': {'u': str(u), 'residual': residual,
                                     'residual_valuation': vp(residual),
                                     'derivative_mod_p': (2*u-t) % 7, 'valuation': vp(u)},
                       'terms': []}
            total, sum_A, sum_B = Q(0), Q(0), Q(0)
            for root in roots:
                for j in range(7**(n-1)):
                    r = root['w']*pow(8, j, modulus) % modulus
                    A_key, A_value = path(Q(r, modulus))
                    B_key, B_value = path(Q(r, 7**(n-1)))
                    weight = comb(j, 2)
                    term = weight*(A_value/Q(u)**n-B_value/Q(u)**(n+1))
                    attempt['terms'].append({'d': root['d'], 'j': j, 'r': r,
                                             'binomial': weight, 'A_path': A_key,
                                             'B_path': B_key, 'A': str(A_value),
                                             'B': str(B_value), 'term': str(term)})
                    sum_A += weight*A_value
                    sum_B += weight*B_value
                    total += term
            v = vp(total)
            passed = v != 'infinity' and attempt['N'] > v
            attempt.update({'sum_A': str(sum_A), 'sum_B': str(sum_B), 'b': str(total),
                            'valuation_b': v, 'strict_bound': passed,
                            'required_terms': 6*7**(n-1), 'actual_terms': len(attempt['terms'])})
            cert['attempts'].append(attempt)
            save()
            print('n', n, 'M', M, 'terms actual/required', len(attempt['terms']), '/',
                  attempt['required_terms'], 'b', total, 'v_7(b)', v, 'N', attempt['N'],
                  'strict', passed, 'certificate', ROOT/'certificate.json', flush=True)
            if passed:
                break
        cert['result'] = {'strict_bound': cert['attempts'][-1]['strict_bound'],
                          'selected_n': cert['attempts'][-1]['n'],
                          'paths': len(cert['paths']),
                          'failures': []}
    except Exception as error:
        cert['failures'].append(f'{type(error).__name__}: {error}')
    save()
    print('ordinary evidence', cert.get('ordinary', {}).get('point_count'),
          't', cert.get('ordinary', {}).get('t'), 'failures', cert['failures'],
          'certificate', ROOT/'certificate.json')
    if cert['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
