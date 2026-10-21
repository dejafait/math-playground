# L047 — Disjoint recovery couples shared-tag overlaps by a quadratic fiber

## Hypotheses

Use the entire gated local tau=1 setup of L043 over F=F_(97^20),
with H the order-sixteen subgroup of F_97, k=8 and the pinned cell.
In particular retain the distinct labels and sets

    A_0={h,d,y_1,y_2}, A_1={h,d,z_1,z_2}, A_2={h,w_1,w_2,w_3},
    B={h,d,y_1,y_2,z_1,z_2}, O=H minus B,
    W(X)=product_(i=1)^3(X-w_i),
    Q(X)=product_(x in H minus (A_0 union A_1 union A_2))(X-x).

The original gamma_i are distinct and finite, lambda!=0, and
p*q*(1-p-q)*r*(1-r)!=0. Free weights and the original chart range
over F. A candidate means a distinct original finite parameter admitted
by L043 (4)–(7), excluding the three stipulated parameters and supports
and K_*. Keep every quotient and finite-denominator gate; do not impose
the recovered-weight gate (9).

Assume one such candidate has a witnessing support K_0 subset O,
|K_0|=4, with quotient scalar nu. Compare only other candidate parameters,
with scalars mu distinct from nu, whose witnesses are

    K={b} union S, b in B, S subset O, |S|=3.

No existence of K_0 in every pencil, twelve-count premise, equality,
full recovered weights, prime-field free weights, rational original
chart or finite universal lift is assumed.

Put Y_2(X)=(X-y_1)(X-y_2), Z_2(X)=(X-z_1)(X-z_2),
and phi(x)=Y_2(x)/Z_2(x) at labels outside the z-pair.

## Conclusion

Every compared overlap satisfies |S intersect K_0|<=2.

Consider those with b in {h,d} and |S intersect K_0|=2. There are
at most two distinct such candidate parameters. If there are any, all
their triples have the form

    S=R union {c}, R subset K_0, |R|=2,

with the **same** c in O minus K_0. For two distinct such parameters,
their R sets are disjoint and partition K_0. For each one, the remaining
pair K_0 minus R is a phi-fiber: its two labels have equal phi values.

There is also an explicit label/weight gate. Let f_0 be the monic
quartic with roots K_0. Its actual relaxed recovery determines a unique
nonzero polynomial ell in F_97[X] of degree at most one satisfying

    a_x(nu) f_0(x)=W(x) ell(x), x in B,                 (1)
    a_yi(mu)=-mu, a_zi(mu)=1,
    a_h(mu)=q-p*mu, a_d(mu)=1-r-r*mu.

For an h-tag or d-tag double intersection respectively define

    eta_h=((1-r)/r)*Z_2(d)/Y_2(d),
    eta_d=(q/p)*Z_2(h)/Y_2(h).                         (2)

Its eta_b must satisfy, for some nonzero scalar k_b in F,

    eta_b*Y_2(X)-nu*Z_2(X)=k_b*ell(X)*(X-c).            (3)

Thus divisibility by ell, degree and the remaining root c are necessary
tests, not sufficient recovery criteria. If ell is nonconstant with
root xi, then xi is outside both singleton pairs and
eta_b=nu*Z_2(xi)/Y_2(xi). If ell is constant, eta_b=nu and
Y_2-Z_2 must have degree exactly one. In either case eta_b and c are
unique for all these overlaps. In particular, occurrence of both tag
types requires

    r*q/((1-r)*p)=phi(h)/phi(d).                       (4)

All displayed denominators are nonzero in the stated cases.

If two of these parameters have full recovered weights, both tags
must be d. Their actual errors, together with the full error on K_0
if it too is full, have support union six, pairwise intersections two,
and empty triple intersection.

In L045's twelve-candidate j=11 profile, K_0 is the unique B-disjoint
support and every recovered error is full. If a finite universal lift
also exists, there are exactly three h/d-tag overlaps. Either two of
them give the d-tag union-six triple just described, or at least two
of the three meet K_0 in at most one label. This is a dichotomy, not
an exclusion of either alternative. The j=12 all-overlap profile has
no K_0 and receives no restriction here.

This is local progress toward the approved eleven-candidate target;
it proves neither eleven nor a twelve-candidate counterexample. It
adds no global improvement to 11/q–16/q. A separate critical audit on
2026-10-08 found no defect in this restriction or its essential L045–L046
uses; its checks appear below. L044 and separate audits of the full
L045–L046 statements remain outside this verdict. POTENTIALLY_NEW
means only local progress beyond the saved inputs and coverage, not
certified originality beyond all literature.

## Proof

### Disjoint and overlapping recoveries in full moments

For a candidate scalar mu let n(mu) be the word supported in B with
coefficients Q(x)*a_x(mu). All four singleton coefficients are nonzero.
L043 (4)–(7) gives a word omega on its witnessing four-set with exactly
these eight moments, allowing zero recovered coefficients. Its actual
error is lambda*omega/(g*E(mu)), a nonzero scalar multiple. The finite
gates and the triple exclusions remain exactly those of L043.

For K_0 the word n(nu)-omega_0 is a codeword by L010's kernel identity.
It is nonzero, since omega_0 vanishes on B whereas n(nu) has four
nonzero singleton coordinates. Its polynomial P_0 of degree at most
seven vanishes on the six distinct labels O minus K_0. Consequently

    P_0(X)=product_(o in O minus K_0)(X-o)*ell(X)

for a nonzero ell of degree at most one. This is divisibility by six
distinct linear factors, not an assumption on the recovered weights.
Since product_(o in O)(X-o)=Q(X)W(X), evaluation at x in B gives
exactly (1), after cancelling Q(x)!=0 and f_0(x)!=0. At the two
z-labels ell(z_i)=f_0(z_i)/W(z_i) is nonzero and in F_97. The unique
polynomial of degree at most one with these two values lies in
F_97[X], proving the asserted descent for ell alone. At either y-label,
ell(y_i)=-nu*f_0(y_i)/W(y_i)!=0. Thus a nonconstant ell has its root
outside all four singleton labels. Nothing forces the original chart
or p,q,r into the prime field.

For an overlap K={b} union S, the same kernel argument gives a nonzero
polynomial of degree at most seven vanishing on O minus S (seven
labels). Nonzeroness follows from a surviving singleton outside K.
Its factorization, evaluated at B minus {b}, gives

    a_x(mu) f_S(x)=u W(x), x in B minus {b}, u!=0,       (5)

where f_S is the monic cubic on S. This is the single-recovery equation
used in the proof of L046; it requires all eight moments and permits
zero weights at the tag and at other recovered coordinates.

Distinct original parameters give distinct mu and nu: L043's formula
T=gamma_0+g*rho/[rho-(1-rho)*mu] is injective on its eligible scalars,
since g*rho and 1-rho are nonzero. Also mu,nu!=0,-1 and both E are
nonzero; no finite or excluded parameter is silently restored.

### Cancel common outside roots

Let i=|S intersect K_0| and C(X) be the monic polynomial on that
intersection. Set F_1=f_S/C and G=f_0/C, of degrees 3-i and 4-i.
For x in B minus {b}, multiply (5) by ell(x), use (1), and cancel
C(x)!=0. This gives

    a_x(mu)*ell(x)*F_1(x)=u*a_x(nu)*G(x).              (6)

Define

    U=ell*F_1-u*G, V=mu*ell*F_1-u*nu*G.

At each surviving z-label U is zero, and at each surviving y-label V
is zero. Both polynomials are nonzero. Indeed U=0 would imply
V=u*(mu-nu)*G, nonzero at a surviving y-label, contradicting its
required zero. V=0 would imply
U=u*(nu-mu)*G/mu, nonzero at a surviving z-label. Such labels always
exist since only one tag was removed, and G has roots only in O.

If i=3, both U,V have degree at most one. At least one singleton pair
survives intact, forcing its nonzero polynomial U or V to have two
distinct roots. This is impossible. Since i<=3, we obtain i<=2.

### Double intersections at shared-coordinate tags

Now let i=2 and b in {h,d}. Write R=S intersect K_0 and S=R union
{c}, so F_1=X-c, while G is the monic quadratic on K_0 minus R.
Both singleton pairs survive. Since U,V have degree at most two and
are nonzero, their two distinct roots give

    U=a Z_2, V=v Y_2, a*v!=0.

Put eta=v/a. At the remaining shared label, (6) gives
(1-r)U(d)=rV(d) if b=h, and qU(h)=pV(h) if b=d.
All Y_2,Z_2 evaluations there and p,r are nonzero. Thus eta is
exactly eta_b in (2).

The polynomial identities, before any division by a value of ell, are

    mu*U-V=u*(nu-mu)*G,
    V-nu*U=(mu-nu)*ell*(X-c).                         (7)

The first identity evaluated at either root of G gives
phi=mu*a/v, proving the remaining-pair fiber condition. All these
roots are outside the singleton pairs, so Z_2 is nonzero there.
The second identity gives (3) with k_b=(mu-nu)/a!=0.

To prove the common-c assertion, first suppose ell is nonconstant,
with its root xi. The nonvanishing checks following (1) give
Y_2(xi)*Z_2(xi)!=0. Evaluating (3) at xi forces the unique value
eta=nu*Z_2(xi)/Y_2(xi). Hence the polynomial eta Y_2-nu Z_2 is
fixed for all these overlaps. It is nonzero: its two quadratics have
disjoint root sets and cannot be proportional. Dividing it by the
fixed ell in (3) gives a polynomial of degree exactly one, up to
a nonzero scalar. Its unique root is c, independent of the overlap.
This also handles a double root at xi without treating a simple
root as divisible twice.

If ell is constant, the right side of (3) has degree exactly one.
The monic quadratic coefficients on its left force eta=nu. The left
side is then nu*(Y_2-Z_2), which must have degree exactly one.
Again its unique root c is fixed. If Y_2-Z_2 has degree zero, no
such overlap exists. These two cases cover every nonzero ell, with
no assumption that its root belongs to H.

For two distinct compared parameters, L046 says their outside triples
are distinct; if they share a pair, their tags must be opposite y/z
singleton types. Here all tags are h or d. Since the common c is
outside K_0, the two R sets must therefore be disjoint: otherwise the
triples share c and at least one label of K_0. Disjoint two-subsets
of a four-set number at most two, proving the distinct-parameter bound.
With two they partition K_0. The quadratic-fiber argument independently
shows their complementary pairs are disjoint: a fiber of phi has at
most two elements, since Y_2-t Z_2 is a nonzero polynomial of degree
at most two for every t. No support tally is substituted for a
parameter count, even if a relaxed parameter has multiple witnesses.

If both tag types occur, their unique eta values coincide. Substitution
from (2) and division by nonzero gates gives (4). This necessary
condition and (3) do not assert that the other recovery equations hold.

### Full-weight consequence and the twelve-profile application

Suppose two of these parameters have full errors e_1,e_2, with tags
b_1,b_2. Their R sets partition K_0 and both use the same c.
The error e_0 at the K_0 parameter may still have zero weights;
it is supported in K_0. The union of all three supports has size
at most seven: K_0, c and at most two tags.

For their distinct original finite parameters T_0,T_1,T_2, the word

    (T_1-T_2)e_0+(T_2-T_0)e_1+(T_0-T_1)e_2

has zero moments, because the syndromes are values of the same affine
pencil. The moment map is injective on any union of at most eight
labels by L010. Thus this word is zero. If b_1!=b_2, coordinate b_1
is present only in the full error e_1, with coefficient T_2-T_0!=0,
a contradiction. Hence both tags coincide.

They cannot both equal h: the three stipulated full errors already
use h at three distinct original parameters, and these two full errors
would give two further distinct roots of the nonzero coordinate
locator ell_h(T). L042's nonpersistence is retained through L043, and
L010 bounds this polynomial's degree by four. Five roots are impossible.
Therefore both tags are d. If e_0 is also full, the supports are
K_0, {d,c} union R_1, {d,c} union R_2. Their union has six labels,
pairwise intersections have size two, and the triple intersection is
empty, as claimed.

Finally apply L045 only in its stated twelve-candidate j=11 case.
It supplies one B-disjoint support K_0 and all full recovered errors.
If the finite universal gates also hold, its incidence balance gives
one h-tag and two d-tag overlaps. At most two can meet K_0 twice,
and if two do, the preceding argument forces precisely the two d-tags
and the union-six triple. Otherwise at most one does; since intersections
of size three have been excluded, at least two of the three meet K_0
in at most one label. This does not guarantee the two-double-intersection
branch, nor exclude the alternative. Without finite universal gates,
these tag multiplicities are not assumed. In j=12 there is no K_0,
so the entire present coupling is inapplicable.

The recurrence input remains the exact known compiler imported in L043:
Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*, live author
TeX v9.2 dated July 17, 2026, source lines 2785–2935,
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler` (DR6–DRC),
inspected and specialized there
([author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex)).
It gives fixed-support full-moment membership, not this simultaneous
quadratic coupling. We reuse that import and L010's proved kernel and
locator identities; no general shortening or recurrence theorem is
reproved. No finite computation, equality premise, descent of the
original pencil or eleven-count claim is used.

### Separate critical audit (2026-10-08)

This audit uses the prior EXPLORE coverage for the exact L047 target.
It found no mathematical error or missing hypothesis. The verdict covers
the conditional restriction and every L045–L046 assertion used here;
it does not certify L044, L040, universal extraction, the eleven bound,
or unrelated claims in those input files. The proof and its direct
mathematical inputs require no change. This is validation of an existing
local result, with no new bound or certified originality claim.

**Recovery, finite parameters and factorization.** L043 (4)–(7)
supplies all eight moments, including when a recovered weight vanishes.
Its scale lambda/(gE) is nonzero. A surviving singleton has nonzero
coefficient because mu,nu!=0, so neither n(nu)-omega_0 nor the
overlap difference is the zero word. L010's kernel identity gives
their actual degree-at-most-seven polynomials. The first vanishes on
the six labels O minus K_0, giving a nonzero degree-at-most-one ell;
the second vanishes on the seven labels O minus S, giving a nonzero
constant u. These factorizations remain valid if further roots arise
from zero recovered weights. Q, W, f_0 and f_S do not vanish on B.
Consequently cancellation gives (1) and (5) at exactly the labels
stated, without requiring a nonzero coefficient at the overlap tag.

The two distinct z-values in (1) uniquely determine ell over F_97;
the two y-values are nonzero since nu!=0. Thus a root xi of a linear
ell is outside both singleton pairs. Only ell is descended. Neither
the original chart nor the free weights are restricted to F_97.
For E(mu)=rho+(rho-1)mu, equality of the finite parameters forces
equal E and hence equal mu, since g*rho*(rho-1)!=0. Every scalar
still has the nonuniversal quotient gate, mu!=0,-1 and E!=0.
The three original finite parameters and the universal support remain
excluded; no parameter at original infinity is inserted.

**Cancellation and all degrees of ell.** All common-root factors
C(x) in B are nonzero, so (6) follows by multiplying (5) by ell
and then using (1); no value of ell is divided out. If U were zero,
V=u(mu-nu)G would be nonzero at a surviving y-label. If V were zero,
U=u(nu-mu)G/mu would be nonzero at a surviving z-label. These
contradictions establish both nonzero polynomials even when b is a
singleton tag. At intersection three each has degree at most one,
while one singleton pair survives intact. Its two roots exclude that
case. This applies to every overlap tag and permits relaxed weights.

At intersection two with h/d tag, the degrees are at most two and
both singleton pairs survive, so U=a Z_2 and V=v Y_2 with a*v!=0.
The remaining shared-label equation gives exactly (2), with nonzero
p,r,1-r and nonzero Y_2,Z_2 evaluations. Direct subtraction checks
both signs in (7). The first identity at a root of G gives
phi=mu/eta, with eta=v/a!=0. The second yields (3), with
k_b=(mu-nu)/a!=0. The quadratics Y_2,Z_2 have disjoint root sets
and cannot be proportional, so their displayed combination is nonzero.

For linear ell, substitution at xi fixes eta uniquely. Existence of
an overlap then forces the fixed quotient (eta Y_2-nu Z_2)/ell to
have degree exactly one, and its root is c. This uses polynomial
division, not cancellation of a simple root: if the numerator has a
double root at xi, the quotient has its root at xi as well, and the
same uniqueness remains valid. For constant nonzero ell, comparison
of leading coefficients forces eta=nu; the difference Y_2-Z_2 must
have degree one. If it is constant there is no overlap of this type.
Thus neither the constant case nor any repeated root is dropped.
Equating the two values in (2) gives (4) with the recorded denominators.
These tests are necessary only; none replaces the other recovery gates.

**Essential L046 use and distinct-parameter counting.** Its five-value
equations follow from the same full-moment factorization. For coincident
outside triples, a surviving y and z give u=u' and mu=nu. If the
two tags remove both y-labels, the z-labels still give u=u' and the
shared d equation gives r(mu-nu)=0. If they remove both z-labels,
the surviving y equations give u/u'=mu/nu and the d equation gives
(1-r)(nu-mu)=0. The gates exclude both exceptions. Coincident tags
are already in the first case. Thus the outside triples are distinct.

For distinct triples sharing a pair, their cancelled equations (4)
in L046 give nonzero linear comparison polynomials. If both z-labels
survive, the first polynomial has two roots and forces c=e; if both
y-labels survive, the second does the same since mu,nu!=0. Hence
the two tags must be one y and one z. In particular h/d tags cannot
share an outside pair, regardless of recovered zero weights. Since
L047 has already fixed the common c outside K_0, overlapping R sets
would supply such a shared pair. The R sets must therefore be disjoint,
and at most two can exist in the four-set K_0. The conclusion counts
parameters: choose any witness for each distinct eligible parameter;
the argument applies to every such pair of choices. Multiple witnesses
for one relaxed parameter are never added to the count. The independent
fiber observation is consistent: Y_2-t Z_2 is always a nonzero
degree-at-most-two polynomial, so each fiber has at most two labels.

**Full weights and essential L045 application.** For three distinct
finite T_i, the displayed affine combination of e_i has zero moments:
its coefficients sum to zero and their T-weighted sum is zero. Its
support lies in K_0 union {c,b_1,b_2}, of size at most seven, so
L010's column injectivity makes it the zero word. This remains true
when e_0 has zero weights. If b_1!=b_2, coordinate b_1 occurs only
in full e_1 and has nonzero coefficient T_2-T_0, a contradiction.
Two h tags would give five distinct roots of L(T,h), counting the
three stipulated full errors. L042 supplies its nonzero polynomial
and L010 its degree at most four. Hence both tags are d. Full e_0
then gives exactly the three claimed four-element supports, whose
union, pairwise and triple intersections have the stated sizes.

The L045 assertions used here were checked before any equality use.
If a nonuniversal K meets B at least twice, n-omega is supported on
at most eight labels, hence vanishes by distance nine; the four nonzero
singleton coefficients would force K=K_*, a contradiction. Each
relaxed recovery is a finite same-support bad parameter by L010 and
L042. A weight-at-most-three parameter makes L010's entire count at
most thirteen. Twelve candidates plus the distinct stipulated triple
give fifteen, so all recovered errors are full and their supports
are unique. Thirteen candidates would give L010 equality, yet B
would have at most 9+13=22 incidences instead of 24; thus twelve
is the relevant remaining case. At twelve, O has 51-j incidences
and capacity forty, giving j>=11; the at-most-one B intersections
give j<=12. For j=11 exactly one support is B-disjoint and every
O coordinate is saturated. No universal lift is needed for this case.

Only when both E_*=r+rho-1!=0 and rq=(1-r)p hold does L043 add
the distinct finite full universal error. Sparse-error uniqueness
prevents a collision with any of the twelve full nonuniversal errors.
The resulting sixteen parameters justify equality and exact coordinate
balance. Subtracting the stipulated and universal incidences leaves
one h, two d, and two of each singleton tag. These are exactly the
three h/d overlaps used in L047's dichotomy. If two meet K_0 twice,
the full-weight argument applies; if at most one does, at least two
meet it at most once, since intersection three was excluded. No
restriction is supplied when the j=12 profile has no K_0. The proof
does not presume a finite universal error from its weight equation
alone, nor use the union-six candidate bound L040.

The inspected primary ingredient coverage in the saved assessment is
reused. In particular, Hall, *Notes on Coding Theory*, section 5.1,
Theorem 5.1.1 and its proof, printed pp. 63–64
([author chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf)),
applies over F to sixteen distinct points, dimension eight and unit
multipliers, giving distance nine. It agrees with the local L010
kernel/injectivity proof; no new MDS theorem is reproved. The precise
DR2/DR6–DRC import retained above supplies membership, not this coupling.
No source refresh, numerical evidence or mathematical script was needed.

## Mathlib

Full overlap/disjoint fiber restriction, common outside label, and
conditional union-six consequence: **not checked**. Supporting polynomial
factorization, finite-field interpolation, Vandermonde injectivity and
root bounds: **not checked** in Mathlib in this step. Informal inputs are
L010, audited L043, and the essential L045–L046 assertions checked in
the separate audit above; the exact primary recurrence import is retained.
Mathlib coverage was not checked during the audit either. No absence
claim or Lean verification is asserted.
