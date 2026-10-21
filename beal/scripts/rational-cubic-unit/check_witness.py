"""Exact arithmetic for L071; no numerical number-field backend required."""
from itertools import product
from pathlib import Path
import json


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def scale(n, a):
    return tuple(n * x for x in a)


def mul(a, b, relation):
    """relation gives s^3 as coefficients in the basis (1,s,s^2)."""
    c = [0] * 5
    for i in range(3):
        for j in range(3):
            c[i + j] += a[i] * b[j]
    for k in (4, 3):
        q = c[k]
        c[k] = 0
        for j in range(3):
            c[k - 3 + j] += q * relation[j]
    return tuple(c[:3])


def det(a):
    return (a[0][0] * (a[1][1]*a[2][2]-a[1][2]*a[2][1])
            - a[0][1] * (a[1][0]*a[2][2]-a[1][2]*a[2][0])
            + a[0][2] * (a[1][0]*a[2][1]-a[1][1]*a[2][0]))


def norm(a, relation):
    columns = [mul(a, e, relation) for e in ((1,0,0),(0,1,0),(0,0,1))]
    return det([[col[i] for col in columns] for i in range(3)])


rt = (-1, -1, 1)  # t^3=t^2-t-1
rs = (2, -6, 4)   # s=t+1, s^3=4s^2-6s+2
one = (1, 0, 0)
theta = (8, -14, 6)
theta2 = mul(theta, theta, rt)
gtheta = add(add(mul(theta2, theta, rt), scale(-4, theta2)),
             add(scale(-160, theta), (-1264, 0, 0)))
inverse_map = add(add((92, 0, 0), scale(62, theta)), scale(-3, theta2))
u_t, inv_t = (0, -1, 0), (1, -1, 1)
u, inv, h = (1, -1, 0), (3, -3, 1), (-23, 26, -6)
uh = mul(u, h, rs)

# O_L/8O_L has exactly 8^3 elements in this Eisenstein basis.
# Its units have odd constant coordinate because its residue field is F2.
records = [{"root": a, "square": tuple(x % 8 for x in mul(a, a, rs))}
           for a in product(range(8), repeat=3) if a[0] % 2]
squares = sorted({tuple(r["square"]) for r in records})
targets = {name: {"exact": a, "residue": tuple(x % 8 for x in a),
                  "matching_roots": [r["root"] for r in records
                                     if tuple(r["square"]) == tuple(x % 8 for x in a)]}
           for name, a in (("u", u), ("h", h), ("uh", uh))}

checks = {
    "theta_satisfies_g": gtheta == (0,0,0),
    "inverse_coordinate_identity": inverse_map == (0,-484,0),
    "unit_inverse_t": mul(u_t, inv_t, rt) == one,
    "unit_norm_t": norm(u_t, rt) == 1,
    "shifted_unit_inverse": mul(u, inv, rs) == one,
    "shifted_unit_norm": norm(u, rs) == 1,
    "theta_shift": (28,-26,6) == (theta[0]-theta[1]+theta[2], theta[1]-2*theta[2], theta[2]),
    "point_h_norm": norm(h, rs) == -2039,
    "point_square_residue": -2039 % 8 == 1,
    "complete_unit_residues": len(records) == 256 and len({tuple(r['root']) for r in records}) == 256,
    "square_residue_count": len(squares) == 16,
    "all_three_nonsquare": all(not target['matching_roots'] for target in targets.values()),
    "product_exact": uh == (-11,13,-8),
    "eisenstein_coefficients": all(c % 2 == 0 for c in (-4,6,-2)) and (-2) % 4 != 0,
}
failures = [k for k,v in checks.items() if not v]
data = {
    "inputs": {"f": [1,1,-1,1], "g": [-1264,-160,-4,1], "shifted_f": [-2,6,-4,1]},
    "coordinates": {"theta_in_t": theta, "theta_squared_in_t": theta2,
                    "u_theta_numerator": [92,62,-3], "u_theta_denominator": 484},
    "unit": {"u_t": u_t, "inverse_t": inv_t, "norm": norm(u_t,rt)},
    "point": {"X": 5, "Y_squared": -2039, "h_s": h, "norm_h": norm(h,rs)},
    "local": {"modulus": 8, "ramification_index": 3, "residue_degree": 1,
              "enumeration": records, "square_residues": squares, "targets": targets},
    "thresholds": {"actual_excluded_unit_witnesses": int(checks['all_three_nonsquare']),
                   "required_excluded_unit_witnesses": 1,
                   "H_order_from_cited_theorem": 2,
                   "full_unit_group_completeness_claimed": False},
    "checks": checks, "failures": failures,
}
path = Path(__file__).with_name('witness-certificate.json')
path.write_text(json.dumps(data, indent=2) + '\n')
print(f"Checks: {sum(checks.values())}/{len(checks)}; failures: {failures}")
print("Complete unit residues modulo8: 256; square residues: 16")
print("u, h, uh nonsquare: " + str(checks['all_three_nonsquare']))
print(f"Excluded unit witnesses actual/required: {data['thresholds']['actual_excluded_unit_witnesses']}/1")
print(f"Certificate: {path.relative_to(Path.cwd())}")
raise SystemExit(bool(failures))
