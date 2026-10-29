# Global obstruction isotropy and the point projection — source comparison

TARGET: Assess whether Calabi-Yau fourfold obstruction isotropy constrains L164's point bracket when the complementary global obstruction component is retained.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 545 searched CY4 isotropic Kuranishi/Serre, cyclic obstruction, product/holonomy and isotropic-cone projection terminology; inspected the primary statements and proof cases listed below. Scoped local checks reused histories/540-544, the two bracket assessments and ATTEMPTS/068,/077,/080,/092; no matching global-projection theorem was found, with no novelty claim.
SOURCE_EVIDENCE: Read Cao--Leung 1407.7659v2 Section 10.3, Theorems 10.7-10.8 and the complete proof of 10.8; PTVV 1111.3209v4 Theorem 2.5 and its pairing proof, Calabi-Yau-source example and Corollary 2.6(3); BBJ 1305.6302v4 Example 5.16, Theorem 5.18 and Corollary 5.20 with the intervening fixed-determinant discussion; Borisov--Joyce 1504.00690v2 Theorem 1.1, Examples 3.3/3.8 and Section 3.8; EKM Chapter I Proposition 1.6/Corollary 1.9; actual trace-duality and Mathlib sources below.
COMPARISON: The narrow Cao--Leung analytic theorem cannot be imported at this product. Broader shifted-symplectic sources permit a determinant-fixed product framework but provide no compatibility with j,a or separate point-bracket constraint. They justify testing the limitations of a full isotropy condition, with H^1(B,M) retained, rather than inferring quotient vanishing.
GAP: No source determines either actual obstruction component, t, beta, or a Serre-compatible splitting for L116's arrows. Full-map isotropy for this exact analytic presentation is not established here; the proposed continuation only tests pointwise isotropic lifts and does not need that application.
REASON: Essential sources are now accessible and compared. A bounded actual-duality cancellation test is source-covered in a separate newly written SPECIALIZE assessment; it requires separate approval before mathematics. No specialization, new lemma or mathematical calculation is performed in this literature-only turn.

## Exact proposed test and relevance

The main gap is primitive Hodge realization; existence of the equality
kernel F remains unproved. The intermediate question is whether a
source-covered isotropy statement for the full quadratic obstruction
in H^2(X,End_0(F)), paired by fourfold Serre duality, gives any constraint
on L164's actual beta. Its plausible use is to compare an independently
specified global quadratic condition with the point obstruction.
It need not determine all sections or prove F nonexistent to be useful.

Retain L071's identical marked K3 factors, common metric and ordered
triple, integral c_1=0, and prescribed full character
2-14e_1-21e_2-tau_D+62P. Use L116 and audited L164, with L094/L111
through them; keep the actual j and a, full M,W,H and unknown t,Z.
No cross-notebook input. X has trivial canonical bundle but is a
product with holomorphic two-forms: a theorem requiring strict
Calabi-Yau holonomy or vanishing intermediate structure-sheaf
cohomology cannot silently be imported. Check real-Kahler stability
and determinant-fixed versus full endomorphism scope as well.

The proposed source review must search the exact statement, standard
terminology, stronger results and known obstructions, then inspect
primary hypotheses and essential proof cases. Distinguish a quadratic
Yoneda identity from an isotropic full Kuranishi map, and a formal
derived-moduli statement from an actual cohomological consequence
for this fixed projection. General DT4 existence statements are not
enough. No virtual cycle or orientation theorem is presently needed.

L116's short exact sequence for H^2 has kernel H^1(B,M) and quotient
H^0(B,W). Retain that kernel throughout; its vector-space splitting
does not specify an orthogonal or positive splitting of the Serre
form. An isotropy identity for the full obstruction must not be
replaced by isotropy, zero norm or vanishing of its quotient component.
No calculation of such an identity is undertaken in this proposal.

Continue only if inspected sources give either an applicable constraint
with a concrete test using these actual maps, or a bounded test of
whether the complementary component can cancel it. If the statements
require unavailable hypotheses or merely return the uncontrolled full
obstruction without an independently testable comparison, park this
proposal with that precise evidence. Do not repeat formality, spectral
or section-vanishing audits. F existence, t, the two obstruction
components, transport and primitive realization remain unresolved.

## Duplicate and failure boundary

ATTEMPTS/068 stops repeating additive Leray/section counting; /092
stops local section-image vanishing without independent information.
The spectral assessment of step 540 already distinguishes formality
from bracket vanishing. ATTEMPTS/077 concerns Chern-form positivity
with missing curvature hypotheses; /080 concerns scalar-curvature
index and generic-trianalytic source mismatches. None supplies the
new full-obstruction pairing comparison. These stops stay preserved;
the targeted absence of a matching local assessment claims no novelty.
Full matching Mathlib coverage is not checked.

LITERATURE_REASON: The invocation-start target introduced essential unread global fourfold obstruction-isotropy sources outside the ready local cup/base-change assessment; step 545 completes that source comparison.

## Step 545: inspected sources and applicability

The preceding proposal records the starting question and tests. The following
comparison supersedes its unread-source status. This is LITERATURE /
EXPLORATION / NOVELTY_UNCHECKED: new source coverage, not a mathematical
result beyond the sources or a computation of the actual projection.

1. Cao--Leung, *Donaldson-Thomas theory for Calabi-Yau 4-folds*,
   [arXiv:1407.7659v2, 24 September 2015, Section 10.3,
   printed pp. 43-44](https://arxiv.org/pdf/1407.7659v2#page=43).
   **Theorem 10.8** assumes a Gieseker stable-sheaf moduli space and
   Hol(X)=SU(4). It produces a holomorphic Kuranishi map with
   Q(kappa,kappa)=0 for the Serre form. The proof uses Seidel--Thomas
   reduction, Chern--Weil (43), a harmonic/coexact curvature
   decomposition, both cross/coexact pairing vanishings, and the
   Hodge type of ch_2. None evaluates a Leray quotient. The theorem
   does not directly cover this product or its real polarization.
   Extending its bundle proof would require a separate specialization,
   not dropping its printed hypotheses. Theorem 10.7 quotes BBJ;
   Remark 10.9 and Proposition 10.11 distinguish different Kuranishi
   presentations. The older indexed theorem number 10.7 for the
   analytic assertion must not be used with v2.

2. Pantev--Toen--Vaquie--Vezzosi, *Shifted Symplectic Structures*,
   [1111.3209v4, 22 April 2013, Theorem 2.5 and its proof,
   printed pp. 32-33; Calabi-Yau source pp. 35-36;
   Corollary 2.6(3), p. 36](https://arxiv.org/pdf/1111.3209v4#page=33).
   The mapping theorem assumes an O-compact, O-oriented source and
   a mapping stack locally of finite presentation that is derived
   Artin. The example verifies these using smooth properness,
   connected fibres and a canonical-bundle trivialization, without
   intermediate H^i(O) vanishing. Corollary 2.6(3) concerns reductive
   G with a nondegenerate invariant symmetric Lie-algebra form.
   Its tangent pairing is cup, coefficient form and Serre trace.
   Thus X and G=SL_2 give the appropriate framework for V: the fixed
   product volume trivializes K_X and the trace form on sl_2 is
   invariant and nondegenerate. A determinant trivialization is
   available for conditional F since Pic^0(X)=0 and integral c_1=0.
   This framework is independent of polarization. No actual j,a
   compatibility or full analytic Kuranishi specialization is proved.

3. Brav--Bussi--Joyce, *A Darboux theorem for derived schemes with
   shifted symplectic structure*, [1305.6302v4, 29 August 2018,
   Example 5.16/(5.28), printed pp. 33-35; Theorem 5.18 and
   Corollary 5.20, pp. 35-37](https://arxiv.org/pdf/1305.6302v4#page=34).
   Over characteristic zero, a negative shifted-symplectic derived
   scheme has minimal Darboux presentations, weak Zariski and strong
   etale in degree -2. The degree -2 example yields an orthogonal
   bundle with an isotropic section whose zero scheme is the classical
   truncation. Corollary 5.20 gives the corresponding simple-sheaf
   chart. The application defines Calabi-Yau by smooth projective
   with trivial canonical bundle and discusses fixed determinant
   and etale charts for algebraic spaces. On this product one must
   retain trace-free obstruction spaces: full Ext^2 contains a scalar
   H^2(O_X) summand. Its displayed full-Ext ranks cannot silently be
   substituted for H^2(V). Nor is a chosen chart section identified
   with a particular Dolbeault map by an isomorphism of zero loci.
   The inspected sources support local isotropic models; they do not
   supply the actual projection comparison required here.

4. Borisov--Joyce, *Virtual fundamental classes for moduli spaces of
   sheaves on Calabi-Yau four-folds*, [1504.00690v2,
   24 November 2016, Theorem 1.1, Examples 3.3/3.8 and
   Section 3.8](https://arxiv.org/html/1504.00690v2).
   The general theorem starts with a separated shifted-symplectic
   derived scheme and a second-countable analytic space. Example 3.8
   identifies its minimal-chart quadratic form with the tangent
   obstruction form. Section 3.8's sheaf-counting application imposes
   H^i(O)=0 for 0<i<4, and Claim 3.29 is explicitly a claim about
   passing from stacks to schemes. Neither that application nor an
   orientation/virtual-cycle theorem resolves this product's projection.

## Bounded continuation and source coverage

The next test is recorded in
[the isotropic-lift assessment](2026-10-25-global-point-quotient-isotropic-lift.md).
It asks only whether the Q-null cone maps onto the point quotient for
the actual Q,j,a. It grants full-obstruction isotropy as a condition
whose information content is being tested; it need not extend any
full Kuranishi theorem. This avoids source-blocked dependent work.
No answer, orthogonality assertion or cancellation formula is derived here.

The reusable duality sources are [Stacks 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT),
[48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81) and
[48.27.1-2, 0FVU](https://stacks.math.columbia.edu/tag/0FVU).
Their statements, cup/trace construction, triangle compatibility and
smooth proper cases were inspected. Local freeness of V, perfectness
of C, and the fixed volume forms meet their hypotheses as already
used in L109/L116. The actual retraction r in L116, not an arbitrary
additive splitting, is the appropriate comparison datum.

For the scalar quadratic tools, inspect Elman--Karpenko--Merkurjev,
*The Algebraic and Geometric Theory of Quadratic Forms*, AMS
Colloquium Publications 56 (2008), Chapter I, Proposition 1.6 and
Corollary 1.9, [author PDF, printed pp. 13-15](https://www.math.ucla.edu/~rse/book/Kniga.pdf#page=23).
The former splits off a subspace on which the form is nondegenerate;
the latter diagonalizes symmetric forms in characteristic different
from two. These cover the general linear algebra, not the actual
restriction to H^1(B,M) or the requested lift. Reproof of those known
theorems is unnecessary. The specialization must verify that restriction,
its nonzero dimension, all signs and the actual quotient first.

Mathlib supporting coverage was inspected in
[QuadraticForm.AlgClosed](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/AlgClosed.html):
`QuadraticForm.equivalent_weightedSumSquares_of_isAlgClosed` assumes
finite dimension, an algebraically closed field, invertible 2 and
a separating associated form. Its linked source was checked at
commit `10dc7882b0311638b63e9aad5506f2cfcf4e61b8`.
This is a scalar normal-form input only. Full actual derived-duality,
Kuranishi/projection and isotropic-lift coverage is not checked.

Search queries included `Cao Leung Donaldson Thomas theory Calabi Yau
4 folds Kuranishi map Q kappa kappa zero holonomy Sp2`, `Borisov Joyce
Darboux theorem isotropic Kuranishi map Calabi Yau fourfold Serre
duality trace free`, `"Kuranishi" "cyclic" "isotropic" "Calabi-Yau"`,
`"isotropic cone" "projection" "nondegenerate" quadratic subspace`
and targeted Mathlib/Stacks quadratic-form queries. The narrow primary
references above, rather than snippets, are the evidence. Shell download
failed DNS; browser primary PDFs resolved access. HTML find failures
were bypassed with targeted PDF ranges. There is no persistent source
blocker. Unread virtual-cycle and orientation leads are unnecessary.

If the pointwise lift test is positive, park scalar-isotropy-only
projection exclusion; it would leave possible polynomial and geometric
compatibility restrictions untested. If a quotient vector has no lift,
record that actual necessary condition before any further bracket
claim. In either case actual beta, both obstruction components, t,Z,
F existence, transport and primitive realization remain undetermined.
