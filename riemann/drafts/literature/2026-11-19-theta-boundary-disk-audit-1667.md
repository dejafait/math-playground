# C828b boundary-disk specialization: approved audit coverage

TARGET: Audit C828b's boundary-disk obstruction, checking the reconstruction factors, whole-disk holomorphy, connected-overlap uniqueness and theta-coordinate agreement against the cited natural-boundary theorem.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Approval1668 reused assessment1665 and source notes1666, read C828b and C828a Section1, stop1667 and history1667, and reopened the exact DLMF and Teschl primary passages below. No new broad search or changed target; the existing duplicate/failure comparison remains applicable.
SOURCE_EVIDENCE: NIST DLMF version1.2.8, 20.1, 20.2.3 and 20.2(ii), https://dlmf.nist.gov/20.2#ii ; Teschl, Ordinary Differential Equations and Dynamical Systems, author April2012 preliminary edition, Section4.1 pp111-114 Theorem4.1/(4.7)-(4.9), Section4.2 p116, https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf . Exact inspected hypotheses and source limits remain in notes1666; step1667 directly rechecked the DLMF natural-boundary statement and convention during application.
COMPARISON: C828b supplies the previously missing transfer proof using the identical Phi=P of C828a and an explicit constant-coefficient Green formula. The audit should check that formula and its local coordinate, rather than reprove theta's natural boundary or infer all-disk continuation from a local IVP theorem.
GAP: Source coverage is approved in separate literature step1668; the mathematical audit remains unperformed. Check C828b equations(3)-(5), both interior initial values, full disk, connected overlap and coordinate orientation. No signed actual-Xi bridge, saddle estimate, contour deformation or RH conclusion follows.
REASON: Separate source approval1668 is complete for the unchanged TARGET. Essential hypotheses and source limits are accessible and covered; proceed to the mathematical audit next turn without another source-approval loop. This approves coverage, not correctness of C828b.
SCOPE: Only the exact TARGET above. Reuse C828b, C828a Proof Section1 (especially (5)), assessment1665 and notes1666. Do not load unrelated moment or Bernstein proofs. No new mechanism or source-discovery claim is licensed.

The main gap remains L030-L032/C032a actual-Xi all-degree positivity.
This audit concerns the reliability of an informative negative result,
not another attempt to establish the failed crossing prerequisite.
The decisive test is whether the alleged Phi extension yields, on an
open disk about tau0=-exp(2R), a holomorphic function equal to
theta3(0|tau) on its upper half. Check the factors 2 and 4, both
interior initial conditions, the connected lower half-disk, the logarithm
branch near1, its side orientation and the arbitrary-real-R quantifier.
A genuine error must be repaired or the obstruction downgraded; a sound
audit leaves this route stopped. It supplies no new mathematical discovery.

Duplicate comparison: the narrowly inspected TARGET/COMPARISON/GAP of
2026-10-31-associated-theta-boundary-growth-test concern a radial
divergence of the first associated correlation, with no boundary trace
or continuation theorem. It is a different object and is not an input.
C828a's single-cusp result is preserved; the broader theta boundary
theorem is imported, not claimed as a new result. No cross-notebook
input; full matching Mathlib coverage remains unchecked.

## Separate literature approval1668 — 19 November 2026

LITERATURE_REASON: The supervisor explicitly requires separate approval
of the newly written assessment1667 before its mathematical audit.
Coverage was reused rather than a new target discovered. This approval
is STALLED in mathematical-outcome terms: no new theorem, obstruction
or source conclusion is claimed, and no exploration budget is renewed.

Directly reopened [DLMF20.1](https://dlmf.nist.gov/20.1),
[20.2.3 and 20.2(ii)](https://dlmf.nist.gov/20.2#ii).
The fixed-argument statement explicitly includes theta3; zero argument
has no excluded denominator. The parameter convention and natural-boundary
domain match the cited theorem. This is a handbook import; the books
cited by DLMF were not independently read. The historical version label
above is retained from notes1666; this approval checked the served
statements, not an archived-version comparison.

Reopened Teschl Section4.1, printed pp112-114: the integral formulation
(4.7), disk path independence via Cauchy's theorem, Theorem4.1 with its
analytic bounded right-hand side on a rectangle and radius
min(epsilon,delta/M), and the connected-component uniqueness passage
with its logarithm counterexample to a unique maximal domain. Theorem4.1
is local and is not a full-disk extension theorem. Those limitations
are essential audit checks, not missing source coverage. Earlier
notes1666's Section4.2 reading remains available; no singular-equation
result or general maximal-continuation theorem is required.

The assessment remains SPECIALIZE: the imported natural boundary does
not directly state a theorem for Phi. C828a(5) is an existing local
identity; C828b's reconstruction and coordinate argument still require
mathematical replay. No formula was differentiated or new implication
proved in this literature turn. Future audit classification is
REPRODUCTION. A repair outside this exact scope requires fresh coverage.
Mathlib full matching coverage remains unchecked. The earlier single-cusp
and associated-correlation comparisons remain contrasts, not extra inputs.
