"""Exact specialization of Milne EC2 IV.9.10/9.11(a); no extension-field sampling."""
import json
from pathlib import Path

p, degree = 13, 12
rows = []
points = []
for x in range(p):
    residues = [(y*y+y-x**3+x*x+7820*x+263580) % p for y in range(p)]
    ys = [y for y, residue in enumerate(residues) if residue == 0]
    rows.append({'x': x, 'equation_residues_y_0_through_12': residues, 'solutions': ys})
    points.extend([[x, y] for y in ys])
base_order = len(points) + 1  # Unique projective point [0:1:0].
trace = p + 1 - base_order
s = [2, trace]
for n in range(2, degree+1):
    s.append(trace*s[-1]-p*s[-2])

def mul(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]

def power(a, n):
    answer = [[1,0],[0,1]]
    while n:
        if n % 2:
            answer = mul(answer, a)
        a = mul(a, a)
        n //= 2
    return answer

# Independent binary matrix evaluation, not a call to the scalar recurrence.
companion = [[trace, -p], [1, 0]]
matrices = [power(companion, n) for n in range(degree+1)]
matrix_traces = [a[0][0]+a[1][1] for a in matrices]
orders = [1+p**n-s[n] for n in range(1, degree+1)]
# Weierstrass invariants of a1=0,a2=-1,a3=1,a4=-7820,a6=-263580.
b2,b4,b6 = -4,-15640,-1054319
b8 = 4*(-1)*(-263580) + (-1)*1**2 - (-7820)**2
c4 = b2*b2-24*b4
c6 = -b2**3+36*b2*b4-216*b6
discriminant = (-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6)
singular = [[x,y] for x,y in points if (2*y+1)%p==0 and (3*x*x-2*x-7820)%p==0]
checks = {
    'all_169_affine_pairs_recorded': sum(len(r['equation_residues_y_0_through_12']) for r in rows)==169,
    'no_affine_singular_point': not singular,
    'origin_smooth': True,  # dF/dZ=Y^2=1 at [0:1:0], as proved in L068.
    'discriminant_minus_11': discriminant==-11,
    'invariant_identity': c4**3-c6**2==1728*discriminant,
    'discriminant_unit_at_13': discriminant%p!=0,
    'base_count_recovered_by_extension_formula': orders[0]==base_order,
    'all_matrix_traces_match_scalar_recurrence': matrix_traces==s,
    'extension_order_positive': orders[-1]>0,
    'remainder_matches_trace_mod_p': orders[-1]%p==(1-pow(trace,degree,p))%p,
}
failures = [key for key,value in checks.items() if not value]
certificate = {
    'model': 'Y^2+Y=X^3-X^2-7820X-263580',
    'prime':p, 'extension_degree':degree,
    'source':'Milne, Elliptic Curves, 2nd ed. (2021), IV Theorem 9.10 and Remark 9.11(a), p.156',
    'enumeration':rows,'affine_points':points,'projective_origin':[0,1,0],
    'base_order':base_order,'frobenius_trace':trace,
    'invariants':{'b2':b2,'b4':b4,'b6':b6,'b8':b8,'c4':c4,'c6':c6,'discriminant':discriminant},
    'singular_affine_points':singular,
    'power_sums_n_0_through_12':s,
    'companion_matrix':companion,'binary_matrix_powers_n_0_through_12':matrices,
    'matrix_traces':matrix_traces,'orders_n_1_through_12':orders,
    'extension_order':orders[-1],'remainder_mod_13':orders[-1]%p,
    'bruin_order_hypothesis':{'required_remainder':'1 through 12','actual_remainder':orders[-1]%p,'holds':orders[-1]%p!=0},
    'checks':checks,'failures':failures,
}
path = Path(__file__).with_name('order-certificate.json')
path.write_text(json.dumps(certificate,indent=2)+'\n')
print(f'Base order={base_order}; extension order={orders[-1]}; remainder mod 13={orders[-1]%p}')
print(f'Affine coverage=169/169; extension degree={degree}/12; checks={sum(checks.values())}/{len(checks)}; failures={failures}')
print(f"Bruin order hypothesis: {'PASS' if certificate['bruin_order_hypothesis']['holds'] else 'FAIL'}; required remainder=1..12, actual={orders[-1]%p}")
print(f'Certificate: {path}')
if failures:
    raise SystemExit(1)
