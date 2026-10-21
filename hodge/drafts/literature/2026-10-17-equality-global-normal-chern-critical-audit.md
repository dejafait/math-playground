# Global normal-summand Chern bound — audit source assessment

TARGET: Critically audit L115's global projector compatibility, induced ASD normal connection and conditional bound |Z|<=800.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-application search and theorem comparison in 2026-10-17-equality-normal-summand-global-chern-bound.md; read full L115, targeted L108 projector/audit passages, L111 hypotheses/conclusion, L114 same-bundle audit passages, history/330 and ATTEMPTS/063/066/067; reopened the versioned primary theorem statements and relevant connection formulas.
SOURCE_EVIDENCE: Perego arXiv:1910.01867v1, section 2.7, Lemmas 2.40/2.42 and Gauss-Codazzi formulas pp. 28--30; Definition 4.20 and Theorem 4.21 p. 65; Corollary 6.42 with its citation paragraph p. 118; reuse complete Theorem 4.19 proof coverage in 2026-10-11-nonspin-normalized-tensor-realization.md and the separate audited L114 removal scope.
COMPARISON: The inspected known tools cover ordinary positive Hermitian bundles of arbitrary rank at a real Kahler metric; the new audit target is their compatibility with the specific global objects, not a stronger general theorem or a second derivation of the bound.
GAP: Independently check same-bundle agreement, smooth dense-open tensor identities, both second fundamental forms, actual restricted Chern curvature and the signed rank-48 specialization; this source review does not verify those mathematical bridges.
REASON: Essential source coverage is ready for the exact bounded critical audit, conditional on L108/L111/audited L114; no new extension theorem, equality-case theorem or general reproof is needed.
SCOPE: Exactly TARGET, retaining hypothetical L071 equality F with full negative tensor ch_2=-14e_1-21e_2-tau_D and original common metrics; direct inputs L108/L111/L114, with L100/L113/L095/L094 through them; Z finite and possibly empty.
LITERATURE_REASON: Startup REVIEW_REQUIRED gate calls for separate approval of the newly proposed independent audit; reuse adequate application coverage and inspect only the audit-specific compatibility scope.

## Gap, intermediate target and bounded use

The main gap remains algebraic realization of arbitrary primitive rational
(2,2)-classes, already unresolved on arbitrary fourfolds. The intermediate
target is an independent audit of L115's conditional upper bound, not
another theorem or a stronger bound. A reliable bound could later constrain
this equality-kernel recipe if combined with independent geometric control
of split fibres. No contradictory lower bound, F existence or exclusion,
separation, reconstruction or transverse transport is available here.

Continue with one proof audit if the cited hypotheses can be checked for
the actual projector and connection. Preserve L115 only if all its bridges
survive; otherwise repair or qualify its canonical proof. Missing identity
of bundles/connections, a surviving second fundamental term, or a wrong
Chern sign is a discriminating failure. Do not replace these tests by a
fresh metric choice, an abstract gauge extension or strict normal stability.

## Primary source scope and reuse

Arvid Perego, *Kobayashi-Hitchin corrispondence for twisted vector bundles*,
[1910.01867v1, 4 October 2019](https://arxiv.org/pdf/1910.01867v1),
section 2.7, pp. 28--30: Lemma 2.40 identifies the projected subbundle
Chern connection; Lemma 2.42 treats invariant subbundles. The full
Gauss-Codazzi blocks retain second fundamental terms. Definition 4.20
and Theorem 4.21, p. 65, give HE implying polystability and semistability.
Corollary 6.42, p. 118, states

\[
\int_X ((r-1)c_1^2-2r c_2)\wedge\sigma_g^{n-2}\leq0
\]

for a semistable rank-r bundle; its citation paragraph refers to Kobayashi
IV, Theorems 4.7/5.7 and Luebke--Teleman 2.2.3/2.2.4. These statements
allow a compact Kahler base, arbitrary rank and a real Kahler metric.
Use trivial twist and zero B-field for ordinary bundles. The needed
Theorem 4.19 saturated-subsheaf and splitting proof cases have ready
complete coverage in the [ordinary-connection assessment](2026-10-11-nonspin-normalized-tensor-realization.md).
No reproof is proposed.

The versioned PDF was accessible. Reopened the complete relevant statements,
Lemma 2.40's proof, invariant-subbundle paragraph, full curvature blocks
and the HE proof's final extension/induction passage. Original books cited
there were not newly inspected; no uninspected book statement is needed
beyond this accessible source and ready coverage. Reuse the original
application's exact-bound and terminology searches; no target expansion
or new lead warrants repeating them. No novelty conclusion follows.

## Audit obligations and inherited qualifications

L115 is the already completed application, so the audit is not a duplicate
construction. L108's projector and its stable-open metric identification
are canonical input claims. Its relevant proof and separate audit passages
were inspected to locate the identification that must be tested. L111's
canonical M=E, integral c_1(N)=0 and normalized budget remain explicit
inputs, rather than new calculations in this review.

L114's separate audit identifies the entire rank-fifty harmonic bundle
with the tangent pullback, cancels coefficient-line scalars in End_0,
and fixes one constant metric normalization before comparing Chern
connections. Its final Hartogs argument treats both inverse matrices
and transports the smooth positive extension to the specific M. These
are precisely the inherited same-bundle assertions the new audit must
use; it need not reopen Parker removal or all ancestor proofs.

The future audit should inspect the existing smooth End(M) derivative
and Hermitian adjoint identities on all B, their claimed vanishing on U,
and the use of density. It should then check restriction to the actual
holomorphic kernel N, including both second fundamental forms, original
complex orientation, ASD/HE compatibility and the stated numerical
inequality with n=2, rank 48 and normalized point class. These are review
questions, not newly established conclusions here. The attained bound
must remain conditional and allow Z empty; no equality-case enhancement
is covered.

## Failures, classification and Mathlib

ATTEMPTS/066 rules out reflexivity as automatic chosen-metric extension;
this audit instead takes audited L114's actual smooth extension as input.
ATTEMPTS/067 rules out a duality-only defect bound; L115 uses an independent
curvature inequality. ATTEMPTS/063's singular-coarse metric/degree bridge
is unused. None of these historical stops is erased or treated as a
global ban. The scoped record contains the completed L115 application
and a pending audit, not a completed independent L115 audit.

This is LITERATURE / EXPLORATION / REPRODUCTION: source scope is ready,
but no mathematical bridge is independently verified and no result beyond
the checked sources is claimed. Full matching Mathlib coverage is not
checked; unknown availability is not absence. No lemma, mathematical
script, DAG or argument overview is changed. The next turn defaults to
the exact proof audit under this saved SPECIALIZE assessment.
