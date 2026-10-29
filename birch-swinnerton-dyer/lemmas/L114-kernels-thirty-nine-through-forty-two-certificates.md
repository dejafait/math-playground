# L114 — Fixed midpoint kernels n=39–42

## Hypotheses

Use L101's definition J_n(t)=integral_1^128 exp(-nty) log(y)/y dy,
L031's signed rational endpoint rules, audited L102's rational Taylor
scheme and the entire audited L103 parameter. Put D=2^256 and

```
c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2*D).
```

L103 supplies c_* in [3/10,1/2], the enclosing c endpoints for
2*pi/sqrt(389), and delta. Every part of that parameter record is
retained. L101 is used only for its kernel definition. No rational or
analytic rank, Sha statement, previous kernel endpoint, period
normalization, signed audit installer or optional numerical library is
an arithmetic premise. The complete production evidence is
`scripts/four-rational-kernels/step-468/`. Prelaunch construction and
post-execution evidence checking are separately retained in
`scripts/four-rational-kernels/step-468-prelaunch/` and
`scripts/four-rational-kernels/step-468-postcheck/`.

## Conclusion

For each row, J_n(c_*) belongs to [l_n/D,u_n/D]. Its exact radius is
(2^73+w_n)/2^257, with w_n the pre-enlargement grid width.

| n | l_n | u_n | w_n |
|---|---|---|---|
| 39 | 2446877204960230355328494233166493896430927296809095098989880688537181 | 2446877204960230355328494233166493896430927296818539831955619978965591 | 1018 |
| 40 | 1699280014139903109034960217417081474436471376887819327894117080928162 | 1699280014139903109034960217417081474436471376897264060859856371356571 | 1017 |
| 41 | 1181336998619743981765809545961678991148473858756063489800207326874522 | 1181336998619743981765809545961678991148473858765508222765946617302933 | 1019 |
| 42 | 822087759433012690187227049806940932181453921972381237307160270054666 | 822087759433012690187227049806940932181453921981825970272899560483075 | 1017 |

All radii are strictly below 2^-183 and 2^-50. Four complete
production/independent-replay pairs pass, each with 1016 panels and
21264880 coefficient pairs per pass. All four child exits and the
parent exit are observed as zero. All 1567 captured inputs pass
post-terminal preservation, under production inclusive bounds
114 seconds and 31844254 new bytes versus 180 and 134217728.

This is local known-method REPRODUCTION, not progress beyond the
checked sources or a new BSD case. The separate step-470 critical signed
audit below passes, with inclusive bounds 141 seconds/52560605 bytes
against 180/134217728 and all 1665 inputs preserved after terminal writing.
Eighty-six kernels remain unproduced, and signed
assembly, exact-parameter transfer and strict derivative zero exclusion
remain. The arbitrary-curve rational-rank comparison, full Sha and
refined BSD remain unresolved. These are midpoint enclosures only.

## Proof

**Imported analysis and applicability.** Apply audited L102 at the
unchanged L103 parameter and n=39,40,41,42, all in its integer range
1<=n<=128. Its standard inputs include NIST DLMF v1.2.8 (2026-09-15),
finite Taylor theorem with its C^(d+1) hypothesis and Lagrange remainder
[1.4.35–37](https://dlmf.nist.gov/1.4.vi), continuous integration
[1.4.26](https://dlmf.nist.gov/1.4.E26), change of variable
[1.4.28](https://dlmf.nist.gov/1.4.E28), integral bound
[1.4.29](https://dlmf.nist.gov/1.4.E29), and the elementary series and
derivative identities precisely identified in L102. These inputs are
imported; no Taylor or integration theorem is reproved here. L103's
entire parameter is in L102's rational range. All log and reciprocal
arguments are positive on the full closed panels, including y=1;
the exponential is entire. Thus the smoothness and real-branch
hypotheses hold. The analytic allowance and grid are unchanged.

The saved SPECIALIZE assessment is
`drafts/literature/2026-10-25-kernels-thirty-nine-through-forty-two-parsed-adapter.md`.
It reuses the analytic/discovery comparison in the preceding target
assessment, and separately approves the parsed-statement interface.
Known results cover the method. The needed additional evidence is
actual complete source specialization, execution and replay; a theorem
citation or source hash alone supplies none of these.

**Prelaunch structural specialization.** The one-shot builder
`scripts/four-rational-kernels/build-parsed-468.py` selects against the
immutable whole step-461 coordinator, SHA256
`ed7b021281df11e29bdab0b640fdc8feb62e1f7e916761915569a05cb436891c`.
UTF-8 decoding/encoding preserves its raw bytes. Selection uses the
module assignment roles and full enclosing try/for/body/orelse field
paths; exact line and old-expression checks supplement the pinned
whole-source identity. In particular the immediate preservation If
and the report-dispatch If reached through four orelse fields are
distinct roles. This avoids ATTEMPTS/051's suffix collision without
editing or running failed step 465.

The full edit map records 19 disjoint spans, their complete old/new
bytes, field paths and enclosing original statements. Edits are applied
in descending byte order. Every interval outside those spans is compared
byte-for-byte, including the trailing interval. The complete diff is
retained. Reparse resolves every saved path in the resulting tree and
compares its entire new source segment. Explicit checks retain all
eighteen old transitions and append exactly the two post-461/post-463
transitions, retain selected records except the prescribed L112-to-L113
substitution, and add the current assessments, source notes, failure
evidence, unfinished note and prelaunch evidence. The whole new source
is compiled with flags=0, dont_inherit=True, optimize=0.

The worker is independently predicted from the pinned whole step-461
worker, SHA256
`628f7f9dbb42289e16d906b90e0f1f11b1b21d08be58273e34f8e6d8739c6e56`.
Exactly two unique substitutions change its allowed indices to
(39,40,41,42) and module prefix to kernel_468_. Every other worker
byte is retained. Its complete text also compiles before execution.
Prelaunch verification is outside the unstarted production measurement;
it is not presented as production arithmetic or a resource certificate.

**Direct execution and whole arithmetic sources.** The shell passes
the complete candidate, including its trailing newline bytes, directly
as Python's -c argument. The coordinator retains sys.orig_argv[-1],
checks the actual -c mode and optimize=0, writes and compiles its whole
source, and later compares source identity again. The retained actual
source equals the prelaunch candidate exactly. No self-delimiter,
AST unparse, tokenizer regeneration or nested Python launcher is used.

Within the production clock the entire worker is reconstructed from
step 461 with the same two exact-once substitutions, compiled and
retained with its full diff. Its bytes equal the prelaunch prediction.
The step-417 top-level PARENT literal is inert source data. Its unique
replacement expression passes the retained whitelist of literal
containers, formatted strings, addition, n/str names and calls only to
str. No historical entrypoint executes. Every whole step-412 producer
and independent replay template is compiled, adapted at unique complete
sites, compiled again, written and source-hashed before import.

The maps/diffs bind both producer arguments n*u*a8/(v*8*2^16) and
n*u/(8*v), both replay arguments num*endpoint*n/(den*524288) and
num*n/(den*8), all four corresponding pre-clip tests, index labels
and destination descriptions. Every other arithmetic byte, including
the log clip seven, series, array degrees, loops and parameter, is
unchanged. No old kernel endpoint or signed installer is imported.

**Entire parameter and complete independent arithmetic.** Each child
binds an immutable identity consisting of index, absolute directory,
unique module prefix and both whole-source hashes. It checks the same
module objects and files before production, after production and after
replay. Production reconstructs the entire L103 parameter and compares
it with step-404/parameter.json. Replay independently reconstructs both
25-term arctangent lists, adjacent sums, Machin bounds and pi grids,
the separate binary-search square-root witness with both squared
inequalities, both outward c endpoints, midpoint and delta. No
midpoint-only projection is accepted.

For j=0,...,1015 the panel is y=(8+j)/8+s/8, 0<=s<=1.
The arrays have 129 exponential, 65 reciprocal and 65 logarithm
slots. Full convolution retains 8385 and 12545 pairs per panel,
including zeros, producing arrays of lengths 193 and 257. All scalar
series terms, sixteen exponential squares, reductions, coefficients,
integration divisors 1,...,257 and dy=ds/8 are retained. Independent
replay reverses both coefficient traversals and changes the outer
factor, using sign-case interval multiplication in place of the
producer's four-product extrema. It checks every directed quotient
by its defining integer inequalities. Full scalar traces and arrays
are reconstructed before digest comparison; hashes do not replace
that reconstruction. Every stored panel field, integral and running
sum, and the full final interval, agree exactly.

Each complete returned report and both count ledgers are deep-copied
and persisted before comparisons. replay.json adds only n to the
returned report. Every field and both full ledgers agree with

```
add=21787232, clip=24386, coefficient_pairs=21264880,
convert=5083, divide=716408, enlarge=2034,
multiply=21801456, negate=356616, scale=2033.
```

Thus every pass accounts for 1016 panels and 21264880 coefficient
pairs. Final comparisons include polynomial sum, grid denominator,
endpoints, midpoint, reduced radius and both threshold fields. The
enlargement is exactly ±2^72 grid units, hence ±2^-184, as required
by audited L102. Its containment theorem therefore applies to these
completely replayed intervals and proves the displayed enclosures.
The endpoint differences are exactly 2^73+w_n from the table, with
0<w_n<=1019<2^73. Dividing by 2D gives radius strictly below
2^74/2^257=2^-183<2^-50. The implementation also checks both strict
comparisons using exact fractions. No assertion about the exact
transcendental parameter follows from these midpoint intervals alone.

**Original-boundary provenance and preservation.** Initial capture
includes entire historical trees, all earlier inventoried paths,
selected mathematical/source inputs, ATTEMPTS/045–051, failed-465
postmortem and the unfinished attempt. Twenty suffixes are applied
in order at steps
417/419/422/424/429/431/433/435/437/440/442/446/449/451/453/455/457/459/461/463.
For each suffix, every before value is checked before applying after.
Every complete recursive report is compared at its original boundary,
including step 461 at post-459 and step 463 at post-461. All complete
source maps match, using source-hashes.json for 461 and
fresh-source-hashes.json for 463. No report is projected, rebased or
given a path exemption. Failed-444 STOP/false flags, empty exits and
completions, absent initial inventory/finalization, postmortem 429 and
all historical timing qualifications remain unchanged. L113/461/463
are provenance, not arithmetic inputs.

**One bounded production lifecycle.** The clock starts before setup
imports, capture and retained source generation. The 174-second work
deadline and remaining child timeouts retain a 131072-byte reserve
within the single 180-second/134217728-new-byte production cap. Pairs
run once in order 39,40,41,42. Observed zero child exits occur at
27.910734792007133, 54.6934029168915, 82.40199462487362 and
110.09063845896162 seconds. There is no failure, retry, resumption,
cap enlargement or extra kernel.

Terminal writing follows an elapsed measurement of
110.38552208384499 seconds. All 1567 initial inputs, tree sets and
fresh sources are compared again after terminal writing. Finalization
records 110.48745579179376 seconds and 31713999 bytes before its own
write. The retained conservative inclusive bounds are 114 seconds
and 31844254 new bytes. Subsequent elapsed and disk-reserve assertions
pass, and the tool observes parent exit zero. The timer remains live
through finalization. Exact parent-exit timestamps and hard Python
signal-dispatch bounds remain unproved. The actual interpreter is
Python 3.15.0, optimize=0, as recorded in manifest.json; documentation
version is not an assertion about that interpreter.

**Post-execution saved-evidence check and limitations.** The separate
`scripts/four-rational-kernels/check-468-evidence.py` imports no
arithmetic module and performs no additional kernel pass. Its full
certificate is step-468-postcheck/evidence.json. It checks every saved
parameter, report, ledger and identity, reconstructs all eight full
arithmetic texts from their exact maps, compares the actual coordinator
and worker with their prelaunch versions, checks every saved panel's
ordered identity and exact running sum, and checks all final endpoints,
radii, resources, source identities and all 1567 current input hashes.
It also compares complete saved original reports with their originals.
It passes. These review outputs are outside the completed production
measurement, not retroactively included in its resource certificate.

That postcheck is not the separately required signed critical audit with
its additional controls and full signed replay; the latter is supplied
by step 470 below. The certificate supplies four local
midpoint inputs only; it neither evaluates the assembled derivative
nor transfers to its exact parameter or excludes zero. It repairs no
historical failure or timing claim. The general BSD gap is unchanged.

**Separate critical signed audit — step 470.** The prior SPECIALIZE
assessment is
`drafts/literature/2026-10-25-kernels-thirty-nine-through-forty-two-audit.md`;
the complete evidence is `scripts/four-rational-kernels/step-470/`.
This is a REPRODUCTION proof audit using the imported analysis above,
not a new theorem beyond the inspected sources. The unchanged L103
parameter, all four permitted integer indices, positive closed panels,
full degrees and analytic allowance retain L102's hypotheses. No
production execution or previous kernel endpoint enters fresh arithmetic.

The direct coordinator retains its entire actual `-c` argument, compiles
at optimize=0 and starts its clock before setup imports, input capture,
source materialization, reconstruction or preflights. It pins the four
whole step-463 audit sources. Independently enumerated structural paths
in the pinned whole step-461 production source reconstruct all 19 edits:
each complete owning statement, old/new segment and byte span agrees
with the prelaunch map. Both the direct preservation If and the report
tail reached through four orelse fields are checked separately. All
20 untouched intervals, including the trailing one, are compared.
Descending byte splices reproduce the complete actual and prelaunch
step-468 coordinators and their entire diffs. Reparsing checks all new
field values; whole texts compile. The pinned worker is reconstructed
with exactly its two approved substitutions, and the entire prelaunch
verification record is compared with these independently obtained facts.
The saved builder is never run. Full results are in
`parsed-reconstruction.json`.

The restricted inert step-417 expression independently reconstructs all
eight arithmetic texts from whole step-412 templates. Complete source
maps/diffs, both scalar and beta arguments, all four pre-clip tests and
all three original identities per index agree. The entire ten-source
map, production manifest, terminal/finalization, statuses, working
records, stdout/stderr, ledgers and resource relations are compared.
Historical prelaunch and postcheck remain outside production measurement.

The audit adapts only the designated identity path, prefix and index
AST sites in the whole step-463 worker/preflight. All other AST remains
unchanged. The lexical installer bytes, -422 sentinel and installer
labels remain unchanged. Static checks retain its allowed calls, absence
of namespace-changing constructs, one immutable IDENTITY binding, and
original module/primitive/counter captures. Four inert preflights finish
at 1.5625435831025243 seconds, before any kernel. Each checks all nine
wrappers and sign cases; the control sign counts are
[9,6,3,6,4,2,3,2,1], with 36 multiplications and 57 floors/ceilings.
Controls are saved, then all counters and the arithmetic ledger reset.

Fresh signed replay runs once in order 39,40,41,42. Each reconstructs
the entire L103 parameter, scalar traces, full coefficient arrays and
1016 panels as described above; digest comparison follows reconstruction.
The wrappers independently check each signed product against all four
endpoint products and each directed quotient by integer inequalities.
Complete returned reports and both ledgers are deep-copied and persisted
before comparison. All report fields, parameter identities, final
endpoints, midpoints, reduced radii and exact ±2^72 enlargement agree.
In particular n=39 is compared as an exact fraction, without assuming
an unreduced denominator. Both strict radius thresholds pass.

For each index the ordinary ledger is exactly the count map above.
The signed counts are floor=ceiling=22522948, multiply=21801456,
divide=716408, convert=5083, plus=521336, negate=356616, clip=24386,
products=2032, zero_operand_multiplications=896, and sign cases
[5644008,5527040,0,5266944,5363464,0,0,0,0]. The complete worker checks
the count identities, including 21264880 coefficient pairs per replay.
The zero entries in these execution sign counts do not remove control
coverage: all nine cases were separately tested before each replay.

All twenty-one original-boundary suffixes through post-468 are applied
with each before value checked at its original boundary. Entire recursive
reports and source maps agree; no projection, rebasing or path exemption
is used. The audit captures the whole prelaunch/postcheck trees, frozen
465 and 429 postmortems, ATTEMPTS/045–051, and failed-444 false flags and
absences. All 1665 input hashes, original tree sets and fresh sources
match again after terminal writing. Documentation changes after the
audit are separately recorded in
`drafts/2026-10-25-l114-audit-document-transition.json`.

Observed zero child exits are at 35.38878787495196, 69.19314104109071,
103.22769462503493 and 137.10075562493876 seconds. Terminal measurement
is 137.422262707958 seconds; post-terminal finalization measurement is
137.54039412504062 seconds and 52430348 bytes before its own write.
The retained inclusive bounds are 141 seconds and 52560605 new bytes,
below 180 seconds and 134217728 bytes. The 174-second work deadline,
remaining child timeouts and 131072-byte reserve remain in force.
The timer stays live through finalization, subsequent time/disk checks
pass, and the execution tool observes parent exit zero. There is no
retry, resumption, enlargement or extra kernel. Exact parent-exit
timestamps and hard signal dispatch remain unproved; all historical
timing qualifications remain. This successful audit supplies only the
four midpoint inputs, not signed assembly, exact-parameter transfer,
strict derivative zero exclusion, general rank comparison or refined BSD.

## Mathlib

Full matching certificate/algorithm coverage is unchecked. Previously
inspected supporting Machin coverage is
[Real.four_mul_arctan_inv_5_sub_arctan_inv_239](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/SpecialFunctions/Trigonometric/Arctan.html#Real.four_mul_arctan_inv_5_sub_arctan_inv_239).
That supporting identity is not a matching finite certificate theorem;
rolling documentation was not pinned or compiled locally. Unknown
full coverage is not evidence of absence or formal verification.
