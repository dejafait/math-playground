# Corollary C034z: the actual-Xi second-derivative sector interface

## Hypotheses

Use the actual completion of L018 and the moments of L021. Write

    X(z)=Xi(z)=xi(1/2+iz),
    gamma_j=j! M_(2j)/(2j)! > 0,
    A(w)=sum_(j>=0) (-1)^j gamma_j w^j/j!,
    Theta(u)=A(-u)=xi(1/2+sqrt(u)).

The square-root notation denotes the even entire series; no branch on
the whole plane is chosen. Thus X(z)=A(z^2). Define

    h(z)=X''(z),                  h(z)=B(z^2),
    J^(d,n)(u)=sum_(j=0)^d binom(d,j) gamma_(j+n) u^j.

Fix a real T>1/2. The only additional zero hypothesis in the
conditional conclusions below is RH_2(T): every zero s of the
ordinary derivative xi'' with |Im(s)|<=T has Re(s)=1/2.
Its truth is not established here. Put

    theta_T=2 arctan(1/(2T)),
    K_T={w: Re(w)>=0, |Im(w)|<=tan(theta_T) Re(w)},
    D_T=T^2+1/2+1/(16T^2).

The cone includes zero. All zero assertions allow multiplicities;
no simplicity, RH, or transformed-derivative sector premise is assumed.

## Conclusion

The exact coefficient interface is

    B=2A'+4wA'',
    B^(r)(w)=2 sum_(j>=0) (2j+2r+1)(-1)^(j+r+1)
                         gamma_(j+r+1) w^j/j!       (r>=0).       (1)

Under RH_2(T), Kim--Lee's even-function argument applies to h.
It gives Z(B^(r)) contained in K_T for every r>=0, and the Jensen
polynomials of B^(r) are hyperbolic for integer 1<=d<=D_T.
In particular the shift-two polynomial thereby covered is

    J(B';d)(u)=2 sum_(j=0)^d binom(d,j)(2j+3)gamma_(j+2)(-u)^j.   (2)

This is not the unweighted J^(d,2)(-u), even up to a common
nonzero scalar when d>=1. The missing sector statement for the
GORRTTW m=2 application is

    Z(A'') contained in K_T, equivalently
    Z(Theta'') contained in -K_T.                              (3)

The cited forward proof does not supply (3) from RH_2(T): applying
it to X requires an unpaid initial sector for A; applying it to h
gives (1)--(2). More explicitly, the paid derivative controls

    B'=2(3+2w d/dw)A'',                                       (4)

and removing this Euler factor requires an additional zero-location
argument. This is an audit of the available justification, not a
proof that (3), GORRTTW Theorem1.2, or any actual-Xi claim is false.
No negative example or new theorem of inverse sector preservation
is asserted. No all-degree mixed sign or RH conclusion follows.

## Proof

### Imported inputs and why specialization is needed

Young-One Kim and Jungseob Lee, *A note on the zeros of Jensen
polynomials*, [arXiv:2105.05386v1](https://arxiv.org/pdf/2105.05386v1),
12 May2021, pp1--4: use the real-entire product and approximation
preliminaries on p1, the stated order-one property of Xi on pp1--2,
and Theorem4, its complete proof on p3 and its final remark on p4.
The theorem assumes an even transcendental real entire function of
order<2 whose nonreal zeros lie in |Im(z)|<1/2, |Re(z)|>=T, with
T>=1/2. Its proof propagates the squared convex sector forward by
differentiation; the final remark includes all derivatives of the
square transform and the degree bound D_T. These results are imported,
not claimed as new. The longer published version is not used.

C. McMullen, *Advanced Complex Analysis*, Harvard Math213a notes,
30 November2023, [author PDF](https://people.math.harvard.edu/~ctm/home/text/class/harvard/213a/23/html/home/course/course.pdf):
Theorem3.15 p80 (Hadamard factorization), the canonical-product
convergence statement p79, Theorem3.7 and its proof pp76--77
(zero-free finite-order entire functions), Theorem1.4 p10 (Cauchy's
formula), and the Cauchy bound p17 supply the standard analytic
inputs for the strict-strip audit below. These inputs are imported;
the audit checks their use for the two actual functions, rather than
reproving factorization or claiming a new strip-preserver theorem.

Griffin--Ono--Rolen--Thorner--Tripp--Wagner, *Jensen polynomials for the
Riemann xi-function*, [arXiv:1910.01227v3](https://arxiv.org/pdf/1910.01227v3),
17 December2020, (1.1)--(1.2), Theorem1.2 and Section5, pp1--2,11--12;
also the [author accepted manuscript](https://uva.theopenscholar.com/files/ken-ono/files/jensenadvmathaccepted.pdf),
corresponding pp1--2,12--13. RH_m(T) concerns ordinary xi derivatives;
Section5 uses derivatives of Theta. The accepted version explicitly
names these latter functions psi_n=Theta^(n). Its m=2 sector step is
the inference being audited, not an imported premise. Lemma5.1
propagates an established sector forward. The Chasse-dependent
Lemma5.2 is outside this audit.

The work below is necessary to match the actual functions, coefficient
weights and endpoints before using Kim--Lee. The elementary product
argument is included only to check the strict derivative-strip
hypothesis, which a limit of polynomial Gauss--Lucas statements alone
would only give with a closed boundary. No generic polynomial model
or purported refutation of an xi-specific theorem is used.

### Actual analytic hypotheses, including the strict strip

L018 identifies X as even and real entire, and places its zeros in
|Im(z)|<1/2. L021 supplies its full entire series and strictly positive
moments. The imported order-one fact and Cauchy's estimate on a
circle of radius r about a point of modulus at most r give

    M_(X^(k))(r) <= k! r^(-k) M_X(2r).

Consequently all its fixed derivatives have order at most one.
Infinitely many nonzero Taylor coefficients show that X, X', h,
A, B, and all derivatives of A and B used here are nonpolynomial.
Indeed M_(2j)>0 makes every even coefficient of X nonzero, and any
fixed number of differentiations leaves infinitely many such terms.
They are real entire; h is even. The maximum-modulus identity
M_B(r)=M_h(sqrt(r)), and the analogous identity for A, give order
at most 1/2 for both square transforms; the same Cauchy estimate
then gives that bound for their fixed derivatives. The entire series
defining these square transforms have infinite radius of convergence.

For completeness, the real canonical product used in Kim--Lee's
preliminaries verifies the needed strict strip for differentiation.
Let E be a nonconstant real entire function of order<2 whose zeros
lie in |Im(z)|<1/2. The cited factorization has the form

    E(z)=c z^m exp(bz) product_a ((1-z/a) exp(z/a)),
    c!=0, m>=0, sum_a |a|^(-2)<infinity.

Here a lists nonzero zeros with multiplicity; finite and empty lists
are allowed. For H(z)=E(z)/z^m, with the removable value at zero,
c=H(0) is real and nonzero. Each genus-one factor has value 1 and
derivative 0 at zero. Compact product convergence and Cauchy's
formula therefore give b=H'(0)/H(0), which is real. This does not
require convergence of the separate sum of 1/a.

Its logarithmic derivative away from its zeros is

    E'/E = b + m/z + sum_a (1/(z-a)+1/a),       b real,          (5)

where m/z is omitted when m=0, including at z=0 if E(0)!=0.
Here is the complete convergence justification. For a compact K
avoiding the zeros, choose R>=1 with K contained in |z|<=R. When
|a|>2R,

    |1/(z-a)+1/a|=|z/[a(z-a)]|<=2R/|a|^2.

The remaining nonzero zeros form a finite set, and their terms have
no poles on K. Thus the corrected series converges absolutely and
uniformly on K. Finite products E_N converge to E uniformly on
compact sets by the imported product theorem. Cauchy's formula on
a slightly larger compact neighborhood of K gives E_N' -> E'
uniformly on K. Since min_K |E|>0, also E_N'/E_N -> E'/E uniformly
there. The finite logarithmic-derivative formula consequently passes
to (5). Only the corrected summands are rearranged below; separate
series of 1/(z-a) and 1/a are never asserted to converge.

Reality of E pairs every nonreal zero with its conjugate and the
same multiplicity. Absolute convergence of the corrected series
permits grouping these pairs and the real zeros.

For z=x+iy with y>=1/2, the imaginary part of a real-zero summand
is -y/|z-a|^2<0. For a=u+iv and its conjugate it is

    -(y-v)/((x-u)^2+(y-v)^2)
    -(y+v)/((x-u)^2+(y+v)^2) < 0,

since |v|<1/2<=y; the imaginary parts of the two 1/a terms cancel.
The term m/z has imaginary part -my/|z|^2. The grouped imaginary
series converges by the preceding absolute convergence. If E has a
zero, either m>0 or at least one real-zero or conjugate-pair term is
present. Fixing that strictly negative contribution bounds the
remaining partial sums above by a strictly negative number; their
limit is therefore strictly negative too. Since E(z)!=0 for
y>=1/2, (5) implies E'(z)!=0 there. Conjugation of E' gives the
assertion on y<=-1/2. Equality y=1/2 was included: each y-v and
y+v is positive because |v|<1/2. No uniform margin in x or in E
is asserted.

If E has no zeros, the cited zero-free classification, equivalently
the empty canonical product, gives E(z)=c exp(bz). Order<2 limits
the exponential polynomial to degree at most one; reality gives
real c!=0 and b. Nonconstancy forces b!=0, so E'=bc exp(bz) is
zero-free. The excluded constant case really is essential because
its derivative would vanish identically.
This covers every case needed here, including multiplicities and the
boundary y=+/-1/2.

First use E=X: its real-entire, nonconstant and order<2 hypotheses
were checked above, and its open zero strip comes from L018, not
from an RH premise. Hence X' has no zeros on or outside either
boundary. Next use E=X': it is real entire, nonconstant and of
order at most one, and its open zero strip is now supplied by the
first application. In fact X'(0)=0 and X''(0)=-M_2<0 by L021,
so X' has a simple zero at zero; its m/z term already gives a
strict negative contribution in the upper half-plane under test.
It follows that every zero of h=X'' lies in |Im(z)|<1/2.
Neither application assumes simplicity of any other zero, a
uniform boundary distance, RH_2(T), or RH_0(T).

**Limited mathematical audit2183 (21 November2026).** The preceding
actual-function growth and strict-strip argument passed its separate
conceptual audit, including compact logarithmic differentiation,
real constants, zero-free cases and both closed boundary lines.
The details above make the existing justification explicit; no
mathematical defect or strengthened conclusion was found. This
audit does not certify the remaining subsections, the truth of
RH_2(T), inverse Euler transfer, or all-degree mixed positivity.

### Translating RH_2(T) and the square sector

The affine chain rule gives h(z)=-xi''(1/2+iz). If z=x+iy, its
corresponding s has Im(s)=x and Re(s)=1/2-y. Thus RH_2(T) says
precisely that h has no nonreal zero with |Re(z)|<=T, preserving
multiplicities and the closed height endpoints. Every nonreal h zero
therefore satisfies |x|>T and |y|<1/2. A real h zero is nonzero
because h(0)=-M_2<0.
The affine substitution has derivative i!=0, and the prefactor -1
does not change any zero order. In particular, zeros at x=+/-T
are covered by the conditional hypothesis; they cannot be discarded
as exceptional height endpoints.

For a nonreal h zero, its square has positive real part and

    |arg(z^2)| = 2 arctan(|y/x|) < theta_T < pi/2.

A real nonzero zero squares to a positive real number. This proves
Z(B) contained in K_T directly from h(z)=B(z^2); no inference from
positive coefficients to half-plane stability is involved. At a
nonzero square root the square map has nonzero derivative: a zero
of B of multiplicity m corresponds to two zeros of h, each of
multiplicity m, not a zero of B of multiplicity 2m. There is no
ramification issue at zero since B(0)=-M_2.
The argument formula uses the principal argument of z^2; replacing
z by -z if needed makes x>0 and leaves z^2 unchanged. Conversely
each B zero has a square root and hence is covered by this argument.

The actual h satisfies all of Kim--Lee Theorem4's hypotheses under
RH_2(T). Their square-sector parameter is

    delta=(1+4T^2)^(-1/2),
    tilde_delta=2 delta sqrt(1-delta^2)=sin(theta_T).

Their right-hand convex sector is exactly K_T. Their proof and final
remark therefore give Z(B^(r)) contained in K_T and Jensen
hyperbolicity through

    tilde_delta^(-2)=T^2(1+1/(4T^2))^2=D_T.

For clarity, T>1/2 gives 0<theta_T<pi/2 and
tilde_delta=4T/(4T^2+1) in (0,1). On Re(w)>=0 the source condition
|Im(w)|<=tilde_delta |w| is equivalent, by squaring nonnegative
quantities, to |Im(w)|<=tan(theta_T) Re(w). It includes w=0.
Thus the imported cone really is the closed convex cone stated here,
not the origin-excluding sector notation in GORRTTW. No use of that
source's exponential parameter or its separate origin factor is needed.
The order bound for B and each of its fixed derivatives is <=1/2<1
by audit2183, as required for the source's sector differentiation.
The nonzero-derivative and Jensen-degree checks are given below.

Algebraically tilde_delta^(-2)=(4T^2+1)^2/(16T^2).
The degree d is an integer, so this upper bound means d<=floor(D_T),
not rounding D_T upward. Equality is permitted when D_T is an integer:
the source uses a non-strict degree inequality. All derivative-sector conclusions retain
closed angular boundaries; neither strict hyperbolicity nor a root
margin is imported. In particular floor(T)^2<=T^2<=D_T does not remove
the coefficient difference below. T=1/2 is outside this audit's
overlap scope; no limiting endpoint claim is needed.

### Matching the derivatives rather than their names

Entire power series may be differentiated locally uniformly. Applying
the ordinary chain rule twice to X(z)=A(z^2) gives

    X''(z)=2A'(z^2)+4z^2 A''(z^2).

Comparison of entire series yields B=2A'+4wA''. Expanding and
differentiating r times proves (1). For the Jensen convention
J(G;d)(u)=sum_(j=0)^d binom(d,j)G^(j)(0)u^j, it follows that

    J(B^(r);d)(u)=2(-1)^(r+1) sum_(j=0)^d
                  binom(d,j)(2j+2r+1)gamma_(j+r+1)(-u)^j.       (6)

In particular B^(r)(0)=2(2r+1)(-1)^(r+1)gamma_(r+1)!=0 for
each integer r>=0. The same formula at r+d shows that J(B^(r);d)
has exactly degree d. Thus no identically zero derivative or zero
limiting Jensen polynomial is silently treated as hyperbolic.
All these functions have real coefficients. Formula (1) follows
directly at r=0 from the coefficient of w^j in 2A'+4wA'', namely
2(2j+1)(-1)^(j+1)gamma_(j+1)/j!; shifting j to j+r gives (1)
for every r, with the factorial in (6) canceled by differentiation.

At r=1 this is (2). By contrast,

    A''(w)=sum_(j>=0)(-1)^j gamma_(j+2)w^j/j!,
    Theta''(u)=A''(-u),
    J(A'';d)(u)=J^(d,2)(-u).

The ratios of the constant and linear coefficients in (2) to those
of J^(d,2)(-u) are 6 and 10 respectively, since gamma_2,gamma_3>0
and d>=1. Hence a scalar normalization cannot identify the two.
Differentiating the identity for B gives (4). For d=0 both Jensen
polynomials are nonzero constants, which says nothing about the
missing all-degree sector statement.

Finally track the operative direction in the even-function proof.
Writing a general even input as q(z)=a(z^2), that proof starts with
zeros of a in the convex square sector. Gauss--Lucas for its
order<1 product places the zeros of a' there. The auxiliary entire
function w(a')^2 then has its zeros there, and differentiation gives

    (w(a')^2)'=a'(a'+2wa'').                                  (7)

For the actual transforms a=A or a=B, a' is nonpolynomial and
nonzero, so w(a')^2 is nonconstant and its derivative is not
identically zero. Its order is at most 1/2, and its additional
zero at w=0 belongs to the closed cone. Every zero of a'+2wa''
is a zero of the product on the right of (7), including shared
zeros with a'; no cancellation or simplicity is required.
Thus the zeros of q'' are in the corresponding double sector;
q'' is even and this can be iterated forward. The proof also
differentiates a itself to obtain its final square-transform remark.

For q=X, this argument needs the sector of A as its starting input.
RH_0(T) would supply it by the same square geometry, but RH_0(T) is
not an assumption here and is not inferred from RH_2(T). For q=h,
the initial square transform is B; the argument controls B and its
derivatives and moves ordinary derivatives toward X''''. In (7)
with a=A, knowing the zeros of B alone does not locate the zeros
of the other factor A', and differentiation of the product cannot
be reversed by the quoted Gauss--Lucas step. None of these forward
operations identifies A'' with B or B'. This proves the stated
scope limitation and identifies exactly (3)--(4) as unpaid.

The bound D_T is finite at fixed T, and RH_2(T) itself remains
conditional. Even a future proof of (3) would not establish the
unshifted all-degree signs in L030/L032/C032a. No step here replaces
algebraic squares by absolute squares, takes an inverse Rolle
implication, assumes a derivative commutation, or turns a missing
justification into a counterexample. The result is a reproduction
and applicability audit of checked mathematics, with an informative
negative interface finding, not progress beyond those sources.

**Remaining-interface audit2191 (21 November2026).** The two preceding
subsections passed independent conceptual checking, reusing audit2183
for the strict strip and growth. Closed height endpoints, both square
roots and their multiplicities, the origin, all nonzero derivative
orders, the integer degree floor including equality, factorials,
r=0/r=1, d=0/d>=1 and the auxiliary-product direction were checked.
The additional details make the existing applicability argument
explicit; no mathematical defect or stronger conclusion was found.
The imported Kim--Lee forward input is validated in this local scope.
The truth of RH_2(T), the inverse implication (3), all-degree signs,
and any assertion of falsehood of GORRTTW Theorem1.2 remain outside
the conclusion. This completes the remaining C034z interface audit.

## Mathlib

Full matching coverage for this actual-Xi conditional interface and
the Kim--Lee theorem has not been checked. No absence claim is made.
The calculus identities and canonical-product argument above are
informal; no Lean verification or machine certificate is asserted.
