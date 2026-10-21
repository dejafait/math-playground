"""Independent exhaustive F2 replay of L089; field justifications are in L089."""
import itertools
import json
from pathlib import Path

OUT = Path(__file__).with_name('audit-certificate.json')
bits = list(itertools.product(range(2), repeat=2))
zero = (0, 0)


def add(*vectors):
    return tuple(sum(v[i] for v in vectors) % 2 for i in range(2))


def nq(x):
    return (0, x[1])


def plus(x):
    return x


def minus(x):
    return (x[0] ^ x[1], x[1])


checks = {}
residue_squares = sorted({x*x % 11 for x in range(1, 11)})
gp = (3*8*8 - 8*8 - 160) % 11
beta_residue = ((4-8)*pow(2, -1, 11)) % 11
d_unit = 16*pow(25*4*gp, -1, 11) % 11
checks['residue_squares'] = residue_squares == [1, 3, 4, 5, 9]
checks['fixed_s_square_and_minus_one_nonsquare'] = 4 in residue_squares and 10 not in residue_squares
checks['exceptional_units'] = (gp, (8-beta_residue)%11, (beta_residue-8)%11, d_unit) == (1, 10, 1, 5)
checks['d_unit_square'] = d_unit in residue_squares
norm_table = [{'input': x, 'L_to_Q': nq(x), 'L_to_M_plus': plus(x),
               'L_to_M_minus': minus(x)} for x in bits]
checks['both_norm_towers'] = all(nq(plus(x)) == nq(x) == nq(minus(x)) for x in bits)
checks['conjugation_is_involution'] = all(minus(minus(x)) == x for x in bits)

rows = []
envelope = set()
for e1, e2, a, ell, b, m, c, n in itertools.product(range(2), repeat=8):
    A, B, C = (a, ell), (b, m), (c, n)
    dk = add(A, B, C)
    df_q = nq(A)
    df_m = add((e1, 0), (e2, 0), plus(B), minus(C))
    accepted = dk == df_q == df_m == zero
    row = (e1, e2, a, ell, b, m, c, n)
    rows.append({'bits': row, 'D_K': dk, 'D_F_Q': df_q, 'D_F_M': df_m, 'accepted': accepted})
    if accepted:
        envelope.add(row)

formula = {(e1, e2, e1 ^ e2 ^ m, 0, b, m, b ^ e1 ^ e2 ^ m, m)
           for e1, e2, b, m in itertools.product(range(2), repeat=4)}
projection = {row[2:] for row in envelope}
full = {(0, 0, a, v, a, v) for a, v in bits}
fibers = {p: sum(row[2:] == p for row in envelope) for p in projection}
witness = (1, 0, 1, 0, 0, 0, 1, 0)
checks['complete_domain'] = len(rows) == 256
checks['exact_parameterization'] = envelope == formula
checks['envelope_size'] = len(envelope) == 16
checks['projection_size'] = len(projection) == 8
checks['every_projection_has_two_preimages'] = set(fibers.values()) == {2}
checks['full_image_size'] = len(full) == 4
checks['full_image_contained_in_projection'] = full <= projection
checks['exact_outside_projection_count'] = len(projection - full) == 4
checks['exact_outside_envelope_count'] = sum(row[2:] not in full for row in envelope) == 8
checks['witness_passes_all_norm_equations'] = witness in envelope
checks['witness_outside_full_image'] = witness[2:] not in full
cert = {'bit_order': ['e1', 'e2', 'a', 'ell', 'b', 'm', 'c', 'n'],
        'norm_table': norm_table, 'exceptional_unit_residues': [gp, 10, 1, d_unit],
        'all_256_rows': rows, 'envelope': sorted(envelope),
        'projection': sorted(projection), 'full_image': sorted(full),
        'outside_projection': sorted(projection - full), 'witness': witness,
        'checks': checks, 'failures': [k for k, v in checks.items() if not v],
        'limits': 'Local envelope only; no global realization or dimension improvement.'}
OUT.write_text(json.dumps(cert, indent=2) + '\n')
print(f'Checks: {sum(checks.values())}/{len(checks)}; failures: {cert["failures"]}')
print(f'Envelope: {len(envelope)}; projection: {len(projection)}; required containment in full image: {len(full)} classes; containment: {projection <= full}')
print(f'Certificate: {OUT}')
assert not cert['failures']
