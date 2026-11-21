# Fixed-prime taper correlation audit — coverage1432

TARGET: Audit C019z's fixed-prime four-taper correlation reduction (6)-(12), including K_1 comparable to (log L)^4 and the O((log L)^3) error, for every j=ab with 1<=a,b<=4 under the original integer-d scales.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1432 searched the scoped Jensen assessments, named witness histories and stops1408/1431, plus exact/fractional-mollifier, fixed-prime correlation and autocorrelation-ratios queries. No completed matching audit or theorem was located in that bounded search; no novelty inference follows. Full evidence: drafts/literature/2026-11-18-jensen-fixed-prime-correlation-source-notes-1432.md.
SOURCE_EVIDENCE: Inspected NIST DLMF v1.2.8 (15 September 2026), 4.6.7 with its domain, 27.4.3 and 27.4.10, https://dlmf.nist.gov/4.6.E7 ; PRZZ arXiv:1802.10521v1 (28 February 2018), Section 4 Theorem 4.1 and proof opening through prime-power separation, printed pp18-19, https://arxiv.org/pdf/1802.10521v1 . Reuse BCR1411.7764v1 Theorem 1/Sections 3.1-3.2 as inspected in source-notes1410/1429 and the other ready1410/1402 comparisons.
COMPARISON: Standard binomial/Euler-product identities cover the supporting coefficient algebra only. The inspected ordinary twisted-moment theorems, including PRZZ's stronger special-coefficient length regime, do not certify the fixed-j four-taper correlations. C019x (9)'s existing audit covers the proposed lower norm input; its applicability and C019z's prime-extraction/boundary estimates remain to be audited.
GAP: Independently check C019z (6)-(12), its K_1 norm order, exact prime-2/3 extraction, complete support to 36R, squared taper error O(ell^2), two-array correlation error O(ell^3), conjugations and all nine local factors under the original integer-d scales. Coverage is ready; these claims remain unvalidated.
REASON: No essential unread theorem remains for this finite coefficient audit: its supporting identities are accessible, and the local norm input has an existing audit. SPECIALIZE permits a separate conceptual audit of the stated finite-taper difference, without importing a time-moment theorem or reopening the exhausted completion route. Newly ready coverage requires separate approval before research.
SCOPE: Original real alpha for zeta^(-1/2) on Re(s)>1, the four linear tapers, both shifted factors, h=3pi/log X, L=floor(X^(1/1000)), positive integer d with C019z's stipulated T,X scales; only fixed j=ab, 1<=a,b<=4. No untapered replacement, RH assumption, ordinary-to-heat moment transfer or near-layer completion.

LITERATURE_REASON: Nomination1431 changed scope from joint divisor completion to an independent coefficient audit; broad witness coverage did not assess the exact norm and prime-extraction hypotheses. Review1432 supplies that missing comparison and does not repeat ready-target browsing.

The main gap remains L030--L032/C032a actual-Xi all-degree positivity.
This intermediate audit could validate or repair the coefficient scale
used by C019z's claimed resonant numerator. Even success leaves its
later prime-sum passage and scalar sign, unequal frequencies,
mixed/nonconjugate channels, denominator, actual-P error and actual-Xi
transfer unresolved.

The full source comparison, access qualifications, local duplicate/stop
checks and concrete audit obligations are in
[source-notes1432](2026-11-18-jensen-fixed-prime-correlation-source-notes-1432.md).
Review1432 derives no new estimate and performs no mathematical audit.
The target text is unchanged from nomination1431. Approval of this
newly ready assessment is separate from invoking research.

Essential inputs are C019y (1), C019z's coefficient definition and
(6)--(12), C019p's finite alpha-convolution bound, and audited C019x
(3)--(9) with its four-taper sector argument. The audit must check
their identical coefficients and scales; no C019y resonant estimate,
C019z (3)--(4), C020a/b sign, actual-P transfer or prime-sum theorem
is a premise. Keep every comparison-array entry beyond R, every
shifted phase and all support/boundary errors.

Continue only by retaining K_1 comparable to ell^4 and the uniform
O(ell^3) error for all nine required j after a complete conceptual
check, or locating a specific failed estimate and its consequence
for (12). A formal untapered Euler product or source availability
does not pass that test. This is proof_audit/conceptual_audit because
support changes and signed normalized correlations need independent
logical scrutiny. No full matching Mathlib coverage was checked.

The completion route remains parked after its three explorations;
this audit does not reset that budget. No justified creative mechanism
at the central gap has emerged; the unresolved coefficient scale is
the essential blocker before relying on its resonant consequence.
No cross-notebook input, new lemma, mathematical script or general
moment reproof is proposed.
