# L062 — Triangle scalar table with changed shared-label roles

## Hypotheses

Use audited L059's full hypotheses and definitions of D(w), M(w), R.
Thus F=F_(97^20), H=(1,8,12,18,22,27,33,47,50,64,70,75,
79,85,89,96), C=RS[F,H,8], and 1/4<=delta<5/16 in the pinned model.
Restrict the ordered shared labels to P=(a,b,c)=(18,22,27) and the
singleton pool to S={1,8,12,64,70,75}. Allow every ordered partition
(Y,Z,W) of S into three unordered pairs, with base supports
{a,b} union Y, {a,c} union Z, {b,c} union W. Put U=P union S.
Original finite gamma_i are distinct, lambda!=0, and the normalized
weights p,q,r range over F with p(1-p)q(1-q)r(1-r)!=0.
Retain both-zero lifts, zero fourth weights and all original finite
exclusions. The final bound assumes neither rational weights nor a
rational original chart.

## Conclusion

For these restricted assignments, |D(w)|<=2 at every rational gated
weight point w in (F_97 minus {0,1})^3. The exact maximum is one for
72 ordered pair partitions and two for 18. Consequently |R|<=12,
including arbitrary extension-field weights and original charts.

This restricted computational partial input awaits separate critical
audit. It supplies no arbitrary P,U coverage, uniform triangle bound,
full M maximum, extraction theorem or global improvement of 11/q–16/q.

## Proof

### Exact table and complete scope

Reproduction commands, relative to this notebook, are:

```
python3 scripts/triangle-recovery/fixed_union_table.py --shared-labels 18 22 27 --singleton-pool 1 8 12 64 70 75 --output scripts/triangle-recovery/shared-role-table.json
python3 scripts/triangle-recovery/verify_fixed_union_table.py --shared-labels 18 22 27 --singleton-pool 1 8 12 64 70 75 --certificate scripts/triangle-recovery/shared-role-table.json --output scripts/triangle-recovery/shared-role-table-verification.json
```

The first certificate saves every support, projected case, tested
scalar and gated or rejected weight point. The second records complete
independent replay. Both scripts take the ordered P explicitly; the
verifier obtains it from its own command, rather than from the producer
certificate. Their old defaults and previous certificates are preserved.
No symmetry changing shared labels or the nine-label union is used.
Within each pair, swaps leave the supports and equations unchanged.

There are 15 choices for Y and six choices for Z among the remaining
four labels; W is forced. Thus all 90 ordered pair partitions are
covered. For each partition, enumerate all binom(13,4)=715 four-sets
K disjoint from P; none is a base support. Set
c_x=product_(h in H minus U)(x-h) for x in U. These coefficients are
nonzero. All arithmetic is exact in F_97.

The producer uses L059 (4), with the full projected and restored beta
data of L057. Two nonzero projected scalars supply their single ratio
mu, admitted only for mu!=0,-1. Two zero scalars supply all 95 eligible
mu in F_97 minus {0,-1}; exactly-one-zero supplies none. For every
eligible scalar, solve all three restored equations for p,q,r. Save
the point even when a weight is 0 or 1, and retain it exactly when all
three weights avoid those values. At retained points compute the
fourth weights by first-four moment inversion and check all eight
residuals. Keep zero fourth weights. Deduplicate mu at each weight
point before computing its fiber cardinality. By audited L059's exact
table identity, this fiber is D(w); an unrepresented weight has empty D.

### Independent full moment replay

The verifier imports no producer function. It reconstructs H as the
roots of x^16=1 in F_97, takes P=(18,22,27) and S from its explicit
command, reconstructs U,c_x, and compares the saved label data. It
checks exact equality of the 90 partition sets without duplicates and,
for each partition, exact equality of all 715 support sets without
duplicates. These checks prevent omitted cases from being certified
by a count alone.

For K, form the 8-by-7 moment matrix V with columns
v_x=(x,x^2,...,x^8)^tr ordered as K followed by a,b,c. Its first
seven rows V_7 are invertible: their determinant is the product of
the seven nonzero labels times the Vandermonde product of their
pairwise differences, up to the fixed column order. Let
Y_m=sum_(y in Y)c_y v_y and Z_m=sum_(z in Z)c_z v_z. Solve
sY=V_7^(-1)(Y_m)_[1:7], sZ=V_7^(-1)(Z_m)_[1:7], and compute
the corresponding eighth-row residuals ry,rz.

Membership of Z_m-mu Y_m in im(V) is equivalent to rz-mu ry=0.
Two zero residuals permit all 95 test scalars; exactly one zero
permits none; two nonzero residuals permit precisely mu=rz/ry,
unless mu=-1. This reconstructs every projected case and scalar
test without the producer's support-polynomial quotient or beta
formulas. The verifier compares the complete ordered scalar-test
list for every K.

Let d_a,d_b,d_c be the final three coordinates of sZ-mu sY.
The actual numerator is

```
N = Z_m-mu Y_m + c_a[1-(1+mu)p]v_a - mu*c_b*q*v_b + c_c*r*v_c.
```

Its coefficients on P vanish exactly when

```
p=(1+d_a/c_a)/(1+mu), q=d_b/(mu*c_b), r=-d_c/c_c.
```

Every denominator is nonzero. The verifier compares these reconstructed
points and their gates with every saved test, including rejected
points. At a gated point, the first four coordinates of sZ-mu sY
are precisely its recovered K weights, compared with the saved weights.
The first seven moment equations hold by construction; the eighth
holds by rz-mu ry=0. Cancellation of the three P coefficients proves
that these are all eight moments of N on K. The producer's independent
first-four inversion also checked all eight residuals at each gated
point. No nonvanishing test discards zero fourth weights.

The verifier reconstructs the entire scalar fiber at every represented
weight point, each fiber-size histogram and every maximal fiber,
comparing all with the producer certificate. It also compares the
projected case counts and both gated and rejected test counts for
each partition. Thus the maximum is obtained from full coverage,
not a preview or selected positive rows.

Completed totals are 90/90 partitions, 64,350/64,350 support rows and
81,522 scalar tests. The 53,348 gated rows include 6,700 both-zero
rows and 1,580 rows with zero fourth weights. The exact partition
maximum histogram is {1:72,2:18}; maximum D is two against necessary
seven. Both complete failure arrays are empty, actual/required 0/0.
The complete producer summary, verifier counts and both empty failure
arrays were inspected with the shared JSON inspector's selected
`--full` values. Complete automated row replay establishes the table
checks; summaries alone do not. There are no seven-scalar survivors,
so no full M computation is needed. The verifier rejects a nonempty
seven-survivor set; it cannot certify an unchecked full M count.

### Arbitrary weights and original finite exclusions

Suppose a pencil in this restricted family has thirteen distinct
additional original finite relaxed recoveries. Audited L059's threshold
equivalence, using descent only at this threshold, forces rational
gated normalized weights, |M(w)|=13 and |D(w)|>=7. The complete
table maximum two contradicts this. Hence |R|<=12.

This uses L059's exact chart formula
|R|=|M(w) minus {rho/(1-rho)}| after the conditional descent. The
original chart may exclude one scalar and is never rationalized.
Both-zero lifts, zero fourth weights and scalar deduplication precede
the threshold argument. Neither support witnesses nor padded supports
are substituted for distinct finite parameters.

The sole direct mathematical input is audited L059. L060/L061 are
implementation precedents only; their unaudited bounds are not assumed.
Reuse the pre-existing EXPLORE assessment
`drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md`.
The precise standard recurrence citation reused through L059/L057 is
Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2, July 17, 2026, DR2 (`drc:lem-locator-recurrence`) and
DR6–DRC (`drc:thm-exact-compiler`), lines 2785–2935 of the
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
Its unchanged specialization is R=8,t=4, multiplier x and
eta_j=s_(j+1), with distinct nonzero labels. No standard theorem is
reproved, and this mutable source is not identified with ePrint
2026/1463. This is new local restricted coverage, not certified
originality or a claim of progress beyond the sources checked.

## Mathlib

The full restricted table exclusion and certificates: **not checked**.
Supporting finite-field arithmetic, Vandermonde invertibility and
finite-set counting: **not checked** for this step. No absence claim
or Lean verification is asserted.
