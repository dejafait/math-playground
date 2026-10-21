#!/usr/bin/env python3
"""Full modulo-27 domain and exact Hensel certificates for L095 at three."""
import json
from pathlib import Path

OUT = Path(__file__).with_name('three-lifts-certificate.json')
COEFF = [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215]


def H(m, n):
    return sum(c * m**i * n**(8-i) for i, c in enumerate(COEFF))


def Hn(m, n):
    return sum((8-i) * c * m**i * n**(7-i) for i, c in enumerate(COEFF[:-1]))


def Q(m, n):
    return 3*m*m + m*n + n*n


def valuation(x):
    if x == 0:
        return None  # infinite; no selected error below is zero
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def parameters(system, m, u):
    if system == 'I':
        C = 5*m + u**5
        return C, C, 1, 5*u**4
    C = m + 5**10*u**5
    return C, 5*C, 5**11, 5**12*u**4


checks = []
records = {}

def check(name, ok):
    checks.append({'name': name, 'pass': bool(ok)})


for system, a_fixed in [('I', 1), ('II', 2)]:
    modulus = 27
    # Every residue, including a=0, is retained. m,u may individually
    # vanish modulo 27; the condition removes only simultaneous multiples of 3.
    cube_roots = {}
    scale = 1 if system == 'I' else 5**11
    for a in range(modulus):
        cube_roots.setdefault(scale*a**3 % modulus, []).append(a)
    admissible = 0
    surviving_pairs = 0
    triples = []
    for m in range(modulus):
        for u in range(modulus):
            C, n, _, _ = parameters(system, m, u)
            if (m % 3 == 0 and u % 3 == 0) or C % 3 == 0:
                continue
            admissible += 1
            roots = cube_roots.get(H(m, n) % modulus, [])
            if roots:
                surviving_pairs += 1
                triples.extend([m, u, a] for a in roots)
    # Choose the first root in the stated disk; this remains within the
    # original modulo-27 bound and needs no additional precision search.
    m = 3
    seeds = []
    for u in range(1, modulus, 3):
        C, n, scale, dn_du = parameters(system, m, u)
        if (H(m, n) - scale*a_fixed**3) % modulus == 0:
            seeds.append(u)
    check(f'{system}: selected modulo-27 seed exists', bool(seeds))
    if not seeds:
        records[system] = {'admissible_pairs': admissible, 'triples': triples,
                           'seed_failure': True}
        continue
    u = seeds[0]
    C, n, scale, dn_du = parameters(system, m, u)
    error = H(m, n) - scale*a_fixed**3
    derivative = Hn(m, n)*dn_du
    ve, vd = valuation(error), valuation(derivative)
    q = Q(m, n)
    A = m*a_fixed
    B = q*u
    check(f'{system}: full complementary identity',
          n**11 - q**5*(n-5*m) == m**3*H(m, n))
    check(f'{system}: defining linear difference',
          n-5*m == scale*u**5)
    check(f'{system}: reconstruction error identity',
          scale*(C**11 - B**5 - A**3) == m**3*error)
    check(f'{system}: exact seed error divisible by 27', error % 27 == 0)
    check(f'{system}: derivative unit', vd == 0)
    check(f'{system}: strict Hensel inequality', ve is not None and ve > 2*vd)
    check(f'{system}: fixed a and m nonzero', A != 0)
    check(f'{system}: u and C units', u % 3 != 0 and C % 3 != 0)
    check(f'{system}: Q and B units', q % 3 != 0 and B % 3 != 0)
    check(f'{system}: primitive pair', m % 3 != 0 or u % 3 != 0)
    check(f'{system}: selected seed in exhaustive list', [m, u, a_fixed] in triples)
    residues = {key: val % 3 for key, val in
                dict(m=m, u=u, a=a_fixed, A=A, B=B, C=C, n=n, Q=q).items()}
    records[system] = {
        'modulus': modulus,
        'total_m_u_pairs': modulus**2,
        'admissible_m_u_pairs': admissible,
        'surviving_m_u_pairs': surviving_pairs,
        'surviving_triples_count': len(triples),
        'surviving_triples': triples,
        'fixed_m_a_seed_u': [m, a_fixed, u],
        'all_seed_u_in_1_mod_3': seeds,
        'C_at_seed': C, 'n_at_seed': n, 'scale': scale,
        'H_at_seed': H(m, n), 'Q_at_seed': q,
        'A_at_seed': A, 'B_at_seed': B,
        'error': error, 'derivative': derivative,
        'error_valuation': ve, 'derivative_valuation': vd,
        'required_error_valuation_strictly_greater_than': 2*vd,
        'error_quotient_mod_3': (error // 3**ve) % 3,
        'derivative_mod_3': derivative % 3,
        'residues_mod_3': residues,
        'hensel_n': 3, 'hensel_k': 0, 'root_congruence_modulus': 27,
        'refinement_used': False,
    }

crosscheck_rows = []
for system, r in records.items():
    m, a, u = r['fixed_m_a_seed_u']
    C, n, scale, _ = parameters(system, m, u)
    q = Q(m, n)
    # Independent H evaluation through L095's complementary identity.
    numerator = n**11 - q**5*(n-5*m)
    check(f'{system}: identity numerator divisible by m cubed', numerator % m**3 == 0)
    h_from_identity = numerator // m**3
    error = h_from_identity - scale*a**3
    check(f'{system}: independent full H matches', h_from_identity == r['H_at_seed'])
    check(f'{system}: independent full error matches', error == r['error'])
    check(f'{system}: independent error valuation four', error % 243 in (81, 162))
    check(f'{system}: A exact valuation one', (m*a) % 9 in (3, 6))
    crosscheck_rows.append({'system': system, 'm': m, 'a': a, 'u0': u,
                           'F_mod_243': error % 243,
                           'derivative_mod_3': r['derivative'] % 3,
                           'C_mod_3': C % 3, 'B_mod_3': q*u % 3})

failures = [c['name'] for c in checks if not c['pass']]
certificate = {'target': 'primitive Z_3 realizations of both complete L095 systems with C a unit',
               'records': records, 'identity_crosscheck': crosscheck_rows,
               'checks': checks, 'failures': failures,
               'check_count': len(checks), 'passed': len(checks)-len(failures)}
OUT.write_text(json.dumps(certificate, indent=2) + '\n')
for name, r in records.items():
    print(f"{name}: admissible pairs={r['admissible_m_u_pairs']}; "
          f"surviving pairs={r.get('surviving_m_u_pairs')}; "
          f"triples={r.get('surviving_triples_count')}; "
          f"(m,a,u0)={r.get('fixed_m_a_seed_u')}; "
          f"v3(error)={r.get('error_valuation')} > "
          f"required {r.get('required_error_valuation_strictly_greater_than')}; "
          f"v3(derivative)={r.get('derivative_valuation')}")
print(f"checks={len(checks)} passed={certificate['passed']} failures={failures}")
print(f'full certificate: {OUT}')
raise SystemExit(bool(failures))
