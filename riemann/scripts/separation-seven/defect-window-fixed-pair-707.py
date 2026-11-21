#!/usr/bin/env python3
"""One frozen exact-neutral bilinear lower test; ready assessment705.

SVD only proposes a pair. All subsequent scalar contractions are exact
integer/rational arithmetic. The actual Z, analytic/entry errors and
original execution contracts are imported from audited C999l(1)-(6).
Existing pair files are reused, never replaced by a second proposal.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import numpy as np

HERE = Path(__file__).resolve().parent
PAIR = HERE / 'defect-window-fixed-pair-707-witness.json'
OUT = HERE / 'defect-window-fixed-pair-707.json'
checks = []


def sha(p):
    return sha256(p.read_bytes()).hexdigest()


def check(label, value):
    checks.append(dict(label=label, passed=bool(value)))
    if not value:
        raise AssertionError(label)


def sqrt_upper(q):
    """Exact rational upper square root, independent of floating sqrt."""
    assert q >= 0
    scale = 10**80
    n = isqrt((q.numerator * scale**2) // q.denominator)
    hi = F(n+1, scale)
    assert hi*hi >= q
    return hi


def common_dyadics(values):
    ratios = [float(v).as_integer_ratio() for v in values]
    powers = [d.bit_length()-1 for _, d in ratios]
    assert all(d == 1 << p for (_, d), p in zip(ratios, powers))
    power = max(powers)
    return [n << (power-p) for (n, _), p in zip(ratios, powers)], power


def vector_dyadics(strings):
    values = [F(s) for s in strings]
    powers = [q.denominator.bit_length()-1 for q in values]
    assert all(q.denominator == 1 << p for q, p in zip(values, powers))
    power = max(powers)
    return [q.numerator << (power-p) for q, p in zip(values, powers)], power


def exact_bilinear(matrix, left, right):
    """left^t matrix right, using every stored dyadic entry exactly."""
    li, lp = left
    ri, rp = right
    mi, mp = common_dyadics(matrix.flat)
    n = len(ri)
    assert matrix.shape == (len(li), n)
    total = 0
    for i, l in enumerate(li):
        total += l * sum(mi[i*n+j]*r for j, r in enumerate(ri))
    return F(total, 1 << (lp+mp+rp))


def exact_norm_squared(vector):
    vi, p = vector
    return F(sum(v*v for v in vi), 1 << (2*p))


def interval(center, radius):
    return dict(lo=str(center-radius), hi=str(center+radius))


def decimal_view(q):
    # Display only. All certificate comparisons use exact F values.
    return format(float(q), '.15g')


def main():
    original = json.loads((HERE/'neutral-head-covariance-559.json').read_text())
    audit = json.loads((HERE/'neutral-head-covariance-audit-561.json').read_text())
    audit534 = json.loads((HERE/'certificate-audit-534.json').read_text())
    pins = {}
    for name, expected in audit['original_hashes'].items():
        actual = sha(HERE/name)
        check('unchanged audited input '+name, actual == expected)
        pins[name] = actual
    for name in ['neutral-head-covariance-audit-561.json', 'certificate-audit-534.json']:
        pins[name] = sha(HERE/name)
    check('original checks all pass', not original['failures'] and all(c['passed'] for c in original['checks']))
    check('audit561 checks all pass', not audit['failures'] and all(c['passed'] for c in audit['checks']))
    check('audit534 failures empty', not audit534['failures'])
    check('complete raw head hash agrees with534', pins['complete-covariance-532.npz'] == audit534['original_sha256']['complete-covariance-532.npz'])
    check('entire saved neutral head hash', pins['neutral-head-covariance-559.npz'] == original['binary_artifact']['sha256'])

    with np.load(HERE/'neutral-head-covariance-559.npz') as data:
        aa, bb = data['a'], data['b'][:, :510]
    check('fixed complete centers shape and finiteness', aa.shape == bb.shape == (510,510) and np.isfinite(aa).all() and np.isfinite(bb).all())

    if not PAIR.exists():
        # A single diagnostic generalized singular pair. No success or
        # eigenvalue claim depends on its numerical accuracy.
        ll = np.linalg.cholesky((aa+aa.T)/2)
        ww = np.linalg.solve(ll, bb)
        ww = np.linalg.solve(ll, ww.T).T
        uu, ss, vh = np.linalg.svd(ww, full_matrices=False)
        alpha = np.linalg.solve(ll.T, vh[0])
        beta = np.linalg.solve(ll.T, uu[:,0])
        frozen = dict(
            scope='ONE independent pair; exact Z of C999l(1), N512, tau=1/4',
            selection='First singular pair of L^-1 Bhat_first L^-t; L from symmetrized Ahat. Proposal only.',
            diagnostic_singular_value=float(ss[0]),
            alpha_free=[str(F(float(v))) for v in alpha],
            beta_free=[str(F(float(v))) for v in beta],
            actual_completion='C999l(1): free raw indices2,...,511; raw p=0,1 is minus the parity sum of exact r_n times the free coefficient; all indices>=512 zero.',
            source_hashes=pins, selection_script_sha256=sha(Path(__file__)))
        # Exclusive creation fixes the point before any certification.
        with PAIR.open('x') as stream:
            stream.write(json.dumps(frozen, indent=2)+'\n')
    frozen = json.loads(PAIR.read_text())
    check('frozen pair original hashes agree', frozen['source_hashes'] == pins)
    check('exactly two complete510-coordinate vectors', len(frozen['alpha_free']) == len(frozen['beta_free']) == 510)
    alpha = vector_dyadics(frozen['alpha_free'])
    beta = vector_dyadics(frozen['beta_free'])
    na, nb = exact_norm_squared(alpha), exact_norm_squared(beta)
    ca = exact_bilinear(aa, alpha, alpha)
    cb = exact_bilinear(aa, beta, beta)
    ct = exact_bilinear(bb, beta, alpha)

    # C999l(6) covers precisely these stored centers, including exact-Z
    # conversion and product roundoff. The full two-orientation error also
    # bounds its first510-column restriction. No scalar roundoff remains.
    z, root2 = F('1.008'), F('1.414213562373096')
    check('rational sqrt2 upper', root2*root2 > 2)
    eta_a = F('.00024')*z*z+F('1e-7')
    eta_b = root2*z*z*512*F('2.1e-7')+F('1e-7')
    check('eta_A dominates audited saved upper', eta_a >= F(original['finite']['head_form_error']['hi']))
    check('eta_B dominates audited saved upper', eta_b >= F(original['finite']['forcing_error']['hi']))
    norm_product = sqrt_upper(na*nb)
    ra, rb, rt = eta_a*na, eta_a*nb, eta_b*norm_product
    ea, eb = interval(ca, ra), interval(cb, rb)
    ti = interval(ct, rt)
    check('actual energy lower bounds positive', F(ea['lo']) > 0 and F(eb['lo']) > 0)
    modulus_lower = max(F(0), abs(ct)-rt)
    modulus_upper = abs(ct)+rt
    lhs = modulus_lower**2
    required = F(3,4)*F(ea['hi'])*F(eb['hi'])
    ratio_lower = lhs/(F(ea['hi'])*F(eb['hi']))
    ratio_upper = modulus_upper**2/(F(ea['lo'])*F(eb['lo']))
    crossed = lhs > required
    result = dict(
        scope='One fixed exact-neutral N512 actual bilinear lower test; tau=1/4',
        classification='REPRODUCTION; local standard-method specialization, not a new general norm/spectral theorem',
        source_script_sha256=sha(Path(__file__)), input_hashes=pins,
        witness=dict(path=PAIR.name, sha256=sha(PAIR), free_dimension=510, raw_dimension=512),
        error_inputs=dict(z_upper=str(z), sqrt2_upper=str(root2), eta_A=str(eta_a), eta_B=str(eta_b)),
        exact_center_contractions=dict(alpha_norm_squared=str(na), beta_norm_squared=str(nb), energy_f=str(ca), energy_g=str(cb), pairing=str(ct)),
        actual_intervals=dict(energy_f=ea, energy_g=eb, pairing=ti, norm_product_upper=str(norm_product), energy_f_error=str(ra), energy_g_error=str(rb), pairing_error=str(rt)),
        strict_test=dict(pairing_modulus_squared_lower=str(lhs), required_three_quarters_energy_product_upper=str(required), strict_margin_lower=str(lhs-required), squared_ratio_lower=str(ratio_lower), squared_ratio_upper=str(ratio_upper), threshold='3/4', crossed=crossed),
        checks=checks, failures=[c['label'] for c in checks if not c['passed']],
        qualifications=['Inherited C744v/w analytic response and IEEE754/Decimal contracts; C744z whole neutral-core and unreplayed c_* qualification.', 'Exact analytical Z defines the actual vectors; dyadic free coefficients and complete centers alone enter the exact integer contractions.', 'No second pair search or tau/cutoff tuning. No upstream certificate replay.', 'No signed coupling, full S3, C744q/H2, higher/mixed/non-neutral endpoints or Xi transfer. New certificate awaits separate audit.'])
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print('Fixed pair frozen:', PAIR.relative_to(HERE.parent.parent), 'sha256='+sha(PAIR))
    for name, ii in [('a0(f,f)',ea), ('a0(g,g)',eb), ('<Tf,g>',ti)]:
        print(name+': ['+decimal_view(F(ii['lo']))+', '+decimal_view(F(ii['hi']))+']')
    print('Squared ratio enclosure: ['+decimal_view(ratio_lower)+', '+decimal_view(ratio_upper)+']; required >.75; crossed='+str(crossed))
    print('Squared pairing lower='+decimal_view(lhs)+'; required energy-product upper='+decimal_view(required)+'; strict margin='+decimal_view(lhs-required))
    print('Checks='+str(len(checks))+'; failures='+str(result['failures']))
    print('Full certificate:', OUT.relative_to(HERE.parent.parent))


if __name__ == '__main__':
    main()
