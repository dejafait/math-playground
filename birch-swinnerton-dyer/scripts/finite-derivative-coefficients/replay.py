#!/usr/bin/env python3
"""One bounded exact replay of L031's fixed coefficient evidence; no kernels."""
import hashlib
import json
from math import isqrt
from pathlib import Path
import signal
import time

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
EXPECTED = '7547b371d675441190256195270c9282213e888cdb666451ae21a062896e4415'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    start = time.monotonic()
    def timeout(*_):
        raise TimeoutError('170-second work deadline; 10 seconds reserved for finalization')
    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(170)
    report = {'failures': [], 'required_seconds': 180,
              'required_new_bytes': 134217728, 'external_theorems_verified': False}
    try:
        fixed = sorted(set(
            [p for folder in ('scripts/twist-five', 'scripts/first-rational-kernel')
             for p in (ROOT/folder).rglob('*') if p.is_file()]
            + [p for pattern in ('lemmas/L030-*.md', 'lemmas/L031-*.md',
                                 'lemmas/L101-*.md', 'lemmas/L103-*.md')
               for p in ROOT.glob(pattern)]))
        before = {str(p.relative_to(ROOT)): digest(p) for p in fixed}
        path = ROOT/'scripts/twist-five/certificate.json'
        assert digest(path) == EXPECTED, 'upstream certificate hash'
        cert = json.loads(path.read_text())
        assert cert['selected_attempt'] == 0 and len(cert['attempts']) == 1
        data = cert['attempts'][0]
        assert data['T'] == 256
        inputs = data['source_inputs']
        assert inputs['model'] == [0, 1, 1, -2, 0]
        assert inputs['N'] == inputs['Delta'] == 389
        def prime(p):
            return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))
        primes = [p for p in range(2, 257) if prime(p)]
        assert [r['p'] for r in data['point_counts']] == primes
        assert data['nodal_count']['p'] == 389
        counts = []
        for row in data['point_counts'] + [data['nodal_count']]:
            p = row['p']
            fibers = []
            pairs = []
            for x in range(p):
                ys = [y for y in range(p)
                      if (y*y+y-x*x*x-x*x+2*x) % p == 0]
                fibers.append(len(ys))
                if p == 2:
                    pairs.extend([[x, y] for y in ys])
            if p == 2:
                assert pairs == row['pairs'], 'p=2 pairs'
            else:
                assert [n-1 for n in fibers] == row['discriminant_characters'], p
            affine = sum(fibers)
            assert (affine, affine+1, p-affine) == (row['affine'], row['total'], row['a_p']), p
            counts.append({'p': p, 'fiber_counts': fibers,
                           'affine': affine, 'total': affine+1, 'a_p': p-affine,
                           'pairs_at_two': pairs if p == 2 else None})
        assert counts[-1]['a_p'] == 1
        ap = {r['p']: r['a_p'] for r in counts[:-1]}
        coefficients = [0, 1]
        records = []
        for n in range(2, 257):
            residual, value, factors = n, 1, []
            for p in primes:
                if residual % p:
                    continue
                exponent = 0
                while residual % p == 0:
                    exponent += 1
                    residual //= p
                terms = [1, ap[p]]
                for k in range(2, exponent+1):
                    assert p < 389
                    terms.append(ap[p]*terms[k-1]-p*terms[k-2])
                factors.append([p, exponent, terms])
                value *= terms[-1]
            assert residual == 1, ('residual factor', n)
            record = [n, factors]
            assert record == data['factorizations_and_prime_powers'][n-2], n
            assert value == data['coefficients'][n], n
            records.append(record)
            coefficients.append(value)
        assert coefficients == data['coefficients']
        assert len(records) == len(data['factorizations_and_prime_powers']) == 255
        exported = [{'n': n, 'a_n': coefficients[n]} for n in range(1, 129)]
        assert [r['n'] for r in exported] == list(range(1, 129))
        evidence = {'upstream_path': str(path.relative_to(ROOT)),
                    'upstream_sha256': EXPECTED, 'selected_attempt': 0,
                    'model': inputs['model'], 'N': 389, 'Delta': 389, 'T': 256,
                    'point_counts': counts, 'factorizations_and_prime_powers': records,
                    'coefficients_with_index_zero_sentinel': coefficients,
                    'export_indices_1_through_128': exported,
                    'normalization': 'a_1=1; full untwisted unnormalized newform coefficients'}
        (OUT/'certificate.json').write_text(json.dumps(evidence, indent=2)+'\n')
        after = {str(p.relative_to(ROOT)): digest(p) for p in fixed}
        assert before == after, 'fixed input preservation'
        (OUT/'preservation.json').write_text(json.dumps(before, indent=2)+'\n')
        report.update({'complete_replay': True, 'good_prime_rows': len(primes),
                       'nodal_rows': 1, 'exhausted_xy_pairs': sum(r['p']**2 for r in counts),
                       'factorization_records': len(records), 'coefficient_slots': 256,
                       'exported_slots': len(exported), 'preserved_files': len(before),
                       'certificate_sha256': digest(OUT/'certificate.json')})
    except Exception as exc:
        report['failures'].append(f'{type(exc).__name__}: {exc}')
    report_path = OUT/'report.json'
    report_path.write_text(json.dumps(report, indent=2)+'\n')
    # Include setup, all replay, preservation, source and final report writes.
    report['measured_seconds_before_final_write'] = time.monotonic()-start
    report['new_artifact_bytes_upper_bound'] = sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())+4096
    if report['measured_seconds_before_final_write'] >= 179:
        report['failures'].append('finalization reserve exceeded')
    if report['new_artifact_bytes_upper_bound'] > 134217728:
        report['failures'].append('artifact byte bound exceeded')
    report_path.write_text(json.dumps(report, indent=2)+'\n')
    elapsed = time.monotonic()-start
    size = sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
    assert elapsed <= 180 and size <= 134217728
    print(f"coverage: primes={report.get('good_prime_rows')} nodal={report.get('nodal_rows')} "
          f"factorizations={report.get('factorization_records')} coefficients={report.get('coefficient_slots')} "
          f"export={report.get('exported_slots')}; failures={report['failures']}")
    print(f'actual execution seconds={elapsed:.6f} required<=180; new bytes={size} required<=134217728')
    print('evidence: scripts/finite-derivative-coefficients/{certificate,preservation,report}.json')
    signal.alarm(0)
    if report['failures']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
