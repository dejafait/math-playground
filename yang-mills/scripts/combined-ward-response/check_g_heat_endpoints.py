"""Exact rational comparisons for L144's readable strict endpoints."""
import json
from fractions import Fraction as F
from pathlib import Path
import enclose_g_heat_form as g

ROOT = Path(__file__).parent
PATH = ROOT/'g-heat-endpoint-check.json'


def main():
    data = json.loads(g.CERT.read_text())
    audit = json.loads(g.AUDIT.read_text())
    assert not data['failures'] and audit['passed'] and not audit['failures']
    assert audit['certificate_sha256'] == g.sha(g.CERT)
    b_bounds = {3: ('2408.3740053', '2408.3740056'),
                6: ('5174.7326818', '5174.7326826')}
    g_bounds = {3: ('-146.92', '-103.56'), 6: ('-315.66', '-222.51')}
    error_bounds = {3: '0.00000008164', 6: '0.000000344'}
    rows = []
    for r, combo in zip(data['results'], data['combined']):
        i = r['probe']
        lo, hi = (g.fraction(r[k]) for k in ('lower', 'upper'))
        gl, gh = (g.fraction(combo[k]) for k in ('lower', 'upper'))
        error = g.fraction(r['total_error'])
        blo, bhi = map(F, b_bounds[i])
        dlo, dhi = map(F, g_bounds[i])
        spatial = F(float.fromhex(r['retained']['radius_hex']))
        assert blo < lo <= hi < bhi
        assert dlo < gl <= gh < dhi < 0
        assert error < F(error_bounds[i]) <= F('0.000000344') < 1
        assert spatial < F('0.0000002896')
        assert g.fraction(r['time_error']) < F('0.00000005401')
        assert g.fraction(r['spectral_tail']) < F('0.0000000000006373')
        rows.append(dict(probe=i, retained=r['retained'], B_bounds=b_bounds[i],
                         G_bounds=g_bounds[i], total_error_bound=error_bounds[i],
                         terms=r['terms'], passed=True))
        print(f'Probe {i}: B in {b_bounds[i]}, G in {g_bounds[i]}; actual error {float(error):.9g}, required <{error_bounds[i]}; exact comparisons PASS')
    out = dict(certificate_sha256=g.sha(g.CERT), audit_sha256=g.sha(g.AUDIT),
               script_sha256=g.sha(Path(__file__)), rows=rows, passed=True, failures=[])
    PATH.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Failures 0; complete exact endpoint checks {PATH}')


if __name__ == '__main__':
    main()
