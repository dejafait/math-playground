"""Check L053's manuscript spectra and strict endpoint against full reconstruction.

Run audit_global_triple_principal.py first for all records, minors and orbits.
This supplement imports neither constructor nor verifier routines.
"""
import hashlib
import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path

ROOT = Path(__file__).parent
SOURCE = ROOT / 'global-triple-principal-audit-results.json'
OUT = ROOT / 'global-triple-critical-audit-results.json'


def enc(x):
    return [x.numerator, x.denominator]


def main():
    raw = SOURCE.read_bytes()
    audit = json.loads(raw)
    lp = json.loads((ROOT / 'delsarte-lp-results.json').read_text())
    primal = [Q(z['numerator'], z['denominator']) for z in lp['exact']['primal']]
    p = [Q(1)] + [Q(0)] * 4 + [
        z / (2 * comb(68, i) * comb(956, i))
        for i, z in zip(range(5, 69), primal)]
    U = Q(comb(1024, 64), comb(68, 64))
    M = (U + 1) / 2
    tau = Q(65537**28, 2**128)
    T = tau.numerator // tau.denominator + 1
    floor_M = M.numerator // M.denominator
    expected = [M] + [Q(1, 2)] * 64 + [
        Q(30789161673, 26556181345), Q(787342157, 801136197),
        Q(478922161, 478531017), Q(476380573, 476387541)]
    checks = []

    def check(name, truth):
        checks.append({'name': name, 'passed': bool(truth)})

    check('complete_prior_reconstruction', audit['verified']
          and audit['failures'] == [] and audit['total_checks'] == 1934857
          and audit['check_counts']['original_orbit_map'] == 1500625
          and audit['check_counts']['full_minor_identities'] == 83931
          and audit['check_counts']['full_minor_signs'] == 83931
          and audit['counts']['stored_principal_minors'] == 586967)
    check('all_69_manuscript_spectra', audit['spectra_over_rho'] == list(map(enc, expected)))
    check('strict_pair_spectra', all(x > 0 for x in expected))
    check('boolean_pair_range', len(p) == 69 and all(0 <= x <= 1 for x in p))
    check('objective_from_every_pair', sum(comb(68, i) * comb(956, i) * p[i]
                                         for i in range(69)) == M)
    check('saved_objective_and_endpoint', audit['objective'] == enc(M) and audit['T'] == T)
    check('constant_schur_zero', audit['constant_schur_over_rho'] == [0, 1])
    check('true_integer_endpoint', T - 1 <= tau < T)
    check('strict_ratio_interval', Q(1383, 1000) < M / tau < Q(1384, 1000))
    check('floor_nonexclusion', floor_M >= T)
    margins = {'lower_ratio': enc(1000 * M - 1383 * tau),
               'upper_ratio': enc(1384 * tau - 1000 * M),
               'floor_above_T': floor_M - T}
    failures = [c['name'] for c in checks if not c['passed']]
    result = {'source': SOURCE.name, 'source_sha256': hashlib.sha256(raw).hexdigest(),
              'checks': checks, 'spectra': list(map(enc, expected)),
              'objective': enc(M), 'tau': enc(tau), 'T': T, 'floor_objective': floor_M,
              'strict_comparison_margins': margins, 'failures': failures,
              'verified': not failures}
    OUT.write_text(json.dumps(result, indent=2) + '\n')
    print('Manuscript checks:', len(checks), '; spectra: 69/69; failures:', failures)
    print('Objective floor:', floor_M, '; useful bound required <', T)
    print('Ratio: 1383/1000 < M/tau < 1384/1000; certificate:', OUT)
    assert not failures


if __name__ == '__main__':
    main()
