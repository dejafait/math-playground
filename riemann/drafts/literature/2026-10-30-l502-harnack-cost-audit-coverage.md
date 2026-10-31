# L502 Harnack detector-cost audit: approved reusable coverage

TARGET: Critically audit L502's support-independent Harnack lower bound, including Fourier integrability, strict rectangle geometry, uniform constant and the claimed detector-class stop.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact-class search and primary-source comparison in drafts/literature/2026-10-30-positive-analytic-window-majorant-feasibility.md and the pre-existing quantitative scope in drafts/literature/2026-10-30-positive-strip-harnack-bound-test.md; this target checks the resulting specialization without changing its assumptions or seeking another theorem.
SOURCE_EVIDENCE: Axler--Bourdon--Ramey, Harmonic Function Theory, second edition, author PDF dated 17 July 2020, Theorem 3.4 and (3.5), printed pp. 47--48 (PDF pages 54--55), https://axler.net/HFT.pdf#page=54; theorem, complete proof and translated/dilated statement independently retrieved during this approval. L502 remains unaudited.
COMPARISON: The source supplies only the disk value-ratio inequality. The audit must check each elementary geometric, integrability and kernel step connecting it to L502's integral lower bound; neither the source nor this assessment certifies that connection.
GAP: Independently replay weak positivity, the selected point's strict cutoffs, common log T>=32pi onset, Fourier integration by parts, nonnegative restriction of the integral and c_*=1/(128pi); check that the conclusion stops only the stated class.
REASON: This is a finite ordinary hypothesis/arithmetic audit of an already covered standard-source specialization, not a new analytic or arithmetic mechanism. It verifies a useful route decision without repeating the stopped construction.
SCOPE: Exactly L502 and its stated class at delta=log log T/log T; no moving-test arithmetic transfer, actual-zero positivity, signed-detector construction or extension to other scales.

## Separate approval completed: 2026-10-30

The required separate literature turn approves source coverage for the
unchanged TARGET. This approves undertaking the audit, not L502's proof.
LITERATURE_REASON: the supplied literature gate requires separate approval
of the newly nominated audit assessment; the research target and its
assumptions have not changed. No further theorem search is needed.

The primary PDF's Theorem 3.4 concerns positive harmonic functions on an
open unit ball in dimension n. Its proof first uses the Poisson formula
on the closed-ball case, then dilation and a limit for the open case.
Equation (3.5) states the translated and scaled form. The audit uses n=2;
neither boundary data nor a global upper bound is an extra hypothesis.
The source is imported; repeating its proof is unnecessary. Weak
positivity is an application issue to check in L502, not a new theorem
being approved here.

The parent exact-class search and real-axis extremal comparison were
reused, including its distinction from the fixed-support real-axis
result of Carneiro--Chandee--Littmann--Milinovich. No claim of novelty or
exhaustive literature coverage follows. The quantitative test assessment
and ATTEMPTS/2026-10-30-positive-strip-analytic-detector-stop.md were
checked for scope: they record this same necessary-bound mechanism.
L500/L501's distinct correlation stops do not duplicate its premises.

L502 was read solely to match audit obligations to available coverage.
Its compact smooth Fourier representation is explicit; integration by
parts, strict rectangle/disk inclusions, weak-positivity limit, kernel
restriction, common onset and numerical constant remain replay tasks.
They require no additional specialized theorem. No inequality in that
chain, or incompatibility conclusion, is independently certified by
this source review. No lemma or mathematical script was changed.

## Bounded audit

The sole result under test is L502. Its proof has no local lemma inputs.
L018 is needed only if a later arithmetic application interprets zero
coordinates; L500/L501 motivate the route and are not audit premises.
No RH, simplicity, spacing, external half-plane bound, selected-amplitude
moment or uniform moving-test asymptotic is assumed. Mathlib remains
unchecked; the mathematical audit does not depend on a formal analogue.

Pass only if the cited Harnack hypotheses, all pointwise inequalities,
absolute convergence and the incompatible scales hold with the stated
quantifiers and common constant. Otherwise identify and repair the exact
failure, preserving the original reasoning and narrowing the route stop
if necessary. Passing certifies only this elementary obstruction, leaving
the main all-degree-positivity gap and weighted-count target unresolved.
