#!/usr/bin/env python3
"""Diagnostic only: full-kernel reflected-majorant scan, no sign certificate.
Run from riemann: python3 scripts/reflected-majorant/scan.py
"""
import json
from pathlib import Path
import numpy as np
from numpy.polynomial import chebyshev as ch
from numpy.polynomial.legendre import leggauss

OUT = Path('scripts/reflected-majorant/scan-certificate.json')
L, R, MODES = 3.0, 6.0, 8
hs = np.linspace(1/8, 4, 129)
qs = np.linspace(1/8, 1/2, 97)
hh, qq = np.meshgrid(hs, qs, indexing='ij')
rr = hh * qq

def kernel(u):
    u = np.abs(u)
    v = np.pi * np.arange(1, MODES+1, dtype=float)**2
    z = np.exp(2*u)[..., None] * v
    # This is the complete positive summand from L019; omitted modes
    # have a separate analytic bound recorded in the canonical proof.
    return np.sum(4*z*(2*z-3)*np.exp(u[..., None]/2-z), axis=-1)

def run(nc, ns):
    theta = (np.arange(nc)+0.5)*np.pi/nc
    ts = L*(1+np.cos(theta))/2
    roots, weights = leggauss(ns)
    ss, ww = R*(roots+1)/2, R*weights/2
    av = np.empty(nc)
    for j,t in enumerate(ts):
        av[j] = 2*np.dot(ww, ss**2 * kernel(ss+t) * kernel(ss-t))
    coeff = (2/nc)*np.cos(np.outer(np.arange(nc), theta)) @ av
    coeff[0] /= 2
    primitive = ch.chebint(coeff)*L/2
    top = ch.chebval(1.0, primitive)
    def G(t):
        t = np.asarray(t)
        # The discarded cumulative constant is bounded independently;
        # no positivity clamp conceals interpolation residuals.
        return np.where(t <= L, top-ch.chebval(2*np.minimum(t,L)/L-1, primitive), 0.)
    def S(t):
        acc = np.zeros_like(t)
        for j in range(int(np.ceil(L/(2*float(hs.min()))))+1):
            acc += G(t+2*j*hh)-G(t+(2*j+1)*hh)
        return acc
    g0 = float(G(0.))
    defects = g0-S(rr)-S(hh-rr)
    ij = np.unravel_index(np.argmin(defects), defects.shape)
    return {
      'chebyshev_nodes': nc, 's_gauss_nodes': ns, 'G0': g0,
      'minimum': {'D': float(defects[ij]), 'D_over_G0': float(defects[ij]/g0),
                  'h': float(hh[ij]), 'r': float(rr[ij]), 'r_over_h':float(qq[ij])},
      'negative_preview_count': int(np.count_nonzero(defects<0)),
      'defects': defects.tolist(),
      'coefficient_last_16_l1': float(np.abs(coeff[-16:]).sum())
    }

runs = [run(nc, ns) for nc,ns in [(128,192),(256,384),(384,512)]]
for a,b in zip(runs,runs[1:]):
    b['max_abs_change_from_previous_grid'] = float(np.max(np.abs(np.array(a['defects'])-np.array(b['defects']))))
result = {
  'status': 'DIAGNOSTIC_ONLY_NO_RIGOROUS_SIGN_CERTIFICATE',
  'target': 'D_h(r)=G(0)-S_h(r)-S_h(h-r), complete actual-theta kernel',
  'domain': {'h': [1/8,4], 'r_over_h':[1/8,1/2]},
  'grid': {'h':hs.tolist(), 'r_over_h':qs.tolist(), 'pairs':int(hh.size)},
  'cutoffs': {'theta_modes':MODES,'s_integral':R,'G_integral':L},
  'analytic_bounds': {
    'complete_G3_upper_bound': '10^-500 (proved in L598)',
    'mode_and_s_tail_effect_on_D_upper_bound': '10^-92 (proved in L598)',
    'full_alternating_cumulative_tail_effect_upper_bound': 'G(3) (proved in L598)'},
  'missing_error_bounds': ['Gauss quadrature discretization','Chebyshev interpolation/integration','floating point rounding'],
  'certified_negative_pairs': 0,
  'required_for_negative_certificate': 'rigorous total absolute error < -computed_D at a pair with computed_D<0',
  'actual_rigorous_total_error_bound': None,
  'failures': ['No rigorous quadrature/interpolation/rounding enclosure; positive grid values prove no signs.'],
  'runs':runs
}
OUT.write_text(json.dumps(result,indent=2)+'\n')
for run in runs:
    print({k:v for k,v in run.items() if k!='defects'})
print('Actual rigorous total error: unavailable; required for a negative certificate: total error < -D at a negative candidate.')
print('Certified negative pairs: 0. This is a numerical preview, not proof of any sign.')
print('Full diagnostic certificate:',OUT)
