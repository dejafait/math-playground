# Source comparison: retained-plus finite local condition

TARGET: Assess whether global Tate reciprocity forces L123's descended outer-plus coefficient to be finite at p, using a nonzero rational Kummer localization and explicitly verified local conditions away from p.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 540 checked the named local plectic assessments, L123/L005, foundations/10 and ATTEMPTS/058, then searched global reciprocity, Tate/Kummer orthogonality and away-p elliptic cohomology; exact queries and inspected ranges are in drafts/source-notes/2026-10-28-retained-plus-reciprocity-coverage.md.
SOURCE_EVIDENCE: Inspected Rubin's 1999 Euler systems manuscript I.7.3 with complete proof and its local/limit prerequisites; Rubin's Euler systems and modular elliptic curves Sections 1/5; Darmon--Fornea's published Mock plectic points Definition 3.7 and Theorem 3.9 sketch; Fornea 2603.28327v2 Section 1.2 and global construction/descent passages. Precise URLs, versions and coverage are in the source note.
COMPARISON: Standard duality covers the proposed conditional mechanism; the published away-p Kummer identification removes the need for a new CM ramification theorem once the rational coefficient is globally lifted to a Tate-module class. No inspected theorem makes this actual coefficient finite without the missing nonzero rational localization.
GAP: Specialize Q-descent, rationalization and the integral limit/local-condition conventions for the actual coefficient; retain a nonzero rational Kummer localization spanning the finite local line as an explicit unproved input, not a consequence of analytic order two.
REASON: Essential source coverage is now available for a conditional known-method application; no new criterion or actual-class Selmer assertion is derived during this literature-only turn.
LITERATURE_REASON: Changed target from integral tower control to global duality and local Selmer membership; exact duality and away-p source hypotheses are essential unread inputs.

This assessment completes the saved source-review target in step 540.
It approves only a conditional specialization, with details in
[the coverage note](../source-notes/2026-10-28-retained-plus-reciprocity-coverage.md).
It does not accept an application or prove the proposed implication.

Retain L123's A/Q, imaginary quadratic K, inert split-multiplicative
p>=5, conductor/residual/integral-CM/incoherence hypotheses, full CM
list, actual coefficient integration, localization and descent. The
class under consideration is the global coefficient in L123 (5)
before localization at p, with its outer-plus descent to Q justified
explicitly; its local image restricts to R. Do not replace it by a
raw measure value or by L128's uncertified scalar formula.

The comparison identifies standard local/global duality and an explicit
away-p statement for integral global Tate-module classes. Their transfer
to the actual rational coefficient remains the bounded specialization.
In particular analytic order two is not permission to assume a rational
point or nonvanishing of its Kummer image. The separately saved
conditional continuation retains that premise explicitly.

Continuation test: apply the inspected theorem with exact coefficient
and local-condition conventions, or identify a failed transfer and
withhold the application. The nonzero rational localization is still
missing for an unconditional actual-class assertion. Stop any claim that finite local
membership alone supplies rational Kummer membership, nonvanishing,
strictness or the BSD rank assertion. ATTEMPTS/058 and L005 preserve
those independent obstructions; ATTEMPTS/061--063 remain parked.

No new creative proof mechanism has yet been source-assessed. This
comparison may prepare one only if it exposes a concrete remaining
arithmetic test; standard reciprocity specialization itself is not
creative work. Mathlib coverage for this proposed target is not checked.
