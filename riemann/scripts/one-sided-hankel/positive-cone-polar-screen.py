"""Bounded degree-2n real-polar diagnostic for the exact L666 family.

This is NOT a sign, optimization, or asymptotic certificate.  It saves
complete Laurent candidates and primal coefficients, including solver
failures.  The rational annulus calculation certifies only the displayed
trapezoidal alias bound for exact samples, not floating-point errors.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np


def displacement(q, pattern):
    r = np.arange(-2*q, 2*q)
    if pattern == "phase":
        k = np.arange(2*q, dtype=float)
        lo, hi = k+0.5, k+0.625
        for _ in range(48):
            mid = (lo+hi)/2
            sign = mid-k-0.5-np.arctan(1/(10*mid))/np.pi
            lo, hi = np.where(sign < 0, mid, lo), np.where(sign >= 0, mid, hi)
        # Rational dyadic nodes, not an assertion of the exact L673 signs.
        epos = np.round(((lo+hi)/2-k-0.5)*2**24)/2**24
        e = np.concatenate((-epos[::-1], epos))
    elif pattern == "independent":
        rng = np.random.default_rng(41000+q)
        e = rng.integers(-8, 9, size=4*q)/64
    else:
        raise ValueError(pattern)
    n = 12*q+3
    return n, e, (27/(10*n))*(r+0.5+e)


def values(n, ys, count):
    u = np.exp(2j*np.pi*np.arange(count)/count)
    t = np.arange(1, n, dtype=float)/n
    first = -1.25-t[:, None]*u
    second = (121/64)*u+1.25*t[:, None]
    out = np.empty((count, len(ys)), dtype=complex)
    for k, y in enumerate(ys):
        # Includes j=0 and the exact U*u-t_j*a denominator angle.
        out[:, k] = (-1.25/(-1.25+1j*y))*np.prod(
            (first/(first+1j*y))*(second-1j*y*t[:, None])/second,
            axis=0)
    return out


def nnls(a, target):
    count = a.shape[1]
    active = np.zeros(count, dtype=bool)
    b = np.zeros(count)
    issues = []
    iterations = 0
    last_singular = []
    while iterations < 20*count:
        gradient = a.T@(target-a@b)
        candidates = np.where(~active, gradient, -np.inf)
        if np.max(candidates) <= 2e-13:
            break
        active[np.argmax(candidates)] = True
        while True:
            trial = np.zeros(count)
            solution, _, rank, singular = np.linalg.lstsq(
                a[:, active], target, rcond=1e-14)
            trial[active] = solution
            last_singular = singular.tolist()
            iterations += 1
            if rank < np.sum(active):
                issues.append("rank-truncated active least-squares problem")
            if np.all(trial[active] > 0):
                b = trial
                break
            invalid = active & (trial <= 0)
            step = np.min(b[invalid]/(b[invalid]-trial[invalid]))
            b += step*(trial-b)
            release = active & (b <= 1e-15)
            b[release] = 0
            active[release] = False
            if iterations >= 20*count:
                break
        if iterations >= 20*count:
            issues.append("iteration cap reached")
    residual = a@b-target
    actions = a.T@residual
    return b, dict(iterations=iterations, active=np.flatnonzero(active).tolist(),
                   last_active_singular_values=last_singular,
                   min_scaled_action=float(np.min(actions)),
                   active_action_max=float(np.max(np.abs(actions[active])))
                   if np.any(active) else 0,
                   issues=sorted(set(issues)))


def rational_alias(n, count):
    # |a|<4/3, |a|>=5/4 and |x/a|<=1 in the entire allowed family.
    # Bounds hold on |u|=4/5 and 6/5, both in the pole-free annulus.
    bounds = []
    for radius in (F(4, 5), F(6, 5)):
        bound = F(1)
        for j in range(1, n):
            t = F(j, n)
            bound *= ((F(5, 4)+t*radius)/(F(5, 4)-t*radius)
                      * (F(121, 64)*radius+F(4, 3)*t)
                      / (F(121, 64)*radius-F(5, 4)*t))
        bounds.append(bound)
    degree = 2*n
    alias = (bounds[0]*F(4, 5)**(count-degree)/(1-F(4, 5)**count)
             + bounds[1]*F(5, 6)**(count-degree)/(1-F(5, 6)**count))
    threshold = F(1, 10**30)
    # Save the full exact rational in a separate text artifact; large JSON
    # integer strings are avoided in ordinary diagnostic output.
    return alias, bool(alias < threshold)


def run_case(q, pattern):
    n, e, ys = displacement(q, pattern)
    count = 1
    while count < 16*n+1024:
        count *= 2
    w = values(n, ys, count)
    frequencies = np.arange(-2*n, 2*n+1)
    hat = np.fft.fft(w, axis=0)/count
    projected = hat[frequencies % count]
    scale = np.linalg.norm(projected, axis=0)
    normalized = projected/scale
    design = np.concatenate((normalized.real, normalized.imag))
    anchor = np.zeros(len(frequencies), dtype=complex)
    anchor[2*n] = 1
    target = -np.concatenate((anchor.real, anchor.imag))
    scaled_b, diagnostics = nnls(design, target)
    b = scaled_b/scale
    residual_hat = anchor+projected@b
    projected_residual_norm = float(np.linalg.norm(residual_hat))
    normalization = float(residual_hat[2*n].real)
    issues = list(diagnostics["issues"])
    if normalization <= 0:
        issues.append("nonpositive anchor normalization")
    p = residual_hat/normalization
    polar_actions = (np.conjugate(p)@projected).real
    p_norm = float(np.linalg.norm(p))
    # A strictly positive-action repair is a distinct feasibility test.
    # Its zero real constant preserves ell(1)=1. Measured singular values
    # and small residuals are diagnostics, never assumed uniform bounds.
    free = np.ones(design.shape[0], dtype=bool)
    free[2*n] = False
    correction_real = np.zeros(design.shape[0])
    solution, _, repair_rank, repair_singular = np.linalg.lstsq(
        design[free].T, np.ones(len(ys)), rcond=1e-14)
    correction_real[free] = solution
    correction = (correction_real[:len(frequencies)]
                  + 1j*correction_real[len(frequencies):])
    repair_margin = max(1e-8, 100*float(np.max(np.abs(
        np.minimum((np.conjugate(p)@normalized).real, 0)))))
    repaired = p+repair_margin*correction
    repaired_actions = (np.conjugate(repaired)@projected).real
    repaired_normalized_actions = (np.conjugate(repaired)@normalized).real
    if repair_rank < len(ys):
        issues.append("rank-truncated positive-action correction")
    if np.min(repaired_actions) <= 0:
        issues.append("positive-action repair has nonpositive numerical action")
    residual = 1+w@b
    sampled_full_norm = float(np.linalg.norm(residual)/np.sqrt(count))
    alias, alias_pass = rational_alias(n, count)
    if not alias_pass:
        issues.append("exact-sample Fourier alias bound exceeds 1e-30")
    if np.min(b) < 0:
        issues.append("negative primal coefficient")
    # Negative numerical actions, even tiny ones, remain explicitly failures
    # of a claimed feasible separator. No positivity is inferred from tolerance.
    negative = np.flatnonzero(polar_actions < 0).tolist()
    row = dict(q=q, n=n, pattern=pattern, degree_each_direction=2*n,
               sample_count=count, displacements=e.tolist(), ordinates=ys.tolist(),
               primal_coefficients=b.tolist(), projected_column_norms=scale.tolist(),
               frequencies=frequencies.tolist(),
               polar_coefficients_real=p.real.tolist(),
               polar_coefficients_imag=p.imag.tolist(),
               numerical_polar_actions=polar_actions.tolist(),
               negative_numerical_action_indices=negative,
               correction_coefficients_real=correction.real.tolist(),
               correction_coefficients_imag=correction.imag.tolist(),
               correction_norm=float(np.linalg.norm(correction)),
               correction_singular_values=repair_singular.tolist(),
               correction_action_residual=float(np.max(np.abs(
                   design.T@correction_real-1))),
               repair_margin=repair_margin,
               repaired_coefficients_real=repaired.real.tolist(),
               repaired_coefficients_imag=repaired.imag.tolist(),
               repaired_numerical_actions=repaired_actions.tolist(),
               repaired_normalized_numerical_actions=repaired_normalized_actions.tolist(),
               repaired_polar_norm=float(np.linalg.norm(repaired)),
               min_repaired_numerical_action=float(np.min(repaired_actions)),
               min_repaired_normalized_action=float(np.min(repaired_normalized_actions)),
               repaired_anchor_action=float(repaired[2*n].real),
               polar_norm=p_norm, polar_log_norm_over_n=float(np.log(p_norm)/n),
               polar_log_norm_excess_over_log_n=float((np.log(p_norm)-n/100)/np.log(n)),
               polar_anchor_action=float(p[2*n].real),
               min_numerical_polar_action=float(np.min(polar_actions)),
               projected_residual_norm=projected_residual_norm,
               sampled_full_residual_norm=sampled_full_norm,
               projection_full_norm_difference=sampled_full_norm-projected_residual_norm,
               primal_dual_product=p_norm*projected_residual_norm,
               full_sampled_sup=float(np.max(np.abs(residual))),
               exact_sample_alias_lt_1e_minus_30=alias_pass,
               diagnostics=diagnostics, issues=issues)
    return row, alias


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--q", nargs="+", type=int, default=[4, 8, 16, 32])
    parser.add_argument("--patterns", nargs="+", default=["phase", "independent"])
    parser.add_argument("--output", type=Path, default=Path(__file__).with_suffix(".json"))
    args = parser.parse_args()
    # Exact rational artifacts can legitimately exceed Python's conversion cap.
    import sys
    sys.set_int_max_str_digits(0)
    rows, failures = [], []
    for q in args.q:
        for pattern in args.patterns:
            row, alias = run_case(q, pattern)
            certificate = args.output.with_name(args.output.stem+f"-n{row['n']}-{pattern}-alias.txt")
            certificate.write_text("Exact-sample Fourier alias upper bound only.\n"
                                   f"numerator={alias.numerator}\ndenominator={alias.denominator}\n"
                                   "required_upper_bound=1/10^30\n"
                                   f"passes={row['exact_sample_alias_lt_1e_minus_30']}\n")
            row["alias_artifact"] = str(certificate)
            exponent = len(str(alias.denominator))-len(str(alias.numerator))-1
            while alias.numerator*10**(exponent+1) <= alias.denominator:
                exponent += 1
            row["exact_sample_alias_upper_power_of_ten"] = -exponent
            rows.append(row)
            failures.extend(f"n={row['n']}, {pattern}: {issue}" for issue in row["issues"])
            if row["negative_numerical_action_indices"]:
                failures.append(f"n={row['n']}, {pattern}: unrepaired candidate has negative numerical actions; exact signs of the repair remain unverified")
            result = dict(status="EXPLORATORY ONLY: floating moments/actions and no uniform-in-displacement proof",
                          required="all exact polar actions >=0, anchor action 1, continuous norm <=exp(n/100)*n^C with absolute C/onset",
                          exact_sample_alias_scope="Cauchy annulus bound only; floating errors not enclosed",
                          failure_scope="negative-action failures concern unrepaired candidates; all repaired exact signs remain unverified",
                          summary=dict(
                              cases=len(rows),
                              min_repaired_norm=min(r["repaired_polar_norm"] for r in rows),
                              max_repaired_norm=max(r["repaired_polar_norm"] for r in rows),
                              min_repaired_normalized_action=min(r["min_repaired_normalized_action"] for r in rows),
                              max_correction_norm=max(r["correction_norm"] for r in rows),
                              unrepaired_negative_case_count=sum(bool(r["negative_numerical_action_indices"]) for r in rows),
                              repaired_nonpositive_numerical_case_count=sum(r["min_repaired_numerical_action"] <= 0 for r in rows),
                              alias_check_failures=sum(not r["exact_sample_alias_lt_1e_minus_30"] for r in rows),
                              solver_issue_case_count=sum(bool(r["issues"]) for r in rows)),
                          failures=failures, rows=rows)
            args.output.write_text(json.dumps(result, indent=2)+"\n")
            print(f"n={row['n']} {pattern}: ||p||={row['polar_norm']:.8g}, "
                  f"log||p||/n={row['polar_log_norm_over_n']:.6g}, "
                  f"min action={row['min_numerical_polar_action']:.3g}, "
                  f"negative actions={len(row['negative_numerical_action_indices'])}, "
                  f"repaired ||p||={row['repaired_polar_norm']:.8g}, "
                  f"repaired min normalized action={row['min_repaired_normalized_action']:.3g}, "
                  f"alias<=1e-{exponent} (required <1e-30), "
                  f"solver issues={row['issues']}", flush=True)
    print("Required rate: 1/100 plus an absolute polynomial factor, all displacements, exact signs. "
          f"Recorded failures: {len(failures)}. Full artifact: {args.output}")


if __name__ == "__main__":
    main()
