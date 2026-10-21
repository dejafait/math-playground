"""Verify the saved one-pass candidate and its failures, without solving again."""
import hashlib
import itertools as it
import json
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_simultaneous_eight_shell import C, beta, enc

sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent
NB = ROOT.parent.parent
OUT = ROOT/'zero-plane-joint-feasibility-verification.json'


def dot(x, y):
    assert len(x) == len(y)
    return sum((a*b for a, b in zip(x, y)), F(0))


def dec(x):
    return [[F(*v) for v in r] for r in x]


def interval(x):
    k = x.numerator*10**6//x.denominator
    return [F(k, 10**6), F(k+1, 10**6)]


def main():
    names = ['zero-plane-joint-feasibility-results.json',
             'fully-cancelling-separator-family-critical-audit.json',
             'zero-plane-positive-mode-compatibility-results.json',
             'eight-distance-full-base-kernel-results.json']
    paths = [ROOT/n for n in names]
    data, audit, eq, col = [json.loads(p.read_text()) for p in paths]
    checks, failures = [], []

    def check(n, ok):
        checks.append(n)
        if not ok:
            failures.append(n)

    for name, obj in zip(names, [data, audit, eq, col]):
        check('clean_'+name, not obj['failures'])
        for rel, h in obj['input_hashes'].items():
            check('bound_'+name+'_'+rel, hashlib.sha256((NB/rel).read_bytes()).hexdigest() == h)
    r = data['reconstruction']
    point = [F(*v) for v in r['point']]
    z = [F(*v) for v in r['z']]
    h = [F(*v) for v in r['h']]
    free = [(a, b) for a, b in it.product(range(9), repeat=2) if a+b >= 8]
    p8 = F(16792471, 1181138102168120460)
    check('exact_plane', point[0] == 1 and point[4] == F(*eq['stationary_t78']))
    mon = [point[i]*point[j] for i, j in eq['monomials']]
    check('saved_exact_P_plus_Nh', z == [dot(p, mon)+dot(n, h) for p, n in zip(dec(eq['particular_coefficients']), dec(eq['right_kernel']))])
    check('all_nonpivot_coordinates', h == [z[j] for j in eq['nonpivot_columns']])
    family = [[F(*v)]+[F(*x) for x in row] for v, row in zip(col['affine']['intercept'], col['affine']['slopes'])]
    factors = [dot(f, point) for f in family]
    check('all_85_original_factors', len(factors) == 85 and enc(factors) == r['domain_factors'])
    raw = [p8*v/F(C(8, a)*C(60, a)*C(8, b)*C(948, b)) for (a, b), v in zip(free, z)]
    check('all_45_raw_moments', enc(raw) == r['raw_moments'])
    slacks, rawslacks = [], []
    for k, m in enumerate(audit['modes']):
        a, b = divmod(k, 9)
        D = C(68-2*a, 8-a)*C(956-2*b, 8-b)
        cross = [dot(row, point) for row in dec(m['source_cross'])]
        inverse = [dot(row, point) for row in dec(m['inverse_affine'])]
        base = dec(m['source_base'])
        check('original_range_'+str(k), [dot(row, inverse) for row in base] == cross)
        # Recompute fixed, full anchor and range energy separately, without
        # evaluating the constructor's assembled quadratic matrices.
        bound = dot([F(*v) for v in m['forced']], point)-F(*m['anchor'])-dot(cross, inverse)/(p8*D)
        coefficients = [-F(beta(68, 8, 8, a, 8-u)*beta(956, 8, 8, b, 8-v),
                           D*C(8, u)*C(60, u)*C(8, v)*C(948, v)) for u, v in free]
        slack = bound-dot(coefficients, z)
        rawslack = sum((beta(68, 8, 8, a, 8-u)*beta(956, 8, 8, b, 8-v)*y for (u, v), y in zip(free, raw)), F(0))+p8*D*bound
        check('original_bound_'+str(k), enc(bound) == r['bounds'][k])
        check('every_original_mode_'+str(k), enc(slack) == r['mode_slacks'][k])
        check('every_raw_schur_mode_'+str(k), rawslack == p8*D*slack and enc(rawslack) == r['raw_schur_slacks'][k])
        slacks.append(slack)
        rawslacks.append(rawslack)
    negatives = {'domain': [i for i, v in enumerate(factors) if v < 0],
                 'moments': [i for i, v in enumerate(z) if v < 0],
                 'modes': [i for i, v in enumerate(slacks) if v < 0]}
    check('complete_failed_rows', negatives == {'domain': r['negative_domain_rows'], 'moments': r['negative_moment_indices'], 'modes': r['negative_modes']})
    check('selected_28_original_equalities', all(slacks[i] == 0 for i in eq['selected_modes']))
    check('single_capped_run_and_one_reconstruction', data['summary']['numerical_runs'] == r['passes'] == 1 and data['proposal']['iterations'] == data['iteration_cap_before_solve'] == 10000)
    check('no_feasibility_or_infeasibility_claim', data['summary']['verdict'] == 'INCONCLUSIVE' and not data['summary']['full_domain_feasibility_decided'])
    ns = data['numerical_scaling']
    zs = [F(*v) for v in ns['zscale']]
    bs = [F(*v) for v in ns['blockscales']]
    # These positive normalizations make failure magnitudes readable without
    # replacing the complete exact residuals saved below.
    fscale = [max(abs(f[0]+point[4]*f[4]), *(abs(v*F(1, 10**11)) for v in f[1:4])) or F(1) for f in family]
    minima = {'domain': min(v/t for v, t in zip(factors, fscale)),
              'moments': min(v/t for v, t in zip(z, zs)),
              'modes': min(v/t for v, t in zip(slacks, bs))}
    report = {'input_hashes': {str(p.relative_to(NB)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
              'checks': checks, 'failures': failures, 'factors': factors, 'raw_moments': raw,
              'original_mode_slacks': slacks, 'raw_schur_slacks': rawslacks,
              'negative_rows': negatives, 'exact_normalized_minima': minima,
              'summary': {'verdict': 'VERIFIED_FAILED_CANDIDATE_ONLY' if not failures else 'FAILED',
                          'checks': len(checks), 'failures': len(failures),
                          'negative_domain_rows': len(negatives['domain']), 'negative_moments': len(negatives['moments']),
                          'negative_modes': len(negatives['modes']), 'selected_equalities_exact': True,
                          'normalized_minimum_intervals': {k: interval(v) for k, v in minima.items()},
                          'required_minimum': 0, 'full_domain_verdict': 'UNDECIDED'}}
    OUT.write_text(json.dumps(enc(report), indent=2)+'\n')
    print(enc(report['summary']), flush=True)
    print('Failures:', failures, '; evidence:', OUT.relative_to(NB), flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
