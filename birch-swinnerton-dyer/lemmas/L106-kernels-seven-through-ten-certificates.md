# L106 — Fixed rational kernels seven through ten

## Hypotheses

Use L101 only for the finite kernel definition
J_n(t)=integral_1^128 exp(-n*t*y) log(y)/y dy, L031's exact outward
endpoint rules, audited L102's uniform integration scheme and audited
L103's parameter portion. Set D=2^256 and

c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2*D).

The unchanged L103 parameter interval contains 2*pi/sqrt(389), has
midpoint c_* in [3/10,1/2] and half-width at most 2^-50. The fixed
evidence is `scripts/four-rational-kernels/step-424/`. The step-412
arithmetic texts and steps 417/422 are implementation/preservation
comparisons only; no previous kernel value or runtime is an input.
No published rank, complex order, Sha or period normalization is assumed.

## Conclusion

For n=7,8,9,10, J_n(c_*) belongs to [l_n/D,u_n/D] below. The last
column is the exact pre-enlargement width w_n in grid units. Its exact
midpoint is (l_n+u_n)/(2D) and its radius is (2^73+w_n)/(2D), strictly
below both 2^-183 and 2^-50.

| n | l_n | u_n | w_n |
|---|---|---|---|
| 7 | 1121699487551703649655189234943959910184498421406162512239298996232012666787 | 1121699487551703649655189234943959910184498421406162521684031961971303177784 | 83605 |
| 8 | 669953856640999286551854629995158354594559340935773015411184239682994029410 | 669953856640999286551854629995158354594559340935773024855917205422284507136 | 50334 |
| 9 | 407986689640460803700184085439134881478595776341805283382325550041227730864 | 407986689640460803700184085439134881478595776341805292827058515780518189320 | 31064 |
| 10 | 252400208463995289135340837770304405088180729569272102545152648326989604635 | 252400208463995289135340837770304405088180729569272111989885614066280051639 | 19612 |

Every complete production and independent replay passes on all 1016
panels and 21264880 coefficient pairs per pass, separately for each
index. The sole aggregate execution observes all child exits with code
zero and records inclusive bounds 107 seconds/5791091 new bytes against
180/134217728, preserving all 255 inventoried inputs through reporting.
This is known-method REPRODUCTION. Its separate step-446 critical audit
passes, as detailed below. These are midpoint-kernel inputs, without parameter transfer,
derivative nonvanishing, a new BSD case or arbitrary-curve comparison.

## Proof

**Imported scheme and scope.** The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-23-kernels-seven-through-ten.md`; its source
note records discovery, duplicate/failure checks and primary hypotheses.
Import the entire audited L102 integration/error theorem without reproof.
Its precise standard inputs include NIST DLMF v1.2.8, Taylor's theorem
[1.4.35--37](https://dlmf.nist.gov/1.4.vi), integration/change of variable
[1.4.26/28/29](https://dlmf.nist.gov/1.4), exponential multiplication
[4.8.16](https://dlmf.nist.gov/4.8.E16), and the series and derivative
identities identified in L102. L103 imports the Machin/alternating
arctangent parameter construction, including
[DLMF 4.24.3](https://dlmf.nist.gov/4.24.E3). These known results are
specialized to four fixed indices; no analytical estimate is replaced.

For these indices, alpha=n*c_* is positive and at most five. At each
left endpoint a=(8+j)/8, 0<=j<1016, one has 1<=a<128. Hence
0<alpha*a/2^16<640/65536<1/8 and 0<alpha/8<=5/8<8.
These verify both distinct exponential-argument conditions before their
containing clips. The remaining panels, log/reciprocal positivity,
rho=1/(8a)<=1/8, all smoothness hypotheses and the a=1 endpoint are
unchanged. Thus L102 applies to every entire panel and every new index.

**Isolated sources and parameter.** The clock starts before imports,
inventory, source generation and setup. The bootstrap exclusively creates
step-424 and reads the step-417 adaptation expression as restricted AST
data, never running an old entrypoint. The allowed expression contains
only constants, containers, f-strings, n, str(n) and addition; its call/name
restrictions are checked. At each new index it reconstructs both fresh
step-412 source texts with uniquely matched exact replacements, changes
only the descriptive step label, parses and writes them, and saves their
complete diffs and replacement reviews. Both exponential arguments,
both pre-clip inequalities and every panel/final index label are changed.
All other arithmetic functions, loops, degrees and grids are retained.

For c_*=u/v and a8=8a, production uses n*u*a8/(v*8*2^16) and n*u/(8*v).
Replay independently uses num*endpoint*n/(den*524288) and num*n/(den*8),
with endpoint=a8. The parameter itself is not scaled. Each child loads
one fresh producer and one fresh replayer with unique names and fresh
arrays/counters. Its single identity tuple records index, resolved output
path, module-name prefix and both source hashes. Actual module names,
files, hashes and both grid constants are checked before production,
after production and after replay. No signed-control block or unscoped
control exec is reused; ATTEMPTS/047 and stopped step 419 are preserved.

Each producer reconstructs all 25 signed terms at both arctangent
arguments, both adjacent partial sums, Machin conversion, outward pi
grid, square-root witness, c endpoints, midpoint and delta. The entire
record agrees with the unchanged step-404 parameter and exact midpoint
above. During the sole full replay, all fractions are independently
reconstructed, square-root bounds are obtained by binary search and
checked by strict squared inequalities, and every parameter field,
range and delta is checked. Each parameter's two conversions belong to
that index's complete ledger, without a preliminary cumulative ledger.
The per-index parameter and identity records remain distinct.

**Complete replay and containment.** Each scalar logarithm has 128
terms. Each scalar exponential has 128 terms, a one-grid-unit analytic
enlargement and sixteen outward squarings. Every panel retains the full
129/65/65 factor slots, all 8385 and 12545 convolution pairs, the entire
193/257 product slots, every signed coefficient division by 1,...,257,
the scalar multiplication, division by eight and running integral sum.
Every panel is saved in its own index's panels.jsonl.

The replayer imports no producer arithmetic. It uses sign-case extrema
instead of four-product selection, absolute-value divmod instead of the
producer's floor/negated-floor formulas, and checks the defining integer
inequalities for every floor and ceiling. It reverses both convolution
traversals, switches the outer factor and reverses signed primitive
summation. It reconstructs all scalar traces, full arrays and divided
coefficients before comparing their prescribed digests, together with
every complete panel value, running sum and final field. Digests and
counts are not substitutes for reconstructing the arithmetic.

The returned full report is deep-copied and persisted before comparisons;
both producer and replay ledgers are separately snapshotted. Adding only
the immutable index gives the saved replay.json, with every original
field retained. Every complete ledger agrees with the following counts:

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

The unchanged outward scheme encloses the integrated polynomial
approximation, with every scalar/coefficient/integration rounding error.
L102 bounds the discrepancy from the true integral by strictly less
than 2^-184, retaining all panel remainders. Executed final enlargement
is exactly +/-2^72 grid units, namely +/-2^-184, so the displayed
intervals contain J_n(c_*). The complete replay checks each polynomial
sum and both enlarged endpoints. Its pre-enlargement widths are exactly
the w_n above, all less than 2^73. Thus the radius is
(2^73+w_n)/(2D)<2^74/(2D)=2^-183<2^-50. Both implementations and the
worker test both strict inequalities with exact rational arithmetic.

**Preservation and resource qualifications.** The initial inventory
contains all first/second/four-kernel and finite-coefficient evidence,
selected canonical/source/failure inputs and this attempt's unfinished
note: 255 files. Each complete old inventory from steps 417,419,422 is
reconciled against the exact applicable post-417/419/422 before/after
transitions, without path exemptions. The corresponding original
preservation inventories and fresh source hashes match. The record
`historical-reconciliation.json` preserves every transition. Full rehashes,
original tree file sets, the exact fresh bootstrap/worker bytes and all
fresh arithmetic sources agree at finalization and again after terminal
reporting. No old numerical evidence, failed run or canonical lemma is
modified during execution.

One aggregate signal deadline stays armed through setup, all four pairs,
logs, preservation and reporting. Each child receives remaining work
time to 174 seconds and must exit before another index starts. Observed
zero-code exits occur at 26.349476584000513, 52.4154813750647,
78.21871408401057 and 104.05520329205319 seconds. Terminal reporting
begins at 104.11253254208714 seconds; finalization records
104.12922808411531 seconds after the post-terminal preservation check.
The parent exits zero after final assertions. Inclusive allowances are
107 seconds and 5791091 bytes, including a reporting/diagnostic reserve,
below 180/134217728. Complete records are in terminal-report.json,
finalization.json and preservation.json. No retry, resumption, other
kernel or derivative assembly executes.

These are observed finite bounds, without an exact parent-exit timestamp,
a signal-dispatch guarantee or future-runtime guarantee. Historical
n=1/n=2/step-417 timing qualifications remain unchanged; fresh timing
does not repair them. Subsequent editorial completion of the attempt
note occurs after this preservation boundary and is recorded separately.
The certificates await a separate critical audit. There remain 118
kernels, full signed assembly, parameter transfer and strict zero
exclusion. Arbitrary-curve rank comparison, full Sha and refined BSD
are independent unresolved gaps.

### Separate critical audit launch — 2026-10-23, step 426

The sole separate audit submission failed while parsing its outer Python
input, with `SyntaxError: invalid syntax` at line 20. The intended nested
triple-single-quoted replacement prematurely ended the outer generator
literal. No statement executed: the aggregate clock, adapter generation,
static checks, four inert preflights and numerical replays all remained
unperformed. There is no measured aggregate audit bound or audit PASS.
The complete diagnostic qualifications are recorded in
`scripts/four-rational-kernels/step-426/launch-failure.json`, with an explicitly
labeled diagnostic excerpt beside it. The full submitted input remains in
the tool transcript; no executable reproduction is claimed for the excerpt.

The first-failure rule stopped the attempt without retry, repair, resumption
or enlargement. This launcher failure contradicts no numerical certificate
and changes no analytical hypothesis or conclusion above. The separate
critical audit remains pending. A different file-based emission/compile
interface is only a proposed, uncovered continuation requiring its own
source review; the old stopped input is not reopened. All original production
evidence and historical timing qualifications remain unchanged.

### File-based critical audit attempt — 2026-10-23, step 429

The separate file-based attempt stops in source materialization, before
source emission, compilation, inert preflights or numerical replay. Its
literal guard expects three occurrences of `-422` in the retained worker,
but there are four: the sentinel assignment, two sentinel assertions and
the compiler label `installer-422`. The first failed assertion stops the
attempt without retry, repair or resumption. This is a launcher error,
not an arithmetic discrepancy; the separate critical audit remains pending.

The complete first failure, historical source/inventory comparisons and
preservation record are in `scripts/four-rational-kernels/step-429/`.
All 353 inventoried inputs match through terminal reporting. The partial
attempt records inclusive bounds 3 seconds/197140 new bytes against
180/134217728, with final measured elapsed time 0.2744104170706123 seconds;
no child starts and these bounds do not describe a completed audit.
The full submitted coordinator is archived verbatim after termination in
`scripts/four-rational-kernels/step-429-postmortem/coordinator-submission.txt`;
its adjacent record explicitly excludes this post-stop archival from the
capped attempt's measurement. No compile PASS is inferred from that text.
ATTEMPTS/049 explains the stopped interface. The incompatible launcher is
parked. All prior mathematical conclusions, source qualifications and
independent unresolved gaps remain unchanged.

### Separate critical audit — 2026-10-24, step 446

The separate audit passes under the unchanged hypotheses. Its prior
SPECIALIZE assessment is
`drafts/literature/2026-10-24-l106-direct-coordinator-audit.md`;
the complete fresh evidence is `scripts/four-rational-kernels/step-446/`.
This is REPRODUCTION of the imported method, not mathematical novelty.
The displayed four intervals and their exact radii are unchanged.

**Applicability and full source review.** Import audited L102 and the
complete audited L103 parameter, with L031 endpoint rules and L101's
definition, without reproof. The positive-argument inequalities above
verify this specialization; the entire panels, including y=1, meet the
imported Taylor/integration hypotheses. The audit reconstructs the whole
step-424 bootstrap serialization from its unique top-level WORKER and
PARENT literals and matches the complete original worker. Neither old
entrypoint executes. Restricted step-417 AST data and the entire step-412
templates reconstruct all eight actual arithmetic files, all source
diffs and every source-review field. Both exponential arguments and their
pre-clip tests change with n; the parameter does not. All three original
identities per index bind both actual source hashes and the original
path/module prefix. Full source maps and older manifest/status/working/
stdout/stderr/exit/finalization schemas are compared, retaining the original
73728-byte reserve and ceil(elapsed)+2 rule rather than later schemas.

**Lexical installation.** The new coordinator retains its actual complete
direct command argument, without self-slicing. Step-442's worker changes
only the designated identity path, unique module prefix and accepted
index tuple; its preflight additionally changes its loop tuple. The
whole resulting ASTs, full diffs and optimization-zero compilation pass.
The installer is byte-identical to steps 442/437/433/422; its complete
body matches the retained signed-check block, with the audited AST,
call/default/annotation/decorator restrictions intact. Four inert tests
finish before numerical execution. They check all nine captured original
primitives and wrapper closures, isolated modules/counters, immutable
identity/sentinel, one deep-copied callback, all nine sign cases, zero
and endpoint controls, post-return bindings and cleared ledger state.
Fresh identities are checked before/after installation and after replay.

**Full finite verification.** Each fresh child executes its sole fixed
replayer, with no producer or other index. It independently reconstructs
every arctangent term, adjacent bound, Machin/grid conversion, strict
square-root witness and entire unchanged parameter record. Both parameter
conversions remain in that child's complete ledger. It reconstructs all
1016 panels and 21264880 coefficient pairs, all scalar terms/squares,
129/65/65 factor slots, 193/257 product slots, signed integration divisors
and running sums before comparing saved records and digests. The nine
wrappers independently check four-product extrema, signed floor/ceiling
inequalities, conversions, divisions, additions, negations, clips and
complete convolution sizes. Inline exact accumulation/scaling and analytic
enlargements retain the original full replay checks.

Each entire returned report and deep-copied ledger/signed snapshot is
persisted before comparison. All original report fields, both complete
ledgers, final kernel fields (including grid denominator), parameter
identity and status agree. Per index there are 21801456 checked interval
multiplications, 716408 interval divisions, 5083 conversions, 356616
negations, 24386 clips, 2032 polynomial products and 521336 wrapper
additions. The remaining 21264880 convolution additions and 1016 inline
scalar-log additions give the full 21787232 addition count. Both floor
and ceiling counts are 22522948. These are complete-run checks, not
samples or counts substituted for reconstruction.

The independently checked polynomial widths are exactly
(83605,50334,31064,19612). Every final endpoint equals its reconstructed
polynomial endpoint plus or minus 2^72 grid units. Exact midpoint and
Fraction radius comparisons give (2^73+w_n)/2^257 for each n, strictly
less than 2^-183 and 2^-50. With the imported analytical containment,
these checks verify precisely the stated J_n(c_*) intervals.

**Preservation and measured bounds.** Initial capture completes with 849
files, including the whole failed step-444 tree. Eleven original
inventories from steps 417/419/422/424/429/431/433/435/437/440/442 are
reconciled through all exact transition suffixes ending post-442, without
path exemptions. Each existing historical reconciliation report is
matched in full at its original boundary, including step-424 at post-422
and step-442 at post-440. All source maps and original preservation records
agree. Step 444's failed flags and absent inventory/finalization remain
unchanged; fresh preservation does not turn that failed attempt into a
successful historical capture. The 429 postmortem retains its explicit
outside-historical-cap qualification.

The four zero-code exits are observed at 32.24119900004007,
64.57329516694881, 96.53456795914099 and 129.01637608394958 seconds.
Terminal writing starts at 129.16379716712981 seconds and the
post-terminal preservation check precedes the finalization timestamp
129.21365020913072. All original hashes/tree file sets and fresh sources
are rechecked after terminal writing with the timer armed. Inclusive
bounds are 133 seconds and 556076 new bytes, below 180 and 134217728;
post-write assertions include the diagnostic reserve. The execution tool
observes parent exit zero. No exact parent-exit timestamp or universal
signal-dispatch/runtime guarantee is claimed. Earlier timing qualifications
and all stopped runs remain intact. Editorial changes to this lemma and
the audit note are separately recorded in
`drafts/2026-10-24-l106-audit-document-transition.json`.

Thus the pending L106 audit is closed. No new kernel is produced: the
remaining 106 midpoint kernels, complete signed assembly, transfer to
the exact parameter and strict zero exclusion remain unperformed.
Arbitrary-curve rank comparison, full Sha and refined BSD remain separate.

## Mathlib

Full theorem/algorithm/certificate coverage is not checked. The previously
inspected supporting identity
[Real.four_mul_arctan_inv_5_sub_arctan_inv_239](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Arctan.html#Real.four_mul_arctan_inv_5_sub_arctan_inv_239)
supports the parameter identity only, without a pinned local compilation.
It does not formally verify this integration implementation or certificates.
