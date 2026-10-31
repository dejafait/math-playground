# Local-density replacement in the aggregate kernel: source comparison

TARGET: Review coverage for replacing L483's unit-shell supremum by L485's local second moment in B_{>=delta(T)}(T), uniformly for 1/log T<=delta(T)<=1/8, testing whether delta(T)log T tending to infinity suffices for little-o of T(log T)^3.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the joint-Blaschke searches/failure record and restricted source audit; added exact Proposition 2.5, local-density kernel and weighted-moment searches. No inspected direct theorem for this B sum or adequate weighted strengthening was identified. Queries, primary reads and narrow duplicate comparisons are recorded in drafts/2026-10-30-local-density-kernel-source-review-working.md; no novelty or absence claim.
SOURCE_EVIDENCE: Maples--Rodgers, IJNT 11 (2015), 2087--2107, arXiv:1404.3080v2 (4 June 2016), https://arxiv.org/html/1404.3080v2: Theorem 2.4/Proposition 2.5 p. 5, (8) p. 6, Corollary 4.2 and (18)--(23), pp. 9--12, with complete relevant proof coverage reused from the restricted audit and L485. Bui--Hall arXiv:2304.05178v1 (11 April 2023), https://arxiv.org/html/2304.05178v1, Section 1 definition of HARDY, Theorem 3 and Section 7 supply the existing continuous fourth-moment input at (0,0,0,0). Source arithmetic proofs remain citations; local kernel input is L483/C483a.
COMPARISON: Proposition 2.5 is precisely a known count-only local moment; use only L485's repaired k=2,c=1/4 specialization. L483/C483a instead use cumulative density and a shell supremum. The replacement needs bandwise count domination, strict-cutoff loosening, window enlargement or almost-everywhere endpoint handling, fixed-multiple base-height padding and finite L2 summation; these are now scoped specialization obligations, not missing arithmetic theorems. Neither the source nor its mesoscopic CLT supplies the |Z|^2-weighted conclusion.
GAP: Derive the uniform variable-kernel estimate and its actual cutoff, including every width, height, cutoff and band-summation loss, then compare with T(log T)^3. No estimate from this replacement, improvement over C483a, all-mesoscopic saving or sharp obstruction is proved in this literature-only step.
REASON: The previous audit excluded this kernel application. The new theorem comparison supplies adequate input coverage for one bounded known-tool specialization while leaving its mathematical success open; no reproof of source arithmetic or unrestricted weighted theorem is justified.
LITERATURE_REASON: L485's ready audit covered only a strict one-sided indicator count; variable widths, inclusive cutoffs and padded dyadic use changed the application hypotheses and required this separate comparison.
SCOPE: Inputs L018, L471, L483, C483a and L485; actual Xi, full multiplicities, one-copy pair quotients, coincident ordinates and clipped/singleton windows; every sufficiently large real T and 1/log T<=delta(T)<=1/8. Use only the restricted count moment, existing continuous fourth moment, nonnegative finite kernel, Cauchy--Schwarz and finite L2 triangle inequality. No RH, simplicity, spacing, favorable correlation, selected-value bound, general-weight (19)/Lemma 4.3 or external fixed-half-plane premise.
COVERED_TARGET: Test the L485 local-second-moment replacement in L483's aggregate kernel for B_{>=delta(T)}(T), uniformly for 1/log T<=delta(T)<=1/8, retaining every loss and deciding whether delta(T)log T tending to infinity suffices for little-o of T(log T)^3.

The mathematical target to preserve during review is a uniform bound
for the original restricted B sum after replacing the pointwise overlap
estimate by L485. L483 gives its exact kernel
k_d(u)=(d^2-u^2)/(u^2+d^2)^2 on |u|<=d, zero otherwise,
and B=integral |Z|^2 sum m_j k_(d_j). No new identity is asserted.
The approved later test is to retain the original sum while grouping
displacements into bands, match each necessary local count to the
strict one-sided source statement, and retain every width, height,
and summation loss before comparing with T(log T)^3. These operations
are a covered research target, not a completed derivation.

The primary/known-tool comparison supports attempting the application;
the research turn must supply the discriminating calculation of the
required cutoff. Stop this count-only certificate as a route to the stated
all-mesoscopic threshold if its proved estimate retains a nonvanishing
loss for admissible delta(T)log T tending to infinity; that would stop
the estimate, not disprove the actual-Xi mass claim. A weaker cutoff
may still be recorded honestly if it changes the research decision.

The previous aggregate recovery stop was procedural, and L475's
exponential Blaschke envelope remains a valid obstruction to that
different tool. Neither is erased or treated as a global ban. L485
is the concrete new input supporting this comparison. Reusing it does
not authorize general-weight source equation (19), a closed-endpoint
extension without justification, or a new zero-density theorem.

In the covered calculation, freeze T and delta before forming finite
dyadic displacement bands, including the truncated final band below
1/2. Compare each band to the strict right-side zero count by a lowered
cutoff in the source range; retain the resulting change in decay.
Handle closed ordinate endpoints by a strict enlargement or an explicit
almost-everywhere argument. Do not discard equality displacements,
coincident ordinates or repeated zeros. At any padded base height U,
the window parameter must satisfy h=H/log U and 1<=H<=U^(1/4),
with every shifted window start in [0,U]. Justify these uniformly over
all bands; any necessary enlargement carries a cost. No arbitrary
translation or fixed-H-only moment is licensed. Finite L2 summation
and the continuous fourth moment are the planned tools, not a
zero-conditioned amplitude theorem. The full obligation list and
source comparison are in the working note cited above.

Readiness authorizes an attempt at the displayed threshold and permits
a weaker bound or informative failure. A bound whose right side fails
to vanish for an admissible cutoff only defeats this certificate; it
does not lower-bound the actual mass or rule out every count-based
method. No optimized cutoff or mathematical result is approved here.

The plausible downstream use is a larger controlled sector of L471's
negative-mass majorant. Smaller displacements, zero-conditioned
amplitudes, full negative-mass saving and all-degree positivity remain
independent gaps. This routine known-tool application is not labeled
creative; a justified new central mechanism still needs a concrete
weighted-correlation input. Full matching Mathlib coverage is unchecked.
