# C998o: Finite scalar-register Gauss setup

## Hypotheses

Use the ONE prescription fixed before execution in
`drafts/2026-11-13-scalar-register-gauss-working-694.md`, implemented in
`scripts/separation-seven/scalar-register-gauss-694.py`. Degrees are
N=63,81,117. Arithmetic is exact rational arithmetic in a real scalar
register program: an addition, subtraction, multiplication, division,
comparison or destination assignment costs one operation. Arithmetic
instructions therefore cost two including their destination assignment;
literal and copy instructions cost one; comparisons branch directly and
cost one. Each division additionally executes a counted nonzero comparison.
This is the scalar convention used in C998g, not a bit-operation or
wall-clock model. No finite-machine rounding guarantee is asserted.

The program generates D=2^640 and all recurrence, tolerance and mesh
constants. Its only initial literals are the integers -1,...,128 and
550,560,640,16384, each explicitly assigned once. Its positive mesh is
1-j^2/16384 for j=0,...,127. It uses C998n's adaptive safeguarded
interval-Newton numerical map: at most17 prefix trials, threshold
Mr<=|d|/8 with derivative exclusion, at most12 Newton updates, conversion
floor2^-560 and node-width gate2^-550. Weights have independent radius
tests. The precise map, derivative bounds and inclusion proofs are C998n.

Fixed loops over degrees, mesh slots, recurrence stages and bounded
trials are finite program macros, expanded at their fixed integer slots.
Their indices are instruction addresses, not numerical service registers.
An operand reference is a wire to a register, not a scalar copy. Explicit
copies, selected endpoints and output stores are instructions and counted.
The data-dependent conversion loop executes counted width/depth tests,
midpoint and width halving, selected-endpoint copying, depth increment
and even a separately counted halving-count register. It uses no remainder,
floor or uncharged numerical table. Symbolic address allocation, transcript
serialization and independent verification are outside the numerical
service. This is an explicitly specified scalar program; its cost is not
a count of all integer operations inside the Python/Fraction interpreter.
Audit695 below verifies this source correspondence and its model limits.

No witness archive or original operator contract is used. The prior
SPECIALIZE assessment687 and inspected source-notes688 cover this finite
construction. Imported general inputs, with their applicability here, are:

- Johansson--Mezzarobba, *Fast and rigorous arbitrary-precision computation
  of Gauss-Legendre quadrature nodes and weights*, arXiv:1802.03948v1,
  12February2018, Section1(1),(3), Section2(5), Proposition3(7), printed
  pp1,4-5, [primary PDF](https://arxiv.org/pdf/1802.03948v1). These supply
  Bonnet's recurrence, the derivative/weight identities and derivative
  bounds on[-1,1]. All three degrees are positive integers and every
  interval remains inside(-1,1), as checked in C998n and the exact trace.
- Alefeld--Claudio, *The basic properties of interval arithmetic, its
  software realizations and some applications*, Computers & Structures
  67(1998),3-8, Section5 Theorem2/scalar case,p6,
  [primary PDF](https://na.math.kit.edu/alefeld/download/1998_The-basic_properties_of_interval_arithmetic_its_software_realization_and_some_applications.pdf).
  Polynomial smoothness and the checked exclusion of zero from the full
  derivative interval give root preservation. No general convergence rate
  or fixed iteration count is imported.
- [DLMF18.2(vi)](https://dlmf.nist.gov/18.2#vi), the simple real interior
  zeros theorem for orthogonal polynomials. The unit weight on(-1,1) is
  positive with finite positive mass and all moments. Verified disjoint
  sign-change intervals, odd parity and zero exhaust the degree-N count.

No general source theorem is reproved. C998n supplies the established
mathematical inclusions; complete exact trace equality below justifies
using them for this different implementation.

## Conclusion

The specified register program constructs all261 Gauss-Legendre node and
weight pairs. Each node radius is<=2^-551 and each weight radius<=2^-542,
so each is separately<=2^-512. Its complete executed scalar-program cost is

    3290939 <= 5000000, with headroom1709061.             (1)

All executed primitive instructions are present in the compressed transcript
`scripts/separation-seven/scalar-register-gauss-694.trace.jsonl.gz`.
The complete mathematical trace and output intervals are in
`scripts/separation-seven/scalar-register-gauss-694.json`.
The independent full transcript replay passes5791600 checks without failure
and is saved in `scripts/separation-seven/scalar-register-gauss-replay-694.json`.
Audit695 below upholds the scalar-program/source correspondence, finite
control expansion, wire references, guards and output completeness. Its
source-directed replay matches all1909636 saved events and passes5901507
checks without failure. This is an audited local implementation specialization
of known methods, not a new discovery beyond the checked sources.

C998n's692 source/ledger remains stopped as submitted by audit693. Equation(1)
does not repair its rejected12-per-pass component claim. The earlier C998l/m
stops retain their stated scopes. No endpoint bank, fourteen moment families,
contraction, complete square error/work, inverse debt, signed S3 comparison,
higher/mixed signs, C744q/H2 or actual-Xi/global assembly follows. There is
no RH candidate.

## Proof

### Exact scalar realization and grid safeguards

The constructor's engine contains only literal, copy, +,-,*,/, comparison
and output-marker instructions. Each arithmetic operation creates a fresh
single-assignment numerical register. Later references to that register
have no numerical effect. Its engine records every instruction as executed,
including both true and false comparisons and every division-domain guard.
No service arithmetic uses a Python float, integer floor, remainder, abs,
min, max or power oracle. Absolute value and endpoint selection use counted
comparisons and arithmetic/copies. Powers of two are generated by640
counted multiplications; factorial-scaled recurrence constants are generated
by counted multiplication/addition. Literal setup and all unused generated
constants are counted as well.

For the point evaluator the source recurrence is the C998n identity

    Q_k=k!D^k P_k(a/D),
    Q_(k+1)=(2k+1)a Q_k-k^2 D^2 Q_(k-1).

The four arithmetic instructions per stage each include a destination
assignment. The fixed stage expansion refers directly to the previously
created Q registers; it does not numerically copy Q_k into a different
stage register. The host's names for those operand addresses are symbolic
wiring. Thus there is no omitted numerical stage-counter update or p=q
copy in THIS single-assignment program. Dynamic sign, interval, threshold
and stopping branches all execute their real comparisons through the engine.
Finite macro expansion does not grant a free numerical value or root seed.

Here is the replacement for692's unimplemented remainder guards. Initially
both mesh endpoints are integer multiples of2^(640-14) in grid units a,
and depth=14. Inductively, endpoints at depth b are multiples of2^(640-b).
When b<640, their exact midpoint is a multiple of2^(640-b-1), so it is
still an integer grid point. Bisection increments b and preserves the
property. During conversion the cell endpoints and width have the same
property; exact division by2 and depth increment preserve it at b+1.
Expansion by that width and selection with old endpoints also preserve
it. Before every derivative midpoint and conversion pass the program
checks depth<640 with a counted comparison. Therefore exact real halving
implements the required integer-grid operation without a parity oracle.
All such guards succeed in this execution. The proof uses the recorded
finite path, not a generic convergence assumption or an extrapolation to
uncomputed roots.

### Complete accuracy evidence, with no borrowed seeds

The constructor reads no692 data. Its independent checker subsequently
compares the entire `rows` value of its certificate with692: all384 mesh
values/signs, every prefix trial and fallback, every midpoint and full
adjacent polynomial value, derivative range, second-derivative bound,
raw/intersected/converted Newton image, depth and halving count, final
weight interval, zero-node case and reflected output. The comparison is
exact structural/rational-value equality of the full evidence, not a
preview, hash-only comparison or comparison of final radii alone.
The maximum node and weight radii also match exactly. The checker verifies
that the692 unscaled-recurrence replay has no failures and binds its saved
source hash to the full692 certificate. C998n contains that independently
checked inclusion proof and its176788-check evidence.

Consequently every C998n isolation, full derivative inclusion, scalar
Newton root-preservation and final independent weight-radius argument
applies to exactly the numerical values produced here. All129 positive
roots,129 reflected roots and three exact zero-root weights are present.
In addition, the new instruction replay computes each of the261 output
quadruples from its own registers and checks both ordered intervals and
each of their522 separate radius tests against2^-512. This directly binds
the accuracy evidence to the program whose cost is claimed in(1).

### Full operation transcript and independent cost replay

The transcript records opcodes, fresh destination identifiers, operand
identifiers, literal values and comparison outcomes. Output markers name
the four numerical endpoint registers and the degree/parity slot. They
perform no numeric computation; the four output stores were already
explicit instructions. All operands can therefore be reconstructed from
the small initial literals by ordinary exact rational evaluation.

The separate checker independently implements every opcode. It verifies
that operand registers exist, each destination is fresh/consecutive,
every division denominator is nonzero, every complete rational comparison
has its recorded truth value and every final output matches the accuracy
trace. A full-stream use-count pass merely permits discarding dead large
rational registers; it omits no instruction or mathematical value. At most
520 registers need remain live. Every instruction is consumed, and no
pending operand use remains at the end.

The complete instruction inventory is:

| Instruction | Count | Scalar cost each |
| --- | ---: | ---: |
|Literal assignment|134|1|
|Copy assignment|91119|1|
|Multiplication|734409|2|
|Division|171529|2|
|Addition|222333|2|
|Subtraction|259769|2|
|Comparison, including division guards|423606|1|

There are1388040 arithmetic instructions. Thus the sum is
2*1388040+134+91119+423606=3290939. The1479293 numerical destinations
are exactly1388040+134+91119; they are not charged a second time.
The checker also reconstructs every cost category and matches its sum to
the constructor. The6476 textual category markers and261 output markers
contain symbolic metadata only; all numerical stores/computations and
endpoint tests associated with those markers are counted above. Program
counter/address management and exact-rational bit implementation are not
real service registers. This qualification is essential to the stated
scalar model, whose source correspondence is verified in audit695 below.

Reproduce from this notebook:

    python3 scripts/separation-seven/scalar-register-gauss-694.py
    python3 scripts/separation-seven/scalar-register-gauss-replay-694.py

The single constructor run was not retuned or repeated. The verifier's
first pass used the wrong existing692 hash-field name (`source_sha256`
instead of `source_certificate_sha256`) and stopped after five checks.
Its failed report is preserved in
`scripts/separation-seven/scalar-register-gauss-replay-first-pass-694.json`.
Correcting only that schema lookup yielded the full passing replay above;
no numeric value, implementation prescription or transcript was changed.

### Audit695: source correspondence and the finite control model

The following is a conceptual audit of the stated real scalar program,
not of Python's bit-operation cost. Its source-directed verification is
`scripts/separation-seven/scalar-register-gauss-audit-695.py`; the complete
report is `scripts/separation-seven/scalar-register-gauss-audit-695.json`.
The report passes5901507 checks with no failure. The original constructor,
trace, accuracy evidence and previous replay files are never overwritten.

**Control and wires.** The finite program can be specified before any
root computation, rather than extracted from its successful transcript.
Expand the powers loop640 times, constant-table loop117 times, and the
three degree cases63,81,117. Each degree has128 mesh evaluations and127
adjacent-sign tests. At each isolation test branch on the counted scalar
comparison. At every leaf of this finite branching tree, the ordered list
of selected bracket-register addresses is fixed. Expand its root loop
at those addresses. There are at most127 brackets, independently of the
actual root count. In each root block expand17 adaptive trials and12
Newton cases, retaining their counted numerical tests and early-exit
edges. No branch outcome or bracket value is supplied by an oracle.

The conversion loop is finite on all paths that reach it: depth starts
at14 and never decreases; each executed pass checks depth<640 and adds1
to it. At most626 passes can succeed in any one call. A further attempted
pass fails its counted depth test. Thus it too admits bounded expansion
including failure exits; the mathematical argument does not assume that
the successful trace is the only possible execution. The actual counts
remain those of executed instructions, not the size of expanded code.

Names such as p,q in the recurrence denote the addresses of immutable
scalar registers. At a statically expanded recurrence stage, setting
p,q=q,z changes the compiler's operand bindings; it does not assign a
new real value to a numerical register. For dynamic control, duplicate
the continuation along each counted comparison outcome and retain the
corresponding address bindings on that edge. This also eliminates the
host lists, iterator positions, seed/done flags and saved Boolean names
from numerical storage. It yields a finite arithmetic branching program
using exactly the emitted real instructions. No free numerical result
is introduced at a merge. Explicit endpoint selections and copies remain
the source's counted `cp` instructions even where this expansion might
eliminate some of them. Address/code storage is excluded by the stated
model; this argument would not establish the same cost for a machine
that charges pointer traffic, all host assignments or finite-word work.

**All numerical entry points.** Direct rational arithmetic on register
values occurs only in Engine.op; direct numerical comparisons occur only
in Engine.cmp. Literal/copy assignments go through their explicit methods.
The small literal set is fixed before any values are computed. Every
power, factorial-scaled denominator, recurrence coefficient, second-
derivative bound and mesh value is produced by these instructions. The
functions zi/rf/iv/gr and integer conversions outside the engine serialize
evidence; their results never enter a numerical service operand or select
a service branch. Guard/category/work counters are proof instrumentation,
not inputs to any successful numeric calculation. The work-cap exit checks
the charged ledger, whose final bound is independently established.

Every value-dependent service test is an Engine comparison. Short-circuit
`or`/`and` implements its ordinary branching graph: skipped comparisons
are not executed and need not be charged. `need` checks the Boolean outcome
on the outgoing edge, not a second real comparison. Engine.op('/') first
executes the denominator comparison and then charges division plus its
destination. Min/max and absolute value each execute their comparison and
selected copy or subtraction. Every chosen bisection endpoint, conversion
endpoint, output and inventory update has its indicated scalar instruction.

**Grid invariant.** In grid units, the initial endpoints and their widths
are multiples of2^(640-14). Suppose endpoints are multiples of2^(640-b).
The derivative midpoint at b<640 is a multiple of2^(640-b-1), hence an
integer. If the adaptive step bisects, the retained endpoints are multiples
of this finer unit and the counted depth increment records b+1. Otherwise
the old endpoint invariant remains at b; merely evaluating a midpoint does
not change the endpoint depth. During conversion, the search-cell endpoints
and its width are multiples of2^(640-b). One guarded halving yields the
corresponding invariant at b+1. Expansion by this width preserves that
unit, and the old endpoints, being on a coarser grid, also lie on it.
Selecting/intersecting them therefore preserves the invariant at the
returned depth. This covers both center branches and both clipping cases.
No parity/remainder calculation is required by this implementation.

**Analytic applicability and outputs.** C998n's mesh sign changes,
reflection and zero exhaust the degree count under the cited Legendre
simple-zero theorem. Its positive brackets remain in(0,1); the derivative
calls explicitly exclude the endpoint1. Both alternatives for M bound
the second derivative on the whole interval, so taking their minimum is
valid. The accepted derivative interval excludes zero. Interval Newton
therefore retains the already isolated root, and the entire image is
contained by the checked conversion. The final derivative interval is
freshly recomputed; the weight denominator uses positive ordered factors.
This verifies the separate weight test, rather than assuming node accuracy
implies weight accuracy. Negative-node endpoints are computed by two paid
subtractions and weights by two paid copies; zero-node endpoints and its
exact rational weight have four paid stores. Symmetry and exactness give
their radius bounds without a further runtime radius calculation. All522
output radii are nevertheless tested by the independent verification.

**Source-directed evidence.** The audit retains the source's full numerical
and control AST. It substitutes a read-and-compare sink for transcript
creation and removes only terminal hashing, serialization and printing
after the complete in-memory report has been formed. Every emitted event,
including markers and output-address quadruples, must match the next
saved event exactly; an unexpected/missing event fails immediately. Every
division must immediately follow its counted nonzero-denominator comparison.
At completion it compares the entire regenerated report with694 and the
entire mathematical `rows` value with692. It independently totals event
costs, checks each output radius and binds both previous complete rational
replays to their unchanged sources/certificates by hashes. Source-directed
replay is not a substitute for those independent arithmetic/inclusion
checks, whose programs and load-bearing cases were also inspected.

All1909636 source events match, including171529 immediately guarded
divisions,6476 category markers and261 output markers. The entire numerical
report matches, not just its result label or largest radii. Independent
event addition reproduces3290939<=5000000 with headroom1709061, and the
complete522 radius tests give the stated bounds2^-551 and2^-542. Thus the
remaining source-correspondence acceptance obligation is discharged for
this exact real scalar model and these fixed degrees. Reproduce this audit
without overwriting any prior artifact:

    python3 scripts/separation-seven/scalar-register-gauss-audit-695.py

No new general theorem, approximate node table, convergence theorem or
precision heuristic is used by this audit. The previous source693 stop,
and C998l/m's distinct prescription stops, remain intact. This audit has
no implication for the unpaid endpoint bank or signed S3/Xi positivity.

## Mathlib

Full matching Mathlib coverage for this finite scalar-register setup,
all-node/weight accuracy and full operation transcript has not been
checked. Supporting Legendre or rational/interval arithmetic results would
not alone establish this finite cost statement. Unknown coverage is not
evidence of absence. The standard inputs are cited with their relevant
hypotheses above; the new work is a finite implementation/reproduction.
