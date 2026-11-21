# Exact scalar execution1808 — work in progress

Approved target: execute the unchanged C033y/C033z rational construction
for C033w's eight positive-real scalars, radius below2^-8 and at most
10^6 defined algebraic operations. Assessment1806 was SPECIALIZE before
this invocation; scope approval1807 supplies the execution gate.

Main gap: L030-L032/C032a actual-Xi all-degree positivity. The intermediate
scalars could support C033w's fixed-three-width interpolation test; exact
weights, conditioning, TV and the full observation interval remain open.

Bounded test: execute the prescribed rational constructors, preserving
complete exact intermediate values before expensive dependent work.
Use Python Fraction, without a floating, rounded or alternative evaluator.
An execution time limit is an operational stopping condition, not a
mathematical lower bound or a failure of the proved operation ledger.
Both reserved2^-10 allowances and the analytic hypotheses remain required.
No scalar enclosure may be claimed from an input-only prefix.

Inputs: C033y/z/u/w, C032s/q/w and C032j conventions. Retain actual
divisor/conjugation/multiplicity, excluded ordinate0, strict strip and
gamma>14, counting, real zeros through100 and one in(14,15), reciprocal
square tail, heat positivity/separate fixed-j errors, both fixed-v1
qualifications, zero drift/killing and Gaussian half-variance. Source-wide
and zero-data correctness and full Mathlib matching remain unverified.
Prior stops C033x/1781/1782 and unfinished C033v are preserved. No argument
or DAG change is planned; execution details and results will be appended
here after the bounded attempt.

## Completed execution

The exact Python Fraction prefix completed in50.039seconds: all48 Gaussian
inputs from C033z(13), then all29 shared moments M_k. Complete rational
values are stored as hexadecimal numerator/denominator pairs under
`scripts/smoothed-law/direct_positive_real_execution_1808/`. The index,
individual bit lengths, timings and SHA256 hashes are in
`scripts/smoothed-law/direct_positive_real_execution_1808.json`.
The last Gaussian denominator has220691bits; the final moment denominator
has226198bits. These values are exact finite constructor outputs, not
new analytic estimates or scalar enclosures.

The remaining-constructor driver executed the unchanged P14 rule and
C033z(19). Its180-second limit stopped during weighted accumulation22/224.
All21 completed weighted summands are saved in `Ihat_partial.json`; the
22nd sample is saved separately as `Ihat_sample_021.json`, but its weighted
addition did not complete. The partial-sum denominator has4063129bits;
the21st weighted accumulation took13.058258seconds including its sample
construction. No profile or scalar was evaluated. The complete record is
`scripts/smoothed-law/direct_positive_real_execution_remaining_1808.json`.
No division-by-zero failure, substituted evaluator or numerical radius
claim occurred.

The prescribed full-construction ledger remains989767 operations versus
the10^6cap, but a completed-run implementation cost has not been verified.
The target radius remains below1/256; no actual scalar radius was obtained.
The analytic25/16384 allowance and both2^-10 arithmetic reserves remain
the inherited contract, not error bounds for an unevaluated scalar.
Wall time and denominator growth do not disprove the rational construction,
prove a lower bound, invalidate its operation ledger, or exhaust exact
arithmetic as a mathematical route.

Independent prefix verification completed in
`scripts/smoothed-law/direct_positive_real_execution_verify_1808.py`:
artifact hashes, integer common-denominator Taylor identities for Gaussian
and completed Ihat samples, integer shared-moment identities and the exact
Ihat prefix sum. All431 checks passed, with no failures; full check results
are in `scripts/smoothed-law/direct_positive_real_execution_verify_1808.json`.
The first21 Ihat samples and their weighted sum were algebraically replayed;
the unused22nd sample is saved and hash-checked but not algebraically replayed.
The verification does not check sources, new analytic estimates, complete
evaluator cost or unevaluated output. In particular a completed input prefix
is not a preview or a certificate of any scalar.

## Decision

Outcome: EXPLORATION, completed implementation/REPRODUCTION under the prior
SPECIALIZE1806 assessment. This is local partial execution, not progress
beyond the cited general results and not an informative mathematical
counterexample. Zero scalars means the intended interpolation input is
still absent. Mathematical exploration usage this step: one bounded exact
execution attempt, with two sequential saved stages; no reset claimed.

Nominate a separate arithmetic-source review before implementing rounding:
`drafts/literature/2026-11-19-direct-positive-real-rounded-execution-review-1808.md`
is REVIEW_REQUIRED. It asks whether new rounding errors and the unchanged
operation cap can both be paid, and approves neither. No rounded arithmetic
was derived or used here. Preserve the exact prefixes for independent
resumption; no global exact-arithmetic stop is asserted. The central
creative blocker1796 remains absence of an independent signed-height input
or representation; this finite arithmetic work is not a creative mechanism.
