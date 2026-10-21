"""Independent exact arithmetic and full finite-evidence audit of L100.

H is reconstructed by multinomial expansion of L095 identity (4).
Residue roots use inversion of cubing on the odd residues, rather than
the original generator's root search. No p-adic existence is inferred
from these finite checks; the canonical proof imports Hensel's theorem.
"""
import hashlib
import json
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
source = HERE / 'two-lifts-certificate.json'
raw = source.read_bytes()
old = json.loads(raw)
checks = []


def check(name, actual, required):
    checks.append(dict(name=name, actual=actual, required=required,
                       passed=actual == required))


def valuation(n):
    if n == 0:
        return None
    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


# Index is the m-exponent; the complementary n-exponent totals eleven.
product = [0] * 12
for r in range(6):
    for s in range(6-r):
        t = 5-r-s
        coefficient = factorial(5)//(factorial(r)*factorial(s)*factorial(t))*3**r
        product[2*r+s] += coefficient
        product[2*r+s+1] -= 5*coefficient
identity_coefficients = [-x for x in product]
identity_coefficients[0] += 1
hc = identity_coefficients[3:]
check('identity: coefficients below m^3 vanish', identity_coefficients[:3], [0, 0, 0])
check('all nine H coefficients', hc, [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215])
check('stored H coefficients', old['H_coefficients_m_ascending'], hc)


def form(m, n):
    return sum(c*m**i*n**(8-i) for i, c in enumerate(hc))


def quadratic(m, n):
    return n*(n+m)+3*m*m


check('odd cube residues form a permutation',
      sorted(pow(x, 3, 32) for x in range(1, 32, 2)), list(range(1, 32, 2)))
check('cubing inverts cubing on odd residues',
      all(pow(pow(x, 3, 32), 3, 32) == x for x in range(1, 32, 2)), True)
check('even cubes are even', all(pow(x, 3, 32) % 2 == 0 for x in range(0, 32, 2)), True)

records, domains, original_checks = {}, {}, []
for system in ['I', 'II']:
    d = 1 if system == 'I' else 5
    scale = d**11

    def right_base(m, u):
        return 5*m+u**5 if system == 'I' else m+5**10*u**5

    triples, residue_failures = [], []
    for m in range(32):
        for u in range(32):
            if (m % 2, u % 2) == (0, 0):
                continue
            c = right_base(m, u)
            n = d*c
            hv = form(m, n)
            normalized = hv*pow(scale, -1, 32) % 32
            a = pow(normalized, 3, 32)
            aa, b = m*a, quadratic(m, n)*u
            if (normalized % 2 != 1 or a % 2 != 1 or
                    (scale*a**3-hv) % 32 != 0 or
                    (aa**3+b**5-c**11) % 32 != 0 or
                    aa % 2 == b % 2 == c % 2 == 0):
                residue_failures.append([m, u, a])
            triples.append([m, u, a])
    expected_domain = dict(modulus=32, primitive_pair_count=768,
                           surviving_triple_count=768, triples=triples,
                           failures=residue_failures)
    check(f'{system}: actual primitive domain size', len(triples), 768)
    check(f'{system}: full-domain arithmetic failures', residue_failures, [])
    check(f'{system}: complete stored domain and every triple',
          old['residue_domains'][system], expected_domain)
    domains[system] = expected_domain

    c = right_base(1, 1)
    n = d*c
    hv, b = form(1, n), quadratic(1, n)
    a0 = pow(hv*pow(scale, -1, 32), 3, 32)
    error = scale*a0**3-hv
    derivative = 3*scale*a0**2
    lhs = n**11-b**5*(n-5)
    residual = c**11-b**5-a0**3
    expected = dict(m=1, u=1, d=d, scale=scale, C=c, N=n, Q=b, H=hv,
                    a0=a0, polynomial_coefficients_ascending=[-hv, 0, 0, scale],
                    error=error, derivative=derivative,
                    error_valuation=valuation(error),
                    derivative_valuation=valuation(derivative), hensel_n=5,
                    twice_k=2*valuation(derivative), required_strict_bound=5,
                    a_root_modulus=32, A_root_residue=a0, B=b,
                    C_valuation=valuation(c), B_valuation=valuation(b),
                    identity_left=lhs, identity_right=hv,
                    seed_original_residual=residual,
                    predicted_seed_residual=-(error//scale))
    check(f'{system}: every stored seed field', old['lift_records'][system], expected)
    check(f'{system}: seed in stated disk', a0, 27 if system == 'I' else 7)
    check(f'{system}: exact error valuation', valuation(error), 5)
    check(f'{system}: derivative valuation', valuation(derivative), 0)
    check(f'{system}: modulo-64 valuation table',
          [n % 64, hv % 64, scale*a0**3 % 64, error % 64],
          [6, 3, 35, 32] if system == 'I' else [34, 59, 27, 32])
    check(f'{system}: shared-coordinate identities', [n-d*c, n-5-scale], [0, 0])
    check(f'{system}: exact numerical identity', lhs, hv)
    check(f'{system}: original seed residual equals -error/scale',
          [error % scale, residual], [0, -(error//scale)])
    check(f'{system}: reconstructed parity and nonzero coordinates',
          [a0 % 2, b % 2, c % 4, a0 != 0, b != 0, c != 0],
          [1, 1, 2, True, True, True])
    records[system] = expected

    # Replay the exact original assertion names as well as their truth values.
    originals = [
        ('complete primitive residue domain, one odd cube root per pair',
         len(triples) == 768 and not residue_failures),
        ('unique odd seed modulo 32', a0 % 2 == 1),
        ('actual error vanishes mod 32', error % 32 == 0),
        ('exact valuation evidence', error != 0 and error % 64 == 32),
        ('strict Hensel inequality', 2*valuation(derivative) < 5),
        ('full complementary identity', lhs == hv),
        ('same shared coordinate and both scales', n == d*c and n-5 == scale),
        ('exact reconstructed residual', error % scale == 0 and residual == -(error//scale)),
        ('nonzero coordinates and local primitivity',
         a0 % 2 == b % 2 == 1 and c != 0),
    ]
    original_checks.extend(dict(name=f'{system}: {name}', passed=bool(ok))
                           for name, ok in originals)

check('all original assertion records replayed', old['checks'], original_checks)
check('all original assertions true', all(c['passed'] for c in original_checks), True)
check('original pass/required/failure totals',
      [old['passed'], old['required'], old['failures']], [18, 18, []])
check('complete original top-level schema', sorted(old),
      sorted(['target', 'scope', 'H_coefficients_m_ascending', 'residue_domains',
              'lift_records', 'checks', 'passed', 'required', 'failures']))
failures = [c['name'] for c in checks if not c['passed']]
out = HERE / 'two-lifts-audit-certificate.json'
result = dict(target='Independent arithmetic audit of both complete L100 constructions',
              source_sha256=hashlib.sha256(raw).hexdigest(),
              H_coefficients_m_ascending=hc, lift_records=records,
              residue_domains=domains, original_assertions_replayed=original_checks,
              proof_scope='Hensel existence, uniqueness and reconstruction checked in L100; finite replay is supporting evidence only',
              checks=checks, passed=len(checks)-len(failures), required=len(checks), failures=failures)
out.write_text(json.dumps(result, indent=2)+'\n')
for name, r in records.items():
    print(f"{name}: full triples={len(domains[name]['triples'])}/768; "
          f"v2(error)={r['error_valuation']} (required >=5); "
          f"2k={r['twice_k']} < n={r['hensel_n']}; "
          f"v2(C)={r['C_valuation']}, v2(B)=0; all seed fields replayed")
print(f"Audit checks={result['passed']}/{result['required']}; "
      f"original assertions={len(original_checks)}/18; failures={failures}; certificate={out}")
raise SystemExit(bool(failures))
