# C212c — Bound the co-closed two-quadratic-flow response

## Hypotheses

Use L212's SU(2) setting, relative box (-4,4)^4, admitted even
meshes a=8/N, straight lower-rooted direction-1 forest, complete
L008 displacement, both actual L010 probes i=3,6 and tau=1/16.
Take the bare expansion at fixed mesh before refinement. All norms
and transposes below use ordinary dimensionless full-link coordinates.
Fixed links are zero; every variable normal end edge is included.

Write D=D_0, C=D_1, L=C^T C, Delta=L+DD^T,
P=I-D(D^TD)^(-1)D^T, S=P Delta^(-1)P, and

    H_s=exp(-s Delta/a^2), E_s=exp(-s L/a^2).

Let z have three independent colors with covariance S. Retain L018's
actual residual A=PAP=A^T, including both insertion subtractions,
and put r(z)=sum_c (z^c)^T A z^c and v(z)=2SAz. The field v is a
signed linear tilt direction, not an independent Gaussian noise.

Let script S_3 be the complete full-link action cubic, before forest
restriction. L181 gives the actual exponential-coordinate quadratic
Wilson-flow vector field Q_2(y)=-a^(-2) grad script S_3(y). Define

    Z(z)=integral_0^tau E_(tau-s) Q_2(H_s z) ds,
    Z_delta(z)=integral_0^delta E_(tau-s) Q_2(H_s z) ds. (1)

Thus Z is L011's second flow jet on the co-closed initial input z.
It is not that jet on Rz. Its quadratic-output contribution is the
single summand j_(i,2)(Z) of F_(i,4)(z) inside L212's joint identity.
No isolated forest polynomial is transferred to the Hodge law.

## Conclusion

For both actual probes,

    |Cov_S(j_(i,2)(Z),r)| <= C_i N^3.                 (2)

For every fixed 0<delta<=tau/2, the same full response satisfies

    Cov_S(j_(i,2)(Z),r)
      -Cov_S(j_(i,2)(Z_delta),r)
                 =O_(i,delta)(N^2 log(eN)).           (3)

Consequently its cubic-scaled asymptotics, if any, are unchanged by
retaining only the initial/initial time square [0,delta]^2 in this
summand. Equation (3) includes both cross rectangles and the remaining
square, rather than discarding them by a time-support claim. No
estimate tending to zero uniformly as delta decreases is proved for
the retained square. Neither (2) nor (3) proves convergence, a sign,
or a nonzero contribution from times comparable to a^2.

The other three complete co-closed quartic terms, in particular the
nested DQ_2 z_2 contribution to z_3, and dF_(i,3)[b] remain outside
this estimate. C212a,b are unchanged. The complete quartic response,
endpoint convergence, compensation, finer asymptotics, finite matching,
the interacting reflected error <=c_box/2, continuum axioms and
infrared finite positive mass remain unresolved. This is a local
specialization of existing heat and Gaussian estimates; no originality
or progress beyond the checked literature is asserted.

## Proof

### 1. The actual output quadratic form retains a circulation

By L008(2), L010's leading-coefficient calculation and L018's
coordinate normalization, there is a real symmetric plaquette matrix
J_i such that

    Q_i=C^T J_i C, ||J_i||_op<=C_i,
    j_(i,2)(w)=sum_c <Cw^c,J_i Cw^c>.                (4)

Indeed q_(i,a)(w/a) has a^4 from its sum and a^(-2) from each
curvature d_a(w/a)=Cw/a^2, so these powers cancel. The triplet
matrix is bounded multiplication by its averaged strain. The shear
is a finite sum of bounded strain multipliers composed with the
actual adjacent clover averages, whose row and column multiplicities
are bounded independently of the mesh. Symmetrization gives J_i
without changing its quadratic form or a uniform norm bound. The
triplet remains an average of squares, not a squared clover average.
This proves (4) for the actual two stencils, including their transition
coefficients. It does not replace either nonlinear probe.

We use the mixed norm ||X||_(p,2)=(E||X||_ell2^p)^(1/p).
For p>=2, Minkowski's inequality gives

    ||X||_(p,2) <= (sum_j ||X_j||_Lp^2)^(1/2).       (5)

The sum includes all spatial, component and color indices. Ordinary
operator norms therefore act on this mixed norm with their usual
bound. All required moments below have fixed finite order.

### 2. Full-spectrum input bounds and the rough tilted input

The complete relative spectrum in L189, proof section 2, has ordinary
orthonormal component product modes e_k with

    ||e_k||_infinity<=C a^2,
    ||C e_k||_infinity<=C a^3(1+|k|),
    lambda_(k,dim)=a^2 lambda_(k,phys),
    c|k|^2<=lambda_(k,phys)<=C|k|^2.                 (6)

There are at most C m^3 modes with max k_j=m. The allowed constant
own-direction cosine index is included, while the other three sine
indices ensure a positive full one-form gap. The circulation estimate
holds on every relative end row, as explained in L189; it is not a
zero-extension assumption about the normal edge component.

Since 0<=S<=Delta^(-1), positive covariance comparison and (6) give,
for 0<=s<=tau and every fixed p<infinity,

    sup_e ||(H_s z)_e||_Lp
                    <= C_p a/(s+a^2)^(1/2),
    sup_p' ||(C H_s z)_p'||_Lp
                    <= C_p a^2/(s+a^2).              (7)

To verify the powers, their squared bounds follow respectively from

    C a^2 sum_(m=1)^(N-1) m exp(-c s m^2),
    C a^4 sum_(m=1)^(N-1) m^3 exp(-c s m^2).

At s=0 these sums are O(N^2) and O(N^4). For s>0 Gaussian integral
comparison gives O(s^(-1)) and O(s^(-2)), with harmless fixed-tau
constants. Taking the smaller of the cutoff and positive-time bounds
gives (7). Gaussian moment formulas extend the variance bounds to
each fixed p. This calculation includes s<a^2 and all modes and rows.

Let F=S^(1/2)AS^(1/2). L186(12), with its two subtractions retained,
gives ||F||_op<=C N. For one color,

    Cov(v)=4SASAS=4S^(1/2)F^2 S^(1/2)<=C N^2 S.     (8)

This is a positive comparison for the genuine covariance of v;
it does not declare 2SAS positive. Applying the same row comparisons
after H_s and C H_s proves (7) for H_s v with its right sides
multiplied by N. No independence of v and z is needed or claimed.
Both fields are co-closed, so E_s z=H_s z and E_s v=H_s v only
on these initial linear fields.

### 3. Preserve both pieces of the full action derivative

L189(5)--(6) retains the ordered full-link plaquette words and gives
the exact decomposition

    script S_3(y)=sum_p <(Cy)_p,w_2(J_p y)>,
    grad script S_3(y)=C^T W(y)+V(y),
    W_p(y)=w_2(J_p y).                               (9)

Here J_p selects the four signed links, with physically fixed entries
zero. The field V is defined without approximation by

    <V(y),h>=sum_p <(Cy)_p,dw_2(J_p y)[J_p h]>.

The map w_2 is the complete (1/2) sum of ordered color brackets.
Thus W is quadratic in neighboring y entries, and V is a fixed
finite sum of products of a neighboring y and Cy. Every local
coefficient and the number of incidences per row are uniformly
bounded, including boundary plaquettes. No forest zeros are imposed.

Put y_s=H_s z. Holder's inequality, (5), (7), and O(N^4)=O(a^-4)
rows now give

    ||W(y_s)||_(4,2) <= C/(s+a^2),
    ||V(y_s)||_(4,2) <= C a/(s+a^2)^(3/2).            (10)

For example each W entry has L4 norm at most C a^2/(s+a^2),
using the L8 bounds on its two factors; taking the square root of
the row count supplies a^(-2). Each V entry instead has bound
C a^3/(s+a^2)^(3/2). These estimates retain correlations by Holder.

Differentiate both quadratic factors in (9), in the actual initial
direction v(z). The two derivatives replace each occurrence of y_s
in turn by H_s v. Equations (7)--(8) and the same Holder calculation
give (10) for these derivatives with an additional factor N. The
direction v is linear in z, and both input slots are differentiated;
no random prefix or covariance is held fixed in this operation.

### 4. Integrate both flow endpoints with the output circulation

The finite cochain identity CD=0 and singular-value calculus for C
give, for t>0,

    ||C E_t C^T||_op <= C min(1,a^2/t),
    ||C E_t||_op     <= C min(1,a/sqrt(t)).           (11)

For a singular value sigma of C, the relevant values are respectively
sigma^2 exp(-t sigma^2/a^2) and
sigma exp(-t sigma^2/a^2); ||C|| is uniformly bounded. The gradient
kernel contributes zero only after this displayed circulation is
applied. At t=0 use the finite incidence norm. Consequently (11)
keeps the full E_t rather than replacing it on a nonlinear field
by H_t without its projection.

From (1),(9), and Q_2=-a^(-2) grad script S_3,

    C Z=-a^(-2) integral_0^tau {
        C E_(tau-s) C^T W(y_s)+C E_(tau-s) V(y_s)} ds. (12)

On 0<=s<=tau/2, the lag tau-s is bounded below. Equations
(10)--(11), followed by Minkowski, bound its mixed norm by

    C integral_0^(tau/2) {
       (s+a^2)^(-1)+(s+a^2)^(-3/2)} ds
                         <= C[log(eN)+a^(-1)]<=C N. (13)

The second integral is exactly
2[a^(-1)-(tau/2+a^2)^(-1/2)]. It is not bounded uniformly in the
cutoff, and no initial interval has been discarded.

On tau/2<=s<=tau, (10) is bounded respectively by C and C a.
Set t=tau-s and T=tau/2. Its contribution is at most

    C a^(-2) integral_0^T min(1,a^2/t) dt
       +C a^(-1) integral_0^T min(1,a/sqrt(t)) dt
                         <= C log(eN).               (14)

For sufficiently small a, the first integral is
a^2[1+log(T/a^2)]; the second is at most 2a sqrt(T).
The t=0 endpoint is handled by the bounded-incidence branch of
each minimum, not by a divergent heat derivative estimate.
Together (13)--(14), and the differentiated versions of (10), prove

    ||C Z||_(4,2)<=C N,
    ||C dZ(z)[v(z)]||_(4,2)<=C N^2.                 (15)

For Z^tail=Z-Z_delta, with delta fixed in (0,tau/2], the first
integral begins at delta. It is then bounded independently of a,
with a delta-dependent constant. The final contribution (14) stays.
Hence

    ||C Z^tail||_(4,2)<=C_delta log(eN),
    ||C dZ^tail[v]||_(4,2)<=C_delta N log(eN).       (16)

The original bounds (15) also hold for Z_delta. All operations so
far are finite-mesh polynomial integrals. They neither interchange
mesh and time limits nor give a uniform delta-removal statement.

### 5. Contract the actual residual and keep the cross rectangles

L212(12)'s normalized Gaussian integration-by-parts identity gives
for any of these quartic polynomials P

    Cov_S(P,r)=(1/2) E[dP(z)[v(z)]].                 (17)

It holds also for the singular ambient covariance. For
P=j_(i,2)(Z), (4) cancels its quadratic derivative's factor 2
against the 1/2 in (17), leaving exactly

    Cov_S(j_(i,2)(Z),r)
       =E sum_c <CZ^c,J_i C(dZ[v])^c>.              (18)

Cauchy--Schwarz, (4) and (15) prove (2). We used a signed derivative
and genuine Gaussian moment bounds, never a positive model for the
tilt. All three colors and both input slots are retained.

To prove (3), expand the difference of the two quadratic polynomials
using Z=Z_delta+Z^tail. Its three resulting terms are
2<CZ_delta,J_i CZ^tail> and <CZ^tail,J_i CZ^tail>, with color sums.
Differentiate each in (17). The two cross derivatives are bounded by
C_delta N^2 log(eN), using (15)--(16); the tail-square derivative
is bounded by C_delta N log(eN)^2, which is also
O_delta(N^2 log(eN)). This proves (3) with both cross rectangles
and the tail square included once. Since a^3=512/N^3, the error
in (3) tends to zero after cubic scaling, while (2) supplies only
boundedness for the retained initial square.

No numerical or synthetic test is used as evidence for these
all-mesh inequalities. The verification is the exact action split
(9), full relative shell bounds (7), both singular-value estimates
(11), their explicit endpoint integrals, and the correctly normalized
quadratic derivative (18). The proof never assumes convergence of
this summand or transfers an isolated forest jet, avoiding L022's
obstruction. L212 keeps every correlated prefix and endpoint
correction elsewhere in the original complete response.

## Mathlib

Full matching result: **not checked**. Supporting coverage of finite
cochain heat bounds, Gaussian moment and integration-by-parts formulas,
singular-value calculus and mixed-norm inequalities: **not checked**;
unknown coverage is not evidence of absence. The standard inputs are
Gaussian moments, Holder, Minkowski and Cauchy--Schwarz; their needed
finite-dimensional specializations and endpoint integrations are given
above. The existing local action/flow, spectrum and signed-form inputs
are used under unchanged hypotheses. The reused
[assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
imports no flow-renormalization theorem as a bare selected-response
estimate. This is not a reproof of general flow renormalizability.
