"""Exact prescribed global pair slice; no numerical PSD conclusions."""
import json
import sys
from fractions import Fraction as Q
from math import comb
from itertools import combinations
from pathlib import Path
from delsarte_lp import hahn, solve_exact, enc

OUT = Path(__file__).with_name('global-pair-slice-results.json')


def main():
    val = [comb(68, i)*comb(956, i) for i in range(69)]
    rho = Q(137**3, comb(963, 7))
    mass = comb(1024, 68)*rho
    fixed = {0: Q(1), **{i: Q(0) for i in range(1, 5)}}
    d = [2442832, 125664, 2856]
    for i in range(5, 8):
        overlap = 7-i
        local_val = comb(7, overlap)*comb(956, 7-overlap)
        fixed[i] = Q(val[i]*d[overlap], local_val)
    coeff = [[hahn(j, i) for i in range(69)] for j in range(69)]
    rhs = [-sum(coeff[j][i]*a for i, a in fixed.items())
           for j in range(1, 69)]
    free = list(range(8, 69))
    x = solve_exact([[coeff[j][i] for i in free] for j in range(1, 62)],
                    rhs[:61])
    a = [fixed[i] if i in fixed else x[i-8] for i in range(69)]
    spectral = [sum(coeff[j][i]*a[i] for i in range(69)) for j in range(69)]
    schur = spectral[0]-mass
    failures = []
    negative = [i for i, z in enumerate(a) if z < 0]
    badrows = [j for j in range(1, 69) if spectral[j] < 0]
    if negative: failures.append('negative distance coordinates')
    if badrows: failures.append('negative nonconstant eigenvalues')
    if schur < 0: failures.append('negative augmented constant coordinate')
    initial = {'active_rows': list(range(1, 62)),
               'distance_coordinates': [enc(z) for z in a],
               'spectral_sums': [enc(z) for z in spectral],
               'constant_schur_sum': enc(schur),
               'negative_distances': negative, 'failed_rows': badrows,
               'primal_feasible': not failures}
    trace = []
    active = list(range(1, 62))
    # Bounded exact basis discovery. Failed bases are not infeasibility.
    for tail in (combinations(range(59, 69), 3) if '--discover' in sys.argv else ()):
        if not failures:
            break
        active = list(range(1, 59))+list(tail)
        try:
            x = solve_exact([[coeff[j][i] for i in free] for j in active],
                            [rhs[j-1] for j in active])
        except ValueError:
            trace.append({'active_tail': list(tail), 'singular': True})
            continue
        a = [fixed[i] if i in fixed else x[i-8] for i in range(69)]
        spectral = [sum(coeff[j][i]*a[i] for i in range(69)) for j in range(69)]
        schur = spectral[0]-mass
        negative = [i for i,z in enumerate(a) if z < 0]
        badrows = [j for j in range(1, 69) if spectral[j] < 0]
        failures = []
        if negative: failures.append('negative distance coordinates')
        if badrows: failures.append('negative nonconstant eigenvalues')
        if schur < 0: failures.append('negative augmented constant coordinate')
        trace.append({'active_tail': list(tail), 'negative_distances': negative,
                      'failed_rows': badrows, 'constant_passes': schur >= 0})
    certificate = {
        'parameters': {'n': 1024, 'w': 68, 'rho': enc(rho),
                       'global_vertex_count': comb(1024, 68),
                       'required_constant_mass': enc(mass),
                       'ambient_threshold': enc(Q(65537**28, 2**128))},
        'fixed_distance_coordinates': {str(i): enc(z) for i,z in fixed.items()},
        'q_matrix': [[enc(z) for z in row] for row in coeff],
        'initial_failed_candidate': initial,
        'discovery_trace': trace,
        'candidate': {'active_rows': active,
                      'distance_coordinates': [enc(z) for z in a],
                      'spectral_sums': [enc(z) for z in spectral],
                      'constant_schur_sum': enc(schur),
                      'negative_distances': negative, 'failed_rows': badrows,
                      'primal_feasible': not failures},
        'discovery_failures': failures,
    }
    # PSD plus exact zero core variance forces all these row equations.
    # This independent triangular reconstruction is the obstruction proof;
    # the search above is not used as evidence of infeasibility.
    b = [fixed[i]/val[i] for i in range(8)]
    core_rows = []
    for t in range(1, 62):
        i_new = t+7
        row = [comb(t+7, t+7-i)*comb(956-t, i-t)
               for i in range(t, t+8)]
        known = sum(Q(row[i-t])*b[i] for i in range(t, i_new))
        b.append((137**3-known)/row[-1])
        core_rows.append({'t': t, 'coefficients': row,
                          'new_b': enc(b[-1]), 'pivot': row[-1]})
    forced_a = [val[i]*b[i] for i in range(69)]
    forced_spectral = [sum(coeff[j][i]*forced_a[i] for i in range(69))
                       for j in range(69)]
    core_residuals = []
    for t in range(62):
        core_residuals.append(sum(Q(comb(t+7, t+7-i)*comb(956-t, i-t))*b[i]
                                  for i in range(t, t+8))-137**3)
    proof_checks = {
        'rho_times_local_vertex_count_equals_L': rho*comb(963, 7) == 137**3,
        'local_row_sum_equals_L': 1+sum(d) == 137**3,
        'all_core_equations_zero': all(z == 0 for z in core_residuals),
        'all_pivots_positive': all(row['pivot'] > 0 for row in core_rows),
        'agrees_with_initial_reconstruction': [enc(z) for z in forced_a]
                                             == initial['distance_coordinates'],
        'forced_entries_nonnegative': all(z >= 0 for z in b),
        'constant_schur_zero': forced_spectral[0] == mass,
        'first_61_nonconstant_sums_zero': all(forced_spectral[j] == 0
                                             for j in range(1, 62)),
        'negative_j63': forced_spectral[63] < 0,
        'negative_j64': forced_spectral[64] < 0,
    }
    proof_failures = [name for name, passed in proof_checks.items() if not passed]
    certificate['exact_obstruction'] = {
        'b_coordinates': [enc(z) for z in b],
        'distance_coordinates': [enc(z) for z in forced_a],
        'core_rows': core_rows, 'core_residuals': [enc(z) for z in core_residuals],
        'spectral_sums': [enc(z) for z in forced_spectral],
        'constant_schur_sum': enc(forced_spectral[0]-mass),
        'checks': proof_checks, 'failures': proof_failures,
        'infeasibility_verified': not proof_failures,
    }
    certificate['failures'] = proof_failures
    OUT.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Exact bounded reconstruction:', 'FEASIBLE' if not failures else 'FAILED',
          '; bases tested:', len(trace), '; active tail:', active[58:])
    print('Negative discovery coordinates count:', len(negative), '; failed spectral rows:', badrows)
    print('Constant condition passes:', schur >= 0)
    print('Mass / ambient threshold:', float(mass/Q(65537**28, 2**128)))
    print('Discovery failures:', failures, '; full certificate:', OUT)
    print('Exact zero-variance obstruction:', not proof_failures,
          '; proof failures:', proof_failures)
    print('Forced spectral sums j=63,64:', forced_spectral[63], forced_spectral[64])


if __name__ == '__main__':
    main()
