# L107 — Fixed kernels eleven through fourteen

## Hypotheses

Use L101's definition
J_n(t)=integral_1^128 exp(-nty) log(y)/y dy, L031's rational
endpoint rules, audited L102's unchanged 1016-panel method, and the
audited parameter portion of L103. Set D=2^256 and use the exact rational

c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2D).

Its complete certified parameter record is unchanged from L103:
c_l D=36887902191165742374446831090090100164633110307723623187031015736440321082816,
c_u D=36887902191165742374446831090090100380471044238365418461395933078627191865791,
3/10<=c_l<=2*pi/sqrt(389)<=c_u<=1/2 and
delta=(c_u-c_l)/2<=2^-50.

The fixed evidence is `scripts/four-rational-kernels/step-431/`.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-kernels-eleven-through-fourteen.md`.
The isolated audited step-412 producer/replayer supply source templates;
the exact retained step-417 adaptation expression is data only.
Step-424's worker supplies an implementation interface, not kernel values
or analytical inputs. L106 numerical values and all signed audit
installers and failed launchers are excluded.

## Conclusion

For n=11,12,13,14, respectively, J_n(c_*) belongs to [l_n/D,u_n/D]
with the following exact grid endpoints:

| n | l_n | u_n |
|---|---|---|
| 11 | 158200451785025084813092823415740853098350890724103904112314399309528890177 | 158200451785025084813092823415740853098350890724103913557047365048819330246 |
| 12 | 100256928494528035603756285614026764594232863130746102392840965326271433596 | 100256928494528035603756285614026764594232863130746111837573931065561869389 |
| 13 | 64138846967788004697611734515223993294838296179321397687364049709405962119 | 64138846967788004697611734515223993294838296179321407132097015448696395255 |
| 14 | 41369590064272697228755091127323947406027702833369538972367709739959250000 | 41369590064272697228755091127323947406027702833369548417100675479249681460 |

Their exact radii are (2^73+w_n)/2^257, where
(w_11,w_12,w_13,w_14)=(12677,8401,5744,4068).
Each radius is strictly less than 2^-183 and 2^-50.

Complete production and independent replay passed for each index,
including all 1016 panels and 21264880 coefficient pairs per pass.
One aggregate invocation recorded conservative inclusive bounds
110 seconds and 5778675 new bytes, below 180 and 134217728, with
all four child exits observed and 367 inventoried inputs preserved
through terminal reporting.

This is REPRODUCTION of the assessed known method. Its separate step-433
critical audit passes, as detailed below. It leaves 114 unproduced kernels, L106's independent audit,
full signed assembly, parameter transfer and strict zero exclusion.
No derivative nonvanishing, arbitrary-curve rank comparison, full Sha
finiteness or refined BSD formula follows.

## Proof

**Imported containment theorem and applicability.**
Import audited L102's entire rational integration/error theorem. Its
standard analytic inputs are Taylor's theorem with the smoothness
hypothesis and full remainder, NIST DLMF v1.2.8 equations
[1.4.35–37](https://dlmf.nist.gov/1.4.vi), continuous integration
and its bound [1.4.26/28/29](https://dlmf.nist.gov/1.4.v),
the exponential series [4.2.19](https://dlmf.nist.gov/4.2.E19),
logarithm series [4.6.1/4](https://dlmf.nist.gov/4.6),
and exponential multiplication [4.8.16](https://dlmf.nist.gov/4.8.E16).
The exact source cases are retained in L102 and the assessed source
note. This step does not reprove the analytic theorem: its difference
from those sources is execution and complete finite evidence.

All four integers lie in L102's range 1<=n<=128; the complete L103
parameter gives c_* in [3/10,1/2]. Hence every positive panel retains
the log/reciprocal smoothness hypotheses, including y=1; exp is entire.
The degrees 128+64+64, complete degree-256 product, grid 2^-256,
128-term scalar series, sixteen squarings, and final enlargement
+/-2^-184 are unchanged. L102 therefore supplies containment as soon
as the prescribed arithmetic has been executed correctly.

**Exact source specialization and isolation.**
The standalone coordinator is retained verbatim from the actual Python
`-c` argument as `coordinator.py`; it has no enclosing nested source
literal. Its clock starts before setup, reading, inventory and generation.
It reads the historical adaptation assignment by restricted AST extraction
as data and never executes a historical entrypoint. For each n it requires
exactly one match for every old fragment in the audited step-412 texts.
The complete old/new fragments and unified diffs are saved separately
in `n-<n>/source-review.json` and `source-diff.txt`.

Both actual exponential arguments and both pre-clip conditions use n:
n*u*a8/(v*8*2^16) and n*u/(8v) in the producer,
num*endpoint*n/(den*524288) and num*n/(den*8) in the replayer.
Panel and final labels are changed explicitly; the log bound seven,
midpoint record, loops, arrays and all independent arithmetic remain intact.
No expected interval or radius is copied from an earlier kernel.

The worker changes are saved in `worker-source-review.json` and
`worker-source-diff.txt`. The parent compiles every entire generated
text in exec mode with flags=0, dont_inherit=True, optimize=0, before
imports. Each fresh child checks optimization zero, separately compiles
both full texts before importing them, and binds its index, resolved
directory, module names and producer/replayer byte hashes. It checks
these identities before and after production and replay. No shared
signed-control block runs and no index is rebound by such a block.
The interpreter is Python 3.15.0; the prior assessment inspected the
official 3.15.1 documentation, so that documentation version is not
represented as the installed version. Compilation and process semantics
are execution guards, not substitutes for arithmetic correctness.

**Complete parameter and arithmetic replay.**
Each producer independently constructs the entire L103 record: both
25-term arctangent lists and sums, exact Machin pi bounds, outward pi
grid, square-root target and squared witnesses, c endpoints, midpoint
and delta. Its full JSON-normalized record equals the original L103
record before production. The independent replayer reconstructs every
term and sum with Fraction arithmetic, finds the square-root witness by
binary search, checks both strict squares and every signed conversion,
and compares the complete stored record. The two parameter conversions
remain in that index's complete full-pass ledger.

For every panel, the producer uses four endpoint products and min/max;
the replayer independently chooses extrema by sign cases and checks
signed floors/ceilings by integer inequalities. It reverses both
convolution traversals, switches the outer factor and reverses the
integration accumulation. All 129/65/65 factor slots and 193/257 product
slots are computed, with no omitted zero or high-degree terms. Every
panel field, stage digest, running sum and final field is reconstructed
and compared, rather than inferred from counts. Complete fresh passes
cover all 1016 panels and all 1016*(8385+12545)=21264880 product pairs
each. Digests supplement the full recomputation.

The returned report is deep-copied and persisted as `returned-report.json`
before any report comparison. Producer and replayer ledgers are separately
deep-copied and persisted before comparison. The complete returned report
is compared with its saved copy and with the exact full report contract;
`replay.json` adds only that child's n identity. Both saved ledgers,
the returned counts and kernel counts agree in every entry:

```text
add=21787232 clip=24386 coefficient_pairs=21264880 convert=5083
divide=716408 enlarge=2034 multiply=21801456 negate=356616 scale=2033
```

Thus none of the parameter, status, panels, pairs, counts, radius,
stage comparisons, signed-rounding or preservation qualifications is
dropped to force agreement.

**Exact intervals and radii.**
The complete pre-enlargement polynomial endpoints and final endpoints
are in each `kernel.json`, all checked by its distinct replay. Their
pre-enlargement widths are respectively 12677,8401,5744,4068 grid units.
Each final endpoint is obtained by adding or subtracting exactly 2^72
grid units; hence the radius formula in the conclusion follows exactly.
Because every w_n<2^73,
(2^73+w_n)/2^257<2^74/2^257=2^-183<2^-50.
Both strict inequalities are also tested with exact Fractions for every
kernel. L102's full panel remainder theorem now gives the claimed
J_n(c_*) containment. No transfer to J_n(2*pi/sqrt(389)) is made.

**One capped lifecycle and preservation.**
The parent reconciles every entry of historical initial inventories
417/419/422/424/429 using the exact recorded post-417/419/422/424/429
editorial transitions. Each transition must match the current expected
before value before its after value is applied. It compares complete
current bytes, old preservation maps and recorded executable-source
maps; there are no path exemptions. It inventories the first/second,
finite-coefficient and four-kernel evidence, stopped 426/429 and the
explicitly outside-historical-cap 429-postmortem archive, together with
selected canonical/source/failure files. L106 is hashed for preservation,
not loaded as a numerical input.

The same timer remains armed throughout source emission, both passes,
all diagnostics, observed subprocess exits and final reporting. Each
child receives only the remaining aggregate work time; the 174-second
work deadline reserves finalization within 180 seconds. Every new
source, diff, report, ledger and panel record lies in this exclusive
fresh evidence directory. Byte measurement includes all its files,
plus a conservative 131072-byte reporting/diagnostic reserve.

All child return codes are zero, with observed exit times approximately
26.1091,52.9647,79.3964,106.1225 seconds. The terminal report records
106.20056958310306 seconds before terminal writing; the post-terminal
finalization record is 106.22402637498453 seconds. Complete original
byte/file-set and fresh-source preservation is rechecked after terminal
reporting. The final assertions enforce actual elapsed <=110<=180
and final bytes plus diagnostic allowance <=5778675<=134217728.
The tool observes coordinator exit code zero. No unobserved exact
parent-exit timestamp is claimed.

The initial unfinished attempt note is an inventoried input. Its later
editorial completion is bound by the exact before/after transition in
`drafts/2026-10-23-kernels-eleven-through-fourteen-document-transition.json`;
the measured evidence remains unchanged. Original timing qualifications
and ATTEMPTS/045–049 are preserved. Success here neither audits L106
nor repairs its parked launchers. The subsequent separate critical audit
of these sources and certificates is recorded below.

### Separate critical audit — step 433, 2026-10-23

**Scope and imported mathematics.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-kernels-eleven-through-fourteen-audit.md`;
its complete source/interface contract is in the corresponding
`drafts/source-notes/2026-10-23-kernels-eleven-through-fourteen-audit-coverage.md`.
Evidence is `scripts/four-rational-kernels/step-433/`. The original
invocation was `python3 -B -c` with the exact contents retained as
`coordinator.py`; its exclusive output directory deliberately prevents
repeating that invocation. No producer, other kernel, retry or resumed
pass ran. The audit imports the already audited L102 containment theorem,
L103 parameter construction and L031 endpoint rules cited above. Each
index remains in 1..128, the midpoint remains in [3/10,1/2], and the
positive closed panels retain all smoothness hypotheses. Reproving the
analytic theorem is unnecessary; the task is to verify its actual finite
specializations. This is known-method validation, not new mathematics
beyond the checked sources or a new BSD case.

**Whole-source and original-identity checks.** The coordinator starts
its clock before imports, inventory or source construction and retains
its own actual command argument directly. Historical entrypoints are
text/AST data only. The restricted step-417 expression permits constants,
containers, f-strings, n and str(n); each old fragment must match uniquely.
All eight complete step-412-to-step-431 source texts, all saved changes
and diffs, and all five step-424-to-step-431 worker changes reconstruct
exactly. The entire original source map, manifest and optimization guards
are checked, including the explicit no-L106-value qualification. For
each index the three original identities before production, after
production and after replay equal the tuple formed from its actual
fixed directory, kernel_431_n prefix and both source hashes. No producer
is imported to establish those identities.

**Isolated signed checks.** The step-422 installer is copied byte for
byte. Its body agrees by whole AST with the retained signed-check block;
it has one top-level function, the inspected call set, no global/nonlocal
or worker-namespace access, and no extra dynamic evaluation. The outer
function has no defaults, annotations or decorators; the retained
enclose wrapper's constant default denominator one is checked explicitly.
Worker and preflight adaptation is confined to recorded identity/path/
index AST sites and explicit extra assertions. The -422 sentinel and
installer labels remain unchanged. Complete texts compile with
flags=0, dont_inherit=True, optimize=0 before execution.

All four inert preflights finish before any kernel. Each constructs its
own module, counters and closures, checks the immutable five-field fresh
identity and sentinel, all nine original primitive captures, exactly one
deep-copied control callback, clearing of controls and ledger, and every
wrapper after installer return. The controls exercise all nine sign bins
with counts (9,6,3,6,4,2,3,2,1), including zero and endpoint cases. Each
actual replay then runs in its own fresh child and binds its fixed path,
fresh path, unique fixed_replay_433_n module and actual replayer hash.
Identity and captured original primitives/counters are checked before
installation and after installation/replay. The module-scope collision
of ATTEMPTS/047 and the stopped launchers of ATTEMPTS/048–049 are not
reused or repaired.

**Every finite operation and report.** Each sole replay reconstructs the
entire unchanged parameter, including both conversions, and all 1016
panels. The full 129/65/65 factors, 193/257 products, scalar series and
sixteen squares, integration divisors and running sums are recomputed
before digests are compared. Every one of 21264880 coefficient pairs
per index is retained. The unchanged installer checks every replay
multiplication against the four endpoint products, independently of the
replayer's sign cases, and checks directed quotient inequalities and
the other retained primitive operations. Complete returned reports and
deep-copied ledger/signed snapshots are persisted before comparisons.
Every report field agrees with both the fixed returned report and the
exact worker contract; adding only n agrees with replay.json. Both fixed
ledgers, kernel counts and fresh counts equal the complete ledger above.

For each index the additional signed ledger has 21801456 multiplications,
716408 divisions, 5083 conversions, 356616 negations, 24386 clips,
521336 wrapped additions and 2032 complete polynomial products. There
are 22522948 floor checks and the same number of ceiling checks, exactly
multiply+divide+convert+1. Inline convolution additions contribute
21264880 and inline log-constant additions contribute 1016, giving
521336+21264880+1016=21787232 total additions. Inline scaling is exactly
one log-two scale plus 1016 log-series and 1016 log-constant scales,
2033 in total. Enlargements are one for log two, 1016 for panel logs,
1016 for scalar exponentials and one final enlargement, 2034 in total.
These inline operations are read in the complete replayer and checked
by its exact reconstruction; they are not misreported as wrapped calls.
The actual multiplication sign bins are (5644008,5527040,0,5266944,
5363464,0,0,0,0); the inert controls separately cover the absent cases.
All four runs record 896 zero-operand multiplications. Full parameter-
identity, status, working, completed and exit schemas also agree,
including identity_unchanged and full_returned_report_persisted.

**Final enclosure and decision.** Every final field and both polynomial
sum endpoints agree with kernel.json and this lemma's endpoint table.
Exactly 2^72 grid units are subtracted/added. Exact Fraction comparisons
give (2^73+w_n)/2^257 with w_n=(12677,8401,5744,4068), retaining reduced
representations for n=13,14. Each radius is strictly below 2^-183 and
separately below 2^-50. Thus the full arithmetic instantiates the imported
L102 theorem and validates precisely the four J_n(c_*) enclosures above.

**Preservation and resource qualification.** Complete historical
inventories 417/419/422/424/429 and 431 reconcile through their exact
editorial transitions, with no path exemptions, including both recorded
sides of the post-431 attempt-note transition. All 461 inventoried inputs,
original tree file sets and fresh source bytes remain unchanged through
terminal reporting. The full original step-431 preservation, manifest,
status, exits, terminal and finalization records are checked, and its
5778675-byte accounting is reconstructed. Its historical timing and the
outside-cap step-429 postmortem qualification remain unchanged.

Fresh child exits are observed at approximately 32.7353,65.4558,98.1994
and 131.6669 seconds, each with code zero. The terminal records
131.75961916707456 seconds before writing; the post-terminal preservation
and finalization record is 131.79127758415416 seconds. The conservative
inclusive bounds are 135 seconds and 407304 new bytes, below the required
180 seconds and 134217728 bytes. They include source construction,
static checks, preflights, all replays, reports and the diagnostic reserve.
The timer remains armed, all original/file-set/source checks run again
after terminal reporting, and the tool observes coordinator exit zero.
No exact historical or fresh parent-exit timestamp is claimed.

The subsequent canonical-lemma and attempt-note editorial completion is
bound by `drafts/2026-10-23-l107-audit-document-transition.json`; it is
outside the measured execution and leaves its evidence unchanged.
The fixed audit passes without a changed mathematical hypothesis or DAG
edge. L106's audit, 114 unproduced kernels, signed derivative assembly,
parameter transfer, strict zero exclusion, general rank comparison,
full Sha and refined BSD remain unresolved.

## Mathlib

Full matching analytical/program coverage was not checked in production
or this separate audit.
The previously recorded supporting elementary identities do not certify
this executable, source adaptation, complete replay or process lifecycle.
No Mathlib absence or formal verification claim is made.

