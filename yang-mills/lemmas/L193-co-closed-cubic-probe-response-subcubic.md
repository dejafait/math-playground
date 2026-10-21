# L193 — The complete co-closed cubic probe response is subcubic

## Hypotheses

Use L181–L183's fixed-mesh SU(2) expansion in the relative box
(-4,4)^4, admitted even N, a=8/N, straight lower-rooted direction-1
forest, complete L008 displacement and both actual L010 probes i=3,6
at tau=1/16. The bare expansion precedes refinement. Coordinates and
adjoints are ordinary dimensionless full-link coordinates. Fixed links
are zero; all variable normal end rows and constant own-direction
modes remain. Vertex prefixes are pinned on every physical face.

Use precisely L183's notation

    C=D_1, L=C^T C, Delta=L+DD^T, P=1-D(D^T D)^(-1)D^T,
    S=P Delta^-1 P, z~N(0,S) independently in three colors,
    t(z)=2SAz, rho_H=script R_3(z)-d script S_3(z)[t(z)],
    b(z)=[z,q Phi z]/2-[D Phi z,q Phi z]/4,
    W(z)=P db(z)[t(z)],
    rho_F(z)=rho(pi_F Rz)=rho_H(z)-<Lz,W(z)>.

A=PAP includes both insertion subtractions; no positivity of A is
assumed. Put H_s=exp(-s Delta/a^2), E_(i,s)=H_(tau-s) Q_i H_tau.
Let T be the symmetric trilinear polarization of the complete action
cubic and T_i that of the full unflowed numerator cubic j_(i,3).
L181 and L189 give the co-closed probe polynomial

    F_i(z)=j_(i,3)(H_tau z)+integral_0^tau U_i(s,z) ds,
    U_i(s,z)=-(6/a^2)T(H_s z,H_s z,E_(i,s)z).             (1)

This is F_(i,3)(z), not F_(i,3)(Rz). The latter also contains the
independent final-time correction J_i=2<B_i z,b(z)> in L183.

## Conclusion

For both actual probes,

    a^3 E[F_i(z) rho_F(z)] -> 0.                         (2)

In particular, for every fixed 0<delta<=tau/2 the retained Duhamel
contribution on [delta,tau] has zero cubic-scaled limit. Its rho_H
pairing is O_delta(N^2); its W derivative has cubic-scaled absolute
integral O_delta(sqrt(a)). The final observable cubic has response
O(N^2). The full interval is handled by L192's uniform initial bound,
not by a mesh-dependent time cutoff.

Thus L183's original joint group satisfies only the reduction

    a^3 G_(i,a)=a^3{E[J_i rho_H]-E[dJ_i[W]]}+o(1).       (3)

No bound or limit for the right-hand prefix group is established here.
L187's Q_3 remains O(N^(7/2)), and its sextic partner remains
uncontrolled. The independent f_(i,2),r_0 term, finer asymptotics,
full compensation, finite matching, interacting reflected error
<=c_box/2, continuum axioms and infrared finite positive mass remain
open. This is local standard-method progress, with no claim of
progress beyond the sources in the unchanged approved assessment.

## Proof

### 1. Uniform exterior mode sums include the final flow endpoint

Use L191's complete product modes e_k=a^2 f_k, with physical
eigenvalues lambda_k, all component labels included. They satisfy

    c|k|^2<=lambda_k<=C|k|^2,
    ||e_k||_infinity<=Ca^2,
    ||C e_k||_infinity<=Ca^3(1+|k|).                     (4)

The positive gap and the allowed own-direction zero index are retained.
L191(6)'s eigenspace argument also bounds P e_k and each fixed number
of its physical differences by a^2 times a fixed polynomial in k:
expand in its eigenspace, whose mode count is polynomial in k, then
differentiate each product mode. No supremum contraction of P is used.

Here we must improve L191(8), which was stated only for s<=tau/2.
Write Q_i=a^2 Q_(i,a) and

    q_(i;kl)=<f_k,Q_(i,a)f_l>_a.

For every fixed nonnegative integer m,

    ||Delta_phys^m Q_(i,a) f_l||_a<=C_(i,m) p_m(l),
    |q_(i;kl)|<=C_(i,m) lambda_k^-m p_m(l),             (5)

with a fixed polynomial p_m, uniformly for sufficiently fine meshes.
We justify the extra regularity rather than assume output heat at s=tau.
L008(2),(6)–(7) writes Q_(i,a)=d_a^* M_(i,a) d_a, with finite adjacent
averages in M_(i,a). Its coefficients are the central strains of the
fixed smooth compact displacement. Every fixed physical difference of
these coefficients is uniformly bounded: a difference quotient is an
average of a derivative of that smooth displacement. Product modes
have physical differences of every fixed order bounded polynomially
in l, since |sin(a omega/2)|/a<=|omega|/2. The finite difference product
rule, iterated through d_a^* M_(i,a) d_a and then through the m physical
Laplacians, gives the first estimate in (5), even at high input indices.
For fixed m all these output stencils are inside a common compact
interior set for sufficiently small a. Consequently no boundary term or
zero-extension derivative is introduced. Self-adjointness of the full
relative Delta_phys and its eigenvector f_k gives the second estimate.
The proof applies to the triplet average of squares and the different
shear averaging operator separately; it does not replace either stencil.

For 0<=s<=tau and 0<=r<=tau/2 define

    E_(i,s)^(r)=H_(tau-s) Q_i H_(tau-r)
      =a^2 sum_(k,l) d_(i;kl)^(r)(s) e_k e_l^T,
    d_(i;kl)^(r)(s)=exp[-(tau-s)lambda_k-(tau-r)lambda_l]q_(i;kl).

For every fixed polynomial p_0, (5) implies

    sup_(s,r) sum_(k,l)|d_(i;kl)^(r)(s)|p_0(k)p_0(l)<infinity. (6)

Indeed choose m so that the k sum of |k|^-2m p_0(k) converges
in four dimensions. The remaining l polynomial is summable against
exp(-tau lambda_l/2). This includes s=tau, with no output heat, every
boundary mode and the full high spectrum. It requires compact smooth
probe coefficients; it is not a claim for an arbitrary bounded Q.

For later use, Minkowski's inequality in this exact mode expansion,
||e_l^T z||_(L^p)<=C_p a^-1 lambda_l^-1/2, and (4),(6) give

    sup_e ||(E_(i,s)^(r) z)_e||_(L^p)<=C_(i,p) a^3,
    sup_p ||(C E_(i,s)^(r) z)_p||_(L^p)<=C_(i,p) a^4.    (7)

Here p in a subscript of a circulation is a plaquette, whereas L^p
denotes a fixed finite Gaussian moment norm. The same bounds hold for
all colors. Correlations of the mode coefficients do not affect
Minkowski's inequality. In particular no derivative is taken through a
rough prefix or tilt to obtain (7).

### 2. Transfer heat in a pure cubic contraction before estimating rho_H

For fixed r>0, the complete spectrum and (4), including the polynomial
P e_k bound, give for every fixed finite moment order p

    sup_e ||(H_r z)_e||_(L^p)<=C_(r,p) a,
    sup_p ||(C H_r z)_p||_(L^p)<=C_(r,p) a^2.            (8)

For example expand z using S^(1/2)e_k=(a sqrt(lambda_k))^-1 P e_k
and independent standard Gaussian coefficients. Squared row sums are
bounded by a^2 times a full exponentially weighted polynomial sum;
circulation contributes another a. Gaussian moment formulas give all
fixed p. The analogous Euclidean norms are
||H_r z||_G<=C_r a^-1 and ||C H_r z||_G<=C_r.

The actual smoothed tilt also obeys a much smaller row bound than a
rough tilt. L185(5)–(6), with A's two subtractions retained, gives

    ||2SAS e_k||_infinity<=Ca^2 p(k).

Since S commutes with H_r, its Gaussian column on the smoothed input is

    2SA H_r S^(1/2)e_k
       =a sqrt(lambda_k) exp(-r lambda_k) (2SAS e_k).

Summing the squared bounds proves

    sup_e ||t(H_r z)_e||_(L^p)<=C_(r,p) a^3.             (9)

The order is exactly 2SA H_r. This proof neither commutes A with heat
nor applies residual consistency to t(z) with a rough input.

L190 section 2 records the full local cubic residual's coefficient
sum at most C N per placement, bounded stencil size, O(N^4)
placements, and the action's O(1) coefficients on every plaquette.
Gaussian Holder and Minkowski, applied to (8)–(9), therefore give

    ||script R_3(H_r z)||_2<=C_r N^4 N a^3<=C_r N^2,
    ||d script S_3(H_r z)[t(H_r z)]||_2
                                  <=C_r N^4 a^2 a^3<=C_r a,
    ||rho_H(H_r z)||_2<=C_r N^2.                        (10)

No circulation gain or cancellation was used in this residual count;
all local words and both insertion subtractions are included. It is
a bound on a smoothed polynomial only, not on rho_H(z) or rho_F(z).

We need the following exact finite Gaussian heat-transfer identity.
For invariant color-alternating cubics g,h and any r>=0,

    E[g(H_r z) h(z)]=E[g(H_(r/2)z) h(H_(r/2)z)].        (11)

Internal contractions of either cubic vanish by their distinct colors,
also after these color-diagonal linear maps. Isserlis' theorem leaves
only the three cross-covariances. On the left each is H_r S; on the
right each is H_(r/2) S H_(r/2)=H_r S. The tensor contractions,
including signs and multiplicities, are identical. This proves (11)
for singular S as well, with no inverse heat estimate or positivity
assumption on the cubic coefficients. In particular h may be the
nonlocal rho_H. It does not assert a transfer through A term by term.

Fix 0<delta<=tau/2 and delta<=s<=tau. Define

    g_s(v)=-(6/a^2)T(H_(s-delta)v,H_(s-delta)v,
                              H_(tau-s)Q_i H_(tau-delta)v).

Then U_i(s,z)=g_s(H_delta z). At v=H_(delta/2)z both short
times are >=delta/2 and the external map is E_(i,s)^(delta/2).
Every term in the complete polarized action has one circulation,
as proved in L189(5)–(6). From (7)–(8), its row L^2 product is at
most C_delta a^6: either a^4 a a or a^3 a^2 a. There are O(a^-4)
plaquettes and the original coefficient is O(a^-2). Gaussian Holder
therefore gives

    sup_(delta<=s<=tau)||g_s(H_(delta/2)z)||_2<=C_delta.  (12)

Apply (11) to g_s and rho_H and then use (10),(12):

    sup_(delta<=s<=tau)|E[U_i(s,z) rho_H(z)]|
                                      <=C_delta N^2.   (13)

The entire retained rho_H pairing is consequently subcubic, including
s=tau. No limit of its two original cumulants separately is assumed.

### 3. Retain all W derivative placements on the positive-time interval

L190(8) gives the exact three derivative placements. L191's external
placement proof uses its mode sum only in (8),(16); its other estimates
are valid for the full range of s with unchanged fields. Replace that
mode sum by (6) with r=0. Its smooth output bound

    ||<e_l,W^c>||_2<=C p(l) N^3                         (14)

is L191(9)–(13), retaining both derivatives of b and the signed
whitened tilt. Its quadratic action coefficient bound from (14)–(15)
there remains ||T(H_s z,H_s z,e_k^c)||_2<=Ca p(k)m_a(s).
Thus the original external placement, with its single -6/a^2, obeys

    |E[V_(i,a)(s)]|<=C_i N^2 m_a(s), 0<=s<=tau.         (15)

For the other two placements L192(7) contracts the same smooth
external Gaussian slot before any inequality. Its exact linear field
X_l^c=dW[h_l^c], h_l^c=S e_l, satisfies
||X_l^c||_G<=Cp(l)N^(9/2). Both db[k_l] and d^2b[h_l,t],
k_l=2SAS e_l, are retained. Its heat estimates (13) and full polarized
action inequality (14) likewise hold for s<=tau. Again the only use
of s<=tau/2 in its contraction proof was the exterior mode sum (5).
Using (6) instead gives exactly

    a^3 |B_(i,a)(s)|
       <=C_i sqrt(a)[(s+a^2)^(-1/2)+(s+a^2)^(-1)],
                                                   0<=s<=tau. (16)

This extension uses the new endpoint regularity (5); it is not an
unjustified continuation of the former output heat bound. The actual
prefix estimates, upper jump, action circulation placements and signs
are unchanged. On [delta,tau], (15)–(16) give

    a^3 integral_delta^tau |E[dU_i(s,z)[W(z)]]| ds
                                      <=C_delta(a+sqrt(a)) ->0. (17)

In particular no cancellation between these placements is required.
L183's divergence-free Gaussian IBP, used at each fixed mesh, gives
E[U_i(s)rho_F]=E[U_i(s)rho_H]-E[dU_i(s)[W]]. Equations
(13),(17) prove the claimed zero retained-interval limit.

For the initial interval use L192(4) without extending its hypotheses:

    a^3 |E[(integral_0^delta U_i(s)ds)rho_F]|
                        <=C_i[eta(delta)+delta^(1/4)].  (18)

First take the mesh limsup at fixed delta in (13),(17),(18), and
then delta down to zero. This proves a zero cubic limit for the
complete Duhamel response. The constants C_delta may diverge at zero;
none is used in (18), and delta is never chosen depending on mesh.

### 4. The final observable cubic obeys the same subcubic test

Both actual j_(i,3) have bounded local coefficients and at least one
linear circulation in each trilinear term, before polarization.
For the triplet this is the plaquette-trace cubic proportional to
<Cy,w_2(J_p y)> from L189(5), with L010's bounded strain weights.
For the shear, expand L010(2)'s product of two clovers to degree three:
each term is a linear clover times a quadratic clover. The linear
clover is a finite average of oriented circulations; the quadratic
clover is a finite sum of brackets of two selected edges from its
four-link words. All basepoints, signs and weights remain. Thus both
polarizations T_i satisfy L192(14)'s inequality with a probe-dependent
constant. Fixed zeros and finite local shifts do not change its proof.

Consequently ||j_(i,3)(H_(tau/2)z)||_2<=C_i by (8): each local
product is O(a^4) in L^2 and there are O(a^-4) placements. Apply
(11) with g=j_(i,3), r=tau, h=rho_H and then (10) to obtain

    |E[j_(i,3)(H_tau z)rho_H(z)]|<=C_i N^2.             (19)

For its derivative retain the original direction H_tau W:

    d(j_(i,3)(H_tau z))[W]
      =3 sum_(k,c) exp(-tau lambda_k)
                       T_i(e_k^c,H_tau z,H_tau z)<e_k,W^c>.

The same full local polarization inequality and Gaussian Holder give

    ||T_i(e_k^c,H_tau z,H_tau z)||_2
      <=C_i{a^3 p(k)(a^-1)^2+a^2 p(k)a^-1}
      <=C_i a p(k).                                    (20)

Here the Euclidean Gaussian moment norms of H_tau z and its
circulation are O(a^-1) and O(1), respectively, by (8). A Euclidean
norm of a Gaussian vector has L^4 norm at most a fixed multiple of
its L^2 norm, from Isserlis' fourth moment formula. This justifies
Holder also for the correlated quadratic expression in (20).
Combine (14),(20), Gaussian Cauchy--Schwarz and the full heat sum:

    |E[d(j_(i,3)(H_tau z))[W]]|<=C_i a N^3<=C_i' N^2.   (21)

No prefix is smoothed at its input to get (21); (14) controls only
its actual smooth output coefficient. Applying L183's Gaussian IBP
to (19),(21) proves the final observable response is O(N^2).
Together with the Duhamel conclusion this proves (2). L183(5)–(6)
then gives (3), with both prefix expectations and their signs intact.

### 5. Verification and qualifications

Verification is analytic. The endpoint mode estimate (5) uses the
actual compact probe stencils and all fixed physical difference
orders; (11) checks every surviving Gaussian cross line before any
norm bound. The mesh powers in (10),(12),(20) count every placement
and circulation. Equations (15)–(17) retain all three derivatives
and the original factors -6 and -12, rather than assigning smoothness
to W or the rough tilt. Equation (18) supplies an independent uniform
initial error before delta removal. No finite spectral diagnostic,
numerical certificate or assumed separate-term convergence is used.

The co-closed contribution is only one part of L183(5). Neither its
zero cubic coefficient nor the improved smoothed residual bound
controls the unsmoothed final-time J_i/rho_F contraction. In particular
the heat transfer in (11) requires common input heat on all three
probe slots, which J_i's explicit prefixes do not supply. No result
here changes the known Q_3 bound or proves forest invariance.

## Mathlib

Full matching result and supporting relative-cochain, nonlinear probe
and Gaussian heat-transfer statements: **not checked**. Unknown coverage
is not evidence of absence. The named standard input is Isserlis'
Gaussian pairing theorem, specialized explicitly in (11), along with
finite-dimensional Gaussian integration by parts already proved in
L183. The compact-stencil regularity and applicability arguments are
given above; general flow renormalization is neither reproved nor
imported as a selected-group bound. The unchanged
[assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
approves this partial attempt within its joint target. Classification
REPRODUCTION records local standard-method progress, without an
originality or complete-response claim.
