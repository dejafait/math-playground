# Capped signed support review1759, completed1760

TARGET: Assess the exact support function of the full signed mass-one TV<=2 class on [1,2] for continuous real Laplace payoffs, retaining atoms and singular parts.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1760 searched signed-measure support, oscillation, mass and variation terminology; the six exact queries and narrow duplicate/stop comparison are in drafts/literature/2026-11-19-capped-signed-support-source-notes-1760.md. No inspected exact matching formula was located; no novelty inference follows.
SOURCE_EVIDENCE: Bass2011 Theorem12.8, complete proof and(12.1), p97; Buhler-Salamon2016 Example1.3.7, p28; Chizat2022 AppendixA PropositionA.1 and proof. Exact links, primary scope, inspected cases and reused C032q integration coverage are in source-notes1760. The probability-distance mismatch1752 is retained.
COMPARISON: General Jordan and variation results cover arbitrary signed Borel inputs, including atoms and singular parts. Chizat treats penalized optimization, not this joint hard cap and mass constraint; C033l/m/n do not evaluate its support value. Thus import the general tools and specialize only the missing joint-constraint calculation.
GAP: The exact upper bound and admissible attainment remain unproved, including constant payoffs and nonsaturated caps. No numerical extrema, effective separator data, runtime or actual-Xi signs follow from the source coverage.
REASON: Essential measure-class coverage is now available for a bounded routine specialization. No new lemma or support identity was derived in this literature turn; the follow-on in assessment1760 requires separate approval.
SCOPE: W=[1,2]; eta finite real signed Borel, eta(W)=1 and |eta|(W)<=2; f(sigma)=sum_j b_j*exp(-B_sigma(q_j)) with finite real b_j and q_j>0 under C033l/C032q's unchanged qualifications. The question concerns the support value for a given continuous real f, not computation of its extrema or construction of separator data.

Review1760 inspected the primary statements and essential proof cases
listed in source-notes1760. The general Jordan theorem has no density
or finite-support restriction. The local joint-constraint calculation
still requires a separate mathematical attempt; none is derived here.
Source-notes1752's probability-distance mismatch remains. No access
retry of the parked general computable-maximum source was needed.

Downstream use: a valid exact reduction could identify what continuum
extrema a certified C033n separator evaluation would actually need. It
does not itself certify those extrema or a positive numerical gap.
Continue after separate approval of assessment1760, requiring a bound
for every allowed signed input and matching admissible attainment,
with constant payoffs checked. Required local inputs are C032q and
C033l/n; C033m is downstream
context only. All actual-zero, heat, fixed-v1 and half-variance assumptions
remain conditional, including C033l's inherited C033i/j/C032s inputs.
Full matching Mathlib coverage is unknown.

No independent signed-height/theta input for a justified central creative
attempt emerged within the present audit scope. This nomination addresses
an explicit remaining finite-interface gap and is not labeled creative.
