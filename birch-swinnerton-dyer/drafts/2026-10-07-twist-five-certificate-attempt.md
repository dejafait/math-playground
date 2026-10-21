# Independent twist-five certificate — working record

2026-10-07, BSD-2026-10-07-076. Ready SPECIALIZE assessment:
`drafts/literature/2026-10-07-twist-five-certificate-specialization.md`.
This is one bounded research attempt, reproducing a known algorithm.

Main gap: rank equality for arbitrary analytic order at least two.
Intermediate target: independently certify the total-period ratio q for
the twist by 5 of the fixed conductor-389 curve. A nonzero value could
feed L028's calibration; C, b, the remaining L026 premises, rational
membership and the complex-order comparison remain unresolved.

Inputs read: L030 minimal arithmetic (including the exact arithmetic
certificate), L028 oriented twist and total-period conventions, the ready
assessment and its full source comparison; ATTEMPTS/022--023 retain their
stops on repeated conditional audits without input production.
No unnormalized L030 functional value enters this calculation.

Attempt sequence: import the exact optimal-model/torsion identification,
derive the base-cusp denominator bound with the total-period factors,
determine the Fricke case exactly, then enclose the independent analytic
series and positive-root AGM period using rational outward arithmetic.
At most three precision refinements; require explicit existence and
uniqueness of a denominator-bounded rational, not a width test alone.
Exact zero stops this calibration twist; inconclusive isolation preserves
the certificate and failure. No value is asserted in this working note.

## Completed attempt

The reasoning above was saved before implementation and is preserved.
The completed step is BSD-2026-10-07-076-twist-five-independent-certificate.
[L031](../lemmas/L031-independent-twist-five-ratio-certificate.md) contains
the full proof and primary citations; `scripts/twist-five/certificate.json`
contains every arithmetic interval and finite witness. The independent
complete replay in `scripts/twist-five/verification.json` passes with
no failures. The first evaluation, D=2^48 and T=256, isolates q=4
under the proved B=2 bound, with full ratio width
633706963/281474976710656<1/4. No refinement was needed.

Local outcome ADVANCE is known-algorithm reproduction: an actual
independent calibration input is now available for this fixed curve.
No beyond-source discovery or BSD candidate is claimed. The new
critical-review continuation is REVIEW_REQUIRED, with separate approval
deferred to the next turn; current routing is only in PROGRESS.md.
