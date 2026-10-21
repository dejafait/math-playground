# L079 — Larger-charge actual orthogonal images have compatible branches

## Hypotheses

Retain L071's marked projective K3 surface S, identical hyperkähler
metrics on X=S x S, actual real classes h and Omega=p_1^*h+p_2^*h,
and full integral mixed class tau_D. The full q-self-adjoint D is
scalar 2lambda on the metric's positive three-plane and preserves
its orthogonal complement. Write e_1=eta tensor 1, e_2=1 tensor eta,
P=e_1e_2 and integral_S eta=1; tau_D^2=156P. Use L052's exact
zero-slope line lattice NS(S) intersect h-perp=Zk, k^2=-14, and
its primitive integral elliptic fibre class f_ell, f_ell^2=0.

Suppose F is locally free holomorphic of rank two, slope-polystable
at Omega, with integral c_1(F)=0 and

\[
\operatorname{ch}_2(F)=-9e_1-10e_2-\tau_D.
\tag{1}
\]

This is precisely (a,b)=(-13,-14). Initial higher characters and
the initial K-class are unrestricted. No F, image, stable summand,
spin lift, inverse, reconstruction or transport is assumed to exist.
Use only L059's dimension-independent parallel real-reduction
construction, not its old rank-seven character or exclusion cases.

## Conclusion

The actual images G=R^1p_2*F and H=R^1p_1*F are base-changing locally
free bundles, with all other higher images zero, compatible unitary
quaternionic-instanton connections and h-slope-zero polystability.
They have perfect parallel symmetric O_S-valued pairings and

\[
\operatorname{ch}(G)=5-8\eta,\qquad
\operatorname{ch}(H)=6-10\eta,
\qquad c_1(G)=c_1(H)=0\text{ integrally}.
\tag{2}
\]

For one common integer t, their cohomology dimensions are
(t,2t-2,t). Their stable decompositions have exactly t trivial lines,
and t is either one or two. The following lists are exhaustive for
the covered character, cohomology, Schur-block and simple-index tests.
All displayed stable blocks are nontrivial and h-slope-zero.

| t | G | Required nontrivial blocks |
|---|---|---|
| 1 | O_S plus K_4 | K_4 stable symmetric, rank 4, c_1=0, c_2=8, acyclic |
| 1 | O_S plus E_4 tensor C^2 | E_4 stable rank 2, det=O_S, c_2=4, acyclic; alternating multiplicity form |
| 2 | O_S^2 plus K_3 | K_3 stable symmetric, rank 3, c_1=0, c_2=8, cohomology (0,2,0) |

The corresponding opposite-image alternatives are:

| t | H | Required nontrivial blocks |
|---|---|---|
| 1 | O_S plus J_5 | J_5 stable symmetric, rank 5, c_1=0, c_2=10, acyclic |
| 2 | O_S^2 plus J_4 | J_4 stable symmetric, rank 4, c_1=0, c_2=10, cohomology (0,2,0) |
| 2 | O_S^2 plus E_5 tensor C^2 | E_5 stable rank 2, det=O_S, c_2=5, cohomology (0,1,0); alternating multiplicity form |
| 2 | O_S^2 plus E plus E^vee | E stable rank 2, c_1=+/-k, ch_2=-5eta, c_2=-2, cohomology (0,1,0); hyperbolic form |

These are necessary alternatives, not existence assertions. In
particular the t=1 combination G=O_S plus E_4 tensor C^2 and
H=O_S plus J_5 is compatible with every covered simple/adjoint index,
cohomological parity and necessary orthogonal characteristic test.
Consequently these tests **do not exclude (-13,-14)**. Stop this
bounded exclusion mechanism. This is a NEGATIVE / REPRODUCTION
specialization of known tools, preserved by the separate audit below;
it constructs no holomorphic block or kernel, cycle or transverse
surface and leaves the universal primitive Hodge gap unchanged.

## Proof

**Every fibre and actual images.** Here p=-9 and b+4=-10, so
p(b+4)=90=6 modulo 12, and both corrections are at most -9.
Thus L071 applies. It establishes stability of F, its compatible
hyperholomorphic connection, and polystability of every factor
restriction by equivariant curvature restriction. The first-factor
charges are nine, the second-factor charges ten. Neither is 14r^2
for an integer r, so L071's exact line-lattice alternative proves
stability of every fibre in both directions, not just generic ones.

Import slope/dual stability, K3 RR and Serre duality from Huybrechts,
*Lectures on K3 Surfaces*, author-hosted prepublication draft,
[Chapter 9 Section 3.1, pp. 175--176](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=175),
and [Chapter 1 (2.5)--(2.6), Proposition 2.4, pp. 11--13](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
A stable rank-two determinant-trivial slope-zero fibre has no
sections: a nonzero section gives a subsheaf O_S of slope zero.
Dual stability and K_S=O_S similarly kill H^2. Its Euler value is
4 minus its charge. The two fibre cohomology triples are therefore
(0,5,0) and (0,6,0), at every closed parameter. This is odd IT.

GAGA algebraizes F. Each projection is smooth projective and flat
of finite presentation over the Noetherian S; F[0] is bounded,
finitely presented, base-flat and has proper support. Apply
[Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
with perfect object O_X: the pushforward is perfect and has derived
base change. Its fibres have only degree-one cohomology of the
fixed ranks above. [Lemma 36.31.3, 0BDK](https://stacks.math.columbia.edu/tag/0BDK)
makes each complex a locally free sheaf in degree one on an open
locus containing every closed point. The complementary closed
locus is empty, since a nonempty finite-type complex closed locus
has a closed point. Hence Rp_2*F=G[-1], Rp_1*F=H[-1]. Smoothness
of the projections and local freeness of F and G,H identify arbitrary
derived base change with ordinary pullback and these shifted bundles.
Proper GAGA identifies their actual holomorphic higher images.

Import Bartocci--Bruzzo--Hernandez Ruiperez, *A hyperkahler Fourier
transform*, Differential Geometry and its Applications 8 (1998),
239--249, [Definition 2, Lemmas 1--2, Theorem 3, pp. 243--246](https://mat.usal.es/ruiperez/Site/Papers_files/Hyperkahler-Fourier-Mukai.pdf#page=5).
The compact source is S, the target uses the identical compatible
rotation sphere, the hermitian quaternionic-instanton kernel is this
actual F, the source instanton is the flat line O_S, and odd IT was
just verified in each direction. The theorem identifies compatible
connections on these actual positive-rank images, without requiring
image stability, a positive mixed scalar or an equivalence kernel.
Invariant surface curvature has zero Kähler contraction coefficientwise
by Verbitsky, *Hyperholomorphic connections on coherent sheaves and
stability*, [math/0107182v10, Proposition 3.7 and Lemma 3.8, pp. 12--13](https://arxiv.org/pdf/math/0107182v10#page=12).
Thus both images are zero-Einstein and of degree zero. Huybrechts,
[Chapter 9 Theorem 4.9, p. 182](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=182),
gives polystability at this same real h, allowing reducibility.
These general theorems are imported; their twistor proofs are not
repeated. L073/L077 are method comparisons, not new-rank premises.

**Full signed GRR and independent Euler check.** L071's rank-two
identities give ch_3(F)=0 and ch_4(F)=ch_2(F)^2/12. Since e_i^2=0,
e_i tau_D=0 and tau_D^2=156P, the square is (180+156)P=336P.
Consequently the forced full character is

\[
\operatorname{ch}(F)=2-9e_1-10e_2-\tau_D+28P.
\tag{3}
\]

Import smooth relative GRR: Fulton, *Intersection Theory*, second
edition (1998), Theorem 15.2, pp. 286--287, Example 15.2.8,
pp. 291--292, retaining the assessment's scan-host qualification;
also the displayed relative case of [Stacks 02UO](https://stacks.math.columbia.edu/tag/02UO).
The projections are proper smooth between nonsingular projective
varieties, the input and all higher images are locally free. Apply
the rational cycle-class map after GRR. For p_2 the relative Todd
class is 1+2e_1, giving pushforward -5+(28-20)eta=-5+8eta.
For p_1 it is 1+2e_2, giving -6+(28-18)eta=-6+10eta.
The mixed class has insufficient fibre degree to push forward and
vanishes after multiplication by the fibre point class; no linear
mixed term survives. Both full mixed-square contributions were
retained in 336P. The alternating classes are -[G] and -[H], so
negation proves (2) rationally. There is no degree-six term before
pushforward, hence no rational first character. Torsion-freeness
of H^2(S,Z) upgrades that to integral first-class vanishing.

Absolute HRR with td(X)=1+2(e_1+e_2)+4P gives
chi(X,F)=8-38+28=-2. Surface RR gives chi(G)=10-8=2 and
chi(H)=12-10=2, their negatives as required by Leray. These
independent Todd computations check the alternating sign.

**Actual symmetric parallel pairings.** Coherent Künneth gives
H^1(X,O_X)=0. The exponential sequence injects Pic(X) into
H^2(X,Z); integral c_1(F)=0 therefore trivializes det(F).
Fix its determinant wedge A:F tensor F->O_X, perfect alternating.
For p_2 choose the nowhere-zero two-form on the first K3 to
trivialize omega_{X/S}; for p_1 choose it on the second. Compose
the cup product, A, multiplication by that two-form and relative
Serre trace to define Q on the corresponding degree-one image.

Import [Stacks 48.19 (2),(9), 0AU3](https://stacks.math.columbia.edu/tag/0AU3),
[48.3.6, 0A9Q](https://stacks.math.columbia.edu/tag/0A9Q) and
[48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT).
The smooth proper relative dimension is two, F is locally free,
and the bounded coherent duality coefficient is O_S. The resulting
isomorphism Rp_*(F^vee tensor omega)[2]=RHom(Rp_*F,O_S)
has both sides in the same degree: G[1] and G^vee[1], or H[1]
and H^vee[1]. Every-fibre base change identifies Q with the
perfect Serre pairing. Hence its bundle map is invertible everywhere;
a nonempty closed degeneracy locus would have a closed point.
The degree-one cohomology interchange contributes -1, and A
contributes a second -1, so Q is symmetric. Explicitly the
Dolbeault integrand A(a,c)u wedge v wedge sigma changes sign in
both A and u wedge v under interchange. This is the commutativity
convention of [Stacks 15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN).
Neither rank nor the mixed-tensor sign enters these two signs.

Import Perego, *Kobayashi--Hitchin corrispondence for twisted vector
bundles*, Complex Manifolds 8 (2021), 1--95,
[Propositions 3.9--3.12 and 3.15, pp. 36--38](https://unige.iris.cineca.it/retrieve/e268c4cd-97f6-a6b7-e053-3a05fe0adea1/10.1515_coma-2020-0107.pdf#page=36).
Use trivial twisting and zero B-field. Duals/tensors of these
zero-Einstein connections have Einstein function zero, and every
holomorphic morphism between them is parallel. In particular Q
and summand projections are parallel. Their summands inherit the
same zero-Einstein connections. Apply L059's dimension-independent
normalization: for parallel positive Hermitian metric g write
Q(u,v)=g(u,Jv); its symmetric matrix B gives J^2=B^*B>0 and
j=J(J^2)^(-1/2), an isometric antilinear involution. The fixed
spaces give a parallel real bundle whose complexification is the
image. H^1(S,Z/2)=0 orients it. This application uses no numerical
conclusion or existence witness of L059.

**Cohomology and complete Schur cases.** A nonzero parallel map
between stable zero-slope summands is an isomorphism: its kernel
and image are parallel subbundles, and a proper such subbundle
would contradict stability. Stable endomorphisms are scalar by
the same eigenspace argument. Duals are stable. Therefore a perfect
symmetric Q pairs each stable type only with its dual. A self-dual
stable type has a symmetric or alternating form; the corresponding
multiplicity form has the same sign. Non-self-dual types occur in
dual pairs with equal multiplicities and hyperbolic form. This is
the elementary Schur-block specialization compared with Serman,
*Orthogonal and symplectic bundles on curves and quiver representations*,
[Section 2.2 (2.2.1), Remark 2.3 and Proposition 2.6, pp. 10--11](https://math.univ-lille1.fr/~serman/grenoble.pdf).
Its curve flatness/moduli results are not K3 inputs; the parallel
Hom argument above supplies the necessary K3 justification.

Every nontrivial stable zero-slope block has H^0=H^2=0. For rank
greater than one the section argument and dual stability apply;
for a nontrivial zero-slope line, any effective divisor would have
positive h-degree, so it and its dual also have no sections.
Consequently h^0(G) equals the multiplicity t of O_S. Symmetry
gives h^2(G)=t, and chi(G)=2 gives h^1(G)=2t-2, so t>=1.
The single-row Leray spectral sequences, [Stacks Lemma 20.13.4,
01F2](https://stacks.math.columbia.edu/tag/01F2), give
H^j(S,G)=H^(j+1)(X,F)=H^j(S,H) for j=0,1,2. Thus H has
the same t and cohomology. Trivial and nontrivial isotypic parts
have no cross Hom to the dual, so each has a perfect parallel
restricted form; no isotropic trivial part is silently removed.

A nontrivial line has class rk, r nonzero, and surface RR gives
chi=2-7r^2, hence h^1>=5. Symmetry forces its dual line also to
occur (there is no nontrivial 2-torsion in Pic(S)). If G contained
such a pair, t<=3 by rank, whereas h^1(G)=2t-2<=4, less than
the pair's required ten. Hence G has no nontrivial lines.
A stable self-dual block has 2c_1=0, so det=O_S by torsion-free
K3 cohomology and Picard injection. A stable rank-two block of
that determinant has its alternating wedge form; simplicity makes
every duality form a scalar multiple of it. It cannot alone be
symmetric. Therefore t=3, which leaves rank two, is impossible;
t=4 leaves a nontrivial line and t=5 would force c_2(G)=0.
This proves t=1 or 2.

For t=1 the residual G has rank four and is acyclic. Its partitions
without lines are 4 or 2+2. The former must be stable symmetric
with c_2=8. In the latter, start with arbitrary individual c_1,
not determinant zero. A potential dual pair E,E^vee has
c_1(E)=rk and ch_2(E)=-4eta. For a stable rank R block of
character R+x+zeta, tensor multiplication and K3 RR give

\[
\chi(\operatorname{End}E)=2R^2+2Rz-q(x,x),\qquad
h^1(\operatorname{End}E)=2-\chi(\operatorname{End}E)\geq0.
\tag{4}
\]

The final equality uses simplicity and Serre duality. This is the
simple-index bound of Huybrechts, [Chapter 9 Sections 1.2--1.3,
Remark 1.5, pp. 169--170](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=169).
For this E it gives h^1(End E)=10-14r^2, hence r=0. E is then
self-dual alternating, with c_2=4. Two distinct such types cannot
pair and a single copy cannot carry symmetric Q. The only case
is two copies of one E_4, with nondegenerate alternating multiplicity
form on C^2. For t=2 the residual rank is three; without lines it
is stable symmetric K_3 with the stated character and cohomology.
This proves all G alternatives.

For H, h^1 is zero or two, so no nontrivial line (already requiring
at least five) can occur. At t=1 its residual has rank five;
the partitions are 5 or 3+2. The latter would leave a lone
rank-two symmetric stable block, impossible. Thus J_5 is the only
case. At t=2 its residual has rank four, with partitions 4 or
2+2. The first is J_4. In the second a possible dual pair has
ch_2(E)=-5eta and c_1(E)=rk. Equation (4) gives
h^1(End E)=14-14r^2, allowing exactly r=0,+/-1. For r=0 the
alternating type must be repeated, with c_2=5. For r=+/-1 it
is not self-dual, and E plus E^vee has its hyperbolic form;
c_2(E)=q(k,k)/2+5=-2. This negative second Chern number is
retained, not rejected: its discriminant is 4(-2)-(-14)=6,
and its simple index equals two. Character and RR give the
cohomology in the table. No other rank partition or multiplicity
type remains.

**All surviving simple and adjoint indices.** Equation (4) gives
the following required dimensions; none is negative or odd.

| Stable block | chi(End block) | h^1(End block) |
|---|---:|---:|
| K_4 | -32 | 34 |
| E_4 | -8 | 10 |
| K_3 | -30 | 32 |
| J_5 | -50 | 52 |
| J_4 | -48 | 50 |
| E_5 | -12 | 14 |
| E with c_1=+/-k | 2 | 0 |

Use the exterior-character identity applied in L059:
ch_2(Lambda^2 V)=(rank V-2)ch_2(V)+c_1(V)^2/2.
Hence A_G=Lambda^2 G has rank 10, ch_2=-24eta and chi=-4;
A_H=Lambda^2 H has rank 15, ch_2=-40eta and chi=-10.
Q identifies these with skew endomorphisms and with their duals.
All global skew endomorphisms are parallel. Their dimensions
are computed from the full multiplicity centralizers: so(t) on
the trivial block, zero on each once-occurring stable symmetric
block, sp(2) of dimension three on a twice-occurring alternating
type, and gl(1) of dimension one on a non-self-dual pair.
There are no cross morphisms between distinct types. Thus:

| Image alternative | (h^0,h^1,h^2) of its adjoint |
|---|---|
| G=O_S plus K_4 | (0,4,0) |
| G=O_S plus E_4 tensor C^2 | (3,10,3) |
| G=O_S^2 plus K_3 | (1,6,1) |
| H=O_S plus J_5 | (0,10,0) |
| H=O_S^2 plus J_4 | (1,12,1) |
| H=O_S^2 plus E_5 tensor C^2 | (4,18,4) |
| H=O_S^2 plus E plus E^vee | (2,14,2) |

These follow also from h^1=2h^0-chi, with chi fixed above.
The adjoint's symmetric coefficient form induces an alternating
middle Serre pairing, so its even middle dimensions pass parity.
For the complete End bundles chi(End G)=-30 and chi(End H)=-48.
The endomorphism dimensions are respectively 2,5,5 and 2,5,8,6
in the table orders, giving nonnegative even middle dimensions
34,40,40 and 52,58,64,60. Polystable images are not assigned
the simple bound h^0=1. Symmetric-image middle cohomology is
zero or two and also satisfies its alternating Serre-pairing parity.
All surface discriminants of the listed stable blocks are positive;
for c_1=0 this is immediate from c_2>0, and the nonzero-first-class
rank-two case has discriminant six as calculated above.

**Necessary topology and a complete compatible branch.** For an
oriented real reduction R of any symmetric block, p_1(R) is minus
the second Chern class of its complexification, not twice that
number. Import Cadek--Vanzura, *On the classification of oriented
vector bundles over 5-complexes*, Czechoslovak Math. J. 43 (1993),
753--764, [Section 2 relation (3), p. 2](https://www.math.muni.cz/~cadek/papers/so5.pdf#page=2):

\[
\rho_4p_1(R)=\mathcal P(w_2(R))+i_*w_4(R),\qquad
i_*:Z/2\longrightarrow Z/4,\quad1\longmapsto2.
\tag{5}
\]

For the single symmetric G blocks this necessary equation is
compatible with p_1=-8: K_4 can formally have w_2=w_4=0;
K_3 can have w_2=rho_2(f_ell), w_4=0, since f_ell^2=0.
No rank-three or rank-four topological existence follows from this
equation or from the rank-five theorem below. For the repeated E_4
case its real rank-four reduction can be the real bundle underlying
the symplectic E_4: its complexification is E_4 plus E_4^vee,
isomorphic to E_4 tensor C^2. The standard complex-to-real class
identities give p_1=-2c_2(E_4)=-8eta, w_2=0, w_4=0.
These identities are conditional on that block, not its construction.

On the H side, J_5 has p_1=-10eta. Choosing w_2=rho_2(k) and
w_4=0 gives P(w_2)=rho_4(k^2)=2rho_4(eta), equal to rho_4(-10eta).
The integral-lift property of the Pontryagin square justifies this
equality. The same classes satisfy the necessary equation for J_4,
without asserting rank-four realization. For E_5 tensor C^2, its
underlying real E_5 has p_1=-10eta, w_2=0, w_4=rho_2(eta),
also satisfying (5). For E plus E^vee with c_1(E)=+/-k and
c_2(E)=-2eta, its real reduction is E_R: p_1=c_1^2-2c_2=-10eta,
w_2=rho_2(k), w_4=0, again satisfying (5). Thus no listed block
fails the covered necessary characteristic equation.

In the t=1 branch one can in addition import Cadek--Vanzura,
[Theorem 1(i), manuscript p. 5](https://www.math.muni.cz/~cadek/papers/so5.pdf#page=5),
which realizes the just-specified compatible J_5 triple in **real
rank five** on a connected CW complex of dimension at most five.
S has a finite real four-dimensional CW structure, so the theorem
supplies that standalone topology. It supplies neither a holomorphic
acyclic J_5 nor its instanton connection, and it is not used for
the rank-four G block. Its chosen w_2 is nonzero; base spin is not
being used to impose a spin lift on the actual image.

Now take the formal t=1 combination with G=O_S plus E_4 tensor C^2
and H=O_S plus J_5. Their prescribed characters are exactly (2),
their cohomology agrees as (1,0,1), their coefficient forms have the
required symmetric signs, every simple and adjoint dimension above
is nonnegative with the required parity, and (5) is satisfied.
They would give H^*(X,F) dimensions (0,1,0,1,0), consistent with
chi(F)=-2 and coefficient duality. This verifies a compatible branch
through all approved tests. It is no existence theorem and does not
claim that independently specified images arise from one F.

The exact bound sought was an exhaustive contradiction, which is
not obtained. Further repetition of these same characters, partitions
or indices cannot exclude this input. Actual image/kernel existence,
additional representation or lifting tests, reconstruction and
transverse transport require different work and separate coverage.
The old stops for other pairs and the flat source blocker are
preserved; no positive-sign curvature obstruction is imported.

Arithmetic cross-check: run
`python3 scripts/larger-charge/check_orthogonal_image_indices.py`.
It independently compares the exterior character of each total image
with the direct-sum exterior formula, retaining all first-class cross
terms, and checks signed relative/absolute HRR, every simple/adjoint
table and the exact quadratic first-class bounds. The complete result
is saved in `scripts/larger-charge/orthogonal_image_indices_certificate.json`.
This is only arithmetic corroboration; the argument above supplies
the source applicability, every-fibre bridges and exhaustive cases.

**Separate critical audit, 2026-10-10.** Under the separately saved
SPECIALIZE audit assessment, the conditional verdict and the exhaustive
lists above survive without a substantive correction. The following
checks concern the actual geometric bridges and all listed cases; the
arithmetic certificate alone would not establish them.

First, L071 applies to the actual full negative tensor, with integral
first class zero, unchanged identical metrics and no initially fixed
higher characters. The congruence is 90=6 modulo 12. Its connection
argument gives polystability on every factor, and charges nine and ten
cannot be split charges 14r^2. Consequently the stable-fibre vanishing
holds at every closed point in both projections. The perfect/base-change
theorems cited above therefore apply before either image is asserted
locally free. The fixed-rank single-degree loci contain every closed
point; their closed complements on the finite-type base are empty.
This verifies both actual derived identities and both single-row Leray
sequences. The transform theorem receives this same compatible kernel
and the flat source line in each direction. It asserts polystability,
not stability, of the positive images; their alternating K-classes have
the separate minus sign used in GRR.

In detail the pure-point product contributes 180P and the entire mixed
square contributes 156P, so rank truncation forces ch_4=28P. Relative
Todd multiplication gives -5+8eta and -6+10eta before negation.
The absolute Todd computation is independently -2. There is no
degree-six term, and torsion-free H^2 makes the resulting first classes
integrally zero, so the image determinants are trivial by Picard
injection on S. Separately the assumed integral c_1(F)=0 and Picard
injection on X trivialize det(F) for the actual coefficient wedge;
rational numerical degrees alone would not suffice. Relative duality
duals G[-1] to G^vee[1] and identifies it
with G[1] after the coefficient and canonical trivializations. Its
fibrewise Serre forms are perfect. Interchanging two degree-one inputs
and interchanging two coefficient factors each contributes -1. The
form is therefore symmetric in both directions, independently of rank.
Perego's zero-Einstein parallel-morphism theorem applies to the actual
connections on the images, their duals and their summands. L059's
positive-square normalization has no rank restriction; it gives real
rank five and six for the images, not their underlying real ranks ten
and twelve. Orientability follows from H^1(S,Z/2)=0.

For completeness, the Schur enumeration was checked without assuming
any individual summand's determinant trivial in advance. Parallel Hom
maps between distinct stable types vanish, and endomorphisms of a
stable type are scalar. Hence self-dual symmetric, self-dual alternating
with even multiplicity, and paired non-self-dual types exhaust the
possibilities. All nontrivial blocks have zero H^0 and H^2. The two
Leray sequences give the same trivial multiplicity t and middle
dimension 2t-2 in both images. A nontrivial line and its distinct dual
would use two ranks in G, forcing t<=3, yet would contribute at least
ten middle dimensions against at most four. Thus none occurs. For
t=3 the residual G rank two cannot have a symmetric stable form: its
determinant is trivial, and simplicity makes its wedge the unique
duality form up to scalar. Larger t leaves a forbidden line or no
second character. This proves t=1 or 2 with no omitted large-t case.

At t=1 the only residual G partitions without lines are 4 and 2+2.
A paired rank-two type has first class rk and second character -4eta;
its self-Ext dimension 10-14r^2 forces r=0. Once its determinant is
trivial it is alternating and must occur twice as the same type.
At t=2 the residual G rank three has no nontrivial partition without
lines. For H, the now-fixed middle dimension zero or two excludes
every nontrivial line. At t=1 its residual ranks are 5 or 3+2; the
latter leaves a lone impossible symmetric rank-two type. At t=2 the
residual partitions are 4 and 2+2. In the paired case the self-Ext
dimension is 14-14r^2, giving exactly r=0,+/-1. The first is a
repeated alternating type; the others are a genuine dual pair. The
negative c_2=-2 in that last case is consistent with discriminant six
and simple self-Ext dimension zero, so cannot be removed by either
of these tests. These arguments establish exactly the table entries.

The multiplicity centralizers give all adjoint section dimensions:
so(t) on trivial lines, sp(2) on a repeated alternating type and
gl(1) on a dual pair, with zero on a single stable symmetric type.
In particular no cross Hom is lost and neither total image is treated
as simple. The exterior-character computation retains the individual
first-class cross terms of the dual pair. All seven adjoint triples,
all total End indices and all eight signed stable-block character
checks agree with the tables. The adjoint coefficient form is
symmetric, hence its middle Serre form is alternating; every required
middle dimension is even. An alternating rank-two block instead has
a symmetric middle Serre form, so the dimension one for E_5 is not a
parity contradiction.

Finally the characteristic convention is p_1(R)=-c_2(R tensor C).
For K_4 and K_3 the displayed classes have Pontryagin-square residue
zero, matching -8 modulo four. For J_5 and J_4 the integral lift k
has square -14, of residue two, matching -10 modulo four. For the
repeated alternating blocks the underlying real rank-four bundle
has w_4 equal to c_2 modulo two: it is zero for E_4 and one for
E_5, with p_1=-8 and -10 respectively. For the non-self-dual pair,
p_1=-14-2(-2)=-10 and w_4=0. Thus every necessary relation (5)
passes with the stated choices. Only J_5 uses the cited real-rank-five
existence theorem; S is connected of real CW dimension four, and the
source's extra injectivity hypotheses are not existence hypotheses.
No rank-three/four realization, holomorphic reduction, acyclicity or
realization of a specified actual image follows from this calculation.

The existing checker was rerun and its complete `signed_grr`,
`simple_indices`, `case_indices`, `exact_first_class_bounds` and
`failures` fields inspected with the scoped JSON inspector. There were
zero failures; minimum simple and adjoint middle dimensions were zero
and four, against nonnegative even dimensions required. The exact
first-class sets were {0} and {-1,0,1}. The program takes the cases
and centralizer dimensions as input; the written audit above, not the
program, verifies their completeness and applicability.

The retained t=1 combination therefore passes precisely the stated
necessary tests. This audit is EXPLORATION / REPRODUCTION: no substantive
error, stronger exclusion or existence conclusion was found, and no
progress beyond the imported general results is claimed. It preserves
the exclusion-route stop and the unresolved kernel and Hodge gaps.

## Mathlib

Full matching result and supporting transform, real-metric,
duality and topological statements: **not checked**. No absence
claim is made. The primary citations above supply the general
theorems; the new-rank every-fibre, character and exhaustive Schur
specializations are written out because the old numerical statements
do not cover this pair. This is local REPRODUCTION under the saved
SPECIALIZE assessment, not a claim of progress beyond checked sources
or a complete informal Hodge candidate.
