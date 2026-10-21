#!/usr/bin/env python3
"""Bounded sensitivity checks. Synthetic bundles are not arithmetic instances.
Only the independent checker is called for rejection. Producer use is confined
to synthetic witness generation. Real structural evidence is replayed once in
full here, and fresh again by the standalone substantive verifier.
"""
import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('.', '_'), ROOT/filename)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    verifier = module('verify_certificate.py')
    producer = module('build_certificate.py')
    sr = Path('scripts/relative-t2/certificate.json').read_bytes()
    abr = (ROOT/'conductor389-arithmetic.json').read_bytes()
    ar, structural = json.loads(abr), json.loads(sr)
    certificate = json.loads((ROOT/'conductor389-certificate.json').read_bytes())
    bundle = verifier.structural(verifier.Check(), structural, sr, 'L030-fixed-v1', ar, ROOT/'sensitivity-structure')
    cases = {}

    def case(name, change):
        cert = copy.deepcopy(certificate)
        change(cert)
        cases[name] = cert

    case('structural_hash_binding', lambda c: c['bindings'].__setitem__('structural_sha256', '0'*64))
    case('arithmetic_hash_binding', lambda c: c['bindings'].__setitem__('arithmetic_sha256', '0'*64))
    case('arithmetic_trace_binding', lambda c: c['arithmetic']['traces'][0].__setitem__('trace', 0))
    case('missing_full_block', lambda c: c['B']['entries'].__delitem__(slice(65, None)))
    case('wrong_transpose', lambda c: c['B'].__setitem__('entries',
         [[str(structural['matrices']['J'][i][j]-int(i == j)) for j in range(65)] for i in range(65)]+c['B']['entries'][65:]))
    case('wrong_geometric_sign', lambda c: c['B'].__setitem__('entries',
         [[str(-structural['matrices']['J'][j][i]-int(i == j)) for j in range(65)] for i in range(65)]+c['B']['entries'][65:]))
    case('zero_nullvector', lambda c: c['line'].__setitem__('v', ['0']*65))
    case('wrong_nullvector', lambda c: c['line']['v'].__setitem__(0, str(verifier.Fraction(c['line']['v'][0])+1)))
    case('zero_minor_claim', lambda c: c['line']['minor'].__setitem__('determinant', '0'))
    case('wrong_nonzero_minor_claim', lambda c: c['line']['minor'].__setitem__('determinant', '1'))
    case('malformed_minor_shape', lambda c: c['line']['minor']['matrix'].__setitem__('cols', 63))
    case('duplicate_minor_row', lambda c: c['line']['minor']['row_indices'].__setitem__(1, c['line']['minor']['row_indices'][0]))
    case('out_of_range_operation', lambda c: c['row_operations'].__setitem__(0, ['swap', 0, 130]))
    case('noninvertible_operation', lambda c: c['row_operations'].__setitem__(0, ['scale', 0, '0']))
    case('noncanonical_rational', lambda c: c['B']['entries'][0].__setitem__(0, '0/2'))
    case('wrong_generator_value', lambda c: c['generator_values']['entries'][0].__setitem__(0, '10000'))
    outcomes, failures = {}, []
    for name, c in cases.items():
        try:
            verifier.linear(verifier.Check(), c, bundle, ar, sr, abr)
        except Exception as error:
            outcomes[name] = {'rejected': True, 'failure': type(error).__name__+': '+str(error)}
        else:
            outcomes[name] = {'rejected': False}
            failures.append(name)
    for name, change in [
        ('duplicate_trace', lambda a: a['traces'].append(copy.deepcopy(a['traces'][0]))),
        ('missing_trace', lambda a: a.__setitem__('traces', [])),
        ('nonprime_trace', lambda a: a['traces'][0].__setitem__('prime', 4)),
        ('bad_prime_at_level', lambda a: a['traces'][0].__setitem__('prime', 389)),
        ('unsupported_arithmetic_claim', lambda a: a.__setitem__('certification', 'BSD_PROVED')),
        ('singular_equation', lambda a: a.__setitem__('model', [0, 0, 0, 0, 0]))]:
        a = copy.deepcopy(ar)
        change(a)
        try:
            verifier.arithmetic(verifier.Check(), a)
        except Exception as error:
            outcomes[name] = {'rejected': True, 'failure': type(error).__name__+': '+str(error)}
        else:
            outcomes[name] = {'rejected': False}
            failures.append(name)

    # Direct core shape/rank fixtures bypass structural and arithmetic claims.
    # Never passed off as verified elliptic inputs; standalone verify() has no
    # synthetic adapter and always replays a recognized complete structure.
    fixtures = {}
    for name, d, jmat, expected_rank, expected_nullity in [
        ('empty_domain', 0, [], 0, 0),
        ('empty_minor_dimension_one', 1, [[1]], 0, 1),
        ('larger_kernel', 2, [[1, 0], [0, 1]], 0, 2),
        ('nullity_zero', 1, [[-1]], 1, 0)]:
        coords = [[int(i == k) for k in range(d)] for i in range(d)]
        fixture_structural = {'presentation': {'d': d, 's': d, 'generator_coordinates': coords},
                              'operators': {'J': {'B': {'entries': jmat}}}}
        fixture_ar = {'certification': 'SUPPLIED_CONDITIONAL', 'traces': []}
        fsr, far = json.dumps(fixture_structural).encode(), json.dumps(fixture_ar).encode()
        c = producer.build(fixture_structural, fixture_ar, 'L038-relative-v1')
        c['bindings'] = {'structural_sha256': verifier.digest(fsr), 'arithmetic_sha256': verifier.digest(far)}
        fixture_bundle = {'d': d, 's': d, 'P': [], 'traces': [], 'matrices': {'J': jmat},
                          'coords': coords, 'relations': [], 'saturated': []}
        try:
            summary = verifier.linear(verifier.Check(), c, fixture_bundle, fixture_ar, fsr, far)
            if (summary['rank'], summary['nullity']) != (expected_rank, expected_nullity):
                raise ValueError('unexpected actual/required fixture dimensions')
            fixtures[name] = {'kind': 'SYNTHETIC_CORE_ONLY', 'actual': summary,
                              'required': {'rank': expected_rank, 'nullity': expected_nullity}}
        except Exception as error:
            failures.append(name)
            fixtures[name] = {'failure': str(error)}
    report = {'real_structural_sha256': verifier.digest(sr),
              'checks': outcomes, 'synthetic_fixtures': fixtures, 'failures': failures,
              'required_rejections': len(cases)+6, 'actual_rejections': sum(x['rejected'] for x in outcomes.values()),
              'qualification': 'Finite sensitivity evidence, not a universal checker soundness or elliptic realization theorem.'}
    output = ROOT/'rejection-checks.json'
    output.write_text(json.dumps(report, indent=2)+'\n')
    print('rejections actual/required', report['actual_rejections'], '/', report['required_rejections'],
          '; synthetic fixtures actual/required', len(fixtures), '/4; failures', failures, '; report', output)
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
