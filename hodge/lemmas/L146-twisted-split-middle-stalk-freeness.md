# L146 — Twisted middle stalk and canonical hull map at a split fibre

## Hypotheses

Retain L071's identical marked projective K3 factors S_1 and B=S_2,
common hyperkähler metric g, real Kähler class h, ordered structures
I,J,K and full integral mixed tensor tau_D. The corresponding operator
satisfies D[sigma]=2lambda[sigma], where sigma=omega_J+i omega_K
and 1<lambda<5/4. Let c_1(L)=k=(-4,-2,1,2), with k.h=0 and
k^2=-14. Suppose F is locally free of rank two, Omega-polystable for
Omega=p_1^*h+p_2^*h, with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Select an actual split parameter z with F_z=L direct sum L^{-1}.
Use the actual compatible connection and natural KS comparison of
L094/L095, both weight ranks of L134, and the actual minimal
representative and last-row ideal established in L145. Put

\[
 G=F\otimes p_1^*L^{-1},\quad R=\mathcal O_{B,z},\quad
 \mathfrak m=\mathfrak m_z,\quad M=(R^1p_{2*}G)_z.
\]

The ring R is the ordinary algebraic local ring of the smooth surface,
with residue field C. Neither F nor a split parameter is known to
exist. No twisted scalar self-duality, ordinary middle base change,
global IT, effectivity or freeness is assumed.

## Conclusion

The entire ordinary middle stalk is free of rank twenty-four:

\[
                         M\simeq R^{24}.
\]

Its canonical evaluation map M -> M^{**}, with dual Hom_R(-,R), is
an isomorphism; its local hull quotient has length zero. The free
identification is noncanonical, whereas the hull-map statement is
intrinsic. This is a conditional ADVANCE / REPRODUCTION of assessed
tools. The separate critical audit below preserves the conclusion
without a substantive repair or stronger result. It supplies a local defect
input, not a metric extension, global positivity, F, nonempty split
locus, algebraic cycle, transport or universal Hodge resolution.

## Proof

**Imported tools and applicability.** Reuse the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-22-twisted-split-middle-hull-defect.md`.
L145 supplies the actual perfect representative, with all higher
coefficients retained,

\[
 K:\quad R\xrightarrow{v}H=R^{26}\xrightarrow{\rho}R,
 \qquad v,\rho\equiv0\pmod{\mathfrak m},\quad \rho v=0,
 \qquad \operatorname{im}\rho=\mathfrak m.                 \tag{1}
\]

It uses [Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
for perfect pushforward/derived base change and
[Lemma 15.77.6, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
for minimal ranks. Here the projection is smooth projective, the
coefficient is locally free and base-flat, and the derived central
cohomology dimensions are (1,26,1). These are not ordinary middle
base-change dimensions. The fixed-coefficient comparison is
Budur–Wang, *Cohomology jump loci of differential graded Lie algebras*,
Compositio Math. 151 (2015), 1499–1528, DOI
10.1112/S0010437X14007970,
[arXiv:1309.2264v2, Definitions 3.2/3.8, Proposition 3.10,
Lemma 3.11, Theorem 6.4 proof (9)–(10), Remark 6.5](https://arxiv.org/html/1309.2264v2#S6).
Remark 6.5 covers this arbitrary holomorphic bundle on compact K3;
no formality or vanishing-Chern hypothesis is imported.

Choose regular parameters x,y of R. They form a regular sequence by
[Stacks Lemma 10.106.3, 00NQ](https://stacks.math.columbia.edu/tag/00NQ).
Use regular-sequence Koszul exactness from
[Lemma 15.31.2, 062D](https://stacks.math.columbia.edu/tag/062D).
Finite direct summands of finite free modules are projective by
[Lemma 10.78.2, 00NX](https://stacks.math.columbia.edu/tag/00NX)
and finite projective modules over a local ring are free by
[Lemma 10.55.8, 00JJ](https://stacks.math.columbia.edu/tag/00JJ).
All these are general inputs, not results to be reproved. The
specialization below must establish the actual unit and splitting.
No scalar pairing of K with itself is imported from L111, which is
a comparison for a different coefficient only.

**The actual incoming boundary.** Let u_1,u_2 be the tangent basis
dual to x,y. With the ordered central splitting (L,L^{-1}), write
the actual KS classes as

\[
 a_i=\begin{pmatrix}0&p_i\\q_i&0\end{pmatrix},\qquad
 p_i\in H^1(L^2),\quad q_i\in H^1(L^{-2}).                \tag{2}
\]

These are the natural classes of L094/L095 before taking the
stabilizer quotient. The central twisted coefficient is
G_0=O direct sum L^{-2}, whose unique section up to scale is
s=(1,0). Fix the residue of the degree-zero generator in (1) to be s.

For each u, the actual dual-number family gives the flat coefficient
sequence 0 -> G_0 -> G_A -> G_0 -> 0 used in L145. Its boundary in
degree zero is the epsilon coefficient of v evaluated on u. Indeed,
tensor the bounded R-flat Cech complex of the actual family and its
finite-free comparison (1) with 0 -> C -> A -> C -> 0. Naturality
of connecting maps ([Stacks Lemma 12.13.12, 0117](https://stacks.math.columbia.edu/tag/0117))
identifies their boundaries. Minimality makes the residue complex's
differential zero, so lifting s, applying the differential and dividing
by epsilon gives precisely this linear coefficient. This is the
same comparison as L145 in degree zero, without R^1 base change.
Exact projective GAGA carries the coherent sequence on S_1 to its
analytic sequence. The perturbed Dolbeault differential is
bar-partial+epsilon a_u acting on the defining coefficient from the
left, so the section boundary is a_u s=(0,q(u)). Therefore

\[
                   v\equiv xq_1+yq_2\pmod{\mathfrak m^2H}.
                                                               \tag{3}
\]

Here H/mH is identified with H^1(L^{-2}). There is no commutator,
dual-coefficient transpose or factor two in (3). L134's negative
weight rank two makes q_1,q_2 linearly independent.

**The actual nonzero mixed pairing.** Normalize the nonzero Serre
functional on H^2(O_{S_1}) by

\[
 T(c)=\frac1{(2\pi i)^2}\int_{S_1}\sigma_{S_1}\wedge c,
 \qquad B_{ij}=T(p_i\wedge q_j).                            \tag{4}
\]

Choose the residue degree-two generator in (1) to have T-value one.
L145's outgoing-row calculation then says its linear functional in
direction u_i is ell_i(c)=T(p_i wedge c). Since every entry of v is
in m=(x,y), choose actual a,b in H with v=xa+yb. Their residues
are q_1,q_2 by (3). The exact relation rho v=0 and the cited
two-parameter Koszul exactness give t in R with rho(a)=yt and
rho(b)=-xt. Comparing their linear coefficients, which use only
the residues of a,b because rho is minimal, gives
B_11=0, B_21=t mod m, B_12=-t mod m and B_22=0. In particular

\[
               B_{11}=B_{22}=0,\qquad B_{21}=-B_{12}.       \tag{5}
\]

To test whether B_{12} is zero we use the actual connection, not
injectivity of KS alone. In local holomorphic base coordinates the
base-(1,0), fibre-(0,1) mixed curvature has the form sum dz_i wedge
b_i. Each b_i represents the actual KS class a_i: varying the fibre
Dolbeault operator differs from this curvature contraction by the
Dolbeault differential of the horizontal connection coefficient.
L094/L095 identify the same derivative; for a real t and
u=(t-iIt)/2 their identity r_{It}^{0,1}=i r_t^{0,1} gives
r_u^{0,1}=r_t^{0,1}, with no extra factor or conjugation. Exact
corrections do not change the following trace integral, by closedness
and Stokes on the compact fibre.

The coefficient of dz_1 wedge dz_2 with fibre type (0,2) in the
curvature square is

\[
 -\operatorname{Tr}(b_1\wedge b_2)
 +\operatorname{Tr}(b_2\wedge b_1)
             =-2\operatorname{Tr}(b_1\wedge b_2).          \tag{6}
\]

This retains moving the fibre one-form past a base one-form and odd
trace cyclicity. Both pure curvature blocks have type (1,1) on their
factors, so neither contributes this base-(2,0), fibre-(0,2) term.
The factor two cancels the factorial in ch_2. L095's actual-form
identity, valid also at the split parameter, is

\[
 \gamma=p_{2*}\left(
 \frac{\operatorname{Tr}(R_F\wedge R_F)}{2(2\pi i)^2}
                    \wedge p_1^*\sigma_{S_1}\right)
                      =-2\lambda\sigma_B.
\]

Consequently (6), followed by the matrix trace in (2), gives

\[
 \begin{aligned}
 2\lambda\sigma_B(u_1,u_2)
 &=T\big(\operatorname{Tr}(a_1\wedge a_2)\big)\\
 &=T(p_1\wedge q_2)+T(q_1\wedge p_2)
   =B_{12}-B_{21}.
 \end{aligned}                                             \tag{7}
\]

No scalar self-duality of G is asserted: (7) is the trace pairing of
actual endomorphism-valued KS classes. Combining (5) and (7) proves

\[
       B_{12}=\lambda\sigma_B(u_1,u_2)\ne0.                \tag{8}
\]

The nonzero value follows from the nowhere-vanishing holomorphic
symplectic form on B and lambda>0. This is stronger than either
weight-rank statement separately and supplies the needed unit test.

**Full module calculation over the original ring.** Retain the
actual vectors a,b and element t just constructed, so v=xa+yb,
with residues q_1,q_2. A nonzero two-by-two residue minor
is a unit in R. Completing that minor with the other coordinate
vectors gives an invertible basis matrix, so

\[
            H=P\oplus Q,\qquad P=Ra+Rb,\qquad Q\simeq R^{24}.
                                                               \tag{9}
\]

No higher term of v has been discarded. The full equations for the
same element t, obtained from the exact chain relation by Koszul
exactness for the regular sequence x,y, remain

\[
                     \rho(a)=yt,\qquad \rho(b)=-xt.        \tag{10}
\]

Taking the linear y coefficient of rho(a), and using its residue
q_1 and L145's actual outgoing row, gives

\[
                   t\bmod\mathfrak m=\ell_2(q_1)=B_{21}
                          =-\lambda\sigma_B(u_1,u_2)\ne0.
                                                               \tag{11}
\]

Thus t is a unit, a conclusion about the full coefficient (10).
In particular rho(P)=(x,y)=m. For a free basis e_j of Q, minimality
implies rho(e_j) in m=rho(P). Choose p_j in P with
rho(p_j)=rho(e_j) and set e'_j=e_j-p_j. Their projections to Q
are its basis, hence they span a free complement Q' of P, and
rho(Q')=0. The entire complex is therefore the direct sum of Q'
in degree one and

\[
 R\xrightarrow{r\mapsto(xr,yr)}R^2
     \xrightarrow{(\alpha,\beta)\mapsto t(y\alpha-x\beta)}R.
                                                               \tag{12}
\]

Since t is a unit and x,y are a regular sequence, the kernel of
the last map is exactly R(x,y). This is the image of the first
map. Koszul exactness computes the whole middle cohomology of
(12) as zero, not merely its associated graded or a finite jet.
It follows that M=ker(rho)/Rv is isomorphic to Q'=R^{24}.
The same summand has H^0=0 and H^2=R/m, consistent with L145.

Finite free modules are reflexive under their canonical evaluation
map; transport this map through the obtained isomorphism M=Q'.
Naturality identifies it with M -> M^{**}, proving that the
actual local hull quotient is zero. This is stronger than choosing
an unrelated free hull and does not assume ordinary middle base
change. In fact the ordinary middle fibre now has dimension 24,
whereas the derived middle fibre has dimension 26; the minimal
Koszul summand in (12) accounts for the difference.

The continuation test succeeds: actual weight rank supplies a
direct summand, and the nonzero actual trace form supplies its unit
Koszul coefficient. All higher coefficients remain in a,b,t and
the corrected complement. The earlier IT, automatic-effectivity,
strict-Euler and necessary-jet stops remain unchanged. No global
defect inequality or existence conclusion follows from this local
calculation. The separate audit below checks these bridges independently.

**Separate critical audit, 2026-10-22 (step 467).** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-22-twisted-middle-stalk-critical-audit.md`
and its inspected primary proof cases. The verdict is EXPLORATION /
REPRODUCTION: no substantive error, necessary repair or stronger
conclusion was found. This verifies the conditional local input; it
does not constitute progress beyond the checked known tools.

First, the incoming and outgoing maps must belong to the same actual
complex. L145's flat coefficient sequence applies to G_A itself, not
to an abstract first-order class with the same ranks. Its bounded
R-flat Cech representative P and the bounded finite-free K admit the
chain comparison described in L145's audit. Tensoring that comparison
with the dual-number sequence preserves quasi-isomorphisms and gives
a map of short exact sequences of complexes. The natural connecting
maps in Stacks 0117 therefore agree in degree zero as well as degree
one. Fix the residue identifications in all three degrees by this
single comparison. One can choose the degree-zero generator to map
to (1,0) and the degree-two generator to have T-value one independently;
these are independent free terms of K. The middle residue identification
is with the entire H^1(L^{-2}), not a selected tangent subspace.
Minimality then identifies the first derivative of v with the boundary
of the chosen section. Exact GAGA and the fixed twist identify that
boundary with a_u(1,0)=(0,q(u)). There is no commutator, dual-action
minus sign or change of family in (3).

Second, the pairing normalization can be checked before local algebra.
For a real base tangent t, put u=(t-iIt)/2. On fibre (0,1) forms,
I_c acts by i, and L095 gives r_{It}=I_c r_t. Thus
r_u^{0,1}=(r_t^{0,1}-i r_{It}^{0,1})/2=r_t^{0,1}.
The holomorphic-family KS class is consequently represented by the
base-(1,0), fibre-(0,1) curvature contraction with this convention.
The horizontal connection contributes a Dolbeault-exact term, as in
L095's equation (4). This comparison is made before the stabilizer
quotient, including at the reducible fibre.

More explicitly, if b_i=a_i+bar-partial h_i are two choices of these
closed endomorphism-valued (0,1) representatives, then

\[
 \operatorname{Tr}(b_1\wedge b_2-a_1\wedge a_2)
 =\bar\partial\operatorname{Tr}
   (h_1a_2-a_1h_2+h_1\bar\partial h_2).
\]

The trace is globally defined on the fibre; wedging with its closed
holomorphic two-form and integrating kills this difference by Stokes.
No multiplicativity of harmonic projection is assumed. With base
forms placed first, the two mixed products in the curvature square
have coefficients -Tr(b_1 wedge b_2) and +Tr(b_2 wedge b_1).
Odd trace cyclicity makes their sum -2 Tr(b_1 wedge b_2).
The pure vertical and horizontal blocks are respectively of fibre
and base type (1,1); they cannot contribute the required fibre-(0,2),
base-(2,0) component. The factor 2 cancels the character factorial,
so gamma(u_1,u_2)=-T(Tr(a_1 wedge a_2)). L095's equality of actual
holomorphic forms, not merely its positive norm or a cohomology class,
now gives precisely (7). For the off-diagonal matrix, the trace is
p_1 wedge q_2+q_1 wedge p_2; commuting the two line-valued odd forms
gives B_12-B_21. An allowed diagonal constant marking rescales the
two weights inversely, leaving this scalar expression unchanged.
This is an endomorphism trace, never a scalar pairing on G with itself.

Third, check that both unit tests concern actual elements of R.
Since m=(x,y), v=xa+yb with a,b in R^26. Reducing this identity modulo
m^2 and using (3) forces a mod m=q_1 and b mod m=q_2. L134's actual
negative-weight rank makes a two-by-two minor a unit, so P=Ra+Rb is
an actual free direct summand. The equality rho v=0 is exact.
Regular-sequence Koszul exactness therefore gives the actual t in
(10), not a sequence of approximations. Reducing these equalities
modulo m^2 gives

\[
 B_{11}=B_{22}=0,\qquad B_{21}=t\bmod\mathfrak m=-B_{12}.
\]

Together with the checked trace identity, this yields
t mod m=-lambda sigma_B(u_1,u_2), which is nonzero because u_1,u_2
are a tangent basis and sigma_B is symplectic. Hence t is a unit in
the original algebraic stalk. Neither rank alone nor the last-row
ideal alone supplies this conclusion. The positive-weight rank is
retained through L145's outgoing-row calculation, although the
nonzero trace also verifies the needed restriction to P here.

Finally, minimality puts every complementary row entry in m, and
the unit t gives rho(P)=m. Each row entry thus has an actual preimage
p_j in P. Replacing e_j by e_j-p_j is a triangular change of basis
with identity on H/P; it preserves P and gives H=P direct sum Q'
with rho(Q')=0. The incoming vector still lies entirely in P and
still has coordinates (x,y). This verifies the whole direct-sum
complex (12), with every higher coefficient present, over R itself.
Koszul exactness gives zero middle cohomology for its rank-two part.
Thus the inclusion Q' into ker rho induces the claimed isomorphism
Q' -> M, of rank 24, without completion or ordinary middle base change.

The canonical evaluation of a finite free module is an isomorphism;
this is also the free case in
[Stacks Lemma 15.24.6, 0AV2](https://stacks.math.columbia.edu/tag/0AV2).
Its Noetherian-domain hypotheses hold for the smooth surface stalk R.
Naturality of evaluation under Q' -> M identifies this free evaluation
with the actual M -> M^{**}. Hence the hull quotient, not just a
chosen abstract comparison, is zero. The ordinary fibre dimension is
24 while the derived middle dimension remains 26, accounted for by
the minimal Koszul summand.

Only L134's weight ranks are needed, not its third-jet conclusion.
The direct inputs remain L071, L094, L095, L134 and L145; L111 is
comparison only. No global extension of a metric, image polystability,
effective index, split-locus nonemptiness or kernel existence is
established. All earlier IT, effectivity, strict-Euler and necessary-jet
stops survive. Full matching Mathlib coverage remains not checked.

## Mathlib

Full matching Mathlib coverage for this conditional twisted-family
specialization is **not checked**. The general local-algebra and
coefficient tools are imported by the precise citations above.
Unknown coverage is not absence. The actual boundary, trace/unit
test and complete splitting are the written specialization; no
originality claim or numerical certificate is made.
