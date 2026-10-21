# L107 — Genus 38 quotient and fixed minus-three lifting

## Hypotheses

Use L106's polynomial phi(T)=(3T²+T+1)^5(1−5T), its distinct-root
open X with coordinates (r,u,v), and its smooth proper normalization
Ctilde. The fixed marking field is Q(w), w²=−3. The involution iota
sends (r,u,v) to (r,u,−v). It extends uniquely to Ctilde.

Let Ytilde be the smooth proper curve with function field
Q(Ctilde)^iota. Let Y denote the open quotient of X. Neither an integer
solution nor a rational point of either curve is assumed.

## Conclusion

Y is a smooth geometrically integral degree-495 cover of
U=P¹ minus {0,1,infinity}. Its smooth proper model Ytilde has genus 38.
The map pi:Ctilde -> Ytilde is finite étale of degree two, including
above all three omitted branch values. In particular it has no
geometric fixed or ramification point at the normalization boundary.

Here is an explicit invariant model and reversible lifting test. Write
phi(T)=sum_i c_i T^i, put z=v² and s=phi(r), and define

    G0(r,u,z) = sum_i c_i sum_{2k<=i} binom(i,2k) u^(i−2k)(−3z)^k − phi(r),
    G1(u,z) = sum_i c_i sum_{2k+1<=i} binom(i,2k+1) u^(i−2k−1)(−3z)^k,
    E = z*((r−u)²+3z)*s*(s−1).

Then Y is G0=G1=0 with E invertible. For P=(r,u,z) in Y(Q), set

    Q_P(T)=(T−u)²+3z,        Delta(P)=disc(Q_P)=−12z.

The polynomial Q_P is an étale quadratic direct factor of phi(T)−s,
disjoint from T−r. A point P lifts to X(Q) if and only if

    [Delta(P)]=[−3] in Q*/Q*²,

equivalently z is a nonzero rational square. In that case Q_P is
irreducible with splitting field Q(sqrt(−3)), and there are precisely
two rational lifts, the two fixed-field root markings.

There is also a complete boundary criterion, without enumerating
Ytilde(Q). At any rational point P of Ytilde, choose a uniformizer tau
in its local ring. The rational function z has even order 2m at P.
The unit eta=z*tau^(−2m) has nonzero residue eta_P in Q*. Then

    P lifts to Ctilde(Q) iff [eta_P]=[1]
                          iff [−12 eta_P]=[−3] in Q*/Q*².

There are two rational lifts when this holds, and none otherwise; in
the latter case the fiber is the degree-two point with residue field
Q(sqrt(eta_P)). The residue square class is independent of tau.
This criterion applies at every boundary point, including infinity and
singular images in a chosen closure. At a boundary point it describes
the normalized double-cover fiber, not a disjoint quadratic polynomial
factor or an L095 integer solution.

## Proof

### Invariant ring and the unmarked meaning

The equations in L106 have the form F0=G0(r,u,v²) and
F1=v*G1(u,v²). Since v is invertible on X, F1=0 is equivalent to G1=0.
Inverting L106's product D is equivalent to inverting E after z=v²:
each of the factors is a unit exactly when its product is. Thus, with

    A=Q[r,u,z,1/E]/(G0,G1),

the coordinate ring of X is exactly

    R=A[v]/(v²−z)=A direct-sum A*v.

This is an isomorphism of rings, not just of rational-point sets: the
two substitutions z=v² and F1/v=G1 give inverse homomorphisms.
In particular A embeds in R. Since 2 is invertible, the invariants of
iota on this free module are exactly A. Since z is a unit, v is a
unit and the derivative 2v is a unit. Consequently Spec(R) -> Spec(A)
is finite étale of degree two, and iota acts freely there. Its two
points over a geometric point are exactly the two signs of v.
This explicit ring calculation constructs the affine quotient; no
assertion of freeness at the boundary is used here.

L106 proves that R remains a domain after algebraic closure. The
displayed direct-sum injection of A into R persists after base change,
so A is geometrically a domain too. Over Qbar put a=u+vw, b=u−vw.
Forgetting the order of a,b identifies Spec(A) with the cover whose
labels are (r,{a,b}) with r,a,b distinct. Conversely the unordered
pair gives its midpoint u and z=−(a−b)²/12. These are inverse invariant
coordinates. Thus Y is finite étale over U, of degree 11*binom(10,2)=495,
and is smooth and geometrically integral. Its function field is the
fixed field: R has fraction field Q(A)(v), of degree two, and invariance
of an element alpha+beta*v forces beta=0. The degree is genuinely two
because R is a domain, whereas a square z in Q(A) would split its
generic algebra in characteristic zero.

Reduction of phi(T)−phi(r) modulo Q(T)=(T−u)²+3z is

    G0(r,u,z)+(T−u)*G1(u,z).

Indeed, expand in T=u+(T−u) and use (T−u)²=−3z. Hence Q divides
phi(T)−s. Its discriminant −12z is nonzero, and Q(r)=(r−u)²+3z is a
unit, so T−r and Q are disjoint factors. The whole fiber is étale over
U; the complementary factor has degree eight. Every unmarked pair of
distinct roots gives precisely this quadratic polynomial, including
split pairs; the quotient does not itself impose the field −3.

The involution and the fixed-field inclusion extend to smooth proper
models by Stacks, Theorem 53.2.6
[tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1); the invariant-field
degree theorem is Lemma 9.21.6
[tag 09DU](https://stacks.math.columbia.edu/tag/09DU). The associated morphism pi
is finite of degree two. Geometric integrality supplies full constant
field Q, as in L106. The rational function s likewise extends to a
finite degree-495 morphism Ytilde -> P¹. Over U its normalization is
the already normal curve Y, so every remaining point lies above
0,1 or infinity. These statements concern smooth proper models, not an
unsaturated homogenization of the invariant equations.

### All branch cycles, genus, and boundary freeness

Use L106's actual geometric root monodromy A_11 and branch types
(5,5,1), (3,1^8), and (11). Its triple transitivity also implies
transitivity on (r,{a,b}); no new monodromy hypothesis is assumed.
On 495 labels the cycles are as follows.

At zero the root permutation has order five. A fixed label would
require a fixed r and an invariant two-element subset of the remaining
letters. There is only one fixed root, and a union of five-cycles cannot
have size two. Hence there are no fixed labels, and all 495 labels
form 99 cycles of length five: ramification 396.

At one, a fixed label must use only the eight fixed root letters: a
3-cycle has no invariant subset of size two. There are
8*binom(7,2)=168 such labels. The other 327 form 109 cycles of length
three. Thus there are 277 cycles and ramification 218.

At infinity the 11-cycle has no fixed r and all 495 labels form 45
cycles of length eleven: ramification 450. These are all branch points
because the cover is étale over U. The same cover/cycle comparison used
in L106 applies: Milne, Lectures on Étale Cohomology, v2.21,
Theorems 3.1 and 21.3, pp.27,130–131
[author PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf), and Stacks,
Theorem 58.6.2 [tag 0BND](https://stacks.math.columbia.edu/tag/0BND).
A length-e cycle completes to a point of ramification index e on the
smooth normalization, including at infinity.

Riemann–Hurwitz, Stacks Lemmas 53.12.2 and 53.12.4
[tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B), now gives

    2g(Ytilde)−2 = −2*495+396+218+450 = 74,
    g(Ytilde)=38.

The map is between smooth proper curves, is generically étale, has
full constants, and is tame in characteristic zero. Genus descends by
Stacks Lemma 53.8.2 [tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6).

To check pi at the boundary, fix any of the three inertia permutations
sigma, of odd order 5,3, or 11. If an unordered label has cycle length e,
sigma^e fixes r and preserves {a,b}. Its restriction to this pair cannot
be a transposition, since a permutation of odd order cannot have an
order-two restriction. Therefore it fixes both a and b. The ordered
label has the same cycle length e: it cannot have a smaller length
than its image. The other ordering gives a second, distinct ordered
cycle; an intersection would supply a power of sigma interchanging the
pair, again impossible. Thus every quotient cycle has exactly two
ordered cycles over it, of the same length. On normalization the relative
ramification index of pi is e/e=1 at every geometric boundary point.
It is already étale over Y. Residue extensions are separable in
characteristic zero, so pi is étale everywhere. This proves boundary
freeness rather than inferring it from the open action or a genus value.
As a check, 2*75−2=2*(2*38−2), in agreement with L106.

### Rational lifting, with normalized boundary charts

Over Y, pi is exactly v²=z. The Kummer square-class theorem applies
with n=2 invertible: Stacks Lemma 59.28.1 and the following sequence
[tag 03PK](https://stacks.math.columbia.edu/tag/03PK). Torsor triviality
is equivalent to a section, Stacks Lemmas 21.4.2–3
[tag 03AG](https://stacks.math.columbia.edu/tag/03AG). At P in Y(Q)
this says precisely z(P) in Q*². Since Delta(P)=−12z(P)=−3*(2²z(P)),
this is equivalent to [Delta(P)]=[−3]. Conversely a quadratic with
that discriminant has exactly two roots u+v*w and u−v*w with v in Q*,
which reconstruct the two X(Q) points. The nonzero discriminant and
Q(r)!=0 retain the three distinct roots. Since −3 is not a rational
square, the quadratic is irreducible. These implications are reversible.

Now let P be any closed point of Ytilde, with residue field k(P), and
choose a uniformizer tau. At any point Q above it, the valuation of the
function z on Ctilde equals ord_P(z), because pi has ramification index
one. On Ctilde the same function is v², so

    ord_P(z)=2*ord_Q(v).

It is therefore even at every P, including every zero, pole and boundary
point of z. Put ord_P(z)=2m and eta=z*tau^(−2m), a unit in the DVR at
P. In the function field extension replace v by h=v*tau^(−m). The local
equation becomes h²=eta, whose unit-root construction is finite étale,
with special fiber k(P)[h]/(h²−eta_P). This is the normalized local
double cover. The local Kummer normalization rule is the unit case of
03PK together with the valuation/ramification analysis in Stacks,
Lemma 15.116.2 [tag 09EV](https://stacks.math.columbia.edu/tag/09EV):
after extracting a square uniformizer power, an odd remaining valuation
would be ramified, and a unit gives the étale quadratic extension.

In particular for rational P, completion gives Q[[tau]], and
eta/eta_P is a square in 1+tau*Q[[tau]] by the formal square-root series.
The completed normalization is consequently Q[[tau]] times Q[[tau]]
when eta_P is square, and Q(sqrt(eta_P))[[tau]] otherwise. The residue
algebra, and hence rational lifts of P, are exactly as asserted. This
also verifies the local description directly in both essential cases.
Changing tau to a*tau for a local unit multiplies eta_P by
residue(a)^(−2m), a square; thus the criterion is intrinsic. The
normalized discriminant representative is

    (Delta*tau^(−2m))(P)=−12 eta_P,

whose square class is −3 precisely when eta_P is square. On the open
z is a unit and m=0, recovering the original formula. At the boundary
one must use this unit representative, even when z or other affine
coordinates vanish or have poles. No boundary point is discarded, and
no direct-factor interpretation is assigned to a degenerate fiber.

### Finite evidence and scope

The general Stacks inputs above are imported in their primary HTML
versions inspected on 2026-10-20 in the ready quotient assessment;
the Milne version and theorem pages are as specified above. The
instance-specific invariant algebra, branch action and lifting
specialization are the work required beyond those general results.

Run `python3 scripts/global-fiber-genus/quotient.py`. The full certificate
is `scripts/global-fiber-genus/quotient-certificate.json`. It retains all
495 unordered labels, every induced permutation and disjoint cycle,
and the return of an ordered lift around each quotient cycle. Every
ordered return has relative local degree one. It also verifies the
invariant polynomials by comparing binomial expansion with independent
quadratic-remainder recurrence. All 863 checks pass, with no failures.
The quotient and ordered degrees are 495 and 990, each below the
1000-label cap. The complete branch sums are 396,218,450, total 1064.
Individual branch representatives are used only for their conjugacy
types, not as an asserted branch-generator tuple.

The continuation test succeeds: invariant quotient, full genus and a
reversible lifting condition, including normalized boundary charts, are
obtained. This is a local specialization of cited quotient, cover and
Kummer theory; no claim of originality or rational-point classification
is made. Genus 38 supplies no emptiness result or effective point method.
Both L095 power systems, gcd/positivity, the remaining global factors,
the minus-eleven branch and the main Beal gap remain open. The separate
critical audit below confirms this result without correction.

### Independent critical audit, 2026-10-20

The audit reuses the approved SPECIALIZE coverage in
`drafts/literature/2026-10-20-unmarked-quotient-critical-audit.md`.
L106's full audited proof is the mathematical input; L107 is the object
of this review. The general quotient, smooth-model, cover comparison,
Riemann–Hurwitz and Kummer results are imported by the precise citations
and source versions above. This audit checks their applicability and the
explicit specialization, not their general proofs. It finds no defect.

First, the localization and invariant-ring calculation hold at the
scheme level. In R, invertibility of D gives v invertible, so division
of F1 by v does not remove a component of the specified open. Conversely,
in A[v]/(v²−z), E invertible implies z and hence v invertible, and each
remaining factor of D is invertible. These maps identify the localized
ideals in both directions. The monic equation gives a free A-basis
(1,v), even before establishing that A is a domain. The invariant part
is exactly A since 2 is a unit. This injection remains injective after
every field extension because it is a direct summand. L106's geometric
domain therefore gives a geometric domain for A. The radical z cannot
be a square in Frac(A): its nonzero square root would split the generic
rank-two algebra, whereas its localization from R is a domain. Thus the
function-field degree really is two and the constants are Q, not a
hidden quadratic extension.

Over Qbar, the inverse formulas u=(a+b)/2 and z=−(a−b)²/12 identify
this quotient with the unordered-pair cover. They are invariant under
interchange of a,b and recover Q(T)=(T−u)²+3z. The polynomial remainder
is G0+(T−u)G1, so the asserted factor divisibility is exact.
The inverted factors z and Q(r) enforce nonzero discriminant and
disjointness from T−r; s(s−1) excludes every finite branch value.
The whole polynomial is separable there, so its remaining degree-eight
factor is étale as well. No condition on its global decomposition is
inferred. The invariant cover has 495 geometric points per fiber and
the ordered cover has 990; their twist disappears for this geometric
comparison but is retained in the rational equation v²=z.

L106's actual A_11 monodromy supplies connectedness; it is not inferred
from the three stored permutation representatives. The geometric domain
and characteristic zero give the unique smooth proper model of the
invariant function field. An algebraic constant extension of Q would
split after base change to Qbar, contrary to that domain. Thus the
full-constant-field hypotheses of the cited genus theorems hold.
The maps to P¹ and between the two smooth proper models extend their
function-field inclusions. The inverse image of U is the original
finite étale cover, by normalization uniqueness, so the only remaining
fibers to check are exactly 0,1,infinity.

At these fibers the complete quotient cycle counts are respectively
99 cycles of length 5; 168 fixed points and 109 cycles of length 3;
and 45 cycles of length 11. They give ramification 396,218,450 and
2g−2=−990+1064=74. For every cycle, a power of its odd-order inertia
permutation preserving {a,b} fixes both letters. The ordered return
therefore has the same length, and the other orientation has a disjoint
cycle of that length. This checks all boundary points geometrically,
including infinity, and gives relative index one throughout. A finite
map of smooth curves is flat here: its local finite modules over the
base DVR are torsion free. Index one and separable residue extensions
give the unramified condition, hence étaleness; it also descends from
the geometric check. This verifies boundary freeness without using
the genus cross-check as a premise.

For completeness the normalized residue algebra can be checked directly
in the local ring, without assuming that completion is a smooth base
change. At a closed point P put B=O_(Ytilde,P), F=Frac(B), and choose a
uniformizer tau. The already proved relative index one and z=v² imply
ord_P(z)=2m. Then eta=z*tau^(−2m) belongs to B*, and

    B'=B[h]/(h²−eta),       h=v*tau^(−m),

has generic field Q(Ctilde): multiplying by the square tau^(−2m)
does not change the nonsquare class of z in F. Thus B' is a domain.
Its derivative 2h is a unit, so it is finite étale over the regular DVR
B and is normal. It is precisely the integral closure of B in this
field: it is integral over B, and any field element integral over B
is also integral over B', hence belongs to B' by normality. Consequently
the full fiber algebra is k(P)[h]/(h²−eta_P). This proves that no local
branch or residue factor was lost in the radical chart.

For rational P, B completes to Q[[tau]], using the existing constant
copy of Q. The formal binomial square root of eta/eta_P is valid in
characteristic zero. The two completed possibilities are exactly
Q[[tau]]×Q[[tau]] and Q(sqrt(eta_P))[[tau]], as claimed. These give two
rational points or no rational point, respectively, in the actual
finite fiber. Replacing tau by a*tau multiplies the residue by
residue(a)^(−2m), so the criterion is independent of the uniformizer.
The calculation applies to every closed curve point, not only a
chosen affine boundary chart. Here the residue characteristic is zero;
there is no appeal to dyadic square-root surjectivity. On the open,
Delta=−12z=−3*(2v)² gives both directions of the fixed-field test and
the irreducibility of the quadratic. At the boundary the same normalized
unit class tests the proper-cover fiber only, with no polynomial-factor
or integer-solution interpretation.

The finite audit is independently reproducible by
`python3 scripts/global-fiber-genus/audit.py` followed by
`python3 scripts/global-fiber-genus/audit_quotient.py`.
The former replays all L106 records (6,822 checks); the latter reads
the complete original quotient certificate, marked certificate and
marked audit report, without importing either producer. It computes
phi by a multinomial expansion, performs monic polynomial long division,
and checks the full quotient/remainder identity. A separate multiplication
in the quadratic algebra checks F0=G0(r,u,v²) and F1=vG1(u,v²).
Every stored invariant coefficient, label, action, cycle edge, ordered
return, histogram and total is compared. Both orientations above each
quotient cycle are independently reconstructed and matched to every
one of L106's 990 ordered labels and all their action edges. The 863
original check names and values and the complete quotient schema are
also checked. The new replay has 9,581 passing checks and no failures;
its complete report is
`scripts/global-fiber-genus/quotient-audit-certificate.json`, including
input hashes and both ordered lift cycles for every quotient cycle.
The actual degrees 495 and 990 meet the required 1000-label cap.
All boundary relative indices are one. No finite preview substitutes
for this full replay, and no script substitutes for the local-ring proof.

The continuation test passes without changing the mathematical argument
or its inputs. This is independent verification of an existing
specialization, not an additional mathematical advance beyond the
sources checked. It supplies no rational-point classification, effective
point bound, exclusion of either L095 integer system, compatibility of
the remaining global factors, or conclusion for the minus-eleven branch.

## Mathlib

Full matching quotient/genus/lifting coverage and supporting Mathlib
results were not checked. The cited primary theorems are mathematical
inputs, not claims of Lean verification. The finite certificate verifies
the stated arithmetic, not the imported general theorems or the whole
geometric proof.
