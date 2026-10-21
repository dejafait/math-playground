# L077 — A complete nonmonic starting order in the degree-48 torsion field

## Hypotheses

Use the entire field K=Q[t]/h from audited L067 for
y²+y=x³+x²−2x. In particular h is monic irreducible of degree 48,
H=343h is primitive integral, and the full rational transports between
the t-power basis and L067's two-coordinate basis are available. Write
H(T)=a₀T⁴⁸+a₁T⁴⁷+⋯+a₄₈, with a₀=343.

The fixed exact evidence is in `scripts/seven-torsion/nonmonic-order-283/`.
`basis.json` retains every H coefficient, all basis and inverse matrices,
both transports to L067 and the SHA256 of its unchanged certificate.
The 48 files `product-00.json` through `product-47.json` retain all
110592 integer multiplication coefficients, including zeros.
`trace.json` retains all 48 traces and 2304 Gram entries.
`trace-elimination.json` and `resultant-elimination.json` retain both
complete input matrices, every pivot, swap and exact divisor, a hash
of every complete elimination stage, and the terminal determinants.
The complete replay reconstructs each stage and every division; hashes
are supplementary checks, not substitutes for computing these identities.
`discriminant.json` retains the full signed discriminant and resultant.

## Conclusion

For b₀=1 and

\[
b_i=a_0t^i+a_1t^{i-1}+\cdots+a_i\quad(1\le i\le47),
\qquad O_H=\bigoplus_{i=0}^{47}\mathbf Z b_i,
\]

O_H is an order in K, with the displayed Z-basis and identity
vector (1,0,…,0). Its trace discriminant is nonzero and equals disc(H).
The exact signed integer, stored without rounding in `discriminant.json`,
is negative and has 6870 decimal digits. It is the **order discriminant**;
neither it nor the order is asserted to be maximal.

All prescribed fixed tables, both rational basis inverses, full L067
transports and the trace/resultant equality pass the independent replay.
The construction is a known-result specialization and finite computation,
not a new general theorem. Its separate fixed critical audit passes,
including full replay and two distinct exact determinant calculations.
It supplies no index-prime coverage, maximal overorder, field discriminant,
S-unit/S-class completeness, faithful power-class quotient, descent local
bounds, successful localization, rational membership or rank comparison.

## Proof

**Imported construction and specialization.** Del Corso--Dvornicich--Simon,
*Decomposition of primes in non-maximal orders*, Acta Arith. **120**
(2005), 231–244,
[Section 2, pp. 232–234, and Proposition 4](https://www.impan.pl/shop/en/publication/transaction/download/product/82018),
define this nonmonic-polynomial order over a Dedekind ring and prove
disc(O_H)=disc(H) by triangular basis change. Apply their statement over
Z to L067's primitive irreducible H with nonzero leading coefficient.
There is one entire degree-48 field; no factor is selected and t is not
assumed integral. This imports the general theorem. The new work verifies
the complete fixed-field arithmetic and its feasibility under the approved
caps; it does not reprove the general construction.

**Basis and faithful transport.** The producer and independent verifier
check all 49 H coefficients against 343h, content one, degree 48 and
leading coefficient 343. Each of the 48 displayed b_i is checked
coefficientwise. Relative to (1,t,…,t⁴⁷), the basis matrix is triangular
with diagonal 1,343,…,343, so is invertible over Q. The full rational
inverse is explicitly checked in both orders. Multiplication by L067's
saved power matrix gives the transport to its original two-coordinate
basis; multiplication by its inverse gives the reverse transport.
All entries and both composite identities are checked. The lattice spans
the entire K and retains both original point coordinates through L067.

**Every product and integrality.** For each ordered pair (i,j), the
producer multiplies the integer polynomial representatives of b_i,b_j,
reduces by H over Q and converts to the displayed basis by descending
triangular substitution. In this instance every reduction division is
exact over Z, and every basis coefficient is an integer. Every zero and
nonzero slot is saved. The independent program imports no producer
arithmetic. For the complete saved vector (c_ijk) it instead constructs

\[
b_i(T)b_j(T)-\sum_{k=0}^{47}c_{ijk}b_k(T)
\]

as an integer polynomial of degree at most 94, divides it by H with
every division checked exact and verifies zero remainder. It checks all
48³ slots, their integrality, and multiplication by b₀ on both sides.
Invertibility of the basis and these full polynomial identities prove
closure for the entire lattice, not just the generators or a sample.
Thus O_H is a finite free rank-48 Z-algebra containing 1 and spanning K.
Every element is integral, since its integral multiplication matrix has
a monic characteristic polynomial annihilating it (apply Cayley--Hamilton
to 1). Hence this is indeed an order, in agreement with the cited theorem.
Ring closure is distinguished from integral closedness/maximality.

**Complete trace form.** Let M_i have column j equal to (c_ijk)_k.
It represents multiplication by b_i on K. The producer first forms
τ_i=tr(M_i), then G_ij=Σ_k c_ijk τ_k. Independently, the verifier constructs
each G_ij as tr(M_i M_j), summing all 48² matrix-composition terms for
each of the 2304 entries, and compares every saved basis trace and entry.
The product identities imply M_i M_j represents b_i b_j, so both
constructions give Tr_(K/Q)(b_i b_j). No numerical root approximation
or selected field embedding is used.

**Two exact determinants.** The complete 48-by-48 G is evaluated by
integer Bareiss elimination with exact divisions. Independently of this
trace construction, the producer builds the full 95-by-95 Sylvester
matrix of H and H′ (47 shifted descending H rows followed by 48 shifted
descending H′ rows) and computes its determinant R. This is Res(H,H′).
The standard discriminant--resultant identity gives

\[
\operatorname{disc}(H)
 =(-1)^{48\cdot47/2}\operatorname{Res}(H,H')/343=R/343.
\]

Both saved matrices and every elimination witness are reconstructed by
the independent verifier, using its own column-major update and exact
integer arithmetic. It checks all 47 trace-elimination steps with
35720 exact divisions and all 94 resultant-elimination steps with
281295 exact divisions, including every pivot choice, swap sign, full
stage hash and terminal determinant. It verifies R is divisible by 343
and R/343=det(G)≠0, as signed integers; it checks every field of the
discriminant record. These are complete exact elimination replays,
rather than modular agreement or an unchecked determinant label.
As an additional explanation of the cited formula, det(basis-to-power)
=343⁴⁷ gives disc(O_H)=343⁹⁴ disc(h)=disc(H); this does not replace
either finite determinant computation.

**Bounded evidence and scope.** One producer took 5.6045 seconds
internally (5.7135 externally); one replay took 7.9672 seconds internally
(8.0377 externally), each below 180/181 seconds respectively. The replay
reports 48/48 basis elements, 110592/110592 product slots and 2304/2304
trace entries, with both discriminants equal and no failures. The stage
outputs, scripts and reports occupy less than 3.2 MB against the fixed
134217728-byte cap. No stage was resumed, retried or enlarged. All
upstream files are read-only. Commands from the notebook directory are
shown for reproducibility; the one-shot runner deliberately refuses to
overwrite its existing outputs:

```bash
python3 -B scripts/seven-torsion/nonmonic-order-283/run_stage.py build_order
python3 -B scripts/seven-torsion/nonmonic-order-283/run_stage.py verify_order
```

`producer-report.json`, `verification-report.json` and both watchdog
reports give the actual counts and limits. The original coefficient and
transport evidence remains in L067's unchanged certificate. This result
is only a starting-order prerequisite for future arithmetic, not a
maximal-order certificate or a BSD candidate.

**Separate critical audit (2026-10-17, step 285).** The complete proof,
producer and verifier were reviewed under the unchanged Section 2 and
Proposition 4 source assessment. The hypotheses are Z Dedekind, primitive
irreducible H of degree 48, and nonzero leading coefficient 343. Audited
L067 supplies irreducibility and the full field identification; the new
run checks its certificate hash against the earlier audit and replays all
4852 upstream checks. Separability follows in characteristic zero. The
basis starts with 1, and the other diagonal entries of the power-basis
change are 343, so the determinant factor is squared, namely 343^94.
No integrality of t, residual-surjectivity hypothesis or maximality input
has entered.

All order evidence is copied byte-for-byte into a fresh directory before
running the unchanged independent verifier. It checks every basis vector,
both inverse matrices and both original-coordinate transports, every one
of the 110592 product slots, both identity actions, and all 2304 trace
entries. The trace-composition indices are consistent: if column j of
M_i is (c_ijk)_k, then the sum used is
sum_(k,l) c_ikl c_jlk=tr(M_i M_j). Polynomial divisibility by the entire H
proves each product identity in the field. These complete identities
justify the lattice and trace form.

The full original Bareiss chains pass all 35720 and 281295 exact divisions,
including every pivot, row swap, stage and terminal sign. The review also
checks that the column-major replay retains the original pivot column
before updating entries; it does not accidentally use overwritten values.
The square Sylvester matrix has 47 shifted descending H rows followed by
48 shifted descending H' rows. It therefore computes Res(H,H'); the
discriminant sign exponent is 48*47/2=1128, which is even.

To guard against a common Bareiss error, the audit additionally evaluates
both complete matrices by primitive-row integer Gaussian elimination,
using no producer/verifier arithmetic. At pivot p=A_kk and entry u=A_ik,
put d=gcd(p,u)>0 and form the complete row

    r=(p/d) row_i-(u/d) row_k.

Divide r by the positive gcd g of all its entries. The new row is
integral, its prefix through column k is zero, and this operation
multiplies the determinant by p/(dg). Every such exact row, p,u,d,g,
pivot choice, swap, and final triangular matrix is retained. Skipped rows
have u=0 and require no operation. All pivots and row contents are nonzero
in the completed run. Multilinearity of the determinant gives the stated
multiplier, since the term with two equal rows vanishes. Thus, if q is
the product of these nonzero rational multipliers and s is the product
of row-swap signs, the original determinant equals

    s * product(final diagonal entries) / q.

The program computes that rational number exactly and checks that its
denominator is one. This supplies a complete second determinant argument,
without Bareiss's previous-pivot division or modular sampling. It processes
all 48 trace and 95 Sylvester pivot columns. Both signed answers equal
the original stored integers, with R=343*det(G), det(G)<0 and 6870 digits
in abs(det(G)). Negativity is retained; no absolute-value discriminant
or field-discriminant interpretation is substituted.

The complete fresh evidence, full row operations, matrices and reports
are in `scripts/seven-torsion/order-audit-285/`. The aggregate internal
time is 10.213518292061053 seconds against 180; external time is
10.340186832938343 against 181. All new artifacts occupy 9080092 bytes
against 134217728. All 65 inventoried original files have matching
before/after hashes, and every failure list is empty. No stage was
retried, resumed or split after execution. Reproduction uses the
one-shot command (which refuses existing output):

```bash
python3 -B scripts/seven-torsion/order-audit-285/run_stage.py
```

This establishes only the audited fixed starting-order certificate. It
does not provide index primes, local or global maximality, the field
discriminant, complete units/classes or a Selmer/rank assertion. The
general theorem and finite methods are known; no progress beyond the
inspected source theorems is claimed.

## Mathlib

Full matching Mathlib coverage of this nonmonic order construction,
the fixed tables, and the resultant certificate was not checked.
Supporting coverage was not checked either; no absence is inferred.
The primary theorem supplies the general input; these standard-library
Python computations are exact instance evidence, not Lean formalization.
