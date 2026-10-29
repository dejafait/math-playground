# L146 — Complete marked degree-one dyadic Kummer image

## Hypotheses

Work over k=Q_2. Use L110/L111's actual proper marked cover D -> B,
with function field k(B)(v), v^2=z, identified in L111 with
h^2=3(4-T^2), R^2=b(T), W=hR/3. Use L113's isomorphic smooth proper
source C, with affine equation

    Y_C^2=G_C(t)=3025t^8-31460t^6+76230t^4-39204t^2+2673,
    T=2(t^2-3)/(t^2+3), W=-12tY_C/(t^2+3)^3.

Use L122's complete feasible Q_2 source-coordinate disks and separate
infinity points. Use precisely L138's monic quintic model Y_B^2=G(X),
its rational infinity O, c=-36300, X=c/(T-2), and factorization
G=(X-r)H with r=9075. Use L145's accepted entire local algebra
k x F, actual eta, nine-bit square-class coordinates and complete
Jacobian image I=span{352,208,404}. No common scalar quotient is taken.

Let pi_C:C -> B denote the proper marked projection. The set sought is

    M={delta_2([pi_C(Q)-O]): Q in C(k)}.

Equivalently these are B(k)-points admitting a point on the **proper
normalized** marked cover. No restriction to the original affine open,
global class basis, Selmer equality or point-completeness over Q is assumed.

## Conclusion

In L145's exact nine-bit convention,

    M={0,208,352,432},
    I={0,36,208,244,324,352,404,432}.

Thus M is a strict four-element subset of the eight-element Jacobian image.
Every element is realized by an actual marked local point. Moreover

    M={i in I: the rational component of i is square}.

The latter condition is precisely the marked-cover character on B(k).
Consequently the quartic evaluation supplies **no further restriction**
after this rational character: its entire admissible half of I is realized.
This is a complete local degree-one calculation by known methods, not a
new general theorem, independent global pruning, a stronger rank bound,
global point control, integer recovery or a resolution of Beal. The
separate critical mathematical audit below accepts this specialization
without a correction to the map, image or saturation claim.

## Proof

### Precise imports and applicability

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-27-marked-dyadic-abel-image.md`, supplied before
this attempt. Import Michael Stoll, *Implementing 2-descent for Jacobians
of hyperelliptic curves*, Acta Arith. 98 (2001), 245–277,
[DOI 10.4064/aa98-3-4](https://doi.org/10.4064/aa98-3-4), Section 4,
Lemmas 4.1/4.3, pp.249–251: on a squarefree monic odd-degree model with
rational infinity, an ordinary point has Kummer value X-theta, infinity
has identity, and the rational branch at X=r has value (H(r),r-eta).
L138 supplies exactly this monic squarefree quintic and infinity; L145
supplies the full k x F factorization, eta, branch sign and coordinates.
No good-reduction hypothesis or rational generation of the Jacobian by
curve points is imposed here.

Import Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
curves*, Math. Comp. 78 (2009), 2347–2370,
[DOI 10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), Section 4,
Lemma 4.4 p.8 and the LocalImage/reciprocal discussion pp.9–11. These
justify complete disk evaluation with strict square neighborhoods over
characteristic-zero complete discretely valued fields with finite residue
field, including dyadic residue characteristic. Here L113 supplies the
squarefree integral source polynomial and proper reciprocal chart; L122
already proves the complete feasible partition. We reuse that partition,
not its five fake-image labels or a conjectural transfer between quotients.

For the strict neighborhood use the Local Square Theorem, Pete L. Clark,
*Algebraic Number Theory II*, [author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 2.24, p.73 (the 161-page version assessed in L145's source review).
In the accepted totally ramified quartic F, v_F(2)=4 and v_F(pi)=1;
therefore 1+epsilon is square whenever v_F(epsilon)>8. L145 proves that
the full unit square classes are decided by reduction modulo pi^9.
Over Q_2 the used criterion is even valuation and normalized unit 1 mod 8.
These are imported general tools, not reproved here. The new work is the
specific composition, all disk values, exceptional evaluations and exact
set comparison.

### Composed proper map and marked character

The known maps give T-2=-12/(t^2+3), hence the exact affine composition

    X=3025(t^2+3), Y_B=3025^2 tY_C.                         (1)

The full polynomial identity is

    G(3025(t^2+3))=3025^4 t^2 G_C(t).                       (2)

It is checked coefficientwise in the certificate, including all zero
coefficients. Equation (1) is not merely a map guessed from (2): it is
the actual projection W=-12tY_C/(t^2+3)^3 followed by L138's map, so its
proper extension is the given marked projection. L111/L113 identify
the full normalized cover; every marked k-lift is represented on C(k).

For finite nonzero t, the Kummer evaluation is

    (X-r,X-eta)=(3025t^2,3025t^2+r-eta).                   (3)

Its first component is square. For q=1/t nonzero, divide both components
by t^2, a genuine square in k and F (no scalar quotient), giving

    (3025,3025+(r-eta)q^2).                               (4)

At t=0 use the branch rule instead of the vanishing first component:
H(r)=73990352390625 has valuation zero and unit 1 mod 8, and r-eta
has F mask 44 and full pair mask 352, as in L145. Thus (3)'s use of the
square first component continues correctly in square classes at t=0.

The meaning of the rational component can be checked directly. On B,
T=2+c/X gives the exact identity

    3(4-T^2)=660^2 (X-r)/X^2.                             (5)

The two numerator coefficient lists are both (-3953070000,435600).
For X finite and different from 0,r, the right side is a unit in the
local ring of B at the point times its indicated square multiplier.
By L111's cover identification and the normalized unit-root criterion,
the point lifts exactly when X-r is square in k. This remains valid
at zeros or poles of the original z: use the equivalent h-cover and
its unit, not the raw value of z. The remaining rational exceptional
points are checked next. Thus (5) identifies the character of this
specific cover; it is not a new unproved condition on global classes.

### All proper exceptional points

At t=0 there are two k-points, since G_C(0)=2673 is a nonzero square
in k. Both map to the single target branch (r,0), whose value is 352
and whose rational component is square. At source infinity the separate
points Z=Y_C/t^4=55 and -55 both map to O: (1) gives poles of orders
two and five for X,Y_B. The target infinity value is identity. Formula
(4) at q=0 also gives the square pair (3025,3025), consistent with that
separate proper rule. These are two source points, not two new target
classes or primitive integer solutions.

There is no k-rational conic-infinity fiber: t^2=-3 has nonsquare unit
5 modulo 8. There is also no k-point of B at X=0, since G(0) has
valuation eight and normalized unit 5 mod 8; this is the sextic-infinity
fiber of L138. The other four target branch coordinates lie in the
irreducible quartic F by L145, so none is in k. These observations
exhaust exceptional target branch/infinity and source map charts.

All original F(T), K(T), L(T) zeros, marking zeros/poles and other
coordinate exceptions are retained on the proper C. The new finite
evaluation has no such denominators: r-eta+3025t^2 never vanishes in F,
since eta is not rational. Its reciprocal expression is nonzero at q=0
and, for nonzero q, is a square multiple of that same nonzero value.
Thus no Q-only exclusion from L113 was used over Q_2 and no additional
exceptional fiber is removed by these evaluations. Equations (5) and
the actual lifts at r and O now give the rational-character criterion
on every B(k)-point.

### Complete disks and strict precision

Set b0=r-eta. L145 gives v_F(b0)=0 and

    eta=(3705900-3441768pi+316932pi^2-6512pi^3)/71.

L122's complete feasible partition is t=a modulo 8 for a=0,2,4,6;
t=a modulo 16 for a=3,13; and q=a modulo 8 for a=0,2,4,6.
The last q=0 disk includes the whole tail and both source infinities.
The other six odd disks modulo 16 have no points, as proved in L122.
Both source signs have the same composed evaluation.

For an affine disk t=a+m u, u in Z_2, the quartic value is

    b(a)+6050am u+3025m^2 u^2, b(a)=b0+3025a^2.

For a reciprocal disk q=a+m u it is

    d(a)+2am b0 u+m^2 b0 u^2, d(a)=3025+b0 a^2.

The minimum valuation of the two nonzero difference coefficients is
a lower bound for every difference on the disk; cancellation can only
increase the bound. The following complete table includes the normalized
unit residue encoding and full nine-bit result in L145's convention.
For each row the bound strictly exceeds v_F(center)+8.

| chart | a | m | v_F(center) | difference bound | required strict threshold | unit mod pi^9 | full mask |
|---|---:|---:|---:|---:|---:|---:|---:|
| t | 0 | 8 | 0 | 24 | 8 | 497 | 352 |
| t | 2 | 8 | 0 | 20 | 8 | 241 | 208 |
| t | 4 | 8 | 0 | 24 | 8 | 497 | 352 |
| t | 6 | 8 | 0 | 20 | 8 | 241 | 208 |
| t | 3 | 16 | 10 | 20 | 18 | 225 | 208 |
| t | 13 | 16 | 10 | 20 | 18 | 225 | 208 |
| q | 0 | 8 | 0 | 24 | 8 | 1 | 0 |
| q | 2 | 8 | 0 | 20 | 8 | 257 | 432 |
| q | 4 | 8 | 0 | 24 | 8 | 1 | 0 |
| q | 6 | 8 | 0 | 20 | 8 | 257 | 432 |

Dividing a difference by its center puts the ratio in 1+pi^9 O_F,
so the imported strict square theorem proves constancy on the **whole**
disk. In particular the odd rows use 20>18, not a weak non-strict test.
All rational components are square, with the separate branch rule above.
The q=0 row is valid uniformly for nonzero q in 8Z_2 and matches both
proper infinity values at zero. No recursion, sampled completeness or
factorization through L122's even-degree scalar quotient is asserted.

### Realizations, comparison and limits

Every retained center has an actual source point: the exact curve value
has even valuation and normalized unit 1 modulo 8 (L122 and the replay).
For the four distinct values it suffices to use t=0, t=2, q=2 (t=1/2)
and either proper infinity, whose source square values are respectively
2673, -173503, -727903 and 55^2 in the reciprocal chart. Thus these
give masks 352,208,432,0. The complete disks give containment, and these
actual points give the reverse containment; M is exactly the stated set.

Enumerating L145's three independent image generators gives exactly the
eight masks in the conclusion. Those of rational mask zero are precisely
0,208,352,432; the other four have rational mask 4. Hence the marked
image is strict, but it saturates the kernel of the rational projection
inside I. Further disk refinements cannot exclude one of its four
realized classes. No quotient rank or independent global restriction
follows from comparing this point set with all Jacobian divisor classes.

Reproduce the bounded arithmetic with
`python3 scripts/pair-genus-two/marked_dyadic_abel_image.py` and
`python3 scripts/pair-genus-two/verify_marked_dyadic_abel_image.py`.
The full evidence is
`scripts/pair-genus-two/marked-dyadic-abel-certificate.json` and
`scripts/pair-genus-two/marked-dyadic-abel-verification.json`.
The producer reuses accepted pi-coordinate field arithmetic and the
replay reuses accepted O-coordinate arithmetic, importing no new producer
code. It independently expands (2) by binomial coefficients, consumes
every full new evaluation and difference coefficient, verifies all
normalizations/square masks, all ten strict bounds and realizations, both
proper infinity rows, the branch row, exact character and complete sets.
The replay passes 59 new checks and 852 supporting arithmetic checks;
the accepted field and square-coordinate construction is reused, not
claimed independently rediscovered or newly critically audited here.

Actual/cap usage: 10/200000 processed disks, depth 4/64, largest reused
residue table 512/2^20, maximum rational arithmetic sizes 640/8192 bits
in the producer and 417/8192 in replay. Every disk closes with no
refinement or unresolved coverage. Full relevant rows, branch values,
character and exceptions were inspected. The initial producer's direct
comparison of Fraction values with JSON strings failed; the preserved
`scripts/pair-genus-two/marked-dyadic-abel-initial-schema-failure.json`
records that schema mismatch. Parsing the saved rational values repaired
the check; no mathematical input or claimed class changed.

The instance result is local progress by the assessed known theory.
The accepted rank bound remains 5+c<=7; sufficient bound one, global
units/classes, point control, marked integer recovery and other residual
Beal signatures remain independent gaps. Prior stops and unfinished L108
are preserved. This image is not a complete Beal candidate.

### Separate critical mathematical audit — 2026-10-28

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-27-marked-dyadic-abel-audit.md`.
This audit accepts the exact four-element image and its saturation of
the rational-character kernel. It is an independently checked application
of the cited methods, not an additional local restriction or a discovery
beyond those sources. The accepted field and square-coordinate input
from L145 and the accepted source partition from L122 are reused.

**Actual proper composition and normalized fibers.** Substituting the
maps of L111/L113 into L138 gives

    c/(T-2)=(-36300)/(-12/(t^2+3))=3025(t^2+3),
    c^2 W/(T-2)^3=c^2 tY_C/144=3025^2 tY_C.

Thus the sign and constant in (1) are those of the actual marked
projection. The replay independently expands all coefficients of (2),
using binomial expansion rather than the producer's Horner composition.
The field identifications extend to proper isomorphisms by
[Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1);
base change to Q_2 preserves these isomorphisms.
Consequently the two smooth source charts exhaust the normalized marked
cover over Q_2. In particular none of L113's exclusions made only over
Q is imported as a Q_2-point exclusion.

The exact identity (5) fixes the twist. At an ordinary B-point with
X different from 0,r, both X-r and X are nonzero regular functions.
The cover obtained by adjoining h is therefore the unit-root cover
of X-r after multiplication by the square (660/X)^2. The source
assessment's [Stacks Lemma 59.28.1, tag 03PK](https://stacks.math.columbia.edu/tag/03PK)
and normalization [Lemma 58.11.2, tag 0BQL](https://stacks.math.columbia.edu/tag/0BQL)
apply to these normal curve local rings: they are
Q_2-algebras, so 2 is invertible. No assertion of etaleness over Z_2
is needed. Their residue fiber splits precisely when X-r is square.
The same field cover remains valid when the original rho or z has a
zero or pole; evaluating the raw value z there is unnecessary.

For clarity, the two rational branch/infinity fibers also admit direct
normalized-unit checks. At P_r=(r,0), Y_B is a uniformizer, since
H(r)!=0, and Y_B^2=(X-r)H(X). Thus

    a/Y_B^2=660^2/[X^2 H(X)],
    residue at P_r=(660/r)^2/H(r),
    a=3(4-T^2).

Its square class is that of H(r), exactly the rational branch Kummer
component, since a square class equals its inverse. Here H(r) is an
odd unit congruent to one modulo eight. This agrees with both actual
source points at t=0, Y_C^2=2673, and their branch mask 352. At O,
Z_B=Y_B/X^3 is a uniformizer by L138's smooth odd chart, and

    a/Z_B^2=660^2 X^4/H(X) -> 660^2.

The normalized fiber therefore splits, in agreement with the two
source infinities Z_C=+55,-55 and the identity Kummer value at O.
The source parameter q has X of pole order two and Y_B of pole order
five at each of them; it does not map either point to a finite fiber.
These checks verify the rational-character criterion also where its
ordinary expression X-r is zero or has a pole.

At X=0 the exact G-value has valuation eight and normalized unit five
modulo eight, hence no B(Q_2)-point. At conic infinity the equation
t^2=-3 has unit five modulo eight and no Q_2-root. L145's irreducibility
of H over Q_2 rules out all four other rational branch coordinates.
There are no further evaluation denominators: r-eta+3025t^2 is nonzero
for every t in Q_2 because eta has degree four, and its reciprocal
expression is nonzero at q=0. The proper-model argument retains every
original F,K,L and marking exception without needing their old affine
coordinates. This accounts for every exceptional fiber relevant here.

**Complete disks and full product coordinates.** Every finite t is
integral or has q=1/t in 2Z_2. L122's accepted coefficientwise tests
give all four even t-disks modulo eight, exactly the odd disks 3,13
modulo sixteen, and all four even q-disks modulo eight. They also
rule out Q_2-rational zeros of G_C. Both Y_C signs give the same new
evaluation; the two infinity points are treated separately.

For nonzero t the first component 3025t^2 is a genuine square; in the
reciprocal chart division by t^2 is a square in each algebra factor.
Thus the representatives used by the replay are valid in the full
product square-class group. No common-scalar quotient from L122 is used.
At t=0 its replacement by the branch value is justified separately above.

All ten full center vectors, normalized vectors and difference coefficients
were inspected and independently replayed in the accepted O basis.
The valuation minima are valid bounds for every u in Z_2 because each
term of the difference polynomial has at least that valuation. The
center valuation is zero in eight rows and ten in the two odd rows.
The bounds are respectively 24 or 20, hence strictly exceed eight;
on the odd rows the critical inequality is 20>10+8=18. The smallest
relative difference valuation is therefore ten, strictly greater than
the required eight. Clark's cited square theorem gives constancy on
each entire disk. In particular it applies uniformly to q in 8Z_2,
including all nonzero tail valuations, with the separate infinity value
at q=0. There is no unexamined refinement or precision-equality case.

The replay checks each complete normalized vector and its nine residue
digits, not only the resulting mask. The respective quartic unit residues
in table order are 497,241,497,241,225,225,1,257,1,257; their full masks
are exactly the ten printed masks. The underlying complete square table
is L145's accepted input, not a new sampled approximation.

**Realization, equality and stopping consequence.** The saved exact source
values at t=0, t=2 and q=2 are nonzero, have even valuation zero and
unit one modulo eight. The Q_2 square criterion supplies actual points
realizing 352,208,432. Each proper infinity realizes zero. These give
reverse containment, while the complete disks give containment, with
no inference that an arbitrary point image is a subgroup. Enumerating
the three accepted generators gives eight distinct Jacobian masks;
exactly 0,208,352,432 have zero rational bits. The other four all have
rational mask four. This proves the set equality and the asserted
saturation, rather than only a comparison of dimensions.

The existing independent replay was rerun with
`python3 scripts/pair-genus-two/verify_marked_dyadic_abel_image.py`.
Its complete saved evidence remains
`scripts/pair-genus-two/marked-dyadic-abel-verification.json`: 59 new
checks and 852 supporting arithmetic checks pass, with zero failures
and no unresolved rows. It binds the entire producer certificate and
the accepted field, model, order and audit inputs by their exact hashes.
All ten rows close at depth at most four; actual/allowed arithmetic
sizes are 417/8192 bits in replay. No new search or arithmetic script
is needed for this audit. The proper-model and square-neighborhood
arguments above are essential in addition to the successful replay.

The direct mathematical inputs in DAG.md are unchanged. This validates
L146 as a local input and confirms the stop in ATTEMPTS/064. It supplies
no extra quartic pruning after the marked rational character, no rank
improvement and no Beal candidate. The accepted bound remains 5+c<=7,
six above the sufficient bound one when c=2. Global units/classes,
point control, integer recovery and other signatures remain unresolved.

## Mathlib

Full matching theorem for this composed marked Q_2 point image, the exact
disk values and cover-character saturation has not been checked in Mathlib.
Supporting coverage was not newly checked; no absence claim or formal
verification is made. Named published tools and the accepted local input
are distinguished above from the specific exact arithmetic reproduction.
