# Second rational kernel: source and interface comparison

2026-10-23, step 411. Completed literature-only review; no kernel,
new mathematical result or mathematical script has been produced.
The exact target remains the TARGET in
`drafts/literature/2026-10-23-second-rational-kernel-certificate.md`.

The main gap is arbitrary-curve rational rank versus complex analytic
order at least two. The intermediate input is one J_2(c_*) enclosure
for L101's fixed signed sum. L102's audited theorem already quantifies
over n=1,...,128; L103 certifies the unchanged midpoint. Execution and
its actual resource requirements remain unverified. Independent gaps
include the other 126 kernels, full signed assembly, parameter transfer,
strict zero exclusion and the arbitrary-curve comparison.

Read L101's full contract, L102's hypotheses and construction through
its complete replay obligations, L103's parameter/construction and full
critical-audit supplement, and the ready first-kernel implementation
and audit assessments. Inspected all producer/replayer arithmetic and
their fixed n=1 run bodies. Both run bodies encode n=1 in the scalar
exponential argument and beta, and both final records encode n=1.
Changing only a label would therefore be invalid. Fresh execution
must keep those two independent paths separate and retain the complete
L103 parameter witness. The old entrypoint targets step-404 and must
not execute again.

## Known results, duplicates and failures

Reuse the inspected queries and stronger-method comparison in
`2026-10-21-rational-kernel-source-review.md` and the source-case map in
`2026-10-22-rational-kernel-audit-coverage.md`. The first-kernel
implementation and critical-audit assessments already cover elementary
parameter certification, complete interval arithmetic and its limits.
No new broad discovery search is needed for this same quantified scheme.
The specific search for `J_2`, `n=2`, `second kernel` and `second-kernel`
in the 2026-10-2* literature assessments, histories 39*--410 and
ATTEMPTS/046 found this proposal but no completed second-kernel
certificate. A failed local search is not evidence of mathematical
novelty. No other notebook was consulted.

Read ATTEMPTS/043, /045 and /046 and L103's complete step-406 supplement.
The direct complex/p-adic comparison lacks its required theorem; the
order-table route stopped on nonunique source insertion; the optional
FLINT backend is unavailable. These are different mechanisms. This
target uses neither a higher-rank comparison nor that backend or nested
source replacement. The optional Berz--Hoffstatter paper's unread
integration cases stay excluded. Preserve all stops. L103's historical
28-second finalization is qualified; its fresh audit timing concerns
only n=1 and supplies no practical bound for n=2.

## Primary inputs and exact applicability

Reopened NIST DLMF v1.2.8, released 2026-09-15, on 2026-10-23:
[1.4.35--37](https://dlmf.nist.gov/1.4.vi) assume C^(d+1)
regularity on the closed interval and give Taylor's finite polynomial
with Lagrange and integral remainders. The interior-point case is for
x>a; the expansion endpoint uses the finite identity. Also inspected
[4.8.16](https://dlmf.nist.gov/4.8.E16), exponential multiplication
for complex arguments. Reuse, rather than reprove, the already
inspected integration 1.4.26/28/29, series 4.2.19 and 4.6.1/4,
derivatives 4.7.3/7/8/10, positive-log identity 4.8.2 and geometric
sum 1.2.11 cases. The same positive panels meet those hypotheses;
n=2 changes neither smoothness nor branches, including at y=1.
The cited books were not separately read. These general statements
give no executed certificate or practical cost bound.

L102's separately audited theorem, not a new error derivation here,
already supplies the entire quantitative method for n=1,...,128 and
c_* in [3/10,1/2]. L103 supplies that exact rational midpoint and its
complete parameter witness. Substituting n=2 meets those hypotheses.
The following checks only match existing hypotheses and interfaces:

| Item | Required n=2 input | Existing coverage retained |
| --- | --- | --- |
| Parameter | The unchanged L103 c_* and full step-404 parameter record | Same closed range; no new pi, root or parameter approximation |
| alpha | 2c_* in [3/5,1] | L102 requires 0<alpha<=64 |
| Scalar exp | w=(2c_*)a/2^16, a=(8+j)/8<128 | w<128/2^16<1/8; 128 terms, q enlargement, 16 squares and [0,1] clips |
| Panel exp | beta=(2c_*)/8 in [3/40,1/8] | L102 permits 0<beta<=8; all 129 slots retained |
| Reciprocal and log | rho=1/(8a), 1/a, log a, binary k | Independent of n; same containing clips and all 65/65 slots |
| Products/integration | ER and (ER)H, then every divisor 1,...,257 and dy=ds/8 | Same complete 8385/12545 pairs, 193/257 slots, 1016 panels and exact +/-2^-184 enlargement |

No n=1 width, sign pattern or small-argument stability observation is
transferred to the new execution. L102's cancellation-safe bounds cover
the full declared ranges. Actual endpoint equality and widths still
need execution; the uniform theorem does not provide their values.

Reopened the rolling official Python 3.15.1
[monotonic clock](https://docs.python.org/3/library/time.html#time.monotonic),
[timer](https://docs.python.org/3/library/signal.html#signal.setitimer)
and [handler-execution](https://docs.python.org/3/library/signal.html#execution-of-python-signal-handlers)
passages. Clock differences measure elapsed time without system-clock
adjustments. A zero timer clears it; Python handlers can be delayed,
including by C work. These contracts do not guarantee timely cleanup.
The new run must report its actual interpreter and successful measured
completion through final writes; old timer behavior cannot certify it.
No installed binary or future performance was tested in this review.

Full Mathlib algorithm coverage remains not checked. Reuse L103's
supporting, previously inspected unconditional Machin identity
`Real.four_mul_arctan_inv_5_sub_arctan_inv_239`, linked there; no new
formal coverage, compilation, absence or novelty claim is made.

## Isolated execution and complete replay contract

SPECIALIZE permits one subsequent REPRODUCTION implementation/calculation
attempt. It does not assert that an uncreated adapter is already correct.
Choose fresh explicit sources under `scripts/second-rational-kernel/`
and an exclusively new evidence directory. Never execute the old
run_once.py, import its top-level runner, mutate historical sources or
replace source text through an ambiguous marker. Reusing separate
copies of the two previously independent arithmetic implementations is
allowed; sharing producer arithmetic with replay is not. Review the
fresh sources before the sole kernel pass, inside the aggregate cap.

Bind n=2 explicitly in both implementations, their manifest and final
records. For midpoint u/v the producer's scalar argument becomes
2*u*a8/(v*8*2^16) and beta becomes 2*u/(8*v); independently use
the same exact mathematical arguments in replay's separate expressions.
Do not double the c_* field or merely change output labels. Check the
exact input ranges before every containing clip. Keep reciprocal/log,
all degrees, term counts, grid and final enlargement unchanged.

Load the fixed step-404 parameter record read-only. Reconstruct it by
the existing producer parameter algorithm and compare the complete
record exactly with the fixed input; the separate replayer independently
reconstructs both arctangent sums, every square inequality and endpoint.
Require the same c_l,c_u,c_*,delta as L103. Preliminary parameter checks
must not leak counters into full-pass ledgers: preserve the old complete
parameter-plus-kernel accounting, explicitly resetting only preliminary
replay counters before the one full replay. No new parameter schedule,
precision refinement, kernel benchmark or hidden retry is allowed.

Persist complete fresh source bytes/hashes, manifest, parameter witness,
all 1016 panel records, exact final endpoints/midpoint/radius, full replay
ledger/report and resource/preservation reports. Recompute every scalar
term and sign, rounded endpoint and containing clip, sixteen squares,
129/65/65 factor slots, both full products and every integration divisor.
Each pass checks all 21264880 coefficient pairs including zeros. Retain
independent signed floor/ceiling checks, sign-case versus four-product
arithmetic, reversed convolution traversal and signed primitive sums.
Compare every reconstructed stage, panel and cumulative sum exactly;
digests and aggregate counts alone do not establish arithmetic validity.
No assumption about n=1's actually encountered sign cases is permitted.

Require final interval ordering, full production/replay equality, actual
radius strictly below 2^-50 and L102's stronger prediction <2^-183,
with exact comparisons after the +/-2^-184 enlargement. Preserve the
first failed obligation, even if a weaker width happens to pass.
The accepted integral is J_2(c_*), never J_2(c).

One clock starts before input reading/inventories, source generation,
copies, imports or arithmetic. One aggregate 180-second and 134217728
new-byte budget includes these operations, all production/replay,
logs, fixed copies and final writing/preservation. Reserve reporting
space and work time; retain the terminal deadline through finalization,
record before/after-write timings and verify measured successful
completion, separately from timer-dispatch semantics. Inventory and
rehash all pre-existing files in `scripts/first-rational-kernel/` and
`scripts/finite-derivative-coefficients/`, plus selected canonical
L031/L101/L102/L103, source-approval and failure inputs. Originals stay
read-only; full copies of every old artifact are unnecessary. Persist
the inventory and all exact preservation comparisons.

Stop at the first hypothesis, arithmetic, equality, width, preservation
or cap failure. Preserve partial evidence without retry, resumption,
enlarged bounds or a third kernel. No pass may rest solely on a timer
installation, requested precision, sample, digest or optimistic reserve.
No kernel or mathematical script ran in this review.

## Decision and downstream limits

Essential source coverage for this exact single-kernel attempt is ready.
The only identified implementation differences are a fixed n=2 binding
at both exponential inputs and output metadata, read-only reuse with
complete parameter reconstruction, and isolated resource/preservation
handling. These remain execution obligations. No new bound, lemma or
reproof was needed or approved beyond the existing quantified scheme.

Direct mathematical inputs are L031's endpoint rules, L101's J_n
definition, audited L102 and audited L103's parameter portion. Eventual
derivative use also retains L030's conductor/modularity, L031's audited
full untwisted coefficients and Fricke sign, L099 and foundations/02
through L101. L035's already published fixed complex order is context
only; L100, published rational bases/Sha, period normalization, optional
Taylor-model papers and unavailable binaries are not kernel premises.

Continue only on all complete acceptance checks; otherwise park this
isolated attempt with its actual failure. Even success leaves 126 other
kernels, signed weighted assembly, parameter propagation, the complete
L101 error and strict zero exclusion. It changes evidence provenance
for a known fixed case, with no new BSD case, uniform rank comparison,
full Sha finiteness or refined leading-coefficient formula. The argument
and DAG have not changed.
