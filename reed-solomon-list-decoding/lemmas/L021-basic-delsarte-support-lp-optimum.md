# L021 — Basic Delsarte LP does not improve the 68-support bound

## Hypotheses

Use C001a's instance: n=1024, k=64, Q=65537, F=F_(Q^28),
epsilon*=2^(-128), the order-1024 subgroup domain, and any integer m>=1.
Messages have row degree strictly less than 64 and B_m denotes the pinned
closed simultaneous column-Hamming list size. Use only the basic
constant-weight Delsarte inequalities for binary A(1024,10,68), without
enhanced constraints, integrality constraints, or RS-specific restrictions.

For 1<=j<=68 and 5<=i<=68 define the rational coefficients

\[
 q_{ji}=\frac{\sum_{h=0}^{i}(-1)^h\binom jh
       \binom{68-j}{i-h}\binom{956-j}{i-h}}
       {\binom{68}i\binom{956}i},
\]

with binomial coefficients zero outside their ordinary range. The primal
LP maximizes sum_i a_i subject to a_i>=0 and
sum_i q_{ji}a_i>=-1 for each j. Its dual minimizes sum_j y_j subject to
y_j>=0 and -sum_j y_j q_{ji}>=1 for each i.

## Conclusion

The exact basic LP optimum is

\[
 P=\frac{\binom{1024}{64}}{\binom{68}{64}}-1.
\]

Here 1+P is an integer. Its code/list upper certificate is therefore

```text
U = 5911400469643253979096668067252516781779963059980537398382691230233477959044083559469669112419568
2^128*U-65537^28 = 1284396016348881038251703468864531590748842823418702723899026088586712660737532177946092631299696396858677716707415484477398868656652287
```

The positive excess and U/(epsilon*|F|) in [2766/1000,2767/1000)
show that this basic LP cannot certify safety at 956 errors. It exactly
reproduces L001's support ratio, and is slightly weaker than C001b's
nested-floor certificate. Neither this feasible distance distribution
nor failure of the LP bound establishes an actual code of size U, an
unsafe RS list, or sharpness. The bracket 955<=t_star(m)<=957 is unchanged.

## Proof

**Imported inequalities and applicability.** Byung Gyun Kang, Hyun Kwang
Kim and Phan Thanh Toan,
[Improved Linear Programming Bounds on Sizes of Constant-Weight Codes](https://arxiv.org/pdf/1108.5104v1),
v1, August 25, 2011, Section II.A, Remark 3, Theorems 4–5 and
equations (8)–(14), pp. 1–2, give precisely these distance-distribution
inequalities, with a_i=A_(2i), A_0=1, and upper bound
1+floor(max sum_i a_i). Their hypotheses are even d and d<2w<=n;
here d=10, w=68, n=1024 satisfy them. This is an imported known theorem,
not a reproof. The prior
[SPECIALIZE assessment](../drafts/literature/2026-10-05-delsarte-support-certificate.md)
inspected this normalization and cross-checked Best et al.,
[Bounds for binary codes of length less than 25](https://ir.cwi.nl/pub/6624/6624D.pdf),
Section 4.2, Theorem 21, printed p. 18. No later enhanced inequalities
from either source are used.

At an arbitrary received array, select 68 simultaneous agreement columns
from each candidate having at least 68 agreements. L001 proves that two
distinct tuples cannot share 64 agreement columns. Thus their selected
supports are distinct, intersect in at most 63 points, and have binary
incidence-vector distance at least 2(68-63)=10. This is the same support
selection used in C001b, allowing extra agreements. It counts the entire
tuple family, uniformly in m; the binary alphabet is only the support
alphabet. The imported theorem bounds B_m(956/1024). C001a supplies the
instance and ambient threshold, not a scalar-to-tuple equality.

**Exact witnesses, compact specification.** Let A be the 64 by 64 rational
matrix A_(j,i-4)=-q_(j,i), j=1,...,64 and i=5,...,68. Define x by Ax=1
and z by A^T z=1, both computed by the following deterministic rational
elimination: in increasing column order select the first nonzero pivot
among the remaining rows, exchange it into the pivot row, divide that
row by its pivot, subtract multiples from all subsequent rows, and then
back-substitute. All 64 pivots exist for each system. Set a_i=x_(i-4),
y_j=z_j for j<=64, and y_j=0 for j>=65. This is a finite exact rational
specification of the witnesses, not use of a numerical solver's values.
The function `solve_exact` in `scripts/finite-support/delsarte_lp.py`
implements this specification. The complete rational vectors, coefficient
matrix, and every slack are retained in
`scripts/finite-support/delsarte-lp-results.json`.

The following are exact finite-arithmetic identities for these witnesses:

* Every a_i is positive, and min_i a_i=9965466368/5.
* Every y_j for j<=64 is positive, with minimum 81499/85; the last four
  y_j are zero.
* The primal slacks 1+sum_i q_(j,i)a_i are zero for j<=64. For
  j=65,66,67,68 respectively, their complete values are
  35022142001/26556181345, 773548117/801136197,
  479313305/478531017, 476373605/476387541. All are positive.
* All 64 dual slacks -sum_j y_j q_(j,i)-1 are exactly zero.
* sum_i a_i=sum_j y_j=U-1, and U=binomial(1024,64)/binomial(68,64).

These identities include every required nonnegativity and inequality,
rather than a sample or an approximate feasibility check. They can be
checked from the rational specification without the discovery tableau.
The independent audit `scripts/finite-support/audit_delsarte_lp.py`
recomputes every numerator as the coefficient of Z^i in

\[
 (1-Z)^j\sum_{r=0}^{68-j}\binom{68-j}r\binom{956-j}r Z^r,
\]

whose expansion gives the displayed numerator exactly, and recomputes
the binomials by integer products. It checks all 4352 coefficient entries,
all 68 primal and 64 dual inequalities, all 132 variable signs, both
objective sums, all stated zeros, and the exact ratio and excess. Its
complete results are in `scripts/finite-support/delsarte-lp-audit-results.json`.
The four nonzero primal slacks and both minimum coefficients were also
inspected in full. Thus the numerical discovery stage is dispensable
for checking the finite certificate. No claim rests on a preview.

**Optimality and threshold.** For any feasible primal a and feasible dual y,
nonnegativity and the dual inequalities imply

\[
 \sum_i a_i\le -\sum_j y_j\sum_i q_{ji}a_i\le\sum_j y_j.
\]

The exact feasible witnesses above attain equality, so the maximum exists
and is P=U-1. The imported Delsarte upper bound is 1+floor(P)=U.
The checked positive integer 2^128 U-65537^28 proves U exceeds the
required threshold, with no equality ambiguity. Even a primal witness
alone above threshold would rule out a sufficient certificate from this
LP; equal feasible objectives additionally establish its exact optimum.
C001a's safety at 955 and unsafe index 958 remain in force. No conclusion
about actual safety at 956 or 957 follows from this LP limitation.

**Reproduction commands.** From this notebook run
`python3 scripts/finite-support/delsarte_lp.py`, then
`python3 scripts/finite-support/audit_delsarte_lp.py`. Decimal simplex at
220-digit precision took 64 pivots to discover the first-64-row basis;
all mathematical claims use the subsequent exact fractions. Both scripts
save full certificates and print bounds, required threshold, failures,
and paths. There were no failures. This is REPRODUCTION of a known LP
method for one finite instance, not progress beyond the assessed sources.

## Mathlib

Full matching constant-weight Delsarte theorem and this exact finite-instance
optimum: **not checked** in Mathlib. The cited primary LP theorem is the
standard input. L001 supplies common-support uniqueness locally; the
separate pinned ArkLib boundary theorems do not supply this LP certificate.
