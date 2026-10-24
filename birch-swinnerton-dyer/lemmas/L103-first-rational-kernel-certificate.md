# L103 — First complete rational kernel certificate

## Hypotheses

Use L101's finite kernel
J_1(t)=integral_1^128 exp(-t*y) log(y)/y dy, L031's exact rational
endpoint and elementary parameter rules, and audited L102's unchanged
grid/Taylor scheme. Let D=2^256 and set

```
c_l*D = 36887902191165742374446831090090100164633110307723623187031015736440321082816
c_u*D = 36887902191165742374446831090090100380471044238365418461395933078627191865791
c_* = (c_l+c_u)/2
delta = (c_u-c_l)/2
```

The fixed finite evidence is in `scripts/first-rational-kernel/step-404/`.
The three static execution sources are `producer.py`, `replay.py` and
`run_once.py` in `scripts/first-rational-kernel/`; their original bytes
and all eight selected mathematical/source/failure input files are
preserved in that evidence directory's `originals/` tree. No published
rank, complex order, Sha, period normalization or optional numerical
library is a hypothesis. L101 is used only to define the kernel here.

## Conclusion

The parameter satisfies
3/10<=c_l<=2*pi/sqrt(389)<=c_u<=1/2 and delta<=2^-50.
At its exact rational midpoint c_*, the following interval contains
J_1(c_*):

```
l*D = 78342903631499187256361960486876775169494019218701933175652563259623587717465
u*D = 78342903631499187256361960486876775169494019218701933185097296225362883911601
```

Its exact midpoint is

```
78342903631499187256361960486876775169494019218701933180374929742493235814533 / D
```

and its exact radius is
(2^72+2883372)/D < 2^-183 < 2^-50. These are endpoints for J_1(c_*),
not for J_1 at the unknown exact transcendental parameter c.

All 1016 original panels and both complete convolutions pass the
independent replay and the separate step-406 critical audit below.
The original execution records inclusive bounds 28 seconds and 1717513
bytes; its historical finalization time has the qualification below.
The separate audit has measured inclusive bounds 30 seconds and 110916
bytes, below 180 seconds and 134217728 bytes. All eleven selected
original inputs and fixed copies match. This is known-method
REPRODUCTION with audited finite evidence. It supplies neither the
other 127 kernels nor a derivative/nonvanishing result or new BSD case.

## Proof

**Parameter containment.** For m=5 and m=239, the producer saves each
of the 25 exact signed terms (-1)^r/((2r+1)m^(2r+1)), 0<=r<=24.
Write S_24 for the sum through r=23 and S_25=S_24+term_24. L031's
alternating-series enclosure gives S_24<atan(1/m)<S_25; positive terms
decrease since both m exceed one. Machin's identity gives the bounds
16*S_24(5)-4*S_25(239) and 16*S_25(5)-4*S_24(239) for pi.
This imports L031's elementary argument and the precisely inspected
[DLMF 4.24.3](https://dlmf.nist.gov/4.24.E3) arctangent series;
no new transcendental approximation theorem is proved here.

The exact fractions, all terms, outward pi-grid endpoints and the
square-root witness are saved in `parameter.json`. The integer lower
square-root witness is

```
h = 2283776977891595760652804042145316256725726163158907990079216915886027883413766
```

and satisfies h^2<389*D^2<(h+1)^2. Thus sqrt(389) belongs to
[h/D,(h+1)/D]. Directed positive division of twice the pi enclosure
by this interval gives exactly the stated c_l,c_u. The independent
replayer reconstructs every arctangent term and both sums with exact
fractions, finds h by a separate binary search, checks both squared
inequalities and every signed floor/ceiling conversion, and compares
the complete stored parameter evidence. Its exact resulting delta is

```
215837933930641795274364917342186870782975 / (2*D).
```

Integer comparisons certify the claimed closed range and delta<=2^-50.
The exact midpoint numerator over 2*D is

```
73775804382331484748893662180180200545104154546089041648426948815067512948607.
```

**Complete finite construction.** Apply L102 at this rational c_* and
n=1. No parameter, precision, panel, degree or series cap is changed.
For j=0,...,1015 use a=(8+j)/8, y=a+s/8, 0<=s<=1. The logarithm
reduction chooses the unique k in {0,...,6} with a/2^k in [1,2).
Each scalar log uses all 128 odd-power terms, outward multiplication
and integer division, the stated containing clips and its one-grid-unit
tail enlargement. Log 2 is computed once by the same prescription.
The scalar exponential uses all 128 terms after division of c_*a by
2^16, a one-grid-unit enlargement and exactly sixteen rounded squares,
retaining a possible zero lower endpoint as an enclosure.

The panel arrays have exactly 129 exponential, 65 reciprocal and
65 logarithm coefficients. Every recurrence, sign and conversion is
the one in L102. The producer retains all 8385 pairs in ER and all
12545 pairs in (ER)H, including zero slots; their degrees are 192 and
256. Every one of the 257 resulting coefficients is divided outwards
by its positive integration divisor. Scalar multiplication and outward
division by eight implement dy=ds/8. All panel intervals and running
sums are saved individually in `panels.jsonl`, together with exact
endpoints, binary reductions, scalar constants, polynomial integrals
and stage digests. Arrays and full scalar traces are recomputed during
replay, as allowed by the approved evidence contract.

Before the final analytic enlargement the summed grid endpoints are

```
78342903631499187256361960486876775169494019218701933180374929742493232931161
78342903631499187256361960486876775169494019218701933180374929742493238697905.
```

Enlargement by exactly 2^72 grid units at each end is precisely L102's
2^-184 analytic allowance. L102's audited containment proof includes
all scalar tails, signed coefficient errors, full products, integration
rounding and all panel remainders. Its hypotheses hold at the certified
midpoint, so this final interval contains J_1(c_*). The half-width
before enlargement is 2883372 grid units; the conclusion's exact
radius and both strict comparisons follow by integer arithmetic.

**Independent complete replay and execution evidence.** The replayer
imports no producer arithmetic or coefficient/convolution functions.
It implements signed floor/ceiling through absolute-value divmod and
checks the defining integer inequalities at every conversion, interval
multiply and positive-integer divide. Its interval multiplication
selects extrema by the full sign cases, while the producer takes the
extrema of four products. The replay reverses both convolution index
traversals and switches the outer factor. It also sums integration
terms in reverse order; exact dyadic additions preserve the result.
The independent reconstruction computes every scalar term, square,
factor slot, product pair and divisor, comparing the prescribed stage
digests and every panel integral/running sum. Exact final interval
equality is checked in addition to diagnostic digests. Missing panels,
unexpected fields or any mismatch fail the run. Completeness tests
require exactly 1016 panels and 1016*20930=21264880 pairs per pass.

`replay.json` records complete parameter reconstruction, all stage
comparisons PASS, all 1016 panels, all 21264880 pairs and agreement
of the two full primitive-count ledgers. `kernel.json` records the
full exact final endpoints, midpoint, radius and both acceptance
thresholds. The count ledger includes 21801456 interval multiplies,
716408 integer interval divisions and 21787232 additions per pass.
These are diagnostic counts, not a new bit-complexity assertion.
The successful replay and L102 containment argument, rather than a
preview or hash match alone, justify the evaluated enclosure.

`run_once.py` starts its work timer before reading inputs, constructing
inventories, copying the chosen static sources, importing either
arithmetic implementation or doing mathematics. It reserves the final
six seconds within the 180-second aggregate cap for stop reporting;
no work deadline is reached. It performs exactly one production and
one complete kernel replay. A preliminary parameter-only reconstruction
is also inside that same cap; it is not a kernel benchmark or retry.
Its elapsed measurements start before parameter production and
source/input copies. The timer is disabled before final preservation
and reporting, so the six-second reserve is not a hard guarantee.
No generated execution
source, library installation, network request or resumed pass occurs.

`status.json` records elapsed time before final status writing
25.26685458305292 seconds, conservative inclusive bound 28 seconds,
and conservative inclusive output bound 1717513 bytes. The original
write-up reports stdout time 25.268027415964752 seconds after writing;
that terminal record is not separately retained in the fixed evidence.
This post-write duration therefore remains a historical narrative
claim, not an independently recovered measurement. The recorded
bound includes a two-second report allowance, static sources, fixed
copies, all output files, 8192 diagnostic bytes and 8192 final-status
bytes. It records PASS, complete replay, no first failure, resource
checks true and eleven preserved inputs. `preservation.json` checks
each original and its fixed copy against the initial inventory hash;
all match. The actual command was

```
python3 scripts/first-rational-kernel/run_once.py
```

The output directory is exclusively created, so this command must not
be rerun over the preserved attempt. The separate critical audit below
uses the fixed evidence and replayer without producing another kernel.

After execution, scoped documentation validation found four relative
links in the verbatim historical failure snapshots with no local copied
destination. Four explicitly labeled navigation bridges now resolve
them to canonical notebook documents. These are post-execution metadata,
not inventoried fixed inputs, copied theorem proofs or mathematical
premises; the eleven original/copy pairs and all execution certificates
remain unchanged. The scoped structural checker passes. It checks
documentation structure, not the correctness of the mathematical claim.

### Separate critical audit — 2026-10-22, step 406

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-22-first-rational-kernel-certificate-audit.md`.
This is one REPRODUCTION audit of the fixed certificate, not a new
kernel, numerical method or BSD case. Full evidence is saved in
`scripts/first-rational-kernel/step-406/`. Before replay, the complete
static producer, independent replayer and runner were read and compared
byte-for-byte with their inventoried copies. Neither producer nor
`run_once.py` was imported or executed. All eleven selected input/copy
pairs matched their original lengths and SHA-256 values.

**Containment interface.** The full parameter reconstruction checks
both sets of 25 arctangent terms, their exact adjacent sums, the Machin
combination, outward pi endpoints, separate binary-search square-root
witness and its two strict squared inequalities, both positive
divisions, c_l,c_u,c_*,delta and their required ranges. This imports
the cited Machin/series rules above and L031's endpoint rules; no
new parameter theorem is needed. In particular c_* lies in L102's
closed permitted interval, and n=1 lies in its permitted integer range.

For every panel, a=(8+j)/8, b=a/2^k and z=(b-1)/(b+1) agree with
L102. Thus 0<=z<1/3 (log 2 uses z=1/3), including z=0 at a=1;
all log clips contain the true inputs. The code's exponential argument
is c_*a/2^16, its panel beta is c_*/8, rho=1/(8a), and reciprocal
constant is 1/a. Consequently the positive-real scalar and factor
clips have exactly the hypotheses of L102. No clip is justified merely
by its nonempty computed intersection. The 128 log terms, 128 scalar
exponential terms and sixteen squares match the audited remainders.
The coefficient recurrences retain all 129/65/65 slots, both complete
products and all divisors 1,...,257. Scalar multiplication and division
by eight retain the differential dy=ds/8. Summing every panel covers
[1,128] exactly; the final addition of 2^72 grid units on each side
is precisely L102's 2^-184 analytic allowance. This establishes the
connection from replayed polynomial intervals to the true integral.

**Full arithmetic replay and independence.** The saved replayer imports
no producer arithmetic. A fresh wrapper additionally checks every
encountered signed floor and ceiling against Python integer floor
division and its negated ceiling formula; the original replayer also
checks the defining integer inequalities. Every sign-case multiplication
is separately compared with all four exact endpoint products and their
outward rounded extrema. Every positive-integer division, conversion,
addition, sign change and clip is checked by its exact endpoint rule.
The convolution loops reverse both index traversals and the outer
factor; their full pair counts, array lengths and endpoint ordering
are checked. Integration adds terms in reverse order, which preserves
the exact dyadic sum. All scalar traces and coefficient arrays are
reconstructed, all saved stage digests compared, and every stored
panel integral and running sum is compared exactly. Digests do not
replace this complete arithmetic reconstruction.

The sole replay checks 1016 panels, 2032 full convolutions and
21264880 coefficient pairs, including zeros. It checks 21801456
interval multiplications, 716408 divisions, 5083 conversions, 24386
clips and 356616 negations. There are 22522948 checks of each directed
rounding function. All 21787232 additions are accounted for: 21264880
inside the reviewed convolution loops, 1016 exact log combinations,
and 521336 checked additions. The full ledger and final replay report
agree exactly with the original. Actual kernel arithmetic encounters
four noncrossing sign classes and 896 multiplications with an exact
zero operand; it does not encounter a strictly zero-crossing operand.
Separate 36-pair controls cover all nine sign classes, endpoint zeros
and strict crossings, and 21 signed quotient controls supplement them.
Those controls are finite checks of the independently reviewed formulas,
not a claim that actual panel data traverse every sign branch.

The final endpoints, exact midpoint and pre-enlargement endpoints agree
with the statement. The half-width before enlargement is exactly
2883372 grid units; the final radius is exactly (2^72+2883372)/2^256.
Both the required <=2^-50 comparison and the stronger <2^-183
comparison pass exact rational tests. No required or stronger arithmetic
obligation failed. The complete selected values and ledgers are in
`step-406/complete-replay.json` relative to the script directory.

**Historical resources and preservation.** The fixed pre-status
disk boundary is reconstructed from the eleven copied inputs and eight
execution records: exactly 1676788 bytes. Adding the three static
sources (24341 bytes), 8192 diagnostic bytes and 8192 status bytes
gives exactly the reported 1717513-byte bound. The actual status uses
400 bytes. All current step-404 files, including post-run navigation
metadata, plus those static sources use 1702991 bytes; even adding
8192 diagnostic bytes remains below the original bound. The historical
stdout contents are not retained, so the diagnostic allowance is a
reserve, not a measurement of saved terminal bytes.

The recorded pre-status elapsed time 25.26685458305292 gives
ceil(elapsed)+2=28, as the source specifies. However, the source clears
its timer before preservation and status writing. Neither the timer
contract nor this two-second allowance independently proves historical
finalization duration. The post-write assertion exists in the runner,
but there is no separate retained terminal log confirming its execution.
The claimed post-write value is therefore qualified as above; a fresh
run does not reconstruct it. This corrects the stronger watchdog
interpretation, without changing any mathematical containment or
interval conclusion. The official Python
[time.monotonic contract](https://docs.python.org/3/library/time.html#time.monotonic)
and [setitimer and handler-execution contracts](https://docs.python.org/3/library/signal.html#signal.setitimer)
inspected in the assessment support this distinction, not a hard deadline
guarantee. Those rolling docs identified Python 3.15.1 when inspected;
the original manifest records Python 3.15.0. Interface coverage does
not verify a historical execution or pin its binary.

**Fresh aggregate resource evidence.** One clock starts before source
writing, inventories, module imports and arithmetic. All fresh source,
control, inventory, replay, preservation and reporting files are in
`step-406/`; no input copies are created. The work timer has a
174-second threshold, with a final 180-second timer retained through
reporting. As with any Python signal handler, this is not an absolute
dispatch-time guarantee. Successful measured completion is separate:
`status.json` records 27.77859245892614 seconds before writing;
`finalization.json` records 27.77887458400801 seconds after that write.
After writing finalization evidence and checking its size, the terminal
report measures 27.779159834142774 seconds. A subsequent elapsed
assertion passes. Conservative inclusive bounds are 30 seconds and
110916 bytes, including 65536 final-report bytes and 8192 diagnostic
bytes, against 180 seconds and 134217728 bytes. All 36 inventoried
files, encompassing every step-404 artifact and the eleven original
inputs, retain their exact hashes and lengths; no mismatch or first
failure is recorded. The fixed evidence and prior failed routes remain.

**Verdict.** Complete replay, containment, required and stronger radius,
and preservation pass. The original inclusive wall-time claim retains
the explicit historical-finalization qualification; it is not used to
prove the integral. The new audit's measured bounds pass. This validates
one midpoint-kernel input only. Direct mathematical inputs and the DAG
remain unchanged; no claim about any unexecuted kernel's runtime follows.

**Qualifications and downstream use.** Known Taylor/integration
methods already cover this fixed mathematical scheme; this certificate
changes implementation/evidence provenance only. The necessary source
specialization was approved in
`drafts/literature/2026-10-22-first-rational-kernel-implementation.md`.
The derivative still requires the other kernels and exact a_n through
128, followed by L101's full bound
B=2^-43+200*delta+4*sum(|a_n|/n)e_n with eta=0 and strict exclusion
of zero. No runtime/storage inference for those remaining kernels
follows from one n=1 pass. Independent analytic premises, rational
directions and the arbitrary-curve rank comparison are unchanged.

## Mathlib

Full algorithm/certificate coverage is not checked. Supporting Machin
coverage is the previously inspected unconditional theorem
[Real.four_mul_arctan_inv_5_sub_arctan_inv_239](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Arctan.html#Real.four_mul_arctan_inv_5_sub_arctan_inv_239).
That rolling documentation was not pinned or compiled locally. Neither
that supporting identity nor absence of a matching theorem is treated
as formal verification of the present implementation.
