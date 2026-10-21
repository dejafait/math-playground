# L097 — Free-pair shells-5–8 batch admits the unchanged common witness

## Hypotheses

Use L021–L023's n=1024, w=68, v=956, d=10 and
T=65537^28/2^128. Set K=floor(T). The source relaxation is over real
pair variables p_0,...,p_68 and real actual-orbit variables y_ij^(t,s),
with the normalization, admissibility and coefficients in
[foundations/04](../foundations/04-constant-weight-triple-sdp-source.md).
Fix only p_0=1, p_1=...=p_4=0, forbidden-distance zeros and source
equalities. Every other pair and touched triple variable remains free.

For each ordered (k,l) in {0,...,8}² retain both source PSD families on
I_(k,l)={5,6,7,8} intersect {k,...,68-k} intersect {l,...,956-l}.
Replace I_(0,0) by {0,5,6,7,8,68}; also retain both families at
(33,33) on {33,34,35} and (34,34) on {34}. These are 83 principal
index sets, giving 166 matrices. Do not identify the ordered labels.

Seed the orbit set with every admissible orbit in these upper-triangular
entry sums and all pair orbits (i,0,0,0), then close under the source
permutations. On this entire set retain y>=0, p_i-y>=0 and
1+y-p_i-p_j>=0, source equalities preserving t-s, repeated-word
identifications, and zeros whenever i,j or h=i+j-t-s belongs to
{1,2,3,4}. Include all original p_h in the complemented entries.
Retain all 68 L021 basic pair-LP inequalities and p_i>=0. No omitted
triple is set zero. No RS-specific labeled restriction is added.

## Conclusion

This entire shared-variable relaxation admits L022/L023's unchanged
rational extension, simultaneously, with

    M=(U+1)/2,  U=binomial(1024,64)/binomial(68,64),
    1383/1000 < M/T < 1384/1000,  floor(M)>T,  M>=K+1.

Thus this finite support cannot supply a sufficient upper certificate
U_bound<K+1, even with free pair variables. Its optimum is not computed.
This is a local negative result using a known method, without a novelty
claim beyond the assessed sources. It supplies no actual packing, RS
list, full-SDP feasibility, or safety/unsafety conclusion. The 955–957
bracket stays unchanged. The separate critical proof review below retains
this finite obstruction.

## Proof

**Imported statements and applicability.** Import A. Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.A (53)–(58), III.B (64)–(67), and the independent restatement in
H. K. Kim and P. T. Toan,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
III.B (31)–(35), III.C.2 (40). The hypotheses are nonempty binary
constant weight with even d and 0<d<2w<=n; here 0<10<136<=1024.
Principal restrictions are necessary PSD conditions. L022 already
supplies the uniform-in-m support application, including extra agreements;
no scalar projection or new support-transfer proof is needed.
Use the explicit two affine families, not Schrijver (61)'s qualified
complement prefactor. Positive-diagonal normalization and the two
distinct beta labels are retained exactly. This specializes cited
formulas; a reproof of block diagonalization is unnecessary.

**One assignment, with no constraints fixing free pairs.** Let a_i^*
be L021's specified rational primal vector, and set

    p_0=1, p_1=...=p_4=0,
    p_i=a_i^*/(2 binomial(68,i) binomial(956,i)) for i>=5,
    lambda=p_68>0.

For an admissible actual orbit with distances (i,j,h), use zero first
if any distance is 1,...,4; use p_b if its sorted distances are (0,b,b);
otherwise use p_i p_j p_h/lambda. This is precisely L022/L023's
extension. Equal numerical values at different t-s do not identify
variables in the relaxation. The stored affine model still has free
pairs; their displayed values are only a test assignment.

**Complete model and exact reconstruction.** The generator
`scripts/finite-support/free_pair_shell_batch.py` saves
`scripts/finite-support/free-pair-shell-batch-results.json`.
For every source entry it saves every original (t,s), its canonical
key (sorted(i,j,h),t-s), and its integer beta-product coefficient,
including zero coefficients. Source closure is saved explicitly.
The affine y dictionary aggregates only equal source keys; the affine
p dictionary separately aggregates the original h coefficients.
The two evaluated entries are respectively sum c*y and sum c*p_h-sum c*y.
Every scalar row is saved by its symbolic row kind, orbit key and pair
indices together with its rational slack. Pair rows retain all their
coefficients. Consequently this is a shared affine model rather than
independently assigned matrices.

There are 7386 source classes including fixed classes, with 32151 actual
ordered closure orbits. After fixed/Boolean identifications, there are
7144 free distinct-triple variables and 64 free pair variables, total
7208<=20000. There are 71688 retained scalar rows plus 68 pair-LP rows,
total 71756<=200000. Nonnegativity of every pair is included by the
seeded repeated-word orbit y_(i,0)^(0,0)=p_i. The other normalization
and forbidden pair values are substituted exactly. No required row was
dropped to meet the caps. Redundant scalar rows are harmless.

The independent verifier `scripts/finite-support/verify_free_pair_shell_batch.py`
imports no generator routine. It enumerates the support independently
by max(5,k,l), with the specified exceptions; regenerates admissibility
from all eight nonnegative multinomial parts; and checks every one of
the six distance permutations using the original t-s and its parity.
It reconstructs beta by the literal full source u-range and factorial
binomials, in contrast to the generator's truncated nonzero range.
Every original orbit/coefficient record and all 42915 nonzero aggregated
affine coefficients are compared. It recomputes every rational value,
all scalar slacks, all pair rows by independent polynomial convolution,
and every entry of all 166 matrices. It also checks the 64 equations
defining L021's primal vector via the corresponding pair slack 1/2,
as well as normalization, pair signs and forbidden/repeated branches.

All 71688 scalar slacks and all 68 pair slacks are nonnegative;
the minimum pair slack is 1/2. All 166 matrices are PSD. For each
matrix A, the complete rational certificate is an invertible E and
nonnegative diagonal D with E^T A E=D. The verifier multiplies out
every entry, checks det(E) is nonzero, and checks every diagonal sign.
There are 471 positive diagonal pivots and one zero pivot across the
472 total dimensions. The zero pivot belongs to the (0,0) complemented
matrix, whose index-0 row vanishes: repeated words give p_j-y_(0,j)=0.
The full congruence identities check the entire transformed zero row;
no division by a zero pivot is used. For arbitrary real x, writing x=Ez
therefore gives x^T A x=z^T D z>=0, also in this singular case.

The full independent output is
`scripts/finite-support/free-pair-shell-batch-verification.json`.
It reports no failures. This is exhaustive exact arithmetic, not sampled
minors, numerical eigenvalues or trust in a saved PSD flag. The scripts
adapt the L022 generator/auditor structure; the new independent source
reconstruction checks the full changed support. They use no L053–L096
Schur costs, ranks, column assignments, solves or constraints.

**Threshold and consequence.** L021 gives sum a_i^*=U-1, hence
M=1+(U-1)/2. The verifier independently reconstructs the binomial ratio
and checks the exact ratio endpoints above. In particular it checks

    2^128 floor(M)-65537^28
    =278623344535004185563774417633448491259524856948687283912464936072396859308983357073255491132778317876968018526278791647748932648566783
    >0.

Thus floor(M)>T and M>=K+1. This retains the integer endpoint, rather
than relying just on M>T. Any upper certificate valid for this relaxation
must bound its common feasible point M. In particular, the trace/scalar
weak-duality identity from Boyd–Vandenberghe, *Convex Optimization*
(2004), corrected 2009 printing,
[§5.9.1, pp. 264–266](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
cannot hold with U_bound<K+1 and nonnegative scalar/PSD multipliers:
evaluation at the witness would have a negative left side and
nonnegative right side. No strong-duality or attainment hypothesis is
used. This stops the entire specified support, not merely an individual
block or a fixed-pair optimization. Omitted blocks/rows may still reject
the extension, and no representing measure or RS realization follows.

Reproduce from the notebook:

    python3 scripts/finite-support/free_pair_shell_batch.py
    python3 scripts/finite-support/verify_free_pair_shell_batch.py

Full coefficients, original-orbit maps, all scalar slacks, both matrix
families and complete rational congruences remain on disk. The original
finite batch and its discriminating test had a prior SPECIALIZE assessment
in `drafts/literature/2026-10-20-free-pair-shell-batch-precheck.md`.

**Separate critical audit (2026-10-20, step 357).** The prior audit
assessment `drafts/literature/2026-10-20-l097-critical-audit.md` supplies
the exact source scope. The complete independent source verifier was
reexecuted with its output redirected to
`scripts/finite-support/free-pair-shell-batch-critical-source-verification.json`,
preserving the original evidence. Every original orbit map, all 42915
affine coefficients, every scalar/pair row and all 166 complete invertible
congruences pass again. This includes every transformed entry of the
singular matrix, not just its diagonal. Symmetry of the beta formula in
i,j and the source orbit equality justify filling the lower triangle.
The two beta labels remain ordered and distinct. No unrepresented orbit
is fixed, no original p_h is dropped, and no old Schur contract is used.

The new independent script `scripts/finite-support/audit_free_pair_shell_batch.py`
also challenges the orbit interpretation by constructing actual sets.
For each retained ordered orbit (i,j,t,s), take X={0,...,67}; inside X
choose removed sets R1,R2 of sizes i,j with intersection t, and outside X
choose added sets A1,A2 of sizes i,j with intersection s. Use an initial
common segment followed by disjoint remaining segments, exactly as in
the script. Admissibility gives i+j-t<=68 and i+j-s<=956, so these
segments fit the 1024-point universe. Put Y=(X\R1) union A1 and
Z=(X\R2) union A2. All three sets have size 68. Direct set differences
and intersections recover the original orbit. Recompute the orbit for
all six orders of X,Y,Z, without using the algebraic reanchoring formula.
For every one of the 32151 ordered orbits, the resulting set of indices
equals its saved closure and preserves the complete source key including
t-s. These 192906 actual presentations include repeated sets and
forbidden-distance cases; they are tests of orbit coordinates, not a
claim that such triples belong to a distance-10 code.

All 96453 original ordered scalar rows map to saved rows with the same
rational slack, and every saved scalar row is used. There are 71688
retained rows because the source equalities identify repeated copies;
no inequality is lost. All 205 Boolean/repeated orbits and 744 forbidden
orbits pass their defining identities. All 7093 L022 orbit records and
all old pair values agree exactly. There are 477 distance multisets with
multiple retained t-s values; their variables stay separate despite
equal test values. Together with the complete coefficient reconstruction,
this checks that the proof uses one shared feasible assignment to the
stated free-variable relaxation.

As an additional check independent of symmetric elimination, the new
audit clears the positive common denominator of each matrix, evaluates
every nonempty principal determinant by the integer Leibniz formula,
and restores that denominator to the power of the minor size. Of the
1498 exact minors, 1466 are positive and 32 are zero. The zeros are
precisely the subsets containing index 0 of the six-dimensional (0,0)
complemented matrix; its complete original index-0 row is checked zero.
All other minors are positive. The proof of PSD still uses the already
verified complete congruences above; this extra calculation does not
replace a missing source identity or rely on floating-point eigenvalues.

The audit reconstructs the support and all manuscript counts, including
471 positive and one zero congruence pivot, 7144+64=7208<=20000 variables
and 71688+68=71756<=200000 rows. It recomputes the full displayed
integer-floor excess and additionally obtains the exact positive value

    M-(K+1)=1637600837540546464980858362792905959718114328038848981235372174379468415819757877226327627676345/2.

Thus the integer obstruction is stronger than a mere M>T comparison.
Evaluating any valid upper certificate at this same point proves the
claimed whole-support stop. This argument needs neither an optimal
solution nor strong duality. The separate audit passes 306463 additional
checks with no failures; its complete set maps, principal minors, exact
threshold values and input hashes are in
`scripts/finite-support/free-pair-shell-batch-critical-audit.json`.
Run `python3 scripts/finite-support/audit_free_pair_shell_batch.py` after
the source replay described in the working record. The result retains
L097 only: omitted global constraints, other pairs or blocks, actual
packing/list realization and the 955–957 boundary remain unresolved.

## Mathlib

Full matching Schrijver SDP and this finite rational common witness:
not checked in Mathlib. The precise primary results above are imported;
the local specialization is checked by exact rational arithmetic.
