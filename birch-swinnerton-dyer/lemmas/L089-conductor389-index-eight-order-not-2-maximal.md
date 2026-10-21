# L089 — The entire index-eight order is not 2-maximal

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive H=343h, L077's original nonmonic
b-basis, L078's full m-order and L080/L084's full n-order. Retain
audited L085/L086's s-order, audited L087's multiplier identification
and audited L088's entire order U, with

\[
n_i=m_i\ (i<47),\quad n_{47}=m_{47}/2,\qquad
s_i=n_i\ (i<46),\quad s_i=n_i/2\ (i=46,47),
\]
\[
u_i=s_i\ (i<45),\qquad u_i=s_i/2\ (i=45,46,47).
\]

All rational transports retain the full field and both original point
coordinates. The 49 fixed U basis/product files in step 339 and their
step-341 audit copies, together with fixed steps 329/331/333/335/337,
are inputs. Keep scales 31/62/124/248 and the actual identity.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-19-index-eight-order-prime-two-test.md`.
Prime two is fixed; no previous-order rank or index is assumed for U.

## Conclusion

For I=√(2U), the complete multiplier is the strict integral overorder

\[
V=(I:I)=\sum_{i=0}^{43}\mathbf Z u_i+
                    \sum_{i=44}^{47}\mathbf Z(u_i/2),
\qquad [V:U]=16.
\]

Thus U is not 2-maximal. The full integral preimages, in u-coordinates, are

\[
I=2\mathbf Z u_0+\sum_{i=1}^{47}\mathbf Z u_i,
\qquad
N=\sum_{i=0}^{43}2\mathbf Z u_i+\sum_{i=44}^{47}\mathbf Z u_i,
\qquad V=N/2.
\]

The sixth Frobenius matrix has rank one and complete kernel
span(e₁,…,e₄₇). The entire 2304-by-48 action on the rank-48 module
I/2I has rank 44 and complete kernel span(e₄₄,…,e₄₇).
An explicit strict witness is u₄₄/2.

One combined input-validation/production/independent-replay execution
passes, with conservative inclusive bounds 12 seconds <180 and
59662925 bytes <134217728. This is a fixed reproduction of a known
method. Its separate critical audit below passes. No multiplication table
for V, further correction, maximality of V, global maximality, complete
units/classes, descent enclosure, rational membership or arbitrary-curve
analytic-order/rank comparison is supplied.

## Proof

**Imported method and applicability.** Import Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2),
Proposition 9.3 with proof and the following full action/kernel/lifting
paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
For a full order A in a number field and nonunit rational prime p,
the integral preimage of the kernel of iterated Frobenius on A/pA,
with p^k>dim(A/pA), is √(pA). For the action of A on the entire
√(pA)/p√(pA), let N be the full integral kernel preimage in A.
The source identifies (√(pA):√(pA))=N/p. Lemma 6.4 supplies integrality;
Proposition 9.3 supplies the local stopping criterion. Both radical cases
are covered. These statements are imported, without reproof or an
odd-prime or monogenic restriction.

L067 and audited L088 supply a full order in the entire number field.
Finite freeness over Z makes two a nonunit; I contains 2U and is a
nonzero full finite module. Six Frobenius iterates suffice since 64>48.
The cited theorem supplies neither the matrices below nor their bounded
execution. The finite specialization is therefore necessary; it claims
no progress beyond that known general method.

**Complete actual input before modular production.** All fresh evidence
is in `scripts/seven-torsion/index-eight-order-two-343/`. Fresh
`input_verify.py` and `verify_u.py` are byte-identical copies of the
independent step-339 verifiers and agree with step 341's fixed copies.
No historical producer or one-shot wrapper executes. The first verifier
reconstructs H=343h, its content one and degree 48, the entire original
b-basis, both b/power inverse products and both L067 coordinate transports.
It reconstructs the explicit even/odd L078 columns with denominator 31,
the n-order and s-order changes, full inverses and every transport entry.
All six S transports, eight inverse products, integral inclusion of
index four, actual identity and 96 left/right identity actions pass.
The 49 fixed S files agree throughout steps 329/331/333/335/337/339/341.

For every one of the 2304 S products, the verifier checks all 48 integer
table coefficients and the full original-H identity at scale 124. It
saves the entire 95-position dividend, 47-position rational quotient
and 95-position zero remainder. The encompassing stage independently
reconstructs every actual dividend and verifies H times the full quotient
plus remainder equals it. This applies to all three complete sets:
step 335's original divisions retained in 337/339, step 339's fresh
S divisions, and the current fresh replay divisions (6912 checks).
Every original division is copied under a distinct fixed name.

The U verifier checks both entire step-335/337 decisions, the audited
independent multiplier and full numerator lattice, not just their indices.
It reconstructs all three half-basis columns and all six U transports
from S, checks eight inverse products and all 18432 transport/inclusion
entries, the full integral inclusion and index eight, and the actual
identity with all 96 actions. Its 49 fixed U files agree byte-for-byte
with both steps 339 and 341. Original scale 31, prior scales 31/62/124,
current scale 248, input scale 124, and enlargement denominator two remain
explicit. Every scaled representative W_i=248u_i is reconstructed using
Fraction arithmetic, including integer zeros, and is integral.

For all 2304 U products, independent exact division verifies

\[
W_iW_j-248\sum_k c_{ijk}W_k\equiv0\pmod H.
\]

Every integer table slot, zero included, and every remainder position
is checked. Division by leading coefficient 343 uses an integer fast
path only after exact divisibility is checked; otherwise rational
arithmetic is used. Zero fallback counts are observed, never assumed.
The stage separately reconstructs the actual dividends of every original
step-339 U division and every fresh U division, and checks each complete
persisted identity (4608 checks). `input-validation.json` records that
all S and U input obligations finish before modular production. Hashes
and reference PASS labels do not replace any arithmetic identity.

**Fresh producer and independent Frobenius replay.** Inside the watchdog,
`prepare.py` performs guarded textual adaptations of step-335 sources;
it executes no historical arithmetic. The producer uses the actual
U basis/table and identity, reconstructs its original b and L067
transports, and checks every input product by polynomial reduction and
triangular conversion with exact divisor 248²=61504. This is distinct
from the independent input verifier's polynomial-zero checks.

The producer reduces the entire table modulo two and computes the first
Frobenius matrix by table multiplication using the actual identity.
Its int64 operands are binary residues; each multiplication has at most
2304 contributions of size one, strictly below 2⁶³. It composes and
saves all six full matrices. The independent kernel verifier imports
no producer arithmetic and reconstructs all six by repeated squaring
in the full table with exact Python integers; all 13824 entries and
every composition agree.

For the terminal matrix, `verify_elimination` replays every reversible
row operation, checks all pivots and leading ones, full pivot columns,
terminal zero rows and every free-variable equation. Its sole pivot
column is zero and its only nonzero reduced row is e₀ᵗ. Consequently
the rank is exactly one and the complete kernel is span(e₁,…,e₄₇).
No old-order rank enters this computation.

For the global preimage, `radical-lattice.json` saves G, containing all
reduced kernel lifts and all 2e_i, a rank-48 basis J, its full rational
inverse, and integer matrices C,D. Complete replay verifies

\[
J=GC,\qquad G=JD,\qquad JJ^{-1}=J^{-1}J=1.
\]

The independent verifier also checks the full reduction of the kernel
basis used to form G. These two integer generation identities prove
equality of the entire integral preimage. The resulting J is
diag(2,1,…,1), proving the displayed description of I by the imported
Frobenius criterion. The implementation supports empty and general
kernels as well; this diagonal form is an output, not a premise.

**Entire I/2I action and complete kernel.** For each u_i, the producer
saves its integral matrix A_i in the verified I-basis J. Let L_i be
multiplication by u_i in U. Independent replay checks all entries of

\[
JA_i=L_iJ.
\]

It additionally reconstructs Z_j=Σ_l J_lj W_l and checks, for all i,j,
the entire original-H identity

\[
W_i Z_j-248\sum_k(JA_i)_{kj}W_k\equiv0\pmod H.
\]

All 110592 action slots are integers and all 2304 polynomial identities
pass. The action is on the full rank-48 I/2I, including directions lost
by mapping into U/2U. Each full action dividend, quotient and remainder
is persisted. The stage rereads every certificate, reconstructs JA_i,
the entire actual dividend and H times the saved quotient plus remainder,
and checks all 2304 identities again at scale 248.

The entire 2304-by-48 binary action stack has row (j,k), column i equal
to (A_i)_kj mod two. Independent replay checks this entire matrix and
every reversible elimination operation. Its pivots are exactly 0,…,43,
all remaining reduced rows are zero, and every free-variable equation
gives precisely e₄₄,…,e₄₇. Its rank is exactly 44 and the kernel is
complete. Across both eliminations and both kernel reductions, 1521
reversible operations are replayed.

`numerator-lattice.json` supplies the same full two-sided integer
generation and inverse certificates for the action kernel's integral
preimage. They give Q=diag(2,…,2,1,1,1,1), with 44 initial twos, as
a basis for N. Hence the imported multiplier theorem identifies the
whole multiplier V=N/2, rather than just a suborder preserving I.

**Index, identity and strictness.** `decision.json` persists M=Q/2,
the full integral inclusion T=2Q⁻¹ and both inverse products MT=TM=1.
The actual identity in U is transported by T and verified by M back
to U's identity; no coordinate e₀ is assumed to be the ring unit.
Every required triangular zero is checked before the determinant is
computed. The complete diagonal of T is 44 ones followed by four twos;
its determinant has absolute value 16, with orientation [V:U], agreeing
with 2 to the complete action-kernel dimension.

The strict numerator e₄₄ is outside 2U. Its saved full integer action B
satisfies A₄₄=2B in all 2304 entries, so u₄₄/2 preserves all of I and
is outside U. Lemma 6.4 makes this multiplier integral. Thus V is a
strict integral overorder of U of index 16, proving U is not 2-maximal.
A nonzero radical alone would not prove this. No product table for V
or maximality of V is asserted.

**One combined bound and preservation.** The sole invocation is

```bash
python3 -B scripts/seven-torsion/index-eight-order-two-343/run_once.py
```

Three prepared sources (`run_once.py`, `prepare.py`, `stage.py`) were
syntax-checked without mathematical execution before the watchdog;
their bytes count in the recursive total. The external watchdog starts
before inventories, copies, source generation and mathematics. A start
marker and exclusive writes forbid another execution. The two generated
sources and two copied independent verifiers bring the total to seven
source files. The 248 fixed copies include the S/U tables, complete
original divisions, full multiplier inputs and the copied verifiers.

`canonical-input-hashes.json` records 2228 originals. All step-341
canonical hashes match except its pre-addendum L088 hash, whose current
hash and documented post-audit addendum are explicitly recorded in
`inventory-transition.json`. The earlier step-337 L087 audit-addendum
transition remains recorded, without adding a mathematical input change.
Current hashes of both lemmas are preserved. ATTEMPTS/041/042/044 and
all unfinished evidence remain intact.

Complete report, basis/table and inventory rereads, all persisted actual
dividend checks, final hashes and evidence writing occur under the same
watchdog. Every one of the 2228 originals, 248 fixed copies and seven
source files has matching before/after hashes. The two input reports,
producer, independent verifier, stage and watchdog reports all pass
with empty failure lists. No correction, retry, fixture, successor table,
other prime or second multiplier test executes.

The encompassing stage takes 10.312747209 seconds; the external execution
through final writing takes 10.425029085 seconds and 59658951 bytes.
`final-bound.json` conservatively bounds inclusive final writing by
12 seconds and 59662925 bytes, and these bounds are checked after the
final write. Both are strictly below 180 seconds and 134217728 bytes.
This advances one local arithmetic input by a known construction.
The separate critical audit below validates this fixed verdict; the independent
global arithmetic and BSD gaps stated above remain unresolved.

**Separate critical audit, 2026-10-19 (step 345).** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-19-index-eight-order-two-critical-audit.md`;
its exact COVERED_TARGET authorizes this replay-only audit. The complete
proof and seven step-343 sources, L088's table audit, L077/L078's canonical
basis formulas, the earlier independent rank/lattice implementation and
ATTEMPTS/041/042/044 were inspected. The cited Stevenhagen theorem applies
to the entire full order U in L067's number field, with nonunit two and
64>48. No source theorem is reproved, and no source supplies the fixed
arithmetic. The earlier S audit has a different lattice and rank, so does
not certify this U verdict.

All fresh evidence is in `scripts/seven-torsion/U-two-audit-345/`. The sole
execution was

```bash
python3 -B scripts/seven-torsion/U-two-audit-345/run_once.py
```

Two prepared sources were syntax-checked without mathematical execution;
their bytes are included. The external watchdog precedes inventories,
copies, the independent-source adaptation and all mathematical checks.
A fresh start marker and exclusive writes prevent rerunning this execution.
The three replay verifiers are byte-identical copies of the step-343
sources. The independent supplement adapts the assessed step-337 complete
rank/lattice mechanism to U and imports no producer/verifier arithmetic
or saved row operations. No historical wrapper or producer executes.

**Complete original evidence and fresh replay.** The inventory includes
all 2228 step-343 inventoried inputs, every step-343 artifact, this lemma,
the unchanged assessment and the reused sources: 2706 original files.
Every prior hash agrees without a new exception. The previously documented
post-audit L087/L088 transitions remain in `inventory-transition.json`.
All 248 entries of the step-343 manifest are checked against both original
source and fixed-copy hashes. There are 447 new fixed copies. All S
basis/table bytes agree with steps 329/331/333/335/337/339/341; all U bytes
agree with steps 339/341. Hash agreement binds provenance; arithmetic is
checked separately.

Fresh input replay reconstructs the entire b/m/n/s/u chain, both original
coordinate transports, all six U transports, eight inverse products,
actual identities and all 96 identity actions in each table. Every one
of the 2304 products and 110592 integer slots in each S/U table is checked
in original H, including zeros. Scales 31/62/124/248 and the leading
coefficient 343 are retained. Fraction arithmetic handles zero entries;
the exact-integer division optimization retains its rational fallback.
The entire audited U multiplier and numerator lattice are compared.

The audit checks all six original step-343 division sets under distinct
`original343-` names: `fixed-S-original-division-`,
`fixed-S-fresh-division-`, `division-`, `fixed-U-division-`,
`u-division-`, and `action-division-`. Each has 2304 identities, totaling
13824. Every dividend is reconstructed from the actual basis/table or
full radical action; all 95 integer dividend entries, 47 rational quotient
entries and 95 zero remainder entries, their shapes and types, and the
full equality to H times quotient plus remainder are checked. Original
saved evidence is never replaced by new output. Fresh replay supplies a
further 6912 division identities, all checked against actual dividends.

The unchanged kernel verifier independently recomputes all six Frobenius
matrices by exact table squaring and checks every composition and all
13824 entries. It replays all original eliminations, pivots, terminal zero
rows and free-variable equations, including the two kernel reductions:
1521 reversible operations. Both global preimages are checked by all
kernel lifts and 2U, full integer generation in both directions and both
basis inverse products. The input-basis certificate is compared with the
validated U. All 48 actions on the rank-48 I/2I are checked in every
integer slot, through JA_i=L_iJ and the full original-H identities.
The entire 2304-by-48 stack uses row (j,k), column i equal to (A_i)_{kj}.
It is not an action on the image in U/2U.

**Independent complete rank/kernel certificates.** The supplement
reconstructs the first Frobenius matrix from the diagonal products in
the validated commutative table: in characteristic two the cross terms
cancel. Five full binary compositions give the sixth matrix independently
of the saved elimination. For each of the sixth Frobenius and full action
matrices M, it persists complete matrices C,B,L with

\[
M=CB,\qquad LC=1_r.
\]

Here C consists of the first r columns and L is obtained by an independent
binary inverse on selected rows; every entry of both products is checked,
not just a selected minor. For Frobenius r=1; for the action r=44.
M=CB proves rank at most r and LC=1_r proves rank at least r. The entire
factor B equals [1_r | 0]. A complete kernel matrix K and projection P
satisfy MK=0 and PK=1_{48-r}, with rank plus kernel dimension equal to 48.
The persisted shapes, binary entries, all full equalities and their
round trips are checked. Both independent kernel spans are compared in
both directions with the original certificates and with the displayed
kernels span(e_1,...,e_47) and span(e_44,...,e_47).

The action stack is independently reconstructed using exact rational
J inverse times L_iJ, checking integrality in every slot and both the
coordinate equation and agreement with every saved action. Thus the
rank certificate is attached to all 110592 actual action entries.
`action-full-rank.json` includes the complete 44-by-2304 left inverse,
not merely the 44-by-44 selected inverse. Both full rank files are
persisted, reread and checked under the same cap.

**Independent global lattices, index and strictness.** For each kernel,
form G from all its independent integer lifts and all 2e_i. The independent
bases J=diag(2,1,...,1) and Q=diag(2,...,2,1,1,1,1), with 44 initial twos
in Q, have integer matrices A,B proving J=GA and G=JB (and likewise for
Q). Both rational inverse products and both integer containments against
the original saved I/N bases are checked. These are equalities of full
global Z-lattices, not just mod-two dimensions. The entire certificates
are persisted and reread, including all generator equations.

The multiplier is independently V=N/2 with basis Q/2. Its old-order
inclusion T=2Q^{-1} is checked in every entry and both inverse products.
Every off-diagonal entry is zero, and the diagonal consists of 44 ones
and four twos. Consequently |det T|=16 with orientation [V:U]. The
actual U identity represents the constant polynomial one at scale 248;
its image in V is checked in both directions. The complete integral
action of u_44/2 is A_44/2, checked in all 2304 entries. Its old coordinate
1/2 proves it lies outside U. The imported finite-module criterion then
makes this strict multiplier element integral. This verifies the full
verdict without constructing a table for V or asserting its maximality.
`independent-multiplier.json` and both independent preimage files are
fully reread and their load-bearing equalities rechecked.

**Preservation and strict combined bounds.** Fresh S/U/kernel reports,
all fixed table/basis files, division summaries, independent certificates,
complete inventories, source hashes and copy manifest are reread under
the watchdog. All 2706 original hashes, 447 copy hashes and six source
hashes match at completion. This lemma is preserved through the audit;
its subsequent documentation addendum is a separate explicit hash
transition in `drafts/2026-10-19-U-two-critical-audit-attempt.md`.
No retry, correction, malformed fixture, successor table or new prime
executes. Earlier stop evidence and unfinished work remain intact.

The audit and all three replay reports, independent report, watchdog and
final-bound report pass with empty failure lists. Actual execution through
final writing took 12.134980541886762 seconds and 81447172 bytes.
Conservative inclusive bounds, checked after the final write, are
14 seconds <180 and 81451146 bytes <134217728. This validates one fixed
known-method input and supplies no new general theorem. Global maximality,
complete units/classes, full descent enclosure, rational membership and
arbitrary-curve rank equality remain unresolved.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit complete
multiplier-order test and its certificates has not been checked.
Unknown availability is not evidence of absence. The precise cited
general method, audited inputs and complete finite replay supply the
evidence; no new general theorem or originality claim is made.
