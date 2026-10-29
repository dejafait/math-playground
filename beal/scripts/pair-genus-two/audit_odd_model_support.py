"""L138 audit supplement: canonical literal binding and exceptional charts.

No producer/replay imports, searches, or upstream arithmetic reruns.
The separately reviewed complete replay supplies field/discriminant arithmetic.
"""
from fractions import Fraction as Q
from pathlib import Path
from math import comb, prod
import hashlib
import json
import re
import traceback

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'odd-model-support-audit.json'
report = {'checks': [], 'failures': [], 'bindings': {}, 'charts': {},
          'bounds': {'coefficient_slots_cap': 7, 'matrix_entries_cap': 64,
                     'chart_degree_cap': 6, 'rational_bits_cap': 4096,
                     'max_rational_bits': 0,
                     'meaning': 'fixed-domain and observed-size bounds, not operation counts'}}


def check(name, value):
    report['checks'].append({'name': name, 'pass': bool(value)})
    if not value:
        report['failures'].append(name)
        raise AssertionError(name)


def read(relative):
    p = ROOT / relative
    b = p.read_bytes()
    report['bindings'][relative] = hashlib.sha256(b).hexdigest()
    return b.decode()


def normal(s):
    s = s.replace('−', '-').replace('≠', '!=')
    s = re.sub('[⁰¹²³⁴⁵⁶⁷⁸⁹]+', lambda m: '^' + m[0].translate(
        str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹', '0123456789')), s)
    return re.sub(r'\s+', '', s)


def polynomial(a, variable):
    terms = []
    for i in range(len(a)-1, -1, -1):
        v = a[i]
        assert type(v) is int
        if not v:
            continue
        term = str(abs(v)) if i == 0 or abs(v) != 1 else ''
        if i:
            term += variable + ('^' + str(i) if i != 1 else '')
        terms.append(('-' if v < 0 else '+') + term)
    return ''.join(terms).lstrip('+') or '0'


def matrix(text, name):
    s = re.search(r'^    ' + re.escape(name) + r' = (\[\[.*?\]\])',
                  text, re.M | re.S)[1].replace('−', '-')
    rows = [[Q(x.strip()) for x in row.split(',')]
            for row in re.findall(r'\[([^\[\]]+)\]', s)]
    assert len(rows) == 4 and all(len(r) == 4 for r in rows)
    return rows


def rational_matrix(rows):
    return [[Q(x) for x in row] for row in rows]


def observe(v):
    if isinstance(v, (int, Q)) and not isinstance(v, bool):
        q = Q(v)
        b = max(abs(q.numerator).bit_length(), q.denominator.bit_length())
        report['bounds']['max_rational_bits'] = max(report['bounds']['max_rational_bits'], b)
        assert b <= 4096
    elif isinstance(v, list):
        for x in v:
            observe(x)


try:
    data = json.loads(read('scripts/pair-genus-two/odd-model-support-certificate.json'))
    replay = json.loads(read('scripts/pair-genus-two/odd-model-support-verification.json'))
    before = json.loads(read('scripts/pair-genus-two/odd-model-support-preaudit-verification.json'))
    # Full objects, including every Euclidean resultant-chain coefficient.
    check('entire_replay_unchanged', replay == before)
    check('replay_source_hash', replay['input_sha256'] == report['bindings'][
        'scripts/pair-genus-two/odd-model-support-certificate.json'])
    for name, obj, count in [('producer', data, 22), ('replay', replay, 82)]:
        check(name + '_all_checks', obj['status'] == 'PASS' and obj['failures'] == []
              and len(obj['checks']) == count and all(x['pass'] is True for x in obj['checks']))
    texts = {i: read('lemmas/' + filename) for i, filename in [
        (110, 'L110-explicit-pair-genus-two-model.md'),
        (133, 'L133-pair-quartic-field-no-quadratic-tower.md'),
        (134, 'L134-pair-quartic-maximal-order.md'),
        (137, 'L137-pair-quartic-localized-parity-bound.md'),
        (138, 'L138-pair-odd-model-and-descent-support.md')]}
    n = {i: normal(s) for i, s in texts.items()}
    m, field = data['model'], data['field']
    check('printed_G', 'G=' + polynomial(m['G'], 'X') + ',' in n[138])
    check('printed_H', 'H=' + polynomial(m['H'], 'X') + '.' in n[138])
    check('printed_A', 'A(U)=' + polynomial(field['alpha_polynomial'], 'U') + ',' in n[138])
    check('L133_same_polynomial', 'g(X)=' + polynomial(field['alpha_polynomial'], 'X') + ',' in n[133])
    check('L110_same_sextic', '=' + polynomial(m['f'], 'T') + '.' in n[110])
    check('L138_exact_Q4', 'Q4(T)=7+52T-6T^2-64T^3-25T^4.' in n[138]
          and m['q4'] == [7, 52, -6, -64, -25])
    for label, key in [('M', 'eta_powers_in_alpha'), ('N', 'alpha_powers_in_eta'),
                       ('B_eta', 'O_basis_in_eta')]:
        check('printed_' + label, matrix(texts[138], label) == rational_matrix(field[key]))
    check('L134_whole_basis', matrix(texts[134], 'B') == rational_matrix(field['O_basis_in_alpha']))
    check('generator_vectors_bound_to_columns',
          [row[1] for row in field['eta_powers_in_alpha']] == field['eta_in_alpha'] and
          [row[1] for row in field['alpha_powers_in_eta']] == field['alpha_in_eta'])
    check('printed_determinants', 'det(M)=' + str(field['eta_to_alpha_determinant']) in n[138]
          and 'det(N)=' + str(field['alpha_to_eta_determinant']) in n[138])
    check('printed_forward_inverse', 'X=c/(T-2),Y=c^2W/(T-2)^3,T=2+c/X,W=cY/X^3.' in n[138])
    check('exact_u_z_marking',
          'u_X=[F(T_X)-11-K0(T_X)W_X]/[60F(T_X)],M_X=2-10u_X,' in n[138]
          and 'z_X=-M_X^2(T_X-2)L0(T_X)^2/[300(T_X+2)K0(T_X)^2],' in n[138]
          and 's_X=H0(u_X,z_X).' in n[138] and 'v^2=z_X' in n[138])
    for name, key in [('G', 'discriminant'), ('H', 'discriminant'), ('linear_H', 'resultant')]:
        d = data['discriminants'][name]
        factors = d['factorization']['factors']
        product = prod(p**e for p, e in factors)
        factor_string = ''.join(str(p) + '^' + str(e) for p, e in factors)
        check('printed_' + name + '_value_factors',
              str(d[key]) + '=' + factor_string in n[138] and d[key] == product)
        check(name + '_positive_complete_factorization', type(d[key]) is int
              and d[key] > 0 and d['factorization']['cofactor'] == 1)
    c, f, G = Q(m['c']), m['f'], m['G']
    # Two complete chart identities computed by the binomial theorem.
    # h=1/X=(T-2)/c, Z=Y/X^3=W/c.
    odd = [sum(Q(f[i])*comb(i,j)*2**(i-j)*c**(j-2)
               for i in range(j, 7)) for j in range(7)]
    expected_odd = [Q(0)] + list(map(Q, reversed(G)))
    report['charts']['odd_infinity_coefficients'] = odd
    check('odd_chart_full_identity', odd == expected_odd and odd[1] == 1)
    # (1-2k)^6 G(ck/(1-2k)) = c^4 k^6 f(1/k).
    sextic = [sum(Q(G[i])*c**i*comb(6-i, j-i)*(-2)**(j-i)
                   for i in range(min(j, 5)+1)) for j in range(7)]
    expected_sextic = [c**4*x for x in reversed(f)]
    report['charts']['sextic_infinity_identity_coefficients'] = sextic
    check('sextic_chart_full_identity', sextic == expected_sextic)
    check('infinity_fiber_residue_field', f[-1] == -275 == -11*5**2
          and G[0] == -275*c**4 != 0)
    check('branch_fibers', sum(f[i]*2**i for i in range(7)) == 0
          and sum(i*f[i]*2**(i-1) for i in range(1,7)) == c
          and sum(f[i]*(-2)**i for i in range(7)) == 0
          and c/(-4) == m['linear_root'] == 9075)
    check('identical_localization', data['support']['finite_rational_primes'] == [2,3,5,11]
          and data['support']['localization_integer'] == 330
          and 'B=O[1/330]' in n[137] and 'dim_F2Cl(B)/2Cl(B)<=32-30=2.' in n[137])
    check('printed_class_bound', 'dim_F2Cl(O_K[1/330])/2Cl(O_K[1/330])<=2.' in n[138])
    # The mathematical distinction is reviewed in L138's audit prose;
    # this check binds the bound, not a proof inferred from wording.
    report['bounds'].update({'coefficient_slots': len(odd), 'chart_degree': 6,
                             'matrix_entries': 4*16})
    observe(odd + sextic)
    for key in ['eta_powers_in_alpha', 'alpha_powers_in_eta', 'O_basis_in_alpha', 'O_basis_in_eta']:
        observe(rational_matrix(field[key]))
    report['status'] = 'PASS'
except Exception as exc:
    report['status'] = 'FAIL'
    report['exception'] = {'type': type(exc).__name__, 'message': str(exc),
                           'traceback': traceback.format_exc()}
    if not report['failures']:
        report['failures'].append(str(exc))
finally:
    def encode(v):
        if isinstance(v, Q):
            return int(v) if v.denominator == 1 else str(v)
        if isinstance(v, list):
            return [encode(x) for x in v]
        if isinstance(v, dict):
            return {k: encode(x) for k, x in v.items()}
        return v
    OUT.write_text(json.dumps(encode(report), indent=2) + '\n')
    print(json.dumps({'status': report['status'], 'checks': len(report['checks']),
        'failures': report['failures'], 'actual_required_bounds': report['bounds'],
        'certificate': str(OUT.relative_to(ROOT))}))
if report['status'] != 'PASS':
    raise SystemExit(1)
