# Conductor-eleven arithmetic and general-adapter replay

Approved target: Independently certify the arithmetic of model
[0,-1,1,-10,-20] and produce and completely replay its L038-relative-v1
dual-kernel certificate at conductor 11 with P={2}.
Prior SPECIALIZE coverage:
`drafts/literature/2026-10-10-conductor-eleven-general-adapter-replay.md`.

The main gap remains arbitrary-curve rank equality when complex order is
at least two. The intermediate target is a full-relative integration line
for this exact new adapter instance, potentially usable in L028/L036 after
independent q. L029 and L038 supply the structural and line inputs;
Cremona Sections 3.1--3.2/3.9 and BCDT Theorem A supply arithmetic sources.
This is known-algorithm reproduction, not a new BSD case or theorem.

Plan saved before production: compute every invariant, certify the only
discriminant prime and its valuation, exclude discriminant decreases by
12, use the multiplicative c4-unit exit, exclude rational CM, and count all
F2 affine pairs plus infinity. Produce fresh structural and dual evidence
under `scripts/conductor-eleven/`, using existing audited programs without
changing them. Replay all structural evidence and independent rank evidence.
Require d>=1, rank d-1, a nonzero full vector, and a nonzero (d-1)-minor.
Do not expand P. Failure calls for diagnosis; a larger kernel is inconclusive.

The duplicate/source search found no completed local exact-model object.
ATTEMPTS/023--024 preserve calibration-production stops; this independent
finite line test does not reopen uniform q. Generic executable provenance
stays SUPPLIED_CONDITIONAL. Independent q, normalized symbols, coefficient
and point witnesses, rational membership, divisible Sha and arbitrary
complex-order comparison remain unresolved. Completion will be recorded
below and in a canonical lemma; a separate critical audit remains required.

## Completed attempt

The independent arithmetic computation and applicability proof are in L039.
Delta=-11^5, v_11(Delta)=5<12, c4 mod 11=1, nonintegral j and all five
F2 points give exact conductor 11, minimality, non-CM and a2=-2. The
structural build produced s=12,r=9,d=3, torsion order one. Complete
general-adapter replay checked all 120 primitive assignments, 24 relations,
sixty paths/218 segments, 43/13 transform operations and their inverses,
every saturated descent and generator reconstruction. The dual matrix has
rank 2=d-1 and nullity one with v=(5/2,5,1); its independent 2-by-2 minor
has determinant two. All twelve functional values, 24 source and nine
saturated relations were checked. No failures occurred; P was unchanged.

Full certificates, conditional adapter input and fresh bound outer and
subordinate reports are under `scripts/conductor-eleven/`, as reproduced
in L039. Existing core programs and prior artifacts were preserved.
Selected complete small fields were inspected with the JSON inspector;
the complete checkers, not these displays, replayed all instance evidence.
This is a local ADVANCE in reproduction, with no beyond-source theorem.
The new assembly awaits separate critical audit. Its continuation is
`drafts/literature/2026-10-10-conductor-eleven-critical-audit.md`, with
REVIEW_REQUIRED; no new audit mathematics was approved in this turn.
