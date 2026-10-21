# L023 — L022's extension passes full zero-index blocks and scalar constraints

## Hypotheses

Use L022's fixed rational pair values p_i for 0<=i<=68 and lambda=p_68>0,
with n=1024, w=68, v=956 and binary minimum distance d=10. The threshold
is T=65537^28/2^128. For the RS interpretation retain L022's instance,
strict message degree less than 64 and any m>=1; selected supports may
have extra agreements.

Extend only the **formula**, without assuming feasibility: on every
actual admissible orbit (i,j,t,s) used by either full (0,0) block, put
h=i+j-t-s. Set y=0 if one of i,j,h is in {1,2,3,4}; otherwise set y=p_b
if the distance multiset is (0,b,b); otherwise set y=p_i p_j p_h/lambda.
Keep different t-s orbits distinct, even when the assigned values agree.
Admissibility means

\[
\max(0,i+j-68)\le t\le\min(i,j),\qquad
\max(0,i+j-956)\le s\le\min(i,j).
\]

For each i,j in {0,...,68}, define A^(0) and A^(1) by Schrijver's
source sums from foundations/04:

\[
A^{(0)}_{ij}=\sum_{t,s}\beta_{ij,0}^{t,68}\beta_{ij,0}^{s,956}y_{ij}^{ts},
\qquad
A^{(1)}_{ij}=\sum_{t,s}\beta_{ij,0}^{t,68}\beta_{ij,0}^{s,956}
 (p_h-y_{ij}^{ts}).
\]

The sums include repeated words and exclude impossible multinomial
orbits. No other block, changed assignment or optimization is included.

## Conclusion

Both full 69-by-69 matrices are exactly positive semidefinite. All values
overlapping L022's certificate, and both old four-index principal
matrices, agree exactly. Thus neither full (0,0) constraint excludes
this prescribed extension, whose objective remains (U+1)/2>1.383T,
where U=binomial(1024,64)/binomial(68,64).

The unchanged extension also satisfies every Schrijver scalar constraint
on all 1500625 actual ordered orbits, including normalization, forbidden
distance zeros and the required permutation equalities preserving t-s.

This parks these fixed-extension exclusion diagnostics. It does not prove
full SDP feasibility, feasibility of other omitted
blocks, an actual packing or list, or safety or unsafety at 67/68
agreements. It excludes no alternative extension, supplies no improved
upper bound, and leaves the 955–957 bracket unchanged.

## Proof

**Imported matrices and specialization.** Schrijver, *New code upper
bounds from the Terwilliger algebra and semidefinite programming*, IEEE
Trans. Inform. Theory 51 (2005), 2859–2866,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf), III.A
(58), III.B (64)–(65), supplies the beta coefficients and both necessary
PSD families. Kim–Toan, [arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
14 December 2012, III.B (32)–(35), printed pp. 8–9, corroborates the
complete index sets and second affine family. These inputs and their
normalization qualifications are recorded in foundations/04. At k=l=0,
W_0={0,...,68}, V_0={0,...,956}, so the intersection gives exactly these
69 indices. The hypotheses even d and 0<d<2w<=n hold. No printed
complement prefactor from Schrijver (61) is used. This is a known source
specialization, with no theorem reproof.

**Exact finite matrices.** The pair values are exactly those specified
in L022, reconstructed from its stored L021 primal witness rather than
from an approximate solver. `scripts/finite-support/full_zero_blocks.py`
streams each actual orbit of each of the 2415 upper-triangular entries.
It evaluates the literal beta formula, with only zero binomial terms
removed. It saves both beta arrays per entry and the integer sums of
their products for each h. Since the prescribed value depends on i,j,h,
these sums evaluate y without changing orbit identification. The saved
t and s ranges recover every individual source coefficient and orbit,
including t-s. No unassigned orbit is silently given zero.

The complete evidence is `scripts/finite-support/full-zero-block-results.json`:
all 86345 beta coefficients, the source ranges and h-coefficient sums,
both rational matrices, and both exact congruences. The construction
covers 771750 actual upper-entry orbits. Every one of the 7093 old
orbit-class values agrees with L022, including its repeated-word and
forbidden branches. Both four-index principal matrices agree at all
32 ordered entries. Full matrices are saved before sign testing.

**Exact sign certificates.** For each A the certificate contains a
rational unit upper triangular E and diagonal D such that

\[
 E^T A E=D.
\]

Symmetric elimination uses a positive pivot a to subtract the multiple
A_kj/a of column k from column j, with the matching row operation; a
zero pivot is accepted only with a zero residual row. The certificate
retains every factor and pivot as well as the full resulting E and D.
The independently verified diagonal signs are:

| Family | Positive pivots | Zero pivots |
|---|---:|---:|
| y | 65 | 4 |
| p_h-y | 68 | 1 |

`scripts/finite-support/audit_full_zero_blocks.py` imports no generator
routine. It reconstructs binomials from factorials and beta from the
full source u range; skipped terms have an explicitly zero factor.
It tests multinomial admissibility by nonnegative parts, independently
reconstructs the prescribed values, checks every saved beta coefficient
and h-coefficient sum, and evaluates the matrix by direct orbit sums
after clearing value denominators, rather than using the stored h sums
for its evaluation. All 9522 ordered matrix entries agree, both matrices
are symmetric, and the old overlaps also agree.

The audit verifies every congruence entry and every diagonal sign.
For its integer implementation, let a>0 be a common denominator of A,
let c_j>0 clear column j of E, and C=diag(c_j). Put A_int=aA and
E_int=EC. The complete integer identities checked are

\[
 E_{\rm int}^T A_{\rm int} E_{\rm int}=aCDC,
\]

which are equivalent to E^T A E=D by multiplying by C^(-1) on both
sides and dividing by a. Thus denominator clearing neither approximates
the matrices nor changes the sign test. Every off-diagonal identity is
checked, including all entries of each zero diagonal's transformed row.
The audit also checks that E is unit upper triangular, giving det(E)=1.
Its full result is `scripts/finite-support/full-zero-block-audit-results.json`;
there are no verification failures.

For any real x, write x=Ez using invertibility. Then
x^T A x=z^T D z>=0, establishing PSD, including the singular cases.
This argument uses complete exact identities, not numerical eigenvalues
or a preview of selected certificate entries.

**Full scalar extension audit (2026-10-06).** The full (0,0) index set
already ranges over every i,j in {0,...,68}; thus its actual orbits are
exactly the full scalar domain, not a changed assignment. Import
Schrijver III.B (62)–(65), printed p. 7, and Kim–Toan III.B (31)–(35),
printed pp. 8–9, with the actual-orbit qualification in foundations/04.
Their necessary scalar conditions are p_0=1, y>=0, p_i-y>=0 and
1+y-p_i-p_j>=0, together with prescribed distance zeros and equality
under permutations of (i,j,h) preserving u=t-s. These source hypotheses
are the same even-distance constant-weight hypotheses checked above.
No general theorem is reproved and no strengthened inequality is added.

`scripts/finite-support/full_scalar.py` saves the complete scalar evidence
in `scripts/finite-support/full-scalar-results.json`. It retains all 4761
ordered (i,j) entries and their inclusive t and s ranges. For each entry,
h runs through every integer between i+j-t_max-s_max and
i+j-t_min-s_min; a stored h-to-record map recovers every scalar evaluation
at every original (i,j,t,s). The numerical cache has 29190 distance
multisets, but these are not orbit-variable identifications: different
t-s values and all original t,s indices remain recoverable from the
ranges. Permutation scope is checked with the original u, never with
distances alone.

All arithmetic is exact. Let D be the positive least common multiple of
the denominators of L022's p_i and put A_i=D p_i. Since lambda=p_68>0,
H=D^2 A_68 is a positive integer. Write P_i=A_i D A_68, so P_i/H=p_i.
On a distinct permitted orbit the prescribed y equals
A_i A_j A_h/H. Forbidden orbits have numerator zero; repeated-word
orbits have numerator P_b. Consequently the three scalar slack
numerators are Y, P_i-Y and H+Y-P_i-P_j over the same positive H.
The certificate retains each cached Y and all upper and lower slack
numerators for the three distances. Exact per-entry maps recover the
required three rows of each original orbit, including repeated distances.

`scripts/finite-support/audit_full_scalar.py` imports no generator
routines. It independently rebuilds the pair values from L021's fixed
witness and factorial binomials. Polynomial convolution checks all 64
defining equations of L021's nonsingular system, fixing that witness
without a numerical solver. It verifies all pair values against L022,
L023's original zero-block certificate and L024's mixed certificate,
then independently computes D,H and every cached rational value and
slack from the prescribed forbidden-first/repeated-second/product-third
formula. Source orbit scope is regenerated by nonnegativity of
(i-t,j-t,t,68-i-j+t) and (i-s,j-s,s,956-i-j+s), not by trusting the
saved ranges. Every actual original orbit and every stored h map agrees;
all cache records are used, and there are no extra ordered entries.
The comparison with L024's pair data is only a consistency check;
no assertion about its mixed PSD matrices is an input to this proof.

For every original orbit the audit checks its three exact slack signs,
forbidden zeros and repeated-word identity. For each of the six
permutations (a,b,c) of (i,j,h), retaining the original u, it computes
t'=(a+b-c+u)/2 and s'=(a+b-c-u)/2, checks integrality and all multinomial
parts, and compares the two assigned values through their original
entry maps. This verifies every required equality, rather than imposing
an unlicensed equality between different u values. Counts include
permutation repetitions when distances coincide.

The independently regenerated totals are 1500625 ordered orbits,
4501875 scalar rows and 9003750 permutation checks. All 10232
forbidden-distance orbits have y=0; all 205 repeated-word orbits have
u=0 and the prescribed pair value, including the all-zero orbit.
Normalization p_0=1 and lambda>0 are checked separately. All 7093 old
orbit values and all 68805 old reduced scalar rows agree exactly.
Every one of the 30856 old closure orbits is retained; the 1469769 new
ordered orbits contribute 4409307 additional expanded scalar rows.
Old closure rows expanded to three per orbit number 92568, so they
are not confused with the earlier reduced-row count. There are no
negative slacks, equality violations or audit failures.

The full independent result, including counts, complete failures lists,
the 64 defining-equation residuals, exact objective and threshold, and
exact minimum slacks with original witnesses, is
`scripts/finite-support/full-scalar-audit-results.json`. All three global
minimum slacks are zero; the proof uses every individual reconstructed
row, not those extrema. This exhaustive finite rational check proves
full scalar feasibility of this assignment. It does not check any
additional PSD block or produce actual triple counts of a code.

The objective is again M=(U+1)/2, and independent exact arithmetic checks
1383/1000<M/T<1384/1000 and floor(M)>T. Thus all ordinary source scalar
constraints fail to exclude this above-threshold extension. Scalar
exclusion for this unchanged assignment is parked; this is an informative
negative diagnostic, not a sharp support bound or unsafe RS list.
Reproduce with `python3 scripts/finite-support/full_scalar.py` followed by
`python3 scripts/finite-support/audit_full_scalar.py`. Both write complete
certificates and print actual/required bounds, failures and paths.
The prior SPECIALIZE assessment is
`drafts/literature/2026-10-05-full-scalar-extension-test.md`; the work is
REPRODUCTION, without a novelty claim. No new lemma identifier is added.

**Interpretation and reproduction.** The extension preserves every old
value and all p_i, so L022 supplies its unchanged objective and strict
threshold excess, including the integer-floor qualification. Passing
these two additional PSD constraints alone does not check scalar rows or
any further block; the separate complete scalar audit above supplies
only the scalar assertion. These checks cannot turn the distribution into an RS
list or decide the main safety gap. This is a REPRODUCTION finite
specialization of the known method, with local negative diagnostic
evidence and no novelty claim beyond the sources checked.

From this notebook run `python3 scripts/finite-support/full_zero_blocks.py`
and `python3 scripts/finite-support/audit_full_zero_blocks.py`. Both save
full rational certificates and print actual/required objectives,
verification failures and artifact paths. Use PYTHONINTMAXSTRDIGITS=0
with the shared JSON inspector because some certificate integers exceed
Python's default conversion limit. The shared inspector is unchanged.

## Mathlib

Full matching Schrijver constant-weight SDP theorem and these finite
full-zero-block and full-scalar certificates: **not checked** in Mathlib.
The primary matrices and scalar constraints are imported by the precise
citations above; complete rational congruences and individual scalar
row checks give the local certificates.
