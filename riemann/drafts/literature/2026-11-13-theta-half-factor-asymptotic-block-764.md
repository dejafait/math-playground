# Formal theta half-factor: bounded asymptotic obstruction test

TARGET: Attempt an eventual 3-by-3 Hermite-block sign test for the formal additive half-powers of L795's centered monic P_d, using coefficient asymptotics through fixed order at most eight and no degree sweep.
CHECKED: 2026-11-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Step764's uniform half-power review searched fractional-divisibility, inverse-convolution, moment-obstruction and stronger preserver terminology; compared theta/additive/free assessments and stops. No inspected matching actual asymptotic block test was identified; no novelty or exhaustive-absence claim.
SOURCE_EVIDENCE: Arizmendi-Perales1611.06598v2 Propositions3.4/3.6 pp7-8 and Lemma4.1 p9; Nathanson1911.01745v2 Lemmas1-2/Theorem1 pp1-3; O'Sullivan2007.13582v2 Theorem1.4, (1.2), Section7/(7.3)-(7.13), with full Laplace-proof coverage reused from step559. URLs and applicability limits below and in the completed parent review.
COMPARISON: Known inversion and Hermite testing permit a necessary-condition diagnostic without real-root assumptions. Actual-coefficient expansions supply inputs, not the block sign. This differs from finite d=3/4 checks, L825's common symbol, L827's reciprocal Stieltjes moments and the unpaid oscillatory bulk estimate.
GAP: Derive the exact block and control every cancellation in its large-d principal minors; neither a negative minor nor eventual PSD has been obtained. Full-factor hyperbolicity, effective onset, shifted/mixed compensation and global assembly remain unproved.
REASON: A bounded analytic obstruction can discriminate the degree-dependent uniform-factor proposal without another finite-degree sweep. This newly ready scope requires separate approval next turn; no actual block formula or sign is asserted in this literature turn.
SCOPE: Integers d>=4 tending to infinity; L019/L021/L795 coefficients, monic normalization then algebraic centering, symmetric additive convolution at the same degree, fixed offsets r=0,...,4, truncation order K<=8; no root premise, fitted law, evaluator replacement, common symbol, dilation repair or growing matrix size.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This intermediate target tests a proposed uniform inverse-factor input.
A failure could prevent further investment in an inadequate input;
a pass does not prove the missing full-factor signs.

Divide L795's P_d by its nonzero leading coefficient and translate to
cancel the next coefficient. Use its formal halved-cumulant polynomial
at degree d in [Arizmendi–Perales v2](https://arxiv.org/pdf/1611.06598v2),
Propositions3.4/3.6; Lemma4.1 supplies Newton conversion. The later
mathematical attempt must write out the identities and uniqueness needed
for this specialization. No common symbol or real-root measure is assumed.

Let s_j be the algebraic jth power sum of the formal polynomial's complex
roots counted with multiplicity, with s_0=d. The selected matrix is
(s_(i+j)) for 0<=i,j<=2. [Nathanson v2](https://arxiv.org/pdf/1911.01745v2),
Theorem1, supplies the full root criterion. Use all principal minors
when asserting PSD; nonnegative leading minors alone do not suffice.
A negative principal minor is an obstruction; a PSD proper block cannot
certify the full factor. Algebraic squares must not become modulus squares.

[O'Sullivan v2](https://arxiv.org/html/2007.13582v2), Theorem1.4 and
(1.2), apply to L021's gamma normalization. Retain fixed-offset remainders
through every centering and minor cancellation. Choose K<=8 before
expansion; do not differentiate remainders. Step764 rechecked the primary
statements and Section7 proof, reusing step559's full Laplace coverage.

The decisive evidence is an eventual strictly negative minor with error
smaller than its signed main term, or a proof of PSD of this block for
all sufficiently large d. In the first case stop the all-degree half-factor
proposal; in the second retire this low-order obstruction without a
full-root inference. If K<=8 does not separate the relevant terms, preserve
the algebra and uncontrolled error and stop without a sign claim. No
automatic increase of order, finite-degree sweep or new source round is
authorized. No numerical onset is promised.

Essential local inputs: L019/L021/L795. L823/L824 are finite contrasts,
L825 the fixed-coordinate contrast, and L827 concerns different reciprocal
data. L778/L791 software contracts are unnecessary for this analytic
test; using finite data would change scope. Full-support interlacing and
oscillatory-bulk stops remain. No cross-notebook result, RH or actual-root
measure is a premise. Full matching Mathlib coverage is unchecked.

This is development with established methods, not a protected creative
mechanism or a theorem reproduction already present in the inspected
sources. The exploratory application is not claimed original. One future
bounded attempt is proposed; none occurred in step764.
