# Growing-degree Laguerre reference nomination1590

TARGET: Assess shifted, scaled or reflected generalized-Laguerre references for unchanged P_d: check source coverage for matching its first three subleading coefficients and testing whether the first two remaining Schmeisser costs can be o(d^2).
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1591 inspected the exact NIST Laguerre formulas, Pan-Zeng2020 opening formulas and Holland2608.08682v1 Lemma4.3 including its proof; bounded exact-family queries and local duplicate/stop comparison are recorded in drafts/literature/2026-11-18-growing-reference-source-notes-1591.md. No matching optimized residual-cost theorem was located; no novelty claim.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 Tables18.3.1/18.9.1 and (18.5.12), https://dlmf.nist.gov/18.3 https://dlmf.nist.gov/18.9 https://dlmf.nist.gov/18.5#E12 ; Pan-Zeng2020 B81e p1 (1.1)-(1.4), https://www.mat.univie.ac.at/~slc/wpapers/s81panzeng.pdf ; Holland2608.08682v1 Sections2-4/Theorem1.1, https://arxiv.org/html/2608.08682v1 ; reuse Schmeisser2002 Theorem1/Corollary1 and full relevant proof coverage in C028a/c and source-notes1503.
COMPARISON: Exact Laguerre coefficient, recurrence and positive-weight norm formulas are available for alpha>-1. C028a/c and C028h/i retain their limited family stops. Holland's large-shift ascending-coefficient comparison does not cover affine matching of the first three subleading coefficients of unchanged unshifted P_d or the retained Schmeisser cost; details and limits are in source-notes1591.
GAP: Affine normalization, three-coefficient feasibility and the fourth/fifth residual-cost test remain mathematical work. No feasible parameters, asymptotic cost or source obstruction is asserted for this family.
REASON: Essential formula coverage is now adequate for one bounded specialization. Nominate the exact test in assessment1591 for separate approval; do not perform it in this literature-only turn or infer full-cost control from two small retained terms.
SCOPE: For each integer d>=5, unchanged actual P_d=R_d/gamma_0; monic generalized-Laguerre reference polynomials through degree d, with alpha_d>-1 and affine real variable change x=m_d+sigma_d*z, m_d real, sigma_d real nonzero. All parameters may depend on d and approach admissible boundaries. No RH, root reality/simplicity, assumed reference match or bounded conditioning.

## Exact proposed test, deferred to a separately covered turn

Let q_n be the monic affine images of the generalized-Laguerre
polynomials with the same alpha_d,m_d,sigma_d for 0<=n<=d.
The prospective positive reference is the affine pushforward of the
normalized weight z^alpha_d*exp(-z) on z>0; negative sigma_d permits
reflection. No recurrence or coefficient identity is derived here.
For P_d=sum a_n*q_n and h_n=integral q_n^2 dmu_d, the proposed matching
conditions are a_(d-1)=a_(d-2)=a_(d-3)=0. The proposed retained statistic
is (h_(d-4)*a_(d-4)^2+h_(d-5)*a_(d-5)^2)/h_(d-1), with threshold o(d^2).
This is a test nomination, not an established mathematical input.

The original nomination asked the source review to recover the primary recurrence, norms,
orthogonality range and affine conventions, and compare exact statements,
stronger results and obstructions for this growing-degree family. Search
the specific non-Gaussian source-notes1503 and actual-Jensen reference
assessments for duplicates before external discovery. Do not substitute
a generic Favard existence result for a residual-cost estimate.
Reuse Schmeisser's assessed height comparison only under its hypotheses.

Continuation test: if sources already settle the required matching or
cost obstruction, import that result with its specialization. Otherwise
nominate one bounded finite/asymptotic test with adequate coverage before
invocation. Abandon this reference if no admissible matching exists for
all sufficiently large d or the retained cost has a positive d^2 floor.
A retained cost o(d^2) would only justify assessment of the omitted sum;
it would not establish the full statistic o(d), RH or root reality.

Inputs for future work are C028a's unchanged coefficients and strict
S_2,S_3 signs, C028c's source norm interface and finite-family contrast,
and C028b's downstream criterion. They are not a new dependency record.
Any future mathematical test must state all actual coefficient contracts
it needs. No mathematical work on this family was performed in1590.
The local searches do not certify novelty. Full matching Mathlib coverage
is unknown. Review1591 completed the source comparison in source-notes1591;
the new mathematical continuation is assessment1591, requiring separate
next-turn approval. No new mathematics is approved and derived together.
