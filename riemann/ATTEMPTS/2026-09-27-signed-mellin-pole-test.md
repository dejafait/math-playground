# Signed Mellin correlation: Möbius pole test — 2026-09-27

The approved target was D_N^w=o(1) at the prescribed moving pairs,
with the signed coefficients retained inside the Mellin–Euler integrals.
The [prior assessment](../drafts/literature/2026-09-27-signed-mellin-sampling.md)
was EXPLORE and explicitly proposed testing whether the nonconstant
ratio terms acquire a useful Möbius zero at the relevant boundary.
The potential downstream use was average endpoint control; exceptional
indices, the pointwise margin and the lower Laguerre signs would remain.

This is distinct from the earlier frequencywise derivative, separated
norm and grid-transfer tests. It uses two Mellin variables and the same
sample index, retaining all ratio collisions and moving parameters.
The Li–Radziwiłł arithmetic-progression theorem is a reviewed motivation,
not an applicable sampling estimate and not a theorem being reproved.

Result: **NEGATIVE; RESEARCH; REPRODUCTION**.
[L353](../lemmas/L353-signed-mellin-correlation-pole-survives.md)
proves that every fixed nonconstant rational frequency retains a
fourth-order pole on the joint diagonal boundary. Its leading coefficient
stays strictly positive as the moving normalization tends to one. The
two centering terms have only first-order poles. The exact sampled
identity and uniform contour tails are also justified; no o(1) sampled
bound is established. The constant frequency remains O(1/N), while the
available complete absolute budget is O(1), against the required o(1).

## WHY IT FAILS

In this correlation the local generating function has the numerator
(1−p^(-sigma)X)^2. At the joint boundary its nonconstant ratio factors
are strictly positive, so the Möbius numerator does not remove the
fourth-order pole. The lower-order centering terms cannot remove it
either. The full proof is L353. This rules out automatic local pole
annihilation; a pole in a continued coefficient is not a lower bound
for a kernel integral or for the actual sampled mean. It also does not
license shifting the infinite Fourier sum to that boundary.

The completed test used one source turn and one research turn. Its
new evidence changes the mechanism decision, so there are zero
consecutive unresolved exploration turns. No global stop on signed
sampling is asserted. The proposed different direction reviews actual
zero compensation for the first Laguerre sign at unbounded heights,
where neither this sampling test nor generic finite-level positivity
supplies the needed input. That target is unscreened and requires a
literature-only turn; its exact action is held only in PROGRESS.md and
its matching assessment.

The [saved work](../drafts/2026-09-27-signed-mellin-residue-test.md)
preserves the initial reasoning and its completion. The local factors
pass 90 independent exact rational-residue checks and three signed
two-prime grouping checks. Infinite convergence and boundary uniformity
are proved analytically. This is a local reproduction of standard
Euler-product methods, with no novelty claim, sign extension or RH
candidate. All earlier unfinished work is preserved.
