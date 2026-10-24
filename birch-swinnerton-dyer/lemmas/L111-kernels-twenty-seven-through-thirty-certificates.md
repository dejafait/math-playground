# L111 — Fixed midpoint kernels n=27–30

## Hypotheses

Use L101's definition J_n(t)=integral_1^128 exp(-nty) log(y)/y dy,
L031's signed rational endpoint rules, audited L102's full rational
Taylor scheme and the entire audited L103 parameter. Put D=2^256 and

```
c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2*D).
```

L103 supplies the closed range [3/10,1/2], the enclosure of
2*pi/sqrt(389) and delta. The parameter is not scaled with n.
L101 is used only for the kernel definition. No published rank,
complex order, Sha assertion, period normalization, prior kernel value,
audit installer or optional numerical library enters the arithmetic.
Complete fixed evidence is in `scripts/four-rational-kernels/step-453/`.

## Conclusion

For each row J_n(c_*) belongs to [l_n/D,u_n/D]. The exact radius
is (2^73+w_n)/2^257.

| n | l_n | u_n | w_n |
|---|---|---|---|
| 27 | 216011097752688527767489019963378981102336647532379759389396180293383422 | 216011097752688527767489019963378981102336647532389204122361919583811848 | 1034 |
| 28 | 147332753619825458574163545974660418157564288075339303885391942506623672 | 147332753619825458574163545974660418157564288075348748618357681797052091 | 1027 |
| 29 | 100694579489652525236839297506599935040799942295864942490011448392783122 | 100694579489652525236839297506599935040799942295874387222977187683211544 | 1030 |
| 30 | 68951087956702293551898062566671723610170352074095254704953133359999755 | 68951087956702293551898062566671723610170352074104699437918872650428169 | 1022 |

All radii are strictly below 2^-183 and 2^-50. Complete production and
independent replay pass for all 1016 panels and 21264880 coefficient
pairs per pass per index. One aggregate run records four zero-code child exits; the tool observes
a zero-code parent exit. It preserves all 1071 captured inputs after
terminal reporting and meets inclusive bounds 111 seconds/6262741 new
bytes versus 180/134217728.

This is known-method REPRODUCTION. Its separate step-455 critical audit
passes all four complete signed replays, full source/provenance checks
and both strict radius tests, preserving all 1166 captured inputs after
terminal writing. Inclusive bounds are 138 seconds/1436439 new bytes
versus 180/134217728, with all child exits and the parent exit zero.
There remain 98 unproduced kernels, full signed assembly, transfer to
the exact transcendental parameter and strict zero exclusion. The main
arbitrary-curve rank comparison, full Sha and refined BSD gaps remain.
L035 already imports this fixed curve's order; no new BSD case follows.

## Proof

**Imported analysis and applicability.** Import audited L102 without
reproving its estimates. Its precise standard inputs include NIST DLMF
v1.2.8, Taylor theorem equations [1.4.35–37](https://dlmf.nist.gov/1.4.vi),
integration [1.4.26](https://dlmf.nist.gov/1.4.E26), change of variable
[1.4.28](https://dlmf.nist.gov/1.4.E28) and the integral bound
[1.4.29](https://dlmf.nist.gov/1.4.E29), with the elementary series
specified in L102. Each new n is an integer in [1,128]; the whole
unchanged L103 parameter is rational and lies in L102's permitted range.
All panels are positive, log and reciprocal are smooth through y=1,
and exp is entire. The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-twenty-seven-through-thirty.md`.
Citations alone do not provide executable correctness or feasibility.

**Whole-source specialization.** The coordinator retains its entire
actual direct -c argument without self-slicing; its full text compiles
with flags=0, dont_inherit=True, optimize=0. Its full diff against
step 449 is persisted. The whole step-449 production worker changes at
only two exact-once sites: allowed tuple (23,24,25,26) becomes
(27,28,29,30), and module prefix kernel_449_ becomes kernel_453_.
The complete worker diff and both changes are saved before import.

The unique top-level PARENT literal in step 417 is extracted as inert
data. Its unique replacement expression is restricted to literal
containers, formatted strings, addition, names n/str and calls to str.
No historical entrypoint executes. For every index the full step-412
producer/replayer texts are adapted with exact-once replacements and
compiled before imports. The saved full source maps/diffs bind both
producer arguments n*u*a8/(v*8*2^16), n*u/(8*v), both pre-clip tests,
the replay arguments num*endpoint*n/(den*524288), num*n/(den*8),
every index label and destination. Log clip seven, all degrees, scalar
terms, loops, precision and the entire parameter remain unchanged.
No step-451 worker, signed installer, preflight or endpoint executes
as production input; stopped 426/429/444 remain untouched.

**Complete parameter and arithmetic replay.** An immutable identity binds
index, absolute path, unique module prefix and both source hashes.
The same module objects and full sources are checked before production,
after production and after replay. Every producer reconstructs and
compares the whole step-404 parameter record. Independent replay checks
all 25 arctangent terms for each of 5 and 239, both adjacent sums,
Machin pi bounds, the independent binary-search square-root witness,
every squared inequality, outward conversion, c endpoint, midpoint
and delta. This checks the entire unchanged record, not only its midpoint.

Every a=(8+j)/8, 0<=j<1016, binary reduction and scalar trace is
reconstructed. Arrays have lengths 129,65,65 and their full products
lengths 193,257. The two convolution pair counts are 8385 and 12545;
1016*(8385+12545)=21264880 pairs are retained per pass. Replay reverses
both coefficient traversals and switches the outer factor, determines
multiplication extrema by signs independently of the producer's
four-product rule and checks every signed floor/ceiling using defining
integer inequalities. It rebuilds all full polynomial arrays/scalar
traces before comparing stage digests, all panel integrals and all
running sums. All divisors 1,...,257 and dy=ds/8 remain present.

Complete returned reports and both ledgers are deep-copied and persisted
before comparison. replay.json adds only n to returned-report.json.
Every field agrees; all four count maps in each child are exactly

```
add=21787232, clip=24386, coefficient_pairs=21264880,
convert=5083, divide=716408, enlarge=2034,
multiply=21801456, negate=356616, scale=2033.
```

The independent final comparison includes grid denominator, polynomial
sum, final endpoints, midpoint, reduced rational radius and both required
thresholds. Each final endpoint is enlarged by exactly 2^72 grid units,
that is 2^-184, as required by audited L102. Thus the completely replayed
polynomial intervals, with that analytic enlargement, contain J_n(c_*).
The endpoint differences in the table equal 2^73+w_n. Since 0<w_n<=1034<2^73, each numerator is less than 2^74, proving radius <2^-183 and hence <2^-50.
The programs also check both strict bounds using exact Fractions.
Hashes and previews alone are not the arithmetic verification.

**Whole provenance and bounded lifecycle.** Complete initial capture
includes all relevant historical trees, all paths in their inventories,
selected mathematical/review inputs, ATTEMPTS/045–050 and the unfinished
attempt note. Fourteen exact transition suffixes through post-451 are
applied in inventory order 417/419/422/424/429/431/433/435/437/440/442/
446/449/451, with suffix starts 0–13. Every applicable before value
matches before applying after; no path exemption or rebasing is used.
Whole recursive original reports retain their own historical boundaries:
449 remains at post-446 and 451 at post-449, including nested reports.
Guarded schemas and complete source maps are checked; the entire step-451
tree and its audit sources remain inert provenance. Failed-444 false
flags, empty completion/exit records and absent inventory/finalization
are explicitly preserved. Step-429 postmortem and historical timing
qualifications remain unchanged.

One clock starts before setup/imports/reads/source materialization.
The 174-second work deadline, remaining child timeouts and 131072-byte
report/diagnostic reserve lie within one 180-second/134217728-new-byte
cap. Complete production/replay pairs run once in order 27,28,29,30;
the first failure would stop all further work without retry or resumption.
Observed child exits occur at elapsed seconds 27.216252124868333, 53.86896295892075, 81.1261022919789, 107.66384854190983, all zero. Complete capture preserves 1071 inputs with no mismatches, equal whole tree sets and unchanged fresh sources. After terminal writing all three are checked again. Finalization records elapsed 107.91914195893332 seconds and 6132481 bytes before its own write; the verified inclusive bounds are 111 seconds and 6262741 new bytes. No failure, retry, resumption, enlarged cap or additional index occurs.

The timer remains armed through final writing. The tool observes parent
exit zero, but no exact parent-exit timestamp is independently retained;
Python signal dispatch alone is not a hard-time guarantee. Fresh timing
does not repair any historical qualification. These midpoint inputs do
not prove the full derivative sum, parameter transfer or nonvanishing.

### Separate critical audit — 2026-10-24, step 455

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-twenty-seven-through-thirty-audit.md`.
Complete fresh evidence is in `scripts/four-rational-kernels/step-455/`.
This is a separate REPRODUCTION proof audit, with no producer, additional
kernel, new analytic estimate or stopped-launcher repair. It imports
audited L102 under the same hypotheses verified above, using L031's
endpoint rules, L101's definition and the entire L103 parameter. The
arithmetic programs implement precisely those retained polynomials,
positive panel changes of variable and final analytic enlargement.

**Whole sources and bindings.** The direct coordinator retains its
whole actual -c argument and compiles it with flags=0,
dont_inherit=True, optimize=0; Python is 3.15.0. The complete original
step-453 coordinator diff against step 449 and ten-entry source map
agree. Its whole production worker is reconstructed from step 449 at
only the allowed tuple and module-prefix sites. All eight complete
producer/replayer texts are reconstructed from the step-412 templates
using the restricted step-417 data expression. Both exponential arguments,
both pre-clip tests, destination paths and every index label are checked,
with the full unchanged parameter, log clip, degrees, terms, precision
and complete loops retained. Every complete source diff/map agrees.
All three original identities per index match the reconstructed sources.

The whole step-451 signed worker/preflight changes only identity_for's
fixed directory 449 -> 453 and module prefix 451 -> 455, check_identity's
tuple (23,24,25,26) -> (27,28,29,30), and preflight's loop tuple. Exact
AST changed-site lists, the entire resulting AST and compilation pass.
The whole lexical installer is byte-identical to step 451 and the older
audited installer. Its body still matches the original signed-check block;
static checks retain the allowed call set, absence of global/nonlocal
binding, immutable selected identity, sentinel -422 and installer labels.
All nine primitive closures capture their actual originals and counters.
All four inert preflights pass before numerical replay, including the
post-return identity/closure tests and all nine sign classes. The control
counters and replay ledger are cleared before each actual replay.

**Full arithmetic.** Each isolated child reconstructs the entire
parameter, including both 25-term arctangent records, adjacent sums,
Machin pi grid, independent square-root witness, squared inequalities,
c endpoints, midpoint and delta. It checks all 1016 panels and both
full convolutions, retaining 21264880 coefficient pairs per index.
The signed wrapper compares every multiplication to four exact endpoint
products, and each signed floor/ceiling to its defining integer
inequalities. Positive divisions, conversions, additions, negations,
clips, product shapes and complete pair counts are checked separately.

Per index the distinct signed evidence has 21801456 multiplications,
716408 divisions, 5083 conversions, 356616 negations, 24386 clips,
521336 additions outside the direct convolution/running accumulations,
2032 full products and 22522948 floor and ceiling checks each.
It retains all 896 zero-operand multiplications. Actual sign counts
are (5644008,5527040,0,5266944,5363464,0,0,0,0); the actual numerical
run does not encounter all nine classes. The inert controls do.
Every field of each returned report, both original ledgers and the
fresh ledger agrees. Fresh identities and closure bindings are checked
before and after replay, separately from the original production identities.

Every kernel field agrees with the table and original evidence: the
polynomial sum, final endpoints, grid, midpoint, reduced radius, both
threshold fields and complete count map. The final analytic enlargement
is exactly +/-2^72 grid units. The widths are 2^73+w_n with
w_n=(1034,1027,1030,1022); rational equality handles reduced radius
denominators. Both strict tests radius <2^-183 and radius <2^-50 pass
for all four indices. Thus the imported containment proof applies to
the fully replayed arithmetic, not merely to its hashes or PASS labels.

**Provenance and lifecycle.** Fifteen transition suffixes are reconciled
in inventory order 417/419/422/424/429/431/433/435/437/440/442/446/
449/451/453, with suffix starts 0–14. Every before value matches before
its after value is applied. Whole recursive original reports remain at
their original boundaries: 449 post-446, 451 post-449 and 453 post-451.
No report is rebased or projected to a smaller schema. Complete tree
sets, original inventories and source maps pass; step 451 retains its
five-entry fresh-source map, while step 453 has its production map.
The failed-444 flags, empty exits/completions and absent capture and
finalization remain unchanged, as do ATTEMPTS/045–050, stopped launchers
and the outside-cap step-429 postmortem. The complete step-453 manifest,
terminal/finalization, stdout/stderr, completed records, child exits and
byte accounting agree with their source contracts. Historical exact
parent-exit timestamps and earlier timing qualifications remain unverified.

One clock starts before setup/imports/capture/source materialization,
with the 174-second work deadline and 131072-byte reserve inside the
180-second/134217728-new-byte cap. Zero-code child exits are observed
in order at elapsed seconds 34.03826533281244, 67.26752158300951,
100.66194904199801 and 134.46256324998103. All 1166 captured inputs,
complete tree sets and fresh sources agree after terminal writing.
Finalization records elapsed 134.7443839579355 seconds and 1306185
bytes before its own write. Conservative inclusive bounds are 138
seconds and 1436439 new bytes. The timer remains armed through final
writing; the tool observes parent exit zero. No exact parent-exit
timestamp or hard Python signal-dispatch guarantee is asserted. There
is no failure, retry, resumption, producer or additional index in this run.

This audit validates the existing four J_n(c_*) inputs only. It leaves
98 unproduced kernels, signed assembly, exact-parameter transfer and
strict zero exclusion, independently of the arbitrary-curve BSD gap.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
Supporting integration/series facts do not constitute a matching
executable-certificate theorem. This informal finite result has passed
production, independent replay and the separate fixed critical audit.
