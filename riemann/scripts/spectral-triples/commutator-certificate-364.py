"""Directed interval certificate for one Fourier row and one commutator ansatz.

Uses the audited L759 entry enclosures. Point candidates from the diagnostic
are exact decimal rationals here; no conclusion trusts its eigensolver/solves.
"""
import ast
from decimal import Decimal as D
import hashlib
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
GENERATOR = HERE / 'finite-parity-359.py'
INPUT = HERE / 'finite-parity-359.json'
SCREEN = HERE / 'commutator-screen-364.json'
OUTPUT = Path(__file__).with_suffix('.json')
started = time.monotonic()
namespace = {}
tree = ast.parse(GENERATOR.read_text())
selected = []
for node in tree.body:
    if isinstance(node, (ast.Import, ast.ImportFrom)):
        selected.append(node)
    elif isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and
            t.id in {'PREC', 'LO', 'HI'} for t in node.targets):
        selected.append(node)
    elif isinstance(node, ast.ClassDef) and node.name == 'I':
        selected.append(node)
exec(compile(ast.Module(body=selected, type_ignores=[]), str(GENERATOR), 'exec'), namespace)
I, LO, HI = [namespace[name] for name in ['I', 'LO', 'HI']]

data, screen = json.loads(INPUT.read_text()), json.loads(SCREEN.read_text())
report = dict(kind='directed interval full-parity row-norm and ansatz certificate',
              cell=dict(lambda_squared=13, N=120, z='i/4'),
              script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              entry_certificate_sha256=hashlib.sha256(INPUT.read_bytes()).hexdigest(),
              generator_sha256=hashlib.sha256(GENERATOR.read_bytes()).hexdigest(),
              screen_sha256=hashlib.sha256(SCREEN.read_bytes()).hexdigest(),
              precision=170, checks={}, failures=[], outcome='IN_PROGRESS')

def save():
    report['elapsed_seconds'] = time.monotonic()-started
    OUTPUT.write_text(json.dumps(report, indent=2) + '\n')

def require(ok, name):
    report['checks'][name] = bool(ok)
    if not ok:
        report['failures'].append(name)
        save()
        raise ArithmeticError(name)

def pair(p):
    require(D(p[0]) <= D(p[1]), 'ordered_input_intervals')
    return I(*p)

def sq(v):
    if v.lo <= 0 <= v.hi:
        return I(0, HI.multiply(v.absupper(), v.absupper()))
    return I(min(LO.multiply(v.lo, v.lo), LO.multiply(v.hi, v.hi)),
             max(HI.multiply(v.lo, v.lo), HI.multiply(v.hi, v.hi)))

def dot(a, b):
    return sum((x*y for x, y in zip(a, b)), I(0))

def norm(v):
    return sum((sq(x) for x in v), I(0)).sqrt()

def inflate(v, radius):
    r = I(radius).absupper()
    return I(LO.subtract(v.lo, r), HI.add(v.hi, r))

def mv(A, v):
    return [dot(row, v) for row in A]

def sv(v):
    return [x.save() for x in v]

def normalize(raw):
    v = [I(x) for x in raw]
    n = norm(v)
    require(n.lo > 0, 'candidate_norm_positive')
    return [x/n for x in v], n

def inertia(A, shift, label):
    M = [[I(v) for v in row] for row in A]
    for j in range(len(M)):
        M[j][j] -= shift
    pivots, negative = [], 0
    for k in range(len(M)):
        p = M[k][k]
        require(not p.lo <= 0 <= p.hi, label+'_all_pivots_nonzero')
        pivots.append(p.save())
        negative += int(p.hi < 0)
        for j in range(k+1, len(M)):
            mult = M[j][k]/p
            for i in range(j, len(M)):
                M[i][j] = M[j][i] = M[i][j]-mult*M[i][k]
    report[label] = dict(shift=shift.save(), pivots=pivots, negative=negative)
    save()
    return negative

try:
    require(data['script_sha256'] == report['generator_sha256'], 'generator_hash')
    require(screen['input_sha256'] == report['entry_certificate_sha256'], 'screen_input_hash')
    require(data['outcome'] == 'CERTIFIED_SIMPLE_EVEN', 'audited_L759_input')
    require(screen['outcome'] == 'DIAGNOSTIC_ONLY', 'screen_has_all_candidates')
    require(data['parameters'] == dict(N=120, K=512, R=160, EM=80, precision=170), 'cell')
    even = [[pair(v) for v in row] for row in data['even_matrix']]
    odd = [[pair(v) for v in row] for row in data['odd_matrix']]
    require(len(even) == 121 and all(len(r) == 121 for r in even)
            and len(odd) == 120 and all(len(r) == 120 for r in odd), 'all_241_directions')
    L, pi = pair(data['constants']['L']), pair(data['constants']['pi'])
    root2, rootL = I(2).sqrt(), L.sqrt()
    t = I(1)/4

    ground = screen['eigenpairs']['ground']
    w, wn = normalize(ground['vector'])
    center = I(ground['value'])  # fixed exact decimal, not an assumed eigenvalue
    residual = [a-center*b for a, b in zip(mv(even, w), w)]
    r = norm(residual)
    require((center+r).hi < D('5e-56'), 'residual_selects_ground_eigenvalue')
    eps = inflate(center, r.hi)
    sep = I('1e-55')-center
    err_u = I(2)*I(r.hi)/sep
    require(err_u.hi < 1, 'unit_ground_vector_error_small')
    report['ground'] = dict(raw_vector=ground['vector'], raw_norm=wn.save(),
                            unit_candidate=sv(w), center=center.save(),
                            residual=sv(residual), residual_norm=r.save(),
                            epsilon=eps.save(), unit_vector_error_upper=str(err_u.hi))
    save()
    print('ground enclosure and vector error certified', flush=True)

    tau = I('3.0559e-55')
    require(inertia(even, tau, 'even_inertia') == 1, 'one_even_below_tau')
    require(inertia(odd, tau, 'odd_inertia') == 0, 'no_odd_below_tau')
    oy, oyn = normalize(screen['eigenpairs']['first_odd']['vector'])
    odd_rayleigh = dot(oy, mv(odd, oy))
    gap = I((tau-eps).lo, (odd_rayleigh-eps).hi)
    require(gap.lo > D('3.0555e-55') and gap.hi < D('3.0556e-55'), 'two_sided_actual_gap')
    report['gap'] = dict(actual_gap=gap.save(), required_bracket=['3.0555e-55','3.0556e-55'],
                         odd_raw_vector=screen['eigenpairs']['first_odd']['vector'],
                         odd_raw_norm=oyn.save(), odd_unit_vector=sv(oy),
                         odd_rayleigh=odd_rayleigh.save())
    save()
    print('both actual-gap endpoints certified', flush=True)

    sinh = ((L*t/2).exp()-(-L*t/2).exp())/2
    pref = 2*sinh/rootL
    erow, orow = [pref/t], []
    for j in range(1, 121):
        freq = 2*pi*j/L
        erow.append(root2*pref*t/(sq(freq)+sq(t)))
        orow.append(-root2*pref*freq/(sq(freq)+sq(t)))
    boundary = [I(1)/rootL]+[root2/rootL]*120
    overlap = inflate(dot(boundary, w), norm(boundary)*err_u)
    require(overlap.lo > 0, 'boundary_overlap_nonzero')
    transform_u = inflate(dot(erow, w), norm(erow)*err_u)
    fvalue = transform_u/overlap
    qe = [a-fvalue*b for a, b in zip(erow, boundary)]
    qo = orow
    nq = norm(qe+qo)
    require(nq.lo > 0, 'full_dual_row_nonzero')
    report['row'] = dict(fourier_even=sv(erow), fourier_odd_imag=sv(orow),
                         boundary_even=sv(boundary), overlap=overlap.save(),
                         fourier_at_unit_ground=transform_u.save(),
                         fourier_at_boundary_normalized_ground=fvalue.save(),
                         q_even=sv(qe), q_odd_imag=sv(qo), norm=nq.save())

    ke, ko = [I(x) for x in screen['h_even']], [I(x) for x in screen['h_odd_imag']]
    re = [a-eps*b-c for a, b, c in zip(mv(even, ke), ke, qe)]
    ro = [a-eps*b-c for a, b, c in zip(mv(odd, ko), ko, qo)]
    nr = norm(re+ro)
    kernel_component = I(dot(w, ke).absupper())+err_u*norm(ke)
    err_h = I(nr.hi)/I(gap.lo)+I(kernel_component.hi)
    nk = norm(ke+ko)
    nh = inflate(nk, err_h.hi)
    require(nh.lo > 0, 'preimage_norm_positive')
    rho = gap*nh/nq
    require(rho.lo > D('5.25e-30') and rho.hi < D('5.26e-30'), 'rigorous_ratio_enclosure')
    require(rho.hi < D('0.1'), 'ratio_below_continuation_threshold')
    report['preimage'] = dict(candidate_even=screen['h_even'], candidate_odd_imag=screen['h_odd_imag'],
                             residual_even=sv(re), residual_odd_imag=sv(ro), residual_norm=nr.save(),
                             kernel_component_upper=str(kernel_component.hi),
                             norm_candidate=nk.save(), error_upper=str(err_h.hi), norm=nh.save())
    report['ratio'] = dict(enclosure=rho.save(), required_upper='0.1')
    save()
    print('rho enclosed in (5.25e-30, 5.26e-30); required <=0.1', flush=True)

    # Test the direct rank-two frequency-resolvent ansatz, with exact
    # beta_j=j*A[j,0] from the source commutator (beta_0=0 by parity).
    # x=u/(sqrt(L)*b(u)), eta^T x=1. At wfreq=i*y, f=-i*S,
    # a=x^T F beta is real, k=i*k0 and q=k(eta^T F-f eta^T).
    # The candidate h0=(k/a)x^T F leaves r0=(k*f/a)(beta^T F-a eta^T).
    u = [inflate(v, err_u.hi) for v in w]
    x = [v/(rootL*overlap) for v in u]
    y = t*L/(2*pi)
    k0 = rootL*sinh/pi
    S = fvalue/(k0*rootL)
    beta = [I(0)] + [I(j)*pair(data['full_matrix'][120+j][120]) for j in range(1,121)]
    avec = [-beta[j]*j/(I(j*j)+sq(y)) for j in range(1,121)]
    a = dot(x[1:], [root2*v for v in avec])
    require(not a.lo <= 0 <= a.hi, 'ansatz_scalar_nonzero')
    scale = k0*S/a
    ansatz_res_even = [-scale*a] + [root2*scale*(v-a) for v in avec]
    ansatz_res_odd = [root2*scale*(-beta[j]*y/(I(j*j)+sq(y))) for j in range(1,121)]
    n_ansatz = norm(ansatz_res_even+ansatz_res_odd)
    residual_ratio = n_ansatz/nq
    report['commutator_ansatz'] = dict(eta_normalized_x_even=sv(x),
                                      beta_positive=sv(beta), frequency_imag=y.save(),
                                      prefactor_imag=k0.save(), f_negative_imag=S.save(),
                                      a=a.save(), residual_even=sv(ansatz_res_even),
                                      residual_odd_imag=sv(ansatz_res_odd),
                                      residual_norm=n_ansatz.save(), residual_to_q_norm=residual_ratio.save())
    # Classification is an observed bound, not an assertion selected before
    # evaluating the full residual. Both endpoints are retained in the file.
    if residual_ratio.lo > 1:
        report['ansatz_decision'] = 'DIRECT_ANSATZ_INCREASES_RESIDUAL_NORM'
    elif residual_ratio.hi < D('0.1'):
        report['ansatz_decision'] = 'RESIDUAL_REDUCTION_ONLY_NO_COMPLETE_PREIMAGE'
    else:
        report['ansatz_decision'] = 'NO_DECISIVE_TENTH_THRESHOLD_REDUCTION'

    # Second commutator: T D^2 x = c eta-D beta, c=beta^T D x.
    # Pay the boundary part explicitly. The remainder is retained openly;
    # its inverse-gap estimate is a partial bound, not an inverse-free
    # exact preimage. No uncomputed ground overlap is hidden in c.
    c = dot(x[1:], [root2*beta[j]*j for j in range(1,121)])
    require(c.hi < 0, 'second_commutator_c_negative')
    eta_row_scale = k0*S
    h_boundary = [I(0)]+[-eta_row_scale/c*x[j]*j*j for j in range(1,121)]
    remainder_even = [erow[0]] + [erow[j]-eta_row_scale/c*root2*beta[j]*j
                                for j in range(1,121)]
    remainder_odd = orow
    remainder_norm = norm(remainder_even+remainder_odd)
    h_boundary_norm = norm(h_boundary)
    relative_remainder = remainder_norm/nq
    relative_explicit_cost = gap*h_boundary_norm/nq
    # P is a contraction. The residual annihilates the ground line
    # algebraically because q does and h_boundary*T does.
    commutator_rho_upper = relative_explicit_cost+relative_remainder
    require(c.lo > D('-1447') and c.hi < D('-1446'), 'second_commutator_c_enclosure')
    require(relative_remainder.lo > D('0.02196') and relative_remainder.hi < D('0.02197'),
            'second_commutator_residual_enclosure')
    require(relative_explicit_cost.hi < D('7e-31'), 'second_commutator_explicit_cost')
    require(commutator_rho_upper.hi < D('0.022'), 'second_commutator_gain_below_tenth')
    excess = residual_ratio-I(1)
    require(excess.lo > D('2.2592e-29') and excess.hi < D('2.2593e-29'),
            'direct_ansatz_strict_residual_increase')
    report['commutator_ansatz']['residual_ratio_excess_above_one'] = excess.save()
    report['second_commutator'] = dict(c=c.save(), boundary_row_scale=eta_row_scale.save(),
                                      partial_preimage_even=sv(h_boundary),
                                      partial_preimage_norm=h_boundary_norm.save(),
                                      residual_even=sv(remainder_even), residual_odd_imag=sv(remainder_odd),
                                      residual_norm=remainder_norm.save(),
                                      residual_to_q_norm=relative_remainder.save(),
                                      relative_explicit_cost=relative_explicit_cost.save(),
                                      resulting_rho_upper=str(commutator_rho_upper.hi),
                                      qualification='R remains on the explicitly bounded residual; not an inverse-free exact preimage')
    print('second commutator residual/q <=', format(relative_remainder.hi, '.8E'),
          'explicit cost <=', format(relative_explicit_cost.hi, '.8E'),
          'rho bound <=', format(commutator_rho_upper.hi, '.8E'), 'required <=0.1', flush=True)
    report['arithmetic_flags'] = {name: [signal.__name__ for signal, val in ctx.flags.items() if val]
                                  for name, ctx in [('floor', LO), ('ceiling', HI)]}
    forbidden = {'InvalidOperation', 'DivisionByZero', 'Overflow', 'Underflow', 'Subnormal', 'Clamped'}
    require(not any(forbidden.intersection(flags) for flags in report['arithmetic_flags'].values()),
            'no_invalid_or_exponent_range_flags')
    report['outcome'] = 'CERTIFIED_FINITE_RATIO_AND_ANSATZ_TEST'
    print('ansatz residual/q in', format(residual_ratio.lo, '.8E'), format(residual_ratio.hi, '.8E'),
          'required <=0.1 for a material residual reduction;', report['ansatz_decision'], flush=True)
except Exception as exc:
    report['outcome'] = 'FAILED'
    if repr(exc) not in report['failures']:
        report['failures'].append(repr(exc))
    raise
finally:
    save()
    print('RESULT', report['outcome'], 'failures', report['failures'], 'certificate', OUTPUT, flush=True)
