"""Enclose L132's four full-displacement physical contractions at K=96.

Imports exactly L082's certified moments and positive time/heat rule.
Every new spatial entry uses outward integer Fourier/IBP arithmetic;
every signed tensor term uses L039's qualified IEEE midpoint-radius rules.
No diagnostic spatial or time values are numerical premises.
"""
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import factorial
from pathlib import Path

import numpy as np
import enclose_continuum_first_pair as en

ROOT = Path(__file__).parent
I, S, rat, sr = en.I, en.S, en.rat, en.sr
ZERO, ONE = rat(0), rat(1)
K = 96
NORM = {3: 6050, 6: 1640736}
AMPLITUDE = {'D': 20582100, 'X': 1395445968,
             'A': 20582100, 'C': 280665}


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def fraction(z):
    return F(int(z['numerator']), int(z['denominator']))


def templates():
    """Exact finite tensors from L132, independently matched to its diagnostic."""
    types = lambda a: tuple('E' if j == a else 'V' for j in range(4))
    ordinary = lambda a: tuple((t, 'b') for t in types(a))
    derivative = {'r': 'rp', 'f': 'fp', 'fp': 'fpp'}
    u = {0: [(1, ('f', 'r', 'fp', 'r'))],
         1: [(1, ('r', 'f', 'r', 'fp'))],
         2: [(-1, ('fp', 'r', 'f', 'r'))],
         3: [(-1, ('r', 'fp', 'r', 'f'))]}

    def deriv(terms, axis):
        out = []
        for sign, factors in terms:
            fs = list(factors)
            fs[axis] = derivative[fs[axis]]
            out.append((sign, tuple(fs)))
        return out

    keys, ids = [], {}

    def integral(left, weight, right, ell):
        key = left, weight, right, ell
        if key not in ids:
            ids[key] = len(keys)
            keys.append(key)
        return ids[key]

    def circulation(a, b):
        if a > b:
            return [(c, -s, v) for c, s, v in circulation(b, a)]
        out = []
        for c, j, s in ((b, a, 1), (a, b, -1)):
            fs = list(ordinary(c))
            fs[j] = (types(c)[j], 'd')
            out.append((c, s, tuple(fs)))
        return out

    def lift(a):
        fs = list(ordinary(0))
        fs[0], fs[a] = ('E', 'prefix'), ('V', 'd')
        return [(a, 1, ordinary(a)), (0, -1, tuple(fs))]

    def add(rows, left, right, coeffs, scale=F(1), ell=False):
        for sign, weights in coeffs:
            for a, sl, ll in left:
                for b, ss, rr in right:
                    mm = [integral(l, w, r, ell and j == 0)
                          for j, (l, w, r) in enumerate(zip(ll, weights, rr))]
                    rows.append((a, b, scale * sign * sl * ss, mm))

    w = {a: deriv(u[a], a) for a in range(4)}
    Q = {3: [], 6: []}
    M = {name: [] for name in AMPLITUDE}
    for a, b in combinations(range(4), 2):
        curl = circulation(a, b)
        add(Q[3], curl, curl, w[a] + w[b])
        shear = deriv(u[b], a) + deriv(u[a], b)
        for c in range(4):
            if c in (a, b):
                continue
            left, right = circulation(a, c), circulation(b, c)
            add(Q[6], left, right, shear, F(1, 2))
            add(Q[6], right, left, shear, F(1, 2))
    div_t = sum((w[a] for a in (1, 2, 3)), [])
    for a in (1, 2, 3):
        add(M['D'], lift(a), lift(a), div_t, ell=True)
        add(M['A'], lift(a), lift(a), w[a], ell=True)
        for b in (1, 2, 3):
            du = deriv(u[a], b)
            add(M['X'], lift(a), lift(b), du, ell=True)
            add(M['X'], lift(b), lift(a), du, ell=True)
            if a != b:
                curl = circulation(a, b)
                add(M['C'], lift(b), curl, u[a], F(1, 2), ell=True)
                add(M['C'], curl, lift(b), u[a], F(1, 2), ell=True)
    return keys, M, Q


class Spatial:
    def __init__(self, source):
        self.pi = en.read(source['pi'])
        self.omega = self.pi / rat(8)
        self.norm0 = en.read(source['zero_norm'])
        self.moments = {(r['h'], r['n']): (en.read(r['real']), en.read(r['imag']))
                        for r in source['moments']}
        assert len(self.moments) == len(source['moments']) == 1156
        expected = {(h, n) for h in (0, 1) for n in range(-192, 193)}
        expected |= {(h, n) for h in (2, 3) for n in range(-96, 97)}
        assert set(self.moments) == expected
        self.used = set()
        self.added_moments = []

    def extend_h2(self, saved):
        """L082(3) applies through |n|<=192; only its saved nodes are used."""
        nodes = [(en.read(z['x']), en.read(z['weight'])*en.read(z['rho']))
                 for panel in saved['positive_panels'] for z in panel['nodes']]
        assert len(nodes) == 288
        eps = F(348, 10**16)
        dt, dc = F(2*3**36, 3*4**84), F(2*3**179, 3*4**284)
        allowance = 2*3**2*(eps+(1+eps)*dt)+10*F(5, 2)**2*dc
        assert allowance < F(63, 10**14)
        er = rat(allowance).hi
        for n in range(97, 193):
            total = ZERO
            for x, wr in nodes:
                _, cosine = en.sw.sin_cos(rat(n)*self.omega*x)
                total = total+rat(2)*wr*x*x*cosine
            real = I(total.lo-er, total.hi+er)
            for signed in (n, -n):
                assert (2, signed) not in self.moments
                self.moments[2, signed] = real, ZERO
                self.added_moments.append(dict(h=2, n=signed, real=en.rec(real), imag=en.rec(ZERO)))
            if n % 24 == 0:
                print(f'Enclosed additional degree-2 moments through {n}/192', flush=True)
        return allowance

    @staticmethod
    def nonzero(z):
        return any(t.lo != 0 or t.hi != 0 for t in z)

    @staticmethod
    def add(z, w):
        return z[0] + w[0], z[1] + w[1]

    @staticmethod
    def multiply(z, w):
        return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]

    def insert(self, out, key, value):
        if self.nonzero(value):
            out[key] = self.add(out.get(key, (ZERO, ZERO)), value)

    @lru_cache(None)
    def basis(self, typ, kind, n):
        freq = self.omega * rat(n)
        if n == 0:
            assert typ == 'E'
            if kind == 'b':
                return {(0, 0): (self.norm0, ZERO)}
            if kind == 'd':
                return {}
            assert kind == 'prefix'
            return {(0, 0): (rat(4)*self.norm0, ZERO),
                    (0, 1): (self.norm0, ZERO)}
        sine = (typ == 'V' and kind == 'b') or (typ == 'E' and kind in ('d', 'prefix'))
        amp = rat(F(1, 2))
        if kind == 'd':
            amp = amp*freq*(rat(-1) if typ == 'E' else ONE)
        if kind == 'prefix':
            assert typ == 'E'
            amp = amp/freq
        out = {}
        for sign in (-1, 1):
            phase = ((1, 0), (0, 1), (-1, 0), (0, -1))[(sign*n) % 4]
            z = (ZERO, -rat(F(sign, 2))*amp) if sine else (amp/rat(2), ZERO)
            out[sign*n, 0] = self.multiply(z, (rat(phase[0]), rat(phase[1])))
        return out

    def product(self, left, right):
        out = {}
        for (n, h), z in left.items():
            for (m, j), w in right.items():
                self.insert(out, (n+m, h+j), self.multiply(z, w))
        return out

    def derivative(self, poly):
        out = {}
        for (n, h), z in poly.items():
            self.insert(out, (n, h), self.multiply(z, (ZERO, self.omega*rat(n))))
            if h:
                self.insert(out, (n, h-1), self.multiply(z, (rat(h), ZERO)))
        return out

    def entry(self, left, weight, right, ell, n, m):
        poly = self.product(self.basis(*left, n), self.basis(*right, m))
        if ell:
            poly = self.product(poly, {(0, 0): (rat(4), ZERO), (0, 1): (ONE, ZERO)})
        base, count = {'r': (0, 0), 'f': (1, 0), 'rp': (0, 1),
                       'fp': (1, 1), 'fpp': (1, 2)}[weight]
        # IBP differentiates the WHOLE product, including ell and prefixes.
        for _ in range(count):
            poly = self.derivative(poly)
        value = (ZERO, ZERO)
        for (freq, h), z in poly.items():
            if not self.nonzero(z):
                continue
            key = h+base, freq
            assert key in self.moments, ('uncovered moment', key, left, weight, right, ell, n, m)
            self.used.add(key)
            value = self.add(value, self.multiply(z, self.moments[key]))
        if count % 2:
            value = (-value[0], -value[1])
        assert value[1].lo <= 0 <= value[1].hi
        return value[0]


def main():
    input_path = ROOT/'continuum-first-pair-enclosure-certificate.json'
    source = json.loads(input_path.read_text())
    old_archive = ROOT/source['factor_archive']
    assert source['factor_archive_sha256'] == sha(old_archive)
    assert source['script_sha256'] == sha(Path(en.__file__))
    assert source['input_sha256'] == sha(ROOT/'stored-fourier-enclosure-certificate.json')
    assert (source['K'], source['degree'], int(source['scale'])) == (96, 28, S)
    assert not source['failures']
    spatial = Spatial(source)
    saved = json.loads((ROOT/'stored-fourier-enclosure-certificate.json').read_text())
    new_moment_allowance = spatial.extend_h2(saved)
    keys, M, Q = templates()
    # Algebraic equality to L132's retained diagnostic, never importing its values.
    template_path = ROOT/'physical-h-K96-s144-t24-certificate.json'
    diagnostic = json.loads(template_path.read_text())
    assert json.loads(json.dumps(keys)) == diagnostic['matrix_keys']
    for name, rows in M.items():
        assert [(a, b, F(c), mm) for a, b, c, mm in diagnostic['tensors']['M'][name]] == rows
    for i, rows in Q.items():
        assert [(a, b, F(c), mm) for a, b, c, mm in diagnostic['tensors']['Q'][str(i)]] == rows

    matrices, archive, matrix_records = [], {}, []
    indices = {'E': range(K+1), 'V': range(1, K+1)}
    for ix, (left, weight, right, ell) in enumerate(keys):
        raw = [[spatial.entry(left, weight, right, ell, n, m)
                for m in indices[right[0]]] for n in indices[left[0]]]
        z = en.enclosed(raw)
        matrices.append(z)
        archive[f'spatial_{ix}_c'], archive[f'spatial_{ix}_r'] = z
        matrix_records.append(dict(key=keys[ix], rows=len(raw), cols=len(raw[0]),
                                   max_radius_hex=float(np.max(z[1])).hex()))
        print(f'Enclosed spatial matrix {ix+1}/{len(keys)}; entries {z[0].size}; max radius {np.max(z[1]):.6g}', flush=True)

    imported = np.load(old_archive)
    he = imported['heat_c'], imported['heat_r']
    weights = imported['weights_c'], imported['weights_r']
    assert he[0].shape == he[1].shape == (644, 97)
    assert weights[0].shape == weights[1].shape == (644,)
    archive.update({name: imported[name] for name in ('heat_c', 'heat_r', 'weights_c', 'weights_r')})
    heat = {'E': he, 'V': (he[0][:, 1:], he[1][:, 1:])}
    types = lambda a: tuple('E' if j == a else 'V' for j in range(4))
    cache, feature_records = {}, []

    def feature(mid, qid, ta, tb):
        key = mid, qid, ta, tb
        if key not in cache:
            prod = sr.multiply(matrices[mid], en.trans(matrices[qid]))
            value = sr.dot(sr.dot(heat[ta], prod), en.trans(heat[tb]))
            cache[key] = value
            feature_records.append(dict(M_matrix=mid, Q_matrix=qid, left_type=ta, right_type=tb))
        return cache[key]

    def integrate(z):
        total = en.exact(0.)
        for a in range(0, 644, 160):
            for b in range(0, 644, 160):
                aa, bb = min(a+160, 644), min(b+160, 644)
                block = z[0][a:aa, b:bb], z[1][a:aa, b:bb]
                wa = weights[0][a:aa], weights[1][a:aa]
                wb = weights[0][b:bb], weights[1][b:bb]
                total = sr.add(total, sr.dot(sr.dot(wa, block), wb))
        return total

    m = 28
    rq = F(factorial(m)**4, (2*m+1)*factorial(2*m)**3)*(1+22*factorial(2*m+1))
    assert rq == fraction(source['relative_quadrature_error'])
    rt = fraction(source['relative_time_tail'])
    assert rt == en.ar.exp_negative(rat(108)).absolute_upper()
    rel = rq+rt
    common_tail = 2*(4*12**4)*(16*12**3)*F(512, 9*96)/20**27
    records, results = [], []
    for i in (3, 6):
        for name, rows in M.items():
            total = en.exact(0.)
            count = 0
            for im, (a, b, cm, mm) in enumerate(rows):
                for iq, (qa, qb, cq, qq) in enumerate(Q[i]):
                    if (qa, qb) != (b, a):
                        continue
                    value = en.exact(np.ones((644, 644)))
                    for j, (mid, qid) in enumerate(zip(mm, qq)):
                        value = sr.multiply(value, feature(mid, qid, types(a)[j], types(b)[j]))
                    term = integrate(sr.multiply(value, en.enclosed(rat(cm*cq))))
                    total = sr.add(total, term)
                    count += 1
                    records.append(dict(probe=i, tensor=name, M=im, Q=iq,
                                        coefficient=str(cm*cq), integral=en.pair(term)))
            c, r = F(float(total[0])), F(float(total[1]))
            te = AMPLITUDE[name]*NORM[i]*(4*12**4)**2*(2*rel+rel*rel)
            tail = AMPLITUDE[name]*NORM[i]*common_tail
            error = r+te+tail
            results.append(dict(probe=i, tensor=name, terms=count, retained=en.pair(total),
                                time_error=en.rational(te), spectral_tail=en.rational(tail),
                                total_error=en.rational(error), lower=en.rational(c-error),
                                upper=en.rational(c+error), error_below_one=error < 1))
            print(f'Probe {i} {name}: center {float(c):.12g}; spatial/arithmetic {float(r):.6g}; time {float(te):.6g}; tail {float(tail):.6g}; total error {float(error):.6g}, required <1', flush=True)

    # Combine exact interval endpoints with L132(3), retaining all signs.
    scalar_bounds = {'D': (F(207,1000), F(31,100)),
                     'X': (F(19,200), F(979,6000)),
                     'A': (F(-7,20), F(-1,4)),
                     'C': (F(3,100), F(3,80))}
    combined = []
    for i in (3, 6):
        lo = hi = F(0)
        for row in results:
            if row['probe'] != i:
                continue
            ll, hh = fraction(row['lower']), fraction(row['upper'])
            sl, sh = scalar_bounds[row['tensor']]
            ends = [ll*sl, ll*sh, hh*sl, hh*sh]
            lo += min(ends)
            hi += max(ends)
        combined.append(dict(probe=i, lower=en.rational(lo), upper=en.rational(hi),
                             sign='positive' if lo > 0 else ('negative' if hi < 0 else 'unresolved')))
        print(f'Full transverse-H coefficient {i}: [{float(lo):.12g}, {float(hi):.12g}]; sign {combined[-1]["sign"]}', flush=True)

    factor_path = ROOT/'physical-h-enclosure-factors.npz'
    np.savez_compressed(factor_path, **archive)
    expected_counts = {(3,'D'):144, (3,'X'):240, (3,'A'):48, (3,'C'):144,
                       (6,'D'):432, (6,'X'):864, (6,'A'):144, (6,'C'):576}
    assert Counter((r['probe'], r['tensor']) for r in records) == expected_counts
    assert len(records) == 2592 and len(keys) == 30
    failures = [f'probe {r["probe"]} {r["tensor"]}: total error >=1'
                for r in results if not r['error_below_one']]
    out = dict(K=K, scale=str(S), moment_source=input_path.name, moment_source_sha256=sha(input_path),
               imported_factor_sha256=sha(old_archive), template_source=template_path.name,
               template_source_sha256=sha(template_path),
               script_sha256=sha(Path(__file__)),
               added_moments=spatial.added_moments,
               added_moment_quadrature_error=en.rational(new_moment_allowance),
               used_moments=[list(key) for key in sorted(spatial.used)],
               spatial_matrices=matrix_records, coordinate_features=feature_records,
               tensors={label: [[a,b,str(c),mm] for a,b,c,mm in rows]
                        for label,rows in [(f'M_{s}',rows) for s,rows in M.items()]
                        + [(f'Q_{i}',rows) for i,rows in Q.items()]},
               tensor_terms=records, results=results, combined=combined,
               relative_time_error=en.rational(rel), failures=failures,
               factor_archive=factor_path.name, factor_archive_sha256=sha(factor_path),
               arithmetic_model='L039 IEEE addition/product/FMA, no overflow; underflow allowance 1e-290',
               qualifications=['Imports precisely L082 certified moments and time/heat inputs.',
                               'New matrix/tensor inclusion relies on outward integer and qualified IEEE induction.',
                               'Full transverse-H only; E,ax,-Q,G,R and the complete comparison remain unevaluated.'])
    path = ROOT/'physical-h-enclosure-certificate.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Failures {len(failures)}; full certificate {path}; factors {factor_path}', flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
