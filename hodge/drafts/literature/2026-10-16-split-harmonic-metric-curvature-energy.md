# Actual split harmonic metric — curvature-energy source assessment

TARGET: Test local square-integrability of the Chern curvature of L112's actual harmonic metric using its smooth quotient-metric formula and the split-plane geometry.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Target-specific quotient-curvature, cohomology-jump harmonic-metric and higher-direct-image searches; read Demailly's coordinate/block formulas and proofs, Verbitsky's coefficient harmonic statements/proofs and Naumann's exact setup/Theorem 2.1; compare L111/L112, relevant L094/L095 passages and ATTEMPTS/063/066/067.
SOURCE_EVIDENCE: Demailly, Complex Analytic and Differential Geometry (21 June 2012), V.12, (12.2)--(12.3)/Theorem 12.4, pp. 268--269, and V.14, Theorems 14.3/14.5, (14.6)--(14.7), pp. 273--275; Verbitsky alg-geom/9307008v1, section 4, Theorem 4.1/Corollary 4.3, pp. 12--15; Naumann, Ann. Fac. Sci. Toulouse 30 (2021), section 2/Theorem 2.1, pp. 172--174; reuse the prior inspected BGS III and Mourougane--Takayama assessments.
COMPARISON: Known formulas cover Chern differentiation and smooth quotient curvature on the puncture, and the coefficient theorem covers central harmonic quaternionic symmetry without simplicity; no inspected theorem gives finite energy for this actual jump, and positivity-based higher-image results do not match its coefficient hypotheses.
GAP: Establish or refute the needed cancellation for the actual pulled-back central Hermitian product and L111's plane/complement, then control the complete quotient derivatives on a full punctured ball; finite energy is not yet established.
REASON: The bounded source comparison covers the tools for one actual-family specialization, leaving a concrete local calculation; no essential unread theorem blocks that calculation, and a citation alone does not settle its central pairing or derivative estimates.
LITERATURE_REASON: The saved gate requires coverage of the changed curvature-derivative target; the earlier ready norm-bound/audit assessments did not cover derivatives or energy at the jump.
SCOPE: Exactly TARGET for L112's actual metric and extending holomorphic frame, retaining L111/L094/L095 and L071 through them, the full negative tensor and common smooth metrics; Z may be empty; no extension theorem or semistability claim is approved.

## Exact proposed test and limits

Retain hypothetical F, the full negative tensor and the given identical
smooth compatible metrics. Inputs are audited L112 and L111, with
L094/L095's split harmonic geometry and L071 through them; L108's
normal summand and corrected budget explain the downstream use, and
L100 remains a stable-open input only. Z is finite and may be empty.
No cross-notebook result is requested.

The requested threshold is finiteness, on a sufficiently small punctured
ball about each z, of the integral of the squared norm of the Chern
curvature of (M,G). Use the fixed smooth base metric and G's induced
metric on endomorphisms. This is a proposed target, not an estimate.
For empty Z the local assertion is vacuous. No effective universal
energy constant is requested.

The assessment distinguishes general bounded singular Hermitian metrics
from L112's particular smooth finite quotient and retains the natural
holomorphic frame. Central Hermitian orthogonality and derivative
cancellation are obligations for the later mathematical attempt, not
new assumptions or conclusions of this review. No curvature calculation
or new lemma has been performed. In particular the two norm inequalities
alone are not a finite-energy theorem.

Potential use is an analytic prerequisite for later connection-extension
or normal-summand work, whose own theorem hypotheses would still need
review. It would not by itself bound |Z|, construct F, provide transport
or close universal primitive rational Hodge realization. The conditional
budget 800-|Z| is unchanged. This target supplies no new theorem now.

The material difference from ATTEMPTS/066 is the now audited actual
smooth quotient formula and Koszul splitting; the new proposed test is
curvature integrability, not automatic extension from reflexivity.
ATTEMPTS/063's metric/coarse-degree gap, ATTEMPTS/065's compatible cone
test and ATTEMPTS/067's duality-only obstruction remain preserved.
The source comparison below now permits one discriminating finite-energy
attempt. If the needed derivative control does not follow, record the
specific missing input or divergence; do not replace the actual metric
or assume a removable-singularity theorem's energy hypothesis. Full
matching Mathlib coverage has not been checked.

## Primary statements and applicability

**Chern and quotient formulas.** J.-P. Demailly, *Complex Analytic and
Differential Geometry*, version 21 June 2012, Chapter V, sections 12
and 14, [primary text on a university mirror](https://www.ime.usp.br/~cordaro/wp-content/uploads/2022/03/Jean-Pierre-Demailly-Complex-Analytic-and-Differential-Geometry-1.pdf#page=269).
For a holomorphic bundle with a smooth positive Hermitian matrix H in
a holomorphic frame, (12.2)--(12.3) and Theorem 12.4 give the Chern
connection matrix H^{-1} partial H and curvature
bar-partial(H^{-1} partial H). Read their coordinate derivation.
For an exact sequence of holomorphic bundles with smooth ambient metric,
Theorems 14.3/14.5 and (14.6)--(14.7), pp. 273--275, describe induced
and quotient connections/curvatures via the second fundamental form.
Read the block-connection proof, including the proof that its diagonal
correction blocks vanish, and the squaring calculation.

These formulas apply on D minus {z}: L112 identifies the actual metric
there, J is its extending holomorphic frame, and the boundary line has
constant rank there. At z the column vanishes, so section 14 is not a
constant-rank extension theorem. The smooth cutoff metric is pulled
back on the full fifty-two-dimensional middle space, not declared to
be the desired fifty-dimensional harmonic metric through z. Direct
matrix differentiation is allowed; no general theorem is to be reproved.

**Coefficient quaternionic input.** M. Verbitsky, *Hyperholomorphic
bundles*, [alg-geom/9307008v1, 29 July 1993](https://arxiv.org/pdf/alg-geom/9307008v1#page=12),
section 4, pp. 12--15, Theorem 4.1 and Corollary 4.3. Read the operator
definitions, Laplacian equalities/proof and harmonic-preservation proof.
A hyperholomorphic bundle with parallel real structure has the stated
real SU(2) action on holomorphic cohomology, quaternionic in degree one.
The coefficient input does not require a simple bundle. Here it applies
to End_0 of the actual split connection, as already justified in L094.
It is not an application of stable coarse-moduli theorems at a reducible
point. L095 supplies actual KS harmonicity and quaternionic variation;
L111 identifies the incoming linear coefficients by the actual stabilizer
commutator and chooses the Serre-orthogonal complement. Whether these
identifications imply the central Hermitian cancellation needed here
remains the specialization to check, including the real versus complex
stabilizer generator and the actual central comparison map.

**Stronger-looking higher-image formula rejected by hypotheses.**
P. Naumann, *Curvature of higher direct images*, Ann. Fac. Sci. Toulouse
30 (2021), 171--201, [DOI 10.5802/afst.1670](https://afst.centre-mersenne.org/item/10.5802/afst.1670.pdf#page=3),
section 2, pp. 172--174, Theorem 2.1. Read the whole setup and theorem,
including local freeness/base-change and the spectral-resolvent discussion.
It treats a proper holomorphic submersion with a relatively positive
Hermitian line bundle, whose curvature supplies the fibre Kähler forms,
and the specified differential-form higher images. This does not match
End_0(F), its given metric or this jump. No later proof is invoked for
this hypothesis rejection. Reuse the already inspected
[Mourougane--Takayama comparison](2026-10-16-split-harmonic-metric-two-sided-bounds.md):
Nakano semipositivity is not furnished here and its Hodge metric must
not be substituted for the actual chosen metric.

**Reused analytic reduction and extension limitations.** BGS III's
precise reduction is already assessed in that same norm-bound assessment
and implemented/audited in L112. It supplies smooth finite cutoff data,
not a bounded inverse for low nonzero eigenvalues. Reuse
[the prior admissibility comparison](2026-10-15-equality-relative-ext-reflexive-obstruction.md)
and ATTEMPTS/066: no surface extension or semistability theorem is
imported. The Bando--Siu author index was located again, but no theorem
or proof from its image-only pages is claimed read. Those pages are not
essential to the present finite-matrix test; downstream extension would
need its own precise source coverage.

## Discovery record and duplicates

Queries included: `"quotient metric" "curvature" holomorphic subbundle
Chern Demailly`; `"higher direct images" "L2" "jumping" curvature
metric`; `"cohomology jump" "curvature" metric`; `"harmonic metric"
"cohomology" "jumping"`; `"quotient metric" "isolated" curvature
integrable`; `"quotient metric" "curvature" "integrability" holomorphic`;
and `"curvature of higher direct images" "Nakano" Mourougane Takayama`.
Search results about flat-local-system jump loci, Riemannian quotients,
Quillen determinant curvature and unrelated singular Kähler metrics
do not match the requested bundle metric and were not used as theorem
inputs. Naumann was followed to its primary published statement.
Demailly's author-hosted large-PDF URLs timed out; the accessible USP
copy identifies its author and version and contains the needed complete
proof cases. The shorter author-hosted Mahdia notes were located but
are unnecessary once the precise book formulas are accessible.
This bounded search establishes no novelty or exhaustive absence claim.

Locally L112 proves norms only; L111 proves module freeness and the
Serre-plane splitting only. Their explicit exclusions of derivative
conclusions avoid a duplicate lemma. ATTEMPTS/063 requires an actual
metric bridge, ATTEMPTS/066 rejects automatic extension from reflexivity,
and ATTEMPTS/067 tests duality alone. None tests the derivatives of the
now audited actual quotient. No historical stop is removed or made a
global ban. No cross-notebook input was used.

## Exact mathematical scope and decision test

SPECIALIZE authorizes the unchanged TARGET, with REPRODUCTION as the
intended classification. The new work is the actual-family application
of known finite-dimensional Hermitian and Chern formulas. There is no
claim of a new general energy theorem.

First check the actual central comparison product on L111's plane and
complement using its natural residual pairing, L094's coefficient real
structure/stabilizer and L095's quaternionic KS. Do not replace the
symplectic complement by a Hermitian complement without proof, or
normalize the actual metric by a singular gauge. Next differentiate
L112's exact quotient expression, retaining the smooth cross block,
the vanishing column and every inverse denominator. Establish uniform
estimates through two real derivatives in the extending holomorphic
frame and insert them into the cited Chern formula. All approach
directions and the two coordinate axes must be covered. Compare the
result with the fixed smooth real-four-dimensional volume and the
actual endomorphism norm, using only L112's proved norm equivalence.

Continue if this proves a finite integral of squared curvature on one
full punctured ball. A directionwise bound or an upper estimate that
does not imply integrability does not settle the test. Abandon this
specific finite-energy derivation if a genuine nonintegrable actual
leading term is established; if an essential central comparison remains
unproved, report it as an unresolved input rather than as divergence.
An arbitrary bounded metric counterexample would only refute the
norm-only shortcut. Z empty is vacuous. None of these outcomes alone
settles extension, bounded contraction, semistability, |Z|, existence of
F, transport or universal primitive Hodge realization. Matching Mathlib
coverage for the full specialization remains unchecked.
