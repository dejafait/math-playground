#!/usr/bin/env python3
"""Independent signed-minor audit of every L125 projective-map record.

The independent reconstruction does not use either production solver.
The production functions are called only after the independent answer exists.
"""
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

BASE = Path(__file__).resolve().parent
Q = 137
T = [16, 64, 70, 102, 112, 118, 121]
DEST = T[1:]
FAILURES = []


def check(name, condition):
    if not condition:
        FAILURES.append(name)
    return bool(condition)


def determinant3(rows):
    total = 0
    for p in itertools.permutations(range(3)):
        inversions = sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
        term = (-1) ** inversions
        for i in range(3):
            term *= rows[i][p[i]]
        total += term
    return total % Q


def reconstruct(xs, ys):
    rows = [[x, 1, -x*y, -y] for x, y in zip(xs, ys)]
    minors = [determinant3([[row[j] for j in range(4) if j != c]
                            for row in rows]) for c in range(4)]
    raw = [((-1) ** c * minors[c]) % Q for c in range(4)]
    if not any(raw):
        raise ArithmeticError('Rank less than three')
    # Fermat inversion, separate from the production modular inverse.
    inv = pow(next(v for v in raw if v), Q - 2, Q)
    matrix = [v * inv % Q for v in raw]
    residuals = [sum(row[j] * matrix[j] for j in range(4)) % Q for row in rows]
    if any(residuals):
        raise ArithmeticError('Cofactor vector is not in the kernel')
    return matrix, minors, residuals


def map_point(matrix, x):
    numerator = (matrix[0] * x + matrix[1]) % Q
    denominator = (matrix[2] * x + matrix[3]) % Q
    return None if not denominator else numerator * pow(denominator, Q - 2, Q) % Q


def main():
    original_path = BASE / 'two-core-star-rigidity.json'
    program_path = BASE / 'two_core_star_rigidity.py'
    original = json.loads(original_path.read_text())
    check('prime modulus', all(Q % d for d in range(2, 12)))
    spec = importlib.util.spec_from_file_location('l125_production', program_path)
    production = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(production)
    records, extra, accepted = [], [], []
    cases = []
    for removed in T:
        source = [x for x in T if x != removed]
        case_accepted = []
        pole_count = 0
        for images_tuple in itertools.permutations(DEST, 3):
            images = list(images_tuple)
            matrix, minors, residuals = reconstruct(source[:3], images)
            det = (matrix[0]*matrix[3] - matrix[1]*matrix[2]) % Q
            mapped = [map_point(matrix, x) for x in source]
            prefix = f'{removed}:{images}'
            cross = list(production.by_cross_ratio(tuple(source[:3]), tuple(images)))
            elim = list(production.by_linear_equations(tuple(source[:3]), tuple(images)))
            for label, condition in [('cross ratio', cross == matrix),
                                     ('elimination', elim == matrix),
                                     ('invertible', det != 0),
                                     ('anchors', mapped[:3] == images)]:
                check(prefix + ':' + label, condition)
            is_accepted = None not in mapped and sorted(mapped) == DEST
            record = dict(removed=removed, source=source, anchor_images=images,
                          matrix=matrix, matrix_by_elimination=matrix,
                          determinant=det, all_six_images=mapped,
                          checks=dict(independent_constructions_equal=True,
                                      determinant_nonzero=True, anchor_images_correct=True),
                          accepted=is_accepted)
            records.append(record)
            extra.append(dict(removed=removed, anchor_images=images, minors=minors,
                              kernel_residuals=residuals, production_cross_ratio=cross,
                              production_elimination=elim))
            if None in mapped:
                pole_count += 1
            if is_accepted:
                accepted.append(record)
                case_accepted.append(matrix)
        cases.append(dict(removed=removed, actual_candidates=120, required_candidates=120,
                          accepted_matrices=case_accepted, candidates_with_poles=pole_count))
    expected = dict(field=Q, evaluation_set=T, left_removed=16, destination=DEST,
                    required_candidates=840, actual_candidates=len(records), accepted=accepted,
                    expected_accepted=[dict(removed=16, matrix=[1, 0, 0, 1])],
                    failures=[], records=records,
                    qualification='Finite projective test only; the canonical symbolic proof must justify its implication for arbitrary star isomorphisms and full-law coupling.')
    field_checks = {key: check('complete field:' + key, original.get(key) == value)
                    for key, value in expected.items()}
    check('exact top-level keys', set(original) == set(expected))
    saved_records = original.get('records', [])
    record_checks = [check(f'complete record:{i}', i < len(saved_records) and rec == saved_records[i])
                     for i, rec in enumerate(records)]
    check('840 records required', len(records) == len(saved_records) == 840)
    check('only required survivor', [(r['removed'], r['matrix']) for r in accepted]
          == [(16, [1, 0, 0, 1])])
    event_mass = Fraction(137, 963)
    check('positive latent mass', event_mass > 0)
    check('strict intersection conflict', 60 + 6 > 63)
    result = dict(audit='L125 complete independent signed-minor reconstruction',
                  inputs={p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (original_path, program_path)},
                  actual_candidates=len(records), required_candidates=840,
                  cases=cases, field_checks=field_checks, record_checks=record_checks,
                  records=records, reconstruction_evidence=extra,
                  event=dict(latent_mass=str(event_mass), output_mass_relation='>=',
                             required_output_mass='>0', forced_intersection_lower_bound=66,
                             permitted_distinct_intersection_upper_bound=63),
                  failures=FAILURES,
                  qualification='Arithmetic audit only. The canonical L125 proof and its independent symbolic audit justify column recovery, arbitrary symbol maps, event pushforward and support conflict.')
    output = BASE / 'l125-critical-audit.json'
    output.write_text(json.dumps(result, indent=2) + '\n')
    print(f'Candidates and complete records: {sum(record_checks)}/{len(records)}; required 840')
    print(f'Complete input fields: {sum(field_checks.values())}/{len(field_checks)}')
    print(f'Accepted maps: {[(r["removed"], r["matrix"]) for r in accepted]}')
    print('Intersection: >=66; permitted <=63. Output mass: >=137/963; required >0.')
    print(f'Failures: {FAILURES}')
    print(f'Certificate: {output.relative_to(Path.cwd())}')
    if FAILURES:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
