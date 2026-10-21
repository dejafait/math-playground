# L129 — Sharp normalization-defect bound for arbitrary finite collisions

## Hypotheses

Retain the conditional setting and actual completed-map identification of
audited L128. In particular, F is a locally free rank-two
Omega-slope-polystable bundle on the identical marked K3 product, with
integral c_1(F)=0 and ch_2(F)=-14e_1-21e_2-tau_D. The common quaternionic
structures and the opposite map's positive metric scale 2lambda are
unchanged. Its finite normalization g:B -> Z has an entire fibre
g^(-1)(z)={b_1,...,b_r}, with r>=1. Existence of F and of any collision
is assumed, not established.

In L128's one common formal ambient chart, V has quaternionic dimension
39 and the images P_i of the branch tangents are distinct quaternionic
lines, hence complex two-planes. Set

\[
 S=\widehat{\operatorname{Sym}_{\mathbb C} V^*},\qquad
 I_i=I(P_i),\qquad J_j=\bigcap_{i=1}^j I_i,\qquad
 B_i=S/I_i\simeq\mathbb C[[u_i,v_i]].
\]

L128 identifies the actual completed image inclusion with
S/J_r -> T_r=product_i B_i. Let
Q_z=(g_*O_B/O_Z)_z be the actual algebraic normalization quotient.

## Conclusion

The quotient Q_z has finite length and

\[
              \operatorname{length}_{O_{Z,z}} Q_z
                         \leq {r+1\choose 3}.                 \tag{1}
\]

For every r>=1 this bound is attained among distinct quaternionic
tangent-line arrangements in H^39. For the explicit real-slope
arrangement below, the degree-d defect is exactly

\[
                   (d+1)\max\{r-d-1,0\},\qquad d\geq0.       \tag{2}
\]

Sharpness concerns tangent arrangements, not actual K3 collisions.
This is a conditional local ADVANCE / REPRODUCTION by specialization of
known union and completion tools. The separate step-391 critical audit
below preserves the result without a stronger conclusion.
It supplies no bound on the number or multiplicities of global collisions,
no F, no cycle or transport, and no universal Hodge resolution.

## Proof

**Coverage and imports.** The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-18-arbitrary-branch-sharp-normalization-defect.md`.
Import [Stacks, Lemma 29.4.6, tag 01QX](https://stacks.math.columbia.edu/tag/01QX):
for any ring S and two ideals I,J, the sequence

\[
 0\longrightarrow S/(I\cap J)\longrightarrow
 S/I\oplus S/J\longrightarrow S/(I+J)\longrightarrow0
                                                               \tag{3}
\]

is exact, with last map the difference of restrictions. For passage to
the actual algebraic quotient use exact completion of finite modules,
[Stacks, Lemma 10.97.1, tag 00MA](https://stacks.math.columbia.edu/tag/00MA),
and L128's verified identification of the completed finite normalization.
These are the same imported inputs covered by the assessment.

The reviewed Derksen--Sidman regularity theorem supplies an alternative
tail bound, but is not needed in this proof: the product containment
below directly bounds each whole finite-length increment. The reviewed
skew-lines-on-a-quadric results motivate the equality model; their WLP,
resolutions and linkage calculations are not imported. The elementary
restriction calculation is necessary to verify quaternionic admissibility
and the precise completed length. Neither a generic Hilbert function nor
an equality between product and intersection ideals is assumed. No general
regularity or liaison theorem is reproved.

**Each added branch contributes at most binom(j,2).** Two distinct
quaternionic lines have zero intersection: a nonzero common vector would
generate both as a quaternionic line. Thus P_i intersect P_j={0} for
i!=j, also as complex vector spaces. Every complex linear functional on
P_j extends to V while vanishing on P_i, by first defining it on the
direct sum P_i+P_j and then extending to V. Consequently the image of
I_i in B_j is the whole maximal ideal m_j=(u_j,v_j).

For j>=2 apply (3) to J_(j-1) and I_j. Write A_j=S/J_j and
T_j=product_(i<=j) B_i. The inclusion A_j -> T_j factors through
A_(j-1) direct sum B_j. Taking the two successive quotients gives

\[
 0\longrightarrow C_j\longrightarrow T_j/A_j
       \longrightarrow T_{j-1}/A_{j-1}\longrightarrow0,
 \qquad C_j=S/(J_{j-1}+I_j).                                 \tag{4}
\]

Indeed, (A_(j-1) direct sum B_j)/A_j=C_j by (3), and
T_j/(A_(j-1) direct sum B_j)=T_(j-1)/A_(j-1). This exact sequence
retains the full previous union, not just its separate pairwise
intersections.

The ideal product satisfies product_(i<j) I_i subset J_(j-1).
Under the surjection S -> B_j its image is the product of the images,
namely m_j^(j-1). Hence, putting K_j=(J_(j-1)+I_j)/I_j,

\[
       \mathfrak m_j^{j-1}\subseteq K_j,\qquad
       C_j=B_j/K_j,\qquad
       \dim_{\mathbb C} C_j\leq
       \dim_{\mathbb C}B_j/\mathfrak m_j^{j-1}
                  =\sum_{d=0}^{j-2}(d+1)={j\choose2}.        \tag{5}
\]

The monomials of total degree at most j-2 form a basis of the last
power-series quotient, so (5) bounds the entire module, including all
higher orders. The containment direction is essential: the intersection
may be strictly larger than the product, which only decreases this
colength. No distributive identity for sums and intersections is used.

Since T_1/A_1=0, induction in (4) proves finiteness and

\[
 \dim_{\mathbb C}(T_r/A_r)
       =\sum_{j=2}^r\dim_{\mathbb C}C_j
       \leq\sum_{j=2}^r{j\choose2}={r+1\choose3}.            \tag{6}
\]

This includes r=1, when both sides are zero. It is independent of the
dimension of the span and in fact applies to any pairwise zero-intersecting
complex two-planes. The extra quaternionic hypothesis supplies this
intersection property for the actual tangents.

**An admissible quaternionic equality arrangement.** Choose an H^2
subspace of H^39 and distinct real numbers t_1,...,t_r. With the fixed
componentwise quaternionic structures, take

\[
                  P_i=\{(v,t_i v):v\in\mathbb H\}.
                                                               \tag{7}
\]

Real scalar multiplication commutes with I,J,K, so each P_i is a
quaternionic line. The t_i are distinct, so the P_i meet pairwise only
at zero. They are flat totally geodesic planes. If a common induced
metric scale is desired at the tangent-model level, the parametrization
v -> sqrt(2lambda/(1+t_i^2))(v,t_i v) gives pullback 2lambda g_flat
for every i. These nonzero scalar reparametrizations change no image
ideal or length. They do not model a nonflat K3 neighborhood.

Use complex coordinates x_1,x_2,y_1,y_2 on H^2 for I, and identify
the i-th plane by x_a=v_a and y_a=t_i v_a. Other ambient variables
restrict to zero and do not affect the image. For degree d, let
E_d subset C^r be the span of the evaluation vectors
(t_i^k)_(i=1)^r, 0<=k<=d. Every degree-d ambient monomial restricts
to a degree-d v-monomial times one such vector. Conversely, fix
v_1^a v_2^(d-a) and k with 0<=k<=d. Choose

\[
          \max(0,k-(d-a))\leq l\leq\min(a,k).
\]

This integer interval is nonempty. The ambient monomial
x_1^(a-l) y_1^l x_2^(d-a-k+l) y_2^(k-l) restricts on every plane
to t_i^k v_1^a v_2^(d-a). Thus the entire degree-d image is exactly

\[
          \operatorname{Sym}^d(\mathbb C^2)^*\otimes E_d
          \ \subseteq\
          \operatorname{Sym}^d(\mathbb C^2)^*\otimes\mathbb C^r.
                                                               \tag{8}
\]

The Vandermonde matrix for the distinct t_i has rank min(d+1,r).
For d<r a polynomial of degree at most d vanishing at all r points
must be zero; for d>=r-1 the first r powers already give an invertible
square Vandermonde matrix. Hence the image dimension is
(d+1)min(d+1,r), whereas the target dimension is r(d+1).
This proves (2) in every degree.

The map on power series is homogeneous. A tuple of branch series is
in its image exactly when each homogeneous degree tuple is in (8):
choose a homogeneous ambient preimage separately in each degree, and
their sum is a well-defined formal series. In particular every tuple
whose branch orders are at least r-1 has a formal preimage. Therefore
the complete quotient is the finite direct sum of the degree-d
cokernels for 0<=d<=r-2. Its dimension is

\[
 \sum_{d=0}^{r-2}(d+1)(r-d-1)
   =\sum_{k=1}^{r-1}k(r-k)
   =\frac{r(r-1)(r+1)}6={r+1\choose3}.                       \tag{9}
\]

For r=1 the sum is empty, also giving zero. This calculation treats
the entire completed quotient, not just a finite jet proposed as a
proxy. It gives values 0,1,4,10 for r=1,2,3,4, consistent with the
earlier three- and four-branch comparisons.

For completeness, T_r is the normalization of this reduced formal
arrangement ring A_r, so its quotient is genuinely a normalization
defect. The ideals I_i are incomparable prime ideals, each with normal
quotient C[[u_i,v_i]], and A_r injects into their product. Each B_i is
a cyclic A_r-module, so T_r is finite over A_r and integral over it.
To see the total quotient ring explicitly, for each i choose, for every
j!=i, a linear form vanishing on P_j but not identically on P_i.
Their product h_i has nonzero i-th restriction and zero other
restrictions. Then s=sum_i h_i is nonzero on every component, hence
is a nonzerodivisor of A_r, and h_i/s is the i-th component idempotent.
For any nonzero b in B_i, lift b to a in A_r and use the denominator
a h_i+sum_(j!=i) h_j, which is nonzero on every component. Together
with these idempotents and surjectivity A_r -> B_i, this shows that
the total quotient ring is product_i Frac(B_i). Every element of it
integral over A_r has each component integral over B_i, and thus in
B_i by normality. This proves the normalization assertion. For r=1
the same argument uses the empty product h_1=1.

**Return to the actual algebraic quotient.** Put A=O_(Z,z) and
T=(g_*O_B)_z. These are Noetherian local and finite A-algebra data
from L128, and Q_z=T/A is a finite A-module. Exact completion gives

\[
                 \widehat Q_z=\widehat T/\widehat A
                              \simeq T_r/A_r.                \tag{10}
\]

The right-hand side is finite dimensional by (6). All its simple
module factors have residue field C, since it is a finite-length
module over the completed local image ring. Its length therefore
equals its C-dimension. To justify finiteness and length before
completion explicitly, choose N such that m_A^N annihilates
widehat Q_z. Exact completion identifies the completion of
m_A^N Q_z with m_A^N widehat Q_z=0. Reduction modulo m_A is
unchanged by completion; Nakayama's lemma therefore gives
m_A^N Q_z=0. A finite module killed by a power of the maximal ideal
is already complete. Consequently Q_z -> widehat Q_z is an
isomorphism and its algebraic length equals the dimension in (6).
This proves (1), without assuming that normalization commutes with
completion or that the original image is normal.

The target bound and arrangement sharpness are thus established
conditionally on L128. No assertion that the equality configurations
occur for the actual classifying map has entered. The global number
of collisions and their fibre sizes are not controlled here, and no
global normalization/Euler comparison reaching a contradiction is
available. The smaller r-1 inference rejected in ATTEMPTS/070 and
the curvature stops in ATTEMPTS/071--072 remain untouched.

**Separate critical audit, 2026-10-18 (step 391).** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-18-sharp-arbitrary-branch-defect-critical-audit.md`.
The outcome is EXPLORATION / RESEARCH / REPRODUCTION, actual task
proof_audit: all three load-bearing tests survive, with no substantive
error, strengthened conclusion or existence result. This checks the
known-tool specialization; it is not a further mathematical advance.

For the quotient test, regard all modules as S-modules. The maps
A_j -> A_(j-1) direct sum B_j -> T_j are injections, the first because
its kernel in S is J_(j-1) intersect I_j=J_j. The second uses the
injection of the whole previous reduced union into its branch product.
The quotient of the second map is T_(j-1)/A_(j-1), and the quotient
of the first is C_j by the cited binary exact sequence. Thus (4) is
the actual nested-submodule filtration, in its asserted direction.
Surjectivity of S -> B_j makes the image of the product of the I_i
equal to the product of their images. Pairwise zero intersection gives
each image exactly m_j, including both independent linear generators;
it is not merely a proper m_j-primary ideal. Therefore (5) follows
from a surjection B_j/m_j^(j-1) -> C_j. Additivity of finite
C-dimension in (4) proves the all-r bound with no filtration-strictness
assumption, no omission of high orders and no constraint on the span.

For the sharpness test, the integer interval for l is nonempty because
0<=a,k<=d: both 0 and k-(d-a) are at most min(a,k).
All four exponents in the displayed ambient monomial are nonnegative
and have total degree d. This produces every tensor of a v-monomial
and an evaluation vector, while restriction of an arbitrary ambient
monomial produces no other kind of vector. Distinct v-monomials lie
in independent coefficient positions in every branch, so their
contributions are a direct sum. The square r-by-r evaluation minor
has determinant product_(i<j)(t_j-t_i), which is nonzero; for smaller
d the root-count argument gives injectivity. Hence the rank formula
and every degree of (2) hold, including d=0 and d=r-1.
Degreewise lifts assemble in the complete ambient power-series ring;
there is no analytic convergence condition. The quotient therefore
has exactly the finite sum (9), not just that many visible jet classes.
Real slopes commute with the entire quaternionic triple, and the
positive rescaling changes neither the planes nor their ideals.
The empty degree range for r=1 gives defect zero. These checks verify
sharpness only in the stated formal flat model.

For its normalization, the component-supported elements h_i also
make the total-fraction argument explicit. An element nonzero in all
B_i is a nonzerodivisor, since multiplication is injective in their
product. Conversely, an element whose i-th component is zero is
annihilated by the nonzero h_i. Thus s=sum_i h_i is an admissible
denominator and e_i=h_i/s is the i-th idempotent in the total quotient
ring. Given b!=0 in B_i and a lift a in A_r, put
D=a h_i+sum_(j!=i) h_j. Its components are b h_i on the i-th branch
and h_j on the others, all nonzero. The fraction h_i/D has i-th
component 1/b and all other components zero. Multiplication by
lifts of numerators and summation over i therefore gives every tuple
of component fractions. Since T_r is finite over A_r, it lies in the
integral closure; projecting any monic integrality equation to B_i
and using normality of B_i gives the reverse containment. This
verifies normalization, including h_1=1 when r=1, without a theorem
asserting that normalization commutes with completion.

Finally, audited L128 identifies the completion of the actual injection
A -> T, not only an abstract ring with the same tangent cone.
Its R -> A is a local quotient, its T is finite, and its factors run
over the entire finite fibre. Thus the cited exact-completion theorem
applies to 0 -> A -> T -> Q_z -> 0 and gives precisely (10), with
the same action of the completed maximal ideal. A finite-dimensional
module over this local C-algebra has only C as its simple factor;
its composition series supplies a power m_A^N annihilating it.
For full detail in descending this assertion, choose finite generators
of m_A^N and the resulting surjection Q_z^k -> m_A^N Q_z.
Completing this map and the inclusion m_A^N Q_z -> Q_z by 00MA
identifies its image with m_A^N widehat Q_z=0. The completed
m_A^N Q_z is therefore zero. Its reduction modulo m_A agrees with
the uncompleted reduction, so Nakayama gives m_A^N Q_z=0.
The completion system is now constant from order N onward, proving
Q_z=widehat Q_z and equality of the actual algebraic length and
the computed C-dimension. No faithful-flatness shortcut or assumption
of normality of Z is needed.

These checks preserve (1), (2), all finite r and special spans under
L128's conditional hypotheses. The source and failed-route comparison
is unchanged: ATTEMPTS/070 refutes minimal defect r-1, while
ATTEMPTS/071--072 do not constrain this local algebra calculation.
Neither actual equality configurations nor F nor any global defect
threshold are established. Full matching Mathlib coverage remains
unchecked as stated below.

## Mathlib

Full matching Mathlib coverage for the sharp arbitrary-branch bound,
the quaternionic equality arrangement and actual-image specialization
was not checked. Unknown coverage is not evidence of absence. The
precise standard union and completion inputs are cited above; the
restriction and colength calculations are provided in full here.
