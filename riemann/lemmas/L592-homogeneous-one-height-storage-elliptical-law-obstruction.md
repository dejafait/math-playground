# Lemma 592: a universal comparison law obstructs homogeneous one-height storage

## Hypotheses

Use the ordinary coordinates and the exact spectral data of L586:

    v=(x_0,y_0,z_0,x_1,y_1,z_1),
    w=(x_0,y_0,x_1,y_1),        dot_w=(y_0,z_0,y_1,z_1),
    I=[-1/2,1/2],
    A_((r,j),(s,k))(u)=Re((iu)^j(-iu)^k exp(i(r-s)u)),
    K=integral_I A(u) du,
    C_I={finite sums sum_l alpha_l A(u_l):alpha_l>=0, u_l in I},
    Q(v)=max(0,x_0 z_0-y_0^2).

Here r,s belong to {0,1}, j,k belong to {0,1,2}, and the coordinate
order in K is the displayed order of v. For a real smooth P-periodic
function h, P>0, set

    J_h(t)=(h(t),h'(t),h''(t),h(t+1),h'(t+1),h''(t+1)),
    C(h)=P^(-1) integral_0^P J_h(t)J_h(t)^T dt.

Let S be any real symmetric four-by-four matrix, let W(w)=w^T S w,
and let U:R^2 -> R be globally C1 with

    U(a x,a y)=a^2 U(x,y) for every a>0 and every (x,y) in R^2.

No evenness, convexity, C2 regularity or sign condition is imposed.
Define

    V(w)=W(w)+U(x_0,y_0),
    D V(v)=gradient W(w) dot dot_w
            +U_x(x_0,y_0)y_0+U_y(x_0,y_0)z_0.

Suppose H is a real symmetric six-by-six matrix satisfying both
global branches, including the origin and every v in R^6:

    v^T H v-D V(v)>=0,
    v^T H v-D V(v)-(x_0 z_0-y_0^2)>=0.                         (1)

For the sufficient periodic upper-bound application also impose

    trace(H A(u))>=0 for every u in the closed interval I.      (2)

The trace is the full matrix trace. No common compact state domain,
stationary-process realization, fixed period, lag commensurability,
cone-closure substitute or dual attainment is assumed. Only L473's
finite-matrix facts and extension template are used, not its arithmetic
moment inputs or corrected height-dependent law.

## Conclusion

There is one bounded, centered probability measure mu on R^6,
independent of U,S,H, such that

    integral vv^T dmu=K,
    integral Q(v) dmu=1/(36pi),
    integral [U_x(x_0,y_0)y_0+U_y(x_0,y_0)z_0] dmu=0          (3)

for every U in the hypotheses. Every permitted quadratic W also has
integral D W dmu=0. All these integrals are absolutely convergent.
Consequently every triple H,S,U satisfying (1) has

    trace(HK)>=1/(36pi)>1/288,
    1/(36pi)-1/288=(8-pi)/(288pi)>0.                          (4)

For each smooth periodic h with K-C(h) in C_I, (1)--(2) do provide
the sufficient bound average Q(J_h)<=trace(HK). But (4) prevents
every certificate in this entire W+U class from costing less than
1/288, even before condition (2) is imposed.

This is an obstruction to the specified certificate class, not an
optimum, a periodic occupation law, a stationary-process construction,
or an actual-Xi sign statement. General periodic clipping, storage
depending nonlinearly on both heights, finite-cone reserve,
fourth/probability assembly and controlled nonlinear Xi transfer are
not decided. The local construction is a specialization under the
prior SPECIALIZE assessment, not a certified novelty claim beyond the
sources checked. The separate conceptual audit in Section 6 passes
without a mathematical correction; the source manuscripts themselves
are not critically audited here.

## Proof

### 1. Imported sufficient method and the whole class's growth

Reuse the sufficient pointwise-dual/zero-flux method of A. Chernyavsky,
J. J. Bramburger, G. Fantuzzi and D. Goluskin,
*Convex relaxations of integral variational problems: pointwise dual
relaxation and sum-of-squares optimization*,
[arXiv:2110.03079v1, Lemma 2.1 and (2.4)--(2.11), printed pp.8--10](https://arxiv.org/pdf/2110.03079v1),
and the C1 field and integrable chain-rule formulation of G. Fantuzzi,
*Verification of some functional inequalities via polynomial
optimization*,
[arXiv:2201.00362v1, Section 3.1, Lemma 5 and (7)--(10), PDF p.3](https://arxiv.org/pdf/2201.00362v1).
The invocation-start assessment
`drafts/literature/2026-10-31-general-homogeneous-storage-scope.md`
records the primary hypotheses and the prior sufficient-method proof
cases. No sharpness or converse theorem is imported. Neither source
supplies the measure (3); only applicability to the changed field
class and the local obstruction are proved here.

Positive homogeneity at the origin gives U(0)=0. Differentiability
there and U(tp)/t=t U(p) for t>0 show that the derivative at zero
vanishes on every p, so gradient U(0)=0. Differentiating the
homogeneity identity in p gives

    gradient U(a p)=a gradient U(p) for a>0.

Continuity on the unit circle supplies finite constants

    M_0=max_|p|=1 |U(p)|,       M_1=max_|p|=1 |gradient U(p)|.

For every p, including p=0, this proves

    |U(p)|<=M_0 |p|^2,       |gradient U(p)|<=M_1 |p|.

In particular the one-height derivative satisfies everywhere

    |U_x(x,y)y+U_y(x,y)z|
      <=M_1 sqrt(x^2+y^2)sqrt(y^2+z^2)
      <=(M_1/2)(x^2+2y^2+z^2)
      <=M_1(x^2+y^2+z^2).                                  (5)

Also |D W(v)|<=2||S|| |v|^2, |v^T H v|<=||H|| |v|^2, and
0<=Q(v)<=(x_0^2+z_0^2)/2. Thus every tested term is integrable
under any finite-second-moment law. The constants may depend on the
fixed U,S,H; no bound uniform over the storage class is required.
These are the p=2 growth conditions of the sufficient method.
They retain origin crossings and require no derivatives of U beyond C1.

For a fixed smooth periodic h, its four-state path w_h and derivative
are bounded on [0,P]. The ordinary C1 chain rule, including at a
zero of (h,h'), gives

    integral_0^P D V(J_h(t)) dt=V(w_h(P))-V(w_h(0))=0.          (6)

Periodicity holds also at lag one: h(P+1)=h(1) and
h'(P+1)=h'(1). No third-derivative state is used. The two branches
of (1) together say

    v^T H v-D V(v)>=Q(v).                                   (7)

Integration along the periodic path and (6) yield
average Q(J_h)<=trace(H C(h)). L588 Section 1's necessary finite-cone
implication applies to f_H(u)=trace(H A(u)): from
K-C(h)=sum_l alpha_l A(u_l), with alpha_l>=0 and u_l in I, (2) gives

    trace(H(K-C(h)))=sum_l alpha_l trace(H A(u_l))>=0.

This proves the stated sufficient upper bound with the actual finite
cone and the full trace, including both off-diagonal contributions.
It does not assert that the sufficient class is sharp.

### 2. A single elliptical marginal and its complete second matrix

Let theta be uniform on [0,2pi] and let k be independent of theta with

    P(k=1/12)=1/6,        P(k=-7/60)=5/6.

Set

    X=sqrt(2)cos(theta),  Y=sin(theta)/sqrt(6),  Z=kX,
    B_0=(X,Y,Z).                                            (8)

This law is bounded. Its means vanish because E cos(theta)=
E sin(theta)=0 and k is independent. The exact curvature moments are

    E k=1/72-7/72=-1/12,
    E k^2=1/864+49/4320=1/80.

The elementary circular averages give E X^2=1, E Y^2=1/12,
E XY=0. Independence now gives E XZ=-1/12,
E YZ=(E k)(E XY)=0, and E Z^2=1/80. Hence all entries are

    E B_0 B_0^T=K_0
      =[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]],              (9)

precisely the same-height block of the stipulated K. The exact
matrix K_0, including the sign of XZ, also follows from integrating
1,u^2,u^4 over I in L473's formula. No marginal independence
between X and Y is used.

### 3. Cancellation for every U, with no angular truncation

For each fixed theta, the two-point average over k is exactly

    E_k[U_x(X,Y)Y+U_y(X,Y)kX]
       =U_x(X,Y)Y-(X/12)U_y(X,Y),                           (10)

because neither X nor Y depends on k. This is a finite conditional
sum; it uses no conditional-density formula or differentiation under
expectation. The bound (5) justifies integrating it over theta.

Write g(theta)=U(sqrt(2)cos(theta),sin(theta)/sqrt(6)). Since U
is globally C1, g is C1 and 2pi-periodic, whether or not U is even.
The parametrization has

    dX/dtheta=-sqrt(12)Y,        dY/dtheta=X/sqrt(12).

Thus its ordinary chain rule gives exactly

    -(1/sqrt(12))g'(theta)
       =U_x(X,Y)Y-(X/12)U_y(X,Y).                           (11)

Integrating (10)--(11) over a full period proves

    E[U_x(X,Y)Y+U_y(X,Y)Z]
       =-[g(2pi)-g(0)]/(2pi sqrt(12))=0.                    (12)

The measure (8) was fixed before U was chosen. Therefore (12)
holds for every U in the hypotheses with that same measure; no finite
basis, density assertion, choice of a separate law for each U,
convexity or C2 assumption occurs. Homogeneity was used for the global
growth check; the closed-curve calculation itself needs only C1.
The global domain in (1) continues to include the origin even though
the first two coordinates of this particular witness avoid it.

### 4. Exact clipped mean and the required threshold

For k=1/12, the signed observable is

    XZ-Y^2=(1/6)cos^2(theta)-(1/6)sin^2(theta)
           =(1/6)cos(2theta).

For k=-7/60 it equals
-(7/30)cos^2(theta)-(1/6)sin^2(theta), which is always negative.
Over one full period, the integral of max(0,cos(phi)) is 2.
The change phi=2theta traverses two periods and divides the integral
by two, so integral_0^(2pi) max(0,cos(2theta)) dtheta=2 as well.
Consequently

    E Q(B_0)=(1/6)(1/6)(2/(2pi))=1/(36pi).                 (13)

The familiar bound 0<pi<4 gives in particular pi<8. Thus (13)
strictly exceeds the required 1/288 with the exact margin in (4).
This is an analytic integral, not a quadrature or sampling certificate.

### 5. Extend the changed marginal to the full K

L473 Sections 3--4 prove strict positivity of this exact K and supply
the finite-dimensional Schur extension template. Write

    K=[[K_0,D_0],[D_0^T,K_0]],
    T_0=K_0-D_0^T K_0^(-1)D_0>0.

These established matrix facts do not depend on the old finite law.
Use the real symmetric square root of T_0, and let e have three
independent uniform sign coordinates, independent of theta and k.
Define

    B_1=D_0^T K_0^(-1) B_0+T_0^(1/2)e,
    B=(B_0,B_1),            mu=law(B).                       (14)

This is the necessary applicability check for a changed marginal,
not a reproof of a general extension theorem. Since E B_0=0,
E e=0 and E ee^T=I_3, E B_1=0. Formula (9) and independence give

    E B_0 B_1^T=K_0 K_0^(-1)D_0=D_0,
    E B_1 B_1^T=D_0^T K_0^(-1)D_0+T_0=K_0.                (15)

The mixed terms containing e vanish. All cross-lag entries and both
same-height blocks are therefore retained exactly: E B=0 and
E BB^T=K. The vector B is bounded because B_0 and e are bounded
and the matrices in (14) are fixed and finite. Unlike the earlier
witnesses, it has a continuous angular parameter; it is not asserted
to have finite support. Its first three coordinates are unchanged,
so (12) and (13) still hold for mu. It is independent of U,S,H.

L589 Section 2 applies to any law with this full second matrix.
For all four-state indices a=(r,j), b=(s,k), j,k in {0,1}, it has

    K_(a+,b)+K_(a,b+)=0,

where a+=(r,j+1) and b+=(s,k+1). Indeed the two integrands have
the common factor (iu)^j(-iu)^k exp(i(r-s)u) times iu-iu.
The successor indices stay among the six coordinates. This imports
the cancellation for every same-lag and cross-lag quadratic term,
with no third derivative or assumption of path realization. Inserting
E BB^T=K into the finite quadratic derivative sum gives

    E D W(B)=0,             E D V(B)=0,                     (16)

the latter by (12). Equation (5) and the quadratic bounds above
ensure absolute convergence of every term.

Finally apply the global inequality (7) to B and take expectations:

    trace(HK)=E[B^T H B]>=E Q(B)+E D V(B)=1/(36pi).           (17)

This proves (3)--(4) for the entire specified class. No use of (2)
was needed for the lower bound, so adding the actual closed-I dual
condition cannot evade it. The witness is a comparison measure for
an inequality imposed on all of R^6. Neither its conditional drift
cancellation nor its covariance proves it is the jet law of a periodic
or stationary process; no such conclusion or actual-Xi substitution
is made. Earlier quadratic and fixed-rational stops retain their
scopes; this argument tests the enlarged all-U class directly.

### 6. Independent conceptual audit, 31 October 2026

The invocation-start SPECIALIZE coverage in
`drafts/literature/2026-10-31-l592-independent-audit-scope.md`
approves exactly this audit. Its primary sufficient-method comparison
is reused, including the C1 field, integrable chain rule and p=2 growth
requirements. No source sharpness, converse, measure realization or
arithmetic theorem is used. The audit checks the following implications
independently of the original construction's asserted conclusion.

**Origin, growth and periodic applicability.** U(0)=a^2 U(0) with
a=2 forces U(0)=0. For each real direction p, differentiability and
the positive-ray limit give D U(0)[p]=lim_(t down to 0)t U(p)=0.
This applies to negative directions as well by choosing -p; evenness
is unnecessary. Differentiating U(ap)=a^2 U(p) with respect to p
gives a gradient U(ap)=a^2 gradient U(p). Compactness of the unit
circle now proves the stated global quadratic/linear growth, including
zero. The two Cauchy--Schwarz/Young inequalities in (5) give the
claimed absolute bound, since (x^2+2y^2+z^2)/2<=x^2+y^2+z^2.
The four-state and successor vectors each have norm at most |v|,
so |D W|<=2||S|| |v|^2. The Q and H bounds in Section 1 also hold.
Thus each fixed tested function is absolutely integrable under a
finite-second-moment law; no uniform constant over U,S,H is claimed.
For smooth h on [0,P], w_h is C1 and the ordinary chain rule is
valid through origin crossings. Its endpoints agree also in the
lagged coordinates for every P>0. Hence (6) requires no third jet,
lag commensurability or boundary-flux assumption beyond periodicity.

**One law and every storage.** The two weights in (8) sum to one.
Direct arithmetic gives E k=(1-7)/72=-1/12 and
E k^2=(5+49)/4320=1/80. Circular averages give means zero,
E X^2=1, E Y^2=1/12 and E XY=0. Independence of k gives
E XZ=-1/12, E YZ=0 and E Z^2=1/80. This checks all six distinct
entries of K_0, not just the variances. For each theta the finite
k-average of the derivative is Y U_x-(X/12)U_y. Computing the
ellipse tangent gives exactly (-sqrt(12)Y,X/sqrt(12)), so this
average equals -g'/sqrt(12), with the sign and constant as in (11).
The ordinary fundamental theorem of calculus on [0,2pi] gives zero.
The same theta,k probability space is fixed for every U; integration
is justified by (5). Neither a finite angular basis, an exchange of
derivative and expectation, nor a different law for each U occurs.

**Both curvature cases and exact margin.** For k=-7/60, the signed
form is -(7/30)cos^2(theta)-(1/6)sin^2(theta)<0 everywhere.
For k=1/12 it is cos(2theta)/6. The integral of max(0,cos(2theta))
is exactly 2 over [0,2pi], since phi=2theta covers two full periods.
Including the amplitude 1/6, positive-branch probability 1/6 and
uniform density 1/(2pi) gives (1/6)(1/6)2/(2pi)=1/(36pi).
Therefore the exact gap
to the threshold is (8-pi)/(288pi)>0, using 0<pi<4. There is no
quadrature error, omitted endpoint mass or assumption about the sign
of an unintegrated branch.

**The full matrix and changed marginal.** L473 Section 3 applies to
this exact fixed-separation K: its quadratic form is the integral of
|P_0(iu)+exp(iu)P_1(iu)|^2. If it vanishes, continuity and the
identity theorem force the entire expression inside the modulus to
vanish. At u=iv, v tending to positive infinity, the polynomial
P_0(-v) equals -exp(-v)P_1(-v), so both polynomials are zero.
Thus K is strictly positive, without an arithmetic asymptotic input.
Its principal block K_0 is invertible; in particular its determinant
is (1/12)(1/80-1/144)=1/2160. The Schur quadratic-form test at
(-K_0^(-1)D_0 z,z) proves T_0>0. Finite-dimensional spectral
diagonalization supplies its real symmetric square root.

The extension uses only centering and (9), not the earlier law's
finite support or fourth moments. Independent sign noise has mean
zero and second matrix I_3. Consequently E B_0 B_1^T=D_0 with
the displayed transpose orientation, while
E B_1 B_1^T=D_0^T K_0^(-1)D_0+T_0=K_0. These identities check
all nine cross entries as well as the second diagonal block. Both
blocks are bounded because all matrices are fixed and finite. No
uniform spectral lower bound or small support radius is needed for
an inequality on all R^6. The first three coordinates, their clipped
mean and their all-U cancellation are unchanged. The extension
depends only on K and the fixed marginal, never on U,S,H.

**Every quadratic, both global inequalities and the full trace.**
For any of the sixteen ordered pairs a=(r,j), b=(s,k) with j,k<=1,
the two successor integrands are the common factor
(iu)^j(-iu)^k exp(i(r-s)u) multiplied respectively by iu and -iu.
Taking real parts and integrating therefore gives
K_(a+,b)+K_(a,b+)=0 for every pair, including all cross-lag pairs.
Successor orders are at most two. Expanding the complete finite sum
D W=sum_(a,b) S_ab(v_(a+)v_b+v_a v_(b+)) gives zero expectation.
Both copies of each off-diagonal term are included, not halved.
Combining this with the all-U cancellation yields E D V=0.

Writing F=v^T H v-D V, the two branches assert F>=0 and
F>=x_0 z_0-y_0^2, hence F>=Q on every point of the comparison
measure's support. Absolute integrability permits expectation and
E v^T H v=sum_(a,b) H_ab K_ab=trace(HK), since K is symmetric.
This proves (17) with the full trace, without (2). Conversely, the
sufficient periodic application uses (2) only through the actual
finite representation of K-C(h): each summand has nonnegative
trace pairing, including nodes at both endpoints of I. No closure,
positive-semidefinite relaxation or dual attainment is substituted.

The audit passes with no mathematical correction. It retains the
whole specified W+U certificate stop, while leaving nonlinear storage
on both heights, periodic realization, reserve/assembly and actual-Xi
transfer unresolved. Necessary averaged drift identities and a full
covariance matrix do not identify a periodic or stationary jet law.
This is verification of the existing local specialization, not a new
obstruction beyond it or a proof of RH.

## Mathlib

Full matching Mathlib coverage for this universal comparison measure
and certificate obstruction has not been checked. The C1 chain rule,
fundamental theorem of calculus, circular integrals, finite-dimensional
positive square root, trace and covariance identities are supporting
standard mathematics, not a claimed formalization of this result.
Unknown coverage is not evidence of absence. The two primary sufficient
method citations above remain imports with their stated qualifications.
