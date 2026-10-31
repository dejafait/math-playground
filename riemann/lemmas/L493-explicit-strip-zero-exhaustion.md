# L493 — Explicit exhaustion of high strip zeros into phase disks

## Hypotheses

Use the exact H_t, M_t=exp(ell_t), and fixed holomorphic logarithm
ell_t of L490–L492, with the normalization of D. H. J. Polymath,
*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn–Newman constant*,
Research in the Mathematical Sciences **6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
equations (4),(6)–(11),(16). In particular H_t is entire and, for
real t, H_t(conj(z))=conj(H_t(z)), as stated after source (4).

For real u>4*pi put

    X_0=4*pi*exp(10000),
    L_u=log(u/(4*pi)),
    g(u,t)=(u/(4*pi))*L_u-u/(4*pi)+11/8+(t/16)*L_u.

Assume

    1/25<=t<=11/50,       z=x+iy,
    x>=X_0+3,            |y|<=1,            H_t(z)=0.

The strip condition is an explicit hypothesis. Use the audited local
quantitative estimates L490, L491 and disk count L492. The source
Theorem 1.3 and Proposition 6.6(ii) saddle estimates retained by L490
are imported, and their proofs remain independently unaudited locally.
No RH, reality or simplicity hypothesis is assumed.

## Conclusion

There is a real X with

    X>x-1>=X_0+2,       |X-x|<1,       g(X,t) in Z,
    |z-X| < 1/(125*L_X) < 1/L_X.

Thus every zero in the stated closed strip/time/height range lies
strictly in an allowed L492 disk. By L492 it is real and simple.

This explicit numerical specialization of the known exhaustion method
is not a new zero-localization mechanism. Its first separate critical
application audit passed on 2026-10-30, as recorded below. It does not
establish a global strip theorem, finite
collision exclusion, smaller-positive-time coverage or zero-time
control. In particular it does not prove RH.

## Proof

### Source comparison and the numerical difference

Source Theorem 1.5(i), pp.9–10, and the separate exhaustion argument
on p.60 following (102)–(104) localize arbitrary sufficiently high zeros
to the phase centers. Their constants are unnamed. L488 replays that
qualitative argument but gives no numerical cutoff usable here. These
are comparisons, not additional mathematical premises of this proof.
The necessary difference is the explicit edge, center existence and
strict disk inclusion from L490–L492. We obtain those with a local
logarithm at the zero and elementary real inversion of the exact g.
Neither source (76) nor an unspecified asymptotic constant is used.

### A fixed logarithm and one integer at an arbitrary zero

If y<0, replace z by conj(z). This remains a zero, has the same x
and |y|, and its distance to any real X is unchanged. It therefore
suffices to work with 0<=y<=1 and transfer the resulting disk inclusion
back by conjugation. The case y=0 is included directly.

For this zero define

    A(z)=M_t((1+iz)/2),       B(z)=M_t((1-iz)/2),
    G(z)=ell_t((1+iz)/2)-ell_t((1-iz)/2).

The two affine arguments are respectively (1-y)/2+i*x/2 and
(1+y)/2-i*x/2. Their imaginary parts are nonzero, so both avoid the
cut (-infinity,1] of the specified logarithms. Thus A and B are
nonzero, and A/B=exp(G) exactly, as in L492's normalization.
For y>=0 this B is L490's B_t, and A/B is its gamma. These explicit
arguments avoid the opposite s_+ naming conventions in L490 and L491.

Let d=153/10^6 and eta=5010/10^12. L490 applies because
x>=X_0+3>X_0 and the closed t and y ranges are satisfied. At our zero,

    |1+exp(G(z))| < d.                                  (1)

Put h=-exp(G(z)) and v=Log(h), using the principal logarithm only
for this value in the disk |h-1|<d<1. This disk lies in Re(h)>0.
The convergent logarithm series at 1 gives exp(v)=h and

    |v| <= sum_(k>=1) |h-1|^k/k
         <= |h-1|/(1-|h-1|) < d/(1-d).                  (2)

This does not identify G with a principal logarithm of exp(G).
Instead exp(G-v)=-1, so the elementary complex exponential identity
gives a unique n in Z with

    G(z)=i*(2*pi*n-pi)+v.                               (3)

Indeed an exponential equal to -1 has real exponent part zero and
imaginary part an odd multiple of pi; the form 2*pi*n-pi lists each
such value once. This retains the full integer branch information.

Apply L491 with its real center equal to x, and w=iy. Its center
hypothesis holds since x>=X_0+3>X_0+2, and |w|=y<=1. In particular
this application does not presume membership in a disk about the
as-yet unselected X. Its fixed-branch estimate is

    G(z)=i*(2*pi*g(x,t)-pi)-(L_x/2)*y+epsilon,
    |epsilon|<eta.                                     (4)

Subtract (3) from (4). With q=1/1000, equations (2)–(4) give

    |i*2*pi*(g(x,t)-n)-(L_x/2)*y|
        =|v-epsilon| < d/(1-d)+eta < q.                (5)

The last comparison is elementary and uniform: d<1/4000 and d<1/2
give d/(1-d)<2*d<1/2000, while eta<1/2000; their sum is <1/1000.
Real and imaginary parts of (5) separately give

    |g(x,t)-n| < q/(2*pi) < 1,
    |y| < 2*q/L_x.                                    (6)

All logarithms L here are positive. No division by H_t or by its
cancelling two-term model has occurred.

### Existence and lower edge of the integer-phase center

Set m=L_(x-1). Since x-1>=X_0+2>X_0, we have m>10000.
On the entire closed interval [x-1,x+1], direct differentiation gives

    partial_u g(u,t)=L_u/(4*pi)+t/(16*u)
                    >=m/(4*pi)>625.                 (7)

The last inequality uses pi<4 and m>10000. Every u in this interval
is positive, and t>0, so the displayed lower bound holds at both
time endpoints. Integration over the two unit intervals yields

    g(x,t)-g(x-1,t)>625,
    g(x+1,t)-g(x,t)>625.

Together with (6), this places n strictly between g(x-1,t) and
g(x+1,t). The intermediate value theorem and strict monotonicity
give exactly one X in (x-1,x+1) with g(X,t)=n. In particular

    X>x-1>=X_0+2,                                    (8)

which is the required center onset even when x=X_0+3. The same
derivative lower bound between x and X gives

    |x-X| <= (4*pi/m)*|g(x,t)-g(X,t)| < 2*q/m.        (9)

The first inequality also holds when x=X, without division by x-X.
No rounding of a sampled phase or numerical search for X is used.

### Comparing logarithmic scales and strict disk inclusion

Since X in (x-1,x+1) and x-1>2, the elementary real bound
log(1+a)<=a for a>=0 gives

    L_X < log((x+1)/(4*pi))
        = m+log(1+2/(x-1))
        <= m+2/(x-1) < m+1 < 2*m.

Also L_x>=m>0. Consequently both ratios satisfy

    L_X/m < 2,       L_X/L_x < 2.                    (10)

The triangle inequality, (6), (9) and (10) now prove

    L_X*|z-X|
      <= L_X*(|x-X|+|y|)
       < 2*q*(L_X/m)+2*q*(L_X/L_x)
       < 8*q = 1/125 < 1.                          (11)

This proves the stronger stated inclusion and hence the exact target
radius. It avoids applying L491 at X before its unit-disk domain has
been verified. For the original lower-half zero, conjugation preserves
the same strict inequality and real center X.

Finally (8), g(X,t)=n in Z and the unchanged closed time band meet
every hypothesis of L492. The zero z is strictly inside its disk,
whose total multiplicity is one and whose unique zero is real.
Therefore z is real and simple. L492's count is applied after the
inclusion and is not a premise used to obtain it.

All estimates are uniform for arbitrarily large x, with the constants
d, eta and q independent of x,t,y. They include both time endpoints,
the spatial endpoint and |y|=1; in the last case (6) rules out a zero.
No limit, floor-dependent holomorphic approximation, finite-height
sampling or unspecified error constant is used. Only the proposed
one-unit padding is used to pass from the zero's edge X_0+3 to the
center's required edge X_0+2. The result does not supply a strip
theorem outside the explicit hypothesis |y|<=1.

### Separate critical application audit, 2026-10-30

The full closed-domain statement passes independent replay without
repair. This verifies the numerical specialization of the known
exhaustion method, not the imported saddle proofs or a new mechanism.
The exact source comparison is the cited v2 Theorem 1.5(i), Lemma 9.2
and the exhaustion case following (104), pp.58–60. The previously
inspected source evidence is reused; no new manuscript verification is
claimed. The mathematical premises used here are precisely the audited
quantitative conclusions of L490, L491 and L492.

First, reflection is applied to the zero itself. For real t, conjugation
preserves H_t's zeros and their distances to any real center. Thus
reducing to 0<=y<=1 does not require a reflected B-normalized residual.
Both affine arguments have nonzero imaginary part because x>0. They
therefore belong to the fixed-log domain even at y=0 and y=1, and
M_t=exp(ell_t) never vanishes there. The denominator B=M_t((1-iz)/2)
is exactly L490's B_t, and its ratio gamma is A/B=exp(G), not B/A.
At a zero, L490 gives (1) by division only by this nonzero B.

For the branch step, h=-exp(G) satisfies |h-1|<d<1, so Re(h)>0
and its principal logarithm v is defined with exp(v)=h. The absolutely
convergent series at 1 yields |v|<d/(1-d). Consequently
exp(G-v)=exp(G)/h=-1. If G-v=a+ib with a,b real, its modulus forces
a=0 and its phase forces b=(2n-1)*pi for one and only one integer n.
This proves (3) for the fixed G itself; no principal-value reduction
of G is made. Only the value v at this zero is needed, so no global
logarithm of a function with zeros is being asserted.

Next, x>=X_0+3 meets L491's real-center onset, and w=iy belongs to
its closed unit disk. Substitution into (i/2)*L_x*w gives -L_x*y/2,
with the sign and normalization in (4). The resulting complex equality
in (5) controls both its real and imaginary parts. Its margin can be
checked independently using exact rationals:

    d<1/2,
    d/(1-d)+eta < 2*d+eta
                 =306005010/10^12 < 1/1000=q.

It follows that |g(x,t)-n|<q/(2*pi)<1 and y<2*q/L_x.
Here L_x>10000 is positive. No prospective phase center or reality
conclusion was used to justify this initial L491 application.

For center existence, differentiating the stated g gives exactly
g_u=L_u/(4*pi)+t/(16*u). On [x-1,x+1], u>0, t>=1/25 and
L_u>=m=L_(x-1)>10000. Since pi<4, g_u>625 throughout that
closed interval. Thus the changes from x-1 to x and from x to x+1
both exceed 625. The integer n, whose discrepancy from g(x,t) is
less than 1, lies strictly between the endpoint values. Continuity
and strict monotonicity give a unique center in (x-1,x+1).
In particular X>x-1>=X_0+2, including when x=X_0+3. Integrating
g_u>=m/(4*pi) between x and X gives
|x-X|<=4*pi*|g(x,t)-n|/m<2*q/m; the case X=x is included.

For the final scale comparison, x-1>2 and X<x+1 imply

    0<L_X<m+log(1+2/(x-1))<=m+2/(x-1)<m+1<2*m,
    L_x>=m>0.

Hence L_X/m<2 and L_X/L_x<2, with strictness valid at the height
edge and for every larger real x. The Euclidean distance satisfies
|z-X|<=|x-X|+|y|, so the two independently established displacement
bounds give L_X*|z-X|<8*q=1/125<1. This checks the stronger
advertised radius, not merely the weaker inclusion needed by L492.
For a lower-half zero, conjugation preserves that same distance.

Only now are all L492 hypotheses invoked: real t in the same closed
band, real X above its required onset, g(X,t)=n in Z, and strict
membership in its open disk. Its total multiplicity-one count and
reality conclusion make this particular zero real and simple. This
is neither an assumption in the branch inversion nor a circular use
of exhaustion. L492 itself is reused, not re-audited here.

Both t endpoints are admitted throughout. The real edge y=0 requires
no limiting argument, while y=1 would contradict y<2*q/L_x and thus
cannot be a zero; reflection covers y=-1. The spatial equality case
retains the strict center padding. The bounds are analytic inequalities
for all unbounded x, not samples, and there is no interchange of limits
or sums involving H_t. No statement or direct mathematical input has
changed. Global strip transfer, finite collisions, smaller times and
zero-time control remain outside this audited conclusion. Full matching
Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this explicit numerical exhaustion result
has not been checked. No absence claim or formal verification is made.
Supporting formalizations of the local complex logarithm, exponential
periodicity, intermediate value theorem and derivative monotonicity
have not been looked up in this step. The proof uses the already
documented quantitative inputs and gives the elementary specialization
in full; no Mathlib citation replaces the imported saddle estimates.
