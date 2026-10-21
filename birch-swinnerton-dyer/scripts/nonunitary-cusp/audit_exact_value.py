#!/usr/bin/env python3
"""BSD-174: fixed L052 audit; preserve all production evidence.

The published geometry and audited L051 containment are imported, not
proved by this finite script. Replay imports only the separate verifier.
Independent tests use Euler characters and integer cross multiplication.
"""
import copy
import json
import traceback
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path

from verify_exact_value import replay

HERE = Path(__file__).resolve().parent
CASE_DIR = HERE / 'exact_audit_cases'
REPORT = HERE / 'exact_audit_checks.json'


def save(path, data):
    path.write_text(json.dumps(data, indent=2) + '\n')


def main():
    names = ['certificate.json', 'verification.json', 'diagnosis.json',
             'reduced_phase_certificate.json', 'reduced_phase_verification.json',
             'audit_full_replay.json', 'audit_discriminating_checks.json',
             'exact_value_certificate.json', 'exact_value_verification.json',
             'recover_exact_value.py', 'verify_exact_value.py']
    before = {name: sha256((HERE / name).read_bytes()).hexdigest() for name in names}
    data = json.loads((HERE / 'exact_value_certificate.json').read_bytes())
    report = {'passed': False, 'failures': [], 'preservation_before': before}
    try:
        full = replay(data)
        full['certificate_sha256'] = before['exact_value_certificate.json']
        assert json.loads((HERE / 'exact_value_verification.json').read_bytes()) == full
        save(HERE / 'exact_audit_full_replay.json', full)
        report['full_replay'] = full

        # Independent recount: Euler's criterion, not y enumeration/histograms.
        counts = []
        for p in (7, 13):
            weights = []
            for x in range(p):
                rhs = (x*x*x + 1) % p
                euler = pow(rhs, (p-1)//2, p)
                assert euler in (0, 1, p-1)
                weights.append(0 if euler == 0 else 1 if euler == 1 else -1)
            total = p + 1 + sum(weights)
            assert total == next(r['total'] for r in data['point_counts'] if r['p'] == p)
            counts.append({'p': p, 'quadratic_characters': weights, 'total': total})
        report['independent_counts'] = counts

        # Coarse containing interval fixed without reference to the answer.
        # All tests below are integer cross products, including endpoint inclusion.
        D = data['scale']
        lo, hi = data['interval_numerators']
        A, B, H = -83333334, -83333333, 10**9
        K = data['clearing_integer']
        inclusion = [lo*H-A*D, B*D-hi*H]
        assert min(inclusion) > 0
        # Strict scaled inequalities -3 < K*A/H < -2 < K*B/H < -1.
        gaps = [K*A+3*H, -2*H-K*A, K*B+2*H, -H-K*B]
        assert min(gaps) > 0
        rows, survivors = [], []
        for q in range(1, K+1):
            hits = [a for a in range(-q, 1) if A*q <= H*a <= B*q
                    and Q(a, q).denominator == q]
            rows.append({'q': q, 'numerators': hits})
            survivors.extend(str(Q(a, q)) for a in hits)
        assert survivors == data['result']['candidates'] and len(survivors) == 1
        report['independent_isolation'] = {
            'interval': [str(Q(A,H)), str(Q(B,H))],
            'input_inclusion_integer_gaps': inclusion,
            'scaled_neighbor_integer_gaps': gaps,
            'all_denominator_rows': rows, 'candidates': survivors,
            'actual_width': str(Q(B-A,H)), 'lattice_spacing': str(Q(1,K)),
            'required_candidate_count': 1, 'candidate_count': len(survivors)}

        CASE_DIR.mkdir(exist_ok=True)
        mutations = [
            ('input_binding', ('input_certificate_sha256',), '0'*64),
            ('differential_scalar', ('absolute_differential_scalar',), 2),
            ('orientation', ('path',), ['infinity', '1/6']),
            ('splitting', ('point_counts', 0, 'cyclotomic_roots'), [3, 4]),
            ('missing_point', ('point_counts', 1, 'entries', 2, 'ys'), [3]),
            ('clearing_factor', ('clearing_integer',), 12),
            ('interval_endpoint', ('interval_numerators', 0), lo+1),
            ('missing_denominator', ('enumeration',), data['enumeration'][:-1]),
            ('nonreduced_numerator', ('enumeration', 23, 'reduced_numerators'), [-2]),
            ('wrong_value', ('result', 'recovered'), '1/12'),
        ]
        cases = []
        for name, keys, value in mutations:
            altered = copy.deepcopy(data)
            node = altered
            for key in keys[:-1]:
                node = node[key]
            node[keys[-1]] = value
            case_path = CASE_DIR / (name + '.json')
            save(case_path, altered)
            try:
                replay(json.loads(case_path.read_bytes()))
                outcome = {'rejected': False, 'failure': 'altered evidence accepted'}
            except AssertionError:
                outcome = {'rejected': True, 'traceback': traceback.format_exc()}
            save(CASE_DIR / (name + '_report.json'), outcome)
            cases.append({'name': name, 'field': list(keys),
                          'rejected': outcome['rejected'],
                          'certificate': str(case_path.relative_to(HERE))})
        report['altered_evidence'] = cases
        assert all(c['rejected'] for c in cases)
        report['passed'] = True
    except Exception:
        report['failures'].append(traceback.format_exc())
    finally:
        after = {name: sha256((HERE / name).read_bytes()).hexdigest() for name in names}
        report['preservation_after'] = after
        report['original_bytes_preserved'] = before == after
        if before != after:
            report['passed'] = False
            report['failures'].append('original evidence changed')
        save(REPORT, report)
    print(json.dumps({'passed': report['passed'],
                      'full_replay': 'scripts/nonunitary-cusp/exact_audit_full_replay.json',
                      'report': 'scripts/nonunitary-cusp/exact_audit_checks.json',
                      'actual_candidates': report.get('independent_isolation', {}).get('candidate_count'),
                      'required_candidates': 1,
                      'actual_outer_width': report.get('independent_isolation', {}).get('actual_width'),
                      'lattice_spacing': report.get('independent_isolation', {}).get('lattice_spacing'),
                      'rejected_cases': sum(c['rejected'] for c in report.get('altered_evidence', [])),
                      'required_rejections': 10,
                      'original_bytes_preserved': report['original_bytes_preserved'],
                      'failures': report['failures']}))
    return report['passed']


if __name__ == '__main__':
    raise SystemExit(0 if main() else 1)
