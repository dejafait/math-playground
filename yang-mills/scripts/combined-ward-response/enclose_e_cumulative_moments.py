"""L134 retained R moments by exact endpoint/IBP reduction of L082 inputs.

Writes every imported and resulting interval to disk. --audit replays all
records and checks a separate moment recurrence and exact product coverage.
No machine trigonometry or new spatial quadrature is used.
"""
import hashlib
import json
import sys
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import enclose_continuum_first_pair as en

ROOT = Path(__file__).parent
I, S, rat = en.I, en.S, en.rat
ZERO = (rat(0), rat(0))
SOURCE = ROOT / 'continuum-first-pair-enclosure-certificate.json'
CERT = ROOT / 'e-cumulative-moments-certificate.json'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def keys():
    return ([(0, n) for n in range(-192, 193)]
            + [(1, n) for n in range(-96, 97)] + [(2, 0)])


def record(z):
    return dict(real=en.rec(z[0]), imag=en.rec(z[1]))


def width(z):
    return max(F(v.hi-v.lo, S) for v in z)


def phase(n):
    a, b = ((1, 0), (0, 1), (-1, 0), (0, -1))[n % 4]
    return rat(a), rat(b)


def scale(z, q):
    return z[0]*rat(q), z[1]*rat(q)


def subtract(z, w):
    return z[0]-w[0], z[1]-w[1]


def generate(source):
    assert int(source['scale']) == S == 10**180 and source['K'] == 96
    assert not source['failures']
    assert source['input_sha256'] == sha(ROOT/'stored-fourier-enclosure-certificate.json')
    pi = en.read(source['pi'])
    assert rat(3).hi < pi.lo < pi.hi < rat(4).lo
    omega = pi/rat(8)
    source_rows = {(r['h'], r['n']): r for r in source['moments']}
    assert len(source_rows) == len(source['moments']) == 1156
    used = {(0, 0)}
    for h, n in keys():
        used.update((j, n) for j in range(h+1)) if n else used.add((h+1, 0))
    inputs = [source_rows[k] for k in sorted(used)]
    moments = {(r['h'], r['n']): (en.read(r['real']), en.read(r['imag'])) for r in inputs}
    # Exact parity allows narrowing the imported zero-frequency imaginary part.
    mass_raw = moments[0, 0]
    assert mass_raw[1].lo <= 0 <= mass_raw[1].hi
    mass = mass_raw[0], rat(0)
    assert rat(5).hi < mass[0].lo <= mass[0].hi < rat(6).lo
    results, values = [], {}
    for h, n in keys():
        if n == 0:
            value = scale(subtract(scale(mass, 4**(h+1)), moments[h+1, 0]), F(1, h+1))
        else:
            inverse = rat(1)/(omega*rat(n))
            reciprocal = rat(0), -inverse  # 1/(i n omega)
            power = rat(1), rat(0)
            value = ZERO
            for j in range(h+1):
                power = en.cmul(power, reciprocal)
                difference = subtract(scale(en.cmul(mass, phase(n)), 4**(h-j)), moments[h-j, n])
                coefficient = (-1)**j * factorial(h)//factorial(h-j)
                value = en.cadd(value, scale(en.cmul(power, difference), coefficient))
        values[h, n] = value
        results.append(dict(h=h, n=n, **record(value), component_width=str(width(value))))
    # Exact symbolic frequency/degree coverage for every direct/prefix product.
    def row(kind, n):
        if n == 0:
            assert kind == 'prefix'
            return {(0, 0), (0, 1)}
        return {(n, 0), (-n, 0)}
    coverage, required = [], set(keys())
    for left, right in (('direct','direct'), ('direct','prefix'),
                        ('prefix','direct'), ('prefix','prefix')):
        used_here, count = set(), 0
        for n in range(0 if left == 'prefix' else 1, 97):
            for m in range(0 if right == 'prefix' else 1, 97):
                count += 1
                for a, h in row(left, n):
                    for b, j in row(right, m):
                        used_here.add((h+j, a+b))
        assert used_here <= required
        coverage.append(dict(left=left, right=right, entries=count,
                             required_moments=[list(k) for k in sorted(used_here)]))
    # Constant-prefix integral and its separate upper-tail contribution.
    whole = scale(en.cadd(en.cadd(values[2,0], scale(values[1,0], 8)),
                         scale(values[0,0], 16)), F(1,8))
    simplified = subtract(scale(mass, F(56,3)), scale(moments[2,0], F(1,2)))
    tail = scale(mass, F(169,24))
    assert all(max(a.lo,b.lo) <= min(a.hi,b.hi) for a,b in zip(whole,simplified))
    assert tail[0].lo > rat(F(845,24)).hi
    assert tail[0].hi < rat(F(169,4)).lo
    assert rat(F(388407,10000)).hi < tail[0].lo
    assert tail[0].hi < rat(F(388408,10000)).lo
    worst = max(results, key=lambda r: F(r['component_width']))
    assert F(worst['component_width']) < F(692,10**14)
    failures = [f"h={r['h']}, n={r['n']}: width >=1e-9"
                for r in results if F(r['component_width']) >= F(1,10**9)]
    return dict(K=96, scale=str(S), source=SOURCE.name, source_sha256=sha(SOURCE),
                script_sha256=sha(Path(__file__)), pi=en.rec(pi),
                imported_moments=inputs, mass=record(mass), moments=results,
                product_coverage=coverage, constant_prefix=record(whole),
                constant_prefix_simplified=record(simplified), upper_tail=record(tail),
                max_component_width=worst['component_width'],
                worst_moment=dict(h=worst['h'],n=worst['n']),
                required_width='1/1000000000', failures=failures,
                qualifications=['L082 source intervals are imported theorem inputs.',
                                'Integer inclusion only; no new quadrature or IEEE calculation.',
                                'R moments only; U_i,W_i and E are not evaluated.']), values, moments, omega, mass


def main(audit=False):
    source = json.loads(SOURCE.read_text())
    data, values, moments, omega, mass = generate(source)
    if audit:
        saved = json.loads(CERT.read_text())
        assert saved == data
        recurrence_checks = 0
        for h, n in keys():
            if not n:
                continue
            rhs = subtract(scale(en.cmul(mass,phase(n)),4**h), moments[h,n])
            if h:
                rhs = subtract(rhs,scale(values[h-1,n],h))
            inv = rat(1)/(omega*rat(n))
            alternate = en.cmul(rhs,(rat(0),-inv))
            assert all(max(a.lo,b.lo) <= min(a.hi,b.hi) for a,b in zip(alternate,values[h,n]))
            recurrence_checks += 1
        for h,n in keys():
            if (h,-n) in values:
                a,b = values[h,n], values[h,-n]
                assert max(a[0].lo,b[0].lo) <= min(a[0].hi,b[0].hi)
                assert max(a[1].lo,-b[1].hi) <= min(a[1].hi,-b[1].lo)
        audit_path = ROOT/'e-cumulative-moments-audit.json'
        audit_path.write_text(json.dumps(dict(certificate_sha256=sha(CERT),
            replayed_moments=len(values), imported_moments=len(moments),
            recurrence_checks=recurrence_checks,
            covered_products=sum(r['entries'] for r in data['product_coverage']),
            max_component_width=data['max_component_width'],failures=[]), indent=2)+'\n')
        print(f'PASS: all {len(values)} moments replayed; {recurrence_checks} recurrence checks; failures 0; audit {audit_path}')
    else:
        CERT.write_text(json.dumps(data,indent=2)+'\n')
    print(f"R moments {len(values)}, imported rho moments {len(moments)}, "
          f"covered products {sum(r['entries'] for r in data['product_coverage'])}; "
          f"max component width {float(F(data['max_component_width'])):.8g}, required <1e-9; "
          f"failures {len(data['failures'])}; certificate {CERT}")
    tail = data['upper_tail']['real']
    print(f"Constant-prefix upper tail [{float(F(int(tail['lo']),S)):.10g}, "
          f"{float(F(int(tail['hi']),S)):.10g}], required positive >845/24")
    assert not data['failures']


if __name__ == '__main__':
    main('--audit' in sys.argv[1:])
