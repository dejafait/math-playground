# Actual-theta translate approximation: completed source review

TARGET: Review the remaining proof of Dimitrov–Xu Theorem 3.2 for an explicit L1 approximation certificate for its cosh-weighted theta correlation, or identify the precise missing estimate if it only restates a zero-free-spectrum premise.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused mechanism 2 of the completed three-mechanism comparison and read both named autocorrelation/parity stops. Directly read the remaining primary proof. Queries "Dimitrov" "Xu" "Theorem 3.2" Wronskians erratum and "1606.05011" correction cosh yielded no inspected correction; search hits are leads only, not evidence of absence.
SOURCE_EVIDENCE: Dimitrov–Xu, Wronskians of Fourier and Laplace transforms, arXiv:1606.05011v1, https://arxiv.org/pdf/1606.05011v1, printed pp. 11–15: (3.7)–(3.10), properties (i)–(iii), Theorems B/3.2, Lemma 3.3, and complete Sections 3.1–3.3; references [5], [10], [12], [20] identified. Reused the prior Theorem 4.1 proof reading.
COMPARISON: The remaining proof assumes density in sufficiency and LP membership in necessity; neither direction constructs finite translate approximants or controls their L1 error independently of the desired spectrum. This closes the specifically unread-proof lead, without proving an impossibility theorem.
GAP: No specified g, coefficients, translations or independently checkable error sequence is supplied for actual theta. The printed odd-kernel Fourier identity in Lemma 3.3 also requires a phase audit before any use of the subsequent Wronskian identity; no correction or counterexample is proved here.
REASON: Park constructive use of this source. Nominate a separate finite phase-consistency audit under its own assessment; neither the criterion nor its printed identities are imported as established local inputs.
LITERATURE_REASON: The exact approved question concerned the previously unread remainder of Theorem 3.2. This turn reads it once; no generic PF search or new mathematical attempt is undertaken.
SCOPE: Completed literature-only source review. No lemma, mathematical script, DAG or argument-overview change; no independent source-proof audit or actual-theta specialization.

## Completed review, 31 October 2026

The source requires an even Schwartz kernel with an entire Fourier
representation, zeros in the open strip |Im z|<alpha, and the displayed
product (3.8). Schwartz decay alone is not an exponential-moment certificate.
Its weight is exactly

    K_2,y(t)=cosh(ty) integral_R (t-2s)^2 K(t-s)K(s) ds.

Theorem 3.2 quantifies over every fixed 0<|y|<alpha; including y=0
adds simplicity. Theorem B needs a nowhere-zero spectrum for L1,
whereas its L2 counterpart needs nonvanishing almost everywhere.

Section 3.1 uses assumed density to exclude spectral zeros, fixes the
sign at x=0, and passes to y=0 by continuity. Its outside-strip step
cites Csordas–Varga [5], Proposition 3.1. Section 3.2 instead assumes
LP, uses (3.8) and Hermite–Biehler theory, obtains strict inequalities,
then invokes Theorem B for density. Section 3.3 offers a bounded
convolution-annihilator reformulation, not approximation bounds.

These are descriptions of the printed argument, not its validation.
In particular Lemma 3.3 identifies the imaginary part with the Fourier
transform of its real odd sinh-weighted kernel under (3.7)'s convention.
The phase and its propagation to Section 3.1 remain unchecked. No
replacement identity is derived in this turn.

No direct approximation reference is invoked at the missing step beyond
Wiener's theorem. Korevaar [10], Theorem 8.1 p. 82, Levin [12], Theorem 3
pp. 311–312, and [5]'s original proof were not independently read here.
Their cited uses concern equivalence/interlacing, not a claimed theta
approximation certificate. No statement about every possible construction
from those books is made. The publisher version is an unread search lead;
the verdict applies to the exact arXiv version reviewed.

Local applicability was checked only in scope: L018 supplies the entire
real-even function/zero correspondence; L019–L020 supply positivity,
decay and the cosine representation. L233 and C233a retain the signed
first-level gap. No new theorem application or normalization bridge is
needed for the negative source comparison. L562 is only a contrast.
No cross-notebook input is used. Matching Mathlib coverage is unchecked.

The test specified at startup therefore fails: the unread proof supplies
no independent approximation/error interface. This is new source evidence
closing that lead, not mathematical progress beyond the checked sources
or a global ban on translate methods. Preserve the September/October stops.
Reopening constructive use needs actual approximants and a verified L1
error tending to zero for the required parameters. Higher signs and
unbounded-height control remain independent gaps.

The newly nominated phase audit is independently testable without any
unknown theta signs. Its exact scope is in
`2026-10-31-dimitrov-xu-fourier-phase-audit.md`; it is subject to a separate
approval turn. No Gaussian calculation has been performed here.

## Original nomination (historical; completed above)

The completed audit remains in L561's retained-input section and L562's
independent conceptual audit. This nomination does not reopen or downgrade
that completed mathematical work. Reuse mechanism 2 of
`drafts/literature/2026-10-31-complete-first-sign-mechanism-discovery.md`
and its exact reading limits.

The main gap is actual-Xi all-degree positivity. An explicit approximation
estimate for the actual weighted correlation could provide a new way to
address that gap; the criterion alone does not. L018, L019 and L020 are the
local entire-function/kernel/normalization inputs for checking the source's
even-Schwartz, canonical-product and zero-strip hypotheses. L233 and C233a
name the currently uncontrolled first-sign residual and its limitations.
L562 is a negative comparison, not an input establishing any theta sign.
No cross-notebook input is proposed.

Recover the exact correlation and weight from the primary theorem before
adopting notation. Seek a specified target function g, finite sums of
translates of that weighted correlation, and an L1 error bound tending to
zero under hypotheses verified independently of the desired zero-free
spectrum. Record which g and which 0<|y|<alpha are covered; do not replace
L1 density by L2 density or ignore y=0/simplicity qualifications. This asks
for source evidence, not permission to derive approximants this turn.

Continue to a separately assessed mathematical target only if the proof or
a direct reference supplies a concrete approximation estimate whose assumptions
can be independently tested on the actual kernel. If it instead invokes the
nonvanishing spectrum/density equivalence or assumes the desired zero
placement, record that precise obstruction and stop this source route. Do not
repeat a Wiener-criterion citation as progress or promise that the unread proof
contains a construction. Preserve the earlier criterion-only stop.

The new point is the unread proof case and an explicit error interface after
the reciprocal model test. Generic autocorrelation and separate parity failures
remain in `ATTEMPTS/2026-09-23-first-associated-autocorrelation-test.md` and
`ATTEMPTS/2026-10-03-complete-parity-positive-definiteness-test.md`.
No justified creative actual-Xi attempt is yet specified: an independently
controlled approximation or signed-remainder estimate is still missing.
Mathlib coverage for this proposed interface is unchecked, not absent.
