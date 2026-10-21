"""Independent rational verification of L154's complete saved inclusion.

No production modules are imported. Fractions are exact; square roots use
dyadic bounds proved by squaring. Every cell and all 256 final vertices
are checked. Heat inclusions remain conditional imported premises.
"""
import hashlib
import itertools
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / 'quartic-residual-coefficient-certificate.json'
OUT = ROOT / 'quartic-residual-independent-audit.json'
DYADIC = 2**140


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def sub(a, b):
    return a[0]-b[1], a[1]-b[0]


def mul(a, b):
    v = [x*y for x in a for y in b]
    return min(v), max(v)


def div(a, b):
    assert b[0] > 0
    return mul(a, (1/b[1], 1/b[0]))


def sqrt_bounds(a):
    assert 0 <= a[0] <= a[1]
    bounds = []
    for x in a:
        n = math.isqrt(x.numerator*DYADIC**2//x.denominator)
        lo, hi = Q(n, DYADIC), Q(n+1, DYADIC)
        assert lo*lo <= x < hi*hi
        bounds.append((lo, hi))
    return bounds[0][0], bounds[1][1]


def const(x):
    return Q(x), Q(x)


def encoded(a):
    return list(map(str, a))


def atan(q, n):
    s = sum((Q((-1)**j, (2*j+1)*q**(2*j+1)) for j in range(n)), Q(0))
    t = s+Q((-1)**n, (2*n+1)*q**(2*n+1))
    return min(s, t), max(s, t)


def cos_at(x):
    # Degree 96, remainder bounded by x^98/98! (degree 97 Taylor).
    term = total = Q(1)
    for j in range(1, 49):
        term *= -x*x/Q((2*j-1)*(2*j))
        total += term
    rem = Q(4**98, math.factorial(98))
    return total-rem, total+rem


def dyadic(a):
    lo = (a[0]*DYADIC).__floor__()
    hi = (a[1]*DYADIC).__ceil__()
    return Q(lo, DYADIC), Q(hi, DYADIC)


def main():
    saved = json.loads(SOURCE.read_text())
    failures, nodes, cells, vertices = [], [], [], []
    def check(ok, message):
        if not ok:
            failures.append(message)
    scale, n = int(saved['SCALE']), saved['N']
    check(n == 256 and scale == 10**30, 'domain')
    def decode(pair):
        return tuple(Q(int(x), scale) for x in pair)
    def contains(outer, inner):
        return outer[0] <= inner[0] <= inner[1] <= outer[1]
    pi = sub(mul(const(16), atan(5, 64)), mul(const(4), atan(239, 24)))
    check(Q(3) < pi[0] <= pi[1] < Q(22, 7), 'pi-domain')
    check(contains((Q(saved['pi']['lower']), Q(saved['pi']['upper'])), pi), 'pi')
    check(len(saved['nodes']) == n+1, 'node-count')
    for j, row in enumerate(saved['nodes']):
        theta = dyadic(mul(pi, const(Q(j, n))))
        # cos is decreasing on [0, pi]; bound exact endpoint values.
        co = (cos_at(theta[1])[0], cos_at(theta[0])[1])
        x = sub(const(2), mul(const(2), co))
        x = max(Q(0), x[0]), min(Q(4), x[1])
        if j in (0, n):
            x = const(0 if j == 0 else 4)
        ok = row['index'] == j and contains(decode(row['x']), x)
        check(ok, f'node-{j}')
        nodes.append(dict(index=j, independently_enclosed_x=encoded(x), passed=ok))
    check(len(saved['cells']) == n*n, 'cell-count')
    totals = [[0, 0], [0, 0]]
    for index, row in enumerate(saved['cells']):
        j, m = divmod(index, n)
        check(row[:2] == [j, m], f'cell-index-{index}')
        x = decode((saved['nodes'][j]['x'][0], saved['nodes'][j+1]['x'][1]))
        y = decode((saved['nodes'][m]['x'][0], saved['nodes'][m+1]['x'][1]))
        k = add(x, y)
        if j == m == 0:
            bx = (Q(0), sqrt_bounds(k)[1]/4)
        else:
            numerator = sub(div(k, const(2)), div(mul(x, y), const(4)))
            numerator = max(Q(0), numerator[0]), numerator[1]
            bx = div(numerator, sqrt_bounds(mul(k, add(k, const(4)))))
        by = div(mul(mul(sub(const(1), div(x, const(2))),
                         sub(const(1), div(y, const(2)))),
                     sub(const(1), sqrt_bounds(div(k, add(k, const(4)))))), const(2))
        ok = all(contains(decode(stored), new) for stored, new in zip(row[2:], (bx, by)))
        check(ok, f'cell-inclusion-{j}-{m}')
        cells.append(dict(index=[j, m], X=encoded(bx), Y=encoded(by), passed=ok))
        for total, stored in zip(totals, row[2:]):
            for r in range(2):
                total[r] += int(stored[r])
    bounds = [tuple(Q(t, scale*n*n) for t in total) for total in totals]
    check(totals == [[int(x) for x in r] for r in saved['totals']], 'totals')
    for b, row in zip(bounds, saved['bounds']):
        check(b == (Q(row['lower']), Q(row['upper'])), 'scalar-bound')
    for result in saved['results']:
        i = result['probe']
        values = []
        # Derive six forms first, then L153's original coefficients.
        for x, y, pd, pa, px, pc, br in itertools.product(
                *bounds, *[tuple(map(Q, v)) for v in result['heat_bounds']]):
            forms = ((pd-br)/2, br, -pa/2, (pa-pd)/2,
                     (pa-pd)/2-pc, (pd+pa-px)/2+pc)
            coef = (-8+60*x-6*y, 10-42*x+3*y, -4+60*x+6*y,
                    3+24*y, Q(9, 2)-24*x-12*y, -Q(3, 2)+6*x+3*y)
            value = sum(a*b for a, b in zip(forms, coef))
            values.append(value)
            vertices.append(dict(probe=i, inputs=encoded((x,y,pd,pa,px,pc,br)), value=str(value)))
        lo, hi = min(values), max(values)
        check((lo, hi) == (Q(result['lower']), Q(result['upper'])), f'endpoints-{i}')
        outer = (Q(-49200), Q(-43073)) if i == 3 else (Q(20982), Q(21570))
        check(outer[0] < lo <= hi < outer[1] and (hi < 0 or lo > 0), f'exclusion-{i}')
        print(f'Lambda_{i}: [{float(lo):.8f}, {float(hi):.8f}]; required strictly inside {outer} and excludes zero')
    check(len(vertices) == 256, 'vertex-count')
    # Check every imported heat interval against its complete saved error,
    # not against a printed center or a finite-cutoff diagnostic.
    def rational(v):
        return Q(int(v['numerator']), int(v['denominator']))
    heat_checks = []
    heat_sources = [('physical-h-enclosure-certificate.json', ('D', 'A', 'X', 'C')),
                    ('r-heat-enclosure-certificate.json', ('R',))]
    expected = {
        3: [('2359.1','2359.2'), ('19170.0','19170.1'),
            ('29198.8','29198.9'), ('1024.8','1024.9'),
            ('1228.1260684','1228.1260686')],
        6: [('703.6','703.7'), ('-4195.9','-4195.8'),
            ('69177.0','69177.1'), ('3218.2','3218.3'),
            ('451.5469823','451.5469825')]}
    for result in saved['results']:
        check(result['heat_bounds'] == [list(r) for r in expected[result['probe']]],
              f'heat-transcription-{result["probe"]}')
    for filename, tensors in heat_sources:
        source = json.loads((ROOT/filename).read_text())
        check(not source['failures'] and len(source['results']) == 2*len(tensors),
              f'heat-domain-{filename}')
        seen = set()
        for r in source['results']:
            i, label = r['probe'], r.get('tensor', 'R')
            check((i, label) not in seen, f'duplicate-heat-{i}-{label}')
            seen.add((i, label))
            c = Q(float.fromhex(r['retained']['center_hex']))
            radius = Q(float.fromhex(r['retained']['radius_hex']))
            time, tail = rational(r['time_error']), rational(r['spectral_tail'])
            error = radius+time+tail
            lo, hi = rational(r['lower']), rational(r['upper'])
            column = ('D','A','X','C','R').index(label)
            outer = tuple(map(Q, expected[i][column]))
            ok = (radius >= 0 and time >= 0 and tail >= 0
                  and error == rational(r['total_error'])
                  and (lo, hi) == (c-error, c+error)
                  and outer[0] < lo <= hi < outer[1])
            check(ok, f'heat-error-endpoint-{i}-{label}')
            heat_checks.append(dict(probe=i, tensor=label, total_error=str(error),
                                    imported=encoded(outer), passed=ok))
        check(seen == set(itertools.product((3,6), tensors)), f'heat-coverage-{filename}')
    for relative, digest in saved['hashes'].items():
        check(hashlib.sha256((ROOT.parent.parent/relative).read_bytes()).hexdigest() == digest,
              f'source-hash-{relative}')
    data = dict(source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                pi=encoded(pi), nodes=nodes, cells=cells, totals=totals,
                bounds=[encoded(b) for b in bounds], vertices=vertices, heat_checks=heat_checks,
                summary=dict(nodes=len(nodes), cells=len(cells), vertices=len(vertices),
                             heat_intervals=len(heat_checks), failures=len(failures), required_failures=0),
                failures=failures, passed=not failures,
                qualification='Independent rational Green inclusion and endpoint enumeration only; L133/L146 heat premises and upstream symbolic/asymptotic lemmas are imported, not independently reverified.')
    OUT.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    print(f'Nodes {len(nodes)}; cells {len(cells)}; vertices {len(vertices)}; failures {len(failures)} (required 0); evidence {OUT}')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
