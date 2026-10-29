# Point-supported quotient Serre form — source scope approved

TARGET: Determine whether L165's actual quotient Serre form is orthogonal across reduced split points and identify its local-duality expression in L164's bracket coordinates.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 556 searched Serre duality/skyscraper/local trace, orthogonal quotient forms, finite evaluation traces and composition of counits; inspected the primary Stacks results below and checked L109/L111/L116/L164/L165/L167, ATTEMPTS/092–094 and relevant ready assessments. No inspected source states this family's actual point-coordinate comparison; no novelty inference is made.
SOURCE_EVIDENCE: Live Stacks HTML inspected 2026-10-25: 48.12.6 (0G81), 48.27.1–4 (0FVU), 57.11.2 (0G23), 48.9.7–8 (0A9X/0B6M), 48.11.4 (0AX2), 48.20.8,11–12 (0AUD/0B6X/0AX4), 48.7 (0AWG), 4.24.9 (0DV0), and 48.15.7 (0BRT); statements and relevant proof/counit cases are detailed below with direct URLs.
COMPARISON: Known derived duality supplies finite-support evaluation, functorial Serre pairings and composite traces. It does not identify L165's actual orthogonal quotient with L109's gamma in L164's coordinates without a specialization. Import the framework; compare those actual arrows with the common trace scalar and local evaluation functionals retained.
GAP: In a separate research turn identify the quotient adjoint against gamma or its inverse, test orthogonality across distinct reduced points, and transport the local-duality expression through theta_z and the fixed h_0 coordinate. Signs, coordinate weights and the actual quartic are not computed by this review.
REASON: New inspection of closed-immersion/finite evaluation traces and composition of counits fills the essential source coverage missing in step 555. A bounded actual-arrow specialization is justified; no general duality reproof, numerical weight, bracket value or exclusion is supplied here.
SCOPE: L116/L165's full conditional family, reduced finite W and actual arrows j,a,r; focus on the formal endpoint s=800,t=48 for L167's quartic application, with no actual F or prescribed point weights assumed.

The main gap remains primitive algebraic realization, including the
existence of F. L167's audited formal counterexample establishes no
actual-map obstruction. The next intermediate target seeks access to
the actual quotient form in the coordinates in which L164 describes
the point bracket. Its plausible downstream use is to express the
actual quartic from actual point-section quadrics with the correct
trace weights, before attempting any minimum-square-count test.
No quartic value, rank bound, diagonal expression or numerical weight
is derived in this proposal.

Essential local inputs are L109,L111,L116,L164,L165,L167, retaining
L071 and L108/L115 through the conditional family. L166 records the
unknown complementary operation and is relevant to the eventual
application, not a proposed vanishing premise. No cross-notebook input.
Preserve identical marked K3 factors, common metric/triple/forms, the
actual connection and locally free rank-two product-polystable F with
integral c_1=0 and ch=2-14e_1-21e_2-tau_D+62P. Retain W with its
full derived dual and the common trace scalar. The existence of F,
the actual section images and all quartic coefficients remain unknown.

For the review, narrowly retrieve L109's actual gamma construction and
L111's relevant local trace normalization, then compare existing primary
finite-length and global Serre duality results with the desired actual
quotient expression. Reuse adequate duality coverage rather than broad
rediscovery. Distinguish a map W^dagger -> W from its inverse, and the
ordinary fibre of W from its derived pullback. Do not replace the
actual orthogonal inverse T by an arbitrary splitting or infer locality
from an arbitrary matrix normal form. Full Mathlib coverage is unchecked.

Continuation test: approve a bounded specialization only if inspected
coverage supports comparing the actual form and local-duality arrows
with all shifts and trace normalizations retained. Import a matching
known result if it already answers the target. If an essential comparison
is missing, name it and keep dependent calculations unapproved. If the
expression is already canonical locally, avoid duplicating a lemma and
record its precise applicability instead. Even a successful expression
need not supply numeric weights or actual section quadrics; state those
remaining inputs explicitly. Persistent source obstruction requires a
different independently testable target, not repeated audit of L167.

ATTEMPTS/092's unknown section-image pairing, /093's scalar-only stop
and /094's cyclicity-only stop remain intact. This is a different
actual-form comparison, not a claim that these failed exclusion
arguments now work. This target was REVIEW_REQUIRED at invocation
start. Step 556 is its separate literature-only approval; it proves
no new local-form formula or mathematical lemma.

## Inspected primary results and applicability

All versions below are live Stacks HTML read on 2026-10-25. Tag IDs
identify the sources independently of chapter renumbering. Import
these general results by citation; no general reproof is warranted.

[Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81)
was read completely, including its cup/evaluation/trace construction
and derived-adjunction explanation. For a proper flat finitely
presented morphism as in 48.12.5, with pseudo-coherent second input
and a pairing inducing the required derived-dual isomorphism, the
pushed-forward cup/trace pairing induces the displayed duality
isomorphism. This supplies the kind of actual adjoint used in L109
and L116, rather than a new choice of pairing.
[Lemma 48.15.7, 0BRT](https://stacks.math.columbia.edu/tag/0BRT),
statement and proof, identifies the relative dualizing complex with
the top relative differential sheaf shifted by the relative dimension
for a smooth proper morphism over a Noetherian base. Here p is
smooth projective of relative dimension two, V is locally free and
trace-self-dual, and the chosen fibre form trivializes its canonical
line. Ordinary local freeness of W is not required.

[Lemma 48.27.1(5),(7), Remarks 48.27.2–3 and Lemma 48.27.4,
0FVU](https://stacks.math.columbia.edu/tag/0FVU) were read with their
proofs where present. On a proper scheme over a field, duality is
functorial and compatible with shifts and triangles; its pairing is
evaluation followed by the global trace. Bounded coherent inputs
give perfect pairings, and for perfect complexes the cup/evaluation
description agrees with this pairing. For a smooth scheme of dimension
d the dualizing complex is the canonical bundle shifted by d. The
smooth projective B and X, fixed canonical forms, C, and coherent
finite-support W meet this scope. This does not itself identify the
notebook's quotient adjoint with a specified local map.

[Lemma 57.11.2, 0G23](https://stacks.math.columbia.edu/tag/0G23),
including its entire finite-length proof, assumes a regular finite-type
scheme over a field and a coherent sheaf supported at a closed point.
The proof uses a normalized local dualizing complex and identifies
the derived dual of a finite-length module with its Matlis dual
shifted by minus the local dimension. It supplies L109's degree-two
finite-length scope, without selecting W_z^dagger=W_z or a numerical
residue normalization. Here O_{B,z} is regular of dimension two;
reduced length-one W comes from L111, not this theorem. Reuse L109's
completed finite-length assessment rather than reprove duality.

[Lemma 48.9.7, 0A9X](https://stacks.math.columbia.edu/tag/0A9X),
statement and uniqueness-of-adjoint proof, realizes the right adjoint
for a pseudo-coherent closed immersion into a quasi-compact,
quasi-separated scheme by derived sheaf Hom on bounded-below
quasi-coherent complexes. Any closed immersion into a Noetherian
scheme has the required pseudo-coherence.
[Example 48.9.8, 0B6M](https://stacks.math.columbia.edu/tag/0B6M),
read completely, specifies its counit: after pushforward it is
induced by O_B -> i_*O_Z under derived Hom. A point trace must
retain this derived map and its shifts, rather than use ordinary
Hom(W,O_B). The reduced finite split-set immersion into B meets
these hypotheses.

[Lemma 48.11.4, 0AX2](https://stacks.math.columbia.edu/tag/0AX2),
statement and proof, gives the derived-Hom realization for a finite
pseudo-coherent morphism with quasi-compact, quasi-separated target.
The proof compares its right adjoints.
[Lemma 48.20.8, 0AUD](https://stacks.math.columbia.edu/tag/0AUD),
statement and proof, and [Example 48.20.11,
0B6X](https://stacks.math.columbia.edu/tag/0B6X), read completely,
identify the normalized dualizing complex under a proper morphism
and its trace arrow. The separated proof case uses composition of
twisted inverse images. Our schemes are separated and finite type
over Spec C, with dualizing complex C[0] on the base field.

[Remark 48.20.12, 0AX4](https://stacks.math.columbia.edu/tag/0AX4),
read completely after its finite-adjoint prerequisites, identifies
the finite-morphism trace as evaluation at 1 on derived Hom, with
dualizing complexes normalized relative to a common Noetherian
dualizing base. This applies to the reduced split set or an individual
point over B and their structure maps over C. It supplies a finite
duality trace, not a preferred generator of W(z). Chapter 49's flat
finite algebra trace is not substituted: a surface's closed point
is not flat over that surface.

[Section 48.7, 0AWG](https://stacks.math.columbia.edu/tag/0AWG),
opening definition and Example 48.7.3, were read: the trace is the
counit, and the affine expression is induced by the ring-unit map
under derived Hom. The base-change proof of 48.7.1 was also read;
no ordinary middle-base-change assertion is imported from it.
[Lemma 4.24.9, 0DV0](https://stacks.math.columbia.edu/tag/0DV0),
including its proof and equation 4.24.9.1, states composition of
adjoints and counits. Together with the finite-trace description it
covers comparison of local evaluation followed by the base trace
with the composite trace. This supplies coherent normalization;
independent pointwise rescalings cannot be silently introduced.

## Search, reuse and comparison with failures

Queries used included `"Serre duality" "skyscraper" "trace" pairing
local`, `"orthogonal" "quotient" "Serre" "duality" point supported`,
`"Serre pairing" "local duality" "skyscraper" surface`, and targeted
Stacks searches for finite evaluation, disjoint supports, trace
composition and composition of counits. Unrelated curve examples,
secondary pages and snippets were not treated as theorem coverage.
The disjoint-support Ext search supplied no distinct matching source.
First determine whether the actual quotient adjoint is a sheaf map,
then use its stalks and finite-support evaluation; do not infer
locality from diagonalizing a global matrix. These bounded searches
do not establish novelty.

Reused the ready finite-length assessment
`2026-10-15-equality-local-duality-defect-sequence.md`, actual-lift
assessment `2026-10-25-global-point-quotient-isotropic-lift.md`, and
point-projection assessment
`2026-10-25-adjoint-point-obstruction-projection.md` (all here).
Searched the L164/L165/L167 audit assessments for overlap. They
cover their existing statements, not this new coordinate comparison.
Read the relevant proof passages: L109's gamma through alpha^{-1}
and dual truncation; L111's actual paired minimal complex and full
Koszul summand; L116's global j,a,r; L164's theta_z, derived middle
inclusion and h_0 coordinate; L165's normalized adjoint and actual
orthogonal lift; and L167's definition of Q_U. These passages do
not already state the requested comparison as a separate result.

ATTEMPTS/092–094 were read completely. Section-image isotropy,
scalar-only exclusion and cyclicity-only vanishing remain parked
with their stated scope. The proposed comparison neither assumes
the complementary operation vanishes nor reopens those exclusions.

## Approved specialization and stopping test

Keep TARGET unchanged. In one subsequent mathematical attempt,
compare the quotient adjoint with actual gamma and its inverse,
retaining alpha:C[2] -> DC and DW=W^dagger[-2]. Check L165's
orthogonal lift against this comparison before asserting pointwise
orthogonality. Use finite-support evaluation and L164's top derived
base change to express the form in the fixed h_0 bracket coordinates.
Keep all local evaluation functionals, coordinate weights and the
common trace scalar explicit. Determine all signs and which direction
of gamma enters; the form is complex bilinear, not Hermitian. This
family-specific comparison is still to be proved.

No general duality theorem needs reproof. The specialization is
necessary because abstract diagonalization would lose the point
coordinates relevant to L167. If an essential new hypothesis or
theorem outside this coverage appears, stop that dependent derivation
and record the precise gap. An explicit analytic residue/Jacobian
coefficient beyond the canonical evaluation functional would require
its own normalization comparison; 0BRT does not silently supply it.
No such numerical coefficient is needed for the proposed canonical
local-duality expression with weights retained symbolically.

Continue only if the actual arrows give an expression usable on
L164's actual section quadrics. Record a failed comparison or a
missing independent datum honestly. Even success leaves F existence,
actual section values, the complementary operation and the quartic's
minimum square count open. No cardinality exclusion follows here.
Mathlib: full matching coverage and local-duality normalization are
unchecked; no absence is asserted. No lemma or mathematical script
was created or modified in this literature-only review.
