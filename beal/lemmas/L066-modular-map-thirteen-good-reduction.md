# L066 — Entire modular-map good reduction at thirteen

## Hypotheses

Use L033's integral model E0: y²+y=x³−x²−10x−20, its origin O,
and points 2T=(16,−61), 3T=(16,60). Use L034's complete FNS modular
map j=(a+by)/d, d=(x−16)^11, and its integral polynomial h.
The coefficients are those of Freitas–Naskręcki–Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio
Math. **156** (2020), 77–113,
[June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.26–27, including (7.4). L034's audited
coefficient certificate is the arithmetic input; no coefficients of
a different twist or translated isogeny map are substituted.

Let R=Z13 and let E/R be the projective Weierstrass model above.
For the local-field application use L064's entire algebra
K tensor_Q Q13=U12, the unramified degree-twelve field, and its
integer ring R12. No primitive integer solution, fixed sigma,
global class basis, Mordell–Weil rank/index, GRH or Selmer equality
is a hypothesis for the map certificate.

## Conclusion

j extends to an R-morphism E -> P1_R. Its special-fiber map is a
separable degree-twelve cover with complete polar divisor

    (O_bar)+11(3T_bar).

The same statements hold after base change to R12, on the entire
degree-twelve local field. In particular both x=16 charts persist:
2T_bar is regular with j=−121=9 modulo thirteen, whereas 3T_bar
has pole order eleven. There is no base point, degree loss or
inseparability defect at thirteen for this map.

This certifies one prerequisite of the general rational-j Chabauty
mechanism. It supplies no zero bound, subgroup index, translated
covering reduction, rational-point classification or integer exclusion.
Independent critical audit completed on 2026-10-14 confirms this
specialization without a mathematical correction.

## Proof

### Scope of the known method

The saved SPECIALIZE assessment covers precisely this full-chart
arithmetic check. The downstream requirement comes from Nils Bruin,
*Chabauty methods using elliptic curves*, J. reine angew. Math.
**562** (2003), 27–49,
[published author copy](https://www.cecm.sfu.ca/~nbruin/bruin_crelle.pdf),
Section 4.2, printed pp.42–45. The
[official Magma handbook, Elliptic Curve Chabauty](https://magma.maths.usyd.edu.au/magma/handbook/text/1568)
also requires good curve and map reduction at each prime above p.
Neither provides the present coefficient certificate. Only this
explicit specialization is proved; no general Chabauty theorem is
reproved or point-enumeration guarantee inferred. L034's two selected
fiber checks alone would not suffice.

### Integral curve and the affine charts

L033 gives discriminant −11^5. Direct invariant arithmetic checks it:
b2=−4, b4=−20, b6=−79, b8=−21 and
Delta=−b2²b8−8b4³−27b6²+9b2b4b6=−161051, whose residue is 6.
Hence E is smooth over R with smooth geometrically integral fibers.

Set N=a+by and N'=a−b−by. The exact integer identity from L034 is

    NN'=−d h³

in the affine curve ring. On the open where d is invertible use
[N:d] as projective target coordinates [j:1]. On the open where N'
is invertible use [−h³:N']; this is the same rational function by
the product identity and is regular even when d vanishes. On the
open where N is invertible use [N:d], equivalently reciprocal
coordinate 1/j=d/N. Each pair has a unit entry, so defines a morphism.

The entire locus x=16, over R and over every geometric residue
field, is accounted for by

    y²+y−g(16)=(y+61)(y−60),    61+60=121 in R^*.

Its two components are disjoint. Exact evaluation gives

    N(2T)=0, N'(2T)=11^22,
    N(3T)=11^22, N'(3T)=0, h(16)=11^8.

Both relevant numerator units reduce to 10 and h(16) reduces to 9.
Thus N' is invertible along 2T and N along 3T. All points of the
affine model lie in the stated opens: away from x=16, d is invertible;
on x=16 one of these two units is invertible. At 2T the regular
chart evaluates to −11^24/11^22=−121, with residue 9. It has no pole.
The relative curve derivative 2y+1 is −121 at 2T and 121 at 3T,
both units. Therefore x−16 is a uniformizer on either geometric
fiber at these points. At 3T, d/N has zero of exact order eleven
on the special fiber, because N is still a unit. This proves the
reduced pole order eleven, without using an uncancelled quotient at 2T.

### The origin chart, without division by a nonunit

In homogeneous coordinates [X:Y:Z] the curve is

    Y²Z+YZ²=X³−X²Z−10XZ²−20Z³.

On the chart Y nonzero, put t=−X/Y and w=−Z/Y. Thus away from
Z=0, x=t/w and y=−1/w, agreeing with t=−x/y. The equation is exactly

    w U=t³,    U=1+t²+(10t−1)w+20w².

At O, t=w=0 and U=1. Work on the open where U is invertible and
put V=U^−1. Then w=t³V is an identity of regular functions on this
open; V is not defined by dividing by t³. Since the derivative of
wU−t³ in w at O is one, t is a special-fiber uniformizer at O.

Write a=sum_(i=0)^11 a_i x^i and b=sum_(i=0)^10 b_i x^i. Clearing
w^11 in N gives the polynomial

    R(t,w)=sum a_i t^i w^(11−i)−sum b_i t^i w^(10−i).

Substitute w=t³V. Exact polynomial identities give

    R(t,t³V)=t^10 Q(t,V),
    (t−16t³V)^11=t^11 H(t,V),
    Q=sum a_i t^(23−2i) V^(11−i)
        −sum b_i t^(20−2i) V^(10−i),
    H=(1−16t²V)^11.

Every displayed exponent is nonnegative. As b_10=1,
Q(0,1)=−1 and H(0,1)=1, both units before and after reduction.
Shrink the origin open to make Q and H invertible. On its dense
ordinary overlap the map is j=Q/(tH). Consequently the projective
pair [Q:tH], with Q invertible, defines it on the whole origin open.
In particular 1/j=tH/Q is regular at O with exact zero order one,
and its reduced leading term is −t. No nonunit division is used
to extend the map; the cancellations merely verify its expression
on the overlap.

### Coverage, gluing, degree and base change

The affine chart Z nonzero omits only O: when Z=0 the homogeneous
equation forces X=0, so the underlying locus is [0:1:0]. The origin
open contains this whole R-section. The preceding opens therefore
cover E, not merely a finite collection of rational points or fibers.
Their morphisms agree on overlaps: each is the same j on the dense
generic ordinary locus, and equality extends since E is integral and
P1_R is separated. This yields the claimed R-morphism.

On the geometric special fiber, all affine points other than 3T are
regular for j by the affine charts. The only omitted point O has the
simple pole just computed. O and 3T remain distinct, and 2T and 3T
also remain distinct since their y-residues are 4 and 8. The full
polar divisor is therefore O+11(3T). Its degree is twelve; the degree
of a nonconstant map from a smooth projective curve to P1 is the
degree of its infinity fiber, so the reduced map has degree twelve,
equal to L034's characteristic-zero degree. Separability also follows
directly from the reduced local expression 1/j=−t+O(t²): its
differential is nonzero. Equivalently a nontrivial inseparable degree
in characteristic thirteen would be divisible by thirteen and hence
could not divide the total degree twelve. No claim of an etale cover
at the ramified cusp is made.

All units and identities persist under base change to R12. Its residue
field is F_(13^12) by audited L064, and the geometric poles and their
orders are unchanged. This is the entire K tensor Q13, not a selected
factor, and establishes the stated local-field prerequisite.

### Complete arithmetic evidence and limitations

Run `python3 scripts/modular-map-thirteen/check_reduction.py`.
The full certificate is
`scripts/modular-map-thirteen/reduction-certificate.json`.
All 20 checks pass; failures are empty. The exact conjugate-product
residual and both origin factorization residuals are zero. Complete
origin polynomials, x=16 values and all checks were inspected, not
only previews. The actual/required map degrees are 12/12, with polar
orders 1/11 as proved above. The script stores full polynomial identities;
the open-cover, gluing and valuation arguments are this proof, rather
than claims deduced from selected finite-fiber computations.

This is a REPRODUCTION of assessed explicit chart methods, not a new
Chabauty theorem or a claimed advance beyond the checked sources.
Unconditional rank below twelve, sufficient global points or subgroup
index control, coset-wise rationality zero tests, translated isogeny
covering reduction, other classes and global primitive power lifting
remain independent gaps. L062's fixed local-class survivor is neither
removed nor promoted to a global primitive power triple.

### Independent critical audit, completed 2026-10-14

Run `python3 scripts/modular-map-thirteen/audit_reduction.py`.
The independent replay imports or executes no construction code. It uses
the source-audited L034 coefficient lists as input, compares every a,b,g,d,h
coefficient with the L066 certificate, multiplies the two source factors
of b, and computes the complete integer residual a²−ab−b²g+dh³. Sparse
integer polynomial arithmetic gives the zero polynomial, not just values
on selected fibers. It independently homogenizes a,b,d, substitutes
(t,w)=(t,t³V), and compares every coefficient of Q and H. Substitution in
the homogeneous Weierstrass equation verifies its sign and the entire
wU=t³ identity. The full product, factorization and origin residuals are
zero. All 36 checks pass, with no failures; the complete evidence is in
`scripts/modular-map-thirteen/audit-certificate.json`. The full relevant
polynomials, residuals, units and orders were inspected.

The scheme-open coverage needs more than this arithmetic. For any prime
ideal of the affine R-curve ring, either x−16 is absent and d is a unit
locally, or that prime lies on x=16. On the latter closed subscheme the
factorization (y+61)(y−60)=0, with difference 121 a unit in R, identifies
the coordinate ring with R×R. This includes the generic points of both
sections and their geometric specializations. On the first component
N'=11²² is a unit; on the second N=11²² is a unit. Thus D(d), D(N'), D(N)
cover the affine scheme, rather than only its F13-points. Their target
pairs have a unit coordinate and agree by NN'=−dh³ wherever compared.

The complement of Z nonzero in the projective model has underlying
support X=Z=0, since the homogeneous equation at Z=0 is X³=0.
Although that hyperplane intersection need not be reduced, an open cover
is a statement about points, so its support is what must be covered.
On the entire origin section U=1, V=1, Q=−1 and H=1. Hence the Y-chart
open D(U) intersected with D(QH), where Q,H are evaluated at V=U^−1,
contains every point omitted by the affine chart. V is a regular inverse
of a unit on this open; no division by t or w defines it. The identities
R(t,t³V)=t¹⁰Q and (t−16t³V)¹¹=t¹¹H are used only to compare rational
functions on a dense overlap. The actual morphism there is [Q:tH],
which has unit first coordinate even at t=0.

For gluing, the unit discriminant gives a smooth, flat projective curve
over the DVR R. Its geometrically integral generic fiber is dense by
flatness, and smoothness makes the total scheme reduced; consequently
E is integral. Every nonempty overlap is therefore reduced and has the
generic ordinary locus schematically dense. The equalizer of two maps
to the separated target P1_R is closed, and equality on that dense
locus implies equality as morphisms on the overlap. This verifies the
integrality and separatedness hypotheses in the original gluing argument.

On the geometric special fiber, d is nonzero at every finite point away
from x=16. At its two points the derivatives 2y+1 have residues 9 and 4,
so x−16 is a local parameter. The first has a regular finite j-value
9; the second has 1/j=(x−16)¹¹/N with N a unit. At O the implicit
w-derivative of wU−t³ is 1, so t is a local parameter and
1/j=tH/Q has leading coefficient −1. These computations account for
every geometric point, giving poles of exactly 1 and 11 and no others.
For a nonconstant map of smooth projective integral curves, the pullback
of infinity has degree the function-field degree; here it is 12, the
same as L034's characteristic-zero degree. The simple zero of 1/j at O
has nonzero differential, proving separability (also 13 does not divide
12). Neither a selected fiber nor the curve discriminant alone is used
to establish map reduction.

Finally, audited L064 supplies the entire field U12 and its integer
ring R12 with residue field F_(13^12). Pullback of this open cover and
these morphisms along R -> R12 preserves every displayed identity and
unit. Over an algebraic closure the special fiber and the two local
parameters are the same, so no additional pole, degree loss or change
of orders occurs. This uses the whole local field, without selecting a
factor or choosing sigma. The audit confirms the original certificate;
it establishes no new point bound or conclusion beyond the assessed
specialization. The rank/index, translated-map, zero-bound, other-class
and global primitive-power gaps stated above are unchanged.

## Mathlib

Full matching explicit integral modular-map chart certificate and its
unramified-field specialization: **not checked**. Supporting scheme
gluing, curve degree/polar divisor and separability coverage: **not
checked**. Unknown coverage is not absence. The source coefficients
and existing integral model are reused from the audited local inputs.
