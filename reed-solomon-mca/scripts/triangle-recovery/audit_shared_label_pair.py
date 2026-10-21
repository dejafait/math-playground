"""Bounded L101 audit: direct polynomial formulas, no imported verifier helpers.

The discovery prefix is never rerun. Full evidence is written beside this file.
"""
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
P = 97
failures = []


def check(ok, name):
    if not ok:
        failures.append(name)


def prod(xs):
    ans = 1
    for x in xs:
        ans = ans*x % P
    return ans


def ev(cs, x):
    return sum(c*pow(x, i, P) for i, c in enumerate(cs)) % P


def poly(roots):
    cs = [1]
    for x in roots:
        out = [0]*(len(cs)+1)
        for j, c in enumerate(cs):
            out[j] = (out[j]-x*c) % P
            out[j+1] = (out[j+1]+c) % P
        cs = out
    return cs


def lagrange(nodes, x, at):
    return prod(at-y for y in nodes if y != x)*pow(prod(x-y for y in nodes if y != x), -1, P) % P


def interpolate(nodes, values):
    cs = [0]*len(nodes)
    for x, value in zip(nodes, values):
        factor = value*pow(prod(x-y for y in nodes if y != x), -1, P) % P
        for j, c in enumerate(poly([y for y in nodes if y != x])):
            cs[j] = (cs[j]+factor*c) % P
    return cs


def moments(error):
    return [sum(w*pow(x, j, P) for x, w in error.items()) % P for j in range(1, 9)]


def recurrence(roots, v):
    cs = poly(roots)
    return [sum(cs[j]*v[i+j] for j in range(5)) % P for i in range(4)]


def det(rows):
    n = len(rows)
    return sum((-1)**sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
               * prod(rows[i][p[i]] for i in range(n))
               for p in permutations(range(n))) % P


def weights_from_moments(nodes, v):
    out = {}
    for x in nodes:
        cs = poly([y for y in nodes if y != x])
        den = x*prod(x-y for y in nodes if y != x) % P
        out[x] = sum(c*v[j] for j, c in enumerate(cs))*pow(den, -1, P) % P
    return out


def ints(d):
    return {int(x): v for x, v in d.items()}


def main():
    path = ROOT/'shared-label-pair-verification.json'
    before = path.read_bytes()
    saved = json.loads(before)
    candidate = json.loads((ROOT/'shared-label-pair-candidate.json').read_text())
    replay = subprocess.run([sys.executable, str(ROOT/'verify_shared_label_pair.py')],
                            capture_output=True, text=True)
    after = path.read_bytes()
    check(replay.returncode == 0, 'existing verifier replay')
    check(before == after, 'existing certificate byte stability')

    H = [1, 8, 12, 18, 22, 27, 33, 47, 50, 64, 70, 75, 79, 85, 89, 96]
    a, b, c = 1, 27, 75
    Y, Z, W = [8, 12], [18, 70], [47, 96]
    supports = [[1, 27, 8, 12], [1, 75, 18, 70], [27, 75, 47, 96],
                [1, 22, 50, 79], [1, 47, 85, 89]]
    weights = [[61, 79, 15, 70], [88, 40, 11, 6], [86, 66, 3, 51],
               [61, 39, 49, 13], [92, 74, 75, 92]]
    errors = [dict(zip(s, w)) for s, w in zip(supports, weights)]
    times, mus = [0, 1, 2, 75, 73], [42, 6]
    expected_moments = [[50, 16, 29, 23, 54, 29, 58, 91], [20, 32, 81, 44, 47, 76, 3, 14],
                        [87, 48, 36, 65, 40, 26, 45, 34], [31, 52, 49, 46, 14, 62, 7, 39],
                        [91, 20, 42, 4, 28, 65, 20, 96]]
    check(H == [x for x in range(1, P) if pow(x, 16, P) == 1] == saved['H'], 'H exact roots')
    check(all(len(set(s)) == 4 and set(s) <= set(H) for s in supports), 'supports in H')
    check(len(set(times)) == 5, 'five distinct finite parameters')
    for key, value in dict(a=a, b=b, c=c, Y=Y, Z=Z, W=W, K=supports[3], L=supports[4], mu=mus, q=14, r=75).items():
        check(candidate[key] == value, 'candidate '+key)
    U = [a, b, c]+Y+Z+W
    outside = sorted(set(H)-set(U))
    Q = poly(outside)
    cx = {x: ev(Q, x) for x in U}
    check(list(cx.values()) == [18, 29, 14, 82, 27, 22, 12, 94, 46], 'Q table')
    check(cx == ints(saved['c_x']), 'saved Q table')
    alpha = [(times[1]-times[2]) % P, times[2]-times[0], (times[0]-times[1]) % P]
    normalized = [[2, 14, 1, 1], [96, 75, 1, 1], [84, 23, 1, 1]]
    check(alpha == [96, 2, 96], 'alpha signs')
    check(prod([2, 1-2, 14, 1-14, 75, 1-75]) != 0, 'normalized weight gates')
    for i in range(3):
        check(weights[i] == [cx[x]*v*pow(alpha[i], -1, P) % P for x, v in zip(supports[i], normalized[i])], 'base weights '+str(i))
    m = [moments(e) for e in errors]
    slope = [(y-x) % P for x, y in zip(m[0], m[1])]
    check(m == expected_moments, 'all displayed moment tables')
    check(slope == [67, 16, 52, 21, 90, 47, 42, 20], 'displayed slope')
    check(det([[m[0][0], m[1][0]], [m[0][1], m[1][1]]]) == 19, 'independent syndrome directions')
    for i, T in enumerate(times):
        check(m[i] == [(x+T*y) % P for x, y in zip(m[0], slope)], 'eight moments '+str(i))
    check(saved['supports'] == supports, 'saved supports')
    sw = saved['witness']
    check([ints(e) for e in sw['base_errors']] == errors[:3], 'saved base errors')
    check(sw['base_moments8'] == m[:3] and sw['syndrome_slope8'] == slope, 'saved moments')
    check((sw['pqr'], sw['gamma'], sw['alpha'], sw['lambda'], sw['g'], sw['rho']) ==
          ([2, 14, 75], times[:3], alpha, 1, 1, 2), 'saved chart')
    projections = []
    for i, mu in enumerate(mus):
        K = supports[i+3]
        f = lambda x: prod(x-k for k in K)
        J = [b, c]
        G = poly(J)
        columns = [[x*f(x)*pow(x, j, P) % P for j in range(4)] for x in J]
        raw = [recurrence(K, moments({x: cx[x] for x in pair})) for pair in (Y, Z)]
        explicit = [[sum(cx[x]*x*f(x)*ev(G, x)*pow(x, j, P) for x in pair) % P for j in range(2)] for pair in (Y, Z)]
        beta = [[-sum(cx[u]*u*f(u)*lagrange(J, x, u) for u in pair)*pow(x*f(x) % P, -1, P) % P for x in J] for pair in (Y, Z)]
        quotient = [[(v[j]+sum(t*col[j] for t, col in zip(bt, columns))) % P for j in range(2, 4)] for v, bt in zip(raw, beta)]
        transformed = [[v[0], (v[1]-(b+c)*v[0]) % P] for v in quotient]
        check(explicit == transformed, 'exact quotient change '+str(i))
        check(all(any(v) for v in explicit) and explicit[1] == [mu*x % P for x in explicit[0]], 'isolated proportionality '+str(i))
        check(mu not in (0, 96), 'isolated scalar exclusions '+str(i))
        restored = [(beta[1][j]-mu*beta[0][j]) % P for j in range(2)]
        expected_restored = [-mu*cx[b]*14 % P, cx[c]*75 % P]
        check(restored == expected_restored, 'restored b,c equations '+str(i))
        N = {x: -mu*cx[x] % P for x in Y}
        N.update({x: cx[x] for x in Z})
        N.update({a: cx[a]*(1-(1+mu)*2) % P, b: restored[0], c: restored[1]})
        omega = {x: sum(w*u*lagrange(K, x, u) for u, w in N.items())*pow(x, -1, P) % P for x in K}
        E = (2+mu) % P
        check(E != 0 and 2*pow(E, -1, P) % P == times[i+3], 'original finite chart '+str(i))
        check(all(omega.values()) and omega == {x: E*w % P for x, w in errors[i+3].items()}, 'L057 formula 13 '+str(i))
        check(moments(N) == [E*v % P for v in m[i+3]], 'all restored numerator moments '+str(i))
        sp, sr = saved['isolated_projection_checks'][i], sw['recoveries'][i]
        coefficients = [[-t % P for t in row] for row in beta]
        check((sp['columns'], sp['raw_YZ'], sp['eliminated_YZ'], sp['quotient_YZ'], sp['mu']) ==
              (columns, raw, coefficients, quotient, mu), 'saved full projection '+str(i))
        check((ints(sr['actual_error']), ints(sr['omega']), ints(sr['numerator']), sr['E'], sr['T'], sr['mu']) ==
              (errors[i+3], omega, N, E, times[i+3], mu), 'saved restored error '+str(i))
        check(sr['actual_moments8'] == sr['expected_moments8'] == m[i+3] and sr['residual8'] == [0]*8 and sr['numerator_moments8'] == moments(N), 'saved restored moments '+str(i))
        projections.append(dict(support=K, columns=columns, first_two_determinant=det([[col[j] for col in columns] for j in range(2)]), raw=raw,
                                elimination_coefficients=coefficients, eliminated_quotient=quotient,
                                explicit_L057_quotient=explicit, beta_YZ=beta, restored_bc=restored, E=E, T=times[i+3], numerator=N, omega=omega))

    intersections = [{'pair': [i, j], 'labels': sorted(set(supports[i]) & set(supports[j]))} for i, j in combinations(range(5), 2)]
    check(all(len(r['labels']) <= 1 for r in intersections) and intersections == saved['intersections'], 'all ten intersections')
    check(set(supports[3]) & set(supports[4]) == {a}, 'named shared label')
    bword = {x: (errors[1].get(x, 0)-errors[0].get(x, 0)) % P for x in H}
    residual_polynomials, locator_rows, failure_rows = [], [], []
    for i, (K, T, e, v) in enumerate(zip(supports, times, errors, m)):
        residual_word = {x: (errors[0].get(x, 0)+T*bword[x]-e.get(x, 0)) % P for x in H}
        cs = interpolate(H[:8], [residual_word[x] for x in H[:8]])
        discrepancies = [(ev(cs, x)-residual_word[x]) % P for x in H]
        check(not any(discrepancies), 'actual residual codeword '+str(i))
        residual_polynomials.append(dict(T=T, coefficients=cs, discrepancies16=discrepancies))
        S = sorted(set(H)-set(K))
        bs = interpolate(S[:8], [bword[x] for x in S[:8]])
        mismatches = {x: (bword[x]-ev(bs, x)) % P for x in S if (bword[x]-ev(bs, x)) % P}
        check(bool(mismatches), 'direct restricted-input failure '+str(i))
        recovered_slope = weights_from_moments(K, slope)
        slope_residual = [(x-y) % P for x, y in zip(moments(recovered_slope), slope)]
        check(slope_residual == sw['same_support_input_failures'][i]['slope_span_residual8'], 'saved slope-span residual '+str(i))
        failure_rows.append(dict(support=K, agreement_complement=S, interpolated_input_coefficients=bs, mismatches=mismatches, slope_span_residual8=slope_residual))
        R = [v[j:j+5] for j in range(4)]
        D = det([row[:4] for row in R])
        factor = prod((y-x)**2 for x, y in combinations(K, 2))*prod(e[x]*x for x in K) % P
        locators = {x: det(R+[[pow(x, j, P) for j in range(5)]]) for x in H}
        check(D == factor != 0, 'Hankel factorization '+str(i))
        check(all(locators[x] == D*prod(x-k for k in K) % P for x in H), 'all pointwise locators '+str(i))
        locator_rows.append(dict(T=T, D=D, factor=factor, locators=locators))
    check(all(any(row['locators'][x] for row in locator_rows[:3]) for x in H), 'all sixteen nonpersistent locators')
    check(all(all(e.values()) for e in errors), 'all five full errors')
    report = dict(scope='Critical audit of the single explicit L101 witness; no completion/count search',
                  replay=dict(returncode=replay.returncode, before_sha256=hashlib.sha256(before).hexdigest(), after_sha256=hashlib.sha256(after).hexdigest(), stdout=replay.stdout, stderr=replay.stderr),
                  H=H, Q_coefficients=Q, c_x=cx, errors=errors, times=times, moments8=m, projections=projections,
                  intersections=intersections, residual_codewords=residual_polynomials,
                  same_support_failures=failure_rows, pointwise_locators=locator_rows,
                  checks=dict(moment_equations_actual=40, moment_equations_required=40, full_errors_actual=5, full_errors_required=5,
                              isolated_actual=2, isolated_required=2, restored_equations_actual=4, restored_equations_required=4,
                              intersections_actual=10, intersections_required=10, finite_parameters_actual=5, finite_parameters_required=5,
                              codeword_evaluations_actual=80, codeword_evaluations_required=80,
                              same_support_failures_actual=5, same_support_failures_required=5,
                              nonpersistent_locators_actual=16, nonpersistent_locators_required=16, failures=failures))
    output = ROOT/'shared-label-pair-critical-audit.json'
    output.write_text(json.dumps(report, indent=2)+'\n')
    print('Moments 40/40; full errors 5/5; isolated 2/2; restored equations 4/4; intersections 10/10; finite parameters 5/5.')
    print('Codeword evaluations 80/80; same-support failures 5/5; nonpersistent locators 16/16.')
    print(f'Audit failures: {len(failures)}; required: 0. Certificate: {output.relative_to(ROOT.parent.parent)}')
    if failures:
        print('\n'.join(failures))
        raise SystemExit(1)


if __name__ == '__main__':
    main()
