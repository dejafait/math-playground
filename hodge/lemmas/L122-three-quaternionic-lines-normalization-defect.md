# L122 — Three quaternionic lines have normalization defect four

## Hypotheses

Equip H^2 with its flat product metric and the standard componentwise
ordered hyperkähler triple I,J,K. Fix I, so H^2 is C^2_x x C^2_y.
Consider the reduced union V of the three quaternionic lines

\[
 V_1=H\times0,\qquad V_2=0\times H,\qquad
 V_3=\{(u,u):u\in H\}.
\]

Write S=C[x_1,x_2,y_1,y_2], m=(x_1,x_2,y_1,y_2), and

\[
 I_1=(y_1,y_2),\quad I_2=(x_1,x_2),\quad
 I_3=(y_1-x_1,y_2-x_2),\quad I=I_1\cap I_2\cap I_3.
\]

The scheme structure is S/I. At the origin let A=(S/I)_m,
let m_A be its maximal ideal, and let P_i=I_i S_m/I S_m.
The same formulas below apply to the convergent analytic germ and the
completed germ, by using convergent or formal power series respectively.

This is an independent flat model of selected local consequences of
L118/L120/L121. Their actual conditional K3 family is not a hypothesis
or a mathematical input to the calculation. No F, global connected K3
normalization, prescribed Chern tensor or nonflat K3 metric is asserted.

## Conclusion

The normalization of A is

\[
 T=\prod_{i=1}^3 C[z_1,z_2]_{(z_1,z_2)}.
\]

Under the restriction map F -> (F(z,0),F(0,z),F(z,z)), A consists
exactly of triples (a,b,c) satisfying

\[
 a(0)=b(0)=c(0),\qquad dc(0)=da(0)+db(0).                \tag{1}
\]

Consequently Q=T/A has length four, not r-1=2 for r=3. More precisely,

\[
 \dim_C(Q/m_AQ)=2,\quad \dim_C(m_AQ)=2,\quad m_A^2Q=0.   \tag{2}
\]

Every pair has reduced scheme-theoretic intersection at the origin:
P_i+P_j=m_A for i!=j. Nevertheless every simultaneous identity needed
for the multicross gluing fails:

\[
 P_i+\bigcap_{j\ne i}P_j=P_i+m_A^2\ne m_A.              \tag{3}
\]

The normalization is finite and unramified and is an isomorphism away
from the origin, component by component. Its source branches are smooth,
quaternionically immersed and totally geodesic; their parameters can all
have the same constant metric scale. Its off-diagonal fibre product has
exactly six reduced ordered points, with a clopen diagonal.

Thus these selected flat local branch properties do not imply defect
r-1. This does not determine the quotient for the actual image in L120,
exclude its F, or refute an implication using its additional K3 metric
or global hypotheses. This is NEGATIVE / RESEARCH / REPRODUCTION under
the approved specialization, not a mathematical originality claim or a
Hodge-conjecture counterexample. The separate critical audit below
preserves this limited conclusion without a stronger result.

## Proof

**Scope, sources and why compute.** The pre-invocation SPECIALIZE assessment
is `drafts/literature/2026-10-17-three-quaternionic-lines-gluing-test.md`.
Its inspected primary coverage is reused without a new literature turn.
The general simultaneous-union and multicross criteria are imported from
Leahy--Vitulli, *Seminormal rings and weakly normal varieties*, Nagoya
Math. J. 82 (1981), Propositions 2.18--2.23, pp. 46--50,
[DOI](https://doi.org/10.1017/S0027763000019279), and *Weakly normal varieties:
The multicross singularity and some vanishing theorems on local cohomology*,
Nagoya Math. J. 83 (1981), Lemma 3.4, sequence (3.3), Theorem 3.5,
pp. 141--144, [DOI](https://doi.org/10.1017/S0027763000019450).
Vitulli's *Corrections to “Seminormal rings and weakly normal varieties”*,
Nagoya Math. J. 107 (1987), pp. 148--149, 157,
[DOI](https://doi.org/10.1017/S0027763000002592), preserves the later union
criteria; the corrected function-theoretic characterization is not used.
Their general criteria are not reproved here. The explicit quotient and
the applicability checks for this chosen arrangement are the identified
specialization not already supplied by those citations. The parent source
comparison checked local duplicates and the stopped Hom inference; no
matching computation was identified, without inferring novelty.

**The entire restriction image.** Work first with polynomials. Each I_i
is prime, the three are incomparable, and their intersection I is radical.
Hence V is reduced with precisely these three components. Restriction
embeds S/I into T_0=C[z_1,z_2]^3, since its kernel is exactly I.
The constant and linear parts of any ambient F give (1).

Conversely, suppose a,b,c are polynomials satisfying (1), with common
constant d. The polynomial F_0=a(x)+b(y)-d has restrictions a,b on
V_1,V_2, and restriction a(z)+b(z)-d on V_3. Therefore the remaining
diagonal discrepancy

\[
 q(z)=c(z)-a(z)-b(z)+d
\]

belongs to n^2, where n=(z_1,z_2). Write
q=z_1 q_1+z_2 q_2 with q_1,q_2 in n. This is possible since
n^2=(z_1^2,z_1z_2,z_2^2). Then

\[
 F=F_0+x_1q_1(y)+x_2q_2(y)                             \tag{4}
\]

has restrictions exactly (a,b,c): the correction vanishes at y=0
because q_i(0)=0, vanishes at x=0, and restricts to q on the diagonal.
Thus (1) is sufficient. This construction also works for local rational
functions regular at the origin, convergent series and formal series:
q in n^2 has such a decomposition in each ring, and the substitutions
in (4) stay in that ring. In particular there is no convergence assumption
on a formally chosen series and no finite-jet extrapolation.

For homogeneous polynomials the image has dimension one in degree zero
(target dimension three), dimension four in degree one (target dimension
six), and is surjective in every degree d>=2. For the latter assertion,
(4) applies with homogeneous q_i of degree d-1; it treats every degree,
with no last computed degree standing for the tail.

**Normalization.** The finite product T_0 is a finite S/I-module: each
factor is a cyclic quotient (S/I)/(I_i/I), and there are three factors.
It is integrally closed in the product of its fraction fields. The
image calculation also gives n^2 x n^2 x n^2 contained in S/I.
In particular d_0=(z_1^2,z_1^2,z_1^2) belongs to S/I; an ambient
representative is x_1^2+y_1^2-x_1y_1. It is a nonzerodivisor because
its restriction is nonzero in each of the three domain factors.
For any t in T_0, d_0t has all components in n^2, so d_0t lies in S/I.
Thus T_0 embeds into the total quotient ring of S/I. Conversely that
total quotient ring embeds into the product of the three fraction
fields: a nonzerodivisor has nonzero restriction on every component.
For this last assertion, if its ith restriction were zero, multiplication
by the nonzero tuple supported on the ith component with entry z_1^2
(which lies in S/I) would make it a zero divisor.

Finiteness makes T_0 integral over S/I. If an element of the total
quotient ring is integral over S/I, its monic equation is also over T_0;
componentwise integral closedness puts that element in T_0. This proves
that T_0 is the normalization. Localizing above the origin gives the
stated T: the projection of the multiplicative set S\m onto each branch
contains every polynomial nonzero at its origin. The same argument with
power-series rings proves the analytic and completed normalization
identifications directly, using the standard theorem that regular local
rings are normal for the component power-series rings.

**The full length and module filtration.** The C-linear map

\[
 T\longrightarrow C^2\oplus (C^2)^*,\qquad
 (a,b,c)\longmapsto
 (a(0)-b(0),\ c(0)-a(0),\ dc(0)-da(0)-db(0))            \tag{5}
\]

is surjective: constant triples supply the first two coordinates and
triples (0,0,l(z)) with l linear supply the last two. Its kernel is A
by (1) and (4). Thus Q has C-dimension four. Map (5) is used as a
C-linear map, not as an A-linear identification with a trivial module.

The product n^2 x n^2 x n^2 is contained in A, so m_A^2Q=0.
Multiplication by m_A gives classes with zero constant discrepancies,
whose space is the two-dimensional linear discrepancy in (5). Both
linear generators occur: multiply the class of (0,0,1) by x_i to get
the class of (0,0,z_i), for i=1,2. Hence m_AQ is precisely this
two-dimensional space, proving (2). Each quotient in that filtration
is a vector space over A/m_A=C; its length is its C-dimension.
The total length is therefore 2+2=4. The quotient is supported only at
the origin, because this same computation globally gives m^2Q=0.

**Pairwise and simultaneous scheme conditions.** Directly from the
displayed ideals, I_i+I_j=m for each distinct pair. Thus each pairwise
intersection is Spec C, with no nilpotents. To compute a simultaneous
sum, restrict I_j intersection I_k to V_i. It has no constant term.
It also has no linear term: the linear spaces of generators of I_j
and I_k have intersection zero, for every distinct j,k. Its restriction
is consequently contained in n^2.

For i=1, the elements x_a(x_b-y_b), a,b in {1,2}, belong to
I_2 intersection I_3, and restrict to z_a z_b. For i=2, use
y_a(y_b-x_b) in I_1 intersection I_3. For i=3, use x_a y_b in
I_1 intersection I_2. In every case the restriction ideal contains
all generators of n^2, so it equals n^2. Its inverse image in S_m is
I_i S_m+m^2 S_m, proving (3). The corresponding quotient is
C[z_1,z_2]_(z)/(z_1,z_2)^2, of length three, whereas S_m/m has length
one. These sums are strictly smaller than m_A, despite all pair sums
being m_A.

In the completed ring, every branch quotient is regular, the common
radical of the pair sums is the prime m_A, and the common quotient is C,
which is regular. These are the ancillary hypotheses of the inspected
Leahy--Vitulli Lemma 3.4. The simultaneous identities themselves fail,
so its multicross gluing and sequence (3.3) cannot be assigned to this
model. The union criterion fails in the same concrete way: V_1 union
V_2 has no linear defining equations, and hence tangent space C^4 at
zero, while T_0V_3 has complex dimension two and is contained in it.
Their tangent intersection is not the zero tangent of their common
reduced point. This checks the preceding-union condition rather than
replacing it by the three pairwise conditions. No general criterion
is being reproved or used without its hypotheses.

**Normalization map and geometric comparison.** The normalization of V
is the disjoint union of its three affine planes, with each map the
displayed linear closed immersion. It is finite by the module argument
above and unramified because the relative differential module for each
surjective coordinate-ring map is zero; each map is of finite type.
Outside the origin the planes are disjoint and the map is an isomorphism.
This is the componentwise birational statement appropriate to this
reducible model, not a claim that V is globally integral.

Each real tangent plane is invariant under componentwise I,J,K. Their
pairwise intersections are zero. With flat source H parameters use
u -> (u,0), u -> (0,u), and u -> (u,u)/sqrt(2). These are quaternionic
isometries onto the branches and have zero second fundamental form and
zero parametrized connection defect. Multiplying all three maps by one
fixed sqrt(c), c>0, gives the same pullback scale c on all source germs
and the same images. The diagonal coordinate z used in the ring
calculation denotes (z,z); the isometric reparametrization changes no
image ideal, quotient or scheme property.

For the actual fibre product of this disjoint normalization over V (or
over C^4), its (i,j)-component has coordinate ring S/(I_i+I_j).
For i=j it is the ith plane and is precisely its diagonal component;
for i!=j it is C. The component decomposition of the disjoint source
makes the union of the three diagonal components both open and closed.
The complement is exactly six reduced ordered points, all over the
origin. Thus the full off-diagonal scheme, not only its set or tangent,
has the required reduced isolated behavior and no diagonal accumulation.

The test retains smooth immersed source germs, finite unramified
normalization, a componentwise isomorphism locus, common flat quaternionic
metric/triple, parametrized geodesy, distinct quaternionic tangent lines
and reduced isolated pairwise coincidences. The simultaneous gluing
condition is the proposed conclusion to test, not an assumed geometric
input: its failure is the informative outcome. The local checks therefore
do not force abandonment of this model as an inference test.

L118/L120/L121 are comparisons, not premises used to realize this model.
Their actual source is a connected projective K3 with its nonflat metric;
their actual stable-moduli target, rank-two F, full tensor and global
normalization data have not been constructed here. Nothing identifies
this V with that image, even locally with its full metric data. The result
only rules out deducing length r-1 from the selected flat local properties
alone. Actual image gluing, collision emptiness, F existence, reconstruction,
transverse transport and universal primitive Hodge realization remain open.
The bounded attempt stops at this three-branch case; no higher arrangement
or global cohomological consequence is asserted.

**Separate critical audit, 2026-10-18.** The pre-invocation assessment
`drafts/literature/2026-10-18-three-quaternionic-lines-critical-audit.md`
approves precisely this verification as REPRODUCTION. Reuse its primary
coverage, including the correction; no general union theorem is reproved.
The audit finds no substantive error and gives no new obstruction to F.

For the local rational ring, substitution of a denominator nonzero at
zero in x alone or y alone leaves a unit in the ambient local ring.
Moreover q in n^2 is an ideal membership assertion, so q=z_1q_1+z_2q_2
with q_i in n holds in that ring, not just its completion. In the
convergent ring this follows from the same finitely generated ideal
identity n^2=(z_1^2,z_1z_2,z_2^2); the coefficients are convergent.
Thus (4) proves surjectivity onto the asserted image separately in
each category. In the polynomial grading its homogeneous version treats
every degree at least two. No passage from a finite truncation is needed.

The normalization argument is also valid in each category: the three
branch rings are normal domains and cyclic A-modules; their product is
finite over A. The tuple d_0 has no zero component, is a nonzerodivisor
of A, and d_0T is contained in A. Hence each t in T is the fraction
(d_0t)/d_0 in the actual total quotient ring. Conversely an integral
fraction satisfies its monic equation in every branch fraction field,
so normality puts it in each branch ring. This checks both inclusions,
without identifying a mere finite extension with the normalization.

For the filtration, any product of two elements of m_A has order at
least two on every branch, and multiplication by any element of T
preserves that order. Therefore m_A^2T is contained in A. The kernel
of the two constant-discrepancy coordinates on Q is two-dimensional;
m_AQ is contained there, and the two classes obtained from x_1 and
x_2 times (0,0,1) span it. This independently verifies both layers
of (2), not just the vector-space colength. In particular Q is not
annihilated by m_A, so it cannot be the two-copy residue-field quotient
suggested by the minimal-defect formula.

For each simultaneous sum the restriction map onto the ith branch is
surjective. An ideal with restriction n^2 therefore has inverse image
I_i+m^2. The explicitly listed quadratic products belong to the two
required ideals, while their linear parts have zero intersection.
These two inclusions prove all three equalities (3), including in the
local, analytic and completed categories. Pairwise intersections remain
the residue field. The (i,j) fibre-product rings over A equal those over
the ambient ring because I is contained in I_i and I_j; the disjoint
component decomposition gives all six off-diagonal points and no others.

Finally multiplication by 1/sqrt(2) on the diagonal commutes with all
three quaternionic structures and exactly cancels its doubled induced
metric. The three parametrizations are linear isometries, so their
parametrized connection defects vanish, not merely their normal second
fundamental forms. These checks establish only the flat local comparison.
The actual L118/L120/L121 source is a connected K3 with a globally
nonflat metric, and its image is integral; neither feature is retained
by this affine union. Global nonflatness also must not be substituted
for a claim of nonzero curvature at every source point. Actual-image
gluing and F existence remain unresolved. This completed audit is
EXPLORATION / REPRODUCTION, not confirmation-as-advance.

## Mathlib

Full matching coverage for this normalization-quotient computation and
the quaternionic geometric comparison is **not checked**. Unknown coverage
is not evidence of absence. The general criteria are cited above; the
specialization is proved explicitly over polynomial, local, convergent
and formal rings. This is an informal proof with no Lean or numerical
verification claim.
