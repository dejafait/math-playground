#!/usr/bin/env python3
"""BSD-170: distinct exact endpoint checks and bounded evidence rejection tests.

This is a fixed audit, not a replacement producer. Original files are read-only.
Exact Horner polynomials have no intermediate rounding. Only their final
Taylor/Lipschitz brackets are rounded, at 160 bits, for compact certificates.
"""
import copy
import json
import subprocess
import sys
from fractions import Fraction as F
from hashlib import sha256
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'audit_cases'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def bracket(lo, hi, bits=160):
    scale = 2**bits
    return [(lo*scale).__floor__(), -((-hi*scale).__floor__())]


def horner(x, coefficients):
    result = F(0)
    for c in reversed(coefficients):
        result = result*x+c
    return result


def endpoint_checks(data):
    den = 2**96
    phases = {F(row['phase']): row for row in data['phases']}
    # Include actual half-open boundary, zero, both signs, near-zero phases.
    selected = {min(phases), max(phases), F(0)}
    for target in (F(-1,4), F(1,4)):
        selected.add(min(phases, key=lambda x: abs(x-target)))
    selected.add(min(x for x in phases if x > 0))
    selected.add(max(x for x in phases if x < 0))
    records = []
    for phase in sorted(selected):
        row = phases[phase]
        lo, hi = (F(v, den) for v in row['theta'])
        center, error = (lo+hi)/2, (hi-lo)/2
        assert abs(center) <= 4
        # Degree 120 real Taylor polynomial; derivative bound one everywhere.
        polynomial = horner(center*center,
                            [F((-1)**k, factorial(2*k)) for k in range(61)])
        remainder = F(4**121, factorial(121))
        independent = bracket(polynomial-remainder-error, polynomial+remainder+error)
        outer = [v*2**64 for v in row['cosine']]
        assert outer[0] <= independent[0] <= independent[1] <= outer[1]
        records.append({'kind': 'cosine', 'phase': str(phase),
                        'center': str(center), 'input_radius': str(error),
                        'degree': 120, 'remainder': str(remainder),
                        'bits': 160, 'independent_interval': independent,
                        'saved_interval_at_160_bits': outer, 'included': True})
    for row in data['dampings']:
        lo, hi = (F(v, den) for v in row['w'])
        assert -8 <= lo <= hi < 0
        center, error = (lo+hi)/2, (hi-lo)/2
        # All intervening arguments are nonpositive: every exp derivative <= 1.
        polynomial = horner(center, [F(1, factorial(k)) for k in range(201)])
        remainder = F(8**201, factorial(201))
        independent = bracket(polynomial-remainder-error, polynomial+remainder+error)
        outer = [v*2**64 for v in row['q']]
        assert 0 < outer[0] <= independent[0] <= independent[1] <= outer[1] < 2**160
        records.append({'kind': 'damping', 'y': row['y'],
                        'center': str(center), 'input_radius': str(error),
                        'degree': 200, 'remainder': str(remainder),
                        'bits': 160, 'independent_interval': independent,
                        'saved_interval_at_160_bits': outer, 'included': True})
    # Independently check complete signed assembly using exact Fraction endpoints,
    # with no intermediate rounding; rounding only at the final quotient.
    integral = [F(0), F(0)]
    for row in data['transports']:
        i, j = row['primitive_ids']
        left = data['primitives'][i]['enclosure']
        right = data['primitives'][j]['enclosure']
        integral[0] += F(right[0]-left[1], den*data['h'])
        integral[1] += F(right[1]-left[0], den*data['h'])
    period = [F(v, den) for v in data['period']['total']]
    assert period[0] > 0
    quotients = [x/y for x in integral for y in period]
    normalized = bracket(min(quotients), max(quotients), 96)
    saved = data['result']['normalized']
    assert saved[0] <= normalized[0] <= normalized[1] <= saved[1]
    width = F(saved[1]-saved[0], den)
    assert width < F(1, 2**38) < F(1, 2**20)
    assert [row['p'] for row in data['arithmetic']['tate']] == [2, 3]
    c_zero = [i for i, row in enumerate(data['transports']) if row['matrix'][2] == 0]
    assert c_zero
    return {'passed': True, 'cosine_cases': len(selected),
            'damping_cases': len(data['dampings']), 'cases': records,
            'C_zero_transport_indices': c_zero,
            'exact_closing_integral': [str(x) for x in integral],
            'single_rounding_normalized': normalized, 'saved_normalized': saved,
            'width': str(width), 'required_width': '1/1048576'}


def change(data, name):
    if name == 'input_binding':
        data['input_certificate_sha256'] = '0'*64
    elif name == 'cosine_remainder':
        data['phases'][0]['remainder'] = '0'
    elif name == 'damping_endpoint':
        data['dampings'][0]['q'][1] -= 1
    elif name == 'finite_sum':
        data['primitives'][0]['finite_sum'][0] += 1
    elif name == 'full_tail':
        data['primitives'][0]['tail_radius'] = 0
    elif name == 'signed_division':
        data['result']['normalized'][0] += 1
    else:
        raise ValueError(name)


def main():
    OUT.mkdir(exist_ok=True)
    originals = [HERE/name for name in ('certificate.json', 'verification.json',
                  'diagnosis.json', 'reduced_phase_certificate.json',
                  'reduced_phase_verification.json')]
    before = {p.name: digest(p) for p in originals}
    data = json.loads((HERE/'reduced_phase_certificate.json').read_text())
    report = {'passed': False, 'original_sha256_before': before, 'rejections': []}
    destination = HERE/'audit_discriminating_checks.json'
    try:
        report['independent_checks'] = endpoint_checks(data)
        destination.write_text(json.dumps(report, indent=2)+'\n')
        print('independent inclusion PASS; cosine cases=', report['independent_checks']['cosine_cases'],
              'damping cases=', report['independent_checks']['damping_cases'], flush=True)
        for name in ('input_binding', 'cosine_remainder', 'damping_endpoint',
                     'finite_sum', 'full_tail', 'signed_division'):
            altered = copy.deepcopy(data)
            change(altered, name)
            path, result = OUT/(name+'.json'), OUT/(name+'_report.json')
            path.write_text(json.dumps(altered, separators=(',', ':'))+'\n')
            # Exercise CLI persistence, replacing a stale passing report.
            result.write_text('{"passed": true, "sentinel": "stale"}\n')
            proc = subprocess.run([sys.executable, str(HERE/'verify_reduced_phase.py'),
                                   str(path), str(result)], capture_output=True, text=True)
            persisted = json.loads(result.read_text())
            assert proc.returncode == 1 and persisted['passed'] is False
            assert 'sentinel' not in persisted and persisted.get('failure')
            report['rejections'].append({'case': name, 'returncode': proc.returncode,
                'certificate': str(path.relative_to(HERE)), 'sha256': digest(path),
                'report': str(result.relative_to(HERE)), 'failure': persisted['failure'],
                'fresh_failure_persisted': True})
            destination.write_text(json.dumps(report, indent=2)+'\n')
            print('altered evidence rejected:', name, 'report=', result, flush=True)
        after = {p.name: digest(p) for p in originals}
        report['original_sha256_after'] = after
        assert before == after
        report['passed'] = True
    except Exception as exc:
        import traceback
        report['failure'] = repr(exc)
        report['traceback'] = traceback.format_exc()
    destination.write_text(json.dumps(report, indent=2)+'\n')
    independent = report.get('independent_checks', {})
    print('audit', 'PASS' if report['passed'] else 'FAIL',
          'width=', independent.get('width'), 'required <', independent.get('required_width'),
          'failure=', report.get('failure'), 'report=', destination)
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
