"""Independent exact-rational audit of L595 and both saved certificates.

No optimizer, NumPy, Decimal arithmetic, or original verifier is imported.
Run from riemann: python3 scripts/coupled-flux/audit_rational_schur_dual.py
All input decimals are exact Fractions. Each complete contribution is
computed exactly before accumulation on a 160-place outward lattice.
"""
from fractions import Fraction as F
from itertools import product
from math import factorial, prod
from pathlib import Path
import hashlib
import json
import time

ROOT = Path(__file__).resolve().parent
SCALE = 10**160
FAILURES = []
COUNTS = {}


def check(label, condition):
    COUNTS[label] = COUNTS.get(label, 0) + 1
    if not condition:
        FAILURES.append(f'{label}, check {COUNTS[label]}')


def pair(values):
    return tuple(F(x) for x in values)


def contains(outer, inner):
    a, b = pair(outer)
    c, d = inner if isinstance(inner, tuple) else (inner, inner)
    return a <= c <= d <= b


def lattice(x):
    n = x.numerator*SCALE
    return (n//x.denominator, -((-n)//x.denominator))


def accumulate(total, values):
    for t, v in zip(total, values):
        lo, hi = lattice(v)
        t[0] += lo
        t[1] += hi


def unscale(values):
    return [(F(a, SCALE), F(b, SCALE)) for a, b in values]


def idot(coefficients, intervals):
    lo, hi = F(0), F(0)
    for c, (a, b) in zip(coefficients, intervals):
        lo += c*(a if c >= 0 else b)
        hi += c*(b if c >= 0 else a)
    return lo, hi


def absmax(interval):
    return max(abs(v) for v in interval)


def encoded(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {str(k): encoded(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encoded(v) for v in value]
    return value


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def basis(degree):
    return sorted(e for e in product(range(degree+1), repeat=4)
                  if sum(e) == degree)


Q = {(2, 0, 0, 0): F(1, 2), (0, 2, 0, 0): F(6),
     (0, 0, 2, 0): F(1, 2), (0, 0, 0, 2): F(6)}


def divide(exponent):
    work, quotient = {exponent: F(1)}, {}
    while any(e[0] >= 2 for e in work):
        e = max(e for e in work if e[0] >= 2)
        factor = (e[0]-2, *e[1:])
        c = 2*work[e]
        quotient[factor] = quotient.get(factor, F(0)) + c
        for a, coefficient in Q.items():
            key = tuple(x+y for x, y in zip(a, factor))
            work[key] = work.get(key, F(0))-c*coefficient
            if not work[key]:
                del work[key]
    rebuilt = work.copy()
    for e, c in quotient.items():
        for a, d in Q.items():
            key = tuple(x+y for x, y in zip(e, a))
            rebuilt[key] = rebuilt.get(key, F(0))+c*d
    check('exact_polynomial_division',
          {e: c for e, c in rebuilt.items() if c} == {exponent: F(1)})
    return quotient, work


def monomial_gradient(ex, w, q):
    p = prod(t**e for t, e in zip(w, ex))
    dq = [w[0], 12*w[1], w[2], 12*w[3]]
    return [((ex[k]*prod(w[j]**(ex[j]-(j == k)) for j in range(4))
              if ex[k] else F(0))*q-p*dq[k])/(q*q)
            for k in range(4)]


def spectral_interval(a, b):
    r, j = divmod(a, 3)
    s, k = divmod(b, 3)
    # Re(i^j (-i)^k i^n) = Re(i^(j+3k+n)); odd moments vanish.
    value = F(0)
    for n in range(25):
        power = j+k+n
        phase = (j+3*k+n) % 4
        if power % 2 == 0:
            real_phase = (1, 0, -1, 0)[phase]
            value += F(real_phase*(r-s)**n,
                       factorial(n)*2**power*(power+1))
    error = F(0) if r == s else F(2, factorial(25)*2**(j+k+25)*(j+k+26))
    return value-error, value+error


def main():
    started = time.monotonic()
    path = ROOT/'rational_schur_dual_inputs.json'
    data = json.loads(path.read_text())
    check('fixed_input_hash', sha(path) ==
          '0178c10b3da0315bf2c67b0715e2f6c41b5a84c8714f516541c3b8d28b41647b')
    denominator = data['state_integer_denominator']
    check('state_denominator', denominator == 10**12)
    states = [[F(x, denominator) for x in row] for row in data['state_integers']]
    R = [[F(x) for x in row] for row in data['mean']]
    A = [[F(x) for x in row] for row in data['acceleration_transform']]
    selected = data['selected_matrix_indices']
    n = len(states)
    check('manifest_dimensions', n == 1536 and all(len(w) == 4 for w in states)
          and len(R) == 2 and all(len(row) == 4 for row in R)
          and len(A) == 2 and all(len(row) == 2 for row in A)
          and len(data['dual_cholesky']) == 3072
          and len(selected) == len(set(selected)) == 46
          and all(0 <= j < 2*n for j in selected))
    all_ex = basis(4)
    exponents = [e for e in all_ex if e[0] < 2]
    divisions = {e: divide(e) for e in all_ex}
    pairs = [(i, j) for i in range(6) for j in range(i, 6)]
    total = [[0, 0] for _ in range(46)]
    all_flux = [[0, 0] for _ in range(35)]
    objective = [[0, 0]]
    columns, betas = {}, {}
    minimum_q = None
    contribution_digest = hashlib.sha256()
    state_coordinates = [0, 1, 3, 4]
    derivative_coordinates = [1, 2, 4, 5]
    for i, w in enumerate(states):
        q = sum(c*prod(t**k for t, k in zip(w, e)) for e, c in Q.items())
        check('positive_exact_q', q > 0)
        minimum_q = q if minimum_q is None else min(minimum_q, q)
        gradients = {e: monomial_gradient(e, w, q) for e in all_ex}
        d = [sum(a*b for a, b in zip(row, w)) for row in R]
        T = [[w[0], 0, 0], [w[1], 0, 0], [d[0], *A[0]],
             [w[2], 0, 0], [w[3], 0, 0], [d[1], *A[1]]]
        for branch in range(2):
            index = i+branch*n
            L = [[F(x) for x in row] for row in data['dual_cholesky'][index]]
            check('factor_shape', len(L) == 3 and all(len(row) == 3 for row in L))
            # Compute each test as three vectors, instead of using Y and T Y T^T.
            vectors = [[sum(T[a][k]*L[k][ell] for k in range(3))
                        for a in range(6)] for ell in range(3)]
            C = [[sum(v[a]*v[b] for v in vectors) for b in range(6)]
                 for a in range(6)]
            flux = {e: sum(L[0][ell]*sum(g[k]*v[derivative_coordinates[k]]
                                        for k in range(4))
                           for ell, v in enumerate(vectors))
                    for e, g in gradients.items()}
            for e, (quotient, remainder) in divisions.items():
                expected = sum(c*flux[a] for a, c in remainder.items())
                for a, c in quotient.items():
                    for k in range(4):
                        if a[k]:
                            residual = list(a)
                            residual[k] -= 1
                            j = residual.index(1)
                            expected += c*a[k]*C[state_coordinates[j]][derivative_coordinates[k]]
                check('all_quartic_flux_division', expected == flux[e])
            col = [C[a][b] for a, b in pairs]+[flux[e] for e in exponents]
            beta = sum(v[0]*v[2]-v[1]**2 for v in vectors) if branch else F(0)
            accumulate(total, col)
            accumulate(all_flux, [flux[e] for e in all_ex])
            accumulate(objective, [beta])
            contribution_digest.update(json.dumps(encoded([index, col, beta])).encode())
            if index in selected:
                columns[index], betas[index] = col, beta
        if (i+1) % 512 == 0:
            print(f'Exact reconstruction: {i+1}/{n} states, all 35 quartics.', flush=True)
    baseline, objective_interval = unscale(total), unscale(objective)[0]
    target = [spectral_interval(a, b) for a, b in pairs]+[(F(0), F(0))]*25
    residual = [(a-d, b-c) for (a, b), (c, d) in zip(target, baseline)]
    matrix = [[columns[j][i] for j in selected] for i in range(46)]
    certificate_reports = []
    for precision, suffix in [(90, ''), (120, '_precision_120')]:
        cp = ROOT/f'rational_schur_dual_certificate{suffix}.json'
        cert = json.loads(cp.read_text())
        check('saved_hashes', cert['input_sha256'] == sha(path)
              and cert['verifier_sha256'] == sha(ROOT/'certify_rational_schur_dual.py'))
        check('saved_dimensions_and_order', cert['states'] == n
              and cert['dual_matrices'] == 2*n and cert['moment_rows'] == 21
              and cert['essential_flux_rows'] == 25 and cert['decimal_precision'] == precision
              and cert['selected_matrix_indices'] == selected
              and cert['quartic_remainder_exponents'] == [list(e) for e in exponents])
        check('saved_q_bound', F(cert['minimum_q_lower']) <= minimum_q)
        for field, actual in [('baseline_moment_intervals', baseline),
                              ('target_moment_intervals', target), ('residual_intervals', residual)]:
            check('array_shape_'+field, len(cert[field]) == len(actual))
            for enclosure, value in zip(cert[field], actual):
                check('enclosure_'+field, contains(enclosure, value))
        check('correction_matrix_shape', len(cert['correction_matrix_intervals']) == 46
              and all(len(row) == 46 for row in cert['correction_matrix_intervals']))
        for i in range(46):
            for j in range(46):
                check('exact_correction_matrix_enclosure',
                      contains(cert['correction_matrix_intervals'][i][j], matrix[i][j]))
        B = [[F(v) for v in row] for row in cert['approximate_inverse']]
        check('inverse_shape', len(B) == 46 and all(len(row) == 46 for row in B))
        inverse_residual = [[F(i == j)-sum(B[i][k]*matrix[k][j] for k in range(46))
                             for j in range(46)] for i in range(46)]
        check('inverse_residual_shape', len(cert['inverse_residual_intervals']) == 46
              and all(len(row) == 46 for row in cert['inverse_residual_intervals']))
        for i in range(46):
            for j in range(46):
                check('exact_inverse_residual_enclosure',
                      contains(cert['inverse_residual_intervals'][i][j], inverse_residual[i][j]))
        exact_eta = max(sum(abs(v) for v in row) for row in inverse_residual)
        saved_eta = F(cert['inverse_residual_infinity_norm_upper'])
        interval_eta = max(sum(absmax(pair(v)) for v in row)
                           for row in cert['inverse_residual_intervals'])
        check('upward_inverse_norm', exact_eta <= interval_eta <= saved_eta < F(1, 10**70))
        z = [idot(row, residual) for row in B]
        check('preconditioned_residual_shape', len(cert['preconditioned_residual_intervals']) == 46)
        for enclosure, value in zip(cert['preconditioned_residual_intervals'], z):
            check('preconditioned_residual_enclosure', contains(enclosure, value))
        zmax = F(cert['preconditioned_residual_infinity_norm_upper'])
        check('upward_preconditioned_norm',
              max(absmax(pair(v)) for v in cert['preconditioned_residual_intervals']) <= zmax)
        delta_pair = pair(cert['weight_correction_infinity_norm_bound'])
        check('division_for_correction', contains(delta_pair, zmax/(1-saved_eta)))
        check('positive_corrected_weights', 0 <= delta_pair[1] < F(3, 250) < 1)
        check('baseline_objective_enclosure', contains(cert['baseline_objective_interval'], objective_interval))
        check('selected_objective_shape', len(cert['selected_objective_intervals']) == 46)
        for j, enclosure in zip(selected, cert['selected_objective_intervals']):
            check('exact_selected_objective_enclosure', contains(enclosure, betas[j]))
        bnorm = F(cert['selected_objective_absolute_sum_upper'])
        check('upward_objective_norm', sum(absmax(pair(v)) for v in cert['selected_objective_intervals']) <= bnorm)
        loss_pair = pair(cert['objective_loss_bound'])
        check('multiplication_for_loss', contains(loss_pair, delta_pair[1]*bnorm))
        lower = F(cert['certified_cost_lower'])
        check('downward_cost_bound', lower <= F(cert['baseline_objective_interval'][0])-loss_pair[1])
        check('required_threshold', contains(cert['required_threshold'], F(1, 288)))
        named = {
            'inverse_residual_lt_1e_minus_70': saved_eta < F(1, 10**70),
            'weight_correction_lt_3_over_250': delta_pair[1] < F(3, 250),
            'baseline_objective_gt_459_over_50000': F(cert['baseline_objective_interval'][0]) > F(459, 50000),
            'selected_absolute_objective_lt_1_over_100': bnorm < F(1, 100),
            'cost_lower_gt_9_over_1000': lower > F(9, 1000),
        }
        check('saved_acceptance_matches_evidence', cert['passed'] and not cert['failures']
              and cert['named_bound_checks'] == named and all(named.values()))
        certificate_reports.append(dict(path=cp.name, sha256=sha(cp), precision=precision,
            exact_inverse_residual=inverse_residual, exact_inverse_residual_norm=exact_eta,
            independently_enclosed_preconditioned_residual=z,
            certified_cost_lower=lower, required_threshold=F(1, 288), named_checks=named))
    check('final_rational_margin', F(459, 50000)-F(3, 250)*F(1, 100) == F(453, 50000)
          and F(453, 50000) > F(9, 1000) > F(1, 288)
          and F(9, 1000)-F(1, 288) == F(199, 36000))
    report = dict(kind='INDEPENDENT FRACTION AUDIT OF L595', passed=not FAILURES,
        failures=FAILURES, counts=COUNTS, input_sha256=sha(path), auditor_sha256=sha(Path(__file__)),
        lattice_denominator=SCALE, exact_contribution_sha256=contribution_digest.hexdigest(),
        states=n, matrices=2*n, all_quartic_exponents=all_ex, remainder_exponents=exponents,
        exact_polynomial_divisions={str(e): {'quotient': q, 'remainder': s}
                                    for e, (q, s) in divisions.items()},
        minimum_exact_q=minimum_q, baseline_moment_intervals=baseline,
        all_quartic_baseline_flux_intervals=unscale(all_flux), exact_K_taylor_intervals=target,
        residual_intervals=residual, selected_indices=selected, exact_correction_matrix=matrix,
        baseline_objective_interval=objective_interval, exact_selected_objectives=[betas[j] for j in selected],
        certificates=certificate_reports, rational_lower_bound=F(453, 50000),
        stated_bound=F(9, 1000), required_threshold=F(1, 288),
        elapsed_seconds=time.monotonic()-started)
    out = ROOT/'rational_schur_dual_independent_audit.json'
    out.write_text(json.dumps(encoded(report), indent=2)+'\n')
    print(json.dumps(encoded({k: report[k] for k in ['passed', 'failures', 'counts',
        'rational_lower_bound', 'stated_bound', 'required_threshold', 'elapsed_seconds']}), indent=2))
    print('Full audit certificate:', out)
    if FAILURES:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
