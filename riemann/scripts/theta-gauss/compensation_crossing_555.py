"""One finite actual n=2,d=5 event; exact rational validation, no theta evaluation.

The candidate phase is executed once and saved. Numpy proposes an elimination
root and at most twenty Newton iterations; it supplies no mathematical evidence.
Validation uses the saved proposal, audited input boxes and Fraction arithmetic.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import sys
import numpy as np

from two_node_540 import I, power
import reference_roots_551 as roots

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('compensation-crossing-certificate-555.json')
checks, failures = [], []


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def check(name, passed):
    checks.append({'name': name, 'passed': bool(passed)})
    if not passed:
        failures.append(name)


def load(name):
    p = ROOT/name
    hashes[name] = digest(p)
    return json.loads(p.read_text())


def coarse(a, digits=40):
    s = 10**digits
    b = I(F((a.lo*s).__floor__(), s), F((a.hi*s).__ceil__(), s))
    check('outward coarsening', b.lo <= a.lo <= a.hi <= b.hi)
    return b


def mid(a):
    return (a.lo+a.hi)/2


def ab(a):
    return max(abs(a.lo), abs(a.hi))


def derivative(c):
    return [c[j]*j for j in range(1, len(c))]


def evaluate(c, x):
    v = I(0)
    for a in c[::-1]:
        v = v*x+a
    return v


def family(q, e, tau):
    return [a+tau*b for a, b in zip(q, e)]


def simple_box(a, digits=9):
    b = coarse(a, digits)
    return b.pair()


def pair_pellet(c, center, radius):
    # Real center; enclosures hold for every tau in the selected interval.
    tay = [sum((c[j]*comb(j, k)*center**(j-k) for j in range(k, 6)), I(0))
           for k in range(6)]
    lower2 = 0 if tay[2].lo <= 0 <= tay[2].hi else min(abs(tay[2].lo), abs(tay[2].hi))
    lower = lower2*radius**2
    terms = [ab(tay[k])*radius**k if k != 2 else F(0) for k in range(6)]
    upper = sum(terms)
    return {'center': str(center), 'radius': str(radius), 'k': 2,
            'taylor_coefficients': [a.pair() for a in tay],
            'dominant_lower': str(lower), 'other_upper_terms': list(map(str, terms)),
            'other_upper_sum': str(upper), 'margin': str(lower-upper),
            'accepted': lower > upper}


def save(report):
    report['checks'], report['failures'] = checks, failures
    report['input_hashes'] = hashes
    report['program_sha256'] = digest(Path(__file__))
    report['status'] = 'PASS' if not failures else 'FAIL'
    OUT.write_text(json.dumps(report, indent=2)+'\n')


hashes = {}


def main():
    inherited_name = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    inherited = load(inherited_name)
    original = load('scripts/central-jacobi/fixed-model-certificate-476.json')
    a433 = load('scripts/actual-fredholm/audit-433/audit-report.json')
    a478 = load('scripts/central-jacobi/audit-478/audit-report.json')
    a542 = load('scripts/theta-gauss/audit-certificate-542.json')
    r551 = load('scripts/theta-gauss/reference-roots-certificate-551.json')
    a553 = load('scripts/theta-gauss/reference-audit-certificate-553.json')
    for name, record in [('433', a433), ('478', a478), ('542', a542), ('553', a553)]:
        check('inherited audit '+name+' PASS/no failures', record['status'] == 'PASS' and not record['failures'])
        if name != '433':
            check('all inherited audit '+name+' checks', all(v['passed'] for v in record['checks']))
    for mapping in [a478['original_hashes'], a542['evidence']['input_hashes'],
                    r551['input_hashes'], a553['evidence']['source_hashes']]:
        for name, expected in mapping.items():
            hashes[name] = digest(ROOT/name)
            check('inherited source hash '+name, hashes[name] == expected)
    check('fixed inherited original digest', hashes[inherited_name] ==
          '2c0aae858cc1e15b17e46dff0e1b81fa41582b4c84f5d74e3477fb72399335de')
    check('original source SHA agrees with audits', hashes[inherited_name] == original['source_sha256'] == a433['original_sha256'])
    replay = load('scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')
    check('entire inherited evaluator equals audited replay', inherited['evaluation'] == replay['evaluation'])
    for filename, record in [('scripts/theta-gauss/audit_542.py', a542),
                             ('scripts/theta-gauss/reference_roots_551.py', r551),
                             ('scripts/theta-gauss/reference_audit_553.py', a553)]:
        hashes[filename] = digest(ROOT/filename)
        check('audited implementation '+filename, hashes[filename] == record['program_sha256'])
    hashes['scripts/theta-gauss/two_node_540.py'] = digest(ROOT/'scripts/theta-gauss/two_node_540.py')
    check('imported interval code provenance', hashes['scripts/theta-gauss/two_node_540.py'] == r551['input_hashes']['scripts/theta-gauss/two_node_540.py'])
    ev = inherited['evaluation']
    check('complex Cauchy radius', F(ev['uniform_disk_radius']) == 1600)
    err = I(*ev['uniform_G_error'])
    check('uniform analytic error', 0 < err.lo <= err.hi < F('3.141e-48'))
    actual_a, gamma = [], []
    for j in range(6):
        poly = I(*ev['coefficients'][j])
        correction = err.hi/F(1600)**j
        actual_a.append(poly+I(-correction, correction))
        gamma.append(actual_a[-1]*(8*4**j*factorial(j)))
        check('positive actual gamma '+str(j), gamma[-1].lo > 0)
        if j < 5:
            old_a, old_g = I(*original['actual_a'][j]), I(*original['gamma'][j])
            check('exact coefficient contained in audited Decimal order '+str(j),
                  old_a.lo <= actual_a[-1].lo <= actual_a[-1].hi <= old_a.hi)
            check('exact gamma contained in audited Decimal order '+str(j),
                  old_g.lo <= gamma[-1].lo <= gamma[-1].hi <= old_g.hi)
    full_nodes = [I(*v) for v in a542['evidence']['independent_nodes']]
    full_weights = [I(*v) for v in a542['evidence']['independent_weights']]
    check('node/weight boxes agree with reference audit',
          [v.pair() for v in full_nodes] == a553['evidence']['input_nodes_full'] and
          [v.pair() for v in full_weights] == a553['evidence']['input_weights_full'])
    nodes, weights = [coarse(v) for v in full_nodes], [coarse(v) for v in full_weights]
    check('positive ordered Gaussian input boxes', 0 < nodes[0].lo <= nodes[0].hi < nodes[1].lo and all(w.lo > 0 for w in weights))
    t = [I(1)]+[gamma[j]/gamma[0]*F(factorial(2*j), factorial(j)) for j in range(1, 6)]
    s = [I(1)]+[sum((weights[i]*power(nodes[i], j) for i in range(2)), I(0)) for j in range(1, 6)]
    p = [I(1)]+[coarse(gamma[j]/gamma[0]*((-1)**j*comb(5, j)), 50) for j in range(1, 6)]
    factors = [F((-1)**j*comb(5, j)*factorial(j), factorial(2*j)) for j in range(6)]
    q = [I(1)]+[coarse(s[j]*factors[j], 50) for j in range(1, 6)]
    e = [I(0) for _ in range(4)]+[coarse(p[j]-q[j], 50) for j in (4, 5)]
    # Exact zeros here use Gaussian exactness through order three, L805/L807.
    h, defect5 = t[4]-s[4], t[5]-s[5]
    b, transition = defect5/h, 90*h/defect5
    check('strict signed compensation and transition', h.lo > 0 and defect5.lo > 0 and e[4].lo > 0 and e[5].hi < 0 and transition.lo > 0)
    check('error ratio agrees with transition enclosure', not (
        (e[4]/(-e[5])).hi < transition.lo or transition.hi < (e[4]/(-e[5])).lo))
    report = {'outcome': 'INPUTS_ONLY', 'analytic_error': err.pair(),
              'actual_a': [v.pair() for v in actual_a], 'gamma': [v.pair() for v in gamma],
              'raw_moments': [v.pair() for v in t], 'gaussian_moments': [v.pair() for v in s],
              'nodes': [v.pair() for v in nodes], 'weights': [v.pair() for v in weights],
              'P_coefficients': [v.pair() for v in p], 'Q_coefficients': [v.pair() for v in q],
              'E_coefficients': [v.pair() for v in e],
              'h2': h.pair(), 'B2': b.pair(), 'X2': transition.pair(),
              'qualifications': 'Audited L778/L791/L805/L807/L808 input and backend contracts retained; Fraction code trusted, not formal verification.'}
    save(report)
    if failures:
        print('INPUT FAILURE:', failures, 'complete evidence:', OUT.relative_to(ROOT))
        return
    if '--validate' in sys.argv:
        previous = json.loads(OUT.with_name('compensation-proposal-555.json').read_text())
        check('proposal fixed input hashes', previous['input_hashes'] == hashes)
        proposal = previous['proposal']
    else:
        # One elimination polynomial proposal, never used as evidence.
        qm, em = [float(mid(v)) for v in q], [float(mid(v)) for v in e]
        pol = np.polynomial.polynomial
        eliminant = pol.polysub(pol.polymul(pol.polyder(qm), em), pol.polymul(qm, pol.polyder(em)))
        candidates = []
        for z in pol.polyroots(eliminant[3:]):
            if abs(z.imag) < 1e-7 and z.real > 0:
                x = float(z.real)
                tau = -pol.polyval(x, qm)/pol.polyval(x, em)
                if 0 < tau < 1:
                    candidates.append((x, float(tau)))
        if not candidates:
            report['outcome'] = 'NO_PROPOSAL'
            save(report)
            print('NO PROPOSAL; complete evidence:', OUT.relative_to(ROOT))
            return
        x, tau = sorted(candidates)[0]
        iterations = []
        for _ in range(20):
            hm = np.array(qm)+tau*np.array(em)
            values = np.array([pol.polyval(x, hm), pol.polyval(x, pol.polyder(hm))])
            jac = np.array([[values[1], pol.polyval(x, em)],
                            [pol.polyval(x, pol.polyder(hm, 2)), pol.polyval(x, pol.polyder(em))]])
            dx = np.linalg.solve(jac, values)
            x, tau = x-dx[0], tau-dx[1]
            iterations.append({'x': float(x), 'tau': float(tau), 'residual_before': list(map(float, values))})
            if max(abs(dx)) < 1e-11:
                break
        proposal = {'elimination_candidates_unvalidated': candidates, 'newton_iterations_unvalidated': iterations,
                    'x0': str(round(float(x), 12)), 'tau0': str(round(float(tau), 12))}
        OUT.with_name('compensation-proposal-555.json').write_text(json.dumps({'input_hashes': hashes, 'proposal': proposal}, indent=2)+'\n')
    report['proposal'] = proposal
    save(report)
    validate(report, p, q, e, transition)


def validate(report, p, q, e, transition):
    proposal = report['proposal']
    x0, tau0 = F(proposal['x0']), F(proposal['tau0'])
    center = [I(x0), I(tau0)]
    # One candidate box, no refinement needed if the inequalities below pass.
    radius = F('0.0000001')
    xb, tb = I(x0-radius, x0+radius), I(tau0-radius, tau0+radius)
    hc = family(q, e, center[1])
    hbox = family(q, e, tb)
    dq, de = derivative(q), derivative(e)
    residual = [evaluate(hc, center[0]), evaluate(derivative(hc), center[0])]
    jac = [[evaluate(derivative(hbox), xb), evaluate(e, xb)],
           [evaluate(derivative(derivative(hbox)), xb), evaluate(de, xb)]]
    # Inverse of a point matrix selected inside the interval center Jacobian.
    jc = [[evaluate(derivative(hc), center[0]), evaluate(e, center[0])],
          [evaluate(derivative(derivative(hc)), center[0]), evaluate(de, center[0])]]
    jm = [[mid(v) for v in row] for row in jc]
    det = jm[0][0]*jm[1][1]-jm[0][1]*jm[1][0]
    check('point Jacobian determinant nonzero', det != 0)
    a = [[jm[1][1]/det, -jm[0][1]/det], [-jm[1][0]/det, jm[0][0]/det]]
    adet = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    check('preconditioner invertible', adet != 0)
    ar = [sum((a[i][j]*residual[j] for j in range(2)), I(0)) for i in range(2)]
    k = [[I(int(i == j))-sum((a[i][l]*jac[l][j] for l in range(2)), I(0))
          for j in range(2)] for i in range(2)]
    y = [ab(v) for v in ar]
    rownorm = [sum(ab(v) for v in row) for row in k]
    z = [r*radius for r in rownorm]
    margins = [radius-y[i]-z[i] for i in range(2)]
    check('strict contraction in both coordinates', all(r < 1 for r in rownorm))
    check('strict self-map in both coordinates', all(m > 0 for m in margins))
    etest, xx = evaluate(e, xb), jac[1][0]
    check('fold interior positive x and parameter', xb.lo > 0 and 0 < tb.lo < tb.hi < 1)
    check('fold derivatives E positive Hxx negative', etest.lo > 0 and xx.hi < 0)
    event_ratio = xb/transition
    report['event'] = {'center': [str(x0), str(tau0)], 'radius': str(radius),
                       'x_box': xb.pair(), 'tau_box': tb.pair(),
                       'residual': [v.pair() for v in residual],
                       'center_Jacobian': [[v.pair() for v in row] for row in jc],
                       'whole_box_Jacobian': [[v.pair() for v in row] for row in jac],
                       'point_Jacobian': [[str(v) for v in row] for row in jm],
                       'point_determinant': str(det), 'preconditioner_determinant': str(adet),
                       'preconditioner': [[str(v) for v in row] for row in a],
                       'I_minus_AJ': [[v.pair() for v in row] for row in k],
                       'preconditioned_residual': [v.pair() for v in ar],
                       'Y': list(map(str, y)), 'row_norms': list(map(str, rownorm)),
                       'Z': list(map(str, z)), 'self_map_margins': list(map(str, margins)),
                       'partial_tau_H': etest.pair(), 'partial_x2_H': xx.pair(),
                       'x_over_X2': event_ratio.pair()}
    save(report)
    if failures:
        report['outcome'] = 'FOLD_VALIDATION_INCONCLUSIVE'
        save(report)
        print('INCONCLUSIVE:', failures, 'complete evidence:', OUT.relative_to(ROOT))
        return
    # A single quantitative neighborhood enclosing the event box strictly.
    delta, pair_radius = F('0.000001'), F(1, 10)
    slab = I(tau0-delta, tau0+delta)
    segment = I(x0-pair_radius, x0+pair_radius)
    hs = family(q, e, slab)
    check('slab interior and degree five throughout', 0 < slab.lo < tb.lo < tb.hi < slab.hi < 1 and hs[5].hi < 0)
    pair_test = pair_pellet(hs, x0, pair_radius)
    check('two roots in fixed disk throughout parameter slab', pair_test['accepted'])
    # One midpoint root list proposes only the three other disks; no tracking.
    other_proposal = np.roots([float(mid(v)) for v in hc][::-1])
    other_centers = sorted((F(str(round(float(z.real), 6))), F(str(round(float(z.imag), 6))))
                           for z in other_proposal if abs(complex(z)-float(x0)) > 2)
    other_tests = [roots.pellet([(v.lo, v.hi) for v in hs], c, F(1, 10)) for c in other_centers]
    check('three remaining uniform simple-root disks', len(other_tests) == 3 and all(v['accepted'] for v in other_tests))
    distances = [(c[0]-x0)**2+c[1]**2-(pair_radius+F(1, 10))**2 for c in other_centers]
    distances += [(a[0]-b[0])**2+(a[1]-b[1])**2-F(1, 5)**2 for i, a in enumerate(other_centers) for b in other_centers[i+1:]]
    check('all four disks disjoint', all(v > 0 for v in distances))
    check('real disks positive and nonreal disks off axis', segment.lo > 0 and all(
        c[0] > F(1, 10) if c[1] == 0 else abs(c[1]) > F(1, 10) for c in other_centers))
    concavity = evaluate(derivative(derivative(hs)), segment)
    e_segment = evaluate(e, segment)
    left_value, right_value = evaluate(hs, I(segment.lo)), evaluate(hs, I(segment.hi))
    left_slope = evaluate(derivative(hs), I(segment.lo))
    right_slope = evaluate(derivative(hs), I(segment.hi))
    check('uniform strict concavity', concavity.hi < 0)
    check('uniform increasing compensation', e_segment.lo > 0)
    check('uniform negative segment endpoints', left_value.hi < 0 and right_value.hi < 0)
    check('unique interior maximum throughout slab', left_slope.lo > 0 and right_slope.hi < 0)
    side_records = {}
    for side, tau in [('lower', slab.lo), ('upper', slab.hi)]:
        hside = family(q, e, I(tau))
        at_center = evaluate(hside, I(x0))
        slope_center = evaluate(derivative(hside), I(x0))
        curvature = evaluate(derivative(derivative(hside)), segment)
        side_records[side] = {'tau': str(tau), 'center_value': at_center.pair(),
                              'center_slope': slope_center.pair(), 'curvature': curvature.pair(),
                              'left_value': evaluate(hside, I(segment.lo)).pair(),
                              'right_value': evaluate(hside, I(segment.hi)).pair()}
        if side == 'lower':
            m = -curvature.hi
            upper_maximum = at_center.hi+ab(slope_center)**2/(2*m)
            side_records[side]['global_segment_maximum_upper'] = str(upper_maximum)
            check('lower side no real root in pair disk', upper_maximum < 0)
        else:
            check('upper side two positive sign brackets', at_center.lo > 0 and
                  evaluate(hside, I(segment.lo)).hi < 0 and evaluate(hside, I(segment.hi)).hi < 0)
    report['local_orientation'] = {'parameter_slab': slab.pair(), 'real_segment': segment.pair(),
                                   'pair_pellet': pair_test, 'other_centers': [list(map(str, c)) for c in other_centers],
                                   'initial_failed_neighborhood': 'scripts/theta-gauss/compensation-crossing-initial-555.json',
                                   'refinement': 'Sole refinement: pair disk radius 1 -> 1/10; same event box/slab. Correct other-root proposal selection to include nonreal roots.',
                                   'other_pellet': other_tests, 'squared_disjointness_margins': list(map(str, distances)),
                                   'uniform_Hxx': concavity.pair(), 'uniform_E': e_segment.pair(),
                                   'uniform_endpoint_values': [left_value.pair(), right_value.pair()],
                                   'uniform_endpoint_slopes': [left_slope.pair(), right_slope.pair()],
                                   'side_tests': side_records}
    check('simple contraction bounds', rownorm[0] < F('1e-5') and rownorm[1] < F('4e-8') and
          y[0]+z[0] < F('1.4e-12') and y[1]+z[1] < F('3e-13'))
    check('simple uniform sign margins', concavity.lo > F('-.000304') and concavity.hi < F('-.000155') and
          e_segment.lo > F('.409') and left_value.hi < F('-2e-7') and right_value.hi < F('-2e-7') and
          left_slope.lo > F('2.28e-5') and right_slope.hi < F('-2.28e-5'))
    check('simple strict side margins', F(side_records['lower']['global_segment_maximum_upper']) < F('-4e-7') and
          F(side_records['upper']['center_value'][0]) > F('4.1e-7'))
    check('simple pair Pellet ratio', F(pair_test['dominant_lower']) > F('1.2')*F(pair_test['other_upper_sum']))
    report['simple_uniform_bounds'] = {
        'Hxx_strictly_between': ['-.000304', '-.000155'], 'E_greater_than': '.409',
        'endpoint_values_less_than': '-2e-7', 'left_slope_greater_than': '2.28e-5',
        'right_slope_less_than': '-2.28e-5', 'lower_maximum_less_than': '-4e-7',
        'upper_center_value_greater_than': '4.1e-7', 'pair_Pellet_ratio_greater_than': '1.2'}
    check('source files unchanged', all(digest(ROOT/n) == h for n, h in hashes.items()))
    report['outcome'] = 'CERTIFIED_LOCAL_NONREAL_TO_REAL_FOLD' if not failures else 'ORIENTATION_INCONCLUSIVE'
    report['simple_bounds'] = {'tau': simple_box(tb), 'x': simple_box(xb),
                               'x_over_X2': simple_box(event_ratio), 'X2': simple_box(transition),
                               'E_at_event': simple_box(etest), 'Hxx_at_event': simple_box(xx)}
    save(report)
    print(report['status'], report['outcome'], 'checks', len(checks), 'failures', failures)
    print('Actual / required: row norms', [float(v) for v in rownorm], '< 1; Y+Z',
          [float(y[i]+z[i]) for i in range(2)], '< radius', float(radius))
    print('Event enclosures:', report['simple_bounds'])
    print('Pair Pellet dominant/other ratio:', float(F(pair_test['dominant_lower'])/F(pair_test['other_upper_sum'])), '> 1')
    print('Complete certificate:', OUT.relative_to(ROOT))


if __name__ == '__main__':
    main()
