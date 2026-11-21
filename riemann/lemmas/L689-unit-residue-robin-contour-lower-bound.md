# Lemma 689: a positive unit-residue response on the Robin node family

## Hypotheses

Use exactly L673's fixed-1/10 node family within L666. For an integer
q>=1 put

    n=12q+3, h=27/(10n), rho=h/10=27/(100n), lambda=pi/h,
    x=-d=-5/4, R=11/8, U=121/64, t_j=j/n (0<=j<n).

For 0<=k<2q let s_k be the unique solution in (k+1/2,k+5/8) of

    s_k=k+1/2+atan(1/(10s_k))/pi,
    y_k=h*s_k, Z={x} union {x+i*y_k,x-i*y_k:0<=k<2q}.

Every original residue is one. Retain the complete rational product

    W_a(u)=(x/a)*product_(1<=j<n)
          [(x-t_j*u)/(a-t_j*u)]*[(U*u-t_j*a)/(U*u-t_j*x)],
    c_0(u)=R^(-1)*sum_(a in Z) W_a(u),
    D=mean_(|u|=1) sum_(a in Z) |W_a(u)|^2/(U-|a|^2),
    V_r=max_(|u|=|zeta|=1)
               |R^(-1)*sum_(a in Z) W_a(u)/(1-r*a*zeta/R)|.

The angular mean is normalized. In particular, D uses the original
nodes and squared unit residues. Set r=1/32. The same node set is
used at every angular and spatial argument.

## Conclusion

For every prescribed n>=300, with F(z)=W_(x+z)(-1),

    |R*c_0(-1)-F(-rho)| <= 10*n*exp(-n/3000),             (1)
    F(-rho) >= exp(-297/500) > 1/2.                       (2)

Consequently, beyond one absolute onset along n=12q+3,

    c_0(-1)>=1/(4R),    V_(1/32)>=1/(4R),                (3)
    V_(1/32)>=n*exp(-n/48)*sqrt(D).                       (4)

Thus the approved original-D norm estimate holds with c=1 after
an absolute onset for this full-support displaced subfamily only.
The onset in (3)--(4) is existential; (1)--(2) have the stated
finite-n range. The general independent-displacement cube remains
unresolved. L683's conditional transfer still needs its audit;
H/support, Xi realization and actual mixed signs remain separate.
No RH candidate is asserted. The separate conceptual audit in Section 5
retains (1)--(4), with their stated finite-n range, existential final
onset and prescribed-family restriction.

## Proof

### 1. Scope and the finite contour inputs

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
This is the specified unit-residue subfamily test of its norm target.
L665's absolute perturbation-kernel stop does not bound the signed
integral here; the L673/L681 auxiliary weights are not used as
original residues. The earlier origin-continuation and exterior-value
costs concern other certificates. None supplies (1).

Import the standard finite residue theorem and simple-pole rule,
with the elementary contour integral bound, as already inspected in
the ready source records: NIST DLMF Section 1.10(iv),
[equation (1.10.8)](https://dlmf.nist.gov/1.10#E8), and R. W. Howell
and J. H. Mathews, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
[Section 6.2, Theorem 6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
These require a positively oriented closed contour, analyticity on a
neighborhood of the contour, finitely many interior poles and no
boundary poles. We verify those hypotheses below. No infinite
quadrature, asymptotic zero census or new source theorem is assumed.
The new calculation is the logarithmic-derivative subtraction and
its finite-edge error; the general residue theorem is not reproved.

L673 verifies admissibility of the specified nodes. L681 Sections 1--2,
with its separate audit, prove that

    Q(z)=z*cosh(lambda*z)+rho*sinh(lambda*z)

has only imaginary zeros: zero and the pairs +/-i*h*s_k for all
k>=0, each simple. Here s_k denotes the same defining root extended
to all k>=0. This exact census applies to any rectangle of positive
left/right widths and the same horizontal height used next.

Put b=1/50, c=1/200 and Y=2qh=9/20-27/(20n). Let Gamma be the
positively oriented boundary of

    -c<=Re z<=b,       |Im z|<=Y.

For n>=300, rho<=9/10000<c/2 and 2/5<Y<9/20. The census gives
exactly zero and the 4q required nonzero zeros of Q inside Gamma.
There are none on its boundary, since lambda*Y=2q*pi. Each residue
of Q'/Q at these zeros is one, including the central zero.

The only possible parameter poles of F are z=d-t_j>=1/4, including
z=d from j=0. Thus F is holomorphic on a neighborhood of this closed
rectangle. The denominators U-t_j*d are positive as well. The
finite residue theorem gives

    sum_(a in Z) W_a(-1)=(1/(2*pi*i))*integral_Gamma F(z)*Q'(z)/Q(z) dz.

Define on the boundary

    H(z)=Q'(z)/Q(z)-lambda-1/(z+rho).

The point -rho is strictly interior, F is analytic there, and the
constant lambda contributes zero to the contour integral. Therefore

    R*c_0(-1)=F(-rho)+(1/(2*pi*i))*integral_Gamma F(z)*H(z) dz. (5)

The pole at -rho belongs to the subtracted rational function. Its
residue is retained in (5); it adds no node or residue to D.

### 2. The complete product on the four edges

For e>1 write W_e(y)=W_(-e+i*y)(-1). L664 Section 3 proves,
including the j=0 factor and the finite-sum errors, that

    |F(b+i*y)|<=exp(11n/250),          |y|<=Y,
    |F(-c+i*y)|<=exp(1-9n/1000),      |y|<=Y,
    |F(s+/-i*Y)|<=exp(1-n/100),       -c<=s<=b.          (6)

Indeed e=d-s runs from 123/100 to d+1/200, and Y is exactly
L664's moving endpoint. Its inequalities (9), (10), (12) have these
same ranges and are valid here since n>=300>27. These are product
bounds for F; they do not require its sampling nodes to be equally
spaced. This is why they can be reused for the Robin nodes.

We also use the monotonicity proved there for

    g_n(e)=sum_(j<n) [1/(e-t_j)+t_j/(U-e*t_j)].

For 123/100<=e<=R, each summand is positive and nonincreasing in e.
Its monotonicity in t and the cited exact bound g(123/100)<11/5
give g_n(e)<11n/5. The same local product identity gives

    d_e log W_e(0)=-g_n(e),     W_d(0)=1.               (7)

### 3. The logarithmic derivative on every boundary segment

Use 3<pi<22/7, so 10n/9<lambda<6n/5. On Re z=b factor

    Q(z)=(z+rho)*exp(lambda*z)*(1+r(z)*exp(-2lambda*z))/2,
    r(z)=(z-rho)/(z+rho).

Here |r|<1, |r'|<=2rho/b^2=1350/n, and

    H(z)=(r'(z)-2lambda*r(z))*exp(-2lambda*z)
                                      /(1+r(z)*exp(-2lambda*z)).

For n>=300, exp(-2lambda*b)<1/2 and
1350/n+12n/5<3n. Consequently

    |H(b+i*y)|<=6n*exp(-2lambda*b).                     (8)

On Re z=-c use the opposite factorization

    Q(z)=(z-rho)*exp(-lambda*z)*(1+p(z)*exp(2lambda*z))/2,
    p(z)=(z+rho)/(z-rho).

Then |p|<1, |p'|<=2rho/c^2=21600/n and

    Q'/Q=-lambda+1/(z-rho)+E(z),
    E(z)=(p'(z)+2lambda*p(z))*exp(2lambda*z)
                                      /(1+p(z)*exp(2lambda*z)).

Since 2lambda*c>n/90>1, exp(-2lambda*c)<1/2. Also
21600/n+12n/5<3n, so |E|<=6n*exp(-2lambda*c)<3n.
The remaining reciprocals satisfy

    |1/(z-rho)|<=200,       |1/(z+rho)|<=250,

using rho<=9/10000<1/1000 for the second. It follows that

    |H(-c+i*y)|<=12n/5+450+3n<10n.                     (9)

On z=s+/-i*Y, the exact phase lambda*Y=2q*pi gives

    Q'/Q=lambda*tanh(lambda*s)
       +(1+rho*lambda*sech(lambda*s)^2)
                         /(s+rho*tanh(lambda*s)+/-i*Y).

Since rho*lambda=pi/10<1/3 and Y>2/5, this implies

    |H(s+/-i*Y)|<=2lambda+(1+rho*lambda)/Y+1/Y
                 <12n/5+7<3n.                         (10)

All bounds include the entire edge and its endpoints. Possible
algebraic exceptional points +/-rho are interior, not on a segment
where a factorization was used. The actual contour in (5) has no
boundary pole.

### 4. Error, positive main term and the original diagonal

On the right edge, (6) and (8) give

    |F*H|<=6n*exp(-(2lambda/n-11/5)*b*n)
           <=6n*exp(-n/2250),

because (20/9-11/5)/50=1/2250. On the left and horizontal edges,
(6), (9), (10) give respectively

    |F*H|<=10n*exp(1-9n/1000),
    |F*H|<=3n*exp(1-n/100).

Each is at most 30n*exp(-n/3000), using exp(1)<3. The perimeter
4Y+2(b+c) is less than 2. The contour bound and 2pi>6 now prove
(1) from (5). This charges all four signed boundary contributions;
there is no omitted infinite tail or unbounded contour deformation.

For the main term, d+rho<R and (7) give

    log F(-rho)=-integral_d^(d+rho) g_n(e) de
                       >=-(11n/5)*rho=-297/500.

It is real and positive before taking the logarithm, since every
factor defining W_(d+rho)(0) is positive. Finally log 2>2/3>297/500:
the first inequality follows, for example, by integrating
log 2=2*integral_0^(1/3) (1-t^2)^(-1) dt. This proves (2).
Conjugate nodes and real product coefficients make c_0(-1) real.
Since 10n*exp(-n/3000) tends to zero, it is at most 1/4 after one
absolute onset, and (1)--(2) give the first inequality of (3).

At u=-1 the function of zeta defining V_r is holomorphic on a
neighborhood of the closed unit disk: r*|a|/R<1 for every original
node. Its constant coefficient is c_0(-1), by a convergent geometric
series (or evaluation at zero). The Cauchy coefficient formula,
[NIST DLMF Section 1.10(iii), equation (1.10.7)](https://dlmf.nist.gov/1.10#E7),
on this positively traversed circle therefore gives V_r>=|c_0(-1)|.
All summations are finite and the denominators
have a uniform positive clearance on that disk. This proves (3).

L661's audited general envelope, applied to L666's admissible family
with exactly M=n/3 unit residues, gives

    D<=n*exp(2*kappa*n+6)/(3*sigma^2),
    kappa=91/5000, sigma^2=137/5000.

Consequently (3) implies

    V_(1/32)/[n*exp(-n/48)*sqrt(D)]
      >=sqrt(3*sigma^2)/(4R*exp(3))
                            *n^(-3/2)*exp(79n/30000) -> infinity,

since 1/48-kappa=79/30000. In particular the ratio is at least one
after another absolute onset, proving (4). The original diagonal is
retained; no weight from the auxiliary Robin quadrature enters it.
This is a local family-specific advance, not a result beyond the
inspected literature certified to be novel, and not uniform coercivity
over L666's independent displacement cube.

### 5. Separate conceptual audit — 3 November 2026, step 90

The invocation-start SPECIALIZE assessment was
`drafts/literature/2026-11-03-unit-residue-robin-contour-audit.md`.
This REPRODUCTION audit retains the existing claims; it adds no stronger
rate, uniform-displacement assertion or novelty claim. The required
finite residue, simple-pole, contour-bound and coefficient-extraction
theorems are precisely those cited above. Their application hypotheses
are checked here. L661's general envelope and L664's product bounds are
imported with their existing separate audits; their arithmetic
certificates are not rerun, and no source-manuscript audit is asserted.

**Nodes, parameter poles and the subtraction.** L673's root intervals
give distinct positive ordinates below 9/20, their negatives, and the
anchor. Thus M=4q+1=n/3 and

    |a|^2<25/16+81/400=353/200<(273/200)^2<R^2.

The symmetric shifts have absolute value below 1/8. These are exactly
admissible original unit residues for L666 and L661, not the auxiliary
weights in L681. The full product in the hypotheses equals B_u(x)/B_u(a),
including the j=0 factor x/a.

For Q, the exponential equation in L681 excludes zeros off the imaginary
axis. The positive zeros solve tan(pi*s)+10*s=0, with exactly one root
in each (k+1/2,k+1); L673 locates it in the stated smaller interval.
Zero has derivative 1+rho*lambda. At a nonzero root i*y the derivative
is cos(lambda*y)*(rho+lambda*(rho^2+y^2))/rho, which is nonzero.
Since Y/h=2q, the contour encloses precisely the required M simple
zeros. Its horizontal sides contain none, and its vertical sides have
nonzero real part. Directly, Q(-rho)=-rho*exp(lambda*rho) is nonzero.

For n>=300, 0<rho<=9/10000<c/2 and 2/5<Y<9/20. Each possible
parameter pole d-t_j of F is at least 1/4, outside the rectangle,
and U-d*t_j>=41/64. These strict inequalities also give analyticity
on a neighborhood of the closed rectangle. The residue of F*Q'/Q at
each enclosed zero is F at that zero. The additional pole of F*H at
-rho has residue -F(-rho); the integral of lambda*F vanishes.
Consequently (2*pi*i)^(-1) times its contour integral is
sum_a W_a(-1)-F(-rho), proving the sign in (5). This pole is neither
a new sampling node nor a term of D.

**Products and every boundary segment.** Under e=d-Re(z), y=Im(z),
L664 Section 3 has exactly the same interval 123/100<=e<=d+c and
moving Y=9/20-27/(20n). Its (9), (10) and (12) give (6), including
the j=0 factor, odd-grid count and left-sum errors. Its derivative
inequalities hold for every 123/100<=e<=R. In particular, although
its displayed upper bound on g_n is used there only for e<=d,
monotonicity extends that same bound to the main-term interval:

    0<g_n(e)<=g_n(123/100)<=n*g(123/100)<11n/5.

No change to a product endpoint or a grid error is required.

On Re(z)=b, |z-rho|<|z+rho| and r'=2rho/(z+rho)^2.
On Re(z)=-c, |z+rho|<|z-rho| and p'=-2rho/(z-rho)^2.
Logarithmically differentiating the two factorizations in Section 3
therefore gives exactly its respective H and E formulas, without a
choice of logarithm branch. The derivative charges for n>=300 obey

    1350/n+12n/5 <=(483/200)*n<3n,
    21600/n+12n/5 <=(66/25)*n<3n.

Also 2lambda*b>2n/45>1 and 2lambda*c>n/90>1, so both geometric
denominators have modulus greater than 1/2. The left reciprocals
are bounded by 200 and 250 because c-rho>1/250. Hence the left
bound before rounding is at most (27/5)*n+450<10n. These checks
establish (8)--(9) for all heights on both edges.

On each horizontal side, lambda*Y=2q*pi makes tanh(lambda*z) and
sech(lambda*z)^2 real with their values at lambda*Re(z). Factoring
Q as cosh(lambda*z)*(z+rho*tanh(lambda*z)) gives exactly (10)'s
logarithmic derivative. The two remaining denominators have modulus
at least Y. The non-lambda charge is

    (2+rho*lambda)/Y <(7/3)*(5/2)=35/6<7,

so 2lambda+7<3n for n>=300. This covers both signs of Im(z) and
all corners; no boundary zero is hidden by a factorization.

The right product/kernel exponent is at most
-(20/9-11/5)*n/50=-n/2250. The left and horizontal exponents
are respectively 1-9n/1000 and 1-n/100, as stated. Using exp(1)<3,
all three bounds are at most 30n*exp(-n/3000). The full perimeter
is 4Y+2(b+c)<2 and 2pi>6. Thus the integral error is at most
10n*exp(-n/3000), with all four finite sides charged. This verifies
(1); no cancellation among these error integrals is assumed.

**Positive main term, spatial mean and original D.** Since d+rho<R,
every factor of W_(d+rho)(0) is positive. Integrating the just-checked
bound for g_n over [d,d+rho] gives log F(-rho)>=-297/500.
The exact integral for log 2 in Section 4 is strictly greater than
2/3>297/500, proving (2). Conjugation of the original node pairs
makes c_0(-1) real. The error 10n*exp(-n/3000) tends to zero,
so the asserted lower bound for c_0 follows beyond an absolute onset;
no positivity at every n>=300 is inferred from the finite-n error.

For fixed u=-1 and |zeta|<=1, the spatial denominator modulus is
at least 1-r*|a|/R>31/32. The finite sum is therefore analytic on
a neighborhood of that disk. DLMF (1.10.7) identifies its constant
coefficient with its normalized circle mean; the triangle inequality
then gives V_r>=|c_0(-1)|. No infinite-family limit is interchanged.

L661's general envelope allows this exact family, with
sum_a r_a^2=M=n/3 and U-|a|^2>=137/5000. It yields precisely the
displayed bound for D. Also D>0, since W_x(u)=1 and its anchor term
is 1/(U-d^2). Dividing the lower bound for V by the proposed target
therefore gives exactly the stated constant times
n^(-3/2)*exp(79n/30000): 1/48-91/5000=79/30000>0.
The polynomial factor cannot prevent divergence. This proves (3)--(4)
after one common absolute onset, with no claim of an effective onset.

No load-bearing defect was found. The result is now an audited local
subfamily input. The full independent-displacement cube, L683's
conditional transfer audit, its inherited L657/L658 qualifications,
H/support and actual-Xi realization/signs remain unresolved here.

## Mathlib

Full matching coverage for this Robin logarithmic-derivative estimate,
its explicit edge constants and the original-D specialization has not
been checked. No absence claim or formal verification is made.
The supporting mathematics is the residue theorem, Cauchy mean formula,
elementary hyperbolic identities and finite product estimates. The
saved Mathlib Mahler-measure coverage in L664 is not needed for (1)--(4)
and does not supply the unresolved full-cube norm estimate.
