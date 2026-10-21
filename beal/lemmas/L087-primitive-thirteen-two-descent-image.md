# L087 — Exact primitive whole-fiber two-descent image at thirteen

## Hypotheses

Use L033/L034's entire modular map j on

    E0: y²+y=x³−x²−10x−20.

By L064 its entire base algebra at thirteen is the single unramified
degree-twelve field U=K tensor_Q Q13, with residue field k=F_(13^12).
For a finite scalar s in Q13 minus {0,1728}, let B_s be the algebra
of the entire projective fiber j^(-1)(s). Retain every Q13-algebra
isomorphism B_s -> U and its tautological point P in E0(U).
For the primitive restricted image additionally require one common
nonzero triple a,b,c in Z13 with

    a³+b⁴=c¹¹, s=1728a³/c¹¹, min(v13(a),v13(b),v13(c))=0.

Use L069's X=4x, Y=8y+4 and the distinguished generator theta of

    g(X)=X³−4X²−160X−1264.

The full two-descent map is denoted kappa, to distinguish it from
L033's five-isogeny connecting map. Its ordinary value is [4x−theta]
in (U[X]/g)^*/(U[X]/g)^{*2}, without a scalar quotient.
No global class, global independence, rank, class-kernel value, integer
solution or further local condition is assumed.

## Conclusion

The full cubic over U splits as U³. Order its factors by the unique
root alpha in Q13 with residue 8, followed by the roots beta,gamma
whose residues are −2+sqrt(2), −2−sqrt(2). These last two roots
lie in the unramified quadratic subfield; their order is immaterial
to the conclusion. For the unique nonsquare unit class nu of U put

    epsilon13=[(1,nu,nu)].

The exact primitive whole-fiber image is

    J13={1,epsilon13}.

It is also the image from all compatible finite nonbranch scalars,
without requiring primitive witnesses. Every isomorphism is retained.
Scalars 1 and 7 respectively realize the two classes by entire fibers
and common primitive triples. The set is a subgroup of order two,
whereas the unrestricted image kappa(E0(U)) has order four. Thus this
is a further necessary local primitive-point filter. It does not
establish independence on L084's T, change its 13+dim ker(n_S) bound,
compute the class kernel, bound full rank or exclude an integer solution.
Independent critical application audit completed on 2026-10-17 confirms
this local statement without a mathematical correction.

## Proof

### Assessed inputs and why an explicit specialization is necessary

This is REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-primitive-thirteen-two-descent-image.md`.
The inspected general theorems do not compute this correlated image.
Only their explicit finite-field, whole-fiber and common-witness
specialization is supplied here; no general descent theorem is reproved.

For the full cubic Kummer map import Bruin–Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. **78** (2009), 2347–2370,
[14 March 2008 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf),
Remark 2.1, Section 4 Lemmas 4.3–4.4 and their proof cases, and
Section 9. The odd-degree map has no scalar quotient. The ordinary
formula, exceptional root evaluation and identity at infinity define
one map on all points. Below the restricted fibers avoid the exceptional
evaluations by proved unit differences, rather than an omitted chart.

For unrestricted comparison import Barrera Salazar–Pacetti–Tornaría,
*On 2-Selmer groups and quadratic twists of elliptic curves*,
[arXiv:2001.02263v3, 17 September 2020](https://arxiv.org/pdf/2001.02263v3),
Lemma 1.3, Definition 1.6, Theorem 1.8 and Corollary 1.9, pp.3–6.
The monic integral cubic has unit discriminant −256·11^5 at thirteen;
its polynomial order is therefore maximal etale. E0 has good reduction
by its unit discriminant −11^5. The odd-characteristic containment and
equality hypotheses hold. Its full Kummer image is the norm-square
unit space. This supplies the unrestricted bound and comparison,
not the restricted equality claimed here.

Use L064's precise Milne unramified-field and coprime factor-lifting
inputs (*Algebraic Number Theory*, v3.08, Theorem 7.33, Corollary 7.42,
Proposition 7.50 and Example 7.54), and Clark's *Algebraic Number
Theory II*, Theorem 1.79, p.58, for strict Hensel lifting. A unit in
these odd-residue-characteristic fields is a square exactly when its
residue is a square: lifting a nonzero residue root has unit derivative.
For entire etale fibers and morphisms use
[Stacks Lemma 10.153.7, tag 04GK](https://stacks.math.columbia.edu/tag/04GK),
with the complete residue fiber, not a selected factor. L066 supplies
the integral map and the origin and x=16 charts. The modular formula
and degree twelve are those of FNS, *The generalized Fermat equation
with exponents 2,3,n*, Compositio Math. **156** (2020), 77–113,
[10 June 2019 manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, pp.25–27, as certified in L033/L034. GRH-dependent global
Selmer computations are not used.

### Full cubic and class labels

Over F13 the cubic is

    gbar=(X−8)(X²+4X+2).

The quadratic roots are −2±sqrt(2), and 2^6=−1 in F13. The factors
are distinct, so Hensel lifts all three roots in U, retaining the fixed
generator theta under its three evaluations. The first root is rational;
the remaining two are in the unramified quadratic subfield of U.
In U³ the unit norm-square classes are the triples whose three residue
quadratic characters have product +1. Each component has exactly two
unit square classes, so there are four such triples. The cited good
reduction equality proves that all four occur in the unrestricted image.
In particular epsilon13 is nontrivial and the restricted two-element
set, once proved below, is proper. The component permutation induced
by any Q13-automorphism of U fixes alpha and at most interchanges
beta,gamma. Both reported triples are invariant under this permutation.

### All nonintegral scalars are incompatible

L066 proves that u=1/j is regular at O on the entire good model and,
in the integral parameter t=−x/y, has expansion

    u=−t+O(t²).

Its linear coefficient is a unit. For every u0 in 13Z13, the integral
local equations at O with u=u0 have a unique solution reducing to O,
by unit-derivative Hensel lifting (equivalently the etale formal
parameter chart). For u0=1/s nonzero this gives a Q13-point of the
finite fiber B_s whenever v13(s)<0. L034 gives that fiber dimension
twelve. A Q13-point gives a unital Q13-algebra map B_s -> Q13.
It cannot exist if B_s is the field U, of degree twelve. Therefore
no negative-valuation scalar is compatible. This argument is uniform
in its valuation and unit part and does not require a primitive-domain
reduction. The point O itself has s=infinity and is outside the stated
finite scalar domain.

### Complete regular residue fibers

Write, as in L034,

    F(x,s)=h(x)^3+J(x)s−d(x)s², J=2a_map−b_map,
    d=(x−16)^11,
    hbar=[9,10,8,12,1].

Coefficient lists here are ascending over F13; a_map,b_map denote
the map polynomials, not the primitive witnesses. Every finite integral
point above an integral s has integral x,y: properness on the good curve
and L066's map exclude reductions O and 3T, the two reduced poles.
The rational-function identity F(x,j)=0 remains valid at the removable
2T chart. For each residue r=1,...,11, exact factorization gives:

| r | Complete factor degrees of Fbar(x,r) |
|---|---|
| 1 | 12 |
| 2 | 1,1,10 |
| 3 | 12 |
| 4 | 4,4,4 |
| 5 | 1,1,2,2,2,2,2 |
| 6 | 4,4,4 |
| 7 | 12 |
| 8 | 1,1,10 |
| 9 | 1,1,10 |
| 10 | 12 |
| 11 | 4,4,4 |

Every polynomial is monic squarefree of degree twelve and coprime to
b_map. Reconstruction y=(r d−a_map)/b_map satisfies the curve equation
on every factor. At every factor the regular expression

    j=−h³/(a_map−b_map−b_map y)

has unit denominator and value r. This expression is L066's conjugate
chart and includes x=16 at r=9. There its point is (xbar,ybar)=(3,4),
the reduction of 2T, and j=−121=9. Consequently these twelve distinct
points exhaust the entire reduced fiber of degree twelve, including
the removable chart. Simplicity of the x-roots gives etaleness: where
d is a unit, reconstruction identifies the local fiber with F=0;
at 2T the conjugate chart gives the same identification with a unit
factor and x is a parameter since 2y+1 is a unit.

For every s reducing to r, Hensel lifts these etale points with their
residue fields and all conjugates. A residue point of degree d lifts
over the unramified degree-d extension, and its degree is at least d
by reduction, hence exactly d. The twelve lifted geometric points
exhaust the characteristic-zero degree-twelve fiber. Alternatively
this is precisely the whole etale fiber lifting of tag 04GK.
Thus the displayed degrees are the full local field degrees throughout
each such scalar disk. Only r=1,3,7,10 can give the single field U,
and every scalar in each of these four disks does give U.

Put H_r=Fbar(x,r) for these four irreducible degree-twelve polynomials.
In F13[x]/H_r choose any square root R_r of 2. The full three-component
quadratic-character calculation is

| r | (chi(4x−8), chi(4x+2−R_r), chi(4x+2+R_r)) |
|---|---|
| 1 | (+1,+1,+1) |
| 3 | (+1,+1,+1) |
| 7 | (+1,−1,−1) |
| 10 | (+1,−1,−1) |

All values are nonzero units, so these are also the exact local square
classes on every lifted point in the disk, not a precision sample.
Changing R_r exchanges two equal entries. Every identification B_s -> U
acts on the residue generator by one of the twelve Frobenius powers.
Frobenius preserves squares and fixes 8, while interchanging or fixing
the other two theta residues. Hence the table covers every such
identification and every unit part of s.

### Both branch neighborhoods, without assuming etale lifting there

The remaining integral residues are 0 and 12=1728 modulo thirteen.
The exact complete residue identities are

    Fbar(x,0)=hbar³,
    Fbar(x,12)=G², G=[10,0,1,12,5,9,1].

hbar and G are irreducible of degrees four and six. Both are coprime
to b_map,d and g(4x). Thus the reduction of any compatible point in
these neighborhoods has xbar a root of hbar or G, respectively,
with ybar uniquely reconstructed, and all three values 4x−theta
are units. Repeated reductions are used only for this necessary
point-reduction assertion, not to assert the fiber is etale or split.

For a root of hbar in F_(13^4), one exact square root of 2 is
R=[10,10,11,2]. The three nonzero values 4x−8,4x+2−R,4x+2+R
have quadratic characters (+1,+1,+1) in that field. These identities
hold at every conjugate root; changing R exchanges the last two
entries. Their images in k therefore remain squares, and lifting gives
the identity class throughout the s=0 residue neighborhood, whenever
a whole-fiber identification exists.

For a root of G the residue lies in F_(13^6). This field contains
F_(13²), hence all three theta residues. The three values are nonzero
elements of F_(13^6). Every such element becomes square in k: the
quotient (13^12−1)/(13^6−1)=13^6+1=4826810 is even, so its
(13^12−1)/2 power is one. Therefore all three unit classes lift to
squares in U, giving identity throughout the s=1728 residue
neighborhood. This covers all distances and unit parts in both branch
disks, including primitive valuations; no exact scalar-domain reduction
or assertion of branch-fiber compatibility is needed for this upper
bound on classes.

The unit differences in both branch cases and all four compatible
regular disks exclude actual two-torsion points from these fibers.
The only remaining affine exceptional map coordinate x=16 reduces
to r=9 or the pole and has already been retained or excluded by full
fiber compatibility. Thus no exceptional Kummer evaluation is lost.
All finite scalars are now covered, and the upper image is {1,epsilon13}.

### Exact entire-fiber common primitive realizations

For s=1 and s=7 respectively set b=2 and prescribe

    a³=16s/(1728−s), c¹¹=27648/(1728−s).

At s=1 their cube and eleventh-root residues may be taken as a=7,c=5;
at s=7 take a=4,c=7. The denominators and both prescribed powers are
units. In each case the corresponding polynomial residual is zero
modulo thirteen and the derivatives 3a² and 11c^10 are units. Strict
Hensel therefore gives exact unit roots in Z13 with those residues.
Together with the same b=2 they satisfy, over Q13 exactly,

    a³+16=c¹¹, 1728a³=s c¹¹.

All three coordinates are units, so they are nonzero and primitive.
The same c supplies both identities. The regular-fiber result above
identifies B_1 and B_7 with the entire U, with all twelve points and
all twelve isomorphisms, not selected factors. Their classes are 1
and epsilon13 by the table. Thus both elements of the upper bound
occur under the common primitive restriction, proving exact equality.
Subgroup status follows from this list and epsilon13²=1.

### Full finite arithmetic evidence and limitations

Run `python3 scripts/primitive-thirteen-two-descent/check_image.py`.
The full certificate is
`scripts/primitive-thirteen-two-descent/image-certificate.json`.
Its 35 named checks pass, with no failures. It recomputes all eleven
regular fibers, complete factorizations, every factor's Frobenius
irreducibility sequence, b and derivative gcds, point reconstructions,
and the regular conjugate chart, including r=9. The factor utility
checks the full product identity. For a degree-n factor it checks
x^(13^n)=x and excludes every proper factor degree by gcds at n/ell
for every prime ell dividing n. Squarefree closure and these gcds
prove irreducibility. These are exact finite-field tests, not numerical
factor guesses. The complete relevant residue records were inspected.

For all four compatible regular fibers and hbar the certificate retains
R²=2 and the exact three values and their (13^n−1)/2 powers. It also
retains the two complete branch identities, irreducibility, all unit
gcds and the exact common rational powers and Hensel residue checks.
The script reuses only the prior checker's pure polynomial utilities;
it does not execute that membership calculation. Its coefficient input
is L034's audited full map certificate. The root search is bounded;
failure would raise an error, and the actual found roots have their
exact square identities recorded. These are construction checks;
the separate independent audit follows below.

The actual restricted/unrestricted sizes are 2/4. A proper local image
does not prove an independent restriction on global supported classes.
It gives neither an extra removed unit direction nor a new dimension
bound. L064's different five-isogeny survivor, ATTEMPTS/029 and the
fixed-probe stop in ATTEMPTS/038 are unchanged. Independence on L084's T,
the class kernel and integer lifting remain unresolved. The independent
audit below confirms only the stated local result.

### Independent critical audit, completed 2026-10-17

This is a REPRODUCTION proof_audit under the pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-17-primitive-thirteen-image-audit.md`.
The audit finds no mathematical correction. Run
`python3 scripts/primitive-thirteen-two-descent/audit_image.py`.
The full evidence is
`scripts/primitive-thirteen-two-descent/audit-certificate.json`:
306 checks pass and failures are empty. The replay imports or executes
no construction code. It reads literal L034 source coefficients, checks
them against the coefficient certificate, and uses separate polynomial
arithmetic and extended-Euclidean inversion. No success flag from the
construction is used to establish a mathematical assertion.

For every one of the eleven regular residues, the replay checks the full
degree-twelve polynomial, every factor product, every Frobenius remainder
and each irreducibility gcd. Closure at degree n proves divisibility by
the squarefree polynomial X^(13^n)−X; the gcds at n/q for all prime q|n
exclude every proper factor degree. Thus the complete factor lists and
their degrees are proved. It also independently checks squarefreeness,
b-unit gcds, every reconstructed point, every conjugate denominator and
every modular value. These are complete records, rather than factor
degrees or selected evaluations alone. At the removable point (3,4)
in residue nine, direct implicit differentiation gives

    dy/dx=7, N'=a−b−by=10, dN'/dx=1, dj/dx=4 in F13.

Here 2y+1=9 and b is nonzero. Hence x is a curve parameter and j−9
has a simple zero, independently checking the exceptional chart's
etaleness. Elsewhere d and b are units and the elimination and
reconstruction identify the fiber locally with its simple F-root.
The twelve distinct reconstructed residue points exhaust the reduced
degree-twelve fiber from L066. Each lifts uniquely over its unramified
residue extension for every scalar in the corresponding disk. There
are already twelve geometric lifts, so the generic degree-twelve fiber
has no omitted point or multiplicity. This verifies the full-fiber
use of the cited henselian finite-etale equivalence, rather than merely
an isomorphism of a selected factor. Exactly residues 1,3,7,10 give U.

For all four compatible regular fibers the replay checks the complete
three values and quadratic characters for both roots R and −R of 2.
The tables are respectively (+++),(+++),(+−−),(+−−). For every residue
embedding, x changes by Frobenius; Frobenius preserves square classes,
fixes 8 and either fixes or exchanges the other two theta residues.
The equality of the last two characters therefore retains all twelve
identifications with the same ordered split cubic. Nonzero residue
values are units, so odd-characteristic square-root Hensel lifting
proves constancy over each entire scalar disk, without a precision
stability assumption.

Both complete repeated branch identities, their degree-four and
degree-six irreducibility proofs, point reconstructions, and all
b,d,g(4x) gcds are replayed. Here g is L069's cubic in X, not the
Weierstrass right-hand side in x. The gcd with g(4x) proves that each
theta difference is nonzero at every possible reduction. At the first
branch, both choices of the degree-four square root of 2 give (+++);
these residue squares remain squares on embedding into F_(13^12).
At the second, the theta roots and x lie in F_(13^6), whose nonzero
elements become squares in F_(13^12) because the extension degree is
two. Lifting unit squares applies independently of any branch
ramification or existence of a whole-fiber identification there.
Consequently these arguments cover all compatible branch-disk points;
no branch sample, etale branch lifting, or exact primitive branch-domain
assertion is substituted for the uniform upper bound.

For completeness, the negative-scalar exclusion uses the actual
integral origin chart. L066 has wU=t³ with U(0,0)=1 and w-derivative
one. The integral implicit function theorem gives w(t) in Z13[[t]],
converging for t in 13Z13. Its Q and H satisfy Q(0,1)=−1, H(0,1)=1,
so u(t)=1/j=tH/Q has linear coefficient −1. Its integral compositional
inverse converges on 13Z13; equivalently apply unit-derivative Hensel
to the two chart equations. Every nonzero u0=1/s in 13Z13 therefore
gives a Q13-point with j=s. Such a point induces B_s -> Q13, which
cannot be a unital homomorphism from the degree-twelve field U: it
would be an injective Q13-linear map to a one-dimensional space.
This excludes every negative valuation and unit part. Properness and
the integral map then ensure every remaining point reduces to the
affine nonpole locus. All scalar cases are covered.

The entire unramified base-field assertion is independently rechecked
on L033's defining polynomial by all degree-twelve Frobenius and gcd
tests. The fixed cubic factorization and exact discriminants are also
recomputed. Its distinct residue roots lift uniquely into U, with alpha
rational and beta,gamma in the quadratic unramified subfield. The unit
discriminant makes the polynomial algebra the maximal etale integer
algebra; E0 and the changed cubic model both have good reduction at
thirteen. Thus the cited BPT odd-characteristic local theorem applies
to the split cubic and gives exactly the four norm-square unit classes,
with no global Section 2 hypothesis. The restricted branch and regular
unit differences exclude all actual root points, while O and 3T are
poles. Thus no exceptional Kummer evaluation was silently discarded.

Finally the replay checks the full rational powers and every Hensel
condition for s=1 and s=7. Their values are respectively
(a³,c¹¹)=(16/1727,27648/1727) and (112/1721,27648/1721).
Denominators and powers are units; roots with residues (7,5) and (4,7)
have unit derivatives. With b=2, the exact equalities a³+16=c¹¹ and
1728a³=s c¹¹ use one common c in each case. These are nonzero primitive
triples on entire fibers B_1 and B_7, so both upper-bound classes
actually occur. Their nontrivial second and third characters prove
distinctness; their squares are identity, proving the stated subgroup
and the actual/required sizes 2/4.

The audit verifies a necessary local input by known methods. It neither
certifies originality nor an independent condition on T. The bounds
13+dim ker(n_S) and fourteen, the localized class-kernel question and
integer lifting are unchanged. ATTEMPTS/029/038 and L064's different
five-isogeny survivor are unaffected. No DAG edge or mathematical
assembly changes; the full audit is kept here rather than duplicating
it in PROOF.md.

## Mathlib

Full matching explicit primitive thirteen-adic whole-fiber image theorem:
not checked. Supporting finite-field, Hensel, unramified extension,
good reduction, cubic Kummer and etale-fiber declarations: not checked.
Unknown coverage is not evidence of absence. This is a specialization
of the cited methods, without a novelty or Beal-resolution claim.
