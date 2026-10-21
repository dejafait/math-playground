# L191 — The external derivative placement in the initial flow interval is subcubic

## Hypotheses

Use L189–L190's fixed-mesh SU(2) expansion in the relative box
(-4,4)^4, admitted even N, a=8/N, the straight lower-rooted direction-1
forest, complete displacement and both actual L010 probes i=3,6 at
tau=1/16. The bare expansion precedes refinement. All matrices use
ordinary dimensionless full-link coordinates, with fixed links zero
and every variable normal end edge retained. Prefix vertex values are
pinned on every physical face.

Keep L183's exact definitions

    Delta=L+DD^T, P=1-D(D^T D)^(-1)D^T, S=P Delta^(-1)P,
    z ~ N(0,S) in each of three independent colors,
    t(z)=2SAz, phi=Phi z,
    b(z)=[z,q phi]/2-[D phi,q phi]/4, W=P db(z)[t(z)].

A=PAP is the complete symmetric residual, including both insertion
subtractions. In particular differentiating b retains both occurrences
of Phi t. Let H_s=exp(-s Delta/a^2), E_(i,s)=H_(tau-s) Q_i H_tau,
and let T be the symmetric trilinear polarization of the full action
cubic, script S_3(y)=T(y,y,y), on combined link/color space. Select the
third placement of L190(8), with its original sign and normalization:

    V_(i,a)(s,z)=-(6/a^2) T(H_s z,H_s z,E_(i,s)W(z)).     (1)

This is one scalar quartic polynomial, not the full dU(s)[W].

## Conclusion

Set ell(r)=1+log(1+1/r) and

    m_a(s)=ell(s+a^2)^(1/2)
                  +(s+a^2)^(-1/2)ell(s+a^2)^(1/4),
    eta(delta)=delta ell(delta)^(1/2)
                         +sqrt(delta)ell(delta)^(1/4).

For all sufficiently fine admitted meshes and 0<=s<=tau/2,

    |E[V_(i,a)(s)]| <= C_i N^2 m_a(s).                  (2)

Consequently for 0<delta<=tau/2,

    a^3 integral_0^delta |E[V_(i,a)(s)]| ds
          <= C_i N^(-1) eta(delta).                     (3)

Thus this entire placement has zero cubic-scaled limit at each fixed
delta, and its initial interval is uniformly removable. No sign is
asserted. In contrast the sum of the two remaining placements is still

    -(12/a^2) E[T(H_s W,H_s z,E_(i,s)z)],                (4)

by symmetry of T. No cubic bound or limit for (4) is proved here.
L190 controls the rho_H pairing separately; together these results do
not remove the complete initial interval. The final-time prefix-probe
quartic and sextic, positive-time response limit, independent
f_(i,2),r_0 term, finer asymptotics, full compensation, finite matching,
interacting reflected error <=c_box/2, continuum axioms and finite
positive infrared mass remain unresolved.

## Proof

### 1. Keep the complete external heat expansion and projection

Use the real full relative product modes e_k=a^2 f_k of L026(6)–(7),
ordinary orthonormal in link coordinates. Here lambda_k denotes their
PHYSICAL eigenvalue, so Delta e_k=a^2 lambda_k e_k. The component label
is included in k. There is one cosine index, allowed to be zero, and
three strictly positive sine indices. The sine bounds give

    c|k|^2 <= lambda_k <= C|k|^2,
    ||e_k||_infinity <= C a^2,
    ||C e_k||_infinity <= C a^3(1+|k|),                 (5)

where C=D_1. The last estimate is L189(11)'s mode estimate: every
unscaled circulation difference of these products supplies a factor
at most C a|k|, also on normal end rows. No zero extension across a
free normal edge is used.

We will also need a smooth bound on P e_l, rather than an assumed
supremum contraction for P. Since P commutes with Delta, P e_l lies
in its lambda_l eigenspace and has Euclidean norm at most one. Every
product mode e_k in that eigenspace has |k|<=C|l| by (5). The number
of such modes, including all component labels, is at most
C(1+|l|)^4. Expand P e_l in this eigenspace and apply Cauchy--Schwarz
at each link, then (5). This proves

    ||P e_l||_infinity <= C a^2 p(l),                    (6)

with, for example, p(l)=(1+|l|)^2 after increasing C. This argument
allows spectral degeneracies and the nonlocal projection. It retains
every allowed constant own-direction mode and every boundary row.

L185(3)–(4) fixes the actual normalization Q_i=a^2 Q_(i,a) and the
bound

    q_(i;kl)=<f_k,Q_(i,a)f_l>_a,
    |q_(i;kl)|<=C_i sqrt(lambda_k lambda_l).

Hence, in the original matrix order,

    E_(i,s)=a^2 sum_(k,l) d_(i;kl)(s) e_k e_l^T,
    d_(i;kl)(s)=exp[-(tau-s)lambda_k-tau lambda_l]q_(i;kl).
                                                               (7)

For every fixed polynomial p_0, the complete sums obey

    sup_(0<=s<=tau/2) sum_(k,l)
             |d_(i;kl)(s)|p_0(k)p_0(l) <= C_(i,p_0).     (8)

Indeed (5) bounds the polynomial eigenvalue factors and the two heat
exponentials by a summable infinite Gaussian mode sum. No truncated
spectrum or change of probe is used. Both exterior heat intervals
in (7) are bounded away from zero; neither short-time H_s is changed.

### 2. A smooth output coefficient of W retains both moving prefixes

For a deterministic spatial link vector v and a color c define
b_v^c=<v,b^c>. It is a quadratic polynomial in the other two colors.
Write K=Phi S Phi^T. The endpoint matrices in its two brackets have
operator norm at most C||v||_infinity, by the bounded row and column
degrees of D and q. L182(14)–(15)'s bilinear trace estimates imply

    ||b_v^c||_2 <= C ||v||_infinity
         [(||S||_HS ||K||_HS)^(1/2)+||K||_HS].           (9)

Here is the correlated quadratic specialization explicitly. Write each
bracket using its two distinct color components, expand its two signed
products, and use the triangle inequality. The two color fields in each
product are independent, although z and Phi z in a given color are
correlated. The first product therefore has squared norm of the form
Tr(S M_v K M_v^T), bounded by
||M_v||_op^2 ||S||_HS ||K||_HS. The second has two K factors and
is bounded by ||N_v||_op^2 ||K||_HS^2. This is the named Isserlis
Gaussian pairing theorem in exactly its two-color bilinear case;
no independence between a prefix and the original field is assumed.

The full-prefix estimates L182(10)–(11) give

    ||K||_HS<=C N^4, ||S||_HS<=C N^2 sqrt(log(eN)).

Insert v=P e_l in (9) and use (6). Since a=8/N and
log(eN)^(1/4)<=C N, this gives

    ||b_(P e_l)^c||_2
       <= C p(l)[N log(eN)^(1/4)+N^2]
       <= C p(l) N^2.                                   (10)

To differentiate this polynomial in the actual direction t, use L183
section 5's whitened residual bound. Choose Z onto im P with ZZ^T=S,
write z^c=Z xi^c, and put M=2Z^T A Z. Then

    t^c=ZM xi^c, M=M^T, ||M||_op<=C N.                 (11)

This does not commute A and S or assert positivity of M. For each
fixed c, collect b_v^c as (xi^d)^T B_v xi^e, where d,e are the two
other colors. Its L2 norm is exactly ||B_v||_HS. The directional
derivative replaces B_v by M^T B_v+B_v M. Therefore

    ||db_v^c(z)[t(z)]||_2
           <=2||M||_op ||b_v^c||_2.                     (12)

This differentiates both inputs of b, including both prefix inputs;
it is not differentiation only of the explicit unprefixed z. Since
P is fixed and self-adjoint, <e_l,W^c>=db_(P e_l)^c[t]. Combining
(10)–(12) proves

    ||<e_l,W^c>||_2 <= C p(l) N^3.                     (13)

The bound is on a smooth output coefficient, not on the full norm
of W or on a smooth realization of its random tilt input. K and the
original Phi retain their upper pinned jump throughout.

### 3. The two short-time action slots still supply an integrable bound

Let e_k^c be e_k in color c and zero in the other colors. Put y=H_s z
and F_(k,c)(s)=T(y,y,e_k^c). L189(5)–(6) gives the complete action
word and its derivative. Since 3F_(k,c)=d script S_3(y)[e_k^c],
there are three types: one with C e_k and two uncirculated y slots,
and two with e_k, a circulated y slot and an uncirculated y slot.
All physically fixed rows are zero in these same full words.

Use L189(7)–(8), including times below a^2, for their true covariances:

    C_s=H_s S H_s, K_s=C C_s C^T,
    ||C_s||_HS<=C a^(-2) ell(s+a^2)^(1/2),
    ||K_s||_HS<=C (s+a^2)^(-1).                         (14)

For each type, expanding the fixed color of e_k^c leaves a sum of
bilinear products in two distinct independent colors. The local
matrices between these two fields have norm at most C||C e_k||_infinity
for the first type, and C||e_k||_infinity for the other types, by the
bounded plaquette incidence count. The same bilinear trace inequality
used in (9) therefore gives

    ||F_(k,c)(s)||_2
       <= C[||C e_k||_infinity ||C_s||_HS
              +||e_k||_infinity (||K_s||_HS ||C_s||_HS)^(1/2)]
       <= C a p_1(k) m_a(s).                            (15)

The finite triangle inequality includes every differentiated action
slot and its original tensor coefficient. Correlations between this
quadratic polynomial and W will be kept in the next expectation;
(15) does not replace that expectation by independent fields.

### 4. Contract in the external heat order and integrate

Insert (7) into (1), expanding the three output colors of W. Exactly,

    E[V_(i,a)(s)]
       =-6 sum_(k,l,c) d_(i;kl)(s)
                    E[F_(k,c)(s) <e_l,W^c>].            (16)

The external a^2 cancels the original a^(-2) once. No prefix or tilt
matrix has been moved through a heat factor. Gaussian Cauchy--Schwarz
in each actual, possibly correlated expectation, (13), (15), and
the full sum (8) yield

    |E[V_(i,a)(s)]|
       <= C_i a N^3 m_a(s)=C_i' N^2 m_a(s),

which proves (2). In particular the tilt bound (11) was applied only
after taking a smooth output coefficient of b; it was not used to
assign residual consistency to either rough short-time slot.

For s>0, m_a(s)<=ell(s)^(1/2)+s^(-1/2)ell(s)^(1/4).
L189 section 5 proves that this majorant integrates on [0,delta]
to at most C eta(delta). It is uniform in a and includes the whole
interval s<a^2. Multiplication by a^3 and a=8/N now proves (3).
At fixed mesh all polynomials are continuous in s, so ordinary finite
Gaussian integration and time integration are legitimate. Equation
(3), rather than an assumed interchange of limits, supplies the
uniform small-interval conclusion for this placement alone.

The two other terms of L190(8) coincide by symmetry of T and give
(4). Their W output is smoothed only for time s, so (7)–(8)'s two
positive external heat intervals do not apply to that output. No
estimate in this proof is transferred to them. Their signed joint
contraction remains the obstruction to complete initial-time removal.

## Mathlib

Full matching result and supporting Gaussian, relative-cochain,
projection and heat estimates: **not checked**. Unknown availability
is not evidence of absence. Isserlis' named pairing theorem is used
only in the explicit bilinear specializations (9), (12), and (15).
The finite matrix inequalities and the projected-mode estimate are
proved here; the full-prefix, residual and spectral estimates are
imported from the canonical results cited above. No general flow
renormalizability theorem is reproved or used outside its hypotheses.
The unchanged [assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this partial attempt on the joint response. This is local
standard-method progress, classified REPRODUCTION, with no claim of
progress beyond the checked sources. Verification is analytic; no
truncated-mode diagnostic is used as a proof of the estimate.
