# C212h — The complete co-closed two-quadratic-flow response is subcubic

## Hypotheses

Use L212's SU(2) bare fixed-mesh expansion in the relative box
(-4,4)^4, admitted even meshes a=8/N, straight lower-rooted direction-1
forest, L008's complete displacement, and both actual L010 probes
i=3,6 at tau=1/16. Refinement follows the bare expansion. All norms
and transposes use ordinary dimensionless full variable-link
coordinates, with three colors and every normal end edge. Fixed
boundary links have zero coordinates; vertex potentials are pinned
on every physical face, including the upper prefix endpoint.

Keep exactly C212c's notation

    C=D_1, D=D_0, L=C^T C, Delta=L+DD^T,
    P=I-D(D^T D)^(-1)D^T, S=P Delta^(-1)P,
    H_s=exp(-s Delta/a^2), E_s=exp(-s L/a^2).

The colors of z are independent with covariance S. The actual
symmetric residual A=PAP retains both insertion subtractions, and

    r(z)=sum_c (z^c)^T A z^c, v(z)=2SAz,
    F=S^(1/2)AS^(1/2), ||F||_op<=C N.                 (1)

The bound in (1) is L186(12), under these unchanged hypotheses.
Let Z be C212c(1)'s entire co-closed quadratic-flow jet,

    Z(z)=-a^(-2) integral_0^tau E_(tau-s)
                       grad script S_3(H_s z) ds.    (2)

The complete full-link action cubic is retained. In C212c(9), or
equivalently L189(5)--(6), its exact derivative splits as

    grad script S_3(y)=C^T W(y)+V(y),
    W_p(y)=(1/2) sum_(r<t) [(J_p y)_r,(J_p y)_t],
    <V(y),h>=sum_p <(Cy)_p,dW_p(y)[h]>.             (3)

Here J_p selects the signed links of the plaquette, with only
physically fixed links replaced by zero. In particular no forest
restriction is made inside (3). For the actual quadratic numerator,
C212c(4) gives Q_i=C^T J_i C with ||J_i||_op<=C_i and
j_(i,2)(w)=sum_c <Cw^c,J_i Cw^c>. The symbol J_i is the bounded
plaquette matrix, whereas J_p is the local link selector.

## Conclusion

With ||X||_G=(E||X||_ell2^2)^(1/2), including colors,

    ||CZ||_G<=C log(eN),
    ||C dZ(z)[v(z)]||_G<=C N log(eN).                (4)

Consequently, for both actual probes,

    |Cov_S(j_(i,2)(Z),r)|<=C_i N log(eN)^2,
    a^3 Cov_S(j_(i,2)(Z),r) -> 0.                   (5)

This controls the entire time square, including its initial corner.
Combined with C212g(3), the complete original forest response obeys

    K_(i,a)=kappa_0(f_(i,2),r_0)
           =K^(c)_(i,N)+O_i(N^(5/2)log(eN)),         (6)
    K^(c)_(i,N)=Cov_S(2<B_i z,c(z)>,r),

where c and B_i are exactly L212's and K^(c) has C212b(4)'s full
signed contraction. The endpoint is still only O(N^3). Thus a finite
cubic-scaled limit of the complete quartic response exists if and
only if that of this endpoint response exists, with equal limits.
Neither limit nor its value or sign is proved here. Full compensation,
finer asymptotics, finite matching, reflected error <=c_box/2,
continuum axioms and infrared finite positive mass remain unresolved.
This is a local specialization of standard Gaussian and matrix bounds,
not a claim of progress beyond the literature checked.

## Proof

### 1. Bound the forcing covariance before counting its output rows

For one color set y_s=H_s z and G_s=Cov(y_s)=H_s S H_s.
The full relative spectral gap and pointwise estimates C212c(6)--(7)
give, uniformly for 0<=s<=tau,

    ||G_s||_op<=C a^(-2),
    max_e (G_s)_(ee)<=C a^2/(s+a^2),
    max_p (C G_s C^T)_(pp)<=C a^4/(s+a^2)^2.        (7)

The first estimate follows from S<=Delta^(-1) and the smallest
dimensionless eigenvalue being at least c a^2. The other two are
exactly the squared Gaussian row estimates already proved there.
Their sine/cosine shell sums include s<a^2, all normal end rows,
and constant own-direction modes. There is no zero full one-form
mode, since each component has three transverse sine indices.

Here is a finite matrix argument for using (7). Let u and w be
independent centered vectors of distinct colors, each with covariance
G_s. Let U select possibly repeated signed coordinates of u, with
uniformly bounded repetition, and let T select either coordinates
or circulated coordinates of w. Let d_j be bounded deterministic
coefficients and q_j=d_j (Uu)_j (Tw)_j. For any real vector h,
conditioning on w gives

    E|sum_j h_j q_j|^2
      <=||U G_s U^T||_op sum_j h_j^2 d_j^2
                                      (T G_s T^T)_(jj)
      <=C ||G_s||_op max_j (T G_s T^T)_(jj) ||h||^2. (8)

The second inequality uses ||U||_op<=C from bounded repetition.
This proof requires neither independence of spatial rows nor
entrywise positivity of G_s. The mean of q is zero by independence
of the two colors. Zero selector rows at fixed links cause no change.

Each color component of W is a finite sum of families of this form,
with T another local link selector. Each color component of V has
one undifferentiated y_s coordinate and one (C y_s) coordinate of a
different color. Indeed differentiating the scalar triple product
in (3) leaves the other two, distinct, colors. Its link output receives
only the finitely many adjacent plaquette contributions. Indexing
families by direction, plaquette orientation, local slot and color
therefore gives a number of families independent of N; each link
appears in U at most a fixed number of times. Boundary rows only
remove terms. The bounded coefficients are those of the complete
action word, without an a-dependent normalization.

If families are first indexed by plaquette incidences rather than
output links, their final aggregation is a fixed finite-incidence
matrix of uniformly bounded operator norm: both its row and column
absolute sums are bounded. Applying that matrix to (8) preserves
the estimate up to a fixed constant. The same observation applies
to stacking the three output colors. Thus (9) below bounds the full
output covariance operator, including cross-row and cross-color
entries, rather than just its diagonal blocks.

For a finite sum of these families, the inequality
E|sum_(j=1)^m X_j|^2<=m sum_j E|X_j|^2 absorbs their correlations.
Applying (8) and then (7), including the finite color sum, proves
the positive covariance operator bounds

    ||Cov(W(y_s))||_op<=C/(s+a^2),
    ||Cov(V(y_s))||_op<=C a^2/(s+a^2)^2.             (9)

Both W and V are centered. Their mutual independence is neither
asserted nor needed. Formula (9) concerns their genuine covariance,
not the signed residual tilt M=2SAS.

### 2. Use the long output heat interval in Hilbert--Schmidt norm

For tau/2<=t<=tau, the exact finite cochain relations give

    ||C E_t||_HS<=C_tau a,
    ||C E_t C^T||_HS<=C_tau a^2.                    (10)

For completeness, CD=0 and the commuting decomposition of Delta
imply C E_t=C H_t. Squaring the two norms in (10) gives respectively

    Tr(L exp(-2t L/a^2)),
    Tr(L^2 exp(-2t L/a^2)).

Their gradient-kernel contributions are exactly zero. On im P,
L=Delta. The full relative product spectrum used in C212c(6) has
dimensionless eigenvalues a^2 lambda_(k,phys), where
c|k|^2<=lambda_(k,phys)<=C|k|^2. Thus these traces are bounded by

    C a^2 sum_k |k|^2 exp(-c tau |k|^2),
    C a^4 sum_k |k|^4 exp(-c tau |k|^2).

The infinite sums converge, with the full component multiplicities
and all permitted constant indices retained. Restriction to im P
can only reduce the corresponding nonnegative trace. This proves
(10) without changing the finite-box covariance or boundary rows.

If X is a centered finite random vector and K is deterministic,

    ||K X||_G^2=Tr(K Cov(X) K^T)
                <=||Cov(X)||_op ||K||_HS^2.         (11)

For 0<=s<=tau/2 use (9)--(11) on the two terms of (3) in (2).
The complete early contribution Z_early satisfies

    ||C Z_early||_G
      <=C a^(-2) integral_0^(tau/2) {
           a^2/(s+a^2)^(1/2)+a^2/(s+a^2)} ds
      <=C log(eN).                                 (12)

Minkowski's inequality is applied to the actual correlated random
fields over time; it does not replace them by independent copies.
The first integral is
2[(tau/2+a^2)^(1/2)-a], uniformly bounded. The second is
log(1+tau/(2a^2)), bounded by C log(eN). These are finite integrals
down to zero at every mesh, not positive-time estimates extended
through an omitted initial layer.

For the late contribution tau/2<=s<=tau, C212c(10) gives
||W(y_s)||_G<=C and ||V(y_s)||_G<=C a. These also follow from
their local Gaussian fourth moments and the full O(a^-4) row count.
Use C212c(11)'s complete endpoint operator bounds, valid also at
t=0 by the bounded-incidence branch:

    ||C E_t C^T||_op<=C min(1,a^2/t),
    ||C E_t||_op<=C min(1,a/sqrt(t)).

Writing T=tau/2, this gives

    ||C Z_late||_G
      <=C a^(-2) integral_0^T min(1,a^2/t) dt
         +C a^(-1) integral_0^T min(1,a/sqrt(t)) dt
      <=C log(eN).                                 (13)

For a^2<=T the first integral is a^2[1+log(T/a^2)]
and the second is at most 2a sqrt(T). The finitely many coarser
admitted meshes are absorbed in the constant. Combining (12)--(13)
proves the first bound in (4). The full nonlinear E_t remains in
every formula; only its circulated output annihilates gradients.

### 3. Differentiate both quadratic slots without a rowwise loss

Represent z=S^(1/2)xi in each color, where xi is a standard real
Gaussian; zero eigenvalues of S are allowed. Then

    v=2SAz=S^(1/2)(2F)xi.                           (14)

On the combined color space put G=I_3 tensor (2F). It is symmetric
with ||G||_op<=C N. Each output coordinate of CZ is a homogeneous
quadratic whose two input colors are different, by (3). All heat
maps and C act identically on colors. At fixed mesh the time
integrals therefore give real symmetric matrices T_j with

    (CZ)_j=xi^T T_j xi,

and every diagonal color block of T_j is zero. In particular
Tr(T_j)=0. Differentiation in direction (14) gives exactly

    (C dZ[v])_j=xi^T (G^T T_j+T_j G)xi.             (15)

It includes both quadratic input slots; the fixed linear direction
v is not independently differentiated. Since G preserves colors,
the matrix in (15) also has zero diagonal color blocks and trace.
There is thus no constant-chaos contribution hidden in this step.

Isserlis' fourth-moment identity for a real symmetric trace-zero
matrix T gives E(xi^T T xi)^2=2||T||_HS^2. The ordinary matrix
ideal inequality yields

    ||G^T T+T G||_HS<=2||G||_op ||T||_HS.

Apply these facts to (15), square and sum over every output j:

    ||C dZ[v]||_G<=2||G||_op ||CZ||_G
                 <=C N log(eN).                    (16)

No covariance commutation with A is used. In particular (14) keeps
SA in its actual order; F is only the whitened signed residual.
The inequality controls a genuine Gaussian norm, not a positive
interpretation of M. It retains all correlations and all modes.
It proves the second bound in (4).

### 4. Return to the original connected response

The normalized quadratic Gaussian integration-by-parts identity
L212(12), specialized in C212c(18), is

    Cov_S(j_(i,2)(Z),r)
        =E sum_c <CZ^c,J_i C(dZ[v])^c>.              (17)

The factor 1/2 of the single-polynomial tilt cancels the factor 2
from differentiating the quadratic output. Both slots of Z have
already been differentiated in (15), with no additional outside
factor. Since ||J_i||<=C_i for each actual probe, Cauchy--Schwarz
and (4) prove (5). Its cubic-scaled upper bound is
C_i N^(-2)log(eN)^2, tending to zero with a^3=512/N^3.

Finally insert (5) into C212g(3). The bound N log(eN)^2 is absorbed
by N^(5/2)log(eN), proving (6). The scaled error there is
O(N^(-1/2)log(eN)), tending to zero. This proves the stated
equivalence of possible endpoint and complete quartic limits, not
their existence. C212b's endpoint contraction retains all correlated
prefixes, upper jumps and internal tilted placements.

The verification is analytic: (8) checks the full local covariance
bound, (10) the complete heat spectrum, (12)--(13) both endpoints,
and (15)--(17) the centered quadratic tensor and response factor.
No numerical diagnostic or mathematical script is needed. In
particular this result is about the co-closed summand already in
L212's joint retraction, not a transfer of the original forest jet
forbidden by L022/ATTEMPTS/010.

## Mathlib

Full matching theorem: **not checked**. Supporting coverage of
Isserlis' formula, covariance operator inequalities, finite cochain
heat traces and Hilbert--Schmidt ideal bounds: **not checked**.
Unknown availability is not evidence of absence. The finite Gaussian
and matrix specializations needed here are proved above. The existing
[assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
covers this unchanged complete target and does not import general
renormalized flow finiteness as a bound for this selected bare
response. The purpose of the specialization is to retain the actual
relative box, complete force, residual and two probe forms.
