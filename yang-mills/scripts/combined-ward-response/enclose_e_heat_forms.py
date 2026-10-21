"""Enclose L134 U_i,W_i with L136 cumulative moments and L082 time rule.
Full retained spatial and signed tensor inclusion under L039 IEEE model.
"""
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
from math import factorial
from pathlib import Path
import numpy as np
import enclose_physical_h_contractions as ph
import enclose_e_cumulative_moments as em

en, I, S, rat, sr = ph.en, ph.I, ph.S, ph.rat, ph.sr
ZERO, ONE = rat(0), rat(1)
ROOT = Path(__file__).parent
K = 96
NORM = {3: 6050, 6: 1640736}
AMPLITUDE = {'U': 160380, 'W': 13783770}
sha, fraction = ph.sha, ph.fraction

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
    for a in (1, 2, 3):
        add(M['U'], lift(a), lift(a), u[0])
        cumulative = {1: [(1, ('R','fp','r','fp'))],
                      2: [(-1, ('f','r','fp','r'))],
                      3: [(-1, ('R','fp','r','fp'))]}
        add(M['W'], lift(a), lift(a), cumulative[a])
    return keys, M, Q

class Spatial(ph.Spatial):
    def __init__(self, source):
        super().__init__(source)
        path = ROOT/'e-cumulative-moments-certificate.json'
        cumulative = json.loads(path.read_text())
        assert cumulative['source_sha256'] == sha(ROOT/'continuum-first-pair-enclosure-certificate.json')
        replay, values, _, _, _ = em.generate(source)
        assert cumulative == replay and not cumulative['failures']
        self.cumulative = values
        self.used_cumulative = set()

    def entry(self, left, weight, right, ell, n, m):
        if weight != 'R':
            return super().entry(left, weight, right, ell, n, m)
        assert not ell
        poly = self.product(self.basis(*left,n), self.basis(*right,m))
        value = (ZERO,ZERO)
        for (freq,h), z in poly.items():
            if not self.nonzero(z):
                continue
            key = h,freq
            assert key in self.cumulative, ('uncovered R moment',key,left,right,n,m)
            self.used_cumulative.add(key)
            value = self.add(value,self.multiply(z,self.cumulative[key]))
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
    keys, M, Q = templates()
    # Q is unchanged; compare every coefficient and spatial key to L133.
    template_path = ROOT/'physical-h-enclosure-certificate.json'
    diagnostic = json.loads(template_path.read_text())
    old_keys = [row['key'] for row in diagnostic['spatial_matrices']]
    for i, rows in Q.items():
        actual = [[a,b,str(c),[json.loads(json.dumps(keys[x])) for x in mm]] for a,b,c,mm in rows]
        expected = [[a,b,c,[old_keys[x] for x in mm]] for a,b,c,mm in diagnostic['tensors'][f'Q_{i}']]
        assert actual == expected

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

    # Combine exact interval endpoints with L135(1), retaining all signs.
    scalar_bounds = {'U': (F(-903,1000), F(-871,1000)),
                     'W': (F(-178,1000), F(-143,1000))}
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
        print(f'Full E coefficient {i}: [{float(lo):.12g}, {float(hi):.12g}]; sign {combined[-1]["sign"]}', flush=True)

    factor_path = ROOT/'e-heat-enclosure-factors.npz'
    np.savez_compressed(factor_path, **archive)
    expected_counts = {(3,'U'):48, (3,'W'):48, (6,'U'):144, (6,'W'):144}
    assert Counter((r['probe'],r['tensor']) for r in records) == expected_counts
    assert len(records) == 384
    failures = [f'probe {r["probe"]} {r["tensor"]}: total error >=1'
                for r in results if not r['error_below_one']]
    out = dict(K=K, scale=str(S), moment_source=input_path.name, moment_source_sha256=sha(input_path),
               imported_factor_sha256=sha(old_archive), template_source=template_path.name,
               template_source_sha256=sha(template_path),
               script_sha256=sha(Path(__file__)),
               cumulative_source='e-cumulative-moments-certificate.json',
               cumulative_source_sha256=sha(ROOT/'e-cumulative-moments-certificate.json'),
               used_cumulative_moments=[list(key) for key in sorted(spatial.used_cumulative)],
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
                               'E only; ax,-Q,G,R and the full comparison remain unevaluated.'])
    path = ROOT/'e-heat-enclosure-certificate.json'
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Failures {len(failures)}; full certificate {path}; factors {factor_path}', flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
