#!/usr/bin/env python3
"""Independent full Fraction replay of the frozen C998r certificate.

Reads original artifacts; never imports or executes the proposal/certifier.
No upstream analytic or c_star replay. No pair, cutoff or tau search.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import numpy as np

BASE = Path(__file__).resolve().parent
OUT = BASE / 'defect-window-fixed-pair-audit-709.json'
checks, failures, evidence = [], [], {}


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def check(label, condition):
    passed = bool(condition)
    checks.append(dict(label=label, passed=passed))
    if not passed:
        failures.append(label)


def read(name):
    return json.loads((BASE / name).read_text())


def contract(matrix, left, right):
    # Different arithmetic organization from707: reduce each scalar and
    # row as a Fraction, without its whole-matrix common denominator.
    assert matrix.shape == (len(left), len(right))
    return sum((li * sum((Q(float(entry)) * rj
                         for entry, rj in zip(row, right)), Q())
                for li, row in zip(left, matrix)), Q())


def main():
    saved = read('defect-window-fixed-pair-707.json')
    pair_name = 'defect-window-fixed-pair-707-witness.json'
    frozen = read(pair_name)
    original = read('neutral-head-covariance-559.json')
    audit561 = read('neutral-head-covariance-audit-561.json')
    audit534 = read('certificate-audit-534.json')
    text_bounds = read('defect-window-text-bounds-707.json')
    check('frozen witness published SHA256', digest(BASE / pair_name) ==
          '99ebc79ed3d82771ad0b5567356ba953e0d123d86aecdfe07d8e57f6fb9c634a')
    check('707 script hash', digest(BASE / 'defect-window-fixed-pair-707.py') == saved['source_script_sha256'])
    check('selection script unchanged', frozen['selection_script_sha256'] == saved['source_script_sha256'])
    pins = {name: digest(BASE / name) for name in saved['input_hashes']}
    check('full707 input hash dictionary', pins == saved['input_hashes'])
    check('full witness input hash dictionary', pins == frozen['source_hashes'])
    check('all561 audited input hashes', all(digest(BASE / name) == h
          for name, h in audit561['original_hashes'].items()))
    check('all559 original input hashes', all(digest(BASE / name) == h
          for name, h in original['input_hashes'].items()))
    check('raw archive original534 identity', pins['complete-covariance-532.npz'] ==
          audit534['original_sha256']['complete-covariance-532.npz'] ==
          '33dbfa73fec9980e5d51d5142d2c167421bbbcebb6ed2a2b4edd3a864bfda402')
    check('saved neutral archive identity', pins['neutral-head-covariance-559.npz'] ==
          original['binary_artifact']['sha256'] ==
          'f9e5288f6bc3465f690fca70d1a71537c4df5b405029e9785cd9706a9c0dcf6a')
    for name, artifact in [('559', original), ('561', audit561), ('707', saved)]:
        check('all inherited recorded checks ' + name,
              bool(artifact['checks']) and not artifact['failures'] and
              all(c['passed'] for c in artifact['checks']))
    check('534 recorded failures empty', not audit534['failures'])
    check('witness metadata dimensions and path', saved['witness'] == dict(
          path=pair_name, sha256=digest(BASE / pair_name), free_dimension=510, raw_dimension=512))

    alpha = [Q(s) for s in frozen['alpha_free']]
    beta = [Q(s) for s in frozen['beta_free']]
    check('all1020 coordinates exact dyadics', len(alpha) == len(beta) == 510 and
          all(q.denominator & (q.denominator - 1) == 0 for q in alpha + beta))
    with np.load(BASE / 'neutral-head-covariance-559.npz', allow_pickle=False) as data:
        aa = data['a'].copy()
        bfull = data['b'].copy()
    check('full saved centers binary64 shapes and finiteness',
          aa.shape == (510, 510) and bfull.shape == (510, 1020) and
          aa.dtype == bfull.dtype == np.dtype('float64') and
          np.isfinite(aa).all() and np.isfinite(bfull).all())
    na = sum((q*q for q in alpha), Q())
    nb = sum((q*q for q in beta), Q())
    cf = contract(aa, alpha, alpha)
    cg = contract(aa, beta, beta)
    ct = contract(bfull[:, :510], beta, alpha)
    center_values = dict(alpha_norm_squared=na, beta_norm_squared=nb,
                         energy_f=cf, energy_g=cg, pairing=ct)
    for key, value in center_values.items():
        check('full independent exact contraction ' + key,
              value == Q(saved['exact_center_contractions'][key]))
    check('both independent free vectors nonzero', na > 0 and nb > 0)

    z, s = Q('1.008'), Q('1.414213562373096')
    ea = Q('.00024') * z*z + Q('1e-7')
    eb = s*z*z*512*Q('2.1e-7') + Q('1e-7')
    check('sqrt2 rational strict upper', s > 0 and s*s > 2)
    check('saved error input dictionary', saved['error_inputs'] == dict(
          z_upper=str(z), sqrt2_upper=str(s), eta_A=str(ea), eta_B=str(eb)))
    check('eta_A covers audited complete saved-center error',
          ea >= Q(original['finite']['head_form_error']['hi']))
    check('eta_B covers audited full two-orientation error',
          eb >= Q(original['finite']['forcing_error']['hi']))
    ints = saved['actual_intervals']
    h = Q(ints['norm_product_upper'])
    q = na*nb
    scale = 10**80
    expected_h = Q(isqrt((q.numerator * scale*scale)//q.denominator)+1, scale)
    check('saved product norm upper formula', h == expected_h)
    check('product norm upper exact square test', h > 0 and h*h > q)
    rf, rg, rt = ea*na, ea*nb, eb*h
    intervals = dict(energy_f=dict(lo=str(cf-rf), hi=str(cf+rf)),
                     energy_g=dict(lo=str(cg-rg), hi=str(cg+rg)),
                     pairing=dict(lo=str(ct-rt), hi=str(ct+rt)),
                     norm_product_upper=str(h), energy_f_error=str(rf),
                     energy_g_error=str(rg), pairing_error=str(rt))
    check('every saved interval and individual error charge', ints == intervals)
    fl, fh, gl, gh = cf-rf, cf+rf, cg-rg, cg+rg
    tl, th = ct-rt, ct+rt
    check('positive actual energies', fl > 0 and gl > 0)
    check('both displayed energy bounds', Q('.9998') < fl <= fh < Q('1.0002') and
          Q('.9998') < gl <= gh < Q('1.0002'))
    check('positive pairing exceeds displayed lower bound', tl > Q('.9216'))
    lhs = max(Q(), abs(ct)-rt)**2
    required = Q(3, 4)*fh*gh
    ratio = lhs/(fh*gh)
    ratio_hi = (abs(ct)+rt)**2/(fl*gl)
    strict_values = dict(pairing_modulus_squared_lower=lhs,
                         required_three_quarters_energy_product_upper=required,
                         strict_margin_lower=lhs-required,
                         squared_ratio_lower=ratio, squared_ratio_upper=ratio_hi)
    for key, value in strict_values.items():
        check('strict ledger exact identity ' + key, value == Q(saved['strict_test'][key]))
    check('strict3/4 comparison independently survives', lhs > required and
          saved['strict_test']['crossed'] and Q(saved['strict_test']['threshold']) == Q(3,4))
    check('full ratio lower exceeds .8491291032', ratio > Q('.8491291032'))
    check('strict margin exceeds .0991660679', lhs-required > Q('.0991660679'))
    check('simple outward proof comparison', Q('.9216')**2 == Q('.84934656') >
          Q('.75030003') == Q(3,4)*Q('1.0002')**2)
    check('text certificate exact comparison', text_bounds['exact_comparison'] == dict(
          pairing_square_lower=str(Q('.9216')**2), required_upper=str(Q(3,4)*Q('1.0002')**2)))
    check('all five text checks independently agree', not text_bounds['failures'] and
          len(text_bounds['checks']) == 5 and all(text_bounds['checks'].values()))
    # Mathematical implications are checked in canonical C998r audit709,
    # not encoded as a machine-verified spectral theorem.
    evidence.update(input_hashes=pins,
                    center_contractions={k:str(v) for k,v in center_values.items()},
                    actual_intervals=intervals,
                    strict_values={k:str(v) for k,v in strict_values.items()},
                    witness_sha256=digest(BASE / pair_name),
                    full_matrix_contraction_terms=3*510*510,
                    coordinate_count=len(alpha)+len(beta))


try:
    main()
except Exception as exc:
    failures.append(type(exc).__name__ + ': ' + str(exc))
result = dict(scope='Independent arithmetic audit of only frozen C998r pair; N512/tau1/4',
              source_script_sha256=digest(Path(__file__)), checks=checks,
              failures=failures, evidence=evidence,
              qualifications=['Analytic response, neutral-core, IEEE754/Decimal and unreplayed c_star remain inherited contracts.',
                              'No upstream archive regeneration or c_star replay; no second pair or parameter tuning.',
                              'Actual energy-domain and both spectral implications are prose audit items in C998r; no signed coupling/S3/H2/Xi transfer.'])
OUT.write_text(json.dumps(result, indent=2) + '\n')
print('Independent exact Fraction audit:', len(checks), 'checks; failures:', failures)
if evidence:
    v = evidence['strict_values']
    print('Actual squared-ratio lower:', format(float(Q(v['squared_ratio_lower'])), '.15g'), '; required >0.75')
    print('Squared pairing lower:', format(float(Q(v['pairing_modulus_squared_lower'])), '.15g'),
          '; required:', format(float(Q(v['required_three_quarters_energy_product_upper'])), '.15g'))
    print('Strict margin:', format(float(Q(v['strict_margin_lower'])), '.15g'))
print('Full certificate:', OUT.relative_to(BASE.parent.parent))
if failures:
    raise SystemExit(1)
