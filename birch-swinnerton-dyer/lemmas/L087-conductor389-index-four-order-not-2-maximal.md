# L087 — The entire index-four order is not 2-maximal

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, primitive H=343h, L077's original nonmonic basis b,
L078's full order R with basis m, L080's multiplier identification,
audited L084/L085 and audited L086's full order S with basis

\[
n_i=m_i\ (i<47),\quad n_{47}=m_{47}/2,\qquad
s_i=n_i\ (i<46),\quad s_i=n_i/2\ (i=46,47).
\]

Keep the entire field, both original coordinates, all rational transports,
scales 31/62/124, and the actual identity. Use all 49 fixed step-329
basis/product files and complete step-331/333 evidence, as specified by
`drafts/literature/2026-10-19-index-four-order-prime-two-test.md`, whose
SPECIALIZE decision predates this attempt. Fix p=2. No old-order rank
or verdict is transferred; no selected factor, global maximality,
complete units/classes, L026 package or cross-notebook input is assumed.

## Conclusion

For I=√(2S), the full multiplier is the strict integral overorder

\[
U=(I:I)=\sum_{i=0}^{44}\mathbf Zs_i
             +\mathbf Z(s_{45}/2)+\mathbf Z(s_{46}/2)+\mathbf Z(s_{47}/2),
\qquad [U:S]=8.
\]

Thus S is not 2-maximal. In s-coordinates the full integral preimages are

\[
I=2\mathbf Zs_0+\sum_{i=1}^{47}\mathbf Zs_i,
\qquad N=\sum_{i=0}^{44}2\mathbf Zs_i+\sum_{i=45}^{47}\mathbf Zs_i,
\qquad U=N/2.
\]

The sixth Frobenius matrix has rank one and complete kernel
span(e₁,…,e₄₇) over F₂. The entire 2304-by-48 action on the rank-48
module I/2I has rank 45 and complete kernel span(e₄₅,e₄₆,e₄₇).
The explicit strict witness is s₄₅/2.

One combined input-validation/production/independent-replay stage passes.
Inclusive bounds are 7 seconds <180 and 24942757 bytes <134217728.
This is a fixed known-method reproduction; the separate step-337 critical
audit below passes. It produces no table for U, further correction, maximality of U,
global maximality, field discriminant, complete units/classes, descent
bound, rational membership or arbitrary-curve complex-order/rank comparison.

## Proof

**Imported method and applicability.** Import Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2),
Proposition 9.3 with proof and the following full action/kernel/lifting
paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
For a full order A in a number field and a nonunit rational prime p,
the integral preimage of the kernel of a Frobenius iterate on A/pA,
with p^k greater than its dimension, is √(pA). The multiplier equals
p⁻¹N, where N is the full integral preimage of the kernel of A/pA's
action on √(pA)/p√(pA). Lemma 6.4 gives integrality of this multiplier;
Proposition 9.3 supplies the local stopping criterion. These results
are imported, without reproof or an odd-prime/monogenic restriction.

L067 and L086 supply a full order in a number field. Two is a nonunit
because S is finite free over Z. Its radical contains 2S, so it is a
nonzero full finite module. Six iterates suffice since 2⁶=64>48.
The imported method gives neither this instance's matrices nor bounded
execution success. These are the finite obligations established below.

**Entire actual-S input before modular production.** All fresh artifacts
are in `scripts/seven-torsion/index-four-order-two-335/`.
`input_verify.py` reuses step 331's repaired independent verifier,
changing only its report/preservation filenames. It imports no producer.
It reconstructs every H coefficient, all original b-basis coefficients,
both b/power inverse products and both L067 coordinate transports.
It reconstructs L078's two exceptional columns explicitly with denominator
31, verifies its complete inverse and transports, then the L080 diagonal
change with its actual full multiplier data. It reconstructs all six
L084 forward/reverse transports and identifies the whole L085 multiplier
against its audited copy. The two final half-basis columns are retained.

For the actual S, all six rational transport matrices, eight inverse
products including the multiplier/inclusion pair, and 18432
transport/inclusion entries agree with the reconstructed matrices.
The full old inclusion is diag(1,…,1,2,2), with determinant four;
every zero as well as nonzero entry is checked. The actual identity u
is obtained by transporting 1 from b-coordinates, is integral and maps
to 1 in K. It acts as identity on both sides of all 48 s-basis vectors.
No order-coordinate e₀ is presumed to be the unit.

Write V_i(T)=124s_i(T). The verifier reconstructs all these integer
polynomials via scales 31/62/124, using explicit Fraction reconstruction
even for integer zeros. For all 2304 ordered pairs it verifies

\[
V_iV_j-124\sum_{k=0}^{47}c_{ijk}V_k\equiv0\pmod H.
\]

Full division in Q[T] retains 95 dividend positions, a 47-position
quotient and all 95 zero remainder positions. At every integer fast
path the division by 343 is checked; nondivisibility falls back to
exact fractions. All 110592 integer table slots, including zeros,
and all 218880 polynomial positions pass. No rational fallback is
needed for this instance, but its absence is not assumed.

Each `division-ii.json` persists the entire dividend, quotient and
remainder for all 48 products. Before any modular production, `stage.py`
rereads every coefficient, reconstructs each dividend from the actual
fixed V and table row, and verifies H times the complete quotient plus
the zero remainder equals that dividend. This supplies 2304 complete
persisted division checks. `input-validation.json` records that they
precede modular production; copies match all of steps 329/331/333.

**Separate production and independent Frobenius replay.** `produce.py`
uses polynomial multiplication, reduction in the original H and triangular
conversion to b, followed by the full integral b-to-S inverse and checked
division by 124²=15376. All 110592 recovered table coefficients agree
with the independently validated fixed table. Both actual identity
actions are checked again. Modular multiplication then uses operands
in {0,1}; its NumPy contraction has bound 48²=2304<2⁶³. Composition
uses Python integers. All six full Frobenius matrices are saved.

`verify.py` imports no producer arithmetic. It reads the validated full
S basis/table and checks every field of the producer's `input-basis.json`.
Using a different loop order and exact Python integer table multiplication,
it independently squares each of the 48 basis images six times. All
13824 saved entries and each composition with the first Frobenius matrix
agree. Metadata retains exponent 64, dimension 48 and prime two.

Every reversible row operation of the terminal matrix's elimination is
replayed, with valid indices, nonzero scalings, pivots and entire pivot
columns. All terminal coefficients and every remaining zero row are
checked. The rank is one and its first reduced row is e₀. All free-variable
equations give exactly e₁,…,e₄₇; every resulting kernel vector is also
checked against the complete original matrix. Hence the kernel is
complete, rather than only a contained subspace.

**Both global integral preimages.** For either computed kernel, the
producer first reduces its entire basis reversibly. If G contains its
reduced integral lifts and all 2e_i, the saved basis L, rational inverse
and integer generation matrices C,D satisfy

\[
L=GC,\qquad G=LD,\qquad LL^{-1}=L^{-1}L=1.
\]

The independent verifier checks the full kernel reduction, every entry
of both integer generation identities, all shapes/integrality and both
inverse products. These prove equality of the whole integral preimage,
including the empty-kernel case supported by the same interface.
Here the Frobenius preimage basis is diag(2,1,…,1), giving the displayed
I by the cited radical theorem.

**Entire I/2I action and its complete kernel.** For every s_i let A_i
be its integral action in this verified I-basis L. If L_i is multiplication
by s_i on S, replay checks all entries of

\[
LA_i=L_iL.
\]

It additionally sets W_j=Σ_l L_lj V_l and, for every i,j, independently
checks in original H

\[
V_iW_j-124\sum_k(LA_i)_{kj}V_k\equiv0\pmod H.
\]

Thus all 110592 integer action slots and every original-H action
identity are checked on the full rank-48 I/2I. Using I/2S instead
would omit essential directions and is not done.

Every action division is persisted in `action-division-ii.json` with
all dividend, quotient and remainder positions. Within the same cap,
the stage reconstructs each W_j and LA_i from the actual full saved
radical basis, table and action matrix, checks the coordinate identity
again, reconstructs the actual dividend and verifies the entire saved
division identity. All 2304 action certificates pass; no dividend label
or preview substitutes for the polynomial equality.

The action stack has row (j,k), column i equal to (A_i)_kj modulo two.
Independent replay verifies its complete 2304-by-48 matrix, every
reversible elimination operation, all pivots, terminal zeros and
free-variable equations. Its pivot columns are 0,…,44, its rank is
45 and its entire kernel is span(e₄₅,e₄₆,e₄₇). Across both eliminations
and both kernel-basis reductions, 1591 reversible row operations pass.
The two-sided integral-generation evidence gives the entire preimage
N with basis Q=diag(2,…,2,1,1,1). The cited multiplier theorem therefore
identifies U=N/2, establishing the asserted full lattice.

**Index and strictness.** `decision.json` saves M=Q/2 and integral
T=2Q⁻¹. Both full inverse products hold, so T includes every S basis
element in U, and the actual identity is Tu with M(Tu)=u.
Every upper-triangular zero is checked before the diagonal determinant
calculation. The complete diagonal of T is 45 ones followed by three
twos, giving |det T|=8, in agreement with 2 to the full kernel dimension.

The strict numerator is e₄₅, outside 2S. Its saved integer action B
satisfies A₄₅=2B in all 2304 slots, so s₄₅/2 preserves all of I
but is outside S. The source integrality result makes U a strict
integral overorder of 2-power index. Consequently S is not 2-maximal.
A nonzero radical alone is never used to assert nonmaximality, and no
maximality of U is inferred.

**One bounded execution and preservation.** The sole command is

```bash
python3 -B scripts/seven-torsion/index-four-order-two-335/run_once.py
```

The external watchdog starts before code generation, hashes, copies
or mathematics. The three prepared source files (`run_once.py`,
`prepare.py`, `stage.py`) are disclosed in `run-start.json` and included
in all recursive bytes. `prepare.py` only generates fresh code using
explicit guarded substitutions; no historical producer or one-shot
wrapper executes. A start marker and exclusive writes prevent a retry.
The watchdog covers the entire input verification, production, independent
replay, all persisted-evidence checks, final preservation and report writes.

`canonical-input-hashes.json` records 1020 originals, including the full
historical evidence used, canonical input lemmas, prior assessment,
histories 329/331/333 and ATTEMPTS/041/042/044. The 49 untrusted fixed
copies match the corresponding original files in all three historical
stages. Final preservation checks every original, fixed copy and all
six setup/generated Python source files. `copy-manifest.json`,
`code-hashes.json` and `preservation-stage.json` distinguish them;
no historical evidence, stopped computation or unfinished work is edited.
These hashes supplement complete arithmetic verification.

Input, producer, independent-verifier, stage and watchdog reports pass
with no failures. The encompassing execution takes 5.374489 seconds
(rounded upward), with 24938782 bytes after watchdog/final-bound writing.
`final-bound.json` conservatively bounds inclusive final writing by
7 seconds and 24942757 bytes, checked after its write, strictly below
180 seconds and 134217728 bytes. All setup code, copies, logs, full
division/elimination/lattice/action certificates, rereads and preservation
are included. No retry, fixture, successor table, correction iteration
or other-prime test occurs. The subsequent documentation records this
completed known-method test; its separate audit is recorded below.

**Separate critical audit, 2026-10-19 (step 337).** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-19-index-four-order-two-critical-audit.md`.
The full proof, all six step-335 scripts, explicit original b/m bases,
L086's full-order identification and prior L085 audit mechanism were
inspected. Stevenhagen's cited radical/multiplier/integrality results
are reused under the same full-order hypotheses; no source theorem is
reproved and no new maximality test is substituted for this audit.
ATTEMPTS/041/042/044 remain intact.

All fresh evidence is in `scripts/seven-torsion/index-eight-audit-337/`.
Three sources (`run_once.py`, `audit.py`, `independent.py`) were prepared
before the watchdog; this preparation read code only and executed no
mathematical checks. Their bytes are included in the recursive total.
The external watchdog starts before inventories, copies or mathematics.
Exclusive writes and its start marker prevent a second invocation.
The sole execution is

```bash
python3 -B scripts/seven-torsion/index-eight-audit-337/run_once.py
```

Neither the original run/prepare/stage wrapper nor any producer executes.
The fresh input and kernel verifiers are byte-identical copies of
step 335's `input_verify.py` and `verify.py`. All 1020 inputs in that
step's canonical inventory match their saved hashes. The new inventory
also includes every original step-335 file, this lemma before the
addendum, the prior assessment and the reused supplement source:
1249 originals. All 49 fixed table/basis copies agree with steps
329/331/333 and 335. The 208 fixed copies comprise those 49 files,
54 input-basis/Frobenius/lattice/action/decision files, two verifier
sources, 96 original division files and seven reference reports.
Reference PASS labels do not establish a new check.

The fresh input verifier reconstructs the entire scale-31/62/124 chain,
all six rational transports, eight inverse products, 18432 transport/
inclusion entries, actual identity with its 96 actions, all 2304
original-H products and all 110592 integer slots. Complete fresh
kernel replay recomputes all six Frobenius matrices and 13824 entries,
replays all 1591 reversible row operations across the eliminations and
kernel reductions, checks every pivot and terminal zero and both complete
kernels, and verifies both full global integral preimages. All 48
integral actions on I, with 110592 slots, pass full original-H replay.
The stale scale-62 comment is not used: the executable polynomial
expansions retain scale 124 and H's leading coefficient 343.

`audit.py` separately reconstructs every original product and action
dividend from the actual V_i=124s_i, table, radical basis and full
integral action. It checks all 95 integer dividend positions, 47 exact
rational quotient positions and 95 zero-remainder positions in every
one of the 2304 original product and 2304 original action division
certificates. It checks exact integer indices and string rational types,
then H times the full quotient plus remainder equals the actual dividend.
These originals have distinct `fixed-` names and are never replaced
by generated evidence. The corresponding 4608 fresh replay divisions
receive the same complete checks within the cap.

The supplement `independent.py` imports no producer/verifier arithmetic
or saved elimination operations. From the validated commutative table
it forms Frobenius using the diagonal products modulo two (cross terms
cancel) and composes it six times. Its terminal matrix agrees in all
entries with the fixed one. Independently it reconstructs every integral
radical action as J^{-1} L_i J, where L_i is multiplication by s_i in
the complete table and J is the independently reconstructed radical
basis; all entries and J A_i=L_i J agree. It builds the entire
2304-by-48 action stack with row (j,k), column i equal to (A_i)_{kj}
modulo two.

For each of these two complete binary matrices M it persists C (its
first r columns), a factor B, a full left inverse L, the complete
kernel matrix K and a coordinate left inverse P. Here r=1 for
Frobenius and r=45 for the action stack. Independent reverse-pivot XOR
selects r rows of C and exactly inverts that square matrix to build L;
no stored elimination operation enters this construction. After writing,
the supplement rereads every entry, checks all shapes and binary types,
and verifies

\[
M=CB,\qquad LC=1_r,\qquad MK=0,\qquad PK=1_{48-r}.
\]

The first two equations prove both bounds on rank M. The last two
and r+(48-r)=48 prove that K is the entire kernel, not a sampled
subspace. All 2304/110592 entries of the respective factorizations
and the full left-inverse products are checked; B consists of the first
r coordinate rows. K consists of the remaining coordinate columns.
Both kernel spans agree in both directions with the saved complete
kernels and the displayed kernels in this statement.

For each kernel the supplement constructs G from all its integral lifts
and all 2e_i, independently reconstructs the displayed diagonal basis
D, and persists integer matrices A,B and the rational inverse D^{-1}
with D=GA and G=DB. Complete reread verifies both integer-generation
identities, both inverse products, and both integral changes of basis
to/from the saved lattice, including their inverse products. Thus these
are the full global preimages I and N. The saved bases are exactly
diag(2,1,...,1) and diag(2,...,2,1,1,1), respectively.

Finally the supplement persists and rereads U=N/2, its full integral
old-order inclusion T, actual identity and strict action. Both multiplier/
inclusion inverse products hold. Every entry of T agrees with the
identity diagonal except its last three entries are two, giving
[U:S]=|det T|=8 with the correct orientation. The original-H identity
is 1, not an assumed order-coordinate vector. The full 2304-entry
action of s_45/2 on I is integral and equals half the independently
reconstructed action of s_45; its old-order coordinate 1/2 proves
strictness. The cited integrality theorem then proves the asserted
strict overorder. No closure table for U or maximality of U is inferred.

`audit-report.json`, `independent-report.json`, `watchdog.json` and
`final-bound.json` all pass without failures. Complete report and
supplement rereads occur inside the watchdog. Final preservation checks
every one of the 1249 originals, 208 fixed copies and five prepared/
copied Python sources; `audit-preservation.json`, `copy-manifest.json`
and `code-hashes.json` retain full before/after evidence. Preservation
of the original lemma precedes this documentation addendum.

The sole execution takes at most 6.741229 seconds and 39833636 bytes.
The persisted conservative inclusive final-writing bounds are
8 seconds <180 and 39837611 bytes <134217728; they are checked after
their write. All setup, copies, logs, full certificates, rereads,
preservation and final reports are included. No retry, malformed-data
fixture, correction, successor table or other-prime test occurs.
This validates the fixed known-method result, without progress beyond
the imported general method. Global maximality, complete units/classes,
full descent enclosure, rational membership and arbitrary-curve BSD
rank equality remain unresolved.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit
multiplier-order test has not been checked; unknown does not mean absent.
The precise cited general method, audited full-order inputs and complete
finite certificates above supply the mathematical evidence. No new
general theorem or progress beyond the checked source method is claimed.
