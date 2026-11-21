"""Audit saved1307 jets and1309 polynomial provenance, without a search.

Run the two existing replays first. This fills their explicitly recorded
provenance limits. L037's Decimal library contract remains assumed.
All input evidence is read only; full audit records are saved separately.
"""
import hashlib
import importlib.util
import json
from decimal import DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal
from fractions import Fraction as F
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
OUT = HERE / 'actual-sign-audit-1311.json'


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def main():
    paths = [HERE / name for name in (
        'actual-singleton-certificate-1307.json', 'actual-singleton-replay-1307.json',
        'actual-sign-certificate-1309.json', 'actual-sign-replay-1309.json')]
    singleton, replay7, source, replay9 = [json.loads(p.read_text()) for p in paths]
    report = {'status': 'running', 'failures': [], 'checks': {},
              'input_sha256': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in paths},
              'limits': 'No new quadrature parameters, sign cells, weights, higher degree or source search.',
              'assumptions': 'L036/L037 interval inclusion; documented Decimal correctness assumed.'}
    OUT.write_text(json.dumps(report, indent=2) + '\n')
    try:
        assert replay7['status'] == replay9['status'] == 'passed'
        assert not replay7['failures'] and not replay9['failures']
        assert replay7['source_sha256'] == report['input_sha256'][str(paths[0].relative_to(ROOT))]
        for saved in (singleton['input_sha256'], source['inputs'], replay9['input_sha256']):
            for name, digest in saved.items():
                assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
        producer_path = HERE.parent / 'heat/low-time-h2-uniform-195.py'
        rational_path = HERE.parent / 'heat/low-time-h1-uniform-180-check.py'
        producer = load_module('fixed_jet_audit1311', producer_path)
        rational = load_module('fraction_audit1311', rational_path)
        R = rational.R
        base = producer.base
        for path in (Path(__file__), producer_path, rational_path,
                     HERE.parent / 'hankel/certify_hankel.py'):
            report['input_sha256'][str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
        producer.SPATIAL_PANELS = 256
        producer.checks()
        pi = base.pi_bounds()
        assert pi.data() == singleton['pi']
        spatial, theta, total = producer.tilted_tail()
        assert {k: v.data() for k, v in zip(('spatial', 'theta', 'total'),
                                           (spatial, theta, total))} == singleton['tails']
        cached, weights, rw = producer.prepare(pi)
        assert len(cached) == len(singleton['panels']) == 256
        assert {str(k): v.data() for k, v in weights.items()} == singleton['weights']
        assert rw.data() == singleton['remainder_weight']
        jet_checks = []
        for index, ((center, domain, midpoint, rectangle), saved) in enumerate(zip(cached, singleton['panels'])):
            assert saved['index'] == index
            assert saved['center'] == center.data() and saved['domain'] == domain.data()
            assert set(saved['orders']) == {str(k) for k in producer.ORDERS}
            for k in producer.ORDERS:
                row = saved['orders'][str(k)]
                assert row['midpoint_even_coefficients'] == {
                    str(j): midpoint[k][j].data() for j in (0, 2, 4, 6)}
                assert row['full_eighth_coefficient'] == rectangle[k][8].data()
                jet_checks.append({'panel': index, 'order': k,
                                   'four_midpoint_and_full_eighth_match': True})
        signals = (DivisionByZero, InvalidOperation, Overflow, Underflow, Subnormal)
        arithmetic = {name: {'precision': ctx.prec, 'rounding': ctx.rounding,
                            'traps': {s.__name__: ctx.traps[s] for s in signals},
                            'exceptional_flags': {s.__name__: ctx.flags[s] for s in signals}}
                      for name, ctx in (('DOWN', base.DOWN), ('UP', base.UP), ('NEAR', base.NEAR))}
        assert arithmetic == singleton['arithmetic']
        assert all(ctx.prec == 100 and all(ctx.traps[s] and not ctx.flags[s] for s in signals)
                   for ctx in (base.DOWN, base.UP, base.NEAR))
        report['jet_checks'] = jet_checks
        report['arithmetic'] = arithmetic
        report['checks']['saved_jet_provenance'] = {'records': len(jet_checks),
                                                  'coefficient_intervals': 5 * len(jet_checks),
                                                  'all_match': True}

        def data(v):
            return {'lower': str(v.lo), 'upper': str(v.hi)}

        def add(p, q):
            return [(p[i] if i < len(p) else R(0)) + (q[i] if i < len(q) else R(0))
                    for i in range(max(len(p), len(q)))]

        def scale(p, c):
            return [a * c for a in p]

        def mul(p, q):
            return [sum((p[i] * q[k-i] for i in range(len(p)) if 0 <= k-i < len(q)), R(0))
                    for k in range(len(p) + len(q) - 1)]

        A, B, C, D, E = (R.read(source['parameters'][s]) for s in 'ABCDE')
        assert all(v.lo > 0 for v in (A, B, C, D, E))
        k = A / (2*C)
        l0, l1 = -E*k + B**2/(2*A), -E*k + E*B/D - B**2/(2*A)
        n0, n1 = A/3 - E*k**2, A/3 - 2*E*k**2
        constants = {'k': k, 'l0': l0, 'l1': l1, 'n0': n0, 'n1': n1}
        assert {s: data(v) for s, v in constants.items()} == source['constants']
        ell = [-l1, l0 + 2*l1]
        n = [n0, -4*n0-n1, 5*n0+2*n1]
        v = add(n, scale(mul([R(-1), R(3)], ell), -k))
        j = add(v, scale(mul([R(-1), R(2)], ell), -(B/D)))
        h = add(add(mul(n, j), scale(mul(mul([R(-1), R(2)], v), ell), -(C/E))),
                scale(mul(mul([R(1), R(-1)], n), ell), B**2/(2*A*E)))
        polynomials = {s: [data(c) for c in p] for s, p in
                       {'l': ell, 'n': n, 'v': v, 'j': j, 'h': h}.items()}
        assert polynomials == source['polynomials']
        report['reconstructed_polynomials'] = polynomials
        report['checks']['polynomial_provenance'] = {'coefficients': 16, 'all_match': True,
                                                   'formula': 'C030z(10); Fraction endpoints from outer boxes'}
        # These two saved closed cells alone exclude the analytic admissible range.
        selected = source['cells'][-2:]
        assert [r['z'] for r in selected] == [['1/4', '1/2'], ['1/2', '1']]
        bounds = []
        for row in selected:
            lrange, jrange = (R.read(row['ranges'][s]) for s in ('l', 'j'))
            assert lrange.hi < F('-3e-11') and jrange.lo > F('5e-7')
            assert row['signs']['l'] == -1 and row['signs']['j'] == 1
            bounds.append({'z': row['z'], 'l': data(lrange), 'j': data(jrange)})
        report['analytic_range_evidence'] = {'cells': bounds,
            'uniform_strict_bounds': {'l_upper': '-3/100000000000', 'j_lower': '1/2000000'},
            'required': 'For -1<=x<1, z=1/(2-x) lies in [1/3,1); J=j/(zl)>0 is necessary.',
            'result': 'l<0 and j>0 force J<0 on this entire range; no L=0 division.'}
        report['checks']['analytic_range_exclusion'] = True
        report['checks']['inherited_replays'] = {'1307': replay7['checks'], '1309': replay9['checks']}
        report['checks']['input_evidence_unchanged'] = all(
            hashlib.sha256(p.read_bytes()).hexdigest() == report['input_sha256'][str(p.relative_to(ROOT))]
            for p in paths)
        assert report['checks']['input_evidence_unchanged']
        report['status'] = 'passed'
    except Exception as error:
        report['status'] = 'failed'
        report['failures'].append({'type': type(error).__name__, 'message': str(error)})
        raise
    finally:
        OUT.write_text(json.dumps(report, indent=2) + '\n')
        print('STATUS:', report['status'], 'FAILURES:', report['failures'])
        print('CERTIFICATE:', OUT.relative_to(ROOT))
    print('PASS: 1792 jet records / 8960 coefficient intervals; 16 polynomial coefficients; inherited replays.')
    print('ACTUAL: l < -3e-11, j > 5e-7 on [1/4,1]; REQUIRED: J=j/(zl)>0; hence excluded.')


if __name__ == '__main__':
    main()
