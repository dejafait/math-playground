# Lemma 997: the fixed continuous-slope projection has exponential leakage

## Hypotheses

Use L994's exact polynomial, including its constant subtraction:

    K_m(t)=(L_(m-1)^(2)(t)-1)/(m-1).

Fix, without subsequently varying these inputs,

    A=7/4, B=9/4, eta_0=3/4+i, eta_1=7/8+2*i,
    r=2, m=n+2, n>=2,
    Q(eta)={eta, conjugate(eta), 1-eta, 1-conjugate(eta)}.

Every quartet point has multiplicity one. These are hypothetical
rational principal-part inputs, not asserted zeros of zeta. For
A<=c<=B define

    a_n(c;eta)=-sum_(omega in Q(eta))
       [integral_m^(c*m) K_m(t)*exp((omega-1)*t)dt
                         -integral_n^(c*n) K_m(t)*exp((omega-1)*t)dt],
    p(w)=w/(1-w), f_c(w)=w*exp(c*p(w)),
    w_c=(2-c+i*sqrt(c*(4-c)))/2,
    alpha_0=eta_0-1,
    z_0(c)=exp(-c*alpha_0)*f_c(w_c).

Set chi(c)=Z^(-1)*exp(-1/(1-16*(c-2)^2)) for A<c<B and zero
at both endpoints and outside the interval, where Z is the integral
of the unnormalized bump over (A,B). Thus Z>0, chi>0 on (A,B),
and integral_A^B chi(c)dc=1. The exact prescribed projection is

    Pi_n(eta)=integral_A^B chi(c)*z_0(c)^n*a_n(c;eta)dc.           (1)

No RH, actual spectral decomposition, complementary holomorphy,
rightmost zero, simplicity of actual zeros, nonresonance assumption,
infinite-zero interchange or regulator limit is used.

## Conclusion

The fixed projection satisfies

    limsup_(n->infinity) |Pi_n(eta_0)|^(1/n)<=1,
    limsup_(n->infinity) |Pi_n(eta_1)|^(1/n)=exp(9/32)>1.         (2)

In particular Pi_n(eta_1)=o(Pi_n(eta_0)) is impossible, including
the interpretation |Pi_n(eta_1)|<=epsilon*|Pi_n(eta_0)| eventually
for each epsilon>0. No nonzero algebraic asymptotic for the selected
response is asserted or needed for this stop criterion.

More precisely, the integrated germ

    F_1(z)=sum_(n>=2) Pi_n(eta_1)*z^n

has Taylor radius R=exp(-9/32). It has no holomorphic extension to
a neighborhood of

    Delta=eta_1-eta_0=1/8+i,
    s_B=exp(-B*Delta), |s_B|=R.                                (3)

Step293, 10 November2026: RESEARCH / POTENTIALLY_NEW under the
unchanged, pre-invocation EXPLORE assessment review291. This is a
new local obstruction for the exact finite assay. The independent
step294 conceptual audit below verifies (2)-(3), including the common
parameter domain and the primitive's integration constant. The tools are known,
and the checked sources did not state this complete projected
comparison. No certified originality, actual-Xi consequence or RH
candidate is claimed. This stops only this fixed filter; actual
signed outputs, infinite-zero/complement/regulator control, L993
recovery and L984(H) remain open.

## Proof

### Imported tools and why the varying parameter requires work

Use the exact Laguerre coefficient identity and real bound from
L994(6)-(7), based respectively on
[DLMF18.12.13](https://dlmf.nist.gov/18.12.E13) and
[DLMF18.14.8](https://dlmf.nist.gov/18.14.E8):

    K_m(t)=1/(m-1)*[w^(m-1)]
             ((1-w)^(-3)*exp(-t*p(w))-(1-w)^(-1)),
    |K_m(t)|<=2*m*exp(t/2), m>=2, t>=0.                       (4)

The lower-slope inverse formula is the c=1 term of L995(6).
For the varying upper slope import the SAME general coefficient
tool, I. M. Gessel, *Lagrange inversion*,
[arXiv:1609.05988v1](https://arxiv.org/pdf/1609.05988v1),
Theorem2.1.1/(2.1.4), pp2-3, and Theorem4.1.1 with its
residue substitution, pp22-23. Import local analytic inversion
and its ramified version from
[DLMF1.10(vii), (1.10.12)-(1.10.17)](https://dlmf.nist.gov/1.10#vii),
and parameter-integral holomorphy from
[DLMF1.10(viii), (1.10.18)-(1.10.19)](https://dlmf.nist.gov/1.10#viii).
Rouche's theorem, the identity theorem and the Cauchy-Hadamard
radius theorem are used in their standard forms.

The general theorems are imported, not reproved. The parameter-
dependent branch selection and the integrated endpoint jump below
are necessary specializations: L995 establishes only fixed slopes,
and neither pointwise Laguerre asymptotics nor decay of a bump's
real-frequency transform controls this projected remainder.
The proof uses exact convergent local expansions, not a truncated
bulk asymptotic. Vanlessen and the Johnson/Tlas endpoint methods
from review291 are therefore not needed as mathematical inputs.

### Exact short intervals and upper root bounds

The four endpoints combine exactly as

    integral_m^(c*m) - integral_n^(c*n)
       = integral_(c*n)^(c*(n+2)) - integral_n^(n+2),           (5)

when applied to the SAME integrand K_(n+2)(t)*exp((omega-1)*t).
This is an identity of antiderivative differences; it needs no
interval-overlap assumption. If delta=Re(eta)-1/2, every quartet
point has Re(omega)-1/2 equal to delta or -delta. From (4)-(5),

    |a_n(c;eta)|<=16*(n+2)*
          [c*exp(delta*c*(n+2))+exp(delta*(n+2))].              (6)

Write w_c=exp(i*theta(c)), theta(c)=arccos(1-c/2). Directly,

    p(w_c)=-1/2+(i/2)*sqrt((4-c)/c),
    f_c(w_c)=exp(-c/2+i*phi(c)),
    phi(c)=theta(c)+sqrt(c*(4-c))/2,
    |z_0(c)|=exp(-c/4).                                      (7)

For eta_0, (6) after normalization is bounded by C*(n+2)
uniformly on [A,B]. Its lower-interval exponent is (1-c)*n/4<0.
For eta_1 the upper exponent is c*n/8 and the lower exponent is
(3/8-c/4)*n<=-n/16. Hence, with constants independent of c,n,

    |z_0(c)^n*a_n(c;eta_0)|<=C_0*(n+2),
    |z_0(c)^n*a_n(c;eta_1)|<=C_1*(n+2)*exp(c*n/8).             (8)

These prove the first bound of (2), the upper bound exp(9/32)
for the second, and uniform summability on compact subsets of
|z|<R. In particular, defining

    Z_c(v)=sum_(n>=2) a_n(c;eta_1)*v^n,
    W_c(z)=Z_c(z*z_0(c)),

we have the exact equality

    F_1(z)=integral_A^B chi(c)*W_c(z)dc, |z|<R.                (9)

Uniform geometric domination from (8) justifies this exchange.
For every fixed epsilon>0 the contribution c<=B-epsilon extends
holomorphically to |z|<exp(-(B-epsilon)/8), by the same bound.
Thus only c near B can obstruct extension at s_B.

### Exact upper-slope inversion, with all subtractions

For d in {1} union [A,B] let U_d(x) be the inverse germ of f_d
at zero, and define

    D_d(w)=1+d*w/(1-w)^2,
    E_d(lambda)=(exp(2*d*lambda)-1)/lambda, E_d(0)=2*d,
    h_(d,alpha)(w)=w^(-1)*(1-w)^(-3)*E_d(alpha-p(w)),
    x=v*exp(d*alpha),
    T_(d,alpha)(v)=[h_(d,alpha)(U_d(x))/D_d(U_d(x))]_(>=2)
                                      -E_d(alpha)*x^2/(1-x).  (10)

The projection [ ]_(>=2) removes precisely Laurent degrees -1,0,1
in v. There are no lower degrees. With theta_v=v*d/dv,

    (theta_v+1)*Z_c(v)
       =-sum_(omega in Q(eta_1))
                   [T_(c,omega-1)(v)-T_(1,omega-1)(v)].       (11)

For d=1 this is the unchanged lower-slope part of L995(6).
For arbitrary upper d the exact finite integration of (4)-(5)
gives the exponential-branch coefficient

    exp(d*n*alpha)*[w^(n+1)]
       (1-w)^(-3)*E_d(alpha-p(w))*exp(-d*n*p(w)).

Moving w^(-1) into h changes this to a coefficient of degree n.
Gessel's residue substitution x=f_d(w) gives exactly the first
term of (10), since dx=exp(d*p(w))*D_d(w)dw. This applies to
the simple Laurent pole of h as well as to analytic h. The
constant branch of (4) gives coefficient one and therefore the
SECOND term of (10), with its displayed minus sign. Multiplication
by n+1 removes the denominator of K_(n+2), and the overall minus
sign and lower-interval subtraction give (11). Thus no endpoint,
quartet point or -1 has been discarded.

This identity initially holds as a germ. Its analytic meaning is
as follows. On |w|=t<1, Re(p(w))>=-t/(1+t). Consequently Rouche
gives exactly one root of w-x*exp(-d*p(w)) in that circle if

    |x|<t*exp(-d*t/(1+t)).

For every 0<d<4 the logarithmic derivative of the right side is
1/t-d/(1+t)^2>0, and its limit as t increases to one is exp(-d/2).
Thus U_d is the unique root in |w|<1 for |x|<exp(-d/2).
The zeros of D_d are exactly exp(+-i*theta(d)) on |w|=1;
the interior inverse is simple. The analytic inverse theorem and
uniqueness make U_d holomorphic on this disk. These assertions
hold for d=1 and for the full closed interval [A,B].

We also need boundary regularity, rather than an assumption about
an unselected inverse sheet. For fixed 0<d<4, U_d maps the upper
x half disk into the upper w half disk: it cannot cross the real
axis, since f_d is real on (-1,1), and its sign near zero fixes
the connected component. Therefore the continuous argument identity

    arg(x)=arg(U_d(x))+d*Im(p(U_d(x)))

has no multiple of 2*pi, and 0<d*Im(p(U_d(x)))<pi there.
Conjugation covers the lower half disk and uniqueness the real
axis. Near any nonzero boundary x_*, U_d is bounded away from
zero, and

    d*Re(p(U_d(x)))=log|x|-log|U_d(x)|

is bounded. Together these bound p(U_d), so U_d cannot approach
w=1. The bounds are uniform when d stays in a compact subinterval
of (0,4) and |x| stays bounded away from zero. The cluster set at
a fixed boundary x_* is connected, by nested closed images of
connected disk caps. It lies among finitely many roots of
f_d(w)=x_* in a compact set avoiding 1, and hence is a singleton.
At a noncritical limiting root the analytic inverse theorem extends
U_d across x_*. No escape to the essential singularity is possible.

The critical points w_+=exp(i*theta(d)) and w_-=conjugate(w_+)
are both reached by this selected inverse. For w=w_+, set

    v_d=-w*(1-i)*sqrt(tan(theta(d)/2)).

At the critical point direct differentiation gives

    D_d'(w)=-(1+w)/(w*(1-w)),
    f_d''(w)/f_d(w)=-(1+w)/(w^2*(1-w)).

The ramified inverse theorem therefore gives, with
q=1-x/f_d(w),

    U_d(x)=w+v_d*q^(1/2)+O(q),
    1/D_d(U_d(x))=1/(D_d'(w)*v_d)*q^(-1/2)+O(1).             (12)

These are convergent expansions in sqrt(q). The square root is
positive for positive real q. Indeed Re(v_d/w)<0, so this local
root is inside |w|<1 for q>0 small, while the other root is outside.
Rouche uniqueness identifies the inside root with U_d. Conjugation
gives the corresponding statement at w_-. This also fixes the
square-root determination, not just its absolute size.

All coefficients of (10) and of these local inverse expansions
depend analytically on d near any fixed d in (0,4). To justify
this parameter assertion, the small inverse at zero follows from
f_d'(0)=1, and the local critical expansion follows from its
nonzero quadratic coefficient, with the displayed analytic choice
of v_d near B. At a noncritical boundary value the implicit inverse
is likewise analytic in d,x. Match it to the selected inverse at
a fixed, slightly interior relative point x=(1-q_0)*x_*(d),
q_0>0: its root stays strictly inside the unit disk for d near B,
so uniqueness applies. Continue that equality in x through the
local neighborhood. This pays joint branch control near B; it is
not an inference from an unparameterized O symbol.

### Isolation of the single endpoint singularity in the full quartet

For the upper-slope, positive-ordinate point alpha=eta_1-1, the
normalized w_c critical value in the z plane is exactly

    s(c)=exp(-c*(eta_1-eta_0))=exp(-c*Delta).                   (13)

The four possible upper-slope critical images from the two
right-half-plane quartet points, including both w branches, are

    s(c), s(c)*exp(-2*i*phi(c)),
    s(c)*exp(4*i*c), s(c)*exp(4*i*c-2*i*phi(c)).               (14)

They all have modulus exp(-c/8). At c=B none of the last three
equals s_B. To check this without a nonresonance assumption,
phi'(c)=(1/2)*sqrt((4-c)/c)>0 and phi(4)=pi, whereas
theta(B)>pi/2. Thus pi/2<phi(B)<pi. The angle -2*phi(B) is
not a multiple of 2*pi. Also 2*pi<9<4*pi and
0<9-2*phi(B)<2*pi, using 3<pi<4. These are the other two
ratios' angles. By continuity they remain separated from s(c)
in a fixed neighborhood of c=B.

Every remaining term of (11) is regular at (c,z)=(B,s_B):

- The reflected quartet has Re(omega)-1/2=-3/8. Its upper-slope
  normalized inverse disks have radius exp(5*c/8)>1.
- The lower-slope right-pair disks have radius
  exp(c/4-3/8)>=exp(1/16)>1; the reflected lower pair has an
  even larger radius.
- In a constant term of (10), |x|=|z|*exp(-c/4+d*Re(alpha))<1
  near this point, since Re(alpha)<0 and |s_B|<1. Its rational
  pole is absent. Finite Laurent subtractions are regular at
  nonzero v=z*z_0(c).
- The other right-pair upper terms have noncritical boundary
  values at c=B by (14), and the boundary regularity and parameter
  argument following (12) extend those selected branches locally.

Consequently, for c sufficiently close to B, the complete W_c
has a convergent local representation

    W_c(z)=A_*(c,z)+q^(1/2)*B_*(c,q), q=1-z/s(c),             (15)

where A_* and B_* are jointly holomorphic near (B,s_B) and
(B,0), respectively. These functions include the analytic
contributions of ALL the other terms. To obtain (15), substitute
the convergent expansions (12) in (11) and solve
(theta_z+1)W_c=(z*W_c)' locally. The analytic part has an analytic
primitive; the lowest fractional exponent of the right side is
-1/2, so its primitive is sqrt(q) times an analytic function.
There is no logarithm. The integration constant is analytic in c:
fix q=q_0>0, where the original subcritical germs and (11) match,
and use analytic parameter continuation as above.

The leading coefficient of (15) is explicitly nonzero. Put

    lambda(c)=eta_1-1-p(w_c), Re(lambda(c))=3/8,
    H_c=h_(c,eta_1-1)(w_c),
    C(c)=-H_c/(D_c'(w_c)*v_c).

The unique singular term of (11) has leading coefficient
C(c)*q^(-1/2), with the minus sign from the complete response.
Thus

    B_*(c,0)=-2*C(c).                                        (16)

None of its factors vanishes: w_c is neither zero nor +-1,
D_c'(w_c)*v_c!=0, and

    H_c=w_c^(-1)*(1-w_c)^(-3)
                       *(exp(2*c*lambda(c))-1)/lambda(c)!=0,

because Re(lambda(c))=3/8>0. In particular B_*(B,0)!=0.
This is a full-quartet comparison at the relevant endpoint, not
a lower bound for an isolated summand while leaving others unpaid.

### The exact projected endpoint jump

Choose epsilon>0 sufficiently small for the common neighborhoods
in (15). The contribution c<=B-epsilon in (9) is holomorphic at
s_B by (8). The integral of A_*(c,z) on [B-epsilon,B] is also
holomorphic there, by uniform boundedness on smaller compact
neighborhoods and integrability of chi. Only the exact fractional
part of (15) remains.

Use the local coordinate and real integration variable

    z=s_B*exp(Delta*y), x=B-c, 0<=x<=epsilon.

Then s(c)=s_B*exp(Delta*x) and

    q=1-exp(-Delta*(x-y))=Delta*(x-y)*e(x-y),
    e(v)=(1-exp(-Delta*v))/(Delta*v), e(0)=1.

Shrink epsilon and the y neighborhood so that e has an analytic
square root with value one at zero. Take the principal sqrt(Delta),
and put

    H(x,y)=sqrt(Delta)*sqrt(e(x-y))
               *B_*(B-x,1-exp(-Delta*(x-y))).                 (17)

H is analytic near (0,0) and H(0,0)!=0 by (16). The projected
fractional part is EXACTLY

    J(y)=integral_0^epsilon chi(B-x)*(x-y)^(1/2)*H(x,y)dx.      (18)

Use the principal square root in (18), initially for y negative
and real, and then on a small disk cut along its positive real
radius. This is the branch of the original germ: for real y<0,
|z|=R*exp(Re(Delta)*y)<R, and, for each x>=0,
|z/s(c)|=exp(Re(Delta)*(y-x))<1. The q in (15) therefore has
positive real part. The factorization in (17)-(18) matches its
square root by continuity from x-y>0 small. Both sides are
holomorphic on the slit neighborhood, so this equality identifies
the continuation of (9), not a separately chosen sheet.

For 0<t sufficiently small the two boundary values at y=t exist.
The factors in (18) are bounded on this compact integration
interval, and sqrt(x-y) has a continuous, vanishing magnitude at
x=t; dominated convergence therefore applies. For x>t the two
values agree. For x<t, approach from Im(y)>0 gives
-i*sqrt(t-x), and approach from Im(y)<0 gives +i*sqrt(t-x).
Thus their exact difference is

    J_+(t)-J_-(t)
       =-2*i*integral_0^t chi(B-x)*sqrt(t-x)*H(x,t)dx.          (19)

This jump is nonzero for EVERY sufficiently small positive t.
Let u=conjugate(H(0,0))/|H(0,0)|. By continuity, after a further
fixed shrinkage,

    Re(u*H(x,t))>|H(0,0)|/2, 0<=x<=t.

The other two factors of the integrand in (19) are positive for
0<x<t. Rotating by u makes its integral have strictly positive
real part. Flatness of chi at x=0 does not change this fact; it
only makes the nonzero jump small as t decreases to zero.

If F_1 extended holomorphically across s_B, its expression in y
would be holomorphic on a full neighborhood of zero. By the
identity theorem it would agree with the continuation (18), plus
the regular contributions, on both sides of the cut. Its upper
and lower values at all small positive t would then coincide,
contradicting (19). The regular contributions have no jump and
cannot cancel it. This proves the singularity asserted in (3).

Together with the disk from (8)-(9), the singularity gives Taylor
radius exactly R. Cauchy-Hadamard yields the second equality in
(2). Finally, a little-o comparison with the first sequence would
force the second root limsup to be at most one, contradicting (2).
This proves precisely the approved leakage stop criterion.

### Qualifications

The proof establishes coefficient root growth through the exact
integrated generating germ. It does not estimate a pointwise
Laguerre remainder under an oscillatory integral, assert a uniform
asymptotic for Pi_n, or infer a lower bound from finitely many
coefficients. Both critical branches, all quartet points, all four
endpoints and K_m's constant subtraction were retained before
regularity was proved for the complementary terms. No boundary
distribution of actual zeta zeros is involved. There is no claim
of uniformity in an infinite collection of quartets or of a
holomorphic actual arithmetic complement.

### Independent conceptual audit — step294, 10 November2026

RESEARCH / REPRODUCTION under the unchanged, pre-invocation EXPLORE
review291. The audit accepts (2)-(3) for precisely the fixed inputs
above. This verifies a previously unaudited obstruction; it asserts
no new theorem, stronger asymptotic or actual zero statement.

**Exact coefficients and thresholds.** Both interval differences
in (5) use K_(n+2); using K_n in the lower interval would invalidate
the coefficient formula. For one quartet point, (4) bounds the
two short intervals by

    4*(n+2)*[c*exp(delta*c*(n+2))+exp(delta*(n+2))].

Summing four points gives (6). Normalization by |z_0(c)|^n yields
upper exponents 0 for eta_0 and c*n/8 for eta_1. The lower exponents
are (1-c)*n/4 and (3/8-c/4)*n; the latter is at most -n/16.
Every remaining factor is bounded on the closed c interval. This
verifies (8) and the compact-uniform exchange in (9).

The factor w^(-1) in h converts the exponential-branch coefficient
of degree n+1 to degree n. For the imported Gessel substitution,
dx=exp(d*p(w))*D_d(w)dw, and hence

    Res_(x=0) [h(U_d(x))/D_d(U_d(x))]*x^(-n-1)dx
       =Res_(w=0) h(w)*exp(-d*n*p(w))*w^(-n-1)dw.

The nonzero linear term f_d'(0)=1 permits the Laurent substitution.
There is at most a simple pole at zero, so removing degrees -1,0,1
leaves precisely n>=2. The constant branch gives
E_d(alpha)*x^2/(1-x) with the minus sign in (10). Multiplication
by n+1 and the outer signs then give (11). This checks every
endpoint and subtraction without replacing the complete response
by a finite asymptotic expansion.

**Selected inverses.** For 0<d<4 and 0<t<1,

    (1+t)^2-d*t=(1-t)^2+(4-d)*t>0.

Thus the Rouche bound increases strictly to exp(-d/2). Uniqueness
on successively larger circles gives uniqueness in the entire
unit disk. The zeros of D_d are the two stated boundary points;
the interior inverse is simple. In the upper x half disk its
imaginary part cannot change sign, since a real root would make
x real. The continuous integer in the argument identity is zero
near zero and hence throughout. This bounds |Im(p(U_d))| by pi/d.
The modulus identity and the lower bound for |U_d| near nonzero
boundary x bound the real part as well, uniformly for real d in
a compact subset of (0,4). Therefore boundary cluster sets avoid
w=1. Nested compact closures of images of connected disk caps have
a nonempty connected intersection; its points are among finitely
many roots in a compact set where f_d is analytic. It is a singleton.
At a noncritical limit the selected inverse extends holomorphically.
This verifies that no sheet can escape to the essential singularity.

At w=w_c the proposed quadratic coefficient satisfies

    v_c^2=-2*i*w_c^2*tan(theta(c)/2),
    [f_c''(w_c)/f_c(w_c)]*v_c^2=-2,
    |w_c+v_c*sqrt(q)+O(q)|^2
       =1-2*sqrt(tan(theta(c)/2))*sqrt(q)+O(q),  q>0.

Its sign selects the inside root; the other sign selects the outside
root. Rouche uniqueness therefore identifies (12) with U_c. At
c=2 this gives v_2=-(1+i), consistent with L995. The critical
points remain quadratic near B, with analytic choices of w_c,
v_c and the ramified coefficients for complex c near B.

**A common parameter domain for the primitive.** Fix a sufficiently
small q_0>0 and set z_b(c)=(1-q_0)*s(c). For real c near B and
0<=tau<=1, every right-pair upper inverse argument at
z=tau*z_b(c) has modulus

    tau*(1-q_0)*exp(-c/2).

There is a uniform strict margin from the inverse-disk boundary.
Lower and reflected arguments have larger margins. Compactness
in (c,tau), simplicity and the analytic implicit-function theorem
give compatible joint analytic inverses for complex c near B
along this path. Uniqueness glues the local choices, and the
Laurent subtractions are removable at tau=0. Let Y_c be the right
side of (11) after v=z*z_0(c). The initial germ satisfies

    W_c(z_b(c))=integral_0^1 Y_c(tau*z_b(c))dt.

The compact integral is analytic in c. This explicitly fixes the
integration constant in solving (z*W_c)'=Y_c near the endpoint.
The local ramified and noncritical inverses match these branches
at z_b(c), then agree by continuation. Thus A_* and B_* in (15)
are jointly holomorphic on common neighborhoods. No pointwise
real-parameter remainder is being promoted to this assertion.

**All other terms and the amplitude.** At c=B the three other
critical-value ratios in (14) have arguments -2*phi(B), 9 and
9-2*phi(B). From pi/2<phi(B)<pi and 3<pi<4 these lie strictly
between -2*pi and -pi, between 2*pi and 4*pi, and between 0 and
2*pi, respectively. None is zero modulo 2*pi. The corresponding
selected inverses are therefore noncritical. The reflected upper
disk radius exp(5*c/8), lower right-pair radius exp(c/4-3/8),
constant-term poles and Laurent terms have the strict clearances
given after (14). There are finitely many terms, so their analytic
neighborhoods can be intersected near (B,s_B).

For the sole singular term, Re(lambda)=3/8 implies
|exp(2*c*lambda)|>1, so H_c is nonzero. Integrating
C(c)*q^(-1/2) in (z*W_c)' with dz=-s(c)dq gives
-2*s(c)*C(c)*sqrt(q). Division by z=s(c)*(1-q) gives exactly
B_*(c,0)=-2*C(c), including its sign. The fractional powers in
the right side start at -1/2, not -1, so there is no logarithm.
The remaining terms and the integration constant are analytic.

**The jump is a continuation of the original germ.** Choose the
common neighborhoods first and then epsilon sufficiently small.
The c<=B-epsilon integral is analytic on the larger disk from (8).
The integral of A_* is analytic near s_B by uniform compact bounds;
integrability of chi suffices. No analytic extension of the bump
in c is needed. For y<0 real and x>=0, v=x-y>0 and

    Re(1-exp(-Delta*v))=1-exp(-v/8)*cos(v)>0.

Near v=0 its square root is sqrt(Delta)*sqrt(v)*sqrt(e(v)) with
the choices in (17). This checks the sheet of (18) on a nonempty
part of the original Taylor disk. On compact subsets of the small
y disk cut along its positive radius, the integrand and its
analytic parameter derivatives have uniform integrable bounds.
The exact integral (18) is therefore holomorphic there. This slit
disk is connected, so the identity theorem identifies BOTH banks
with continuations of the same initial germ.

Dominated convergence gives (19). On 0<x<t the weight chi(B-x)
is strictly positive despite its flatness at zero. Continuity and
H(0,0)!=0 put every H(x,t), 0<=x<=t, in one strict rotated
half-plane for all small t. Thus the jump integral is nonzero for
every such t. This is an exact sign inequality, not an approximation
or a lower bound inferred from finitely many coefficients.
A holomorphic extension at y=0 would agree on the connected slit
disk and have equal limits on its two banks, contradicting these
jumps arbitrarily close to zero. No quantitative lower bound on
their size as t decreases is required.

Together with (8), this verifies radius exactly exp(-9/32) and,
by Cauchy-Hadamard, the full interfering root limsup exp(9/32).
An eventual little-o comparison with the selected sequence would
force this root limsup to be at most one. The approved fixed-filter
stop therefore survives independent audit.

The direct mathematical inputs remain L994 and L995. The audit
establishes no selected algebraic leading term, uniformity over
infinitely many quartets, or actual prime/complement/regulator
control. Actual signed outputs, L993 recovery and L984(H) remain
unpaid. No numerical experiment, new source theorem or additional
DAG edge is used.

## Mathlib

Full matching coverage of this integrated moving-band projection,
its endpoint jump and its exact leakage radius is unchecked and
unknown. No absence claim is made. The cited generating-function,
residue/inversion, holomorphic parameter-integral and power-series
tools are supporting mathematics; their corresponding Mathlib
theorem names and this parameter specialization were not checked.
No numerical certificate or formal proof is being asserted.
