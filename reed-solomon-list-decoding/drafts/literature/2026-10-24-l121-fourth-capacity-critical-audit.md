# L121 fixed-triple capacity — proposed critical review

TARGET: Critically audit L121's fixed-triple fourth-order Boolean/cardinality capacity pass and its complete exact certificates.
CHECKED: 2026-10-24
DECISION: REVIEW_REQUIRED
SEARCH_EVIDENCE: The completed step reused the prior fixed-triple SPECIALIZE assessment and its duplicate/failure comparison; no separate audit-target comparison has been completed.
SOURCE_EVIDENCE: Prior inspected coverage is foundations/15, Laurent CWI PNA-R0108 Section 3.1 (11)–(12), Lemma 2(ii) pp.5–6, and Raghavendra–Tan arXiv:1110.1064v1 Section 3 pp.7–9, reused from drafts/literature/2026-10-24-fixed-triple-fourth-cardinality-capacity.md; audit applicability remains to be assessed.
COMPARISON: Known inversion and homogeneous cardinality support the completed specialization; an independent constructor-free exact check is complete, while a dedicated critical proof audit is a separate target.
GAP: Review must compare all sixteen atom signs, raw empty normalization, the attainable inner-capacity direction, repetitions, exhaustive multiplicities and the single-row construction against their exact hypotheses.
REASON: This is a newly proposed continuation, not approval of uncovered audit work during the calculation turn; obtain separate literature approval before a proof audit.

## Proposed audit scope and limits

The exact proposed target is the TARGET above. Essential inputs are
L021,L098,L112,L113,L114,L121 and foundations/12,13,15. Inspect the complete
constructor and independent verifier, with their full factored occupancy
certificate and regular verification report. Use the unchanged root,
pairs,N,H,rho and original endpoints. Confirm that the lower bound on
the *actual* upper capacity, rather than an outer upper bound, licenses
the common-factor construction.

No new triple, refinement, alternative assignment, PSD claim or global
fourth-order solve is proposed. The exact-N condition is required only
at L112's enclosed root when combined with lower-order contractions;
the scalar local interval pass holds throughout the box. Full/excluded
PSD, other triple-conditioned rows, shared fourth moments, representing
measures, packing, RS realization and 67/68 safety remain open.

Primary direct URLs for reuse are
[Laurent CWI report](https://ir.cwi.nl/pub/4319/04319D.pdf) and
[Raghavendra–Tan v1](https://arxiv.org/pdf/1110.1064v1).
No new browsing or source import occurred in the completed research
turn. This proposed audit must receive a separate gate decision.
