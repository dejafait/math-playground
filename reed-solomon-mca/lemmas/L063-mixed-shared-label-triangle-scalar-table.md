# L063 — Triangle scalar table with mixed shared-label roles

## Hypotheses

Use audited L059's full hypotheses and definitions of D(w), M(w), R.
Thus F=F_(97^20), H=(1,8,12,18,22,27,33,47,50,64,70,75,
79,85,89,96), C=RS[F,H,8], and 1/4<=delta<5/16 in the pinned model.
Restrict the ordered shared labels to P=(a,b,c)=(1,18,64) and the
singleton pool to S={8,12,22,27,70,75}. Allow every ordered partition
(Y,Z,W) of S into three unordered pairs, with base supports
{a,b} union Y, {a,c} union Z, {b,c} union W. Put U=P union S.
The original finite gamma_i are distinct, lambda!=0, and p,q,r range
over F with p(1-p)q(1-q)r(1-r)!=0. Retain both-zero lifts, zero fourth
weights and all original finite exclusions. No rational original chart
or normalized-weight rationality is assumed in the bound on R.

## Conclusion

For this restricted assignment, |D(w)|<=2 at every rational gated
weight point w in (F_97 minus {0,1})^3. The exact maximum is one for
77 ordered pair partitions and two for 13. Consequently |R|<=12,
including arbitrary extension-field weights and original charts.

This restricted computational partial input awaits separate critical
audit. It establishes neither arbitrary P,U coverage, a uniform triangle
bound, a full M maximum, extraction nor a global improvement of 11/q–16/q.

## Proof

### Exact enumeration and its independent reconstruction

Reproduction commands, relative to this notebook, are:

```
python3 scripts/triangle-recovery/fixed_union_table.py --shared-labels 1 18 64 --singleton-pool 8 12 22 27 70 75 --output scripts/triangle-recovery/mixed-role-table.json
python3 scripts/triangle-recovery/verify_fixed_union_table.py --shared-labels 1 18 64 --singleton-pool 8 12 22 27 70 75 --certificate scripts/triangle-recovery/mixed-role-table.json --output scripts/triangle-recovery/mixed-role-table-verification.json
```

The scripts are unchanged in this step; previous certificates are
preserved. Ordered P is supplied independently to both commands, rather
than inferred by the verifier from the producer's certificate. No
symmetry changing P or U is used. Swaps within a pair leave the supports
and defining sums unchanged, so unordered pairs cover these swaps.

There are binom(6,2)=15 choices for Y, then binom(4,2)=6 for Z;
W is forced. These are all 90 ordered pair partitions. For each one,
enumerate all binom(13,4)=715 four-subsets K of H minus P; none is a
base support. Set c_x=product_(h in H minus U)(x-h) for x in U.
Distinctness gives c_x!=0. All arithmetic is exact modulo 97.

The producer evaluates L059 (4), using the full projected and restored
label data imported there from L057. Two nonzero projected scalars give
one mu, excluded when mu=0,-1. Both-zero projected scalars give all 95
mu in F_97 minus {0,-1}, and exactly-one-zero gives no test. For every
tested mu, solve all three restored equations for p,q,r, save the point
even if a weight is 0 or 1, and retain it exactly when each weight avoids
those two values. At retained points invert the first four moments on K
and check all eight residuals. Zero recovered fourth weights are kept.
Deduplicate mu at each weight point. Audited L059 identifies the resulting
fiber with D(w), and a weight point absent from the table has empty D.

The verifier imports no producer functions and uses neither its quotient
polynomials nor its beta formulas. It reconstructs H as the roots of
x^16=1 in F_97, takes P and S from its own command, reconstructs U,c_x,
and checks the saved label data. It checks equality of the full sets of
90 partitions and, in each partition, all 715 supports, including
absence of duplicates. Counts alone are not substituted for these tests.

For each K let V be the 8-by-7 matrix whose columns are
v_x=(x,x^2,...,x^8)^tr, ordered by K then a,b,c. Its first seven rows
V_7 are invertible: det(V_7) is the product of the seven nonzero labels
times their Vandermonde product, up to the fixed column order. Define
Y_m=sum_(y in Y)c_y v_y and Z_m=sum_(z in Z)c_z v_z. Solve
sY=V_7^(-1)(Y_m)_[1:7], sZ=V_7^(-1)(Z_m)_[1:7], and form their
eighth-row residuals ry,rz. Then Z_m-mu Y_m belongs to im(V) precisely
when rz-mu ry=0. This gives all 95 test values if ry=rz=0, none if
exactly one is zero, and mu=rz/ry otherwise, excluded when mu=-1.
The verifier compares every projected case and its entire scalar-test
list, including tests rejected by weight gates.

Let d_a,d_b,d_c be the last three entries of sZ-mu sY. The actual
numerator whose recovery is tested is

```
N = Z_m-mu Y_m + c_a[1-(1+mu)p]v_a - mu*c_b*q*v_b + c_c*r*v_c.
```

Its coefficients on P vanish precisely for

```
p=(1+d_a/c_a)/(1+mu), q=d_b/(mu*c_b), r=-d_c/c_c.
```

Every denominator is nonzero for the tested scalars. The verifier
compares this independently reconstructed point and its gate with every
saved test. For a gated point, the first four entries of sZ-mu sY are
the K coefficients of N; they are compared with the producer's recovered
weights. The first seven equations hold by construction, and the eighth
by rz-mu ry=0. Cancellation of the three P coefficients proves that
these are all eight moments of N on K. This reconstructs each retained
row independently of the producer's first-four inversion; neither
method rejects a row for vanishing fourth weights.

For each partition the verifier reconstructs every scalar fiber,
the fiber-size histogram and every maximal fiber, then compares them
with the producer certificate. It also compares all projected-case and
gated/rejected-test counts. Thus the computed maximum rests on complete
automated replay, rather than a preview or selected positive cases.

### Completed certificate and threshold consequence

Coverage is 90/90 partitions and 64,350/64,350 support rows. The verifier
replayed all 80,976 scalar tests. There are 52,645 gated rows, including
6,118 both-zero rows and 1,560 with a zero fourth weight. The exact
partition-maximum histogram is {1:77,2:13}; maximum D is two against
the necessary threshold seven. The complete failure arrays in both
certificates are empty (actual/required 0/0). The producer summary,
verifier counts and both entire failure arrays were inspected using
the shared JSON inspector's selected `--full` values after successful
replay. These summaries report the complete replay; they alone would
not verify the enumeration.

There are no seven-scalar survivors. Therefore no full M computation is
needed for this assignment. The present verifier requires an empty
survivor set and cannot certify an unchecked full M count.

If an original gated pencil in this family had thirteen distinct
additional finite relaxed recoveries, audited L059's threshold argument
would force rational gated normalized weights, |M(w)|=13 and |D(w)|>=7.
The complete maximum two contradicts this, proving |R|<=12 for arbitrary
extension-field weights. Rationality is used only after the hypothetical
thirteen-recovery threshold, as justified by L059; it is not assumed
from the finite table alone. L059 retains the original finite gate via
|R|=|M(w) minus {rho/(1-rho)}|, without rationalizing gamma_i, rho,
lambda or the excluded direction. Distinct scalars, not support witnesses,
are counted, and both-zero lifts and zero fourth weights are retained
before the threshold argument.

### Sources and qualifications

The sole direct mathematical input is audited L059. L060/L061/L062 are
implementation precedents only; none of their unaudited conclusions is
assumed. Reuse the pre-existing EXPLORE assessment
`drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md`.
The precise standard recurrence input, imported through L059/L057, is
Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2, July 17, 2026, DR2 (`drc:lem-locator-recurrence`) and
DR6–DRC (`drc:thm-exact-compiler`), lines 2785–2935 of the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
Its unchanged specialization is R=8,t=4, multiplier x and
eta_j=s_(j+1), with distinct nonzero labels. No standard theorem is
reproved, and the mutable source is not identified with ePrint 2026/1463.
This result extends local restricted coverage; it is not certified
originality, progress beyond the inspected sources, or a challenge solution.

## Mathlib

The full restricted table exclusion and certificates: **not checked**.
Supporting finite-field arithmetic, Vandermonde invertibility and
finite-set counting: **not checked** for this step. No absence claim
or Lean verification is asserted.
