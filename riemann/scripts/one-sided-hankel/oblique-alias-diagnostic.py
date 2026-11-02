"""Bounded Fourier/contour diagnostic; no interval or asymptotic claim."""
import json
from pathlib import Path
import numpy as np

NGRID = 8192
x, R, r = -1.25, 1.375, .54
U = R*R
phi = 13*np.pi/16
u = np.exp(1j*phi)
angles = 2*np.pi*np.arange(NGRID)/NGRID
records, contours, failures = [], [], []

def log_weights(n, v):
    logs = np.log(x/v)
    for j in range(1, n):
        t = j/n
        logs += np.log((x-t*u)/(v-t*u)*(U*u-t*v)/(U*u-t*x))
    return logs

for n in (51, 99, 195, 387, 771):
    m = n//3
    per_shift = []
    for h in (0., .2, .4):
        tt = angles-1j*h
        v = x+1j*r*np.cos(tt)
        logs = log_weights(n, v)
        coeffs = []
        for k in range(6):
            ell = 2*m*k
            integrand = np.exp(logs-1j*ell*tt)
            z = np.mean(integrand)
            coeffs.append({"index": ell, "real": float(z.real), "imag": float(z.imag),
                           "abs": float(abs(z)),
                           "absolute_mean_to_result": float(np.mean(abs(integrand))/max(abs(z),1e-300))})
        b = [complex(c['real'], c['imag']) for c in coeffs]
        leading = abs(b[0]-2*b[1])
        per_shift.append({"h": h, "coefficients": coeffs,
                          "leading_abs": float(leading),
                          "leading_rate": float(-np.log(leading)/n),
                          "four_selected_higher_aliases_abs": float(2*sum(abs(z) for z in b[2:])),
                          "contour_log_sup_over_n": float(max(logs.real)/n)})
    nodes = x+1j*r*np.cos((2*np.arange(m)+1)*np.pi/(2*m))
    node_avg = np.mean(np.exp(log_weights(n,nodes)))
    records.append({"n": n, "m": m, "shifts": per_shift,
                    "node_average": [float(node_avg.real),float(node_avg.imag)],
                    "node_average_abs": float(abs(node_avg))})

for h in (.1, .15, .2, .25, .3, .35, .4):
    logs = log_weights(1200,x+1j*r*np.cos(angles-1j*h))
    sup = float(max(logs.real)/1200)
    contours.append({"h":h, "sampled_log_sup_over_n":sup,
                     "sampled_higher_alias_decay":4*h/3-sup,
                     "sampled_first_alias_decay":2*h/3-sup})

for rec in records:
    zs = [complex(*[s['coefficients'][1][k] for k in ('real','imag')]) for s in rec['shifts']]
    disagreement = max(abs(z-zs[0]) for z in zs)/max(abs(zs[0]),1e-300)
    rec['first_alias_shift_relative_disagreement'] = float(disagreement)
    if disagreement > 1e-7:
        failures.append(f"n={rec['n']}: first alias shift disagreement >1e-7")

# A half-plane bound can control the entire ellipse without following
# its maximizing point. These floating values only select a certificate.
tt=(np.arange(4096)+.5)/4096
c,s=np.cos(phi),np.sin(phi)
hline=1.25-.54*.3
a=hline+tt*c
g=((U*c+tt*hline)**2+s*s*(U-tt*tt)**2)/(a*a)
off=-tt*s*(U-tt*tt)/a
vmax=(tt*tt+g+np.sqrt((tt*tt-g)**2+4*off*off))/2
ratios=vmax*(1.25**2+2*1.25*c*tt+tt*tt)/(U*U+2*U*1.25*c*tt+1.25**2*tt*tt)
half_plane={"hline":hline,"sampled_log_ratio_mean":float(np.mean(np.log(ratios))/2),
            "sampled_ratio_squared_max":float(max(ratios)),
            "alias_tail_contour_exponent":float(4*np.arcsinh(.3)/3)}

out=Path(__file__).with_suffix('.json')
out.write_text(json.dumps({"status":"NONRIGOROUS_DIAGNOSTIC_ONLY", "required_rate":1/32,
                          "angle":float(phi), "quadrature_points":NGRID,
                          "records":records,"contours":contours,"half_plane":half_plane,"failures":failures,
                          "limitations":["No rounding or quadrature enclosure.",
                          "Selected higher aliases are not the full tail.",
                          "One angle and finitely many n prove no asymptotic or angular bound."]},indent=2)+'\n')
print('NONRIGOROUS DIAGNOSTIC ONLY; required leading rate <',1/32)
for rec in records:
    s=rec['shifts'][0]
    print('n',rec['n'],'leading rate',s['leading_rate'],'selected tail',s['four_selected_higher_aliases_abs'],
          'shift disagreement',rec['first_alias_shift_relative_disagreement'])
print('Sampled contour decay:',[(c['h'],c['sampled_higher_alias_decay']) for c in contours])
print('Half-plane diagnostic:',half_plane)
print('Shifted b0 evaluations have severe cancellation and are not reliable.')
print('Failures:',failures)
print('Full diagnostic:',out)
