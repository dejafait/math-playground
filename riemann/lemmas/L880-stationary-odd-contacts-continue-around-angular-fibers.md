# Lemma 880: a stationary single odd contact continues around its whole angular fiber

## Hypotheses

Assume exactly L879's hypotheses, using L847's actual entire G and
positive constants R,C, full form and original angular orientation:

\[
 F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
 \qquad z_j(y)=R\exp(u_j(y)+iy_j),
\]
\[
 u:\mathbb T^2\longrightarrow\mathbb R^2\text{ smooth and periodic},
 \quad J=\det(I-iDu)\ne0\text{ everywhere},\quad Q=F(z_1,z_2)J.
                                                               \tag{1}
\]

Stationarity is for every smooth real radial variation compactly
supported in {Q!=0}, as in L879(3); it is not stationarity through
zeros. At a point p suppose z1(p)!=z2(p), exactly one G(z_j(p))
vanishes, and its zero label zeta has odd multiplicity m>=1.
Since the graph takes values in (C*)^2, zeta!=0.

No positivity, real analyticity of u, simple-zero premise, symmetry,
finite pulled-back contact census, contact transversality, graph
existence or RH is added. Other encountered zeros have arbitrary
finite multiplicities. All simultaneous and diagonal contacts remain.

## Conclusion

Writing a=arg(zeta) modulo 2pi, the same label persists on the entire
angular fiber:

\[
                   z_j(y)=\zeta\quad\text{whenever }y_j=a.
                                                               \tag{2}
\]

In particular, u_j=log(|zeta|/R) along this circle. This is a necessary
condition on an already given stationary graph, not construction or
exclusion of such a graph. It propagates the label, not the assertion
that every point remains a single off-diagonal contact: simultaneous
G contacts and G-diagonal coincidences on the circle are allowed.

This is the completed bounded attempt under
`drafts/literature/2026-11-06-stationary-odd-fiber-continuation.md`,
DECISION EXPLORE, saved before invocation. The independent conceptual
audit of 6 November 2026 below accepts the continuation argument under
these unchanged hypotheses. The checked sources supply elementary inputs,
not (2); their bounded comparison does not certify originality.
L879's mass-gap branch is now globally constrained, but is not
excluded or realized. Sharp period, compactness, higher signs and
actual-Xi all-degree mixed positivity remain open.

## Proof

### Reused inputs and exact local reduction

Use L879's proved global phase line Q=lambda*s, with |lambda|=1 and
s real smooth, its componentwise constancy of Q/|Q| off zeros, and
its same-label local fiber at the stipulated single odd contact.
The full expression (1) and its angular coordinates are those of
L847; no positive-density contact result is used.

Import the standard finite-order holomorphic zero factorization from
Jiří Lebl, *Guide to Cultivating Complex Analysis*, v1.10,
5 November 2026, [Theorem 2.4.7 and its proof, pp49–50](https://www.jirka.org/ca/ca.pdf#page=49).
It applies since G is entire and G(0)>0, so G is not identically
zero. Near any encountered zero eta of order n,
G(eta+w)=w^n g_eta(w) with g_eta holomorphic and g_eta(0)!=0;
shrink the disc to contain no other zero. This says nothing about
analyticity or isolated zeros of a smooth pullback.

Also use the elementary conjugation invariance of the multiset of
complex projective linear factors of a nonzero real homogeneous
binary polynomial, with multiplicities. This is the real-coefficient
factorization observation in Mateusz Michalek, *Algebraic Varieties*,
17 April 2018, [Example 7, printed p4](https://www.math.uni-konstanz.de/~michalek/april17.pdf#page=4),
as inspected in the prior assessment. Only this consequence of the
fundamental theorem of algebra and factor uniqueness is imported;
its nonnegative-form conclusions are not used. Below the polynomial
is verified to be nonzero and real before applying this fact.

It suffices first to consider j=1. Suppose an interval of the fiber
y1=a has z1=zeta and approaches a point p0=(a,b) from one side.
By continuity z1(p0)=zeta. Choose local angular lifts
x=y1-a, t=y2-b with p0=(0,0). Since u1 is constant on the incoming
interval and is smooth,

\[
 \partial_2u_1(p_0)=0,\quad
 A=\partial_1u_1(p_0)\in\mathbb R,\quad
 c=\partial_1u_2(p_0)\in\mathbb R,\quad
 d=\partial_2u_2(p_0)\in\mathbb R.
                                                               \tag{3}
\]

Put alpha=A+i, beta=d+i and rho=sqrt(x^2+t^2). Both alpha and beta
are nonzero. Differentiability of the actual radial coordinates gives

\[
 z_1-\zeta=\zeta\alpha x+o(\rho),\qquad
 z_2-\eta=\eta(cx+\beta t)+o(\rho),\quad \eta=z_2(p_0).
                                                               \tag{4}
\]

The first-order approximation is enough: finite holomorphic
factorization and continuity of the nonzero remaining factors give
the leading homogeneous term of Q. In particular there is no use
of an identity theorem for u or a formal jet as a contact set.

If G(eta)!=0 and eta!=zeta, L879's intrinsic single-odd-contact
argument applies at p0 and already extends the same fiber across it.
The only other cases are (i) eta!=zeta and G(eta)=0, and
(ii) eta=zeta. They are treated next, without dropping any factor.

### Distinct simultaneous G contacts

Let eta!=zeta have arbitrary order n>=1. Isolate the two zero labels
in separate discs, and shrink the angular neighborhood so z1!=z2
throughout. From (1) and (4),

\[
 Q(x,t)=D x^m(cx+\beta t)^n+o(\rho^{m+n}),
                                                               \tag{5}
\]
\[
 D=-C\frac{g_\zeta(0)g_\eta(0)(\zeta-\eta)^2}
                 {\zeta^2\eta^2}
       J(p_0)\zeta^m\alpha^m\eta^n\ne0.
\]

All factors in D are nonzero by the present hypotheses. The
polynomial P=conjugate(lambda)*D*x^m*(cx+beta*t)^n is real-valued
on R^2: for any real v, it is the limit as epsilon decreases to zero
of epsilon^(-m-n)*conjugate(lambda)*Q(epsilon*v). Thus its
coefficients are real, and it is a nonzero homogeneous polynomial.

Its distinct projective factors are x and l=cx+beta*t; they are
distinct because beta!=0. Conjugation fixes x. It cannot send l
to x, since conjugating again would identify l with x. Therefore
l is proportional to its conjugate. Normalizing its t coefficient
to 1 says c/beta is real. But

\[
             \operatorname{Im}\frac{c}{d+i}
                  =-\frac{c}{d^2+1},
\]

so c=0. Consequently, with a real nonzero kappa,

\[
        \overline\lambda Q(x,t)
              =\kappa x^m t^n+o(\rho^{m+n}).            \tag{6}
\]

Here kappa=conjugate(lambda)*D*beta^n is real because it is a
nonzero coefficient of the real polynomial just obtained. Reality
of the leading term has restricted the actual derivative at p0;
it has not yet proved the outgoing contact. That final step follows
below from exact phase constancy on nonzero sectors.

### A G zero on the diagonal

Now eta=zeta. Both G factors have the same actual odd order m.
The diagonal factor in (1) has order two. The full expansion is

\[
 Q(x,t)=D x^m l_2(x,t)^m l_\Delta(x,t)^2
                         +o(\rho^{2m+2}),               \tag{7}
\]
\[
 l_2=cx+\beta t,\qquad
 l_\Delta=(\alpha-c)x-\beta t,\qquad
 D=-C g_\zeta(0)^2 J(p_0)\zeta^{2m-2}\alpha^m\ne0.
\]

The factors x,l2,lDelta are pairwise nonproportional. Both latter
factors have nonzero t coefficient, and l2+lDelta=alpha*x with
alpha!=0 prevents their being proportional: their t coefficients
would force a proportionality constant -1, contrary to that sum.
The phase-normalized leading polynomial is real and nonzero by the
same rescaled limit as above, now of degree 2m+2.

Conjugation fixes x, so neither other factor can be sent to x.
It also cannot interchange l2 and lDelta: their multiplicities are
m and 2, which differ because m is odd. Each is therefore separately
real up to scalar. For l2, as in (5), this gives c=0. For lDelta,
normalizing its t coefficient now gives alpha/beta real. Since

\[
          \operatorname{Im}\frac{A+i}{d+i}
                        =\frac{d-A}{d^2+1},
\]

we have A=d and alpha=beta. Thus, for another real nonzero kappa,

\[
   \overline\lambda Q(x,t)
       =\kappa x^m t^m(x-t)^2+o(\rho^{2m+2}).           \tag{8}
\]

Indeed kappa=conjugate(lambda)*D*alpha^(m+2) is the coefficient
of x^(m+2)*t^m in the real polynomial, and is nonzero. This
argument uses oddness only where stated; it does not extend this
multiplicity comparison to m=2 or to even contacts in general.

### From incident phase signs to exact outgoing fibers

In case (i), the isolated-label discs and the angular graph imply
that all possible nearby zeros of Q lie on x=0 or t=0. J is
nonzero, and the diagonal was excluded by shrinking. A zero of
the first G factor requires x=0; a zero of the second requires
t=0. These are containing lines, not assertions of contact on
the lines. Hence Q is nonzero in each open quadrant.

In case (ii), isolate zeta for both coordinates. All possible
nearby zeros lie on x=0, t=0 or x=t; the last condition is
necessary for z1=z2 because equality of nonzero complex numbers
implies equality of their angles. Again these are only containing
lines. No additional zeros arise from J.

Let sigma be either +1 or -1, and take delta>0 sufficiently small.
On each of the two connected open wedges

\[
 W_+=\{0<\sigma t<\delta,\ 0<x<|t|/2\},\qquad
 W_-=\{0<\sigma t<\delta,\ -|t|/2<x<0\},             \tag{9}
\]

Q is nonzero in either case. L879 gives a constant phase on each
wedge. Fix 0<epsilon0<1/2 and approach p0 on the rays
(x,t)=r*(epsilon0,sigma) and r*(-epsilon0,sigma), r>0.
For (6) the two nonzero real leading values have opposite signs
because m is odd. For (8) they also have opposite signs: the
t^m factors have the same sign on the two rays and both
(x-t)^2 factors are strictly positive. Taking normalized limits
therefore shows that the two constant wedge phases are opposite.

For every t with 0<sigma*t<delta, (0,t) belongs to the closure
of both wedges. If Q(0,t) were nonzero, continuity of Q/|Q|
at that point would make the two phases equal. This contradiction
forces Q(0,t)=0. At that point t!=0, so the second G factor is
nonzero in the isolated-label neighborhood; also the diagonal is
absent (in case (ii), x=0!=t). Since J!=0, the zero is necessarily
G(z1(0,t))=0. The isolated first label then gives exactly
z1(0,t)=zeta throughout this interval.

Thus an incoming same-label odd-contact interval extends across
every possible endpoint, including both sorts of actual vertex.
The conclusion holds on both sides; it does not merely prescribe
a compatible first derivative or infer an exact set from a Taylor
polynomial. The exact implication uses nonzero sectors, their
constant phases, continuity and the isolated ambient label.

### Closing the angular circle

The initial single odd contact supplies a nonempty interval of
z1(a,t)=zeta by L879. Choose t0 in its interior in a real periodic
lift of the second angle. Consider the supremum b in
[t0,t0+2pi] such that z1(a,t)=zeta for every t in [t0,b].
The set is nonempty beyond t0, and continuity includes its supremum.
If b<t0+2pi, the one-sided interval ending at b gives (3), and
the endpoint argument just proved extends it beyond b, a
contradiction. Therefore the equality holds on [t0,t0+2pi].
Periodicity gives the entire circle, with the same label zeta.
This includes vertices at any chosen angular cut; local lifts do
not change the exponentials or the original density.

For j=2, exchange coordinate indices in the scalar factorization
and the angular argument. F is symmetric in its two arguments and
the full J remains included; no differential-form orientation is
reassigned and no integral or extra sign is used. The same proof
then gives the horizontal version of (2).

This finishes the stated continuation test. No assertion that the
contact branch is globally realizable, impossible, or sufficient
for an RH-related sign follows from (2). In particular the
session43 automatic-single-ray stop is not removed by proving
continuation alone, and the earlier product, retired two-period,
positive-contact and relaxed-dual obstructions retain their scopes.

### Independent conceptual audit, 6 November 2026

The unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-06-stationary-odd-fiber-continuation.md`
covers this audit of exactly (2). It accepts the proof without a
mathematical repair or stronger conclusion. This is independent local
verification of the submitted argument, classified REPRODUCTION,
not a new theorem beyond that argument or a claim of originality.
The full proof remains above; the load-bearing checks follow.

The input from L879 is its accepted phase line, componentwise phase
constancy and intrinsic local odd-contact fiber. Its variation only
uses supports compactly contained in {Q!=0}; the present argument
introduces no variations through zeros. L847 supplies the actual
entire nonzero G and the full scalar density and orientation. Its
positive-product obstruction is not used. The two cited elementary
factorization statements retain exactly the scopes recorded above.

At an endpoint of the incoming interval, u1(a,t) is one constant on
one side and at the endpoint. Smoothness makes its tangential
derivative zero there. Thus (3) and (4) hold without an assumption
of analytic u or an isolated contact set. Each linear factor in
(5) and (7) is a nonzero polynomial. Multiplying finitely many
O(rho) expansions with o(rho) errors, then the continuous units and
J, gives the asserted uniform o(rho^degree) remainder. The fact that
a leading factor vanishes on some rays does not make the polynomial
zero or invalidate this expansion. Its nonzero rays are the ones
used later. For (5) the scalar is exactly the displayed D. For (7),
the numerator contributes zeta^(2m+2) and the denominator zeta^4,
giving precisely zeta^(2m-2) in D. Neither coefficient can vanish.

Since conjugate(lambda)Q is real everywhere, rescaling along each
real vector makes its leading homogeneous polynomial real on R2.
The imaginary part is a polynomial vanishing on all R2, so all
its coefficients vanish. This supplies the real-coefficient premise
of the cited conjugation fact; merely selecting one real ray would
not suffice. In (5), x and cx+beta*t are distinct because beta!=0.
The factor x is fixed under conjugation. Involution then prevents
the other factor from being sent to x, even if m=n. It must be
fixed projectively, and c/(d+i) real forces c=0.

For (7), the two t coefficients are beta and -beta. Proportionality
of l2 and lDelta would therefore have multiplier -1, contradicting
l2+lDelta=alpha*x with alpha!=0. Neither is proportional to x.
Conjugation fixes x and cannot send another factor to it, including
when both have multiplicity m. Interchanging the other two factors
would require m=2. Every allowed odd m excludes this case, including
m=1. Consequently both factors are fixed projectively: first c=0,
then alpha/beta real. The imaginary part of alpha/beta is
(d-A)/(d^2+1), so A=d. The real nonzero coefficients in (6) and (8)
are respectively conjugate(lambda)D*beta^n and
conjugate(lambda)D*alpha^(m+2), as claimed. No statement for even m
is inferred from the unequal-multiplicity argument.

Isolating each ambient zero label, and using local angular lifts of
width less than 2pi, makes its angular line a necessary condition
for a contact. In case (i) disjoint label discs exclude the diagonal,
even when distinct labels have the same argument. In case (ii) the
diagonal requires x=t. Thus every point of each wedge (9) is an
actual nonzero point of Q; no claim that all containing lines are
zero sets has been made. The wedges are connected for each sign of
t. Along both selected rays, all leading factors are nonzero. The
two normalized limits differ by -1 because m is odd; the t factor
has the same sign on both rays and the diagonal square is positive.
Componentwise phase constancy makes those limiting phases the exact
wedge phases, independent of how small a nonzero value of Q becomes.

For any fixed 0<|t|<delta, continuity at (0,t) would identify the
opposite wedge phases if Q(0,t) were nonzero. Hence it is zero.
The isolated second label requires t=0, and a diagonal contact in
case (ii) requires x=t, so neither can cause this zero. J is nowhere
zero. The remaining first G factor must therefore vanish at precisely
zeta. This verifies exact labeled continuation, not just a necessary
jet condition, on both sides of the vertex. The remaining endpoint
case, with G(eta)!=0 and eta!=zeta, is exactly L879's intrinsic
single-contact argument. These three cases are exhaustive.

For closure, the set of b for which the entire interval [t0,b]
has the same label is downward closed. The initial local fiber
makes its supremum strictly larger than t0; continuity supplies
the label at that supremum and at every preceding point. If the
supremum precedes t0+2pi, the established endpoint argument extends
the interval, a contradiction. Equality at t0+2pi is also included
by continuity. Periodicity covers the circle, and local angular
lifts cover vertices at the cut. This does not require a finite
census of pullback contacts. Exchanging both coordinate indices
conjugates the matrix I-iDu by the permutation matrix, preserving
its determinant; F is symmetric. This scalar relabeling adds no
orientation change to Q and proves the j=2 assertion.

No error or missing case was found. L847 and L879 remain the only
direct local mathematical inputs; there is no new DAG edge. The
result still neither excludes nor realizes an odd-contact stationary
graph and supplies no mass equality, sharp period, compactness,
higher sign or actual-Xi transfer. No mathematical script or numerical
evidence was needed for this analytic and topological audit.

## Mathlib

Full matching coverage and formal coverage of the supporting
factorization/conjugation and phase-sector arguments were not
checked. No Mathlib theorem is imported, and unknown coverage is
not evidence of absence. The continuation result now has an independent
informal conceptual audit. That audit does not change the Mathlib
coverage status or constitute formal verification or a complete
candidate proof of RH.
