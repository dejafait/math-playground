"""Exact gate-approved global trial; full minors saved, no full SDP claim."""
import json
import sys
from fractions import Fraction as Q
from itertools import combinations
from math import comb, lcm
from pathlib import Path

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).parent
OUT = ROOT / 'global-triple-principal-results.json'
N, W, V = 1024, 68, 956


def enc(x):
    return [x.numerator, x.denominator]


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def main():
    lp = json.loads((ROOT / 'delsarte-lp-results.json').read_text())
    old = json.loads((ROOT / 'selected-triple-sdp-results.json').read_text())
    p = [Q(1)] + [Q(0)] * 4 + [
        Q(z['numerator'], z['denominator']) / (2*comb(W, i)*comb(V, i))
        for i, z in zip(range(5, 69), lp['exact']['primal'])]
    assert list(map(enc, p)) == old['p'] and p[68] > 0
    val = [comb(W, i)*comb(V, i) for i in range(69)]
    U = Q(comb(N, 64), comb(W, 64))
    objective = (U+1)/2
    universe = comb(N, W)
    rho = objective/universe
    tau = Q(65537**28, 2**128)
    T = tau.numerator//tau.denominator+1
    spectra, failures = [], []
    for j in range(69):
        coeff = [sum((-1)**h*choose(j, h)*choose(W-j, i-h)
                     *choose(V-j, i-h) for h in range(i+1))
                 for i in range(69)]
        z = sum(c*x for c, x in zip(coeff, p))
        spectra.append({'j': j, 'coefficients': coeff, 'eigenvalue_over_rho': enc(z)})
        if z < 0:
            failures.append({'kind': 'pair spectrum', 'j': j, 'value': enc(z)})
    schur = Q(*spectra[0]['eigenvalue_over_rho'])-rho*universe
    assert sum(c*x for c, x in zip(val, p)) == objective
    assert 0 < rho <= 1 and objective >= T and schur == 0
    D = lcm(*(z.denominator for z in p))
    A = [int(z*D) for z in p]
    H = D*D*A[68]
    P = [z*D*A[68] for z in A]  # H*p_i
    assert H > 0
    cache, records, entries = {}, [], []

    def record(distances, changed):
        key = (*sorted(distances), bool(changed))
        if key in cache:
            return cache[key]
        a, b, c, changed = key
        if changed or any(1 <= z <= 4 for z in (a, b, c)):
            Y = 0
        elif a == 0:
            assert b == c
            Y = P[b]
        else:
            Y = A[a]*A[b]*A[c]
        assert Y >= 0
        # Full principal-minor evidence for every possible anchor of this
        # distance multiset. Minors of H times each normalized matrix.
        anchors = []
        for i, j in sorted(set(((a, b), (a, c), (b, c)))):
            if a == 0:
                # Remove duplicate set-indices: one index when all equal,
                # otherwise {A, A union {B}} regardless of repeated position.
                matrix = [[H]] if b == 0 else [[H, P[b]], [P[b], P[b]]]
            else:
                matrix = [[H, P[i], P[j]], [P[i], P[i], Y], [P[j], Y, P[j]]]
            minors = [matrix[r][r] for r in range(len(matrix))]
            minors += [matrix[r][r]*matrix[s][s]-matrix[r][s]**2
                       for r, s in combinations(range(len(matrix)), 2)]
            if len(matrix) == 3:
                minors.append(H*P[i]*P[j]-H*Y*Y-P[i]*P[i]*P[j]
                              -P[j]*P[j]*P[i]+2*P[i]*P[j]*Y)
            anchors.append({'distances_from_anchor': [i, j], 'dimension': len(matrix),
                            'principal_minor_numerators': minors})
            if any(z < 0 for z in minors):
                failures.append({'kind': 'conditioned matrix', 'key': list(key),
                                 'anchor': [i, j], 'matrix_over_rho':
                                 [[enc(Q(x, H)) for x in row] for row in matrix],
                                 'minors': minors})
        index = len(records)
        cache[key] = index
        records.append({'distances': [a, b, c], 'incidence_override': changed,
                        'triple_numerator': Y, 'anchors': anchors})
        return index

    counts = {'ordered_orbits': 0, 'repeated_orbits': 0,
              'pair_forbidden_orbits': 0, 'incidence_zero_orbits': 0}
    for i in range(69):
        for j in range(69):
            tl, th = max(0, i+j-W), min(i, j)
            sl, sh = max(0, i+j-V), min(i, j)
            hl, hh = i+j-th-sh, i+j-tl-sl
            ids = [record((i, j, h), False) for h in range(hl, hh+1)]
            override = None
            for t in range(tl, th+1):
                for s in range(sl, sh+1):
                    h = i+j-t-s
                    # Independent incidence equations, not merely distances.
                    changed = ((W-i-j+t, j-t, i-t, s, t, i-s, j-s)
                               == (61, 2, 2, 2, 3, 3, 3))
                    if changed:
                        assert (i, j, t, s, h) == (5, 5, 3, 2, 5)
                        override = {'t': t, 's': s, 'record': record((i, j, h), True)}
                    counts['ordered_orbits'] += 1
                    counts['repeated_orbits'] += min(i, j, h) == 0
                    counts['pair_forbidden_orbits'] += any(1 <= z <= 4 for z in (i, j, h))
                    counts['incidence_zero_orbits'] += changed
                    if counts['ordered_orbits'] > 2000000:
                        raise RuntimeError('planning cap exceeded; unfinished trial')
            entries.append({'i': i, 'j': j, 't_range': [tl, th], 's_range': [sl, sh],
                            'h_first': hl, 'h_records': ids, 'override': override})
    counts.update({'numerical_records': len(records), 'ordered_entries': len(entries),
                   'retained_matrix_checks': counts['ordered_orbits'],
                   'distinct_numeric_anchor_checks': sum(len(r['anchors']) for r in records),
                   'stored_principal_minors': sum(len(a['principal_minor_numerators'])
                                                for r in records for a in r['anchors'])})
    result = {'parameters': {'n': N, 'w': W, 'd': 10, 'universe': universe,
                            'p': list(map(enc, p)), 'rho': enc(rho), 'U': enc(U),
                            'objective': enc(objective), 'threshold': enc(tau), 'T': T},
              'pair_spectra': spectra, 'constant_schur_over_rho': enc(schur),
              'common_denominators': {'pair': D, 'triple': H, 'pair_numerators': A,
                                      'pair_numerators_over_H': P},
              'entries': entries, 'records': records, 'counts': counts,
              'summary': {'trial_feasible': not failures, 'objective_at_least_T': objective >= T,
                          'batch_insufficient': not failures and objective >= T,
                          'objective_ratio': enc(objective/tau), 'orbit_cap': 2000000},
              'failures': failures}
    with OUT.open('w') as f:
        json.dump(result, f, separators=(',', ':'))
        f.write('\n')
    print('Actual/required ordered orbits:', counts['ordered_orbits'], '/ <=2000000; expected 1500625')
    print('Matrix checks:', counts['retained_matrix_checks'], '; spectral coordinates:', len(spectra), '/ 69')
    print('Exact objective:', objective, '; required sufficient bound <', T)
    print('Incidence overrides:', counts['incidence_zero_orbits'], '; repetitions:', counts['repeated_orbits'])
    print('Failures:', len(failures), '; feasible:', not failures, '; certificate:', OUT)


if __name__ == '__main__':
    main()
