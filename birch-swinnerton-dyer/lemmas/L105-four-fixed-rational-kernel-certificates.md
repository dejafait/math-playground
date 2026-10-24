# L105 — Four fixed rational kernel certificates

## Hypotheses

Use L101 only for the finite kernel definition
J_n(t)=integral_1^128 exp(-n*t*y) log(y)/y dy, L031's exact outward
endpoint rules, audited L102's uniform integration scheme and audited
L103's parameter portion. Set D=2^256 and

c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2*D).

L103 certifies c_* in [3/10,1/2] as the midpoint of its unchanged
containing interval for 2*pi/sqrt(389). The complete fixed evidence is
`scripts/four-rational-kernels/step-417/`. L104 and its step-412 sources
are implementation comparisons only: neither J_1 nor J_2's value or
runtime is a mathematical input. No published rank, complex order,
Sha or period normalization enters these kernel computations.

## Conclusion

For each n in {3,4,5,6}, J_n(c_*) belongs to [l_n/D,u_n/D] below.
The last column is the exact pre-enlargement width w_n in grid units.
The exact midpoint is (l_n+u_n)/(2D) and exact radius is
(2^73+w_n)/(2D), strictly below 2^-183 and 2^-50 in every case.

| n | l_n | u_n | w_n |
|---|---|---|---|
| 3 | 12524596246398253029854743057382825610977041957559923927326496305406378458170 | 12524596246398253029854743057382825610977041957559923936771229271145669808234 | 922672 |
| 4 | 6322754449568274397496865761578710543006533653458007958829314490020765232929 | 6322754449568274397496865761578710543006533653458007968274047455760056126744 | 466423 |
| 5 | 3411514639044930219897346670033525187654143716698646428272847548800960301573 | 3411514639044930219897346670033525187654143716698646437717580514540250981147 | 252182 |
| 6 | 1924828939567964407177809788965844589527982656774197182202210368834261120667 | 1924828939567964407177809788965844589527982656774197191646943334573551690751 | 142692 |

All four production/replay pairs complete in order, with all 1016 panels
and 21264880 coefficient pairs per pass. One aggregate execution records
inclusive bounds 105 seconds and 6025081 new bytes against required
180 and 134217728, preserving all 95 inventoried input files. Every
child exits with code zero before final reporting. This is known-method
REPRODUCTION; the separate step-422 critical audit below passes. It supplies four finite
inputs, not J_n at the exact transcendental parameter, derivative
nonvanishing, a new BSD case or any arbitrary-curve rank comparison.

## Proof

**Imported mathematical scheme.** Import the audited L102 theorem on
all 1<=n<=128, rational c_* in [3/10,1/2], the original 1016 panels,
256-bit fractional grid and full degrees 128+64+64. Its precise primary
inputs include NIST DLMF v1.2.8 (2026-09-15), Taylor's theorem
[1.4.35--37](https://dlmf.nist.gov/1.4.vi), continuous integration and
change of variable [1.4.26/28/29](https://dlmf.nist.gov/1.4), and the
series, derivative and geometric identities cited there, including
exponential multiplication [4.8.16](https://dlmf.nist.gov/4.8.E16).
The full uniform error theorem is imported without reproof. The
pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-23-kernels-three-through-six.md`, with its
source/interface comparison in the referenced source note. The present
specialization produces actual rational intervals; the uniform operation
bound alone gives no practical timing guarantee.

For each permitted index n, alpha=n*c_* lies in [9/10,3]. On each
panel a=(8+j)/8, 0<=j<1016, y=a+s/8 with s in [0,1]. Thus the scalar
argument w=n*c_*a/2^16 is positive and strictly below 384/65536<1/8,
and beta=n*c_*/8 is positive and at most 3/8<8. These verify L102's
two distinct exponential-argument conditions. The remaining log and
reciprocal arguments stay on the original positive panels, including
a=1, with rho=1/(8a)<=1/8. All Taylor smoothness hypotheses hold on
closed panels. No changed logarithm branch or omitted endpoint occurs.

**Parameter and isolated implementation.** The aggregate bootstrap
exclusively creates a new evidence tree and starts its clock before
source generation, input inventory and imports. For each index it reads
the two distinct step-412 implementation texts, requires every exact
replacement to occur once, parses and writes the fresh sources, then
launches an isolated child. No historical entrypoint executes. Each
source-diff.txt and source-review.json preserves the complete adaptation:
scalar argument, beta argument and their range checks, index labels in
panel/final records and the descriptive module label. All other
arithmetic functions, degrees and loops remain unchanged.

For c_*=u/v the producer uses n*u*a8/(v*8*2^16) and n*u/(8*v);
the independent replay uses num*endpoint*n/(den*524288) and
num*n/(den*8). Here a8=endpoint=8a. Both range checks precede containing
clips. The midpoint itself is never multiplied by n. Separate children,
modules, directories and saved ledger copies prevent cross-index state
or shared n-dependent arrays.

Each producer reconstructs the entire L103 parameter record: all
25 signed arctangent terms at each of 1/5 and 1/239, adjacent partial
sums, Machin combination, outward pi endpoints and square-root witness.
Complete record equality with step-404 parameter.json and exact midpoint
equality are checked before production. During the sole full replay,
the independent parameter routine reconstructs all fractions, uses
binary search for the square root and checks both strict squared
inequalities, rational conversions, range and delta<=2^-50. These
are imported elementary enclosures from L031/L103 and the inspected
arctangent series [DLMF 4.24.3](https://dlmf.nist.gov/4.24.E3).
No preliminary replay ledger is accumulated: its two parameter
conversions belong to the full replay, matching the producer's full
ledger. Each n directory saves its complete parameter and identity record.

**Complete arithmetic evidence.** Each scalar logarithm retains 128
odd-power terms; the scalar exponential retains 128 terms, its one-grid
unit enlargement and sixteen rounded/clipped squares. Each panel builds
all 129/65/65 factor slots, both complete convolutions with 8385 and
12545 pairs, and all 193/257 product slots, including zeros. Every
signed coefficient is integrated using the positive divisors 1,...,257,
then multiplied by the scalar exponential and divided by eight. All
panel records and running sums are saved separately per n in panels.jsonl.
Full scalar traces, arrays and divided coefficients are reconstructed
during replay and compared through their prescribed stage digests;
complete panel values and final endpoints are compared exactly as well.
Digests alone are not the replay.

The producer selects extrema of all four endpoint products. Independent
replay selects extrema by sign cases, obtains floor/ceiling via
absolute-value divmod and checks their defining integer inequalities at
every conversion, multiplication and positive division. It reverses
both convolution traversals, exchanges the outer factor and sums the
signed primitive terms in reverse order. Exact dyadic additions preserve
the sums. Each separate replay.json records all stage comparisons PASS,
1016 panels and 21264880 pairs. Each producer-ledger.json and
replay-ledger.json is a persisted independent snapshot; their complete
counts agree:

| primitive | count per kernel per pass |
|---|---:|
| add | 21787232 |
| clip | 24386 |
| coefficient_pairs | 21264880 |
| convert | 5083 |
| divide | 716408 |
| enlarge | 2034 |
| multiply | 21801456 |
| negate | 356616 |
| scale | 2033 |

Each kernel.json retains the exact polynomial sum, final endpoints,
midpoint, radius, thresholds and ledger. L102's outward arithmetic
encloses the integrated exact polynomial approximation, retaining all
scalar, coefficient and integration rounding. Separately, L102 bounds
the analytic discrepancy between that approximation and the true
integral by strictly less than 2^-184, including all panel remainders.
The executed final enlargement
is exactly 2^72 grid units on each side, namely 2^-184. It therefore
gives true containment. The saved pre-enlargement widths are exactly
the w_n in the conclusion; all are positive and less than 2^73.
Consequently (2^73+w_n)/(2D)<2^74/(2D)=2^-183, and 2^-183<2^-50.
The executable producer and replay each check both exact strict tests.
No numerical differentiation, approximate zero or parameter transfer
is used in this conclusion.

**Preservation and aggregate resource evidence.** The initial inventory
covers all existing first-kernel, second-kernel and finite-coefficient
files, selected canonical L031/L101/L102/L103/L104 inputs, the prior
assessment/source note, three retained failures and the unfinished
attempt note: 95 files. Final complete rehashes and original tree file
sets agree. Both fresh arithmetic sources per index, worker and exact
bootstrap remain unchanged. preservation.json and source-hashes.json
retain this evidence. Later canonical documentation edits are editorial
after this measured preservation boundary; the attempt-note transition
is recorded separately in drafts/2026-10-23-four-kernel-document-transition.json.

One parent clock and terminal signal deadline cover setup, all source
writing, input reads, isolated children, inventories and final reports.
Each child launch receives only the remaining aggregate work time to
174 seconds. No timeout, arithmetic failure, retry, resumed run or
unapproved kernel occurs. Observed child exits (seconds from the same
start) are 25.824810625053942, 51.55866258405149,
76.76381437503733 and 102.14102283399552 for n=3,4,5,6 respectively,
all with return code zero. Terminal reporting starts after preservation
at 102.1715818750672 seconds; finalization records
102.17291866708547 seconds after the terminal write. The measured
execution exits zero after its final assertions and printed report.
Inclusive bounds are 105 seconds and 6025081 new bytes, including a
73728-byte reporting/diagnostic reserve; final assertions retain an
8192-byte allowance. The terminal timer remains armed. This is observed
completion, not a hard signal-dispatch guarantee or a measured exact
parent-exit timestamp. Historical n=1 finalization and n=2 bootstrap/
process-exit qualifications remain unchanged.

The separate step-422 audit below validates this finite specialization. Remaining
fixed-route obligations are 122 other kernels, full signed assembly,
parameter transfer and strict zero exclusion, with L030/L031 coefficient/
sign and L099/L101 lower-vanishing inputs retained for derivative use.
The arbitrary-curve rank gap, full Sha finiteness and refined formula
remain independent and unresolved.

### Separate critical audit attempt — 2026-10-23, step 419

The approved single audit stopped at its first report-identity failure;
it does **not** complete this lemma's critical audit. The immutable evidence
is `scripts/four-rational-kernels/step-419/`. Its historical/source checks
reconcile the complete step-417 bootstrap/worker, all four exact source
adaptations and diffs, original source hashes, manifest, observed child
exits, byte accounting and the exact attempt-note editorial transition.

Only the n=3 replay ran. Its `run` returned after complete parameter,
1016-panel, 21264880-pair, final-endpoint, radius and operation-ledger
checks, with the distinct signed wrappers active. The fresh worker then
failed at line 31, comparing the returned report plus its index against
the saved report. Its copied deterministic control block executes at
module scope and contains `for n in (..., 2*D+1)`. Thus it overwrites
the worker's selected index with `2*D+1`, where D=2^256, before the
comparison. The n=3 directory and independently loaded replay module
were fixed earlier; their mathematical index remains three. This is
an audit-harness namespace error, not an established certificate error.
The return report was not persisted, subsequent distinct ledger/radius
comparisons were not reached, and n=4,5,6 were not attempted. Consequently
no complete per-kernel or four-kernel critical-audit PASS is claimed.

The post-stop static diagnosis is
`drafts/2026-10-23-four-kernel-audit-static-diagnosis.json`; it executes
no arithmetic replay. The parent observed child exit code one at
31.107311832951382 seconds. Terminal bounds are 34 seconds and 164026
new bytes against 180 and 134217728. All 170 inventoried inputs and
fresh source identities were preserved, rechecked after terminal
reporting. No producer, retry, resumption or other kernel executed.
These resource bounds describe a stopped audit, not four successful
audits. Historical timing qualifications and all mathematical claims
above retain their prior status; full separate critical validation
remains pending. The recorded failure does not refute the integration
scheme or BSD.

### Separate critical audit — 2026-10-23, step 422

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-23-isolated-four-kernel-audit.md`. One fresh
aggregate audit passes for exactly the four original certificates. Its
complete evidence is `scripts/four-rational-kernels/step-422/`. Step 419
remains stopped, with its original failure, sources and reports preserved;
neither its entrypoint nor any producer runs. The mathematical inputs and
conclusions above are unchanged. This establishes separate finite-certificate
validation, not new mathematics beyond the checked sources.

**Applicability and source identity.** L102 is imported with the unchanged
parameter, positive panels, degrees, complete product and analytic allowance
specified above. Both index-dependent exponential arguments are checked in
each independent implementation, before clipping. The audit parses the
step-417 bootstrap as data, verifies its entire embedded worker, and exactly
reconstructs all eight arithmetic sources and all four complete diffs from
their specified step-412 base texts. Each replacement is unique; complete
source equality and original source hashes hold. The full historical
manifest, child-exit records, terminal/finalization records, original byte
accounting and source/parameter/status identities are reconciled. Both the
post-417 attempt-note transition and the exact two-file post-419 editorial
transition match their recorded before/after hashes and lengths. No pathname
exemption is used.

**Lexical isolation before arithmetic.** The installer contains the entire
retained signed-wrapper/control block unchanged inside a genuine function,
with explicit parameters `replay, D, signed, save`, followed only by its
explicit tuple return. Its AST body is compared with the retained block,
which is also compared with the step-415 source. Static review checks all
assignments and calls, absence of global/nonlocal directives, dynamic
evaluation and worker-name access, and all defaults/decorators/annotations.
Only the nine prescribed replay primitives are installed. Each wrapper
captures its original primitive and its own counters; the product wrapper
also captures its intended replay module. Thus wrapping does not recursively
capture an already replaced primitive. The installer definition is evaluated
in one fresh explicit dictionary, then invoked with its four arguments.
The documented rules are Python's [binding and name resolution,
§§4.2.1–2](https://docs.python.org/3/reference/executionmodel.html#binding-of-names)
and the [single-namespace exec case](https://docs.python.org/3/library/functions.html#exec),
as inspected in the ready source note. Actual execution uses Python 3.15.0,
recorded in `audit-manifest.json`; the source review used rolling 3.15.1
documentation. These rules alone do not certify arbitrary programs.

Before any kernel, each index 3,4,5,6 passes an inert preflight of this
actual installer. The doubles have no kernel entrypoint. The immutable
identity tuple contains the index, canonical input/output paths, unique
module name and replay-source hash. The worker has exactly one identity
binding site. Preflight retains sentinel index −422 and checks the tuple,
both paths, actual module identity/name/file/hash, the exact nine replaced
attributes, all other module fields and every wrapper's lexical captures.
Each complete control report has 36 multiplications, 57 signed floors and
57 ceilings, nine sign-bin counts (9,6,3,6,4,2,3,2,1), and eleven
zero-operand multiplications. There is exactly one callback write, then
zero counters and an empty preliminary ledger. Every retained wrapper is
called after installer return, including an inert zero-product shape test,
so a lost closure cannot be hidden by installation-time success. Complete
preflight records are saved in `identity-preflight.json`; this finite test
is supplemented by the static review, not treated as universal correctness.

**Full mathematical replay.** Each real per-index module is loaded once
and checked against its identity immediately before/after installation and
after its sole full replay. Every parameter term, adjacent arctangent sum,
Machin conversion, square-root inequality, grid endpoint, midpoint and delta
is reconstructed during that replay, with complete equality against the
unchanged step-404 record and the per-index parameter. Its two parameter
conversions remain in that index's ledger. All 1016 panels and 21264880
coefficient pairs are reconstructed per index, retaining all scalar terms,
sixteen squarings, coefficient slots, signed divisors, panel sums and exact
final enlargement. Full panel/stage and final comparisons pass; hashes do
not substitute for reconstructing the arithmetic.

The distinct wrappers test every encountered multiplication against all
four endpoint products and every floor/ceiling against separate quotient
inequalities, with signed division, conversion, addition, negation and
clipping checks. Each actual replay records 21801456 multiplications,
716408 divisions, 5083 conversions, 356616 negations, 24386 clips,
521336 wrapped additions and 2032 full products. Its 22522948 floors
and equally many ceilings are exactly multiply+divide+convert+1; the last
one is the separate parameter quotient. The full addition count 21787232
also includes 21264880 inline convolution additions and 1016 log-constant
combinations. All 2033 scales and 2034 enlargements remain checked in the
source and complete replay. Actual sign bins are
(5644008,5527040,0,5266944,5363464,0,0,0,0), with 896 zero-operand
multiplications; the separate controls cover the missing crossing cases.

Immediately after each replay returns, its complete report is deep-copied
and persisted before any subsequent comparison; the complete ledger and
nested signed counters are separately copied and saved. Adding exactly the
index from the unchanged identity makes that whole report equal to the
original saved `replay.json`. Every field and both complete producer/replay
ledgers agree. No field is dropped and no cumulative-only ledger is used.
The polynomial sums, displayed endpoints and midpoints all agree with the
conclusion table. Exact rational checks give each radius
(2^73+w_n)/2^257, with the four original w_n, and both strict inequalities
radius<2^-183<2^-50. The enlargement is exactly ±2^-184, so L102 supplies
containment for J_n(c_*), without a transfer to the transcendental c.

**Aggregate boundary.** One clock starts before fresh setup, source
generation, input inventory, imports and preflight. All four child exits
are observed with return code zero, at elapsed seconds
31.74247133312747, 63.821516582975164, 95.73855658294633 and
128.0029280409217. Terminal reporting begins at 128.04708308307454;
post-terminal preservation is checked again before finalization, whose
elapsed measurement is 128.0614997080993. All 194 inventoried inputs,
original tree file sets and five fresh source/data identities remain
unchanged. The process exits zero after its final assertions. Inclusive
bounds are 131 seconds and 250769 new bytes, including the reporting
reserve, versus 180 and 134217728. The terminal timer stays armed and the
post-report assertions include the final allowance. This is observed
completion under the cap, not guaranteed signal dispatch or an exact
parent-exit timestamp. Historical n=1, n=2 and step-417 timing
qualifications remain unrepaired and explicit.

This completes the separate audit of these four fixed certificates only.
There are still 122 missing kernels, the full signed derivative assembly,
parameter transfer and strict zero exclusion. No derivative nonvanishing,
new BSD case, uniform production or arbitrary-curve rank comparison follows.

## Mathlib

Full theorem/algorithm/certificate coverage is not checked. The previously
inspected supporting identity
[Real.four_mul_arctan_inv_5_sub_arctan_inv_239](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Arctan.html#Real.four_mul_arctan_inv_5_sub_arctan_inv_239)
is supporting parameter coverage only, without a pinned local compilation.
It does not formally verify these finite certificates or the integration
implementation.
