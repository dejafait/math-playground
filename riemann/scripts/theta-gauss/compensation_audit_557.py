"""Independent exact audit of L809; no producer imports or fresh theta evaluation.

All input decimal endpoints are exact Fractions. The audited L778 complex
analytic estimate and its software contracts are inherited premises.
Complete rational reconstructions, not saved acceptance flags, decide the audit.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).with_name('compensation-audit-certificate-557.json')
checks, failures, hashes, evidence = [], [], {}, {}


def check(name, ok):
    checks.append({'name': name, 'passed': bool(ok)})
    if not ok:
        failures.append(name)


def sha(name):
    result = hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    hashes[name] = result
    return result


def load(name):
    sha(name)
    return json.loads((ROOT/name).read_text())


def box(v):
    a, b = map(F, v)
    assert a <= b
    return a, b


def pt(x):
    return F(x), F(x)


def add(a, b):
    return a[0]+b[0], a[1]+b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    products = (a[0]*b[0], a[0]*b[1], a[1]*b[0], a[1]*b[1])
    return min(products), max(products)


def div(a, b):
    assert b[0] > 0 or b[1] < 0
    return mul(a, (1/b[1], 1/b[0]))


def scale(a, s):
    return mul(a, pt(s))


def total(values):
    out = pt(0)
    for v in values:
        out = add(out, v)
    return out


def power(a, n):
    out = pt(1)
    for _ in range(n):
        out = mul(out, a)
    return out


def absmax(a):
    return max(abs(a[0]), abs(a[1]))


def absmin(a):
    return F(0) if a[0] <= 0 <= a[1] else min(abs(a[0]), abs(a[1]))


def coarse(a, digits):
    s = 10**digits
    lo = (a[0]*s).__floor__()
    hi = -(-a[1]*s).__floor__()
    out = F(lo, s), F(hi, s)
    check('outward rational rounding', out[0] <= a[0] <= a[1] <= out[1])
    return out


def derivative(a):
    return [scale(a[j], j) for j in range(1, len(a))]


def value(a, x):
    out = pt(0)
    for term in reversed(a):
        out = add(mul(out, x), term)
    return out


def serial(v):
    if isinstance(v, F):
        return str(v)
    if isinstance(v, (tuple, list)):
        return [serial(x) for x in v]
    if isinstance(v, dict):
        return {k: serial(x) for k, x in v.items()}
    return v


def match(name, actual, saved):
    check('exact reconstruction '+name, serial(actual) == saved)


def cmul(a, b):
    return sub(mul(a[0], b[0]), mul(a[1], b[1])), add(mul(a[0], b[1]), mul(a[1], b[0]))


def cpow(z, n):
    out = pt(1), pt(0)
    for _ in range(n):
        out = cmul(out, z)
    return out


def pellet(coeff, center, radius, k, saved, real=False):
    z = pt(center[0]), pt(center[1])
    tay, mod = [], []
    for j in range(6):
        terms = [cmul((scale(coeff[l], comb(l, j)), pt(0)), cpow(z, l-j)) for l in range(j, 6)]
        v = total(t[0] for t in terms), total(t[1] for t in terms)
        tay.append(v)
        mod.append((max(absmin(v[0]), absmin(v[1])), absmax(v[0])+absmax(v[1])))
    dominant = mod[k][0]*radius**k
    powers = [radius**j for j in range(6)]
    other = [mod[j][1]*powers[j] if j != k else F(0) for j in range(6)]
    upper = sum(other)
    record = {'taylor_coefficients': [v[0] for v in tay] if real else tay,
              'dominant_lower': dominant, 'other_upper_terms': other,
              'other_upper_sum': upper, 'margin' if real else 'strict_margin': dominant-upper}
    if not real:
        record['modulus_bounds'] = mod
    for name, v in record.items():
        match('Pellet '+str(center)+' '+name, v, saved[name])
    check('raw strict Pellet dominance '+str(center), dominant > upper > 0)
    check('Pellet metadata '+str(center), F(saved['radius']) == radius and saved['k'] == k and
          (F(saved['center']) == center[0] if real else list(map(F, saved['center'])) == list(center)))
    if not real:
        check('Pellet K=1', saved['K'] == 1)
        sc = saved['simple_comparison']
        lo, hi = F(sc['dominant_lower_at_least']), F(sc['other_upper_less_than'])
        check('coarse display bounds valid', dominant >= lo and upper < hi)
        check('coarse display decisiveness reported honestly', sc['strictly_decisive'] == (lo > hi))
    record.update(center=center, radius=radius, k=k, radius_powers=powers, ratio=dominant/upper)
    return record


def main():
    prefix = 'scripts/theta-gauss/'
    cert = load(prefix+'compensation-crossing-certificate-555.json')
    initial = load(prefix+'compensation-crossing-initial-555.json')
    proposal = load(prefix+'compensation-proposal-555.json')
    srcname = 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
    src = load(srcname)
    replay = load('scripts/actual-fredholm/audit-433/fixed-pair-certificate-431.json')
    modelname = 'scripts/central-jacobi/fixed-model-certificate-476.json'
    model = load(modelname)
    a433 = load('scripts/actual-fredholm/audit-433/audit-report.json')
    a478 = load('scripts/central-jacobi/audit-478/audit-report.json')
    a542 = load(prefix+'audit-certificate-542.json')
    r551 = load(prefix+'reference-roots-certificate-551.json')
    a553 = load(prefix+'reference-audit-certificate-553.json')
    maps = {'555': cert['input_hashes'], 'proposal': proposal['input_hashes'],
            'initial': initial['input_hashes'], '478': a478['original_hashes'],
            '542': a542['evidence']['input_hashes'], '551': r551['input_hashes'],
            '553': a553['evidence']['source_hashes']}
    for label, mapping in maps.items():
        for name, expected in mapping.items():
            check('digest '+label+' '+name, sha(name) == expected)
    evidence['complete_inherited_hash_maps'] = maps
    for name, expected in [
        (prefix+'compensation_crossing_555.py', cert['program_sha256']),
        (prefix+'audit_542.py', a542['program_sha256']),
        (prefix+'reference_roots_551.py', r551['program_sha256']),
        (prefix+'reference_audit_553.py', a553['program_sha256']),
        ('scripts/actual-fredholm/fixed_pair_431.py', a433['source_sha256']),
        ('scripts/actual-fredholm/check_saved_431.py', a433['checker_sha256'])]:
        check('implementation digest '+name, sha(name) == expected)
    check('fixed ancestor identity', sha(srcname) == model['source_sha256'] == a433['original_sha256'] ==
          '2c0aae858cc1e15b17e46dff0e1b81fa41582b4c84f5d74e3477fb72399335de')
    check('fixed actual-moment identity', sha(modelname) ==
          '2b429e4029fd7f50b30ea61b43d1be5aa22155b4c680c69440a716ff26643b2e')
    check('complete evaluator identity', src['evaluation'] == replay['evaluation'])
    for label, data in [('433', a433), ('478', a478), ('542', a542), ('551', r551), ('553', a553), ('555', cert)]:
        check('saved status consistency only '+label, data['status'] == 'PASS' and not data['failures'])
        if label != '433':
            check('saved checks consistency only '+label, all(x['passed'] for x in data['checks']))
    evidence['inherited_status_records_not_arithmetic_proof'] = {
        label: data['checks'] for label, data in [('433', a433), ('478', a478), ('542', a542), ('551', r551), ('553', a553)]}
    ev = src['evaluation']
    error = box(ev['uniform_G_error'])
    check('complex disk and error premise', F(ev['uniform_disk_radius']) == 1600 and 0 < error[0] <= error[1] < F('3.141e-48'))
    actual, gamma, additions = [], [], []
    for j in range(6):
        raw = box(ev['coefficients'][j])
        delta = error[1]/1600**j
        a = raw[0]-delta, raw[1]+delta
        g = scale(a, 8*4**j*factorial(j))
        actual.append(a)
        gamma.append(g)
        additions.append({'j': j, 'raw_coefficient': raw, 'Cauchy_addition': delta,
                          'actual_a': a, 'gamma_factor': 8*4**j*factorial(j), 'gamma': g})
        check('positive gamma '+str(j), g[0] > 0)
        if j < 5:
            oa, og = box(model['actual_a'][j]), box(model['gamma'][j])
            check('audited Decimal contains exact a/gamma '+str(j),
                  oa[0] <= a[0] <= a[1] <= oa[1] and og[0] <= g[0] <= g[1] <= og[1])
    fullnodes = [box(v) for v in a542['evidence']['independent_nodes']]
    fullweights = [box(v) for v in a542['evidence']['independent_weights']]
    match('prior full nodes', fullnodes, a553['evidence']['input_nodes_full'])
    match('prior full weights', fullweights, a553['evidence']['input_weights_full'])
    nodes = [coarse(v, 40) for v in fullnodes]
    weights = [coarse(v, 40) for v in fullweights]
    check('positive separated Gaussian nodes and weights', 0 < nodes[0][0] <= nodes[0][1] < nodes[1][0] and all(v[0] > 0 for v in weights))
    moments = [pt(1)]+[scale(div(gamma[j], gamma[0]), F(factorial(2*j), factorial(j))) for j in range(1, 6)]
    gaussian = [pt(1)]+[total(mul(weights[i], power(nodes[i], j)) for i in range(2)) for j in range(1, 6)]
    factors = [F((-1)**j*comb(5, j)*factorial(j), factorial(2*j)) for j in range(6)]
    check('factorial coefficient convention', factors == list(map(F, ['1', '-5/2', '5/6', '-1/12', '1/336', '-1/30240'])))
    p = [pt(1)]+[coarse(scale(div(gamma[j], gamma[0]), (-1)**j*comb(5, j)), 50) for j in range(1, 6)]
    q = [pt(1)]+[coarse(scale(gaussian[j], factors[j]), 50) for j in range(1, 6)]
    e = [pt(0)]*4+[coarse(sub(p[j], q[j]), 50) for j in (4, 5)]
    h, d5 = sub(moments[4], gaussian[4]), sub(moments[5], gaussian[5])
    b, transition = div(d5, h), div(scale(h, 90), d5)
    inputs = {'analytic_error': error, 'actual_a': actual, 'gamma': gamma,
              'nodes': nodes, 'weights': weights, 'raw_moments': moments,
              'gaussian_moments': gaussian, 'P_coefficients': p, 'Q_coefficients': q,
              'E_coefficients': e, 'h2': h, 'B2': b, 'X2': transition}
    for name, v in inputs.items():
        match(name, v, cert[name])
    check('both defect signs and coefficient signs', h[0] > 0 and d5[0] > 0 and e[4][0] > 0 and e[5][1] < 0)
    # Identity is L805 exactness + L807, not a comparison of these boxes.
    check('exact coefficient ratio is 90', factors[4]/(-factors[5]) == 90)
    evidence['inputs'] = inputs
    evidence['complete_Cauchy_additions'] = additions
    evidence['exactness_reason'] = 'L805 exact Gaussian identities S_j=t_j, j=0..3; L807 supplies both defects. Interval overlap is not used as equality.'
    family = lambda tau: [add(qj, mul(tau, ej)) for qj, ej in zip(q, e)]
    x, t, radius = F('43.721094942044'), F('.988536981668'), F('1e-7')
    check('proposal center only', F(proposal['proposal']['x0']) == x and F(proposal['proposal']['tau0']) == t and cert['proposal'] == proposal['proposal'])
    xb, tb = (x-radius, x+radius), (t-radius, t+radius)
    hc, hb = family(pt(t)), family(tb)
    res = [value(hc, pt(x)), value(derivative(hc), pt(x))]
    jac = lambda hs, xx: [[value(derivative(hs), xx), value(e, xx)],
                          [value(derivative(derivative(hs)), xx), value(derivative(e), xx)]]
    jc, jb = jac(hc, pt(x)), jac(hb, xb)
    mid = [[sum(v)/2 for v in row] for row in jc]
    det = mid[0][0]*mid[1][1]-mid[0][1]*mid[1][0]
    check('point determinant nonzero', det != 0)
    a = [[mid[1][1]/det, -mid[0][1]/det], [-mid[1][0]/det, mid[0][0]/det]]
    ad = a[0][0]*a[1][1]-a[0][1]*a[1][0]
    check('preconditioner inverse and invertible', ad != 0 and ad*det == 1 and all(
          sum(a[i][l]*mid[l][j] for l in range(2)) == int(i == j) for i in range(2) for j in range(2)))
    ar = [total(scale(res[j], a[i][j]) for j in range(2)) for i in range(2)]
    k = [[sub(pt(int(i == j)), total(scale(jb[l][j], a[i][l]) for l in range(2))) for j in range(2)] for i in range(2)]
    y, rows = [absmax(v) for v in ar], [sum(absmax(v) for v in row) for row in k]
    z = [radius*v for v in rows]
    margins = [radius-y[i]-z[i] for i in range(2)]
    etest, xx = value(e, xb), jb[1][0]
    ratio = div(xb, transition)
    event = dict(center=[x, t], radius=radius, x_box=xb, tau_box=tb, residual=res,
                 center_Jacobian=jc, whole_box_Jacobian=jb, point_Jacobian=mid,
                 point_determinant=det, preconditioner_determinant=ad, preconditioner=a,
                 I_minus_AJ=k, preconditioned_residual=ar, Y=y, row_norms=rows, Z=z,
                 self_map_margins=margins, partial_tau_H=etest, partial_x2_H=xx, x_over_X2=ratio)
    for name, v in event.items():
        match('event '+name, v, cert['event'][name])
    check('whole-box contraction', max(rows) < 1)
    check('whole-box self-map', min(margins) > 0)
    check('two nondegeneracies and interior', etest[0] > 0 and xx[1] < 0 and xb[0] > 0 and 0 < tb[0] < tb[1] < 1)
    check('reported contraction bounds', rows[0] < F('1e-5') and rows[1] < F('4e-8') and y[0]+z[0] < F('1.4e-12') and y[1]+z[1] < F('3e-13'))
    evidence['event'] = event
    slab, segment = (t-F('1e-6'), t+F('1e-6')), (x-F('.1'), x+F('.1'))
    hs = family(slab)
    orient = cert['local_orientation']
    match('parameter slab', slab, orient['parameter_slab'])
    match('real segment', segment, orient['real_segment'])
    check('event strictly contained, degree five uniformly', 0 < slab[0] < tb[0] < tb[1] < slab[1] < 1 and segment[0] < xb[0] < xb[1] < segment[1] and hs[5][1] < 0)
    centers = [(F('21.963634'), F(0)), (F('82.294347'), F('-3.823747')), (F('82.294347'), F('3.823747'))]
    match('other centers', centers, orient['other_centers'])
    tests = [pellet(hs, (x, F(0)), F('.1'), 2, orient['pair_pellet'], real=True)]
    tests += [pellet(hs, c, F('.1'), 1, saved) for c, saved in zip(centers, orient['other_pellet'])]
    check('four complete disk counts exhaust degree', len(orient['other_pellet']) == 3 and sum(v['k'] for v in tests) == len(hs)-1 == 5)
    distances = [(c[0]-x)**2+c[1]**2-F('.2')**2 for c in centers]
    distances += [(a[0]-b[0])**2+(a[1]-b[1])**2-F('.2')**2 for i, a in enumerate(centers) for b in centers[i+1:]]
    match('disk separation margins', distances, orient['squared_disjointness_margins'])
    check('all disjoint', min(distances) > 0)
    check('conjugation and positivity geometry', segment[0] > 0 and centers[0][0] > F('.1') and centers[0][1] == 0 and centers[1][0] == centers[2][0] and centers[1][1] == -centers[2][1] and abs(centers[1][1]) > F('.1'))
    curvature, es = value(derivative(derivative(hs)), segment), value(e, segment)
    vals = [value(hs, pt(v)) for v in segment]
    slopes = [value(derivative(hs), pt(v)) for v in segment]
    uniform = {'uniform_Hxx': curvature, 'uniform_E': es, 'uniform_endpoint_values': vals, 'uniform_endpoint_slopes': slopes}
    for name, v in uniform.items():
        match(name, v, orient[name])
    check('full rectangle strict curvature and correction', curvature[1] < 0 and es[0] > 0)
    check('full slab endpoint values and slopes', max(v[1] for v in vals) < 0 and slopes[0][0] > 0 and slopes[1][1] < 0)
    check('displayed full rectangle margins', curvature[0] > F('-.000304') and curvature[1] < F('-.000155') and es[0] > F('.409') and max(v[1] for v in vals) < F('-2e-7') and slopes[0][0] > F('2.28e-5') and slopes[1][1] < F('-2.28e-5'))
    sides = {}
    for label, tau in zip(['lower', 'upper'], slab):
        hside = family(pt(tau))
        cv, cs = value(hside, pt(x)), value(derivative(hside), pt(x))
        cc = value(derivative(derivative(hside)), segment)
        record = dict(tau=tau, center_value=cv, center_slope=cs, curvature=cc,
                      left_value=value(hside, pt(segment[0])), right_value=value(hside, pt(segment[1])))
        if label == 'lower':
            check('lower-side strong concavity', cc[1] < 0)
            record['global_segment_maximum_upper'] = cv[1]+absmax(cs)**2/(-2*cc[1])
            check('strict lower-side bound', record['global_segment_maximum_upper'] < F('-4e-7'))
        else:
            check('strict upper-side two brackets', cv[0] > F('4.1e-7') and record['left_value'][1] < 0 and record['right_value'][1] < 0)
        for name, v in record.items():
            match('side '+label+' '+name, v, orient['side_tests'][label][name])
        sides[label] = record
    check('reported pair dominance ratio', tests[0]['ratio'] > F('1.2128'))
    check('event before transition', ratio[0] > 0 and ratio[1] < 1)
    for name, v in {'tau': tb, 'x': xb, 'x_over_X2': ratio, 'X2': transition, 'E_at_event': etest, 'Hxx_at_event': xx}.items():
        match('reported outward bound '+name, coarse(v, 9), cert['simple_bounds'][name])
    check('exact event coordinate bounds in lemma', xb == (F('43.721094842044'), F('43.721095042044')) and tb == (F('.988536881668'), F('.988537081668')))
    evidence['uniform_orientation'] = dict(parameter_slab=slab, real_segment=segment, polynomial_coefficients=hs,
                                         tests=tests, squared_disjointness_margins=distances, **uniform, sides=sides)
    # Retain and independently diagnose the failed first neighborhood; no sweep.
    initialsegment = x-1, x+1
    initialcurv = value(derivative(derivative(hs)), initialsegment)
    match('initial failed curvature', initialcurv, initial['local_orientation']['uniform_Hxx'])
    check('initial curvature genuinely inconclusive', initialcurv[0] < 0 < initialcurv[1])
    check('initial incomplete disk proposal preserved', len(initial['local_orientation']['other_pellet']) == 1 and
          set(initial['failures']) == {'three remaining uniform simple-root disks', 'uniform strict concavity'})
    evidence['preserved_initial_failure'] = dict(curvature=initialcurv, failures=initial['failures'],
                                               proposed_other_centers=initial['local_orientation']['other_centers'])
    evidence['requirements'] = {'contraction_row_norms_less_than': '1', 'self_map_Y_plus_Z_less_than': str(radius),
                              'Pellet_dominance_ratios_greater_than': '1', 'curvature_upper_less_than': '0',
                              'correction_lower_greater_than': '0', 'endpoint_upper_less_than': '0'}
    evidence['summary_displays_not_proof'] = {'row_norms': [float(v) for v in rows],
                                           'Y_plus_Z': [float(y[i]+z[i]) for i in range(2)],
                                           'Pellet_ratios': [float(v['ratio']) for v in tests],
                                           'Hxx': [float(v) for v in curvature], 'E_lower': float(es[0]),
                                           'endpoint_uppers': [float(v[1]) for v in vals]}
    check('all inputs unchanged', all(hashlib.sha256((ROOT/n).read_bytes()).hexdigest() == h for n, h in hashes.items()))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        failures.append(type(exc).__name__+': '+str(exc))
    report = {'scope': 'L809 independent exact reconstruction and full-slab audit; inherited analytic/backend contracts retained',
              'status': 'PASS' if not failures else 'FAIL', 'checks': checks, 'failures': failures,
              'evidence': serial(evidence), 'input_hashes': hashes,
              'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    OUT.write_text(json.dumps(report, indent=2)+'\n')
    print(report['status'], 'checks', len(checks), 'failures', failures)
    print('Actual:', evidence.get('summary_displays_not_proof', {}))
    print('Required:', evidence.get('requirements', {}))
    print('Complete evidence:', OUT.relative_to(ROOT))
    raise SystemExit(bool(failures))
