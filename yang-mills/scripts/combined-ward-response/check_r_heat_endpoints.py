"""Exact rational comparisons for L146's readable strict endpoints."""
import json
from fractions import Fraction as F
from pathlib import Path
import enclose_r_heat_form as g

ROOT = Path(__file__).parent
PATH = ROOT/'r-heat-endpoint-check.json'


def main():
    data = json.loads(g.CERT.read_text())
    audit = json.loads(g.AUDIT.read_text())
    assert not data['failures'] and audit['passed'] and not audit['failures']
    assert audit['certificate_sha256'] == g.sha(g.CERT)
    b_bounds = {3: ('1228.1260684', '1228.1260686'),
                6: ('451.5469823', '451.5469825')}
    g_bounds = {3: ('-74.916', '-52.809'), 6: ('-27.545', '-19.416')}
    error_bounds = {3: '0.00000003173', 6: '0.00000001061'}
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
        assert error < F(error_bounds[i]) <= F('0.00000003173') < 1
        assert spatial < F('0.00000003172')
        assert g.fraction(r['time_error']) < F('0.000000001362')
        assert g.fraction(r['spectral_tail']) < F('0.000000000000005329')
        rows.append(dict(probe=i, retained=r['retained'], B_bounds=b_bounds[i],
                         R_bounds=g_bounds[i], total_error_bound=error_bounds[i],
                         terms=r['terms'], passed=True))
        print(f'Probe {i}: B in {b_bounds[i]}, R in {g_bounds[i]}; actual error {float(error):.9g}, required <{error_bounds[i]}; exact comparisons PASS')
    spatial = json.loads((ROOT/'r-spatial-enclosure-certificate.json').read_text())
    required = spatial['required_moments']
    maxima = {str(h): max(abs(n) for hh,n in required if hh==h) for h in {h for h,n in required}}
    assert maxima == {'0':192, '1':192, '2':96, '3':0}
    out = dict(required_moment_frequency_maxima=maxima, certificate_sha256=g.sha(g.CERT), audit_sha256=g.sha(g.AUDIT),
               script_sha256=g.sha(Path(__file__)), rows=rows, passed=True, failures=[])
    PATH.write_text(json.dumps(out, indent=2)+'\n')
    print(f'Failures 0; complete exact endpoint checks {PATH}')


if __name__ == '__main__':
    main()
