# Exact-theta layer allocation: bounded negative-witness test

TARGET: Test C604b's exact theta allocation G_x(a) for a rigorously negative rational witness with 1<=x<=64 and 1/16<=a<=4, including all evaluation errors.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact/stronger searches and duplicate/failure comparison in 2026-11-01-theta-integrated-layer-compensation-scope.md; this is its single mathematical continuation, written after the literature-only review, not a completed calculation or novelty claim.
SOURCE_EVIDENCE: https://arxiv.org/pdf/1802.07942v1 Sections 2-2.1, pp.2-3 (interval inclusion and analytic-branch obligations); https://arxiv.org/pdf/1806.06725v1 Section 1.2, p.4, and Section 1.4.2 (1.18)-(1.20), pp.12-13 (certified series/derivative truncations with positive denominators). Exact sign/known-result comparison and version qualifications are in the companion assessment; local inputs C604b/C604a/L604/L605/L019/L016 and L564's complete-kernel envelope were read as specified there.
COMPARISON: The inspected known results cover base identities, theta regularity and numerical inclusion methods, not G's sign. The pointwise-remainder, generic-Stein and total-cancellation stops do not certify or refute this fixed-a actual-theta allocation. A witness rejects this allocation only, never Xi positivity or RH.
GAP: Verify the proposed allocation's admissibility from the existing identities and establish explicit enclosures for every quantity at any selected rational point; no witness, numerical budget, denominator separation or global sign is supplied by this assessment.
REASON: One bounded counterexample test can decide whether this particular sufficient-sign allocation survives before investing in global compensation estimates; no independently controlled signed estimate yet supports a creative proof attempt.
SCOPE: Exactly the full-line density and G below; one finite search and at most three rigorous candidate-certification attempts. Allow direct differentiated theta sums, explicit geometric truncation majorants, existing complete-kernel spatial envelopes, interval algebra and certified finite-interval quadrature. No generic density substitutions, wider box, global-sign claim, parameter-family sweep or higher-sign calculation.

## Fixed object and inputs

Use C604b's exact normalized full-line p=k/Z with k(u)=4 Phi(u/2),
L605's h and tau, q=-tau', and C604a's J_a. Retain exactly
L604's full K_x, including both cosines and both sine terms. The
proposed quantity, unchanged from the nomination, is

\[
G_x(a)=q(a)J_a(x)^2+
2p(a)\int_0^a[\tau(b)-\tau(a)]p(b)K_x(a,b)\,db.
\]

This restates the target, not a derived identity or sign. Before using
it as a sufficient mechanism, check its assembly from L604 and C604a,
including absolute convergence and the possible ell F^2 floor.
Do not discard that floor, change p to Phi(sqrt(s))/J, replace an
algebraic product by a modulus, or infer G's sign from total R<0.
L607 and the recorded Stein stops are contrasts, not theorem inputs.
L564 is used only for its existing complete-kernel envelope, with
its explicitly stated Phi_R/K scaling; no Hermite approximation is
required. No cross-notebook input is proposed.

## One bounded experiment and its certificate

An optional floating preview may evaluate the finite grid
x in {1,...,64}, a=j/16 for j in {1,...,64} (4096 points).
Record its grid and selection rule; the preview supplies no sign
evidence. Select at most three rational candidates in the stated box
for rigorous certification and stop upon one certified negative.
No random enlargement or repeated finer sweep is covered. A direct
analytic witness at a rational point in the same box also fits scope,
provided every evaluation bound is proved.

For each certification, retain and rigorously bound all theta summands
and omitted tails, the derivative used in q, the weighted spatial tail
in h, normalization Z, J_a and the complete b integral. Prove finite
theta truncation majorants using the inspected geometric-series method
and L016/L019, rather than treating their qualitative decay constants
as evaluated errors. Apply the existing spatial envelope only after
checking coordinates and factors; give the resulting explicit tail
constants and cutoffs. Any simplification or normalization cancellation
must be justified in the mathematical write-up, not assumed here.

All divisions need certified nonzero denominator intervals; mathematical
positivity alone does not justify division by a ball containing zero.
Interval subintegration may use the source's direct real box inclusion.
If an analytic quadrature branch is used, verify its whole complex
ellipse and callback analyticity, including every denominator; real-axis
smoothness is insufficient. Requested tolerances and small differences
between floating approximations are not error bounds. Reject a
non-finite enclosure or an interval crossing zero as an uncertified
sign. The inspected methods are imports, not claims of new algorithms;
all exact-theta specializations and implementation checks remain work.

Store complete evidence under scripts/ in the notebook and print only
the selected point, enclosure, actual/required error or upper bound,
failures and artifact paths. A witness needs a strictly negative upper
endpoint after every error contribution. Inspect the complete relevant
certificate values, using the shared JSON inspector for bounded access;
a preview is never verification. A future mathematical result belongs
in a canonical lemma with hypotheses, proof, citations and Mathlib
qualifications. None is established by this assessment.

## Decision threshold and remaining gaps

Reject the allocation if one fully certified G_x(a)<0 is found.
This does not sign its a integral or D. If no witness is certified,
record exactly the attempted finite domain and error failures; leave
global G positivity and the sufficient mechanism unresolved. Further
search requires a refined mechanism or informative new input, not a
larger copy of this sweep. Even global first-sign success leaves all
independent higher-sign obligations unresolved.

Expected next mathematical classification is POTENTIALLY_NEW only for
the exact allocation test, meaning the bounded comparison found no
matching result; no originality certification is intended. Imported
numerical methods remain known mathematics. Full/supporting Mathlib
coverage for this target is unchecked. Calculation/standard/high is
the appropriate purpose route; no creative proof is being relabeled
as routine, and no controlled theta-compensation estimate is invented
to satisfy a scheduling preference. This newly ready scope receives
separate next-turn approval before its mathematics is invoked.
