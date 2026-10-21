# L086 — Preserved full table of the index-four multiplier order

## Hypotheses

Use audited L067's entire degree-48 field K=Q[t]/h for
E: y²+y=x³+x²−2x, with primitive H=343h. Use L077's original
nonmonic basis b, L078's full order R with basis m, L080's identification
of R⁺, L084's complete table and transports for its basis
n_i=m_i (i<47), n_47=m_47/2, and audited L085's full multiplier
identification

\[
J=\sqrt{2R^+},\qquad S=(J:J)
=\sum_{i=0}^{45}\mathbf Z n_i+\mathbf Z(n_{46}/2)+\mathbf Z(n_{47}/2),
\qquad [S:R^+]=4.
\]

All these inputs retain the whole field and both original coordinates.
The fixed table bytes are step 329's `basis.json` and all 48
`product-00.json` through `product-47.json` in
`scripts/seven-torsion/index-four-table-329/`. They are untrusted inputs
to this replay; neither its producer status nor its failed zero-product
verifier is mathematical evidence. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-preserved-index-four-table-replay.md`.

## Conclusion

Put s_i=n_i for i<46 and s_i=n_i/2 for i=46,47.
The unchanged preserved files give the complete integral table

\[
s_i s_j=\sum_{k=0}^{47}c_{ijk}s_k \quad(0\le i,j\le47)
\]

of the entire order S. Every one of the 2304 ordered products and
110592 integer slots, including zeros, passes independent original-H
polynomial replay. All rational basis transports, their inverses, the
actual identity and its 96 left/right basis actions, and the full
integral inclusion of index four are checked.

This is fixed known-method reproduction. The single replay uses at
most 2.140810 seconds, below 180, and 12127696 bytes, below 134217728.
All 713 canonical inputs, 68 historical source files, 49 fixed copies
and three fresh Python source files are preserved. The separate step-333
critical audit below passes. No successor maximality, field
discriminant, complete units/classes, full descent enclosure, rational
membership or arbitrary complex-order/rank comparison is supplied.

## Proof

**Known multiplier input.** L085 supplies the full lattice S, not merely
a suborder of the multiplier. Its theorem input is Peter Stevenhagen,
*The arithmetic of number rings*, in *Algorithmic Number Theory*,
MSRI Publications **44** (2008), pp.209–266,
[Lemma 6.4 p.221 and Section 9 pp.233–235, equation (9-2),
Proposition 9.3 and the following action/kernel/lifting paragraph](https://library.slmath.org/books/Book44/files/08psh.pdf#page=27).
L067/L084 supply a full order in a number field; two is a nonunit and
J contains 2R⁺, so it is a nonzero full finite module. These are the
same hypotheses already checked in L085, without an odd-prime or
monogenic restriction. The cited general integrality/multiplier results
and that audited instance are imported. No new radical, stopping test
or reproof occurs here. The source theorem supplies no instance table
or resource guarantee; these are the finite obligations verified below.

**Complete identification of the lattice.** Matrices act on columns.
Let B₀ be L077's b-to-power matrix, A L078's m-to-b matrix, C=A⁻¹,
D=diag(1,…,1,1/2) (last entry only), and E=D⁻¹. The n-to-b matrix is
M=AD, with inverse C_n=EC. Put

\[
Z=\operatorname{diag}(1,\ldots,1,1/2,1/2),\qquad
T=Z^{-1}=\operatorname{diag}(1,\ldots,1,2,2).
\]

The proposed s-to-b and inverse matrices are B=MZ and B⁻¹=TC_n.
The power transports are G=B₀B and G⁻¹=B⁻¹B₀⁻¹. With P and P⁻¹
L067's original power/two-coordinate transports, the corresponding
pair is PG and G⁻¹P⁻¹.

The fresh `verify.py` imports no producer routine. It reconstructs
all 49 coefficients of H from L067/L077, verifying H=343h, degree 48,
content one and leading coefficient 343. It reconstructs every b_i
from the nonmonic formula and checks both full B₀ inverse products.
Both full P inverse products and original b-coordinate transports are
checked. A is reconstructed from the explicit even/odd columns in
L078 divided by 31, with all other columns unchanged; both inverse
products, its full numerator and both original-coordinate transports
are verified. It checks L080's complete D/E description and all six
L084 forward/reverse transport matrices, their inverses, scale and
actual identity, before identifying the input as R⁺.

The complete L085 decision agrees byte-for-data with its audited copy.
Every entry of its multiplier matrix Z, numerator 2Z, inverse T,
index and determinant agrees with the displayed matrices. Each of
the six supplied successor transport matrices equals the reconstructed
matrix above; all six inverse products are checked. The supplied
s-to-n matrix is Z, the old inclusion is T, and BT=M. Every off-diagonal
and diagonal entry of T is checked, giving |det T|=4. Hence the entire
old lattice is included and has exactly index four in this actual S.
There is no inference from an index label alone. The eight supplied
transport/inclusion matrices contain 18432 entries; the three transport
pairs and Z/T account for eight inverse-product checks.

The actual identity is u=TC_n e₀, not a presumed coordinate vector e₀.
All its entries are integral, it agrees with L085's saved identity,
and Gu=e₀ in the original power basis. The full rational invertibility
identifies the whole 48-dimensional vector space faithfully with K.

**All products independently in original H.** Let W_i(T)=31m_i(T).
The verifier reconstructs the entire integer polynomials 62n_i from
B₀M and compares them coefficientwise with L084. It then obtains W_i
by dividing 62n_i by two for i<47 and by one for i=47. Every quotient
is constructed as `Fraction(x, denominator)`, including integer zeros,
and is checked integral before conversion to int. No float or unchecked
truncation is used. Therefore the successor representatives are

\[
V_i(T)=124s_i(T)=
\begin{cases}
4W_i(T)&i<46,\\
2W_{46}(T)&i=46,\\
W_{47}(T)&i=47.
\end{cases}
\]

All coefficients agree with 124 times G and the fixed saved polynomials.
The metadata scales 31, 62, 124 and enlargement denominator two are
checked separately. The old factor 31 is retained throughout.

For every ordered (i,j), the verifier reads all 48 integers c_ijk and
constructs the full polynomial of degree at most 94

\[
F_{ij}(T)=V_i(T)V_j(T)-124\sum_k c_{ijk}V_k(T).
\]

Its convolution and expansion use original-H polynomials and do not
use the producer's table-rescaling formula. Full division in Q[T] by
H proceeds down degrees 94 through 48. For an integer leading value
x, `divmod(x,343)` permits an integer fast path only when the remainder
is zero; otherwise the quotient is explicitly Fraction(x,343).
Rational leading values likewise use exact Fraction reconstruction.
Every resulting coefficient in all 95 positions vanishes. This checks
218880 positions across all 2304 identities. No rational fallback is
needed for these particular data, but it is not assumed away.

For each product `division-ii.json` retains the complete 95-position
dividend, 47-position rational quotient and 95-position zero remainder.
Within the same watchdog, `stage.py` rereads all 2304 certificates,
checks every shape and integer dividend entry, and independently
multiplies each full quotient by H. The complete result equals the
saved dividend. Thus the persisted certificates, rather than only the
verifier's in-memory status, are checked. Dividing the proven congruence
by 124² establishes every displayed product in K.

All 110592 output coefficients are integers. Integral closure under
multiplication holds for the full lattice, and u is checked to act as
identity on both sides of all 48 basis vectors. The lattice has already
been identified with L085's entire S; an abstract associative table or
a selected field embedding is not substituted for it.

**Fixed-byte execution and preservation.** All fresh evidence is in
`scripts/seven-torsion/preserved-table-replay-331/`. The sole execution is

```bash
python3 -B scripts/seven-torsion/preserved-table-replay-331/run_once.py
```

The runner refuses an existing start marker and writes exclusively.
The external watchdog starts before generating the fresh mathematical
code, hashing or copying. The inspected exact replacements in the
stopped verifier repair rational reconstruction and create a new input
inventory; the old directory is never edited. The runner generates
`verify.py` and `stage.py`, copies only the 49 fixed basis/product inputs,
and executes the verifier once. No producer is imported or run.

`canonical-input-hashes.json` contains the unchanged 712 historical
canonical inputs plus the prior replay assessment. Every old canonical
hash still matches. `historical-source-hashes.json` separately records
all 65 step-329 files and three failure/preservation records.
`copy-manifest.json` names all sources, fixed untrusted copies and
hashes, distinguishing both inventories and `fresh-code-hashes.json`.
The historical input inventory and old reports are never reused as new
reports or altered. Final original, fixed-copy and source-code hashes
are checked in `preservation-stage.json`. The successful verifier also
records canonical preservation. Digests supplement the full arithmetic.

`verification-report.json` and `stage-report.json` pass with empty
failure lists and every required count. Internal replay takes 1.226269
seconds (rounded upward), and the encompassing stage 2.020029 seconds.
`watchdog.json` passes; through its write the run takes at most 2.140810
seconds and occupies 12127696 bytes. The byte count includes all code,
fixed copies, logs, full division certificates, hashes and final reports;
recursive accounting includes the preparation bytecode artifact too.
There is no excluded setup/copy or post-cap mathematical check.
No retry, malformed fixture, new correction or maximality test occurs.
The preserved failed execution and ATTEMPTS/041/042/044 remain intact.

The step establishes a usable fixed multiplication table by a known
method, without a new theorem beyond the assessed sources or any
resolution of the independent BSD gaps.

**Separate critical audit, 2026-10-19 (step 333).** The unchanged prior
SPECIALIZE assessment is
`drafts/literature/2026-10-18-preserved-index-four-table-critical-audit.md`.
The complete proof and repaired verifier/stage/watchdog were inspected,
along with the explicit L077/L078 bases, L084/L085 audit ranges and
ATTEMPTS/041/042/044. The cited Stevenhagen coverage and its hypotheses
are unchanged and reused; the audit does not reapply a maximality
criterion, produce a table, or repeat an order correction.

All fresh evidence is in
`scripts/seven-torsion/preserved-table-audit-333/`. Three setup source
files (`run_once.py`, `stage-template.py`, `independent-template.py`)
were prepared before watchdog start, disclosed in `run-start.json`
and included in recursive bytes. No mathematical check was executed
before the watchdog. It starts before fresh code copies, inventories,
fixed table copies and arithmetic. All writes are exclusive, and the
start marker prevents another invocation. The sole execution is

```bash
python3 -B scripts/seven-torsion/preserved-table-audit-333/run_once.py
```

The fresh `verify.py` is byte-identical to step 331's repaired verifier,
checked against that step's code inventory. All 49 fixed table copies
agree with both step 329 and step 331. No historical one-shot wrapper
or producer executes. The new original inventory includes all canonical
inputs plus every step-329/331 file, this lemma before this addendum,
the prior assessment and the preserved failure records: 897 distinct
originals. `copy-manifest.json`, `canonical-input-hashes.json`,
`code-hashes.json` and `audit-preservation.json` distinguish originals,
fixed copies and all six setup/generated source files. Every final
original, fixed-copy and code hash agrees. Preservation precedes this
canonical addendum.

Fresh full replay checks all 2304 ordered products, 110592 integer
slots, 218880 polynomial positions, 18432 transport/inclusion entries,
eight inverse products and 96 identity actions. All 2304 complete
division certificates are persisted. The new stage reconstructs every
95-position dividend from its actual fixed product row and the full
124-scaled polynomials, retaining every zero. It rereads all quotient
and remainder coefficients, checks their complete shapes and exact
integer dividends, and checks H times the quotient plus the zero
remainder equals the reconstructed dividend in every position. Thus
saved dividend labels alone are not accepted. H retains leading
coefficient 343. There are no failures or rational-division fallbacks;
the verifier still checks integer divisibility before its fast path.

The distinct `independent.py` imports no producer or verifier helpers
and uses no saved inverse as a solve input. It reconstructs B₀ directly
from H, A directly from the displayed even/odd L078 columns divided
by 31, and full power matrices F=B₀A for m, G for n (last F column
halved), and W for s (last two G columns halved). It uses unnormalized
exact rational forward elimination and back substitution, independently
of the replay's composition and saved-inverse checks. Its six systems are

\[
WX=[I\mid G\mid e_0],\quad GX_0=I,\quad JX_J=I,\quad
B_0X_b=W,\quad BY_b=I,\quad (PW)X_P=I,
\]

where X's blocks give U=W⁻¹, J (the actual old-to-new inclusion),
and u (the actual identity), B=X_b, and P is L067's full power-to-original
coordinate matrix; Y_b is the separately solved inverse of B. Every entry
of the six forward/reverse transports agrees with the saved data;
both full inverse products hold. Every entry of J is integral,
WJ=G, and its separately solved inverse agrees with both the saved
s-to-n matrix and L085's full multiplier matrix. The whole inclusion
agrees with L085's inverse. Exact pivot products with swap signs give
|det J|=4 and det G/det W=det J. Hence the audit reconstructs the entire
lattice and its index, rather than checking only a determinant label.

All entries of u are integral, agree with both saved identities, and
Wu=e₀. No order-coordinate e₀ is presumed to be the unit. All 6912
coefficients of 31m_i, 62n_i and 124s_i are reconstructed and checked
integral, with full equality to the saved n/s arrays and all metadata
scales 31/62/124. These checks retain the complete original field and
both original coordinate components.

`exact-lattice-certificate.json` persists the full reconstructed
matrices, all six system matrices and right sides, upper matrices,
transformed right sides, every reversible row operation, all nonzero
pivots, swap signs, solutions and determinants, plus full scaled
polynomials, inclusion/inverse and identity. Within the same cap the
supplement rereads the complete certificate, checks exact round-trip
equality, replays every row operation with its exact elimination factor,
checks every upper-triangular zero, pivot/sign and determinant, and
checks every full original and transformed system residual. Every
inverse system also receives the reverse inverse check. This is full
persisted evidence, not a preview or a hash-only validation.

`audit-report.json`, `independent-report.json` and `watchdog.json`
pass with no failures. The single execution takes 5.051671 seconds
(rounded upward) and occupies 15826777 bytes. The persisted
`final-bound.json` conservatively bounds the inclusive final writing
by 7 seconds and 15830752 bytes, strictly below 180 seconds and
134217728 bytes; the runner checks those bounds after writing it.
All setup/generated code, copies, logs, certificates, rereads and
preservation checks are included. No retry or altered-data fixture
occurs. The historical stops and unfinished work remain preserved.
This validates only the fixed known-method input: no global maximality,
complete units/classes, descent enclosure, rational membership or
arbitrary complex-order/rank comparison follows.

## Mathlib

Full matching and supporting Mathlib coverage for this explicit full
multiplier-order table and its certificates has not been checked.
Unknown availability is not evidence of absence. The cited multiplier
theory, audited inputs and exact finite replay are the mathematical inputs.
