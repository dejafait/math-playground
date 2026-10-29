"""Independent replay: alpha companion arithmetic, Gaussian norms,
iterative uniformizer division and low-pivot binary elimination.
Does not import producer code. Consumes every branch/witness/product record.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import hashlib
import traceback

ROOT = Path(__file__).resolve().parent
OUT = ROOT/'eleven-adic-filter-verification.json'
R = dict(completed=False, failures=[], checks=0, bindings={}, verified=[],
         bounds=dict(field_operations=0, field_operations_cap=100000,
                     max_rational_bits=0, rational_bits_cap=4096,
                     max_absolute_valuation=0, valuation_cap=128))
G = [-109375, -32500, 150, 64]


def need(p, label):
    R['checks'] += 1
    assert p, label


def size(x):
    if isinstance(x, (tuple, list)):
        for y in x:
            size(y)
    else:
        x = F(x)
        b = max(abs(x.numerator).bit_length(), x.denominator.bit_length())
        R['bounds']['max_rational_bits'] = max(b, R['bounds']['max_rational_bits'])
        need(b <= 4096, 'bit cap')
    return x


def operation(x):
    R['bounds']['field_operations'] += 1
    need(R['bounds']['field_operations'] <= 100000, 'operation cap')
    size(x)
    return x


def load(name, h=None):
    b = (ROOT/name).read_bytes()
    digest = hashlib.sha256(b).hexdigest()
    R['bindings'][name] = digest
    if h is not None:
        need(digest == h, 'input hash '+name)
    return json.loads(b)


def shifted(p, t):
    # Horner substitution, without the producer's binomial formula.
    r = []
    for c in reversed(p):
        z = [F(0)]*(len(r)+1)
        for i, a in enumerate(r):
            z[i] += a*t
            z[i+1] += a
            size(z)
        z[0] += F(c)
        size(z[0])
        r = z
    return r


def times_alpha(a):
    lead = a[3]
    return operation([(a[i-1] if i else F(0))-lead*G[i] for i in range(4)])


def multiply(a, b):
    # Companion Horner, not convolution and reduction.
    r = [F(0)]*4
    for t in reversed(b):
        r = times_alpha(r)
        r = operation([x+t*y for x, y in zip(r, a)])
    return r


def determinant(a):
    cols, v = [], a
    for _ in range(4):
        cols.append(v)
        v = times_alpha(v)
    M = [[cols[j][i] for j in range(4)] for i in range(4)]
    result = F(1)
    for k in range(4):
        j = next((j for j in range(k, 4) if M[j][k]), None)
        need(j is not None, 'nonzero norm determinant')
        if j != k:
            M[j], M[k] = M[k], M[j]
            result = -result
        pivot = M[k][k]
        result *= pivot
        size(result)
        for i in range(k+1, 4):
            t = M[i][k]/pivot
            size(t)
            for j in range(k+1, 4):
                M[i][j] -= t*M[k][j]
                size(M[i][j])
            M[i][k] = 0
    return result


def valuation(x):
    x = F(x)
    need(bool(x), 'valuation nonzero')
    n, d, v = abs(x.numerator), x.denominator, 0
    while n % 11 == 0:
        n //= 11
        v += 1
    while d % 11 == 0:
        d //= 11
        v -= 1
    return v


def residue(x):
    x = F(x)
    need(x.denominator % 11 != 0, 'residue defined')
    # Fermat inversion, unlike producer modular inverse.
    return x.numerator % 11 * pow(x.denominator % 11, 9, 11) % 11


def division_u(a):
    c = a[0]/49500
    return operation([a[1]+29700*c, a[2]+660*c, a[3]-44*c, -c])


def multiply_u(a):
    return operation([-49500*a[3], a[0]+29700*a[3],
                      a[1]+660*a[3], a[2]-44*a[3]])


def qr(t):
    need(0 < t < 11, 'nonzero unit residue')
    return int(pow(t, 5, 11) != 1)


def check_pair(saved, alpha, rational):
    a = shifted(alpha, -5)
    f, q = saved['quartic'], saved['rational']
    need(a == list(map(F, f['u_coefficients'])), 'transported exact element')
    # Integral scaling followed by repeated division computes valuation
    # without the producer's minimum-of-four weighted valuations algorithm.
    d = min(valuation(x) for x in a if x)
    integral = operation([x/F(11)**d for x in a])
    j, quotients = 0, [integral]
    while residue(integral[0]) == 0:
        integral = division_u(integral)
        need(all(x == 0 or valuation(x) >= 0 for x in integral), 'each quotient integral')
        quotients.append(integral)
        j += 1
        need(j <= 128, 'division cap')
    n = 4*d+j
    t = residue(integral[0]) * pow(10, d, 11) % 11
    R['bounds']['max_absolute_valuation'] = max(abs(n), R['bounds']['max_absolute_valuation'])
    need(abs(n) <= 128, 'field valuation cap')
    normal = a
    for _ in range(abs(n)):
        normal = division_u(normal) if n >= 0 else multiply_u(normal)
    need(all(x == 0 or valuation(x) >= 0 for x in normal), 'exact normalized integral')
    need(residue(normal[0]) == t, 'two normalization methods')
    termvals = [None if not x else 4*valuation(x)+i for i, x in enumerate(a)]
    need(f == dict(u_coefficients=f['u_coefficients'], term_valuations=termvals,
                   minimum_index=termvals.index(n), valuation=n,
                   normalized=f['normalized'], residue=t, bits=[n % 2, qr(t)]), 'full field class record')
    need(normal == list(map(F, f['normalized'])), 'exact normalization vector')
    need(F(q['value']) == rational, 'rational pair coordinate')
    v = valuation(rational)
    R['bounds']['max_absolute_valuation'] = max(abs(v), R['bounds']['max_absolute_valuation'])
    need(abs(v) <= 128, 'rational valuation cap')
    unit = rational/F(11)**v
    size(unit)
    r = residue(unit)
    need(q['valuation'] == v and F(q['unit']) == unit and q['residue'] == r and
         q['bits'] == [v % 2, qr(r)], 'full rational class record')
    bits = [v % 2, qr(r), n % 2, qr(t)]
    mask = int(''.join(map(str, reversed(bits))), 2)
    need(saved['bits'] == bits and saved['mask'] == mask, 'full local mask')
    return dict(mask=mask, valuation=n, residue=t, integral_scaling=d,
                division_chain=quotients)


def rank(rows):
    piv = {}
    for x in rows:
        while x:
            k = (x & -x).bit_length()-1
            if k not in piv:
                piv[k] = x
                break
            x ^= piv[k]
    return len(piv)


def combination(rows, c):
    x = 0
    for i, row in enumerate(rows):
        if c >> i & 1:
            x ^= row
    return x


def verify_elimination(e, rows):
    need(len(rows) <= 39 and all(x.bit_length() <= 39 for x in rows), 'matrix cap')
    need(e['rank'] == rank(rows), 'independent rank')
    need(len(e['trace']) == len(rows), 'complete elimination trace')
    seen = {}
    for i, t in enumerate(e['trace']):
        x, c = rows[i], 1 << i
        need(t['input'] == x, 'trace input')
        for k in t['additions']:
            need(k in seen and x.bit_length()-1 == k, 'valid pivot addition')
            y, a = seen[k]
            x ^= y
            c ^= a
        need((x, c) == (t['reduced'], t['coefficients']), 'trace result')
        need(combination(rows, c) == x and c < 1 << (i+1), 'coefficient identity')
        if x:
            seen[x.bit_length()-1] = [x, c]
    need({str(k): v for k, v in seen.items()} == e['pivots'], 'complete pivot records')
    K = e['kernel']
    need(len(K) == len(rows)-rank(rows) == rank(K), 'complete independent kernel basis')
    need(all(0 < c < 1 << len(rows) and combination(rows, c) == 0 for c in K), 'all kernel identities')


def main():
    d = load('eleven-adic-filter-certificate.json')
    need(d['completed'] and not d['failures'], 'producer completed')
    sources = {name: load(name, h) for name, h in d['bindings'].items()}
    real = sources['real-kummer-certificate.json']
    need(real['completed'] and not real['failures'] and
         sources['real-kummer-audit.json']['bindings']['real-kummer-certificate.json'] ==
         d['bindings']['real-kummer-certificate.json'], 'audited original real data')
    need(real['g'] == G+[1], 'actual field')
    need(shifted(G+[1], -5) == list(map(F, d['field']['shifted'])) ==
         [49500, -29700, -660, 44, 1], 'shift polynomial')
    need(all(int(x) % 11 == 0 for x in d['field']['shifted'][:4]) and 49500 % 121 != 0,
         'Eisenstein and root uniformizer')
    need((-4500) % 11 == pow((-4500) % 11, 9, 11) == 10, 'rho residue')
    model = sources['odd-model-support-certificate.json']
    base = sources['quartic-class-certificate.json']
    size(real['G'])
    size([[F(x) for x in row] for row in real['basis']])
    need(d['field']['prime'] == base['generators'][1] and
         d['field']['prime']['factor'] == [5, 1], 'prime identification')
    need(real['G'] == model['model']['G'], 'same model')
    H = model['model']['H']
    size(H)
    p = [0]*6
    for i, c in enumerate(H):
        p[i] -= 9075*c
        p[i+1] += c
        size(p)
    need(p == real['G'], 'all factor-product coefficients')
    eta = list(map(F, model['field']['eta_in_alpha']))
    size(eta)
    need(multiply(eta, [-50, 1, 0, 0]) == [-907500, 0, 0, 0], 'rational eta transport')
    h = [F(0)]*4
    for c in reversed(H):
        h = multiply(h, eta)
        h[0] += c
        size(h)
    need(h == [0]*4, 'H root in actual irreducible local field')
    b = [-x for x in eta]
    b[0] += 9075
    h_r = 0
    for c in reversed(H):
        h_r = h_r*9075+c
        size(h_r)
    need(h_r == d['branch']['H_at_root'] == determinant(b) == 73990352390625 != 0,
         'branch norm and distinct factors')
    need(H == d['branch']['H'] and shifted(eta, -5) == list(map(F, d['branch']['eta_u'])),
         'all branch polynomial coordinates')
    bc = check_pair(d['branch']['pair'], b, F(h_r))
    need(bc['mask'] == 5 and d['local_image_span'] == [0, 5] and
         d['local_factor_count'] == 2 and d['branch']['actual_dimension'] ==
         d['branch']['required_dimension'] == 1 and d['branch']['infinity_mask'] == 0,
         'complete branch-image gate')
    R['branch'] = bc
    need(len(d['witnesses']) == len(real['witnesses']) == 39, 'exact input domain')
    rows, alpha, rational, masks, real_masks = [], [], [], [], []
    for r, w in zip(d['witnesses'], real['witnesses']):
        need(r['source'] == w and r['id'] == w['id'], 'entire witness record')
        a = list(map(F, w['power_coefficients']))
        size(a)
        n = determinant(a)
        q = F(w['inverse_norm'])
        size(q)
        need(n == F(w['signed_norm']) == F(r['signed_norm']) and n*q == 1, 'all signed norms')
        need(a == [sum(F(real['basis'][i][j])*w['coefficients'][j] for j in range(4))
                   for i in range(4)], 'all basis coordinates')
        checked = check_pair(r['pair'], a, q)
        bits = w['sign_bits']
        need(sum(bits) % 2 == 0 and w['mask'] == sum(x << i for i, x in enumerate(bits)), 'real sign record')
        row = bits[0]+2*(bits[1]^bits[2])
        need(row == r['real_quotient'], 'real quotient')
        need(r['pair']['bits'][:2] == [r['pair']['bits'][2], 0], 'local norm bits')
        rows.append(row)
        alpha.append(a)
        rational.append(q)
        masks.append(checked['mask'])
        real_masks.append(w['mask'])
        R['verified'].append(dict(id=w['id'], signed_norm=n, **checked))
    need(set(real['local_rows']) == {0, 24, 30}, 'actual W')
    verify_elimination(d['real_kernel'], rows)
    need(d['real_kernel']['rank'] == 2 and len(d['real_kernel']['kernel']) == 37, 'real kernel threshold')
    need([p['coefficients'] for p in d['products']] == d['real_kernel']['kernel'], 'complete product domain')
    R['products'] = []
    for p in d['products']:
        c = p['coefficients']
        a, q, ids = [F(1), F(0), F(0), F(0)], F(1), []
        for i in range(39):
            if c >> i & 1:
                a = multiply(a, alpha[i])
                q *= rational[i]
                size(q)
                ids.append(real['witnesses'][i]['id'])
        need(ids == p['ids'], 'actual coefficient support')
        n = determinant(a)
        need(n == F(p['signed_norm']) and n*q == 1, 'product signed norm')
        checked = check_pair(p['pair'], a, q)
        need(checked['mask'] == combination(masks, c), 'all product localizations multiplicative')
        need(p['real_mask'] == combination(real_masks, c) and p['real_mask'] in (0, 6, 24, 30),
             'all products real compatible')
        quotient = int(checked['mask'] not in (0, 5))
        need(quotient == p['local_quotient'] == p['pair']['quartic']['bits'][1], 'exact quotient')
        R['products'].append(dict(coefficients=c, **checked))
    verify_elimination(d['quotient_elimination'], [p['local_quotient'] for p in d['products']])
    need(d['quotient_elimination']['rank'] == 1, 'one extra codimension')
    chosen = next(p for p in d['products'] if p['ids'] == ['rational-2'])
    need(chosen == d['obstruction'] and chosen['real_mask'] == 0 and chosen['pair']['mask'] == 8,
         'explicit positive witness outside complete local image')
    expected = dict(required_local_dimension=1, actual_local_dimension=1, global_columns=39,
                    real_coefficient_rank=2, real_kernel_dimension=37, quotient_rank=1,
                    filtered_dimension_constant=8, rank_bound_constant=7, c_upper_bound=2,
                    unconditional_rank_upper_bound=9, sufficient_rank_upper_bound=1, shortfall=8)
    need(d['result'] == expected, 'all reported bounds')
    need(all(c['passed'] for c in d['checks']), 'no producer failures hidden')
    R['result'] = expected
    R['bounds'].update(global_columns=39, field_coordinates=4, coefficient_kernel_vectors=37,
                       max_matrix_rows=39, max_matrix_columns=39)
    R['completed'] = True


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        R['failures'].append(str(exc))
        R['traceback'] = traceback.format_exc()
    OUT.write_text(json.dumps(R, indent=2, default=lambda x: x.numerator if x.denominator == 1 else str(x))+'\n')
    print(json.dumps({k: R.get(k) for k in ('completed', 'checks', 'result', 'bounds', 'failures')} |
                     dict(certificate=str(OUT))))
    if not R['completed']:
        raise SystemExit(1)
