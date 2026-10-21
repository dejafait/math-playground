# Two-descent even valuations above eleven — completed source comparison

TARGET: Determine whether the full local two-descent Kummer image at every place of K above 11 has even valuations in L069's entire cubic algebra.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bare-unit, rational-dyadic, rational-cubic and eleven-adic local-algebra assessments; checked L033, L041, L069, L072, ATTEMPTS/032 and history/229. Searched odd-prime Kummer unit containment, multiplicative reduction, component indices and the exact curve; inspected the primary passages below. No inspected theorem decides this exact all-place specialization.
SOURCE_EVIDENCE: BPT arXiv:2001.02263v3 (17 September 2020), Section 1 p.3, Lemmas 1.3/1.5 and Remark 1.4 p.4, Definition 1.6/Remark 1.7/Theorem 1.8 pp.5–6 with all proof cases, Examples 1–3 and Corollary 1.9 p.6, https://arxiv.org/pdf/2001.02263v3; Bruin–Stoll 14 March 2008 manuscript Section 2/Remark 2.1 p.3, Lemma 4.3 pp.6–7, Lemma 4.4 and complete SquareClasses/LocalImage proof cases pp.7–10, Section 9 p.15, https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf; Simon 2002 Propositions 1.1–1.4 and complete Proposition 1.4 proof pp.8–9, https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf. Reused Clark local-field coverage as specified below.
COMPARISON: Known conditional unit-containment and full-image methods cover the required test, including bad reduction and exceptional points. Odd residue characteristic alone gives no containment; neither L070 nor the five-isogeny calculations decide it. The remaining difference is the exact cubic base change and Kummer valuation calculation at L041's three places.
GAP: All specialized local factorizations, theorem applicability and valuation parities remain to be proved; this review establishes neither containment nor a counterexample. Ordinary class-norm data, other finite places, rank, index/coset bounds and primitive integer lifting remain independent gaps.
REASON: Essential source coverage is now adequate for one bounded mathematical specialization of the unchanged target; import the general results and prove only the local arithmetic difference, without reproving descent theory.
SCOPE: Exactly TARGET for L033's K and E0, L069's entire cubic D, maximal integer rings and all factors at every place above 11. Direct valuation proofs, exact point/exceptional evaluations and complete-image certification by known size or proved local disks are covered. No class-group calculation, global Kummer containment or rank theorem is approved.
LITERATURE_REASON: The invocation required a literature-only review of this uncovered eleven-adic target; prior ready dyadic coverage did not assess odd-prime bad-reduction hypotheses after ramified base change.

## Target, relevance and existing evidence

The main gap remains positive primitive integer emptiness, including the
54a1 branch of ordered (3,4,11). The intermediate target tests one
prerequisite for using audited L072's all-finite-even space W as a global
two-descent upper space. Success would justify omitting eleven from the
exceptional valuation support at this local stage. It would not prove
that units exhaust W or give a rank bound.

The fixed inputs are L033's entire degree-twelve field K and
E0: y²+y=x³−x²−10x−20, L069's origin-preserving model
Y²=g(X), g=X³−4X²−160X−1264, and D=K[X]/(g).
L069 already proves that g is square-free and globally irreducible.
L041 supplies the complete base algebra

    K tensor Q11 = Q11 × Q11 × L,  L=Q11[r]/(r^10+55),

with ramification/residue pairs (1,1),(1,1),(10,1). This is existing
base-field evidence, not the still-uncomputed decomposition of D at
those places. The two rational places must both be covered; identical
rational curve coefficients may allow the same justified local argument.
Normalize each maximal-prime valuation by a uniformizer, not by 11.
No cross-notebook input is used.

The duplicate/failure check found no existing result for this target.
ATTEMPTS/032 stops the unfiltered unit shortcut, and remains intact.
The rational-dyadic and rational-cubic assessments cover a different
place and localization question. L041–L044 concern a fifth-power
connecting map, so their image vectors cannot be reused as two-descent
image evidence. L072 and its accepted audit supply a conditional
class-norm criterion, without this local containment premise.

## Primary theorem comparison

**BPT.** Daniel Barrera Salazar, Ariel Pacetti and Gonzalo Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020; Math. Res. Lett. 28 (2021), 1633–1659,
[DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1).
Locators above refer to v3. For a finite extension F/Qp, use its full
cubic algebra A and maximal ring O_A. Definition 1.6 assumes an integral
monic square-free cubic and one of: A a field; O_A generated by that
cubic root; odd residue characteristic and odd nonsingular-reduction
subgroup index; or unramified dyadic base and good reduction.
Theorem 1.8 gives norm-square unit containment; Corollary 1.9 gives
equality at odd p. Lemma 1.3 gives full image size
[O_F:2O_F] times |E(F)[2]| independently of those alternatives.
Examples 1–3 exhibit failure without them, including multiplicative
reduction. The proof's field, split, quadratic-factor, component-index
and dyadic cases were inspected. No converse is asserted.

This comparison leaves every relevant alternative to be checked over
the actual local base, especially L. Failure to establish an alternative
is not a counterexample. The source's E^0(F), points with nonsingular
reduction, must not be confused with our curve's name E0. Rational-field
component information cannot be transferred unchanged to a ramified
completion. A nonunit polynomial discriminant alone settles neither
maximality nor containment. No global narrow-class hypothesis is needed
for these local statements; their separate global Selmer bounds are
not approved here.

**Bruin–Stoll.** Nils Bruin and Michael Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. 78 (2009), 2347–2370;
[14 March 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf).
Section 2 and Remark 2.1 use the full square-class algebra without scalar
quotient for odd degree. If f=(x−a)h, the exceptional image at (a,0) is
represented by (a−theta)+h(theta); the monic odd-degree infinity image
is 1. Lemma 4.4: for irreducible h, integral x0 and e>=0, the strict
coefficient-valuation inequality

    ord(h(x0+epsilon*pi^e)−h(x0)) > ord(h(x0))

makes (x0−theta)(x1−theta) a square whenever
x1 lies in x0+pi^(e+ord(4)) O. The complete algorithm discussion covers
realization, termination, root neighborhoods and reciprocal nonintegral
charts. Section 9 identifies the monic cubic genus-one case with usual
two-descent. Lemma 4.3's discriminant-valuation-at-most-one hypothesis
prevents treating it as an unconditional bad-prime shortcut.

These formulas allow a point or two-torsion witness, or an exhaustive
local calculation, while retaining O and every exceptional point.
If using a finite disk computation, cite the precision theorem and prove
its strict inequality for every irreducible factor involved. A residue
sample does not establish exact realization or completeness. Prefer a
short exact valuation argument or an image-size certificate when it
already answers the target; no general algorithm implementation is
required.

**Simon.** Denis Simon, *Computing the rank of elliptic curves over
number fields*, LMS J. Comput. Math. 5 (2002), 7–17,
[primary publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf),
[DOI](https://doi.org/10.1112/S1461157000000668).
Propositions 1.1–1.2 apply to an integral irreducible cubic over a number
field. Proposition 1.4 retains primes dividing the derivative at theta
above base primes whose squares divide the cubic discriminant. Its
complete proof handles negative x-valuation and the discriminant-one
case. It supplies support control, not permission to delete eleven.
Use BPT/Bruin–Stoll for split local algebras and rational two-torsion,
rather than silently extending Simon's stated irreducibility scope.

**Local-field inputs reused.** The inspected Clark coverage in
[drafts/literature/2026-10-08-primitive-eleven-connecting-valuations.md](2026-10-08-primitive-eleven-connecting-valuations.md)
and L041 is adequate for factorization and root lifting: Pete L. Clark,
*Algebraic Number Theory II: Valuations, Local Fields and Adeles*,
[author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
accessible 161-page version, no identified revision date; tensor/CRT
p.53, coprime Hensel factor lifting Theorem 1.75/Remark 1.76 p.57,
Hensel–Newton Theorem 1.79 p.58, Eisenstein Proposition 2.9/Corollary
2.10 p.65. Preserve their complete-DVR and strict derivative hypotheses.
Repeated residue factors do not establish irreducibility or maximality.
The five-isogeny theorems in that earlier assessment are outside this
reuse; its elementary local-field inputs do not depend on isogeny degree.

## Search record and bounded mathematical continuation

Queries: `2 descent elliptic curve local image odd prime multiplicative
reduction even Tamagawa units cubic algebra`; `Barrera Pacetti Tornaria
2 Selmer Theorem 1.8 1.11 odd prime local condition`; `"11a1" "2-descent"
"11"`; `"2-Selmer" "even" "multiplicative" "valuation" cubic`;
`"local image" "Kummer" "odd" "component" elliptic units`.
The useful primary match is the BPT conditional theorem and its explicit
failure examples; Bruin–Stoll supplies a general fallback. The exact-curve
query produced no inspected theorem matching the target. Unverified
research claims and unrelated code pages in search results were not used.
No novelty is inferred. No additional source blocker remains for the
bounded test. Other search leads are not mathematical inputs.

The next research turn should base-change g in full over both rational
places and L. Certify every factor and its maximal valuation normalization.
First check whether the conditional containment theorem applies; if so,
import it with the local hypotheses proved. Otherwise evaluate exact
local points, including rational two-torsion by the exceptional formula,
and use the full-image size theorem or proved exhaustive valuation cases
when claiming positive containment. Model changes must preserve the
specified Kummer map. No alternate cubic generator is silently treated
as a new Weierstrass coordinate.

Acceptance threshold: every component valuation is even for every point
at all three places. A single exactly realized point class with an odd
component disproves the universal local containment statement; full
image enumeration is unnecessary for that outcome. In that case park
this all-even local route and retain exceptional support in a later,
separately assessed descent target. A local counterexample would not
prove that any global point has that class, invalidate L072's conditional
criterion, or exclude a Beal branch. If the bounded attempt is inconclusive,
record the exact unresolved factor, root or image-completeness obligation.

This SPECIALIZE decision approves the unchanged target for one subsequent
REPRODUCTION attempt. It does not certify a local answer. Class-norm
kernel data, all other finite-place containment, further local pruning,
rank below twelve, subgroup indices/cosets and primitive integer lifting
remain unresolved. Mathlib matching and supporting coverage: not checked.
No lemma, mathematical script, PROOF or DAG was changed in this review;
full specialized proofs and citations belong in a canonical lemma only
if the later mathematical attempt establishes a result.
