"""Coarse enclosure of L046 A,B with the actual Fourier coefficient errors.

Reuses L039's exact inverse-linear Gauss rule and stated IEEE error model.
All feature tensors are saved, together with full integer input enclosures.
No machine exponential or regenerated Fourier table is a premise.
"""
import hashlib
import json
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt
from pathlib import Path

import numpy as np

import check_exact_fourier_quadrature as ar
import check_signed_retained_enclosure as sr
from check_companion_functional import products, scalar_weight
from check_continuum_pure_sectors import operators

ROOT = Path(__file__).parent
OUTPUT = ROOT/'companion-enclosure-certificate.json'
S, I, M = ar.S, ar.I, 112
ONE, ZERO = I(S), I(0)


def tail_bounds():
    # L033's complete moment upper bounds; all decimals are rational.
    s0, s10 = F('9.95308720484'), F('5.32283164890e12')
    t0, t10 = F('2.10711391688e-49'), F('7.25796325172e-29')
    radial = 7**4*(7*t10*s0**6+42*s10*t0*s0**5)
    constants = [11584512, 46338048]
    tails = [c*radial for c in constants]
    # Both factors have degree 4; scalar S has weighted sum 32.
    new_constants = [(F(2916, 256)**2/F(2**8))*F(64, 27)**2*q*192
                     for q in (192, 768)]
    assert all(n < c for n, c in zip(new_constants, constants))
    assert tails[0] < F('1.38e-11') and tails[1] < F('5.50e-11')
    return tails, dict(moment_upper=[str(x) for x in (s0, s10, t0, t10)],
                       radial_upper=sr.rational_record(radial),
                       domination_constants=constants,
                       companion_constants=[sr.rational_record(x) for x in new_constants])


def main():
    source = ROOT/'stored-fourier-enclosure-certificate.json'
    data = json.loads(source.read_text())
    transforms = {}
    for row in data['transforms']:
        key = row['h'], row['n']
        assert key not in transforms
        error = sr.rat(F(9 if key[0] else 6, 10**12)).hi
        values = [sr.rat(F(float.fromhex(row[f])))
                  for f in ('stored_real_hex', 'stored_imag_hex')]
        transforms[key] = tuple(I(v.lo-error, v.hi+error) for v in values)
    assert set(transforms) == {(h, n) for h in (0, 1) for n in range(-224, 225)}

    def atan(q):
        a = sum(((-1)**j*q**(2*j+1)/F(2*j+1) for j in range(80)), F(0))
        return I(sr.rat(a).lo, sr.rat(a+q**161/F(161)).hi)

    pi = sr.rat(16)*atan(F(1, 5))-sr.rat(4)*atan(F(1, 239))
    omega = pi/sr.rat(8)
    z = isqrt(S*S//8)
    zero = I(z, z+1)
    assert 8*z*z <= S*S < 8*(z+1)**2 and pi.lo > 3*S
    nodes, dr, _, roots, mapped = sr.gaussian_rule()
    assert len(nodes) == 276
    heat_rows, heat_c, heat_r = [], [], []
    for t in [sr.rat(F(1, 16))]+nodes:
        rows, cs, rs = [], [], []
        for n in range(M+1):
            h = ar.exp_negative(t*omega*omega*sr.rat(n*n))
            h = I(max(0, h.lo), min(S, h.hi))
            assert h.lo <= h.hi
            c, r = sr.midpoint_radius(h)
            cs.append(c); rs.append(r); rows.append(sr.record(h))
        heat_rows.append(rows); heat_c.append(cs); heat_r.append(rs)
    heat_c, heat_r = np.asarray(heat_c), np.asarray(heat_r)
    print('Exact rule and heat entries enclosed; path:', OUTPUT, flush=True)
    qs, _, _ = operators((1, 3))
    ops = [products(q, r) for q in qs for r in (scalar_weight(), qs[0])]
    weighted = []
    for op in [*qs, scalar_weight()]:
        restricted = {k: v for k, v in op.items()
                      if k[1] == k[3] == 0 and not k[2][0] and not k[4][0]}
        assert {sum(d)+sum(a)+sum(b) for d, _, a, _, b in restricted} == {4}
        weighted.append(sum((abs(v)*2**sum(k[0]) for k, v in restricted.items()), F(0)))
    assert all(x <= b for x, b in zip(weighted, (192, 768, 32)))

    @lru_cache(None)
    def prefactor(t, positives, zeros):
        return sr.power(omega, t)*sr.rat(F(1, 4**positives))*sr.power(zero, zeros)

    @lru_cache(None)
    def weak(h, d, a, b, k, ell):
        # Axial modes are both zero cosines; transverse modes both sines.
        cosine = k == ell == 0
        lp, rp = (k if cosine else k+1), (ell if cosine else ell+1)
        if (h+d+a+b+lp+rp) % 2 or (cosine and (d or a or b)):
            return ZERO
        value = ZERO
        for p in ((0,) if cosine else (-k, k)):
            for q in ((0,) if cosine else (-ell, ell)):
                phase = p+q+a+b-d
                coefficient = p**a*q**b*(p+q)**d
                if not cosine:
                    phase -= 2
                    coefficient *= (1 if p > 0 else -1)*(1 if q > 0 else -1)
                re, im = transforms[h, p+q]
                value = value+sr.rat(coefficient)*(re, -im, -re, im)[phase % 4]
        return prefactor(d+a+b, 0 if cosine else 2, 2 if cosine else 0)*value

    tables, baseline, coverage, weak_evidence, files = [], [], [], [], []
    for axis in range(4):
        indices = [0] if axis == 0 else list(range(1, M+1))
        h = int(axis in (1, 3))
        features = sorted({key[axis] for op in ops for key in op})
        table, base, archives = {}, {}, {}
        es = heat_c[1:, indices], heat_r[1:, indices]
        er = heat_c[1:, indices].T, heat_r[1:, indices].T
        e0 = heat_c[0, indices], heat_r[0, indices]
        for index, key in enumerate(features):
            matrices = []
            for feature in key:
                intervals = [[weak(h, *feature, k, ell) for ell in indices] for k in indices]
                a = np.asarray([[sr.midpoint_radius(v) for v in row] for row in intervals])
                matrices.append((a[:, :, 0], a[:, :, 1]))
                # Every integer weak enclosure is retained for bounded/full audit.
                weak_evidence.append(dict(axis=axis, feature=feature,
                                          entries=[[sr.record(v) for v in row] for row in intervals]))
            product = sr.multiply(*matrices)
            table[key] = sr.dot(sr.dot(es, product), er)
            absolute = sr.ua(np.abs(product[0]), product[1])
            abs_e0 = sr.ua(np.abs(e0[0]), e0[1])
            base[key] = float(sr.udot(sr.udot(abs_e0, absolute), abs_e0))
            name = f'feature{index}'
            archives[name+'_center'], archives[name+'_radius'] = table[key]
            coverage.append(dict(axis=axis, index=index, key=key,
                                 initial_absolute_upper_hex=base[key].hex()))
        path = ROOT/f'companion-enclosure-axis{axis}.npz'
        np.savez_compressed(path, **archives)
        files.append(dict(path=path.name, sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        tables.append(table); baseline.append(base)
        weak.cache_clear()
        print('Enclosed axis', axis, 'features', len(features), 'path:', OUTPUT, flush=True)

    cgauss = F(factorial(12)**4, 25*factorial(24)**3)
    exp_tail = 1/sum((F(108)**j/F(factorial(j)) for j in range(161)), F(0))
    eps = cgauss*(1+22*factorial(25))+exp_tail
    tails, tail_evidence = tail_bounds()
    final, failures = [], []
    for slot, op in enumerate(ops):
        local = np.zeros((276, 276)), np.zeros((276, 276))
        absolute_initial = F(0)
        for key, coefficient in sorted(op.items()):
            value = tables[0][key[0]]
            envelope = F(baseline[0][key[0]])
            for axis in range(1, 4):
                value = sr.multiply(value, tables[axis][key[axis]])
                envelope *= F(baseline[axis][key[axis]])
            local = sr.add(local, sr.multiply(value, sr.midpoint_radius(sr.rat(coefficient))))
            absolute_initial += abs(coefficient)*envelope
        center, radius = sr.dot(sr.dot(dr, local), dr)
        center, radius = float(center), float(radius)
        weight_error = absolute_initial*F(64, 27)**2*(2*eps+eps**2)
        error = F(radius)+weight_error+tails[slot//2]
        lo, hi = F(center)-error, F(center)+error
        final.append(dict(probe=(3, 6)[slot//2], trace=('A', 'B')[slot%2],
                          terms=len(op), center_hex=center.hex(), radius_hex=radius.hex(),
                          absolute_initial_upper=sr.rational_record(absolute_initial),
                          weight_error=sr.rational_record(weight_error),
                          spectral_tail=sr.rational_record(tails[slot//2]),
                          total_error=sr.rational_record(error),
                          lower=sr.rational_record(lo), upper=sr.rational_record(hi)))
    comparisons = []
    required = [F('21734.4'), F('160876.8')]
    def frac(record):
        return F(int(record['num']), int(record['den']))
    for i in range(2):
        a, b = final[2*i:2*i+2]
        al, ah = frac(a['lower']), frac(a['upper'])
        bl, bh = frac(b['lower']), frac(b['upper'])
        jl, jh = 16*al+24*min(F(0), bl), 16*ah+24*max(F(0), bh)
        separated = jh < required[i]
        if not separated:
            failures.append(f'probe {(3,6)[i]} separation upper >= {required[i]}')
        comparisons.append(dict(probe=(3, 6)[i], J_lower=sr.rational_record(jl),
                                J_upper=sr.rational_record(jh),
                                required_J_upper_below=str(required[i]), separated=separated))
    result = dict(status='PASS' if not failures else 'FAIL', scale=str(S), cutoff=M,
                  degree=12, input_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
                  implementation_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  pi=sr.record(pi), zero_amplitude=sr.record(zero), roots=roots,
                  mapped_rule=mapped, heat_enclosures=heat_rows,
                  weak_enclosures=weak_evidence, feature_coverage=coverage, feature_files=files,
                  weighted_expansion_sums=[str(x) for x in weighted],
                  inverse_linear_relative_error=sr.rational_record(eps),
                  spectral_tail_evidence=tail_evidence, final=final, comparisons=comparisons,
                  arithmetic_model=dict(dtype='IEEE binary64', unit_roundoff='1/9007199254740992',
                                        dot_gamma_upper=sr.G.hex(), maximum_inner_dimension=276,
                                        additive_error_per_operation=sr.TINY.hex(),
                                        qualification='L039 standard correctly rounded addition/product or FMA; arbitrary summation order; no overflow; underflow bounded by 1e-290.'),
                  failures=failures, full_response_computed=False)
    OUTPUT.write_text(json.dumps(result, indent=2)+'\n')
    for row in final:
        print('Probe', row['probe'], row['trace'], 'interval:',
              float(frac(row['lower'])), float(frac(row['upper'])),
              'total error upper:', sr.display(frac(row['total_error'])))
    for row in comparisons:
        print('Probe', row['probe'], 'J interval:', float(frac(row['J_lower'])),
              float(frac(row['J_upper'])), 'required upper <', row['required_J_upper_below'])
    print('Failures:', failures, 'path:', OUTPUT)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
