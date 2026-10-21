"""Bounded mod-32 test and exact Hensel hypotheses for both L095 systems.

The certificate records full finite evidence. Exact existence follows from
the cited Hensel theorem and reconstruction in L100, not from sampling.
"""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
COEFF = [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215]


def q(m, n):
    return 3*m*m + m*n + n*n


def h(m, n):
    return sum(c*m**i*n**(8-i) for i, c in enumerate(COEFF))


def v2(n):
    if n == 0:
        return None
    return (abs(n) & -abs(n)).bit_length()-1


checks = []


def check(name, ok):
    checks.append(dict(name=name, passed=bool(ok)))


domains, records = {}, {}
for name, d, scale in [('I', 1, 1), ('II', 5, 5**11)]:
    # C is substituted before either the finite test or exact seed check.
    def c_value(m, u):
        return 5*m + u**5 if name == 'I' else m + 5**10*u**5

    triples = []
    pairs = 0
    failures = []
    for m in range(32):
        for u in range(32):
            if m % 2 == 0 and u % 2 == 0:
                continue
            pairs += 1
            c = c_value(m, u)
            n = d*c
            roots = [a for a in range(32)
                     if (scale*a**3-h(m, n)) % 32 == 0]
            if len(roots) != 1:
                failures.append([m, u, roots])
            for a in roots:
                aa, b = m*a, q(m, n)*u
                if a % 2 != 1 or (aa % 2 == b % 2 == c % 2 == 0):
                    failures.append([m, u, a, 'parity/primitivity'])
                if (aa**3+b**5-c**11) % 32:
                    failures.append([m, u, a, 'reconstructed equation'])
                triples.append([m, u, a])
    domains[name] = dict(modulus=32, primitive_pair_count=pairs,
                         surviving_triple_count=len(triples),
                         triples=triples, failures=failures)
    check(f'{name}: complete primitive residue domain, one odd cube root per pair',
          pairs == 768 and len(triples) == 768 and not failures)

    m = u = 1
    c = c_value(m, u)
    n = d*c
    hv = h(m, n)
    a0s = [a for a in range(32) if (scale*a**3-hv) % 32 == 0]
    check(f'{name}: unique odd seed modulo 32', len(a0s) == 1 and a0s[0] % 2 == 1)
    a0 = a0s[0]
    error = scale*a0**3-hv
    derivative = 3*scale*a0*a0
    b = q(m, n)*u
    identity_left = n**11-q(m, n)**5*(n-5*m)
    identity_right = m**3*hv
    record = dict(m=m, u=u, d=d, scale=scale, C=c, N=n, Q=q(m, n),
                  H=hv, a0=a0, polynomial_coefficients_ascending=[-hv, 0, 0, scale],
                  error=error, derivative=derivative, error_valuation=v2(error),
                  derivative_valuation=v2(derivative), hensel_n=5,
                  twice_k=2*v2(derivative), required_strict_bound=5,
                  a_root_modulus=32, A_root_residue=a0 % 32, B=b,
                  C_valuation=v2(c), B_valuation=v2(b),
                  identity_left=identity_left, identity_right=identity_right,
                  seed_original_residual=c**11-b**5-(m*a0)**3,
                  predicted_seed_residual=-m**3*error//scale)
    records[name] = record
    check(f'{name}: actual error vanishes mod 32', error % 32 == 0)
    check(f'{name}: exact valuation evidence',
          error != 0 and error % 2**(v2(error)+1) == 2**v2(error))
    check(f'{name}: strict Hensel inequality', v2(derivative) == 0 and 0 < 5)
    check(f'{name}: full complementary identity', identity_left == identity_right)
    check(f'{name}: same shared coordinate and both scales',
          n == d*c and n-5*m == scale*u**5 and d**11 == scale)
    check(f'{name}: exact reconstructed residual',
          m**3*error % scale == 0 and
          record['seed_original_residual'] == record['predicted_seed_residual'])
    check(f'{name}: nonzero coordinates and local primitivity',
          m == u == 1 and a0 % 2 == 1 and b % 2 == 1 and c != 0)

failures = [x['name'] for x in checks if not x['passed']]
result = dict(target='primitive Z_2 points in both complete L095 systems',
              scope='Existence only; no global compatibility or integer solution',
              H_coefficients_m_ascending=COEFF, residue_domains=domains,
              lift_records=records, checks=checks,
              passed=len(checks)-len(failures), required=len(checks), failures=failures)
out = HERE / 'two-lifts-certificate.json'
out.write_text(json.dumps(result, indent=2)+'\n')
for name, r in records.items():
    print(f"{name}: primitive pairs=768, surviving triples={len(domains[name]['triples'])}; "
          f"a0={r['a0']}, actual v2(error)={r['error_valuation']}, "
          f"k={r['derivative_valuation']}, required 2k < n: {r['twice_k']} < 5; "
          f"v2(C)={r['C_valuation']}, v2(B)={r['B_valuation']}")
print(f"Checks={result['passed']}/{result['required']}; failures={failures}; certificate={out}")
raise SystemExit(bool(failures))
