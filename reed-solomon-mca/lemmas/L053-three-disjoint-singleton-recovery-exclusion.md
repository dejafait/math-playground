# L053 — Three same-singleton recoveries cannot have disjoint outside triples

## Hypotheses

Use the complete gated local tau=1 setup of L043 over F=F_(97^20),
H the order-sixteen subgroup of F_97^*, and C=RS[F,H,8] in the pinned
cell 1/4<=delta<5/16. Thus the nine labels in

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3}

are distinct. Set B={h,d,y_1,y_2,z_1,z_2}, O=H minus B,
Q(X)=product_(x in H minus (B union {w_1,w_2,w_3}))(X-x),
c_x=Q(x), and W(X)=product_(i=1)^3(X-w_i).
Retain distinct original finite gamma_i, lambda!=0,
p*q*(1-p-q)*r*(1-r)!=0, and every L043 (4)–(7) gate.
These quantities range over F; no rational original chart is assumed.

Suppose three distinct additional nonuniversal finite candidate parameters
have witnessing supports K_i={b} union S_i, i=1,2,3, where b is one
fixed singleton label in {y_1,y_2,z_1,z_2}, S_i is a three-subset of O,
and the recovered weights may vanish. In particular retain mu_i!=0,-1,
E(mu_i)!=0 and exclusions of all three base parameters. Do not assume
L043 (9), a twelve count, a finite universal lift, rational free weights,
or equality completion.

## Conclusion

The three outside triples S_1,S_2,S_3 cannot be pairwise disjoint.
This is uniform over the specified fixed H, every labeling, arbitrary
extension-field weights and the original finite chart. It is a finite
conditional obstruction, not the uniform eleven bound or a global
interval improvement. It leaves triples with outside intersections,
all other distributions of tags, arbitrary extraction and the
challenge-definition gap unresolved. A separate critical audit on
2026-10-10 found no defect in this conditional exclusion; its full
reduction, renaming and certificate checks are recorded below.

## Proof

### Full-moment equations, including relaxed recovery

First take b=y_1; exchanging y_1,y_2 handles the other y tag.
L043 supplies a word n(mu) on B with coefficients

    n_x=c_x*a_x(mu),
    a_y1=a_y2=-mu, a_z1=a_z2=1,
    a_h=q-p*mu, a_d=1-(1+mu)*r,

whose eight moments equal those of the recovered word omega on K.
This is full membership before the fourth-weight gate. The precise
standard recurrence input already specialized there is Przemek
Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author TeX
v9.2, July 17, 2026, source lines 2785–2935,
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler`
(DR6–DRC), inspected in the reused assessment:
[author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
This mutable source is not certified identical to ePrint 2026/1463.
Here it applies to redundancy eight, support size four, distinct labels,
nonzero column multipliers x and shifted moments sigma_(j+1).
Its fixed-support compiler does not state the simultaneous exclusion
below. No recurrence theorem is reproved.

By L010's kernel identity, n-omega is the evaluation of a polynomial
P of degree at most seven. It vanishes on O minus S, seven labels.
It is nonzero because the three singleton labels other than y_1 lie
outside K and have nonzero n coefficients. Consequently, with
f_S(X)=product_(s in S)(X-s), the factor theorem gives

    P(X)=u product_(o in O minus S)(X-o), u!=0.

At x in B minus {y_1}, P(x)=c_x*a_x(mu). Since
product_(o in O)(X-o)=Q(X)W(X), and Q(x),f_S(x) are nonzero there,

    a_x(mu) f_S(x)=u W(x), x in B minus {y_1}.          (1)

This remains necessary even when omega has zero coefficients. It uses
the complete eight moments, not just projected compatibility.

For each i apply (1) at z_1,z_2,y_2,d. The z equations force

    f_i(z_2)/f_i(z_1)=W(z_2)/W(z_1),
    u_i=f_i(z_1)/W(z_1),
    mu_i=-u_i W(y_2)/f_i(y_2).                         (2)

All evaluations divided by here are nonzero, since the roots of W
and the S_i lie outside B. They belong to F_97. Thus these u_i and
mu_i belong to F_97 without imposing any descent hypothesis.
L043 (5) is injective in mu for the unchanged chart: equal T gives
equal E, and rho-1!=0 then gives equal mu. Hence the three mu_i are
distinct. If W has the same roots as any S_i, monicity gives u_i=1
and mu_i=-1, excluded. W is therefore a fourth distinct cubic in
the common ratio group.

The d equations in (1) now force

    r = r_i := (1-u_i W(d)/f_i(d))/(1+mu_i), i=1,2,3.  (3)

The denominators 1+mu_i and f_i(d) are nonzero. Each r_i is rational;
equality over F is the same as equality in its prime field. Thus even
extension-field choices require one common r_i not in {0,1}.
The computation below proves that this necessary condition never holds
for three pairwise-disjoint S_i. The h equations, p,q and E gates are
not needed for this overapproximation; dropping them cannot invalidate
a rejection. No rationality of gamma_i, rho, lambda or the original
excluded direction is used.

### Complete finite test of the necessary condition

Scale all labels by z_1^(-1) in H, so the distinguished z labels become
1,z with z in H minus {1}. This changes every cubic evaluation by the
same scale factor z_1^(-3). Ratios in (2), u_i, mu_i and (3) remain
unchanged. This normalization acts only on label equations; it does
not assert a projective change of the original finite chart.

For each of the fifteen z values enumerate all 364=binom(14,3)
monic cubics with distinct roots in H minus {1,z}, grouping them by
f(z)/f(1). Every possible S_i and W belongs to this enumeration.
A relevant group has at least four members because W differs from
each S_i. Within each group enumerate all unordered triples of members
whose root sets have union nine. Their triples are pairwise disjoint
and their complement in H minus {1,z} has five labels. The distinct
y_2 and d must lie in that complement. Enumerate every ordered choice
of them, and every remaining member W whose roots avoid y_2 and d.
This deliberately ignores the additional requirements that h,y_1
also avoid W: it only enlarges the tested family.

For each case compute (2). Reject if a mu_i is -1 or two mu_i coincide;
otherwise compute (3) and reject if the three r_i differ or their
common value is 0 or 1. No mu_i can be zero because all factors in
(2) are nonzero. The exhaustive result is:

| Complete test | Actual | Required coverage |
| --- | ---: | ---: |
| Cubic memberships across fifteen z values | 5,460 | 5,460 |
| Disjoint three-cubic choices in groups of size at least four | 704 | 704 |
| Choices of W,y_2,d tested | 28,688 | 28,688 |
| Excluded or colliding scalar cases | 504 | — |
| Inconsistent or ungated r cases | 28,184 | — |
| Cases with three distinct eligible mu and common gated r | 0 | 1 for a witness |

Reproduce with `python3 scripts/simultaneous-recovery/three_singleton.py`.
The full certificate is
`scripts/simultaneous-recovery/three-singleton-result.json`: all cubic
groups, all 704 disjoint triples, all 28,688 tested cases and their
u,mu,r values or excluded-scalar reason are saved, not merely totals.
The producer's later h and full-moment witness branches are never reached
and supply no premise for the exclusion.

Run `python3 scripts/simultaneous-recovery/verify_three_singleton.py`.
The verifier checks all fifteen partitions against all expected cubics,
checks every membership by f(z)=ratio*f(1), independently enumerates
all disjoint triples and every W,y_2,d case, and compares exact sets
with the saved records. It checks every u,mu,r equation by cross
multiplication, rather than using the producer's inversions. Distinct
case keys and exact coverage are checked, including rejected cases.
It verifies the actual/required counts above with no failures, saving
`scripts/simultaneous-recovery/three-singleton-verification.json`.
Both checks were executed; the full verification result and all
load-bearing case values were checked through this complete replay.

The enumeration covers every necessary configuration, and every one
fails (2)–(3) or a retained scalar/r gate. This contradicts the assumed
pairwise-disjoint three-y-tag recovery.

Finally interchange base indices 0 and 1 to handle a fixed z tag.
The local setup has new Y=old Z, new Z=old Y, new p=q, new q=p,
new r=1-r, and new lambda=-lambda; the prescribed finite parameters
are merely reordered. All triple gates remain valid. The nonuniversal
scalar transforms to mu'=1/mu, which preserves the exclusions of 0
and -1 and distinctness. Each actual recovery and its original
finite parameter is unchanged. Thus the same y-tag argument applies
to the renamed setup. This completes the conditional exclusion.

### Separate critical audit (2026-10-10)

The audit reused the approved standard inputs and checked the complete
proof and both programs. No new theorem beyond L053's conditional scope
is asserted. In particular, this is not an audit of every result on the
route to eleven, nor a proof that three same-tag recoveries are impossible
when their outside triples intersect.

**Full moments and scalar gates.** L043 (7) puts N_K in the K-span
before its nonzero-weight gate. Thus n-omega has all eight moments zero,
including when some omega coefficients vanish. L010's kernel identity
gives a degree-at-most-seven polynomial. The seven distinct labels of
O minus S are roots, while at either z label its value is c_z!=0.
The polynomial is therefore exactly a nonzero scalar times their monic
degree-seven product. At every x in B, Q(x), W(x) and f_S(x) are nonzero:
their roots lie outside B. Cancelling Q(x) proves (1) without cancelling
a possibly zero h or d coefficient. Equations (2) then determine nonzero
u and mu in F_97. If W=S, the same equations force u=1 and mu=-1,
which is excluded. In (3), 1+mu is nonzero; hence r is uniquely determined
in F_97. Equalities or inequalities between these prime-field values
persist in F. No original parameter, rho, lambda, p or q has been assumed
rational. In L043 (5), g*rho!=0 and E!=0; equal T implies equal E,
and rho-1!=0 then implies equal mu. Conversely equal mu implies equal T.
Thus counting distinct retained scalars correctly respects distinct
original finite parameters.

**Both tag renamings and the original chart.** Exchanging y_1,y_2
leaves U,Q,Y,Z,p,q,r,lambda and every base support unchanged. It only
renames the chosen tag and the other y label, so the argument applies
with either tag. For a z tag, swap indices 0 and 1, with primes denoting
the renamed quantities. Then

    gamma'_0=gamma_1, gamma'_1=gamma_0, gamma'_2=gamma_2,
    g'=-g, rho'=1-rho, alpha'_i=-alpha_(pi(i)),
    lambda'=-lambda, p'=q, q'=p, r'=1-r,
    Y'=Z, Z'=Y, mu'=1/mu, E'=-E/mu,

where pi swaps 0,1 and fixes 2. The formulas for alpha and lambda
show that every actual base weight is unchanged. All original triple
gates are preserved, including 1-p'-q'=1-p-q. For a fixed K use the
same left-kernel basis in L043 (3), since h,d and K are unchanged.
Its two projected vectors interchange, remain nonzero and proportional,
and have ratio mu'=1/mu. In particular the system stays nonuniversal,
distinct scalars remain distinct, mu'!=0,-1 and E'!=0. With
t=rho/E, direct substitution gives t'=rho'/E'=1-t and

    gamma'_0+g'*t'=gamma_0+g*t=T.

This is an identity in the unchanged original affine chart, even for
nonrational rho. On B the renamed normalized word is n'=-n/mu:
the y,z coefficients interchange, the h coefficient is p-q/mu,
and the d coefficient is r-(1-r)/mu. Consequently N'=-N/mu and
omega'=-omega/mu. The missing-column equations (6)–(7) are preserved
with beta'=-beta/mu; contained shared columns impose no extra gate.
Moreover lambda'*omega'/(g'*E')=lambda*omega/(g*E), so actual
recovered weights, including their possible zeros, are unchanged.
The same finite T still differs from all three reordered gamma_i.
After this swap, either former z tag is a y tag already covered above.

**Complete finite coverage.** Multiplication by z_1^(-1) is a
bijection of H and multiplies every monic cubic evaluation by
z_1^(-3). It therefore preserves (2)–(3), all disjointness and all
scalar gates; no transformation of the syndrome pencil is needed.
The producer covers all fifteen remaining choices of z. Its ratio
groups partition all three-subsets of H minus {1,z}. Nonzero cubic
evaluations at 1,z give a unique nonzero ratio. Since W differs from
each of three distinct disjoint S_i, relevant groups have at least
four members. Nine used labels leave five available labels for the
ordered pair (y_2,d). The actual W is in that same group and avoids
both labels. Thus every actual configuration occurs among the saved
cases, even when W intersects one or more S_i. Omitting h,y_1 and
their restrictions, as well as the h equations and E gate, enlarges
this necessary-condition test. It cannot remove an actual configuration.

The independent verifier checks every cubic's allowed roots, unique
membership and ratio equation, rather than assuming the producer's
partition. It checks every group ratio is distinct, and exact coverage
of all 364 cubics for each z. From these validated partitions it
enumerates every disjoint unordered triple and every eligible W,y_2,d
choice. Duplicate saved keys are rejected; exact key-set comparisons
exclude both omissions and extraneous triple/case records. For every
case it checks the unique u,mu values by cross multiplication and
nonzero ranges. Scalar rejections are checked before division by 1+mu.
For all other cases, cross multiplication verifies all three r values,
and the verifier requires either disagreement or a common value in
{0,1}. Thus no claim rests only on the producer's counters or on samples.

Both reproduction commands above completed normally in this separate
audit. All 5,460 memberships, 704 triples and 28,688 cases passed the
verifier: 504 scalar rejections and 28,184 inconsistent/ungated-r
rejections, zero common gated r, and no failures. The existing result
and verification certificates reproduced byte-for-byte, as did the
unchanged programs; pre-replay SHA-256 values are saved in
`drafts/2026-10-10-three-singleton-audit-before.json`. The complete
case evidence was consumed by the checked verifier, not inferred from
a bounded preview. The unused producer witness branch is not relied on.
This validates precisely the fixed-H exclusion stated here, retaining
zero recovered weights and arbitrary original finite charts.

## Mathlib

Full matching theorem and supporting finite-field enumeration: not
checked. L010's kernel identity and L043's complete reduced recovery
criterion are the informal mathematical inputs. No Mathlib absence or
Lean verification is claimed. The fixed-H certificate is essential;
this does not assert an arbitrary-domain theorem or originality beyond
the sources checked. Supporting polynomial factor/root statements from
the reused inspection are `Polynomial.mul_divByMonic_eq_iff_isRoot`
and `Polynomial.dvd_iff_isRoot` in
[Div.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Div.lean#L566),
and `Polynomial.card_le_degree_of_subset_roots` in
[Roots.lean](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Polynomial/Roots.lean#L121).
Their ring/domain hypotheses hold over F; the nonzero-polynomial
hypothesis was checked above. These were inspected on mutable master
2026-10-08, without a pinned commit or Lean compilation; they do not
verify the enumeration. The separate informal audit found no defect.
