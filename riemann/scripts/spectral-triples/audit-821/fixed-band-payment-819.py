"""Single approved s1 fixed-band residual, with complete analytic errors.

Only arithmetic definitions are loaded from the audited 814 source; its
matrix calculation is NOT run. See C759g for all analytic bounds.
"""
import ast
import hashlib
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ARITH = BASE / 'two-sine-primitive-814.py'
tree = ast.parse(ARITH.read_text())
prefix = []
for node in tree.body:
    if isinstance(node, ast.ClassDef) and node.name == 'Z':
        break
    prefix.append(node)
namespace = {}
exec(compile(ast.Module(body=prefix, type_ignores=[]), str(ARITH), 'exec'), namespace)
I, D, PI, pm, trig = (namespace[k] for k in ('I', 'D', 'PI', 'pm', 'sincos_turns'))

K_GAMMA, K_PSI, N_MID = 4096, 8192, 512
sh = ((I(1)/2).exp()-(-I(1)/2).exp())/2
alpha = 2*PI*sh/(PI*PI+I('0.25'))
# F_s(+i/2)=alpha, F_s(-i/2)=-alpha;
# F_g(+/-i/2)=-2*pi*alpha, with g=-1-cos(pi*x).
pole_s = -2*alpha*alpha
pole_g = 8*PI*PI*alpha*alpha
relative_pole = pole_g/3-pole_s
prime_rows, prime_s, prime_g = [], I(0), I(0)
for n, p in ((2, 2), (3, 3), (4, 2), (5, 5), (7, 7)):
    y = I(n).ln()
    weight = I(p).ln()/I(n).sqrt()
    sn, cs, arg, shift = trig(y/2)
    c_s = (1-y/2)*cs+sn/(2*PI)
    c_g = (2-y)*(1+cs/2)+3*sn/(2*PI)
    e_s, e_g = -2*weight*c_s, -2*weight*c_g
    relative = e_g/3-e_s
    simplified = -2*weight*(2-y)*(1-cs)/3
    # Both formulas are independently enclosing the same exact expression.
    overlap = max(relative.lo, simplified.lo) <= min(relative.hi, simplified.hi)
    prime_s += e_s
    prime_g += e_g
    prime_rows.append({'n': n, 'prime_base': p, 'delay': y.save(),
                       'weight': weight.save(), 'sin': sn.save(), 'cos': cs.save(),
                       'reduced_argument': arg.save(), 'shift': shift,
                       'C_s': c_s.save(), 'C_g': c_g.save(),
                       'E_s_term': e_s.save(), 'E_g_term': e_g.save(),
                       'relative_term': relative.save(),
                       'simplified_relative_term': simplified.save(),
                       'formulas_overlap': overlap})
e_s, e_g = pole_s+prime_s, pole_g+prime_g
residual_R = e_g/3-e_s

# gamma = lim(H_N-log N); 0 <= H_N-log N-gamma <= 1/N.
harmonic_rows, harmonic = [], I(0)
for k in range(1, K_GAMMA+1):
    term = I(1)/k
    harmonic += term
    harmonic_rows.append(term.save())
gamma_center = harmonic-I(K_GAMMA).ln()
gamma = gamma_center+I((I(1)/K_GAMMA).hi.copy_negate(), 0)

psi_rows, symbols = {}, {}
for t in (1, 2):
    a, b = I(1)/4, I(t)/2
    zeroth = -gamma-a/(a*a+b*b)
    partial, rows = I(0), []
    for k in range(1, K_PSI+1):
        z = I(k)+a
        term = I(1)/k-z/(z*z+b*b)
        partial += term
        rows.append(term.save())
    # All omitted terms positive and <= a/k^2+b^2/k^3.
    tail_upper = a/K_PSI+b*b/(2*K_PSI*K_PSI)
    psi = zeroth+partial+I(0, tail_upper.hi)
    symbol = psi-PI.ln()
    symbols[t] = symbol
    psi_rows[str(t)] = {'a': a.save(), 'b': b.save(), 'zeroth': zeroth.save(),
                        'terms': rows, 'partial_sum': partial.save(),
                        'tail': I(0, tail_upper.hi).save(),
                        'psi': psi.save(), 'm': symbol.save()}

mass_rows, masses = {}, {}
for length in (1, 2):
    step = I(length)/N_MID
    total, rows = I(0), []
    for j in range(N_MID):
        t = I(length)*(2*j+1)/(2*N_MID)
        sn, cs, arg, shift = trig(t/(2*PI))
        q = 4*PI*PI*sn*sn/(PI*PI-t*t)**2
        total += q
        rows.append({'j': j, 't': t.save(), 'sin_t': sn.save(),
                     'reduced_argument': arg.save(), 'shift': shift,
                     'abs_F_squared': q.save()})
    middle = step*total
    # |(|F|^2)''| <= 4/3+4/sqrt(5) < 4, everywhere.
    error = I(4)*length**3/(24*N_MID*N_MID)
    integral = pm(middle, error)
    mass = integral/PI
    masses[length] = mass
    mass_rows[str(length)] = {'terms': rows, 'midpoint_sum': middle.save(),
                             'second_derivative_bound': 4,
                             'full_quadrature_error': error.save(),
                             'integral_0_L': integral.save(),
                             'mass_abs_t_le_L': mass.save()}
p1, p2 = masses[1], 1-masses[2]
h = 3/(PI*PI)
increment = symbols[2]-symbols[1]
resource_B = p1*p2/h*increment*I('0.75')
defect = residual_R-resource_B
derivative_bound = I(4)/3+4/I(5).sqrt()
checks = {
    'all_and_only_overlapping_prime_powers': I(7).ln().hi < 2 < I(8).ln().lo,
    'Lambda4_log2': prime_rows[2]['prime_base'] == 2,
    'correlation_simplification_overlap': all(row['formulas_overlap'] for row in prime_rows),
    'eligible_by_C759d': D('0.00364123566126519') < (I(1)/250).lo,
    'primitive_actual_norm': h.lo > 0,
    'q_second_derivative_bound': derivative_bound.hi < 4,
    'compact_formula_denominator_positive': (PI*PI-4).lo > 0,
    'low_mass_probability': 0 < p1.lo < p1.hi < 1,
    'high_mass_probability': 0 < p2.lo < p2.hi < 1,
    'symbol_increment_positive': increment.lo > 0,
    'resource_positive': resource_B.lo > 0,
    'positive_residual_at_required_threshold_zero': defect.lo > 0,
}
failures = [name for name, ok in checks.items() if not ok]
certificate = {
    'kind': 'single-input fixed-band signed-payment certificate; REPRODUCTION; unaudited',
    'parameters': {'input': 's1=sin(pi*x)', 'half_width': 1, 'cap': '1/250',
                   'bands': [1, 2], 'gamma_N': K_GAMMA, 'psi_N': K_PSI,
                   'midpoint_N_each_interval': N_MID, 'precision': 60},
    'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'arithmetic_source': {'path': str(ARITH.relative_to(BASE.parent.parent)),
                          'sha256': hashlib.sha256(ARITH.read_bytes()).hexdigest(),
                          'scope': 'AST prefix before class Z, no matrix execution'},
    'constants': {'pi': PI.save(), 'sinh_half': sh.save(), 'alpha': alpha.save(),
                  'harmonic_terms': harmonic_rows, 'harmonic_sum': harmonic.save(),
                  'gamma_center': gamma_center.save(), 'gamma': gamma.save()},
    'correction': {'pole_s': pole_s.save(), 'pole_g': pole_g.save(),
                   'relative_pole': relative_pole.save(), 'prime_terms': prime_rows,
                   'prime_s': prime_s.save(), 'prime_g': prime_g.save(),
                   'E_s': e_s.save(), 'E_g': e_g.save(),
                   'relative_prime': (prime_g/3-prime_s).save(), 'R': residual_R.save()},
    'digamma': psi_rows, 'quadrature': mass_rows,
    'result': {'h': h.save(), 'R': residual_R.save(), 'p1': p1.save(), 'p2': p2.save(),
               'm1': symbols[1].save(), 'm2': symbols[2].save(),
               'm_increment': increment.save(), 'B': resource_B.save(),
               'R_minus_B': defect.save(), 'required_threshold': 0,
               'decision': 'STOP fixed-band sufficient estimate at eligible s1' if not failures else 'INCONCLUSIVE'},
    'analytic_bounds': {'gamma_error': '[-1/N,0]',
                        'psi_tail': '[0,a/N+b^2/(2*N^2)]',
                        'q_second_derivative_actual_bound': derivative_bound.save(),
                        'quadrature_error': '4*L^3/(24*N^2)',
                        'infinite_fourier_complement': 'Plancherel: p2=1-mass(|t|<=2)'},
    'checks': checks, 'failures': failures,
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(certificate, indent=2)+'\n')
for key, val in certificate['result'].items():
    print(key, val)
print('Checks:', len(checks), 'Failures:', failures, 'Full certificate:', out)
if failures:
    raise SystemExit(1)
