# L085 — Exact primitive whole-fiber two-descent image at eleven

## Hypotheses

Use L033/L034's entire modular map on

    E0: y²+y=x³−x²−10x−20,

and the ordered full base algebra of L041,

    A11=Q11 × Q11 × L,    L=Q11[r]/(r^10+55).

Let s range over Q11 minus {0,1728}, with common nonzero primitive
a,b,c in Z11 satisfying a³+b⁴=c¹¹ and s=1728a³/c¹¹. Consider every
isomorphism from the entire modular fiber B_s to A11 and the resulting
tautological point in E0(A11). Use L069's origin-preserving coordinates
X=4x, Y=8y+4 and the same distinguished generator θ of

    g(X)=X³−4X²−160X−1264.

At each rational base factor use L073's full cubic algebra Q11 × M,
where M=Q11(sqrt(−11)), ordered by the simple root α=8 modulo eleven
and the quadratic factor. At the L factor order the full cubic L³
by α,β,γ, with β,γ=9 modulo r. No global class, rank, positivity,
other-prime condition, or bounded-precision assumption is imposed.

## Conclusion

In the full cubic square-class groups put

    ε_Q=[(1,−1)] in (Q11 × M)^*/(Q11 × M)^{*2},
    ε_L=[(1,−1,−1)] in (L³)^*/(L³)^{*2}.

The exact primitive whole-fiber two-descent image is

    J11 = {(1,1,1), (ε_Q,ε_Q,ε_L)}.

Every compatible primitive scalar has residue 4 or 10 by L044.
Residue 4 always gives the first tuple and residue 10 always gives
the second. Both occur at exact finite common scalars and entire
fibers. Each ε is nontrivial. Thus this particular restricted set is
a subgroup of order two, whereas the unrestricted product image has
order 2·2·4=16. Subgroup status is a consequence of the exact list,
not an assumption about restricted images.

This is a necessary primitive-point filter only. It neither proves
an additional independent global condition nor improves L084's
13+dim ker(n_S) bound, decides the class kernel, bounds full rank,
or excludes any integer solution. The separate critical audit below
confirms this local statement without correction.

## Proof

### Assessed imports and conventions

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-primitive-eleven-two-descent-image.md`.
This is REPRODUCTION of its assessed methods. We reuse the precise
theorem coverage; no new general local descent theorem is reproved.

The entire modular map is the one in Freitas–Naskręcki–Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio
Math. **156** (2020), 77–113,
[10 June 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, equation (7.4), PDF pp.25–27, as fixed in L033/L034.
Its GRH-dependent Selmer calculation and its dyadic Lemma 7.6 are
not inputs to this eleven-adic calculation.

For the full cubic Kummer map use Bruin–Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. **78** (2009), 2347–2370,
[14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Section 2/Remark 2.1, p.3, and Section 9, p.15. At the non-root
affine points below its value is [X−θ], without a scalar quotient.
Exceptional evaluations and infinity are retained by the general
map, but the proved scalar and coordinate restrictions below exclude
them from these fibers.

L073 applies Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups
and quadratic twists of elliptic curves*, Math. Res. Lett. **28**
(2021), 1633–1659,
[arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
17 September 2020, Lemma 1.3 and Remark 1.4, p.4, to obtain full
image sizes two, two and four. The identity
|δ_F(E0(F))|=[O_F:2O_F]|E0(F)[2]| applies at these finite extensions
of Q11 without the additional containment hypotheses of Theorem 1.8.

For Hensel lifting use Pete L. Clark, *Algebraic Number Theory II:
Valuations, Local Fields and Adeles*,
[161-page author notes, no identified revision date](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
Theorem 1.79, p.58. In a complete DVR of residue characteristic eleven,
a unit with nonzero square residue is a square: lift a residue square
root using derivative 2u, a unit. Conversely a square unit has square
residue. We apply this only in the full fields already identified by
L041/L073, all with residue field F11. No precision sample or assertion
about the polynomial order replaces a maximal-DVR statement.

### Uniform reduction of every compatible fiber

L044 proves that every scalar in these hypotheses is integral with
residue in {4,10}; it excludes all negative scalars and both primitive
branch disks uniformly. L042 then gives one smooth rational root

    x_sm=5−s+s² modulo eleven

and eleven cluster roots, all of the form

    x=16+121Z,    Z=1/(s−1) modulo the maximal ideal.

Every cluster root is included, through every embedding, and the
reconstruction y=(sd−a(x))/b(x) identifies all twelve roots with the
whole fiber. Here a(x),b(x),d(x) denote the fixed modular polynomials,
not the primitive scalar witnesses. The smooth root has b(x) a unit;
each cluster root has v11(b(x))=20. Also x=16 is excluded since
F(16,s)=11²²(s+121) is nonzero. These facts are proved in L042 for
all unit parts, rather than inferred from sampled scalars.

For a compatible fiber, the rational factors consist of the smooth
point and one rational cluster point, in either order; the degree-ten
factor is a cluster point generating L. Write v for the extension of
v11 with v(11)=1, so ord_L=10v. The residue Z is 4 if s=4 modulo
eleven, and 5 if s=10 modulo eleven.

### Full unit classes at the clustered points

L073 gives the exact roots

    c0=(4−α)/2,    β=c0+d0/2,    γ=c0−d0/2,
    v(d0)=5/2,    g'(α)=1 modulo eleven.

The same formulas apply in M and in L, and α has residue 8.
The unique lifts of α modulo 121 and 1331 are 118 and 844.
Consequently

    c0=911=64+121·7 modulo 1331.

These are exact congruences for the Hensel root: substitution in g
checks the residual zeros and g' remains a unit. For any cluster root,
X=4x=64+484Z, hence

    (X−c0)/121 = 4Z−7 modulo the maximal ideal.

The residues are 9 for Z=4 and 2 for Z=5, both nonzero. Thus
v(X−c0)=2. Since v(d0/2)=5/2>2, the two units
(X−β)/121 and (X−γ)/121 have those SAME residues. This proves
uniform square-class constancy on every feasible cluster point,
including all fractional-valued variations of Z in L. The normalized
L valuations of X−β and X−γ are both 20, and over M they are both
4; dividing by 121 removes an actual square, not merely an even
valuation. The other component X−α is a unit of residue
64−8=1 modulo eleven.

The nonzero squares in F11 are {1,3,4,5,9}; −1 has nonsquare residue
10. A nonsquare unit is in the square class of −1, because its ratio
to −1 has square residue and Hensel applies. Therefore every rational
cluster point has Kummer class 1 for residue s=4 and ε_Q for residue
s=10. Every degree-ten cluster point has class 1 or ε_L respectively.
In particular, none of these points has X equal to a cubic root.

### The smooth point and correlation of all factors

At the smooth rational point all cubic differences are units. The
complete residue computations are

| s mod 11 | x_sm mod 11 | X−α mod 11 | X−β mod 11 (=X−γ) |
| --- | --- | --- | --- |
| 4 | 6 | 5 | 4 |
| 10 | 7 | 9 | 8 |

Thus its class in Q11 × M is respectively 1 and ε_Q. This is the
same class as the rational cluster point at the SAME scalar.
Consequently both rational-factor permutations give identical tuples.
Every Q11-embedding of the degree-ten factor fixes the residue field
F11 and the rational number 121; the preceding unit-residue argument
applies to each embedded Z. Any interchange of β and γ also preserves
the displayed class. No selection of independent local points has
entered the upper containment.

We have proved J11 is contained in the asserted two-element set,
including full unit square classes. The branch disks and poles were
already excluded, and the nonzero differences just established rule
out every exceptional two-torsion evaluation in the remaining fibers.

### Exact whole-fiber realization of both tuples

L042 already realizes residue 4 with x=500=16+121·4 and
y=60+121V, where V is the exact Hensel root

    V²+V=8520,    V=2 modulo eleven.

Its entire fiber is A11 and L041 supplies common primitive witnesses.
It therefore realizes the identity tuple, not just its components.

For residue 10 use x=621=16+121·5 and y=60+121V. Direct substitution
in E0 gives

    V²+V=6·5+47·5²+121·5³=16330.

At V=8 modulo eleven the residual equation is zero and derivative
2V+1 has residue 6. Hensel therefore gives an exact V in Z11 and
an exact point P_R. Set s=j(P_R). At x=621 the scaled modular
coefficients satisfy

    b(x)/11²⁰=1,
    (a(x)+60b(x))/11²²=9,
    d(x)/11²²=5                 modulo eleven.

They are integral units. The denominator d is nonzero, so s is
integral and its residue is (9+8)/5=10. In particular s is neither
0 nor 1728, and this is one shared scalar throughout the construction.

Here is the full factor check, using L042's uniform coefficient
identities. There is a smooth rational root at this s. Removing it,
rescaling x=16+121Z and dividing by the leading unit gives L042's
monic integral polynomial M_s(Z) of degree eleven, with reduction
(Z−5)¹¹. The constructed point supplies its rational root Z=5.
Then

    G(W)=M_s(5+W)/W

is monic integral of degree ten, reduces to W¹⁰, and L042's derivative
table at residue s=10 gives G(0)/11=5 modulo eleven. It is therefore
Eisenstein. If w is its root, division of G(w)=0 by eleven gives
w¹⁰/11=−5 in the residue field. The unit (−55)/w¹⁰ has residue one,
so Hensel with derivative 10 lifts a tenth root u of that unit.
Then (wu)¹⁰=−55. The Eisenstein degree-ten polynomial X¹⁰+55
shows that Q11(wu)=Q11(w), identifying this WHOLE factor with L.
L042's reconstruction accounts for all twelve distinct fiber points,
so B_s is exactly Q11 × Q11 × L. This proves entire-fiber realization
without assuming every scalar in the residue disk is compatible.

Finally s/1728 and 1−s/1728 are units. L041's simultaneous scalar
theorem supplies nonzero primitive a,b,c in Z11 at this very s,
using only cube and fourth-root Hensel lifting and one freely chosen
common c. No eleventh-root surjectivity is used. This realizes the
second tuple. Its factors are nontrivial since −1 is a nonsquare
unit in each of the relevant residue fields. The exact list consists
of the identity and one nonidentity element of order two; this proves
its asserted subgroup status. L073's unrestricted sizes give 16 for
the product comparison.

### Verification, relevance and limits

Run `python3 scripts/primitive-eleven-vectors/check_two_descent.py`.
The full certificate is
`scripts/primitive-eleven-vectors/two-descent-certificate.json`.
All 26 checks pass, and all actual/required check values and bounds
were inspected in full using the scoped JSON inspector. The script
checks the root lifts, both full residue-class tables, exact coefficient
scalings, and both realization equations and unit derivatives. The
uniform inequality is 2<5/2, or 20<25 in normalized L valuation;
this proof, not the finite certificate alone, covers all unit parts.

The achieved local size is two versus unrestricted sixteen. The
plausible downstream test, after critical review and its own coverage,
is whether localization of L084's current primitive containing space
is already confined to this diagonal subgroup. No such comparison or
independence computation is made here. The unit bound fourteen and
supported bound 13+dim ker(n_S) remain unchanged, and the latter
is not a full Mordell–Weil rank bound. Global class contributions,
other modular twists and rational/integer power lifting remain open.
L073's unrestricted odd class and the five-isogeny survivor are not
contradicted. No progress beyond the assessed general source methods
or complete Beal candidate is claimed.

### Independent critical audit — 2026-10-17

The prior SPECIALIZE assessment
`drafts/literature/2026-10-17-primitive-eleven-two-descent-audit.md`
authorizes this proof audit. No mathematical correction was needed.
The general Kummer, local-image-size and complete-DVR theorems remain
imported with the precise citations above. This is REPRODUCTION and
verification of the local specialization, not a new general theorem.

The audit checked the complete L042 proof, L041's actual base algebra
and common-witness construction, L044's audited primitive-domain
exhaustion, and L069/L073's fixed generator and entire cubic factors.
It reuses L033/L034's audited source transcription of the modular map.
The independent script
`python3 scripts/primitive-eleven-vectors/audit_two_descent.py`
reads only its literal coefficient assignments; it neither imports nor
executes the construction scripts. Horner composition and exact integer
arithmetic recheck the reconstruction identity, coordinate change,
coefficient bounds, root lifts, square residues and both realizations.
All 47 checks pass. The full evidence is
`scripts/primitive-eleven-vectors/two-descent-audit-certificate.json`.
Every actual/required check, both complete realization records, all
intermediate coefficient valuations, and the full scaled and derivative
residue polynomials were inspected. The common source transcription is
not claimed to be independently retranscribed from FNS.

Here are the load-bearing uniform checks beyond finite replay. For
1<=i<=10 the coefficient valuations are at least 23−2i in each
component of F(16+W,s). For every unit s with s−1 a unit, c0 has
valuation 22 and c11 is a unit. The unique-minimum argument therefore
forces v(W)=2 for every cluster root, including roots in extensions.
The scaled reduction is s((1−s)Z^11+1), so the residue of Z is fixed.
Reconstruction has b/11^20 congruent to (Z+1)^10, a unit at both
residues 4 and 5. The smooth root has b a unit, and F(16,s) is nonzero.
Thus every root supplies one affine point with the same s; the original
degree-twelve unramified fiber supplies completeness. No selected-factor
or finite-precision substitute is used for the entire fiber.

The simple alpha root lifts uniquely to 118 modulo 121 and 844 modulo
1331, with derivative residue one. The exact center consequently differs
from 64+121·7 by an element of valuation at least three. Thus for any
feasible Z the normalized center difference has residue 9 or 2, and
valuation exactly two before division by 121. The quadratic discriminant
is −11(16·11^2/g'(alpha))^2, so both half-separations have valuation
5/2. Subtracting them leaves the normalized unit residues unchanged.
In M the strict comparison is 4<5, and in L it is 20<25. Division by
121 is division by an actual square in both fields. Unit square classes
are determined by F11 residues by unit-derivative Hensel lifting;
the error terms remain in the maximal ideal under every embedding.
The smooth-point residues agree with the rational cluster classes.
Any base-field identification permutes the two rational factors and
possibly beta,gamma, fixes alpha and F11, and preserves these calculations.
Hence no further tuple can arise from a different identification.

For the two exact rational cluster points, the curve equations are
V^2+V=8520 and V^2+V=16330, with residues 2 and 8 and unit derivatives
5 and 6. Their scalar reconstructions have scaled coefficient residues
(1,3,4) and (1,9,5), giving s residues 4 and 10. These are integral
scalars with both s and s−1728 units. After removing the smooth point,
the monic degree-eleven cluster polynomial has integral roots and
therefore integral coefficients. Division by its exact rational root
Z=4 or Z=5 gives a monic degree-ten polynomial reducing to W^10.
The exact relation R_s=U_s M_s at that root yields
G(0)/11=(R_s'/11)/U_s: the two numerator/denominator residues are
6/10 and 1/9, both equal to 5. This proves Eisenstein over Q11.
For a root w, the unit (−55)/w^10 reduces to one, so the derivative-ten
Hensel correction gives an element with tenth power −55. Its Eisenstein
degree is ten, forcing equality of the two entire degree-ten fields.
Together with the two rational points this exhausts all twelve geometric
points with multiplicity one. This argument proves both exact realizations;
it does not assert compatibility for every scalar of either residue.

Finally, at each of these very scalars put t=s/1728 and q=1−t. Choose
one rational eleven-adic unit c with residue q^−1. Then q c^11 has
residue one and has a fourth root b by the unit derivative 4. The cube
map permutes F11^*, so t c^11 has a unit cube root a, with derivative
3a^2 a unit. This gives the same c in both identities and all three
coordinates units. It neither takes an eleventh root nor changes s.
These witnesses and the whole fibers prove attainment, whereas the
uniform argument proves containment. Nontriviality follows from the
nonsquare residue of −1. Only after equality is proved is subgroup
closure inferred. L073's full-image size theorem gives 2·2·4=16 without
its unrelated additional containment conditions.

The audit validates precisely the two-class primitive filter. It does
not test independence from L084, improve 13+dim ker(n_S) or the unit
bound fourteen, remove the five-isogeny survivor, or exclude integers.
L073's unrestricted odd class remains valid. The existing DAG inputs
are exactly those used; no new dependency or global premise is added.

## Mathlib

Full matching restricted-image theorem: **not checked**. Supporting
Hensel, maximal local rings, square classes, cubic Kummer evaluation
and local-image-size coverage: **not checked**. Unknown coverage is
not evidence of absence.
