# Fixed-cutoff density cap loss: proposed known-tool specialization

TARGET: Test whether the mass removed by the (log T)^4 cap from C481a's microscopic density difference is O(T), uniformly for all sufficiently large real T.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed sharp-polynomial and truncated-density searches in 2026-10-31-truncated-microscopic-density-review.md. They identified a sharp unconditional finite mean-square input, but no matching absolute-difference lower-bound theorem; no novelty is asserted for this upper-tail specialization.
SOURCE_EVIDENCE: Curran 2303.10123v2 Lemma 2.3 explicitly gives (T+O(N)) sum |a_n|^2 for arbitrary complex coefficients; Montgomery--Vaughan (1974) Corollary 3 pp. 75/82 supplies its original weighted-error background, with extraction qualifications recorded in the completed review. Retain C481a's definitions and L481 Section 1's finite divisor-coefficient method.
COMPARISON: Known finite mean squares and elementary finite coefficient/tail inequalities cover the proposed method. The difference needing proof is its sharp squared cutoff, three translated densities, complete unweighted cap loss and uniformity in real T. This is reproduction, not a creative positivity mechanism or a reproof of the mean-value theorem.
GAP: Establish the required fourth-polynomial-moment upper scale and pass it to the removed mass with all constants independent of T. No cap-loss bound, capped lower bound, ratio lower bound or full-residual comparison is established in this assessment.
REASON: Nominate a bounded known-tool calculation that determines whether the explicit cap is an independent concentration obstacle. It uses newly inspected essential coverage and requires a separate approval next turn before calculation; the completed source review is not a mathematical proof.
SCOPE: T real tending to infinity; L=log T, h=1/L, M=floor(sqrt(T/(2 pi))) fixed for that T; A_M(t)=sum_(n<=M)n^(-1/2-it), F_M=|A_M|^2, D_h(t)=F_M(t+h)-2F_M(t)+F_M(t-h), J=[T+h,2T-h]. All ordered pairs and endpoints retained; no RH, moving cutoff, independent phases, Haar limit, sharp lower-bound or residual-weighted hypothesis.

The exact target is the existence of absolute C,T_0>0 such that for
every real T>=T_0,

    E_cap(T)=integral_J (|D_h(t)|-min(|D_h(t)|,L^4))dt
                  <= C T.

This is a proposed estimate, not a result. The required loss is smaller
than T log T. An O(T log T) estimate alone does not meet the test.
If successful, write the precise conditional comparison between the
capped and uncapped lower-bound premises, distinguishing the same
constant from any smaller eventual constant. Do not assert either
premise. If the sharp finite-height estimates fail at this threshold,
record the actual loss and stop this implementation without claiming
the target false.

Import the mean-square theorem, without reproving Hilbert's inequality:
[Curran v2, Lemma 2.3](https://arxiv.org/html/2303.10123v2#S2).
The direct original reference and exact extraction limitations are in
the completed review. Its arbitrary finite coefficients are sufficient;
no RH-dependent part of Curran's argument is authorized. Retain the
actual support of A_M squared, and account for interval translation by
unit-modulus phases or an explicitly justified interval enlargement.
Do not replace the finite-height average by a coefficient diagonal
without the theorem's error.

The intended calculation uses the finite multiplicative convolution
of A_M with itself and an elementary upper bound for its coefficient
squares, as in the finite factorization-count method of L481 Section 1.
The two-factor instance and its harmonic sum must be justified in the
mathematical turn, with the restricted supports retained or enlarged
only in an upper bound. Standard finite algebra and nonnegative
integral inequalities need no new analytic distribution hypothesis.
This nominates a specialization; it does not derive that coefficient
bound or the fourth moment in the literature turn.

Essential local input IDs are C481a (definitions and downstream
conditional transfer) and L481 (complete ratio normalization and
finite-coefficient proof template). L477 fixes the surrounding cutoff
and independent residual problem. L481's stopped interpolation,
L482's global polynomial-length obstruction and L572's rank certificate
remain unchanged; they are contrasts, not upper-tail premises.

Even success supplies no positive mass: the actual-height uncapped
c T log T density premise remains unresolved. Ratio-to-full-residual
transfer, both defects, negative mass and all Xi signs remain open.
No new central creative lower-bound mechanism has yet been justified.
Do not repeat source browsing on the unchanged cap-loss target once
this assessment is separately approved. Full and supporting Mathlib
coverage are unchecked. No cross-notebook input.
