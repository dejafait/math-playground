# L113 — Fixed midpoint kernels n=35–38

## Hypotheses

Use L101's definition J_n(t)=integral_1^128 exp(-nty) log(y)/y dy,
L031's signed rational endpoint rules, audited L102's rational Taylor
scheme and the entire audited L103 parameter. Put D=2^256 and

```
c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2*D).
```

L103 supplies c_* in [3/10,1/2], the enclosure of 2*pi/sqrt(389)
and delta. The entire parameter record is unchanged with n. L101 is
used only for the kernel definition. No rank, complex order, Sha,
period normalization, previous kernel endpoint, audit installer or
numerical library enters this arithmetic. Complete evidence is in
`scripts/four-rational-kernels/step-461/`.

## Conclusion

For every row J_n(c_*) belongs to [l_n/D,u_n/D], with exact radius
(2^73+w_n)/2^257.

| n | l_n | u_n | w_n |
|---|---|---|---|
| 35 | 10642145968790247487971635503900840727586193978973851418810326357484636 | 10642145968790247487971635503900840727586193978983296151776065647913048 | 1020 |
| 36 | 7355623622663299655428087756299660345806927993395166219778907190674477 | 7355623622663299655428087756299660345806927993404610952744646481102889 | 1020 |
| 37 | 5090551164673843549583973683791171174095576720439237446564613924511620 | 5090551164673843549583973683791171174095576720448682179530353214940029 | 1017 |
| 38 | 3527260635679429274436911608240773538424208377624060960453359781669043 | 3527260635679429274436911608240773538424208377633505693419099072097452 | 1017 |

All radii are strictly below 2^-183 and 2^-50. All four complete
production/independent replay pairs pass, retaining 1016 panels and
21264880 coefficient pairs per pass/index. One aggregate invocation
observes four zero-code child exits and the tool observes parent exit
zero. All 1391 captured inputs survive preservation after terminal
writing, under inclusive bounds 119 seconds/12393323 new bytes versus
180/134217728.

This is known-method REPRODUCTION. The separate step-463 critical audit
below passes all four full signed replays, with all 1486 captured inputs
preserved after terminal writing, inclusive bounds 147 seconds/13663063
new bytes, four observed zero-code children and tool-observed parent
exit zero. These bounds are below 180 seconds/134217728 bytes.
Ninety kernels, signed assembly, exact-parameter transfer and strict
zero exclusion remain. The arbitrary-curve rank comparison, full Sha
and refined BSD remain unresolved. L035 already imports this fixed
complex order; no new BSD case or candidate follows.

## Proof

**Imported analysis and applicability.** Apply audited L102 without
reproving its estimates. Its precise standard inputs include NIST DLMF
v1.2.8, Taylor theorem [1.4.35–37](https://dlmf.nist.gov/1.4.vi),
continuous integration [1.4.26](https://dlmf.nist.gov/1.4.E26),
change of variable [1.4.28](https://dlmf.nist.gov/1.4.E28), integral
bound [1.4.29](https://dlmf.nist.gov/1.4.E29), and the elementary
series/derivative identities specified in L102. Every requested integer
lies in [1,128] and the rational midpoint is in [3/10,1/2]. All log
and reciprocal arguments are positive on every panel, including y=1;
exp is entire. Thus the smoothness, branch and range hypotheses hold.
The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-thirty-five-through-thirty-eight.md`.
The known results cover the analytic scheme; only this approved fixed
execution and its complete independent arithmetic replay are supplied
here. Citations alone prove neither source correctness nor feasibility.

**Whole-source specialization.** The direct coordinator retains its
whole actual -c argument via sys.orig_argv, without self-slicing, and
compiles at flags=0, dont_inherit=True, optimize=0. Its complete diff
against step 457 is retained. The entire step-457 worker changes at
exactly two unique sites: allowed tuple (31,32,33,34) becomes
(35,36,37,38), and module prefix kernel_457_ becomes kernel_461_.
The complete worker diff and change record precede imports.

The unique top-level PARENT literal in step 417 is extracted as inert
data. Its unique replacements expression permits only literal
containers, formatted strings, addition, names n/str and calls to str.
No old entrypoint executes. Complete step-412 producer/replay templates
are adapted at exact-once sites and compiled before import. Complete
maps/diffs bind both producer arguments n*u*a8/(v*8*2^16), n*u/(8*v),
replay arguments num*endpoint*n/(den*524288), num*n/(den*8), both
corresponding pre-clip tests in each implementation, index labels and
destination descriptions. Log clip seven, grid, degrees, series,
loops and the entire parameter stay unchanged. No signed installer,
preflight or old endpoint enters production. Stopped 426/429/444 are
not repaired or executed.

**Parameter, panels and independent arithmetic.** Each immutable
identity binds index, absolute destination, unique module prefix and
both source hashes. The same module objects and source files are
checked before production, after production and after replay. Every
producer reconstructs and compares the whole step-404 parameter record.
The replay independently rebuilds both 25-term arctangent records,
adjacent sums, Machin bounds, pi grids, binary-search square-root
witness and squared inequalities, both outward c endpoints, midpoint
and delta. Equality is of the entire fixed record, not only c_*.

For j=0,...,1015 set a=(8+j)/8 and y=a+s/8, 0<=s<=1.
Each scalar series, binary logarithm reduction and panel array is
reconstructed. The factor lengths are 129,65,65 and the full product
lengths 193,257. Each panel retains 8385+12545 coefficient pairs,
giving 21264880 per pass. The replay reverses both coefficient
traversals and switches the outer factor. Its sign-case multiplication
is independent of the producer's four-product min/max formula; every
floor and ceiling is checked by its defining integer inequalities.
Full scalar traces and coefficient arrays are rebuilt before digest
comparisons. Every stored panel field, signed integral and running
sum agrees, including zero slots, divisors 1,...,257 and dy=ds/8.

Deep copies of the complete returned report and both ledgers are
persisted before comparison; replay.json adds only n to the returned
report. Every report field and both full count maps agree:

```
add=21787232, clip=24386, coefficient_pairs=21264880,
convert=5083, divide=716408, enlarge=2034,
multiply=21801456, negate=356616, scale=2033.
```

Final comparisons include the polynomial sum, grid denominator,
endpoints, midpoint, reduced radius and both threshold fields. The
final enlargement is exactly +/-2^72 grid units, or +/-2^-184, as
required by L102. Its analytic containment therefore applies to the
completely replayed polynomial intervals. The endpoint differences
are 2^73+w_n, with 0<w_n<=1020<2^73. Thus each radius is strictly
less than 2^74/2^257=2^-183, hence also less than 2^-50. Both strict
tests pass exact Fraction comparison, including denominator reduction.
Stored PASS labels and hashes are not substitutes for reconstruction.

**Recursive provenance.** Initial capture includes entire historical
trees, every inventoried path, selected mathematical/review inputs,
ATTEMPTS/045–050 and the saved unfinished attempt. Eighteen transition
suffixes through post-459 are applied in order
417/419/422/424/429/431/433/435/437/440/442/446/449/451/453/455/457/459,
with suffix starts 0–17. Every before value matches before applying
after. Whole recursive original reports keep their own boundaries:
449 post-446, 451 post-449, 453 post-451, 455 post-453, 457 post-455
and 459 post-457. There is no projection, rebasing or pathname
exemption. All original inventories, complete tree sets and source
maps match, including step-457 production sources and all five
step-459 fresh sources. The latter audit tree is inert provenance,
not an arithmetic input. Failed-444 STOP/false flags, empty exits and
completions, absent initial capture/finalization, step-429 postmortem
and every historical timing qualification are preserved.

**Single bounded lifecycle.** One clock covers setup/imports,
capture, source materialization, all four complete pairs and final
writing. It has a 174-second work deadline, remaining child timeouts
and 131072-byte reserve inside one 180-second/134217728-new-byte cap.
Pairs execute once in order 35,36,37,38. Four zero-code child exits
are observed at elapsed seconds 27.724650959018618, 58.11481299996376,
86.98539887508377 and 114.96859887498431. All 1391 captured inputs,
whole tree sets and fresh sources match after terminal writing.
Finalization records elapsed 115.3095315839164 seconds and 12263067
bytes before its own write; conservative inclusive bounds are
119 seconds and 12393323 new bytes. The required bounds are 180
seconds and 134217728 bytes. No failure, retry, resumption, larger
cap or other kernel occurs.

The timer stays armed through final writing and the tool observes
parent exit zero. An exact retained parent-exit timestamp and a hard
Python signal-dispatch guarantee are not claimed. Actual interpreter:
Python 3.15.0, optimize=0, as retained in manifest.json. Fresh timing
repairs no historical qualification. These are J_n(c_*) inputs only;
signed assembly, exact-parameter transfer and derivative nonvanishing
remain to be established. These production claims are distinguished
from the separate critical audit below.

### Separate critical audit — 2026-10-24, step 463

**Scope and imported containment.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-thirty-five-through-thirty-eight-audit.md`.
The complete fresh evidence is in `scripts/four-rational-kernels/step-463/`.
The attempt audits existing midpoint inputs; it executes neither producer
nor historical entrypoint and introduces no new analytic estimate.
Apply the audited L102 containment theorem at the same entire audited
L103 parameter and integer indices 35–38. The positive panel arguments,
smoothness and branch hypotheses of the standard DLMF inputs cited
above are unchanged. This applicability argument and complete arithmetic
reconstruction suffice; no reproof of Taylor's theorem is needed.

**Whole sources and lexical controls.** The direct coordinator retains
and compiles its whole actual `-c` argument with flags=0,
dont_inherit=True, optimize=0, preserving its complete diff against
step 459. The whole original step-461 coordinator is compiled and its
diff against step 457 checked. The production worker is reconstructed
from the whole step-457 worker with exactly the two approved changes.
The restricted step-417 expression reconstructs all eight complete
arithmetic texts from the whole step-412 templates; every exact-once
change, complete diff, review map and the ten-source hash map agrees.
Both scalar and panel exponential arguments and both pre-clip tests
are bound at each index. All three original identities per index match
the fixed path, unique production prefix and both source hashes.

The step-459 installer is byte-for-byte unchanged. Worker/preflight
adaptation changes only identity_for's fixed path and fresh prefix,
check_identity's allowed tuple and the preflight loop tuple. Exact
changed AST-site lists, untouched AST, static bindings, permitted calls
and all nine closure captures are checked before any replay. The -422
sentinel and installer labels remain unchanged. All four inert
preflights pass; their controls cover all nine multiplication sign
cases, eleven zero-operand controls and 21 quotient controls. Counters
and the replay ledger reset afterward. Distinct immutable fresh
identities and original primitive/counter captures survive each replay.

**Complete signed reconstruction.** Each replay independently rebuilds
the entire L103 parameter record, including both arctangent term lists
and adjacent sums, pi grids, square-root witness and squared inequalities,
both c endpoints, midpoint and delta. Every one of 1016 panels is
reconstructed, including scalar traces, full coefficient arrays, reverse
convolutions with 21264880 pairs, every stored field, signed integrals
and running sums. No digest or saved PASS label replaces reconstruction.
The unchanged installer checks every encountered floor/ceiling by its
integer inequalities and every interval product by the four extrema,
independently of the replayer's sign-case implementation; it also checks
division, conversion, addition, negation, clipping and product lengths.

Deep copies of the full returned report and both fresh ledgers are saved
before comparison. Complete reports, original ledgers, metadata addition
of n only, final grid, polynomial sum, midpoint, reduced radius, parameter
identity and status contracts all agree. The full count map above is
unchanged. For every index the signed counts include multiply=21801456,
divide=716408, convert=5083, negate=356616, clip=24386, plus=521336,
products=2032 and floor=ceiling=22522948. The latter equals multiply+
divide+convert+1. The observed sign-case vector is
[5644008,5527040,0,5266944,5363464,0,0,0,0], summing to multiply;
there are 896 zero-operand multiplications. Missing sign cases in this
particular arithmetic are covered by the separate inert controls.

The endpoints are exactly those in the conclusion. Exact Fraction
comparison checks the reduced midpoint and radius, the enlargement of
exactly +/-2^72 grid units, u-l=2^73+w and both strict radius tests.
In particular 0<w<=1020<2^73 gives radius <2^-183<2^-50.
The denominator reduction for n=35,36 is retained. L102 therefore
encloses J_n(c_*), without asserting an enclosure at the exact c.

**Provenance and bounded lifecycle.** All nineteen transition suffixes
through the exact post-461 note edit pass with matching before values.
Every complete recursive report remains at its original boundary:
449 post-446, 451 post-449, 453 post-451, 455 post-453, 457 post-455,
459 post-457 and 461 post-459. All original inventories, complete trees
and source maps match, including the five step-459 fresh sources and
ten step-461 production sources. No projection, rebasing or pathname
exemption is used. Failed-444 flags, absences and empty exits/completions,
step-429 postmortem, ATTEMPTS/045–050 and all historical timing
qualifications remain intact. Complete step-461 manifest, terminal,
finalization, exit, status, working and stdout contracts and byte/reserve
relations are checked against the whole source.

One clock starts before setup/imports, capture and materialization;
the four signed replays execute once in order. Observed zero-code
child exits occur at elapsed seconds 38.88985725003295,
74.46013008314185, 109.32942504202947 and 143.73006833298132.
All 1486 captured inputs, whole tree sets and fresh sources match
after terminal writing. Finalization records elapsed
144.12638491694815 seconds and 13532806 bytes before its own write.
Inclusive bounds 147 seconds/13663063 new bytes satisfy the required
180/134217728, with 174-second work deadline and 131072-byte reserve.
The timer remains armed through final writing; the tool observes
parent exit zero. No failure, retry, resumption, enlargement or other
kernel occurs. Actual interpreter is Python 3.15.0, optimize=0.

An exact retained parent-exit timestamp and hard Python signal-dispatch
bound remain unproved, including historical qualifications. The later
editorial update to this file and the attempt note is recorded in
`drafts/2026-10-24-l113-audit-document-transition.json`; it does not
change the pre-edit preservation statement. This validates known-method
midpoint inputs only. Ninety kernels, signed assembly, exact-parameter
transfer and zero exclusion remain; the general rank comparison,
full Sha and refined BSD are unresolved. No candidate is asserted.

## Mathlib

Full matching coverage is not checked; no absence claim or
formalization is asserted. Supporting integration and series theorems
are distinguished from a complete matching executable-certificate
theorem. Known-method production, independent replay and the separate
complete signed critical audit pass.
