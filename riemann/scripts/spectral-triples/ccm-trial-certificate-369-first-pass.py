"""Fixed CCM trial certificate; stdlib Decimal directed intervals.

Full analytic justification: L761. Point inverse iterations merely supply
exact rational candidates. Certification includes the infinite Schur tail,
residuals, normalization and all 241 coefficients, with no inversion parity.
"""
import ast
from decimal import Decimal as D, getcontext
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
BASE = HERE / 'finite-parity-359.py'
OUTPUT = Path(__file__).with_suffix('.json')
started = time.monotonic()
namespace = {}
selected = []
for node in ast.parse(BASE.read_text()).body:
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        selected.append(node)
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and
            t.id in {'PREC', 'LO', 'HI'} for t in node.targets):
        selected.append(node)
    elif isinstance(node, ast.ClassDef) and node.name == 'I':
        selected.append(node)
    elif isinstance(node, ast.FunctionDef) and node.name in {
            'pm', 'atan_recip', 'sincos_reduced'}:
        selected.append(node)
exec(compile(ast.Module(body=selected, type_ignores=[]), str(BASE), 'exec'), namespace)
I, LO, HI = [namespace[k] for k in ['I', 'LO', 'HI']]
LO.prec = HI.prec = 260
getcontext().prec = 240
pm = namespace['pm']
M = 96
report = dict(kind='infinite prolate residual/tail and full CCM projection certificate',
              parameters=dict(lambda_squared=13, N=120, even_dimension=M,
                              max_degree=2*M-2, interval_precision=260,
                              candidate_precision=240),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              interval_source_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest(),
              checks={}, failures=[], outcome='IN_PROGRESS')


def save():
    report['elapsed_seconds'] = time.monotonic()-started
    OUTPUT.write_text(json.dumps(report, indent=2) + '\n')


def require(ok, name):
    report['checks'][name] = bool(ok)
    if not ok:
        report['failures'].append(name)
        save()
        raise ArithmeticError(name)


def square(v):
    if v.lo <= 0 <= v.hi:
        return I(0, HI.multiply(v.absupper(), v.absupper()))
    return I(min(LO.multiply(v.lo, v.lo), LO.multiply(v.hi, v.hi)),
             max(HI.multiply(v.lo, v.lo), HI.multiply(v.hi, v.hi)))


def norm(v):
    return sum((square(x) for x in v), I(0)).sqrt()


def mid(v):
    return (v.lo+v.hi)/2  # candidate selection only


def pair_list(v):
    return [x.save() for x in v]


def tridiag_mv(a, b, v):
    out = [a[k]*v[k] for k in range(len(v))]
    for k in range(len(v)-1):
        out[k] += b[k]*v[k+1]
        out[k+1] += b[k]*v[k]
    return out


def point_candidate(a, b, shift):
    aa, bb = list(map(mid, a)), list(map(mid, b[:-1]))
    pivots = [aa[0]-shift]
    for k in range(1, len(a)):
        pivots.append(aa[k]-shift-bb[k-1]*bb[k-1]/pivots[-1])
    v = [D(int(k == 0)) for k in range(len(a))]
    for iteration in range(24):
        y = [v[0]]
        for k in range(1, len(a)):
            y.append(v[k]-bb[k-1]*y[-1]/pivots[k-1])
        v = [y[k]/pivots[k] for k in range(len(a))]
        for k in reversed(range(len(a)-1)):
            v[k] -= bb[k]*v[k+1]/pivots[k]
        nv = sum((x*x for x in v), D(0)).sqrt()
        v = [x/nv for x in v]
        if v[0] < 0:
            v = [-x for x in v]
    Av = tridiag_mv(aa, bb, v)
    center = sum((x*y for x, y in zip(v, Av)), D(0))
    return v, center


def inertia(a, b, threshold, correction, name):
    diagonal = [v-threshold for v in a]
    diagonal[-1] -= correction
    pivots = []
    for k in range(len(a)):
        p = diagonal[k] if k == 0 else diagonal[k]-square(b[k-1])/pivots[-1]
        require(not p.lo <= 0 <= p.hi, name+'_pivot_'+str(k)+'_nonzero')
        pivots.append(p)
    count = sum(int(p.hi < 0) for p in pivots)
    return dict(pivots=pair_list(pivots), negative=count,
                last_diagonal_correction=correction.save())


try:
    pi = 16*namespace['atan_recip'](5)-4*namespace['atan_recip'](239)
    namespace['PI'] = pi
    L, lam = I(13).ln(), I(13).sqrt()
    c2 = square(26*pi)
    aa, bb = [], []
    for k in range(M):
        j = 2*k
        aa.append(I(j*(j+1))+c2*(2*j*(j+1)-1)/((2*j+3)*(2*j-1)))
        bb.append(c2*(j+1)*(j+2)/((2*j+3)*I((2*j+1)*(2*j+5)).sqrt()))
    tail_floor = (2*M)*(2*M+1)
    report['constants'] = dict(pi=pi.save(), L=L.save(), lam=lam.save(), c2=c2.save())
    report['operator'] = dict(diagonal=pair_list(aa),
                              off_diagonal_including_omitted_coupling=pair_list(bb),
                              tail_floor=tail_floor)
    report['infinite_counts'] = {}
    for threshold, expected in [(80, 0), (82, 1), (723, 2), (726, 3)]:
        t = I(threshold)
        require(tail_floor > threshold, 'tail_positive_at_'+str(threshold))
        correction = square(bb[-1])/(tail_floor-t)
        upper = inertia(aa, bb, t, I(0), 'upper_'+str(threshold))
        lower = inertia(aa, bb, t, correction, 'lower_'+str(threshold))
        require(upper['negative'] == lower['negative'] == expected,
                'infinite_count_'+str(threshold))
        report['infinite_counts'][str(threshold)] = dict(
            upper=upper, lower=lower, infinite_negative=expected)
    save()
    print('Infinite even-spectrum counts certified: 80:0, 82:1, 723:2, 726:3.', flush=True)

    modes = {}
    report['modes'] = {}
    for label, shift, low, high in [(0, '80.92907752', 80, 82),
                                    (4, '724.21755299', 723, 726)]:
        raw, center = point_candidate(aa, bb, D(shift))
        raw_i = [I(x) for x in raw]
        raw_norm = norm(raw_i)
        require(raw_norm.lo > 0, 'mode_'+str(label)+'_normalizable')
        q = [x/raw_norm for x in raw_i]
        residual = [x-I(center)*y for x, y in zip(tridiag_mv(aa, bb, q), q)]
        residual.append(bb[-1]*q[-1])
        r = norm(residual)
        separation = min((I(center)-low).lo, (high-I(center)).lo)
        require(separation > r.hi, 'mode_'+str(label)+'_identified')
        error = 2*I(r.hi)/I(separation)
        require(error.hi < D('1e-70'), 'mode_'+str(label)+'_error_below_1e-70')
        modes[label] = dict(q=q, error=error)
        report['modes'][str(label)] = dict(
            raw_exact_decimal_vector=list(map(str, raw)), raw_norm=raw_norm.save(),
            normalized_candidate=pair_list(q), center=str(center),
            residual_including_tail=pair_list(residual), residual_norm=r.save(),
            eigenvalue_enclosure=pm(I(center), r.hi).save(),
            separation_lower=str(separation), unit_L2_error_upper=str(error.hi),
            omitted_coordinate_residual=residual[-1].save())
        save()
        print('Mode', label, 'residual <=', format(r.hi, '.5E'),
              'L2 error <=', format(error.hi, '.5E'), '(required < 1e-70).', flush=True)

    q0, q4 = modes[0]['q'], modes[4]['q']
    e0, e4 = modes[0]['error'], modes[4]['error']
    require((q0[0]-e0).lo > 0, 'true_mode0_additive_integral_nonzero')
    root2lam = (2*lam).sqrt()
    j0, j4 = root2lam*q0[0], root2lam*q4[0]
    trial_error = 2*root2lam*(e0+e4)
    transport = sum((1/I(r).sqrt() for r in range(1, 14)), I(0))
    vector_error = transport*trial_error
    require(vector_error.hi < D('1e-65'), 'transport_error_below_1e-65')
    report['trial'] = dict(
        approximate_additive_integrals={'0': j0.save(), '4': j4.save()},
        exact_integral_errors={'0': (root2lam*e0).save(), '4': (root2lam*e4).save()},
        additive_L2_error_upper=str(trial_error.hi),
        transport_norm_upper=str(transport.hi),
        full_projected_vector_L2_error_upper=str(vector_error.hi),
        normalization='h = integral(phi4)*phi0 - integral(phi0)*phi4; phi_n L2(-lambda,lambda) unit')

    # Exact rational Legendre monomials, P_0 through P_190.
    polys = [[F(1)], [F(0), F(1)]]
    for n in range(1, 2*M-2):
        following = [F(0)]*(n+2)
        for k, x in enumerate(polys[-1]):
            following[k+1] += F(2*n+1, n+1)*x
        for k, x in enumerate(polys[-2]):
            following[k] -= F(n, n+1)*x
        polys.append(following)
    # H(lambda*x) = sqrt(2)*(q4[0]*q0(x)-q0[0]*q4(x)).
    coeff = [I(0)]*(2*M-1)
    for k in range(M):
        if k == 0:  # exact determinant cancellation, no assumed parity
            amplitude = I(0)
        else:
            amplitude = I(2).sqrt()*(q4[0]*q0[k]-q0[0]*q4[k])*I(D(2*k)+D('0.5')).sqrt()
        for m, value in enumerate(polys[2*k]):
            if value:
                coeff[m] += amplitude*(I(value.numerator)/value.denominator)
    report['trial']['monomial_coefficients_H_lambda_x'] = pair_list(coeff)
    save()

    # Each support interval is integrated exactly in powers; endpoint phases
    # are enclosed by Taylor intervals. r=13 has zero interval length.
    maxdegree = 2*M-2
    lower_terms = [I(0)]*(maxdegree+1)
    rootlam = lam.sqrt()
    for r in range(1, 13):
        power = I(1)
        for m in range(maxdegree+1):
            lower_terms[m] += power/rootlam
            power *= I(r)/13
    logs = {r: I(r).ln()/L for r in range(2, 13)}
    weights = {r: (lam/r).sqrt() for r in range(1, 13)}
    report['integration'] = dict(
        method='exact polynomial power antiderivatives on each r support interval',
        nonzero_support_indices=list(range(1, 13)),
        index_13_zero_length=True, lower_endpoint_sums=pair_list(lower_terms),
        max_j=120, conjugation='exp(-2*pi*i*j*log(lambda*u)/L)',
        quadrature_error='0 (closed antiderivatives; transcendental rounding separately enclosed)')
    exact_coefficient_intervals = {}
    polynomial_coefficient_intervals = {}
    maxradius = D(0)
    for j in range(121):
        omega = 2*pi*j/L
        upper_re, upper_im = weights[1], I(0)
        for r in range(2, 13):
            if j == 0:
                sine, cosine = I(0), I(1)
            else:
                sine, cosine = namespace['sincos_reduced'](j*logs[r])
            upper_re += weights[r]*cosine
            upper_im += weights[r]*sine
        re, im = I(0), I(0)
        for m in range(0, maxdegree+1, 2):
            a = I(D(m)+D('0.5'))
            denom = square(a)+square(omega)
            dr = upper_re-lower_terms[m]
            re += coeff[m]*(a*dr-omega*upper_im)/denom
            im += coeff[m]*(omega*dr+a*upper_im)/denom
        re, im = re/L.sqrt(), im/L.sqrt()
        # Reality implies conjugate coefficients, not equality (inversion parity).
        if j == 0:
            require(im.lo <= 0 <= im.hi, 'zeroth_coefficient_imaginary_zero')
            im = I(0)
        for index, imag in ([(0, im)] if j == 0 else [(j, im), (-j, -im)]):
            polynomial_coefficient_intervals[str(index)] = dict(real=re.save(), imag=imag.save())
            exact_re, exact_im = pm(re, vector_error.hi), pm(imag, vector_error.hi)
            if index == 0:
                exact_im = I(0)
            exact_coefficient_intervals[str(index)] = dict(real=exact_re.save(), imag=exact_im.save())
            maxradius = max(maxradius, HI.divide(HI.subtract(exact_re.hi, exact_re.lo), D(2)),
                            HI.divide(HI.subtract(exact_im.hi, exact_im.lo), D(2)))
    require(len(exact_coefficient_intervals) == 241, 'all_241_complex_coefficients')
    require(maxradius < D('1e-65'), 'every_component_radius_below_1e-65')
    report['projection'] = dict(
        polynomial_coefficients=polynomial_coefficient_intervals,
        exact_trial_coefficients=exact_coefficient_intervals,
        every_real_imag_component_radius_upper=str(maxradius),
        required_radius='1e-65',
        direction_loss='none; only conjugation from reality used',
        interpretation='rectangle enclosures; common L2 approximation error recorded separately')
    report['outcome'] = 'CERTIFIED_TRIAL_PROJECTION'
    save()
    print('All 241 coefficients enclosed; maximum component radius <=',
          format(maxradius, '.5E'), '(required < 1e-65).')
    print('Failures:', report['failures'])
    print('Full certificate:', OUTPUT.relative_to(HERE.parent.parent))
except Exception as exc:
    report['outcome'] = 'FAILED'
    report['exception'] = repr(exc)
    save()
    print('FAILED:', repr(exc), 'certificate:', OUTPUT)
    raise
