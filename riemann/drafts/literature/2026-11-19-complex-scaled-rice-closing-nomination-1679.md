# Complex scaled Jensen argument: closing-test assessment1679/1680

TARGET: Determine whether, with C048l's c=-1/4, b=d+1/2, h=d/log d and rectangle R_d, the absolute closing contribution A_d(i)=(1/(2pi))*integral_(top,right,bottom of R_d)|F_d^I(s)*exp(s*Log(-i/d))| |ds| tends to zero as integer d tends to infinity.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: New bounded exact-target discovery and scoped duplicate/failure comparison completed in source-notes1680; seven queries found standard Rice tools and different families, with no matching bound identified. No absence or originality claim; reuse notes1656/1660/1676 and approval1677.
SOURCE_EVIDENCE: Flajolet--Sedgewick1995 Section2 Lemma1/(6), pp104--105, Section4 Thm2/both proof cases pp110--111, https://algo.inria.fr/flajolet/Publications/FlSe95.pdf ; DLMF4.2.3/19/27--29 https://dlmf.nist.gov/4.2 ; reused full-argument tools DLMF5.11.1/5.11(ii)/(iii), https://dlmf.nist.gov/5.11 . Exact statements, versions and inspected passages are in source-notes1680.
COMPARISON: Finite Rice covers analytic coefficient functions separately at each degree, and DLMF gives the exact principal-power modulus identity. Neither supplies degree-uniform closing control. C048l's unweighted bound/conjugation and C048o/p's vertical tails do not settle the changed multiplier; no inspected result duplicates this target.
GAP: In a later mathematical turn check the weighted integer samples, residue normalization/orientation for U_d(i), then establish all three actual closing-side costs or a decisive actual-subarc lower bound. Retain the full multiplier, uniform actual-I transfer and both horizontal sides; no such estimate is derived in review1680.
REASON: Essential complex-power source scope is now covered for one bounded REPRODUCTION specialization. This newly completed assessment needs the supervisor's separate next-turn approval before the mathematical test; no further source discovery is presently essential.

LITERATURE_REASON: The proposed argument changes from x=-1 to x=i/d, adding a degree-dependent complex power to the Rice integrand; this lies outside the unchanged ready assessment1675. Reuse its basic calculus and gamma coverage, and compare only the newly relevant weighted finite-contour hypotheses and known obstructions.
SCOPE: Exact TARGET only: integers d>=3, actual I and F_d^I=E B_d, Z=gamma_0, principal Log(-i/d), C048l's finite rectangle and three closing sides; finite normalization and a rigorous subarc obstruction are included. Excludes infinite opening, saddle relocation, theta-boundary crossing, other arguments, parameter neighborhoods and Xi signs. Ready source coverage written1680; separate approval remains due.

## Completed review1680

Full source comparison, query record, local applicability obligations,
retained failures and qualifications are in
[source-notes1680](2026-11-19-complex-scaled-rice-closing-source-notes-1680.md).
The original nomination below is preserved as history; its statements
that discovery is undone are superseded by the completed fields above.
No weighted mathematical conclusion is asserted. Full matching
Mathlib coverage remains unchecked. After separate approval, citation
of the known tools suffices; reproof of finite Rice is unnecessary.

## Original nomination1679 (preserved)

## Relevance and the discriminating test

The main gap is L030--L032/C032a actual-Xi positivity. C028b/g identify
the unpaid H_d=o(d), equivalently vanishing full reciprocal-zero mass
S_F, in the actual unshifted scaled Jensen family. Audit1679 accepts
C048p, but that result remains confined to J_d(-1). Read only the
normalizations and relevant conclusions of C028b/g and C048k/l to
nominate this continuation; no new bridge is proved in this turn.

The proposed multiplier is intended to represent U_d(i) by the same
finite Rice template. Its residue normalization is an explicit future
applicability obligation, not an identity established by this nomination.
Testing just w=i is deliberately limited: it can decide whether this
particular rectangle pays even one nonreal scaled argument. Success
would justify considering a separately assessed parameter neighborhood;
it would not prove a zero-free neighborhood or S_F=0. Failure would
stop this rectangle and absolute-budget mechanism for that extension,
while leaving other contours and signed mechanisms available.

Continue to a mathematical test only after the source review covers
the exact multiplier and finite-contour hypotheses. In that test,
either prove A_d(i)->0 on all three closing sides, or obtain a rigorous
lower bound on an actual edge subarc that rules out this limit. A
single endpoint value, principal-term calculation without actual-I
transfer, or upper bound that merely fails to tend to zero does not
settle the target. If neither direction is proved, retain the missing
edge estimate without claiming an obstruction.

Essential local inputs are C048a/j's actual branches and value
estimate, C048k's finite interpolation/normalization and C048l's
rectangle. C048p is relevant evidence for the unweighted vertical
segment, not a theorem about the multiplied integrand. C028b/g supply
the intended scaled-family meaning and remaining gap only. Reuse the
recorded fixed-degree infinite-opening, stationary-sector and
theta-boundary stops; this finite weighted target performs none of
those operations. A source review must also search for already known
complex-argument Rice closing results and local duplicates before
authorizing work. No theorem absence or novelty is inferred here.

This is a proposed prerequisite test, not a protected creative attempt.
The central-mechanism blocker remains a sufficient compact nonreal-zero
mass bridge; the immediate source blocker is the uncovered complex
multiplier. Do not label a routine weighted-contour specialization
creative to satisfy scheduling. No mathematical result, new lemma or
script is contained in this nomination. Mathlib coverage of the full
target is unchecked.
