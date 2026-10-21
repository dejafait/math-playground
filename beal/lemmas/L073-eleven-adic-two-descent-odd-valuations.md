# L073 — Full two-descent has odd valuations at the ramified eleven-adic place

## Hypotheses

Use L033's entire degree-twelve field K and curve

    E0: y²+y=x³−x²−10x−20.

Use L069's origin-preserving coordinates X=4x, Y=8y+4 and the SAME
cubic generator θ in

    Y²=g(X),     g(X)=X³−4X²−160X−1264,     D=K[θ]=K[X]/(g).

L041 identifies all completions above eleven as

    K tensor Q11 = Q11 × Q11 × L,
    L=Q11[r]/(r^10+55),     ord_L(r)=1,     ord_L(11)=10,

with residue field F11 in every base factor. For each such completion
F, let δ_F be the full cubic two-descent Kummer map
E0(F)/2E0(F) -> (D tensor_K F)^*/(D tensor_K F)^{*2}.
Every factor valuation below is its maximal-DVR valuation, normalized
to take value one on a uniformizer. No primitive solution, global point
approximation, class-group condition, or rank hypothesis is assumed.

## Conclusion

There is a simple root α in Q11, α=8 modulo 11, and, on putting
M=Q11(sqrt(-11)), the complete local cubic algebras are

    D tensor_K Q11 = Q11 × M       (at EACH rational base place),
    D tensor_K L   = L × L × L.

M/Q11 is totally ramified quadratic with residue field F11. Order the
three roots over L as α,β,γ, where β and γ reduce to 9. Then

    ord_L(α−β)=ord_L(α−γ)=0,     ord_L(β−γ)=25.

The full valuation images modulo two are exactly

    {(0,0)}                       at each rational base place,
    {(0,0,0),(0,1,1)}             at the degree-ten base place.

In particular, the exactly defined local two-torsion point (X,Y)=(β,0)
has Kummer component valuations (0,25,25). Its E0 coordinates are
(x,y)=(β/4,−1/2). Thus the universal all-even local containment above
eleven is FALSE. Eleven cannot be deleted from exceptional valuation
support by asserting that full local containment. This does not prove
that any global E0(K) point has odd valuations, that the global image
fails all-finite-even containment, or that any Beal branch is empty.

## Proof

### Imported general inputs and scope of the specialization

The prior assessment is
`drafts/literature/2026-10-15-eleven-adic-even-valuation-containment.md`,
SPECIALIZE at invocation start. We reuse its inspected primary results.

For any finite extension F/Qp and its full cubic étale algebra, the
Kummer-image size is

    |δ_F(E0(F)/2E0(F))|=[O_F:2O_F] |E0(F)[2]|.

This is Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and
quadratic twists of elliptic curves*,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Lemma 1.3 and Remark 1.4, printed p.4;
Math. Res. Lett. 28 (2021), 1633–1659,
[DOI](https://doi.org/10.4310/MRL.2021.v28.n6.a1).
This local size statement needs none of Definition 1.6's additional
containment hypotheses. Here p=11, so 2 is a unit and the index is one.

For the exceptional evaluation, if g=(X−a)h and P=(a,0), the full
odd-degree class is represented by

    (a−θ)+h(θ).

Its value in the factor θ=a is h(a)=g'(a); in every other root factor
it is a minus that root. This is Bruin–Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. 78 (2009), 2347–2370,
[14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 2 and Remark 2.1, printed p.3; Section 9, printed p.15,
identifies the monic cubic genus-one case with ordinary two-descent.
Infinity has class one. These are full algebra classes with no scalar
quotient. General Kummer identification, exceptional evaluation and the
image-size theorem are imported, not reproved.

Hensel lifting and the Eisenstein local-field conclusions are the
inspected inputs in L041: Pete L. Clark, *Algebraic Number Theory II:
Valuations, Local Fields and Adeles*,
[161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
no identified revision date, Theorems 1.75/1.79, printed pp.57–58,
and Proposition 2.9/Corollary 2.10, printed p.65. Each lifting below
has integral coefficients, a root modulo the maximal ideal and a unit
derivative. Only the exact local specialization is supplied here.

### The entire cubic at both rational places

Direct polynomial arithmetic gives

    g(X) = (X−8)(X−9)² modulo 11,
    g'(8)=−32=1 modulo 11.

For example, the exact difference from the displayed integer product is
11(2X²−35X−56). Simple-root Hensel lifting therefore gives a UNIQUE
root α=8 modulo 11 in Q11. Divide by this root to write

    g(X)=(X−α) q(X),
    q(X)=X²+(α−4)X+(α²−4α−160).

The resultant of X−α with q is q(α)=g'(α), a unit. Since L069 gives

disc(g)=−256·11^5, the quadratic discriminant is exactly

    Δ=disc(q)=−256·11^5/g'(α)²
              =−11 (16·11²/g'(α))².                 (1)

The valuation v11(Δ)=5 is odd, so Δ is not a square in Q11. Hence q
is irreducible and its root field is exactly M=Q11(sqrt(-11)). The
polynomial Z²+11 is Eisenstein; M is totally ramified of degree two,
with residue field F11 and ord_M(11)=2. CRT gives the full cubic as
Q11 × M, not a selected factor. This argument applies separately at
both rational places because the cubic and its generator come from Q.

### Full splitting after the actual degree-ten base change

The unit 5 has a square root s in Q11: start with 4 modulo 11 in
Z²−5, whose derivative is 8 modulo 11. In L put

    z=r^5/s,     z²=−11,
    d=(16·11²/g'(α))z.

By (1), d²=Δ. Consequently BOTH remaining roots belong to L:

    β=(4−α+d)/2,     γ=(4−α−d)/2.

All three roots are distinct, since Δ and g'(α) are nonzero. These
formulas exhaust the degree-three polynomial, proving L³ is the entire
base-changed algebra. Since s and g'(α) are units,

    ord_L(d)=2·10+5=25.

Both β and γ have residue (4−8)/2=9 in F11; α has residue 8.
Thus α−β and α−γ are units, while β−γ=d has valuation 25.
No maximality of the polynomial order generated by θ is assumed.
In particular, the value 25 uses ord_L(r)=1, rather than the valuation
normalized by ord(11)=1.

### Complete rational-place images

The point Pα=(α,0) is rational over Q11 on Y²=g(X), and its
exceptional class in Q11 × M is

    δ(Pα)=[(g'(α), α−β)],

where β denotes either chosen root of q in M. Both entries are units:
their residues are respectively 1 and −1=10 in F11. The latter is
not a square; the nonzero squares of F11 are {1,3,4,5,9}. A square
unit in M has square residue, so this full class is nontrivial.

The only Q11 root of g is α. Hence E0(Q11)[2]={O,Pα}, of size two.
The cited local size theorem gives exactly two Kummer-image classes,
so they are 1 and δ(Pα). Every component valuation is zero modulo
two. This certifies the full image at EACH rational base place,
including infinity and every other exceptional evaluation, without
assuming containment from the residue characteristic alone.

### The exact odd class and complete ramified-place valuation image

In L³, with factors ordered α,β,γ, the same exceptional formula gives

    δ(Pα)=[(g'(α), α−β, α−γ)],
    δ(Pβ)=[(β−α, (β−α)(β−γ), β−γ)],     Pβ=(β,0).

All entries are nonzero. The first vector consists of units and its
last two entries have residue −1, a nonsquare in F11, so its class is
nontrivial in (L^*/L^{*2})³. The second vector has EXACT
component valuations (0,25,25). Its parity vector (0,1,1) is nonzero,
so it is nontrivial and independent of the first class, whose parity
vector is zero. Valuation parity is well-defined on square classes
because multiplication by a square changes each valuation by an even
integer.

Since g splits into three distinct roots in L, E0(L)[2] has four
elements, and the cited size theorem gives a Kummer image of size
four. The two independent displayed classes therefore generate that
whole image. Its valuation image is precisely {000,011}; all four
classes, all points and all exceptional cases are included. At Pβ the
norm of the displayed representative is ((β−α)(β−γ))², as required
for a norm-square class despite the two odd component valuations.

The point is exact, defined by Hensel roots and the algebraic formulas
above; no residue sample is promoted to a local point. The inverse
coordinate change gives x=β/4 and y=−1/2 on E0. Distinct local roots
do not contradict L069's global irreducibility or E0(K)[2]={O}.
No global rationality or approximation assertion is made.

### Relevance, stopping decision and remaining gaps

The required universal even-valuation threshold fails at precisely the
ramified base place in this calculation. The two rational places meet
it. The complete decompositions account for all 36 Q11-dimensions:
two copies of degrees 1+2, and three copies of degree 10. Thus no base
place or cubic factor was omitted.

This is a NEGATIVE result for deleting eleven using full local
containment. Preserve L072's conditional all-finite-even criterion and
ATTEMPTS/032: neither is contradicted. A later global descent upper
space allowing exceptional eleven support requires its own assessed
target. Other finite places, the global class-norm kernel, filtered
unit and non-unit dimensions, rank, subgroup indices/cosets and
primitive integer lifting remain unresolved. There is no rank bound,
54a1 exclusion, Beal counterexample or complete Beal candidate here.
The result specializes the cited standard methods; originality beyond
the sources checked is not claimed. The separate critical audit below
confirms this result without correction.

### Independent critical audit — 2026-10-15

The audit used the separately approved SPECIALIZE assessment
`drafts/literature/2026-10-15-eleven-adic-two-descent-audit.md`.
It found no mathematical correction. General Hensel, Eisenstein, Kummer
evaluation and local-image-size theorems remain imported through the
precise citations above; this audit verifies their specialization, not
their general proofs. In particular, BPT Section 1, Lemma 1.3 and
Remark 1.4 apply to the full square-free cubic algebra, including
products, without the later containment hypotheses.

**Fixed inputs and complete factors.** L033 supplies the entire field
and the curve independently of a primitive solution's existence. The
relevant L041 proof was checked: the two simple residue roots of its
defining polynomial have derivative residues 6 and 5; the complementary
degree-ten Hensel factor is Eisenstein because the shifted constant is
−209 and the other factor has unit constant residue 5. Its uniformizer
π satisfies π^10/11=6 in the residue field. Hence −55/π^10 has residue
one, and the tenth-root lift has derivative 10, a unit. This justifies
the exact model r^10=−55, not only its ramification degree. For L069's
coordinate change, (8y+4)^2=64(y²+y)+16 is exactly g(4x) on E0;
it is an invertible pointed isomorphism and preserves the two-torsion.

**Independent cubic arithmetic.** Writing a for an indeterminate,
q_a(X)=X²+(a−4)X+(a²−4a−160) satisfies
(X−a)q_a(X)=g(X)−g(a). Its discriminant is
−3a²+8a+656. Exact reduction modulo g(a) verifies

    (−3a²+8a+656)(3a²−8a−160)² = −256·11^5.

The independent cubic-discriminant formula gives the same integer
−41229056. At the simple root α, g'(α) has residue 1, so the quadratic
has discriminant of valuation exactly five and is irreducible over
Q11. The quadratic Eisenstein polynomial Z²+11 proves its full root
field has residue field F11. In L, the lift s²=5 exists from residue 4,
and z=r^5/s has square −11 and normalized valuation five. Thus d has
valuation 25 exactly. The formulas for β,γ give residues 9,9, distinct
from α's residue 8; all three actual roots are distinct and exhaust g.
The two rational base places contribute dimension three each and the
third contributes thirty. This verifies the whole dimension 36 and
every normalized maximal-prime valuation used above.

**Exceptional values and exhaustiveness.** In the root-a component,
(a−θ)+h(θ) equals g'(a); in the other components h vanishes. This
recovers every displayed exceptional entry, all nonzero. Over Q11 the
second entry for Pα is a unit of residue 10 in M. Over L both its last
entries have residue 10. Since the residue field in each case is F11
and 10 is not in {1,3,4,5,9}, these classes remain nonsquares; ramified
extension has not been assumed to preserve arbitrary nonsquares.
For Pβ the valuations are exactly (0,25,25), and its representative
norm is ((β−α)(β−γ))². Its nonzero parity separates its class from
both the identity and the zero-parity nonidentity class of Pα.
Consequently the generated subgroup has size four over L. The cited
size theorem gives exactly two classes at each rational base place
and exactly four over L, because 2 is a unit and the respective
two-torsion orders are two and four. The displayed subgroups therefore
exhaust the images; the argument leaves no untested point disk or
exceptional evaluation. Infinity contributes the identity.

**Arithmetic certificate and limits.** Run
`python3 scripts/eleven-adic-two-descent/audit_local.py`.
The independent standard-library implementation records all fourteen
exact checks in
[the full certificate](../scripts/eleven-adic-two-descent/audit-certificate.json).
All fourteen pass, and all actual/required values were inspected in
full. The achieved odd valuation is 25 against the even-valuation
requirement; the complete parity images have sizes one, one and two.
The certificate checks finite identities only; the preceding lifting,
residue-field and image-size arguments establish exact realization
and completeness. No numerical approximation is used as proof.

The audit therefore confirms the local stop in ATTEMPTS/033. It neither
constructs a global point in the odd class nor disproves global
all-finite-even containment. L072's conditional criterion remains
unchanged. The audit adds verification of a local input, not a new
theorem beyond the assessed methods, a rank bound or a Beal exclusion.

## Mathlib

Full matching eleven-adic decomposition and complete Kummer valuation
images: **not checked**. Supporting Hensel, Eisenstein, CRT,
discriminant, square-class, exceptional two-descent and local image-size
coverage: **not checked**. Unknown coverage is not absence.
