#!/usr/bin/env python3
"""Independent fixed-point/rational audit of C999j; no trial adjustment.

Integer outward intervals use 110 decimal places, with no imported interval
implementation. log(3)/2 uses its positive atanh series and geometric tail;
pi uses Machin's identity and alternating tails; sqrt uses integer isqrt.
Every contributing matrix product is accumulated exactly as a rational.
Analytic/IEEE754 entry contracts and the unreplayed c_star remain hypotheses.
"""
import hashlib
import json
from fractions import Fraction as F
from math import isqrt
from pathlib import Path

import numpy as np

BASE = Path(__file__).resolve().parent
SCALE = 10**110


class Q:
    def __init__(self, x=0):
        r = F(x)*SCALE
        self.lo, self.hi = r.__floor__(), r.__ceil__()

    @staticmethod
    def ends(lo, hi):
        assert lo <= hi
        r = object.__new__(Q)
        r.lo, r.hi = lo, hi
        return r

    @staticmethod
    def cast(x):
        return x if isinstance(x, Q) else Q(x)

    def __add__(self, x):
        x = Q.cast(x)
        return Q.ends(self.lo+x.lo, self.hi+x.hi)

    __radd__ = __add__

    def __neg__(self):
        return Q.ends(-self.hi, -self.lo)

    def __sub__(self, x):
        return self+-Q.cast(x)

    def __rsub__(self, x):
        return Q.cast(x)+-self

    def __mul__(self, x):
        x = Q.cast(x)
        products = [a*b for a in (self.lo, self.hi) for b in (x.lo, x.hi)]
        return Q.ends(min(products)//SCALE, -(-max(products)//SCALE))

    __rmul__ = __mul__

    def __truediv__(self, x):
        x = Q.cast(x)
        assert not x.lo <= 0 <= x.hi
        quotients = [F(a*SCALE, b) for a in (self.lo, self.hi)
                     for b in (x.lo, x.hi)]
        return Q.ends(min(quotients).__floor__(), max(quotients).__ceil__())

    def __rtruediv__(self, x):
        return Q.cast(x)/self

    def __pow__(self, n):
        assert n >= 0
        out = Q(1)
        for _ in range(n):
            out *= self
        return out

    def sqrt(self):
        assert self.lo >= 0
        lo, hi = isqrt(self.lo*SCALE), isqrt(self.hi*SCALE)
        return Q.ends(lo, hi+(hi*hi < self.hi*SCALE))

    def ab(self):
        return Q.ends(max(abs(self.lo), abs(self.hi)),
                      max(abs(self.lo), abs(self.hi)))

    def json(self):
        return dict(lo=str(F(self.lo, SCALE)), hi=str(F(self.hi, SCALE)))


def l1(x):
    return sum((z.ab() for z in x), Q())


def atan(q):
    x = Q(1)/q
    out = sum((((-1)**j)*x**(2*j+1)/(2*j+1) for j in range(100)), Q())
    error = (x**201/201).hi
    return out+Q.ends(-error, error)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    old_path = BASE/'fixed-trial-residual-550-80.json'
    old = json.loads(old_path.read_text())
    replay = json.loads((BASE/'fixed-trial-residual-550-100.json').read_text())
    direction = json.loads((BASE/'response-prefix-direction-546.json').read_text())
    preserved = [old_path.name, 'fixed-trial-residual-550.py',
                 'response-prefix-direction-546.json']+[r['path'] for r in old['input_hashes']]
    hashes = {n: digest(BASE/n) for n in preserved}
    failures, checks = [], []

    def check(ok, label):
        checks.append(dict(label=label, passed=bool(ok)))
        if not ok:
            failures.append(label)

    def enclosed(value, saved, label):
        check(F(saved['lo']) <= F(value.lo, SCALE) <= F(value.hi, SCALE)
              <= F(saved['hi']), label)

    def upper(value, saved, label):
        check(0 <= value.lo <= value.hi and F(value.hi, SCALE) <= F(saved['hi']), label)

    check(not old['failures'] and not replay['failures'], 'original/replay failures empty')
    check(old['source_script_sha256'] == hashes['fixed-trial-residual-550.py']
          == replay['source_script_sha256'], 'generator hash')
    check(hashes['response-prefix-direction-546.json'] == old['direction_sha256']
          == replay['direction_sha256']
          == 'f39d45d9754d0415f5180e2cb5803d8152bfbaba3eb34130b4bf4b91b81da013', 'direction pin')
    for row in old['input_hashes']:
        check(row['actual'] == row['expected'] == hashes[row['path']], 'input pin '+row['path'])
    check(direction['modes'] == 512 and direction['denominator'] == 2**40,
          'exact fixed size and denominator')

    half = Q(F(1, 2))
    # ell=atanh(1/2); positive omitted denominators are all >=401.
    ell = sum((half**(2*j+1)/(2*j+1) for j in range(200)), Q())
    ell += Q.ends(0, (half**401/(401*(1-half*half))).hi)
    pi = 16*atan(5)-4*atan(239)
    rt2 = Q(2).sqrt()
    enclosed(ell, old['constants']['ell'], 'independent log3/2')
    enclosed(pi, old['constants']['pi'], 'independent Machin pi')
    k = [n*pi/ell for n in range(512)]
    k2 = [z*z for z in k]
    nu = [(Q(1 if n == 0 else 2)/ell).sqrt() for n in range(512)]

    def neutral(key):
        integers = direction[key]
        check(len(integers) == 510 and all(type(v) is int for v in integers), key)
        u = [Q(), Q()]+[Q(F(v, 2**40)) for v in integers]
        for n in range(2, 512):
            p = n % 2
            ratio = (Q('.25')+k2[p])/(Q('.25')+k2[n])
            if p == 0:
                ratio *= rt2
            u[p] -= ratio*u[n]
        return u

    f, g = [neutral(key) for key in ['f_free_numerators', 'g_free_numerators']]
    h = [((-1)**n)*v for n, v in enumerate(f)]
    w = [Q() for _ in range(512)]
    w[2], w[0] = Q(1), -rt2*Q('.25')/(Q('.25')+k2[2])
    coefficients = dict(f=f, g=g, h=h, w=w)
    for name, values in coefficients.items():
        check(len(old['coefficients'][name]) == 512, 'coefficient count '+name)
        for n, v in enumerate(values):
            enclosed(v, old['coefficients'][name][n], 'coefficient '+name+':'+str(n))
    check(all(g[n].lo == g[n].hi == 0 for n in range(1, 512, 2)), 'exact even middle')

    rho = [rt2/(6*(Q('64.25')**2+z/4)) for z in k2]
    c = Q('131072.5')
    t = [1/(c*c)+2*z*(1/(6*c**3)+1/c**4) for z in k2]
    elementary = Q('1e-7')*l1(g)*l1(w)
    head_error, allowance_records = elementary, []
    expected_rows = {(i, j) for i in [0, 2] for j in range(0, 512, 2)
                     if g[j].ab().hi != 0}
    saved_rows = {(r['row'], r['column']): r for r in old['analytic_entry_allowances']}
    check(len(saved_rows) == len(old['analytic_entry_allowances'])
          and saved_rows.keys() == expected_rows, 'all contributing allowance entries exactly once')
    for i, j in sorted(expected_rows):
        if i == j:
            error = rho[i]+2*nu[i]*nu[i]*t[i]
        else:
            gap = k2[max(i, j)]-k2[min(i, j)]
            check(gap.lo > 0, 'strict squared-frequency gap '+str((i, j)))
            error = nu[i]*nu[j]*(k[i]*rho[i]+k[j]*rho[j])/gap
        contribution = error*w[i].ab()*g[j].ab()
        head_error += contribution
        row = saved_rows[i, j]
        enclosed(error, row['analytic_error'], 'analytic entry '+str((i, j)))
        upper(contribution, row['weighted_allowance'], 'weighted entry '+str((i, j)))
        allowance_records.append(dict(row=i, column=j, analytic_error=error.json(),
                                      weighted_allowance=contribution.json()))
    upper(head_error, old['pairings']['head_error'], 'complete head allowance')
    t1error = Q('2.1e-7')*l1(f)*l1(w)
    t2error = Q('2.1e-7')*l1(w)*l1(h)
    upper(t1error, old['pairings']['Tf_w_error'], 'full Tf,w allowance')
    upper(t2error, old['pairings']['Tw_h_error'], 'full Tw,h allowance')

    with np.load(BASE/'complete-covariance-532.npz') as archive:
        head = archive['m0']
        seven = archive['mc']+archive['mg']
        # Charge the addition allowance on every used T entry independently.
        used = {(i, j) for i in [0, 2] for j in range(512)}
        used |= {(i, j) for i in range(512) for j in [0, 2]}
        add_error = max(abs(F(float(seven[i, j]))-F(float(archive['mc'][i, j]))
                            -F(float(archive['mg'][i, j]))) for i, j in used)
    check(add_error < F('1e-8'), 'stored T addition allowance')
    products = []

    def product(label, matrix, xn, yn, saved):
        xv, yv = coefficients[xn], coefficients[yn]
        x = [(v.lo+v.hi)//2 for v in xv]
        y = [(v.lo+v.hi)//2 for v in yv]
        ex = F(sum(max(abs(v.lo-p), abs(v.hi-p)) for v, p in zip(xv, x)), SCALE)
        ey = F(sum(max(abs(v.lo-p), abs(v.hi-p)) for v, p in zip(yv, y)), SCALE)
        ii = [i for i, v in enumerate(yv) if v.ab().hi]
        jj = [j for j, v in enumerate(xv) if v.ab().hi]
        entries = {(i, j): float(matrix[i, j]).as_integer_ratio() for i in ii for j in jj}
        den = max(d for n, d in entries.values())
        check(all(den % d == 0 for n, d in entries.values()), 'dyadic common denominator '+label)
        integer = sum(y[i]*x[j]*n*(den//d) for (i, j), (n, d) in entries.items())
        center = F(integer, den*SCALE*SCALE)
        maximum = max(abs(F(n, d)) for n, d in entries.values())
        error = maximum*(F(sum(map(abs, x)), SCALE)*ey
                         +F(sum(map(abs, y)), SCALE)*ex+ex*ey)
        lo, hi = center-error, center+error
        check(F(saved['lo']) <= lo <= hi <= F(saved['hi']), 'exact rational matrix product '+label)
        products.append(dict(label=label, integer_sum=str(integer), matrix_denominator=str(den),
            coefficient_scale=str(SCALE), coefficient_uncertainty=str(error),
            lo=str(lo), hi=str(hi), original_enclosure=saved, contributing_entries=len(entries)))
        return lo, hi

    a = product('a(g,w) center', head, 'g', 'w', old['pairings']['head_center'])
    b = product('Tf,w center', seven, 'f', 'w', old['pairings']['Tf_w_center'])
    d = product('Tw,h center', seven, 'w', 'h', old['pairings']['Tw_h_center'])
    error = F(head_error.hi+t1error.hi+t2error.hi, SCALE)
    pair_lo, pair_hi = b[0]+d[0]-a[1]-error, b[1]+d[1]-a[0]+error
    norm = 1+w[0]*w[0]
    enclosed(norm, old['summary']['norm_w_squared'], 'neutral test norm squared')
    check(F(old['summary']['residual_pairing']['lo']) <= pair_lo <= pair_hi
          <= F(old['summary']['residual_pairing']['hi']), 'full independent residual pairing')
    check(F('-.072312080263') < pair_lo <= pair_hi < F('-.0721574607336'),
          'canonical strict pairing bounds')
    lower_norm = pair_hi**2/F(norm.hi, SCALE)
    lower_majorant = lower_norm/F('8.9e-18')
    check(pair_hi < 0 and lower_norm > F('.0052066612648'), 'Cauchy-Schwarz lower screen')
    check(lower_majorant > F('5.85018e14') > F('.094207'), 'majorant rejects actual upper energy')
    required_squared = F('8.9e-18')*F('.094207')*F(norm.hi, SCALE)
    check(required_squared < F('9.156683e-10')**2 < pair_hi**2,
          'required pairing threshold without rounded square root')
    for name in preserved:
        check(hashes[name] == digest(BASE/name), 'preserved '+name)
    certificate = dict(scope='C999j fixed546 n=2 full-residual audit only',
        source_script_sha256=digest(Path(__file__)), preserved_hashes=hashes,
        constants=dict(pi=pi.json(), ell=ell.json()),
        coefficients={n: [v.json() for v in vv] for n, vv in coefficients.items()},
        analytic_entry_allowances=allowance_records,
        complete_allowances=dict(head=head_error.json(), Tf_w=t1error.json(), Tw_h=t2error.json()),
        exact_rational_products=products, stored_T_addition_error=str(add_error),
        summary=dict(residual_pairing=dict(lo=str(pair_lo), hi=str(pair_hi)),
            norm_w_squared=norm.json(), residual_norm_squared_lower=str(lower_norm),
            residual_majorant_lower=str(lower_majorant), required_pairing_squared=str(required_squared),
            actual_trial_energy_upper='.094207', rejects_fixed_majorant=lower_majorant > F('.094207')),
        checks=checks, failures=failures,
        qualifications=['Analytic/IEEE754 entry contracts inherited; no source floor replay.',
                        'Particular strong trial only; not a whole-core audit or minimized sign.'])
    path = BASE/'fixed-trial-residual-audit-552.json'
    path.write_text(json.dumps(certificate, indent=2)+'\n')
    print('Checks:', len(checks), '; allowance entries:', len(allowance_records),
          '; exact matrix terms:', sum(r['contributing_entries'] for r in products))
    print('Residual pairing in (-.072312080263,-.0721574607336); required |pair| < 9.156683e-10')
    print('Residual norm squared > .0052066612648; majorant > 5.85018e14; rejection threshold .094207')
    print('Failures:', failures)
    print('Certificate:', path.relative_to(BASE.parent.parent))
    assert not failures


if __name__ == '__main__':
    main()
