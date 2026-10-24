# L109 — Fixed midpoint kernels nineteen through twenty-two

## Hypotheses

Use L101's definition
J_n(t)=integral_1^128 exp(-nty) log(y)/y dy, L031's exact rational
endpoint rules, audited L102's uniform 1016-panel containment theorem,
and the complete audited parameter portion of L103. Set D=2^256 and
fix the unchanged rational midpoint

```text
c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2D).
```

L103 certifies 3/10<=c_l<=2*pi/sqrt(389)<=c_u<=1/2,
c_*=(c_l+c_u)/2 and delta=(c_u-c_l)/2<=2^-50, with its complete
parameter record retained. No scaling of c_* is made.

The fixed finite evidence is `scripts/four-rational-kernels/step-440/`.
The assessment saved before this invocation is
`drafts/literature/2026-10-24-kernels-nineteen-through-twenty-two.md`
(SPECIALIZE). The executable interface uses step-412 templates,
restricted step-417 adaptation data and the isolated step-435 worker.
Audited L108 supplies interface/provenance precedent, not numerical
values for these indices. No L106 value, signed installer, stopped
launcher, published complex order, period or Sha computation is an input.

## Conclusion

For n=19,20,21,22 respectively, J_n(c_*) belongs to [l_n/D,u_n/D]
with these exact integer grid endpoints:

| n | l_n | u_n |
|---|---|---|
| 19 | 5066897338522576182766789562568468029665931599118860166603272338398568656 | 5066897338522576182766789562568468029665931599118869611336238077688997437 |
| 20 | 3377350064912667295941765744142954920173155705803311723440370806923005374 | 3377350064912667295941765744142954920173155705803321168173336546213434036 |
| 21 | 2259667712196350796272330766466511384653665759982168974314755790639073781 | 2259667712196350796272330766466511384653665759982178419047721529929502359 |
| 22 | 1517081357211430668438475966755160294852301690012014090350725945441091851 | 1517081357211430668438475966755160294852301690012023535083691684731520373 |

The exact radii are (2^73+w_n)/2^257, where
(w_19,w_20,w_21,w_22)=(1389,1270,1186,1130).
Every radius is strictly below both 2^-183 and 2^-50.

Every production and independent replay checks 1016 panels and 21264880
coefficient pairs per pass per index. One aggregate execution observes
four zero-code child exits, preserves all 683 inventoried inputs through
terminal reporting and meets conservative inclusive bounds 109 seconds
and 5779283 new bytes, below 180 and 134217728 respectively. The tool
observes coordinator exit code zero; no exact parent-exit time is claimed.

This is known-method REPRODUCTION, completing four local finite inputs.
Its separate step-442 critical audit passes, with inclusive bounds
136 seconds/495028 new bytes and all 777 inventoried inputs preserved
through terminal reporting, as detailed below. There remain 106 unproduced
kernels, L106 audit, signed assembly, parameter transfer and strict zero
exclusion. No derivative nonvanishing, new BSD case, arbitrary-curve
rank comparison, full Sha finiteness or refined formula is established.

## Proof

**Imported analysis and applicability.** Apply audited L102 without
reproving its analytic estimates. Its primary inputs include NIST DLMF
v1.2.8 (2026-09-15), Taylor's theorem with the C^(d+1) hypothesis and
Lagrange remainder [1.4.35–37](https://dlmf.nist.gov/1.4.vi), integration,
change of variable and integration bounds [1.4.26/28/29](https://dlmf.nist.gov/1.4.v),
exponential series [4.2.19](https://dlmf.nist.gov/4.2.E19), logarithm
series [4.6.1/4](https://dlmf.nist.gov/4.6) and exponential multiplication
[4.8.16](https://dlmf.nist.gov/4.8.E16). L102 records the precise
derivative, logarithm-additivity and geometric-sum inputs. The ready
assessment and its source note cover these hypotheses and all four
indices; citations supply the analysis, not the new finite outputs.

Here 1<=n<=128 and c_* belongs to [3/10,1/2] by L103. The closed
panels are positive, including y=1, so log and reciprocal are smooth
on every panel and exp is entire. With a=1+j/8, y=a+s/8,
0<=s<=1, the scalar argument is n*c_*a/2^16 and beta=n*c_*/8.
They lie in the pre-clip ranges required by L102. The log clip [0,7]
is unchanged. All 128 scalar terms, sixteen squarings, degrees
128+64+64, full degree-256 product, dy=ds/8 and 2^-256 grid remain
unchanged. Thus correctness of the complete specified arithmetic
instantiates L102's containment theorem for these four inputs.

**Exact source construction.** The direct coordinator is retained
verbatim from its actual Python -c argument in `coordinator.py`.
Its single clock starts before setup, imports, reads, inventories and
generation of workers or per-index sources. No historical entrypoint
is executed. Restricted AST extraction of the step-417 expression
permits only its constants, containers, f-strings, n, addition and str(n)
to obtain the retained adaptation fragments. Every old fragment matches
exactly once in the complete step-412 template. Each index retains the
entire old/new map and complete diff in `source-review.json` and
`source-diff.txt` in its n-directory.

The producer's scalar and beta arguments become n*u*a8/(v*8*2^16)
and n*u/(8*v); the replay's become num*endpoint*n/(den*524288) and
num*n/(den*8). Both preceding index-dependent pre-clip conditions and
all panel/final labels are adapted as well. Parameter construction,
unrelated constants, loops and arithmetic primitives are unchanged.
The step-435 worker changes only the permitted tuple to (19,20,21,22)
and its unique module prefix to kernel_440_; its full diff is saved.

All full generated texts compile before import with flags=0,
dont_inherit=True and optimize=0, in both coordinator and fresh child.
The actual interpreter is Python 3.15.0 with optimization zero; reviewed
rolling Python documentation labeled 3.15.1 is not a binary attestation.
For each index one isolated child retains its two module objects and
checks the index, resolved n-directory, unique module names and both
source hashes before production, after production and after replay.
All three complete identity records are persisted. No shared signed
audit-control namespace is introduced.

**Full parameter and arithmetic replay.** Each producer reconstructs
all 25 signed arctangent terms at both 5 and 239, both exact partial
sums, Machin pi bounds, outward pi grid, square-root target and both
squared witnesses, c endpoints, midpoint and delta. Its entire
JSON-normalized record must equal the audited step-404 parameter.
Each replayer independently reconstructs every field with exact
fractions and a binary-search square root, checking signed directed
conversions and the two strict square inequalities. Both parameter
conversions are included in each full-pass ledger.

The producer uses extrema of all four endpoint products. The independent
replayer imports no producer arithmetic and uses sign-case extrema and
integer inequalities for each floor and ceiling. It reverses both
coefficient traversals and exchanges the outer factor, and accumulates
integration terms in reverse order. It reconstructs every scalar term,
square, all 129/65/65 factor slots, all 193/257 product slots and all
257 integration divisors, retaining zeros and high-degree cross terms.
Every saved panel and running sum is compared exactly after complete
recomputation. Digests supplement this arithmetic, rather than replacing
it. All 1016 panels cover [1,128], with
1016*(129*65+193*65)=21264880 coefficient pairs per pass.

Each full returned report and both full deep-copied ledgers are saved
before comparison. The worker checks every report field, not merely
its status; `replay.json` adds only n to the returned report. Kernel
counts, returned counts, both module ledgers and both saved ledgers
agree in every entry:

```text
add=21787232 clip=24386 coefficient_pairs=21264880 convert=5083
divide=716408 enlarge=2034 multiply=21801456 negate=356616 scale=2033
```

The final endpoints, midpoint, radius, grid and thresholds all replay
exactly. The complete saved polynomial sums have respective widths
1389,1270,1186,1130 grid units. The final lower endpoint subtracts
exactly 2^72 units and the upper adds exactly 2^72 units. Hence the
exact radius is (2^73+w_n)/(2D), as stated. Each w_n<2^73, so this is
strictly below 2^74/2^257=2^-183<2^-50; the worker separately tests
both strict inequalities by exact Fraction comparisons. L102's full
analytic allowance is precisely this 2^-184 enlargement at each end.
Its audited containment proof and the successful full finite replay
therefore yield the four J_n(c_*) enclosures. No J_n(c) transfer is used.

**Lifecycle and preservation.** The coordinator reconciles every entry
of the full initial inventories at steps 417/419/422/424/429/431/433/435/437.
For each inventory it uses exactly its applicable post-step transition
suffix, including both post-435 and post-437 editorial maps. Every
transition's before value must match before applying after; final
actual bytes and hashes must agree without path exemptions. Historical
preservation records and executable-source maps are also checked.
The entire first/second-kernel, finite-coefficient and listed historical
four-kernel trees, stopped 426/429 and the outside-historical-cap
429-postmortem archive are included, as are selected inputs and this
attempt's pre-execution note. Historical timing qualifications are
retained. L106 values are not used for computation or expectations.

One live timer covers setup through terminal reporting. The work
deadline is 174 seconds; each child gets only remaining work time.
The exclusive output directory contains generated sources, diffs,
panels, parameters, identities, ledgers, reports and captured diagnostics;
bytecode is disabled. Accounting retains a 131072-byte reserve. This
records observed feasibility, not a hard Python-signal dispatch guarantee
or a future runtime theorem. No retry, resumption, other kernel or
failed-launcher repair occurs.

The four zero-code exits are observed at 26.210389042040333,
52.86702125007287, 79.69572533387691 and 105.74192312499508 seconds.
All persisted statuses agree with the complete reports and stdout.
Terminal writing starts at 105.86546349991113 seconds; the post-terminal
finalization record is 105.90608666697517 seconds and 5649002 disk bytes.
All 683 original inputs, entire tree file sets and fresh source identities
are rechecked after terminal reporting. Final assertions require actual
elapsed<=109<=180 and disk plus 8192 diagnostic bytes<=5779283<=134217728.
The tool observes coordinator exit zero. No historical timing is repaired.

The later editorial completion of the pre-execution note is bound by
`drafts/2026-10-24-kernels-nineteen-through-twenty-two-document-transition.json`.
It is outside the measured execution and changes no fixed certificate.
The new finite assembly passes the separate critical audit below.

### Separate critical audit — 2026-10-24, step 442

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-nineteen-through-twenty-two-audit.md`.
Complete evidence is in `scripts/four-rational-kernels/step-442/`.
This is one REPRODUCTION audit of the four fixed inputs, without a
producer, retry, resumption, other kernel or stopped-launcher repair.
Known analysis is imported from the precise DLMF cases above through
audited L102. L103's entire parameter satisfies its rational range and
each selected integer lies in 1..128. All closed panels are positive;
the logarithm/reciprocal smoothness and exponential hypotheses hold.
The source's scalar argument, beta, clipping ranges, full products,
dy=ds/8 and final analytic enlargement match that theorem. No new
analytical estimate or parameter transfer is asserted.

**Whole sources and identities.** Restricted extraction of step-417's
retained expression reconstructs every producer/replayer from the full
step-412 templates. Every old fragment occurs exactly once; all four pairs of
whole sources, review maps and full diffs match the fixed evidence.
Both exponential arguments, both pre-clip inequalities and all index
labels are bound; the midpoint, log clip seven and all loops stay fixed.
The five step-424-to-431 worker changes and the two changes at each
of 431-to-435 and 435-to-440 reconstruct entire workers, reviews and
diffs. The step-440 coordinator, complete manifest and ten-source map
are checked. Complete texts compile at optimization zero before import.
Historical entrypoints are data only, never executed.

All THREE original identities for each index agree with its resolved
step-440 directory, kernel_440_n prefix and actual producer/replayer
hashes. The fresh schema instead binds index, fixed directory, new
output directory, fixed_replay_442_n module and actual replayer hash.
These schemas are compared separately. Index, paths, module object,
sentinel and source identity are checked before/after installation and
after replay; original primitive and counter captures are retained.

**Lexical controls.** The installer is byte-identical to steps 437,
433 and 422. Its whole function body equals the retained signed block;
AST checks retain all nine wrappers, allowed calls/defaults, closure
captures and the absence of imports, global/nonlocal directives or
worker-namespace access. Only the designated worker/preflight function
sites change: identity_for's fixed path/module prefix, check_identity's
index tuple and preflight's index tuple. The -422 sentinel and installer
labels stay unchanged. Full adaptation sites and diffs are persisted.

Four inert preflights finish before any kernel. Separate modules,
counters and closures retain immutable metadata and all nine wrappers
after return. Each callback is deep-copied once, giving floor=ceiling=57,
multiply=36, zero-operand products=11 and all nine sign bins
(9,6,3,6,4,2,3,2,1); controls and ledger are then cleared.
The preflights test controls, not kernel values.

**Full independent arithmetic.** Each fresh child imports only its fixed
replayer and reconstructs the entire unchanged L103 parameter: both
25-term arctangent lists and sums, exact pi endpoints and conversions,
independent binary square-root search and strict squared inequalities,
c endpoints, midpoint and delta. Every one of 1016 panels is rebuilt,
including all 128 scalar terms, sixteen squares, 129/65/65 factor slots,
193/257 product slots, all 21264880 coefficient pairs, integration
divisors and running sums. Digests supplement this full reconstruction.
The sign-case replayer is checked throughout by distinct four-product
extrema, with exact signed quotient inequalities for all roundings.
Addition, negation, clip, conversion and division wrappers compare
their entire results. Inline convolution/log additions use exact grid
integers and satisfy 21787232=521336+21264880+1016. The source's
2033 scales and 2034 enlargements, including the final +/-2^72, are
explicit integer expressions; no floating arithmetic is omitted.

Complete fresh returned reports and deep-copied count/signed snapshots
are persisted BEFORE comparison. Every report field agrees with the
original and the whole worker contract; adding only n gives replay.json.
Both full original ledgers, fresh counts and kernel counts agree with
the complete map above. Each pass has 21801456 distinct multiplication
checks, 716408 divisions, 5083 conversions, 356616 negations, 24386
clips, 521336 wrapped additions and 2032 full products. Each directed
rounding count is 22522948. Actual sign bins are
(5644008,5527040,0,5266944,5363464,0,0,0,0), with 896 zero-operand
products. The inert controls cover bins absent in actual panel data;
they do not claim those bins occur during replay. Complete parameter
identity, working/status/completed records and child exits retain every
field, including identity_unchanged and full_returned_report_persisted.

Every final kernel field matches full replay and this lemma's endpoint
table. Polynomial widths are exactly 1389,1270,1186,1130 grid units;
the final endpoints enlarge each side by exactly 2^72. Thus the radii
are precisely (2^73+w_n)/2^257, with reduced fraction encodings allowed.
Exact rational tests verify both strict bounds <2^-183 and <2^-50.
Together with imported L102 this validates the four J_n(c_*) enclosures.
Neither an interval for the actual transcendental parameter nor a
derivative sign is obtained by this audit.

**Preservation and resources.** All ten complete inventories at steps
417/419/422/424/429/431/433/435/437/440 reconcile with their exact
transition suffixes through post-440. Every before value matches before
applying after; no pathname exemption or rebaselining occurs. The whole
683-entry step-440 inventory, original preservation/source maps, manifest,
reports and terminal/finalization records pass. Its original historical
reconciliation is checked at its post-437 boundary, separately from the
post-440 transition applied to current bytes. Historical tree accounting
recovers 5779283 bytes including reserve and the recorded 109-second
bound. Its exact parent-exit timestamp and all earlier timing caveats
remain unverified; fresh evidence does not repair them.

The fresh inventory has 777 inputs, including entire step-440/437 trees,
all prior roots retained by step-440, stopped 426/429 and the explicitly
outside-historical-cap 429-postmortem archive. One timer starts before
imports/setup/inventory/source generation and remains armed through
final reporting; each child receives only remaining work time. All four
zero-code exits are observed at 33.06341241719201, 65.94282500003465,
99.10540254204534 and 132.85354658402503 seconds. Terminal writing
begins at 132.99844737513922 seconds; post-terminal finalization records
133.04581600008532 seconds and 364743 disk bytes. Original hashes,
entire tree file sets and fresh sources are rechecked after terminal
writing. Final actual elapsed/disk assertions and tool-observed parent
exit zero establish conservative inclusive bounds 136 seconds and
495028 new bytes, against 180 and 134217728. The 131072-byte finalization
reserve and 8192-byte diagnostic allowance are retained. Python 3.15.0
with optimization zero is recorded; a signal is not a hard dispatch
guarantee, and this successful observation gives no future runtime bound.

The subsequent editorial completion of this lemma and the pre-execution
note is recorded in `drafts/2026-10-24-l109-audit-document-transition.json`,
outside the measured execution. No fixed certificate is changed. Direct
mathematical inputs and the DAG remain unchanged. This is local validation
of known-method inputs, not progress beyond the checked sources or a new
BSD case. All stated downstream gaps remain.

## Mathlib

Full matching certificate/algorithm coverage has not been checked.
L103 records supporting Machin-identity coverage; that supporting result
does not formally verify these programs or establish a full match.
No assertion of absence from Mathlib is made. The proof here imports
audited L102's analysis and retains the actual finite replay evidence.
