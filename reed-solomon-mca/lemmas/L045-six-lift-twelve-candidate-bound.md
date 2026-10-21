# L045 — Six-coordinate lift bounds relaxed candidates by twelve

## Hypotheses

Use the entire local tau=1 setup of L043 over F=F_(97^20), with
H of order sixteen in F_97, k=8, and 1/4<=delta<5/16. In particular,

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3}

have nine distinct labels. The three original finite gamma_i are
distinct, lambda!=0, and p*q*(1-p-q)*r*(1-r)!=0. Retain L043's
c_x, Y, Z, v_x, g, rho, E and K_*. No rationality of p,q,r,
rho, gamma_i or the original excluded direction is assumed.

Let R be the distinct original finite parameters admitted by L043
(4)–(7) on at least one four-set K other than A_0,A_1,A_2,K_*.
Keep every quotient case and all finite-parameter exclusions exactly
as there. The recovered fourth-weight nonvanishing gate (9) is not
required. Thus R counts parameters, not supports or equations.
Put B={h,d,y_1,y_2,z_1,z_2} and O=H minus B, of sizes six and ten.

## Conclusion

Every witnessing four-set K for a parameter in R satisfies

\[
                         |K\cap B|\le1.                 \tag{1}
\]

Uniformly over all labels, normalized weights and original finite charts,

\[
                              |R|\le12.                 \tag{2}
\]

If |R|=12, all twelve recovered errors have weight four, have unique
supports, and are bad on their respective twelve-coordinate complements.
Write j for the sum of their support intersections with B. Then

\[
                              j\in\{11,12\}.            \tag{3}
\]

For j=11 exactly one of these supports avoids B, and each coordinate
of O occurs in exactly four supports among these twelve errors and
the three stipulated errors. For j=12 every additional support meets
B once; exactly one coordinate of O occurs three times among those
fifteen errors, and each of the other nine occurs four times.

If L043's universal support additionally has an eligible original finite
lift, then j=11. Among the twelve nonuniversal supports, h occurs once,
d twice, and each y_i,z_i twice. The unique disjoint support and eleven
one-coordinate overlaps exhaust them. This last assertion requires both
universal gates E_*=r+rho-1!=0 and r*q=(1-r)*p. An excluded universal
point at original infinity is not included in this assertion.

This bounds twelve rather than the approved eleven. It leaves the
remaining simultaneous recovery constraints, universal extraction,
other patterns and ABF26 identification unresolved, and does not
improve the global 11/q–16/q interval. This is a local partial result
under the saved EXPLORE assessment, not certified originality beyond
all sources. It awaits a separate critical audit.

## Proof

### The six-coordinate lift, including relaxed weights

For a witnessing K, its nonuniversal quotient scalar satisfies
mu!=0,-1 and E!=0. Equations (4)–(7) of L043 place

\[
 N=Z-\mu Y+c_h(q-\mu p)v_h
                    +c_d[1-(1+\mu)r]v_d
\]

in the moment span of K. This is all-eight-moment membership,
established before its fourth-weight gate. Let n be the word supported
in B with these coefficients: at y_i its coefficient is -mu*c_(y_i),
at z_i it is c_(z_i), and at h,d it has the displayed coefficients.
All four singleton coefficients are nonzero. The h,d coefficients
may vanish; neither is divided out.

Let omega be the word supported in K whose moment vector is N,
allowing zero coefficients. L043 recovers it uniquely, and the actual
error at T_K is lambda*omega/(g*E). This scalar is nonzero. The two
words n and omega have equal full moments, so n-omega lies in the
RS code by L010's kernel identity. If |K intersect B|>=2, their
union has size at most eight. The code has distance nine; equivalently,
the moment map on that union is injective. Hence n=omega. The four
nonzero singleton coefficients force y_1,y_2,z_1,z_2 into K, which
has only four elements. This gives K=K_*, contrary to its exclusion.
It proves (1) without assuming full fourth weights or descent.

L042 supplies nonzero D and all nonzero degree-at-most-four
coordinate locators. L010 therefore identifies every recovered sparse
representative with an actual same-support bad parameter and makes
it unique. The three stipulated errors are full and their parameters
are distinct from R. If any finite bad error had weight at most three,
L010 (2) would bound the whole bad set by thirteen. In particular,
whenever |R|>=11, these three parameters and R already give at least
fourteen bad parameters; no lower-weight finite bad error is possible.
Each witnessing K then equals the actual four-element support.

### Excluding thirteen distinct nonuniversal parameters

L010 bounds the entire finite bad set by sixteen, so |R|<=13.
Suppose |R|=13. Together with the stipulated triple this gives all
sixteen bad parameters and forces L010 equality. Every coordinate
then occurs in exactly four actual supports. Across B this requires
6*4=24 incidences.

The stipulated supports contribute 4+4+1=9 incidences in B: the
third meets B only at h. By (1), the thirteen other supports contribute
at most thirteen. Thus B has at most 22 incidences, contradicting
the required 24. An additional universal finite error would already
exceed the total sixteen bound, so no support was omitted in this
argument. This proves (2).

### The remaining twelve profiles

Suppose |R|=12. The preceding lower-weight argument gives full,
unique four-element supports. At each coordinate, their incidences
together with those of the stipulated triple are distinct roots of
its nonzero degree-at-most-four locator, by L010's pointwise identity.
Consequently each coordinate occurs at most four times.

The three stipulated errors contribute exactly three incidences to O,
namely their three w-labels in A_2. The twelve additional errors
contribute 48-j there. Since O has ten coordinates, its capacity is
forty. Thus

\[
                         51-j\le40,\qquad j\ge11.
\]

Each additional support meets B at most once, so j<=12. This proves
(3). If j=11, the O-incidence sum equals forty and all ten coordinate
capacities are saturated. Exactly eleven additional supports meet B
and one avoids it. If j=12, all twelve meet B; the O-incidence sum is
39. Ten nonnegative integers each at most four and summing to 39
have exactly one entry three and the other nine entries four. These
are incidence statements about actual errors, not a classification
of possible labelings or a construction of either profile.

Finally suppose the universal gates of L043 hold. Its additional
finite full-weight error is on K_* and is different from the stipulated
triple. It is also different from every parameter in R: otherwise
uniqueness of the weight-at-most-four representative would identify
its support with a nonuniversal witnessing K. There are therefore
sixteen distinct finite bad parameters, so L010 equality holds.
The universal support contributes four B incidences and none to O.
Hence 9+j+4=24, giving j=11. Coordinate balance determines the
additional occurrences individually: h already occurs in the three
stipulated supports and not K_*; d occurs in A_0,A_1 and not K_*;
each y_i or z_i occurs once in the stipulated triple and once in K_*.
Their respective remaining capacities are one, two, and two.
Together these are eleven incidences, as claimed.

The degree budget alone permits both j values when there is no finite
universal lift. For example, in the coordinate order
(h,d,y_1,y_2,z_1,z_2), the additional incidence vectors
(1,2,2,2,2,2) and (1,2,3,2,2,2) satisfy the six coordinate capacities
for j=11 and j=12 respectively. The corresponding outside totals are
forty and 39. These vectors merely show why this budget does not
force a contradiction; they do not assert support or moment realizability.
No count eleven, full challenge solution or verified candidate follows.

The proof uses only the local kernel/distance and locator identities
of L010, the audited nonpersistence input L042, and the audited exact
recovery input L043. It does not use L044's unaudited descent, L016's
fixed-label count, a new recurrence reproof or a finite computation.

## Mathlib

The full uniform twelve bound and its near-threshold incidence profiles:
**not checked**. Supporting MDS distance, Vandermonde injectivity,
polynomial root bounds and finite counting: **not checked** in Mathlib
for this step. L043 retains the precise primary recurrence citation
and its already justified specialization. No matching Mathlib theorem,
absence claim or formal verification is asserted.
