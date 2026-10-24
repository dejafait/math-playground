# L112 — Fixed midpoint kernels n=31–34

## Hypotheses

Use L101's definition J_n(t)=integral_1^128 exp(-nty) log(y)/y dy,
L031's signed rational endpoint rules, audited L102's rational Taylor
scheme and the entire audited L103 parameter. Put D=2^256 and

```
c_* = 73775804382331484748893662180180200545104154546089041648426948815067512948607 / (2*D).
```

L103 supplies c_* in [3/10,1/2], the enclosure of 2*pi/sqrt(389)
and delta. The parameter is unchanged with n. L101 supplies only the
kernel definition. No rank, complex order, Sha, period normalization,
prior kernel value, audit installer or numerical library enters the
arithmetic. Complete evidence is in `scripts/four-rational-kernels/step-457/`.

## Conclusion

For each row J_n(c_*) belongs to [l_n/D,u_n/D]. Its exact radius
is (2^73+w_n)/2^257.

| n | l_n | u_n | w_n |
|---|---|---|---|
| 31 | 47299243292571405927683744156717475898369490350297430788003360049052671 | 47299243292571405927683744156717475898369490350306875520969099339481088 | 1025 |
| 32 | 32501213773206764811110412886976459706920933660629576922508159846488744 | 32501213773206764811110412886976459706920933660639021655473899136917158 | 1022 |
| 33 | 22368431105729947824919294895884768895159102326820296873817556244832377 | 22368431105729947824919294895884768895159102326829741606783295535260789 | 1020 |
| 34 | 15417848571534448461918545169608993122667517036757205020921596559363290 | 15417848571534448461918545169608993122667517036766649753887335849791700 | 1018 |

All radii are strictly below 2^-183 and 2^-50. All four complete
production/independent replay pairs pass, retaining 1016 panels and
21264880 coefficient pairs per pass/index. One aggregate invocation
observes four zero-code child exits; the tool observes parent exit zero.
All 1231 captured inputs survive post-terminal preservation, with
inclusive bounds 114 seconds/7507917 new bytes versus 180/134217728.

This is known-method REPRODUCTION; the separate step-459 critical audit
passes as detailed below.
There remain 94 unproduced kernels, signed assembly, exact-parameter
transfer and strict zero exclusion. The arbitrary-curve rank comparison,
full Sha and refined BSD remain unresolved. L035 already imports this
fixed curve's analytic order; no new BSD case or candidate follows.

## Proof

**Imported analysis and applicability.** Import audited L102 without
reproving its estimates. Precise standard inputs include NIST DLMF
v1.2.8, Taylor theorem [1.4.35–37](https://dlmf.nist.gov/1.4.vi),
integration [1.4.26](https://dlmf.nist.gov/1.4.E26), change of variable
[1.4.28](https://dlmf.nist.gov/1.4.E28), integral bound
[1.4.29](https://dlmf.nist.gov/1.4.E29), and the elementary series and
derivatives specified in L102. Each requested integer lies in [1,128],
and the entire unchanged L103 midpoint is rational in [3/10,1/2].
All panels are positive; log and reciprocal are smooth through y=1,
and exp is entire. The pre-existing SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-thirty-one-through-thirty-four.md`.
The citations supply neither program correctness nor capped feasibility.

**Whole-source specialization.** The direct coordinator retains its
entire actual -c argument via sys.orig_argv without self-slicing, and
compiles it with flags=0, dont_inherit=True, optimize=0. Its full diff
against step 453 is persisted. The whole step-453 production worker
changes only at two exact-once sites: allowed tuple (27,28,29,30)
becomes (31,32,33,34), and module prefix kernel_453_ becomes kernel_457_.
The entire worker diff and both edits are retained before imports.

The unique top-level PARENT literal in step 417 is extracted as inert
data. Its unique replacements expression is restricted to literal
containers, formatted strings, addition, names n/str and calls to str.
No old entrypoint executes. For each index, complete step-412 templates
are adapted at exact-once sites and compiled before import. The full
maps and diffs bind both producer arguments n*u*a8/(v*8*2^16),
n*u/(8*v), both pre-clip tests, replay arguments
num*endpoint*n/(den*524288), num*n/(den*8), index labels and destination
descriptions. Log clip seven, degrees, terms, loops, grid and the entire
parameter stay unchanged. No signed installer, preflight or prior
endpoint is a production input. Stopped 426/429/444 remain untouched.

**Parameter, panels and independent arithmetic.** Each immutable
identity binds index, absolute path, unique module prefix and both source
hashes. The same module objects and sources are checked before production,
after production and after replay. Each producer reconstructs and compares
the entire step-404 parameter. The independent replay rebuilds both
25-term arctangent records, adjacent sums, Machin bounds, pi grid,
binary-search square-root witness, squared inequalities, outward c
endpoints, midpoint and delta. It retains all fields, not just c_*.

For every j=0,...,1015 put a=(8+j)/8 and y=a+s/8, 0<=s<=1.
Each scalar series, binary logarithm reduction and panel array is
reconstructed. Factor lengths are 129,65,65; full product lengths are
193,257. There are 8385+12545 pairs per panel, hence 21264880 per pass.
The replay reverses both coefficient traversals and switches the outer
factor. It uses sign cases independently of the producer's four-product
min/max arithmetic, checking every signed floor and ceiling by its
defining integer inequalities. All full scalar traces and coefficient
arrays are reconstructed before digest comparisons. Every panel field,
integral, running sum and final field agrees, including all zero values,
divisors 1,...,257 and the dy=ds/8 factor.

Deep copies of complete returned reports and both ledgers are persisted
before comparison. replay.json adds only n to returned-report.json.
Every returned field and every original/fresh count map agrees:

```
add=21787232, clip=24386, coefficient_pairs=21264880,
convert=5083, divide=716408, enlarge=2034,
multiply=21801456, negate=356616, scale=2033.
```

Final comparisons include polynomial sum, grid denominator, final
endpoints, midpoint, reduced radius and both threshold fields. The final
enlargement is exactly +/-2^72 grid units, namely +/-2^-184, as required
by audited L102. Its analytic containment therefore applies to the
fully replayed polynomial interval. Endpoint differences in the table
are 2^73+w_n. Since 0<w_n<=1025<2^73, every radius is strictly less
than 2^74/2^257=2^-183 and hence 2^-50. Both strict tests also pass in
exact Fraction arithmetic, retaining any denominator reduction. Hashes
or PASS labels alone are not used as arithmetic verification.

**Recursive provenance.** Initial capture includes complete historical
trees, every inventoried path, selected mathematical/review inputs,
ATTEMPTS/045–050 and the unfinished attempt note. Sixteen transition
suffixes through post-455 are applied in order
417/419/422/424/429/431/433/435/437/440/442/446/449/451/453/455,
with suffix starts 0–15. Every before value must match before applying
after. Whole recursive original reports remain at their own boundaries:
449 post-446, 451 post-449, 453 post-451 and 455 post-453. No current
projection, smaller replacement schema or path exemption is used.
Complete original inventories, tree sets and source maps pass, including
453's production map and 455's five-entry fresh-source map. The full
step-455 tree is inert provenance. Failed-444 STOP/false flags, empty
exits/completions and absent capture/finalization remain preserved, as
do the step-429 postmortem and all historical timing qualifications.

**Single bounded lifecycle.** One clock starts before setup/imports,
capture and source materialization. The work deadline is 174 seconds,
with remaining child timeouts and a 131072-byte report/diagnostic reserve
inside the unchanged 180-second/134217728-new-byte cap. Complete pairs
run once in order 31,32,33,34; first failure would stop all further work.
Zero-code exits are observed at elapsed seconds 27.56380599993281,
54.433921499876305, 81.86765554104932 and 110.17523725004867.
All 1231 inputs agree with no mismatches, equal complete tree sets and
unchanged fresh sources; all are checked again after terminal writing.
Finalization records elapsed 110.48550220788456 seconds and 7377661
bytes before its own write. Conservative inclusive bounds are 114
seconds and 7507917 new bytes. There is no failure, retry, resumption,
cap enlargement or other kernel.

The timer remains armed through final writing; the tool observes parent
exit zero. No independently retained exact parent-exit timestamp or hard
Python signal-dispatch guarantee is asserted. Fresh timing repairs no
historical qualification. These are J_n(c_*) inputs only: signed assembly,
parameter transfer and derivative nonvanishing still require proof.

### Separate critical audit — 2026-10-24, step 459

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-kernels-thirty-one-through-thirty-four-audit.md`.
This audit imports the unchanged analysis above, with n=31,32,33,34
inside L102's range and the entire audited L103 parameter. No new
analytic estimate or reproof is needed. The complete fresh evidence is
`scripts/four-rational-kernels/step-459/`; no producer or other kernel
executes. The desired endpoint table is used only after reconstruction.

**Source and binding audit.** The direct coordinator retains its entire
actual command argument, compiles at optimize=0 and saves its whole diff
against step 455. It reconstructs the entire step-457 production worker
from step 453 at only its approved tuple and module-prefix sites,
compares the whole production coordinator/diff and ten-source map,
and reconstructs all eight arithmetic texts from the whole step-412
templates and restricted step-417 expression. Both selected-index
exponential arguments, both pre-clip tests and every original identity
are checked. The step-455 audit worker/preflight change only their
designated identity-path, module-prefix and index-tuple AST sites.
Exact site lists and the complete resulting AST agree. The lexical
installer is unchanged, including its sentinel and labels. Static
binding/allowed-call checks and four inert preflights verify all nine
primitive replacements and their closure captures before numerical work.

**Complete signed arithmetic.** For each index, the full parameter is
reconstructed, including both 25-term arctangent records, adjacent sums,
pi grids, square-root witness and inequalities, c endpoints, midpoint
and delta. All 1016 panels and 21264880 coefficient pairs replay.
Full scalar traces and coefficient arrays are reconstructed before their
digest comparisons. The installer independently checks multiplication
against all four products, signed floor/ceiling inequalities, positive
division, conversion, addition, negation, clipping and full polynomial
product shapes. Controls reset all counters before the actual replay;
the selected index and source/module identities remain unchanged.
Every returned-report field, both full original ledgers, fresh ledger,
original/fresh identities, panel/final field and endpoint comparison
passes. Each replay has 21801456 checked multiplications, 716408
positive divisions, 5083 conversions, 356616 negations, 24386 clips,
2032 polynomial products and 22522948 each of floor/ceiling checks.
The full count map is the one recorded above. The exact final enlargement
is +/-2^72 grid units. All four exact radii equal the table's
(2^73+w_n)/2^257, with w=(1025,1022,1020,1018), and both strict
comparisons to 2^-183 and 2^-50 pass. Thus the imported analytic
containment applies to these fully replayed midpoint intervals.

**Whole provenance and preservation.** Seventeen transition suffixes
through post-457 reconcile inventories in order
417/419/422/424/429/431/433/435/437/440/442/446/449/451/453/455/457.
Every before value matches before its after value is applied. Entire
recursive original reports retain their original boundaries, including
449 post-446, 451 post-449, 453 post-451, 455 post-453 and 457 post-455.
There is no rebasing, projection or pathname exemption. Every complete
historical tree/source map is retained, including the step-457 ten-source
map and step-455 fresh sources. Failed-444 flags/absences, the step-429
postmortem and ATTEMPTS/045–050 remain intact. Original production
manifest, reports, exit/status/stdout/working records, byte accounting
and finalization contract all agree. Citations and stored PASS labels
are not used in place of these complete comparisons.

**Fresh bounded lifecycle.** One clock covers setup/imports, capture,
source materialization, preflights, all four replays and final writing.
The work deadline is 174 seconds and the reserve is 131072 bytes inside
the 180-second/134217728-new-byte cap. Four zero-code child exits are
observed at elapsed seconds 34.83387229195796, 68.7344494999852,
103.04516087495722 and 137.09402349987067. The tool observes parent
exit zero. All 1326 captured inputs, complete tree sets and fresh sources
agree after terminal writing. Finalization records
137.40800962504 seconds and 3781802 bytes before its own write;
conservative inclusive bounds are 141 seconds and 3912059 new bytes,
strictly below 180 and 134217728. No failure, retry, resumption or cap
change occurs; the timer remains armed through final writing.

The separate fixed audit passes. This validates existing known-method
inputs, not a new BSD case or an improvement beyond the checked sources.
Fresh measurements do not repair the unverified exact historical
parent-exit timestamp or any earlier timing qualification, and Python
signal dispatch is not asserted to be a hard real-time guarantee.
Ninety-four kernels, signed assembly, exact-parameter transfer and strict
zero exclusion remain. No arbitrary-curve rank comparison, full Sha
finiteness or refined formula follows; there is no candidate resolution.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
Supporting integration/series results do not constitute a full matching
executable-certificate theorem. Production, independent replay and
the separate fixed critical audit pass. No formalization is claimed.
