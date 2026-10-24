# L110 — Fixed midpoint kernels n=23–26

## Hypotheses

Use L101's definition
J_n(t)=integral_1^128 exp(-nty) log(y)/y dy, L031's exact signed
endpoint rules, audited L102's full rational Taylor scheme and the
entire audited L103 parameter. Put D=2^256 and

```
c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2*D).
```

L103 supplies c_* in [3/10,1/2], its enclosure of 2*pi/sqrt(389)
and its delta; none is scaled with n. L101 is used only for the kernel
definition. No L035 complex order, published rank, period normalization,
Sha assertion, signed audit installer or optional numerical library enters.
The fixed complete evidence is `scripts/four-rational-kernels/step-449/`.

## Conclusion

For each row below, J_n(c_*) belongs to [l_n/D,u_n/D]. Both endpoints
are integers on the unchanged grid. Write the exact radius as
(2^73+w_n)/2^257.

| n | l_n | u_n | w_n |
|---|---|---|---|
| 23 | 1021756564506792060330755703534906169491502437168274794326260559722624902 | 1021756564506792060330755703534906169491502437168284239059226299013053388 | 1094 |
| 24 | 690165451249566804868994887805548124413246779208805522011949498962681657 | 690165451249566804868994887805548124413246779208814966744915238253110121 | 1072 |
| 25 | 467445919344060726550573376514386897266364132705937603376649747396740705 | 467445919344060726550573376514386897266364132705947048109615486687169149 | 1052 |
| 26 | 317393104637852413926090736782105029632288286539640333106009221668763236 | 317393104637852413926090736782105029632288286539649777838974960959191673 | 1045 |

All four exact radii are strictly below 2^-183 and 2^-50. Complete
production and independent replay pass for all 1016 panels and all
21264880 coefficient pairs per pass per index. One aggregate execution
observes four zero-code child exits and preserves all 913 inventoried
inputs after terminal reporting, with inclusive bounds 112 seconds and
5921349 new bytes, below 180 seconds and 134217728 bytes. The parent
is also observed to exit zero. The separate step-451 critical audit below
passes all four complete signed replays and post-terminal preservation.

This is known-method REPRODUCTION of finite midpoint inputs. It leaves
102 kernels, signed assembly, exact-parameter transfer and strict zero
exclusion. It gives no new BSD case or arbitrary-curve comparison.

## Proof

**Imported analysis and applicability.** Import audited L102, without
reproving its Taylor error estimates. Its precise standard inputs include
NIST DLMF v1.2.8, Taylor theorem equations
[1.4.35–37](https://dlmf.nist.gov/1.4.vi), integration/change of variable
[1.4.26](https://dlmf.nist.gov/1.4.E26),
[1.4.28](https://dlmf.nist.gov/1.4.E28) and the integral bound
[1.4.29](https://dlmf.nist.gov/1.4.E29), with the elementary series
specified in L102. Every new index is an integer in [1,128]. The entire
unchanged L103 parameter gives a rational c_* in L102's closed range.
On all 1016 positive panels the logarithm and reciprocal are smooth
through the endpoints, including y=1; the exponential is entire.
The existing SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-twenty-three-through-twenty-six-direct.md`.
The specialization here is finite execution and independent arithmetic
replay, not a new analytic estimate or a runtime consequence of L102.

**Whole-source specialization.** The actual direct command argument is
retained verbatim in `coordinator.py`; it is not sliced or reconstructed
using a marker within itself. Its complete text is compiled with
flags=0, dont_inherit=True and optimize=0. The actual interpreter/version
and optimization flag are in `manifest.json`. The complete step-440
production worker is adapted at exactly two unique sites: its allowed
index tuple and module prefix. `worker-source-review.json` and the full
diff retain both changes. No audit worker, installer, preflight or L106
endpoint is used as a production input.

The step-417 PARENT literal is extracted from its unique top-level AST
assignment as data; that entrypoint is never executed. Its unique
replacement expression is restricted to literals/containers, formatted
strings, addition, names n and str, and calls to str. For each selected
index the full step-412 producer and independent replayer are reconstructed
by exact-once replacements. Both full texts compile before their import.
All changes and full source diffs are persisted separately for every n.
They bind the producer's scalar argument n*u*a8/(v*8*2^16), beta
n*u/(8*v), both pre-clip assertions, both corresponding replay arguments
num*endpoint*n/(den*524288) and num*n/(den*8), all n labels and paths.
The log clip seven, full parameter, signed arithmetic and all loops
remain unchanged. Neither stopped step 444 nor the stopped 426/429
launchers is repaired or executed.

**Parameter and all panel arithmetic.** Each isolated child binds an
immutable tuple of index, absolute destination, module prefix and both
complete source hashes. The same module objects, paths, names and hashes
are checked before production, after production and after replay. The
producer reconstructs the entire parameter record and compares it with
the audited step-404 record; the independent replayer reconstructs every
arctangent term, adjacent sum, pi bound, square-root witness, directed
conversion, c endpoint, midpoint and delta. Equality of the whole record,
rather than its midpoint alone, is required.

All panel endpoints a=(8+j)/8, 0<=j<1016, reductions k and scalar
logarithm/exponential constants are reconstructed. The unchanged arrays
have lengths 129,65,65 and their complete products have lengths 193,257;
no coefficient pair, zero slot or high-degree contribution is dropped.
The independent replayer traverses both convolution indices backwards
with the opposite outer factor, uses sign-based endpoint extrema instead
of the producer's four-product extrema and independently checks every
signed floor/ceiling by its defining integer inequalities. It rebuilds
all factor/product arrays and scalar traces before comparing their stage
digests, then checks every panel integral and running sum. Integration
retains all divisors 1,...,257 and dy=ds/8. Complete panel count is
1016, and pair count is 1016*(8385+12545)=21264880 per pass per n.

Full returned reports and both count ledgers are deep-copied and saved
before comparison. Every report field is checked; `replay.json` adds
only n to the complete returned report. Both ledgers and every returned
count map equal

```
add=21787232, clip=24386, coefficient_pairs=21264880,
convert=5083, divide=716408, enlarge=2034,
multiply=21801456, negate=356616, scale=2033.
```

The replayer checks every final endpoint, polynomial sum, midpoint,
radius, grid denominator and both required radius fields. On each side
the final enlargement is exactly 2^72 grid units, namely L102's 2^-184
analytic allowance. Consequently audited L102 turns these completely
replayed polynomial intervals into containing intervals for J_n(c_*).
The endpoint differences are exactly 2^73+w_n in the table, proving
the displayed radii. Since 0<w_n<=1094<2^73, their numerators are less
than 2^74, so each radius is strictly below 2^-183 and hence 2^-50.
The programs separately check both inequalities with exact Fractions.
These arithmetic/containment checks, not displayed previews or hashes
alone, establish the finite result.

**Provenance and one capped lifecycle.** Initial capture includes the
whole historical trees, every path named by their complete inventories,
selected canonical inputs, review records, ATTEMPTS/045–050 and the new
unfinished attempt note. Successful historical inventories are reconciled
through the twelve ordered exact transitions from post-417 to post-446,
with suffix starts 0,...,11. Each before value must match before applying
its after value; there are no path exemptions or rebasing. Complete
original historical reports are checked at their own boundaries: in
particular step 440 at post-437, step 442 at post-440 and step 446 at
post-442. The full step-446 report schema and complete fresh-source map
are retained and checked as data. The entire failed step-444 tree is
frozen separately, with its false preservation flags, absent initial
inventory and absent finalization unchanged. Historical timing and
step-429 postmortem qualifications are preserved.

One clock starts before setup, reads, capture, source generation,
compilation and imports. The 174-second work deadline, remaining child
timeouts, aggregate byte checks and 131072-byte report/diagnostic reserve
operate within one 180-second/134217728-new-byte cap. Each child completes
production and replay before the next starts. Observed zero exits occur
at elapsed seconds 26.966716000111774, 54.09039858309552,
81.26681725005619 and 107.8513965420425, in order. No failure, retry,
resumption, enlarged cap or other kernel occurs.

`preservation.json` reports complete capture, 913 original files, no
mismatches, identical full tree sets and identical fresh sources. After
writing `terminal-report.json`, all originals, tree sets and sources are
checked again. `finalization.json` records post-terminal preservation
at elapsed 108.07217329205014 seconds, with 5791091 bytes before its own
write. The source then verifies its inclusive bounds 112 seconds and
5921349 new bytes, including the diagnostic allowance, with its timer
still armed; the tool observes parent exit zero. Exact parent-exit time
is not independently retained, and an armed Python signal alone is no
dispatch-time guarantee. No fresh timing claim repairs earlier historical
timing qualifications. The separate critical audit is recorded below.

These are only J_n(c_*) inputs. L101's full signed sum, all remaining
kernels, transfer to c and strict exclusion of zero have not been executed.
L035 already imports the fixed curve's analytic order, so this changes
finite-certificate provenance and no known BSD scope. Full Sha, refined
BSD and arbitrary-curve rank comparison remain independent gaps.

### Separate critical audit — 2026-10-24, step 451

The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-twenty-three-through-twenty-six-audit.md`.
This is one REPRODUCTION proof audit, importing the already audited L102
analysis under exactly the hypotheses above. No new analytic bound or
producer is used. All four indices lie in [1,128]; the complete L103
parameter is unchanged and belongs to [3/10,1/2]. The positive panels
retain every smoothness hypothesis. The proof above identifies the
replayed full polynomial integrals with L102's scheme; the final analytic
enlargement remains exactly 2^-184 on each side.

Evidence is `scripts/four-rational-kernels/step-451/`. Its direct
`coordinator.py` is the whole actual command argument, compiled at
optimization zero without self-slicing. It reconstructs all eight whole
arithmetic texts from the step-412 templates and restricted step-417
expression, and compares every exact replacement, full source diff and
source-review field. Both exponential arguments and both pre-clip tests
are bound to the selected index. The entire step-449 production worker
is reconstructed from its two step-440 changes. Its complete coordinator
is compiled and included in the whole ten-source map; no historical
entrypoint executes. All three original identities per index agree
with the actual paths, module prefixes and complete source hashes.

The audit worker and preflight use only the approved step-446 AST sites:
the fixed path, unique module prefix, allowed-index tuple and preflight
loop. All untouched AST content is retained. The complete lexical
installer is byte-identical to the retained earlier installer. Static
binding and call checks retain the -422 sentinel, one immutable identity
binding and all nine original primitive captures. Four inert preflights
pass before any kernel runs; they test all nine sign classes and verify
the closure bindings again after return. Their counters are cleared
before the numerical replay.

The four isolated complete replays run in order 23,24,25,26. Each
reconstructs the entire parameter, all 1016 panels, both full convolutions
and 21264880 coefficient pairs. Independent four-product extrema and
integer inequalities check every signed multiplication and rounding.
Per index, the signed evidence records 21801456 multiplications,
716408 divisions, 5083 conversions, 356616 negations, 24386 clips,
521336 additions outside the direct convolution/running accumulations,
2032 full products and 22522948 floor/ceiling checks each. All 896
zero-operand multiplications are retained. Actual sign-case counts are
(5644008,5527040,0,5266944,5363464,0,0,0,0); the numerical replay is
not asserted to encounter all nine classes. The separate inert controls
cover all nine. Every returned report field, both original ledgers,
the fresh ledger and original/fresh identity records pass comparison.

Every kernel field is checked, including the exact endpoints in the
table, polynomial sum, midpoint, reduced rational radius and both
threshold fields. The exact widths remain 2^73+w_n grid units with
w_n=(1094,1072,1052,1045); the same rational calculation above gives
radius <2^-183<2^-50. Neither a displayed decimal nor a saved PASS
replaces this complete arithmetic verification.

The historical comparison retains all thirteen exact transitions in
inventory order 417/419/422/424/429/431/433/435/437/440/442/446/449,
with suffix starts 0–12. Complete original reports are compared at their
own boundaries, including step 449 at post-446 and its entire nested
step-446 report. The exact post-449 note transition is applied only
after that original boundary. All original inventories/source maps,
failed step-444 flags and absent capture/finalization, ATTEMPTS/045–050
and the outside-cap step-429 postmortem are preserved without exemptions.
The guarded step-449 manifest, terminal, finalization, child exits,
completed records, stdout/stderr and byte accounting are checked in full.
Historical exact parent-exit timing remains qualified.

One clock covers setup through source construction, capture, preflights,
all replays and final reporting. The four zero-code child exits are
observed at elapsed seconds 33.54461995791644, 67.05837224982679,
100.93009062483907 and 134.20911762490869. All 1007 inventoried inputs,
complete tree file sets and fresh sources agree after terminal writing.
Finalization records elapsed 134.62215029099025 seconds and 629166
bytes before its own write. Conservative inclusive bounds are 138
seconds and 759422 new bytes, below 180 and 134217728, including the
131072-byte reporting/diagnostic reserve. The timer stays armed; the
parent is observed to exit zero. No exact parent-exit timestamp or
hard Python signal-dispatch guarantee is claimed. No failure, retry,
resumption, producer or additional kernel occurs within this invocation.

Thus this separate fixed critical audit passes. It validates the existing
four J_n(c_*) inputs only. It produces no additional kernel and leaves
the 102 missing kernels, full signed assembly, parameter transfer and
strict zero exclusion, as well as the independent general BSD gaps.

## Mathlib

Full matching algorithm/certificate coverage is unchecked, not asserted
absent. L103 records the supporting Machin-identity theorem; it does not
formally verify these programs or replace the complete finite replay.
