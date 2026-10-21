#!/usr/bin/env python3
"""Independent coefficient, complete-record and finite-domain audit of L099.

Derive H by the multinomial theorem from L095's identity; expand F in U
and formally differentiate. Do not import or execute the original generator.
"""
import hashlib
import itertools
import json
from math import comb, factorial
from pathlib import Path

BASE = Path(__file__).resolve().parent
OUT = BASE / 'three-lifts-audit-certificate.json'
SOURCE = BASE / 'three-lifts-certificate.json'
CROSS = BASE / 'three-lifts-identity-crosscheck.json'
original = json.loads(SOURCE.read_text())
cross = json.loads(CROSS.read_text())
checks = []


def check(name, value):
    checks.append({'name': name, 'pass': bool(value)})


def v3(x):
    if x == 0:
        return None
    result = 0
    while x % 3 == 0:
        x //= 3
        result += 1
    return result


# Expand (3m^2+mn+n^2)^5 by multinomial coefficients, then multiply
# by n-5m. Sparse keys are the full (m,n) exponents.
q5 = {}
for i in range(6):
    for j in range(6-i):
        k = 5-i-j
        key = (2*i+j, j+2*k)
        value = factorial(5)//(factorial(i)*factorial(j)*factorial(k))*3**i
        q5[key] = q5.get(key, 0) + value
complement = {(0, 11): 1}
for (i, j), value in q5.items():
    complement[i, j+1] = complement.get((i, j+1), 0) - value
    complement[i+1, j] = complement.get((i+1, j), 0) + 5*value
complement = {key: value for key, value in complement.items() if value}
check('complement has exactly m^3 times all nine degree-eight monomials',
      set(complement) == {(i+3, 8-i) for i in range(9)})
hc = [complement.get((i+3, 8-i), 0) for i in range(9)]
check('all independently derived H coefficients match L095 and L099',
      hc == [55, 165, 594, 1100, 2145, 2475, 2970, 1782, 1215])


def h(m, n):
    return sum(hc[i]*m**i*n**(8-i) for i in range(9))


def horner(coefficients, u):
    result = 0
    for c in reversed(coefficients):
        result = result*u+c
    return result


replayed_records = {}
audit_rows = {}
identity_rows = []
cross_rows = []
replayed_checks = []
tail_checks = []
for name, a, u0, scale in [('I', 1, 25, 1), ('II', 2, 7, 5**11)]:
    # N(U) = 15 + scale*U^5, not an independently varied C.
    fc = [0]*41
    for i, c in enumerate(hc):
        for j in range(9-i):
            fc[5*j] += c*3**i*comb(8-i, j)*15**(8-i-j)*scale**j
    fc[0] -= scale*a**3
    dc = [(j+1)*fc[j+1] for j in range(40)]
    check(f'{name}: full substituted polynomial modulo three',
          [x % 3 for x in fc] == [2]+[0]*39+[1])
    check(f'{name}: full formal derivative modulo three',
          [x % 3 for x in dc] == [0]*39+[1])
    reduced_h = [hc[i]*3**i % 243 for i in range(9)]
    check(f'{name}: full H(3,N) modulo 243',
          reduced_h == [55, 9, 0, 54, 0, 0, 0, 0, 0])
    # Exhaustive direct product of (m,u,a), including all zero residues.
    admissible_pairs = set()
    triples = []
    for m, u, cube in itertools.product(range(27), repeat=3):
        n = (5*m + scale*pow(u, 5, 27)) % 27
        C = n if name == 'I' else 11*n % 27  # 5^-1 = 11 modulo 27
        if (m % 3, u % 3) == (0, 0) or C % 3 == 0:
            continue
        admissible_pairs.add((m, u))
        if (h(m, n)-scale*cube**3) % 27 == 0:
            triples.append([m, u, cube])
    surviving_pairs = {(m, u) for m, u, _ in triples}
    seeds = [u for u in range(1, 27, 3) if horner(fc, u) % 27 == 0]
    m = 3
    n = 15+scale*u0**5
    C = n if name == 'I' else n//5
    q = 3*m*m+m*n+n*n
    A, B = m*a, q*u0
    error = horner(fc, u0)
    derivative = horner(dc, u0)
    hv = h(m, n)
    # Independent derivative from the differentiated complementary identity.
    numerator_d = 11*n**10-5*q**4*(m+2*n)*(n-5*m)-q**5
    check(f'{name}: exact derivative from differentiated identity',
          numerator_d % m**3 == 0 and
          derivative == (numerator_d//m**3)*5*scale*u0**4)
    check(f'{name}: independently expanded error equals direct identity',
          (n**11-q**5*(n-5*m)) == m**3*(error+scale*a**3))
    check(f'{name}: actual error valuation 4 exceeds required 0', v3(error) == 4)
    check(f'{name}: actual derivative valuation 0 and 0 < Hensel n=3',
          v3(derivative) == 0 and error % 27 == 0)
    check(f'{name}: both exact chosen coordinates a and m nonzero', a != 0 and m != 0)
    check(f'{name}: cube coordinate nonunit A has exact valuation one', v3(A) == 1)
    check(f'{name}: complete finite-domain counts',
          len(admissible_pairs) == 486 and len(surviving_pairs) == 162 and
          len(triples) == 810)
    check(f'{name}: selected first seed and all zero cube residues retained',
          seeds[0] == u0 and [m, u0, a] in triples and
          any(cube == 0 for _, _, cube in triples))
    residues = {key: value % 3 for key, value in
                dict(m=m, u=u0, a=a, A=A, B=B, C=C, n=n, Q=q).items()}
    r = dict(modulus=27, total_m_u_pairs=729,
             admissible_m_u_pairs=len(admissible_pairs),
             surviving_m_u_pairs=len(surviving_pairs),
             surviving_triples_count=len(triples), surviving_triples=triples,
             fixed_m_a_seed_u=[m, a, u0], all_seed_u_in_1_mod_3=seeds,
             C_at_seed=C, n_at_seed=n, scale=scale, H_at_seed=hv,
             Q_at_seed=q, A_at_seed=A, B_at_seed=B, error=error,
             derivative=derivative, error_valuation=v3(error),
             derivative_valuation=v3(derivative),
             required_error_valuation_strictly_greater_than=0,
             error_quotient_mod_3=(error//81) % 3,
             derivative_mod_3=derivative % 3, residues_mod_3=residues,
             hensel_n=3, hensel_k=0, root_congruence_modulus=27,
             refinement_used=False)
    stored = original['records'][name]
    for key in r:
        check(f'{name}: complete stored field {key}', r[key] == stored.get(key))
    check(f'{name}: exact record schema', set(r) == set(stored))
    replayed_records[name] = r
    truths = [
        ('selected modulo-27 seed exists', bool(seeds)),
        ('full complementary identity', n**11-q**5*(n-5*m) == m**3*hv),
        ('defining linear difference', n-5*m == scale*u0**5),
        ('reconstruction error identity', scale*(C**11-B**5-A**3) == m**3*error),
        ('exact seed error divisible by 27', error % 27 == 0),
        ('derivative unit', v3(derivative) == 0),
        ('strict Hensel inequality', v3(error) > 2*v3(derivative)),
        ('fixed a and m nonzero', A != 0),
        ('u and C units', u0 % 3 != 0 and C % 3 != 0),
        ('Q and B units', q % 3 != 0 and B % 3 != 0),
        ('primitive pair', (m % 3, u0 % 3) != (0, 0)),
        ('selected seed in exhaustive list', [m, u0, a] in triples)]
    replayed_checks.extend({'name': f'{name}: {s}', 'pass': bool(t)} for s, t in truths)
    extra = [
        ('identity numerator divisible by m cubed', (n**11-q**5*(n-5*m)) % m**3 == 0),
        ('independent full H matches', (n**11-q**5*(n-5*m))//m**3 == hv),
        ('independent full error matches', hv-scale*a**3 == error),
        ('independent error valuation four', error % 243 in (81, 162)),
        ('A exact valuation one', A % 9 in (3, 6))]
    tail_checks.extend({'name': f'{name}: {s}', 'pass': bool(t)} for s, t in extra)
    row = dict(system=name, m=m, a=a, u0=u0, F_mod_243=error % 243,
               derivative_mod_3=derivative % 3, C_mod_3=C % 3, B_mod_3=B % 3)
    identity_rows.append(row)
    cross_row = dict(row, checks=dict(
        H_matches_independent_identity=(n**11-q**5*(n-5*m))//m**3 == hv,
        full_error_matches=error == hv-scale*a**3,
        error_mod_243_nonzero_multiple_81=error % 243 in (81, 162),
        derivative_mod_3_is_1=derivative % 3 == 1,
        C_and_B_unit=C % 3 != 0 and B % 3 != 0,
        A_exact_valuation_1=v3(A) == 1))
    cross_rows.append(cross_row)
    audit_rows[name] = dict(F_coefficients_ascending=fc,
                            derivative_coefficients_ascending=dc,
                            N_mod_243=n % 243, scale_a3_mod_243=scale*a**3 % 243,
                            H_mod_243=hv % 243, F_mod_243=error % 243,
                            error_valuation=v3(error), required_error_lower_bound=0,
                            derivative_valuation=v3(derivative),
                            derivative_identity_numerator=numerator_d,
                            C_reconstruction=C, n_reconstruction=n)

replayed_checks.extend(tail_checks)
expected = dict(target='primitive Z_3 realizations of both complete L095 systems with C a unit',
                records=replayed_records, identity_crosscheck=identity_rows,
                checks=replayed_checks,
                failures=[c['name'] for c in replayed_checks if not c['pass']],
                check_count=len(replayed_checks),
                passed=sum(c['pass'] for c in replayed_checks))
check('all 34 independently replayed original assertions pass',
      len(replayed_checks) == 34 and all(c['pass'] for c in replayed_checks))
check('complete original certificate equality including failures and all lists', original == expected)
check('complete second certificate equality including all row checks',
      cross == dict(rows=cross_rows, failures=[]))
failures = [c['name'] for c in checks if not c['pass']]
out = dict(target="Independent critical arithmetic audit of L099's two Z_3 constructions",
           source_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
           crosscheck_sha256=hashlib.sha256(CROSS.read_bytes()).hexdigest(),
           H_coefficients=hc,
           full_complementary_polynomial={f'{i},{j}': c for (i, j), c in sorted(complement.items())},
           audit_rows=audit_rows, replayed_original_certificate=expected,
           replayed_crosscheck_certificate=dict(rows=cross_rows, failures=[]),
           checks=checks, check_count=len(checks),
           passed=len(checks)-len(failures), failures=failures)
OUT.write_text(json.dumps(out, indent=2)+'\n')
for name, row in audit_rows.items():
    print(f"{name}: v3(error)={row['error_valuation']} > required 0; "
          f"v3(derivative)={row['derivative_valuation']}; "
          f"full triples={len(replayed_records[name]['surviving_triples'])}/810")
print(f"audit checks={len(checks)}, passed={out['passed']}, failures={failures}")
print('original assertions=34/34; original certificates compared in full')
print(f'full certificate: {OUT.relative_to(BASE.parent.parent)}')
raise SystemExit(bool(failures))
