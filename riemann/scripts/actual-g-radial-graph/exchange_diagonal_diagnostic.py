"""One fixed-circle diagnostic; floats and samples certify no inequality."""
import cmath
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / 'scripts/actual-fredholm/fixed-pair-certificate-431.json'
OUT = Path(__file__).with_name('exchange-diagonal-diagnostic.json')
data = json.loads(SOURCE.read_text())
coeff = [(float(a)+float(b))/2 for a, b in data['evaluation']['coefficients']]
rows = []
for j in range(2048):
    m = 2*math.pi*j/2048
    disc = math.sqrt(600**2-400**2*math.sin(m)**2)
    radius = -400*math.cos(m)+disc
    hprime = 400*math.sin(m)/disc
    z = radius*cmath.exp(1j*m)
    g = 0j
    for a in reversed(coeff):
        g = g*z+a
    f = g/z
    phi = cmath.phase(f)
    psi = 2*phi-math.atan(hprime)
    rows.append({'m': m, 'radius': radius, 'hprime': hprime,
                 'f_real': f.real, 'f_imag': f.imag, 'phi': phi,
                 'psi': psi, 'normal_derivative': math.tan(psi/3)})
summary = {
    'min_sampled_real_G_over_z': min(r['f_real'] for r in rows),
    'required_uniform_real_G_over_z': '> 0',
    'max_sampled_abs_phi': max(abs(r['phi']) for r in rows),
    'sufficient_uniform_abs_phi': '< pi/2',
    'max_sampled_abs_psi': max(abs(r['psi']) for r in rows),
    'required_uniform_abs_psi': '< 3*pi/2',
    'max_sampled_abs_normal_derivative': max(abs(r['normal_derivative']) for r in rows),
}
OUT.write_text(json.dumps({
    'status': 'NONRIGOROUS_DIAGNOSTIC_ONLY',
    'circle': {'center': -400, 'radius': 600},
    'input': str(SOURCE.relative_to(ROOT)),
    'input_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'summary': summary, 'samples': rows,
    'limitations': ['Floating point and midpoint coefficients.',
                    'No rounding, coefficient-width, G-error or between-sample certificate.']
}, indent=2)+'\n')
print('NONRIGOROUS_DIAGNOSTIC_ONLY')
print(json.dumps(summary))
print('Full diagnostic:', OUT.relative_to(ROOT))
