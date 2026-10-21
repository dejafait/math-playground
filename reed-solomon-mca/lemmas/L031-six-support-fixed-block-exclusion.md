# L031 — Six equality supports cannot lie in eight coordinates

## Hypotheses

Let F be a finite field containing a multiplicative subgroup H of order
sixteen, and let C be the degree-less-than-eight evaluation code on H.
For arbitrary a,b in F^H use L010's moments and affine syndrome pencil
\[
 \sigma_j(z)=\sum_{x\in H}z_xx^j,\qquad
 s(T)=\sigma(a)+T\sigma(b),\qquad 1\le j\le8.
\]
Assume L010's hypotheses: its Hankel determinant D and all sixteen
coordinate locators are nonzero polynomials. Assume also its equality
case: there are sixteen bad finite parameters for the pinned event at
1/4<=delta<5/16. L010 supplies their unique full-weight four-error
representatives, sixteen distinct supports, and exactly four supports
containing each coordinate.

Choose any six of these distinct parameters gamma_1,...,gamma_6, write
their error representatives as e_1,...,e_6, and put
\[
 A_i=\operatorname{supp}(e_i),\qquad U=\bigcup_{i=1}^6 A_i.
\]
In particular sigma(e_i)=s(gamma_i) and each indicated weight on A_i is
nonzero. All weights and parameters may lie anywhere in F.

## Conclusion

The union U has size at least nine. Thus six distinct full-weight
four-error supports whose union has size at most eight cannot occur
in L010 equality, over any allowed field or coordinate labeling.

This is a conditional equality obstruction, not a theorem that every
abstract family has such a cluster. It gives no uniform fifteen-count
bound; the frozen model's global interval remains 11/q–16/q, and its
identification with the ABF26 challenge remains unresolved.

## Proof

Suppose |U|<=8. Choose an eight-element set B with U subset B subset H;
this is possible even when |U|<8 because |H|=16. Order its coordinates
and form the constant matrix
\[
 M_B=(x^j)_{1\le j\le8,\ x\in B}.
\]
L010's established eight-column moment invertibility applies to B:
its coordinate labels are distinct and nonzero. Define the polynomial
vector
\[
 f(T)=M_B^{-1}s(T)\in F[T]^B.                         \tag{1}
\]
Every f_x has degree at most one. This is the fixed-block inverse used
in L024, now on an arbitrary enlargement B; it does not posit an affine
lift of codewords or sparse errors at other parameters.

For each selected i the error e_i is supported in U subset B. Hence
M_B(e_i|_B)=sigma(e_i)=s(gamma_i). Inverting M_B gives
\[
 f(gamma_i)=e_i|_B\qquad(1<=i<=6).                    \tag{2}
\]
This verifies the affine lift only against the six actual errors, as
needed, including the smaller-union case. Coordinates in B minus U
vanish at all six selected parameters; nothing requires them to be
nonzero or their values to be actual errors elsewhere.

Fix x in U. L010's equality incidence says that x occurs in exactly
four of the sixteen supports. It therefore occurs in at most four of
the six selected supports, and is absent from at least two, say A_i
and A_j with i!=j. Equation (2) gives
f_x(gamma_i)=f_x(gamma_j)=0. Write f_x(T)=alpha+beta*T.
Subtracting these two equations yields
beta*(gamma_i-gamma_j)=0. The parameters are distinct in the field,
so beta=0 and then alpha=0. Thus f_x is identically zero.

But x in U means x belongs to some A_k. Its full-weight error satisfies
e_k(x)!=0, whereas (2) and f_x=0 give e_k(x)=0, a contradiction.
U is nonempty because every A_i has four elements, so such an x exists.
This proves |U|>=9.

Only L010's moment invertibility, syndrome/error correspondence and
equality incidence are mathematical inputs. L024 supplies the already
used lifting mechanism as motivation, rather than an additional theorem
premise. No determinant is divided by D(gamma_i); indeed equality already
gives D(gamma_i)!=0. Identically zero affine coordinates are treated by
the same contradiction, and the argument is valid over every extension
field satisfying the hypotheses. It makes no prime-field, normalization,
matching-number or disjoint-triple assumption.

The underlying standard distance input is J. I. Hall, *Notes on Coding
Theory*, GRS chapter, Theorem 5.1.1, printed pp. 63–64, undated
author-hosted copy retrieved 2026-10-05
([primary PDF](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)).
Its hypotheses allow any field, distinct evaluation points, nonzero
column multipliers and 0<k<=n. Here H gives sixteen distinct points,
all multipliers are one and k=8, so the cited distance is nine.
That result and L010's existing linear algebra are reused, not reproved.
Hall does not supply the conditional six-support passage; equations
(1)–(2) and the two-zero contradiction justify this specialization.
This is recorded as REPRODUCTION under the approved assessment, without
claiming novelty or progress beyond the unread ePrint 2025/1712.

### Critical audit, 2026-10-06

The separate critical audit found no defect in the conditional statement
or its proof. The complete L010 proof and the pinned event in
foundations/02 were checked against the uses above. The following records
the load-bearing checks; it does not strengthen the conclusion.

For the stated radius cell, 16(1-delta) lies in (11,12], so the integer
agreement threshold is exactly twelve. Thus an actual bad parameter has
an error supported on at most four coordinates. L010's kernel identity
uses only subgroup sums in degrees 1 through 15 and the eight-column
Vandermonde determinant. For any ordered B=(x_1,...,x_8), that determinant
is (product x_i)(product_{i<j}(x_j-x_i)), which is nonzero. All eight
moments have indices 1 through 8; their nonzero column factors must be
retained when using an unshifted Vandermonde matrix.
The cited Hall distance-nine theorem ensures uniqueness of each sparse
representative. Its hypotheses apply over F itself, including every
allowed extension, without requiring prime-subfield weights.

The equality incidence used here was also checked, rather than assumed
from an abstract balanced family. L010's rank factorization at a
weight-w error makes every four-by-four minor divisible by
(T-gamma)^(4-w) for w<=3: in each determinant term of smaller degree,
more than w rows come from the rank-at-most-w constant matrix and are
dependent. Therefore these parameters cost respectively 16,32,48,64
locator-root multiplicities for weights 3,2,1,0. A full-weight four-error
has nonzero D(gamma), and its locator is D(gamma) times the product of
its four distinct coordinate factors; its cost is at least four.
Sixteen nonzero locators each of degree at most four have total capacity
64. Sixteen bad parameters exhaust that capacity, exclude every lower
weight, and leave exactly four distinct support incidences per coordinate.
This argument includes singular parameter values before equality rules
them out; it does not discard them as exceptional cases.

L010's identification of decodability with badness respects input failure
on the same agreement support. If b agreed with a codeword off an error
support A, its syndrome would have a representative on A; together with
the actual error this represents the entire pencil on A. For |A|<=3
this contradicts D nonzero as a polynomial, and for |A|=4 it contradicts
the nonzero coordinate locators. The same fixed-support argument excludes
two different parameters with the same four-element support. No converse
decoder assumption or abstract-support realization is needed by L031.

For the local step, H has enough distinct coordinates to enlarge every
U of size at most eight to B. The inverse M_B is constant over F, so
every coordinate in (1) is affine, including coordinates identically
zero. Each actual e_i is supported on B and has all eight required
moments, so invertibility proves (2) without constructing codewords
affinely or making a claim about errors at unselected parameters.
For x in U, global four-incidence implies at least two absences among
the six selected, distinct finite parameters. Their nonzero difference
is invertible in any field. Consequently the two zeros force f_x=0;
an occurrence of x among the six then contradicts its actual nonzero
weight. Added coordinates in B minus U need no nonvanishing condition.
No division by a parameter-dependent determinant, projective change of
parameters, assumption on syndrome-span dimension, or coordinate-label
symmetry enters this argument.

The direct mathematical input remains L010; the reference to L024 is
mechanism reuse only. The audit requires no finite calculation or
additional external theorem. It establishes confidence in this existing
local reproduction, not a new theorem or progress beyond the inspected
sources. In particular, ATTEMPTS/017's obstruction to universal cluster
extraction remains: this audit supplies no cluster-existence premise,
global fifteen bound, ABF26 identification, or stronger-source comparison.

## Mathlib

Coverage of this exact conditional obstruction and its affine-lifting
ingredients in Mathlib is **not checked**. No matching theorem, absence
claim or Lean verification is asserted. The proof uses the canonical
L010 inputs and elementary affine root counting as written above.
