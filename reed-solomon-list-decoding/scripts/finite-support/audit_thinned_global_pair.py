"""Independent direct Farkas verification; no constructor imports or solver."""
import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT/'thinned-global-pair-results.json'
OUT = ROOT/'thinned-global-pair-audit-results.json'


def binomial(n, k):
    if k < 0 or k > n:
        return 0
    k = min(k, n-k)
    z = 1
    for r in range(1, k+1):
        z = z*(n-k+r)//r
    return z


def dec(z):
    return Q(z['numerator'], z['denominator'])


def enc(z):
    return {'numerator': z.numerator, 'denominator': z.denominator}


def reconstruct(matrix, rhs):
    """Independent Gauss-Jordan elimination, checking every pivot."""
    aug = [list(row)+[z] for row, z in zip(matrix, rhs)]
    n = len(aug)
    pivots = []
    for k in range(n):
        r = next(r for r in range(k, n) if aug[r][k])
        aug[k], aug[r] = aug[r], aug[k]
        pivot = aug[k][k]
        pivots.append(pivot)
        aug[k] = [z/pivot for z in aug[k]]
        for r in range(n):
            if r != k:
                mult = aug[r][k]
                if mult:
                    aug[r] = [z-mult*v for z, v in zip(aug[r], aug[k])]
    return [row[-1] for row in aug], pivots


def main():
    saved = json.loads(SOURCE.read_text())
    checks = []
    def check(name, truth):
        checks.append({'check': name, 'passed': bool(truth)})
    M = binomial(1024, 68)
    L = 137**3
    rho = Q(L, binomial(963, 7))
    tau = Q(65537**28, 2**128)
    T = tau.numerator//tau.denominator+1
    theta = Q(T)/(M*rho)
    p = saved['parameters']
    check('universe', p['n'] == 1024 and p['w'] == 68 and p['M'] == M)
    for name, z in [('rho', rho), ('tau', tau), ('theta', theta), ('singleton_f', Q(T, M))]:
        check('parameter_'+name, dec(p[name]) == z)
    check('T_exact', p['T'] == T)
    check('smallest_unsafe_integer', T-1 <= tau < T)
    check('retention_range', 0 < theta < 1)
    check('singleton_mass', M*theta*rho == T)
    # Polynomial convolution, rather than the constructor's direct sum.
    val = [binomial(68, i)*binomial(956, i) for i in range(69)]
    coeff = []
    for j in range(69):
        pol = [0]*69
        for h in range(j+1):
            for r in range(69-j):
                if h+r <= 68:
                    pol[h+r] += ((-1)**h*binomial(j, h)
                                  *binomial(68-j, r)*binomial(956-j, r))
        row = [Q(pol[i], val[i]) for i in range(69)]
        coeff.append(row)
        for i in range(69):
            check(f'q_{j}_{i}', dec(saved['q_matrix'][j][i]) == row[i])
    d2 = binomial(7, 2)*136
    d1 = 7*(137**2-1)-2*d2
    d0 = L-1-d1-d2
    d = [d0, d1, d2]
    check('local_pair_counts', d == [2442832, 125664, 2856])
    fixed = [Q(1)]+[Q(0)]*4
    fixed += [theta*Q(val[i]*d[7-i], binomial(7, 7-i)*binomial(956, i))
              for i in range(5, 8)]
    candidate = saved['candidate']
    a = [dec(z) for z in candidate['distance_coordinates']]
    check('candidate_length', len(a) == 69)
    for i in range(8):
        check(f'fixed_coordinate_{i}', a[i] == fixed[i])
    # Verify the direct certificate in the original, unscaled system.
    direct = saved['phase_one']['exact']['direct_farkas']
    weights = [dec(z) for z in direct['weights']]
    check('weight_length', len(weights) == 69)
    for r, z in enumerate(weights):
        check(f'nonnegative_weight_{r}', z >= 0)
    check('strict_positive_support', all(weights[j-1] > 0
                                        for j in list(range(1, 61))+[62, 63, 64]))
    spec = direct['witness_spec']
    unknown = list(range(1, 61))+[62]
    check('canonical_witness_spec', spec['unknown_rows'] == unknown
          and dec(spec['lambda63']) == Q(23191266, 140599441)
          and dec(spec['lambda64']) == 1
          and spec['zero_rows'] == [61, 65, 66, 67, 68, 'constant']
          and spec['free_equalities'] == list(range(8, 69)))
    small, pivots = reconstruct([[coeff[j][i] for j in unknown] for i in range(8, 69)],
                               [-Q(23191266, 140599441)*coeff[63][i]-coeff[64][i]
                                for i in range(8, 69)])
    for j, z in zip(unknown, small):
        check(f'canonical_weight_{j}', z == weights[j-1])
    for k, z in enumerate(pivots):
        check(f'canonical_pivot_{k}', z != 0)
    check('canonical_fixed_weights', weights[62] == Q(23191266, 140599441)
          and weights[63] == 1
          and all(weights[j-1] == 0 for j in [61, 65, 66, 67, 68])
          and weights[68] == 0)
    slacks = []
    for i in range(8, 69):
        slack = -sum(weights[j-1]*coeff[j][i] for j in range(1, 69))-weights[68]
        slacks.append(slack)
        check(f'free_slack_{i}_matches', slack == dec(direct['free_slacks'][i-8]))
        check(f'free_slack_{i}_nonnegative', slack >= 0)
    check('all_free_terms_cancel', not any(slacks))
    fixed_b = [sum(coeff[j][i]*fixed[i] for i in range(8)) for j in range(1, 69)]
    bound = sum(weights[j-1]*fixed_b[j-1] for j in range(1, 69))
    bound += weights[68]*(sum(fixed)-T)
    check('bound_matches', bound == dec(direct['weighted_bound']))
    check('bound_strictly_negative', bound < 0)
    check('bound_rational_bracket', -Q(1433, 1000) < bound < -Q(1432, 1000))
    # Independently report real candidate failures; never mask them.
    spectral = [sum(coeff[j][i]*a[i] for i in range(69)) for j in range(69)]
    bad = [j for j in range(1, 69) if spectral[j] < 0]
    for j in range(69):
        check(f'candidate_spectrum_{j}', spectral[j] == dec(candidate['spectral_sums'][j]))
    check('candidate_failed_rows_preserved', bad == candidate['failed_rows'])
    check('candidate_not_presented_feasible', not candidate['primal_feasible'])
    failures = [z['check'] for z in checks if not z['passed']]
    result = {'verified_infeasible': not failures, 'checks': checks, 'failures': failures,
              'direct_weights': [enc(z) for z in weights],
              'direct_free_slacks': [enc(z) for z in slacks], 'weighted_bound': enc(bound),
              'support': direct['support'], 'T': T, 'theta': enc(theta),
              'constant_weight': enc(weights[68]),
              'canonical_pivots': [enc(z) for z in pivots],
              'candidate_failed_rows': bad,
              'candidate_failures_are_not_verification_failures': True}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('Direct original-system Farkas certificate verified:', not failures)
    print('Checks:', len(checks), '; failures:', failures)
    print('T:', T, '; required unsafe mass >', tau)
    print('Support:', direct['support'], '; constant weight:', weights[68])
    print('Weighted bound sign:', (bound > 0)-(bound < 0),
          '; candidate failed rows:', bad, '; full certificate:', OUT)


if __name__ == '__main__':
    main()
