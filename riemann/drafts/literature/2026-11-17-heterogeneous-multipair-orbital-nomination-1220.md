# Heterogeneous multipair response: completed comparison1221

TARGET: Establish or refute a universal bound |E_k(x)|<=C*x*sum_l b_l^2 for D_b=diag(a_1+i*b_1,a_1-i*b_1,...,a_m+i*b_m,a_m-i*b_m,r,...,r), finite m>=1,n>=2m, a_l,r,x>0, real b_l, x*sum_l|b_l|<=1/4 and 0<=k<n, where E_k is the adjacent-rank logarithmic-derivative difference from D_0 under separately normalized Haar laws with all entries fixed under differentiation; C must be independent of m,n and all real parts.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1221 made a bounded changed-family search for uniform imaginary-perturbation, real-field covariance, logarithmic-derivative and matrix-Bingham results; scoped orbital records retain only common-real-part and fixed-two-pair bounds. Exact queries, inspected passages and nonexistence/novelty qualifications are in drafts/working/2026-11-17-heterogeneous-multipair-source-review-1221.md; reuse adequate1213/1217 coverage.
SOURCE_EVIDENCE: Reopened Leake--McSwiggen--Vishnoi STOC2021 author PDF Thms1.3-1.4 p2, Prop2.2/degeneracies p3, Thm2.3/full proof p4; Novak2203.10746v1 (1.2) p2 and full Thm1.2/domain p6; newly inspected Miglioli2312.16816v5 Section2/Prop2.2 pp2-4, Prop3.1/Thm3.2 and full proofs pp5-6. Reuse1213/1217's Olshanski, Sra, Collins--Sniady and McSwiggen statement/version qualifications; precise citations and read limits below and in working1221.
COMPARISON: Real HCIZ pushforward allows arbitrary Hermitian fields and repeated spectra without fixed pair count, but supplies no uniform imaginary-response estimate. Novak retains bounded external spectra/small coupling; the target phase restriction does not bound unrestricted real contrasts. Miglioli supplies an exact kernel/unitarity identity, not TARGET. C030o/common-real-part and C030p/two-pair scopes do not cover this heterogeneous unbounded-pair claim.
GAP: No inspected theorem or source counterexample settles TARGET. Positive-real nonvanishing, the full physical derivative and a pair-count-independent C remain mathematical obligations. Actual-Xi reference, signed complement, scales, all-degree signs, theta signing and realization remain independent; no essential source is blocked for a direct bounded test.
REASON: The changed-interface literature comparison is complete enough for one bounded attempt using ready real-array/orbital inputs, without novelty certification. EXPLORE approves investigation, not a mathematical result; the supervisor owns separate approval of this updated assessment before invocation.
SCOPE: Exactly the unchanged finite-m TARGET with arbitrary positive pair real parts and common positive background, including n=2m, ranks0/n, zero phases, coincident real parts, every contrast sign, separate normalizers and the physical derivative; no arbitrary unpaired backgrounds, unread theorem applications or Xi transfer. Full matching Mathlib coverage unchecked; no cross-notebook input.
LITERATURE_REASON: Unbounded heterogeneous pair count is outside both ready1213's common-real-part and1217's two-pair scopes; reuse their unchanged standard inputs and inspect only the changed joint-phase interface and the specific new exact-kernel lead.

## Original nomination1220 (historical source status)

The following nomination records the pre-review obligations. Its
REVIEW_REQUIRED status and prospective source instructions are superseded
by the fields above and completed comparison1221 below; no mathematical
claim in the nomination is promoted to a proved result.

## Exact object and downstream use

For each rank j=0,...,n, take any orthogonal projection P_j on C^n
of rank j and probability Haar V in U(n). In the target, D_0 means
the diagonal obtained by setting every b_l to zero while retaining
each a_l and every background entry r. The definitions are

    Z_(j,b)(x)=integral exp(-x*tr(D_b*V*P_j*V*))dV,
    G_(j,b)(x)=-Z'_(j,b)(x)/Z_(j,b)(x),
    E_k(x)=(G_(k+1,b)-G_(k,b))-(G_(k+1,0)-G_(k,0)).

Each derivative fixes all diagonal entries. Each rank and reference
uses its own normalizer. When n=2m there are no r entries. Positive-real
nonvanishing on the closed window is part of the proposed result;
it must not be an unproved premise used to define a preferred branch.
These are proposed definitions and obligations, not a derived lemma.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. A uniform
heterogeneous finite-reference perturbation cost could accommodate a
growing finite collection with different pair real parts. Its relevance
does not assert that the actual-Xi phase window, finite-reference factor
supply or signed-complement budget has been paid. Theta signing and
graph realization remain separate. The existing source stops1117/1181/
1193/1200/1107 retain exactly their recorded scopes.

## Source comparison needed before an attempt

Reuse the inspected primary statements and full source qualifications
in working1213/1217 and assessment1202; reopen only essential changed
hypotheses or a specific new lead. The exact source citations are
Olshanski, J. Lie Theory23(2013), Cor3.2/Prop3.1,
[pp1015-17](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf);
Sra, author v3, 2 November2026, LemmaC.7/ThmC.8,
[pp25-27](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf);
and Collins--Sniady, arXiv math-ph/0402073v1, Cor2.4/Prop2.5,
[pp4-6](https://arxiv.org/pdf/math-ph/0402073v1).
These sources are not asserted to contain the new target. The changed
joint-phase problem at unrestricted heterogeneous real fields needs
theorem-level comparison. Unread sampling/Bingham/asymptotic leads in
working1213/1217 stay unread unless the new comparison makes them relevant.

Inputs to assess: C030l's full weak-row fixed-field comparison with
separate normalizers; C030p as the now-audited two-pair benchmark;
C030o as the audited common-real-part benchmark. Their proofs cannot
be summed under intermediate complex laws. Whole-block real invariance,
independence of disjoint corners and uniformity in m are not assumed.
No generalization of their proofs was derived in audit1220.

After coverage, the discriminating test would be an explicit absolute C
valid in the entire family, or a rigorous admissible sequence with
nonzero sum_l b_l^2 and unbounded |E_k|/(x*sum_l b_l^2). A bound growing
with m, a fixed-m calculation or finite samples would not decide this
target. Preserve a concrete unpaid estimate if neither result is reached;
do not repeat an unchanged failed mechanism. No mathematical exploration
budget is spent by this nomination.

Next turn is literature_comparison, standard/high, for the exact target.
If adequate coverage is established, a subsequent creative attempt can
be nominated with its specific mechanism and bounded test. No ready
assessment is written or approved by this research turn. Full matching
Mathlib coverage is unchecked; no cross-notebook input is proposed.

## Completed source comparison1221 (2026-11-17)

The full bounded source review, exact query strings, duplicate/failure
comparison, precise source versions and inspected proof ranges are in
[working1221](../working/2026-11-17-heterogeneous-multipair-source-review-1221.md).
This is a literature-only EXPLORATION; it proves no bound or obstruction.

Leake--McSwiggen--Vishnoi, STOC2021,
[DOI10.1145/3406325.3451094](https://doi.org/10.1145/3406325.3451094),
[author PDF](https://www.cs.yale.edu/homes/vishnoi/HCIZ.pdf), Theorem2.3
and full proof p4, with Prop2.2/affine-span qualification p3, cover the
real-reference representation at arbitrary finite dimension and repeated
spectra. Theorems1.3-1.4 p2 concern approximate sampling, with spectral
spreads in Theorem1.4's complexity; neither states the required response
bound. No algorithm or general orbital-law proof was audited.

Novak, [arXiv2203.10746v1](https://arxiv.org/pdf/2203.10746v1),
(1.2) p2 and Theorem1.2/domain p6, retains its absolute small coupling
and bounded external spectra. Reuse1213/1217's normalization mismatch
for unrestricted real contrast. This is a source-application limit,
not a counterexample to the target.

Miglioli, [arXiv2312.16816v5](https://arxiv.org/pdf/2312.16816v5),
Section2/Prop2.2 pp2-4, Prop3.1 and Theorem3.2 pp5-6, supplies the
complex kernel identity and its equivalent unitary restriction map.
Their statements and both theorem proof directions were read. The
regular-spectrum quotient is not directly evaluable at repeated
projection eigenvalues; no new limiting specialization is made here.
No nonvanishing or uniform logarithmic-derivative estimate at the
target's distinct kernel arguments is stated in these inspected results.

All three PDFs were accessible. Reuse the earlier fully inspected
Olshanski/Sra real-array and Collins--Sniady Haar-moment coverage and
McSwiggen complex-HCIZ identity; no general theorem needs reproof.
Optional Bingham and extensive-rank leads remain unread, nonessential
and noninputs. New use of an unread theorem needs separate coverage.

The unchanged target is ready for separate supervisor approval, then
one bounded proof_attempt/creative. Investigate whole-phase real-array
comparison without a pair-count loss; do not assume such an estimate.
Seek an explicit absolute C or a rigorous admissible divergent normalized
response sequence. Reality/nonvanishing, fixed-entry differentiation,
separate normalizers, n=2m and all listed endpoints remain obligations.
No additional target is nominated, no lemma/script is modified, and
actual-Xi signs/transfer, theta signing and realization remain open.
