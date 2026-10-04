# Pure factor-point correction calculation checkpoint

Date: 2026-10-04. The saved Next action is explicitly covered by
`drafts/literature/2026-10-04-fixed-lower-chern-stability-test.md`,
with DECISION: SPECIALIZE. Reuse that assessment and L046's precise
inequality citation; no further literature work is needed here.

The main gap is a compatible bundle permitting transport of the cubic
action into the fourth NS-fixed RM direction. The intermediate target
keeps L044's mixed character and actual ample chamber fixed and changes
only the two pure factor-point coefficients. Finding no rational
correction satisfying the necessary inequality would close this repair;
finding a nonempty region would specify lower data worth a subsequent
realizability test, without supplying a bundle or transport.

L046 stopped the unchanged lower data across all ranks; L045 stopped
one exact rank-two K-class. Neither calculates the permitted point
corrections. All those stops and the existing unfinished work remain.

Write beta=2[C]+B_c, e_1=eta tensor 1, e_2=1 tensor eta,
h=omega_c, s=q(h,h)>0 and Omega=p_1^*h+p_2^*h. For rational
a,b put beta_(a,b)=beta+a e_1+b e_2. L046's contraction and
integral_X e_i Omega^2=s give

integral_X beta_(a,b) Omega^2=(8+4lambda+a+b)s.

For c_1=0 and any positive rank, Bogomolov therefore requires
a+b<=-8-4lambda. Since lambda is irrational and a+b rational,
equality is impossible: the admissible rational region is precisely
a+b<-8-4lambda. It is nonempty. Exact boundary and integer examples
were checked below and proved in the completed lemma. No integrality of
Chern classes, K-class or bundle existence is asserted by this region.

The correction classes here have codimension two on X, namely
{point} x S and S x {point}. A codimension-four point sheaf on X
cannot change ch_2 and is not the correction under consideration.

Completed proof:
[L047](../lemmas/L047-pure-point-bogomolov-region.md).
For z>=1, f'(z)>0, while f(1)=-1 and f(5/4)=1/64. Hence
1<lambda<5/4 and 12<8+4lambda<13. The exact integer total
threshold is -13. Symmetric rational corrections -13/2 each pass;
symmetric integer corrections pass exactly at -7 or below.
The sign obstruction is therefore removable numerically with the
same mixed action. No rank-truncation or integrality calculation for
the corrected data was performed. Actual bundle existence, stability
and transverse transport remain unresolved.

This is REPRODUCTION / ADVANCE for a relevant local numerical input,
not progress beyond the checked literature, a cycle construction or
a complete informal Hodge candidate. Consecutive mathematical
exploration usage is zero. The prior failures remain valid; the
span stays 21 and three RM directions are attained against four
required.

Exact verification used the following command from the notebook.
It reuses L046's established scaled square, checks the new endpoint
and correction values with exact fractions, and writes no script or
cache files. The strictly open root interval justifies strict signs
even when an endpoint value of the linear expression is zero.

```bash
python3 -B - <<'PY'
from fractions import Fraction as Q
import sys
sys.path.insert(0, 'scripts/cubic-kahler')
from check_eigenvector_certificate import f, polynomial_multiply

assert f(Q(1)) == -1
assert f(Q(5, 4)) == Q(1, 64)
assert f(Q(-1)) == 1

def reduce_cubic(poly):
    poly = list(poly)
    for degree in range(len(poly) - 1, 2, -1):
        coefficient = poly[degree]
        poly[degree] = Q(0)
        poly[degree - 1] -= coefficient
        poly[degree - 2] += 2 * coefficient
        poly[degree - 3] += coefficient
    return tuple(poly[:3])

square_scaled = [Q(2), Q(12), Q(4)]
for total, expected, expected_sign in [
    (Q(-12), (8, -8, 16), 'positive'),
    (Q(-13), (6, -20, 12), 'negative'),
    (Q(-14), (4, -32, 8), 'negative'),
]:
    direct = reduce_cubic(polynomial_multiply([8 + total, Q(4)], square_scaled))
    assert direct == tuple(map(Q, expected))
    endpoint_values = [8 + total + 4 * endpoint for endpoint in (Q(1), Q(5, 4))]
    if expected_sign == 'negative':
        assert max(endpoint_values) <= 0
    else:
        assert min(endpoint_values) >= 0
    assert endpoint_values[0] < endpoint_values[1]
    print(f'total correction {total}: sign {expected_sign}; scaled contraction coefficients {direct}')

assert 2 * Q(-13, 2) == -13
assert 2 * Q(-7) == -14
assert 2 * Q(-6) == -12
print('PASS: rational endpoint isolation; irrational boundary via f(+-1); integer total -13 and symmetric integer -7 thresholds.')
PY
```

The command passed. The scaled contractions for correction totals
-12,-13,-14 were (8,-8,16), (6,-20,12), (4,-32,8) in the
basis 1,lambda,lambda^2. The first sign is positive, the other two
negative. Mathematical applicability and the distinction between
numerical necessity and existence are proved in L047, not certified
by these checks.
