# Lemma 890: a finite trace shear can have negative interface flux while its full mass still increases

## Hypotheses

Use L847's actual entire function and positive constants

\[
G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\qquad
R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2,
\]
\[
F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
\qquad
\omega=C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^3z_2^3}
                    dz_1\wedge dz_2.                       \tag{1}
\]

Assume L879's smooth real periodic u:T2 -> R2, with
J=det(I-iDu) nowhere zero, and stationarity of the full mass under
real radial variations supported away from its density zeros. Write

\[
z_j=R e^{u_j+iy_j},\qquad Q=F(z_1,z_2)J=\lambda s,
\quad |\lambda|=1,\quad s\text{ real and smooth},\qquad
\mathcal B(u)=(2\pi)^{-2}\int_{T^2}|Q|.                   \tag{2}
\]

The phase-line conclusion in (2) is supplied by L879. Condition on
the same clean strip as L889:

\[
S=(l,r)\times(c,d),\quad l=\alpha-\epsilon,
\quad r=\beta+\epsilon,\quad \epsilon>0,\quad\alpha<\beta, \tag{3}
\]

with compact closure in a lifted angular chart. Its only density
zeros are the complete simple G(z1)-zero fibers x=alpha,beta;
G(z2), z1-z2 and J are nonzero on its closure. Here x=y1 and y=y2.
On each fiber, z1=zeta_gamma is a fixed simple zero and
partial_y u1=0. The signs of s on the interiors of

\[
D_0=[l,\alpha]\times[c,d],\quad
D_1=[\alpha,\beta]\times[c,d],\quad
D_2=[\beta,r]\times[c,d]
\]

are sigma,-sigma,sigma, respectively. All rectangles use the original
dx wedge dy orientation. Define on the two fibers

\[
p_\gamma=\partial_xu_1(\gamma,y),\quad
k_\gamma=\partial_yu_2(\gamma,y),\quad
h_\gamma=\partial_xs(\gamma,y),\quad
\eta_\gamma=z_2(\gamma,y).                                \tag{4}
\]

The real h_gamma is nonzero, with h_alpha=-sigma*|h_alpha| and
h_beta=sigma*|h_beta|. Impose this additional, explicit condition:
there is one y0 in (c,d) such that, at both fibers,

\[
 k_\gamma(y_0)\bigl(1-p_\gamma(y_0)^2\bigr)
                         +2p_\gamma(y_0)\ne0.            \tag{5}
\]

Neither (5), the clean configuration, nor a stationary actual-G
graph realizing it is asserted to exist. No condition |p_gamma|<1
is imposed. The result below is conditional on precisely these data.

## Conclusion

There are explicit smooth real fields A,b with compact support in S,
finite constants B_alpha,B_beta with |B_gamma|>1, and tau_*>0 such
that for every 0<tau<=tau_* the single two-component replacement

\[
                 u_\tau=u+(\tau A,b)                     \tag{6}
\]

is periodic, agrees with u near and outside the entire strip boundary,
and satisfies det(I-iDu_tau)!=0 everywhere. Both first traces are
nonzero. The second trace has value zero and derivative B_gamma at
(gamma,y0). Thus this family is outside L889's small-trace box
whenever that box is defined: its derivative bound there is <=1/2.

Let E_tau be the complete, unnormalized phase cost

\[
E_\tau=\sum_{j=0}^2\int_{D_j}
 \left(|Q_\tau|-\sigma_j
                \operatorname{Re}(\overline\lambda Q_\tau)\right),
\qquad (\sigma_0,\sigma_1,\sigma_2)=(\sigma,-\sigma,\sigma).
                                                               \tag{7}
\]

The signed interface term I_tau in L889(7) is strictly negative.
Nevertheless, with the positive finite constant e=E_0 constructed
below and another finite constant C_1>0,

\[
-C_1\tau^2\le I_\tau<0,\qquad E_\tau\ge 3e/4,
\qquad C_1\tau^2\le e/4,
\]
\[
\boxed{\displaystyle
 \mathcal B(u_\tau)-\mathcal B(u)
   =\frac{E_\tau+I_\tau}{(2\pi)^2}
   \ge\frac{e}{2(2\pi)^2}>0.}                            \tag{8}
\]

All cutoff collars and new numerator zeros are included. This stops
this fixed finite shear followed by sufficiently small depinning,
even when both trace contributions have the desired negative sign.
It does not stop arbitrary finite depinning, arbitrary fillings of
these traces, or families whose shear and support change together
with the first amplitude. The positive constant e depends on the
fixed shear and its supports; no uniform lower bound for shrinking
supports is claimed. The construction uses two disjoint neighborhoods
within the nominated strip and does not test an interaction through
the intervening cell.

This is a conditional specialization of the known boundary method,
classified REPRODUCTION, not a new general calibration theorem or
certified novelty. It supplies neither minimizer existence nor
exclusion of the paired configuration, L868's sharp bound, higher
mixed signs or RH. The result is unaudited.

## Proof

### Ready coverage, imported method and checked working identity

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-07-paired-fiber-finite-replacement-test.md`.
Its scope allows both components, finite endpoints and a scoped
boundary obstruction on this conditional strip. Reuse Scott Lawrence
and Yukari Yamauchi, *Convex optimization and contour deformations*,
arXiv:2311.13002v2, 14 August 2024,
[Section III, (18)-(19), p5](https://arxiv.org/pdf/2311.13002v2#page=5),
for the known dominated closed-form boundary method. The three forms
sigma_j*Re(conjugate(lambda)*omega) are individually dominated by
|omega| on every real tangent plane. Their different internal boundary
fluxes must be retained; they do not constitute a single closed signed
ambient certificate. No attainment or graph-realization theorem is used.

For smooth pullback differentiation reuse Guillemin and Sternberg,
*Semi-classical analysis*, 13 January 2010,
[Sections 13.13-13.14.1, (13.7)-(13.9), pp449-455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
For the integrated boundary comparison reuse Lebl, *Tasty Bits of
Several Complex Variables*, v4.4, 31 May 2026,
[Appendix C, Theorem C.6 and regularity remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
These primary-source hypotheses and application scopes are recorded
in the reused assessment. All homotopies here are smooth on compact
parameter rectangles with images in compact annuli in (C*)2. The
holomorphic form has no singularity at its numerator zeros. Hence the
stated pullback and Stokes hypotheses hold. The application difference
is the finite shear, its nonzero endpoint Jacobian and the paid cost
in (8); no general theorem is reproved.

We use L889's working identity only after checking its needed signs
and endpoint reduction. With eps_alpha=2*sigma and eps_beta=-2*sigma,
set, for real q,A and w in C*,

\[
K_\gamma(q,w)=-F(\zeta_\gamma e^q,w),\qquad
D_\gamma(A,w)=\int_0^1(1-t)\partial_qK_\gamma(tA,w)\,dt,
\]
\[
W_\gamma(A,B,Z;y)=\varepsilon_\gamma
 \operatorname{Re}\{\overline\lambda(k_\gamma+i+Z)
                         D_\gamma(A,\eta_\gamma e^B)\}. \tag{9}
\]

For traces a_gamma=v1(gamma,y), b_gamma=v2(gamma,y), the identity is

\[
(2\pi)^2[\mathcal B(u+v)-\mathcal B(u)]
 =E(v)+I(v),\qquad
I(v)=\sum_\gamma\int_c^d
 a_\gamma^2 W_\gamma(a_\gamma,b_\gamma,b_\gamma';y)\,dy.   \tag{10}
\]

To check the reduction, put P_gamma(A,w)=integral_0^A K_gamma(q,w)dq.
For the fiber homotopy w_t=eta_gamma*exp(t*b_gamma), its derivative
quotient in y is ell_t=k_gamma+i+t*b_gamma'. Direct differentiation gives

\[
\partial_t[P_\gamma(ta_\gamma,w_t)\ell_t]
-\partial_y[P_\gamma(ta_\gamma,w_t)b_\gamma]
=K_\gamma(ta_\gamma,w_t)
 [a_\gamma\ell_t-tb_\gamma a_\gamma'].                    \tag{11}
\]

The holomorphic w derivatives and the b_gamma' terms cancel. The
y endpoint terms vanish by compact support, and the t=0 term is zero.
Since K_gamma(0,w)=0, two finite integrations give
P_gamma(A,w)=A^2 D_gamma(A,w), for either sign of A, including A=0.
Thus the finite fiber flux is integral a_gamma^2 D_gamma times
(k_gamma+i+b_gamma'). L879's division-free pullback differentiation
gives cell period changes T_alpha, T_beta-T_alpha and -T_beta.
The original cells saturate their signed real parts. Their weighted
sum gives the eps_gamma in (9)-(10). This checks the exact needed
identities without an invertible intermediate homotopy, and without
claiming an independent audit of all of L888 or L889.

The L887 fixed-field expansion, L888 pinned stop, L889 positive
small-trace box, and attempt65/69 signed-kernel/primitive failures
were compared before this attempt. None supplies a sign for the
finite shear used here; none is strengthened to a universal stop.

### A finite derivative makes both trace coefficients negative

For the next definitions p_gamma,k_gamma,h_gamma are evaluated at y0.
Put H_gamma=|h_gamma(y0)|>0. At a contact partial_y u1=0, so

\[
J=(1-ip_\gamma)(1-ik_\gamma),\qquad
\lambda h_\gamma
 =F_{z_1}(\zeta_\gamma,\eta_\gamma)\zeta_\gamma
       (p_\gamma+i)(1-ip_\gamma)(1-ik_\gamma).
\]

Since D_gamma(0,eta_gamma)=-zeta_gamma F_(z1)/2, this gives
(k_gamma+i)D_gamma(0,eta_gamma)=lambda*h_gamma/[2(p_gamma+i)^2].
Also eps_gamma*h_gamma=-2H_gamma at either fiber. Consequently (9)
has the following exact affine dependence on a real derivative B:

\[
W_\gamma(0,0,B;y_0)=w_\gamma+c_\gamma B,
\quad w_\gamma=H_\gamma\frac{1-p_\gamma^2}{(1+p_\gamma^2)^2},
\]
\[
c_\gamma=H_\gamma
 \frac{k_\gamma(1-p_\gamma^2)+2p_\gamma}
      {(1+k_\gamma^2)(1+p_\gamma^2)^2}.                  \tag{12}
\]

In particular (5) is precisely c_gamma!=0. Choose the finite number

\[
B_\gamma=-\operatorname{sgn}(c_\gamma)
 \left(1+\frac{|w_\gamma|+H_\gamma}{|c_\gamma|}\right).
                                                               \tag{13}
\]

Then |B_gamma|>1 and W_gamma(0,0,B_gamma;y0)<=-H_gamma-|c_gamma|.
If (5) fails, this affine derivative test does not provide this
construction; no substitute sign or actual-data claim is asserted.

### Complete shear and nonzero Jacobian, including its collars

Choose fixed smooth real cutoffs xi,psi with values in [0,1],
compact support in (-1,1), and value 1 on [-1/2,1/2]. Write
K_xi=sup|xi'|, B_*=max_gamma |B_gamma|, and let

\[
M_1=1+\sup_{\overline S}|\partial_x\partial_yu_1|,
\qquad N_0=\sup_{\overline S}|\partial_xu_2|.
\]

Choose positive widths rho,h satisfying

\[
\rho<\min\{\epsilon/2,(\beta-\alpha)/3,
                         1/[4(1+M_1N_0)]\},
\]
\[
h<\min\{(y_0-c)/2,(d-y_0)/2,
                         1/[4(1+M_1B_*K_\xi)]\}.        \tag{14}
\]

Put xi_gamma(x)=xi((x-gamma)/rho), and define the entire second field

\[
b(x,y)=\sum_{\gamma=\alpha,\beta}
B_\gamma(y-y_0)\xi_\gamma(x)\psi((y-y_0)/h).             \tag{15}
\]

Its two supporting rectangles are disjoint and compactly contained
in S. Extending by zero is smooth and periodic. In either rectangle
write P=u1,x, T=u1,y, N=u2,x and K=u2,y. Since T(gamma,y)=0,
|T|<=M1*|x-gamma|. The full Jacobian at u_b=u+(0,b) is exactly

\[
J_b=(1-iP)(1-i(K+b_y))+T(N+b_x),
\qquad
\operatorname{Re}\frac{J_b}{1-iP}
       =1+\frac{T(N+b_x)}{1+P^2}.                       \tag{16}
\]

On that whole rectangle, including all x and y transitions,

\[
|TN|\le M_1\rho N_0<1/4,\qquad
|Tb_x|\le M_1B_*hK_\xi<1/4.                             \tag{17}
\]

Thus the real part in (16) exceeds 1/2, and |J_b|>=1/2 there.
Outside the rectangles the derivatives of b vanish and J_b=J.
In particular J_b is globally nonzero. There is no smallness
assumption on b_y: its finite derivative B_gamma at the contacts
was chosen in (13). All radial values remain finite and real.

### The fixed shear pays a strictly positive full phase cost

For a=0, (10) gives the exact pinned equality

\[
e:=E(0,b)=(2\pi)^2[\mathcal B(u_b)-\mathcal B(u)]\ge0.    \tag{18}
\]

In fact e>0. On the slice y=y0 and near either fiber, b=b_x=0 and
b_y=B_gamma*xi_gamma. At points off the fiber the original Q is
nonzero and the exact full-density quotient is

\[
\frac{Q_b}{Q}=1-B_\gamma\xi_\gamma\frac{P+i}{J}.          \tag{19}
\]

On the fiber, the smooth expression (P+i)/J has imaginary part

\[
\operatorname{Im}\frac{p_\gamma+i}
          {(1-ip_\gamma)(1-ik_\gamma)}
       =\operatorname{Im}\frac{i}{1-ik_\gamma}
       =\frac1{1+k_\gamma^2}>0.                         \tag{20}
\]

Choose x strictly to the right of alpha, sufficiently close that
xi_alpha=1 and the imaginary part in (20) remains positive. The
point lies in the interior of D1 and Q!=0. Since B_alpha!=0,
the quotient z=Q_b/Q in (19) has nonzero imaginary part. At this
point the phase-cost integrand in (7) equals
|s|*(|z|-Re z)>0. By continuity it is positive on an open rectangle
inside D1. It is nonnegative everywhere else, proving e>0.
All integrals are finite on compact domains. This proof uses the
actual F and full J; no replacement model, omitted zero or numerical
sign test enters (18)-(20).

### Depinning with negative traces and a fully paid mass bound

On |y-y0|<h/2, the second traces in (15) are exactly
b_gamma=B_gamma*(y-y0) and b_gamma'=B_gamma. The functions W_gamma
are smooth in all their displayed variables on every compact set:
the radial exponentials stay nonzero, G is entire, and (9) has only
a finite integral. By (12)-(13), choose 0<a0<=1 and 0<h_a<h/2
small enough that for both fibers

\[
W_\gamma(A,B_\gamma(y-y_0),B_\gamma;y)\le-H_\gamma/2
\quad\text{if }|A|\le a_0,\ |y-y_0|\le h_a.             \tag{21}
\]

Take a further smooth cutoff zeta with values in [0,1], compact
support in (-1,1), and value 1 on [-1/2,1/2]. Write
f(y)=zeta((y-y0)/h_a) and set

\[
A(x,y)=(\xi_\alpha(x)+\xi_\beta(x))f(y).                 \tag{22}
\]

Both first traces equal tau*f. The two fields in (6) depend on
both variables, and their entire supports and collars are specified
by (15),(22). For 0<tau<=a0, (10),(21) give

\[
I_\tau\le-\frac{H_\alpha+H_\beta}{2}\tau^2
                           \int_c^d f(y)^2dy<0.          \tag{23}
\]

Define a finite positive constant which also bounds its magnitude:

\[
C_1=1+\sum_\gamma\int_{y_0-h_a}^{y_0+h_a}f(y)^2
 \sup_{|A|\le a_0}
 |W_\gamma(A,B_\gamma(y-y_0),B_\gamma;y)|\,dy.
                                                               \tag{24}
\]

Then I_tau>=-C1*tau^2. No first-trace derivative has been discarded;
it was integrated exactly in (11).

For the complete interior cost, define Q_t to be the full density
of u+(t*A,b), for -1<=t<=1, and put

\[
L_E=1+2|S|\sup_{\substack{|t|\le1\\(x,y)\in\overline S}}
                         |\partial_t Q_t(x,y)|<\infty.   \tag{25}
\]

The density, rather than its modulus, is smooth in t even at
numerator zeros or a possible intermediate Jacobian zero. Its
derivative is bounded because the parameter and image sets are
compact. The inequality ||z|-|w||<=|z-w| and the real-part bound
therefore give, for |tau|<=1,

\[
|E_\tau-e|\le2\int_S|Q_\tau-Q_0|\le L_E|\tau|.         \tag{26}
\]

This estimate is on the entire strip, including every transition
collar. It uses no differentiation of a nonsmooth modulus.

Finally set H_b=I-iDu_b and

\[
K_A=\sup_{T^2}\|H_b^{-1}D(A,0)\|<\infty,
\]
\[
\tau_* =\min\left\{
 \tfrac12,\tfrac{a_0}{2},\frac{e}{4L_E},
 \sqrt{\frac{e}{4C_1}},\frac1{2(1+K_A)}\right\}>0.       \tag{27}
\]

The norm is the Euclidean complex matrix operator norm. Since

\[
I-iDu_\tau=H_b\bigl(I-i\tau H_b^{-1}D(A,0)\bigr),
\qquad \tau K_A<1/2,                                   \tag{28}
\]

the second factor cannot have a nonzero null vector: its existence
would imply ||w||<=tau*K_A*||w||<||w||. This proves the endpoint
Jacobian assertion. The exterior and a neighborhood of every strip
boundary point are unchanged. Equations (24)-(27) give E_tau>=3e/4
and I_tau>=-e/4, proving (8) for every stated finite endpoint.

The failure is specifically that the fixed shear's positive cost
persists while its useful interface term is quadratic in the small
first trace. Taking that trace sufficiently small is not a descent
mechanism. A family changing its shear and support together is not
covered by a uniform e here. No assertion about that untested family
or an arbitrary finite replacement follows.

## Mathlib

Full matching coverage for this finite conditional shear comparison
and supporting coverage for the constrained pullback and boundary
integration have not been checked. No Mathlib theorem is imported,
and no absence claim is made. The proof is informal and unaudited;
the compact estimates and endpoint checks are analytic, with no
mathematical script, numerical certificate or Lean verification.
