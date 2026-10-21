# L094 — Complete table of the index-64 multiplier order

## Hypotheses

Use L067's audited entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive integer H=343h. Retain L077's
nonmonic b-basis, L078's m-order, L080/L084's n-order, L085/L086's
s-order, L087/L088's u-order, L089/L090's v-order, L091/L092's
w-order W and audited L093's entire multiplier identification:

\[
I=\sqrt{2W},\qquad Z=(I:I)
=\sum_{i<42}\mathbf Z w_i+\sum_{42\leq i<48}\mathbf Z(w_i/2),
\qquad[Z:W]=64.
\]

All subscripts are zero-based. Both original point-coordinate components,
the actual unit, every rational transport and scales
31/62/124/248/496/992 are retained. Complete fixed evidence through
355/357/359/361, including original V/direct-W solves and both audited
global preimages, is supplied. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-index-sixty-four-multiplier-table.md`.

## Conclusion

Set z_i=w_i for i<42 and z_i=w_i/2 for 42≤i<48. The files
`z-basis.json` and `z-product-00.json` through `z-product-47.json` in
`scripts/seven-torsion/index-sixty-four-table-363/` give the entire table

\[
z_i z_j=\sum_{k=0}^{47}e_{ijk}z_k,\qquad e_{ijk}\in\mathbf Z
\quad(0\leq i,j<48).
\]

Independent original-H replay checks all 2304 products/110592 integer
slots, six transports, eight inverse products, actual unit with all
96 two-sided actions and agreement with the entire audited multiplier.
The common power-coordinate denominator is 1984, reconstructed from
every rational map entry; every scaled coefficient and persisted actual
dividend is checked. One combined execution meets conservative inclusive
bounds 73 seconds <180 and 96522288 new bytes <134217728, preserving
8721 originals, 383 fixed copies and twenty source artifacts.

Its separate fixed critical audit passes, including six independent
direct Z systems and complete fixed/fresh replay within inclusive bounds
82 seconds and 101327514 bytes. This is fixed known-method reproduction.
It supplies no new multiplier test, local/global maximality,
complete units/classes, descent enclosure, rational membership or
arbitrary-curve rank/order comparison.

## Proof

**Imported identification and applicability.** Import audited L093's
whole multiplier, without recomputing a radical or producing a new
multiplier verdict. The general input is Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2), both radical
cases, Proposition 9.3 with proof and the full action/kernel/lifting
paragraph p.235](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
L067 supplies a number field and audited L092 the full order W, finite
free over Z. Two is a nonunit, and I contains 2W, so I is a nonzero
full finite module. The multiplier integrality theorem applies without
odd-prime or monogenic-integral-generator hypotheses. Thus L093's entire
identified multiplier is an order. The named theorem is imported without
reproof; it supplies neither the instance's new products nor a resource
bound. Those are the necessary specialization below, not a new general
result.

**Single execution and preservation scope.** The sole completed command is

```bash
python3 -B scripts/seven-torsion/index-sixty-four-table-363/run_once.py
```

It must not run again. Exclusive writes and `run-start.json` prevent a
second execution. All following fresh artifacts are in that directory.
Only `run_once.py` and `stage.py` were prepared and syntax-checked before
the watchdog, without mathematical execution, and their bytes count.
The watchdog begins before inventories, copying, source adaptation or
arithmetic and includes final rereads, preservation and writing.
`execution.py` adapts the inspected input portion of the step-361 audit;
no historical wrapper, stage or producer executes. Its fixed-evidence
replay does not produce a radical, discover a rank/kernel or run a new
multiplier test. The only producer is the new table transport below.

`audit-input-hashes.json` includes all 8040 original step-361 inputs,
every step-361 artifact, its complete earlier chain, approved assessment,
histories 361/362 and the prepared attempt note: 8721 originals.
All 377 step-361 copy bindings are checked against both source and fixed
bytes; all seventeen recorded source hashes agree. Exact post-361
transitions for L093 and its audit note bind old inventory hashes to
current bytes and history 361, SHA256
`5f01bba525a8e7b0aa262c51ef00565ce2637fce631c6e45431c77f682da01f2`.
The note has one completion marker and its prefix has the old hash.
All other step-361 originals agree. `post361-transition.json` records
these equalities. The exact earlier transitions through 353/355/357/359,
complete copy manifests and executed-source hashes are also checked;
there is no pathname exemption or blanket documentation bypass.

**Complete input arithmetic.** Fresh byte-identical S/U/V/W verifiers
reconstruct the full canonical chain, both original point components,
all six transports/eight inverse products and every actual unit action.
Each table has 2304 original-H products and 110592 integer slots.
Exact Fraction reconstruction includes untouched integer zeros and
retains rational fallback in polynomial division. Leading coefficient
343 and every original scale remain explicit.

Fixed input division replay checks 64512 identities through step 357,
9216 step-359 input identities and 9216 step-361 input identities:
82944 in total. The two fixed W-action sets add 4608 identities.
Fresh S/U/V/W replay adds 9216 persisted identities, and fresh fixed-W
action replay adds 2304. Each identity retains all 95 integer dividend,
47 exact rational quotient and 95 zero-remainder positions. Shapes and
types are checked; each dividend is reconstructed from its actual full
basis/table and verified equal to H times the quotient plus remainder.
For action identities, all coordinates of JA_i=L_iJ are checked first.
Historical U and V actions retain their respective original radicals;
only W actions use W's radical. These are full identities, not samples
or transfers of historical ranks.

All six original V systems from 349/351/353 and their later complete
copies through 355/357/359/361 are matched and replayed. The direct W
reconstruction begins with H, the canonical nonmonic b formula, both
L078 denominator-31 columns and every successive half-column, retaining
all five W half-columns. Its six systems reconstruct W's inverse,
V inclusion and unit; V's inverse and unit; inverse inclusion; W's b
coordinates; their inverse; and full L067-coordinate inverse. Saved W
inverse matrices do not supply these solve inputs. The full certificates
from 357/359/361 agree and every original operation, pivot, swap sign,
determinant, terminal zero and original/transformed residual is replayed.
`W-exact-lattice-certificate.json`, `W-solve-report.json` and the complete
input reports retain this evidence.

**Fixed complete kernels, preimages and changed interface.** The fresh
fixed `W_verify.py` replays all saved original eliminations and both
global integral preimages, with full actions and actual dividends.
It discovers no new multiplier. The separate fixed-factorization check
in `execution.py` uses only binary-product definitions from
`fixed_independent.py`, with no rank search or inverse construction.
For every full saved matrix A, it checks all binary entries/shapes and
the step-361 equations A=CB and LC=1, the entire kernel equation AK=0,
its left inverse PK=1, rank plus kernel dimension 48 and equality with
the original complete kernel. Both selected square inverse products are
also checked. The terminal Frobenius is independently reconstructed from
the validated table diagonals and five compositions; every saved iterate
agrees. All 110592 action entries and the entire 2304-by-48 stack are
bound to the actual W table and its full rank-48 radical. The complete
saved ranks one/42 and kernels are input evidence, not a new verdict.

For each independently certified global preimage, all kernel lifts and
every 2W generator are retained. Integer matrices give both GC=L and
LD=G; both rational inverse products and both integral comparisons with
the original saved lattice are checked. The whole radical preimage
agrees with the basis used for every action dividend.

`new-successor-interface-body.txt` separately compares every entry of the
original step-359 decision/numerator, their complete step-361 fixed
counterparts and the step-361 independent multiplier/numerator preimage.
Put a_i=1 for i<42 and a_i=2 otherwise, M=diag(1/a_i), T=diag(a_i),
Q=2M. All decisions, numerator matrices, both MT=TM=1 products,
determinant/index 64, actual identity and orientation [Z:W] agree.
The numerator's 54 generators are e_42,…,e_47,2e_0,…,2e_47.
Both original and independent certificates give this entire preimage
in both integer generation directions, with 48-by-54, 54-by-48 and
48-by-54 shapes, both full inverses and both integral containments.
The full strict-action matrix of w_42/2 agrees in all 2304 entries.
The older five-column V-to-W interface is preserved separately; it is
not substituted for this six-column interface.
`new-successor-input-validation.json` records completion before products.

**Full table construction and independent check.** If c_ijk is the
validated W table, `produce_z.py` constructs

\[
e_{ijk}=\frac{c_{ijk}a_k}{a_i a_j}.
\]

This is the unique expansion because z_i=w_i/a_i. Exact division is
checked at every slot, including zeros. For each forward coordinate
matrix A the new map is AM, and for its inverse B the new inverse is TB.
All six transports to/from b, power and L067 coordinates are produced;
the actual unit is transported by T.

`verify_z.py` imports no producer arithmetic. It checks every transported
entry, both inverse products in each of the three systems, both
multiplier/inclusion inverse products and all old-order containment
equations: 18432 transport/inclusion entries and eight inverse products.
All entries of the full diagonal T are checked; its determinant is
the product of 42 ones and six twos, namely 64 with orientation [Z:W].
The integral actual unit agrees with both audited interfaces, represents
the constant polynomial one in original H and passes all 96 actions.
The original point-coordinate components remain present in full.

Let P be the actual rational power map. The lcm of the denominators of
all 2304 entries is checked to equal 1984. Each Q_j=1984P_j is reconstructed
with exact Fraction arithmetic, checked integral and compared with the
entire saved array and the transported W array. Thus Q_j=1984z_j, and
the scale chain is 31/62/124/248/496/992/1984, retaining H's leading 343.

For every ordered pair, independently convolve in Q[t] to form

\[
D_{ij}=Q_iQ_j-1984\sum_k e_{ijk}Q_k.
\]

Complete division by original H gives zero remainder. No producer
reduction or transported-product assertion supplies this check. All
2304 products, 110592 integer slots and 218880 remainder positions
pass. Each full 95-position dividend, 47-position rational quotient and
95-position zero remainder is saved in `z-division-00.json` through
`z-division-47.json`. Every persisted entry is reread, D_ij is reconstructed
again from the actual basis/table and D_ij=H·quotient+remainder is checked
in every position. Observed rational-fallback count zero is not assumed.
Since P is invertible, these field identities prove the entire table;
ring closure is not inferred merely from a dimension or index.
`z-verification-report.json` and `table-persisted-input-checks.json`
have PASS and empty failures.

**Final preservation and bounds.** Every whole table and report is reread.
`preservation-table.json` gives unchanged before/after hashes for all
8721 originals, 383 fixed copies and twenty prepared/generated sources.
All inventories, manifests, source hashes and preservation records are
reread before acceptance. `stage-report.json`, `watchdog.json` and
`final-bound.json` pass without failures. Actual external execution
through final writing takes 71.13548762490973 seconds and writes
96518314 bytes. The conservative inclusive bounds are 73 seconds and
96522288 bytes, checked after final writing and strictly below
180 and 134217728. There is no failure, correction, retry, resumption,
new radical/multiplier test or iteration. The later completion append
to the attempt note is an exact transition recorded in history 363;
all executed sources and certificates stay fixed.

This supplies an explicit table of the already identified multiplier
only. Global maximality, complete units/classes and all later
descent/rational-rank gaps remain open.

**Separate critical audit (step 365).** The sole completed fresh command is

```bash
python3 -B scripts/seven-torsion/Z-table-audit-365/run_once.py
```

It must not run again. All audit artifacts below are in that directory.
The prior unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-20-index-sixty-four-table-critical-audit.md`.
The watchdog begins before source adaptation, inventories, copies or
arithmetic and includes final preservation and writing; the two prepared
source files count toward its byte bound. `stage.py` reads step 363's
execution source only up to the unique boundary before successor source
adaptation. No producer, historical wrapper/stage or new multiplier test
executes. Fixed W radical/action arithmetic is replayed as input evidence;
no radical or multiplier of Z is computed.

`Z_reconstruct.py` starts with the original 49 coefficients of H and
checks them against L067's whole primitive polynomial and h=H/343.
It reconstructs every b_i by L077's formula, both explicit denominator-31
columns of L078, and successive half-column ranges 47, 46–47, 45–47,
44–47, 43–47, 42–47. Write P_Z and P_W for the resulting power-coordinate
matrices. No saved inverse or producer helper supplies a solve input.
Six complete exact systems solve:

1. P_Z X=[1_48 | P_W | e_0], giving P_Z inverse, W inclusion and the unit.
2. P_W X=[1_48 | e_0], giving W inverse and its unit independently.
3. T X=1_48 for the solved W inclusion T, giving the inverse inclusion.
4. P_b X=P_Z, giving every b-coordinate of Z.
5. B X=1_48 for that solved b-coordinate matrix B.
6. (P_067 P_Z) X=1_48, retaining all original two-coordinate slots.

`Z-exact-lattice-certificate.json` retains every full input, right side,
row operation, pivot, swap sign, triangular matrix, transformed right
side, solution and determinant. After persistence, the verifier replays
every operation and checks both original and transformed residuals,
every terminal lower-triangular zero and all nonzero pivots. The solved
maps agree entrywise with all six saved Z transports. All eight inverse
products pass, including the two inclusion products. Solved W maps
agree with the separately replayed full W input.

The solved inclusion and inverse inclusion agree with both original
359/361 decisions, the independent full multiplier, both original
numerator preimages and its independent preimage. With the same T and
M as above, P_Z T=P_W and P_W M=P_Z. The two comparisons between the
direct Z lattice and the audited whole multiplier have integral entries,
give both lattice containments and are inverse matrices. The inclusion
determinant is 64, and det(P_W)/det(P_Z)=det(T), so the orientation is
[Z:W]=64. The separately retained [W:V]=32 is not substituted.
Both directly solved units represent constant one and satisfy all
192 two-sided W/Z basis actions.

For each canonical m/n/s/u/v/w/z power map, the lcm of all 2304 rational
denominators is independently computed as 31/62/124/248/496/992/1984,
respectively. All 16128 scaled slots agree with the saved complete
arrays, and every scale metadata transition passes. In particular the
final scale is reconstructed, not inferred from metadata.
`Z-solve-report.json` records all six systems with no failure.

Fresh S/U/V/W/Z table replay checks every full table, transport, inverse
and unit. The unchanged `verify_z.py` separately verifies all 2304 Z
product identities in original H with leading coefficient 343, including
110592 integer coefficients and 218880 zero-remainder slots. Every
persisted dividend is reconstructed from the actual basis/table (and
the appropriate radical for actions), not merely compared with a saved
PASS label. `audit-dividend-report.json` records 92160 fixed S/U/V/W
divisions, 6912 fixed W-action divisions, 2304 fixed Z divisions, 9216
fresh S/U/V/W divisions, 2304 fresh W-action divisions and 2304 fresh Z
divisions: 115200 complete identities. All 95/47/95 dividend/quotient/
remainder positions and exact types are checked. Rational fallback
remains implemented; all exact zeros use Fraction arithmetic.

All original V solves and direct-W systems through 363 are compared in
full and replayed operation by operation. The saved original eliminations,
independent complete rank/kernel factorizations, both global preimages
and every full rank-48 radical action pass as fixed evidence. The
six-column Z interface remains separate from the older five-column W
interface. This imports L093's audited multiplier identification and the
same cited theory; it does not reprove a general multiplier theorem.

The encompassing inventory contains 9509 originals, including all 8721
step-363 inputs, every step-363 artifact, canonical L094 and the approved
audit assessment. All 383 step-363 copy bindings and twenty recorded
source hashes are checked, together with earlier exact transitions.
`post363-transition.json` binds the precise old/current attempt-note
hashes to its original inventory and unique completion append, and to
history 363 (SHA256
`e76e1a2bf343f96dae3eb0e863181666b8aff145551c31f72a176358b7f937cb`).
There is no pathname exemption. `preservation-audit.json` checks all
9509 original hashes, all 433 fresh fixed copies and twenty fresh source
hashes after arithmetic; all complete inventories/manifests/reports are
reread before acceptance.

The external execution takes 80.38757325010374 seconds and writes
101323541 bytes through final writing. `stage-report.json`,
`watchdog.json` and `final-bound.json` pass with empty failures and
conservative inclusive bounds 82<180 seconds and
101327514<134217728 bytes. There is no failure, repair, retry, resumption
or cap enlargement. The subsequent canonical-proof and attempt-note
updates are recorded as exact post-execution transitions in history 365;
executed sources and certificates remain fixed. This validates L094's
fixed table only and adds no mathematics beyond the checked known methods.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit entire
multiplier-order table and its certificates has not been checked.
Unknown availability is not evidence of absence. The cited theory,
audited input hypotheses and full exact replay provide the present
evidence; no additional Mathlib availability claim is made.
