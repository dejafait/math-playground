# L117 — Actual scalar cup map and the remaining global entry

## Hypotheses

Retain the complete conditional equality family and actual maps of L116,
including its inputs L108/L109/L111/L115. In particular, on the original
common-metric product X=S_1 x B, the hypothetical locally free rank-two F
has integral c_1=0, ch_2=-14e_1-21e_2-tau_D and the compatible connection
of L071. Set V=End_0(F), C=Rp_*V, M=R^1p_*V and W=R^2p_*V.
The finite split set Z may be empty. Use L116's actual triangle

\[
 M[-1]\xrightarrow{j}C\xrightarrow{a}W[-2]\longrightarrow M
\]

and its global retraction r, with rj=id. Here M is locally free,
W has finite support, M=T_B direct sum N, and N is slope-zero
polystable with full trivial summand O_B^t. L116 gives
h^0(M)=h^2(M)=t and its stated cardinality constraints. Existence of F,
a value of t, independent factorwise rotation invariance, and a
multiplicative Leray splitting are not assumed.

Let theta_1 and theta_2 be the conjugate metric symplectic classes on
S_1 and B, respectively, with exactly the normalization for which the
product class is x=p_1^*theta_1+p^*theta_2. Denote by ell_1:C -> C[2]
the actual pushforward of scalar cup with p_1^*theta_1.

## Conclusion

There is a uniquely determined actual class

\[
 A_1\in\operatorname{Ext}^2_B(M,M),\qquad
                  \ell_1j=j[2]A_1.                         \tag{1}
\]

In (1), A_1 denotes the shifted morphism M[-1] -> M[1]. Under the
canonical isomorphisms induced by j in L116, the actual scalar cup map is

\[
 H^1(X,V)\longrightarrow H^3(X,V),\qquad
 H^0(B,M)\xrightarrow{\ J+\Phi_1\ }H^2(B,M),              \tag{2}
\]

where J is cup with theta_2 and Phi_1 is the map induced by A_1.
J is an isomorphism. Thus the imported coefficient Lefschetz theorem
requires precisely

\[
 \det(1+K)\ne0,\qquad K=J^{-1}\Phi_1\in
                     \operatorname{End}(H^0(B,M)).         \tag{3}
\]

For t=0 this is the empty-dimensional isomorphism. For t>0 the
retained inputs do not evaluate Phi_1. In particular fibrewise degree
vanishing does not set A_1 to zero. This bounded test reaches an
uncontrolled actual global cup entry and supplies no additional
cardinality exclusion beyond L116. Park the coefficient-Lefschetz
exclusion mechanism unless independent information evaluates that entry.
This is NEGATIVE / REPRODUCTION of assessed tools, not a new theorem
beyond the checked sources or an existence assertion. The separate critical
audit below preserves this specialization, with outcome EXPLORATION /
REPRODUCTION and no substantive error or stronger exclusion found.
It supplies no normal section
count, F, cycle, transport or universal primitive Hodge realization.

## Proof

**Known input and scope.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-equality-coefficient-lefschetz-constraints.md`.
Import M. Verbitsky, *Hyperholomorphic bundles*,
[arXiv:alg-geom/9307008v1](https://arxiv.org/pdf/alg-geom/9307008v1),
29 July 1993, Theorems 4.2/4.2.A, PDF pp. 16--17, only for the
symplectic Lefschetz isomorphism. These are preprint theorem numbers;
the published version was not inspected. Definition 1.1 and the
coefficient operator proof allow this compact product with its diagonal
hyperkahler triple. L071's actual connection induces a hyperholomorphic
connection on V; the trace-free projection is parallel. In complex
dimension four the imported conclusion is x cup -:H^1(X,V) -> H^3(X,V)
an isomorphism. The assessment checks the real-coefficient convention
and passage to (0,*) forms. Do not import the preprint's printed
middle-degree one-step injection endpoint, scalar-ring equality, or an
independent harmonic Lefschetz action for either factor. The theorem
is cited, not reproved. The specialization below computes its actual
map through L116, rather than checking dimensions again.

Use L116's already justified canonical truncation and derived-global-
section framework (Stacks 13.12.4, [08J5](https://stacks.math.columbia.edu/tag/08J5),
and 20.13.1--4, [01EY](https://stacks.math.columbia.edu/tag/01EY)).
The actual j is split before any scalar action is considered.

**The fibre term and its shifts.** The composite

\[
 M[-1]\xrightarrow{j}C\xrightarrow{\ell_1}C[2]
                              \xrightarrow{a[2]}W
\]

belongs to Hom_D(M[-1],W)=Ext^1_B(M,W). Since M is locally free,
this Ext group equals H^1(B,M^vee tensor W). Indeed internal Hom
from M is the exact functor M^vee tensor -, and derived global Hom
therefore computes precisely this sheaf cohomology. The tensor has
finite support, so its positive-degree cohomology vanishes, as for W
in L116. The composite is zero globally, not merely at each stalk.

Apply Hom_D(M[-1],-) to the shifted truncation triangle
M[1] -> C[2] -> W -> M[2]. Exactness supplies a factorization
ell_1j=j[2]A_1. The map j[2] has left inverse r[2], so the
factorization is unique, and A_1=r[2]ell_1j. In particular

\[
 \operatorname{Hom}_D(M[-1],M[1])=
                      \operatorname{Ext}^2_B(M,M).
\]

This identifies an actual global class, rather than replacing the
coefficient complex by a freely assigned matrix. Its independence
of a chosen splitting follows from uniqueness with this fixed j.

Locally the last Ext group vanishes because M is a vector bundle,
while globally it is H^2(B,End(M)), which need not vanish.
Consequently local degree or local splitting arguments cannot remove
this component. The relative fibre cup sends degree-one fibre
cohomology to degree three, hence zero on a surface; that statement
about fibres does not evaluate the global Ext^2 entry in (1).

**The base term and actual cohomology.** Scalar cup by theta_2 on B
is the central natural transformation D(B) -> D(B)[2]. Naturality
with j, or the projection formula on Dolbeault representatives, gives

\[
              \ell_2j=j[2]\,\mu_{2,M}.              \tag{4}
\]

Here mu_{2,M}:M[-1] -> M[1] is ordinary scalar cup on M.
The degree is even, so shifting j introduces no odd interchange sign.
This is naturality for the actual morphism j, not multiplicativity
of an additive decomposition of C. L116 identifies H^1(X,V) with
H^0(B,M) and H^3(X,V) with H^2(B,M) by this same inclusion: the
remaining summand W[-2] contributes in degree two only. Apply derived
global sections to (1) and (4), and use x=theta_1+theta_2, to obtain
(2). Possible derived effects of fibre cup survive as Phi_1; none
has been discarded by looking only at the Leray associated graded.
The supported summand cannot contribute to either endpoint in (2).

**Why the base map is already invertible.** L116 gives an actual
holomorphic decomposition N=O_B^t direct sum A with H^0(A)=0.
Also H^0(T_B)=0. Thus every section of M lies in this full trivial
summand. Cup with nonzero theta_2 maps H^0(O_B^t) isomorphically
onto H^2(O_B^t), since H^2(B,O_B) is one-dimensional on a K3.
The inclusion of a direct summand injects its H^2 into H^2(M).
The latter has dimension t by L116, so this injection is surjective
as well. This proves J invertible, using actual polystability and
cohomology, with no assigned value of t or acyclicity assumption.

It follows that (2) equals J(1+K). Verbitsky's theorem is exactly
condition (3) on this map. No retained calculation determines K,
and the theorem does not determine it either. The known dimensions
alone do not violate (3): for a vector space of any admitted dimension,
1+0 is invertible. This last elementary observation only describes
why the dimension test cannot exclude a case; it assigns no operator
to F and claims no compatible realization of all its other structures.
In particular we have neither proved Phi_1=0 nor found an eigenvalue
-1 for its actual normalized map. Establishing either requires more
information than this test supplies. The assessment explicitly directs
stopping when actual cup entries remain uncontrolled. We stop here,
retaining ATTEMPTS/047/063/066/068 and all independent geometric gaps.

**Separate critical audit, 2026-10-17 (step 340).** Use the unchanged
SPECIALIZE assessment
`drafts/literature/2026-10-17-equality-actual-scalar-cup-critical-audit.md`.
L116's actual global retraction and L109/L111's normalized middle form
are retained inputs. This audit checks the scalar-action specialization;
it is not a new proof of all its ancestors or an evaluation of the
unknown fibre entry. The cited Verbitsky theorem is reused with exactly
the product, real-structure, trace-free and Dolbeault qualifications
specified above.

First, the global Ext calculation is justified by
[Stacks 20.44, 0B6A](https://stacks.math.columbia.edu/tag/0B6A)
and the perfect-dual/internal-Hom identifications in
[20.50.5--6, 0FP7](https://stacks.math.columbia.edu/tag/0FP7).
For this finite locally free M they identify
RHom_B(M,W) with RΓ(B,M^vee tensor W). The latter tensor is coherent
with zero-dimensional support on the locally Noetherian surface B.
[Stacks Lemma 30.9.10, 0B3J](https://stacks.math.columbia.edu/tag/0B3J)
therefore kills its positive-degree cohomology, including when W=0.
This is a global vanishing, whereas the same reasoning gives
Ext^2_B(M,M)=H^2(B,End(M)), with no finite-support vanishing available.

The shifts are checked directly: after shifting the actual triangle
by two, its first three objects are M[1], C[2], W. Consequently
a[2] ell_1 j is in Hom(M[-1],W)=Ext^1_B(M,W), and is zero.
Exactness of Hom on this triangle, as in
[Stacks Lemma 13.4.2, 0149](https://stacks.math.columbia.edu/tag/0149),
gives a factor in Hom(M[-1],M[1])=Ext^2_B(M,M).
If two factors had the same image, composing their difference with
r[2]j[2]=id would give zero, proving uniqueness. Hence the factor
is exactly r[2]ell_1j, independent of a choice of retraction once j
is fixed. Uniqueness is not inferred from stalkwise Ext vanishing.
Restriction to a fibre gives no degree-three coherent cohomology on
the K3 fibre, but such restrictions do not detect this global Ext class.

For the base term, represent theta_2 by theta_2:O_B -> O_B[2].
Tensoring this morphism with any object K defines mu_{2,K}:K -> K[2].
The cup construction in
[Stacks 20.31 and Lemma 20.31.1, 0FKU/0FP2](https://stacks.math.columbia.edu/tag/0FP2)
and the natural projection formula
[20.54.2.1 and Lemma 20.54.3, 01E6](https://stacks.math.columbia.edu/tag/01E6)
identify pushforward of cup by p^*theta_2 with mu_{2,C}.
Here the base unit and its shifts are perfect, and p is the actual
morphism of ringed spaces, so the projection-formula hypotheses hold.
Naturality for j gives mu_{2,C}j=j[2]mu_{2,M[-1]}.
Moving a degree-two scalar past the shift by minus one has sign
(-1)^(2*(-1))=+1; thus mu_{2,M[-1]} is precisely the shifted ordinary
base cup used in (4). No fibre-cup naturality over B, independent
factorwise Lefschetz theorem or multiplicative splitting is inserted.

Next apply RΓ to the actual triangle. In degree one the terms of
W[-2] adjacent to j are H^{-2}(W) and H^{-1}(W), both zero.
In degree three they are H^0(W) and H^1(W): the first boundary is
zero because k=0 in L116, and the second group is zero by finite
support. Thus j induces isomorphisms H^0(M) -> H^1(X,V) and
H^2(M) -> H^3(X,V), with these same arrows at both endpoints.
Applying these identifications to the two naturality equations proves
J+Phi_1, rather than just an associated-graded description. In particular
the supported summand has not been silently ignored at the degree-three
boundary.

Finally L116 identifies the full section summand of M with O_B^t
and gives h^2(M)=t. For its actual split inclusion i:O_B^t -> M,
scalar naturality says J H^0(i)=H^2(i) J_triv. Here H^0(i) is an
isomorphism; H^2(i) is injective by the splitting, and an isomorphism
by the dimension t. The map J_triv is invertible since theta_2 is a
nonzero generator of the one-dimensional H^2(O_B). This proves J is
invertible for the actual full section space, including t=0, without
choosing independent endpoint bases or assuming the complement acyclic.
Consequently the cited isomorphism imposes exactly (3) on this map.

The audit preserves the reduction and ATTEMPTS/069's bounded stop.
It finds no substantive error and supplies neither Phi_1 nor a stronger
cardinality exclusion. This says what this reduction has not computed;
it is not a theorem that all the retained geometry is incapable of
controlling Phi_1. Formal invertible matrices are not geometric
realizations. No value of t, kernel existence or nonexistence, cycle,
transverse transport or universal primitive Hodge realization follows.
The completed audit is EXPLORATION / REPRODUCTION, not a second
mathematical advance or a claim of progress beyond the inspected tools.

## Mathlib

Full matching Mathlib coverage for this actual-family scalar-action
factorization and its global Ext entry has not been checked. The
coefficient Lefschetz theorem and standard derived framework are cited
above; unknown coverage is not absence. This is an informal conditional
specialization and a limitation of the bounded exclusion test, not a
formal verification, novelty claim or Hodge-conjecture candidate.
