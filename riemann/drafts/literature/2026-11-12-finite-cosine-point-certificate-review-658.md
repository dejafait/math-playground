# Continuation658: a bounded finite-cosine point certificate

TARGET: Construct and certify a finite-cosine Carleman point evaluator for the six frozen C998a parity densities on a*2^-80<=t<=a with whole-sum absolute error at most2^-53 and an explicit finite scalar work ledger before any batch run.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse completed review657/source-notes658's scoped duplicate/failure search and primary Si/Ci validated-evaluation comparison; the mathematical data, interval and error threshold are unchanged. No novelty inference.
SOURCE_EVIDENCE: Primary URLs: https://dlmf.nist.gov/6.2#ii (definitions), https://dlmf.nist.gov/6.6 (6.6.5-6), https://dlmf.nist.gov/6.7#iii (6.7.13-14), https://dlmf.nist.gov/6.12#ii (6.12.5-8 and remainder paragraph), https://arxiv.org/pdf/1606.06977v2 (Sections3.1,4.1 Theorem1/proof,4.2,6.5), https://raw.githubusercontent.com/flintlib/arb/2.23.0/arb_hypgeom/si.c and https://raw.githubusercontent.com/flintlib/arb/2.23.0/arb_hypgeom/ci.c (stable implementation cases), https://arxiv.org/pdf/1410.7176v2 (Sections2-5). Full inspected hypotheses/cases and reuse655/656 scalar inclusion coverage remain in2026-11-12-finite-cosine-source-notes-658.md.
COMPARISON: Known methods cover primitive evaluation and error propagation; they do not supply the frozen-transform identity, uniform full-sum precision or usable work count. Derive only this fixed-data specialization; no general theorem reproof or sign claim.
GAP: Pay zero frequency, parity, exact neutral coefficients, all modes through255, positive argument/input errors, transition and small-argument cancellation, series/asymptotic truncations, rounding, constants and complete scalar costs; compare the prescribed work with a declared execution budget.
REASON: Primary coverage now suffices for one bounded REPRODUCTION attempt. Newly written continuation requires separate supervisor approval next turn; no evaluator or mathematical result was derived658.
SCOPE: Unchanged a=log(3)/4, delta=.01,m=286,J=14, all six frozen C998a parity densities and exact C999q neutral completion; real point oracle only, no new trial/reference, outer complex-box theorem or norm computation.

The main gap is L030-L032/C032a actual-Xi positivity, locally including
the unpaid signed S3 remote-plus-induced comparison. A complete point
certificate would remove one oracle gap in the graded full residual-norm
ledger and could then support C999 inverse-action errors and an independent
signed-pairing test. It need not settle the other independent gaps.

Use the inspected primary primitives and tail/error algorithms, with all
hypotheses verified locally. Check the finite-interval transform identity
by substitution/differentiation, explicitly retaining its limits, zero mode
and both parity signs. This is applicability work; do not reprove general
special-function or interval-arithmetic theorems. If optimized library
internals are not cost-bounded, use an explicit finite recurrence and pay
its rounding and elementary calls. No oracle call is free work.

Continuation test: prove a uniform whole-density absolute error<=2^-53
with finite prescribed parameters, and give complete per-point scalar
work, including setup and sharing across the six densities. Compare the
prospective batch count with a declared ceiling before execution. If no
usable prescription is obtained, save its precise failure and stop that
prescription. Do not substitute sample agreement, a precision request,
unbounded doubling or the unaudited657 node ledger for the certificate.

Essential inputs: C998a/audit655 and654/655 ledgers; C999/audit650
Sections3-4; C999z/audit646; C999q exact Z; C999y/audit642 exact X;
C744v full operators. Retain C744w/z,C999k and analytic/arithmetic/
source-to-Xi/whole-core/unreplayed c_* contracts. C998b/657 is preserved
as an unaudited prescription stop, not an audited mathematical input.
The frozen archive is scripts/separation-seven/frozen-reference-proposal-652.npz,
SHA256 2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6.
No cross-notebook input. Outer analyticity/forcing/projection/norm-width
budgets, higher/mixed endpoints,C744q/H2 and global Xi assembly remain open.

This is standard numerical specialization, not a creative central sign
mechanism. A justified creative nomination still needs an independently
motivated signed comparison beyond the currently missing residual and
inverse-pairing control. Mathlib matching coverage is unchecked.

## Source-link recovery659 (2026-11-12)

The supervisor reported that ready assessments require a direct source URL.
The SOURCE_EVIDENCE field now contains direct primary URLs, rather than
only pointing to source-notes658. Reopened DLMF6.6 equations5-6 and its
finite-argument convergence statement, DLMF6.12 finite remainders, and
Johansson1606.06977v2 PDF/version record. Reuse658 for the previously
inspected full theorem proof and implementation cases; this repair adds
no new applicability claim. TARGET, SCOPE, SPECIALIZE decision and all
unpaid quantitative obligations are unchanged. No mathematical attempt
was performed; this is a metadata repair, not additional discovery.
