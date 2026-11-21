# Source-approved independent audit: L756 dyadic specialization

TARGET: Audit L756's uniform dyadic zero-ordinate cancellation proof, checking the Selberg normalization, right-continuous Stieltjes identity, count correction and all endpoint multiplicities.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact/stronger-result and duplicate/failure comparison in 2026-11-04-zero-ordinate-exponential-cancellation-scope.md; the proposed audit keeps exactly the same scalar dyadic hypotheses and standard inputs.
SOURCE_EVIDENCE: https://arxiv.org/html/2505.14228v1 (3)--(4) and Section 2/(6)--(8), pp.2--5; https://arxiv.org/html/2006.08503v2 Section 1.1 and (1.4), pp.1--2; reused inspected BPT Section 2/(5)--(8), Lemma 2 and proof, pp.2926--2927, https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf and https://doi.org/10.1090/mcom/3652; L467 closed-shell conclusion and its existing critical audit.
COMPARISON: This is an audit of an elementary localization and moment application, not a new cancellation mechanism or a reproof of Selberg. The research target's completed ready assessment supplies unchanged source scope; original Selberg proof and source-manuscript audits remain outside this claim.
GAP: L756 has a full written proof but no independent critical audit. Verify exact endpoint signs, absolute constants and the uniform supremum limit, without presuming the claimed conclusion.
REASON: Separate literature-only approval completed in step 347 after reading L756 and matching its audit obligations to inspected standard inputs and reused BPT/L467 coverage; approval authorizes the next audit, not its verdict.
SCOPE: Only L756's scalar sum over every zero order for arbitrary real T tending to infinity and T<=tau<=2T; no beta weights, short windows, paid margin, initial signs, RH, Lindelof or simplicity.

Read L756 in full. Read only the necessary L467 closed-shell and
critical-audit passages. Essential input ID: L467; L018 is transitive
through L467 and is not a fresh direct input to L756. Source coverage is
reused from `2026-11-04-zero-ordinate-selberg-specialization.md` and its
parent, with the BPT proof/conventions retained from the October signed
count comparison. Original Selberg proof remains unread; the named
standard second moment is imported through its precise inspected
restatement. Full matching Mathlib coverage is unchecked.

Check N_+=N_*+m/2, R=N_+-M, and the identity on (T,2T], including T and
2T themselves being ordinates. Verify that values at the discrete
ordinate set do not affect the integrals, that endpoint R=O(log T)
retains m, and that q's integral is at most tau/(300T). Verify the
smooth primitive by differentiation and the weighted Cauchy--Schwarz
bound using integral_T^(2T) u^(-2) du=1/(2T). Check all constants are
independent of T,tau in the band, and inspect all strict/closed/half
endpoint correction signs. Do not infer RH from the scalar result.

Continue only if all those cases pass with the stated unconditional
inputs; otherwise repair a real error or preserve the specific failure.
No numerical experiment is needed. This assessment now approves the source scope for a separate audit; it
is not the independent audit verdict and does not classify the proof
as verified.


## Separate source approval — 2026-11-04, step 347

LITERATURE_REASON: The supervisor requires separate approval of the
new audit continuation. No target or hypotheses changed, so reuse the
completed exact/stronger-result and failure comparison rather than
repeat discovery searches.

Read L756 in full for source scope, L467's hypotheses, closed-shell
proof and 2026-10-26 critical-audit passages, the specialization and
parent comparisons, and the BPT source evidence in
`2026-10-07-signed-count-oscillation-comparison.md`, especially its
Section 2/Lemma 2 record. No independent mathematical audit is performed
in this literature-only step.

Reopened GSS v1 (3)--(4) and complete Section 2/(6)--(8): its
pointwise S estimate is unconditional, and its Stieltjes decomposition
retains the smooth term and boundary term. Its strict-count display
is not an arbitrary-endpoint theorem with bounded endpoint masses;
the next audit must check L756's explicit right-continuous count
replacement, not import the paper's endpoint O(1) uncritically.
Neither its contour argument nor its RH-dependent Corollary 1 is needed.

Reopened Chirre--Quesada-Herrera v2 Section 1.1 and Section 1.2/(1.4).
The normalization includes 1/pi in S, half endpoint weights in N and
averaged one-sided values for S. Display (1.4) is expressly unconditional
and attributes the moment to Selberg 1946, Theorems 6--7; its error is
O(T sqrt(log log T)). This covers L756's stated moment input, while
the paper's own Theorem 1 assumes RH and is excluded. The original
Selberg proof remains unread; import the named standard theorem via
this precise inspected restatement, without reproof.

The BPT author-offprint refresh timed out again. Reuse the already
inspected primary coverage, not the failed request: Lemma 2 and proof,
pp.2926--2927, supply |q(t)|<=1/(150t) for t>=2pi and continuity of
the difference at zero heights under half-count conventions. This is
not an essential source blocker because unchanged coverage is saved.
L467's prior critical audit covers closed shells, all analytic orders
and coincident ordinates. No full-manuscript audit is claimed for BPT,
Bellotti--Wong or Selberg.

DECISION remains SPECIALIZE for the exact TARGET. The next turn may
perform a REPRODUCTION proof audit using L756, direct local input L467
and these standard sources. Its complete obligations are those listed
above: right/half counts, both endpoint masses and their signs, smooth
primitive, correction, weighted moment estimate and uniform constants.
Any real error must be repaired or recorded; no audit verdict is
prejudged. Beta weights, smaller windows, paid costs and sign margins
remain outside coverage. Full matching Mathlib coverage is unchecked.

This approval repeats the existing source decision with a separate
scope check. It is STALLED as mathematical progress, not a new result
or evidence beyond the checked sources. No lemma, script, PROOF or DAG
change is authorized or needed. A creative transfer target has not
been assessed; finish the required audit before selecting one.
