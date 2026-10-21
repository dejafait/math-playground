# L091 — The entire scale-496 order V is not two-maximal

## Hypotheses

Use L067's audited entire degree-48 number field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive H=343h. Use L077's original
nonmonic b-basis, L078's m-order, L080/L084's n-order,
L085/L086's s-order, L087/L088's u-order U, L089's audited
multiplier identification and L090's audited complete table of

\[
V=\sum_{i<44}\mathbf Z u_i+\sum_{44\le i<48}\mathbf Z(u_i/2).
\]

Write v_i=u_i for i<44 and v_i=u_i/2 otherwise. Retain both
original point-coordinate components, every rational transport, the
actual identity and the complete scale chain 31/62/124/248/496.
Fixed steps 329/331/333/335/337/339/341/343/345/347 and all step-349
certificates, inventories, source hashes and six exact solves are inputs.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-19-index-sixteen-order-prime-two-test.md`.

## Conclusion

For the entire actual V, the complete radical and multiplier are

\[
I=\sqrt{2V}=2\mathbf Z v_0+\sum_{i=1}^{47}\mathbf Z v_i,
\qquad
(I:I)=\sum_{i<43}\mathbf Z v_i+
                  \sum_{43\le i<48}\mathbf Z(v_i/2).
\]

The multiplier has index 32 over V. In particular V is not
two-maximal. This is a fixed specialization of a known construction.
Complete input, production and independent replay pass in one combined
execution, with conservative inclusive bounds 27 seconds <180 and
125666372 new staged bytes <134217728. All 4817 inventoried originals,
643 fixed copies and eight source files are preserved through execution.

The separate fixed critical audit passes, with independent full-rank and
global-lattice certificates and inclusive bounds 34 seconds and 60802066
new bytes, strictly below 180 and 134217728. No table or
maximality verdict for the multiplier, further correction, global
maximality, complete units/classes, full descent enclosure, rational
membership or arbitrary-curve complex-order/rank comparison follows.

## Proof

**Imported method and applicability.** Import Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2), both
radical cases, Proposition 9.3 and the following action/kernel/lifting
paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
For an order A in a number field and nonunit prime p, iterated
Frobenius on A/pA with p^k>dim_Fp(A/pA) gives the complete radical
preimage J=√(pA). If N is the integral kernel preimage for A acting
on all of J/pJ, the source identifies (J:J)=N/p and supplies the
integrality and local stopping/strictness criterion. Both the zero
and nonzero radical cases are retained. These named results are
imported without reproof, monogenicity or an odd-prime restriction.

L067 and audited L090 give the entire number field and a full order V.
Finite freeness over Z makes two a nonunit. The ideal I contains 2V,
so is a nonzero full finite Z-module to which the multiplier integrality
criterion applies. Six iterates suffice because 2^6=64>48. The source
does not supply this instance's matrices, ranks, exact index or bounded
execution. U's earlier ranks do not transfer to V.

**Complete fixed inputs before modular production.** All fresh evidence
below is in `scripts/seven-torsion/index-sixteen-order-two-351/`.
`input_verify.py`, `verify_u.py` and `verify_v.py` are byte-identical
copies of the step-349 replay verifiers. They reconstruct the canonical
b/m/n/s/u/v chain, both original point-coordinate transports, all six
transports for each S/U/V table, eight inverse products per table,
the actual units and 96 left/right identity actions per table.
Every one of the 2304 products and 110592 integer entries per table,
including zeros, passes full polynomial division in original H.
Fraction reconstruction handles untouched integer zeros explicitly.
The division's checked integer fast path retains rational fallback;
observed zero fallback is not a hypothesis.

All 49 S files agree across steps 329/331/333/335/337/339/341,
all 49 U files agree across 339/341/343/345, and all 49 V files
agree across 347/349. Every entry of the 248/447/449/643-entry
step-343/345/347/349 copy manifests is checked against both source
and fixed bytes. All six step-347 and seven step-349 recorded source
artifacts retain their hashes. Hashes bind provenance; the complete
polynomial and lattice identities independently establish the arithmetic.
Historical U actions and radical/numerator/decision files are copied
under `old-U-` names, preserving them separately from new V outputs.

The entire original/audited L089 decision, both numerator certificates,
independent multiplier and two-sided global preimage are compared.
With M=diag(1,…,1,1/2,1/2,1/2,1/2), T=M⁻¹ and Q=2M,
all entries, both inverse products, both integer generation equations
for the complete numerator lattice and both integral lattice comparisons
agree. The actual units agree in both directions. The determinant is
16, with orientation [V:U]; the V verifier's historical
`exact_index_eight_orientation` label does not change its actual checked
value. The extracted lattice-interface report's inherited
`all_inputs_before_production` label concerns that interface only;
`complete-input-validation.json` is written after every input obligation
below and before this execution's modular production.

All six original step-343 division sets retained under `original343-`
are replayed: 13824 identities. Step 347's S/U/V divisions add 6912,
and all 6912 fresh divisions persisted by step 349 are read in place,
giving all 27648 original step-349 identities. The latter files remain
inventoried originals, rather than being replaced by newly generated
evidence. Current S/U/V replay supplies another 6912 identities.
Every persisted dividend is reconstructed from its actual scaled basis
and full table. For historical action divisions, the full U radical
basis and every coordinate equation JA_i=L_iJ are used. Each certificate
retains 95 integer dividend positions, 47 rational quotient positions
and 95 rational zero-remainder positions. Exact shapes/types, all
positions and dividend=H·quotient+remainder are checked.

**All six exact step-349 solves.** A fresh `independent.py`, adapted
from the fully inspected step-349 independent reconstruction, rebuilds
the canonical basis matrices without using saved inverses to solve.
It solves the same six full systems for V's power inverse, U inclusion
and unit, U's inverse and unit, the inverse inclusion, b coordinates,
their inverse and both original-coordinate transports. Every swap,
elimination factor, pivot, transformed right side, solution entry and
determinant is persisted and replayed. All upper-triangular zeros,
nonzero pivots and both original/transformed residual equations pass.
All six V transports, both integral comparisons with the whole audited
V, index sixteen, both units and all 11520 scale-31/62/124/248/496
coefficients agree. The full fresh exact certificate equals the original
step-349 certificate, and all six original systems' row operations and
residuals are replayed again. Thus no selected minor, dimension or
stored PASS label substitutes for the original solve evidence.

**Actual V producer and independent Frobenius.** Inside the watchdog,
guarded source adaptations create a fresh producer and independent
kernel verifier from the inspected step-343 method. The producer reads
V's actual scale-496 basis/table and unit. It reconstructs the original
b and L067 transports, all inverse equations and every input product by
polynomial reduction and triangular conversion with exact divisor
496²=246016. The scale chain and L090 index sixteen are checked anew.
This differs from the input verifier's polynomial-zero method.

The producer uses the entire binary table and the actual unit to form
the first Frobenius matrix, then composes all six full iterates.
Its int64 operands are binary, with at most 48²=2304 unit contributions
per multiplication, strictly below 2^63. The independent verifier uses
exact Python integers and repeated squaring of all basis vectors.
All six matrices, all 13824 entries and every composition agree.

For the terminal matrix, independent replay checks every reversible
row operation, every pivot/leading one, all pivot-column entries,
all terminal zero rows and every free-variable equation. Its rank is
one; its only nonzero reduced row is e_0ᵗ and its full kernel is
span_F2(e_1,…,e_47). This is computed for V, not inherited from U.

`radical-lattice.json` records all reduced kernel lifts together with
2e_0,…,2e_47 as a generator matrix G, a rank-48 basis J,
its rational inverse and integer matrices C,D. Complete replay checks

\[
GC=J,\qquad JD=G,\qquad JJ^{-1}=J^{-1}J=1.
\]

The kernel-basis reduction is also fully replayed. These two integer
generation equations prove equality of the global preimage, not merely
containment or equality modulo two. Here J=diag(2,1,…,1), giving the
displayed entire radical by the imported criterion. The implementation
does not require this kernel shape or exclude empty kernels.

**Every action on the full I/2I.** For each v_i let L_i denote
multiplication in V's verified table. The producer constructs a full
integer matrix A_i on the rank-48 I-basis J. Independent replay checks
every one of the 110592 integer action slots and all equations

\[
JA_i=L_iJ.
\]

Put W_i=496v_i and Z_j=Σ_l J_lj W_l in Q[t]. For all 2304 pairs
the independent verifier additionally checks the entire original-H
identity

\[
W_i Z_j-496\sum_k(JA_i)_{kj}W_k\equiv0\pmod H.
\]

Every action dividend, quotient and full zero remainder is persisted.
The stage rereads all 2304 certificates, reconstructs the actual
dividend from V and J, checks all coordinate entries and checks the
complete division identity again. The module is all of I/2I, of
rank 48; its image in V/2V is not substituted.

The action stack has 2304 rows indexed by (j,k), with column i equal
to (A_i)_kj modulo two. Independent elimination replay checks this
entire matrix, reversible operations, pivots, terminal zero rows and
all free-variable equations. The rank is 43, the pivots are 0,…,42
and the complete kernel is span_F2(e_43,…,e_47). Across the two full
eliminations and two kernel-basis reductions, 1452 reversible row
operations are replayed.

`numerator-lattice.json` supplies the same complete two-sided integer
generation and inverse certificates for this kernel's global preimage
N. They give Q=diag(2,…,2,1,1,1,1,1), with 43 initial twos.
Hence Stevenhagen's theorem identifies the entire multiplier with
N/2, whose basis Q/2 gives the claimed five half-basis columns.

**Index, identity and strictness.** `decision.json` gives the complete
multiplier matrix M=Q/2 and integral old-order inclusion T=2Q⁻¹.
Both MT=TM=1 products and every required triangular zero are checked.
T has 43 initial diagonal ones and five final twos, so
|det T|=32=[(I:I):V], agreeing with 2 to the complete kernel dimension.
The actual unit is transported by T and then by M back to its V
coordinates; no basis vector is presumed to be the unit.

The saved numerator e_43 is outside 2V. Its full integral radical
action B satisfies A_43=2B in all 2304 entries. Therefore v_43/2
preserves all of I and lies outside V. The imported finite-module
integrality criterion makes it an algebraic integer. This is a strict
integral multiplier overorder, proving V is not two-maximal. The radical
alone, table closure alone or an earlier U rank would not prove this.

**Single execution, exact transitions and preservation.** The sole
invocation is

```bash
python3 -B scripts/seven-torsion/index-sixteen-order-two-351/run_once.py
```

Only `run_once.py` and `stage.py` are prepared and syntax-checked before
the external watchdog, without mathematical execution; their bytes
count. The watchdog precedes inventories, copies, helper extraction,
source adaptation, all mathematics, persisted-certificate rereads,
preservation and final evidence writing. Exclusive writes and the start
marker forbid rerun. No historical stage, producer or one-shot wrapper
executes. Full input validation precedes this single new modular test.

Every one of the 4001 step-349 inventoried inputs and every step-349
artifact is retained, together with the prior provenance chains:
4817 originals in total. The exact two post-349 documentation hash
transitions for L090 and its audit-attempt note are checked against
both the original inventory hashes and the current hashes recorded in
the approved assessment. The step-347 attempt-note prefix is reconstructed
and hashed at its unique completed-execution marker. The earlier
L087/L088/L089 transitions are checked against their actual historical
inventories and current bytes. Every other historical hash agrees;
there is no pathname exemption. `inventory-transition.json` retains
the exact values and complete prior transition records.

At final preservation all 4817 originals, 643 fixed copies and eight
source files have unchanged before/after hashes. Full input, producer,
verifier, stage, table, manifest, inventory and preservation records
are reread. All reports pass with empty failures. The external execution
through final evidence writing takes 26.004252834012732 seconds and
125662399 bytes. Conservative inclusive bounds 27 seconds and
125666372 bytes, checked after the final write, are strictly below
180 seconds and 134217728 bytes. No failure, retry, correction,
malformed fixture, successor table, second test or other prime occurs.
The pre-execution attempt note is extended afterwards only by the
separately recorded documentation append.

This supplies one local order-arithmetic input by known-method
reproduction. The independent global arithmetic and BSD gaps in the
conclusion remain unresolved.

**Separate critical audit (step 353, 2026-10-20).** The unchanged prior
SPECIALIZE scope is
`drafts/literature/2026-10-19-index-sixteen-order-two-critical-audit.md`.
The source hypotheses above still apply to the entire V, including
both original point components, leading coefficient 343 and all scales.
No new theorem is claimed and no general source theorem is reproved.
The single replay-only invocation is

```bash
python3 -B scripts/seven-torsion/V-two-audit-353/run_once.py
```

This command has already run and its exclusive start marker forbids a
second execution. All evidence below is in that fresh directory. No
producer or historical stage executes. `audit.py` reads inspected
definitions and the full fixed input-comparison block, writes their
prepared source and runs fresh verifier copies. The old U action data
remain under `old-U-` names; the V action data are distinct.

Before preparation, `canonical-input-hashes.json` inventories all 5745
originals, including the complete 4817-input step-351 inventory and all
step-351 artifacts. Every original copy-manifest entry and executed
source hash from steps 343/345/347/349/351 is bound to actual bytes.
The exact step-351 attempt-note append, both post-349 document transitions
and all retained prior transitions are checked against their historical
inventories; no pathname is exempted. `inventory-transition.json` records
these exact cases. The 432 large retained division files are read in
place with full checks and before/after hashes, avoiding unnecessary
copies without changing their mathematical meaning.

Fresh complete S/U/V replay verifies all 2304 products and 110592 integer
slots per table, the six transports and eight inverse products per table,
both unit actions, and the whole audited V/U index-sixteen interface.
`solve_replay.py` independently reconstructs all six systems and checks
the full exact certificate against both steps 349 and 351. It replays
all six original systems in each, including every operation, upper zero,
pivot, determinant, transformed right side and both residual equations.
`exact-lattice-certificate.json` retains this complete reconstruction.

`persisted-input-checks.json` records 27648 original step-349 divisions
and 9216 step-351 divisions (S/U/V and V actions), plus 9216 fresh
divisions. For every identity the actual dividend is reconstructed from
the validated corresponding basis/table and, for actions, its actual
radical. All 95 dividend, 47 rational quotient and 95 zero-remainder
positions and the whole H-times-quotient equality are checked. Historical
U actions use U's radical; V actions use V's radical. Rational division
fallback and exact integer-zero handling are retained.

`verification-report.json` follows complete replay of all six V Frobenius
matrices and their compositions, all 1452 saved reversible row operations,
both full kernels and both two-sided integral preimages, all 110592
action slots on the rank-48 module I/2I, and every original-H action
identity. The independently reconstructed full stack uses row (j,k),
column i equal to (A_i)_kj modulo two. The entire input-basis certificate
is compared with validated V. The original index, identity, strict witness
and all multiplier inverse equations pass.

The separate `independent.py` imports no producer/verifier helpers and
does not use their elimination operations. From the complete table it
reconstructs terminal Frobenius and every integral action by J inverse,
then constructs the entire action stack. For each full binary matrix M,
`frobenius-full-rank.json` or `action-full-rank.json` persists matrices
C,B,L with M=C B and L C=1. Their sizes are respectively
48-by-48 with r=1 and 2304-by-48 with r=43; C has r columns,
B has r rows, and L is r-by-height. All shapes, binary entries and full
products are reread and checked. The factorization gives rank at most r,
the left inverse gives rank at least r, and B is the first r rows of
the identity. The persisted K consists of the last 48-r identity
columns; every M K=0 equation and a left inverse of K are verified.
Thus these are complete kernels, not selected-minor lower bounds.
Both span containments with the original saved kernels are checked.

For each kernel, the independent preimage certificate uses all its lifts
together with 2 times every standard basis vector as a generator matrix
G. It verifies integer matrices U,W with G U=J and J W=G, both inverse
products of J, and both integral comparisons with the saved lattice.
The reread bases are exactly diag(2,1,...,1) for the radical and
diag(2,...,2,1,1,1,1,1), with 43 twos, for the numerator. Their
complete certificates are `radical-independent-preimage.json` and
`numerator-independent-preimage.json`.

`independent-multiplier.json` then verifies the whole numerator divided
by two, the integral old-order inclusion, both inverse products and
the actual identity. Every entry of the inclusion is checked to equal
diag(1,...,1,2,2,2,2,2); its determinant 32 has orientation
[(I:I):V]. The full 2304-entry action of v_43/2 is integral and twice
it is A_43, while its coordinate 1/2 proves nonmembership in V.
This independently validates strictness using the cited integrality
criterion, without constructing a successor table or asserting maximality.
All independent certificates are persisted, reread and fully checked.

`audit-report.json` and `independent-report.json` have PASS and empty
failures. `audit-preservation.json` verifies all 5745 originals,
266 fixed copies and nine prepared/executed source files unchanged
through final preservation. Complete inventories and reports are reread.
The external watchdog includes setup, all preparation and mathematics,
preservation and final writing: actual execution was
32.465139917097986 seconds and 60798092 new bytes. `final-bound.json`
records conservative inclusive bounds 34 seconds and 60802066 bytes,
strictly below 180 seconds and 134217728 bytes, checked after writing.
There was no failure, retry, correction or iteration. Later additions
to this lemma and the attempt note are documented separately as
post-execution documentation changes; original certificates stay fixed.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit complete
V multiplier test and its certificates has not been checked. Unknown
availability is not evidence of absence. The cited known theory,
audited input hypotheses and complete exact replay supply the evidence.
