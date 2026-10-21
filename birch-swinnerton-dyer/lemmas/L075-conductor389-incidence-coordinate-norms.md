# L075 — Two full incidence coordinate norms

## Hypotheses

Use the audited entire incidence algebra of L074 for the short model
Y²=X³−3024X+46224 of y²+y=x³+x²−2x at seven. Retain its full presentations
D=Q[Z]/h, L=D[T]/k, B=L[V]/(V²−c′(T)) and I=B[X]/F, with
F=N−Tq² monic of degree seven. All coefficient inputs, y-factor y_f,
projection pullbacks and basis transports are those certified in L074,
including its successful step-271 audit. The point-coordinate images are
X and Y=Vy_f, and the original coordinates are (X−12)/36 and Vy_f/216−1/2.

Use the ordered B-basis (1,X,…,X⁶) of I and rational coefficient order
ZʲTⁱVᵉ, j fastest, 0≤j<8, 0≤i<3, 0≤e<2. Thus a B entry always has
48 rational coordinates. Neither B nor I is assumed to be a field.
No L026, residual-image, unit/class, Selmer or analytic hypothesis is used.

## Conclusion

Both full multiplication operators μ_X, μ_Y on I over B are explicitly
certified, including all 98 B-valued entries (4704 rational slots).
Their determinant norms are

\[
N_{I/B}(X)=n_0(Z)+Tn_1(Z),\qquad
N_{I/B}(Y)=Vn_y(Z),
\]

with the following complete coefficient table. The entry in row j is
the coefficient of Zʲ; all unlisted T,V components are zero.

| j | n₀ | n₁ | nᵧ |
|---|---|---|---|
| 0 | −1701398502827606016/2048947 | −950047151493841920/100398403 | −1292048201778906519429120/702788821 |
| 1 | 77813244453758976/2048947 | 34602064230783744/100398403 | 45471271405184575478784/702788821 |
| 2 | −1605013091458560/2048947 | −644811510453120/100398403 | −903793137186176308224/702788821 |
| 3 | 811353977856/2048947 | 2063857332816/14342629 | 2191310295421475520/100398403 |
| 4 | −1322561088/2048947 | −397537461816/702788821 | −420898496838717600/4919521747 |
| 5 | −74571144/2048947 | 731878288/301195209 | 233253912285936/702788821 |
| 6 | 1004088/14342629 | −57247/258167322 | −639000576/100398403 |
| 7 | 3817/6146841 | −184162729/19127100552336 | −193468056687/137746608916 |

All full matrices and both 48-coordinate norms are in
`scripts/seven-torsion/coordinate-norm-273/coordinate-matrices.json` and
`coordinate-norms.json` in that same directory. This fixed known-algorithm
specialization passes complete independent replay and the separate critical
audit below. Two coordinate tests do not certify
norms of arbitrary power classes, descent conditions or any Selmer bound.

## Proof

**Imported norm and determinant results.** The invocation-start SPECIALIZE
assessment is
`drafts/literature/2026-10-17-incidence-coordinate-norm-certificate.md`.
[Stacks Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)
defines the finite-locally-free norm by the determinant of multiplication,
independent of basis and compatible with base change. L074 supplies a global
free basis of rank seven over the entire B, so its hypotheses hold on
Spec(I)→Spec(B). This applies to every element; unit status is not needed
for computing the norm and is not asserted here.

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
356 (2004), 1209–1231, DOI 10.1090/S0002-9947-03-03366-X,
[author long version, 13 June 2001, Proposition 7.10 and preceding incidence proof/following matrix paragraph, printed p.19](https://www.mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf#page=19),
identifies the incidence map as point pullback followed by norm along the
line projection. Q and the odd prime seven meet its stated setup, and its
Section 3 allows products of fields. L074 supplies this exact projection,
not an unidentified seven-dimensional algebra. Its inverse ordinary-functional
indexing and Cartier conventions remain unchanged. This citation identifies
the geometric meaning of the computed norm; it supplies no arithmetic
descent certificate from these two elements.

The producer imports ordered cofactor expansion over a commutative ring,
as in
[Mathlib Matrix.det_succ_row_zero and Matrix.det_fin_zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_succ_row_zero).
It makes no division by a matrix entry. Its cache stores minors with
inherited column order and remaining rows r,…,6, r=7−number of columns.
For the j-th remaining column it uses sign (−1)ʲ; the empty minor is one.
Zero summands can be skipped without changing this expansion.

The independent verifier imports Christian Bär,
[*The Faddeev–LeVerrier algorithm and the Pfaffian*, arXiv:2008.04247v3](https://arxiv.org/pdf/2008.04247v3#page=3),
PDF dated 6 August 2021, Section 2.1, pp.3–4, equations (1)–(6)
(published Linear Algebra Appl. 630 (2021), 39–55).
For a commutative Q-algebra and a 7-by-7 matrix A, it uses
N₁=Id, cₖ=−tr(ANₖ)/k and Nₖ₊₁=ANₖ+cₖId. The characteristic polynomial
has coefficients c₀=1,c₁,…,c₇, its constant coefficient is −det(A), and
N₈=0. Here the base is the entire B; division only by k=1,…,7 is allowed
in this Q-algebra, even if it has zero divisors. No general norm or
characteristic-polynomial theorem is reproved.

**Exact fixed specialization.** Each program reconstructs h,k,c′ from the
accepted input coefficients and F=N−Tq² from the full N,q polynomials.
The producer uses sparse convolution and monic reduction in D,L,E₀=L[X]/F,
and a full quadratic pair over L for B. The verifier uses separately
implemented fixed-length Horner shifts in dimensions eight, three and seven,
and the full even/odd V pair. It imports no producer or earlier notebook
arithmetic; its only shared module handles I/O, time and file preservation.
Both methods compute rational normal forms, without evaluating an embedding.

The verifier reconstructs y_f=q³M⁻¹ from the audited full M-inverse input,
checks MM⁻¹=1, and compares every y-factor coefficient to L074 and the
producer. It checks c′y_f²=X³−3024X+46224 over the entire E₀. Accepted
L074 supplies the geometric identification, quotient fibers and full
projection maps; no earlier construction or audit is repeated as a claim.

For each coordinate α=X,Y, column r is the complete normal form of αXʳ,
0≤r≤6. For Y the odd part is retained explicitly. The two programs
independently form every column and compare all 4704 rational coefficients.
The shape requirement is two 7-by-7 matrices, with exactly 48 coefficients
per entry, including zeros. Thus these are the multiplication operators on
the proved B-basis, not samples of their actions or a selected fiber.

The producer rechecks all 48 standard point columns and both entire
source-basis transports. The verifier independently computes all 48 standard
columns and all 48 direct Y-power columns in E₀⊕VE₀, with V²=c′, then
checks both full 48-by-48 rational transports. Each compares to all L074
map coordinates, retaining the full 336-dimensional target. Both original
coordinate changes are compared in every coordinate; the verifier also
checks all 48 line inclusions and all 336 flatten/unflatten basis round trips.
The full arrays are retained in `construction-transports.json` and
`verification-transports.json`, respectively.

Laplace expansion produces both complete norms and its computed ordered
minors in `laplace-X.json` and `laplace-Y.json`. Independent reconstruction
then feeds the two full matrices to Bär's recurrence. For each coordinate,
`faddeev-<coordinate>-k.json`, k=1,…,7, saves the entire Nₖ, ANₖ, trace,
cₖ and Nₖ₊₁; the corresponding `faddeev-<coordinate>-result.json` saves
all eight characteristic coefficients, the full norm and the entire zero
terminal matrix. Every one of the 48 coefficients of each determinant is
compared against both the Laplace output and the saved norm. The terminal
zero alone is not used as a determinant certificate. These exact normal
forms give the table in the conclusion.

The scalar controls repeat both determinant algorithms for 0·Id and 2·Id,
giving 0 and 2⁷=128 in the constant B coordinate, with all other coordinates
zero. All control recurrence matrices are retained too. Complete saved-data
inspection reads all 4704 matrix slots, both 48-coordinate norms and all
28 recurrence records, checking their shapes, full coefficient-record
agreement, successive N-record agreement and all four full zero terminal
matrices. This is recorded in `complete-evidence-inspection.json`; it is
inspection of completed certificates, not another arithmetic execution.

**Bounded execution, rejection scopes and preservation.** Each stage ran once:

```bash
python3 -B scripts/seven-torsion/coordinate-norm-273/run_stage.py build_norms
python3 -B scripts/seven-torsion/coordinate-norm-273/run_stage.py verify_norms
```

The fixed stage limit was 180 seconds each, external watchdog 181 seconds
each, and combined directory bound 134217728 bytes. Construction took
10.427161374944262 seconds internally, 10.549155790940858 externally;
verification took 27.820701541029848 internally, 27.91460833302699 externally.
Neither watchdog fired. After complete evidence inspection the directory
contains fewer than 5.8 million bytes, below the cap. No stage was retried,
subdivided or extended. Both reports have empty failure lists.

Three deliberately limited altered-data tests reject: changing one matrix
coefficient fails `full_matrix_coefficient_comparison`; changing one saved
norm coefficient fails `full_determinant_coefficient_comparison`; removing
the odd-V coefficient block fails `full_48_coefficient_basis_shape`. Full
mutated inputs and `rejections.json` retain these scopes, each explicitly
with `full_malformed_replay: false`. Missing a basis block is not selecting
a geometric sign. The tests supplement the full successful original replay.

The pre-execution 404-file inventory includes and matches every entry of
the successful 379-file step-271 inventory, all incidence-268/269 evidence,
and all stopped/failed upstream evidence. Both stages verify every original
hash with no changed or missing file. L069 and stopped incidence columns
are excluded from the mathematical inputs.

This completes only the two approved coordinate tests by known algorithms.
It does not certify arbitrary-input norms or their power-class compatibility,
global units/classes, descent functions, local bounds, Selmer containment,
other L026 premises, successful localization, rational membership,
divisible-Sha removal or arbitrary-curve complex-order/rank comparison.
No progress beyond the sources checked or BSD candidate is asserted.
The separate critical review below validates this fixed certificate assembly.

**Separate critical audit (2026-10-17, step 275).** The unchanged
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-17-incidence-coordinate-norm-critical-audit.md`.
The entire proof, producer, independent verifier and I/O/wrapper code were
read. Accept L074's audited geometry and all its stated inputs; no upstream
arithmetic construction, L069 or stopped column computation was resumed.
No source-hypothesis or arithmetic defect was found.

The single audit command was

```bash
python3 -B scripts/seven-torsion/coordinate-norm-audit-275/run_stage.py
```

The fresh sibling directory holds byte-identical verifier and I/O copies,
with ten source/copy hashes in `input-inventory.json`. Required construction
inputs are copied there; upstream paths still reference the originals.
The copied construction report is provenance, not a new construction.
The wrapper executes the copied verifier exactly once in-process and retains
its arithmetic namespace. Runtime overrides affect only start/finish timing,
output tracking and the final exit: one alarm covers the whole audit and is
not reset by the verifier. No arithmetic code is patched and the producer
is not run. Exclusive output creation prevents overwriting original records.

The fresh complete replay passes in 27.802622125018388 seconds. It reconstructs
the whole B and I and y_f, all 4704 matrix coordinates, both point bases and
both full source transports, both original-model coordinates, every line
inclusion and all 336 rational basis round trips. Its Horner shift replaces
the top power by the negative monic-modulus coefficients; coefficientwise
addition and successive shifts therefore compute the full normal form.
The explicit quadratic pair retains both V components. These reviewed
operations require neither fieldness nor division by a matrix entry.

`complete-output-comparisons.json` compares all 40 fresh output objects
against their saved counterparts, in full. This includes all 28 recurrence
records with N_k, AN_k, trace, c_k and N_(k+1), all four characteristic
coefficient arrays and terminal matrices, every matrix and transport entry,
scalar controls, the three complete altered fixtures and their rejection
records. Only `seconds`, `preserved_files` and `changed_or_missing` in the
verification report are excluded from equality because the audit has a new
time and a larger inventory; its own preservation test independently requires
an empty changed/missing list. No coefficient or mathematical check is omitted.
The complete incidence-269 and successful incidence-audit-271 replay evidence
also agree. All five transport arrays match those and the latter audit's
dense evidence, both F and y_f match in full normal form, and all retained
upstream residual coefficients are zero. These are checks of accepted input
evidence, not a repeat of its upstream construction.

The audit separately checks each saved Laplace certificate using the fresh
verifier's B arithmetic, without importing producer arithmetic. Starting with
the ordered root columns (0,...,6), it derives the entire reachable key set
by following every nonzero matrix-entry branch. Each key retains increasing
column order and row 7−length. A bottom-up pass checks the full signed sum
of its child minors with sign (−1)^j at position j. The empty minor is checked
as one separately, including all 48 coefficients; branches skipped for zero
matrix entries contribute zero even if other entries are zero divisors.
Exact equality of saved and reachable key sets rejects missing and surplus
records. The counts are 7 for X, 127 for Y, 1 for the zero scalar matrix and
7 for twice the identity. Full values and signed terms for every checked
minor are saved in `checked-laplace-<label>.json` in the audit directory.
Every root agrees coefficientwise with the saved Laplace norm, the fresh
Faddeev determinant and the stored coordinate/control norm. For the zero
matrix only the root is reachable through nonzero branches; this is sufficient
and does not omit a nonzero contribution.

The recurrence review checks matrix orientation, N_1=Id, the trace sign,
division by the rational integer k, and the final det(A)=−c_7 convention.
All intermediate matrices are recomputed in the fresh replay and compared,
rather than inferring the characteristic polynomial from terminal zero alone.
The independent cofactor checks above additionally validate the full determinant.
The scalar controls keep rank seven, giving zero and 128 with all other
coefficients zero. The audit parses all eight rows of the conclusion's table
and checks every one of its 96 rational slots, including every unlisted zero;
`canonical-table-check.json` retains the full comparison vectors. The recorded
lemma hash identifies the pre-audit table source; the table itself is unchanged.

All three original condition-only rejection fixtures are reproduced exactly:
changed matrix coefficient, changed norm coefficient and omitted odd-V block.
Their intended conditions and `full_malformed_replay: false` flags agree.
These tests do not claim full malformed-certificate replay, and a missing
odd-V block is basis loss, not selection of one geometric sign.

The total internal stage takes 30.236730000004172 seconds against 180;
the external watchdog takes 30.3722816669615 seconds against 181 and does not
fire. The entire new directory, including all input copies, logs and the final
watchdog report, contains 7184458 bytes against 134217728. There is no retry,
cap extension or subdivision. `audit-preservation.json` checks all 464 original
files with no changed or missing path: the complete 404-file inventory, the
matched prior 379-file inventory, all incidence-268/269 files, and every file
of coordinate-norm-273 are retained. Failed/stopped evidence remains intact.

This is an ADVANCE in local certificate reliability, using known algorithms,
not a result beyond the sources checked. It validates exactly the two full
coordinate norms. No arbitrary-unit or seventh-power-class norm certificate,
descent function, complete units/classes, local bound, Selmer containment,
successful localization, rational membership, divisible-Sha removal or
arbitrary-curve rank comparison follows. Mathematical hypotheses and direct
inputs are unchanged; this audit adds no lemma or DAG edge.

## Mathlib

[Algebra.norm_eq_matrix_det](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Norm/Defs.html#Algebra.norm_eq_matrix_det)
matches the generic norm statement for a finite basis over a commutative
base ring; `Algebra.norm_algebraMap_of_basis` gives the scalar convention.
The determinant expansion results cited above support the producer.
The exact fixed algebras, coefficient table, projection transports and
independent replay have not been checked for full matching Mathlib coverage.
Unknown coverage is not absence; this certificate is not a Lean proof.
