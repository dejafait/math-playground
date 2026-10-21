# Step 329 — index-four successor table attempt

Prior gate: `drafts/literature/2026-10-18-index-four-multiplier-table.md`
is SPECIALIZE for this exact target. This is RESEARCH / REPRODUCTION /
implementation; no further literature is needed. Audited L085 supplies
the entire multiplier, not merely a candidate suborder. L084's table is
for its input, and no successor table was found in the inspected scope.
ATTEMPTS/041/042 remain preserved and are not rerun.

The main gap is arbitrary analytic-order/rational-rank equality above
one. This intermediate input could support further local order arithmetic
and eventually L066's global descent enclosure. It supplies none of
global maximality, complete units/classes, full descent, rational
membership or arbitrary rank comparison.

Before execution: reconstruct the original H basis and all canonical
transports. From the L084 n-basis use Z=diag(1,...,1,1/2,1/2), T=Z^-1.
Check every entry against L085's multiplier and audited copy. Construct
all successor coefficients from the old integral table with checked
integer division. Independently reconstruct every successor representative
and verify every product by full Q[T] division by H, without using the
producer's coefficient-scaling routine. The original scales 31 and 62
give the justified common successor scale 124; retain both original
coordinates, every inverse, actual identity and complete index-four
inclusion. Save the complete division quotients and zero remainders.

Discriminating test: one fresh directory, exclusive writes, and one
external 180-second/134217728-byte watchdog covering production, replay,
hashes, code, logs, certificates and final writing. Stop on the first
missing input, nonintegral coefficient, incomplete coverage, identity,
lattice, preservation or cap failure; preserve partial evidence with no
retry or further correction. Success licenses only this fixed table;
a later separate critical audit remains necessary.

## Outcome: STALLED, implementation failure

The sole execution was
`python3 -B scripts/seven-torsion/index-four-table-329/run_once.py`.
It stopped at the first verifier failure, with no retry or code change
after execution. The producer reports 110592/110592 integer slots,
96 identity actions and index four, but these are unverified production
claims. The independent verifier reports zero product slots, zero product
identities and zero remainder positions checked; no division certificates
were written. The canonical full table result is therefore not established,
and no lemma, DAG node or argument change is warranted.

The failure is `AttributeError: 'float' object has no attribute 'denominator'`.
In `verify.py` the matrix routine starts entries at integer zero; some
zero coordinates therefore remain Python integers in `nscaled`. The
subsequent `x/(1 if i==47 else 2)` creates floats for those coordinates.
The following `.denominator` test stops before V reconstruction and
before every original-H product. This is a verifier type error, not a
nonintegral field coefficient or mathematical obstruction. It supplies
no evidence against the identified multiplier or against table closure.
The earlier preparation generator also had a text-match error before
emitting any mathematical code or starting the one-shot run; it was
corrected during preparation. That was not a mathematical retry.

`producer-report.json`, `verification-report.json`, `stage-report.json`
and `watchdog.json` in that run directory retain the full failure.
The producer used 0.924550 internal seconds and the verifier 0.910987.
Through watchdog writing the failed run used at most 1.985842 seconds
against 180 and 4765354 bytes against 134217728. Meeting the caps does
not repair its incomplete mathematical evidence. The watchdog's failure
is `stage_exit_1`; the stage's failure is `verify_exit_1`.

Because the stage aborted before its final preservation check, a separate
post-stop preservation-only read checked every recorded hash without
rerunning any mathematical arithmetic. All 712 input files and all five
new code files are unchanged. The complete hashes are in
`scripts/seven-torsion/index-four-table-stop-329/preservation.json`.
This administrative check is explicitly outside the failed watchdog;
it is not a completed bounded table certificate. All original files,
the entire unverified table, failed verifier and unfinished work remain.

Route decision: retire this execution permanently. Propose a distinct,
replay-only verification of the preserved output, with explicit Fraction
reconstruction for integer zeros and no production rerun. Its changed
provenance and cap obligations receive a separate REVIEW_REQUIRED
assessment; no corrected verifier or mathematical replay is run now.
The global arithmetic and BSD gaps named above remain unchanged.
