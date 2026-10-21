# Coverage: one slowly growing Poisson-law feasibility test

TARGET: Test whether a sufficiently slowly growing finite-prime Poisson covariance weight extends L423's counterlaw to every fixed single-prime second correlation while preserving its original selected tolerances, negative bulk support, fixed physical envelopes and vanishing capped cubic.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 209's completed comparison in drafts/literature/2026-10-18-growing-prime-poisson-covariance.md records exact queries, inspected primary statements and local duplicate/failure searches; it identifies the standard GCD/Poisson representation but no full matching law. Reuse that comparison; this is a newly written ready continuation awaiting separate approval, not an executed construction.
SOURCE_EVIDENCE: Aistleitner--Berkes--Seip, JEMS 17 (2015), section 3, pp. 1523, 1527, Lemma 1/(23) and preceding identity, DOI 10.4171/JEMS/537, https://ems.press/content/serial-article-files/32047?nt=1 ; Young, Arch. Math. 95 (2010), Lemmas 4--5 through audited L381 (7) and L428's sharp polarization; Kowalski B.6.3/B.6.5 and 3.2.5/3.2.6, Tao Lemma 2.3, and local L419's Borel Schur--Horn implementation as compared in the completed assessment.
COMPARISON: Standard finite-product Fourier identities and fixed-cutoff averaging cover the input class. No source establishes the full H-dependent covariance-law extension. Only the exact changed-weight coefficient, threshold and simultaneous law bookkeeping are authorized for the proposed mathematical attempt; no growing-twist theorem or conditional actual moment is imported.
GAP: Prove or obstruct compatibility of a slow cutoff with the exact normalization/full covariance correction, response-weighted limits, translated support and every original moment/envelope/cap requirement. Feasibility and all new asymptotic statements remain unproved.
REASON: The changed ansatz has adequate essential coverage for one bounded specialization test. Known representation and moment theorems should be cited, with a local proof only for the unprovided law specialization. No novelty or RH consequence is certified by this assessment.
SCOPE: The exact TARGET for the unmodified product P_y below, unchanged L421 rare components, actual full response, sharp dt/H height marginal, and a qualitative cutoff tending to infinity on all sufficiently large real H; no prescribed cutoff rate, global realization or conditional critical-jet law.

This is a continuation assessment written during step 209, to receive
separate supervisor approval next turn. No mathematics under its target
was attempted during the literature-only review. All source versions,
hypotheses, proof cases, applicability limits and duplicate/failure
comparisons are in
`drafts/literature/2026-10-18-growing-prime-poisson-covariance.md`.

The main gap is global mixed positivity. The intermediate target is a
single selected-law feasibility test after relaxing L428's exhausted
uniform density bound. A feasible construction would show that the
additional fixed-prime information still does not force this capped
lower implication in the relaxation. A specific incompatibility would
constrain this replacement mechanism. Neither outcome supplies actual
clipping, critical-function realization, capped nondegeneracy for the
actual functions, L413's full-error regulator margin or RH.

Use the proposed unmodified product and L423's normalization:

    P_y(t)=product_(p<=y) (1-1/p)/|1-p^(-1/2-it)|^2,
    N_H=E_H[w P_y], g_H=P_y/N_H, ell=log H.

Retain L421's high and intermediate kernels, their full Q,J_R,D_R,
and remaining mass w. Use L423's exact bounded-mean and full symmetric
matrix correction formulas, rather than its old bounds for fixed g0.
The original constraints, not the stronger error estimates achieved by
the fixed mixture, set the required tolerances. Every fixed prime p is
tested against the complete raw x-second density q_H through

    E_H[(q_H-f^2)p^(-it)]=o(ell),

with its onset allowed to depend on p. No simultaneous uniform estimate
over primes increasing with H is a target. The additional W^2 x^2
requirement in L423 is its stated T ell+o(ell) hypothesis; an unchanged
O(sqrt(ell)) remainder from the fixed-mixture conclusion is not imposed.

Import the finite-product representation by its exact citation and
L428's actual sharp prime limits; do not reprove a general GCD theorem
or Young's moment theorem. Establish only the necessary fixed-product
specializations and the actual-response W,W^2/gamma limits. For tails,
prove an adequate normalized weighted-mass bound or explicit alternative;
neither weak convergence for a moving test nor an uncontrolled
supremum-times-tail estimate is sufficient.

The decisive test is simultaneous, not a sequence of assumed margins:
write the minimum/maximum product bounds and normalization estimates,
then check the order-sqrt(ell) full matrix subtraction, positive
definiteness, negative trace and translated six-atom negativity with
their actual errors. Check all six exact raw seconds and first-B mean,
the first-D limit, signed cubic, all 23 quartic limits, absolute
third/fourth envelopes, the fixed physical-jet constants, and the capped
absolute cubic for every fixed lambda with one cap-independent family.
A slow diagonal must retain all these requirements together on an
eventual real-H ray, not merely a subsequence. Its finite thresholds
may depend on the finite prime stage; no effective rate is demanded.

Continue only if that simultaneous proof closes or a quantitative
conflict specific to this ansatz is established. If the approach needs
new uncovered moment inputs, a changed product, extra rare second
mass or an unproved actual conditional law, stop that attempt and
record the missing condition for separate review. Do not silently
repair the target or recast L428 as a ban on all unbounded weights.

Essential local input IDs are L381, L389, L419, L421, L422, L423 and
audited L428; L427 is only a narrower historical contrast. Their
selected-list results and previous stops are preserved. The independent
global-realization, actual-clipping and regulator assumptions remain
unresolved; I and C426c play no role. Mathematical exploration usage
remains 0 of 3 before this proposed attempt. Full matching Mathlib
coverage has not been checked; no absence claim is made.
