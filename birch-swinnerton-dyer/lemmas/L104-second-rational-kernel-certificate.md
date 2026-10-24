# L104 — Second complete rational kernel certificate

## Hypotheses

Use L101's definition
J_2(t)=integral_1^128 exp(-2*t*y) log(y)/y dy, L031's exact outward
endpoint rules, audited L102's uniform rational integration scheme and
the parameter portion of audited L103. Write D=2^256. The unchanged
parameter is

```
c_l*D = 36887902191165742374446831090090100164633110307723623187031015736440321082816
c_u*D = 36887902191165742374446831090090100380471044238365418461395933078627191865791
c_* = (c_l+c_u)/2
```

The new fixed evidence and isolated sources are in
`scripts/second-rational-kernel/step-412/`. In particular `run.py` is
the saved aggregate execution body, not the historical first-kernel
entrypoint. This result uses neither the value of J_1 nor its runtime,
published complex order, rank, Sha or period normalization. L101 only
defines the finite kernel here; no derivative identity is applied.

## Conclusion

At this exact rational midpoint, J_2(c_*) belongs to [l,u], where

```
l*D = 27752108342762384198586753289291805502031167688405252130383566291743051605286
u*D = 27752108342762384198586753289291805502031167688405252139828299257482344076057
```

Its exact midpoint is

```
55504216685524768397173506578583611004062335376810504270211865549225395681343 / (2*D)
```

and its exact radius is

```
(2^73 + 2043379)/(2*D) < 2^-183 < 2^-50.
```

All 1016 panels and all 21264880 coefficient pairs per pass pass complete
production and independent replay. Recorded production execution bounds
are 28 seconds and 1661714 new bytes, below 180 and 134217728, with the
historical finalization qualification below. All 62
inventoried input files, including every existing first-kernel and
finite-coefficient artifact, are preserved. The terminal timer remains
armed in the saved final-reporting body. The separate critical audit
passes complete replay and distinct signed checks, preserving 83 files
under fresh inclusive bounds of 34 seconds and 145485 bytes. This is
known-method REPRODUCTION. It certifies J_2(c_*), not J_2 at the
unknown exact transcendental parameter c, nor any derivative or BSD claim.

## Proof

**Imported scheme and parameter.** Import L102's already audited uniform
theorem for every integer 1<=n<=128 and supplied rational c_* in
[3/10,1/2]. Its primary inputs are NIST DLMF v1.2.8 (2026-09-15),
Taylor's theorem [1.4.35--37](https://dlmf.nist.gov/1.4.vi), continuous
integration/change of variable [1.4.26/28/29](https://dlmf.nist.gov/1.4),
and the series, derivatives and multiplication identities cited precisely
in L102, including [4.8.16](https://dlmf.nist.gov/4.8.E16).
Those theorems and L102's analytic/rounding bounds are imported without
reproof. The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-23-second-rational-kernel-certificate.md`;
the theorem/interface comparison is in its referenced source note.
This computation supplies an actual finite interval under that theorem,
not a new analytic bound or practical consequence of an operation count.

Both fresh implementations reconstruct the entire fixed
`scripts/first-rational-kernel/step-404/parameter.json` record exactly.
The producer reconstructs all 25 signed arctangent terms at each of
1/5 and 1/239, both adjacent partial sums, their Machin combination,
outward pi endpoints and integer square-root witness. The independent
replayer reconstructs those exact fractions and uses binary search for
the square-root witness, checking both strict squared inequalities.
Each directed rational conversion is checked by signed integer
floor/ceiling inequalities. These are the elementary enclosure rules
and Machin identity already justified in L031 and L103; the arctangent
series input is [DLMF 4.24.3](https://dlmf.nist.gov/4.24.E3).
The complete record equality, not just equality of a digest or midpoint,
is required. `parameter.json` and `parameter-identity.json` record this.
Thus L103's c_l,c_u,c_*,delta are unchanged, c_* belongs to [3/10,1/2],
and delta<=2^-50. In particular the midpoint field is not doubled.

**Specialization and fresh sources.** For n=2, alpha=2c_* belongs to
[3/5,1]. On each original panel a=(8+j)/8, 0<=j<1016, use
y=a+s/8, 0<=s<=1. The scalar exponential input is exactly
w=2c_*a/2^16, so 0<w<128/2^16<1/8. The panel coefficient input is
beta=2c_*/8 in [3/40,1/8], within L102's range (0,8]. These identities
are distinct obligations: changing the scalar alone would not compute
the prescribed integrand. The producer uses
`exponential(2*u*a8, v*8*(1 << 16))` and `cv(2*u,8*v)` for c_*=u/v;
the separate replayer uses `exp_series(num*endpoint*2,den*524288)`
and `enclose(num*2,den*8)`. Both check positive scalar/beta ranges
before clipping. All log, reciprocal and subsequent containing clips
retain L102's hypotheses: a in [1,128), the reduced logarithmic
argument in [0,1/3], rho=1/(8a)<=1/8 and 1/a<=1. The endpoint a=1
uses the same valid zero logarithm argument. All functions are smooth
on the entire positive panels; no logarithm branch changes.

The bootstrap starts its clock before directory creation, input reads,
source generation or module imports. It exclusively creates the new
directory, reads each separate historical implementation as text and
requires each exact replacement to occur once. `source-diff.txt` and
`source-review.json` retain the complete changes: both arguments in
each implementation, n=2 labels, added range checks and strict
<2^-50 acceptance. The separate arithmetic functions and all full
loops remain unchanged. The resulting sources are parsed and compared
with the expected exact text before loading either new module; their
initial/final hashes agree. Neither the old runner nor a top-level
historical execution source is imported or executed. No producer
arithmetic is imported by the independent replayer.

**Complete construction and replay.** Each scalar log retains 128
odd-power terms; the scalar exp retains 128 terms, its one-grid-unit
enlargement and exactly sixteen rounded/clipped squares. The polynomial
factors have lengths 129,65,65. ER retains all 8385 pairs and (ER)H
all 12545 pairs, including zeros, with lengths 193 and 257. All 257
coefficients are integrated by outward division by their positive
divisors, then multiplied by the scalar exponential and divided by
eight for dy=ds/8. Every panel integral and cumulative sum is saved
in `panels.jsonl`, with its endpoints, scalar values, integrated
polynomial and full-stage digests. Stage arrays and scalar traces are
recomputed completely during replay; no digest substitutes for their
arithmetic reconstruction. Every reconstructed panel record is compared
exactly, as are the complete final endpoints and both count ledgers.

The producer uses four-product extrema. The replayer uses independent
sign-case extrema and absolute-value divmod for signed floor/ceiling,
checking their defining inequalities at every multiplication,
conversion and division. It reverses both convolution traversals and
the outer factor, and sums signed primitive terms in reverse order.
These exact dyadic additions preserve the sum. Its preliminary
parameter-only ledger is cleared before the sole full replay, which
reconstructs the parameter again. The producer's parameter conversions
remain included in its full ledger. The complete per-pass counts are
21264880 pairs, 21801456 multiplications, 716408 divisions, 5083
conversions, 21787232 additions, 356616 negations, 24386 clips,
2033 integer scales and 2034 enlargements. `replay.json` records exact
ledger equality and all-stage PASS for all 1016 panels. This is one
producing pass and one replay, with no benchmark, retry or third kernel.

The summed polynomial endpoints before analytic enlargement are

```
27752108342762384198586753289291805502031167688405252135105932774612696818982
27752108342762384198586753289291805502031167688405252135105932774612698862361
```

Their difference is 2043379 grid units. The final enlargement is exactly
2^72 grid units at each end, namely L102's 2^-184 allowance for all
analytic panel remainders. Its hypotheses and complete arithmetic
construction have just been checked, so L102 proves that the resulting
interval contains the true integral J_2(c_*). The radius is exactly
(2^73+2043379)/(2D). Since 2043379<2^73, it is strictly less than
2^74/(2D)=2^-183, and hence strictly less than 2^-50. `kernel.json`
retains exact endpoints, midpoint, radius and both thresholds; the
replayer compares all these values by exact rational arithmetic.

**Resources and preservation.** `initial-inventory.json` records hashes
and lengths of all files in the first-kernel and finite-coefficient
directories, plus nine selected canonical/source/failure inputs.
`preservation.json` rehashes all 62 files, requires their exact inventory
equality and unchanged historical directory file sets, and checks both
new source hashes. No original is written. Full copies of old artifacts
are unnecessary; every original is checked, including retained failures.

The work deadline is 174 seconds; finalization retains a terminal
180-second timer. Signal dispatch itself is not a mathematical or hard
timing guarantee. Successful measured completion is separate:
`status.json` records 25.281850165920332 seconds before writing;
`finalization.json` records 25.282420499948785 after that write;
`terminal-report.json` records 25.282815540907905 after finalization
writing. The saved body then asserts exact disk and elapsed
bounds, prints the report and asserts elapsed time again. Its retained
terminal timestamp precedes its own write; there is no separate historical
post-exit log or executable bootstrap. These source assertions and reported
timestamps do not independently certify historical process completion.
Recorded conservative bounds are 28 seconds and 1661714
new bytes, including all new sources, certificates, 65536 report-reserve
bytes and 8192 diagnostic bytes. Actual pre-status disk usage is 1587986
bytes. The intended accounting includes setup through final preservation/reporting;
no timer is cleared in the saved body before finalization. `status.json` reports PASS,
complete replay and no first failure. These measurements concern only
this n=2 instance and provide no bound for any remaining kernel.

**Qualifications and use.** This is a known-method fixed finite input;
the source coverage and error theorem predate this invocation. Its
separate critical audit passes below. L101 would still need the
other 126 kernels, signed finite assembly, parameter propagation,
all errors and strict zero exclusion. Nothing here supplies a
derivative, a new BSD case, arbitrary-curve rank comparison, full Sha
finiteness or a refined leading-coefficient formula.

### Separate critical audit — 2026-10-23, step 415

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-23-second-rational-kernel-audit.md`.
This audit imports the unchanged L102 theorem and L031/L103 parameter
rules with precisely the primary citations above. It establishes executed
certificate validity, not a new integration theorem. The complete fresh
source and evidence are in `scripts/second-rational-kernel/step-415/`.
The self-contained `bootstrap.py` retains its embedded `audit-body.py`;
it requires exclusive creation of the step-415 output directory and
intentionally refuses an in-place rerun. The actual bounded invocation
does not rerun production or any old runner.

**Source, parameter and analytic applicability.** Static review checks
the complete separate producer/replayer and saved aggregate body. The
fresh harness parses the old body without executing it, extracts its
unique literal transformation record, checks every unique replacement
against both original source files, and compares all resulting bytes,
manifest/source-review hashes and sizes, and the complete unified diff.
Both scalar and panel arguments are the n=2 arguments displayed above;
neither the parameter midpoint nor either integrand factor is left at n=1.
The original report has one additional `n:2` field added by its runner;
the audit verifies exact equality after adding exactly that field to the
fresh replay result, without discarding any mismatched field.

The single full replay checks every parameter term, adjacent partial
sum, Machin conversion, squared root inequality, c endpoint, midpoint
and delta, with complete record equality to both step 412 and step 404.
Consequently the exact midpoint is in [3/10,1/2]. For every panel,
alpha=2c_* is in [3/5,1], w=alpha*a/2^16 is in (0,1/8),
beta=alpha/8 is in [3/40,1/8], rho=1/(8a) is in (0,1/8],
and 1/a is in (0,1]. The binary log reduction has 0<=z<1/3,
with z=1/3 only for the separately evaluated log 2. Every positive
log/reciprocal argument and smooth real Taylor interval therefore meets
the imported scheme, including a=1 and the zero logarithm. Clips use
the containing ranges proved in L102; nonempty intersection alone is
not substituted for that containment argument.

**Complete arithmetic and independent checks.** Only the unchanged
step-412 replay module executes. Its scalar series, sixteen squares,
all 129/65/65 factor entries, both full convolutions, 257 positive
integration divisors, every panel record and running sum are reconstructed.
Convolution reverses both indices and exchanges the outer factor; the
primitive integral sums in reverse order. Exact integer addition and
the complete saved panel equality retain all signed terms and zero slots.
Stage hashes supplement these complete computations.

Every encountered signed quotient is checked both by the replay's
absolute-value divmod and by independent integer floor/ceiling formulas
and defining inequalities. Every multiplication is also checked against
all four endpoint products; positive division, conversion, addition,
negation and clipping are independently compared with their exact rules.
All 2032 convolution lengths and complete pair counts are checked.
`complete-replay.json` records 21801456 checked multiplications, 716408
divisions, 5083 conversions, 356616 negations, 24386 clips, and 22522948
checks of each directed quotient. There are 521336 wrapped additions;
the 21264880 direct convolution additions and 1016 scalar-log additions
give the full ledger total 21787232. All 2033 integer scales and 2034
enlargements agree as well. Every operation count matches the original
producer and replay, in addition to complete data equality.

The actual multiplication sign counts are
(5644008,5527040,0,5266944,5363464,0,0,0,0), with 896 exact zero
operands. Thus this kernel does not itself exercise crossing intervals.
Separate deterministic 36-pair controls exercise all nine sign cases,
zero and zero-endpoint intervals; their sign counts are
(9,6,3,6,4,2,3,2,1). Separate signed quotient controls include negative,
positive, zero and exact endpoint values. These controls are saved before
resetting their counters and the replay ledger; they are not a second
kernel run and do not inflate the complete-replay counts.

The exact final endpoints and midpoint agree with the statement. The
pre-enlargement width is exactly 2043379 grid units, and the final
enlargement is exactly 2^72 at each endpoint. L102 then supplies true
integral containment. Exact rational comparisons give the actual radius
(2^73+2043379)/2^257, strictly below both 2^-183 and 2^-50. The
weaker n=1 acceptance convention is not used.

**Preservation and resources.** The audit inventories all 18 fixed
step-412 files, its original 62 inputs and three additional canonical/
assessment files, for 83 files. It checks every original hash/length,
both old directory file sets, and the complete original preservation
record. After replay every inventoried file and directory set is
unchanged; there are no pathname exemptions or mismatches.
`historical-review.json` retains the full source, resource and status
comparison. Reconstructing the historical pre-status file set gives
1587986 bytes; adding its 65536 reporting reserve and 8192 diagnostic
allowance gives 1661714. All later historical file sizes fit that bound.
The reported times are ordered and below 28 seconds, but the descriptive
bootstrap and pre-write terminal timestamp have the limitations stated
above. Fresh measurements do not repair those historical limitations;
L103's original n=1 finalization qualification also remains unchanged.

The fresh parent clock starts before setup, imports, source writing and
inventories. A single aggregate cap covers the explicit harness, the
one replay, diagnostics, preservation and reports. The child exits
successfully at 31.132010750006884 seconds; the parent measures
31.132945334073156 seconds after writing its terminal report.
`terminal-report.json` and `finalization.json` retain inclusive bounds
34 seconds and 145485 bytes against required 180 and 134217728,
including 73728 reserved reporting/diagnostic bytes. The terminal timer
remains armed, and post-finalization assertions and the observed process
exit code zero pass. No exact parent process-exit time or hard signal
dispatch guarantee is inferred. No failure, retry, producer or other
kernel executes. Subsequent canonical documentation edits are editorial
transitions recorded separately in the working record, after preservation.

This validates L104's fixed finite input only. It supplies neither
J_2(c), the other 126 kernels, full signed assembly, parameter transfer,
zero exclusion, nor any arbitrary-curve rank comparison.

## Mathlib

Full algorithm/certificate coverage is not checked. Supporting Machin
coverage remains the previously inspected
[Real.four_mul_arctan_inv_5_sub_arctan_inv_239](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Arctan.html#Real.four_mul_arctan_inv_5_sub_arctan_inv_239),
without a pinned local compilation. This supporting identity does not
formally verify this implementation or its complete certificate.
