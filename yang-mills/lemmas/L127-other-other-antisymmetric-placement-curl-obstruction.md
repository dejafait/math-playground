# L127 — The retained antisymmetric placement is not universally curl-only

## Hypotheses

Import L126(1)--(3), L125(1)--(3), L123(1)--(2), L118(4)--(9)
and L113(1)'s original path-label signs. Their actual coefficient scope
is SU(2), both L010 probes i=3,6, the straight lower-rooted direction-1
forest, relative all-face fixed-link box D=(-4,4)^4, admitted even N,
a=8/N, tau=1/16, and the bare small-coupling coefficient at fixed mesh
before refinement. These coefficient limits and their full axial/heat
tails are imported; no new mesh limit is taken here. L120(2)'s actual
prefix fields and its constant axial mode remain in those coefficients.

The calculation below tests a **universal stencil identity**. In this
separate test, replace an exterior field by any real smooth transverse
vector V, using exactly the same path limits
phi_(pi,b)=V_mu+V_nu, phi_(pi,q)=-V_mu+V_nu. Use the same universal
M^- tensor, complete ordered generator list and L123's local expression
with h=curl V. Test vectors, symmetric bilinear coefficients and a compact
displacement may be freely selected for this identity test. They are not
asserted to be the two actual probe mode sums or L007's fixed displacement.
An obstruction in this enlarged test space only rejects a universal
identity; it need not obstruct a further identity on the actual fields.

All torus integrals have normalized measure on [-pi,pi]^3. The derivative
of a symbol is a frequency derivative, whereas a derivative of V is a
physical derivative. Work in the plaquette order (23),(24),(34).

## Conclusion

Let L_(alpha,a) be the real coefficients phi_alpha(V)=sum_a
L_(alpha,a) V_a, a=2,3,4. Sum **both** ordered generators with
rho(r)=2, and define the physical-component tensor entry

 T=sum_(r:rho(r)=2) sum_(alpha,beta)
          L_(alpha,2) M^-_(r,3;alpha,beta) L_(beta,3).       (1)

No plaquette plane or path type is omitted from (1). Then T=tau, where

 tau=-integral eta_2^2 eta_3^2 d_4^2/lambda
       [d_3^2+(d_3^2-d_4^2)(d_2^2+d_4^2)/(2 lambda)],
 lambda=d_2^2+d_3^2+d_4^2, d_a=2 sin(theta_a/2),
 eta_a=cos(theta_a/2),                                      (2)

and the complete integral satisfies the strict bounds

                         7/1000 < tau < 1/100.             (3)

The proof uses exact integer interval arithmetic and a rigorous full
midpoint quadrature bound. It requires no binary floating-point or libm
accuracy assumption; displayed decimal summaries are not the certificate.

Consequently L126's antisymmetric derivative term plus L123's K_f cannot
universally be replaced by expressions bilinear in V and curl V, with
L126's H contribution held fixed and with no new displacement-derivative
term. A curl-free symmetric jet already retains (1). Compact curl-free
fields give the explicit integrated test in proof section 6.

H remains present with its original sign. This conclusion neither removes
nor evaluates H, and does not rule out cancellations involving H, other
physical-component entries or the actual constrained mode sums. No value
or sign of either actual-probe coefficient, K_(i,oo)+4 gamma D_i, or the
complete response is established. All other L124 terms, its single
outside factor 3, and L084's reference and arithmetic qualifications
remain. Finer powers/logarithm, other jets, matching, interacting error
<=c_box/2, continuum axioms, reflection positivity, infrared control and
finite positive mass remain unresolved.

## Proof

### 1. Substitute the complete projected exterior paths

Use L118's component-center phases. Its exact paths and L113's signs
show that for a real vector v,

 F(v)=sum_alpha phi_alpha(v) (S_alpha)_c,
 P_c F(v)=d f(v)^T/lambda,
 f(v)_(mu nu)=2[d_nu eta_mu v_mu-d_mu eta_nu v_nu],
 F(v)^* P_c F(w)=f(v) f(w)^T/lambda.                       (4)

Indeed P_c annihilates the imaginary circulation part of each S_alpha
separately. The remaining edge column in plane mu nu is
2[-eta_nu v_nu e_mu+eta_mu v_mu e_nu]; applying d d^T/lambda
proves (4). Thus every path pair and every plane is retained before
we select a physical-component tensor entry.

L125(9) tracks the derivative of the plaquette phase explicitly. Its
phase commutator has imaginary odd trace against each real even
Q_(alpha,beta),c and integrates to zero. Linear combinations (4) have
the same property, including their antisymmetric combination. Therefore
we may calculate (1) using centered derivatives only **after** that
integrated phase check. No frequency integration by parts of an
individual nonperiodic centered entry is made.

### 2. Differentiate both generators and all three planes

Put x=d_2, y=d_3, z=d_4, A=eta_2, B=eta_3, C=eta_4, L=x^2+y^2+z^2.
Use the real circulation matrix Z with D_c=i Z and set

 n=(z,-y,x)^T, S=I-n n^T/L,
 v=(y,z,0)^T, w=(-x,0,z)^T, t=(0,x,y)^T.

L118(9) gives for the complete displacement-2 generator

 G=i Bmat,
 Bmat=A[-B^2 w e_(23)^T+C^2 t e_(24)^T] S.                 (5)

The first term is output 3, plane (23); the second is output 4,
plane (24), both with positive ordered sign. Its three output
plaquette rows include (34). The exterior columns are f(e_2)=2A v,
f(e_3)=2B w by (4); their (24) and (34) entries are retained.

Let a prime denote partial_(theta_3). Then y'=B, B'=-y/4,
A'=C'=x'=z'=0. Also S v=v, S w=w, and differentiation of these
identities gives

 S'v=(I-S)v'=B z n/L,                  S'w=0.             (6)

In (6) v'=B e_(23), while w is constant under this derivative.
Since w dot t=zy and |w|^2=x^2+z^2, (5)--(6) give

 f(e_3)^T Bmat' f(e_2)
   =4 A^2 B^2 [ y^2(x^2+z^2)/2+C^2 z^2
                -z^2{B^2(x^2+z^2)+C^2 y^2}/L ],
 f(e_2)^T Bmat' f(e_3)=2 A^2 B^2 x^2 y^2.                 (7)

For completeness the first differentiated column equals

 Bmat' f(e_2)
   =2 A^2 [B y^2 w/2+C^2 B z e_(34)
                  +B z(-B^2 z w-C^2 y t)/L];
 Bmat' f(e_3)=-A B^2 x y w.

These verify (7) directly without a symbolic or numerical inference.
Using C^2-B^2=(y^2-z^2)/4, subtraction simplifies to

 f(e_3)^T Bmat' f(e_2)-f(e_2)^T Bmat' f(e_3)
    =2 A^2 B^2 z^2 [y^2+(y^2-z^2)(x^2+z^2)/(2L)].         (8)

The i in L125's moment formula and G=i Bmat supply a minus sign.
The antisymmetrization supplies 1/2, and (4) supplies 1/L.
Equation (8) therefore proves (2). Its integrand is O(|theta|^2)
near zero and bounded away from zero, so it is absolutely integrable.
Assigning the value zero at zero frequency is harmless. There is no
color factor or outside group factor in this calculation.

### 3. Integrate one angle exactly before certification

Write X=x^2, Y=y^2, Z=z^2, k=X+Z, so A^2=1-X/4, B^2=1-Y/4.
For k>0 the elementary integrals over theta_3 are

 J0=integral 1/(k+Y)=1/sqrt(k(k+4)),
 J1=integral 1/(k+Y)^2=(k+2)/[k(k+4)]^(3/2).              (9)

The substitution t=tan(theta_3/2) gives
J0=(1/pi) integral_R dt/[k+(k+4)t^2], which evaluates to the first
formula. Differentiate under the integral at fixed k>0 to obtain J1;
the positive lower bound k justifies that differentiation.

Let I=-tau. Set U0=integral B^2/(k+Y)=(1+k/4)J0-1/4 and
U1=integral B^2/(k+Y)^2=(1+k/4)J1-J0/4. Substitution in (2) gives

 integral_(theta_3) B^2 Z/(k+Y)
           [Y+(Y-Z)k/(2(k+Y))]
       =Z[1-k U0-k(k+Z)U1]/2.

Use (9) to conclude

 I=normalized integral_[0,pi]^2 F(theta_2,theta_4),
 F=(1-X/4) Z/8
       [k+4-(k^2+6k+2Z)/sqrt(k(k+4))].                   (10)

The reduction from the two full circles to [0,pi]^2 uses their even
cosine dependence, with the corresponding normalized measure 1/pi^2.
The one point k=0 is assigned F=0 by continuous extension.

### 4. Bound the full midpoint error, including the origin

Here X,Z are in [0,4], k in [0,8]. For k>0 put
R=[k(k+4)]^(-1/2), N=k^2+6k+2Z and J=k+4-NR.
Elementary differentiation gives

 R<=1/(2 sqrt(k)), |R'|<=1/(2 k^(3/2)),
 0<=R''<=1/k^(5/2), N<=16k,
 N_X<=22, N_Z<=24, N_XX=N_ZZ=2.

For R'', use (log R)'=-[1/k+1/(k+4)]/2 and
(log R)''=[1/k^2+1/(k+4)^2]/2. Hence the following convenient bounds
hold (35>12+8 sqrt(8)):

 |J|<=35, |J_X|<=1+19/sqrt(k), |J_Z|<=1+20/sqrt(k),
 |J_XX|<=1/sqrt(k)+38/k^(3/2),
 |J_ZZ|<=1/sqrt(k)+40/k^(3/2).

Since F=(1-X/4)Z J/8, these imply

 |F_X|<=Z[39/4+19/sqrt(k)]/8,
 |F_XX|<=Z[1/2+(21/2)/sqrt(k)+38/k^(3/2)]/8,
 |F_Z|<=79/8,
 |F_ZZ|<=[2+44/sqrt(k)+40Z/k^(3/2)]/8.

The angle derivatives obey (X')^2<=4X, (Z')^2<=4Z and
|X''|,|Z''|<=2. Use XZ<=16, XZ/sqrt(k)<=6,
XZ/k^(3/2)<3/4, Z/sqrt(k)<=2 and Z^2/k^(3/2)<=2 to obtain

 |partial_(theta_2)^2 F|
    <=4+(21/4)6+19(3/4)+39/4+19/2=69<70,
 |partial_(theta_4)^2 F|
    <=4+44+40+79/4=431/4<108.                            (11)

These bounds extend to the corner k=0. More explicitly the nonsmooth
part of F is a constant times Z N R. Near that corner k is comparable
to theta_2^2+theta_4^2; this part and its angle derivatives through
order two are O(r^3), O(r^2), O(r), respectively, by the same R
bounds and chain rule. It therefore extends C^2 with zero derivatives
through order two. The polynomial part of F is smooth. Other corners
have k>0. This justifies the C^2 midpoint theorem on the closed square.

Apply the one-dimensional midpoint remainder separately in each angle,
and average the error in the other angle. At n equal panels per angle,
for the normalized integral the error is at most

 pi^2(70+108)/(24 n^2) < 1780/(24 n^2).                  (12)

The bound pi^2<10 follows, for example, from the exact pi interval
constructed in the certificate (its upper bound is <22/7).
No corner or omitted spectral/angle region is excluded in (12).

### 5. Exact arithmetic enclosure and complete evidence

Reproduction command, from the active notebook:

    python3 scripts/combined-ward-response/check_joint_curl_tensor.py
    python3 scripts/combined-ward-response/check_joint_curl_tensor.py --audit

Full certificate: scripts/combined-ward-response/joint-curl-tensor-certificate.json.
The script uses scale Q=10^30 and intervals [l/Q,h/Q]. Addition and
subtraction are exact. Multiplication rounds the minimum and maximum
of the four integer endpoint products outward by floor/ceiling division
by Q. Division uses the four integer endpoint quotients and a strictly
positive denominator. Square roots use integer isqrt(l Q), and the
ceiling of sqrt(h Q), with an exact square test. Thus every operation
is an inclusion, using arbitrary-precision integers only.

The pi interval comes from Machin's formula
pi=16 atan(1/5)-4 atan(1/239), enclosing each arctangent by the two
successive alternating-series sums with 60 and 20 terms. The formula
can also be verified directly: tan(4 atan(1/5))=120/119, subtraction
of atan(1/239) gives tangent 1, and the resulting angle is in (0,1),
hence is pi/4 (using the elementary bound pi>2). The alternating
series bounds place it in that range. Each midpoint angle is then enclosed by integer interval
multiplication. The cosine Taylor polynomial through degree 94 has
remainder at most 4^96/96! for angles below 4. Interval recurrence
bounds the polynomial; intersecting with [-1,1] is valid. It follows
that all 256 X-node intervals enclose their true 2-2cos(theta) values.
They are strictly positive, so every square root and divisor in (10)
has a verified positive lower bound.

All 65,536 midpoint records, every input-node interval, the full total,
exact rational final bounds and the 27 exact complete-plane matrix
checks are saved. The latter checks compare (7)--(8)'s matrix derivative
with (2)'s integrand at rational d,eta satisfying eta^2+d^2/4=1; every
residual is zero. They supplement the analytic algebra, not replace it.
All midpoint operations use the formula (10) with the outward rules
above, and the final error is the exact rational 445/393216 from (12).
The complete certificate reports no failures. Its exact final interval
implies

 0.0072335960 < tau < 0.0094969831,

where these deliberately weakened decimal endpoints follow by rational
comparison; in particular (3) follows. The complete /bounds and
/exact_stencil_checks values and empty /failures were inspected. The saved-record
audit replays every input, every midpoint interval and the complete aggregation;
it passes with no failures and is saved in
scripts/combined-ward-response/joint-curl-tensor-audit.json. This checks
full saved-record integrity using the same implementation, not an independent
processor or independently implemented mathematical verification. The
printed floating approximations do not enter the certificate. Earlier
uncertified midpoint diagnostics near -0.00836529 for I were used only
to select a feasible quadrature size, not in the bound or sign proof.

### 6. A curl-free test and the precise failed shortcut

Choose a compact set in D with positive distance from every face and
smooth chi equal to one on a neighborhood of that set. Let
V_l=grad_T(x_2 chi), V_k=grad_T(x_3^2 chi/2). On that neighborhood
V_l=e_2, V_k=x_3 e_3 and the only nonzero derivative of V_k is
partial_3 V_(k,3)=1. Both fields are globally transverse gradients,
so both transverse curls vanish. Take the symmetric test coefficients
c_lk=c_kl=1/2 and the two diagonal coefficients zero; take a smooth
nonnegative nonzero test displacement u_2 supported in that set and
u_3=u_4=0. These are tests of the universal identity, not actual probes.

In L126's antisymmetric contribution the derivative on V_l is zero
on that support. Therefore the full label sum is, by (1)--(3),

               (tau/2) integral_D (x_1+4) u_2 dx > 0.     (13)

L123's beta_k and beta_l are zero because h_k=h_l=0, so its entire
K_f mixed expression vanishes. Any universal replacement of the sum
by bilinear expressions in V and curl V would also vanish in this
test, contradicting (13). The result keeps H fixed. Spatial integration
by parts could transfer terms to a changed displacement-derivative
tensor; this proof makes no claim excluding that different regrouping.
Nor does it assign (13) to the actual c_(i;kl) or actual displacement.

The calculation is RESEARCH / REPRODUCTION under the unchanged EXPLORE
assessment drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
Canonical coefficient limits, projection/path/generator formulas and
phase qualifications are imported at the equation references above.
The finite specialization and the exact quadrature are needed because
no inspected source evaluates this isolated coefficient or its physical
jet test. This is local standard-method obstruction evidence, with no
originality claim beyond the checked sources. L124's complete comparison
still requires all retained coefficients and actual heat-weighted fields.

## Mathlib

Full matching tensor/curl obstruction: **not checked**. Supporting
orthogonal projections, weak Fourier derivatives, elementary integrals,
midpoint remainder and integer interval arithmetic: **not checked**.
Unknown coverage is not evidence of absence. The proof and exact
certificate are given here; no numerical sign is assumed from a preview.
