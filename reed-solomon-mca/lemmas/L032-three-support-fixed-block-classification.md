# L032 — Conditional three-support incidence and weight classification

## Hypotheses

Let F be a finite field containing a multiplicative subgroup H of order
sixteen, and let C be the degree-less-than-eight evaluation code on H.
For a,b in F^H use L010's eight shifted moments
\[
 \sigma_j(z)=\sum_{x\in H}z_xx^j,\qquad
 s(T)=\sigma(a)+T\sigma(b),\qquad 1\le j\le8.
\]
Retain the pinned radius cell 1/4<=delta<5/16, L010's nonzero polynomial
Hankel determinant D and all nonzero coordinate-locator polynomials,
and its equality hypothesis of sixteen bad finite parameters.

Choose three distinct such parameters gamma_1,gamma_2,gamma_3 in F,
with their actual unique errors e_1,e_2,e_3. Put A_i=supp(e_i),
U=A_1 union A_2 union A_3 and m=|U|, and assume m<=8.
L010 gives |A_i|=4, every weight on A_i nonzero, the A_i distinct,
and sigma(e_i)=s(gamma_i). All labels, parameters and weights are
retained over F; no prime-subfield descent is assumed.

## Conclusion

Every such triple has one of the following two incidence patterns:

| m | Common intersection K | Z_i=U minus A_i | Pair intersection |
| --- | --- | --- | --- |
| 5 | two coordinates | three pairwise disjoint singletons | three coordinates |
| 6 | empty | three pairwise disjoint two-sets partitioning U | two coordinates |

In either row, U is the disjoint union of K,Z_1,Z_2,Z_3 and
A_i=K union Z_j union Z_k for {i,j,k}={1,2,3}. In particular every
coordinate in U occurs in two or three selected supports; union sizes
seven and eight cannot occur. This does not assert that either row has
a completion to sixteen-count equality.

The exact local weight relations are as follows. There is a unique affine
vector f(T)=u+Tv supported in U taking values e_i at gamma_i.
For x in Z_i there is c_x in F^* such that
\[
 e_i(x)=0,\qquad e_j(x)=c_x(\gamma_j-\gamma_i)
       \quad(j\ne i),\qquad f_x(T)=c_x(T-\gamma_i).       \tag{1}
\]
For x in K, f_x is an arbitrary affine polynomial subject to
f_x(gamma_i)!=0 for all three i, and its three values satisfy
\[
 (\gamma_2-\gamma_1)e_3(x)
   =(\gamma_2-\gamma_3)e_1(x)
     +(\gamma_3-\gamma_1)e_2(x).                       \tag{2}
\]
Nonzero constants on K are allowed. Thus for j,k different from i,
\[
 \frac{e_j(x)}{e_k(x)}
       =\frac{\gamma_j-\gamma_i}{\gamma_k-\gamma_i}
       \quad(x\in Z_i).                              \tag{3}
\]
Equations (1) and (2), with the stated nonvanishing, are also sufficient
for precisely these three full-weight vectors to be values of an affine
vector on U. Consequently their eight moment vectors lie on the same
affine parameterized line. If their moment vectors at the first two
selected parameters equal those of a specified pencil s, the third
vector does also. This converse asserts local
affine/moment compatibility only; it does not establish locator
nonpersistence, same-support badness, or sixteen-error completion for an
arbitrary constructed triple. The coefficient vectors u,v and their
syndromes are linearly independent.

For the m=5 row, the whole syndrome pencil is represented on U. Under
L015's additional hypotheses F=F_(97^20) and H the order-sixteen subgroup
of F_97^*, its bound |B(a,b)|<=5+M(U) therefore applies, requiring M(U)>=11
for equality. No M(U) value or finite-certificate verification is claimed
here. The m=6 row falls outside that five-coordinate hypothesis. No
universal small-union extraction or global fifteen bound follows.

## Proof

### Reuse of the affine mechanism and exact incidence specialization

Use L010's invertibility of any eight shifted-moment columns. As in the
already written fixed-block construction in L031, enlarge U to an
eight-set B inside H, put M_B=(x^j)_(1<=j<=8,x in B), and set
f_B(T)=M_B^(-1)s(T). This is an affine polynomial vector over F.
For each selected i, M_B(e_i|_B)=s(gamma_i), so invertibility gives
f_B(gamma_i)=e_i|_B. Each coordinate of B minus U vanishes at two distinct
selected parameters and hence is identically zero. Extend f_B by zero
outside B to get f(T)=u+Tv supported in U. Its moments are s(T) as a
polynomial identity. Its values at the selected parameters are e_i.
Two distinct evaluations uniquely determine an affine vector, so this
lift is unique. No values at other parameters are assumed to be errors.

For x in U, some selected error has a nonzero x-weight. Thus f_x is a
nonzero affine polynomial. Reuse the scalar-affine zero accounting from
L006/L007: such a polynomial has at most one finite zero, including the
case of a nonzero constant with none. A coordinate cannot be absent from
two selected supports. Equivalently the sets Z_i=U minus A_i are
pairwise disjoint. Each has size m-4, whence
\[
 3(m-4)\le m,\qquad m\le6.                            \tag{4}
\]
Since the distinct A_i all have size four, m>=5. Every coordinate outside
the disjoint Z_i belongs to all A_i, so K=U minus their union is their
common intersection and
\[
 |K|=m-3(m-4)=12-2m.                                  \tag{5}
\]
This yields the two rows. For i!=j, the pair intersection is U minus
(Z_i union Z_j) and has size m-2(m-4)=8-m. All incidence claims follow;
no classification of the remaining thirteen supports was used.

### Weights, actual rank, and the limited converse

For x in Z_i, the nonzero f_x vanishes at gamma_i, so its slope c_x is
nonzero and f_x(T)=c_x(T-gamma_i). Evaluation proves (1) and (3);
every denominator in (3) is nonzero by the full weights and distinct
parameters. On K all three evaluations are nonzero. The unique affine
interpolation through the first two gives (2), with no normalization of
the parameters and no restriction on the field characteristic. Conversely
(2) says exactly that the third value equals that interpolation. One can
choose any nonzero first two values on K for which this third value is
nonzero; this includes a constant choice.

For the converse take either displayed partition, arbitrary nonzero c_x
on each Z_i, and affine polynomials on K nonzero at all three parameters.
Define f_x by (1) on the Z_i, by these polynomials on K, and by zero
outside U. At gamma_i it vanishes exactly on Z_i within U, so the
resulting e_i=f(gamma_i) has support A_i and full weight four. Equations
(1) and (2) characterize all such choices, by the necessity just proved.
Linearity of sigma gives sigma(f(T))=sigma(u)+T sigma(v). Agreement of
this affine moment vector with a specified s at the first two distinct
parameters forces polynomial agreement, hence the third value as well.
This proves only the stated local converse. Additional equality gates
are not consequences of this construction.

Both Z_1 and Z_2 are nonempty. Choose x in Z_1 and y in Z_2. In the
coefficient rows u,v, their columns are
c_x*(-gamma_1,1) and c_y*(-gamma_2,1). Their determinant is
c_x*c_y*(gamma_2-gamma_1)!=0. Thus u,v have rank two. The moment map
is injective on vectors supported in U, because |U|<=8 and L010's eight
columns are independent. It follows that sigma(u),sigma(v) are independent
as well. Identically zero coordinates were removed before this rank
claim; repeated directions inside each Z_i cause no difficulty.

### Five-coordinate comparison and precise standard inputs

When m=5, the identity sigma(f(T))=s(T) represents both sigma(a) and
sigma(b) on U. For F and H exactly as in L015, all its other hypotheses
are inherited from L010. Apply L015 with its five-set A=U to obtain
16=|B(a,b)|<=5+M(U). This is precisely the required threshold M(U)>=11.
Its accompanying enumeration reports maximum six, but that certificate
was neither reexecuted nor audited in this step and is not used here as
an additional proved bound. L015 supplies no such reduction for a six-set
or arbitrary fields. The field-uniform incidence and weight proof above
does not depend on that finite configuration.

The standard RS distance input already used in L010 is J. I. Hall,
*Notes on Coding Theory*, GRS chapter, Theorem 5.1.1, printed pp. 63–64,
undated author-hosted copy retrieved 2026-10-05
([primary PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)).
Its hypotheses allow any field, distinct evaluation points, nonzero
multipliers, and 0<k<=n; H and multipliers one with n=16,k=8 qualify,
giving distance nine. The distance and moment arguments are reused,
not reproved. L031's construction and L006/L007's root accounting are
mechanisms reused from their proofs, not applications of their global
bounds. The direct local theorem inputs are L010 and, solely for the
field-specific final threshold, L015.

R. P. M. J. Jurrius, *Codes, arrangements, matroids, and their polynomial
links*, Eindhoven PhD thesis (2012), Proposition 4.2, printed pp. 33–35,
DOI [10.6100/IR734704](https://doi.org/10.6100/IR734704)
([version-of-record PDF](https://pure.tue.nl/ws/portalfiles/portal/102837385/734704.pdf)),
gives the indexed-column-hyperplane interpretation of zero coordinates
for a full-row-rank generator of a nondegenerate finite-field linear code.
Here dropping coordinates outside U and the rank-two check above meet
those hypotheses for the generator with rows u,v. A message (1,gamma_i)
has precisely Z_i as its zero coordinates; repeated column hyperplanes
remain indexed. This supplies the known interpretation of the accounting,
not an imported classification or an essential extra theorem premise.
The only new derivation is this conditional three-point specialization,
recorded as REPRODUCTION under the prior SPECIALIZE assessment; no
originality or progress beyond the unread stronger sources is claimed.

### Critical audit, 2026-10-07

The separate critical audit found no defect in the stated conditional
classification, local converse or field-specific analytic threshold.
It checked the whole proof above, L010's load-bearing moment, locator,
multiplicity and same-support passages, and L015's analytic proof through
its threshold. It did not use L015's reported finite maximum. The checks
below validate the existing specialization; they add no stronger bound.

For the pinned event, 1/4<=delta<5/16 gives
11<16(1-delta)<=12, hence exactly the agreement threshold twelve.
L010's kernel calculation uses subgroup sums with exponents 1 through
15. For any ordered eight-set B=(x_1,...,x_8), the shifted-moment
determinant is (product x_i)(product_{i<j}(x_j-x_i)), nonzero because
all labels are nonzero and distinct. The shift by one is retained.
The kernel is the dimension-eight evaluation code, and its distance
nine gives uniqueness of an error of weight at most four. These facts
hold over F itself, without descent of the error weights.

The equality premises also survive inspection. At a full-weight
four-error, L010's factorization gives
D(gamma)=det(V)^2 product_{x in A}(e_x x)!=0 and locator
D(gamma) product_{x in A}(X-x). At a weight-w error with w<=3,
each four-by-four minor has order at least 4-w at the parameter:
every lower-order determinant term uses more than w rows of the
rank-at-most-w constant matrix. The sixteen coordinate locators thus
charge at least 16(4-w) multiplicities to such a parameter, versus four
for weight four, within total degree at most 64. Sixteen bad parameters
force all errors to have weight four and exhaust the degrees. No
singular parameter was discarded to obtain this conclusion.
Same-support badness is justified because agreement of b with a
codeword off an error support would represent the entire pencil on
that support, forcing D=0 or a persistent coordinate locator. Two
distinct parameters with the same four-support give that same
contradiction by subtracting their moment equations. Thus the actual
errors used here have full weights and distinct supports, as required;
these properties were not inferred from abstract incidence alone.

The enlargement U subset B is always available. The inverse matrix is
constant, so the lift is affine even at parameters where a locator
matrix could be singular. Coordinates in B minus U vanish at the first
two distinct parameters and are identically zero. On U, an occurrence
in one selected error excludes an identically zero coordinate. A
nonzero constant has no zeros; a nonconstant affine coordinate has at
most one. Thus the three absence sets really are pairwise disjoint,
not merely disjoint in a generic case. Their sizes m-4 and distinctness
of the four-supports give 5<=m<=6. The remaining common coordinates
number 12-2m, and pair intersections number 8-m. This exhausts the
possibilities without any assumption about the other thirteen errors.

For the weight relations, interpolation at gamma_1 and gamma_2 has
denominator gamma_2-gamma_1, which is nonzero. Multiplication by this
difference yields exactly (2), including its signs. A coordinate
absent at gamma_i has nonzero slope, and both gamma_j-gamma_i and
gamma_k-gamma_i in (3) are nonzero. Conversely, the displayed partition
and those weights make the zero coordinates within U exactly Z_i at
gamma_i; the common coordinates stay nonzero by the explicitly stated
condition. There are therefore exactly four nonzero coordinates at
each selected parameter. Equality of two affine moment polynomials at
the first two parameters implies their identity in F[T], not just
agreement at the third point. None of this verifies nonpersistence or
badness for an arbitrary triple from the converse. In either partition
Z_1,Z_2 are nonempty, and their coefficient-column determinant is
c_x c_y(gamma_2-gamma_1), with the stated sign. Moment injectivity on
the fixed subspace F^U then preserves the independence of u and v;
no assertion of injectivity on differences of arbitrary sparse words
is being made. Removing zero columns and this rank check also justify
the cited indexed-hyperplane interpretation, with constants and repeated
hyperplanes allowed.

Finally, in the five-coordinate row both coefficient syndromes are
represented on U by the polynomial identity, so L015's five-set
hypothesis holds. Its field hypotheses are separately required:
F=F_(97^20) and H subset F_97^*. In its analytic argument every
coordinate of the lift is a nonzero polynomial; otherwise the pencil
would be represented on at most four coordinates, contradicting D or
locator nonvanishing. At most five finite parameters cancel such a
coordinate. Away from those parameters the lift has weight five.
Any sparse representative must have weight four and support K disjoint
from U: every other case makes their nonzero difference a codeword of
weight at most eight. The difference is a scalar multiple of the
degree-seven product on (H minus U) minus K. Thus its values on U
give exactly L015's rational projective point p_K. Conversely these
values produce a full-weight four-error, and L010 supplies same-support
failure under its nonvanishing hypotheses.

Independent u,v make gamma -> [u+gamma v] injective. Distinct K give
distinct points: equality of their projective evaluations on U would
give a degree-less-than-eight codeword supported on K union K', of
size at most eight, forcing equality of the two polynomials up to
scale and hence equality of their root sets. A line over F through
two distinct rational points is the base extension of their F_97-line.
Its rational vectors lie in their F_97-span: solve for the two
coefficients using any invertible two-row minor of the rational point
matrix. Lines containing fewer than two configuration points satisfy
the same bound since this distinct 330-point configuration has M(U)>=2.
Consequently the number of external parameters is at most M(U), and
16<=5+M(U) gives precisely M(U)>=11. This checks the extension-field
passage rather than presuming rational input weights. No finite
enumeration value, six-coordinate extension or field-uniform version
of that import has been used.

The direct inputs remain L010 and L015, and the standard citations above
are reused with their recorded hypotheses. No new external theorem,
mathematical computation, universal cluster extraction, or all-sixteen
completion is supplied. The global interval remains 11/q–16/q; this
audit validates a local reproduction rather than progress beyond the
sources already assessed.

## Mathlib

Coverage of this exact classification, its local converse, and Jurrius's
arrangement statement is **not checked**. No matching Mathlib theorem or
absence claim is asserted. The cited standard inputs and local informal
proofs supply the present argument; no Lean verification is claimed.
The separate critical audit above found no defect. Arbitrary-family equality,
all-sixteen compatibility, the global fifteen bound, and ABF26
identification remain unresolved.
