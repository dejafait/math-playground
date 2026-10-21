"""L052 critical audit: integer dual identities; no solver imports.

Run after audit_thinned_global_pair.py, which reconstructs the unique
rational solution by Gauss-Jordan elimination. This verifies the complete
saved witness again after clearing denominators and retains both failed
primal candidates. All checks and exact values are written to disk.
"""
import json
from fractions import Fraction as Q
from math import comb, lcm
from pathlib import Path

ROOT = Path(__file__).parent
OUT = ROOT / 'thinned-pair-critical-audit-results.json'


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def decode(z):
    return Q(z['numerator'], z['denominator'])


def encode(z):
    z = Q(z)
    return {'numerator': z.numerator, 'denominator': z.denominator}


def main():
    saved = json.loads((ROOT / 'thinned-global-pair-results.json').read_text())
    audit = json.loads((ROOT / 'thinned-global-pair-audit-results.json').read_text())
    direct = saved['phase_one']['exact']['direct_farkas']
    checks = []

    def check(name, truth):
        checks.append({'check': name, 'passed': bool(truth)})

    check('complete_prior_reconstruction', len(audit['checks']) == 5172
          and all(c['passed'] for c in audit['checks']) and not audit['failures'])
    weights = list(map(decode, direct['weights']))
    check('all_reconstructed_weights_match', weights == list(map(decode, audit['direct_weights'])))
    check('weight_count', len(weights) == 69)
    denominator = lcm(*(z.denominator for z in weights))
    integer_weights = [int(z * denominator) for z in weights]
    for j, (a, z) in enumerate(zip(integer_weights, weights)):
        check(f'integer_weight_{j+1}', Q(a, denominator) == z and a >= 0)
    check('exact_positive_support', [j+1 for j, z in enumerate(integer_weights) if z]
          == list(range(1, 61)) + [62, 63, 64])
    check('constant_weight_zero', integer_weights[68] == 0)
    valencies = [comb(68, i)*comb(956, i) for i in range(69)]
    eigenvalues = [[sum((-1)**h*choose(j, h)*choose(68-j, i-h)
                       *choose(956-j, i-h) for h in range(i+1))
                    for i in range(69)] for j in range(69)]
    for j in range(69):
        for i in range(69):
            check(f'integer_spectral_entry_{j}_{i}',
                  Q(eigenvalues[j][i], valencies[i]) == decode(saved['q_matrix'][j][i]))
    M = comb(1024, 68)
    multiplicities = [comb(1024, j)-choose(1024, j-1) for j in range(69)]
    check('all_eigenspaces_nonzero', all(z > 0 for z in multiplicities))
    check('dimensions_exhaust_universe', sum(multiplicities) == M)
    check('constant_relation_row', eigenvalues[0] == valencies)
    check('identity_relation_column', all(row[0] == 1 for row in eigenvalues))
    # Complete trace orthogonality checks detect transposition/valency errors.
    for i in range(69):
        for k in range(i, 69):
            trace = sum(multiplicities[j]*eigenvalues[j][i]*eigenvalues[j][k]
                        for j in range(69))
            check(f'trace_orthogonality_{i}_{k}', trace == (M*valencies[i] if i == k else 0))
    residuals = [sum(integer_weights[j-1]*eigenvalues[j][i] for j in range(1, 69))
                 for i in range(69)]
    for i in range(8, 69):
        check(f'free_integer_cancellation_{i}', residuals[i] == 0)
    tau = Q(65537**28, 2**128)
    T = tau.numerator // tau.denominator + 1
    rho = Q(137**3, comb(963, 7))
    theta = Q(T, M) / rho
    check('strict_integer_endpoint', (T-1)*2**128 <= 65537**28 < T*2**128)
    check('thinning_range', 0 < theta < 1)
    check('recorded_T', T == saved['parameters']['T'] == audit['T'])
    check('recorded_theta', theta == decode(saved['parameters']['theta']) == decode(audit['theta']))
    check('boolean_diagonal', theta*rho == Q(T, M) and theta*theta*rho != Q(T, M))
    d = [2442832, 125664, 2856]
    fixed_terms = [Q(residuals[0], denominator)] + [Q(0)]*4
    fixed_terms += [theta * Q(residuals[i]*d[7-i],
                             denominator*comb(7, 7-i)*comb(956, i)) for i in range(5, 8)]
    bound = sum(fixed_terms)
    check('fixed_contribution', bound == decode(direct['weighted_bound']) == decode(audit['weighted_bound']))
    check('strict_negative_bound', -Q(1433, 1000) < bound < -Q(1432, 1000) < 0)
    candidate_evidence = {}
    for name, expected in [('initial_candidate', [63, 64]), ('candidate', [60, 62])]:
        a = list(map(decode, saved[name]['distance_coordinates']))
        check(name+'_length', len(a) == 69)
        sums = [sum(Q(eigenvalues[j][i], valencies[i])*a[i] for i in range(69))
                for j in range(69)]
        bad = [j for j in range(1, 69) if sums[j] < 0]
        check(name+'_failed_rows', bad == expected == saved[name]['failed_rows'])
        candidate_evidence[name] = {'spectral_sums': list(map(encode, sums)),
                                    'failed_rows': bad, 'constant_schur_sum': encode(sums[0]-T)}
    failures = [c['check'] for c in checks if not c['passed']]
    result = {'verified': not failures, 'checks': checks, 'failures': failures,
              'common_denominator': denominator, 'integer_weights': integer_weights,
              'integer_eigenvalues': eigenvalues, 'valencies': valencies,
              'multiplicities': multiplicities, 'integer_residuals': residuals,
              'fixed_contributions': list(map(encode, fixed_terms)), 'bound': encode(bound),
              'T': T, 'theta': encode(theta),
              'unsafe_margin_numerator': T*2**128-65537**28,
              'safe_predecessor_margin_numerator': 65537**28-(T-1)*2**128,
              'candidate_evidence': candidate_evidence}
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('Integer critical audit:', not failures, '; checks:', len(checks), '; failures:', failures)
    print('Free cancellations:', sum(z == 0 for z in residuals[8:]), '/ required 61; nonconstant weights:',
          sum(z > 0 for z in integer_weights[:68]), '; constant weight:', integer_weights[68])
    print('Fixed contribution:', bound, '; required < 0; T:', T, '; required >', tau)
    print('Preserved candidate failed rows: initial [63, 64], final [60, 62]; certificate:', OUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
