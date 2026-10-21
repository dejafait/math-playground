"""Exact exterior-algebra corroboration of L142; no numerical optimization."""
import json
from pathlib import Path


def add(*forms):
    out = {}
    for form in forms:
        for key, value in form.items():
            out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value}


def scale(c, form):
    return {key: c * value for key, value in form.items() if c * value}


def wedge(a, b):
    out = {}
    for u, c in a.items():
        for v, d in b.items():
            if set(u).intersection(v):
                continue
            sign = (-1) ** sum(i > j for i in u for j in v)
            key = tuple(sorted(u + v))
            out[key] = out.get(key, 0) + sign * c * d
    return {key: value for key, value in out.items() if value}


def product(*forms):
    out = {(): 1}
    for form in forms:
        out = wedge(out, form)
    return out


def pullback(form, mapping):
    return add(*(scale(c, product(*(mapping[i] for i in indices)))
                 for indices, c in form.items()))


def encode(form):
    return {','.join(map(str, key)): value for key, value in sorted(form.items())}


e = [{(i,): 1} for i in range(8)]
z = [add(e[i], e[i + 4]) for i in range(4)]
alpha = add(wedge(z[0], z[1]), scale(-1, wedge(z[2], z[3])))
beta = product(*z)
psi = wedge(add(wedge(e[0], e[1]), wedge(e[2], e[3])),
            add(wedge(e[4], e[5]), wedge(e[6], e[7])))
vol = {tuple(range(8)): 1}
I0 = [(1, -1), (0, 1), (3, -1), (2, 1)]
J0 = [(2, -1), (3, 1), (0, 1), (1, -1)]
I = [scale(sign, e[j + offset]) for offset in (0, 4) for j, sign in I0]
J = [scale(sign, e[j + offset]) for offset in (0, 4) for j, sign in J0]
K = [pullback(one, J) for one in I]
checks = {
    'I_invariance': pullback(alpha, I) == alpha,
    'J_invariance': pullback(alpha, J) == alpha,
    'K_invariance': pullback(alpha, K) == alpha,
    'alpha_squared_equals_minus_two_beta': wedge(alpha, alpha) == scale(-2, beta),
    'beta_squared_zero': wedge(beta, beta) == {},
    'beta_psi_equals_two_vol': wedge(beta, psi) == scale(2, vol),
    'alpha_squared_psi_equals_minus_four_vol': product(alpha, alpha, psi) == scale(-4, vol),
    'product_complex_orientation': product(add(wedge(e[0], e[1]), wedge(e[2], e[3])),
                                        add(wedge(e[0], e[1]), wedge(e[2], e[3])),
                                        add(wedge(e[4], e[5]), wedge(e[6], e[7])),
                                        add(wedge(e[4], e[5]), wedge(e[6], e[7]))) == scale(4, vol),
    'full_characteristic_square': 2 * 14 * 21 + 156 == 744,
}
certificate = {
    'checks': checks,
    'failures': [name for name, passed in checks.items() if not passed],
    'forms': {name: encode(form) for name, form in {
        'alpha': alpha, 'beta': beta, 'psi': psi,
        'alpha_squared': wedge(alpha, alpha), 'beta_squared': wedge(beta, beta),
        'beta_psi': wedge(beta, psi)}.items()},
    'normalization': {
        'T1': 'diag(i,-i)/sqrt(2); -tr(T1*T1)=1',
        'C': '-alpha^2/(8*pi^2)=beta/(4*pi^2)',
        'Q': '0', 'L': '1/(2*pi^2)', 'ratio': '0',
    },
    'threshold': {'J': 744, 'M': '2*lambda*s', 'volume': 's^2/4',
                  'gamma_required': '93/(2*lambda^2)',
                  'lambda_interval': '1<lambda<5/4 (L071)',
                  'strict_lower_bound': '744/25',
                  'actual_ratio': '0',
                  'verdict': 'No universal gamma>0; in particular none above gamma_required'},
}
path = Path(__file__).with_name('quartic_witness_certificate.json')
path.write_text(json.dumps(certificate, indent=2) + '\n')
print(f'Exact checks: {sum(checks.values())}/{len(checks)}; failures: {certificate["failures"]}')
print('Actual Q/L^2=0; required gamma>93/(2*lambda^2)>744/25.')
print(f'Certificate: {path}')
if certificate['failures']:
    raise SystemExit(1)
