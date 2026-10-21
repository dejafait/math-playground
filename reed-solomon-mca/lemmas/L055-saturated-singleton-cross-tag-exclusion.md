# L055 — A saturated singleton row excludes every other nonuniversal candidate

## Hypotheses

Use the complete gated local tau=1 setup of audited L043 over
F=F_(97^20), H={x in F_97^*:x^16=1}, C=RS[F,H,8], in the pinned cell
1/4<=delta<5/16. Write

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3},
    B={h,d,y_1,y_2,z_1,z_2}, O=H minus B,
    W(X)=product_(i=1)^3(X-w_i).

All nine labels are distinct. Retain arbitrary distinct original finite
gamma_i in F, lambda!=0, p*q*(1-p-q)*r*(1-r)!=0, and every L043
(4)–(7) gate. Count distinct original finite parameters, before the
nonzero recovered-weight gate (9). A nonuniversal candidate has some
four-support other than A_0,A_1,A_2,K_*; multiple witnessing supports
at the same parameter count only once. No rational original chart,
finite universal lift, twelve-count premise or equality is assumed.

Suppose three distinct such parameters have witnessing supports
K_i={b} union S_i, with one fixed b in {y_1,y_2,z_1,z_2} and
three-subsets S_i of O. Outside triples may intersect, and recovered
weights are initially allowed to vanish.

## Conclusion

There are exactly three distinct nonuniversal candidate parameters in
total. Every one is witnessed by a full-weight support tagged by b;
there is no fourth nonuniversal candidate of any support type.

Consequently, for every gated local pencil in this fixed-H scope, at
most eight distinct nonuniversal candidates have a witnessing support
{b} union S with b a singleton of B and S a three-subset of O. This
does not bound all nonuniversal candidates by eleven: candidates tagged
by h or d and candidates disjoint from B require further accounting.
It does not improve the global 11/q–16/q interval, extract a local triple
from arbitrary equality families, or resolve ABF26 identification.

The separate critical audit on 2026-10-10 verified the finite reduction
and complete certificates, finding no defect in the conditional count.
It corrected an indexed-weight transcription below; the programs already
used the correct weights. This is a local mathematical input beyond the
conclusions of the inspected sources, with no certified originality claim.

## Proof

### Audited equations and rational free weights

First take b=y_1. Audited L053 derives from all eight moments, using
L010's moment-kernel identity and L043's recovery equivalence,

    a_x(mu_i) f_i(x)=u_i W(x), x in B minus {y_1},       (1)
    a_y1=a_y2=-mu, a_z1=a_z2=1,
    a_h=q-mu*p, a_d=1-(1+mu)*r,
    f_i(X)=product_(s in S_i)(X-s).

It retains zero recovered weights. Precisely, the difference between
the B-supported normalized word n(mu_i) and its K_i representative
has eight moments zero. L010 identifies it with a polynomial of degree
at most seven; the seven roots O minus S_i and its nonzero value at
z_1 force its scalar product form. This is the already proved L053
reduction, not a new proof of an external recurrence theorem.

The standard recurrence specialization used in L043 and L053 is
Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2, July 17, 2026, source lines 2785–2935,
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler` (DR6–DRC),
including the inspected proofs and zero-direction cases,
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
The source is mutable and is not certified identical to ePrint 2026/1463.
Here redundancy is eight, support size four, labels distinct, column
multipliers x nonzero and moments shifted to sigma_(j+1). The source
supplies the fixed-support criterion, not this simultaneous finite count;
the computation below is needed for the stated difference.

Every evaluation of f_i and W on B is nonzero. Equations (1) force

    f_i(z_2)/f_i(z_1)=W(z_2)/W(z_1),
    u_i=f_i(z_1)/W(z_1),
    mu_i=-u_i W(y_2)/f_i(y_2),
    r=(1-u_i W(d)/f_i(d))/(1+mu_i).                   (2)

Thus u_i,mu_i,r belong to F_97. The exclusions mu_i!=0,-1 are
essential, and the original-chart formula in L043 is injective in mu.
Our three parameters therefore have distinct mu_i. W differs from
every S_i, since equality of the monic cubics would force mu_i=-1.
All four cubics lie in one ratio group. A gated common r is required.

Put R_i=u_i W(h)/f_i(h). The h equations are q-mu_i*p=R_i.
For two distinct scalars they uniquely force

    p=(R_2-R_1)/(mu_1-mu_2), q=R_1+mu_1*p.          (3)

All quantities on the right lie in F_97, so p,q are rational as well.
The third equation and p*q*(1-p-q)!=0 remain necessary. This is descent
of the three normalized weights only; gamma_i,rho,lambda are unrestricted.
It is specifically the shared h/d coupling absent from a single-tag
degree sum.

### Complete normalized saturated-row coverage

Scale labels by z_1^(-1). The new z_1 is 1 and z_2 ranges over the
other fifteen elements of H. Every monic cubic evaluation scales by
z_1^(-3), preserving all ratios in (2), R_i, and p,q,r. This only
normalizes label equations, not the original chart.

For the later all-support count this normalization also preserves full
moment membership. Write a=z_1^(-1), x'=a*x, and let Q' be the monic
degree-seven polynomial on the scaled complement of U. Then
Q'(a*x)=a^7 Q(x), so the normalized B-word satisfies
n'_(a*x)(mu)=a^7 n_x(mu). Its j-th moment is a^(7+j) times the old
j-th moment for j=1,...,8. Scaling any recovered word by the same rule
has exactly the same effect. The diagonal moment map has eight nonzero
diagonal entries, giving equivalence of all-eight-moment membership on
K and a*K. It preserves mu, zero coefficients, candidate exclusions and
distinctness. Thus the normalized all-support checks apply to the
original labeling, not just to necessary cubic ratios.

For each z=z_2, enumerate all 364 monic cubics with three distinct
roots in H minus {1,z}, grouped by f(z)/f(1). A relevant group has
at least four members. For each W in the group and every ordered pair
y_2,d outside {1,z} and W, enumerate the other group members S avoiding
y_2,d. Compute u,mu and r from (2), retaining every excluded-mu and
ungated-r rejection. Within each common r not in {0,1}, enumerate all
unordered three-member choices. Reject coincident scalars. For each
choice with distinct scalars, the possible h,y_1 labels must be distinct
and outside the union of its S_i, W and {1,z,y_2,d}. Test every such h
by (3), the third equation and the triple gate, and retain every possible
y_1 other than h. Disjoint S_i are already excluded by audited L053;
the independent replay also confirms that no common-r disjoint triple
occurs, so this branch removes no untested survivor.

This exhausts any assumed three-y_1-tag configuration, including
intersections of W with S_i and intersections between the S_i. It does
not require fourth weights nonzero, a universal lift or rational rho.
The resulting exact coverage is:

| Complete coverage | Actual | Required |
| --- | ---: | ---: |
| Cubic memberships | 5,460 | 5,460 |
| Ordered W,y_2,d configurations | 403,040 | 403,040 |
| Scalar/r cases | 1,213,312 | 1,213,312 |
| Common gated-r triple choices | 96 | 96 |
| h tests after distinctness and label-room gates | 288 | 288 |
| Gated normalized label/free-weight configurations | 8 | — |

These are eight normalized label/free-weight configurations, not eight
original pencils: the original chart and lambda still range over F.
The producer saves the complete cubic partitions, every scalar/r case,
every common-r triple and h test, and all survivors in
`scripts/simultaneous-recovery/cross-tag-saturated-result.json`.
It has a 55-second bound; the executed run finished all fifteen z values
with `complete=true` and no stop location. No timeout prefix is used as
complete coverage. Reproduce with
`python3 scripts/simultaneous-recovery/cross_tag_saturated.py`.

### All-support count and extension-field coverage

For each of the eight configurations, form the B-supported word

    n_(y_i)(mu)=-mu*c_(y_i), i=1,2,
    n_z1(mu)=c_z1, n_z2(mu)=c_z2,
    n_h(mu)=c_h(q-mu*p), n_d(mu)=c_d[1-(1+mu)r],

where Q(X)=product_(x in H minus (B union W))(X-x) and c_x=Q(x).
Its eight moments have the form m_0+mu*m_1 over F_97. For each of all
1820 four-supports K, invert the shifted Vandermonde matrix in moments
1..4 on K to recover affine coefficient vectors A_K+mu*V_K.
Comparing all remaining moments gives residual vectors R_K,S_K in
F_97^4. Full membership over F is exactly

    R_K+mu*S_K=0.                                    (4)

For every tested K, either S_K!=0 or S_K=0 and R_K!=0. In the latter
case there is no solution. In the former, a nonzero coordinate of S_K
forces the unique scalar mu=-(R_K)_j/(S_K)_j in F_97; all remaining
coordinates are checked. This excludes an untested extension-field
solution or an identically compatible support. No enumeration of
prime-field T is substituted for (4).

Exclude mu=0,-1 and supports A_0,A_1,A_2,K_*. These are precisely
the base/universal exclusions for the nonuniversal count; every
nonuniversal candidate from L043 must be in the remaining list by its
all-eight-moment equivalence. Conversely, (4) is used as an
overapproximation until the arbitrary original-chart gate E!=0 is
imposed. That gate can remove scalars and cannot add any. L043 makes
T=gamma_0+g*rho/E injective on retained scalars and supplies the actual
weights lambda*omega/(gE).

For every one of the eight configurations, exactly three supports and
three distinct nonexcluded scalars pass (4). All three supports have
the generating singleton tag, and all four recovered coefficients on
each are nonzero. Thus there are at most three nonuniversal candidates
for every original chart. The hypothesis already supplies three, so
there are exactly three and their actual weights are full.

The independent program
`python3 scripts/simultaneous-recovery/verify_cross_tag_saturated.py`
imports no producer routine. It verifies every partition against all
expected cubics, each ratio by cross multiplication, and exact case and
triple coverage. It checks every u,mu,r equation, excluded-mu decision,
free-label set, p,q solve, third residual and weight gate, including all
rejections. It compares the exact set of surviving configuration keys.
For each survivor it independently performs all 1820 Vandermonde and
residual computations, checks every admitted full eight-moment vector,
and compares all singleton rows with the producer's list. It saves the
complete 14,560 support records, including rejected supports, in
`scripts/simultaneous-recovery/cross-tag-saturated-verification.json`.
Both programs were executed. Coverage is 14,560/14,560; the maximum
nonuniversal scalar count is three; verification failures are zero.
The full replay consumed all load-bearing evidence, rather than relying
on a summary preview. L054's numerical example appears and is directly
checked as a regression case; its unaudited theorem is not a premise.

Exchanging y_1,y_2 covers the other y tag. To cover either z tag, use
audited L053's complete base swap: p'=q,q'=p,r'=1-r,lambda'=-lambda,
gamma'_0=gamma_1,gamma'_1=gamma_0,gamma'_2=gamma_2,mu'=1/mu.
It preserves every triple and finite gate and the actual original T,
with E'=-E/mu and normalized recovered weights omega'=-omega/mu.
In particular, zeros and nonzero weights, all nonuniversal candidates
and their distinctness are preserved. No rational original chart is
assumed. The proven conditional result therefore holds for every
singleton tag.

Finally let M_b be the set of distinct nonuniversal parameters with a
singleton-b witnessing support. If any |M_b|>=3, the conditional result
bounds the entire nonuniversal set by three. Otherwise every |M_b|<=2,
so |union_b M_b|<=sum_b |M_b|<=8. This includes possible multiple
witnessing supports and never counts them as distinct parameters.
The other support types remain outside this eight-count conclusion.

### Separate critical audit (2026-10-10)

The audit verified exactly the conditional conclusion above, using L010,
audited L043 and audited L053. It used neither the unaudited L054 theorem
nor full L044–L046, L040 or a universal-lift assumption. The prior stops
in ATTEMPTS/022–024 remain applicable to their respective failed routes.
The sole correction is to the displayed y coefficients: the two values
are -mu*c_(y_1) and -mu*c_(y_2), not equal values with an unindexed c_y.
Q may take different values at those labels. Both original programs
already use the separate coefficients, so no certificate or count changes.

**Reduction, descent and coverage.** L043 (7) supplies full moment
membership even before its nonzero-weight gate. L053 (1) therefore
applies to each hypothesized recovery with no full-weight assumption.
Each divided evaluation of W or f_i is nonzero since its roots avoid B.
The z and y_2 equations force u_i and mu_i in the prime field, with
mu_i nonzero; mu_i=-1 is excluded by the third original parameter.
The d equation then forces r in the prime field. Distinct original
parameters force distinct mu_i by the injectivity of L043 (5); they
also force distinct S_i, since (2) determines mu from S for fixed labels.
None of the S_i equals W. Thus all four distinct cubics occur in one
group of size at least four. Subtracting the first two h equations gives
(mu_1-mu_2)p=R_2-R_1; the nonzero difference justifies (3). The third
h equation and every p,q,r gate must still pass. No h/d coefficient
was cancelled merely on the basis of a triple gate.

Scaling labels by a=z_1^(-1) permutes H. Cubic evaluations scale by a^3;
Q evaluations scale by a^7. Consequently both the ratio equations and
the complete moment-span test are invariant, the latter by the invertible
diagonal map with entries a^8,...,a^15 on the eight moments. This retains
zero recovered coefficients and the same mu, and does not change rho.
After normalization every W and S lies among the 364 allowed cubics.
The actual ordered y_2,d pair occurs in its W loop, and the actual S_i
avoid both labels. Grouping the resulting candidates by their computed
r and choosing every unordered triple covers the hypothesized triple.
The labels h and y_1 must lie in the enumerated free complement and be
distinct. Solving for each h and retaining every other free label as y_1
therefore loses no actual case, even when the four cubics intersect.
The saved disjoint-triple branch has no occurrences on complete replay;
it is not an unverified pruning step. Requiring three distinct scalars
before solving for p handles every possible collision.

The producer and verifier were read in full. The verifier independently
reconstructs the allowed cubic set at every one of the fifteen z values,
checks unique membership and every ratio equation, then visits every
ordered W,y_2,d case and every eligible S index. It verifies each u,mu,r
by cross multiplication, including all excluded mu and r cases. The
exact ordered case traversal and final lengths preclude omitted suffixes.
For every common-r triple it checks its scalars, free-label set, h-test
list, two solved equations, third residual and gate. Exact survivor-key
equality plus the eight-record length excludes omitted or duplicate seeds.
Both original reproduction commands completed normally in this separate
audit. The producer completed all fifteen z values within its bound,
with no stop location. The replay checked 5,460 cubic memberships,
403,040 ordered configurations, 1,213,312 scalar/r cases (including
1,960 excluded-mu cases), 96 common-r triples and 288 h tests. Eight
configurations survived. Both certificates and all three original
programs, including the producer's helper, reproduced byte-for-byte;
the pre-replay hashes are in
`drafts/2026-10-10-saturated-singleton-audit-before.json`.

**Complete support evidence and extension fields.** In addition to the
original complete replay, run
`python3 scripts/simultaneous-recovery/audit_cross_tag_saturated.py`.
This program imports neither prior program. For each seed it consumes
the entire saved support certificate and verifies the exact ordered list
of all 1820 four-subsets. It reconstructs Q, the two normalized B-words
and their eight moments. For every stored intercept/slope weight vector
it checks the first four moments, which uniquely specify that vector by
the shifted Vandermonde determinant. It then checks every stored residual
directly against the last four moments. Independently it constructs f_K
and applies L043's cited recurrence criterion to both moment vectors.
It records all four constant and all four slope recurrence coefficients
and checks that their linear system gives the same classification as
the saved residual system for every support, including rejections.

These checks consume all 14,560 support records. There are 16
base/universal-excluded records, 14,512 inconsistent records, eight
constant-inconsistent records and 24 admitted records, with no
persistent supports.
For each of the eight seeds exactly three admitted records have distinct
scalars, full weights and the generating singleton tag. Every admitted
weight vector is checked on all eight moments. The independent complete
recurrence evidence is saved in
`scripts/simultaneous-recovery/cross-tag-saturated-audit.json`;
there are zero verification failures. No sampled record or summary
preview substitutes for these full checks.

For any support the complete residual system has coefficients in F_97.
If its slope is zero, its nonzero constant makes it inconsistent over
every extension. Otherwise one nonzero slope entry uniquely determines
mu in F_97; disagreement in another entry persists over F_(97^20).
The checks exclude a zero constant-and-slope system. Thus an extension
cannot supply an untested scalar or persistent support. Finite mu=0,-1
are the excluded second and third base parameters; the omitted normalized
point mu=infinity is the first base parameter. All other original finite
candidate parameters are covered by L043 (5), subject to E!=0. Removing
E=0 can only reduce the three-scalar upper bound. The hypothesis supplies
three eligible original parameters, so in its case all three counted
scalars survive and all recovered weights stay nonzero after multiplication
by lambda/(gE). No rationality of the original chart is inferred.

**Renaming and the eight bound.** Swapping y_1,y_2 leaves Q,Y,Z and
every gate unchanged. For either z tag, L053's audited base swap has
g'=-g, rho'=1-rho, mu'=1/mu, E'=-E/mu and t'=1-t. In particular
gamma'_0+g't'=gamma_0+gt is the identical original parameter. Its
n'=-n/mu and omega'=-omega/mu preserve all moment equations and zero
patterns; lambda'=-lambda makes the actual weights identical. The base
support exclusions are permuted and K_* is unchanged. This carries the
whole nonuniversal candidate set, not only its chosen three supports.
The conditional three-count therefore holds for all four singleton tags.
Finally, if any tag has at least three distinct candidates the whole
nonuniversal set has size three; otherwise each of the four tag sets has
size at most two. Taking their union gives at most eight even if a relaxed
candidate has more than one witnessing support. This neither bounds the
h/d and disjoint types nor proves the uniform eleven bound.

## Mathlib

The full conditional count and finite certificate: not checked in
Mathlib. Supporting kernel/Vandermonde and recovery inputs are L010,
audited L043 and audited L053. Their cited polynomial, recurrence and
finite-field inputs retain their stated hypotheses. No full matching
Mathlib theorem, absence result or Lean verification is claimed.
The new finite enumeration is required because the inspected source
compiler does not provide simultaneous saturated-row or cross-tag counts.
The separate informal audit above verifies this conditional count and
complete certificate; it is not a Lean formalization or a global bound.
