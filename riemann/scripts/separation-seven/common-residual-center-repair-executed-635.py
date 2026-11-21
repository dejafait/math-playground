#!/usr/bin/env python3
"""One fixed635 point prerequisite. No scalar objective or optimizer.

Exact point coordinates are recursive rational expressions in C999y.
This checks every JY bound by outward arithmetic, and replays600's
given inclusion. All original graph radii remain unchanged.
"""
import hashlib
import json
from decimal import Decimal
from fractions import Fraction
from pathlib import Path

import numpy as np

P = Path(__file__).resolve().parent
TARGET = ('Test whether the fixed zero-center prescription with only fresh JY '
          'and head Delta repairs yields an exact equality-compatible box point for C999w.')
out = P / 'common-residual-center-repair-635'
checks, failures, data, report = [], [], {}, {}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ck(ok, name):
    checks.append({'label': name, 'passed': bool(ok)})
    if not ok:
        failures.append(name)
        raise RuntimeError(name)


def keep(name, a):
    data[name] = a
    return a


try:
    manifest = json.loads((P / 'joint-entrywise-600.json').read_text())
    pins = dict(manifest['input_hashes'])
    pins['joint-entrywise-600.py'] = manifest['script_sha256']
    pins['joint-entrywise-600.npz'] = manifest['archive']['sha256']
    report['input_hashes'] = pins
    for name, expected in pins.items():
        ck(sha(P / name) == expected, 'pin ' + name)
    ck(manifest['failures'] == [], '600 recorded arithmetic checks')

    # Read definitions only. Never run600's calculation or write its artifacts.
    source = (P / 'joint-entrywise-600.py').read_text().split('\nnames = ')[0]
    ns = {'__file__': str(P / 'joint-entrywise-600.py')}
    # Verification arithmetic only: gamma_2044<2.28e-13 <1e-12.
    # This changes no primitive/product radius in the defined AA graph.
    exec(compile(source.replace('1e-11', '1e-12'), str(P / 'joint-entrywise-600.py'), 'exec'), ns)
    Ball, I, iv = ns['Ball'], ns['I'], ns['iv']
    up, ab, pdot, block = ns['up'], ns['abs_upper'], ns['positive_dot'], ns['block']
    with np.load(P / 'joint-entrywise-600.npz') as q:
        keys = ['Z_center', 'Z_radius', 'M_center', 'M_radius',
                'galerkin_solution_center', 'galerkin_solution_radius',
                'galerkin_W', 'galerkin_proposal', 'galerkin_K_center',
                'galerkin_K_radius', 'galerkin_z_center', 'galerkin_z_radius',
                'galerkin_inclusion_box', 'galerkin_inclusion_image_radius',
                'head_reference_W']
        a = {k: q[k].copy() for k in keys}
    with np.load(P / 'original-galerkin-586.npz') as q:
        tc, tsc, uc = [q[k].copy() for k in ['t_entries', 'ts_entries', 'u_entries']]
    zc, zr, mc, mr, yc, yr = [a[k] for k in keys[:6]]
    ck(zc.shape == (1024, 1022) and yc.shape == (1022, 2044), 'fixed full dimensions')
    ck(all(np.isfinite(v).all() for v in a.values()), 'finite saved dyadics')
    ck(np.all(zr >= 0) and np.all(mr >= 0) and np.all(yr >= 0), 'nonnegative primitive radii')
    ck(np.array_equal(mc, mc.T) and np.array_equal(mr, mr.T), 'M shared symmetric boxes')
    ck(np.array_equal(tc, tsc.T), 'T adjoint sharing')
    template = np.eye(1024)[:, 2:]
    template[:2] = zc[:2]
    ck(np.array_equal(zc, template), 'all sparse Z center positions')
    mask = np.zeros_like(zc, dtype=bool)
    mask[np.arange(2, 1024) % 2, np.arange(1022)] = True
    ck(np.all(zr[~mask] == 0), 'all unused Z radii exactly zero')
    ck(np.array_equal(mr, ns['response_radius']()), 'unchanged600 local radii')

    def powi(x, n):
        ans = I(1)
        for _ in range(n):
            ans *= x
        return ans

    def atan(q):
        t = I(1) / q
        val = sum(((-1)**j * powi(t, 2*j+1) / (2*j+1) for j in range(80)), I(0))
        rem = powi(t, 161) / 161
        return val + I(-rem.hi, rem.hi)

    pi, ell = 16*atan(5)-4*atan(239), I(3).ln()/2
    ratio_records = []
    for n in range(2, 1024):
        p = n % 2
        rr = (I('.25') + powi(p*pi/ell, 2)) / (I('.25') + powi(n*pi/ell, 2))
        if p == 0:
            rr *= I(2).sqrt()
        c, r = Fraction(float(zc[p, n-2])), Fraction(float(zr[p, n-2]))
        ck(c-r <= -Fraction(rr.hi) and -Fraction(rr.lo) <= c+r,
           'exact directed ratio containment ' + str(n))
        ratio_records.append(rr.json())
    report['directed_ratio_intervals'] = ratio_records

    # Replay the saved matrix-RHS inclusion against the original input boxes.
    z, m = Ball(zc, zr), Ball(mc, mr)
    cross = float(up(float(Decimal('.000001'))))
    t, ts = Ball(tc, cross), Ball(tsc, cross)
    aa = z.T @ m @ z
    bb = z.T @ block([[t @ z, ts @ z]])
    w, proposal = Ball(a['galerkin_W']), a['galerkin_proposal']
    kk = Ball(np.eye(1022)) - w @ aa
    zz = w @ (bb - aa @ Ball(proposal))
    oldk = Ball(a['galerkin_K_center'], a['galerkin_K_radius'])
    oldz = Ball(a['galerkin_z_center'], a['galerkin_z_radius'])
    kmargin = keep('K_reenclosure_margin', np.nextafter(oldk.r - ab(kk-Ball(oldk.c)), -np.inf))
    zmargin = keep('z_reenclosure_margin', np.nextafter(oldz.r - ab(zz-Ball(oldz.c)), -np.inf))
    ck(np.all(kmargin >= 0), 'all saved K entries enclose replay')
    ck(np.all(zmargin >= 0), 'all saved z entries enclose replay')
    image = up(oldz.r + pdot(ab(oldk), a['galerkin_inclusion_box']))
    imargin = keep('strict_inclusion_margin', np.nextafter(
        a['galerkin_inclusion_box']-up(np.abs(oldz.c)+image), -np.inf))
    ck(np.all(imargin > 0), 'strict inclusion all1022x2044 entries')
    ck(np.all(image <= a['galerkin_inclusion_image_radius']), 'all saved image radii enclose replay')
    # Bound the exact dyadic recentering proposal+z_center-Yc with paid additions.
    shift = ab(Ball(proposal)+Ball(oldz.c)-Ball(yc))
    ymargin = keep('Y_recenter_margin', np.nextafter(
        yr-up(a['galerkin_inclusion_image_radius']+shift), -np.inf))
    ck(np.all(ymargin >= 0), 'saved exact-Y boxes contain all recentered solutions')
    rows = up(np.sum(ab(oldk), axis=1)*(1+1e-12)+1e-280)
    ck(np.all(rows < 1), 'saved inclusion contraction regularity')

    # Exact AA centers are enclosed here; no floating center becomes its definition.
    z, m = Ball(zc), Ball(mc)
    ac = z.T @ (m @ z)
    ac = (ac+ac.T).scale(.5)
    bc = z.T @ block([[Ball(tc) @ z, Ball(tsc) @ z]])
    residual = bc-ac @ Ball(yc)
    upper = keep('JY_repair_residual_abs_upper', ab(residual))
    # Every mr>=1e-7 exactly. Downward dyadic proxy is a STRICT lower bound.
    mr_min = float(mr.min())
    ck(Fraction(mr_min) >= Fraction(1, 10**7), 'all actual M radii >= rational1e-7')
    beta = float(np.nextafter(1e-7, 0))
    ck(Fraction(beta) < Fraction(1, 10**7), 'dyadic lower proxy < rational1e-7')
    sums = np.sum(yr, axis=0)
    # Positive dot length1022; gamma_1022<1.14e-13. Factor1-1e-12
    # pays summation and its own rounding; nextafter pays final multiplication.
    lower = keep('JY_fresh_coefficient_column_lower', np.nextafter(
        np.nextafter(sums*(1-1e-12), -np.inf)*beta, -np.inf))
    margin = keep('JY_repair_unit_margin', np.nextafter(lower[None, :]-upper, -np.inf))
    ck(np.all(lower > 0), 'no JY zero-radius case: all2044 lower bounds positive')
    ck(np.all(margin > 0), 'all2089064 prescribed JY coordinates strictly within unit box')
    normalized_upper = up(upper/lower[None, :])
    keep('JY_normalized_abs_upper', normalized_upper)
    ck(np.all(normalized_upper < 1), 'all normalized repair bounds <1')
    report['bounds'] = {
        'JY_equalities_checked': int(upper.size),
        'head_equalities_symbolically_checked': 512*2044,
        'JY_max_normalized_abs_upper': float(normalized_upper.max()),
        'required_normalized_abs_upper': 1,
        'JY_min_fresh_coefficient_lower': float(lower.min()),
        'JY_max_center_residual_upper': float(upper.max()),
        'JY_min_unit_margin': float(margin.min()),
        'Y_min_recenter_margin': float(ymargin.min()),
        'inclusion_min_margin': float(imargin.min()),
        'contraction_max_row_upper': float(rows.max()),
    }
    report['head_symbolic_certificate'] = {
        'exact_H': 'm0-(3/12500)I-(100/307)(cov00+(23/5000)I)',
        'rho0_P': 'first512 rows of [Tc Zc,Tc^t Zc]-(Mc Zc)Yc',
        'X0': 'adj(H) rho0_P / det(H)',
        'identity': 'H adj(H)=det(H)I; H>=239999/1000000 I, hence det(H)!=0',
        'Delta': '(H^-1-W)rho0_P',
        'unit_bound': '|Delta_aj|<=h0^-1 sum_ab |(I-HW)_ab| |rho0_bj|<=e_j',
        'zero_e_j': 'Delta_:j=0 by same bound; eta_:j=0',
        'reference_floor_is_inherited': True,
    }
    ck(all(sha(P/name) == value for name, value in pins.items()), 'all inherited input files preserved')
except Exception as exc:
    if not failures:
        failures.append(type(exc).__name__ + ': ' + str(exc))

archive = out.with_suffix('.npz')
np.savez_compressed(archive, **data)
report.update(target=TARGET, result='PASS' if not failures else 'INCONCLUSIVE',
              checks=checks, failures=failures, script_sha256=sha(Path(__file__)),
              archive={'path': str(archive.relative_to(P.parent.parent)), 'sha256': sha(archive)},
              qualifications=['Exact symbolic head identity and all-zero graph coordinates are justified in C999y',
                              'All original analytic-response/IEEE754/Decimal/core/c_star and reference-floor contracts retained',
                              'No physical assignment, scalar sign, PSD witness or .000999 floor established'])
out.with_suffix('.json').write_text(json.dumps(report, indent=2)+'\n')
print('result', report['result'], 'bounds', report.get('bounds'), 'failures', failures)
print('certificate', out.with_suffix('.json').relative_to(P.parent.parent), 'arrays', archive.relative_to(P.parent.parent))
