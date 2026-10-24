# L108 — Fixed midpoint kernels fifteen through eighteen

## Hypotheses

Use L101's definition J_n(t)=integral_1^128 exp(-nty) log(y)/y dy,
L031's rational endpoint rules, audited L102's 1016-panel containment
theorem, and the complete audited parameter portion of L103. Put D=2^256
and fix exactly

```text
c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2D)
c_l D = 36887902191165742374446831090090100164633110307723623187031015736440321082816
c_u D = 36887902191165742374446831090090100380471044238365418461395933078627191865791
```

L103 certifies 3/10<=c_l<=2*pi/sqrt(389)<=c_u<=1/2,
c_*=(c_l+c_u)/2 and delta=(c_u-c_l)/2<=2^-50.
The fixed evidence is `scripts/four-rational-kernels/step-435/`.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-kernels-fifteen-through-eighteen.md`.
Step-412 supplies the isolated producer/replayer templates, restricted
step-417 AST data supplies only adaptation fragments, and step-431
supplies the worker interface. No L106 numerical value, signed audit
installer or stopped launcher is an input.

## Conclusion

For n=15,16,17,18 respectively, J_n(c_*) belongs to [l_n/D,u_n/D]
with these exact integer grid endpoints:

| n | l_n | u_n |
|---|---|---|
| 15 | 26875261430996018939663558047746797857529080403119782247225031317379464641 | 26875261430996018939663558047746797857529080403119791691957997056669895035 |
| 16 | 17570049414841032310921565514858390890886248656309599776039637316752026735 | 17570049414841032310921565514858390890886248656309609220772603056042456438 |
| 17 | 11551559446991068207445091491242516149964980947477100327288152138378310663 | 11551559446991068207445091491242516149964980947477109772021117877668739929 |
| 18 | 7633120201755795888320788186527412939345243720399617209847638914955554028 | 7633120201755795888320788186527412939345243720399626654580604654245983002 |

Their exact radii are (2^73+w_n)/2^257 with
(w_15,w_16,w_17,w_18)=(3002,2311,1874,1582).
Each is strictly below 2^-183 and separately below 2^-50.

Complete production and independent replay pass for each index, with
1016 panels and 21264880 coefficient pairs per pass per index. The single
aggregate invocation observes four zero-code child exits and conservative
inclusive bounds 110 seconds/5766585 new bytes, below 180/134217728.
All 525 inventoried inputs and their complete tree file sets are preserved
through terminal reporting. This REPRODUCTION supplies four known-method
finite inputs; its separate step-437 critical audit passes as detailed
below. There remain
110 unproduced kernels, L106 audit, full signed assembly, parameter transfer
and strict zero exclusion. No derivative nonvanishing, new BSD case,
arbitrary-curve rank comparison, full Sha or refined formula follows.

## Proof

**Imported theorem and specialization.** Import audited L102, including
its analytic remainders and all outward arithmetic errors. Its standard
inputs are NIST DLMF v1.2.8 (2026-09-15), Taylor's theorem with its
C^(d+1) hypothesis and full remainder, equations
[1.4.35–37](https://dlmf.nist.gov/1.4.vi), continuous integration/change
of variable/bounds [1.4.26/28/29](https://dlmf.nist.gov/1.4.v), exponential
series [4.2.19](https://dlmf.nist.gov/4.2.E19), logarithm series
[4.6.1/4](https://dlmf.nist.gov/4.6), and exponential multiplication
[4.8.16](https://dlmf.nist.gov/4.8.E16). The precise derivative, log
additivity and geometric-sum cases are recorded in L102 and the prior
assessment's source note. No analytical reproof is needed: the difference
here is complete finite execution at four further indices.

Each integer is in 1..128, and the entire unchanged L103 record places
c_* in [3/10,1/2]. All closed panels are positive, including their endpoint
y=1; log and reciprocal retain their smoothness hypotheses, and exp is
entire. The degrees 128+64+64, full degree-256 product, 2^-256 grid,
128-term scalar exponential, sixteen squares and final +/-2^-184
analytic enlargement are unchanged. Thus the only further obligation
for these instances of L102 is correctness of the specified arithmetic.

**Source construction and isolated identities.** The direct coordinator
is retained verbatim from its actual Python `-c` argument as
`coordinator.py`. Its clock starts before setup, imports, reads, inventory
or source generation. It executes no historical entrypoint. Restricted
AST extraction accepts only the recorded step-417 constants/containers,
f-strings, n, addition and str(n) adaptation expression. Each old fragment
must match exactly once in the step-412 template. Complete fragments and
diffs are saved per index as `source-review.json` and `source-diff.txt`.

Both exponential arguments and both pre-clip conditions use the selected
index: producer n*u*a8/(v*8*2^16) and n*u/(8v), replayer
num*endpoint*n/(den*524288) and num*n/(den*8). Panel and final labels
are adapted explicitly. No unrelated numeral, log clip seven, parameter,
loop, array or arithmetic primitive is changed. In particular the midpoint
is not multiplied by n. The complete worker adaptation changes only its
allowed tuple and unique `kernel_435_` module prefix, with full diff saved.

Each full generated source compiles with flags=0, dont_inherit=True,
optimize=0 before import, both in the parent and the fresh child; both
check optimization zero. Each child retains the same two module objects
and checks its selected index, resolved directory, module names and
both actual source hashes before production, after production and after
replay. All three complete identities are persisted. There is no shared
signed-control block. The actual interpreter is Python 3.15.0, while
the prior review inspected documentation labeled 3.15.1; they are not
asserted to be the same version.

**Complete parameter and numerical reconstruction.** Each producer
constructs both 25-term signed arctangent lists and exact sums, the
Machin pi bounds and outward grid, square-root target and both squared
witnesses, both c endpoints, midpoint and delta. Its complete
JSON-normalized record equals step-404's audited L103 record. Every
replayer reconstructs all these values with exact Fraction arithmetic,
uses an independent binary square-root search and checks every directed
conversion and strict square inequality. Both parameter conversions
remain in each full-pass ledger.

Each producer calculates all four endpoint products for interval
multiplication. The independent replayer uses sign cases and checks
each signed floor/ceiling by integer inequalities. It reverses both
convolution traversals, switches the outer factor and reverses integration
accumulation. It reconstructs all 129/65/65 factor slots and 193/257
product slots, every scalar series and sixteen squares, every integrated
coefficient, panel record, running sum and final field. No zero or
high-degree cross term is omitted. Every panel is compared before
acceptance; digests and counts supplement complete recomputation.
There are exactly 1016*(8385+12545)=21264880 coefficient pairs per pass.

The complete returned report and both deep-copied full ledgers are
persisted before comparison. Every report field must equal the exact
worker contract, including status, parameter reconstruction, panels,
pairs, counts, actual radius, stage comparisons, signed rounding scope
and the aggregate-preservation qualification. `replay.json` adds only n.
The producer ledger, replay ledger, saved ledgers, kernel counts and
returned counts agree in all entries:

```text
add=21787232 clip=24386 coefficient_pairs=21264880 convert=5083
divide=716408 enlarge=2034 multiply=21801456 negate=356616 scale=2033
```

**Exact containment.** Each `kernel.json` contains the fully replayed
polynomial sum, final endpoints, midpoint and radius. The polynomial
widths in grid units are respectively 3002,2311,1874,1582. The final
lower endpoint subtracts exactly 2^72 units, and the upper endpoint adds
exactly 2^72 units. Therefore the radius is precisely
(2^73+w_n)/(2D), including reduced forms in saved reports. All w_n<2^73,
so this radius is strictly below 2^74/2^257=2^-183<2^-50.
The workers also test both inequalities separately with exact Fractions.
The successful full arithmetic now instantiates L102 and gives the
four claimed J_n(c_*) enclosures. No transfer to J_n(c) is made.

**Aggregate lifecycle and preservation.** Every entry in historical
initial inventories 417/419/422/424/429/431/433 is reconciled using its
exact applicable post-417/419/422/424/429/431/433 transition suffix.
Each matching before value must agree before applying after; all final
actual bytes/hashes are compared without path exemptions or rebaselining.
Historical preservation and executable-source maps are checked. Entire
first/second-kernel, finite-coefficient and listed earlier four-kernel
trees, stopped 426/429, the outside-historical-cap 429-postmortem archive,
and selected mathematical/source/failure files are inventoried. L106
evidence is preserved by hashing, without using its numerical values.

One timer remains armed throughout setup, generation, all passes,
diagnostics, observed child exits and terminal reporting. A 174-second
work deadline reserves finalization within 180 seconds; children receive
only the remaining work time. All new source/diff/report/ledger/panel
files are within the exclusive evidence directory, bytecode is disabled,
and accounting includes a conservative 131072-byte reporting/diagnostic
reserve. This is observed feasibility for this batch, not a runtime
theorem for future kernels or a hard timer-dispatch guarantee.

Child exits are observed with code zero at approximately
26.8542,53.4914,79.6733,106.6130 seconds. Each persisted status agrees
with its full returned report and captured child stdout. Terminal writing
starts at 106.73328466690145 seconds; the post-terminal finalization
record is 106.76637412491255 seconds. All 525 original inputs, complete
original file sets and fresh source identities are rechecked after
terminal reporting. Final assertions enforce actual elapsed<=110<=180
and final disk bytes plus diagnostic allowance<=5766585<=134217728.
The tool observes coordinator exit code zero. No exact parent-exit
timestamp or repair of any historical timing qualification is claimed.

The later editorial completion of the initially inventoried attempt note
is bound by `drafts/2026-10-23-kernels-fifteen-through-eighteen-document-transition.json`.
It is outside the measured execution and leaves the evidence unchanged.
The sole invocation performs no retry, resumption, other kernel,
derivative assembly or repair of a failed launcher. The separate critical
audit is recorded below.

### Separate critical audit — step 437, 2026-10-24

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-kernels-fifteen-through-eighteen-audit.md`;
the full approved contract is in
`drafts/source-notes/2026-10-24-kernels-fifteen-through-eighteen-audit-coverage.md`.
Evidence is `scripts/four-rational-kernels/step-437/`. The direct
coordinator is retained from its actual `python3 -B -c` argument.
One aggregate invocation executes exactly one complete independent
replay for each n=15,16,17,18, in order. No producer, other kernel,
retry, resumption or stopped launcher executes.

The audit imports the unchanged L102 containment theorem and L103
parameter, with the specialization justified above. The new obligation
is verification of the entire finite evidence and its provenance, not
an analytical reproof. The exact arithmetic below supplies this
obligation for the four claimed midpoint intervals only.

**Full sources and both identity schemas.** Restricted AST data from
step-417 reconstructs every actual step-435 producer/replayer byte from
the step-412 templates. Every old fragment occurs exactly once; the
whole source, complete saved adaptation/diff and actual hash agree.
Both index-dependent exponential arguments, their pre-clip tests and
all labels change together, while the log clip, midpoint and all loops
stay fixed. The five step-424-to-431 worker adaptations and the two
step-431-to-435 changes reconstruct both entire worker texts, reviews
and diffs. The full coordinator, manifest and source map are checked.
All complete source texts compile with flags=0, dont_inherit=True,
optimize=0 before imports. Historical entrypoints are read as data only.

For each index all THREE original identities match the resolved
step-435 directory, kernel_435_n prefix and actual producer/replay
hashes. Fresh identities instead bind the fixed directory, new output,
fixed_replay_437_n module and replay hash. These different five-element
schemas are checked separately; neither substitutes for the other.
The fresh module, paths, index, sentinel and source identity are checked
before installation, after installation and after replay. Captured
original primitives, counter objects and module closures are checked
before and after the numerical pass.

**Lexical signed controls.** The step-433 installer is byte-identical
to step-422 and its entire function body matches the retained signed
block. AST checks enforce its single function, permitted calls, defaults
and absence of imports, global/nonlocal directives and worker namespace
access. Its original captures, all nine wrappers and callback clearing
remain unchanged. The worker/preflight adapt only identity_for's fixed
path and module prefix, check_identity's allowed tuple and preflight's
index tuple. The -422 sentinel and installer labels remain unchanged.
Complete adaptation evidence and diffs are retained.

All four inert preflights precede any numerical replay. Each checks
immutable metadata, separate module/counters/closures, all nine wrappers
after installer return, one deep-copied callback and cleared controls
and ledger. The controls cover all nine sign bins, zeros and endpoints;
their counts are floor=ceiling=57, multiply=36, zero-operand products=11
and sign bins (9,6,3,6,4,2,3,2,1). The controls do not supply kernel values.

**Complete numerical reconstruction.** Every parameter field is rebuilt,
including both arctangent lists, rational pi endpoints, square-root
witnesses, c endpoints, midpoint and delta, with both conversions in the
ledger. Every one of 1016 panels is reconstructed before comparison,
with all 21264880 coefficient pairs per index, 129/65/65 factors,
193/257 products, 128 scalar terms, sixteen squares, signed integration
divisors and running sums. Digest comparison supplements this full
reconstruction. Distinct four-product extrema check the replayer's
sign-case multiplication throughout; integer quotient inequalities
check every floor and ceiling. Addition, negation, clipping, conversion
and division wrappers check their entire returned values.

Inline additions in convolution and log scaling use exact grid integers;
they incur no rounding. Their complete reconstruction and the ledger
identity add=521336+21264880+1016=21787232 account for them separately.
The 2033 scale operations and 2034 enlargements are the exact integer
expressions displayed in the replayer, including the final +/-2^72
enlargement; no omitted floating-point operation is assumed exact.

Each fresh complete report and deep-copied ledger/signed snapshot is
persisted BEFORE comparison. Every report field agrees with the fixed
returned report and exact worker contract; adding only n yields the
fixed replay.json. Both original ledgers, final counts and fresh counts
agree in every entry of the count map above. Each kernel has 21801456
distinct checked multiplications, 716408 divisions, 5083 conversions,
356616 negations, 24386 clips, 521336 additions and 2032 full products.
Both floor and ceiling counts are 22522948. The actual sign-bin counts
are (5644008,5527040,0,5266944,5363464,0,0,0,0), with 896 zero-operand
multiplications; absent bins in the actual pass were tested by the inert
controls. Complete parameter-identity, working, status, completed and
observed-exit records retain every field, including identity_unchanged
and full_returned_report_persisted.

Every final kernel field agrees with full replay and this lemma's exact
endpoint table. The polynomial widths are 3002,2311,1874,1582 grid
units, and the final enlargement is exactly +/-2^72. Thus the four exact
radii are (2^73+w_n)/2^257, allowing reduced fraction encodings.
Each is tested strictly below BOTH 2^-183 and 2^-50 with exact rational
arithmetic. These tests certify the asserted J_n(c_*) intervals; they
do not transfer the parameter or establish a derivative sign.

**Preservation and resources.** All entries of the eight complete
historical inventories 417/419/422/424/429/431/433/435 reconcile through
their exact applicable transition suffixes. Every before value matches
before applying after; no path exemption or rebaselining is allowed.
All 525 step-435 originals, entire source maps, preservation records,
manifest, historical reconciliation, statuses, exits, terminal and
finalization records pass full comparison. Step-435's fixed-tree byte
accounting reproduces 5766585 including its reserve. Its lack of an
exact parent-exit timestamp and older timing qualifications remain.

The new inventory contains 619 inputs, including whole step-435 and
step-433 trees, all retained prior roots, stopped launchers and the
explicitly outside-historical-cap 429-postmortem. Original bytes, whole
tree file sets and fresh sources are checked again after terminal
writing. Child exits are observed with code zero at approximately
32.8789,65.7775,99.1661,131.8661 seconds. Terminal writing starts at
131.98175737517886 seconds; the post-terminal record is
132.01967754215002 seconds. Conservative inclusive bounds are
135 seconds and 442226 new bytes, below 180 and 134217728.

The sole timer starts before imports/setup/reads/source generation and
remains armed through final reporting. The 174-second work limit passes
only remaining time to each child; finalization and diagnostic reserves
are retained. All new executable/output evidence is inside step-437,
bytecode is disabled, and final assertions check actual elapsed and
complete disk bounds after reporting. The tool observes parent exit
zero, without an exact retained parent-exit timestamp. This is measured
feasibility, not a future runtime or hard timer-dispatch guarantee.
The actual interpreter is Python 3.15.0; the source review's rolling
3.15.1 documentation is not represented as the same version.

Post-audit editorial changes to this lemma and the attempt note are bound
by `drafts/2026-10-24-l108-audit-document-transition.json`; they are
outside measured execution. No mathematical hypothesis or DAG edge
changes. The fixed audit passes. L106's audit, 110 unproduced kernels,
signed assembly, parameter transfer, strict zero exclusion and all
arbitrary-curve BSD obligations remain open. This validates a known
method's fixed finite inputs and establishes no new result beyond the
checked mathematical sources.

## Mathlib

Full matching analytic/program coverage is not checked. Supporting
elementary identities recorded in L102/L103 do not certify this source
adaptation, complete execution, lifecycle or this separate audit. No absence or formal
verification claim is made.
