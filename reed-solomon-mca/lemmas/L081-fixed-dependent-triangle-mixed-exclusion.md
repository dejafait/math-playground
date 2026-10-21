# L081 — No both-zero recovery at a full isolated anchor for one dependent triangle

## Hypotheses

Use L057's hypotheses: F=F_(97^20), H the order-sixteen subgroup of
F_97^*, C=RS[F,H,8], and the pinned four-omission cell. Fix the ordered
shared labels and singleton pairs to
\[
 P=(a,b,c)=(18,22,27),\quad Y=(1,96),\quad Z=(8,89),\quad W=(12,85).
\]
The original finite gamma_0,gamma_1,gamma_2 are arbitrary distinct
elements of F, lambda is arbitrary nonzero, and p,q,r range over F
with p(1-p)q(1-q)r(1-r)!=0. Retain zero recovered fourth weights,
all restored equations, and original exclusions mu!=0,-1 and E!=0.
Suppose there is an additional **full-weight isolated** recovery on
some four-subset K_* disjoint from P, as defined by L057.

## Conclusion

There is no additional both-zero recovery in this pencil, including
recoveries with zero fourth weights. In particular this fixed assignment
cannot attain L066's bound three while admitting the required anchor.

This is a computer-assisted restricted exclusion, supported by the two
complete certificates below. Its separate October 13 critical audit
found no mathematical defect in this restricted conclusion. It proves
neither uniform nonattainment for other labels nor the
triangle twelve bound, and does not change the global 11/q–16/q interval.

## Proof

### Assessed input and exact finite reduction

Use audited L057's necessary and sufficient recovery test and audited
L065's split-net classification. The ready assessment is
`drafts/literature/2026-10-13-isolated-anchor-both-zero-attainability.md`
(EXPLORE); it approves this one fixed-assignment complete test.
L066 is the bound whose sharpness is being tested, not an input to
this exclusion. L068/L080 and their different labels are not used.

The standard recurrence input is already imported and specialized in
L057: P. Chojecki, *Shortening Bounds for Reed–Solomon MCA*, author TeX
v9.2, July 17, 2026, DR2 (`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), source lines 2785–2935,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
reinspected by the assessment on October 13. It assumes distinct
weighted Vandermonde columns, nonzero multipliers and t<R. Here
R=8,t=4 and multiplier x!=0 at every x in H, exactly as in L057.
The mutable source is not certified identical to ePrint 2026/1463.
No general recurrence theorem is reproved. The work below computes
the actual simultaneous lifts not supplied by that theorem.

There are exactly binom(13,4)=715 possible anchor supports. For every
isolated support disjoint from P, L057 (7) fixes mu in F_97^*, and
(11) fixes all three weights p,q,r in F_97. These statements hold
even if the original chart and lambda are outside F_97. Discard
mu=-1, a weight in {0,1}, or an anchor with a zero fourth weight.
Every possible full anchor survives this finite list; no sampling of
weights is involved. The later E exclusion can only remove anchors.

For this assignment Y_2=X^2-1, Z_2=X^2-64, W_2=X^2-47, and
W_2=48 Y_2+50 Z_2 over F_97. The coefficients are nonzero and
sum to one. On V=H minus the nine labels the two-element fibers
of Y_2/Z_2 are exactly (33,64) and (47,50). L065's classification,
including the three two-original-pair supports before lift rejection,
therefore gives precisely these ten both-zero supports:
\[
\begin{split}
 &(1,8,89,96),\ (1,12,85,96),\ (8,12,85,89),\\
 &(1,33,64,96),\ (1,47,50,96),\\
 &(8,33,64,89),\ (8,47,50,89),\\
 &(12,33,64,85),\ (12,47,50,85),\ (33,47,50,64).
\end{split}
\]
They are also independently identified among all 715 supports by
the moment-span replay below. Thus none is omitted on the basis
of a projected candidate count or a failure of full fourth weights.

At each full-anchor weight point and each of these ten supports,
use L057 (9): if B is identically zero the lift is impossible;
otherwise its nonzero pivot fixes mu=-A_x/B_x. Check all three
restored equations and exclude only mu=0,-1. A consistent pivot
would automatically be in F_97 since A and B are prime-field.
The prohibited all-zero A,B branch is excluded by L057 under the
base-weight gates. Thus no extension-field scalar can evade the
complete prime-field linear tests. Leave E unrestricted at this stage:
this enlarges the eligible scalar set for every original chart.

### Complete producer certificate

Run
`python3 scripts/triangle-recovery/mixed_anchor_both_zero.py`.
The full certificate is
`scripts/triangle-recovery/mixed-anchor-both-zero.json`.
It saves every support's projected values and restored beta values,
all computed isolated weights and gates, every recovered anchor's
four weights and eight residuals, and every both-zero pivot/lift
at every retained weight point. It deduplicates eligible scalars.

The complete 715-row partition is 594 isolated, 111 one-zero and
10 both-zero. Among isolated rows, 56 have mu=-1, 36 fail base
weight gates, 102 have a zero fourth weight and 400 have full
fourth weight. The 400 full rows have 400 distinct weight points.
All 4,000=400*10 both-zero lift tests are executed, retaining zero
fourth weights if a lift were eligible. Their distinct-scalar
histogram is exactly {0:400}: **no** weight point has an eligible
both-zero scalar. The attained maximum is zero against the
requested threshold three. All anchor moment residuals vanish.

### Independent full-moment replay and coverage

Run
`python3 scripts/triangle-recovery/verify_mixed_anchor_both_zero.py`.
It reads every producer case, uses no producer functions, and saves
every replay case in
`scripts/triangle-recovery/mixed-anchor-both-zero-verification.json`.
It includes the producer SHA256 and the full failure array (empty).

For each support K it independently builds v_x=(x,...,x^8)^tr
and verifies rank seven of the columns indexed by K union P.
It determines projected zero membership by solving for the full
moment vectors Y and Z in that seven-column span. Thus the exact
both-zero and one-zero classifications are independently reproduced.
For an isolated row, [v_K,v_P,Y] is an invertible eight-column
matrix; solve
\[
 \sum_{k\in K}\omega_kv_k+\sum_{x\in P}s_xv_x+\mu Y=Z.
\]
In L057's numerator this means s_x=-c_xd_x, where
d_a=1-(1+mu)p, d_b=-mu q, d_c=r. Hence, after the scalar gates,
\[
 p=(1+s_a/c_a)/(1+\mu),\quad
 q=s_b/(\mu c_b),\quad r=-s_c/c_c.
\]
These are compared with every producer weight, all four recovered
weights and every full-anchor gate. All 715 supports and all 400
weight points agree. The replay also reconstructs the quadratic
dependency, the complete outside fiber partition, and the ten-support
split-net list, rather than assuming the old selected regression.

For each of the 4,000 both-zero lift cases independently write
N(mu)=N_0+mu N_1 from L057 (12). Invert the shifted four-point
Vandermonde on the first four moments to obtain omega_0,omega_1.
Then check **all eight** affine residuals
\[
 R_j(\mu)=\sum_{k\in K}(\omega_{0,k}+\mu\omega_{1,k})k^j
                         -(N_{0,j}+\mu N_{1,j}),\quad 1\le j\le8.
\]
A nonzero linear coefficient fixes the sole possible mu; all residuals
must vanish at it. With all linear coefficients zero, a nonzero
constant forbids every scalar; the entire-zero branch is checked
absent. This tests membership over F as well as F_97. The complete
eligible-scalar sets agree with the restored-equation producer,
and all 4,000 cases have no eligible scalar. The replay reports
actual/required support rows 715/715, lift tests 4000/4000, and
failures 0/0. The full evidence, not a JSON preview, is consumed
by this replay. Both implementations use Python and residue arithmetic;
this is independent recovery logic, not independent execution hardware.

Every actual full anchor is therefore among those 400 points, where
all both-zero lifts fail even before the original infinity exclusion.
Allowing arbitrary gamma_i and lambda, or changing the original chart,
cannot restore a failed chart-free lift. Same-support input failure and
the meaning of every admitted relaxed recovery are supplied by L057;
there is no admitted both-zero parameter to construct here. This proves
the stated restricted conclusion with explicit finite-computation
dependence. No larger label family or uniform strict bound is inferred.

### Separate critical audit (2026-10-13, step 194)

The approved REPRODUCTION audit checked the complete proof and both
entire programs against audited L057 and L065. No formula, conclusion,
or direct mathematical input required repair. This validates an existing
restricted computational input; it is not a stronger theorem or evidence
of originality beyond the sources already assessed.

**Extension-field and chart coverage.** All seven moment columns at
K union P are independent: their first seven entries form a shifted
Vandermonde with distinct nonzero nodes. When Y is outside this span,
adjoining it gives rank eight. Thus the isolated equation displayed above
has a unique solution over F, and its prime-field matrix and right side
force that solution into F_97. An isolated Z also lies outside the
seven-column span, so its solution has mu!=0. The extracted signs are
s_a=-c_a[1-(1+mu)p], s_b=mu c_b q, s_c=-c_c r, giving exactly the
three weight formulas above. Only mu=-1 must be discarded before those
divisions. The producer's projected ratio and restored beta formulas
match L057 (5), (6), and (11) with J=P, including their minus signs.
The 56 scalar exclusions, 36 base-weight exclusions, 102 zero-fourth-
weight rows and 400 full rows exhaust all 594 isolated rows. The
102 rows are excluded only as full anchors; no full-anchor hypothesis
is imposed on a prospective both-zero recovery.

The four producer coefficients omega represent N_K, not the unscaled
original error. L057 (14) multiplies them by lambda/(gE), nonzero
at every eligible original parameter, so this fullness test is exact
for arbitrary gamma_i and lambda. L057's bijection between finite T
outside the three base parameters and mu!=0,-1 with E!=0 justifies
every chart passage. Dropping E!=0 enlarges the tested set. It does not
rationalize the original chart or assert that its excluded point is
prime-field.

**Complete support classification.** L057 excludes both-zero supports
meeting P, so all of them occur among the 715 enumerated supports.
The producer's combinations and the verifier's complete ordered support
list agree exactly, not just in length. Seven-column span membership
independently gives the partition 594/111/10. The quadratic coefficients
are (48,50), and the complete V-fiber computation has precisely the
two double fibers (33,64) and (47,50). L065 therefore supplies six
one-original-pair supports, one union of outside double fibers, and
three two-original-pair supports. The verifier checks equality between
this entire ten-support family and the moment-based both-zero list.
The displayed list above agrees entry by entry. In particular, no
two-original-pair shape is silently omitted using its known lift failure.

**Every restored lift and rejection.** The producer's vectors A and B
are exactly L057 (9). Its nonzero-B pivot tests all three equations;
zero B with nonzero A forbids every scalar, while all-zero A,B is
excluded by L057's base-weight and sparse-uniqueness argument. The
independent replay instead inverts the first-four shifted Vandermonde
for N_0 and N_1 and tests every one of the eight affine residuals.
Four distinct nonzero nodes make both inversions valid. The RREF
implementation reduces all rows, detects inconsistent rows, and
returns unique solutions in every matrix used for this audit. No free
variable is used to choose an anchor or a fourth weight.

All 400 weight-point groups and their complete anchor-row lists agree;
each has exactly the ten distinct lift rows. All 4,000 producer systems
have a nonzero B pivot and a nonzero restored residual at the forced
scalar. Independently all 4,000 replay systems have a nonzero linear
residual coefficient and a nonzero residual at its forced scalar.
Thus every rejection is inconsistency, even before mu=0,-1 or E=0
are excluded. For each system, the pivot is in F_97 and any solution
over F would have to equal the pivot's prime-field root. A different
extension-field root, a constant-consistent system, and an entirely
zero system cannot escape these complete tests. Every empty scalar set
and its deduplication agree. No division by a recovered fourth weight
occurs, so possible zero fourth weights remain covered.

**Complete replay evidence.** Both reproduction commands above were
rerun successfully. The two program files and both full output files
have exactly their pre-audit SHA256 hashes. The verifier's embedded
producer hash matches the full current producer certificate. The
complete original failure arrays are empty. All 502 stored recovered
anchor rows have eight zero moment residuals; rejected base/scalar rows
are checked by the independent unique-solution and gate calculations.
The complete restored and replay rejection residuals were also checked,
not merely the reported maxima. Actual/required totals are 715/715
support rows, 400/400 full-anchor weight points, 4000/4000 lifts, and
0/0 failures. The maximum remains zero against attainment threshold
three. Full before/after hashes, partitions, rejection totals and failure
arrays are saved in
`scripts/triangle-recovery/mixed-anchor-both-zero-critical-audit.json`;
the pre-replay hashes are in
`scripts/triangle-recovery/mixed-anchor-both-zero-critical-audit-before.json`.
All load-bearing individual cases remain in the two complete original
certificates, whose content is unchanged.

The independent paths share Python, residue arithmetic and the same
mathematical field. This is an informal proof/certificate audit, not
formal verification or independent hardware. It closes only the fixed
assignment in the hypotheses; other labels, L066 sharpness, uniform
triangle twelve and arbitrary-family extraction remain unresolved.

## Mathlib

Full matching and supporting Mathlib coverage are **not checked**.
The proof uses L057's exact criterion, L065's classification and
finite-field linear algebra. These Python certificates are not Lean
proofs; no absence or formal-verification claim is made.
