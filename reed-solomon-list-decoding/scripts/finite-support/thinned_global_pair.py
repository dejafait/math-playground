"""One assessed threshold-thinned pair slice, exact rational verification."""
import json
from decimal import Decimal, localcontext
from fractions import Fraction as Q
from math import comb
from pathlib import Path
from delsarte_lp import hahn, solve_exact, enc

OUT = Path(__file__).with_name('thinned-global-pair-results.json')


def phase_one(coeff, fixed, initial, T):
    """Decimal basis discovery, followed by exact primal/dual checks."""
    # a_i=scale_i*x_i, so every column is of comparable practical size.
    scales = initial[8:]
    assert all(z > 0 for z in scales)
    A = [[-coeff[j][i]*scales[i-8] for i in range(8, 69)]
         for j in range(1, 69)]
    b = [sum(coeff[j][i]*fixed[i] for i in range(8)) for j in range(1, 69)]
    A.append([-z for z in scales])
    b.append(sum(fixed)-T)
    rows, count = len(A), 61
    norm = [max([abs(z) for z in row]+[abs(rhs), Q(1)])
            for row, rhs in zip(A, b)]
    signs = [1 if z >= 0 else -1 for z in b]
    # Positive right sides; negative original rows get surplus and artificial.
    arts = [r for r in range(rows) if signs[r] == -1]
    artcol = {r: count+rows+k for k, r in enumerate(arts)}
    cols = count+rows+len(arts)
    eq = [[Q(signs[r])*z/norm[r] for z in A[r]]
          +[Q(signs[r] if k == r else 0) for k in range(rows)]
          +[Q(int(k == r)) for k in arts] for r in range(rows)]
    rhs = [Q(signs[r])*b[r]/norm[r] for r in range(rows)]
    cost = [Q(0)]*(count+rows)+[Q(-1)]*len(arts)
    basis = [count+r if signs[r] == 1 else artcol[r] for r in range(rows)]
    trace = []
    with localcontext() as ctx:
        ctx.prec = 240
        dec = lambda z: Decimal(z.numerator)/Decimal(z.denominator)
        tab = [[dec(z) for z in row]+[dec(t)] for row, t in zip(eq, rhs)]
        obj = [-dec(z) for z in cost]+[Decimal(0)]
        for r in range(rows):
            if cost[basis[r]]:
                cb = dec(cost[basis[r]])
                obj = [z+cb*v for z, v in zip(obj, tab[r])]
        tab.append(obj)
        eps = Decimal('1e-180')
        status = 'iteration_limit'
        for iteration in range(600):
            entering = next((k for k, z in enumerate(tab[-1][:-1]) if z < -eps), None)
            if entering is None:
                status = 'decimal_optimal'
                break
            options = [(row[-1]/row[entering], basis[r], r)
                       for r, row in enumerate(tab[:-1]) if row[entering] > eps]
            if not options:
                status = 'decimal_unbounded_or_scaling_failure'
                break
            _, _, leaving = min(options)
            old = basis[leaving]
            pivot = tab[leaving][entering]
            tab[leaving] = [z/pivot for z in tab[leaving]]
            for r in range(rows+1):
                if r != leaving:
                    factor = tab[r][entering]
                    if factor:
                        tab[r] = [z-factor*v for z, v in zip(tab[r], tab[leaving])]
                        tab[r][entering] = Decimal(0)
            basis[leaving] = entering
            trace.append({'iteration': iteration, 'entering': entering,
                          'leaving': old, 'objective': str(tab[-1][-1])})
        discovery = {'status': status, 'precision': ctx.prec,
                     'basis': basis, 'trace': trace, 'objective': str(tab[-1][-1])}
    # Remove basic slack columns and their matching rows from reconstruction.
    basic_other = sorted(k for k in basis if not count <= k < count+rows)
    active = [r for r in range(rows) if count+r not in basis]
    mat = [[eq[r][k] for k in basic_other] for r in active]
    xsmall = solve_exact(mat, [rhs[r] for r in active])
    values = [Q(0)]*cols
    for k, z in zip(basic_other, xsmall):
        values[k] = z
    for r in range(rows):
        if count+r in basis:
            values[count+r] = (rhs[r]-sum(eq[r][k]*values[k] for k in basic_other))/signs[r]
    eq_res = [sum(row[k]*values[k] for k in range(cols))-t
              for row, t in zip(eq, rhs)]
    ysmall = solve_exact(list(map(list, zip(*mat))), [cost[k] for k in basic_other])
    y = [Q(0)]*rows
    for r, z in zip(active, ysmall):
        y[r] = z
    dual_slacks = [sum(eq[r][k]*y[r] for r in range(rows))-cost[k]
                   for k in range(cols)]
    primal_obj = sum(cost[k]*values[k] for k in range(cols))
    dual_obj = sum(rhs[r]*y[r] for r in range(rows))
    exact = {'values': [enc(z) for z in values],
             'equality_residuals': [enc(z) for z in eq_res],
             'dual': [enc(z) for z in y],
             'dual_slacks': [enc(z) for z in dual_slacks],
             'primal_objective': enc(primal_obj), 'dual_objective': enc(dual_obj),
             'active_rows': active, 'basic_other_columns': basic_other,
             'primal_feasible': all(z >= 0 for z in values) and not any(eq_res),
             'dual_feasible': all(z >= 0 for z in dual_slacks),
             'equal_objectives': primal_obj == dual_obj}
    exact['infeasibility_verified'] = exact['dual_feasible'] and dual_obj < 0
    # Direct Farkas certificate for original inequalities A a <= b.
    weights = [Q(signs[r])*y[r]/norm[r] for r in range(rows)]
    positive = next((z for z in reversed(weights) if z > 0), Q(1))
    weights = [z/positive for z in weights]
    # Simplify the discovered ray using three bounded rational tail choices.
    # This is certificate reconstruction, not an additional mathematical target.
    simple_trials = []
    witness_spec = None
    unknown = list(range(1, 61))+[62]
    for tail63 in (Q(165), Q(164), weights[62].limit_denominator(10**9)):
        try:
            wsmall = solve_exact([[coeff[j][i] for j in unknown] for i in range(8, 69)],
                                 [-tail63*coeff[63][i]-coeff[64][i] for i in range(8, 69)])
        except ValueError:
            simple_trials.append({'lambda63': enc(tail63), 'singular': True})
            continue
        trial = [Q(0)]*69
        for j, z in zip(unknown, wsmall):
            trial[j-1] = z
        trial[62], trial[63] = tail63, Q(1)
        trial_bound = sum(trial[j-1]*sum(coeff[j][i]*fixed[i] for i in range(8))
                          for j in range(1, 69))
        good = all(z >= 0 for z in trial) and trial_bound < 0
        simple_trials.append({'lambda63': enc(tail63),
                             'negative_weights': [r+1 for r, z in enumerate(trial) if z < 0],
                             'bound': enc(trial_bound), 'valid': good})
        if good:
            weights = trial
            witness_spec = {'unknown_rows': unknown, 'lambda63': enc(tail63),
                            'lambda64': enc(Q(1)), 'zero_rows': [61, 65, 66, 67, 68, 'constant'],
                            'free_equalities': list(range(8, 69))}
            break
    free_slacks = [-sum(weights[j-1]*coeff[j][i] for j in range(1, 69))
                   -weights[68] for i in range(8, 69)]
    bound = sum(weights[j-1]*sum(coeff[j][i]*fixed[i] for i in range(8))
                for j in range(1, 69))+weights[68]*(sum(fixed)-T)
    exact['direct_farkas'] = {
        'weights': [enc(z) for z in weights],
        'support': [r+1 if r < 68 else 'constant' for r, z in enumerate(weights) if z],
        'free_slacks': [enc(z) for z in free_slacks],
        'weighted_bound': enc(bound),
        'all_weights_nonnegative': all(z >= 0 for z in weights),
        'all_free_slacks_nonnegative': all(z >= 0 for z in free_slacks),
        'bound_negative': bound < 0,
        'verified': all(z >= 0 for z in weights+free_slacks) and bound < 0,
        'witness_spec': witness_spec, 'simplification_trials': simple_trials}
    a = fixed+[scales[k]*values[k] for k in range(count)]
    evidence = {'discovery': discovery, 'column_scales': [enc(z) for z in scales],
                'row_norms': [enc(z) for z in norm], 'row_signs': signs,
                'artificial_rows': arts, 'exact': exact}
    print('Phase I:', status, '; pivots:', len(trace),
          '; exact artificial objective sign:', (primal_obj > 0)-(primal_obj < 0),
          '; exact dual valid:', exact['dual_feasible'], flush=True)
    print('Direct Farkas verified:', exact['direct_farkas']['verified'],
          '; support:', exact['direct_farkas']['support'],
          '; bound approximately:', float(bound), flush=True)
    return a, evidence


def main():
    M = comb(1024, 68)
    rho = Q(137**3, comb(963, 7))
    tau = Q(65537**28, 2**128)
    T = tau.numerator // tau.denominator + 1
    theta = T/(M*rho)
    val = [comb(68, i)*comb(956, i) for i in range(69)]
    d = [2442832, 125664, 2856]
    fixed = [Q(1)]+[Q(0)]*4
    fixed += [theta*Q(val[i]*d[7-i], comb(7, 7-i)*comb(956, i))
              for i in range(5, 8)]
    coeff = [[hahn(j, i) for i in range(69)] for j in range(69)]
    rhs = [-sum(coeff[j][i]*fixed[i] for i in range(8))
           for j in range(1, 69)]
    free = list(range(8, 69))
    active = list(range(1, 62))
    x = solve_exact([[coeff[j][i] for i in free] for j in active], rhs[:61])
    a = fixed+x
    spectral = [sum(coeff[j][i]*a[i] for i in range(69)) for j in range(69)]
    failures = []
    negative = [i for i, z in enumerate(a) if z < 0]
    badrows = [j for j in range(1, 69) if spectral[j] < 0]
    if negative: failures.append('negative distance coordinates')
    if badrows: failures.append('negative nonconstant spectral sums')
    if spectral[0] < T: failures.append('negative constant Schur sum')
    if not 0 < theta < 1: failures.append('retention parameter not in (0,1)')
    initial = {'distance_coordinates': [enc(z) for z in a],
               'failed_rows': badrows, 'failures': failures.copy()}
    print('Initial exact candidate failed rows:', badrows, flush=True)
    phase = None
    if failures:
        a, phase = phase_one(coeff, fixed, a, T)
        spectral = [sum(coeff[j][i]*a[i] for i in range(69)) for j in range(69)]
        negative = [i for i, z in enumerate(a) if z < 0]
        badrows = [j for j in range(1, 69) if spectral[j] < 0]
        failures = []
        if negative: failures.append('negative distance coordinates')
        if badrows: failures.append('negative nonconstant spectral sums')
        if spectral[0] < T: failures.append('negative constant Schur sum')
        if not 0 < theta < 1: failures.append('retention parameter not in (0,1)')
    result = {
        'parameters': {'n': 1024, 'w': 68, 'M': M, 'rho': enc(rho),
                       'tau': enc(tau), 'T': T, 'theta': enc(theta),
                       'singleton_f': enc(Q(T, M))},
        'q_matrix': [[enc(z) for z in row] for row in coeff],
        'candidate': {'active_rows': ([r+1 for r in phase['exact']['active_rows']]
                                      if phase else active),
                      'distance_coordinates': [enc(z) for z in a],
                      'b_coordinates': [enc(a[i]/val[i]) for i in range(69)],
                      'spectral_sums': [enc(z) for z in spectral],
                      'constant_schur_sum': enc(spectral[0]-T),
                      'negative_distances': negative, 'failed_rows': badrows,
                      'primal_feasible': not failures, 'failures': failures},
        'discovery_candidate_failures': failures,
        'failures': ([] if phase and phase['exact']['direct_farkas']['verified']
                     else failures),
        'initial_candidate': initial, 'phase_one': phase,
    }
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('Final candidate exact feasible:', not failures)
    print('T:', T, '; required unsafe mass >', tau)
    print('theta approximately:', float(theta), '; negative coordinates:', negative,
          '; failed spectral rows:', badrows, '; constant passes:', spectral[0] >= T)
    print('Candidate failures:', failures, '; certificate verification failures:',
          result['failures'], '; full certificate:', OUT)


if __name__ == '__main__':
    main()
