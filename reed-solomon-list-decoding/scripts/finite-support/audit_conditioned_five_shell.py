"""Independent set-union/Schrijver-beta reconstruction of the full shell."""
import hashlib
import json
from fractions import Fraction as Q
from math import factorial
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / 'conditioned-five-shell-results.json'
OUT = ROOT / 'conditioned-five-shell-audit-results.json'


def choose(n, k):
    return factorial(n)//factorial(k)//factorial(n-k) if 0 <= k <= n else 0


def enc(x):
    return [x.numerator, x.denominator]


def beta_eigen(n, k, r):
    # foundations/04 (53)-(58), on the single weight-five layer.
    t = 5-r
    beta = sum((-1)**(u-t)*choose(u, t)*choose(n-2*k, u-k)
               *choose(n-k-u, 5-u)**2 for u in range(max(k, t), 6))
    return Q(beta, choose(n-2*k, 5-k))


def main():
    raw = SOURCE.read_bytes()
    saved = json.loads(raw)
    lp = json.loads((ROOT/'delsarte-lp-results.json').read_text())
    primal = [Q(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    p = [Q(1)] + [Q(0)]*4 + [z/(2*choose(68, i)*choose(956, i))
                              for i, z in zip(range(5, 69), primal)]
    failures, counts = [], {}

    def check(kind, truth, detail=None):
        counts[kind] = counts.get(kind, 0)+1
        if not truth:
            failures.append({'kind': kind, 'detail': detail})

    check('pairs', saved['parameters']['p'] == list(map(enc, p))
          == json.loads((ROOT/'selected-triple-sdp-results.json').read_text())['p'])
    # The full-rank L021 defining system identifies the unchanged input.
    for j in range(1, 65):
        pol = [0]*69
        for r in range(69-j):
            for h in range(j+1):
                pol[r+h] += (-1)**h*choose(j, h)*choose(68-j, r)*choose(956-j, r)
        check('L021_defining_equations', 1+sum(Q(pol[i], choose(68, i)*choose(956, i))
                                             *primal[i-5] for i in range(5, 69)) == 0, j)
    U = Q(choose(1024, 64), choose(68, 64))
    M = (U+1)/2
    tau = Q(65537**28, 2**128)
    T = tau.__floor__()+1
    rho = M/choose(1024, 68)
    alpha = p[5]**2/p[68]
    check('positive_normalization', rho > 0 and alpha > 0 and p[5] > 0)
    check('parameters', saved['parameters'] == {
        'n': 1024, 'w': 68, 'tail': 956, 'shell_distance': 5, 'p': list(map(enc, p)),
        'alpha': enc(alpha), 'size': choose(68, 5)*choose(956, 5),
        'anchor_over_rho': [1, 1], 'anchor_shell_over_rho': enc(p[5])})
    check('objective', M.__floor__() >= T and Q(1383, 1000) < M/tau < Q(1384, 1000))
    A = frozenset(range(68))
    X = frozenset(range(5))
    Y = frozenset(range(68, 73))
    B = (A-X) | Y
    entries, dictionaries = [], []
    for r in range(6):
        row = []
        for q in range(6):
            X2 = frozenset(range(5-r)) | frozenset(range(5, 5+r))
            Y2 = frozenset(range(68, 73-q)) | frozenset(range(73, 73+q))
            C = (A-X2) | Y2
            support_family = {A, B, C}
            distances = [len(A-B), len(A-C), len(B-C)]
            common = A & B & C
            pair_only = [(A & B)-C, (A & C)-B, (B & C)-A]
            private = [A-(B|C), B-(A|C), C-(A|B)]
            incidence = (len(common) == 61 and all(len(z) == 2 for z in pair_only)
                         and all(len(z) == 3 for z in private))
            if len(support_family) == 2:
                value = p[len(A-B)]
            elif min(distances) < 5 or incidence:
                value = Q(0)
            else:
                value = Q(1, p[68])
                for d in distances:
                    value *= p[d]
            t, s = len((A-B) & (A-C)), len((B-A) & (C-A))
            check('set_dictionary', len(B) == len(C) == 68 and distances == [5, 5, r+q]
                  and (t, s) == (5-r, 5-q) and incidence == ((r, q) == (2, 3)), [r, q])
            check('boolean_union_entries', saved['coefficient_table_over_rho'][r][q] == enc(value)
                  and saved['coefficient_table_scaled'][r][q] == enc(value/alpha), [r, q])
            dictionaries.append({'r': r, 'q': q, 'distances': distances, 't': t, 's': s,
                                 'family_size': len(support_family), 'incidence': incidence,
                                 'entry_over_rho': enc(value)})
            row.append(value)
        entries.append(row)
    spectra = {}
    multiplicities = {}
    for index, n in enumerate((68, 956)):
        E = [[beta_eigen(n, k, r) for r in range(6)] for k in range(6)]
        m = [choose(n, k)-choose(n, k-1) for k in range(6)]
        for k in range(6):
            for r in range(6):
                check('independent_beta_normalization', E[k][r].denominator == 1
                      and E[k][r] == saved['factors'][index]['eigenmatrix'][k][r], [n, k, r])
        check('factor_multiplicities', m == saved['factors'][index]['multiplicities']
              and sum(m) == choose(n, 5) and all(z > 0 for z in m), n)
        check('identity_and_valency', all(E[k][0] == 1 for k in range(6))
              and E[0] == [choose(5, r)*choose(n-5, r) for r in range(6)], n)
        # Complete eigenmatrix orthogonality verifies relation normalization.
        for r in range(6):
            for s in range(6):
                lhs = sum(m[k]*E[k][r]*E[k][s] for k in range(6))
                rhs = choose(n, 5)*E[0][r] if r == s else 0
                check('factor_trace_orthogonality', lhs == rhs, [n, r, s])
        spectra[n], multiplicities[n] = E, m
    size = choose(68, 5)*choose(956, 5)
    modes, negatives = [], []
    for a in range(6):
        for b in range(6):
            eigen = sum(entries[r][q]*spectra[68][a][r]*spectra[956][b][q]
                        for r in range(6) for q in range(6))
            correction = size*p[5]**2 if a == b == 0 else Q(0)
            z = {'a': a, 'b': b, 'multiplicity': multiplicities[68][a]*multiplicities[956][b],
                 'shell_over_rho': enc(eigen), 'shell_scaled': enc(eigen/alpha),
                 'anchor_correction_over_rho': enc(correction),
                 'schur_over_rho': enc(eigen-correction),
                 'schur_scaled': enc((eigen-correction)/alpha)}
            check('every_mode', saved['modes'][6*a+b] == z, [a, b])
            modes.append(z)
            if eigen-correction < 0:
                negatives.append([a, b])
    check('mode_completeness', len(saved['modes']) == 36 and sum(z['multiplicity'] for z in modes) == size)
    check('shell_trace', sum(Q(*z['shell_over_rho'])*z['multiplicity'] for z in modes) == size*p[5])
    check('schur_trace', sum(Q(*z['schur_over_rho'])*z['multiplicity'] for z in modes) == size*(p[5]-p[5]**2))
    check('summary', saved['summary'] == {'mode_count': 36, 'dimension_sum': size,
          'negative_modes': negatives, 'anchored_psd': not negatives,
          'verdict': 'FIXED_TRIAL_EXCLUDED' if negatives else 'SHELL_PASSES'} and saved['failures'] == [])
    report = {'source_sha256': hashlib.sha256(raw).hexdigest(), 'counts': counts,
              'checks': sum(counts.values()), 'failures': failures,
              'dictionary': dictionaries, 'modes': modes,
              'normalization': {'rho': enc(rho), 'alpha': enc(alpha), 'objective': enc(M),
                                'threshold': enc(tau), 'T': T, 'size': size},
              'negative_modes': negatives, 'verified': not failures}
    OUT.write_text(json.dumps(report, separators=(',', ':'))+'\n')
    print('Independent checks:', report['checks'], '; failures:', len(failures))
    print('Actual/required modes: 36/36; complete dimension:', size)
    print('Negative exact Schur coordinates:', negatives, '; required: all nonnegative')
    print('Unchanged objective floor >= T:', M.__floor__() >= T, '; T:', T)
    print('Certificate:', OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
