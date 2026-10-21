# L093 — The entire scale-992 order W is not two-maximal

## Hypotheses

Use L067's audited entire degree-48 number field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive integer polynomial H=343h.
Use L077's nonmonic starting basis, L078's m-order, L080/L084's n-order,
L085/L086's s-order, L087/L088's u-order, L089/L090's v-order V,
audited L091's entire multiplier identification and audited L092's entire
order W and multiplication table. In particular
w_i=v_i for i<43 and w_i=v_i/2 for 43≤i<48, with [W:V]=32.
Retain both original point-coordinate components, actual identity,
all rational transports, leading coefficient 343 and the complete
31/62/124/248/496/992 scale chain. Complete fixed evidence through steps
355/357, their inventories/copies/sources, original divisions and original
six-system V and direct W solves are supplied inputs.

The prior SPECIALIZE scope is
`drafts/literature/2026-10-20-index-thirty-two-order-prime-two-test.md`.
All basis subscripts below are zero-based, as in the certificates.

## Conclusion

For this entire actual W,

\[
 I=\sqrt{2W}=2\mathbf Z w_0+\sum_{i=1}^{47}\mathbf Z w_i,
 \qquad
 (I:I)=\sum_{i<42}\mathbf Z w_i+
                 \sum_{42\le i<48}\mathbf Z(w_i/2).
\]

The full integral multiplier has index 64 over W; w_42/2 is a strict
integral multiplier witness. Thus W is not two-maximal. This is one fixed
known-method reproduction. Complete input replay, production and independent
replay pass in one combined execution, with conservative inclusive bounds
56 seconds <180 and 86332038 new staged bytes <134217728. All 7363
inventoried originals, 322 fixed copies and 17 source artifacts are
preserved through execution. Its separate fixed critical audit passes:
full replay and independent complete rank/kernel/global-preimage evidence
meet conservative inclusive bounds 62 seconds and 84707839 bytes,
preserving 8040 originals, 377 fixed copies and seventeen source artifacts.

No successor table or maximality of the multiplier, global maximality,
complete units/classes, full descent enclosure, rational membership or
arbitrary-curve complex-order/rank comparison follows.

## Proof

**Imported theory and applicability.** Import Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2), both
radical cases, Proposition 9.3 with proof and the following complete
action/kernel/lifting paragraph p.235](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
For an order A in a number field and prime p, iterated Frobenius on
A/pA with p^k>dim_Fp(A/pA) gives the complete radical preimage
I=√(pA). If N is the integral preimage of the kernel of the action of
A on all of I/pI, the source identifies (I:I)=N/p and supplies the
integrality and local stopping criterion. These results are imported
without reproof; the saved primary assessment covers both radical cases
and the full lifting rule, rather than only the proposition statement.

L067 gives the whole number field and audited L092 a full order W.
Finite freeness over Z makes two a nonunit. Since 2W⊂I, the ideal is a
nonzero full finite module, so the multiplier integrality theorem applies.
No monogenic integral generator, odd-prime hypothesis or selected field
factor is used. Six iterates suffice since 2^6=64>48. The source supplies
neither this instance's matrices nor its ranks, index or resource bounds.
Earlier V ranks are not transferred to W. The specialization is needed
to produce and independently check those concrete arithmetic inputs.

**Sole execution and complete provenance.** All fresh evidence below is in
`scripts/seven-torsion/W-two-359/`. The sole completed command is

```bash
python3 -B scripts/seven-torsion/W-two-359/run_once.py
```

It must not run again: exclusive writes and `run-start.json` prevent a
second execution. Only `run_once.py` and `stage.py` were prepared and
syntax-checked before the watchdog, without mathematical execution; their
bytes count. The watchdog starts before inventorying, copying, adaptation
or arithmetic and covers final rereads, preservation and writing. Fresh
`execution.py` adapts the inspected step-357 replay body; historical
stages/wrappers/producers never execute. Fresh verifier copies and adapted
modular sources run only in this directory.

The encompassing inventory includes all 6801 step-357 originals and every
step-357 artifact, the approved scope, histories and prepared attempt note:
7363 originals. All 322 step-357 copy-manifest entries bind both original
sources and fixed bytes, and all fourteen step-357 source hashes agree.
`post357-transition.json` records the exact old/current L092 and audit-note
hashes supplied by history 357 and the approved assessment. The note's
unique completed-execution boundary reconstructs its old hash. All other
step-357 original hashes agree. The exact step-355 append and earlier
history-353/355 transition chain are replayed, with no pathname exemptions.
The 272 step-355 copies/twelve sources and every inherited chain manifest
are checked as in the audited input. Hashes bind provenance; the full
identities below establish the mathematics independently of PASS labels.

**Entire input replay before modular production.** Byte-identical S/U/V/W
verifiers reconstruct the canonical b/m/n/s/u/v/w definitions. On each
whole table they check all 2304 products and 110592 integer slots, six
transports, eight inverse products, actual identity and all 96 two-sided
unit actions in original H. Both original point components remain present.
Exact Fraction reconstruction includes integer-zero entries. The integer
division fast path retains exact rational fallback.

All persisted dividends are reconstructed from their actual scaled basis
and complete table. Fixed evidence consists of 27648 step-349 identities
and 9216 each from steps 351, 353, 355 and 357, totaling 64512. Fresh
S/U/V/W input replay contributes 9216 further identities. Every identity
retains all 95 integer dividend, 47 rational quotient and 95 rational
remainder positions; shapes/types, every zero remainder and full equality
with H times the quotient are checked. Historical U and V action dividends
use their respective actual radicals and all entries of JA_i=L_iJ;
neither historical radical is used for the new W action.

The six original V systems from steps 349/351/353 and their complete
step-355 copy agree with the fresh full reconstruction. Every original
operation, pivot, swap sign, determinant, upper zero and original/transformed
residual is replayed. The separate direct W reconstruction starts from H,
the canonical nonmonic b formula, L078's two explicit denominator-31
columns and all successive final-column divisions, retaining all five W
half-columns. Its six full systems solve W's power inverse, V inclusion
and unit; V's inverse and unit; inverse inclusion; W's b coordinates;
their inverse; and W's full L067-coordinate inverse. Saved W inverse
matrices do not supply these solve inputs.

The fresh `W-exact-lattice-certificate.json` equals the entire original
step-357 certificate, and every original step-357 system is replayed with
all operations, pivots, determinants and both residual equations. All
transports, scale coefficients, actual units, index 32 and both integral
comparisons with the entire audited W agree. Both original/audited
multiplier decisions, both 53-generator numerator preimages and the
95-generator V-radical preimage are checked in both integer generation
directions. These checks finish before the new modular producer runs.

`audit-report.json` retains the inherited `index=32` for the input
W-over-V table; `W_multiplier_index=64` is the new result. Its inherited
`original_divisions=55296` counts fixed evidence only through step 355;
`fixed357_divisions=9216` records the additional full step-357 set.
`persisted-input-checks.json` likewise concerns input replay; the separate
new W action evidence is described next.

**Actual W and six Frobenius matrices.** `W_produce.py` and `W_verify.py`
are fresh specializations of the inspected step-351 known method. They
read W's actual `w-basis.json`, all `w-product-*.json` and its actual unit;
scale 992 replaces 496, input scale is 496 and the full prior-scale list
includes 496. The producer independently reconstructs every input product
by original-H reduction and triangular b-coordinate conversion, with
exact divisor 992²=984064. It verifies every integral coordinate and both
full inverse/point-coordinate transports. Input table index 32 is checked
as an input, not assumed to predict the new multiplier index.

The producer forms the first Frobenius from the entire binary table and
actual identity, then composes all six full matrices. Its binary int64
multiplications have at most 48²=2304 unit contributions, below 2^63.
The independent verifier uses exact Python integers and repeated squaring
of every basis vector. All six matrices, all 13824 entries and every
composition agree in `test-frobenius.json`.

Independent replay checks every reversible elimination operation, pivot,
pivot column, terminal zero row and free-variable equation. The terminal
rank is one, the only nonzero reduced row is e_0ᵗ and the full kernel is
span_F2(e_1,…,e_47). `test-radical-lattice.json` supplies all those lifts
and 2e_0,…,2e_47 as columns of G, a rank-48 integral basis J, rational
inverse and integer matrices C,D. Full replay checks

\[
 GC=J,\quad JD=G,\quad JJ^{-1}=J^{-1}J=1.
\]

The kernel-basis reduction is also fully replayed. Both integer generation
equations prove equality of the global preimage, not only equality of
mod-two dimensions. Here J=diag(2,1,…,1), giving the displayed I by the
imported radical theorem. No preceding radical shape is assumed.

**Full rank-48 radical action and numerator.** For each w_i, write L_i
for its multiplication operator in the independently validated W table.
The producer constructs an integral 48-by-48 A_i on the whole I-basis J.
Independent replay checks every one of the 110592 integer action slots
and all equations JA_i=L_iJ. This is the action on I/2I, a module of
rank 48, rather than the image of I in W/2W.

If P_i=992w_i in Q[t] and Z_j=Σ_l J_lj P_l, the independent verifier
also checks all 2304 full original-H identities

\[
 P_i Z_j-992\sum_k(JA_i)_{kj}P_k\equiv0\pmod H.
\]

Every actual dividend and its entire quotient/remainder is persisted in
`test-action-division-*.json`. The encompassing stage rereads all 2304,
reconstructs their dividends anew from W and J and checks the full
division equality again. No earlier action dividend is substituted.

The full 2304-by-48 binary action stack has row (j,k), column i equal to
(A_i)_kj modulo two. The independent verifier checks its entire saved
matrix, all reversible elimination operations, pivots 0,…,41, all terminal
zero rows and every free-variable equation. The rank is 42 and its full
kernel is span_F2(e_42,…,e_47). Across both full eliminations and both
kernel-basis reductions, all 1385 saved reversible row operations are
replayed.

`test-numerator-lattice.json` supplies every kernel lift and 2 times
every W-basis vector, a full basis Q, inverse and integer generation
matrices in both directions. The same two global generation and two
inverse equations are verified. Here
Q=diag(2,…,2,1,1,1,1,1,1) with 42 initial twos. Thus the imported
multiplier formula gives precisely N/2 and the displayed full multiplier.

**Index, identity and strictness.** `test-decision.json` supplies M=Q/2
and the integral old-order inclusion T=2Q⁻¹. Both MT=TM=1 products and
every upper-triangular zero are checked. Its diagonal is 42 ones followed
by six twos. The exact determinant 64 has orientation [(I:I):W] and
agrees with 2 to the full kernel dimension. The actual identity is
transported by T into the multiplier and by M back to W; no basis vector
is presumed to be the unit.

The saved numerator e_42 is outside 2W. The saved full integral matrix B
satisfies A_42=2B in all 2304 entries. Consequently w_42/2 preserves every
I-basis vector and lies outside W. Stevenhagen's finite-module criterion
makes it integral. The exact full multiplier index and this strict witness
prove nonmaximality; a nonzero radical alone would not prove it. There is
no new table or further test of this multiplier.

**Rereads, preservation and bounds.** The producer and independent
verifier both pass, with empty failures and matching computed decision,
index, Frobenius/action ranks and dimensions. All final input tables,
reports, copy/source inventories and preservation records are reread.
`preservation-audit.json` binds before/after hashes for all 7363 originals,
322 copies and seventeen source artifacts, including prepared and
extracted sources; all agree through final preservation. Complete modular
certificates are reread by the independent verifier and new action
divisions by the encompassing stage.

`watchdog.json` and `final-bound.json` pass. External execution through
final writing takes 54.38746220781468 seconds and 86328064 staged bytes.
Conservative inclusive bounds are 56 seconds and 86332038 bytes, checked
after final writing and strictly below 180 and 134217728. No failure,
correction, retry, resumption, malformed fixture, successor table, second
test or other prime occurred. The subsequent attempt-note completion
append is recorded separately in history 359; executed mathematical bytes
stay fixed. This establishes only the fixed local order-arithmetic result
stated above; the independent global arithmetic and BSD gaps remain open.

**Separate fixed critical audit (step 361).** The prior SPECIALIZE
assessment `drafts/literature/2026-10-20-W-two-critical-audit.md`
approves this distinct replay-only target. The sole completed invocation
is `python3 -B scripts/seven-torsion/W-two-audit-361/run_once.py`.
It must not run again. All evidence in this paragraph and the following
audit paragraphs is in that fresh directory. No producer, historical
wrapper, new multiplier test or successor table executes. The cited
source hypotheses, formula and interpretation above are unchanged.

The watchdog begins before inventories, copying, source adaptation and
arithmetic; prepared harness bytes count. The inventory includes every
one of the 7363 step-359 originals, every step-359 artifact, this canonical
statement, approved assessment, histories and prepared audit note: 8040
originals in total. Every one of the 322 step-359 fixed-copy bindings and
seventeen source hashes is checked. The unique step-359 attempt-note
completion append is bound to its actual old inventory hash and current
history-359 hash, as specified in the prior assessment. All other originals
agree. The exact earlier transitions through 353/355/357 are retained;
there is no pathname exemption. All 322 fixed copies also agree with the
fresh replay's bytes. Adding the complete fixed W modular certificates
and verifier gives 377 copied artifacts in
`audit-complete-copy-manifest.json`; the earlier input-only
`complete-copy-manifest.json` retains its separate 322-entry scope.

Fresh byte-identical S/U/V/W verifiers check all 2304 products and
110592 integer slots of each entire table, all transports and inverses,
both original point components, scales 31/62/124/248/496/992, original
leading coefficient 343, and the actual units' two-sided actions.
All 64512 fixed input divisions through step 357 and 9216 step-359 input
divisions are checked against reconstructed actual dividends. The entire
2304 original step-359 W action divisions are also checked. Fresh replay
adds 9216 input and 2304 action divisions, each persisted and reread.
Every identity retains all 95 dividend, 47 rational quotient and 95
zero-remainder positions and full equality with H times the quotient.
Historical U/V actions use their own radicals, separately from W.

Six V and six direct W systems are reconstructed from their canonical
definitions, without supplying stored W inverses as solve inputs.
All original V system certificates from 349/351/353/355/357/359 and direct
W system certificates from 357/359 agree completely with the fresh
certificates. Every original operation, pivot, swap sign, determinant,
upper zero, transformed right side and original/transformed residual is
replayed. The whole W/V lattice, both global input preimages, actual
units and index 32 agree. `W-exact-lattice-certificate.json`,
`W-solve-report.json` and `persisted-input-checks.json` record this input
validation; input index 32 is distinct from multiplier index 64.

The copied `W_verify.py` then replays all six Frobenius matrices on
the validated entire W table, every elimination operation, complete
free-variable kernel, both global preimages and all 110592 integral action
entries on the full rank-48 I/2I. All 1385 original row operations pass.
The entire original-H action replay and subsequent actual-dividend
reread pass. The original and fresh complete W modular certificates
agree. No production output or PASS label substitutes for these checks.

The separate `independent.py` imports no producer or verifier helpers.
It specializes the previously assessed step-353 full-rank/lattice
mechanism to W, using the validated W table and fixed `test-` certificates.
All values 992, ranks one/42, six terminal kernel directions, index 64
and column 42 are tested, not inferred from V.
It reconstructs terminal Frobenius from table diagonals and five further
binary compositions, and independently forms every exact integral action
J⁻¹L_iJ and the full row-(j,k), column-i stack. For each entire matrix A,
`frobenius-full-rank.json` or `action-full-rank.json` persists and rereads
binary matrices C,B,L with A=CB and LC=1. Full binary shapes and entries
are checked, as are both products, the full kernel matrix K with AK=0,
its left inverse and rank plus kernel dimension 48. These equations
prove both rank inequalities and completeness. Both span comparisons
with the original full kernels pass; a selected minor alone is not used.
The action factorization checks all 110592 entries, its left inverse
has 96768 entries, and the selected square inverse has 1764 entries.

`radical-independent-preimage.json` and
`numerator-independent-preimage.json` persist all kernel lifts together
with all 2W generators. For each full global preimage, integer matrices
give both generator-to-basis and basis-to-generator equations; both full
inverse products and both integral comparisons with the original and
displayed lattices are checked and reread. They recover
J=diag(2,1,…,1) and Q=diag(2,…,2,1,1,1,1,1,1), with 42 initial twos.
Thus the independently verified kernels and global preimages are precisely
those used in the imported radical and multiplier formulas.

`independent-multiplier.json` persists Q/2, its integral old-order
inclusion T, both inverse products, the actual unit and the strict witness.
Every entry of T is checked against diag(1,…,1,2,2,2,2,2,2); hence all
off-diagonal zeros are checked and |det T|=64 has orientation
[(I:I):W]. The entire actual identity transport passes. The numerator
e_42 is outside 2W, and every one of the 2304 entries of A_42/2 is
integral and agrees with the original witness. All these persisted
equations are reread, proving the claimed strictness and full multiplier
identity independently of the saved elimination operations.

`audit-report.json`, `independent-report.json`,
`test-verification-report.json`, `preservation-audit.json`,
`watchdog.json` and `final-bound.json` pass with no failures.
All 8040 original hashes, 377 copied-artifact hashes and seventeen
prepared/generated source hashes agree through final preservation;
the complete inventories and reports are reread.
External execution through final writing takes 60.435195416910574 seconds
and writes 84703865 bytes. Conservative inclusive bounds 62 seconds and
84707839 bytes are checked after the final write and are strictly below
180 and 134217728. There is no failure, correction, retry, resumption or
malformed-evidence fixture. The later canonical audit addition and
attempt-note completion append are exact documentation transitions
recorded in history 361; executed sources and certificates remain fixed.
This validates the existing fixed known-method input only; none of the
independent global-arithmetic or BSD gaps in the conclusion is removed.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit entire
W multiplier test and its certificates has not been checked. Unknown
availability is not evidence of absence. The cited known theory,
audited input hypotheses and complete exact replay supply the evidence.
The separate fixed critical audit above passes; no additional Mathlib
availability claim is made.
