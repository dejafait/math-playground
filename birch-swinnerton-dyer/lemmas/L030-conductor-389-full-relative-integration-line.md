# L030 — A conductor-389 full-relative real-integration line

## Hypotheses

Let E/Q be the curve y^2+y=x^3+x^2-2x, and let f be its normalized
weight-two newform supplied by the modularity theorem. Let M be the
entire torsion-free relative weight-two modular-symbol module for
Gamma_0(389), with {alpha,beta} oriented from alpha to beta. Set
I({alpha,beta})=Re(2 pi i integral_alpha^beta f(z) dz).

The full exact finite evidence is `scripts/relative-t2/certificate.json`;
its independent replay report is `scripts/relative-t2/verification.json`.
Both are part of this instance proof, rather than database premises.
Reproduction from this notebook directory is:

```bash
python3 scripts/relative-t2/build_certificate.py
python3 scripts/relative-t2/verify_certificate.py
```

The verifier reads the entire certificate and does not import the
construction program. No analytic rank, rational rank, period, Manin
constant, twist value, Sha assertion or database eigenvalue is assumed.

## Conclusion

The displayed equation is globally minimal, has minimal discriminant
and conductor 389, is non-CM, and has good-prime eigenvalue a_2=-2.
The certificate presents M as Z^390/R_sat, gives an integral quotient
basis of size 65 and the coordinates of every generator, and identifies
the full-relative geometric-reflection and T_2 matrices J,H_2.

On the entire 65-dimensional rational dual the matrix

\[
B=\begin{pmatrix}J^{\mathsf t}-1\\H_2^{\mathsf t}+2\end{pmatrix}
\]

has rank 64 and kernel dimension exactly one. Its nonzero rational
kernel vector v and all values phi(g_i)=v^t[g_i] are saved, with
phi(x)=v^t[x]. Consequently L029 gives

\[
I=\beta\phi\quad\text{on }M\otimes\mathbf R,
\qquad \beta\in\mathbf R\setminus\{0\}.
\]

This supplies L028's full-relative presentation and integration-line
inputs for this curve. It supplies no Neron-normalized scale, independent
nonzero twist ratio q, denominator C for that normalized map, quadratic
coefficient b, or BSD rank conclusion. The coordinate denominator one
below concerns the integral quotient coordinates; it is not the unknown
normalized modular-symbol denominator bound.

## Proof

**Named results and their applicability.** Import Cremona, *Algorithms
for Modular Elliptic Curves*, corrected second edition (1997),
[Sections 3.1--3.2, printed pp. 62--67](https://johncremona.github.io/book/fulltext/chapter3.pdf):
the Weierstrass invariants and discriminant change-of-model formula, and
the good/multiplicative exits of Tate's algorithm (multiplicative exit,
algorithm lines 19--22). Import its Section 3.9, printed p. 103, list of
rational CM j-invariants. All entries are integral. Import
Breuil--Conrad--Diamond--Taylor, *On the modularity of elliptic curves
over Q: wild 3-adic exercises*, JAMS 14 (2001), 843--939,
[Theorem A and Introduction's equivalent conductor-level statement](https://virtualmath1.stanford.edu/~rltaylor/st.pdf).
These give the normalized rational weight-two newform for E at its
conductor, whose good-prime coefficient is determined by point counts.
No identification of a database newform label is needed.

Import Stein, *Modular Forms, a Computational Approach*, online v0.1,
[weight-two Proposition 3.10, Proposition 3.11 and Theorem 3.13](https://wstein.org/books/modform/modform/weight_two.html).
At weight two the coefficient polynomial is constant. Theorem 3.13 gives
the complete relative Manin presentation modulo torsion, not merely
surjectivity onto absolute cycles. Proposition 3.10 identifies cosets by
projective bottom rows; Proposition 3.11 permits integral cusp-path
reduction. These theorems are imported, not reproved. The elementary
telescoping witnesses below verify only this finite instance. L029
supplies the already-proved real-integration sufficiency statement and
its operator and sign conventions.

**Independent arithmetic.** From [a_1,a_2,a_3,a_4,a_6]=[0,1,1,-2,0],
the invariant formulas give

\[
(b_2,b_4,b_6,b_8)=(4,-4,1,-3),\quad
c_4=112,\quad c_6=-856,\quad \Delta=389,
\quad c_4^3-c_6^2=1728\Delta.
\]

Every divisor trial 2 through floor(sqrt(389))=19 has nonzero remainder,
as saved and checked, so 389 is prime. An integral equation has
nonnegative local discriminant valuation. A reduction to a smaller
integral discriminant changes its valuation by a positive multiple of
12. Here every local valuation is 0 or 1, so no such reduction exists;
the equation is globally minimal. At 389, c_4 is a unit. The cited Tate
algorithm therefore gives multiplicative reduction with conductor
exponent one. Every other prime has good reduction and exponent zero.
Thus N=389. The rational j-invariant is 1404928/389, with denominator
389, excluding every rational CM j-invariant in the cited list.

Modulo 2 all four affine pairs (0,0),(0,1),(1,0),(1,1) satisfy the
equation. They exhaust F_2^2, and there is one point at infinity.
Good reduction follows also from the odd discriminant. Independently,
the affine derivative with respect to y is 1 modulo 2; the homogeneous
equation's derivative with respect to Z is 1 at [0:1:0]. Hence the
five-point count is on the smooth elliptic reduction and a_2=3-5=-2.
Modularity now identifies precisely the newform required in L029.

**Complete integral presentation and saturation.** Number the cosets
from 0 through 389. Their projective bottom rows are (1,t), 0<=t<389,
and (0,1). The corresponding SL_2(Z) representatives are

\[
g_t=\begin{pmatrix}0&-1\\1&t\end{pmatrix},\qquad g_{389}=1.
\]

Each generator represents g_i{0,infinity}. Thus its endpoints are
{-1/t,0} for i=t (with -1/0=infinity), and {0,infinity} for i=389.
For S=(0,-1;1,0) and U=(0,-1;1,-1), the right actions on bottom rows are
(c,d)S=(d,-c), (c,d)U=(d,-c-d), (c,d)U^2=(-c-d,c).
The certificate saves every permutation index and every row of the
780-by-390 relation matrix R: e_i+e_(iS) and
e_i+e_(iU)+e_(iU^2), for all 390 indices. These are exactly the complete
two/three-term relations of the imported theorem.

The certificate's elementary integral row operations and column
operations give U_R R C=D, where U_R and C are unimodular and D is
rectangular diagonal. Here U_R is represented by its complete operation
log, not an unverified assertion of an inverse. Each operation is a
swap, sign change or addition of an integer multiple of a distinct row
or column, with an explicit inverse. The verifier replays every operation
on the full R; C and C^(-1) are reconstructed from the column log in
forward and inverse order, and both inverse products are checked.
The diagonal has 325 positive nonzero entries, 324 equal to one and
one equal to two; all other entries of D are zero. No divisibility-ordered
Smith form is needed for this diagonal equivalence.

It follows that R has rank 325 and that saturation, in the transformed
coordinates, is generated by the first 325 standard row vectors. Thus
R_sat has basis the first 325 rows of C^(-1), with index
[R_sat:R]=2; this order-two torsion is removed, not ignored. The remaining
65 rows of C^(-1) lift an integral basis of M. The coordinates of the
original generator e_i in that quotient are the final 65 entries of row
i of C. All these coordinates are integral. The verifier checks the
saturated basis, original relations and quotient-basis inverse identities
against the full coordinate matrix. This proves a complete integral
relative presentation, not a dimension-only computation.

**Geometric operators on every generator.** For each generator's
oriented endpoints alpha,beta, the certificate includes its original
path and the paths obtained by each of

\[
\alpha\mapsto-\alpha,\qquad
\alpha\mapsto2\alpha,\qquad
\alpha\mapsto\alpha/2,\qquad
\alpha\mapsto(\alpha+1)/2,
\]

applied to both endpoints without reversing them. The first gives
geometric reflection; the sum of the last three is exactly L029's
good-prime T_2 at N=389. The three determinant-two matrices and the
reflection matrix are explicitly saved. No software plus/star label
is used.

For every resulting path {alpha,beta}, its raw integral expression is
{infinity,beta}-{infinity,alpha}. Each of these two summands has a saved
continued fraction and complete chain from infinity to its endpoint.
Every segment records its starting and ending cusp, an SL_2(Z) lift h
mapping {0,infinity} to that segment, a coset index i, and the exact
matrix gamma=h g_i^(-1). The verifier checks determinant one,
gamma's lower-left entry divisible by 389, and each successive endpoint
equality. Hence gamma is in Gamma_0(389), so the segment is exactly
generator i. Telescoping proves the raw expression including its signs.
Negative rational endpoints and infinity are checked by the same exact
rational/projective rules; no infinity division is performed. All
8,142 saved segments are checked, not a sample. The complete original
generator paths are also reduced and compared with their coordinates.

Summing segment coordinates gives the image of every integral generator.
The verifier checks images of every row of R and of the saturated
relation basis vanish. The images therefore descend to M. Multiplying
the generator-image rows by the quotient-basis lifts and transposing
gives the column-convention matrices J and H_2. Reconstruction on every
original generator is checked. These are thus the certified geometric
operators on the whole relative quotient. The additional exact checks
J^2=1 and J H_2=H_2 J pass, but these alone would not have identified the
operators or the module.

**Full-space rank and application.** The certificate saves the entire
130-by-65 B, its rational RREF, and all reversible elimination operations.
The independent verifier constructs B from the certified matrices and
a_2=-2, then replays the complete row log. Every pivot column is a unit
column with zeros before its leading entry; there are 64 pivots and all
remaining rows are zero. The one saved kernel vector has its sole free
coordinate equal to one, and every row of B annihilates it exactly.
Thus rank_Q B=64 and dim_Q ker B=1 on the full relative dual. In this
basis v has denominators at most two, and its integral-generator values
are stored exactly as dot products with the integral coordinates. They
are nonzero as a family and annihilate R_sat.

All hypotheses of L029 now hold with P={2}: E is minimal and non-CM,
its conductor and good-prime coefficient are independently certified,
the entire integral relative module and both geometric matrices are
certified, and the exact dual-kernel threshold is met. L029 gives the
nonzero real scalar beta and the conclusion on all of M_R. It does not
require L(E,1) to be nonzero. The execution report has 27 passing complete
checks and no failures, and binds to the certificate by SHA-256.

This is an actual finite specialization of known algorithms and L029,
not a new Manin or multiplicity theorem. The independent calibration
and the other downstream hypotheses remain unresolved; in particular
neither the rational rank nor the complex vanishing order has been
computed or equated.

**Complete critical audit (2026-10-07).** The separate approved audit
read both complete programs and L029, and replayed the entire certificate:
all 27 replay checks pass, including all 8,142 segments. Supplemental
evidence is `scripts/relative-t2/audit.json`, reproduced by
`python3 scripts/relative-t2/audit_certificate.py`. This program imports
neither other program. Its nine checks pass on the same certificate;
both reports bind to its SHA-256. It checks all matrix/vector shapes,
integer types, operation index bounds and rational entries, and every
path's shape and canonical cusp representation. Thus the original
verifier's uses of `zip` do not silently truncate any actual witness.
This is an audit of this fixed evidence, not a claim that the original
verifier rejects every malformed possible input.

The convention comparison is explicit: Stein's Theorem 3.13 uses
tau=(1,-1;1,0), with tau^2=U and tau^3=-1. Consequently U^2=-tau,
and projective right cosets identify these signs. The audit checks for
all 390 cosets that i tau=i U^2 and i tau^2=i U, and reconstructs each
entire three-term row. Thus the source and certificate have the same
relations, not merely the same dimension. All two-term rows were
reconstructed by the original replay. The complete diagonal has exactly
324 ones and one two. Row operations commute with column operations as
maps R -> A R C, so replaying the two recorded lists separately is valid
even though the builder interleaves them. Every logged elementary integer
operation is reversible; both reconstructed inverse products are the
identity. This justifies the saturated lattice and integral quotient
basis used above, including removal of the actual order-two torsion.

For an additional rank proof independent of the builder's rational
elimination log, the audit reconstructs B from the certified J,H_2 and
selects 64 original rows and 64 columns. The complete integer minor,
its selected indices, its modular elimination log and triangular form
are in `audit.json` under `rank_witness`. Its determinant modulo the
prime 101 is 75. The saved reversible row swaps/additions preserve the
determinant up to their recorded signs; multiplying the triangular
diagonal gives that residue. Therefore this integer minor is nonzero
and rank_Q B>=64. The same audit checks that w=2v is a nonzero integer
vector and that all 130 entries of B w are exactly zero, so rank_Q B<=64.
This corroborates the full rational replay's rank 64 and dimension one;
no floating-point rank estimate or extra operator is used.

The replay proves endpoint equality, determinant-one lifts and Gamma_0
membership directly, rather than trusting the builder's continued-fraction
recurrence. Those equalities, telescoping and the imported presentation
identify every path and operator on the whole relative module. Common
conventions in the programs have therefore been checked against the
source and L029, rather than inferred from their agreement. L029's
relative adjointness puts I in this kernel; its geometric-reflection
calculation fixes the sign; absolute real-period duality and the
absolute-to-relative injection make I nonzero; rational rank equals
real rank by minors. These apply to the independently established
minimal non-CM curve and good prime 2, and yield precisely I=beta phi
on all of M_R. No central nonvanishing or normalization is used.
The audit finds no failed equality or missing instance hypothesis.
It verifies this known-algorithm specialization, without supplying any
of the independent calibration or BSD premises listed above.

**Parameterized executable supplement (2026-10-10; separate critical audit
completed with a failure-reporting repair).** This supplements the same fixed line, rather than establishing a
new mathematical theorem. The existing fixed certificate and programs above
are preserved. A finite-P producer and independent checker now live under
`scripts/dual-kernel/`. Their exact model/conductor/trace input is
`conductor389-arithmetic.json`, with the L030 arithmetic provenance above.
The complete new evidence is `conductor389-certificate.json`; the full report
is `conductor389-verification.json`. Paths in this paragraph are prefixed by
`scripts/dual-kernel/`. Reproduce from the notebook root:

```bash
python3 scripts/dual-kernel/build_certificate.py --structural scripts/relative-t2/certificate.json --arithmetic scripts/dual-kernel/conductor389-arithmetic.json --adapter L030-fixed-v1 --out scripts/dual-kernel/conductor389-certificate.json
python3 scripts/dual-kernel/verify_certificate.py scripts/dual-kernel/conductor389-certificate.json --structural scripts/relative-t2/certificate.json --arithmetic scripts/dual-kernel/conductor389-arithmetic.json --out scripts/dual-kernel/conductor389-verification.json
python3 scripts/dual-kernel/check_rejection.py
```

The producer implements standard rational right-kernel/echelon computation;
see SageMath 10.8, [matrix2.right_kernel_matrix](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix2.html#sage.matrix.matrix2.Matrix.right_kernel_matrix)
for the exact field-kernel contract, including empty shapes, and Cremona,
corrected second edition, Section 2.7, printed pp.25--26, for column-action
and transpose dual vectors. It does not call Sage. L029 supplies the entire
relative ambient space and sufficiency theorem; these citations alone do
not emit a finite rank witness. The new work is evidence production and
binding, not a reproof of multiplicity or modular-symbol integration.

The checker does not import the producer. The fixed-schema adapter first
reruns the existing shape/source-convention audit, with assertions enabled,
and then the complete fixed verifier, on an exact input snapshot. Both
fresh reports bind to the original structural certificate bytes. Their
program hashes, report hashes and complete results are retained under
`conductor389-verification-structure/` and in the new verification report.
Thus no old success flag or operator hash replaces full structural replay:
all 1,950 paths, 8,142 segments, saturation operations and complete operator
reconstruction are rechecked. The supplied arithmetic file is separately
bound by its byte hash and exact parsed content, and its fixed identity
is checked against the independently replayed arithmetic above. Byte binding
alone is not an arithmetic proof.

From these checked column matrices, the independent checker reconstructs
every entry of B=(J^t-Id; H_2^t+2Id), retaining all 65 relative dimensions.
The new certificate saves explicit 130-by-65 B and RREF shapes, 3,525
reversible rational row operations, all 64 pivot indices and the entire
one-row kernel basis. Strict canonical rational parsing, all operation
indices, nonzero scales, complete unit pivot columns, leading entries and
every zero-tail row are checked before asserting rank 64. The free-coordinate
basis test and every exact Bv entry check both independence and completeness;
no truncated vector or approximate rank is used.

For independent lower-rank evidence the certificate retains 64 original
row indices and 64 column indices, the full selected matrix and its exact
determinant **-58,000**. The checker selects that minor anew from reconstructed
B and computes its determinant by fraction-free Bareiss elimination after
row-denominator clearing, checking every exact division. The producer used
rational Gaussian determinant elimination instead. All 130 entries of the
saved nonzero v's residual vector are exactly zero. Consequently the minor
gives rank at least 64 and the nonzero nullvector gives rank at most 64.
The threshold is exactly dimension one, as required by L029; it is not
inferred from a vector alone or a plateau in kernel dimension.

The checker recomputes all **390** generator values from the certified
integral coordinates and v, then checks all **780** source-relation and
**325** saturated-relation values vanish. These values identify the same
unnormalized full-relative functional as the existing L030 evidence.
The original standalone full replay has no failures. The separate
code-to-source critical audit below checks the new implementation and repairs
one subordinate failure-reporting defect; it makes no universal software claim.

`rejection-checks.json` records all 22 required corruption rejections,
including hashes/arithmetic binding, missing blocks, transpose and reflection
sign, zero/wrong nullvectors, malformed/zero/wrong minor claims, operation
bounds/noninvertibility, rational syntax and incorrect generator values.
The complete four core-only synthetic fixtures check d=0, d=1's empty minor
(det=1), larger kernel and zero nullity. These fixtures bypass structural
and arithmetic claims intentionally and are not accepted elliptic instances.
The standalone verifier exposes no synthetic adapter. Larger/empty kernels
are recorded as INCONCLUSIVE and carry no integration-line claim. The
sensitivity tests establish only these bounded cases, not universal soundness.

The generic interface also accepts the distinct L038-relative-v1 structural
schema, running its entire independent structural checker before linear
replay; that adapter has not been executed on a new elliptic arithmetic
instance here. It retains supplied positive exact conductor, integral
nonsingular model, finite sorted distinct good primes, integer Hasse-bounded
traces and explicit minimality/non-CM/conductor/newform/trace provenance.
Unsupported arithmetic certification claims are rejected. Generic provenance
is classified SUPPLIED_CONDITIONAL: the interface does not compute or prove
minimality, conductor, non-CM or newform association for arbitrary inputs.
There is no assertion of uniform software correctness, cutoff or runtime.
No new normalized scale, q, denominator C, coefficient or BSD comparison
is supplied. The mathematical argument and existing DAG inputs are unchanged.

**Separate parameterized executable critical audit (2026-10-10).** All three
complete dual-kernel programs, both fixed structural checkers and the general
structural checker were examined against the stated imports and L029/L038
contracts. All seven hashes in the original manifest matched before execution;
their original bytes and manifest are retained in
`scripts/dual-kernel/critical-audit/originals/`. The new complete evidence is
`scripts/dual-kernel/critical-audit/manifest.json`, with full reports below
that directory. The rebuilt dual certificate equals the original byte for
byte. The fixed arithmetic is the independent invariant/Tate/CM/modularity
and complete point-count argument above. Generic provenance strings and Hasse
bounds certify neither that arithmetic nor conductor/newform association.

The source-to-code rank argument is exact: each recorded row operation is
invertible (nonzero scales, distinct bounded source and target for additions),
so the complete reconstructed B and replayed RREF have equal rank. Strictly
increasing leading unit pivots and a wholly zero tail prove rank 64. The
free coordinate is index 59, with value one; every pivot coordinate is fixed
by its row equation. Thus the complete basis spans the right kernel, and its
130 zero residuals give the upper rank bound. The independently selected
64-by-64 original minor gives the lower bound. For its exact determinant,
clearing each row denominator multiplies the determinant by the product
of those denominators; row swaps change its sign. Bareiss updates divide
each cross-product by the preceding pivot, with every division checked exact.
The resulting signed last entry divided by that denominator product is
-58000, agreeing with the producer's rational Gaussian method. Empty order
has determinant one. This supplements, rather than replaces, the complete
elimination proof; neither a numerical rank nor an unchecked minor is used.

The full replay rechecks all 1950 paths, 8142 segments, every lattice
operation and both products of the integral column transform with its inverse,
all operator source/saturated
descent identities and reconstruction on every generator. All 3525 rational
row operations, 390 generator values, 780 source-relation values and 325
saturated-relation values pass. Every linear check label and summary equals
the original report; the two full subordinate reports also equal their
originals. The 22 rejection outcomes and all four fixture summaries equal
the originals in full. Direct inspection of the fixture constructions gives:
d=0 has rank/nullity (0,0) and no line; J=(1) at d=1 has (0,1), vector (1)
and the empty determinant one; J=Id_2 has (0,2) and no line; J=(-1) at d=1
has (1,0) and no line. These are synthetic linear-core tests only. The
standalone verifier always enters a recognized structural adapter first.

The general adapter's coordinates are the columns Pi e_i stored as rows,
and its saturated relations are precisely the transposes of all columns
of K. L038's full checks establish K=W^(-t)E_h, Pi=E_t^t W^t and all
operator columns before extraction. The r=0 branch has no saturated rows;
explicit shapes in the structural checker protect empty dimensions. The
general checker persists every caught failure in its subordinate report.
This code inspection supplies no new elliptic-instance execution for that
adapter and no universal soundness assertion. Missing requested operators
or traces cannot silently shrink the domain: the exact prime/domain/block
binding and complete structural operator set must agree. A genuinely empty
supplied P is allowed; the line threshold still applies.

One real defect was found and repaired. The old fixed verifier writes
explicit check() failures but has bare assertions in its path replay.
The fixed adapter had not caught those exceptions to write a subordinate
report. The preserved reproduction changes the first basepath end-chain
segment's claimed Gamma0 matrix from [-1,0,0,-1] to [0,0,0,-1], retaining
all dimensions and updating the external structural hash. The shape audit
passes, but the full geometric replay rejects: the claimed matrix is not
the computed h g_i^(-1), and its determinant is zero. Before repair the
outer report rejected while an existing subordinate success report survived.
This is not a false acceptance of a line, but violates the promised evidence
persistence. The adapter now catches every ordinary verifier exception,
writes a fresh report with the actual input hash, partial checks, the failure
and no results, then rethrows. The same corruption now rejects in both
reports; the stale success is replaced and the failed input hash matches.
Complete before/after artifacts are retained under `before-repair/` and
`after-repair/` in the audit directory. Existing evidence was not overwritten.

Reproduce the corrected finite audit from this notebook:

```bash
python3 scripts/dual-kernel/audit_failure_persistence.py after-repair
python3 scripts/dual-kernel/build_certificate.py --structural scripts/relative-t2/certificate.json --arithmetic scripts/dual-kernel/conductor389-arithmetic.json --adapter L030-fixed-v1 --out scripts/dual-kernel/critical-audit/rebuilt-certificate.json
python3 scripts/dual-kernel/run_critical_audit.py
```

The original seven-file manifest remains historical, so its checker hash
intentionally differs after this documented repair; the new audit manifest
binds the current program. The new audit has 11/11 passing comparison and
persistence checks and no unexpected failures. Acceptance is limited to the
inspected finite evidence and repaired path. No normalized scale, independent
q, new coefficient, universal termination/runtime claim or BSD conclusion
is added. Mathlib qualifications below are unchanged.

## Mathlib

Full matching conductor-389 presentation/operator/integration-line
certificate: not checked. Supporting Manin presentation, path reduction,
integral saturation, Hecke adjointness and real-period duality coverage:
not checked. Python certificate verification is not formal-library
verification. Unknown Mathlib availability is not evidence of absence.
