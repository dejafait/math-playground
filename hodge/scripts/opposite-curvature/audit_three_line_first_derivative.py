"""Independent entrywise and exact-rank audit of L124's saved evidence."""
import json
from fractions import Fraction as F
from pathlib import Path

root = Path(__file__).parent
saved = json.loads((root / 'three_line_first_derivative_certificate.json').read_text())
exponents = [(i, j, k, 5-i-j-k) for i in range(6)
             for j in range(6-i) for k in range(6-i-j)]


def exact_rank(rows):
    # Sparse rational row reduction, separate from the construction script.
    pivots = {}
    for row in rows:
        row = {j: F(c) for j, c in enumerate(row) if F(c)}
        while row:
            j = min(row)
            if j not in pivots:
                c = row[j]
                pivots[j] = {k: v/c for k, v in row.items()}
                break
            c = row[j]
            for k, v in pivots[j].items():
                value = row.get(k, F(0)) - c*v
                if value:
                    row[k] = value
                else:
                    row.pop(k, None)
    return len(pivots)


def entries(e, point, direction=None):
    """Monomial values/derivatives using the product rule at coordinate axes/diagonal.

    point entries are None, 0 or 1, meaning zero, x0 or x1. Direction
    entries are pairs of coefficients of u0,u1. No polynomial substitution
    or differentiation functions from the original script are reused.
    """
    value = [F(0)] * (6 if direction is None else 10)
    terms = [(None, 1)] if direction is None else enumerate(e)
    for j, multiplicity in terms:
        if not multiplicity:
            continue
        powers = list(e)
        if j is not None:
            powers[j] -= 1
        if any(p and axis is None for p, axis in zip(powers, point)):
            continue
        x0_power = sum(p for p, axis in zip(powers, point) if axis == 0)
        if direction is None:
            value[x0_power] += 1
        else:
            for u in range(2):
                value[2*x0_power+u] += multiplicity * direction[j][u]
    return value


def rows(columns):
    return [list(row) for row in zip(*columns)]


def neg(A):
    return [[-x for x in row] for row in A]


identity = [[F(1), F(0)], [F(0), F(1)]]
points = [[0, 1, None, None], [None, None, 0, 1], [0, 1, 0, 1]]
failures = []
records = []
for sample in saved['samples']:
    a, b, s, r = [F(sample[key]) for key in
                  ('a', 'b', 'q_real', 'q_imaginary_length')]
    t = a+b+2*s
    C = [[s/a, -r/a], [r/a, s/a]]
    D = [[s/b, r/b], [-r/b, s/b]]
    H = [[(a+s)/t, r/t], [-r/t, (a+s)/t]]
    one_minus_H = [[identity[i][j]-H[i][j] for j in range(2)]
                   for i in range(2)]
    directions = [neg(C)+identity, identity+neg(D), one_minus_H+neg(H)]
    N = [row for p, d in zip(points, directions)
         for row in rows([entries(e, p, d) for e in exponents])]
    R = [row for p in points
         for row in rows([entries(e, p) for e in exponents])]
    expected_N = [[F(c) for c in row] for row in sample['normal_matrix']]
    expected_R = [[F(c) for c in row] for row in sample['restriction_matrix']]
    ranks = [exact_rank(N), exact_rank(N+R)]
    checks = {'positive_metric': a > 0 and b > 0 and a*b > s*s+r*r,
              'all_normal_entries_match': N == expected_N,
              'all_restriction_entries_match': R == expected_R,
              'ranks_match_required': ranks == [30, 48],
              'saved_ranks_match': ranks == [sample['normal_rank_actual'],
                                             sample['full_jet_rank_actual']],
              'saved_range_matches': ranks[1]-ranks[0] ==
                                    sample['restriction_rank_actual'] == 18}
    failures.extend(sample['name']+': '+k for k, v in checks.items() if not v)
    records.append({'name': sample['name'], 'entries_checked': 48*56,
                    'ranks_actual': ranks, 'ranks_required': [30, 48],
                    'checks': checks})

mixed = [e for e in exponents if e[0]+e[1] in (2, 3)]
diagonal = points[2]
first_direction = identity + [[F(0), F(0)]]*2
interpolation = rows([entries(e, diagonal) for e in mixed]) + rows([
    entries(e, diagonal, first_direction) for e in mixed])
correction_columns = []
radial_zero = True
value_zero = True
for i in range(3):
    for j in range(2):
        # Delta*x0^i*x1^(2-i)*y0^j*y1^(1-j), directly as two monomials.
        plus = (i+1, 2-i, j, 2-j)
        minus = (i, 3-i, j+1, 1-j)
        correction_columns.append([v-w for v, w in zip(
            entries(plus, diagonal, first_direction),
            entries(minus, diagonal, first_direction))])
        value_zero &= entries(plus, diagonal) == entries(minus, diagonal)
        # Radial substitution u=x sends the two directional polynomials
        # to quintics with coefficients accumulated by x0 exponent.
        radial = [F(0)]*6
        for power in range(5):
            for u in range(2):
                radial[power+(u == 0)] += correction_columns[-1][2*power+u]
        radial_zero &= not any(radial)
correction = rows(correction_columns)
checks = {
    'all_interpolation_entries_match': interpolation ==
        [[F(c) for c in row] for row in saved['interpolation']['matrix']],
    'all_correction_entries_match': correction ==
        [[F(c) for c in row] for row in saved['interpolation']['correction_matrix']],
    'interpolation_rank': exact_rank(interpolation) == 16,
    'correction_rank': exact_rank(correction) == 4,
    'zero_values': value_zero, 'zero_radial_derivatives': radial_zero,
    'saved_failure_list_empty': saved['failures'] == [],
    'saved_passed': saved['passed'] is True,
}
failures.extend(k for k, v in checks.items() if not v)
certificate = {
    'scope': 'Complete entrywise reconstruction and independent rational ranks; '
             'finite samples only, not a uniform or real-module proof.',
    'input': 'scripts/opposite-curvature/three_line_first_derivative_certificate.json',
    'samples': records, 'interpolation_checks': checks,
    'entries_checked_actual': 4*48*56+16*24+10*6,
    'entries_checked_required': 11196,
    'failures': failures, 'passed': not failures,
}
path = root / 'three_line_first_derivative_audit_certificate.json'
path.write_text(json.dumps(certificate, indent=2)+'\n')
for record in records:
    print(f"{record['name']}: ranks {record['ranks_actual']}/[30, 48]; "
          f"all {record['entries_checked']} entries match: {all(record['checks'].values())}")
print(f"Entries: {certificate['entries_checked_actual']}/11196; "
      f"interpolation rank {exact_rank(interpolation)}/16; "
      f"correction rank {exact_rank(correction)}/4; failures: {failures}; "
      f"certificate: {path}")
raise SystemExit(bool(failures))
