# Pair-only quotient: bounded attempt

The approved target is the exact TARGET in
`drafts/literature/2026-10-20-forget-distinguished-root-quotient.md`;
reuse its SPECIALIZE coverage. Main gap: rational-point control and both
L095 integer systems. Inputs: audited L106 monodromy/branch data and
L107 invariant coordinates and marking. No L108 boundary-field
classification is needed, and its unfinished work is preserved.

Intermediate target: forget r, retaining u,z and the quadratic factor
(T−u)²+3z. Put s=H0(u,z), the even binomial remainder of phi, and
H1(u,z)=G1(u,z) from L107. Candidate open: H1=0 with z*s*(s−1)
invertible; candidate marked companion: v²=z. This is a construction
to verify, not an asserted hyperelliptic model.

Initial counts on 55 unordered pairs predict branch histograms
5^11, 1^28 3^9, 11^5, hence genus two; 110 ordered pairs predict
genus three. All inertia orders are odd, suggesting an everywhere
étale marked double cover. The incidence map forgetting r should have
degree nine. Remaining checks: scheme equations, full geometric
connectedness, rational twist, proper extension, complete branch
normalization and reversible normalized-unit lifting.

Continue if these checks succeed and genus is strictly below 38;
abandon this simplification on a hidden component or wrong twist.
A favorable genus is only a necessary rational-point image: rational
root recovery, open points, remaining global factors, both integer power
tests, gcd/positivity and minus-eleven remain open. Arithmetic cap:
at most 1000 labels in any one permutation universe.

This file checkpoints unfinished reasoning before the finite check and
canonical proof are written.

Completed in this invocation: the canonical proof is
[L109](../lemmas/L109-pair-only-genus-two-and-minus-three-lifting.md).
The genus-two diagnostic succeeds; the full finite certificate is
`scripts/global-fiber-genus/forget-root-certificate.json` with 3,082
checks passing and no failures. Proof details and qualifications live
in L109. Its independent critical audit is pending; the newly proposed
audit target requires a separate coverage approval.
