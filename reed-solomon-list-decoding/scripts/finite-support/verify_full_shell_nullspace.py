"""Independent exact substitution of the canonical L059 column.

Uses distance-one recurrence, not the constructor's Gram-Schmidt/elimination.
Writes all 36 projections, entries, spectra and full relevant comparisons.
"""
import hashlib
import json
import re
from fractions import Fraction as F
from math import comb
from pathlib import Path

ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT / 'full-shell-nullspace-verification.json'


def enc(x):
    x = F(x)
    return [x.numerator, x.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    failures, checks = [], []

    def check(name, ok):
        checks.append(name)
        if not ok:
            failures.append(name)

    shell_path = NB / 'lemmas/L056-released-zero-five-shell-nonexclusion.md'
    column_path = NB / 'lemmas/L059-full-shell-nullspace-compatible-column.md'
    pattern = r'^\| \((\d),(\d)\) \| ([0-9/]+) \|$'
    z = {(int(r), int(q)): F(v) for r, q, v in re.findall(pattern, shell_path.read_text(), re.M)}
    t = {(int(i), int(j)): F(v) for i, j, v in re.findall(pattern, column_path.read_text(), re.M)}
    check('manuscript_free_domain', set(t) == {(i, j) for i in range(6)
                                                 for j in range(6) if i+j <= 5})
    d = {(r, q): val / (choose(5, r)*choose(63, r)*choose(5, q)*choose(951, q))
         for (r, q), val in z.items()}
    for i in range(6):
        for j in range(6):
            if i+j == 6:
                t[i, j] = d[6-i, i]
            elif i+j > 6:
                t[i, j] = F(0)
            check(f'nonnegative_{i}_{j}', t[i, j] >= 0)
    p5, p6 = F(1, 68881143660), F(133, 9357995374380)
    pairs = json.loads((ROOT / 'selected-triple-sdp-results.json').read_text())['p']
    check('fixed_positive_pairs', F(*pairs[5]) == p5 > 0 and F(*pairs[6]) == p6 > 0)

    def E(n, a, r):
        return sum((-1)**s*choose(a, s)*choose(5-a, r-s)*choose(n-5-a, r-s)
                   for s in range(r+1))

    def recurrence(n):
        weights = [choose(6, i)*choose(n-6, 5-i) for i in range(6)]
        all_vectors = []
        for a in range(6):
            theta = E(n, a, 1)
            v = [F(1)]
            for i in range(5):
                down, up = i*(n-11+i), (5-i)*(6-i)
                stay = 5*(n-5)-down-up
                v.append(((theta-stay)*v[i]-(down*v[i-1] if i else 0))/up)
            for i in range(6):
                down, up = i*(n-11+i), (5-i)*(6-i)
                stay = 5*(n-5)-down-up
                check(f'recurrence_{n}_{a}_{i}', stay*v[i]
                      +(down*v[i-1] if i else 0)+(up*v[i+1] if i < 5 else 0)
                      == theta*v[i])
            all_vectors.append(v)
        for a in range(6):
            check(f'basis_norm_{n}_{a}', sum(weights[i]*all_vectors[a][i]**2
                                             for i in range(6)) > 0)
            for b in range(a):
                check(f'basis_orthogonality_{n}_{a}_{b}', sum(
                    weights[i]*all_vectors[a][i]*all_vectors[b][i] for i in range(6)) == 0)
        return weights, all_vectors

    wh, h = recurrence(68)
    wt, k = recurrence(956)
    data = {'column': [{'i': i, 'j': j, 'value': enc(t[i, j])}
                       for i in range(6) for j in range(6)], 'projections': []}
    zeros = []
    for a in range(6):
        for b in range(6):
            schur = 1+sum(value*E(68, a, r)*E(956, b, q) for (r, q), value in d.items())
            if (a, b) == (0, 0):
                schur -= p5*comb(68, 5)*comb(956, 5)
            projection = sum(wh[i]*wt[j]*h[a][i]*k[b][j]*t[i, j]
                             for i in range(6) for j in range(6))
            shift = sum(wh[i]*wt[j]*h[a][i]*k[b][j]*p6
                        for i in range(6) for j in range(6))
            check(f'schur_psd_{a}_{b}', schur >= 0)
            if schur == 0:
                zeros.append([a, b])
                check(f'full_zero_mode_projection_{a}_{b}', projection == 0)
                check(f'anchor_transport_{a}_{b}', shift == 0)
            data['projections'].append({'a': a, 'b': b, 'schur': enc(schur),
                                        'raw': enc(projection), 'transported': enc(projection-shift)})
    check('all_20_zero_modes', len(zeros) == 20)
    saved = json.loads((ROOT / 'full-shell-nullspace-results.json').read_text())
    check('constructor_zeros', zeros == saved['zero_modes'])
    for coord, value in zip(saved['free'], saved['nonnegative_test']['solution']):
        check(f'constructor_free_{coord}', t[tuple(coord)] == F(*value))
    for item in saved['fixed']:
        check(f'constructor_fixed_{item["i"]}_{item["j"]}',
              t[item['i'], item['j']] == F(*item['value']))
    for rec in saved['orbits']:
        i, j = rec['i'], rec['j']
        check(f'full_atoms_{i}_{j}', rec['atoms'] ==
              [945+j, 6-j, 5-j, j, i, 5-i, 6-i, 57+i])
        check(f'orbit_size_{i}_{j}', rec['multiplicity'] == wh[i]*wt[j])
    for n, vec in [(68, h), (956, k)]:
        old = saved['head' if n == 68 else 'tail']['vectors']
        for a in range(6):
            oldvec = [F(*v) for v in old[a]]
            check(f'independent_basis_{n}_{a}', all(oldvec[i] == oldvec[0]*vec[a][i]
                                                     for i in range(6)))
    lo = F(3826948593076525737749263, 221908927759242896073805386355372500)
    hi = F(689512027427211313039687769, 826754522994296083897677764417880000)
    check('interval_nonempty', 0 < lo < hi)
    check('selected_endpoint', t[2, 3] == lo and t[0, 3] == 0)
    data.update({'zero_modes': zeros, 'head_vectors': [list(map(enc, v)) for v in h],
                 'tail_vectors': [list(map(enc, v)) for v in k],
                 'p5': enc(p5), 'p6': enc(p6),
                 'checks': len(checks), 'failures': failures,
                 'source_hashes': {str(path.relative_to(NB)): hashlib.sha256(path.read_bytes()).hexdigest()
                                   for path in [shell_path, column_path]}})
    OUT.write_text(json.dumps(data, indent=2)+'\n')
    print(f'column=36/36 nonnegative entries; zero projections={len(zeros)}/20; '
          f'checks={len(checks)}; failures={failures}')
    print(f'certificate={OUT.relative_to(NB)}; scalar energy inequality NOT TESTED')
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
