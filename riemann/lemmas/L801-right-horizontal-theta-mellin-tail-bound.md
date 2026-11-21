# Lemma 801: a standalone right horizontal theta-Mellin tail bound

## Hypotheses

Use L797's saddle and L798's phase and principal branches:

    D={s: |s|>=6000, Re(s)>=-|s|/(8 log|s|)},
    c=9/4, F(z)=z(pi exp(2z)-c), F(x)=s, x=u+ih,
    q=pi exp(2x), Q=|q|=pi exp(2u), d=3/(16u),
    S_s(z)=2s Log(z)+(9/2)z-pi exp(2z),
    A=2F'(x)/x, B=|A|, theta=Arg A, a=exp(-i theta/2),
    C=sqrt(2pi/A)=a sqrt(2pi/B).

L797 gives u>3, |h|<pi/4-1/(4u), Re A>0, Q>1000 and
pi exp(6)>1000, including both closed boundaries of D. L798 gives
S_s'(x)=0, S_s''(x)=-A, (15/4)Q<B<5Q and, on |z-x|<=d,
|S_s'''(z)|<10Q. Its endpoint decrement is

    Re(S_s(x+da)-S_s(x)) < -(85/48)Qd^2.

Use L799's normally convergent series on U={z: |Im z|<pi/4}:

    P(z)=sum_{n>=1} [4pi^2 n^4 exp(9z/2)
                    -6pi n^2 exp(5z/2)] exp(-pi n^2 exp(2z)),
    H(z)=4pi^2 exp(9z/2-pi exp(2z)), rho(z)=P(z)/H(z)-1.

Set z_R=x+da and define, once convergence is established below,

    T_R(s)=|integral_0^infinity exp(2s Log(z_R+t))P(z_R+t) dt|
             / |4pi^2 exp(S_s(x)) C|.

This is exactly the standalone right-ray target preapproved by the
unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-mellin-right-horizontal-tail-test.md`.
Its source comparison is bramble_trace, *A continuum certificate for
the decreasing Levy factor associated with Riemann xi*,
[paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section 3, Lemma 2, (10)–(14). The source's combined
horizontal-tail allowance is not an assumption. The effective method
is the concave tangent envelope in Luc Devroye, *Non-Uniform Random
Variate Generation*, Springer-Verlag, 1986, Chapter VII, Section 2.6,
pp.299–300, the envelope preceding Theorem 2.6 and the first integral
of its proof, [author-hosted primary text](https://luc.devroye.org/chapter_seven.pdf).
No unread supplementary derivation is used.

## Conclusion

For every s in D the numerator integral converges absolutely and

    T_R(s) < (512/105)(u/sqrt(Q)) exp(-(85/48)Qd^2)
           < (14u/sqrt(Q)) exp(-(77/50)Qd^2).           (1)

More specifically, for z(t)=z_R+t, t>=0, and
phi(t)=Re(S_s(z(t))-S_s(x)), the proof establishes

    |1+rho(z(t))|<2,
    phi'(0)<-(105/256)Q/u,
    phi''(t)<-(15/16)Q/u.                             (2)

These are uniform inequalities on the whole closed, unbounded D.
The proof completed in step523 passed the independent conceptual audit
in step525, recorded below, without a mathematical correction.
This is a reproduction of one source component, with stronger constants
for this specified single ray; no originality beyond the sources checked
is asserted. It spends less than the nominated allowance on the right
tail alone and establishes neither the source's combined two-tail claim
nor a Mellin contour identity. Left tails, continued endpoint, global
deformation and assembly, quotient/inversion estimates, certificates
and sufficient actual-Xi signs remain open. This is not an RH candidate.

## Proof

### Geometry of the entire ray

Some elementary saddle estimates will be useful. Since c/Q<1/400,
|h|<pi/4<1 and u>3,

    |s|=|x||q-c| < (401/400)Q(u+1) < (3/2)Qu,       (3)
    |s| > (399/400)Qu > exp(2u),
    log|s|>2u.                                      (4)

For (3), u+1<(4/3)u and 401/300<3/2. For (4),
(399/400)pi u>1. The function exp(2u)/u increases for u>=3,
as its logarithmic derivative is 2-1/u>0. Hence

    Q/u > 1000/3,
    c(2u+1)/Q < (9/4)(7/3)(3/1000)=63/4000<1.       (5)

Also L797's clearance implies

    cos(2h)>sin(1/(2u))>=1/(4u).                     (6)

Here 1/(2u)<1/6 and sin v>=v-v^3/6>=v/2 on this interval.

We check how the rotated displacement changes the height; mere
membership of the endpoint in U would not give the signs below.
Suppose first that h>0. On 0<=h<pi/4,

    sin(2h)>=2h cos(2h),

because the difference vanishes at zero and has derivative
4h sin(2h)>=0. From A=4q+2(q-c)/x,

    Im A = 4Q sin(2h)
           +2[Q(u sin(2h)-h cos(2h))+ch]/(u^2+h^2)>0.

Thus 0<theta<pi/2. Rotating the same identity gives

    Im(A exp(-2ih))
      =2[-Qh+c(u sin(2h)+h cos(2h))]/(u^2+h^2)<0.   (7)

Indeed sin(2h)<=2h, cos(2h)<=1 and (5) make its numerator
strictly negative. Both theta and 2h are in (0,pi/2), so their
difference is in (-pi/2,pi/2). Equation (7) therefore implies
theta<2h; no argument wrap is involved. Writing

    z_R=v_0+iy,
    v_0=u+d cos(theta/2), y=h-d sin(theta/2),

we obtain

    v_0>u,  (1-d)h<y<h,                              (8)

since 0<sin(theta/2)<h and d<1/16. At h=0, A is positive
real and theta=y=0. Conjugation, valid for x and A with the stated
branches, supplies the reflected inequalities when h<0. In all cases
v_0>u, |y|<=|h| and y has the same sign as h when nonzero.

We also need the sign of Im s. For h>0 the saddle identity, (6),
and sin(2h)>=2h cos(2h) give

    Im s=Q(u sin(2h)+h cos(2h))-ch
         >=[Q(2u+1)cos(2h)-c]h
         > (Q/2-c)h>0.                              (9)

For h=0 it is zero, and conjugation covers h<0. Consequently
(Im s)y>=0 in every case.

For the entire ray let v=v_0+t. Then v>u>3 and |y|<=|h|<pi/4.
It lies inside U and the right half-plane, so P and the principal Log
are defined throughout. Its real theta parameter satisfies

    tau(t)=Re(pi exp(2(v+iy)))
          =Q exp(2(v-u))cos(2y)>Q/(4u)>Q/(5u)>2.    (10)

Here cos(2y)>=cos(2h), (6) applies, and (5) supplies the last
inequality. This establishes a full-ray bound without extending the
finite-disc assertion by assumption.

### Full theta-amplitude majorant

L799's normal convergence and the nonvanishing of H give on U

    rho(z)=-(3/(2pi))exp(-2z)
       +sum_{n>=2}[n^4-(3/(2pi))n^2 exp(-2z)]
                  exp(-(n^2-1)pi exp(2z)).           (11)

For z=v+iy on the ray, v>u>0, pi>3 and (10) imply

    |rho(z)| <= (1/2)exp(-2v)
        +sum_{n>=2}(n^4+n^2/2)exp(-(n^2-1)tau).

The positive tail terms have consecutive ratio at most
(81/16)exp(-5tau)<1/10 when tau>1, exactly as in L799:
the polynomial ratio is at most (3/2)^4 and
e^5>98 makes (81/16)e^(-5)<1/10. Thus the full tail, not just
its first term, is less than 20exp(-3tau). In particular, with
L799's eta(u) retained for comparison,

    |rho(z)| < (1/2)exp(-2u+2d)+20exp(-3Q/(5u))
             =eta(u)<1.                             (12)

To verify the last bound, u-d>0 makes its first term less than
1/2; Q/(5u)>2 and e^6>343 give a second term less than
20/343<1/2. Therefore |1+rho(z)|<2 on the entire ray.
No claim about log-concavity or positivity of complex P is used.
Normal convergence justifies the pointwise series bound; there is
no exchange of this series with an improper integral.

### Real-phase concavity on the entire ray

Write s=sigma+i beta and z=v+iy on the ray. Since v>3>|y| and
beta y>=0 by (9),

    Re(s/z^2)
      =[sigma(v^2-y^2)+2 beta v y]/(v^2+y^2)^2.      (13)

If sigma>=0, (13) is nonnegative. If sigma<0, the positive
coefficient (v^2-y^2)/(v^2+y^2)^2 is at most 1/v^2, so
(13)>=sigma/v^2. By the defining inequality of D and (3)–(4),

    sigma >= -|s|/(8 log|s|)>-3Q/32.

Thus in both cases Re(s/z^2)>-3Q/(32u^2). Since the real
ray parameter differentiates z with derivative one,

    phi''(t)=Re S_s''(z)
            =-2 Re(s/z^2)-4 tau(t)
            < 3Q/(16u^2)-Q/u
            < -(15/16)Q/u<0.                        (14)

The final strict inequality uses u>3. This calculation keeps the
favorable beta y term; replacing all of Re(s/z^2) by a modulus
estimate would not prove the stated uniform concavity this way.

### Effective negative endpoint slope

The straight segment from x to x+da lies in L798's closed phase
disc. Taylor's formula for S_s' on this segment gives

    S_s'(x+da)=-Ada+R,
    R=(da)^2 integral_0^1(1-r)S_s'''(x+r da) dr,
    |R|<5Qd^2.                                      (15)

Because Aa=B exp(i theta/2), |theta|<pi/2 and
cos(theta/2)>1/sqrt(2)>2/3, L798's B>(15/4)Q implies

    phi'(0)=Re S_s'(z_R)
      < -(5/2)Qd+5Qd^2
      < -(35/16)Qd=-(105/256)Q/u.                   (16)

This verifies the derivative in the horizontal direction, rather
than confusing it with the derivative along the rotated diameter.
The phase at the endpoint itself is supplied by L798:

    phi(0)<-(85/48)Qd^2.                            (17)

### Tangent envelope, convergence and normalized constants

The standard concave tangent envelope cited above applies to the real
phase phi. Its unnormalized use here follows directly from (14): for
each finite t>=0, integration of phi'(r)<=phi'(0) gives

    phi(t)<=phi(0)+t phi'(0).

This does not assume integrability or normalize a putative density.
With kappa=(105/256)Q/u>0, equations (16)–(17) give

    exp(phi(t)) <= exp(-(85/48)Qd^2)exp(-kappa t).   (18)

The exact pointwise factorization from (11) and the definitions is

    exp(2s Log z)P(z)=4pi^2 exp(S_s(z))(1+rho(z)).

Together with (12) and (18), this dominates the absolute integrand
by an integrable exponential on [0,infinity). Continuity on finite
segments and this majorant prove absolute convergence of the specified
complex integral. The triangle inequality is therefore legitimate and

    T_R(s) < (2/|C|) exp(-(85/48)Qd^2)/kappa.

L798's principal-root normalization gives

    1/|C|=sqrt(B/(2pi))<sqrt(Q),

since B<5Q and 2pi>6>5. Substitution of kappa proves the first
inequality in (1). The requested comparison follows from the exact
strict margins

    14-512/105=958/105>0,
    85/48-77/50=277/1200>0,

and Qd^2>0. These are bounds on the full domain, not sampled checks.

Every geometric estimate used strict inequalities provided on the
closed D, so |s|=6000 and its curved left boundary are included without
passing to a limit. The h=0 case and both signs of h were treated
explicitly. There is no upper cutoff on u or fixed positive strip
width assumption. No contour deformation, continued endpoint identity,
interchange of infinite operations or zero-location premise occurs.

The parameter-specific derivation is necessary because Devroye supplies
the envelope method, not these theta or phase hypotheses and constants;
the inspected paper23 outline delegates its global estimates to unread
supplements. This proof reproduces the separately nominated right-ray
component only. It does not verify that outline's other components.

### Independent conceptual audit, 5 November 2026 — step525

Reused the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-mellin-right-horizontal-tail-audit.md`.
The entire standalone claim (1)–(2) passes. This establishes the
reviewed status of this local source reproduction; it is not a result
beyond the sources checked or verification of the combined tail budget.
No hypothesis, constant or proof inequality needs correction.

**Inputs, domain and branches.** The relevant statements and proofs of
L797–L799, including their prior conceptual audits, use exactly the
same D, saddle, phase and theta normalization. L797 gives a unique
inverse on an open neighborhood of D and strict clearance on both
closed boundaries. L798 supplies a holomorphic radius-d disc, the
uniform third derivative bound, the endpoint decrement and the
principal-root identity. L799 supplies normal convergence on U and
the pointwise series factorization. Its finite-diameter amplitude
estimate is not being assumed on an infinite ray. A has positive real
part, so Arg A is unambiguously in (-pi/2,pi/2), and C is nonzero.

**Height displacement and signs.** Recomputing A=4q+2(q-c)/x gives
the displayed Im A and Im(A exp(-2ih)) in (7). For h>0,
u sin(2h)-h cos(2h)>0 follows from u>3 and
sin(2h)>=2h cos(2h). The second imaginary part is negative because
its numerator is at most [-Q+c(2u+1)]h and
c(2u+1)/Q<63/4000<1. Both angles lie in (0,pi/2), so the
negative sine of their difference implies theta<2h without wrapping.
Thus 0<sin(theta/2)<h, v_0>u and (1-d)h<y<h.
At h=0, A>0 and y=theta=0. Conjugation of x and A, with these
principal branches, proves the corresponding lower-half-plane case.
Equation (9) independently gives Im(s) the sign of h. Consequently
beta y>=0 on every ray, including zero height.

The scalar bounds (3)–(6) are uniform: |x|<u+1,
|q-c| lies strictly between (399/400)Q and (401/400)Q,
log|s|>2u, and Q/u>1000/3. The latter follows from monotonicity
of exp(2u)/u, not a finite parameter sample. Since |y|<=|h| and
v>u, tau(t)>Q/(4u)>Q/(5u)>2 for every t>=0. This verifies
strip admissibility and the theta-parameter lower bound on the full
unbounded ray even as the available strip clearance tends to zero.

**Complete amplitude, before integration.** L799's locally uniform
convergence permits division by the nonzero H at each ray point.
For n>=2 the polynomial ratio in the positive majorant is a weighted
average of ((n+1)/n)^4 and ((n+1)/n)^2, hence at most 81/16.
The exponential ratio is at most exp(-5tau), so the complete series
is bounded by 18exp(-3tau)/(9/10)=20exp(-3tau), strictly.
The n=1 correction is separately less than exp(-2u+2d)/2.
As u-d>0 and Q/(5u)>2, eta(u)<1/2+20/343<1.
This proves |1+rho|<2 throughout the ray. No normal-convergence
claim on the whole unbounded ray and no series/integral interchange
is required; the eventual integrable majorant is proved separately.

**Signed curvature and horizontal derivative.** Direct multiplication
by (v-iy)^2 gives exactly (13), with the positive term 2 beta v y.
For sigma<0 the coefficient inequality

    0<(v^2-y^2)/(v^2+y^2)^2<=1/v^2

must reverse upon multiplication by sigma. Therefore
Re(s/z^2)>=sigma/v^2>-3Q/(32u^2), using the left boundary
of D, |s|<(3/2)Qu, log|s|>2u and v>u. For sigma>=0
the real part is nonnegative. Differentiation with dz/dt=1 then
gives phi''<-(1-3/(16u))Q/u<-(15/16)Q/u. The sign
of the beta term is essential; no absolute-value estimate replaces it.

Taylor's formula applied to S_s', not to the rotated real-phase
derivative, gives R=(da)^2 integral_0^1(1-r)S_s'''(x+r da) dr.
Its magnitude is <5Qd^2, with the factor 1/2 from the integral.
The linear term -Ada has real part -Bd cos(theta/2).
Using B>(15/4)Q, cos(theta/2)>2/3 and d<1/16 gives
phi'(0)<-(35/16)Qd=-(105/256)Q/u. Separately L798's
decrement at the real parameter v=d gives exactly (17). Thus the
horizontal slope and the rotated endpoint value are both justified.

**Convergence and constants.** Integrating the negative second
derivative on each finite interval proves the tangent envelope before
any improper integral is taken. The exact factorization multiplies
exp(S_s) by 4pi^2(1+rho), without a Jacobian since dz=dt.
The decaying exponential in (18), together with |1+rho|<2,
proves absolute convergence. The nonzero normalization cancels
|4pi^2 exp(S_s(x))| exactly. Since
|C|=sqrt(2pi/B) and B<5Q<2pi Q, its reciprocal is <sqrt(Q).
The resulting coefficient is 2*(256/105)=512/105. The comparison
margins are 14-512/105=958/105 and
85/48-77/50=277/1200, both strictly positive; Qd^2>0.
Strict endpoint and amplitude inequalities also justify the strict
integral bound. No uniform positive slack or boundary limit is needed.

All arguments apply at |s|=6000 and at the curved left boundary of D,
to both signs of h and h=0, and with no upper cutoff on u. The direct
mathematical uses are exactly the existing L797, L798 and L799 inputs;
L800 is not a premise. No numerical script, new external theorem,
continued endpoint, global contour identity or Xi sign assumption
enters the audit. Left tails and the other stated independent gaps
remain open. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
Supporting mathematics consists of L797–L799, elementary complex
algebra and trigonometry, Taylor's integral remainder, the tangent
inequality for a differentiable concave real function, and integration
of a decaying exponential. No specific Mathlib declaration or formal
verification is asserted.
