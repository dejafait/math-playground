# Equality normal summand — global Chern test source assessment

TARGET: Test whether L114's smooth ASD extension preserves L108's normal splitting and forces |Z|<=800 via L111's Chern budget.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L108's actual projector/normal-metric passages, L111's bundle and budget, audited L114, the ready removal and real-Kahler inequality assessments, and ATTEMPTS/063/066/067; targeted HE/Chern and exact K3 normal-bound searches are recorded below.
SOURCE_EVIDENCE: Perego arXiv:1910.01867v1, Theorem 1.1 p. 4, Lemmas 2.40/2.42 and section 2.7 pp. 28--30, Theorems 4.19/4.21 and Definition 4.20 pp. 63--65, Corollary 6.42 p. 118; reuse the prior complete Theorem 4.19 proof assessment and Verbitsky's surface orthogonality coverage from the removal assessment.
COMPARISON: Known real-Kahler HE and Chern tools cover arbitrary rank, including rank 48, without an integral polarization; the remaining task is the actual global-projector and connection specialization, not a new general stability theorem. No matching published numerical 800 bound was identified, and no novelty inference follows.
GAP: The separate research turn must verify global parallelness and orthogonality of the already extended projector for L114's specific connection, identify the restricted Chern curvature on the actual N, and apply the cited inequality with L111's normalized budget. This review proves none of those conclusions.
REASON: Essential source coverage is ready for this bounded specialization; reuse audited removal rather than reopen blocked singular-metric or reflexivity shortcuts. No general theorem reproof is justified.
SCOPE: Exactly TARGET; conditional L071 equality F with ch_2=-14e_1-21e_2-tau_D, integral c_1=0 and the original common metrics; L108, L111, audited L114, and L100/L113/L095/L094 through these inputs; finite Z possibly empty. No F, global projector parallelness, normal semistability or cardinality bound is assumed.
LITERATURE_REASON: The startup gate requires coverage of the new global application beyond audited removal; the essential new comparison is real-Kahler HE/Chern scope and restriction to the actual normal summand.

## Relevance and bounded test

The main gap remains algebraic realization of arbitrary primitive rational
Hodge classes, already unresolved for general fourfolds. The intermediate
threshold is a conditional upper bound |Z|<=800 for this equality-kernel
recipe. A later bound could constrain that recipe together with independent
geometric information about split fibres. No lower bound on |Z|, existence
of F, reconstruction or transverse transport is supplied. A cardinality
bound alone would neither exclude F nor resolve the Hodge conjecture.

Continue only if the global algebraic projector is compatible with the
specific smooth connection on M=E and the restricted connection satisfies
the inspected hypotheses at the unchanged real metric. Failure of either
comparison stops this application and must be recorded explicitly. The
bound must use the corrected budget, including its minus point-defect
sign. Z empty remains within scope. This is source approval, not the
mathematical application or approval of any newly derived result.

## Inspected standard inputs

Arvid Perego, *Kobayashi-Hitchin corrispondence for twisted vector
bundles*, [arXiv:1910.01867v1, 4 October 2019](https://arxiv.org/pdf/1910.01867v1):
Theorem 4.21, p. 65, gives polystability from a Hermite--Einstein metric
on a compact Kahler manifold. Theorem 4.19, pp. 63--65, includes arbitrary
saturated subsheaves and the equality splitting case. Reuse the complete
proof reading in the [ordinary-connection assessment](2026-10-11-nonspin-normalized-tensor-realization.md);
this turn rechecked its statement and final extension/induction passage.
Definition 4.20 includes semistability in polystability. Corollary 6.42,
p. 118, states for a semistable rank-r bundle on a compact Kahler n-fold:

\[
 \int_X ((r-1)c_1^2-2r c_2)\wedge\sigma_g^{n-2}\le0.
\]

Read that entire statement and citation paragraph; its proof refers to
Kobayashi IV Theorems 4.7/5.7 and Luebke--Teleman 2.2.3/2.2.4.
Lemma 2.40 identifies the induced subbundle Chern connection;
Lemma 2.42 treats invariant subbundles. Section 2.7, pp. 29--30,
gives the curvature blocks with second fundamental forms retained.
These are metric statements, with no rationality restriction on the
Kahler form. Set the twist to one and the auxiliary B-field to zero
for ordinary bundles. The numerical specialization is deferred.

Reuse the [ready removal assessment](2026-10-16-split-harmonic-connection-removability.md)
and its surface orthogonality input: Verbitsky, *Hyperholomorphic
bundles*, alg-geom/9307008v1, section 2, Lemma 2.1 and Theorems 2.3--2.4;
*Deformations of trianalytic subvarieties of hyperkahler manifolds*,
alg-geom/9610010v1, section 2.2, Proposition 2.13/Lemma 2.14.
No new removal theorem is required. Audited L114 already supplies the
smooth positive metric and ASD Chern connection on the specific M,
not merely an abstract gauge extension. Preserve its original base
orientation and Kahler metric in the subsequent restriction check.

## Actual-family specialization obligations

L108 constructs P=i r as a global holomorphic idempotent of E, with
kernel the actual rank-48 normal bundle N and image i(T_B). Its
stable-open construction identifies that splitting with the parallel
metric splitting from L100. L111 identifies M with E canonically and
gives integral c_1(N)=0 and c_2(N)=(800-|Z|)eta, with eta normalized by \int_B eta=1.
These are inputs to the proposed application, not new results here.

The later proof must compare this very P with the extended smooth
metric and Chern connection, using their agreement on U. In particular,
it must check smoothness of the induced End(M) connection applied to P
and extension of the orthogonality identity. An abstract new parallel
splitting or a changed Hermitian metric would not identify the required N.
This is a finite-dimensional smooth bundle compatibility check using
already extended objects; it calls for no independent singular PDE
or previously uncovered extension theorem.

Next identify the restricted connection as the Chern connection of the
induced positive metric on N and retain the second fundamental forms
until their vanishing is justified. Check ASD/zero Kahler contraction
for this connection at the original metric before invoking the HE result.
Strict stability or irreducibility is unnecessary and must not be assumed.
The final application must retain complex dimension two, positive rank,
L111's integral first-class vanishing and normalization of eta when
comparing the inequality to the requested threshold. This assessment
allows that application only; no equality-case or stronger exclusion
claim is preapproved.

## Duplicates, failures and source-access record

The scoped comparisons read L108's hypotheses/conclusion, projector,
extension and metric audit passages; L111's hypotheses/conclusion;
L114's hypotheses, conclusion and imported scope; the supplied overview,
DAG and next assessment; history/326 and history/328; ATTEMPTS/063/066/067.
The prior removal assessment explicitly stopped before this global
application. No duplicate completed normal-bound proof was found in these
specific records. The old arbitrary-rank inequality assessment
`2026-10-04-fixed-lower-chern-stability-test.md` supplies reusable real-metric
source scope but concerns a different bundle and base dimension.

ATTEMPTS/066 rejected reflexivity as metric extension. L114 supplies the
materially different actual smooth extension input. ATTEMPTS/067 rejected
duality alone as a numerical bound; this target uses an independent
curvature inequality and retains the corrected defect budget. Neither
failure is erased. ATTEMPTS/063's singular-coarse metric/degree bridge is
not invoked, and no local degree or branch separation is proposed.

Queries this turn: `Kobayashi differential geometry complex vector bundles
pdf Luebke inequality Hermitian Einstein 4.4`; `parallel holomorphic
endomorphism Hermitian Einstein bundle Kobayashi proposition`;
`"K3" "normal bundle" "800" instanton`; `"parallel" "projector" "smooth"
"connection" "dense"`; `"K3" "totally geodesic" "Chern" "normal bundle"`.
The exact-bound queries yielded no usable matching theorem; several
results were irrelevant and were not used as evidence. No originality
claim rests on these searches.

The MSJ-hosted 2013 retypesetting of Kobayashi's 1987 book opened at its
front matter, but targeted text reads failed and screenshot requests
returned no inspectable page content. A direct shell retrieval failed
DNS resolution. Its theorem bodies are not claimed read this turn.
Perego's inspected statements and reusable complete proof coverage suffice;
these nonessential access failures are not an essential source blocker.
Perego's HTML endpoint was unavailable; the versioned PDF was readable.
Published-page numbering is not inferred from the preprint. No additional
Bando--Siu search, cross-notebook input or mathematical script was used.

## Mathlib and classification

Full matching Mathlib coverage for this actual normal-summand application
has not been checked. Unknown availability is not absence. This review
approves a REPRODUCTION/specialization of named known tools, with no
claim of new mathematics or a completed |Z| bound. Canonical proofs remain
in the existing lemma files; no lemma, DAG or argument edit is made.
