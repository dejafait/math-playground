# L061 — Second restricted triangle scalar table exclusion

## Hypotheses

Use audited L059's full hypotheses and definitions of D(w), M(w), R.
In particular F=F_(97^20), H=(1,8,12,18,22,27,33,47,50,64,70,75,
79,85,89,96), C=RS[F,H,8], and 1/4<=delta<5/16 in the pinned model.
Restrict the ordered shared labels to P=(a,b,c)=(1,8,12) and the
singleton pool to S={18,22,27,64,70,75}. Put U=P union S. Allow every
ordered partition (Y,Z,W) of S into three unordered pairs, with base
supports {a,b} union Y, {a,c} union Z, {b,c} union W. The original
finite gamma_i are distinct, lambda!=0, and p,q,r belong to F with
p(1-p)q(1-q)r(1-r)!=0. Neither weights nor original chart are assumed
rational for the final recovery bound. Retain both-zero lifts, zero
fourth weights and every original finite exclusion of L059.

## Conclusion

For these restricted label assignments, |D(w)|<=2 for every rational
gated weight point w in (F_97 minus {0,1})^3. The exact maximum is one
for 63 ordered pair partitions and two for 27. Consequently |R|<=12
for this family, including extension-field weights and arbitrary original
charts.

This computational partial input awaits separate critical audit. It
supplies no uniform triangle bound, arbitrary P,U coverage, full M
maximum, extraction theorem or global improvement of 11/q–16/q.

## Proof

### Enumeration and reproduction

All arithmetic is exact modulo 97. Reproduction commands are relative
to the active notebook:

```
python3 scripts/triangle-recovery/fixed_union_table.py --singleton-pool 18 22 27 64 70 75 --output scripts/triangle-recovery/second-union-table.json
python3 scripts/triangle-recovery/verify_fixed_union_table.py --singleton-pool 18 22 27 64 70 75 --certificate scripts/triangle-recovery/second-union-table.json --output scripts/triangle-recovery/second-union-table-verification.json
```

These two JSON files contain the complete producer table and independent
verification report. Earlier default certificates are preserved. There
are 15 choices for Y and 6 remaining choices for Z, with W forced: all
90 ordered partitions. Within-pair swaps leave the supports and every
equation unchanged. No change of shared labels, subgroup symmetry or
symmetry between singleton pools is used.

For each partition the producer enumerates all binom(13,4)=715 supports
K disjoint from P, each nonbase. It sets c_x=product_(h in H minus U)
(x-h), which is nonzero at every x in U. It computes the complete L057
projected and restored beta data used in L059's table formula (4).
Two nonzero projected scalars supply their unique ratio, tested only
when mu!=0,-1; both-zero projected scalars supply all 95 eligible
rational mu; exactly-one-zero supplies none. The producer saves every
tested point, including nongated points, and retains precisely those
whose three weights avoid 0,1. No fourth-weight nonvanishing filter
is applied. At each retained point it deduplicates mu. L059's exact
table identity identifies these fibers with D(w); unrepresented weight
points have empty fibers.

### Independent complete moment reconstruction

The verifier imports no producer functions. It reconstructs H from
x^16=1 in F_97, fixes P=(1,8,12), and takes the singleton pool from
its explicit command rather than trusting the certificate's scope.
It reconstructs U,c_x and checks equality with the saved label data.
It verifies exact partition-set equality with no duplicates and, in
each partition, exact support-set equality with no duplicates.

For each K, form the 8-by-7 matrix V with columns
v_x=(x,x^2,...,x^8)^tr, in order K followed by a,b,c. The first seven
rows V_7 are invertible: their determinant is the product of the seven
nonzero labels times the Vandermonde product of their pairwise
differences. Define Y_m=sum_(y in Y)c_y v_y and
Z_m=sum_(z in Z)c_z v_z. Solve the first seven moments to obtain
sY=V_7^(-1)(Y_m)_[1:7] and sZ=V_7^(-1)(Z_m)_[1:7]. Let ry,rz be
the corresponding eighth-row residuals. Membership of Z_m-mu Y_m
in im(V) is equivalent to rz-mu ry=0. Both residuals zero permit
all 95 scalars; exactly one zero permits none; two nonzero residuals
permit the single ratio rz/ry, except -1. This reconstructs every
projected case and eligible scalar independently of support-polynomial
quotients and beta formulas.

For any such scalar let d_a,d_b,d_c be the final three coordinates of
sZ-mu sY. The actual numerator of L057 (12) is

```
N = Z_m-mu Y_m + c_a[1-(1+mu)p]v_a - mu*c_b*q*v_b + c_c*r*v_c.
```

Its P coefficients vanish exactly when

```
p=(1+d_a/c_a)/(1+mu), q=d_b/(mu*c_b), r=-d_c/c_c.
```

Every denominator is nonzero. The verifier compares these reconstructed
weights with every saved test, including rejected gates. For a gated
point the first four coordinates of sZ-mu sY give the recovered K
weights. The first seven moment equations hold by construction, the
eighth holds because rz-mu ry=0, and the P coordinates cancel. Thus
all eight moments hold. The verifier compares every recovered
coefficient and saved residual. Independently, the producer solves
the first four moments on K and checks all eight residuals for each
gated point. Zero coefficients are retained in both reconstructions.

The verifier reconstructs each complete scalar fiber, its histogram and
every maximal fiber, comparing all with the saved table. Checked totals
are 90/90 partitions, 64,350/64,350 support rows, 85,782 scalar tests,
57,736 gated rows, 11,140 gated both-zero rows and 2,220 gated rows
with a zero fourth weight. The exact case-maximum histogram is
{1:63,2:27}, hence maximum D is two against necessary threshold seven.
There are zero seven-scalar survivors, so no full M test is needed.
Producer and verifier failure arrays are empty, with actual/required
failures 0/0. The complete selected summary, verifier counts and empty
failure arrays were inspected using the shared JSON inspector; the
full row evidence was checked by the replay rather than inferred from
a preview. The verifier fails if any seven-scalar survivor appears,
so it cannot certify an unverified survivor full count.

### Arbitrary-weight and original-chart consequence

Suppose a pencil in this restricted family has thirteen distinct
additional original finite relaxed recoveries. Audited L059's threshold
proof invokes its audited descent input only at this threshold and
forces w into F_97, |M(w)|=13 and |D(w)|>=7. This contradicts the
complete table maximum two. Therefore |R|<=12. L059 retains the exact
original-chart relation, removing at most the scalar rho/(1-rho), and
does not rationalize the given gamma_i or infinity. Both-zero lifts,
relaxed zero weights and scalar deduplication precede the threshold
argument; no support witnesses are substituted for distinct parameters.

The sole direct mathematical input is audited L059. L060 is an
implementation precedent, not a premise. Reuse the pre-existing
EXPLORE assessment `drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md`
and L059's precise primary recurrence citation and unchanged
specialization; no new external theorem or standard recurrence reproof
is claimed. This extends local restricted coverage, with no certified
originality or progress beyond the checked sources asserted. Separate
critical audit and the uniform counting problem remain open.

## Mathlib

The full restricted table exclusion and certificates: **not checked**.
Supporting finite-field arithmetic, Vandermonde invertibility and
finite-set counting: **not checked** in this step. No absence claim
or Lean verification is asserted.
