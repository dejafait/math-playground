# Lemma 891: a balanced shrinking two-component profile still increases full mass

## Hypotheses

Use L847's actual entire function, positive constants and full density:

\[
G(z)=\tfrac18\xi(\tfrac12+\tfrac{\sqrt z}{2}),\quad
R>0,\quad RG'(R)/G(R)=1,\quad C=R^2/G(R)^2,
\]
\[
F(z_1,z_2)=-C\frac{G(z_1)G(z_2)(z_1-z_2)^2}{z_1^2z_2^2},
\quad z_j=R e^{u_j+iy_j},\quad
J=\det(I-iDu),\quad Q=F(z_1,z_2)J,
\quad \mathcal B(u)=(2\pi)^{-2}\int_{T^2}|Q|.             \tag{1}
\]

Assume L879's smooth real periodic u, nowhere-zero J and stationarity
under smooth real radial variations supported away from {Q=0}.
Use its phase-line conclusion Q=lambda*s, with |lambda|=1 and smooth
real s. Condition on the approved clean lifted strip

\[
S=(l,r)\times(c,d),\qquad l<\alpha<\beta<r,              \tag{2}
\]

whose compact closure lies in an angular chart. Its only density zeros
are the complete simple G(z1)-zero fibers x=alpha,beta. The factors
G(z2), z1-z2 and J are nonzero on its closure. On each fiber
z1=zeta_gamma is a fixed simple zero and partial_y u1=0.

For this particular test impose the additional slope restriction at
one y0 in (c,d):

\[
Du(\gamma,y_0)=A_*:=\begin{pmatrix}1&0\\0&1\end{pmatrix}
\quad(\gamma=\alpha,\beta).                             \tag{3}
\]

Thus p=u1,x=1, k=u2,y=1, n=u2,x=0 at both nominated points.
Neither (2), (3), nor an actual stationary graph realizing them is
asserted to exist. In particular (3) is not deduced from stationarity.
No condition on Du away from these two points is imposed beyond (1)-(2).

Define one fixed smooth compact profile, including all its transitions:

\[
\eta(t)=\begin{cases}\exp[-t^2/(1-t^2)],&|t|<1,\\0,&|t|\ge1,
\end{cases}\qquad
\chi(X,Y)=\eta(X)\eta(Y),\qquad V=(\chi,-Y\chi).          \tag{4}
\]

For small positive epsilon set

\[
v_\epsilon(x,y)=\epsilon\sum_{\gamma=\alpha,\beta}
 V\left(\frac{x-\gamma}{\epsilon},
         \frac{y-y_0}{\epsilon}\right),\qquad
u_\epsilon=u+v_\epsilon.                                \tag{5}
\]

The two supports will be disjoint and compactly contained in S.
They do not span the intervening cell. Both amplitudes and both support
widths shrink together; DV has fixed, nonzero size. This is not a
uniform application of a fixed-field small-amplitude expansion.

## Conclusion

There is a positive, data-dependent epsilon_* specified below such
that every 0<epsilon<=epsilon_* gives a smooth real periodic endpoint
(5), equal to u near and outside the whole strip boundary, with
det(I-iDu_epsilon) nowhere zero. If

\[
h_\gamma=\partial_xs(\gamma,y_0),\qquad
H=|h_\alpha|+|h_\beta|>0,
\]

then its complete mass satisfies

\[
\boxed{\displaystyle
\mathcal B(u_\epsilon)-\mathcal B(u)
   \ge \frac{\epsilon^3 H}{2520(2\pi)^2}>0.}             \tag{6}
\]

The normalized leading full-mass coefficient m for each fiber obeys
m>1/1260. Its signed-cell contribution is -K3/6<0, where
K3=integral_{-1}^1 eta(Y)^3 dY. The nonnegative phase cost pays more
than this negative contribution. The corresponding actual signed-cell
change is also negative for the stated epsilon_*.

All cutoff collars, the full determinant, all new numerator zeros and
the actual-G remainder are included. This stops only the balanced
profile (4)-(5) under the explicit slope restriction (3), for sufficiently
small finite epsilon. It does not stop other slopes, other compact
profiles, finite changes across the intervening cell or arbitrary
replacements. It does not exclude the paired configuration from a
minimizer, establish realization or compactness, prove L868's sharp
bound, higher signs or RH. This is an unaudited conditional
specialization, classified REPRODUCTION; no certified originality or
progress beyond the checked sources is claimed.

## Proof

### Assessed scope and the elementary specialization

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-07-paired-fiber-finite-replacement-test.md`.
It covers finite changes of both components on this conditional strip,
with the full mass and an independently checked finite endpoint. Reuse
its primary-source comparison of Scott Lawrence and Yukari Yamauchi,
*Convex optimization and contour deformations*, arXiv:2311.13002v2,
14 August 2024,
[Section III, (18)-(19), p5](https://arxiv.org/pdf/2311.13002v2#page=5).
The known method bounds mass by dominated signed forms. Here the
elementary inequality |q|>=sign(X) Re(q) is applied on each half-square;
the signed integral change is retained explicitly. No single global
calibration, perfect-contour existence or attainment theorem is imported.

L847 supplies (1) including the complete determinant, and L879 supplies
the phase line. Taylor's theorem with integral remainder and the
fundamental theorem of calculus are the standard named analytic inputs.
The computation below is the application difference for one fixed
profile at a shrinking scale, not a reproof of a general contour theorem.
In particular it uses neither a boundary identity from unaudited L889
nor L890 as a mathematical premise. Their pinned/small-trace/fixed-shear
stops, L887's fixed-field logarithm and attempt65/69 were compared before
work and retain their scopes. None evaluates (4)-(5).
The slopes in (3) are a deliberate boundary test: p=1 lies outside
L889's strict |p|<1 positive box, while the balanced second component
has derivative -1 at the central trace. The negative signed term below
is retained. The two components have the same amplitude scale, so the
test does not merely send the first amplitude to zero after a fixed
second field. These observations are comparisons, not extra premises.

### The full contact model and its determinant

At either contact F=0 and F_z2=0. Simplicity and the other nonvanishing
factors give F_z1(zeta_gamma,z2(gamma,y0))!=0. Therefore

\[
\lambda h_\gamma
 =F_{z_1}(\zeta_\gamma,z_2(\gamma,y_0))\zeta_\gamma
                          (1+i)J_*,\qquad J_*=(1-i)^2=-2i.
                                                               \tag{7}
\]

All factors on the right are nonzero, proving h_gamma!=0. This checks
the normalization rather than replacing an actual G zero by a model.
The actual-data remainder is controlled separately below.

Put phi=chi+Y*chi_Y and let j=det(I-i(A_*+DV)). Its four derivative
entries are 1+chi_X, chi_Y, -Y*chi_X, 1-phi, so, exactly,

\[
j=r_0+i t_0,\quad
r_0=\phi-(1-\chi)\chi_X,\quad
t_0=-2+\phi-\chi_X,\quad r_0-t_0=2+\chi\chi_X.          \tag{8}
\]

For a determinant bound on the entire closed square K=[-1,1]^2, set
T=1/(1-X^2)>=1 for |X|<1. Direct differentiation gives

\[
|\eta(X)\eta'(X)|
 =2T^{3/2}\sqrt{T-1}\,e^{2-2T}
 \le\frac{3\sqrt3}{2e}<1.                               \tag{9}
\]

For clarity, the logarithmic derivative for T>1 is
3/(2T)+1/[2(T-1)]-2; its numerator is -4T^2+8T-3.
The only critical point in (1,infinity) is T=3/2, where the maximum
is the displayed value; the expression tends to zero at both ends.
The strict last inequality follows from e>8/3 and 243<256.
The endpoints follow by smooth extension. Since 0<=eta(Y)<=1,
|chi*chi_X|<1. Thus (8) proves, everywhere on K,

\[
|j|\ge\frac{|r_0-t_0|}{\sqrt2}>\frac1{\sqrt2}.          \tag{10}
\]

No cutoff derivative or possible Jacobian zero was discarded.

By (7) the leading density divided by epsilon*lambda*h_gamma is

\[
q(X,Y)=\frac{(1+i)X+\chi}{1+i}\frac{j}{-2i}
       =\frac{\chi+i(2X+\chi)}4(r_0+i t_0).              \tag{11}
\]

The original leading density in this normalization is X. In particular

\[
\operatorname{Re}q
 =X+\frac\chi2+\frac{\chi^2\chi_X}4
            +\frac{X\chi_X}2-\frac{X\phi}2.             \tag{12}
\]

### A rigorous full-integral margin, with a negative signed term

All integrals in this paragraph are over the full square K unless
specified otherwise. Set K_j=integral_{-1}^1 eta(Y)^j dY and

\[
m=\int_K(|q|-|X|),\quad
E=\int_K(|q|-\operatorname{sgn}(X)\operatorname{Re}q)\ge0,
\quad I=\int_K\operatorname{sgn}(X)(\operatorname{Re}q-X).
                                                               \tag{13}
\]

The value of sgn(0) is immaterial. These are finite continuous or
bounded piecewise continuous integrands, and m=E+I exactly.
In (12), chi is even and chi_X is odd in X. The chi/2 and X*chi_X/2
terms therefore contribute zero to I. The chi^2*chi_X/4 term gives
-eta(Y)^3/6 after the X integral, by differentiating chi^3/3.
Finally phi=partial_Y(Y*chi), whose Y integral vanishes. Hence

\[
                         I=-K_3/6<0.                    \tag{14}
\]

For 0<a<1 let T_a=[-a,0]x[-1,1]. On this rectangle
|q|+Re q>=2 Re q, and the phase-cost integrand is nonnegative on
its complement. Consequently E>=2 integral_{T_a} Re q. The complete
integration of (12) on T_a is

\[
\int_{T_a}\operatorname{Re}q
 =-a^2+\frac{a\eta(a)K_1}{2}
                   +\frac{(1-\eta(a)^3)K_3}{12}.         \tag{15}
\]

Indeed the terms (chi+X*chi_X)/2 are partial_X(X*chi)/2,
the cubic term is partial_X(chi^3)/12, and the phi term has zero
Y integral, including its boundary. These checks account for every
term and all transitions of (4). Combining (13)-(15) gives

\[
m\ge -2a^2+a\eta(a)K_1-\eta(a)^3K_3/6.                 \tag{16}
\]

Here are explicit elementary bounds sufficient for a=1/4:

\[
\eta(1/4)=e^{-1/15}>14/15,\qquad
\eta(1/4)^3=e^{-1/5}<5/6,\qquad
K_3\le32/35,\qquad K_1>13/12.                           \tag{17}
\]

The first two follow from e^{-t}>1-t and e^t>1+t for t>0.
For 0<=b<1, -log(1-b)=integral_0^b (1-s)^{-1}ds<=b/(1-b).
Taking b=Y^2 yields eta(Y)<=1-Y^2. Thus
K3<=integral_{-1}^1(1-Y^2)^3 dY=32/35.

To verify the last bound without quadrature, the exponential series
gives 8/3<e<11/4. For the upper bound, its terms through order four
sum to 65/24; its remaining positive tail is at most
(1/120)/(1-1/6)=1/100, and 65/24+1/100<11/4.
Its terms through order five at 11/10 sum to more than 3, so
log 3<11/10. On [0,1/2], eta(t)>=1-t^2/(1-t^2), and therefore

\[
2\int_0^{1/2}\eta(t)dt\ge2-\log3>9/10.                 \tag{18}
\]

The bump is decreasing for t>=0. On [1/2,2/3], eta>2/5:
e^{4/5}=e/e^{1/5}<(11/4)/(6/5)=55/24<5/2.
On [2/3,3/4], eta>1/4: the positive exponential series gives
e^{2/7}<1/(1-2/7)=7/5, hence e^{9/7}<77/20<4.
On [3/4,13/16], t^2/(1-t^2)<=169/87<2 and
e^2<(11/4)^2<8, so eta>1/8. Including the reflected intervals,

\[
K_1>\frac9{10}+\frac2{15}+\frac1{24}+\frac1{64}
       =\frac{349}{320}>\frac{13}{12}.                   \tag{19}
\]

Inserting (17) into (16) at a=1/4 proves the strict margin

\[
m> -\frac18+\frac14\frac{14}{15}\frac{13}{12}
                  -\frac16\frac56\frac{32}{35}
       =\frac1{1260}>0.                                 \tag{20}
\]

This is a lower bound for the full mass coefficient, not merely
for its trace term. It uses no numerical evidence.

### Uniform actual-G remainder and the finite endpoint

Choose epsilon_0>0 so small that the two closed squares of radius
epsilon_0 about (gamma,y0) are disjoint and lie inside S. For example,
one quarter of the minimum of alpha-l, r-beta, beta-alpha, y0-c,
d-y0 and 1 suffices. For gamma fixed and (X,Y) in K define

\[
w_{\gamma,\epsilon}=(\gamma+\epsilon X,y_0+\epsilon Y),
\quad Z_j^v=R\exp\{u_j(w_{\gamma,\epsilon})
                     +\epsilon V_j(X,Y)+i(w_{\gamma,\epsilon})_j\},
\]
\[
Q_\gamma^v(\epsilon,X,Y)
  =F(Z_1^v,Z_2^v)
       \det(I-i[Du(w_{\gamma,\epsilon})+DV(X,Y)]).        \tag{21}
\]

Let Q_gamma^0 be the same expression with V=DV=0. All these functions
are smooth on [0,epsilon_0]xK. The image lies in compact annuli in
(C*)^2; F is holomorphic there, including its numerator zeros.
At epsilon=0 both densities vanish. Differentiating (21), F=F_z2=0
eliminates every term except the derivative in Z1, so (7) gives

\[
\partial_\epsilon Q_\gamma^v(0,X,Y)=\lambda h_\gamma q(X,Y),
\qquad
\partial_\epsilon Q_\gamma^0(0,X,Y)=\lambda h_\gamma X.   \tag{22}
\]

Define the finite constants

\[
M_\gamma=\frac12\sup_{[0,\epsilon_0]\times K}
 (|\partial_\epsilon^2Q_\gamma^v|
                      +|\partial_\epsilon^2Q_\gamma^0|),
\qquad M=M_\alpha+M_\beta,
\]
\[
j_\gamma(\epsilon,X,Y)
   =\det(I-i[Du(w_{\gamma,\epsilon})+DV]),\qquad
L=\max_\gamma\sup_{[0,\epsilon_0]\times K}
                       |\partial_\epsilon j_\gamma|.   \tag{23}
\]

Taylor's integral remainder, uniformly on the entire K, gives

\[
|Q_\gamma^v-\epsilon\lambda h_\gamma q|
 +|Q_\gamma^0-\epsilon\lambda h_\gamma X|
                         \le M_\gamma\epsilon^2.        \tag{24}
\]

Applying ||z|-|w||<=|z-w| and the exact physical area factor epsilon^2
to (24), the contribution from each complete square differs from
epsilon^3*|h_gamma|*m by at most 4 M_gamma epsilon^4. Outside those
squares the graph is unchanged, including its density zeros. Hence

\[
(2\pi)^2[\mathcal B(u_\epsilon)-\mathcal B(u)]
       \ge\epsilon^3H/1260-4M\epsilon^4.                \tag{25}
\]

For the determinant, j_gamma(0,X,Y)=j(X,Y). Equations (10),(23) give
|j_gamma(epsilon)-j|<=L*epsilon throughout K. There is no inference
from a sampled determinant minimum. Choose

\[
\epsilon_* =\min\left\{\epsilon_0,
 \frac1{4(1+L)},\frac{H}{10080(1+M)},
                     \frac{HK_3}{48(1+M)}\right\}>0.    \tag{26}
\]

For every stated epsilon, the deformed determinant on the squares
has modulus greater than 1/sqrt(2)-1/4>1/4. It equals the original
nonzero J outside. Formula (25) then proves (6).

For completeness, the signed-cell statement has the same actual-data
error. The original signs in each square are sgn(h_gamma)*sgn(X),
since the only contact is its simple fiber. Multiply the real part
of (24) by this sign and integrate. By (14), the unnormalized signed
change I_epsilon satisfies

\[
|I_\epsilon+\epsilon^3HK_3/6|\le4M\epsilon^4.
\]

The last bound in (26) implies I_epsilon<=-epsilon^3 H K3/12<0.
Subtracting these signed integrals from the modulus integrals gives
the nonnegative phase cost on the original signed cells. Thus even
the actual negative signed contribution is outweighed by full mass.

The standard bump (4) is smooth and flat at |X|=1 or |Y|=1, so (5)
extends by zero smoothly and periodically and leaves a neighborhood
of the whole strip boundary unchanged. New numerator zeros need not
be classified: (21)-(25) hold at them. No division by a varying density,
interchange of infinite integrals, passage to a singular limiting
graph or intermediate-homotopy invertibility is used.

### Verification and limitations

Reproduction command for the finite rational checks in (9),(17)-(20):

`python3 scripts/actual-g-radial-graph/common_scale_exact_checks_79.py`

Its complete arithmetic certificate is
`scripts/actual-g-radial-graph/common-scale-exact-checks-79.json`.
It checks only the displayed rational arithmetic, not the analytic
proof, existence of conditional data or actual-data constants (23).

The earlier diagnostic command
`python3 scripts/actual-g-radial-graph/common_scale_profile_79.py`
writes `scripts/actual-g-radial-graph/common-scale-profile-diagnostic-79.json`.
It suggests m about 0.590534, but its floating quadrature and sampled
Jacobian are not verification and are not used anywhere in (6)-(26).

The certified analytic threshold is m>1/1260; the desired descent
would require a negative full coefficient or another finite comparison.
The conclusion remains restricted to (3)-(5). In particular it is
not a universal shrinking-support obstruction or an actual-G example.

## Mathlib

Full matching coverage for this conditional scaled replacement, and
supporting formal coverage for these compact Taylor bounds and profile
integrals, have not been checked. No Mathlib theorem is imported and
no absence is asserted. This is an informal, unaudited proof with
finite arithmetic checks, not a Lean verification.
