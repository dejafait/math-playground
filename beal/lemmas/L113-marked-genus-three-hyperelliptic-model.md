# L113 — Hyperelliptic model retaining the fixed-minus-three marking

## Hypotheses

Work over Q. Use audited L111's smooth proper geometrically integral
marked curve D, whose function field is Q(T,h,R), with

    h²=3(4−T²),
    R²=b(T)=825T⁴+2112T³+198T²−1716T−231.

Use L109's original scalar and L110–L111's exact functions:

    F=T⁵+T⁴−4T³−3T²+3T+1,
    K=T²−T−1, L=T²+T−1,
    W=hR/3, u=(F−11−KW)/(60F), M=2−10u,
    rho=ML/[30(T+2)K], v=rho*h,
    z=−M²(T−2)L²/[300(T+2)K²]=v².

Let phi(X)=(3X²+X+1)^5(1−5X)=sum_(i=0)^11 c_i X^i. The original
scalar is precisely

    s=H0(u,z)=sum_(i=0)^11 c_i sum_(2j<=i)
                  binom(i,2j) u^(i−2j)(−3z)^j.

No rational-point completeness, rational distinguished root, compatible
remaining factor, integer solution or descent arithmetic is assumed.

## Conclusion

An exact hyperelliptic Q-model of D is the smooth proper completion C of

    Y²=G(t)=11(275t⁸−2860t⁶+6930t⁴−3564t²+243).          (1)

The polynomial is squarefree of degree eight, and C has genus three.
Inverse function-field maps are

    d=t²+3,
    T=2(t²−3)/d, h=−12t/d, R=3Y/d²;
    t=h/(T−2), Y=(t²+3)²R/3.                            (2)

These extend to inverse Q-isomorphisms of smooth proper curves. The
original functions are exactly those in the hypotheses after (2),
including W=−12tY/d³, z=v² and s=H0(u,z). The elliptic projection is
the morphism (t,Y) -> (2(t²−3)/d,3Y/d²) to L111's E.

Every omitted rational fiber is accounted for: t=0 has no rational
point; C has exactly two rational points at infinity. The latter map
to (T,h,R)=(2,0,±165), with u=z=v=0 and s=1. Every other rational
point has finite nonzero t, and all denominators F,K,T+2 and rho
in the indicated transport/inverse formulas are nonzero there.
The conic-infinity fibers and F,K,L exceptions add no rational points.
This classifies coordinate exceptions, not the full s-boundary or C(Q).

This is an instance-specific reproduction of the assessed conic/model
methods. It provides an input to possible point-cover descent, without
point completeness, degree-nine root recovery, remaining-factor control,
either L095 integer exclusion or a minus-eleven conclusion. Its separate
critical audit passes as recorded below, without a model correction.

## Proof

### Imported methods and the instance calculation

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-21-marked-genus-three-hyperelliptic-model.md`.
Import [Stacks Proposition 53.10.4, tag 0C6L](https://stacks.math.columbia.edu/tag/0C6L):
a smooth proper geometrically integral genus-zero curve with an
invertible sheaf of degree one is P¹. Here the projective conic
h²+3T²=12J² is smooth (its three diagonal coefficients are nonzero),
geometrically integral, and has the rational point [2:0:1]. Its
point divisor supplies the degree-one sheaf. The explicit maps must
still be computed: the general theorem does not supply this instance's
polynomial, square multiplier or marked functions.

The line h=t(T−2) meets the affine conic again at
T=2(t²−3)/(t²+3), h=−12t/(t²+3). Substitution verifies the conic
identity and h/(T−2)=t. Globally, with t=a/c, these are

    [T:h:J]=[2(a²−3c²):−12ac:a²+3c²].                  (3)

There is no common zero of these three forms over Qbar: their vanishing
would imply a²=c²=0. Thus the slope chart has not discarded its tangent
point at t=infinity. The direct inverse identities below suffice for
the field claim, without reproving the general conic theorem.

Set Y=d²R/3, retaining the rational-square factor 9 exactly. Expansion
of the actual b gives the polynomial identity

    sum_(i=0)^4 b_i [2(t²−3)]^i (t²+3)^(4−i)=9G(t).    (4)

Consequently R²=b(T) is exactly (1), with no changed constant twist.
The Euclidean algorithm gives gcd(G,G')=1. A reproducible Bezout witness
A*G+B*G'=1 has ascending coefficient lists

    A=[1/2673,0,−8315/2985984,0,8465/4478976,0,−2225/8957952],
    B=[0,−8233/29196288,0,51875/71663616,0,
       −22715/71663616,0,2225/71663616].

Multiplying verifies the identity. Thus all eight roots are simple,
and G is nonsquare over Qbar(t). In particular (1) is geometrically
integral, rather than an extra component of a singular equation.

Both inverse compositions can be checked without point sampling. On C,
T−2=−12/d and h=−12t/d give t back, and Y=d²R/3 gives Y back.
Conversely, in Q(D),

    t²=−3(T+2)/(T−2), d=−12/(T−2),
    2(t²−3)=−12T/(T−2).

These identities recover T; then −12t/d=h and 3Y/d²=R. All divisions
are by nonzero functions, since T is transcendental and h is nonzero
as a function. This identifies the full Q-fields, including h and R,
not just the genus, invariants or an unmarked quotient.

### Smooth proper model, genus and transported maps

The full model of C is covered by (1) and the chart

    q=1/t, Z=Y/t⁴,
    Z²=11(275−2860q²+6930q⁴−3564q⁶+243q⁸).            (5)

The finite chart is geometrically smooth by squarefreeness. At q=0,
Z²=3025=55² and 2Z is nonzero, so (5) is smooth there as well.
The monic quadratic charts glue to a finite curve over P¹, hence a
proper curve; geometric integrality follows from the verified field.
These are therefore the smooth proper model, not a singular plane
closure. Its separable degree-two map to P¹ branches at the eight
simple finite roots and is unramified at both infinity points.
The characteristic-zero Riemann–Hurwitz formula in
[Stacks Section 53.12, tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B)
applies to these smooth proper geometrically integral curves and gives
2g−2=−4+8=4, so g=3.

Import [Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1).
The verified inverse Q-function-field maps extend uniquely to inverse
maps of the smooth proper curves C and L111's D. Its hypotheses hold
over the perfect field Q; smoothness/properness and geometric integrality
were verified above and in L111. Composing with L111's proper elliptic
projection gives the claimed morphism to E, also at omitted coordinates.

Substituting T,h,R in the hypotheses gives the precise original W,u,
rho,v,z, without replacing s by a function on E. Inverse composition
fixes T,h,R and therefore fixes every rational expression for these
functions; it fixes each term of the displayed finite H0 polynomial.
Thus it preserves the entire s, not a truncation or approximation.
The exact identity v²=z follows either from L111's z=3(4−T²)rho²
or from the complete arithmetic residual. Proper extension interprets
poles in the corresponding normalized local rings.

### Every omitted rational fiber

For the new forward formulas the only finite denominator is d=t²+3,
which has no rational zero. For completeness, its two geometric zeros
are retained in the conic-infinity chart: at d=0, G=1900800 is nonzero,
and

    H=h/T=−6t/(t²−3), S=R/T²=3Y/[4(t²−3)²]

are regular, with H²=−3 and S²=825. These are exactly L111's four
geometric infinity points, none rational. Conversely a rational D-point
at T=infinity would give the impossible rational equality H²=−3.
No rational point is hidden behind a pole of T.

The inverse slope formula excludes T=2. Its D-fiber consists of exactly
the two points (2,0,±165), by L111's smooth finite chart. Chart (5)
recovers them at q=0, Z=±55, through the regular formulas

    T=2(1−3q²)/(1+3q²),
    h=−12q/(1+3q²), R=3Z/(1+3q²)²,
    W=−12qZ/(1+3q²)³.                                 (6)

Here q is a genuine local parameter, since 2Z!=0. At t=0 the equation
is Y²=2673=81*33, so it has no rational point; it corresponds precisely
to T=−2,h=0,R²=297, also without rational points. Thus the affine
formula R=3W/h from the old presentation loses no further rational
point. All remaining rational points have finite nonzero t, finite T
different from ±2, and h nonzero.

For the original functions, F is monic with constant term one; any
rational zero must be ±1, whereas F(1)=F(−1)=−1. Both K and L have
discriminant five and no rational root. A rational finite t has T+2
nonzero unless t=0, already excluded. Hence F,K,L,T+2 are units at
every remaining rational point. To check also the inverse division
by rho, use L110's identities, with J=(T+2)(T²−1):

    F+1=KJ, N=11J+W, Nbar=11J−W,
    M=KN/(6F), N*Nbar=396(T+2)F.

The last identity and the nonzero factors just established force N
and M, hence rho, to be nonzero there. Thus v=rho*h is nonzero.
At T=2 the original expressions are regular and rho=1/12, so this
division does not remove either infinity point either. These checks
exhaust the extra denominators introduced by the marked transport.

If using L110's inverse T-expression in the original coordinates,
its denominator is d0²+3ze0², where d0=3u²+u+1−9z and e0=6u+1.
At a rational point z=v², its vanishing requires d0=ve0=0. If v=0,
d0=3u²+u+1 has no rational zero. Otherwise e0=0 gives u=−1/6
and d0=0 gives v²=11/108, also nonsquare in Q. Thus this denominator
has no rational zero wherever these finite rational functions are used.
F,K were checked separately above. This is not a classification of
the full original s-boundary.

Finally (6) and rho=1/12 give h/q -> −12, v/q -> −1,
W/q -> −12Z0=∓660 and z/q² -> 1. Hence v/W -> ±1/660,
exactly L111's normalized boundary lifts. In particular u=z=v=0
and s=phi(0)=1 at both points. The ramified elliptic fibers have
one source point each; they are not two new lifts for each sign.
They are boundary points, not disjoint roots in a regular fiber
or primitive integer solutions. No additional rational coordinate
exception remains, and no assertion about other rational points follows.

### Evidence, downstream use and limitations

Run `python3 scripts/pair-genus-two/marked_hyperelliptic.py`.
The full certificate is
`scripts/pair-genus-two/marked-hyperelliptic-certificate.json`.
All 31 exact checks pass with no failures: the 14 complete field
residuals vanish, the Bezout identity is one, and the rational-fiber
arithmetic agrees. The degree, genus and boundary-lift actual/required
values are respectively 8/8, 3/3 and 2/2; their justification is the
proof above. Complete residuals, Bezout coefficients, transported
functions, check flags and rational-exception fields were inspected.
The script uses exact rational polynomial arithmetic with no point scan.

The first run exposed an incorrect expected remainder 608256 for G
modulo t²+3. Direct evaluation at t²=−3 gives 1900800; correcting
that check leaves the polynomial and maps unchanged. The failed
certificate is preserved as
`scripts/pair-genus-two/marked-hyperelliptic-initial-check-failure.json`.
This was a check-constant error, not concealed evidence of a failed model.

A concrete prospective consumer is Bruin–Stoll, *Two-cover descent on
hyperelliptic curves*, Math. Comp. 78 (2009), 2347–2370,
DOI [10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
[arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2), Section 2 p.3,
Theorem 3.4 pp.5–6 and Sections 6 and 8. Equation (1) meets its
characteristic-zero, squarefree even-degree smooth-model input. That
is an applicability observation, not a descent execution: support,
unit/class computations, certified local images, surviving-cover point
control and lifting remain independent tasks. The two rational boundary
points must survive; an empty fake-Selmer-set exclusion is unavailable.
Positive elliptic rank does not determine marked points. ATTEMPTS/050–051
and unfinished L108 are preserved. No progress beyond the checked general
source methods, rational-point completeness or Beal resolution is claimed.

### Independent critical audit, 2026-10-21

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-21-marked-hyperelliptic-critical-audit.md`.
Use the audited original functions and smooth charts of L109–L111.
The audit confirms the conclusions without changing the polynomial,
constant twist, maps, genus or exceptional-point classification.
It reproduces the assessed instance methods; it does not establish
progress beyond the general sources cited above.

Independently substitute the actual quartic b into T=2(t²−3)/(t²+3).
Multiplication by (t²+3)^4 gives exactly 9G, with all nine ascending
coefficients (2673,0,−39204,0,76230,0,−31460,0,3025). Multiplication
of both complete displayed Bezout polynomials by G and G' gives one.
Thus the degree is eight and all geometric roots are simple. A square
in Qbar(t) has even valuation at every point; a simple zero of G
therefore proves that G is nonsquare and the quadratic function field
is geometrically integral. The projective conic is smooth because its
partial derivatives cannot vanish simultaneously at a projective point.
Its displayed rational point and the cited conic theorem apply. The
three homogeneous forms (3) have no common projective zero, so the
parametrization covers the tangent point too.

The independent field computations use the two bases (1,Y) over Q(t)
and (1,h,R,hR) over Q(T). In the second field h²=12−3T² and R²=b(T);
its degree four and geometric integrality are audited in L111. The
identity t²=−3(T+2)/(T−2) gives d=−12/(T−2), recovering T,h,R
separately. Conversely h/(T−2) and d²R/3 recover t,Y separately.
The audit checks these compositions in their respective fields,
including Y²=G(t) in the four-dimensional field. Nonzero rational
functions are being inverted, not values at excluded points. Thus this
is an identification of the full Q-fields, not just a relation between
invariants or a composition checked on one subfield.

All complete producer expressions for W,u,rho,z,v agree with independent
rational-function computations. Both field compositions fix all five
functions, with v²=z and W=hR/3; the old inverse T expression and the
inverse h=v/rho, R=3W/h also agree. Re-expanding phi from its factored
form gives all twelve c_i in L110. Its even binomial expansion has
exactly 39 nonzero terms c_i binom(i,2j)(−3)^j u^(i−2j)z^j. Each term
is fixed because u,z are fixed in both fields. This verifies the entire
finite H0 scalar without a truncated series or an assumption that it
descends to the elliptic quotient. The latter projection is exactly
(T,R) from (2), composed with L111's proper morphism.

For properness, the two coordinate rings of (1) and (5) are free of
rank two over Q[t] and Q[q]. On their overlap q=1/t and Z=q^4Y
identify them. These finite morphisms glue to a finite morphism to P¹,
hence a proper curve over Q. The injection of each free chart into
its generic quadratic field excludes vertical components. The finite
Jacobian criterion uses gcd(G,G')=1; on the infinity chart the two
points Z=±55 have nonzero derivative 2Z. Thus the entire curve is
smooth and geometrically integral. At a simple finite root of G,
Y is a uniformizer and t−t0 has order two. At infinity q is a
uniformizer at each sign of Z, so the degree-two map is unramified
there. There are exactly eight geometric simple branch points.
Characteristic-zero separability and smooth proper geometric
integrality justify the cited Riemann–Hurwitz formula, giving
2g−2=−4+8 and g=3. The hypotheses of Stacks Theorem 53.2.6
are now satisfied, so the inverse field maps extend uniquely over
all points. Proper extension does not assert that every transported
rational function is regular everywhere.

Here is the complete rational-coordinate exception check. Finite
rational t cannot have t²+3=0; the geometric fibers there have
G=1900800, H²=−3 and S²=825 in L111's infinity chart. Conversely,
a rational point at T=infinity would have rational H with H²=−3,
which is impossible. At t=0, Y²=81*33 is nonsquare; equivalently
T=−2 gives R²=9*33. The only inverse-slope exception T=2 consists
of the two points (2,0,±165), recovered at q=0,Z=±55. There is
one source point above each sign of R, of ramification index two
over E, rather than two distinct lifts of either sign.

For every remaining rational point, T is finite and different from
±2. Monicity and constant term one restrict rational roots of F
to ±1, where F=−1. The discriminants of K,L equal five. Thus F,K,L
and T+2 are nonzero. Independent polynomial multiplication verifies
F+1=KJ and 121J²−f=396(T+2)F. Consequently N,Nbar and
M=KN/(6F) are nonzero, so rho and v=rho*h are nonzero too.
At the two T=2 points, rho is regular with value 1/12.
For the old inverse denominator, rational z=v² makes
 d0²+3ze0²=d0²+3(ve0)².
Its vanishing forces d0=ve0=0. If v=0, the quadratic
3u²+u+1 has discriminant −11 and no rational root. Otherwise
u=−1/6 and v²=11/108=33/18², impossible over Q. All these
functions are finite at the rational points under consideration,
since their other denominators were already checked. This exhausts
the rational denominator exceptions, not all original s-boundary
fibers and not C(Q).

Finally, compute in the q chart separately at Z=−55 and Z=55.
The exact limits are h/q=−12, W/q=−12Z, v/q=−1 and z/q²=1.
Thus v/W=1/(12Z)=−1/660 and 1/660 respectively. Here q is a
uniformizer, and W/q is a nonzero unit, so these are normalized
boundary residues in genuine local parameters. They agree with
L110–L111's two unramified marked lifts. Both points have u=z=v=0
and s=c_0=1. No rational extra fiber is missing; these boundary
points are not disjoint pairs in a regular fiber or integer solutions.

Run `python3 scripts/pair-genus-two/audit_marked_hyperelliptic.py`.
The full independent evidence is
`scripts/pair-genus-two/marked-hyperelliptic-audit-certificate.json`.
All 75 exact checks pass with no failures. Actual/required degree,
genus and rational boundary-lift counts are 8/8, 3/3 and 2/2;
the geometric arguments above, not these printed counts, justify
properness, genus and completeness of the exceptional fibers.
The auditor imports no producer or producer arithmetic classes.
It reuses rational-function utilities from the independent L111 auditor,
uses xor-indexed basis multiplication and Gaussian matrix inversion,
and stores all coefficients and full residuals. The complete residuals,
transported functions, Bezout witness, scalar terms, both boundary rows,
producer checks and input hashes were inspected and compared.

The preserved producer failure changes only its expected conic-infinity
remainder text and failed-check metadata: the true remainder is 1900800,
not 608256; its polynomial, functions and Bezout evidence are unchanged.
The audit itself initially expected 40 nonzero H0 terms; the full
expansion has 1+2+3+3+4+4+5+5+6+6=39. The initial audit certificate
is retained as
`scripts/pair-genus-two/marked-hyperelliptic-audit-initial-count-failure.json`.
Correcting that count changes no term, identity or model. Neither
implementation failure is presented as a mathematical counterexample.

The verified model remains only a possible point-cover input. Certified
descent arithmetic, points on surviving covers, distinguished-root
recovery of degree nine, remaining factors, both L095 integer systems
and minus-eleven remain unresolved. The two known rational points
must survive any sound point-cover computation. ATTEMPTS/050–051 and
unfinished L108 remain intact. There is no complete Beal candidate.

## Mathlib

Full matching conic/model specialization, exact-instance maps and
hyperelliptic point-cover workflow were not checked in Mathlib.
Supporting coverage was not searched in this step. No absence or
formal verification is claimed.
