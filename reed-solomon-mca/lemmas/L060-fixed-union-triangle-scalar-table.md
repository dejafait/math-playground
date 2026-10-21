# L060 — Restricted fixed-union triangle table exclusion

## Hypotheses

Use audited L059's hypotheses and definitions of D(w), M(w), R.
Thus F=F_(97^20), C=RS[F,H,8], and the pinned cell is [1/4,5/16).
Here H=(1,8,12,18,22,27,33,47,50,64,70,75,79,85,89,96).
Restrict P=(a,b,c)=(1,8,12) and
U={1,8,12,18,22,27,33,47,50}. Allow every ordered partition
(Y,Z,W) of U minus P into three unordered pairs, defining base supports
{a,b} union Y, {a,c} union Z, {b,c} union W. The original finite
gamma_i are distinct, lambda!=0, and p,q,r range over F with
p(1-p)q(1-q)r(1-r)!=0. Neither weights nor original chart are assumed
rational for the recovery bound. Retain both-zero lifts, zero fourth
weights and all original finite exclusions.

## Conclusion

For these **restricted** assignments, the exact table calculation gives
|D(w)|<=2 for every w in (F_97 minus {0,1})^3. Its maximum is one
for 66 ordered pair partitions and two for the other 24. Consequently
|R|<=12 for this family, including extension-field weights and arbitrary
original charts.

This computational partial input awaits separate critical audit. It
does not cover arbitrary P or U, give the uniform triangle twelve bound,
or improve the global 11/q–16/q interval. Full M maxima below thirteen
are uncomputed; the necessary seven-scalar threshold has no survivors.

## Proof

### Complete restricted enumeration

Reproduction commands, relative to the notebook:

```
python3 scripts/triangle-recovery/fixed_union_table.py
python3 scripts/triangle-recovery/verify_fixed_union_table.py
```

The complete certificates are
`scripts/triangle-recovery/fixed-union-table.json` and
`scripts/triangle-recovery/fixed-union-table-verification.json`.
All arithmetic is exact modulo 97, with no random sampling.

There are binom(6,2)=15 choices for Y and binom(4,2)=6 remaining
choices for Z; W is then forced. These are all 90 ordered partitions.
Within-pair swaps leave L057's equations and supports unchanged; no
permutation of P, scaling symmetry or change of U is assumed. For
each partition all binom(13,4)=715 supports K disjoint from P are
generated, each nonbase. Compute c_x=product_(h in H minus U)(x-h).
The producer records complete L057 projected scalars and beta scalars.
Two nonzero projected scalars give one ratio, admitted for testing only
when mu!=0,-1; both-zero scalars give all 95 admissible rational mu;
exactly-one-zero gives none. Each weight point is computed from L059 (4).
Every tested point, including nongated points, is saved. Retain precisely
the points whose coordinates avoid 0,1; deduplicate mu at each point.
L059's two-direction table identity identifies these fibers exactly
with D(w). Empty fibers have count zero and need no generated row.

### Independent reconstruction of every entry

The verifier imports no producer code and uses neither support-polynomial
quotients, beta formulas nor L059's point formula. It reconstructs H,
P,U,c_x, verifies exact case-set equality without duplicates, and verifies
exact support-set equality without duplicates separately in each case.

For each K it constructs the 8-by-7 matrix with columns
v_x=(x,x^2,...,x^8)^tr, indexed by K followed by a,b,c. Its first
seven rows are invertible: their determinant is the product of the seven
nonzero distinct labels times their Vandermonde product. Solve these
rows for Y=sum_(y in Y)c_y v_y and Z=sum_(z in Z)c_z v_z, obtaining
coordinate vectors sY,sZ. Write ry,rz for their eighth-row residuals.
Then Z-mu Y belongs to the seven-column span exactly when rz-mu ry=0.
Both residuals zero permit all 95 scalars; exactly one zero permits none;
two nonzero residuals give rz/ry, excluding -1. This independently
reconstructs all projected zero cases and eligible ratios, which must
agree with the producer despite a possible quotient normalization factor.

Let d_a,d_b,d_c be the final three coordinates of sZ-mu sY. In
L057 (12), N adds P coefficients c_a[1-(1+mu)p], -mu*c_b*q,
c_c*r to Z-mu Y. Their cancellation is equivalent to

```
p=(1+d_a/c_a)/(1+mu), q=d_b/(mu*c_b), r=-d_c/c_c.
```

All denominators are nonzero. The verifier compares these solved weights
with every saved test, including every rejected gate. For a gated row,
the first four coordinates of sZ-mu sY are its K weights; P has been
cancelled. The first seven moment equations were solved and the eighth
residual is zero, so these weights satisfy all eight moments. The verifier
compares all four recovered coefficients and every saved residual. The
producer separately checks each gated row through first-four inversion
and all eight residual equations, without using the projected residual
as that check. No nonzero-fourth-weight filter is imposed.

The verifier reconstructs complete scalar fibers, their full histogram
and every maximal fiber for each case and compares them with the saved
certificate. Complete checked counts are 64,350 support rows, 84,144
scalar tests, 55,610 gated rows, 9,498 gated both-zero rows and 2,160
gated rows with a zero fourth weight. Actual/required failures are 0/0,
with the full empty failure arrays inspected. Case-maximum histogram is
{1:66,2:24}; maximum D is 2 against necessary threshold 7. There are
no seven-scalar survivors. These maxima and counts are exact assertions
checked by independent reconstruction of every test, not a preview.
The exact summary, complete counts and empty failures were inspected
using the shared JSON inspector. No full M test is needed on an empty
survivor set.

### Extension-field consequence and qualifications

If one restricted original pencil had thirteen distinct additional
finite relaxed recoveries, L059's threshold proof, using its audited
L058 descent input, would force w into F_97, |M(w)|=13 and |D(w)|>=7.
The checked |D(w)|<=2 contradicts this. Hence |R|<=12 for these
assignments. No rationality of the original infinity is assumed and no
E exclusion is lost: L059 establishes the exact original-chart relation
before this threshold implication. Lower-weight witnesses remain
admitted, and scalars are deduplicated before counting.

The sole direct mathematical input is L059. Seven-column inversion
independently checks the computation; it does not reprove a standard
recurrence or shortening theorem. The pre-existing EXPLORE coverage
`drafts/literature/2026-10-10-triangle-twelve-recovery-bound.md` and
its precise primary-source comparisons are reused through L059 with
unchanged hypotheses. This is restricted local progress, with no
certified originality asserted. Separate proof/code/certificate critical
audit, arbitrary label coverage, other patterns, extraction and challenge
definitions remain open. No actual thirteen-parameter violation is found.

## Mathlib

The full restricted table exclusion and computational certificate:
**not checked**. Supporting finite-field arithmetic, Vandermonde
invertibility and finite-set counting: **not checked** in this step.
No absence claim or Lean verification is asserted.
