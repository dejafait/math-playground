"""Exact-rational checks of ALL saved contour boxes and finite norm data.

This is not an independent audit of the theta evaluator or analytic tails.
It checks complete saved coverage, crossing counts and finite arithmetic.
"""
import json
from decimal import Decimal as D
from fractions import Fraction as F
from pathlib import Path

BASE = Path(__file__).resolve().parent
d = json.loads((BASE/'fixed-pair-certificate-431.json').read_text())
checks = []


def pair(x):
    a, b = map(F, x)
    assert a <= b
    return a, b


def contains(x, num, den=1, square=False):
    assert den > 0
    a, b = pair(x)
    if square:
        assert a >= 0
        a, b = a*a, b*b
    assert a.numerator*den <= num*a.denominator
    assert num*b.denominator <= b.numerator*den


assert not d['failures']
ev = d['evaluation']
assert len(ev['quadrature_cells']) == 128
for k, cell in enumerate(ev['quadrature_cells']):
    assert cell['cell'] == k
    contains(cell['center'], 2*k+1, 128)
    assert len(cell['A_Taylor_coefficients']) == 25
    assert len(cell['moment_integral_error_upper']) == 96
    assert all(F(x) > 0 for x in cell['moment_integral_error_upper'])
checks.append('all 128 quadrature-cell records complete; no independent exp/quadrature replay')

for name in ['inner_contour', 'outer_contour']:
    cc = d[name]
    records = cc['segments']
    count, minimum = 0, None
    for quadrant in range(4):
        parts = [x for x in records if x['quadrant'] == quadrant]
        last = F(0)
        for rec in parts:
            left, right = map(F, rec['t'])
            assert left == last and left < right
            last = right
        assert last == 1
    for k, rec in enumerate(records):
        rr, ii = map(pair, rec['G_box'])
        lower = max(F(0), rr[0], -rr[1], ii[0], -ii[1])
        assert 0 < F(rec['G_lower']) <= lower
        minimum = lower if minimum is None else min(lower, minimum)
        for point in rec['point_enclosures']:
            for bounds, whole in zip(point, [rr, ii]):
                a, b = pair(bounds)
                assert whole[0] <= a <= b <= whole[1]
        assert rec['vertices'][1] == records[(k+1) % len(records)]['vertices'][0]
        for vertex in rec['vertices']:
            assert rr[0] <= F(vertex[0]) <= rr[1]
            assert ii[0] <= F(vertex[1]) <= ii[1]
        (x, y), (xx, yy) = [[F(v) for v in p] for p in rec['vertices']]
        cross = x*yy-y*xx
        assert cross != 0 or not (y <= 0 < yy or yy <= 0 < y)
        count += int(y <= 0 < yy and cross > 0)-int(yy <= 0 < y and cross < 0)
    assert count == cc['count_with_multiplicity'] == 1
    assert 0 < F(cc['G_boundary_lower']) <= minimum
    checks.append(f'{name}: all {len(records)} segments, endpoint inclusions, nonzero boxes and exact winding=1')

z = d['zero']
assert F(-800) < F(z['root_w'][0]) < F(z['root_w'][1]) < F(-799)
ends = list(map(pair, z['endpoint_G']))
assert ends[0][1] < 0 < ends[1][0] or ends[1][1] < 0 < ends[0][0]

n = d['norm']
N, L = n['N'], n['L']
assert N == 192 and L == 1024 and N < L-1
assert len(n['samples']) == L
for j, sample in enumerate(n['samples']):
    assert sample['j'] == j
    rr, ii = map(pair, sample['G'])
    assert rr[0] > 0 or rr[1] < 0 or ii[0] > 0 or ii[1] < 0
assert len(n['beta_hat']) == len(n['epsilon']) == len(n['beta_enclosures']) == N
for bh, err, enc in zip(n['beta_hat'], n['epsilon'], n['beta_enclosures']):
    lo, hi = pair(enc)
    assert lo <= F(bh) <= hi
    assert F(err) >= max(F(bh)-lo, hi-F(bh))
ah, dh = F(n['alpha_hat']), F(n['residue_hat'])
for hat, err, enc in [(ah, F(n['alpha_error']), z['alpha']),
                       (dh, F(n['residue_error']), z['residue'])]:
    lo, hi = pair(enc)
    assert err >= max(hat-lo, hi-hat)
sigma, a, rho = F(5, 4), F(4, 5), F(9, 10)
assert max(map(abs, pair(z['alpha']))) < a < rho < 1 < sigma
msig = F(d['outer_contour']['G_boundary_lower'])/(sigma+a)
assert 0 < pair(n['m_sigma'])[0] <= msig
mb = (1+a/sigma)/pair(n['m_sigma'])[0]
assert pair(n['M_b'])[1] >= mb
hsq = sum(j*F(bh)**2 for j, bh in enumerate(n['beta_hat'], 1))
assert pair(n['h_b'])[1]**2 >= hsq
q = sigma**-2
tn = q**(N+1)*((N+1)-N*q)/(1-q)**2
contains(n['T_N'], tn.numerator, tn.denominator)
assert pair(n['delta_b'])[1]**2 >= (
    sum(j*F(e)**2 for j, e in enumerate(n['epsilon'], 1))
    +pair(n['M_b'])[1]**2*tn)
hb = abs(dh)/(rho-a)*rho/(1-rho*rho)
db = (F(n['residue_error'])/(rho-a)
      +abs(dh)*F(n['alpha_error'])/(rho-a)**2)*rho/(1-rho*rho)
assert pair(n['h_B'])[1] >= hb and pair(n['delta_B'])[1] >= db
err = (pair(n['delta_b'])[1]*pair(n['h_B'])[1]
       +pair(n['h_b'])[1]*pair(n['delta_B'])[1]
       +pair(n['delta_b'])[1]*pair(n['delta_B'])[1])
assert pair(n['full_product_error'])[1] >= err

# Integer Horner arithmetic: all hatted entries are exact finite decimals.
# A common power-of-ten denominator avoids repeated huge rational gcds.
def scale_of(x):
    return max(0, -D(x).as_tuple().exponent)


def scaled(x, scale):
    tt = D(x).as_tuple()
    digits = int(''.join(map(str, tt.digits)))
    return (-1 if tt.sign else 1)*digits*10**(scale+tt.exponent)


sa = scale_of(n['alpha_hat'])
sb = max(map(scale_of, n['beta_hat']))
A, T, B = scaled(n['alpha_hat'], sa), 10**sa, 10**sb
bet = [scaled(b, sb) for b in n['beta_hat']]
gn, gd = 0, B*B*T**(2*(N-3))
for i in range(3, N+1):
    acc, denpower = bet[-1], 1
    for j in range(N-1, i-1, -1):
        denpower *= T
        acc = acc*A+bet[j-1]*denpower
    contains(n['U_rows'][i-3], acc, B*T**(N-i))
    gn += acc*acc*T**(2*(i-3))
contains(n['Gram_U'], gn, gd)
yn, yd = A**4, T*T*(T*T-A*A)
contains(n['Gram_Y'], yn, yd)
kn, kd = gn*yn*dh.numerator**2, gd*yd*dh.denominator**2
contains(n['finite_norm'], kn, kd, square=True)
lo, hi = pair(n['original_norm'])
kl, ku = pair(n['finite_norm'])
assert lo <= kl-pair(n['full_product_error'])[1]
assert hi >= ku+pair(n['full_product_error'])[1]
assert 0 < lo < hi < 1
checks.append('all 1024 DFT sample denominators exclude zero; all 192 coefficient error records included')
checks.append('192-mode finite Gram/norm arithmetic checked with exact integers/rationals, including every U row')
checks.append('complete L777 upper error and reverse-triangle lower error verified rationally')
out = {'status': 'PASS', 'checks': checks, 'actual_norm': n['original_norm'],
       'required_upper': '1', 'failures': [],
       'limitations': 'Does not independently audit theta jets, analytic truncation, Cauchy contour enclosure or Fourier alias theorem; separate critical review required',
       'input': 'scripts/actual-fredholm/fixed-pair-certificate-431.json'}
path = BASE/'saved-data-check-431.json'
path.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({**out, 'certificate': str(path)}, indent=2))
