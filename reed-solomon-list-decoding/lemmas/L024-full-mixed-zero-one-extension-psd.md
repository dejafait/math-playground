# L024 — The prescribed extension passes both full mixed (0,1) blocks

## Hypotheses

Use L022's unchanged rational p_i, 0<=i<=68, and lambda=p_68>0,
at n=1024, w=68, v=956 and binary minimum distance d=10.
Retain L023's prescribed extension on actual admissible orbits:

\[
\max(0,i+j-68)\le t\le\min(i,j),\qquad
\max(0,i+j-956)\le s\le\min(i,j),\qquad h=i+j-t-s.
\]

Set y=0 first if any of i,j,h is in {1,2,3,4}; otherwise set
y=p_b when the distance multiset is (0,b,b); otherwise set
y=p_i p_j p_h/lambda. Different t-s orbit variables remain distinct,
even when their assigned values coincide. No feasibility is assumed.

Use exactly the two Schrijver matrices at block labels (k,l)=(0,1),
on I={1,...,68}:

\[
A^{(0)}_{ij}=\sum_{t,s}\beta_{ij,0}^{t,68}\beta_{ij,1}^{s,956}y_{ij}^{ts},
\qquad
A^{(1)}_{ij}=\sum_{t,s}\beta_{ij,0}^{t,68}\beta_{ij,1}^{s,956}
 (p_h-y_{ij}^{ts}).
\]

Only actual orbits are summed, including repeated words. For the RS
interpretation retain L022's field, domain, strict message degree less
than 64, simultaneous agreement and any m>=1; extra agreements are allowed.
Block labels k,l are unrelated to the RS dimension.

## Conclusion

Both full 68-by-68 matrices are positive semidefinite; A^(1) is positive
definite. Thus neither mixed (0,1) constraint excludes this unchanged
extension. Its objective remains M=(U+1)/2>1.383T, where
U=binomial(1024,64)/binomial(68,64) and T=65537^28/2^128.
L022's integer-floor excess also remains in force.

This is a negative exclusion diagnostic, not a threshold upper certificate.
This matrix diagnostic alone leaves scalar feasibility, other PSD blocks, full SDP feasibility,
actual packing or RS-list realization and safety at 67/68 agreements
undecided. The 955–957 bracket is unchanged. Further individual-block
diagnostics of this assignment are parked pending a different mechanism.

## Proof

**Imported constraint and specialization.** Alexander Schrijver,
*New code upper bounds from the Terwilliger algebra and semidefinite
programming*, IEEE Trans. Inform. Theory 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.A (55)–(58), pp. 6–7, and III.B (64)–(65), p. 7, supplies
the beta coefficients, complete block index sets and both PSD families.
Kim–Toan, [arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1),
14 December 2012, III.B (32)–(35), printed p. 9, independently
corroborates these statements. The precise imported input and the unused
printed (61) prefactor qualification are in foundations/04.

Here W_0={0,...,68} and V_1={1,...,955}, so their intersection is
exactly I. The hypotheses even d and 0<10<136<=1024 hold. In particular,
these matrices use beta_(ij,1)^(s,956); they are not obtained by deleting
index zero from L023's matrices. The literal source formula used is

\[
\beta_{ij,a}^{b,N}=\sum_{u=a}^{N-a}(-1)^{u-b}
 \binom ub\binom{N-2a}{u-a}
 \binom{N-a-u}{i-u}\binom{N-a-u}{j-u},
\]

with out-of-range ordinary binomials zero. This is a finite specialization
of the imported result, without reproving the general theorem.

**Complete matrix construction.** `scripts/finite-support/mixed_zero_one.py`
reconstructs the pair values from L021's exact primal witness using
L022's formula, and compares all 7093 old orbit-class values with L022.
It streams every actual orbit for each of the 2346 upper-triangular
entries. The saved t and s ranges and both beta arrays recover individual
coefficients and t-s identities. Integer beta products may be aggregated
by h only for evaluating the fixed formula, whose value depends on i,j,h;
this imposes no new equality of SDP variables.

The construction saves both full rational matrices before sign testing.
The complete certificate `scripts/finite-support/mixed-zero-one-results.json`
contains 86207 source beta coefficients and covers 771681 actual orbits.
All 2346 weight-68 beta arrays agree with the overlapping arrays in L023;
the weight-956 factor is reconstructed with label 1. Pair values, branch
order and old orbit values are unchanged; no old principal matrix is
claimed to equal a mixed principal matrix.

**Independent exact audit.** `scripts/finite-support/audit_mixed_zero_one.py`
imports no generator routine. It recomputes binomials from factorials,
uses the entire source u range (skipping only terms with an explicitly
zero binomial factor), and reconstructs orbit admissibility from the four
nonnegative multinomial parts. It independently reconstructs each assigned
value and evaluates entries by direct integer orbit sums after clearing
value denominators, rather than relying on the stored h aggregation.
Every saved beta coefficient, range and h aggregate agrees. All 9248
ordered rational matrix entries agree with the independent sums, and
both matrices are symmetric. All 7093 old orbit values and the 2346 old
weight-68 beta-array overlaps agree. These are exhaustive checks, not
samples or numerical spectra.

For each A, symmetric rational elimination supplies a unit upper
triangular E and a diagonal D. A positive pivot removes its remaining
off-diagonal entries by matched column and row operations; a zero pivot
is accepted only with an entirely zero residual row. The saved certificates
have the independently checked signs:

| Family | Positive pivots | Zero pivots | Original indices of zero pivots |
|---|---:|---:|---|
| y | 64 | 4 | 1, 2, 3, 4 |
| p_h-y | 68 | 0 | none |

The audit verifies every identity in E^T A E=D and every diagonal sign,
including all transformed entries associated with a zero pivot. Its exact
integer implementation takes a common denominator a>0 of A and positive
column denominators c_j of E, puts C=diag(c_j), A_int=aA and E_int=EC,
and checks all 4624 identities per family in

\[
E_{\rm int}^{T}A_{\rm int}E_{\rm int}=aCDC.
\]

Multiplication by C^(-1) and division by a give precisely E^T A E=D.
The audit also checks E is unit upper triangular, hence det(E)=1.
Its complete output is `scripts/finite-support/mixed-zero-one-audit-results.json`;
there are no failures. All diagonal signs and all zero-pivot indices were
also inspected in full. For any real x write x=Ez. Then
x^T A x=z^T D z>=0, proving both PSD assertions, including the singular
first family. Strictly positive D for the second family proves positive
definiteness. Complete identities, rather than elimination flags alone,
are the sign certificates.

**Threshold and scope.** The independent binomial sum of p_i agrees with
L022's M=(U+1)/2, and the required T is unchanged. L022 supplies the exact
ratio 1.383<M/T<1.384 and floor(M)>T. Passing these two new constraints
therefore fails to exclude the above-threshold extension. It does not
show that a full feasible point has this objective, or that any actual
code or list realizes it. This diagnostic does not test scalar constraints
or other blocks; L023 now records the separate subsequent full scalar audit.
This local computation reproduces known constraints and makes
no claim of mathematical novelty beyond the assessed sources.

From the notebook run `python3 scripts/finite-support/mixed_zero_one.py`
and then `python3 scripts/finite-support/audit_mixed_zero_one.py`.
Both retain complete certificates and print actual/required objectives,
failures and paths. Set PYTHONINTMAXSTRDIGITS=0 when using the shared JSON
inspector on certificates containing large exact integers.

## Mathlib

Full matching Schrijver constant-weight SDP theorem and this finite mixed
block certificate: **not checked** in Mathlib. The general matrices are
imported by the precise primary citations above. The local result rests
on complete rational congruence identities and signs, not an assumed
library theorem or approximate eigenvalues.
