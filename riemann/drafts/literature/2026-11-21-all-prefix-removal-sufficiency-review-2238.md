# All-prefix removal sufficiency: nomination2238, reviewed2239

TARGET: Review whether F(z)=exp(-z^2)(2+cos(z))sin(z)/(3z) can refute all-prefix real-zero-removal positivity as an RH bridge, checking every finite quotient, smooth positive inverses, uniform second moments and the growth-order limitation.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed2239: scoped all-prefix/cosine-power/sinc and named-failure comparisons plus bounded external transform, zero-removal and stronger-criterion searches; exact queries, inspected passages and unread leads are in drafts/literature/2026-11-21-all-prefix-source-notes-2239.md. No novelty claim follows.
SOURCE_EVIDENCE: DLMF1.2.8 equations5.12.5,5.12.1,5.5.1,5.5.3,4.22.1,4.14.1-2 and5.2(i); Tao2009 Exercises14/16/29/41 and inversion(11); Csordas1309.0055v2 Theorem3.7/full proof p8 and order statement p10; Arellano-Pena amended30September2026 section5.3 p10 supplies exact base-factor overlap. Full citations and qualifications are in source notes2239.
COMPARISON: Classical formulas cover the ordinary tools, not the assembled all-prefix model. C919m/C919o remain finite actual-Xi inputs; L262 and finite-block1117 do not cover one fixed function at every n. Csordas's all-order correlation positive-definiteness criterion is a different assertion. The Gaussian-cosine base factor is already recorded externally.
GAP: A later proof must establish the exact normalized quotients for every n, all removable points, smooth strict inverse signs and super-exponential derivative tails, uniform second moments, complete real-root inventory, one surviving nonreal zero and exact growth order. An order-two model cannot refute an order-one or actual-Xi theorem.
REASON: Essential identity coverage is now accessible; a source-covered specialization is justified without reproving standard formulas. No all-prefix countermodel or RH bridge has been established in this literature turn.
LITERATURE_REASON: Startup2238 was REVIEW_REQUIRED for a changed all-prefix quantifier and unread cosine-power/product coverage. This completes that coverage; it does not repeat a ready finite-removal assessment.
SCOPE: One fixed F and its proposed P_n, every integer n>=0; no parameter change, actual-Xi theorem, unproved residual zero-freeness or new mathematics in this literature turn. A newly written continuation2239 requires the supervisor's separate next-turn approval.

## Completed review2239

The full source comparison, exact hypotheses, base-factor overlap and
unresolved specialization obligations are recorded in
[source notes2239](2026-11-21-all-prefix-source-notes-2239.md).
The bounded mathematical continuation is
[assessment2239](2026-11-21-all-prefix-model-specialization-2239.md).
This is EXPLORATION, not a proved model obstruction or novelty finding.
Full matching Mathlib coverage remains unchecked. PROOF.md and DAG.md
are unchanged because no mathematical argument changed.

## Preserved nomination2238

The following is the original proposal and its then-uninspected leads;
the completed source decisions above supersede its review status.

## Exact proposed test, not a result

Let the proposed model be the function in TARGET, with its removable
value at zero. For integers n>=0 propose the finite divisors

    P_n(z)=product_(k=1)^n (1-z^2/(k*pi)^2),  P_0(z)=1,
    F_n(z)=F(z)/P_n(z), with removable values where justified.

The proposed future obstruction asks whether every F_n is the
angular-frequency Fourier transform of an even, smooth, strictly
positive probability density f_n on R, with every derivative decaying
faster than each fixed exponential, and whether

    sup_(n>=0) integral_R u^2 f_n(u)du < infinity

can hold while one fixed nonreal zero survives in every F_n. The
complete positive real-zero list, multiplicities and removability
must be checked; labeling the listed factors as an exhaustive prefix
is part of the obligation. A finite-n check cannot settle this target.

The suggested source leads are Fourier transforms of compactly
supported even cosine powers (beta/gamma integral identities), the
sine product and Gaussian/convolution/translation formulas. These
are leads, not inspected theorem evidence or a derivation. In
particular no inverse density, identity, moment bound or nonreal-zero
certificate is proved here. Use precise primary statements and proof
cases before attempting the specialization; ordinary formula recall
is not source approval. No Mathlib matching coverage is asserted.

Growth is a load-bearing qualification: the Gaussian factor suggests
an order-two mismatch with Xi, which the source review must delimit.
Do not silently upgrade such a model to order one, infer that any
actual-Xi theorem is false, or add an unproved zero-free residual
condition. No normalization/tightness claim is a substitute for
the later signed or arithmetic bridge.

## Three mechanisms compared and routing decision

1. A third finite actual-Xi removal would extend the count in C919o.
   It offers no new uniform mechanism or bridge; do not nominate it
   merely because the finite computation passed.
2. Global decrease of C919m's residual remains a legitimate open
   gap. Review2230 and the local-origin result do not pay the signed
   cosine comparison; no new comparison estimate was found in this
   audit. Do not repeat that search or reopen the parked optional
   Spigler access attempts without a specific new input.
3. The explicit all-prefix sufficiency test is selected. It asks
   whether even an infinite sequence of individually positive inverse
   kernels plus a uniform second-moment bound would settle the generic
   zero question. Its test is independent of actual-root existence,
   finite certificates and inaccessible source supplements. If viable,
   it would identify a necessary distinction for any proposed removal
   bridge; it would not provide the missing actual-Xi estimate.

This is a nomination for source comparison, not a creative proof
attempt relabeled to meet scheduling preferences. A genuinely new
central actual-Xi mechanism remains blocked by the absence of a
specific uniform signed/arithmetical estimate. The next review should
import ordinary identities where available and classify the later
specialization honestly, rather than presume originality.

## Recorded failures and distinguishing scope

The September23 positive-kernel-three-level stop (canonical L262,
not newly loaded here) explicitly retains its Gaussian/order-two
limitation. It does not assert all-prefix real-zero-removal positivity.
The finite-block1117 comparison allows changing finite countermodels;
this nomination demands a single fixed function and all n. The
September23 nonreal-deflation stop removes the detecting pair; this
candidate must retain its nonreal zeros. The finite-divisor667 stop
concerns unpaid signed Cauchy--Binet residual minors at growing rank,
not positivity of these direct inverse densities. None is a premise
proving this candidate; the differences require verification.

The scoped filename/content searches found related sinc and Gaussian
constructions but no inspected matching all-prefix statement. This
is not a novelty finding. Further exact local/source comparison is
required before a mathematical attempt, including stronger results
and obstructions at the same quantifiers. No cross-notebook input.

## Continuation or abandonment

Continue to a separately gated mathematical test only when exact
source coverage supports the candidate's full all-n formulation, or
isolates a concrete unproved difference without assuming the desired
positivity. Abandon this particular candidate if any defining factor,
inverse sign, all-n identity or required uniform bound fails; record
the first defect rather than changing parameters. If a source already
settles the claim, import it with the necessary specialization only.
An order-two obstruction must remain explicitly order two. Actual-Xi
iteration, all-degree mixed positivity and RH remain unresolved.

Essential continuation inputs are L018/L019/L058 and accepted
C919m/C919o as motivation and scope comparisons, not premises for
the model's signs. C919f's backend contracts remain attached to the
actual finite result and do not establish any fact about F_n. The
new target needs its own primary transform/product coverage. Newly
written REVIEW_REQUIRED is not approval, and does not reject the
completed audit2238.
