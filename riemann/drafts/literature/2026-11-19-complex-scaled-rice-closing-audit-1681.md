# Weighted finite Rice obstruction: audit coverage1681, approved1682

TARGET: Critically audit C048q's finite normalization and limit log A_d(i)/(d/log d)->pi/2, including the uniform actual-integrand lower bound on the top subarc c<=Re(s)<=c+1/log d and the upper bound on all three closing sides.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact weighted-target discovery and duplicate/failure comparison in assessment1679/source-notes1680; the actual I, principal multiplier, rectangle and degree limit are unchanged. No new search or novelty claim.
SOURCE_EVIDENCE: Reuse Flajolet--Sedgewick1995 Section2 Lemma1/(6), pp104--105, https://algo.inria.fr/flajolet/Publications/FlSe95.pdf ; DLMF4.2.3/19/27--29 https://dlmf.nist.gov/4.2 ; full-argument gamma coverage DLMF5.11.1/5.11(ii) https://dlmf.nist.gov/5.11 ; exact inspected statements and qualifications remain in source-notes1680 and reused notes1660/1676.
COMPARISON: The finite Rice and principal-power inputs are known, and C048l supplies the actual uniform main term and corner scale; C048q specializes these to the previously assessed weighted target. Audit the new lower-bound transfer and integration without redoing discovery or claiming new source mathematics.
GAP: Source coverage is sufficient; the mathematical audit remains undone: residue parity and principal sign, absolute derivative bound for explicit G_d only, uniform two-sided actual-I error, shrinking subarc length, full-union upper bound and common onset.
REASON: Separate literature-only approval1682 accepts this unchanged SPECIALIZE scope for one REPRODUCTION conceptual audit. Reuse the inspected primary-source records; no essential unread theorem or changed hypothesis requires further discovery. This approves coverage, not C048q's correctness.

LITERATURE_REASON: The supervisor requires separate approval of the newly written audit continuation. This turn compares its exact scope with retained primary-source evidence1680/1660/1676; no additional browsing or new mathematical target is needed.

SCOPE: Exact TARGET only, under C048k/C048l input contracts, integers d>=3, principal Log(-i/d), c=-1/4, b=d+1/2, h=d/log d. Excludes a fresh saddle mechanism, a different contour, other arguments, parameter neighborhoods, signed cancellation, compact zero mass and Xi signs.

## Review obligations

The canonical proof is
[C048q](../../lemmas/C048q-complex-scaled-rice-absolute-closing-obstruction.md).
Its direct inputs are the exact entire/sample normalization in C048k
and C048l's uniform (7)--(13), corner (21), and unweighted bound.
Recheck the actual two-sided transfer; an upper envelope or a large
point value would not establish the obstruction. Verify the derivative
bound on explicit G_d, with no differentiated asymptotic error, before
integrating over width 1/log d. Then check that (3)'s multiplier bound
holds on the entire closing union, including both horizontal signs.

Passing this audit would validate a local absolute-budget stop only.
It would not estimate the signed closing sum, prove U_d(i)!=0 or pay
H_d=o(d), S_F=0, compact nonreal-zero mass or RH. Full matching
Mathlib coverage is unchecked. This nomination performs no audit and
imports no new mathematical result. Reuse coverage unless a concrete
hypothesis defect emerges; no further browsing is presently essential.

## Separate source-scope approval1682

19 November2026. Reused the full primary-statement and proof-case
records in [notes1680](2026-11-19-complex-scaled-rice-closing-source-notes-1680.md),
[notes1660](2026-11-19-degree-coupled-rice-source-notes-1660.md)
and [notes1676](2026-11-19-upper-finite-rice-tail-source-notes-1676.md).
Read C048q's hypotheses, conclusion and imported-input passage, and
C048k's normalization and C048l's uniform-domain/main-term contracts
to compare source scope only. No proof audit was performed.

Flajolet--Sedgewick Section2 Lemma1/(6) is the finite analytic-contour
template; the polynomial-growth conditions for infinite opening and
Section4 Theorem2's two proof cases are not required here. The fixed
nonzero base at each degree makes DLMF4.2's principal-power definition
the relevant input; it does not supply a uniform weighted edge bound.
The gamma input behind C048l uses full arguments in the right
half-plane, covered by DLMF5.11.1/5.11(ii); fixed-shift ratio and
bounded-real-part formulas are not substitutes. Recorded versions,
pagination, unread leads and PDF legibility qualifications remain
those of the cited ledgers. No fresh external passage was retrieved.

The existing actual-I value comparison and explicit G_d identities
are local mathematical contracts, not conclusions of the Rice paper.
Their use in the shrinking-subarc lower transfer is exactly the
remaining audit obligation. Neither a point value nor an upper
envelope suffices. The whole closing union and common onset must
also be checked. These obligations fit the original source scope;
no derivative of an asymptotic error or new uniform theorem is
authorized. C048o/p's vertical tails do not duplicate this target;
the scoped discovery and failure comparison in notes1680 is reused.

SPECIALIZE is retained: one later mathematical audit may check this
routine local specialization without reproving the cited theorems.
The source gate is approved; C048q remains unaudited. This procedural
approval supplies no new mathematical evidence and is recorded
STALLED, not as a discovery or a fresh negative result. The full
matching Mathlib theorem remains unchecked. No lemma, mathematical
script, DAG or PROOF edit is part of this literature-only step.
