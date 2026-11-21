# Short-time collision-current scope — nomination963, source review964

TARGET: Assess the complete localized Stokes identity under C466s with the added short-time condition M_1 T_0<min{R-a,L-b}, including exclusion of prior outer exits and vanishing collision/initial-axis cutoff flux.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Review964 searched the exact/stronger short-time singular-flow, zero-extension and collision-current terminology listed below; reused review960 for extension/transport coverage and searched the named local current records for duplicates and buffer restrictions. No matching short-time theorem was identified; this is bounded coverage, not novelty certification.
SOURCE_EVIDENCE: Reuse assessment959/review960: HP1970 Theorem2.1/Lemma2.2 and Theorem5.2, TNV1706.03822v2 Section2.2/AppendixB and WKM2008.10321v2. Newly inspected WKM Section3.1 Proposition5 with its proof, printed p9, all-k scope https://arxiv.org/pdf/2008.10321v2; Teschl author-hosted preliminary ODE text, Lemma2.14/Corollary2.15 printed p52 and Theorem6.1/proof pp189–190 https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf. Exact applicability and access qualifications below.
COMPARISON: Smooth-survivor ODE/compound machinery and weak cutoff proofs are available. Neither these sources nor C466s supplies the restricted complete-current identity. The new buffer premise must be tested against actual outer hits; complete coefficient integrability and zero collision/initial-axis flux still require a mathematical specialization.
GAP: Prove outer-hit exclusion from the stated quantitative restriction, then complete-form L1_loc and zero weak cutoff error at collisions and r=0, or exhibit an admissible defect. No regular lifetime, hitting surface, boundary trace or post-exit map is assumed.
REASON: Essential coverage is sufficient for one bounded established-tool proof/obstruction attempt, with no direct import and no persistent source blocker. This literature-only review derives none of the missing estimates and leaves stop961 intact.
LITERATURE_REASON: The added M_1 T_0 buffer hypothesis changes the failed all-stopped-events scope; essential comparison of outer-hit exclusion and complete-current flux was REVIEW_REQUIRED at invocation. Existing removability coverage is reused rather than searched again.
SCOPE: Exact nomination963 hypotheses and target; changed finite time/buffer restriction only. Arbitrary coupled holomorphic H, unit raw physical time, first lifetime, complete beta/gamma and coefficientwise zero extension remain. EXPLORE covers investigating the missing specialization, not its truth.

## Exact proposed question and its relevance

Retain all C466s hypotheses and notation, and require T_0>0 with
M_1 T_0<min{R-a,L-b}. On Q=(0,T_0) times I, use the same
survivor-only map Psi and complete forms as C466t:
Omega=q^2 exp(-H) dq wedge dz,
beta_chi=Psi^*(chi Omega), gamma_chi=Psi^*(dchi wedge Omega).
For every smooth compactly supported chi on B, the proposed conclusion
is coefficientwise L1_loc of both zero extensions and
d bar(beta_chi)=bar(gamma_chi) on Q. It is a question, not a result.

The next review must first assess whether the quantitative restriction
actually excludes earlier outer hits for the whole initial rectangle,
and whether this yields an independently testable target outside
stop961's mechanism. It must retain collision and initial-axis tests,
arbitrary coupled H, the complete time minors and the inhomogeneous
gamma term. Neither a regular hitting surface nor a boundary trace
may be added implicitly. Review the exact primary assumptions already
recorded in assessment959 before deciding whether new reading is
essential; do not repeat general browsing solely for this nomination.

A proved identity in this scope could pay a local collisional boundary
step. Extension to longer times, restarting from a deformed initial
surface, global signed integration, a positivity mechanism and
actual-Xi realization would remain independent gaps. C466s's modulus
bound and C466t's obstruction do not supply them. This is development
of a restricted transport question, not a creative central sign
mechanism. Its value must be weighed against that missing link.

The continuation test is a source comparison precise enough to approve
one bounded complete-form/cutoff attempt, or a source/local obstruction
that parks this variant. Any later mathematical attempt must either
pay all the stated limits or exhibit an admissible nonzero defect;
an absolute density estimate alone does not pass. Preserve working961's
unproved mixed-minor idea without treating it as a theorem, and preserve
stops927/932/941/947/948/959/961. Full matching Mathlib coverage is
unchecked. No cross-notebook input, same-turn approval or mathematical
derivation of this proposed variant is supplied by nomination963.

## Completed source comparison964 — 14 November 2026

The preceding question is retained verbatim as the object of review.
Statements above about coverage being unassessed describe nomination963;
this section and the current fields record the subsequent source review.
No outer-exclusion inequality, mixed-minor estimate, cutoff limit,
counterexample or lemma has been derived in this literature turn.

### Search and local overlap

New queries were `"holomorphic gradient flow" "finite time" "boundary"
singularities Stokes`, `"logarithmic" "gradient flow" "removable"
differential forms`, `"short time" "Stokes" "Lefschetz" zeros`,
`"Lefschetz" "collision" "Stokes" flow boundary zeros`, and
`"gradient flow" "zero extension" "logarithmic"`. A source-location
query was `"k-Contraction: Theory and Applications" "Proposition 5"`.
The new searches supplied no exact theorem for this restriction.
Saddle-collision/Stokes-phenomenon hits were not treated as results
about a trajectory hitting the divisor. Search failure proves no
novelty or absence theorem; unrelated hits were not pursued.

Read assessment959/review960 and assessment960 in full, C466s including
its audit, C466t's hypotheses/conclusion and explicit earlier-hit case,
stop961, coverage962's relevant comparison and history963. Searched
only the named current assessments, working records, stop and local
foundations for short-time/buffer/outer-exclusion passages. Nomination963
was the only proposed buffer theorem in those records. Working961's
velocity/mixed-minor suggestion remains unfinished, not a proved input.
Earlier phase, independence, marginal-sign and jet stops927/932/941/
947/948/959 retain their assessed scopes from review960; no new audit
of those older proofs was needed. C466t explicitly leaves collision-only
and no-prior-escape variants open. This changed quantitative target
therefore needs its own test, while the universal claim stays stopped.

### Primary hypotheses and scope

**ODE continuation and local flow.** Gerald Teschl, *Ordinary
Differential Equations and Dynamical Systems*, author-hosted
[preliminary version](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
preface April2012, accessed 14 November2026, Lemma2.14 and Corollary2.15
p52, Theorem6.1 pp189–190, including proofs: continuation requires
an interior endpoint or suitable compact recurrence in the open ODE
domain. The smooth autonomous flow has an open maximal domain and
its group law holds only where defined. For C466s the relevant
real domain excludes q=0; these statements give no continuation
through a collision or a first outer exit. Theorem2.5 p40, also
inspected, uses a bound on the full vector field in its existence
ball. M_1 bounds the regular gradient of H, not the singular raw
velocity; that theorem does not directly import the proposed buffer
conclusion. A later attempt must justify the radial comparison and
first-hit exclusion rather than cite a global small-velocity bound.

**Complete volumes.** Wu–Kanevskiy–Margaliot, *k-Contraction:
Theory and Applications*, [arXiv:2008.10321v2](https://arxiv.org/pdf/2008.10321v2),
27 September2021, Section3.1, Proposition5 and its proof, printed p9,
were inspected with (29) and its continuity premise on p8. The
compound norm upper bound is exp of the integral of the matrix
measure of A^[k], for every integer 1<=k<=n. Its proof uses the
compound evolution and Coppel's inequality; negative uniform measure
is required for the contraction consequence, not this upper bound.
Use is available on compact surviving intervals of the real
variational system. It does not assert uniform singular estimates,
weighted cancellation, or any zero-extension theorem. The later
attempt must justify velocity/parameter vectors and whichever
exterior degrees its complete beta, gamma and cutoff errors require;
a bound for one spatial minor cannot substitute for those tasks.
The nonlinear global convex-state-space hypotheses are not imported.

**Weak extension and raw collisions.** Reuse the exact primary
hypotheses/proof cases recorded in
[review960](2026-11-14-collision-current-stokes-source-959.md):
Harvey–Polking, Acta Math.125(1970),39–56, Theorem2.1/Lemma2.2
pp40–41 and Theorem5.2 pp48–49. Their neighborhood-mass or weak
trace premises remain unpaid. For this inhomogeneous equation an
operator/unknown formulation needs justification before invoking a
homogeneous removability statement. No smallness of the preimage
stopping set follows from the dimension of the ambient divisor.
The rough-chain/worldvolume sources assessed there still need
unprovided regularity; no further reading of them is essential for
the selected direct cutoff method.

TNV, *Gradient flows without blow-up for Lefschetz thimbles*,
[arXiv:1706.03822v2](https://arxiv.org/html/1706.03822v2#S2.SS2),
Section2.2, (2.21)–(2.23) and footnotes1–2, was spot-checked against
review960: its raw zero-hit example and fixed-time weighted-Jacobian
discussion do not supply a complete coupled weak-current identity.
Its complete modified flow changes the metric. Neither argument
imports the proposed result. AppendixB variational coverage is reused.

New primary extracted text was readable, including the cited WKM
proof and Teschl continuation/local-flow proofs. Screenshot requests
returned references without visible page images; no visual verification
is claimed. A direct shell PDF download failed at DNS resolution and
was not retried; web-extracted primary text supplied the needed
passages. There is no essential access blocker. Full matching Mathlib
coverage remains unchecked; no theorem absence is inferred.

### Decision and one continuation

EXPLORE is warranted for one bounded attempt under the exact stated
restriction; no theorem or new estimate is approved as established.
First test whether the restriction excludes every prior outer hit
for all the initial rectangle, including limiting simultaneous events
and M_1=0. Only if that succeeds should a proof seek complete-form
integrability and zero weak survivor-cutoff flux. Retain the gamma
term, arbitrary compact tests and r=0; no regular lifetime surface
or auxiliary flow after exit may be assumed. An admissible nonzero
defect or nonintegrable coefficient refutes the restricted identity;
failure of a chosen bound alone only stops that method.

The exact proof/obstruction task is nominated in
[assessment964](2026-11-14-short-time-collision-current-attempt-964.md)
for separate next-turn approval. It uses established ODE, compound
and cutoff tools, so its purpose is proof_attempt/development,
not creative. No known result is being reproved for novelty: the
uncovered part is their singular stopped-flow applicability and
limit passage. Do not reproduce C466s's already audited spatial
bound as a substitute.

A successful identity would pay one local signed boundary step.
The main gap is still L030-L032/C032a actual-Xi all-degree algebraic-
square positivity. No paid implication from this identity to that
sign is known; original metric, intersecting divisors, long times,
restarted initial surfaces, global signed integration, other endpoints
and Xi realization remain independent. That missing implication is
the blocker to a justified central creative nomination. No RH
candidate, cross-notebook input or exploration-counter reset is claimed.

Outcome EXPLORATION records new bounded source comparison, not
progress beyond the sources or a mathematical theorem. No lemmas,
mathematical scripts, PROOF, DAG or stop evidence were modified.
