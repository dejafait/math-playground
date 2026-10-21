# L078 — One strict 31-overorder from the full radical action

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h, audited L077's
nonmonic order O=O_H, H=343h primitive of degree 48, and all original
basis, inverse, transport and multiplication data. Write its ordered
Z-basis as (b_0,...,b_47), with b_0=1. Use audited C077a's fixed prime
31 and full homogeneous gcd with affine representative G=T²+24.
No other index prime, L026 premise, selected field factor, cross-notebook
result or stopped step-293 power evidence is assumed.

All new exact evidence is in `scripts/seven-torsion/radical-overorder-295/`.
The unchanged original inputs are recorded in `input-hashes.json`.

## Conclusion

There is a strict order O' containing O in the entire K, with

\[
 I=\sqrt{31O},\qquad O'=(I:I),\qquad [O':O]=31^2=961.
\]

In O-coordinates define r_0 to have zero odd entries and even entries
(from positions 0 through 46)

    1,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28,4,5,14;

define r_1 to have zero even entries and odd entries (positions 1 through 47)

    1,9,19,16,20,25,8,10,28,4,5,14,2,18,7,1,9,19,16,20,25,8,10,28.

An explicit Z-basis of O' is

\[
 m_0=\frac1{31}\sum_{k=0}^{47}(r_0)_k b_k,\quad
 m_1=\frac1{31}\sum_{k=0}^{47}(r_1)_k b_k,\quad
 m_i=b_i\quad(2\le i\le47).
\]

This is also the known nonmonic source lattice
O+(1/31)B^46 U(t), where B has O-basis (343b_0,b_1,...,b_47),
and `source.json` retains every coefficient of the degree-46 lift U
with leading coefficient 2 and G Ubar=Hbar modulo 31. No ideal power
is expanded or imported from the stopped execution.

Complete independent replay verifies the two full kernels, both integral
preimage lattices, both inverse transports and every new product. This
is fixed known-method reproduction; its separate critical audit passes.
It asserts neither 31-maximality nor global maximality, a field
discriminant, complete units/classes, a descent/Selmer bound, successful
localization, rational membership or a BSD rank comparison.

## Proof

**Imported results and exact specialization.** Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications 44 (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27),
especially Proposition 9.3 and its following full action/kernel/lifting
paragraph on p.235, supplies the following construction. For an order O
in a number field and a rational prime p, the radical I of pO is the
inverse image of the kernel of an iterated Frobenius on O/pO with
p^k>dim_Fp(O/pO). The multiplier order is

\[
 (I:I)=p^{-1}N,\qquad
 N=\ker\bigl(O\longrightarrow\operatorname{End}_{\mathbf F_p}(I/pI)\bigr),
 \qquad pO\subseteq N\subseteq O.
\]

Lifts of the entire kernel modulo pO, together with pO, generate N;
division by p gives the enlarged order. The finite-module integrality
criterion and strictness in the non-p-maximal case are included in the
cited results. These statements, including the full quotient I/pI, are
imported, rather than reproved from a dimension count.

L067 supplies the number field, L077 supplies the exact order O, and
C077a supplies non-31-maximality. Here dim_F31(O/31O)=48 and 31²=961>48,
so two Frobenius iterates suffice. The input is the entire field and the
nonmonic order; t is not assumed integral.

Del Corso–Dvornicich–Simon, *Decomposition of primes in non-maximal
orders*, Acta Arith. 120 (2005), 231–244, DOI 10.4064/aa120-3-2,
[Section 2, Proposition 9 and Theorem 2(ii), pp.238–240](https://www.impan.pl/shop/en/publication/transaction/download/product/82018),
identifies this same (I:I) with O+(1/31)B^(48-g)U(t), of index 31^g,
where g is the degree of the full homogeneous gcd and U lifts Hbar/G.
The hypotheses are a Dedekind base ring, primitive irreducible H with
nonzero leading coefficient, and precisely its nonmonic order R_H.
They hold over Z by L067/L077. C077a gives g=2, degrees 46,2,48 for
the original homogeneous lifts and top units modulo 31; hence there
is no infinity factor. The certificate verifies all 49 coefficients
of G Ubar=Hbar and deg U=46. The two imported descriptions of the same
multiplier order identify the source lattice after the full kernels and
preimages below pass. No equality follows from dimension two alone.

**Original field arithmetic.** Each program checks all original H
coefficients, H=343h, content one, the cited 48 basis polynomials,
both complete rational basis inverses and both transports to L067.
The producer reconstructs all 110592 original product coefficients by
integer polynomial multiplication and reduction by original H followed
by triangular conversion. The independent replay instead tests
b_i b_j−sum_k c_ijk b_k for divisibility by H for all 2304 ordered
pairs, with every division exact and every remainder coefficient zero.
It retains all integer coefficient slots, including zeros, and both
identity actions. Thus the arithmetic used is identified in K, rather
than an unchecked abstract table. Audited L067's fieldness and the
published source hypotheses remain the mathematical starting inputs.

**Full Frobenius kernel.** `frobenius.json` contains both full 48-by-48
Frobenius matrices F and F² and the entire elimination certificate for
F². The producer computes b_i^31 by the original multiplication table.
Its numpy int64 operations take residues in [0,30]; each bilinear
contraction has at most 2304 summands, each at most 30³, so there is
no machine-integer overflow. The replay uses only Python exact integers
and rational numbers. It independently powers each basis polynomial
twice modulo H over F31 and converts through the original inverse
basis matrix, whose denominators are checked invertible modulo 31.
Every coefficient of both F and F² agrees.

Every saved finite-field row operation is replayed. Swaps are invertible,
scalings are by nonzero residues and row additions have distinct source
and destination. The entire terminal matrix equals the saved RREF;
all 46 pivot columns, leading ones and every remaining zero row are
checked. The complete free-variable construction supplies two kernel
vectors, whose membership is also checked against every original row.
This proves rank 46 and the full kernel, not merely two nilpotent
elements. The cited exponent criterion identifies its inverse image
with I. Its canonical row-reduced kernel basis is exactly (r_0,r_1).

**Exact integral radical preimage.** In `radical-lattice.json`, S_I
is the 48-by-50 matrix of those two integer lifts and all 48 columns
31e_i. The selected columns give

\[
 J=(r_0\ r_1\ 31e_2\ \cdots\ 31e_{47}).
\]

The certificate includes integer matrices C_I of size 50-by-48 and
D_I of size 48-by-50, and the complete rational J inverse. The replay
checks all entries and the exact identities

\[
 J=S_I C_I,\qquad S_I=J D_I,\qquad JJ^{-1}=J^{-1}J=1.
\]

The first two identities prove equality of the generated Z-lattices
in both directions; the inverse proves full rank. The preceding
finite-field reduction is itself fully replayed and retains the same
kernel. Thus J Z^48=I with an actual global integral basis, without
a local-only basis or a normal-form label standing in for generation.

**The entire action on I/31I.** For each old b_i, `action-ii.json`
stores its 48-by-48 integral multiplication matrix A_i in the J-basis.
The producer reconstructs W_i=multiplication_by_b_i times J using the
complete original table and solves J A_i=W_i over Z, checking every
coefficient before reduction. The replay independently checks all 2304
identities b_i (sum_l J_lj b_l)=sum_k (J A_i)_kj b_k by polynomial
divisibility in original H. This covers every one of the 110592 integer
action slots, including zeros, before reduction modulo 31.

Stack the complete operators as a 2304-by-48 matrix with row (j,k)
and column i equal to (A_i)_kj modulo 31. This is exactly the map
O/31O -> End_F31(I/31I) in the cited theorem. The action is not on
the image I/31O. `action-kernel.json` retains every coefficient, every
invertible row operation, all pivots and the entire terminal RREF.
The replay reconstructs the full stack from the verified integral
operators. The same complete elimination checks give rank 46 and
kernel dimension two. Canonical reduction again gives (r_0,r_1).
Across both main eliminations and the two kernel reductions, all 48715
recorded row operations are replayed, with no omitted trailing rows.

**Exact numerator lattice and overorder.** `numerator-lattice.json`
gives S_N consisting of the entire action-kernel lifts and 31e_i, with
full integer C_N,D_N and a rational inverse for its basis Q. The replay
checks Q=S_N C_N and S_N=Q D_N and both inverse identities, exactly
as for I. Hence Q Z^48=N, the full integral action preimage. In this
instance Q=J; this is a computed equality, not a source assumption.
The imported lifting theorem now gives O'=M Z^48 for M=Q/31 and
identifies it with (I:I) and the nonmonic source lattice stated above.

`basis.json` retains M, its full inverse C, all entries of 31M=Q and
both complete L067 transports. Every entry of C is an integer, and
MC=CM=1. Consequently every old basis element belongs to O'; in
particular 1 does. The full C is lower triangular, with diagonal
(31,31,1,...,1). The replay checks every entry above the diagonal is
zero and evaluates the entire diagonal product, giving det C=961.
This proves the index of the old lattice inside the new one, and
strictness, independently of the source's predicted index. Both
L067 transports equal their complete matrix compositions with M,C,
and both new composite inverse identities hold.

**Every new product in K.** All 48 files `product-00.json` through
`product-47.json` retain the complete ordered product table in the
m-basis. If V_i is the original integral polynomial representing
31m_i and c_ijk are the claimed integral coefficients, the independent
replay checks the full polynomial

\[
 V_i V_j-31\sum_k c_{ijk}V_k
\]

for exact divisibility by original H. All 2304 remainders vanish, and
all 110592 coefficient slots are integers. This proves closure on the
entire Z-lattice, independently of a producer integrality claim. The
lattice contains 1 and spans K, so it is indeed an order, consistent
with the imported multiplier-order theorem.

**Bounded execution and limitations.** The one producer takes
1.558305 seconds internally and 1.837445 externally; the one replay
takes 1.340107 internally and 1.422083 externally, below 180/181
seconds per stage. Reports show full actual/required slot coverage,
ranks 46, kernel dimensions two, index 961 and no failures. After
metadata consolidation the entire new directory is 9430944 bytes,
below 134217728. All 72 inventoried original files have identical
before/after hashes in both stages. They include the original L067
certificate and the starting-order/residual-prime evidence; no stopped
step-293 file is read. Preservation hashes supplement full arithmetic
checks, rather than replacing them. No retry, resumption, larger cap,
second prime or second enlargement occurs. Reproduction commands
below are one-shot and refuse to overwrite existing evidence:

```bash
python3 -B scripts/seven-torsion/radical-overorder-295/run_stage.py produce
python3 -B scripts/seven-torsion/radical-overorder-295/run_stage.py verify
```

The scripts, full certificates, `producer-report.json`,
`verification-report.json`, both watchdog reports and `summary.json`
are retained. The production check and separate critical
audit of this assembly are complete. No computation of a
maximal order, global unit/class group or BSD input follows from a
single strict correction. There is no claimed progress beyond the
checked general source theorems, and no complete BSD candidate.

**Separate critical audit (completed 2026-10-18, step 297).** The full
proof, producer and independent verifier were reviewed under the unchanged
approved source assessment. The original degree-48 field, primitive
nonmonic H, order basis and homogeneous degrees/top units match the
imported theorems above. The leading unit 343 modulo 31 makes reduction
through the rational power-basis inverse valid; it does not assert that
t is globally integral. The 961>48 radical threshold, full action on
I/31I and two global integral preimages are essential to identifying
(I:I). This also identifies the source lattice with B^46 U by the
imported Theorem 2(ii); no equality is inferred merely from the index.

The fresh evidence is in `scripts/seven-torsion/radical-overorder-audit-297/`.
All 104 copied verifier/certificate files are byte-identical to their
step-295 originals. The directory has the same depth, so even the
verifier's input paths are unchanged. Its fresh complete replay checks
all 110592 old-product slots, 110592 integral action slots and 110592
new-product slots, all 48715 finite-field row operations, both entire
kernel/preimage certificates and both full transports. It gives rank
46 for each kernel matrix, rank 48 for both lattices and exact index
961, with zero failures. Every new-product identity retains its factor
31. All 186 inventoried original files, comprising the 114 step-295
files and its 72 upstream inputs, have identical before/after hashes.

The independent supplement constructs the displayed r_0,r_1 directly
from the statement, and compares every entry of both bases J=Q and
their generator matrices. In the block split 2+46, put R=(r_0,r_1)
restricted to the last 46 coordinates. Then the explicit checked
matrices are

\[
 J=Q=\begin{pmatrix}1_2&0\\R&31\,1_{46}\end{pmatrix},\quad
 M=J/31,\quad C=\begin{pmatrix}31\,1_2&0\\-R&1_{46}\end{pmatrix}.
\]

For S=(r_0,r_1,31e_0,...,31e_47), the forward generator matrix selects
columns 0,1,4,...,49 and the reverse generator matrix is (e_0,e_1,C).
The supplement independently verifies both full integer identities
S C_I=J and J D_I=S for each preimage, and J(C/31)=(C/31)J=1.
It matches all saved inverse coefficients, verifies MC=CM=1 and checks
every entry above the diagonal of C and its diagonal (31,31,1,...,1).
Thus the full old-order inclusion and its determinant 961 are checked
with the correct column convention, rather than a transposed inclusion.

For a further rank check, streaming row reduction of each actual matrix,
without reading its saved operation sequence, selects 46 original rows.
On the saved 46 pivot columns these yield nonsingular 46-by-46 minors.
Fresh modular elimination, including every swap sign and pivot, gives
determinants 16 for Frobenius squared and 1 for the full action, modulo
31. Both complete displayed vectors annihilate every row of each actual
matrix, and their first two coordinates are (1,0),(0,1). The nonzero
minors give rank at least 46; these two independent kernel vectors give
rank at most 46. This independently proves kernel completeness.
The selected original rows/columns, entire minors, elimination steps,
terminal matrices and vectors are saved in `frobenius-minor.json` and
`action-minor.json`. All direct basis/generator data are saved in
`independent-basis.json`.

The producer's integer contraction bound is explicitly 48²*30³=62208000
<2^63; every operand is reduced before the next contraction. Independent
replay uses exact polynomial Frobenius arithmetic and does not rely on
that machine calculation. The aggregate audit takes 1.723253 internal
and 1.840105 external seconds, below 180/181. Its evidence occupies less
than 9.6 MB, below 134217728 bytes; `audit-report.json`, `watchdog.json`
and `audit-preservation.json` retain the exact results and limits.
The one-shot reproduction command is:

```bash
python3 -B scripts/seven-torsion/radical-overorder-audit-297/run_stage.py
```

No altered-evidence fixtures were run in this audit, and none are claimed.
The stopped step-293 power evidence is neither read nor an input.
No second enlargement or maximality test occurs. This validates the
fixed known-method input under its audited dependencies; it establishes
no result beyond the cited general theorems and no BSD candidate.

## Mathlib

Complete matching Mathlib coverage for the radical/action lifting
construction, its nonmonic source identification and this fixed
certificate is not checked. Supporting coverage is not checked either;
no absence is inferred. This is exact finite instance evidence, not
Lean formalization.
