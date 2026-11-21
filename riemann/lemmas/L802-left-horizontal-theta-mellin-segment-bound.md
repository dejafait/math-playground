# Lemma 802: a standalone left horizontal theta-Mellin segment bound

## Hypotheses

Use L797's saddle and L798's phase and principal branches:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    c=9/4, F(z)=z(pi exp(2z)-c), F(x)=s, x=u+ih,
    q=pi exp(2x), Q=|q|=pi exp(2u), d=3/(16u),
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z),
    A=2F'(x)/x, B=|A|, theta=Arg A, a=exp(-i theta/2),
    C=sqrt(2pi/A)=a sqrt(2pi/B).

L797 gives u>3, |h|<pi/4-1/(4u), Re A>0 and pi exp(6)>1000,
including both closed boundaries of D. L798 gives S_s'(x)=0,
S_s''(x)=-A, (15/4)Q<B<5Q, |C|=sqrt(2pi/B)>0 and

    |S_s'''(z)|<10Q on |z-x|<=d,
    Re(S_s(x-da)-S_s(x))<-(85/48)Qd^2.

Use L799's normally convergent series on U={z: |Im z|<pi/4}:

    P(z)=sum_{n>=1} [4pi^2 n^4 exp(9z/2)
                    -6pi n^2 exp(5z/2)] exp(-pi n^2 exp(2z)),
    H(z)=4pi^2 exp(9z/2-pi exp(2z)), rho(z)=P(z)/H(z)-1.

Set z_L=x-da=v_L+i y_L. Define the finite observable

    T_L(s)=|integral_{u/2}^{v_L}
                  exp(2s Log(v+i y_L))P(v+i y_L) dv|
             / |4pi^2 exp(S_s(x)) C|.

The ordering and admissibility of the entire interval are proved below.
This is the exact standalone target in the unchanged SPECIALIZE
assessment `drafts/literature/2026-11-05-mellin-left-horizontal-segment-test.md`.
Its source comparison is bramble_trace, *A continuum certificate for
the decreasing Levy factor associated with Riemann xi*,
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section 3, Lemma 2, (10)–(14). That source prints a
combined horizontal allowance, not this split at u/2 or coefficient 9.
Neither its allowance nor its unread supplementary derivations is used.

The standard method is the left tangent envelope in Luc Devroye,
*Non-Uniform Random Variate Generation*, Springer-Verlag, 1986,
Chapter VII, Section 2.6, pp.299–300, the envelope preceding Theorem 2.6
and the reflected-case reduction and first integral in its proof,
[author-hosted primary text](https://luc.devroye.org/chapter_seven.pdf).
The source assessment inspected these cases in step526. The elementary
unnormalized specialization is justified below; no property of a
probability density or positivity of complex P is assumed.

## Conclusion

For every s in D the defining integral is admissible and absolutely
convergent, and

    T_L(s)<(512/105)(u/sqrt(Q))exp(-(85/48)Qd^2)
          <(9u/sqrt(Q))exp(-(77/50)Qd^2).             (1)

For every v in the entire closed interval [u/2,v_L], put
z(v)=v+i y_L and phi(v)=Re(S_s(z(v))-S_s(x)). The proof also gives

    tau(v)=Re(pi exp(2z(v)))>3,
    |1+rho(z(v))|<2,
    Re(s/z(v)^2)>0,     phi''(v)<-12,
    phi'(v_L)>(105/256)Q/u.                          (2)

These are uniform statements on all of D, with no upper bound on u.
The proof was completed in step527 and passed the independent
conceptual audit in step529 below without a mathematical correction.
This is a reproduction/specialization of a known
endpoint method for a nominated source component, not a claim of
novelty beyond the sources checked. L801 is downstream context and
comparison only; its right-ray bounds are not used as left-segment
premises. This does not control the portion before u/2, a continued
endpoint, global contour equality or error assembly, quotient/inversion,
certificates, or sufficient actual-Xi signs. It is not an RH candidate.

## Proof

### Ordering, height and branches on the whole segment

We first record an elementary consequence of L797's clearance:

    cos(2h)>sin(1/(2u))>=1/(4u).                     (3)

Indeed 0<1/(2u)<1/6, and sin t>=t-t^3/6>=t/2 in this range.
The function exp(2u)/u has positive logarithmic derivative 2-1/u
for u>=3. Hence

    Q/u>pi exp(6)/3>1000/3,
    Re(q-c)=Q cos(2h)-c>Q/(4u)-c>0.                (4)

To locate the height of the left endpoint, differentiate F and use
s=x(q-c), as in L798, to obtain

    A=4q+2(q-c)/x.

If h>0, then sin(2h)>=2h cos(2h); the difference has value zero
at zero and derivative 4h sin(2h)>=0. Therefore

    Im A=4Q sin(2h)
          +2[Q(u sin(2h)-h cos(2h))+ch]/(u^2+h^2)>0. (5)

Here u sin(2h)-h cos(2h)>0 because u>3, h>0 and cos(2h)>0.
Since Re A>0, (5) gives 0<theta<pi/2. The endpoint coordinates are

    v_L=u-d cos(theta/2),    y_L=h+d sin(theta/2).

Thus u-d<=v_L<u and y_L>h when h>0. At h=0, q=Q>c,
A=4Q+2(Q-c)/u is positive real, theta=0 and y_L=0.
L797's conjugation identity, the explicit formula for A and its positive
real part imply that theta and y_L change sign under conjugation,
while u,d and v_L stay fixed. In particular |y_L|>=|h| in all cases.

In addition |theta|<pi/2 implies |sin(theta/2)|<1/sqrt(2)<5/7.
Combining this with the saddle clearance gives

    |y_L|<=|h|+d|sin(theta/2)|
           <pi/4-1/(4u)+15/(112u)
           =pi/4-13/(112u).                         (6)

Since d<1/16<u/2, we have u/2<u-d<=v_L<u. The whole nonempty
closed segment z(v), u/2<=v<=v_L, therefore has positive real part
and the strict height clearance (6). It lies in U and in the domain
of the principal Log, with a neighborhood there for each fixed s.
This checks the entire segment, rather than only its radius-d endpoint.

### A full-segment theta parameter and amplitude majorant

Let r=13/(56u), so 0<r<13/168<1/10. From (6) and the
monotonicity of cosine on [0,pi/2],

    cos(2y_L)>sin r> (99/100)r.

The last bound follows from sin r>=r-r^3/6 and r^2/6<1/600.
Since v>=u/2, this gives

    tau(v)=pi exp(2v)cos(2y_L)
            >(1287/5600)pi exp(u)/u.                (7)

The logarithmic derivative of exp(u)/u is 1-1/u>0 for u>=3.
The exponential series gives e>2 and e^2>7, so exp(3)>14.
Using pi>3 and u>3 in (7) proves

    tau(v)>(1287/5600)*14=9009/2800>3.              (8)

The lower real endpoint therefore still has ample theta convergence;
L799's diameter bound has not been extended by assertion.

L799's normal convergence and H!=0 give, at every point of U,

    rho(z)=-(3/(2pi))exp(-2z)
       +sum_{n>=2}[n^4-(3/(2pi))n^2 exp(-2z)]
                  exp(-(n^2-1)pi exp(2z)).          (9)

On this segment v>=u/2>0 and 3/(2pi)<1/2. Consequently the
absolute value of its n>=2 sum is bounded by sum_{n>=2}b_n, where

    b_n=(n^4+n^2/2)exp(-(n^2-1)tau)>0.

For n>=2 the ratio of the polynomial factors is at most (3/2)^4.
Thus

    b_{n+1}/b_n <=(81/16)exp(-(2n+1)tau)
                  <(81/16)exp(-5)<1/10.

For the final comparison e^5=e(e^2)^2>98, so 81/(16e^5)
<81/1568<1/10. Since b_2=18exp(-3tau), the entire tail satisfies

    sum_{n>=2}b_n<20exp(-3tau).

Together with (8) and the separate n=1 correction in (9),

    |rho(z(v))|<(1/2)exp(-u)+20exp(-3tau)
                <1/2+20/343<1.                    (10)

Here tau>3>2 and e^6=(e^2)^3>343. Hence |1+rho|<2 on the
whole interval. Normal convergence justifies the complete-series
triangle inequality. No complex summand has been assigned a sign and
no series has been interchanged with an integral.

### Strict horizontal phase concavity

It suffices first to consider h>0. Write

    alpha=Arg x,   psi=Arg(q-c),   gamma=Arg z(v).

Then alpha>0. By (4) and Im(q-c)=Q sin(2h)>0,
0<psi<pi/2. Since y_L>=h, v<=u and all the real coordinates
are positive, gamma>=alpha. Moreover (6) gives y_L<pi/4<1,
whereas v>=u/2>3/2, so 0<gamma<pi/4. The saddle identity
s=x(q-c) now shows that s/z(v)^2 has modulus |s|/|z(v)|^2
and the following argument representative:

    -pi/2 < -2gamma < alpha+psi-2gamma
                         <=psi-alpha<pi/2.         (11)

The cosine of this representative is positive. Therefore
Re(s/z(v)^2)>0. This uses the outward height and smaller real
coordinate of the left segment; a right-ray bound is not a premise.
At h=0, both s=u(Q-c)>0 and z(v)=v>0 are real, giving the
same strict positivity. For h<0, all the quantities in this quotient
are complex conjugates of the corresponding h>0 ones. Its real part
is unchanged, proving positivity in that case as well.

Differentiating with respect to the real horizontal coordinate v gives

    phi''(v)=Re S_s''(z(v))
             =-2Re(s/z(v)^2)-4tau(v)<-12<0,          (12)

by (8) and (11). This proves concavity throughout the closed segment;
it does not claim log-concavity of the complex theta amplitude.

### Positive horizontal endpoint slope

The straight Taylor segment from x to x-da lies in L798's phase disc.
Taylor's formula for S_s' gives

    S_s'(x-da)=Ada+R,
    R=(-da)^2 integral_0^1(1-t)S_s'''(x-t da) dt,
    |R|<5Qd^2.                                     (13)

As Aa=B exp(i theta/2) and |theta|<pi/2, we have
cos(theta/2)>1/sqrt(2)>2/3. Using B>(15/4)Q and d<1/16,

    phi'(v_L)=Re S_s'(z_L)
        >(5/2)Qd-5Qd^2
        >(35/16)Qd=(105/256)Q/u=:kappa>0.           (14)

This is the derivative in the horizontal direction. The initial
Taylor displacement is rotated, but no derivative along that rotated
line has been substituted for phi'. Separately L798 gives the endpoint
value

    phi(v_L)<-(85/48)Qd^2.                          (15)

### Left tangent envelope and exact normalized payment

The cited concave left-tangent principle applies to the real phase.
For clarity its use for this unnormalized finite interval follows
directly from (12): phi' is decreasing, so for v<=v_L,

    phi(v_L)-phi(v)=integral_v^{v_L}phi'(w) dw
                       >=phi'(v_L)(v_L-v)
                       >=kappa(v_L-v).

It follows from (15) that

    exp(phi(v))<=exp(-(85/48)Qd^2)exp(-kappa(v_L-v)). (16)

The principal Log is defined throughout the segment, and the pointwise
factorization of (9) is exactly

    exp(2s Log z)P(z)=4pi^2 exp(S_s(z))(1+rho(z)).    (17)

The integrand is continuous on the compact interval inside its
holomorphy domain, so its finite integral exists and is absolutely
convergent. Equations (10), (16) and (17), with the denominator in
the hypotheses kept unchanged, imply

    T_L(s)<(2/|C|)exp(-(85/48)Qd^2)
                  integral_{u/2}^{v_L}exp(-kappa(v_L-v)) dv
           <(2/(|C| kappa))exp(-(85/48)Qd^2).        (18)

The last integral is exactly (1-exp(-kappa(v_L-u/2)))/kappa,
strictly below 1/kappa. Extending its positive exponential majorant
would give the same bound; no theta integral is extended before u/2.
The exact principal-root normalization from L798 gives

    1/|C|=sqrt(B/(2pi))<sqrt(Q),

because B<5Q and 2pi>6>5. Substitution of (14) in (18) proves
the first inequality in (1). The required threshold follows from

    9-512/105=433/105>0,
    85/48-77/50=277/1200>0,

and Qd^2>0. These are strict uniform margins, not sampled payments.

All estimates start from L797/L798's strict bounds on every point of
the closed D. Thus the cases |s|=6000 and Re(s)=-|s|/(8log|s|)
are included directly. Both signs of h and h=0 were treated explicitly.
The monotonic comparisons apply on the entire range u>3, with no
cutoff, limiting argument at infinity, or fixed strip-width premise.
No global contour identity, continued endpoint, zeta zero information
or uninspected supplement was used.

The parameter-specific proof is necessary because the primary tangent
envelope supplies none of the moving complex theta geometry, series
majorant or effective constants. The result verifies only this selected
component and does not establish the source's combined-tail or global
Mellin assertion. The independent audit below verifies only this scope.

### Independent conceptual audit, 5 November 2026 — step529

Reused the pre-existing SPECIALIZE assessment
`drafts/literature/2026-11-05-mellin-left-horizontal-segment-audit.md`.
All of (1)–(2) passes independent reconstruction. This establishes the
reviewed status of this local source specialization, with no correction
to its statement, proof or constants and no claim beyond the checked
sources. The following checks are analytic, not numerical sampling.

**Inputs, branches and the full interval.** L797 supplies its inverse
and strict clearance at every point of the closed D, together with
conjugation and Re A>0. L798's admissible closed phase disc, derivative
bound, strict nonzero-displacement decrement and principal-root
normalization have exactly the definitions used here. L799's normal
convergence and series division apply on all U; its separate diameter
amplitude estimate is not used on the longer left segment. Neither
L800 nor L801 is an input to this argument.

For h>0 the imaginary part of 2(q-c)/x is
2[Q(u sin(2h)-h cos(2h))+ch]/(u^2+h^2), so (5) has the correct
sign. The inequality sin(2h)>=2h cos(2h) makes its bracket positive:
u sin(2h)-h cos(2h)>=(2u-1)h cos(2h)>0. Thus theta>0 and
y_L=h+d sin(theta/2)>h. Reflection handles h<0, and h=0 gives
A>0 and y_L=0 directly. The endpoint is genuinely to the left,
since cos(theta/2)>0. Its height remains strictly inside U because

    1/4-(3/16)(5/7)=13/112,
    u/2<u-d<=v_L<u,    |y_L|<pi/4-13/(112u).

Every point of the closed interval therefore has positive real part
and a neighborhood in the principal-Log domain and U. No endpoint
limit or positive strip width independent of u is being assumed.

**Theta parameter and complete-series payment.** The bound
r=13/(56u)<1/10 gives sin r>99r/100, including the minimum real
coordinate v=u/2. Consequently

    tau(v)>(1287/5600)pi exp(u)/u
           >(1287/5600)*14=9009/2800>3.

Here exp(u)/u is strictly increasing for u>3; pi>3 and exp(3)>14
justify the second comparison. The latter exponential inequality is
elementary: e>2 and the first five terms of exp(2) sum to 7, with
positive remaining terms. No assumption that u is bounded above enters.

At any fixed point of the interval, put p_n=n^4+n^2/2. Then

    p_(n+1)/p_n
      =((n+1)/n)^4
        (1+1/(2(n+1)^2))/(1+1/(2n^2)) <=81/16, n>=2.

Thus b_(n+1)/b_n<81/(16e^5)<1/10. The deliberately weaker
exp(-5) used in the original proof is legitimate since tau>3>1.
The geometric majorant bounds the full tail strictly by
18 exp(-3tau)/(1-1/10)=20 exp(-3tau). The separate first correction
is less than exp(-u)/2. Hence

    |rho|<1/2+20/343=383/686<1,

which pays |1+rho|<2 uniformly. Normal convergence permits the
pointwise division and absolute summation; no series/integral
interchange or positivity of a complex theta summand is used.

**The load-bearing angle comparison.** Clearance gives
Re(q-c)>Q/(4u)-c>250/3-9/4=973/12>0. This check is necessary
before putting psi=Arg(q-c) in (0,pi/2) for h>0. Both alpha and
psi are then positive. Since y_L>=h>0 and v<=u, gamma>=alpha;
since y_L<pi/4<1 and v>3/2, gamma<pi/4. Therefore the real
number beta=alpha+psi-2gamma satisfies

    -pi/2<-2gamma<beta<=psi-alpha<pi/2.

The product identity s=x(q-c) gives
s/z^2=(|s|/|z|^2)exp(i beta); this uses an argument representative
and does not assume that Arg s=alpha+psi in a chosen branch.
It proves Re(s/z^2)>0 at every interval point, even when Re s<0.
For h=0, s=u(Q-c)>0 and z=v>0. For h<0 the quotient is the
complex conjugate of its value for the conjugate parameter in D.
Thus phi''=-2Re(s/z^2)-4tau<-12 in all cases. The calculation
concerns the real phase alone, with no log-concavity assertion for P.

**Horizontal slope, tangent direction and normalization.** Taylor's
formula for S_s' with displacement -da has linear term +Ada and
remainder (-da)^2 integral_0^1(1-t)S_s'''(x-tda)dt. Its modulus
is less than 5Qd^2. Because Aa=B exp(i theta/2), its real linear
term is Bd cos(theta/2), giving

    phi'(v_L)>(5/2)Qd-5Qd^2
               >(35/16)Qd=(105/256)Q/u=kappa>0.

This is the horizontal derivative; there is no replacement by the
derivative along the rotated displacement. L798's decrement uses
its real parameter -d!=0, so the strict 85/48 bound at z_L applies.
Concavity makes phi' decreasing: integration from v to v_L yields
phi(v)<=phi(v_L)-kappa(v_L-v), in the direction required for an
upper bound. The positive majorant has finite integral
(1-exp(-kappa(v_L-u/2)))/kappa<1/kappa.

The exact factorization (17) cancels |4pi^2 exp(S_s(x))| from the
denominator. The horizontal measure is dz=dv; no factor a belongs
to this integral. L798 gives C!=0 and
1/|C|=sqrt(B/(2pi))<sqrt(Q). The resulting coefficient is exactly
2*(256/105)=512/105. The required comparison margins are
9-512/105=433/105>0 and 85/48-77/50=277/1200>0, with Qd^2>0.
Strictness is supported by the endpoint, amplitude and finite integral
bounds; no uniform positive numerical slack is required.

Both boundaries of D, both signs of h, h=0 and unbounded u are
included by the same strict input estimates. The existing direct
mathematical inputs L797, L798 and L799 are exactly sufficient; the
ID-only DAG needs no change. The audit imports no new external result.
The segment before u/2, continued endpoint, global contour identity
and assembly, quotient/inversion, certificates and sufficient Xi signs
remain unverified. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage has not been checked. The cited concave tangent
principle is a standard real-calculus input; its finite unnormalized
specialization is proved above. No Mathlib theorem supplying the full
moving complex theta bound or the displayed constants is asserted, and
unchecked availability is not evidence of absence. There is no Lean
formalization or formal verification claim for this lemma.
