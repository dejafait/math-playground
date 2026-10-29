# Double-gap endpoint cap — bounded symbolic continuation

TARGET: Attempt one symbolic integer-junction proof of T^j(n)<=n+1 for actual first-drop words 1^a0^2 1^c0^d with a,c,d>=1, retaining every prefix guard and a potentially partial final run.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact b=2 search and local failure comparison in 2026-10-29-two-peak-double-gap-endpoint-bound.md; no inspected matching theorem and no novelty claim.
SOURCE_EVIDENCE: https://math.colgate.edu/~integers/t8/t8.pdf#page=2 — Rozier2019 Lemma1/equation(4)/affine proof, printed pp.2–3, rechecked 2026-10-29, covers every finite word; https://arxiv.org/html/2502.00948v5 Remark5.5/AppendixA supplies only one-peak motivation; https://arxiv.org/html/2605.13886v1 Theorems2,4,7 supply finite-word or bounded-length comparisons, reused from the companion review.
COMPARISON: Primitive finite coding imports directly, but the uniform bound for the changed two-peak family is not a cited theorem. L110's b=1 integer-increment method is available for adaptation; its conclusion and C110a cannot be applied to b=2.
GAP: The requested endpoint cap, including all positive integer starts and unbounded run lengths satisfying the guards, remains to be proved or refuted. No b=2 identity or parameter reduction is established in this assessment.
REASON: A single established-route extension can test the coefficient-to-actual bridge beyond the unit gap without another source search; this nomination requires separate supervisor approval before execution.
SCOPE: Exactly one symbolic pass for middle even length2; no longer gaps, additional peaks, enumeration, closure premise or universal finite-drop assumption.

## Exact hypotheses and purpose

Use T(n)=n/2 when even and (3n+1)/2 when odd. Let n>1 be a
positive integer whose actual parity word before its first j steps is
1^a0^2 1^c0^d, with integers a,c,d>=1 and j=a+2+c+d.
If q_k counts ones in its first k bits, retain separately every condition
3^{q_k}>=2^k for 0<=k<j and 3^{a+c}<2^j. The finite first drop
is a hypothesis for this family, not a theorem for arbitrary starts.
Both odd runs and the intervening two even steps are exact. The terminal
d even steps may be partial, and the endpoint has no imposed parity.
No minimum, seed, closure, distinctness or primitive-period premise is added.

The main gap is universal eventual descent. The intermediate cap would
reduce this family's possible non-descent to equality or unit growth.
Eliminating those cases, other shapes and finite-drop existence remain
separate obligations; this turn approves no such corollary in advance.

## Inputs, proposed attempt and stopping test

The essential local exact-run input is L002. Import Rozier's finite
congruence/affine theorem at the cited location, using it on the observed
terminal run without claiming maximality. L110's integer-endpoint proof
is a method comparison only: adapt it to the two chronological odd-run
starts and retain the changed middle-run hypothesis explicitly. C110a
and the closed-cycle source are scope comparisons, not cap premises.
No finite-coding reproof or additional source is required within this scope.

Make one symbolic elimination pass under the full integer and prefix
conditions. Seek h=T^j(n)-n<=1, with both equality and growth retained.
Continue on a full proof, a useful proved subcase with exact residual
boundary, or a materially refined mechanism. An actual feasible word
with h>=2 rejects the cap; a witness to a relaxation rejects only that
relaxation. An unresolved sign supplies no negative theorem: preserve
the expression and stop the pass as EXPLORATION. Do not replace it by
larger finite searches. The shared two-unproductive-turn reassessment
rule applies, with earlier failure evidence retained.

This is established-route development, not a newly creative mechanism.
L109/Attempt036's false sorting inequality is not reused. No central
finite-drop mechanism is nominated without its own essential coverage.
Matching Mathlib coverage is not checked. This file contains a proposed
test and source coverage, not a new lemma, proof or mathematical result.

## Direct-source gate repair (2026-10-29)

Reopened [Olivier Rozier, *Parity sequences of the 3x+1 map on the
2-adic integers and Euclidean embedding*, INTEGERS 19 (2019), A8](https://math.colgate.edu/~integers/t8/t8.pdf#page=2).
The map in equation (1) is the shortcut T used here. Definition 1 uses
the first j input parities, with no constraint on the parity of T^j(n).
Section 2 permits rational integers; Lemma 1 covers any finite binary
sequence of positive length j, gives its starting congruence class
modulo 2^j in equation (4), and its proof on printed p.3 states the
affine iterate identity. Positive integer starts are a specialization
of that domain. Neither maximality of a final even run nor closure is
required. Thus the observed word in this target is covered, but its
prefix coefficient inequalities and the proposed endpoint cap remain
separate hypotheses and an unproved conclusion respectively. Import
the finite-word input without reproof.

The prior source comparison and local duplicate/failure assessment in
`2026-10-29-two-peak-double-gap-endpoint-bound.md` are reused unchanged.
The direct versioned comparison links now also appear in SOURCE_EVIDENCE;
those comparisons were not newly reread or extended in this repair.
No new mathematical result, lemma, script or Mathlib coverage claim is
made. The exact target and bounded stopping test above are unchanged.
