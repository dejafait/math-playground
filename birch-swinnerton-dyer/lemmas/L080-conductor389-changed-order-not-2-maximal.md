# L080 — The changed order is not 2-maximal

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive integer H=343h. Use audited L077's
nonmonic starting basis b and complete rational transports, and audited
L078's changed order R with ordered basis m, full integral table,
basis matrix M₀ in b-coordinates, inverse C₀ and actual identity C₀e₀.
This is the same R tested in L079; its 31-maximality is not used at 2.
Fix p=2. No L026 premise, selected field factor, stopped step-293 power
or cross-notebook input is used.

All fresh finite evidence is in `scripts/seven-torsion/changed-order-two-303/`.
Its `input-hashes.json` retains 434 before hashes, including the original
L067 certificate and the L077/L078 construction and audit files, together
with the L079 test/audit files. Preservation is checked before and after.

## Conclusion

For I=sqrt(2R), the computed multiplier R⁺=(I:I) is a strict order with

\[
 R^+=\mathbf Zm_0+\cdots+\mathbf Zm_{46}
                 +\mathbf Z(m_{47}/2),\qquad [R^+:R]=2.
\]

In particular R is not 2-maximal. Its radical and multiplier numerator
have the following complete global integral preimages in m-coordinates:

\[
 I=2\mathbf Zm_0+\sum_{i=1}^{47}\mathbf Zm_i,\qquad
 N=\sum_{i=0}^{46}2\mathbf Zm_i+\mathbf Zm_{47},\qquad R^+=N/2.
\]

The sixth Frobenius matrix has rank one and kernel dimension 47 over F₂;
the full 2304-by-48 action matrix on I/2I has rank 47 and kernel F₂e₄₇.
The strict witness is m₄₇/2=b₄₇/2, with a complete integral action on I.
One producer and independent complete replay pass the single aggregate
180/181-second and 134217728-byte limits. This is fixed known-method
reproduction. Its separate fixed critical audit passes below.
No further correction, new multiplication table, 2-maximality of R⁺,
global maximality, field discriminant, complete units/classes, descent,
Selmer bound, successful localization, rational membership or BSD rank
comparison is supplied.

## Proof

**Imported theorem and specialization.** Import Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2),
Proposition 9.3 and its following complete action/kernel/lifting
paragraph p.235](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
For a full order R in a number field, the inverse image of the kernel
of an iterated Frobenius on R/pR, with p^k greater than its dimension,
is I=sqrt(pR). The multiplier is p⁻¹N, where N is the full integral
preimage of the kernel of R/pR acting on I/pI. Lifts of the entire
kernel and all pR generate N. Lemma 6.4 gives integrality of the
multiplier; it is an order containing R, and Proposition 9.3 supplies
the local equality stopping criterion. These general statements are
imported; no new theorem is claimed or reproved.

Audited L067/L077/L078 supply the field and full order. The prime 2 is
not a unit in an order finite free over Z. The source has no odd-prime
restriction, and 2⁶=64>48. The original nonmonic first-correction theorem
is not reapplied to this changed basis. All six iterates and both full
preimages must be recomputed. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-changed-order-prime-two-test.md`.

**Identifying the full input in original H.** Both programs check all
49 H coefficients against 343h, content one and degree 48. The replay
reconstructs every original b-polynomial from H, checks both original
power-basis inverse products and both L067 transports. It checks
M₀C₀=C₀M₀=1, both complete changed transports and their inverses, and
the actual identity u=C₀e₀, including M₀u=e₀. Multiplication by u on
both sides of all m_i is verified; e₀ is not assumed to be the identity
in m-coordinates.

Let V_i(T) represent 31m_i, computed from the original b-polynomials
and L078's entire integer numerator 31M₀. The producer reconstructs
every input product using exact integer polynomial reduction by H,
conversion to b and then C₀/31². The independent replay instead checks,
for every ordered pair and the entire supplied coefficient vector c_ij,

\[
 V_iV_j-31\sum_k c_{ijk}V_k\equiv0\pmod H.
\]

Every division is exact, every remainder coefficient is zero and all
110592 integer coefficient slots, including zeros, are covered.
Thus the table is identified in the entire K. The original scale 31
remains in these identities; it is distinct from the testing prime 2.
No rational transport is used as an inverse modulo the new prime.

**Six full Frobenius iterates.** The producer computes each m_i² from
the verified table, starting powers with the actual identity modulo 2,
and composes its full first Frobenius matrix to retain all six iterates.
Its NumPy int64 operands and table entries are reduced to {0,1}; every
bilinear contraction is bounded by 48²=2304<2⁶³. Matrix compositions
use Python integers. The independent verifier uses only exact Python
integer table multiplication in a different loop order, successively
squaring all 48 basis images six times. It checks all 13824 entries of
the saved matrices and every successive composition with the first.
`frobenius.json` also retains prime 2, dimension 48 and exponent 64.

The complete sixth-matrix elimination is replayed: every invertible
row operation, pivot, leading entry, whole terminal matrix and all
terminal zero rows are checked. Free-variable reconstruction and full
matrix membership verify the entire kernel, not only 47 witnesses.
The rank is one, its pivot is 0 and its kernel is spanned by e₁,…,e₄₇.
The cited Frobenius theorem therefore identifies its preimage with I.

`radical-lattice.json` retains the lift generator matrix S_I, comprising
all kernel lifts and every 2e_i, basis J=diag(2,1,…,1), integer generation
matrices C_I,D_I and the full rational inverse. Replay checks every entry of

\[
 J=S_IC_I,\qquad S_I=JD_I,\qquad JJ^{-1}=J^{-1}J=1.
\]

These two integral generation identities identify the whole global
preimage, rather than a lattice with the same local dimension.

**Full integral action and numerator.** Each `action-ii.json` contains
all entries of the integer operator A_i for multiplication by m_i on I
in the verified J-basis. Both programs check J A_i=L_i J, using the full
input multiplication table. Independently, for W_j=Σ_l J_lj V_l, replay
checks in original H every polynomial identity

\[
 V_iW_j-31\sum_k(JA_i)_{kj}V_k\equiv0\pmod H.
\]

Every exact division and every zero remainder is checked. All 110592
integral action slots are covered before reduction. The module is the
full rank-48 I/2I, not its dimension-47 image I/2R.

The complete action stack has row (j,k), column i equal to (A_i)_kj
modulo 2. Its full elimination, all terminal rows and free-variable
kernel are independently replayed. The rank is 47 and the entire kernel
is F₂e₄₇. Across the two main eliminations and both kernel-basis
reductions, replay checks all 1735 recorded invertible row operations.
`numerator-lattice.json` retains all kernel lifts and 2R, full basis
Q=diag(2,…,2,1), both integer generation matrices and its rational inverse.
The same two-sided generation and inverse identities as for J prove
Q Z⁴⁸=N globally. The imported lifting result gives R⁺=N/2.

**Exact inclusion and strictness verdict.** `decision.json` retains
M=Q/2, T=2Q⁻¹=diag(1,…,1,2), both inverse products, integral old-order
inclusion and the transported actual identity T u. Every entry above the
diagonal and all 48 diagonal entries are checked, giving det(T)=2 and
index two; this also equals 2 to the full action-kernel dimension.
Thus R⊂R⁺ with the displayed complete basis.

The saved strict witness has numerator e₄₇ and column 47. It is outside
2R. Its full integral radical action B is checked in all 2304 slots by
A₄₇=2B. Consequently m₄₇/2 preserves every element of I, while it does
not belong to R. The imported multiplier integrality identifies a strict
integral overorder of 2-power index, so R is not 2-maximal. No equality
branch or stopping criterion for R⁺ is asserted. No correction is iterated
and no new order multiplication table is constructed.

**Bounds and preservation.** The producer takes 1.297114 seconds internally
and replay 0.941681. The aggregate report gives 2.547015 internal seconds,
below 180; the outer watchdog gives 2.626339 seconds, below 181. The full
execution directory occupies 5424404 bytes, below 134217728, including
code, certificates, logs and reports. Both stages report all required
products, actions and Frobenius slots, ranks 1 and 47, index two and zero
failures. Full reports are `producer-report.json`,
`verification-report.json`, `aggregate-report.json` and `watchdog.json`.
All 434 original files have equal before/after hashes in both stage
preservation reports and `preservation-aggregate.json`. Hashes supplement
complete arithmetic replay. No stopped-power input, malformed fixture,
retry, resumed execution or increased allowance occurs. The one-shot
command refuses to overwrite its marker or output evidence:

```bash
python3 -B scripts/seven-torsion/changed-order-two-303/run_once.py
```

This completes the fixed first-decision test. Its separate critical audit
is recorded below. The computed strictness is a local arithmetic input, with
no progress beyond the imported general method or resolution of BSD.

**Separate critical audit (2026-10-18, step 305).** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-changed-order-two-critical-audit.md`.
The complete proof, producer, independent verifier, aggregate and watchdog
were inspected before execution. The cited source is applied to the full
order R from audited L067/L077/L078: I is a nonzero full ideal, the
residue algebra has dimension 48, and 2 is a nonunit. The prime-two case
has no extra oddness hypothesis. The iterated Frobenius threshold is
64>48. The action is on the entire I/2I, not I/2R. Multiplier integrality
and its full numerator description are precisely the imported results;
no nonmonic criterion is reapplied to the changed basis.

Fresh evidence is in `scripts/seven-torsion/changed-order-two-audit-305/`.
The audit inventories all 434 upstream inputs and all 70 step-303 files,
504 distinct originals in total. It copies 56 required files to this
fresh sibling directory with equal hashes, including the byte-unchanged
verifier. Relative upstream paths consequently have their original
meaning and all report paths are fresh. The producer is not run.
`copy-manifest.json` records every copied hash; `original-hashes.json`
and `audit-preservation.json` record the complete original inventory
and its equal before/after hashes.

The fresh verifier passes all 110592 original-H product slots, all
110592 integral action slots, every identity and transport, all 13824
Frobenius entries, and all 1735 row operations with all pivots, terminal
rows and reconstructed kernels. It checks both two-sided global lattice
generation identities and inverses, old-order inclusion, actual identity,
index and every strict-witness product. This is a complete replay rather
than inspection of the old reports. The original factor 31 in all
polynomial identities remains distinct from modulus 2. Reduced producer
contractions are bounded by 2304<2^63; the fresh replay uses exact Python
integers and does not depend on that machine representation.

The supplement does not reuse saved elimination operations. Let F_6 be
the complete sixth Frobenius matrix and u its column zero. In
`frobenius-rank-one.json` it checks all 2304 entries of

\[
 F_6=u e_0^{\mathsf T},\qquad u_r=1\text{ for a recorded row }r.
\]

This gives both rank inequalities and identifies the whole kernel as
the span of e_1,...,e_47. All 2256 entries of its product with that
kernel basis are checked. The actual identity coordinates are separately
reconstructed from the displayed L078 basis as
31e_0 minus the even-position coefficients of r_0 in positions 2,...,46;
their full Frobenius-fixed identity is checked.

The full action stack A is reconstructed from all 48 integral actions
with row (j,k), column i equal to (A_i)_{kj} modulo 2. Its equality
with all 110592 saved entries and its entire zero column 47 are checked.
Fresh reverse-row bit-vector selection chooses 47 original rows on
columns 0,...,46. For the resulting square minor B, reverse-column
Gauss--Jordan constructs C, then checks all entries of BC=CB=1 over F_2
(4418 product slots). These full inverse products prove rank at least
47 without trusting the selection routine or old elimination. The
nonzero vector e_47 is in the kernel, verified in all 2304 rows, so
rank is exactly 47 and the whole kernel is F_2 e_47.
`action-minor.json` retains A, row/column selection, B, C, both products
and the full kernel product.

`independent-lattices-witness.json` reconstructs both global preimages
without the saved kernel reductions. For the respective free-coordinate
sets U={1,...,47} and U={47}, form S whose columns are e_i for i in U
followed by every 2e_i. Put d_i=1 for i in U and d_i=2 otherwise and
J_U=diag(d_i). The forward matrix selects e_i when i is in U and 2e_i
otherwise; the reverse matrix has row i equal to row i of S divided
by d_i. Every quotient is checked integral, all coefficients agree with
the saved matrices, and both S C_U=J_U and J_U D_U=S are checked in
full, as are both inverse products with diag(1/d_i). Thus these are
equal global integer lattices, not merely bases after localization:

\[
 I=\operatorname{diag}(2,1,\ldots,1)\mathbf Z^{48},\quad
 N=\operatorname{diag}(2,\ldots,2,1)\mathbf Z^{48}.
\]

Dividing N by two gives the entire multiplier basis
diag(1,...,1,1/2). The supplement independently checks every entry
of this matrix, its inclusion inverse diag(1,...,1,2), both inverse
products, the transported actual identity, and the determinant two.
The witness numerator is exactly e_47, outside 2R. Every one of the
2304 entries of A_47/2 is integral and equals the supplied witness
action. Hence m_47/2 preserves all of I, while its half-integral
m-coordinate proves it is outside R. The full changed-basis column
also verifies m_47=b_47. Together with the source multiplier theorem,
these checks prove a strict integral overorder of index two and the
claimed non-2-maximality of R. They make no claim about maximality of
that multiplier or any further correction.

`audit-report.json` records PASS with zero failures, 1.228407 internal
seconds against 180; `watchdog.json` records 1.272049 external seconds
against 181. The complete directory occupies 5770005 bytes against
134217728. All 504 originals are preserved. One command was executed:

```bash
python3 -B scripts/seven-torsion/changed-order-two-audit-305/run_once.py
```

The command is one-shot and refuses overwrites; it is not a resumption
instruction. There were no retries or altered-data fixtures, and none
are claimed. This completes the fixed audit of a known-method local
input. It supplies no global maximality, units/classes, descent,
rational-direction or arbitrary-curve BSD conclusion.

## Mathlib

Matching coverage for the radical/multiplier criterion, full integral
lifting and this exact certificate is not checked. Supporting coverage
is also unchecked; no absence is inferred. This is exact finite informal
evidence, not a Lean formalization.
