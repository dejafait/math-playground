# L112 — Residual gates exclude every disjoint third row for two fixed supports

## Hypotheses

Use F=F_(97^20), the order-sixteen subgroup H of F_97^*, dimension
eight, L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. The actual D and all coordinate locators are nonzero
polynomials, and both coefficient syndromes belong to U_S for
S={1,8,12,18,22,27,33}. Assume sixteen original finite bad parameters
and L104's t=0. All weights and the original finite chart are arbitrary
over F. Retain the inherited finite-certificate qualifications of audited
L109, L111 and L086.

Fix actual two-overlap supports A1={1,8,47,50} and
A2={12,18,64,70}. Suppose there is an actual two-overlap support A3
disjoint from A1 union A2. A support A=I union K has I subset S and
K subset J=H minus S, each of size two. Use exactly L109's six-by-21
block N_A and increasing S-pair column order.

## Conclusion

These hypotheses are contradictory. None of the thirty disjoint third
choices of L111 occurs in this fixed-two-row equality class.

More precisely, all 266 indexed pairwise-linear deficient fourth-row
occurrences retained by L111 fail L109's necessary gates over F and
every field extension of F_97. The 257 one-dimensional kernels each
have a decomposable generator. Each of the nine two-dimensional kernels
has exactly two decomposable projective points, also over extensions.
All 275 points have rank-one projection at every one of the four rows,
but their fourth-row intersection has lambda=0. None is a full fourth
recovery. The prescribed original chart cannot repair this failure.

This is a restricted computational exclusion. The separate step-305
critical proof/program audit below found no defect; its finite-computation
and inherited input qualifications remain essential.
No equality pencil is assumed to contain the two fixed supports or a
third row disjoint from them. Arbitrary t=0 profiles, seven-sets,
universal representation, the seven-coordinate fifteen bound and the
global interval 11/q–16/q remain unresolved.

## Proof

### Imported scope and the finite input

Use L109's exact necessary Plucker, projected-rank, lambda and full-weight
gates. Its shortening input is imported through L104 from J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[accepted manuscript, section 5, Definitions 5.1–5.2, Lemma 5.3 and the following shortening formula, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The field, sixteen distinct labels and nonzero multipliers are unchanged;
shortening the seven coordinates J minus K leaves dimension one and
nonzero retained multipliers. No standard distance, shortening or
exterior-algebra theorem is reproved. Only the finite specialization of
the already proved gates is calculated.

L111 supplies complete audited kernels, stable under scalar extension,
for all the residual occurrences. Its source is
`scripts/seven-coordinate/third-row-variation.json`, SHA-256
`34d6bb68537b8e5b153552801426c2f37266c96fa1446bb8ec89ae03885f85c2`.
The new calculation verifies this source's field, column order and empty
failure list, matches the complete residual index set with no duplicate,
and recomputes every saved basis residual against the full four-row
stack. Kernel completeness is imported from audited L111, rather than
inferred from these residuals alone. Occurrences are not deduplicated
as unordered four-support families.

### Complete projective Plucker test

For a one-dimensional kernel its sole projective point is the saved
generator b0 up to scalar. All 35 Plucker equations vanish at each of
the 257 generators. For a two-dimensional kernel use the complete
projective parameterization p(s,t)=s*b0+t*b1, with (s,t)!=(0,0).
For each increasing quadruple a<b<c<d in S compute the coefficients of

    p_ab*p_cd - p_ac*p_bd + p_ad*p_bc.

In each of the nine kernels every such homogeneous quadratic is
c_abcd*s*t, and at least one coefficient c_abcd is nonzero in F_97.
All 35 coefficient triples are retained, not merely selected evaluations.
Consequently their simultaneous zero set over any extension is exactly
[s:t]=[1:0] or [0:1]. This includes infinity and excludes all other
extension-field directions without a rational-point sampling assumption.

As an additional exact certificate, on s=1 the program computes the
monic gcd of all the quadratics in t, together with 35 polynomial Bezout
coefficients whose combination equals that gcd, and checks divisibility
of every quadratic. In all nine cases the gcd is t. Thus the affine root
is exactly t=0; the direct homogeneous coefficient check supplies infinity.
There is no whole-line or quadratic-extension branch left untested.
The projective counts are therefore 257+2*9=275.

### Complete recovery-gate test

For each nonzero decomposable p choose the first nonzero p_ab. Extend p
antisymmetrically and reconstruct the independent pair from L109:

    u_x=p_xb/p_ab,  v_x=p_ax.

Every entry of u wedge v is checked against p. For each of the four
supports form L109's four quotient covectors Q_A. Compute Q_A*u and
Q_A*v and all six minors. In all 1,100 row tests the minors vanish and
at least one of the eight quotient entries is nonzero; the projected
rank is exactly one, with no rank-zero branch discarded.

If n is the first row with (Q_A*u)_n or (Q_A*v)_n nonzero, set

    alpha=-(Q_A*v)_n, beta=(Q_A*u)_n, h=alpha*u+beta*v.

The vector h is nonzero, Q_A*h=0, and it spans the unique intersection
line. With z the least element of S minus I and
g_K(X)=product_(y in J minus K)(X-y), compute

    lambda=h_z/g_K(z),
    e_i=h_i-lambda*g_K(i) for i in I,
    e_k=-lambda*g_K(k) for k in K.

All g_K(z), g_K(i) and g_K(k) here are nonzero by distinctness of
the sixteen labels. Every outside-overlap identity h_x=lambda*g_K(x)
is checked. For every rank-one row, including failed full-weight rows,
all eight shifted moments of h-e vanish. The program records lambda,
both overlap weights, all four error weights, all eight residuals and
every failed gate. The exact aggregate results are:

| I3 | K3 | Occurrences | Decomposable points | Fourth-row lambda=0 |
| --- | --- | ---: | ---: | ---: |
| {22,33} | {79,89} | 101 | 110 | 110 |
| {22,33} | {85,89} | 55 | 55 | 55 |
| {27,33} | {79,96} | 55 | 55 | 55 |
| {27,33} | {85,96} | 55 | 55 | 55 |

Thus every candidate fails the nonzero-lambda condition at its fourth
row. Across all rows there are 550 zero-lambda failures and 550 zero
overlap weights; these are separate failed gates, not counted events.
There are no intrinsic survivors. The required count is zero survivors,
which is attained after complete projective coverage, rather than merely
after checking base-field values of a free parameter.

The finite-direction condition is retained explicitly: if the prescribed
original basis is u_original=A*u+B*v, v_original=C*u+D*v with AD-BC!=0,
then h has original first coefficient
(D*alpha-C*beta)/(AD-BC). Finiteness requires D*alpha-C*beta!=0, and
the actual error is divided by that first coefficient. Every row's
linear gate in C,D is saved. No original basis is supplied by a
support-only kernel, and no new chart is substituted for it. Because
lambda=0 is invariant under nonzero scaling, every candidate fails in
every original chart, even if its direction is finite. Thus chart
unspecifiedness creates no gap in this exclusion.

### Exact certificates and independent reconstruction

Reproduce the full certificate with
`python3 scripts/seven-coordinate/residual_kernel_gates.py`.
The complete bases, indices, 35 coefficient triples per occurrence,
Bezout certificates, projective points, reconstructed planes and all
1,100 row gates are in `scripts/seven-coordinate/residual-kernel-gates.json`.
No failures were reported.

Same-step supplementary verification is
`python3 scripts/seven-coordinate/verify_residual_kernel_gates.py`;
full evidence is in `scripts/seven-coordinate/residual-kernel-gates-replay.json`.
It imports no producer routine. It compares all 266 occurrences with
the audited source, and recovers every homogeneous coefficient using
direct Plucker values at (1,0),(0,1),(1,1),(1,-1), with the mixed
coefficient obtained by division by 2, which is nonzero in characteristic
97. It checks every Bezout combination and the complete st-only pattern.

For each of the 275 points it checks that the seven-by-seven alternating
matrix has rank two, uses its last nonzero coordinate pair to construct
a differently scaled basis of the same plane, and checks proportionality
of all wedge entries. It obtains g_K values independently by differentiating
X^16-1=g_K(X)*product_(y in S union K)(X-y): at x in S union K,

    g_K(x)=16*x^15/product_(y in (S union K) minus {x})(x-y).

The numerator and denominator are nonzero. It takes the greatest
observed label as pivot and uses ratio quotients
h_x/g_K(x)-h_z/g_K(z). All 1,100 reconstructed intersection lines agree
projectively with the producer. All projected ranks, lambda-zero flags,
zero-weight flags and failed-gate lists agree; all 8,800 full-moment
residuals vanish. The original-chart linear inequalities are checked
against the saved basis coordinates. There are no failures.

Both programs still share Python, the same residue field and audited
source bases. This is finite-computation evidence with independently
constructed gates, not a proof-assistant verification or the separate
critical audit required before stronger reliance on the new result.

### Consequence for actual equality

Suppose the three actual supports in the hypotheses exist. L109 gives
at least twelve distinct actual two-overlap rows at t=0 equality, so
choose a fourth different from the three selected rows. Audited L086
makes it pairwise linear with them. If A3 is one of L111's twenty-six
excluded choices, there is already a contradiction. For any of the four
remaining choices, L111's complete fourth-row list says either the
four-row stack has rank 21, impossible for the nonzero equality wedge
by L109, or it is one of these 266 occurrences. In the latter case
L109 requires a decomposable kernel vector with rank-one projections,
nonzero lambda and both nonzero overlap weights. The complete calculation
above excludes every such vector, also over F. This is the contradiction.

Only the necessary direction of L109 is used. Its r>=6 converse is not
applied to four rows, and no local survivor is promoted to nonpersistence,
t=0 or a sixteen-event construction. ATTEMPTS/041's failure of uniform
rank-21 extrapolation remains valid; these kernels really do have lower
rank, and the new exclusion uses their previously untested weight gates.
The unchanged EXPLORE assessment is
`drafts/literature/2026-10-17-seven-coordinate-syndrome-bound-review.md`.
This is REPRODUCTION of a known local gate mechanism, not a claim of
originality or a global sharp bound beyond the checked literature.

### Separate critical audit, 2026-10-18

Step 2026-10-18-mca-305-residual-gates-critical-audit checked the entire
proof, both complete residual-gate programs and the producer's imported
support-block module. The unchanged EXPLORE assessment is
`drafts/literature/2026-10-18-residual-kernel-gate-audit-review.md`.
It reuses the inspected Hall/shortening sources with their precise
citations above; no changed source hypothesis or new standard theorem
is needed. L109's full proof and audit, L111's complete classification
and audit, L104's exact recovery and equality balance, and L086's exact
hypotheses and canonical audit were inspected. ATTEMPTS/041's rank-only
stop remains valid. No mathematical error or changed dependency was found.

The standalone audit imports neither existing gate program nor a producer
module. Reproduce it with
`python3 scripts/seven-coordinate/audit_residual_kernel_gates.py`.
Full evidence is in
`scripts/seven-coordinate/residual-kernel-critical-audit.json`.
The L111 source hash is exactly the one stated above and equals both
before/after hashes of its prior successful producer audit. This ties
reuse of L111's complete coverage to the audited source, rather than
assuming completeness from vanishing residuals. The current audit also
reconstructs the full 24-by-21 stack for each of the 266 occurrences.
Polynomial coefficient multiplication and Horner evaluation on all H
rebuild every g_K; its zeros are exactly J minus K. Direct covectors and
exterior rows rebuild the stack in the specified column order.
Gauss-Jordan elimination computes every rank and the complete normalized
nullspace afresh. Its basis agrees entry by entry with L111 and this
certificate, is independent, and annihilates all 24 rows. Rank-nullity
therefore certifies completeness, also after scalar extension. All 266
indices match the entire linear deficient list once and in order, and
all four supports at every occurrence are pairwise linear.

All 9,310 homogeneous coefficient triples (35 per occurrence) are
recomputed by direct expansion. The 257 point kernels satisfy every
Plucker equation. For each of the nine line kernels, every quadratic
is c*s*t with at least one c nonzero. Since these are equations over a
field, their simultaneous projective zero set over every extension is
exactly [1:0],[0:1]. Independence of the two saved basis vectors remains
true after extension, so this parameterization loses no projective
direction. All 35 Bezout summands per occurrence are independently
multiplied and added; the sums are the saved affine gcd, t in each
line case. No whole-line, nonprime root or infinity branch is discarded.
All 275 resulting alternating matrices have rank two, and an independent
row-space basis spans the same plane as the producer's reconstructed
pair. The producer's wedge agrees exactly with the saved bivector.

For every candidate and each row, the audit solves all five equations

    alpha*u_x+beta*v_x-lambda*g_K(x)=0,  x in S minus I,

as a homogeneous five-by-three system. Its rank is two, and its complete
one-dimensional kernel has (alpha,beta) nonzero. This is a different
recovery path from choosing a projected quotient pivot. Every projected
restriction has rank one, and the recovered intersection agrees with
the producer's nonzero vector by an explicitly saved nonzero scale.
All lambda values and all four error weights agree by that same scale;
every failed gate and overlap-weight flag agrees. The audit checks the
full sixteen-coordinate polynomial identity h-e=lambda*g_K as well as
all eight shifted moments, giving 17,600 identity entries and 8,800 zero
moment residuals across 1,100 row systems. At every fourth support an
additional direct check finds that the restriction of the reconstructed
plane to S minus I has rank one. Its one-dimensional kernel constructs
a nonzero vector supported on I. The unique row intersection is therefore
this line and has lambda zero, independently of a recovery-pivot formula.
All 275 fourth-row failures are confirmed. The per-seed counts agree with
the complete table above, and no intrinsically passing point remains.

The prescribed-chart gate has the correct basis transformation. Writing
h=alpha*u+beta*v=x*u_original+y*v_original gives
x=(D*alpha-C*beta)/(AD-BC). All stored coordinates reproduce h and their
saved linear inequalities have exactly these coefficients. If x is zero,
the direction is omitted in that original chart. If x is nonzero, the
actual representative and its lambda are divided by x. Either way,
lambda zero cannot become a full four-error under any invertible basis
change or nonzero extension-field scaling. Thus a rational reconstructed
plane does not rationalize or replace the arbitrary original chart.

For the equality consequence, L109 already supplies independent lift
coefficients and 12<=r<=14 distinct actual two-overlap rows, with fullness
established before row counting. The three fixed rows have a distinct
fourth actual row. L086 applies to the same F,H,k, pinned event, actual
polynomial nonpersistence and sixteen original finite bad parameters,
with all its inherited audited finite-certificate inputs retained.
Thus this fourth row is in L111's enumerated pairwise-linear list.
The 26 excluded third seeds contradict rank immediately. For the other
four, a full-rank fourth stack contradicts the nonzero wedge; every
remaining fourth stack is one of the 266 audited occurrences, whose
entire extension-field decomposable locus fails the necessary full-weight
gate. Only L109's necessary direction is used. No four-row converse,
universal pair extraction or disjoint-third extraction is invoked.

Both original programs exited successfully and reproduced their entire
artifacts byte for byte. The source and all prior artifacts are preserved.
Both paths still share Python and exact integer/residue arithmetic; this
is not proof-assistant verification, and L086/L109/L111's inherited
finite-certificate qualifications are not removed or all rerun. The audit
validates this reproduced restricted input without adding a new bound or
claiming originality beyond the sources checked. The mathematical argument
and direct dependencies are unchanged; PROOF.md and DAG.md need no edit
for audit status alone. This canonical audit supersedes their pending-L112
audit wording. Arbitrary profiles, seven-sets, universal representation,
the seven-coordinate fifteen bound and challenge qualifications remain
unresolved.

## Mathlib

Full matching residual-kernel classification and fixed-two-row exclusion:
**not checked**. Supporting Plucker, exterior-power, rank and finite-field
coverage: **not checked anew**; the canonical inputs retain their own
qualifications. Unknown availability is not evidence of absence. The
explicit finite-computation dependence and inherited input qualifications
remain after the separate critical audit above.
