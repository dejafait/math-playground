# L109 — Pair-only genus two and fixed minus-three lifting

## Hypotheses

Let phi(T)=(3T²+T+1)^5(1−5T)=sum c_i T^i, as in audited L106,
and let U=P¹_Q minus {0,1,infinity}. Fix w²=−3. Define

    H0(u,z)=sum_i c_i sum_{2k<=i} binom(i,2k) u^(i−2k)(−3z)^k,
    H1(u,z)=sum_i c_i sum_{2k+1<=i} binom(i,2k+1) u^(i−2k−1)(−3z)^k,
    s=H0(u,z),   E=z*s*(s−1),
    A=Q[u,z,1/E]/(H1),   R=A[v]/(v²−z).

Write B°=Spec(A), D°=Spec(R). Let B and D be the smooth proper
normalizations of the reduced closures of these specified opens.
Only the closure of the open is taken: no components of unsaturated
projective equations are added. Existence and geometric integrality
of these curves are established below.

Let Ytilde and Ctilde be L107's unmarked and marked curves, of genera
38 and 75, with opens Y and X and their coordinates (r,u,z) and
(r,u,v). No rational point, integer solution, positivity condition or
remaining-factor decomposition is assumed.

## Conclusion

B° and D° are smooth geometrically integral covers of U of degrees
55 and 110. Their proper normalizations B and D have genera two and
three respectively, each with one geometric component and full
constant field Q. The map D -> B is finite étale of degree two
everywhere, including the boundary.

Forgetting r gives finite degree-nine morphisms Ytilde -> B and
Ctilde -> D over Q. The square formed with the two marked double
covers is Cartesian on the opens and on the smooth proper models.
Forgetting r is an incidence morphism; no group action on Ytilde
with this quotient is asserted.

For P=(u,z) in B°(Q), the polynomial

    Q_P(T)=(T−u)²+3z

is an étale quadratic direct factor of phi(T)−s. Conversely every
rational monic quadratic factor of a fiber at s in U(Q) gives one
such P. The point lifts to D°(Q) exactly when

    z is a nonzero rational square,
    equivalently [disc(Q_P)]=[−3] in Q*/Q*².

There are exactly two rational lifts in that case, marking the two
roots in Q(sqrt(−3)); otherwise there are none. This does not restore
a rational root in the complementary degree-nine factor.

For any rational point P of B, including every boundary point, choose
a uniformizer tau at P. Then ord_P(z)=2m is even. With the unit
eta=z*tau^(−2m) and its residue eta_P in Q*, one has

    P lifts to D(Q) iff eta_P is a rational square
                      iff [−12 eta_P]=[−3].

The fiber is Spec(Q[h]/(h²−eta_P)). It consists of two rational
points if eta_P is square, and a degree-two point otherwise. The
criterion is independent of the uniformizer. It concerns normalized
fibers at the boundary, not disjoint factors of a degenerate polynomial.

The complete geometric boundary data of B -> P¹ are:

| Base value | Ramification indices, with multiplicity | Orders of z, with multiplicity |
| --- | --- | --- |
| 0 | eleven indices 5 | four orders 2, seven orders 0 |
| 1 | twenty-eight indices 1, nine indices 3 | one order 2, thirty-six orders 0 |
| infinity | five indices 11 | five orders −2 |

Every point in each row has two geometric lifts to D with the same
index over P¹. These are geometric counts, not rational residue-field
decompositions or a classification of B(Q).

## Proof

### Exact model, rational descent and unique component

Expansion modulo Q(T)=(T−u)²+3z gives the polynomial identity

    phi(T) mod Q(T) = H0(u,z)+(T−u)H1(u,z).                 (1)

In particular H1=0 makes Q divide phi(T)−s. Its discriminant is
−12z, nonzero on B°, and s lies in U. L106 proves that the whole
degree-eleven fiber is étale there, so this quadratic factor and
the degree-nine complementary factor are disjoint and étale.
Conversely a rational monic quadratic factor T²+bT+c has uniquely
u=−b/2 and z=(c−u²)/3. Its remainder in (1) vanishes exactly when
H1=0 and s=H0; étaleness gives z!=0. This proves the claimed
factor interpretation in both directions.

The algebra R is free over A with basis 1,v, and A injects into R,
also after any field extension. The involution v -> −v has invariant
ring exactly A, because 2 is invertible. Since z and hence v are
units, the derivative 2v is a unit. Thus D° -> B° is finite étale
of degree two, with its two geometric points exchanged freely.
This explicit invariant-ring construction verifies the quotient
hypotheses; it is the finite free quotient case of Stacks,
Proposition 39.23.9, [tag 03BM](https://stacks.math.columbia.edu/tag/03BM).
No boundary freeness is assumed here.

Over Qbar make the invertible linear change

    a=u+wv, b=u−wv;    u=(a+b)/2, v=(a−b)/(2w).

Then phi(a)−phi(b)=(a−b)H1(u,v²). Since v is invertible,
H1=0 is precisely phi(a)=phi(b), with a!=b. Their common value is
H0(u,v²) and belongs to U. This is a scheme isomorphism with the
ordered distinct-pair subcover of the twofold root fiber product,
not just a point correspondence. The root cover is finite étale of
degree eleven over U by L106. Its ordered distinct-pair cover is
finite étale of degree 11*10=110, so the same holds for D° after
descent. Quotient by interchanging a,b is the unordered-pair
cover of degree binom(11,2)=55. Its invariant coordinates are
u=(a+b)/2 and z=−(a−b)²/12. Hence B° is precisely that cover.

L106 establishes the actual geometric monodromy A_11, including
transitivity on ordered triples, hence on ordered and unordered
pairs. The finite-cover component/orbit correspondence therefore
makes both pair covers connected over Qbar. We import Stacks,
Theorem 58.6.2, [tag 0BND](https://stacks.math.columbia.edu/tag/0BND),
and its complex-cover comparison in Milne, *Lectures on Étale
Cohomology*, v2.21 (22 March 2013), Theorems 3.1 and 21.3,
pp.27,130–131, [author PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf).
The hypotheses hold on the connected characteristic-zero open U.
Smooth connected curves over an algebraically closed field are
integral, since distinct components of a regular curve cannot meet.
This proves geometric integrality of both opens. Their reduced
closures and proper smooth models each have one geometric component.
Their function fields have no nontrivial algebraic constants over Q:
such a separable extension would split after algebraic closure,
contradicting geometric integrality. In particular the full constant
field is Q, not the quadratic marking field.

Both morphisms to U and the double-cover inclusion extend uniquely
to nonconstant morphisms of smooth proper curves by Stacks,
Theorem 53.2.6, [tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1).
They are finite of the same function-field degrees 55,110 and two.
Their inverse images over U are exactly the original normal finite
étale covers. Thus no branch points outside 0,1,infinity can appear
on normalization. This also justifies taking the smooth proper
models rather than the arithmetic genus of an affine equation.

The descent above fixes the Q-form. Over Q, a point of D° has
a=u+vw in Q(w), v!=0, and phi(a)=s in Q. Its conjugate b is the
second root. Conversely every such nonrational a uniquely supplies
u,v in Q and the equations. Over Qbar the same cover is the
ordered-pair cover, but over Q it is its specified minus-three
twist. The geometrically ordered cover without this descent is not
silently substituted for D.

### Forgetful incidence maps on the proper models

On the opens, L107's equations are H0(u,z)−phi(r)=0 and H1(u,z)=0,
with z*s*(s−1)*Q(r) invertible. Thus forgetting r maps Y to B°.
Identity (1) factors phi(T)−s as Q(T)J(T) over A, where J has
degree nine and invertible leading coefficient −1215.
Over U, Q and J are relatively prime and their fibers are étale.
The algebra obtained by adjoining r with phi(r)=s and Q(r)
invertible is therefore A[r]/(J(r)). This is a finite étale algebra
of rank nine. Its geometric labels are exactly the nine choices
of r outside the prescribed pair, so Y -> B° is finite étale
of degree nine. L107's geometric integrality proves this is one
connected incidence cover; the degree count does not assume
that a rational point has a rational preimage.

Adjoining v²=z gives precisely X. Hence the open diagram is
Cartesian and X -> D° is also finite étale of degree nine.
The function-field inclusions give finite degree-nine proper maps
Ytilde -> B and Ctilde -> D by 0BY1. Boundary ramification for
these maps is permitted. Once D -> B is proved étale below, the
proper pullback D times_B Ytilde is finite étale over Ytilde and
is smooth and normal. Here finite-étale base change is Stacks Lemma
58.5.2, [tag 0BL6](https://stacks.math.columbia.edu/tag/0BL6);
normality and identification with normalization are Lemma 58.11.2,
[tag 0BQL](https://stacks.math.columbia.edu/tag/0BQL).
Its dense open is X, with the function field
of Ctilde. Every component of a nonempty finite étale cover of
the connected Ytilde dominates Ytilde and meets that open; the
integrality of X thus gives a single component. Uniqueness of the
smooth proper model identifies the pullback with Ctilde, proving
the proper Cartesian assertion.

### Complete branch action, genera and double-cover freeness

Use L106's actual root branch types (5,5,1), (3,1^8), (11).
At zero a fixed two-element subset would be a union of root
cycles. There is only one fixed root and the others have length
five, so there is no such subset. The 55 pairs form eleven
five-cycles. Their ramification contribution is 55−11=44.

At one, a fixed pair must lie among the eight fixed roots,
giving binom(8,2)=28 fixed pairs. The other 27 pairs form nine
three-cycles. There are 37 cycles and ramification contribution
55−37=18. At infinity all pairs form five eleven-cycles, with
contribution 55−5=50. This exhausts every label at every branch.

A length-e cycle completes to a normalization point of index e:
the local punctured complex disk cover is the one of degree e,
which fills as t -> t^e. This is the same cover comparison used
in L106/L107, valid here for these finite étale covers of U.
The corresponding smooth proper morphism is separable and all
ramification is tame in characteristic zero. Riemann–Hurwitz,
Stacks Lemmas 53.12.2 and 53.12.4,
[tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B), gives

    2g(B)−2=−2*55+44+18+50=2,       g(B)=2.                (2)

To verify the marked cover at every boundary point, let sigma be
the relevant inertia permutation. Its order is 5,3 or 11, all odd.
If sigma^e preserves an unordered pair, its restriction cannot
be the swap, which has order two. Thus sigma^e fixes both ordered
entries. The ordered cycle has exactly the same length e as the
unordered cycle. Its reverse ordering gives a distinct cycle;
otherwise a power of sigma would swap the pair. Hence each
unordered cycle has exactly two ordered cycles above it, each
with relative ramification index one. This proves boundary
freeness and, with characteristic-zero residue separability and
the étale open, proves D -> B finite étale everywhere.

The ordered-pair ramification contributions are accordingly
88,36,100, totaling 224 on 110 sheets. Thus

    2g(D)−2=−220+224=4,             g(D)=3.                (3)

Equivalently its étale double cover satisfies 2*3−2=2*(2*2−2).
The full constant fields checked above allow genus base change,
Stacks Lemma 53.8.2, [tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6);
the normalization interpretation is Stacks Lemma 53.18.2,
[tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0).

For completeness, the degree-nine incidence morphism has no
relative ramification above zero or infinity: all incidence and
pair cycles there have equal lengths five or eleven. Above one,
each of the 28 fixed pairs leaves six other fixed roots and one
moving triple available for r. It therefore has six incidence
points of relative index one and one of index three. Every other
pair has length three and all its incidence cycles have length
three, so their relative indices are one. The entire relative
ramification is 28*(3−1)=56, consistent with
2*38−2=9*(2*2−2)+56. The marked map doubles this ramification
to 112, consistent with 2*75−2=9*(2*3−2)+112.
These checks do not use a purported generator relation between
arbitrarily chosen representatives of the branch conjugacy types.

### Complete normalized lifting and the boundary orders of z

On B°, the marked cover is exactly v²=z, and disc(Q_P)=−12z.
With 2 invertible, Kummer theory (Stacks Lemma 59.28.1 and its
cohomology sequence, [tag 03PK](https://stacks.math.columbia.edu/tag/03PK))
and the torsor/section criterion (Lemmas 21.4.2–3,
[tag 03AG](https://stacks.math.columbia.edu/tag/03AG)) give the stated
square test. Explicitly, if z=v² with v in Q*, the roots are
u±v*w. They are distinct and nonrational, and generate Q(w).
Conversely discriminant class −3 gives z a nonzero square and
the two signs of v give the two rational lifts.

Let P be any closed point of B. Because D -> B is unramified,
at any point above P the valuation of z equals ord_P(z).
Since z=v² on D, this order is even, say 2m. For a local
uniformizer tau the function eta=z*tau^(−2m) is a unit.
Replacing v by h=v*tau^(−m) gives the local equation h²=eta.
The associated rank-two algebra over the DVR O_{B,P} is
finite étale because eta and 2 are units. It is normal, has
the same generic quadratic algebra as D and is therefore the
integral closure over that DVR. This is the unit-root case of
03PK, with normality and normalization supplied by 0BQL. Stacks
Lemma 15.116.2, [tag 09EV](https://stacks.math.columbia.edu/tag/09EV),
treats a root of a uniformizer, not this unit-root algebra, and is
not needed to establish its normality. Its residue algebra is
k(P)[h]/(h²−eta_P), retaining both the split and nonsplit cases.

When P is rational, k(P)=Q. That residue algebra proves exactly
the rational lifting criterion and the number of rational lifts.
Replacing tau by a*tau for a local unit a multiplies eta_P by
a(P)^(−2m), a square. The criterion is thus intrinsic. In particular
the normalized discriminant representative is −12 eta_P, whose
class equals −3 if and only if eta_P is square. Evaluating z
as zero or infinity at a boundary point would not give this test.

Here are all boundary orders, proved on geometric local branches,
rather than inferred merely from their required parity. At zero the
two roots alpha,beta of 3T²+T+1 each have ramification five,
and 1/5 is simple. Locally about alpha,
phi(alpha+x)=c_alpha*x^5+O(x^6), with c_alpha!=0.
After s=t^5 the five expansions start
alpha+d_alpha*zeta*t, for the five distinct fifth roots of unity
zeta and a nonzero d_alpha; the same holds at beta. This follows
by extracting the fifth root of the unit power series, possible
in characteristic zero. The inertia index for every pair is five,
so t is also a uniformizer on each completed pair branch, up to
a unit. Two roots in the same cluster have difference of exact
order one and therefore z=−(a−b)²/12 of order two. There are
2*binom(5,2)=20 such labels, hence four points. Every other pair
has different constant roots and z a unit: 35 labels give seven
points. This accounts for all eleven points over zero.

At one, phi(T)−1=−55T³+O(T^4) near zero. Its three local roots
have distinct leading coefficients after s−1=t³. The three
within-cluster pairs form one cycle, giving one point with order
two for z. The 24 pairs joining a cluster root to one of the
eight simple roots form eight three-cycles, all with z a unit.
The 28 pairs of simple roots are unramified and also have z a
unit, since the simple roots are distinct and nonzero. Thus
there is one order-two point and 36 order-zero points over one.

At infinity take s=t^(−11). The eleven expansions have leading
terms d*zeta*t^(−1), with −1215*d^11=1 and distinct eleventh
roots of unity zeta. All pair differences have exact order −1.
Each pair branch has index eleven, so t is its uniformizer up
to a unit, and all five boundary points have ord(z)=−2.
No other zero or pole exists because z is a unit on B°.
The geometric divisor degrees agree: 4*2+1*2−5*2=0.
These expansions verify every listed chart order; the normalized
unit test above retains its actual residue at whatever rational
boundary point is under consideration. No residue field or
rational point is assumed from a geometric branch label.

### Evidence, use and limitations

The general theorems above are imported, with their stated versions
and the primary Stacks statements inspected on 2026-10-20 in the
approved assessment. The need for this specialization is that those
theorems and the unordered-pair examples of Dèbes–Fried and Putz
do not compute this polynomial's pair curve or its rational twist.
No general quotient, comparison, Riemann–Hurwitz or Kummer theorem
is re-proved, and no originality is inferred from the calculation.

Run `python3 scripts/global-fiber-genus/forget_root.py`.
The full certificate is
`scripts/global-fiber-genus/forget-root-certificate.json`.
It saves the exact polynomial and both invariant polynomials,
checked by independent binomial and quadratic-remainder formulas;
all 55,110,495,990 labels and induced actions; every disjoint cycle;
all projection maps and relative indices; every geometric z order;
and all named checks. There are 3,082 passing checks and no failures.
The largest label universe is 990, below the cap 1000.
The script's branch permutations are individual representatives,
not a claimed branch-generator tuple; actual monodromy comes from
L106. The proofs of descent and normalized lifting above are not
replaced by the finite arithmetic.

The intermediate diagnostic succeeds: a verified pair-only model
has genus 2<38 and retains a reversible fixed-minus-three marking
test. This provides a smaller necessary rational-point image of
L107's curve, potentially useful for a later point method.
It gives neither B(Q) nor D(Q), an effective point method, a
rational root over each pair point, a compatible global complement,
or either L095 integer power/gcd/positivity system. The minus-eleven
branch and the main Beal gap remain open. Independent critical
audit of this specialization passes as recorded below.

### Independent critical audit, 2026-10-20

The audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-20-pair-only-quotient-critical-audit.md`.
The full audited proofs of L106 and L107 are inputs. The target is
exactly the pair-only construction and its proper maps and normalized
lifting; neither L108's unfinished boundary decomposition nor a
rational-point classification is assumed. The audit confirms the
mathematical assertions. The two explicit Stacks citations added above
clarify the existing base-change and normality arguments; no model,
genus, lifting condition or mathematical input lemma changes.

For the scheme identification, the quadratic-remainder identity (1)
is an identity over Q[u,z], not merely on rational points. R is free
over A on 1,v before integrality has been proved, and its invariants
are exactly A. Inverting E makes each of z,s,s−1 a unit, hence v a
unit in R. After adjoining w, the linear change from (u,v) to (a,b)
has determinant −2w, a unit. Moreover
phi(a)−phi(b)=2wv H1(u,v²), with 2wv invertible on this open.
Thus the equations and localizations identify the entire ordered
distinct-pair scheme, without a diagonal or nilpotent component.
Its invariant coordinates are the midpoint and −(a−b)²/12.
Their inverse recovers the monic polynomial (T−u)²+3z, so the
unmarked scheme is precisely the pair cover, of degree 55.
The marked scheme has degree 110; its rational equation remains
v²=z. In particular it is the specified minus-three twist, not the
untwisted rational ordered-root cover.

L106's actual A_11 monodromy is transitive on both label sets.
Consequently these geometric covers are connected and smooth, hence
integral. Their proper normalizations have the same geometrically
integral function fields and full constants Q. In particular z is
not a square in Q(B), since otherwise the generic algebra of D
would split, contrary to its integrality. The degree-two field
extension is genuine; it is not a constant quadratic extension.
The cited smooth-model theorem applies to all function-field
inclusions, and normalization uniqueness identifies the preimages
of U with the original finite étale covers. No additional branch
values arise from the chosen closures.

For the incidence algebra, monic division by Q gives a degree-nine
J with leading coefficient −1215, which is invertible over Q.
Since phi(T)−s is étale over U, its two factors Q,J are relatively
prime there: their resultant is invertible, as may be checked
in every geometric fiber. The Chinese remainder decomposition of
A[T]/(QJ), followed by inversion of Q(T), removes exactly the
Q-factor and gives A[T]/(J). Hence the degree is nine and the
algebra is finite étale. L107's open coordinates give exactly this
algebra, with v²=z adjoined in the marked case. Its connectedness
and that of the marked incidence open come from L107. This proves
the open Cartesian square and the degrees of the proper maps,
without inferring a rational preimage of a rational pair.

Every branch cycle is accounted for. At zero an invariant pair
cannot be a union of the root cycles of lengths 5,5,1; all 55
labels therefore form eleven cycles of length five. At one the
28 pairs of fixed roots are fixed, and the other 27 labels form
nine three-cycles. At infinity the five cycles have length eleven.
These contributions are 44,18,50, giving genus two. The ordered
action gives twice each cycle and contribution, hence genus three.
If a power of inertia preserves a pair, its restriction to that
pair has odd order, so it fixes both letters. Thus the two ordered
cycles above every unordered cycle have the same length. This
proves relative index one at every geometric boundary point.
Finite morphisms between these smooth integral curves are flat:
locally their finite modules over the base DVR are torsion free.
Index one and separable residue extensions give the unramified
condition; alternatively the geometric étale check descends.
This establishes finite étaleness everywhere before base change.

Above one, each fixed pair leaves six fixed roots and the moving
triple for the distinguished root. Its incidence fiber therefore
has six points of relative index one and one of index three.
There are 28 such pairs, giving relative ramification 56.
For a moving pair, all source and target cycles have length three.
At zero and infinity both lengths are respectively five and eleven,
so there is no additional relative ramification. The marked
incidence map has twice this contribution, 112. Thus the degree-nine
Riemann–Hurwitz checks agree with L107's genera 38 and 75.

Now form the proper pullback Z=D times_B Ytilde. By 0BL6 it is
finite étale over the normal integral Ytilde. By 0BQL its connected
components are normal integral curves dominating Ytilde. Every
component meets the inverse image of its dense open Y, which is
exactly the integral X. Therefore Z has one component and its
function field is Q(Ctilde). It is proper over Q and normal;
0BY1, or the normalization characterization in 0BQL, identifies
it with Ctilde. This proves the proper Cartesian assertion and
does not rely on an unjustified normalization of an arbitrary
fiber product.

For local lifting let O=O_(B,P), F=Q(B), with uniformizer tau.
Every point Q of D above P has e(Q/P)=1, so z=v² implies
ord_P(z)=2 ord_Q(v)=2m. Set eta=z tau^(−2m) in O*.
Then O'=O[h]/(h²−eta), h=v tau^(−m), is a domain: its generic
polynomial is irreducible because z is not a square in F.
It is finite free and étale since 2h is a unit. The normality
theorem 0BQL applies to this connected finite-étale cover of
Spec(O), so it is normal. It is the entire integral closure of
O in F(v): any element of F(v) integral over O is also integral
over O', hence belongs to O'. This retains every point above P
and gives the full residue algebra k(P)[h]/(h²−eta_P).

For rational P the completed base is Q[[tau]], with the given
constant copy of Q. The formal binomial series supplies a square
root of eta/eta_P in 1+tau Q[[tau]]. If eta_P is square, the
completed normalization is Q[[tau]] times Q[[tau]], with two
rational residue points. If it is nonsquare, it is
Q(sqrt(eta_P))[[tau]], with one degree-two residue point and no
rational point. This verifies both essential cases, including
negative m at poles. Multiplying tau by a local unit multiplies
eta_P by a rational square, so the test is intrinsic. The
discriminant is exactly −12z=−3(2v)² on the open and its
normalized representative is −12eta_P at the boundary. No
factor interpretation is assigned to degenerate fibers.

The boundary orders also follow independently from the actual
leading terms. At a zero-fiber critical root alpha of q, the
coefficient is (6alpha+1)^5(1−5alpha), nonzero since q has
distinct roots and q(1/5)=33/25. Within either five-root cluster
the distinct fifth-root leading coefficients give difference
order one; between clusters or at the simple root the difference
has order zero. Dividing the 20 within-cluster labels by five
gives four order-two points, with seven unit points. At one the
coefficient −55 is nonzero; the three within-cluster pairs give
one order-two point, the other 36 points have unit z. At infinity
the coefficient −1215 is nonzero, and all distinct eleventh-root
leading coefficients have difference order −1. All five points
have order −2. The pair indices are respectively five, three
(or one at simple pairs), and eleven, so the expansion parameter
used in each ramified case is a uniformizer of that pair branch.
There are no other zeros or poles and the divisor degree is zero.
This is geometric evidence, not a rational residue-field list.

The independent replay command is
`python3 scripts/global-fiber-genus/audit_forget_root.py`.
It reads the full original certificate without importing or
running its producer, expands phi by multinomial coefficients,
and verifies the full polynomial long-division identity and every
coefficient of H0,H1. It reconstructs all four complete label
sets, every action edge and disjoint cycle, every cycle owner,
all projections, every relative index and fiber degree, all
geometric z orders and the full summaries. All 3,082 original
check names and truth values and every certificate field are
checked. Its 3,167 checks pass with no failures. The full report
is `scripts/global-fiber-genus/forget-root-audit-certificate.json`;
the original certificate SHA-256 is
`d8c9aa175c32969a154861c99f3081a1fc24925e1eee6d589f562bb433265c46`.
The actual pair genus is 2 against required <38; the largest label
set has 990 elements against cap 1000. The replay verifies the
finite evidence, not the imported general theorems or the
geometric and local-ring arguments.

The audit therefore passes without a change of mathematical
conclusion or dependencies. This verifies an existing specialization,
not a new result beyond the sources checked. It leaves rational
points, degree-nine rational lifting, remaining-factor compatibility,
both L095 integer systems and the minus-eleven branch unresolved.

## Mathlib

Full matching pair-curve genus, twist and normalized lifting coverage
in Mathlib was not checked. Supporting formal theorems were not
searched in this step. No absence from Mathlib or Lean verification
is claimed; the precise named sources are mathematical inputs.
