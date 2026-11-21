# Consecutive actual Hermite displacement — completed review2052

TARGET: Review whether the canonical Newton-moment displacement D_N=H_(N+1)-diag(H_N,0) of C029m's Jensen-weighted family admits a coefficient-explicit rank-two signed update, starting with a fixed N=6-to-7 feasibility test.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for consecutive Newton-sum Hermite matrices, Jensen/Pollaczek rank updates, changing-polynomial Hankel differences and displacement rank; scoped November20/21 tilted-family reviews/stops distinguish C029q's embedding. No adequate exact-family update theorem identified; this is not novelty evidence. Queries and primary inspections below.
SOURCE_EVIDENCE: Reuse review2019's inspected Wu–Wu–Yang Propositions3.7–3.11 and Lemma4.3/Proposition4.4, Heinig–Rost Section4.1(2)–(3)/Corollary4.4, and Kuznetsov pp563/566/568–569; reuse review2001/comparison2012 for Newton identities and Hermite interpretation. Newly inspect Beckermann–Townsend arXiv:1609.09494v1, (1.1), Theorem2.1/proof pp4–5 and Section5.2/Corollary5.4 pp17–18; Holtz–Tyaglov arXiv:0912.4703v3 Section4.1(4.1)–(4.4), pp66–67, including repeated-root logarithmic derivative. Direct sources below.
COMPARISON: Standard displacement rank bounds rank(AX-XB); it does not identify H_(N+1)-diag(H_N,0). Common-Hankel extension requires one moment sequence, absent here. C029q's affine-quotient derivative-Bezoutian residual is a different embedding; separate congruence representations do not identify the two residuals. The nominated fixed rank test is meaningful and nonduplicate within the local records checked, but unsupported as a uniform theorem.
GAP: No rank bound, signed update, invariant negative direction, degree uniformity or eventual index estimate has been established. Even rank<=2 at one pair leaves independent sign restrictions and all eventual hypotheses unpaid. Essential source coverage for the bounded coefficient/minor test is now adequate; the rank hypothesis itself remains an exploratory ansatz.
REASON: Do not import fixed-size displacement or positive-measure results as actual-family propagation. Retain only the single fixed N=6-to-7 rank discriminator, with no root fitting, embedding change or degree sweep. The separate calculation assessment2052 is newly written and requires next-turn approval; this turn performs no mathematics beyond source comparison.
LITERATURE_REASON: Changed target from the ready fixed theta=0 audit to an uncovered cross-degree root-moment difference; essential rank-update applicability is unassessed. Reuse the cited coverage rather than repeat its source extraction.

SCOPE: Literature-only review of the nominated actual-family difference; no new lemma, rank calculation, mathematical script or source reproof. Mathlib matching coverage not checked. No cross-notebook input.

## Completed comparison2052

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is a small signed description of
changing root-moment forms, potentially relevant to C029m's eventual
negative-index ceiling. Only rank feasibility is ready for testing;
no independent sign control has emerged.

### Primary scope and applicability

B. Beckermann and A. Townsend, *On the Singular Values of Matrices
with Displacement Structure*, [arXiv:1609.09494v1](https://arxiv.org/pdf/1609.09494v1),
29 September 2016: read (1.1), Theorem2.1 and complete proof, printed
pp4–5; Section5.2 through Corollary5.4 and its factorization argument,
pp17–18. Displacement rank concerns AX-XB. Theorem2.1 assumes normal
A,B, their spectra contained in E,F, and a width-nu factorization of
AX-XB; it bounds singular values using Zolotarev numbers. Its proof
builds low-rank polynomial-transform differences and rational
approximants. It does not compare independent changing-degree forms.
Section5.2 explicitly separates Hankel displacement structure from
numerical low rank. Corollary5.4 requires real positive definite
Hankel matrices and concludes approximation bounds, not exact rank
two. C029p already gives an indefinite H_6, so that positive definite
specialization is unavailable. No singular moment-representation
assertion from Lemma5.3 is imported or audited here. Our inference:
these results provide no rank or sign certificate for D_6.

O. Holtz and M. Tyaglov, *Structured matrices, continued fractions,
and root localization of polynomials*,
[arXiv:0912.4703v3](https://arxiv.org/pdf/0912.4703v3), 9 March 2011,
Section4.1, (4.1)–(4.4), printed pp66–67: read the real degree-n
polynomial hypotheses, logarithmic derivative, factorization with
positive integer root multiplicities, and Laurent expansion at
infinity. These identify the Newton sums of one polynomial, counting
its algebraic root multiplicities. The subsequent infinite-Hankel
rank statement counts its distinct roots. It supplies no comparison
of two polynomials' root moments and no rank-two cross-degree update.
We use this as terminology/applicability evidence only; no new
rational-difference theorem or singular inertia algorithm is imported.

Reuse the full primary inspections in review2019, rather than repeat
them: Wu–Wu–Yang's factor/translation/dilation hypotheses and Heinig–Rost's
common-sequence, inverse/pivot and signed-weight qualifications remain
unchanged. Reuse review2001 and comparison2012 for Kuznetsov's exact
coefficients, Newton identities (Coste Exercise1.13), Hermite conventions
and rational certification. Kuznetsov's numerical degrees6–20 observation
does not supply the proposed update. The optional NSF mirror returned
502; the primary arXiv source was accessible, so this is not a source
blocker. All new online inspections: 21 November 2026.

### Searches, duplicates and preserved failures

Queries: `"Newton sums" "consecutive" "Hermite" matrix rank`;
`"Jensen polynomials" "Hermite matrix" rank`;
`Hankel matrices Newton sums polynomial sequences low rank difference degree displacement`;
`"Newton sums" "Hankel" "rank" "Tyaglov"`;
`"Hankel" "displacement rank" "Beckermann" "Townsend"`;
`"Kuznetsov" "Jensen" "rank" Pollaczek`;
`"Newton sums" "Hankel" "Tyaglov" structured matrices`;
`"Kuznetsov" "Meixner" "Newton" matrix rank`.
Search snippets and third-party summaries were discovery leads only.
Mourrain's multivariate structured-rank work and the measure-modification
preprint arXiv:2412.17663 remain unread leads, not supporting theorems;
neither is essential to a direct finite minor certificate.

Read C029m's full exact-family/conditional argument; C029l's hypotheses
and imported root-count convention; C029n's constant-enclosure proof;
C029p's inertia/congruence scope; C029q's complete coefficient, degree,
quotient and kernel construction through the witness setup. C029q
certifies degrees6/7 for U_N=T_N/S with S>0 and its own negative PSD
residual. Its embedding multiplies descending Pollaczek coordinates
by the affine quotient. The present proposal instead fixes monomial
root-moment coordinates and zero-padding before signatures. No
inter-degree congruence identifying these residuals is established.
C029p supplies H_6's inertia, not H_6's entries in those coordinates.
C029w is an undamped contrast and is not substituted for this input.

Scoped searches in the November20 tilted-family reviews and November21
Hermite nominations, plus tilted/Jensen/full-bulk stops, found no
completed zero-padding rank test. Read stops2042/2044/2047: unsigned
local splitting lacks a signed input; the endpoint-only quadratic
defect has bulk coefficients; an unspecified full-support metric adds
no coefficient rule or signature estimate. Preserve them and C029q/r/v;
none proves the new rank hypothesis false or forbids a distinct test.

### Decision and continuation

EXPLORE only the unchanged coefficient-defined finite pair. One
certified nonzero 3-by-3 minor suffices to reject rank<=2 at this
pair by the standard determinantal rank criterion. This is an approved
test design, not a computed minor or a newly proved lemma. A minor
enclosure containing zero is inconclusive, including if the exact
minor vanishes; it does not certify rank<=2. No precision/degree
campaign or altered embedding follows. Even a separately proved
rank-two result would leave relative signs, exceptional/singular
cases, initialization and eventual uniformity open.

The exact bounded continuation is in
`drafts/literature/2026-11-21-consecutive-hermite-rank-test-2052.md`.
It is a newly ready nomination for separate next-turn approval. The
source review is EXPLORATION: it closes missing coverage and separates
known theorem scopes, but establishes no actual-family rank/sign
fact or result beyond the inspected sources. A creative proof target
is not yet justified: independent signed evolution remains missing.

## Original nomination2051 (preserved, now assessed)

### Proposed bounded mechanism and discriminator

Use exactly C029m's real Jensen-weighted T_N, with every odd coefficient
retained and weights N!/((N-k)!N^k). H_N is its monomial Newton-sum
Hermite form, indexed by powers 0,...,N-1 only when actual degree N
has first been certified. For the finite first test the needed degrees
six and seven are already recorded in C029q; verify their applicability
when reading that input. Zero-padding means H_N in the upper-left block
and a final zero row and column. No free scaling, root fitting or change
of embedding after a sign inspection is proposed. If degree drops occur
in a future uniform argument, that case needs separate treatment.

The proposed condition is rank(D_N)<=2, not an asserted identity or a
consequence of ordinary Hankel structure. Only if a source review finds
this a meaningful nonduplicate hypothesis should a separately gated
calculation reconstruct the single N=6-to-7 difference from the exact
coefficients and unchanged certified pi/sqrt(2) intervals. One rigorously
nonzero 3-by-3 minor would reject this rank-two ansatz at this pair.
A rank-two certificate would preserve the mechanism for investigation
only; it supplies no favorable sign relative to the existing negative
subspace. An unresolved minor is inconclusive. No degree/precision sweep,
matrix-size campaign or theorem about eventual N follows automatically.

The plausible downstream use is a coefficient-explicit small-dimensional
description of how negative directions can change with N. Independently
signed update restrictions, initialization, singular/degree-drop cases
and uniformity would still be required to reach C029m. If the comparison
finds only a generic inertia theorem assuming the missing signs, a
different fixed-size displacement, or an already exhausted embedding,
park this nomination rather than rename it or claim progress.

Inputs for the review: C029m's exact family and index convention;
C029l's multiplicity-aware interpretation; C029n's audited2012 constants;
C029p's Jensen-weighted degree-six certificate; C029q's exact degrees
six/seven and distinct affine-quotient obstruction; review2019's common-
Hankel qualification. C029w/audit2051 is an undamped theta=0 contrast,
not the H_6 input here. Preserve C029r/v and stops2042/2044/2047; none
is a global prohibition. Read additional canonical proofs only for the
specific comparison needed. No cross-notebook theorem or Mathlib
coverage is assumed. Weighted convergence/upstream[9] remains qualified
and unused in any finite feasibility test.

At nomination time no mathematical derivation, rank computation or source approval
had been performed for this nomination. The completed audit2051 remains
valid independently of whether this next mechanism survives review.
Creative proof routing remains blocked by the lack of an independently
controlled signed update; this source comparison must not be labeled a
creative proof attempt merely because it addresses a central premise.
