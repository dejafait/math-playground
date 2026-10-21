"""Full two-angle Green inclusion and L153 actual-probe recombination.

All mathematical arithmetic uses integers/Fraction/isqrt. --audit replays
every cell. Imported full heat intervals retain L133/L146's IEEE premise.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from check_joint_curl_tensor import I, SCALE, atan_bounds, cosine

ROOT = Path(__file__).parent
CERT = ROOT/'quartic-residual-coefficient-certificate.json'
AUDIT = ROOT/'quartic-residual-coefficient-audit.json'
N = 256
HEAT = {
    3: [('2359.1', '2359.2'), ('19170.0', '19170.1'),
        ('29198.8', '29198.9'), ('1024.8', '1024.9'),
        ('1228.1260684', '1228.1260686')],
    6: [('703.6', '703.7'), ('-4195.9', '-4195.8'),
        ('69177.0', '69177.1'), ('3218.2', '3218.3'),
        ('451.5469823', '451.5469825')],
}
# Column order P_D, P_A, P_X, P_C, B_R; rows constant, X, Y.
COEFFICIENTS = [list(map(F, row)) for row in (
    ('-17/2', '5', '3/4', '-6', '14'),
    ('45', '-39', '-3', '30', '-72'),
    ('-15/2', '9/2', '-3/2', '15', '6'))]
READABLE = {3: (F(-49200), F(-43073)), 6: (F(20982), F(21570))}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def inputs():
    al, au = atan_bounds(5, 60)
    bl, bu = atan_bounds(239, 20)
    pl, ph = 16*al-4*bu, 16*au-4*bl
    assert F(3) < pl <= ph < F(22, 7)
    pi = I(I.rat(pl).lo, I.rat(ph).hi)
    nodes = []
    for j in range(N+1):
        theta = pi*I.rat(F(j, N))
        co = cosine(theta)
        x = I.rat(2)-I.rat(2)*co
        x = I(max(0, x.lo), min(4*SCALE, x.hi))
        if j == 0:
            x = I(0)
        if j == N:
            x = I(4*SCALE)
        nodes.append(dict(index=j, theta=theta.data(), cosine=co.data(), x=x.data()))
    return dict(lower=str(pl), upper=str(ph), interval=pi.data()), nodes


def cell_values(x, y, corner):
    one, two, four = map(I.rat, (1, 2, 4))
    k = x+y
    # Averaging 1/(k+2-2cos(theta_3)) gives 1/sqrt(k(k+4)).
    if corner:
        xv = I(0, (k.sqrt()/four).hi)
    else:
        assert k.lo > 0
        numerator = k/two-x*y/four
        assert numerator.hi >= 0
        numerator = I(max(0, numerator.lo), numerator.hi)
        xv = numerator/(k*(k+four)).sqrt()
    # This expression is continuous even at k=0; no corner omission.
    yv = (one-x/two)*(one-y/two)*(one-(k/(k+four)).sqrt())/two
    return xv, yv


def records(nodes):
    xs = [I(*map(int, r['x'])) for r in nodes]
    ranges = [I(xs[j].lo, xs[j+1].hi) for j in range(N)]
    for j, x in enumerate(ranges):
        for m, y in enumerate(ranges):
            values = cell_values(x, y, j == m == 0)
            yield [j, m, *[v.data() for v in values]], values


def recombine(bounds):
    xlo, xhi = map(F, (bounds[0]['lower'], bounds[0]['upper']))
    ylo, yhi = map(F, (bounds[1]['lower'], bounds[1]['upper']))
    results = []
    for i, heat in HEAT.items():
        corners = []
        for x in (xlo, xhi):
            for y in (ylo, yhi):
                coefficients = [a+x*b+y*c for a,b,c in zip(*COEFFICIENTS)]
                products = [[coeff*F(end) for end in ends]
                            for coeff, ends in zip(coefficients, heat)]
                lo = sum(map(min, products), F(0))
                hi = sum(map(max, products), F(0))
                corners.append(dict(X=str(x), Y=str(y), coefficients=list(map(str, coefficients)),
                                    lower=str(lo), upper=str(hi)))
        lo = min(F(r['lower']) for r in corners)
        hi = max(F(r['upper']) for r in corners)
        results.append(dict(probe=i, heat_bounds=heat, corners=corners,
                            lower=str(lo), upper=str(hi),
                            sign='negative' if hi<0 else ('positive' if lo>0 else 'unresolved')))
    return results


def coefficient_check():
    # L153's ordered A,B,C,D,E,F, each constant + X term + Y term.
    old = [list(map(F, row)) for row in (
        ('-8','60','-6'), ('10','-42','3'), ('-4','60','6'),
        ('3','0','24'), ('9/2','-24','-12'), ('-3/2','6','3'))]
    transform = [list(map(F, row)) for row in (
        ('1/2','0','0','0','-1/2'), ('0','0','0','0','1'),
        ('0','-1/2','0','0','0'), ('-1/2','1/2','0','0','0'),
        ('-1/2','1/2','0','-1','0'), ('1/2','1/2','-1/2','1','0'))]
    actual = [[sum((old[k][r]*transform[k][c] for k in range(6)), F(0))
               for c in range(5)] for r in range(3)]
    assert actual == COEFFICIENTS
    return dict(L153_rows=[list(map(str, r)) for r in old],
                transform=[list(map(str, r)) for r in transform],
                reconstructed=[list(map(str, r)) for r in actual], passed=True)


def main(audit):
    pi, nodes = inputs()
    algebra = coefficient_check()
    paths = [Path(__file__), ROOT/'check_joint_curl_tensor.py',
             ROOT.parent.parent/'lemmas/L133-other-other-actual-physical-heat-enclosures.md',
             ROOT.parent.parent/'lemmas/L146-other-other-r-physical-heat-enclosures.md',
             ROOT/'physical-h-enclosure-certificate.json',
             ROOT/'r-heat-enclosure-certificate.json', ROOT/'r-heat-endpoint-check.json']
    hashes = {str(p.relative_to(ROOT.parent.parent)): sha(p) for p in paths}
    saved = json.loads(CERT.read_text()) if audit else None
    if audit:
        assert saved['N'] == N and saved['SCALE'] == str(SCALE)
        assert saved['hashes'] == hashes and saved['pi'] == pi and saved['nodes'] == nodes
        assert len(saved['cells']) == N*N
    cells, totals = [], [I(0), I(0)]
    count = 0
    for q, (record, values) in enumerate(records(nodes)):
        if audit:
            assert saved['cells'][q] == record
        else:
            cells.append(record)
        totals = [a+b for a,b in zip(totals, values)]
        count += 1
    assert count == N*N
    bounds = [dict(name=name, lower=str(F(t.lo, N*N*SCALE)),
                   upper=str(F(t.hi, N*N*SCALE)))
              for name,t in zip(('X','Y'), totals)]
    results = recombine(bounds)
    failures = []
    for r in results:
        if r['sign'] == 'unresolved':
            failures.append(f"probe-{r['probe']}-zero-not-excluded")
        lo, hi = READABLE[r['probe']]
        if not lo < F(r['lower']) <= F(r['upper']) < hi:
            failures.append(f"probe-{r['probe']}-readable-endpoints")
        r['readable_strict_bounds'] = [str(lo), str(hi)]
    data = dict(N=N, SCALE=str(SCALE), hashes=hashes, pi=pi, nodes=nodes,
                cells=cells, totals=[t.data() for t in totals], bounds=bounds,
                coefficient_rows=[list(map(str, row)) for row in COEFFICIENTS],
                algebra=algebra, results=results, failures=failures,
                qualification='Complete exact-integer cell inclusion; imported full heat intervals inherit L133/L146 IEEE arithmetic model; no full-response compensation claimed.')
    if audit:
        for key in ('totals', 'bounds', 'coefficient_rows', 'algebra', 'results', 'failures'):
            assert saved[key] == json.loads(json.dumps(data[key])), key
        path = AUDIT
        data = dict(certificate_sha256=sha(CERT), cells_replayed=count, bounds=bounds,
                    results=results, failures=failures, passed=not failures)
    else:
        path = CERT
    path.write_text(json.dumps(data, separators=(',', ':'))+'\n')
    for r in bounds:
        print(f"{r['name']} [{float(F(r['lower'])):.10g}, {float(F(r['upper'])):.10g}]")
    for r in results:
        print(f"Lambda_{r['probe']} [{float(F(r['lower'])):.10g}, {float(F(r['upper'])):.10g}]; {r['sign']}; required: excludes zero")
    print(f'Cells {count}; failures {len(failures)}; complete evidence {path}', flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--audit', action='store_true')
    main(parser.parse_args().audit)
