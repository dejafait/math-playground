# Lemma 691: two independently shifted halves have bounded complete logarithmic loss

## Hypotheses

Use L666's exact family, with

    q>=1 integer, n=12q+3, M=4q+1=n/3, h=27/(10n),
    x=-d=-5/4, R=11/8, U=121/64, t_j=j/n (0<=j<n).

Choose two independent real numbers alpha,beta in [-1/8,1/8],
possibly depending on n, and specialize only the displacement vector:

    e_m=alpha for 0<=m<2q,
    e_m=beta  for -2q<=m<0,
    Z={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q}.

The anchor is fixed and every original residue is one. Keep one pole
set at all angles, all spatial moments, the j=0 factor and angle 1/u:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_(a in Z) W_a(u)*(a/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)*zeta^k,
    A_n(alpha,beta)=mean_(|u|=|zeta|=1) log|G(u,zeta)|.

Both circle measures are normalized. Use L657's complete K,Q,m_0,
Z_n,P_n. Here Z_n denotes its angular zero charge, not the pole set.
The original diagonal, when mentioned as downstream context, is
mean_u sum_a |W_a(u)|^2/(U-|a|^2).

## Conclusion

There are absolute finite constants C_0,C_1,C_2 and an absolute onset
N, independent of alpha,beta, such that for every admissible n>=N,

    A_n(alpha,beta)>=-C_0,
    A_n(alpha,beta)>=A_n(0,0)-C_1,                         (1)
    Z_n(alpha,beta)>=Z_n(0,0)-C_2.                        (2)

The same constants hold simultaneously at every point of the straight
homotopy (alpha,beta) -> (t*alpha,t*beta), 0<=t<=1. In particular the
approved loss n/100+C log n is paid on this two-parameter subfamily.
The constants/onset are existential, not numerically effective here.

This includes outward pairs alpha=1/8,beta=-1/8, for which L665's
specified absolute kernel-transfer cost is exponentially excessive.
There is no contradiction: (1) is a complete logarithmic lower bound,
not an o(1) inherited-anchor approximation. Common shifts are already
covered by L690; independently moving the two halves is the extension.

The full cube, in which shifts can vary within either half, is not
controlled. The argument does not assume the response is pointwise
nonzero on the angular or product torus. It does not prove the main
homotopy target on that cube, H/support transfer, actual-Xi realization
or mixed signs. Section 8 separately audits this local partial result under the prior
SPECIALIZE assessment. It is not certified originality or an RH candidate.

## Proof

### 1. Source scope, previous stops and exact imports

The invocation-start assessment
`drafts/literature/2026-11-03-independent-shift-mahler-homotopy.md`
approves the complete logarithmic-loss target, including useful partial
complete-charge estimates inside L666's cube. Its singular-log and
failure comparisons are reused, not refreshed by another search.
L665's outward-pair absolute-cost stop, L666's scalar signed-energy
stop, and L670/L671's complete clearing costs do not bound the actual
mean in (1). L664 has complementary offsets on each positive half;
it does not supply the present independent two-half statement. L684
and L686 control other, sparse-support norms, not this complete mean.
These are contrasts, not mathematical premises of (1).

The quantitative contour inputs below are the audited statements in
L690 Sections 2–4, including its pointwise bound (6), finite-product
bound (11), moving sides and kernel estimates. Its unperturbed mean
in (2) supplies the comparison with A_n(0,0). L666 supplies family
admissibility. L657 supplies the full logarithmic accounting and its
integrability/nonzero-slice conclusions. No unchanged certificate or
source manuscript is claimed to have been independently replayed here.

Use the residue theorem and contour inequality as already inspected:
J. H. Mathews and R. W. Howell, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18–6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
For the local zero-factor argument use the analytic form of Rouché's
theorem in [NIST DLMF 1.10(iv)](https://dlmf.nist.gov/1.10#iv), already
inspected in the reused full-circle assessment. It requires strict
comparison on the selected auxiliary contours; that is verified below.
The one-root mean, including unit-circle roots, is F. Brunault and
W. Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, pp.6–7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
The standard identity theorem, open mapping theorem and maximum modulus
principle are used with the connected domains specified below.

No general Jensen, residue or Rouché theorem is reproved. The annular
limit and its logarithmic specialization are written out because the
degrees grow with n and the limiting functions may have circle zeros;
fixed-degree coefficient continuity alone would not justify this use.

### 2. A fixed complex angular annulus and the outer contour

Put

    eps=1/100000, e_0=117/100, b=2/25, c=1/8,
    Omega=20*pi/27, Y_n=2q*h=9/20-27/(20n),
    U_ann={u: 1-eps<|u|<1+eps}.

Let Gamma_n be the positive boundary of [-Y_n,Y_n]+i[-b,c]
in the y-plane. On its entire closed rectangle, a=x+i*y satisfies

    Re a<=-e_0, |a|<29/20<U, |a|>=e_0.

Every W_a is holomorphic and nonzero there and on the closed angular
annulus. Indeed |a|>|t_j*u| and |U*u|>|t_j*a|; the anchor factors have
the same clearances. All following contour applications are finite.

The rational continuation, with j=0 already separated, is

    W_a(u)=(x/a)*product_(1<=j<n)
                  [(x-t_j*u)/(a-t_j*u)]
                  [(U*u-t_j*a)/(U*u-t_j*x)].              (3)

Its logarithmic u-derivative, interpreted as a quotient rather than
as a chosen global logarithm, has modulus at most 20n. Explicitly the
per-factor upper bound is

    1/(d-1-eps)+1/(e_0-1-eps)
      +U/[U*(1-eps)-29/20]+U/[U*(1-eps)-d] < 20.          (4)

Radial integration from u/|u| therefore changes log|W_a| by at most
20n*eps=n/5000. L690's complete outer-contour estimate, discarding
only its nonnegative spatial cost beta(a), gives on Gamma_n

    |W_a(u)|*exp(-Omega*n*(-Im y)_+)
                 <=exp(43/2-9*n/5000).                  (5)

Here 43/2=8+27/2 includes its finite left-sum error and moving-side
cost. The angular radial charge is paid in 1/500-1/5000=9/5000.

For gamma in [-1/8,1/8] define L690's kernel

    K_(gamma,n)(y)=-i*Omega*n/
                      [1+exp(i*Omega*n*y-2*pi*i*gamma)].  (6)

Its simple poles are exactly h*(m+1/2+gamma), of residue one.
No such pole lies on Gamma_n or on its central vertical segment.
The outer horizontal/vertical estimates in L690 give

    |K_(gamma,n)(y)|<=2*Omega*n*
                           exp(-Omega*n*(-Im y)_+).       (7)

The total rectangle length is at most 221/100. From (5)–(7), the
common-beta zeroth response is

    c_(n;beta,beta)(u)=1/R+O(n*exp(-9*n/5000)),            (8)

uniformly on the closed annulus and in beta. The absolute O constant
includes exp(43/2); it does not depend on n or the parameters. This
is the c_0 contour formula, so no spatial truncation is used in (8).

### 3. Split contour, central orientation and a uniform dominating bound

Use the right half-rectangle [0,Y_n]+i[-b,c]. Its kernels (6) have
exactly the positive-ordinate nodes m=0,...,2q-1 inside. The first
node is at least 3h/8 from zero and the last is at least 3h/8 from
Y_n. Subtracting the common-beta formula thus gives exactly

    c_(n;alpha,beta)-c_(n;beta,beta)
      =(1/(2*pi*i*R))*integral_(right rectangle)
                       W_(x+i*y)*(K_(alpha,n)-K_(beta,n))dy. (9)

The three outer edges contribute O(n*exp(-9*n/5000)) by (5)–(7).
The central edge is directed from i*c down to -i*b. Define

    A_gamma(s)=1/[1+exp(-Omega*s-2*pi*i*gamma)],
    Delta A(s)=A_alpha(s)-A_beta(s).

With s=n*Im y, the central contribution, including its orientation,
is

    (i*Omega/(2*pi*R))*integral_(-bn)^(cn)
                               W_(x-s/n)(u)*Delta A(s) ds. (10)

For r>0 and |gamma|<=1/8, |1+r*exp(-2*pi*i*gamma)|>=max(1,r).
Consequently

    |Delta A(s)|<=2*exp(-Omega*|s|).                     (11)

We next bound W on this entire central edge, not just at fixed s.
For real a=-e, e_0<=e<=R, and |u|=1, the single-factor modulus in
(3), including t=0 in the unsplit product, is

    |(d+t*u)/(e+t*u)|*|(U*u+t*e)/(U*u+t*d)|.

When e<d each logarithmic ratio is decreasing in Re u; when e>d
each is increasing. For t>0 the first ratio's derivative sign is that
of (d-e)*(t^2-d*e), and for the second that of
(e-d)*(U^2-t^2*d*e). The denominators are positive; at t=0 there
is no angular dependence. Thus for e<d
the product is maximal at u=-1, and for e>d it is maximal at u=1.
At u=1 the product is at most one, since

    (d+t)*(U+t*e)-(e+t)*(U+t*d)=(d-e)*(U-t^2)<=0.

It follows that |W_(x-v)(u)|<=1 for 0<=v<=c on the unit circle.

For the lower part write e=d-w, 0<=w<=b. At u=-1 the logarithm
of a single factor is

    f_t(w)=log[(d-t)/(d-w-t)]
                       +log[(U-t*d+t*w)/(U-t*d)].

It vanishes at zero and is convex: its second derivative is
1/(d-w-t)^2-t^2/(U-t*d+t*w)^2>=0, because
U>2*t*(d-w)-t^2 (the latter is at most 2d-1=3/2).
Hence log W_(x+w)(-1)<= (w/b)*log W_(x+b)(-1).
At y=-i*b, L690's fixed-boundary bound (6) and finite-product
bound (11), with zero spatial cost, give

    log W_(x+b)(-1)<=n*(Omega*b-1/500)+8.

Using 500b=40 and the angular maximum just proved yields

    |W_(x+w)(u)|*exp(-Omega*n*w)
                             <=exp(8-n*w/40), |u|=1.    (12)

To extend these central estimates radially without an unscaled
exp(O(n)) error, differentiate (3) also in a. On this real a-segment
the mixed logarithmic derivative has modulus at most 50n, since

    1/(e_0-1-eps)^2+U/[U*(1-eps)-R]^2 < 50.             (13)

The u-derivative of log W_x is zero. Integrating the mixed derivative
from x to x-v and then radially in u adds at most
50n*eps*|v|=n*|v|/2000 to log|W|. Combining (11)–(13), on the
closed annulus and throughout the interval in (10), gives the
integrable bound

    |W_(x-s/n)(u)*Delta A(s)|
                       <=2*exp(8)*exp(-|s|/50).         (14)

For s<0 use 1/40-1/2000=49/2000>1/50. For s>=0 use
Omega-1/2000>2, which follows already from pi>3. Thus all long
central tails and both ends of the moving contour are paid.

### 4. Uniform analytic limit and why it is not identically zero

Define the holomorphic function on U_ann

    g(u)=-integral_0^1 [1/(x-t*u)+t/(U*u-t*x)]dt.         (15)

For fixed bounded real s, integrate the a-logarithmic derivative
starting at W_x=1. The same clearances as above give uniformly in u

    log W_(x-s/n)(u)=-s*g_n(u)+O(s^2/n),
    g_n(u)=-(1/n)*sum_(0<=j<n)
                 [1/(x-t_j*u)+t_j/(U*u-t_j*x)].

Here a local logarithm is defined by that integral along the small
a-segment. Ordinary uniform Riemann sums give g_n->g. In particular

    W_(x-s/n)(u)->exp(-g(u)*s)                           (16)

uniformly on bounded s-intervals and the closed annulus. No angular
response logarithm has been differentiated.

The pre-kernel bounds leading to (14), applied to any fixed positive
or negative s and then to arbitrarily large such s after n->infinity,
also give

    -1/2000<=Re g(u)<=Omega-49/2000.                    (17)

For example (12) after the radial charge gives
exp(Re g(u)*r)<=exp(8+(Omega-49/2000)*r) for every r>0;
letting r grow proves the upper inequality. The upper central edge
gives the lower inequality. Thus the image lies strictly inside
the connected strip S={z: -Omega<Re z<Omega}.

For z in S put

    F_(alpha,beta)(z)=1+(i*Omega/(2*pi))*integral_R
                                  exp(-z*s)*Delta A(s)ds. (18)

Estimate (11) makes this holomorphic on S and jointly continuous in
the compact parameter square, locally uniformly in z. All complex
z-derivatives on a compact substrip are justified by the same bound
with a fixed power of |s|. Uniform convergence in (16) and the uniform
tail (14), together with (8)–(10), prove

    c_(n;alpha,beta)(u)->F_(alpha,beta)(g(u))/R            (19)

uniformly on the closed annulus and the whole parameter square.

At z=0 the integral is explicit without choosing a root branch.
The primitive of A_gamma(s) is
Omega^(-1)*Log(exp(Omega*s)+exp(-2*pi*i*gamma)). The argument
has positive real part, so the principal Log is valid throughout.
Subtract the two primitives. Their difference tends to zero at
+infinity and to -2*pi*i*(alpha-beta)/Omega at -infinity. Hence

    F_(alpha,beta)(0)=1-alpha+beta>=3/4.                 (20)

Also g is nonconstant. Directly from (15),

    g(-1)=integral_0^1 [1/(d-t)+t/(U-t*d)]dt,
    g(1)=integral_0^1 [1/(d+t)-t/(U+t*d)]dt,

and the first exceeds the second strictly, term by term for t>0.
The annulus is connected. By the open mapping and identity theorems,
F_(alpha,beta)(g(u)) cannot vanish identically there: otherwise F
would vanish on an open subset of S and then at zero, contradicting
(20). This assertion is for every parameter pair, including limits
of varying pairs. It permits isolated angular zeros.

### 5. Passing to logarithmic means, including circle zeros

We spell out the needed specialization of the root formula. Suppose
holomorphic functions f_l on a neighborhood of a fixed closed annulus
converge locally uniformly to f, and f is not identically zero there.
Then

    mean_(|u|=1) log|f_l(u)| -> mean_(|u|=1) log|f(u)|.  (21)

To see this, choose a smaller closed annulus containing the circle
whose two boundary circles avoid zeros of f. There are only finitely
many zeros of f in it. Surround them by disjoint small disks inside
the original annulus, with f nonzero on their boundaries. Outside
these disks f has a positive minimum in modulus on the smaller
annulus. Uniform convergence prevents other zeros there and gives
|f_l-f|<|f| on every disk boundary for all large l. Rouché's theorem
therefore gives the exact same numbers of zeros, with multiplicity,
in the disks. Shrinking disks shows that these roots converge in
multisets to the roots of f.

Let p_l,p be the monic polynomials of these roots, including every
root in the disks. They converge coefficientwise. The quotients
h_l=f_l/p_l and h=f/p are holomorphic and zero-free on a neighborhood
of the unit circle. Away from the disks, their convergence is uniform.
On each disk boundary it is uniform too, and the maximum modulus
principle applied to h_l-h extends it across the disk. Thus h_l->h
uniformly near the circle and their log moduli converge uniformly
there, since h is bounded away from zero. Finally the cited one-root
formula gives

    mean log|p_l(u)|=sum_(roots r of p_l) log max(1,|r|).

This expression is continuous in the roots even at |r|=1. Adding
the zero-free quotient means proves (21), with multiplicities and
crossings intact. Only the auxiliary disk boundaries avoid zeros;
the unit circle is never assumed zero-free. Possible degree growth
outside the annulus is irrelevant to this local factorization.

Apply this argument on a slightly smaller annulus than U_ann to
(19). It is uniform over the parameter square in the following exact
sense. From any sequence of parameter pairs take a convergent
subsequence. Joint continuity in (18) and uniform convergence (19)
make the corresponding c_n converge holomorphically near the circle
to the nonidentically-zero limiting composition for that limiting
pair. Equation (21) then applies to that sequence. The same reasoning
applied just to the limiting compositions shows that their circle
logarithmic means are continuous on the compact parameter square.
They therefore have a finite minimum, and a contradiction-sequence
argument with (21) gives constants C_0,N such that

    mean_(|u|=1) log|c_(n;alpha,beta)(u)|>=-C_0          (22)

uniformly for all n>=N. The proof gives existence, not an effective
minimum or onset. Nonzero limiting compositions also ensure that
these c_n are not identically zero for all sufficiently large n.

### 6. All spatial moments and the complete angular charge

For every fixed unit u, L657's full spatial root formula gives

    mean_(|zeta|=1) log|G(u,zeta)|>=log|c_0(u)|.          (23)

This keeps the whole polynomial: every spatial root's nonnegative
Jensen contribution is included in the inequality. At isolated zeros
of c_0 the right side is -infinity and (23) still holds. Its angular
logarithm is integrable, since c_0 is a nonzero rational function
with no poles on that circle. L657 supplies absolute product-log
integrability and the nonzero spatial slices, so integrating (23)
is justified. Equation (22) proves the first inequality of (1).

L690 gives A_n(0,0)=-log R+o(1), with a uniform absolute bound on
the error after its stated onset. Enlarging C_1,N proves the second
inequality of (1). Every pair (t*alpha,t*beta) lies in the same compact
square; no path derivative is needed for the simultaneous assertion.

Finally L657 applies at every point of this admissible homotopy:

    A_n=m_0+Z_n-P_n,
    log[M*d^2/(R*(R-1/100)^2)]<=m_0
                                <=log[M/(R*(1-273/275))].

The complete interior denominator charge P_n depends only on n,x,R,
not on the two shifts. Thus the difference of the m_0 values is at
most

    C_m=log[(R-1/100)^2/(d^2*(1-273/275))],

an absolute constant. Subtracting the two exact charge identities
proves (2) with C_2=C_1+C_m. Cancelled factors, zero multiplicities,
angular degree drops and the exceptional center-zero spatial slices
are handled exactly as in L657. No numerator zero has been discarded
from Z_n. The complete response, rather than an unweighted zero count,
has been controlled on this subfamily.

The full-cube target remains open. This proof has only one interface,
at ordinate zero. Arbitrarily varying shifts cannot be represented by
this single decaying kernel difference; (14), (19) and (20) have not
been established for them. L661's general diagonal envelope explains
the downstream relevance of (1), but is not a premise of this lemma.

### 7. Verification and qualifications

The elementary rational clearance comparisons in (4), (13), the
radial/central decay charges and convexity margin are checked by

    python3 scripts/one-sided-hankel/two-half-logarithmic-98.py

The full exact-rational certificate is
`scripts/one-sided-hankel/two-half-logarithmic-98.json`. It verifies
only those inequalities, not analytic convergence, the inherited L690
certificate, a numerical onset, a root screen or an independent audit.
The proof above carries the contour, limit and singular-log reasoning.

### 8. Separate conceptual audit — 3 November 2026, step 100

This audit accepts (1)–(2) with their stated two-half hypotheses and
existential absolute constants/onset. It uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-11-03-two-half-logarithmic-audit-scope.md`, whose
TARGET exactly matches the completed audit. The inspected standard
sources in Section 1 are reused. This is verification of the existing
family-specific specialization, not another source import, a new bound,
or a claim of originality. No essential dependency or bound changes.
The following details make the limit and zero-factor checks explicit.

**Domains, census and orientation.** The radial segments from the unit
circle have length at most eps and stay in the closed annulus. The
strict clearances in (4) hold on a neighborhood of that closed set;
for every complex y in the rectangle, Re(x+i*y)<=-e_0 and
|x+i*y|<29/20. Both numerator and denominator factors in (3) therefore
remain nonzero, not just on its boundary. The angular derivative bound
17.1251298582<20 pays n/5000 on the outer contour. The inherited
L690 -1/500 fixed-boundary estimate, left-sum error 8 and moving-side
cost 27/2 then give (5); dropping beta(a)>=0 is in the safe direction.
This audit reuses L690's separately audited interval evidence, rather
than claiming another independent backend replay.

Since Omega*n*h=2*pi, every kernel pole is real, simple and of residue
one. The right half contains precisely m=0,...,2q-1 for either parameter;
the first and last clearances are >=3h/8, including parameter endpoints
and q=1. The central line has no kernel pole, because at Re y=0 its
denominator has real part 1+r*cos(2*pi*gamma)>0. The contour in (9)
is positively oriented. Parameterizing its central side by y=i*s/n,
with s descending from cn to -bn, gives
K_alpha-K_beta=-i*Omega*n*Delta A and dy=i*ds/n. Multiplication
by 1/(2*pi*i*R) and reversal of the integration limits give exactly
the positive i*Omega/(2*pi*R) in (10). All three remaining edges
are subsets of the already bounded outer contour. The fixed anchor
cancels in the difference and remains the 1/R in (8).

**Entire central segment and radial error.** On the unit circle the
squared-modulus ratios depend only on Re u. Their derivative signs
are those displayed in Section 3: d*e>t^2 and U^2>t^2*d*e over the
entire real a-segment. They put the maximum at -1 for e<d and at
+1 for e>d. At +1 the difference of the numerator and denominator
products is (d-e)*(U-t^2)<=0, including t=0; hence W<=1 on the
upper central segment. On the lower segment f_t(0)=0 and

    f_t''(w)=1/(d-w-t)^2-t^2/(U-t*d+t*w)^2>=0.

The denominators are positive; U-[2*t*(d-w)-t^2]>=25/64>0
for 0<=t<=1 and 0<=w<=b. Convexity gives the endpoint chord
bound, and L690 evaluated at a=x+b,u=-1 gives
log|W|<=n*(Omega-1/40)*w+8*w/b. Replacing 8*w/b by 8
is legitimate throughout 0<=w<=b and proves (12).

The exact mixed derivative per nonzero factor in (3) is
-t/(a-t*u)^2+U*t/(U*u-t*a)^2. Its absolute sum is bounded by
the quantity in (13), whose rational value is <41.7177799376*n<50*n.
At a=x the full u-logarithmic derivative vanishes, because W_x=1.
Integrating first along the real a-segment and then along the radial
u-segment costs at most n*|v|/2000; a global logarithm is unnecessary
for integrating its real logarithmic derivative. Multiplication by
(11) leaves lower-tail decay 1/40-1/2000=49/2000>1/50.
The upper-tail decay is Omega-1/2000>2. Thus (14) dominates the
whole expanding interval, uniformly in n,u,alpha,beta. No estimate
only at fixed s has been substituted for a moving-tail estimate.

**Uniform limit and nonidentity.** For |s|<=L fixed, the a-derivative
at x is n*g_n, with the sign in Section 4. Its next a-derivative
is a sum of 1/(a-t*u)^2-t^2/(U*u-t*a)^2, bounded by C*n on
the central segment and closed annulus by the same strict clearances.
Taylor's remainder is therefore O_L(1/n). The integrand defining
g_n has a uniformly bounded t-derivative there, so its left Riemann
sums converge uniformly to (15). This proves (16) uniformly for bounded
s, without differentiating log c_0 or a response logarithm.

For s>=0 the pre-kernel bound is |W|<=exp(s/2000). For s=-r<0
it is |W|<=exp(8+(Omega-49/2000)*r). Take n to infinity at each
fixed r, and only then let r increase without bound. These inequalities
give both sides of (17) on the whole closed annulus. They put g inside
the open strip of holomorphy of F with positive uniform margins.
Estimate (11) gives locally uniform convergence of the integral for F,
all z-derivatives and continuity in the parameter square. For (19),
first truncate s to [-L,L], use the uniform Riemann/Taylor limit there,
and then send L to infinity using (14) and the same limiting bound.
The outer-edge error tends uniformly to zero. This checks the order
of all limits and parameter uniformity; smaller closed annuli can be
used for locally uniform holomorphic convergence.

The principal-Log primitive in Section 4 stays in the right half-plane.
Its endpoint difference gives integral Delta A=2*pi*i*(alpha-beta)/Omega,
so F(0)=1-alpha+beta>=3/4, with the correct sign. At u=-1 and +1
the two real integrands in the displayed formulas for g differ
strictly on t>0. Hence g is nonconstant on the connected annulus.
Its image is open and lies in the connected strip S. If F composed
with g vanished identically, F would vanish on an open subset of S
and therefore at zero, a contradiction. This applies to every pair
in the closed parameter square, including subsequential limits. It
asserts no zero-free circle and no effective lower pointwise bound.

**Circle zeros and compact parameters.** In (21) use a connected
annular neighborhood of the unit circle. A nonzero holomorphic limit
has only finitely many zeros in a smaller closed annulus whose two
boundary circles are zero-free. Choose disjoint closed disks around
these zeros inside the original analytic domain, sufficiently small
that each boundary is zero-free and contains no additional limit zero.
The compact part of the smaller annulus outside the disk interiors
has positive minimum modulus. Uniform convergence excludes extra roots
there. Strict Rouche on each disk boundary fixes the multiplicity
inside; successively smaller disks prove root-multiset convergence.
Roots outside this selected region need not be bounded in degree.

Dividing by the monic products of these local roots gives holomorphic
quotients on all the disks, since the complete multiplicities have
been removed. On the disk boundaries and off the disks the quotients
converge uniformly. The maximum-modulus principle for their difference
extends convergence through each disk. The limiting quotient is
zero-free near the unit circle, so the log moduli of the quotients
converge uniformly there. The cited finite one-root formula contributes
sum log max(1,|root|) for the monic products; this is continuous even
at circle roots. Adding the two means proves (21). It neither assumes
boundary-root exclusion nor infers logarithmic convergence just from
uniform convergence of the original functions.

For any convergent parameter sequence, the limiting compositions
converge locally uniformly by the uniform strip margins and continuity
of F. They have a nonzero holomorphic limit by nonidentity, so (21)
makes their circle means continuous. Compactness of the parameter
square gives a finite minimum. If (22) failed uniformly for unbounded
admissible n, select violating parameter pairs and a convergent
subsequence. Uniform (19) and (21) give convergence to that finite
limit mean, a contradiction. Likewise, infinitely many identically
zero c_n along varying parameters would contradict (19) and nonidentity
on the same subsequence. This justifies a single absolute onset and
lower bound, without estimating either numerically.

**Spatial integration and every angular charge.** L666's radius and
positive-residue hypotheses hold for all pairs and their straight paths:
all ordinates are distinct, nonzero except for the anchor, and
|a|^2<353/200<(273/200)^2. Thus the L657 inputs already checked by
L690's audit apply. For a nonzero spatial polynomial, the complete
root formula implies mean log|G|>=log|c_0|, since each factor
max(1,|root|)>=|root|. When c_0=0 the inequality still holds with
right side -infinity. Above the established onset c_0 is a nonzero
rational function, has no circle poles, and has only finitely many
circle zeros, all with integrable logarithms. L657's nonzero spatial
slices and absolute product-log integrability justify Fubini and
integration of this inequality. No spatial moments are omitted in
this lower bound.

The common-shift comparison uses only L690's audited bounded error
for A_n(0,0)+log R beyond its onset; enlarging C_1 and N is sufficient.
For the zero-charge comparison, Q's interior roots are exactly
p_j=t_j*x/U; every A_b root b/t_j is outside. Hence P_n is unchanged
under either half shift, even if numerator factors cancel poles.
L657's two bounds for m_0 have the same M, so their difference is at
most the stated C_m; subtracting the exact identities gives
Z_n(alpha,beta)-Z_n(0,0)>=-C_1-C_m. All multiplicities, degree drops,
cancellations and the finite exceptional center-zero slices remain
in the original K/Q accounting. Compact-square uniformity includes
every t in the straight path, without a path derivative at torus zeros.

**Arithmetic replay and limits of this audit.** Ran the Section 7
producer and inspected all eleven full exact-rational check records,
not only a preview. All eleven comparisons passed with no failures:
the angular and mixed derivative bounds are <20 and <50; the outer
rate is 9/5000; the lower-tail rate is 49/2000>1/50; the upper-tail
rate exceeds 39991/18000>2 using pi>3; the convexity margin is 25/64;
all four recorded clearances are positive; and F(0)'s minimum is 3/4.
The complete evidence remains
`scripts/one-sided-hankel/two-half-logarithmic-98.json`.
The producer does not check the analytic arguments; those were audited
above. No independent interval backend, source-manuscript audit,
effective onset, full-cube estimate, support/H transfer or Xi/sign
conclusion is claimed. No new Mathlib coverage is asserted.

## Mathlib

The reused assessments record supporting univariate results in
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
notably `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.mahlerMeasure_mul`. They support the finite root means,
not the family-specific contour limit or its parameter uniformity.
Full matching coverage for (1)–(2), annular logarithmic convergence
and the split-contour specialization has not been checked. No absence
claim or formal verification is made.
