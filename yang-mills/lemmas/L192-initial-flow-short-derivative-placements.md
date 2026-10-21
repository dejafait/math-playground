# L192 — The two short-output derivative placements are subcubic

## Hypotheses

Use L189–L191's fixed-mesh SU(2) expansion in the relative box
(-4,4)^4, admitted even N, a=8/N, the straight lower-rooted direction-1
forest, the complete displacement and both actual L010 probes i=3,6
at tau=1/16. The bare expansion precedes refinement. Coordinates are
ordinary dimensionless full-link coordinates. Fixed links are zero;
every variable normal end edge, physical face and allowed constant
own-direction mode remains. Prefix vertex values are pinned on every
physical face, including the upper face.

Keep precisely

    C=D_1, L=C^T C, Delta=L+DD^T, P=1-D(D^T D)^(-1)D^T,
    S=P Delta^(-1)P, z~N(0,S) independently in three colors,
    A=PAP=A^T, t=2SAz, V=q Phi, F=D Phi,
    b(z)=[z,Vz]/2-[Fz,Vz]/4, W(z)=P db(z)[t(z)],
    H_s=exp(-s Delta/a^2), E_(i,s)=H_(tau-s) Q_i H_tau.

A includes both insertion subtractions. The bracket is minus the
color cross product. T is the symmetric trilinear polarization of the
complete full-link action cubic, script S_3(y)=T(y,y,y). Select the
sum of the two short-output placements in L190(8), namely L191(4):

    B_(i,a)(s)=-(12/a^2) E[T(H_s W,H_s z,E_(i,s)z)].       (1)

This B_(i,a)(s) is a scalar expectation, not a quadratic probe matrix.
All constants below are independent of sufficiently fine meshes.

## Conclusion

For r=s+a^2 and 0<=s<=tau/2,

    a^3 |B_(i,a)(s)|
       <= C_i a^(1/2)[r^(-1/2)+r^(-1)].                  (2)

In particular, for 0<s<=tau/2 this is at most C_i s^(-3/4).
For every 0<delta<=tau/2,

    a^3 integral_0^delta |B_(i,a)(s)| ds <= C_i delta^(1/4),
    a^3 integral_0^delta |B_(i,a)(s)| ds
       <= C_i a^(1/2)[2 sqrt(delta)+log(1+delta/a^2)].     (3)

The second bound tends to zero at fixed delta as a tends to zero.
Thus these entire placements, even integrated up to tau/2, have zero
cubic-scaled limit. Combining L190(2)–(3), L191(3) and (3),

    a^3 |E[I_(i,a,delta) rho(pi_F Rz)]|
       <= C_i[eta(delta)+delta^(1/4)] -> 0               (4)

uniformly in the meshes, with eta as in L189. This removes the
complete co-closed initial-flow interval in the joint response.

It does not prove a mesh limit of the retained positive-time response,
the final-time prefix-probe quartic or its sextic partner, or the joint
cubic group. The independent f_(i,2),r_0 term, finer asymptotics, full
compensation, finite matching, reflected error <=c_box/2, continuum
axioms and finite positive infrared mass remain unresolved.

## Proof

### 1. Contract the external smooth leg before estimating W

Use L191(5)–(8)'s full relative eigenmodes e_k=a^2 f_k, with physical
eigenvalue lambda_k and component labels included. In the original order,

    E_(i,s)=a^2 sum_(k,l) d_(i;kl)(s) e_k e_l^T,
    sum_(k,l)|d_(i;kl)(s)|p_0(k)p_0(l)<=C_(i,p_0)          (5)

uniformly for s<=tau/2 and every fixed polynomial p_0. Also

    ||e_k||_infinity<=Ca^2,
    ||C e_k||_infinity<=Ca^3(1+|k|).

No short-time heat is removed from (1), and no output mode of W is
asserted smooth. For a fixed color c put h_l^c=S e_l in that color,
zero in the others, and set k_l^c=2SAh_l^c. L191(6) and commutation
of P with Delta imply

    h_l=(a^2 lambda_l)^(-1)P e_l,
    ||h_l||_infinity<=C p(l),
    ||k_l||_infinity=||2SAS e_l||_infinity<=Ca^2 p(l).     (6)

The last bound is exactly the smooth-column estimate L185(5)–(6),
using both residual subtractions. It is used only on this contracted
column, never on t. The positive physical spectral gap absorbs
lambda_l^(-1). Enlarge the fixed polynomial p when needed.

Finite-dimensional Gaussian integration by parts gives the exact identity

    E[(e_l^T z^c) T(H_s W,H_s z,e_k^c)]
       =E[T(H_s X_l^c,H_s z,e_k^c)],
    X_l^c(z)=dW(z)[h_l^c]
       =P{d^2b(z)[h_l^c,t(z)]+db(z)[k_l^c]}.             (7)

Here d^2b is constant in z. To justify the identity including singular
S, write z=Z xi with ZZ^T=S and apply ordinary standard Gaussian
integration by parts in xi. Differentiation of the second slot also
produces E[T(H_s W,H_s h_l^c,e_k^c)], which is zero: E W=0 since
each bracket in W has two distinct colors of centered, color-diagonal
linear fields. Differentiation of W includes the derivative of t,
which is k_l^c; it is not just differentiation of the explicit z in b.
All polynomials are finite, so this integration by parts is legitimate.

Consequently (1) is exactly

    B_(i,a)(s)=-12 sum_(k,l,c) d_(i;kl)(s)
                       E[T(H_s X_l^c,H_s z,e_k^c)].      (8)

The external a^2 cancels a^(-2) once, with no extra Wick or color
factor. The three colors are the displayed sum. No prefix, tilt,
projection or multiplier has been commuted through a heat factor.

### 2. A full-prefix bound for the contracted linear field

Write ||Y||_G=(E sum_(edges,colors)|Y|^2)^(1/2) for a random link
field, and analogously for vertex fields. Import the complete trace
bounds Tr S<=CN^4 and Tr K<=CN^5, K=Phi S Phi^T, from L187(9)
and its adjacent full-spectrum argument. Their input is L182(10)'s
positive domination K<=M tensor G_T, M_st=min(s,t), with the actual
pinned prefix and both axial ends retained. L183(18) gives
Cov(t)<=CN^2 S in each color. Taking traces and applying Phi to this
positive comparison yields

    ||z||_G<=CN^2,       ||t||_G<=CN^3,
    ||Vz||_G+||Fz||_G<=CN^(5/2),
    ||Vt||_G+||Ft||_G<=CN^(7/2).                         (9)

D and q have uniformly bounded Euclidean operator norm on the full
relative complex, including normal end edges. These estimates require
no independence between a field and its prefix, or positivity of A.
For deterministic fields Phi sums at most N entries in each row, so
(6), including all pinned upper jumps, gives

    ||Vh_l||_infinity+||Fh_l||_infinity<=CN p(l),
    ||Vk_l||_infinity+||Fk_l||_infinity<=CN^(-1) p(l).    (10)

Differentiate the actual b, without discarding either prefix slot:

    d^2b[h,t]=([h,Vt]+[t,Vh])/2
                       -([Fh,Vt]+[Ft,Vh])/4,
    db(z)[k]=([k,Vz]+[z,Vk])/2
                       -([Fk,Vz]+[Fz,Vk])/4.           (11)

For a deterministic coefficient u, the pointwise color bracket obeys
||[u,Y]||_G<=C||u||_infinity||Y||_G. In the order displayed in the
first line of (11), (6), (9)–(10) bound its four terms by

    C p(l) times N^(7/2), N^4, N^(9/2), N^(9/2).

For its second line the four bounds are respectively

    C p(l) times N^(1/2), N, N^(3/2), N^(3/2).

P is an orthogonal contraction. Thus the entire actual linear field
in (7), with the tilt on both possible contracted inputs, satisfies

    ||X_l^c||_G<=C p(l) N^(9/2)=C' p(l) a^(-9/2).       (12)

This is not a bound on W itself or on a smooth rough-direction tilt.
The upper jump was allowed its full O(N) size in (10). The trace
estimate in (9), rather than a worst-case prefix operator norm on
each rough input, is essential for (12).

### 3. Short-time heat estimates with every source row retained

The full relative spectrum of L026 and L189 gives, with r=s+a^2,

    ||H_s z||_G<=Ca^(-1) r^(-1/2),
    ||C H_s z||_G<=C r^(-1),
    ||H_s||_op<=1,       ||C H_s||_op<=Ca r^(-1/2).      (13)

For completeness, the first squared bound is
3 Tr[S exp(-2s Delta/a^2)]. A shell max k_j=m has at most C m^3
modes, inverse dimensionless eigenvalue at most C a^(-2)m^(-2),
and physical eigenvalue at least c m^2. Its trace is bounded by
Ca^(-2) sum_(m<N) m exp(-cs m^2)<=Ca^(-2)r^(-1).
For the second squared bound, LS=P on im P gives
3 Tr[P exp(-2s Delta/a^2)]<=C sum_(m<N)m^3 exp(-cs m^2)
<=Cr^(-2). At s=0 these estimates use the finite sums; for s>0
Gaussian integral comparison gives the other bound. Taking their
minimum proves the r bounds uniformly, including s<a^2.

Finally C^T C=L<=Delta and the bounded dimensionless spectrum imply
||C H_s||_op^2<=sup_(0<lambda<=16)lambda exp(-2s lambda/a^2)
<=Ca^2/(s+a^2). This is a bound on the full input space; it does not
require X to have the covariance of z. Every constant own-direction
mode and normal end row remains in these estimates.

### 4. Keep all circulation placements in T and count the mesh powers

Polarize the full word L189(5), script S_3(y)=sum_p<(Cy)_p,w_2(J_p y)>.
Each term in T(x,y,v) has the circulation on one of x,y,v. Bounded
plaquette incidence and color bracket norms give for arbitrary fields

    |T(x,y,v)|<=C{||Cv||_infinity ||x|| ||y||
                 +||v||_infinity[||Cx|| ||y||
                                      +||x|| ||Cy||]}.  (14)

Indeed each polarized w_2 is a finite sum of products of two selected
edge values. If v is selected in that product its supremum bounds
that factor and Cauchy--Schwarz sums the remaining two arrays over
plaquettes; if Cv occurs, apply Cauchy--Schwarz to the two edge arrays.
Each variable edge belongs to a uniformly bounded number of these
words. The same argument holds at all faces with the fixed rows zero.
It retains all polarizations rather than assuming a curvature-only
transfer of a nonlinear vertex.

Apply (14) with x=H_s X_l^c, y=H_s z, v=e_k^c, then apply Gaussian
Cauchy--Schwarz to the products of Euclidean norms. Equations
(5), (12)–(13) give

    |E T(H_s X_l^c,H_s z,e_k^c)|
      <=C p(k)p(l) a^(-9/2){a^3 a^(-1)r^(-1/2)
                       +a^2[a r^(-1/2)a^(-1)r^(-1/2)
                                                +r^(-1)]}
      <=C p(k)p(l) a^(-5/2)[r^(-1/2)+r^(-1)].           (15)

The last two summands account separately for circulation on the
short-output X leg and on the short-time z leg. No independence of
these correlated fields was used. Summing (15) by (5) in (8) and
multiplying by a^3 proves (2).

For sufficiently fine meshes r<=1 on this time interval. Since
a^(1/2)<=(s+a^2)^(1/4), (2) is bounded by Cr^(-3/4), hence by
Cs^(-3/4) for s>0. Integration gives the first bound (3).
Direct integration of (2) gives the second because

    integral_0^delta (s+a^2)^(-1) ds=log(1+delta/a^2),
    integral_0^delta (s+a^2)^(-1/2) ds
                         =2(sqrt(delta+a^2)-a)<=2sqrt(delta).

At fixed delta, a^(1/2)log(1+delta/a^2) tends to zero. These explicit
bounds cover the entire interval below a^2 as well as its complement;
no initial interval is deleted before estimating it.

### 5. Assemble only the initial contribution

L190(8) splits dU[W] into (1)'s two placements and L191's external
placement, with their original signs. Fixed-mesh polynomial expectation
commutes with the finite time integral. L191(3) and (3) therefore give
zero cubic-scaled limit for E[dI_(i,a,delta)[W]] at every fixed delta
<=tau/2, and a uniform absolute bound by
C_i[N^(-1)eta(delta)+delta^(1/4)]. L190(2)–(3) then imply (4).

This is response-side uniform initial-time removal. It supplies no
separate fixed-delta mesh limit for E[I rho_H], and no mesh limit on
[delta,tau]. Neither the other final-time forest corrections nor the
independent response jets have been added or assumed to cancel.

## Mathlib

Full matching result and supporting relative-cochain, heat and Gaussian
statements: **not checked**; unknown coverage is not evidence of absence.
Finite Gaussian integration by parts is justified explicitly in (7),
also for singular S. The actual residual smooth-column and positive
prefix/tilt estimates are imported from the canonical results cited
above, with their hypotheses retained. The needed trace heat bounds,
polarization inequality and integrable envelope are proved here.
The unchanged [assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this partial attempt on the joint group. This is local standard-
method progress, classified REPRODUCTION, with no claim of progress
beyond the checked sources. Verification is analytic; no numerical
preview or finite-mode sample is treated as proof.
