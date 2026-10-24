# L145 — Twisted defining-coefficient top stalk at a split equality fibre

## Hypotheses

Retain L071's identical marked projective K3 factors S_1 and B=S_2,
their common hyperkähler metric g, real Kähler class h and full integral
mixed tensor tau_D. Let k=(-4,-2,1,2) be the zero-slope divisor class,
with k^2=-14, and L the line bundle on S_1 with c_1(L)=k.
Suppose F is locally free of rank two and slope-polystable at
Omega=p_1^*h+p_2^*h, with integral c_1(F)=0 and

\[
             \operatorname{ch}_2(F)=-14e_1-21e_2-\tau_D.
\]

Select an actual split parameter z with F_z=L direct sum L^{-1}.
Use L094/L095's natural actual-family KS identification and L134's
audited conclusion that both weight projections of that complex-linear
KS map have rank two. The twist p_1^*L^{-1} is fixed as the parameter
varies. Write

\[
 G=F\otimes p_1^*L^{-1},\quad C=Rp_{2*}G,\quad W=R^2p_{2*}G,
 \qquad R=\mathcal O_{B,z},\quad \mathfrak m=\mathfrak m_z.
\]

Neither F nor a split parameter is known to exist. L096 permits the
split set to be empty. No ordinary split-point base change, odd IT,
twisted self-duality, cohomology constancy or stalk length is assumed.

## Conclusion

At every selected actual split parameter,

\[
                W_z\simeq R/\mathfrak m,\qquad
                \operatorname{length}_R W_z=1.                 \tag{1}
\]

The isomorphism requires a generator choice; annihilation by the
maximal ideal and the length are intrinsic. The actual last-row
cotangent rank is two, equal to the required base cotangent dimension.
This is a conditional ADVANCE / REPRODUCTION of the covered tools.
The separate critical audit below preserves it without a stronger
conclusion. It supplies a local multiplicity
for a possible later twisted-complex defect comparison. It supplies
no global index effectivity, kernel existence, nonempty split locus,
cycle, reconstruction, transport or universal primitive Hodge realization.

## Proof

**Imported results and scope.** Reuse the pre-invocation SPECIALIZE
assessment `drafts/literature/2026-10-21-twisted-split-top-stalk-length.md`.
Budur–Wang, *Cohomology jump loci of differential graded Lie algebras*,
Compositio Math. 151 (2015), 1499–1528, DOI 10.1112/S0010437X14007970,
[arXiv:1309.2264v2, Definitions 3.2/3.8, Proposition 3.10,
Lemma 3.11, Theorem 6.4 proof (9)–(10), and Remark 6.5](https://arxiv.org/html/1309.2264v2#S6),
provides the fixed-tensor Dolbeault-module comparison with actual
deformation cohomology; Remark 6.5 covers arbitrary holomorphic
bundles on a compact complex manifold. Here the manifold is compact
K3, the central bundle is locally free, and the module is the defining
bundle with its fixed line twist. Simplicity and zero Chern classes
are unnecessary for that comparison. Theorem 1.3's resonance/formality
conclusion is not used. L110 concerns the adjoint coefficient and
serves only as a comparison, not as an input proving (1).

Import perfect pushforward and derived base change from
[Stacks Lemma 36.30.1, 0A1H](https://stacks.math.columbia.edu/tag/0A1H).
The projection is smooth projective and finitely presented, G is
locally free and base-flat with proper support, and O is the perfect
first input. Thus all hypotheses hold, including for dual-number
pullbacks. Minimal finite-free representatives are
[Lemmas 15.77.6–7, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
and [0BCD](https://stacks.math.columbia.edu/tag/0BCD).
Connecting-map naturality is
[Lemma 12.13.12, 0117](https://stacks.math.columbia.edu/tag/0117).
Use the projective GAGA cohomology comparison on S_1 and actual
dual-coefficient cup/trace Serre duality; relative trace and its
pairing compatibility are
[Remarks 48.12.5–6, 0B6S](https://stacks.math.columbia.edu/tag/0B6S)
and [0G81](https://stacks.math.columbia.edu/tag/0G81).
The proper flat finitely presented projection and locally free
evaluation pairing satisfy those hypotheses. The final local algebra
is Nakayama, [Lemma 10.20.1, 00DV](https://stacks.math.columbia.edu/tag/00DV).
These general theorems are imported. The calculation below is needed
because none states this family's defining-coefficient rank or length.

**Central cohomology and the whole top presentation.** At z,

\[
                 G_0=\mathcal O\oplus L^{-2},\qquad
                 G_0^\vee=\mathcal O\oplus L^2.                \tag{2}
\]

L094's line calculation gives H^0(L^{+/-2})=H^2(L^{+/-2})=0 and
h^1(L^{+/-2})=26. Its hypotheses are k nonzero, k.h=0 and k^2=-14:
a nonzero effective divisor has positive h-degree, Serre duality
gives the other endpoint, and line RR gives 2+(2k)^2/2=-26.
The standard K3 formulas are Huybrechts, *Lectures on K3 Surfaces*,
author-hosted draft, [Chapter 1, Section 2.3/(2.5), pp. 11–12](https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf#page=11).
Together with h^*(O)=(1,0,1), (2) gives h^*(G_0)=(1,26,1).

Consequently the actual perfect C has a minimal representative over R

\[
 K:\quad R\xrightarrow{d^0}R^{26}\xrightarrow{d^1}R,
       \qquad d^i\equiv0\pmod{\mathfrak m},                    \tag{3}
\]

in degrees 0,1,2. The ranks come from derived fibre cohomology, not
ordinary sheaf base change. If I is the ideal of all entries of d^1,
then I is contained in m and the whole ordinary stalk is W_z=R/I.
All higher parameter terms in both differentials remain in (3).

**The actual coefficient connecting sequence.** For u in T_zB let
A=C[epsilon]/(epsilon^2) be the base pullback defined by u. The actual
bundle G_A on S_1 x Spec A gives, after forgetting A, the coherent
coefficient sequence on the projective S_1

\[
              0\longrightarrow G_0\xrightarrow{\epsilon}G_A
                       \longrightarrow G_0\longrightarrow0.  \tag{4}
\]

Its derived pushforward triangle is identified with the triangle of
0 -> K_C -> K_A -> K_C -> 0 by natural derived base change. Concretely,
a finite affine Čech complex for G over Spec R is bounded and R-flat:
on each affine intersection G is a finite projective module over an
R-flat product algebra. Its scalar extensions compute the actual
coefficient cohomology. A comparison from the bounded free K to that
complex and its scalar extensions identifies the exact triangles and
their connecting homomorphisms. Thus the degree-one connecting map
of (4) is exactly the linear last-row evaluation ell(u):H^1(G_0) ->
H^2(G_0). In (3) this also follows by lifting a degree-one residue
vector, applying d_A^1=epsilon ell(u), and dividing by epsilon.
Exact projective GAGA on (4) identifies the same connecting map with
the analytic one; it does not require ordinary R^1 base change.

In a smooth splitting the actual central Dolbeault differential is
bar-partial_E+epsilon a_u. Its class is the natural actual KS class.
The determinant is holomorphically trivial (integral c_1=0 and
Pic^0(S_1 x B)=0), so a trace-free representative is available.
Since H^1(O)=0, its diagonal class is zero; by a first-order smooth
gauge choose a closed representative

\[
       a_u=\begin{pmatrix}0&p(u)\\q(u)&0\end{pmatrix},\quad
       p(u)\in H^1(L^2),\quad q(u)\in H^1(L^{-2}).             \tag{5}
\]

L094/L095 identify this natural KS with the actual harmonic derivative,
and L134 proves each of u -> p(u) and u -> q(u) has complex rank two.
The map is taken before the stabilizer quotient. Changing the allowed
constant central marking rescales each weight block invertibly.

Twisting by the fixed L^{-1} leaves the matrix action (5) unchanged.
The coefficient differential on a degree-j G_0-valued form b is
bar-partial b+epsilon a_u wedge b. This is one-sided defining action,
not the adjoint commutator. On cohomology every middle class is (0,b),
with b in H^1(L^{-2}), so (4) gives

\[
                 \ell(u)b=[p(u)\wedge b]\in H^2(O)
                                      =H^2(G_0).              \tag{6}
\]

Gauge changes of a_u alter (6) by a coboundary. No constancy of the
degree-zero or degree-two fibre cohomology near z was used.

**Correct dual coefficient and full cotangent rank.** Fix a nonzero
holomorphic fibre two-form sigma and the Serre functional
T(t)=integral_{S_1} sigma wedge t on H^2(O), with any fixed nonzero
normalization. Serre duality makes

\[
 H^1(L^2)\times H^1(L^{-2})\longrightarrow\mathbf C,
                       (c,b)\longmapsto T(c\wedge b)         \tag{7}
\]

perfect. The dual coefficient is G_A^vee, with central fibre in (2).
Its unique central section up to scalar is s=(1,0), the row projection
onto O. The dual differential on a degree-zero row section is
bar-partial s-epsilon s a_u, by differentiating the evaluation pairing.
Its actual degree-zero connecting class is therefore

\[
                    \delta^\vee_u(s)=(0,-p(u))
                                   \in H^1(G_0^\vee).         \tag{8}
\]

With the degree-one dual coefficient placed first in the evaluation
cup product, equations (6)–(8) give the explicit transpose identity

\[
 T\big(s\,\ell(u)b\big)
       =T(p(u)\wedge b)
       =-T\big(\delta^\vee_u(s)\wedge b\big).                \tag{9}
\]

This retains the dual connection sign and the odd cup order. The
endpoint evaluation is nonzero because s is the O projection and
H^2(G_0)=H^2(O). In particular, no scalar self-duality of G is asserted;
its two line twists in (2) are different.

If ell(u) vanishes on all H^1(G_0), (6) and the perfect pairing (7)
force p(u)=0. L134's rank-two positive-weight projection then forces
u=0. Hence u -> ell(u) is injective on the two-dimensional T_zB.
The transpose of the linear last row

\[
            H^1(G_0)\longrightarrow\mathfrak m/\mathfrak m^2
\]

is this injective map after choosing the generator of H^2(G_0).
Finite-dimensional duality proves surjectivity of the last-row map.
Thus its actual rank is two, exactly the required cotangent rank.
Testing all b in H^1(L^{-2}), rather than just family tangent classes,
is essential here.

**From first variation to the entire ordinary stalk.** The last-row
entries therefore satisfy I+m^2=m. The finite R-module m/I obeys
m(m/I)=(m^2+I)/I=m/I. Nakayama yields m/I=0, so I=m. This proves
(1) for the whole ordinary cokernel, including all higher coefficients
in (3). The equality is not inferred from derived top dimension one
or from finite support. R is a Noetherian regular local surface ring
with residue field C, so R/m indeed has length one.

The continuation test succeeds locally. The parked all-fibre IT and
global effectivity mechanisms are untouched: G_0 has nonzero endpoint
cohomology, and a length-one top stalk alone supplies no global positive
cycle or inequality. The split locus may be empty, making the local
statement vacuous; F and universal primitive Hodge realization remain
unproved. The separate audit below checks the natural sequence, the
correct dual transpose and the rank-to-whole-length passage.

**Independent critical audit, 2026-10-22 (step 463).** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-21-twisted-split-top-stalk-critical-audit.md`
and the precise primary inputs cited above. This audit finds no
substantive error, necessary repair or stronger conclusion. Its outcome
is EXPLORATION / REPRODUCTION, not a new mathematical advance.

First check the algebraic-to-analytic naturality in (4). Local freeness
of G makes its pullback flat over A, so multiplication by epsilon
identifies its kernel and quotient with G_0. The fibre S_1 is fixed;
the line twist has no parameter deformation. For a finite affine
cover of S_1, every intersection remains affine because S_1 is
separated. Its product with Spec R has R-flat coordinate algebra;
the locally free G gives a finite projective module over that algebra.
The resulting bounded Cech complex P consists of R-flat modules and
computes C and its actual scalar extensions. The bounded finite-free K
computes derived morphisms by ordinary chain maps
([Stacks Lemma 13.19.8, 064B](https://stacks.math.columbia.edu/tag/064B)), so the
isomorphism K to P in the derived category has a quasi-isomorphism
chain representative. Both complexes are bounded and flat; tensoring
this comparison with A or the residue field preserves the quasi-isomorphism.
The sequence 0 -> \(\mathbf C\) -> A -> \(\mathbf C\) -> 0 therefore gives a map
between their short exact complex sequences. Connecting-map naturality
identifies the two boundaries, including their sign. Minimality makes
the degree-one boundary exactly the epsilon coefficient of d_A^1.
Exact GAGA applies to the coherent sequence on the projective S_1
after the finite dual-number projection is forgotten. Consequently
the Dolbeault boundary (6) really computes this algebraic last row.

Second, the central ranks and coefficient action are checked without
ordinary middle base change. Nonzero classes +/-2k have zero h-degree
and cannot be effective, and their negatives have the same property.
Serre duality and RR give (0,26,0) for both line cohomologies, hence
(1,26,1) for G_0. These are precisely the ranks of the minimal K.
In the ordered splitting (L,L^{-1}), the upper-right KS component is
p(u) in H^1(Hom(L^{-1},L))=H^1(L^2). Tensoring the whole splitting
by the fixed L^{-1} makes the coefficient (O,L^{-2}) but leaves this
endomorphism entry unchanged. Its one-sided action on (0,b) is
(p(u) wedge b,0). There is no adjoint commutator or factor two.
Diagonal deformation classes vanish by H^1(O)=0; removing their exact
representatives changes no boundary on cohomology.

Third, evaluation into O fixes the dual sign independently of any
self-duality convention. For a degree-zero dual row s, the compatibility
identity is d(s b)=(d^vee s)b+s(db). With d=d_0+epsilon a_u, the
variation of d^vee s is -epsilon s a_u. Thus the actual section
s=(1,0) has boundary (0,-p(u)) in O plus L^2. Placing that degree-one
dual coefficient before b gives -p(u) wedge b, exactly the minus sign
in (9). Reversing the two degree-one factors would introduce the
additional odd interchange sign. The endpoint functional is nonzero
on H^2(O); Serre duality pairs every class of H^1(L^2) perfectly with
the entire H^1(L^{-2}). No restriction to the two-dimensional family
tangent image is permitted or used.

Finally, L134's audited rank passage uses the actual derivative:
L095 gives injectivity and L094's actual real moment equation equates
the two weight norms. Thus either weight projection has zero kernel
on its complex two-dimensional source. Constant allowed central
markings rescale the blocks invertibly, preserving this rank. It
follows that the boundary u -> ell(u) has rank two, so the actual row
entries span m/m^2. Since I is contained in m, the finite module m/I
satisfies m/I=m(m/I); the cited Nakayama lemma gives I=m, without
discarding any higher coefficient of d^1. Minimality also ensures
I is proper, so the cokernel is nonzero and its length is exactly one,
not merely at most one. This proves the claimed entire ordinary stalk.

Only the weight-rank part of L134 is used, not its higher-jet or image
ring conclusion. L096's global finiteness and L110's different adjoint
coefficient are not inputs to the local length proof. The direct inputs
remain L071, L094, L095 and L134. The audit supplies no middle-module
freeness, metric extension, effectivity or inequality; the split locus
may be empty and F remains hypothetical. Full matching Mathlib coverage
remains not checked.

## Mathlib

Full matching coverage of this conditional twisted defining-module
stalk specialization is **not checked**. The general results are
imported by the precise citations above; no absence or novelty claim
is made. The actual coefficient action, dual sign and cotangent
specialization are written out here without a numerical certificate.
