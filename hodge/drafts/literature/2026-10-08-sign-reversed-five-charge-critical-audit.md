# Sign-reversed five-charge exclusion — audit coverage

TARGET: Critically audit L072's sign-reversed five-charge slice exclusion, including every-fibre concentration and the full signed relative-GRR character.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped L072/L071, the prior application assessment, the fixed-pair and five-charge assessments, the L071 audit assessment, ATTEMPTS/039--040 and 050, and history/156; reused recorded exact-statement searches and Maciocia comparison rather than repeating discovery.
SOURCE_EVIDENCE: Inspected Stacks 0A1H statement and Noetherian proof case, 0BDH Lemma 36.31.3 statement and complete proof, 02UO smooth-proper statement, and 02UM character expansion on CHECKED; reused previously inspected Fulton second edition Theorem 15.2 and Example 15.2.8 and the approved Verbitsky/Huybrechts coverage.
COMPARISON: The general inputs cover an audit of the exact negative-mixed locally free rank-two slice; no cited theorem imports its numerical exclusion verbatim, and L055's positive-sign hypotheses cannot replace L071.
GAP: A separate mathematical audit must verify L072's application of every-fibre input, actual concentration, full rank-truncated character, pushforward signs and infinite integer domain; source approval does not certify those calculations.
REASON: Essential coverage is adequate for this unchanged critical-audit target; reuse known tools without reproof and classify the separate audit as REPRODUCTION.
LITERATURE_REASON: The newly saved audit target was REVIEW_REQUIRED; this turn compares its obligations with ready application coverage, rather than reopening discovery for a ready mathematical target.
SCOPE: L072 under L071's identical marked product and common real metric, full integral -tau_D, locally free rank-two product slope-polystability, c_1=0, a=-9 and every admitted integer b, with initially unrestricted higher characters.

## Gap, target and discriminating test

The main gap is universal primitive rational Hodge-class algebraicity.
This intermediate target is independent verification of the sign-reversed
five-charge bundle exclusion. A valid exclusion can direct future bundle
construction to larger charges; it supplies no algebraic cycle or transport.
Continue with one audit if the established local inputs and cited theorems
cover all hypotheses. Retain the slice stop only if the complete application
survives. A failure of every-fibre concentration or signed character requires
an explicit correction or narrower statement; a compatible subcase is not
existence. This turn approves that audit, without performing it.

## Primary coverage and applicability obligations

[Stacks Lemma 36.30.1, Tag 0A1H](https://stacks.math.columbia.edu/tag/0A1H)
requires finite presentation, a perfect object, and a bounded finitely
presented base-flat complex with proper support. It gives perfect derived
pushforward and arbitrary base change. Read its Noetherian proof case;
the approximation case is unnecessary on the projective complex base.
The audit must instantiate the perfect object as O_X and the complex as
F[0], after Serre's GAGA theorem (coherent equivalence and cohomology
comparison for projective complex varieties). Local freeness and smooth
projection are the pertinent flatness hypotheses. GAGA is a named standard
input, not a new lemma; irrational h is used for stability only.

[Stacks Lemma 36.31.3 in Tag 0BDH](https://stacks.math.columbia.edu/tag/0BDH)
requires a perfect complex. It characterizes its open degree-i/rank-r
concentration locus by derived pullbacks. The complete proof uses vanishing
of other fibre Betti numbers, a finite-free complex criterion and open rank
loci. The intended case is i=1,r=1. The audit must check every closed fibre
and the empty-complement argument on a finite-type complex base; generic
concentration, virtual rank or constant Euler characteristic do not suffice.
These statements cover the criterion, not L072's fibre calculation.

[Stacks Section 42.66, Tag 02UO](https://stacks.math.columbia.edu/tag/02UO)
states smooth-proper relative GRR for finite locally free input and finite
locally free higher direct images, retaining their alternating sum and the
relative tangent Todd class. Its general proof is deferred there. Reuse
Fulton, *Intersection Theory*, second edition (1998), Theorem 15.2,
pp. 286--287, and Example 15.2.8, pp. 291--292, previously inspected in the
[fixed-pair assessment](2026-10-05-minimum-pair-relative-cohomology.md).
Its proper morphism of nonsingular quasi-projective varieties case covers
the projection. The recorded [scan](https://djvu.online/file/87GFN2nbfbdF7)
host's 1997 label versus cited-edition 1998 qualification is retained;
no fresh book extraction was needed. Pass to rational cohomology through
the cycle-class map. Verify the relative, rather than ambient, Todd class,
and distinguish the actual positive image bundle from the alternating class.

[Stacks Section 42.45, Tag 02UM](https://stacks.math.columbia.edu/tag/02UM)
defines the character by Chern roots and displays terms through degree four.
Reuse Fulton Theorem 3.2(a), pp. 50--52 for finite-rank truncation. The audit
must apply these to actual ranks two and one, retaining the full mixed square,
not setting the fourth character to zero or retaining a former virtual class.
Factor degrees and the integral congruence domain are local calculations,
not additional source gaps. A vanishing rational first character suffices
for the line identity; integral triviality or image stability is unnecessary.

## Local inputs, overlap and limits

L071, not L055, supplies changed-sign every-fibre polystability and forced
higher characters. Its prior audit coverage inspected Verbitsky,
arXiv:math/0107182v10, Definition 2.1 p. 9, Theorem 3.9 pp. 13--14,
Proposition 3.7/Lemma 3.8 p. 13, and reused Huybrechts, *Lectures on K3
Surfaces*, author-hosted draft, Chapter 9 Theorem 4.9 p. 182, Section 3.1
pp. 175--176, and Chapter 1 (2.5)--(2.6)/Proposition 2.4 pp. 11--13.
See the [application assessment](2026-10-08-sign-reversed-five-charge-direct-image.md)
and [L071 audit coverage](2026-10-08-sign-reversed-necessity-critical-audit.md).
No new restriction theorem or stability of the opposite factor is required.
Check L072's use of these already local inputs; a defect in their necessary
bridge must be reported, not bypassed by ordinary restriction stability.

The recorded Maciocia theorem comparison concerns equivalence kernels under
extra determinant/line-subsheaf or presentation hypotheses, and does not
classify this arbitrary product-polystable F. Its precise statements and
queries remain in the application assessment; they were not freshly read.
No new external discovery query was necessary. Unread leads remain unread;
absence of a matching search result is no novelty evidence.

ATTEMPTS/039--040 preserve positive-tensor failures; ATTEMPTS/050 and L072
record the changed-sign calculation pending audit. The present review does
not duplicate that calculation or reopen L070 or the charge-seven stop.
Essential continuation inputs: L072 and L071; L055 is method comparison,
with L044/L048/L052 inherited through L071. No cross-notebook input,
L060/L067, transform equivalence or image stability is proposed. F existence,
larger-charge gluing, other representatives and transverse transport remain
unresolved. Mathlib full matching and supporting coverage is not checked;
no absence claim is made.

## Outcome

One LITERATURE / EXPLORATION / NOVELTY_UNCHECKED coverage review makes the
exact TARGET SPECIALIZE for a separate REPRODUCTION proof audit. It establishes
no new mathematics and no independent correctness verdict for L072. Mathematical
exploration usage is zero. Canonical proofs, DAG and PROOF remain unchanged.
