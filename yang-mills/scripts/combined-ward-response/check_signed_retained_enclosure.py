"""Enclose L035's signed fixed-table cutoff-112 tensor.

Exact Gaussian weight error; integer root/heat/weak enclosures; binary64
midpoint-radius tensors with an explicit conservative dot error model.
No machine exp, regenerated Fourier table or sampled inverse-weight test.
"""
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt
from pathlib import Path

import numpy as np

import check_exact_fourier_quadrature as ar
from check_continuum_pure_sectors import operators
from check_continuum_tensor import product_terms

S, I = ar.S, ar.I
ONE, ZERO = I(S), I(0)
ROOT = Path(__file__).parent
OUTPUT = ROOT/'signed-retained-enclosure-certificate.json'
M, DEGREE = 112, 12
G = np.nextafter(1e-12, np.inf)
TINY = 1e-290


def updiv(a, b):
    return -((-a)//b)


def rat(q):
    return I.rational(q)


def record(z):
    return dict(lo=str(z.lo), hi=str(z.hi))


def rational_record(q):
    return dict(num=str(q.numerator), den=str(q.denominator))


def display(q, places=24):
    n = updiv(q.numerator*10**places, q.denominator)
    return f'{n//10**places}.{n%10**places:0{places}d}'


def upward(q):
    z = float(q)
    while F(z) < q:
        z = np.nextafter(z, np.inf)
    return z


def midpoint_radius(z):
    mid = float(F(z.lo+z.hi, 2*S))
    rad = upward(max(abs(F(mid)-F(z.lo, S)), abs(F(mid)-F(z.hi, S))))
    assert F(mid)-F(rad) <= F(z.lo, S) and F(mid)+F(rad) >= F(z.hi, S)
    return mid, rad


def ua(a, b):
    return np.nextafter(a+b, np.inf)


def um(a, b):
    return np.nextafter(a*b, np.inf)


def udot(a, b):
    assert np.all(a >= 0) and np.all(b >= 0)
    assert F(float(1-G)) < 1-F(554, 2**53-554)
    z = np.nextafter((a@b)/(1-G), np.inf)
    return ua(z, TINY)


def add(a, b):
    ac, ae = a; bc, be = b
    c = ac+bc
    e = ua(ua(ae, be), ua(um(1e-15, np.abs(c)), TINY))
    return c, e


def multiply(a, b):
    ac, ae = a; bc, be = b
    c = ac*bc
    e = ua(ua(um(np.abs(ac), be), um(ae, np.abs(bc))), um(ae, be))
    e = ua(e, ua(um(1e-15, np.abs(c)), TINY))
    return c, e


def dot(a, b):
    ac, ae = a; bc, be = b
    inner = ac.shape[-1]
    assert inner <= 276
    # 2n+2 IEEE elementary operations, arbitrary order or FMA, no overflow.
    gamma = F(2*inner+2, 2**53-(2*inner+2))
    assert F(G) > gamma
    c = ac@bc
    e = ua(ua(udot(np.abs(ac), be), udot(ae, np.abs(bc))), udot(ae, be))
    e = ua(e, ua(um(G, udot(np.abs(ac), np.abs(bc))), TINY))
    assert np.all(np.isfinite(c)) and np.all(np.isfinite(e))
    return c, e


def power(z, n):
    result = ONE
    for _ in range(n):
        result = result*z
    return result


def legendre(z):
    prev, cur = ONE, z
    for j in range(2, DEGREE+1):
        prev, cur = cur, (rat(2*j-1)*z*cur-rat(j-1)*prev)/rat(j)
    return cur, prev


def sign(t):
    p, _ = legendre(I(t))
    assert p.lo > 0 or p.hi < 0
    return 1 if p.lo > 0 else -1


def gaussian_rule():
    proposals, _ = np.polynomial.legendre.leggauss(DEGREE)
    rows, roots, weights = [], [], []
    for x in proposals:
        c = rat(F(float(x))); radius = rat(F(1, 10**10)).hi
        lo, hi = c.lo-radius, c.hi+radius
        sl, sh = sign(lo), sign(hi)
        assert -S < lo < hi < S and sl != sh
        while hi-lo > S//10**50:
            mid = (lo+hi)//2
            sm = sign(mid)
            if sm == sl:
                lo, sl = mid, sm
            else:
                hi, sh = mid, sm
        z = I(lo, hi)
        p, pm = legendre(z)
        derivative = rat(DEGREE)*(pm-z*p)/(ONE-z*z)
        weight = rat(2)/((ONE-z*z)*derivative*derivative)
        assert weight.lo > 0 and (not roots or roots[-1].hi < z.lo)
        roots.append(z); weights.append(weight)
        rows.append(dict(root=record(z), weight=record(weight), sign_lo=sign(lo), sign_hi=sign(hi)))
    panels = [(F(0), F(1, 2**14))]+[(F(2)**j, F(2)**(j+1)) for j in range(-14, 8)]
    nodes, dr, ds, mapped = [], [], [], []
    for panel, (a, b) in enumerate(panels):
        for j, (z, w) in enumerate(zip(roots, weights)):
            v = rat((a+b)/2)+rat((b-a)/2)*z
            weight = rat((b-a)/2)*w
            assert v.lo > 0 and weight.lo > 0
            nodes.append(rat(F(1, 16))+v)
            dr.append(midpoint_radius(weight)); ds.append(midpoint_radius(weight*v))
            mapped.append(dict(panel=panel, node=j, v=record(v), weight_r=record(weight), weight_s=record(weight*v)))
    return nodes, tuple(np.asarray(dr).T), tuple(np.asarray(ds).T), rows, mapped


def main():
    source = ROOT/'stored-fourier-enclosure-certificate.json'
    data = json.loads(source.read_text())
    transforms = {}
    for row in data['transforms']:
        key = row['h'], row['n']
        assert key not in transforms
        transforms[key] = tuple(rat(F(float.fromhex(row[f]))) for f in ('stored_real_hex', 'stored_imag_hex'))
    assert set(transforms) == {(h, n) for h in (0, 1) for n in range(-224, 225)}
    def atan(q):
        a = sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(80)), F(0))
        return I(rat(a).lo, rat(a+q**161/F(161)).hi)
    pi = rat(16)*atan(F(1, 5))-rat(4)*atan(F(1, 239))
    omega = pi/rat(8)
    assert 3*S < pi.lo < pi.hi < 4*S
    z = isqrt(S*S//8); zero = I(z, z+1)
    assert 8*z*z <= S*S < 8*(z+1)**2
    nodes, dr, ds, roots, mapped = gaussian_rule()
    assert len(nodes) == 276
    heat_c, heat_r, heat_rows = [], [], []
    for j, t in enumerate(nodes):
        cs, rs, row = [], [], []
        for n in range(M+1):
            h = ar.exp_negative(t*omega*omega*rat(n*n))
            # e^-x in [0,1], intersect after outward Taylor evaluation.
            h = I(max(0, h.lo), min(S, h.hi))
            assert h.lo <= h.hi
            c, r = midpoint_radius(h)
            cs.append(c); rs.append(r); row.append(record(h))
        heat_c.append(cs); heat_r.append(rs); heat_rows.append(row)
    heat_c, heat_r = np.asarray(heat_c), np.asarray(heat_r)
    print(json.dumps(dict(stage='root/heat enclosures', nodes=len(nodes), path=str(OUTPUT))), flush=True)
    algebra = [operators(pair) for pair in ((0, 2), (1, 3))]
    products = {(alpha, i, c): product_terms(algebra[alpha][0][i], algebra[alpha][1], c)
                for alpha in range(2) for i in range(2) for c in range(4)}
    sensitivity_path = ROOT/'full-time-sensitivity-enclosure-certificate.json'
    sensitivity = json.loads(sensitivity_path.read_text())
    assert sensitivity['input_sha256'] == hashlib.sha256(source.read_bytes()).hexdigest()
    assert int(sensitivity['scale']) == S
    def nested(x):
        return tuple(nested(y) for y in x) if isinstance(x, list) else x
    baselines = {(r['alpha'], r['component'], r['axis'], nested(r['key'])): int(r['baseline_upper'])
                 for r in sensitivity['feature_tables']}
    expected = {(alpha, c, j, key[j]) for (alpha, i, c), op in products.items() for key in op for j in range(4)}
    assert set(baselines) == expected
    absolute_initial = [0, 0]
    for (alpha, i, c), op in products.items():
        for key, coefficient in op.items():
            raw = 1
            for j in range(4):
                raw *= baselines[alpha, c, j, key[j]]
            bound = updiv(raw, S**3)
            v = abs(coefficient)
            absolute_initial[i] += updiv(bound*v.numerator, v.denominator)
    absolute_full = [F(x, S)*8*F(64, 27)**3 for x in absolute_initial]
    cgauss = F(factorial(DEGREE)**4, (2*DEGREE+1)*factorial(2*DEGREE)**3)
    exp_tail = 1/sum((F(108)**j/F(factorial(j)) for j in range(161)), F(0))
    eps_b = cgauss*(1+22*factorial(2*DEGREE+1))+exp_tail
    eps_a = cgauss*(1+2*DEGREE+22*(2*factorial(2*DEGREE+2)+2*DEGREE*factorial(2*DEGREE+1)))+109*exp_tail
    weight_errors = [a*(eps_a+eps_b+eps_a*eps_b) for a in absolute_full]

    @lru_cache(None)
    def prefactor(t, positives, zeros):
        return power(omega, t)*rat(F(1, 4**positives))*power(zero, zeros)

    @lru_cache(None)
    def weak(h, d, a, b, lc, rc, k, ell):
        lp, rp = (k if lc else k+1), (ell if rc else ell+1)
        if (h+d+a+b+lp+rp) % 2 or (k == 0 and (not lc or a)) or (ell == 0 and (not rc or b)):
            return 0., 0.
        value = ZERO
        for p in ((0,) if k == 0 else (-k, k)):
            for q in ((0,) if ell == 0 else (-ell, ell)):
                phase = p+q+a+b-d
                coefficient = p**a*q**b*(p+q)**d
                if not lc:
                    phase -= 1; coefficient *= 1 if p > 0 else -1
                if not rc:
                    phase -= 1; coefficient *= 1 if q > 0 else -1
                re, im = transforms[h, p+q]
                value = value+rat(coefficient)*(re, -im, -re, im)[phase % 4]
        zeros = int(k == 0)+int(ell == 0)
        return midpoint_radius(prefactor(d+a+b, 2-zeros, zeros)*value)

    totals = [(np.zeros((276, 276)), np.zeros((276, 276))) for _ in range(2)]
    groups, coverage, feature_evidence = [], [], []
    for alpha in range(2):
        for component in range(4):
            ops = [products[alpha, i, component] for i in range(2)]
            tables = []
            feature_arrays = {}
            for axis in range(4):
                ks = [0] if axis == 0 else list(range(1, M+1))
                ls = list(range(0 if axis == component else 1, M+1))
                if axis == 0:
                    ls = [n for n in ls if n % 2 == 0]
                h = int(axis in ((0, 2), (1, 3))[alpha])
                features = sorted({key[axis] for op in ops for key in op})
                es = heat_c[:, ks], heat_r[:, ks]
                er = heat_c[:, ls].T, heat_r[:, ls].T
                table = {}
                for index, key in enumerate(features):
                    modes = []
                    for feature in key:
                        rows = [[weak(h, *feature, axis == 0, axis == component, k, ell)
                                 for ell in ls] for k in ks]
                        a = np.asarray(rows)
                        modes.append((a[:, :, 0], a[:, :, 1]))
                    product = multiply(*modes)
                    table[key] = dot(dot(es, product), er)
                    # Complete signed coordinate-table enclosures are saved.
                    name = f'axis{axis}_feature{index}'
                    feature_arrays[name+'_center'] = table[key][0]
                    feature_arrays[name+'_radius'] = table[key][1]
                    coverage.append(dict(alpha=alpha, component=component, axis=axis, index=index, key=key))
                tables.append(table)
            path = ROOT/f'signed-retained-tables-{alpha}-{component}.npz'
            np.savez_compressed(path, **feature_arrays)
            feature_evidence.append(dict(path=path.name, sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
            for i, op in enumerate(ops):
                local = np.zeros((276, 276)), np.zeros((276, 276))
                for key, coefficient in sorted(op.items()):
                    value = tables[0][key[0]]
                    for axis in range(1, 4):
                        value = multiply(value, tables[axis][key[axis]])
                    value = multiply(value, midpoint_radius(rat(coefficient)))
                    local = add(local, value)
                contracted = dot(dot(ds, local), dr)
                groups.append(dict(alpha=alpha, component=component, probe=[3, 6][i],
                                   center=float(contracted[0]), radius=float(contracted[1]), terms=len(op)))
                totals[i] = add(totals[i], local)
            weak.cache_clear()
            print(json.dumps(dict(completed_potential=alpha, component=component,
                                  features=len(coverage), path=str(OUTPUT))), flush=True)
    values = [multiply(dot(dot(ds, t), dr), (8., 0.)) for t in totals]
    final = []
    failures = []
    for i, (c, r) in enumerate(values):
        c, r = float(c), float(r)
        e = F(r)+weight_errors[i]
        coefficient_error = F(int(sensitivity['full_time_sensitivity_upper'][i]), S)
        spectral_tail = [F('1.37381915696e-11'), F('5.49527662781e-11')][i]
        full = e+coefficient_error+spectral_tail
        lo, hi = F(c)-full, F(c)+full
        passed = e < [100, 1000][i]
        sign_certified = lo > 0 or hi < 0
        if not passed or not sign_certified:
            failures.append(f'probe {[3,6][i]} budget/sign failed')
        final.append(dict(probe=[3, 6][i], reported_value_hex=c.hex(), reported_value=c,
                          arithmetic_radius_hex=r.hex(), arithmetic_radius_upper=display(F(r)),
                          weight_error_upper=display(weight_errors[i]), retained_error_upper=display(e),
                          required_retained_error=[100, 1000][i], coefficient_error_upper=display(coefficient_error),
                          spectral_tail_upper=display(spectral_tail), total_error_upper=display(full),
                          exact_I_lower=rational_record(lo), exact_I_upper=rational_record(hi),
                          exact_I_lower_float=float(lo), exact_I_upper_float=float(hi),
                          budget_pass=passed, sign_certified=sign_certified))
    result = dict(status='PASS' if not failures else 'FAIL', scope='Selected upper-face class only; no complete Ward coefficient.',
                  cutoff=M, degree=DEGREE, scale=str(S), input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  sensitivity_input_sha256=hashlib.sha256(sensitivity_path.read_bytes()).hexdigest(),
                  pi_interval=record(pi), zero_amplitude=record(zero), roots=roots, mapped_rule=mapped,
                  heat_enclosures=heat_rows, feature_coverage=coverage, feature_evidence=feature_evidence,
                  collected_groups=groups, absolute_initial_upper=[str(x) for x in absolute_initial],
                  absolute_full_upper=[rational_record(x) for x in absolute_full],
                  inverse_weight_errors=dict(A=rational_record(eps_a), B=rational_record(eps_b)),
                  arithmetic_model=dict(dtype='IEEE binary64', unit_roundoff='1/9007199254740992',
                                        dot_gamma_upper=G.hex(), maximum_inner_dimension=276,
                                        additive_error_per_operation=TINY.hex(),
                                        qualification='Standard correctly rounded product/addition or FMA, arbitrary summation order, gradual underflow or flush-to-zero bounded by 1e-290; no overflow.'),
                  final=final, failures=failures,
                  qualifications=['Gaussian quadrature roots/weights and heat/weak entries use integer outward induction.',
                                  'Tensor enclosure uses the explicitly stated binary64 forward-error model.',
                                  'Saved coordinate tables are complete enclosures, not independently recomputed dot certificates.',
                                  'Other action/measure/insertion/flow classes and nonlinear forest compensation are unresolved.'])
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
    summary = [dict(probe=r['probe'], reported=r['reported_value'],
                    E_upper=r['retained_error_upper'], required_E=r['required_retained_error'],
                    total_error_upper=r['total_error_upper'],
                    I_interval_preview=[r['exact_I_lower_float'], r['exact_I_upper_float']],
                    sign_certified=r['sign_certified']) for r in final]
    print(json.dumps(dict(status=result['status'], final=summary, failures=failures, path=str(OUTPUT))), flush=True)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
