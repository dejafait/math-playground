# Direct shifted heat-product attempt — source coverage1377

TARGET: Attempt (C) for C019k at h_d=3*pi/log(Y_-): determine the signed leading band coefficient and control both moving-cutoff product remainders below B_d*log(Y_-).
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-target searches and local duplicate/failure checks in assessment1376/review1377; the statement, actual heat time, phase, band and floors are unchanged. No additional discovery search or novelty claim.
SOURCE_EVIDENCE: Assessment1376/review1377 inspected Bettin1111.0925v1 Theorem1 and proof, Koesters0803.1141v2 Section2/(2.4)-(2.6) and AppendixA.1-A.3, Mawia2019 pp239-240 entry-time correction, and the actual Polymath formulas already specialized in C019k/audit1376.
COMPARISON: Known shifted zeta moments do not supply this deformed signed mean. Primary real-part product proofs and moving-entry methods provide a direct finite-sum strategy; only the actual heat-weighted coefficient and its error payment are proposed work.
GAP: Prove or reject (C) at its fixed shift by retaining both real-product channels, all unequal/equal-index cases, the exact gamma multiplier and the two actual floor domains, with errors compared to B_d*log(Y_-). No sign or error saving is assumed.
REASON: This is a bounded new signed-product mechanism for the moving heat reference after its approximation audit. It uses available standard estimates and needs no unread historical shifted-moment theorem; a negative coefficient cannot be inferred from the undeformed sine kernel.
SCOPE: Positive integers d tending to infinity; C019k's exact T,Y_-,Y_+,t_d(Y),s_*,G_t,m and floors; h_d=3*pi/log(Y_-); no RH, nonvanishing, simplicity or heat real-zero hypothesis; one existential common onset.

## Exact input and proposed test

Use the unchanged (C) displayed in
[assessment1376](2026-11-17-jensen-heat-shifted-correlation-1376.md).
B_d=Y_+-Y_-. The integral ends at Y_+-h_d; the second factor is
S_d(Y+h_d) at its own t_d(Y+h_d) and its own source floor. Every
normalization and branch is exactly C019k's. Its mathematical inputs
are C019k/C019j, with the inherited actual-xi setup L018/L021.
Reading those canonical proofs is sufficient; no cross-notebook input.

The proposed mechanism is to retain the exact finite-sum real product,
separate its oscillatory contributions with their true entry domains,
and determine its full leading sign. No expansion or limit formula for
that product is asserted in this assessment. Neither replacing the heat
weights by 1 nor replacing both floors by a constant is preapproved.
Any approximation must have an explicit error on the requested scale.
No lemma need be created if the test fails or remains inconclusive.

## Precisely available standard estimates

Koesters, [arXiv:0803.1141v2](https://arxiv.org/html/0803.1141v2),
AppendixA, states these classical tools with exact hypotheses:

- A.1 (=Titchmarsh, *The Theory of the Riemann Zeta-function*, second
  edition, Lemma4.2): for real differentiable F on [a,b], with monotone
  F' and either F'>=epsilon>0 throughout or F'<=-epsilon throughout,
  |integral_a^b exp(iF(x))dx|<=4/epsilon.
- A.2 (=Titchmarsh Lemma4.4): for real twice differentiable F on [a,b],
  if F''>=epsilon>0 throughout or F''<=-epsilon throughout, the
  corresponding bound is 8/sqrt(epsilon).
- A.3 (=Titchmarsh Lemma7.2):
  sum_{1<=m<n<=X} 1/(sqrt(m*n)*log(n/m))=O(X log X).

These are standard inputs, not new results. Any use with a varying
amplitude must separately justify its integration-by-parts or variation
bound; an unweighted test is not a weighted theorem. Any monotonicity,
derivative separation, exceptional phase region, entry interval or
summability condition must be verified for C019k, not copied from the
source's different phase. The gamma/Stirling input is the one already
cited and audited in C019k; differentiating a mere O-term is prohibited.
C019k's pointwise floor treatment is not itself a moment calculation.

The completed source review records the primary proof cases inspected.
Koesters's (2.4)-(2.6) is a fourth-moment proof with divisor coefficients;
its published bounds are not imported for this sum. Mawia's correction
has q>1 and gives an entry-time method, not a q=1 shifted heat theorem.
Bettin's shifts are fixed in the integration variable and his chi factors
remain essential. Selberg's original Lemma15 and Atkinson1948's original
proof are unread leads, not assumptions. Their access limitations do not
block this direct finite-sum attempt. Matching Mathlib coverage is
unchecked; no formalization claim is made.

## Bounded decision and downstream use

Continue only with a negative full leading coefficient and remainder
strictly below its B_d*log(Y_-) margin at a common onset. A nonnegative
coefficient plus controlled lower-order remainder rejects (C); an unpaid
remainder, floor endpoint or phase term parks the attempted proof without
claiming (C) false. Preserve all terms and the first precise obstruction.
Do not optimize the shift or change the band without a new assessment.

A proved negative correlation could start a sign-distribution argument.
It does not on its own supply amplitude margins, error transfer from
C019k through C019j to actual Jensen values, robust disjoint ordered
samples, c*sqrt(d) roots or bulk separation. Every-degree hyperbolicity
and the L030-L032/C032a actual-Xi positivity gap remain independent.
Stops1345/1355/559 and the parked direct (A) route are preserved.

This assessment was written during literature review1377. It nominates a
ready bounded attempt; it does not perform it. Per the supervisor gate,
newly written ready coverage receives separate approval before research.
