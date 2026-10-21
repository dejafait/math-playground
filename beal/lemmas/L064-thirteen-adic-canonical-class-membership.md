# L064 — The fixed canonical class survives the thirteen-adic filter

## Hypotheses

Use L033's degree-twelve field K, curve
E0: y²+y=x³−x²−10x−20, dual connecting map delta and its normalized
function f=(x−4)y−4x²+30x−55. Use L034's entire degree-twelve modular
map j and its notation j=(a(x)+b(x)y)/d(x), d=(x−16)^11,
J=2a−b, and F(x,s)=h(x)^3+J(x)s−d(x)s².
Here a,b are modular-map coefficient polynomials, not power witnesses.

Fix exactly L062's rational identification sigma of the entire canonical
fiber at s0=9261/8 with K, and alpha_sigma=delta(P_sigma).
Set A13=K tensor_Q Q13. For a finite scalar s, B_s is the coordinate
algebra of the entire projective fiber j^(-1)(s) over Q13.
The restricted image comprises delta(P) from every Q13-algebra
isomorphism B_s -> A13 and common nonzero a,b,c in Z13 with

    a³+b⁴=c¹¹, s=1728 a³/c¹¹, min(v13(a),v13(b),v13(c))=0.

No global class basis, integer solution, GRH, Selmer/point equality or
independent choice of a localized global conjugate is assumed.

## Conclusion

A13 is one unramified field of degree twelve over Q13. The localization
of L062's fixed class is the identity in A13^*/A13^{*5}.
The entire fiber B_3 is isomorphic to A13, and its connecting class is
also the identity under every whole-fiber isomorphism. There are exact
common primitive witnesses

    b=2, a³=16/575, c¹¹=9216/575,
    a in 1+13 Z13, c in 10+13 Z13.

Consequently loc13(alpha_sigma) belongs to the primitive whole-fiber
image. The canonical scalar s0 itself has no primitive power witness
at thirteen, but this does not remove its class: scalar 3 realizes it.
This retires the proposed removal of that survivor at thirteen, without
computing the full image, all-place intersection or an integer lift.
Independent critical application audit completed on 2026-10-13 confirms
this conclusion; the audit below corrects only a source-page ambiguity.

## Proof

### Standard inputs and why this specialization is needed

Use the assessed standard local-field results of J. S. Milne,
*Algebraic Number Theory*,
[v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 7.33/Remark 7.36, printed pp.121–123 (coprime factor lifting),
Corollary 7.42/Remark 7.43, p.124 (degree ef), and Proposition 7.50
with its proof, pp.127–128 (classification of unramified extensions
by residue extensions), and Example 7.54, p.129 (uniqueness over a
characteristic-zero local field). The base and residue fields here are
perfect, as required by Proposition 7.50. A monic integral polynomial with irreducible
degree-d reduction defines an unramified degree-d extension: reduction
gives residue degree at least d, while ef=d forces e=1 and f=d.
Integrality of roots rules out a monic factorization over Q13 whose
reduction would contradict irreducibility. Thus these results identify
the entire fields, rather than matching degrees for ramified fields.

Use Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields
and Adeles*, [161-page author notes](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
revision date unidentified, Theorem 1.79, printed p.58. In a complete
valued field, an integral polynomial and approximation r with
v(F(r))>2v(F'(r)) give an exact integral root close to r. We use it
over Q13 and its unramified degree-twelve extension, always with unit
derivative. The residue fifth-root identities below provide the required
approximate roots; a unit derivative alone would not suffice.

L033 supplies ordinary connecting evaluation and exceptional charts from
Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
**356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, printed pp.8–10, and Section 9, pp.21–23.
Their restriction diagram identifies evaluation of the same rational
function after base change with localization of the fixed global class.
L062 already fixes the point and sigma, so no new conjugate is chosen.
All evaluations used below are units at ordinary points.

L034's modular-map data come from Freitas–Naskręcki–Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio
Math. **156** (2020), 77–113,
[June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2: entire-fiber identification on printed p.25, modular-map
coefficients on p.26, formula (7.4) and Table 5 on p.27 (PDF indices
24,25,26 respectively).
Its GRH-dependent classification is not used. The existing general
lifting and descent theorems do not decide this restricted membership;
the particular residue identities and common witnesses are the necessary
specialization. No general theorem is reproved or novelty claimed.

### Complete residue certificates

All coefficient lists here are ascending and belong to F13. Let m be
L033's polynomial for K. Exact reduction gives

    mbar=[10,6,4,12,11,0,0,4,7,6,7,0,1].

For the canonical scalar, s0 reduces to 1728=12 modulo thirteen. Direct
polynomial multiplication with L034's coefficients gives

    Fbar(x,12)=G(x)²,
    G=[10,0,1,12,5,9,1].

For scalar 3 the complete candidate polynomial has reduction

    M=Fbar(x,3)=[7,3,1,0,4,2,5,7,7,12,10,0,1].

mbar, G and M are irreducible, of degrees 12,6,12 respectively.
The certificate records R_i=x^(13^i) modulo each polynomial; its
complete relevant sequences have been inspected. In each case R_n=x.
For n=12 the tests gcd(H,R_6−x)=gcd(H,R_4−x)=1 pass; for n=6
the tests use R_3−x and R_2−x. These are conclusive: R_n=x says H
divides x^(13^n)−x, a squarefree polynomial whose irreducible factors
have degrees dividing n. Every proper divisor of n divides n/ell for
some prime ell dividing n, and the gcd tests exclude those factors.
This proves the asserted irreducibility without a guessed factorization.

The same exact arithmetic gives gcd(b,G)=gcd(d,G)=1 and
gcd(b,M)=gcd(d,M)=1. With x denoting the residue generator, reconstruct
y=(s d−a)/b in each field. The curve residual y²+y−(x³−x²−10x−20)
is zero in both cases. The resulting f-values and exact fifth roots are

    modulo G:
      y=[10,4,3,8,7,5],
      f=[11,11,9,2,7,7],
      w=[0,2,6,0,3,3],              w^5=f;
    modulo M:
      y=[1,10,12,4,5,7,5,2,5,5,4,5],
      f=[10,2,5,9,3,6,1,1,12,3,4,10],
      w=[5,3,10,11,11,6,9,12,7,9,0,8], w^5=f.

Both f-values and w-values are nonzero. These explicit polynomial
identities, not an inference from precision stability, certify residue
fifth roots. They are reproducible by multiplication and reduction.

Run `python3 scripts/thirteen-adic-membership/check_membership.py`.
The complete certificate is
`scripts/thirteen-adic-membership/membership-certificate.json`.
It contains all Frobenius remainders, gcd tests, reconstruction values,
fifth-root identities and exact power-witness data. All 16 checks pass,
with no failures; actual whole-field degrees 12 match required 12.
Its bounded initial search tests all eleven nonbranch integral residue
scalars with unit power witnesses; that search is not an exhaustion of
all thirteen-adic scalars and is not used for a negative image claim.
Only mbar, G, M and the displayed exact witness are load-bearing here.

### Localization of the same canonical class

Irreducibility of mbar and the cited unramified-field results identify
A13 with one unramified degree-twelve field U12. It is the entire
twelve-dimensional tensor algebra, with no remaining factors.

Base change the same P_sigma from L062 to A13. It has j=s0 and is
neither O nor T. Also x is not 16, since the two points there have
j=-121 and infinity, neither equal to s0. L034's elimination identity
therefore gives F(x,s0)=0. This is a monic integral polynomial because
s0 is integral at thirteen; hence x is integral in U12.
Its reduction satisfies G(xbar)²=0. The residue ring of U12 is a
field, so G(xbar)=0, and irreducibility of G makes xbar generate the
degree-six residue subfield. The gcd identities show b(x) and d(x)
are units. Thus y=(s0 d−a)/b is integral and its reduction is precisely
the displayed y modulo G. In particular f(P_sigma) is a unit whose
residue is the displayed nonzero f modulo G.

Evaluate the displayed polynomial w modulo G at xbar inside the residue
field of U12, and lift it arbitrarily to an integral element w0 of U12.
For H(W)=W^5−f(P_sigma), H(w0) reduces to zero and
H'(w0)=5w0^4 is a unit. Hensel–Newton gives an exact fifth root in
U12. Hence loc13(alpha_sigma)=[f(P_sigma)]=1.
This uses the fixed global point under base change, not a replacement
point or an independently selected local embedding. Any residue
embedding of G retains the polynomial fifth-root identity.

### The whole fiber at three and its connecting class

F(x,3)=h³+3J−9d is monic integral with irreducible reduction M.
Consequently C=Q13[x]/(F(x,3)) is the entire unramified degree-twelve
field, isomorphic to U12. The residue gcd tests make b(x),d(x) units
in its integer ring. Reconstruct y=(3d−a)/b. L034's exact identity

    (3d−a)²+b(3d−a)−b²(x³−x²−10x−20)=−d F(x,3)

proves the curve equation, and d invertible proves j=3. The polynomial
is separable: its irreducible finite-field reduction is separable and
has nonzero derivative gcd, so its discriminant is a unit. Thus its
twelve distinct roots give twelve distinct ordinary points in the
fiber. L034's map is finite locally free of degree twelve. These
points exhaust its entire fiber, so B_3=C, rather than a selected
factor. There is no point at x=16 or at a reconstruction zero, and
scalar 3 avoids all characteristic-zero branch and exceptional values.

The displayed f modulo M is nonzero and has the explicit root w.
Lift that residue polynomial to B_3 and apply the same Hensel argument
to W^5−f(P_3): the residual value is zero and the derivative is a unit.
It follows that the ordinary universal fiber point P_3 has delta(P_3)=1.
Every Q13-algebra isomorphism B_3 -> A13 preserves this fifth-power
identity. The transported point therefore has exactly the localization
of alpha_sigma, since both classes are the identity. No explicit
coordinate choice for the isomorphism or fifth-power collision
enumeration is needed for this positive witness.

### One common primitive power triple

Set b=2. The rational numbers 16/575 and 9216/575 are thirteen-adic
units since 575=3 modulo thirteen. For H_a(U)=U³−16/575 use r=1:

    H_a(1)=559/575, v13(H_a(1))=1,
    H_a'(1)=3, v13(H_a'(1))=0.

For H_c(V)=V¹¹−9216/575 use r=10:

    H_c(10)=57499999990784/575, v13(H_c(10))=2,
    H_c'(10)=11*10^10=7 modulo thirteen.

Both strict Hensel inequalities hold. They yield exact units
a in 1+13 Z13 and c in 10+13 Z13 with the prescribed powers.
Together with the same b=2 these satisfy

    a³+b⁴=16/575+16=9216/575=c¹¹,
    1728 a³/c¹¹=1728*16/9216=3.

Every coordinate is a unit, so primitivity and nonzero coordinates
hold. The same c enters both identities; no independently lifted
right-hand roots are substituted. This completes the restricted-image
membership witness on the entire algebra.

For comparison, at s0 the ratios are t=343/512 and q=169/512,
with valuations zero and two. If a primitive integral triple had those
ratios and c were a nonunit, then 3v(a)=11v(c) and
4v(b)=2+11v(c) would make both a,b nonunits, a contradiction.
Thus c would be a unit, forcing 4v(b)=2, impossible. The canonical
scalar's failure is real, but the scalar-3 witness proves why it is
insufficient for class exclusion. The thirteen-adic test cannot remove
this global survivor; other local conditions and integer lifting remain
unresolved. This is a local REPRODUCTION using assessed known methods,
not a complete Beal candidate or a discovery beyond the checked sources.

### Independent critical application audit, completed 2026-10-13

The independent replay `python3 scripts/thirteen-adic-membership/audit_membership.py`
passes all 52 checks. Its full evidence is saved in
`scripts/thirteen-adic-membership/audit-certificate.json`. No construction
code is imported or executed, and no scalar search is repeated. Coefficients
are independently transcribed from the primary FNS manuscript; sparse
integer polynomial multiplication checks J=2a−b and the entire elimination
identity, rather than only reductions of selected coefficients. Direct
binary powering from x independently recomputes every x^(13^i) remainder
for mbar, G and M. Extended Euclidean computations retain and verify
Bezout identities for every irreducibility gcd, derivative gcd and
reconstruction unit. Their complete sequences and all relevant original
certificate values agree. The explicit y polynomials are tested by both
b y=s d−a and the curve equation; direct fifth powers verify the displayed
w values without invoking the original fifth-root exponent calculation.
The full integer coefficient, irreducibility, point and scalar evidence
was inspected, not only previews or success flags.

The irreducibility proof above retains all prime divisors of 12 and 6,
namely 2 and 3. Frobenius closure also forces squarefreeness. The monic
integral m and F(x,3) therefore each define a field of degree twelve;
their residue degree is at least twelve, so the degree=ef theorem
forces residue degree twelve and ramification index one. Unramified
uniqueness over Q13 identifies the entire fields. G² is used only to
identify the canonical point's residue, never as a prime decomposition
of the power order or as evidence for two local factors.

The fixed-sigma argument uses exactly
`(sigma tensor 1)((f|_Z) tensor 1)=sigma(f|_Z) tensor 1` from audited
L062. Its ordinary evaluation is justified because the canonical scalar
differs from j(T), j(O), and both values at x=16. Monicity makes its
x-coordinate integral, and the certified b,d units give the asserted
y and nonzero f residues. In each of the two entire complete fields,
the fifth-root residual has valuation at least one and its derivative
has valuation zero. Clark's strict Hensel inequality thus gives an exact
fifth root. This argument is valid for every embedding of the residue
generator and every subsequent field isomorphism, while sigma itself
remains fixed before localization.

For clarity, whole-fiber exhaustion can also be checked on coordinate
algebras. Reconstruction defines Spec(C) -> j^(-1)(3). The pullback
B_3 -> C contains the coordinate x, which generates C, and is therefore
surjective. The coordinate x is regular on this finite fiber because
its only pole O maps to infinity. L034's finite locally free degree is
twelve, as is dim(C); hence this surjection is an isomorphism. This
confirms the direction of the map and retains every projective fiber
point. The certified fifth root is transported along C -> A13; it
matches the localized fixed class since both classes are the identity.

The common power witness is checked over Q exactly. Its two Hensel
residual valuations are 1 and 2, respectively, against the required
strict lower bound zero in both cases. All three coordinates are units,
and the same c satisfies the sum and scalar identities. At the canonical
scalar, v(t)=0 and v(q)=2 prove the separate impossibility exactly as
above; this does not contradict class membership at scalar 3.

The primary PDF resolves the qualified page locator in the prior
assessment: FNS's printed pages are 25 for the entire-fiber paragraph,
26 for a,b, and 27 for Table 5 and (7.4). The assessment's alternative
25/26 labels for the latter two pages were zero-based PDF indices.
The source coefficients and theorem scope require no mathematical
correction. The GRH-dependent Selmer dimensions are not inputs.

This confirms the existing local survivor-removal stop, without a new
general theorem, full local image, all-prime membership, class/unit
basis or integer lift. The original proof and certificate are preserved.

## Mathlib

Full explicit thirteen-adic same-class membership theorem: not checked.
Supporting finite-field arithmetic, unramified-extension classification,
Hensel lifting, fiber base change and connecting-map declarations: not
checked. Unknown coverage is not absence. The proof uses the precise
standard citations above and the canonical local inputs stated here.
