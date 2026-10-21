"""Bounded complete homogeneous-locus classification of the approved selector.

All evidence is written to active-rank19-complete-loci.json. Historical
certificates are read-only. A genuinely unresolved component stops the attempt.
"""
from collections import Counter
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json

import zero_anchor_support_filter as direct
import residual_kernel_gates as gates
import verify_fixed_three_row_extensions as derivative
from verify_inactive_coordinate_screen import nullspace

HERE = Path(__file__).resolve().parent
P = 97


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def selected(record):
    return (record['status'] == 'screen_failure' and record['rank'] == 19
            and 'L112_exchanged_rows' not in record['prior_exclusions']
            and (record['third_index'], record['fourth_index']) != (0, 320))


def run():
    audit_path = HERE/'inactive-coordinate-partition-critical-audit.json'
    audit = json.loads(audit_path.read_bytes())
    assert not audit['failures'] and audit['replay_returncode'] == 0
    assert all(c['passed'] for c in audit['checks'])
    assert audit['artifact_hashes_before'] == audit['artifact_hashes_after']
    for name, value in audit['artifact_hashes_after'].items():
        assert digest(HERE/name) == value, name
    for name, value in audit['code_hashes'].items():
        assert digest(HERE/name) == value, name
    source_path = HERE/'inactive-coordinate-screen.json'
    source = json.loads(source_path.read_bytes())
    assert not source['failures'] and all(c['passed'] for c in source['checks'])
    assert digest(source_path) == audit['artifact_hashes_after'][source_path.name]
    assert len(source['records']) == 599
    assert sum(r['status'] == 'screen_failure' for r in source['records']) == 239
    manifest = [[r['third_index'], r['fourth_index']] for r in source['records'] if selected(r)]
    records, unresolved = [], []
    for input_position, source_record in enumerate(source['records']):
        if not selected(source_record):
            continue
        index = [source_record['third_index'], source_record['fourth_index']]
        rows = [{'I': i, 'K': k} for i, k in source_record['four_rows']]
        blocks = [direct.block(r['I'], r['K']) for r in rows]
        matrix = [r for b in blocks for r in b['matrix']]
        assert matrix == [r for row in rows for r in derivative.block(row['I'], row['K'])]
        pivots, basis = nullspace(matrix)
        assert len(pivots) == 19 and len(basis) == 2
        assert basis == source_record['kernel_basis']
        free = sorted(set(range(21))-set(pivots))
        assert free == source_record['free_columns']
        residuals = [[sum(x*y for x, y in zip(row, v)) % P for row in matrix] for v in basis]
        assert not any(map(any, residuals))
        assert [[v[c] for c in free] for v in basis] == [[1, 0], [0, 1]]
        rank, minor_rows = direct.rank_and_rows(matrix)
        minor = [[matrix[r][c] for c in pivots] for r in minor_rows]
        det = direct.determinant(minor)
        assert rank == 19 and det
        quadrics = gates.plucker_polynomials(basis)
        gcd, bezout = gates.gcd_certificate([gates.trim(q) for q in quadrics])
        quotients = []
        for q in quadrics:
            if gcd:
                quotient, remainder = gates.divrem(q, gcd)
                assert not remainder
                quotients.append(quotient)
        infinity = all(q[2] == 0 for q in quadrics)
        finite_roots = [t for t in range(P) if gcd and sum(c*pow(t, n, P) for n, c in enumerate(gcd)) % P == 0]
        rec = {'historical_index': index, 'source_record_position': input_position,
               'rows': rows, 'original_matrix': matrix, 'kernel_basis': basis,
               'free_columns': free, 'kernel_residuals': residuals,
               'rank_minor_rows': minor_rows, 'rank_minor_columns': pivots,
               'rank_minor_residue': det,
               'homogeneous_coefficients_s2_st_t2': quadrics,
               'affine_gcd': gcd, 'bezout_coefficients': bezout,
               'gcd_quotients': quotients, 'infinity_is_decomposable': infinity}
        if not gcd:
            assert all(not any(q) for q in quadrics)
            rec.update(locus_type='whole_line', unresolved_branch='whole-line chartwise gates')
        else:
            remaining = gcd[:]
            factors = []
            for root in finite_roots:
                multiplicity = 0
                while remaining and len(remaining) > 1:
                    quotient, remainder = gates.divrem(remaining, [-root % P, 1])
                    if remainder:
                        break
                    remaining = quotient
                    multiplicity += 1
                factors.append({'root': root, 'multiplicity': multiplicity})
            rec['affine_linear_factors'] = factors
            rec['remaining_affine_factor'] = remaining
            if len(remaining) > 1:
                rec.update(locus_type='nonsplit_quadratic', unresolved_branch='quadratic-extension gate evaluation')
            else:
                rec['locus_type'] = 'finite_split' if finite_roots or infinity else 'empty'
                parameters = [[1, t] for t in finite_roots]+([[0, 1]] if infinity else [])
                points = []
                for s, t in parameters:
                    p = [(s*a+t*b) % P for a, b in zip(*basis)]
                    point = gates.plane_gates(p, rows)
                    point['homogeneous_parameter'] = [s, t]
                    for row, gate in zip(rows, point['row_gates']):
                        if gate['projection_rank'] == 0:
                            continue
                        error = dict(zip(row['I']+row['K'], gate['error_weights']))
                        identity = [((gate['intersection_vector'][direct.S.index(x)] if x in direct.S else 0)
                                     -error.get(x, 0)-gate['lambda_value']*direct.g(row['K'], x)) % P
                                    for x in direct.H]
                        assert not any(identity) and not any(gate['moment_residuals'])
                        gate['h_minus_error_minus_lambda_g_on_H'] = identity
                    points.append(point)
                rec['points_and_all_row_gates'] = points
                rec['disposition'] = ('intrinsic_survivor' if any(p['passes_intrinsic_gates'] for p in points)
                                      else 'excluded_necessary_gates')
        records.append(rec)
        if 'unresolved_branch' in rec:
            unresolved.append({'historical_index': index, 'branch': rec['unresolved_branch']})
            break
    completed_manifest = [r['historical_index'] for r in records]
    assert completed_manifest == manifest[:len(records)]
    points = [p for r in records for p in r.get('points_and_all_row_gates', [])]
    row_gates = [g for p in points for g in p['row_gates']]
    survivor_details = []
    for record_position, rec in enumerate(records):
        for point_position, point in enumerate(rec.get('points_and_all_row_gates', [])):
            if point['passes_intrinsic_gates']:
                survivor_details.append({'historical_index': rec['historical_index'],
                    'record_position': record_position, 'point_position': point_position,
                    'rows': rec['rows'], 'homogeneous_parameter': point['homogeneous_parameter'],
                    'u': point['u'], 'v': point['v'],
                    'row_gates': [{key: gate[key] for key in
                        ['direction_coefficients', 'lambda_value', 'error_weights', 'prescribed_finite_gate']}
                        for gate in point['row_gates']]})
    summary = {'required_occurrences': len(manifest), 'processed_occurrences': len(records),
               'locus_types': dict(Counter(r['locus_type'] for r in records)),
               'complete_points': len(points), 'row_gates': len(row_gates),
               'projection_rank_counts': dict(Counter(g['projection_rank'] for g in row_gates)),
               'intrinsically_passing_points': sum(p['passes_intrinsic_gates'] for p in points),
               'failing_points_with_lambda_zero': sum(any(g.get('lambda_value') == 0 for g in p['row_gates']) for p in points),
               'excluded_occurrences': sum(r.get('disposition') == 'excluded_necessary_gates' for r in records),
               'surviving_occurrence_indices': [r['historical_index'] for r in records
                                                if r.get('disposition') == 'intrinsic_survivor'],
               'surviving_parameters': [p['homogeneous_parameter'] for p in survivor_details],
               'affine_gcd_histogram': dict(Counter(str(r['affine_gcd']) for r in records)),
               'infinity_points': sum(r['infinity_is_decomposable'] for r in records),
               'repeated_affine_factors': sum(f['multiplicity'] > 1 for r in records
                                               for f in r.get('affine_linear_factors', [])),
               'failed_gate_histogram': dict(Counter(f for g in row_gates for f in g['failed_gates'])),
               'unresolved_branches': len(unresolved)}
    assert all(digest(HERE/name) == value for name, value in audit['artifact_hashes_after'].items())
    out = {'scope': 'Approved L118 rank-19 selector only; necessary L109 gates, no four-row converse',
           'modulus': P, 'H': direct.H, 'S': direct.S,
           'source_path': source_path.name, 'source_sha256': digest(source_path),
           'audit_path': audit_path.name, 'audit_sha256': digest(audit_path),
           'audited_artifacts_checked_unchanged': len(audit['artifact_hashes_after']),
           'code_sha256': digest(Path(__file__)),
           'original_chart_condition': 'u_original=A*u+B*v; v_original=C*u+D*v; AD-BC!=0; require D*alpha-C*beta!=0 at every rank-one row. Otherwise direction is omitted; if finite, divide h,lambda,error by (D*alpha-C*beta)/(AD-BC).',
           'selected_manifest': manifest, 'processed_manifest': completed_manifest,
           'summary': summary, 'survivor_details': survivor_details,
           'records': records, 'unresolved': unresolved, 'failures': []}
    target = HERE/'active-rank19-complete-loci.json'
    target.write_text(json.dumps(out, separators=(',', ':'))+'\n')
    print(json.dumps(summary, sort_keys=True))
    print(f'Processed {len(records)}/{len(manifest)}; rank 19/21 with nonzero minors; failures 0; certificate {target}')


if __name__ == '__main__':
    run()
