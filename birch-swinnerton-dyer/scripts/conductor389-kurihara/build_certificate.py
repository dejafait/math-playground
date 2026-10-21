#!/usr/bin/env python3
"""One assessed Kim depth-one sum; no rank or point inputs."""
import hashlib
import json
from fractions import Fraction as Q
from math import gcd, isqrt
from pathlib import Path

ROOT = Path('scripts/conductor389-kurihara')
INPUTS = [f'scripts/{t}/{n}.json' for t in
          ('relative-t2', 'twist-five', 'calibrated-symbols')
          for n in ('certificate', 'verification', 'audit')]


def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(1048576), b''):
            h.update(b)
    return h.hexdigest()


def cusp(a, b):
    if not b:
        return [1, 0]
    q = Q(a, b)
    return [q.numerator, q.denominator]


def main():
    ROOT.mkdir(exist_ok=True)
    cert = {'input_sha256': {p: sha(p) for p in INPUTS},
            'instance': {'model': [0, 1, 1, -2, 0], 'conductor': 389,
                         'p': 7, 'm': 1, 'prime_cap': 500, 'product_cap': 100000,
                         'period': 'total minimal real', 'orientation': 'infinity to a/N',
                         'selection': 'lexicographically first distinct increasing pair'},
            'candidates': [], 'eligible': [], 'pairs': [], 'logs': [], 'failures': []}
    def save():
        (ROOT/'certificate.json').write_text(json.dumps(cert, indent=2)+'\n')
    try:
        base = json.loads(Path(INPUTS[0]).read_text())
        sym = json.loads(Path(INPUTS[6]).read_text())
        assert sym['scale'] == '-1' and sym['denominator']['lcm'] == 2
        coords = base['presentation']['integral_generator_coordinates']
        values = [Q(x) for x in sym['integral_generator_values']]
        functional = [Q(x) for x in sym['basis_functional']]
        lifts = base['SL2_lifts']
        for ell in range(8, 501, 7):
            trials = [[d, ell % d] for d in range(2, isqrt(ell)+1)]
            prime = all(r for d, r in trials)
            row = {'ell': ell, 'division_trials': trials, 'prime': prime,
                   'coprime': gcd(ell, 389*7) == 1}
            if prime and row['coprime']:
                # Root-count histogram for y^2+y; separate replay enumerates y.
                histogram = [0]*ell
                for y in range(ell):
                    histogram[(y*y+y) % ell] += 1
                rhs = [(x**3+x*x-2*x) % ell for x in range(ell)]
                counts = [histogram[r] for r in rhs]
                points = 1+sum(counts)
                row.update({'y_histogram': histogram, 'rhs': rhs,
                            'x_counts': counts, 'point_count': points,
                            'trace': ell+1-points, 'eligible': points % 7 == 0})
                if row['eligible']:
                    cert['eligible'].append(ell)
            cert['candidates'].append(row)
        eligible = cert['eligible']
        cert['pairs'] = [{'pair': [a, b], 'product': a*b, 'within_cap': a*b <= 100000}
                         for i, a in enumerate(eligible) for b in eligible[i+1:]]
        admissible = [r['pair'] for r in cert['pairs'] if r['within_cap']]
        cert['selected_pair'] = admissible[0] if admissible else None
        save()
        print('eligible', eligible, 'selected', cert['selected_pair'],
              'caps ell<=500, product<=100000', flush=True)
        if not admissible:
            cert['result'] = {'status': 'NO_ELIGIBLE_PAIR', 'scalar': None, 'terms': 0}
            save()
            return
        left, right = cert['selected_pair']
        N = left*right
        log_tables = []
        for ell in (left, right):
            tested = []
            for eta in range(1, ell):
                powers = [pow(eta, j, ell) for j in range(ell-1)]
                tested.append({'eta': eta, 'distinct_powers': len(set(powers))})
                if len(set(powers)) == ell-1:
                    break
            table = [None]*ell
            for j, a in enumerate(powers):
                table[a] = j
            cert['logs'].append({'ell': ell, 'eta': eta, 'smaller_root_tests': tested[:-1],
                                 'powers': powers, 'exponents': table})
            log_tables.append(table)
        save()
        total, terms, segments, zeros = 0, 0, 0, 0
        with (ROOT/'terms.jsonl').open('w') as out:
            for a in range(1, N):
                if gcd(a, N) != 1:
                    continue
                n, d, cf = a, N, []
                while d:
                    k = n//d
                    cf.append(k)
                    n, d = d, n-k*d
                p0, q0, p1, q1 = 0, 1, 1, 0
                raw, path = [0]*390, []
                for k in cf:
                    p2, q2 = k*p1+p0, k*q1+q0
                    sign = p2*q1-p1*q2
                    assert abs(sign) == 1
                    A, B, C, D = sign*p2, p1, sign*q2, q1
                    i = D*pow(C % 389, -1, 389) % 389 if C % 389 else 389
                    e, f, g, h = lifts[i]
                    gamma = [A*h-B*g, -A*f+B*e, C*h-D*g, -C*f+D*e]
                    path.append({'start': cusp(p1, q1), 'end': cusp(p2, q2),
                                 'lift': [A, B, C, D], 'coset': i,
                                 'Gamma0_reduction': gamma})
                    raw[i] += 1
                    p0, q0, p1, q1 = p1, q1, p2, q2
                support = [(i, k) for i, k in enumerate(raw) if k]
                quotient = [sum(k*coords[i][j] for i, k in support) for j in range(65)]
                value = sum((k*values[i] for i, k in support), Q(0))
                assert value == sum((x*y for x, y in zip(quotient, functional)), Q(0))
                logs = [log_tables[0][a % left] % 7, log_tables[1][a % right] % 7]
                residue = value.numerator*pow(value.denominator, -1, 7) % 7
                term = residue*logs[0]*logs[1] % 7
                out.write(json.dumps({'a': a, 'argument': [a, N], 'continued_fraction': cf,
                                      'segments': path, 'raw': raw, 'coordinates': quotient,
                                      'value': str(value), 'logs': logs,
                                      'symbol_mod7': residue, 'term': term}, separators=(',', ':'))+'\n')
                terms += 1
                segments += len(path)
                zeros += term == 0
                total = (total+term) % 7
        assert terms == (left-1)*(right-1)
        cert['terms_sha256'] = sha(ROOT/'terms.jsonl')
        cert['result'] = {'status': 'ONE_SCALAR_COMPLETE', 'scalar': total,
                          'N': N, 'terms': terms, 'required_terms': (left-1)*(right-1),
                          'segments': segments, 'zero_terms': zeros}
    except Exception as error:
        cert['failures'].append(f'{type(error).__name__}: {error}')
    save()
    print('result', cert.get('result'), 'failures', cert['failures'],
          'certificate', ROOT/'certificate.json', 'terms', ROOT/'terms.jsonl', flush=True)
    if cert['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
