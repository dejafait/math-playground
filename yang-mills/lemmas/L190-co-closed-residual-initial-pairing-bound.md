# L190 — Cubic control of the co-closed residual part of the initial pairing

## Hypotheses

Use L183 and L189's fixed-mesh SU(2) expansion in (-4,4)^4,
admitted even N, a=8/N, straight lower-rooted direction-1 forest,
complete displacement and both actual L010 probes i=3,6 at tau=1/16.
The small-coupling expansion precedes refinement. Work in ordinary
dimensionless full-link coordinates, with fixed boundary links zero
and every variable normal end edge retained. Set

    Delta=L+DD^T, Sigma=Delta^-1, S=P Sigma P,
    z ~ N(0,S) independently in each of three colors,
    t(z)=2SAz, rho_H=script R_3(z)-d script S_3(z)[t(z)].

These are L183's exact full-link cubics, with both residual insertion
subtractions, before forest retraction. In particular rho_H is NOT
the original effective residual rho(pi Rz). Keep L183's exact W,
including both moving prefixes. Let I_(i,a,delta) be L189's complete
co-closed initial Duhamel integral, 0<delta<=tau/2, and put

    eta(delta)=delta ell(delta)^(1/2)
                   +sqrt(delta) ell(delta)^(1/4),
    ell(delta)=1+log(1+1/delta).

## Conclusion

There is a mesh-independent constant C such that

    ||script R_3(z)||_2 <= C N^3,
    ||script S_3(z)||_2 <= C N^2,
    ||rho_H(z)||_2 <= C N^3.                              (1)

Consequently, for both actual probes,

    a^3 |E[I_(i,a,delta) rho_H]| <= C_i eta(delta) -> 0   (2)

uniformly in sufficiently fine meshes. This removes the logarithmic
loss in L183(27) for the local cubics; it does not improve that lemma's
O(N^4) estimate for the forest effective residual.

The actual initial contribution remains exactly

    E[I_(i,a,delta) rho(pi Rz)]
       =E[I_(i,a,delta) rho_H]-E[dI_(i,a,delta)[W]].       (3)

There is no cubic bound or uniform initial-interval removal for the
second term here. No scaled limit, coefficient, full compensation,
finite matching, interacting reflected estimate, continuum theory
or mass gap follows. The final-time prefix-probe quartic/sextic group
and independent f_(i,2),r_0 contribution also remain unresolved.

## Proof

### 1. Covariance comparison for the actual cubic tensors

L155, proof section 2, proves that every local scalar cubic here is
alternating in color and contains each color once. The same property
for the action follows directly from L189(5)'s full plaquette word.
Thus, after collecting the color orders, each complete polynomial F
has a spatial coefficient array f with

    F(z)=sum_(e,f,g) f_(efg) z_e^1 z_f^2 z_g^3.

This uses the coefficient of that color-ordered monomial, with no
extra factorial; it is L183(22)'s convention before whitening. For
any positive semidefinite one-color covariance C, independence of
the three colors gives exactly

    E_C[F^2]=<f,(C tensor C tensor C)f>.                  (4)

It also shows there are no internal contractions. Equation (4) is
valid for singular C and for arbitrary signs of f. It is the direct
color specialization of the named Isserlis Gaussian pairing theorem.

Delta commutes with the orthogonal Hodge projection P, so
0<=S<=Sigma. Set K=Sigma-S>=0. The exact identity

    Sigma^tensor3-S^tensor3
       =K tensor Sigma tensor Sigma
          +S tensor K tensor Sigma+S tensor S tensor K

is a sum of positive semidefinite tensor products. Apply it to f
in (4) to obtain ||F||_(L2(S))<=||F||_(L2(Sigma)). This is a
comparison of polynomial norms only. It neither changes the law in
(3) nor makes a pointwise comparison between entries of S and Sigma.
In particular it is not an assertion of nonlinear gauge invariance
under replacing the forest or co-closed Gaussian.

### 2. The three-covariance product is summable on the complete box

Use L166, proof section 2, equation (11): for every two variable
same-component links e,f, including both normal end layers,

    |Sigma_(ef)| <= C[(1+dist(e,f))^-2+N^-2].            (5)

Different components of Sigma vanish. Distances are in lattice
units between midpoints. That proof uses the exact mixed relative
heat image formula and its full large-time spectral tail; the
constant own-direction modes and all physical faces are included.
No compact-observation restriction is needed for (5).

Write F as its sum of local stencil polynomials F_lambda. L149's
finite word formulas, applied to the cubic in L155(2), imply a
bounded stencil radius and boundedly many terms per placement. The
absolute coefficient sum per residual placement is at most C N:
the endpoint generator contributes 1/a, while the displacement,
strain coefficients and both insertion subtractions have bounded
coefficients. This is also the count recorded in L183 section 6.
For the full action, L189(5) gives a bounded coefficient sum per
plaquette. There are O(N^4) placements, with bounded multiplicity
at any lattice site, for either polynomial. No forest zeros are
imposed in these full-link words.

More generally suppose the coefficient sum per placement is at
most B_N. For placements with anchors at distance r, every link in
one stencil is within a fixed distance of its anchor. Equation (5)
and this bounded radius bound each of the three cross-color
covariances by C[(1+r)^-2+N^-2]. Expanding (4) therefore gives

    |E_Sigma[F_lambda F_mu]|
      <= C B_N^2 [(1+r)^-2+N^-2]^3
      <= C B_N^2 [(1+r)^-6+N^-6].                       (6)

The last inequality uses (x+y)^3<=4(x^3+y^3) for x,y>=0;
it retains every mixed term through this bound. A shell of anchor
radius m contains at most C(1+m)^3 placements. For each lambda,

    sum_mu [(1+dist(lambda,mu))^-6+N^-6]
      <= C sum_(m=0)^infinity (1+m)^-3+C N^4 N^-6
      <= C.                                             (7)

Thus E_Sigma[F^2]<=C B_N^2 N^4, even after absolute values of
every cross-placement term are taken. Equations (4)-(7) give
||F||_(L2(S))<=C B_N N^2. Taking B_N=C N for the residual and
B_N=C for the action proves the first two estimates of (1).
Deleting fixed rows only supplies zero entries, and never removes
a variable boundary row in this argument.

### 3. The signed tilt and the initial-interval consequence

On E=im P choose Z with ZZ^T=S and z^c=Z xi^c. L183 section 6
gives the real symmetric matrix M=2Z^T A Z, t^c=ZM xi^c, and
||M||<=C N from the whitened residual form bound. This bound makes
no smooth-input or positivity assumption about A or M. The
color-ordered coefficient tensor beta of script S_3(Z xi) has
||beta||=||script S_3||_2 by (4). Differentiating the polynomial in
the fixed direction t(z) applies M to each of its three slots. The
operator norm of their sum on the tensor space is at most 3||M||.
Equivalently, in M's common orthogonal eigenbasis it multiplies
beta_(abc) by mu_a+mu_b+mu_c, exactly as in L183(24). Therefore

    ||d script S_3(z)[t(z)]||_2
       <=3||M|| ||script S_3(z)||_2 <= C N^3.

The triangle inequality with the residual bound proves the last
estimate of (1). There is no commutation of A with S. L189(3)
and Gaussian Cauchy--Schwarz now prove (2), since a^3 N^3=8^3.
The bound concerns the whole interval including s<a^2 and retains
L189's complete external heat sums and all three action derivative
placements. No limit interchange or time cutoff is needed.

### 4. Locate precisely the remaining signed derivative term

L183(3) and its finite co-closed Gaussian integration by parts give
(3). For specificity write script S_3(y)=T(y,y,y), where T is its
full symmetric trilinear polarization on combined link/color space,
and E_(i,s)=H_(tau-s) Q_i H_tau. L189(1) is

    U_(i,a)(s,z)=-(6/a^2)T(H_s z,H_s z,E_(i,s)z).

Its exact directional derivative is

    dU(s,z)[W(z)]=-(6/a^2){
       T(H_s W,H_s z,E_(i,s)z)
       +T(H_s z,H_s W,E_(i,s)z)
       +T(H_s z,H_s z,E_(i,s)W)}.                        (8)

All three placements are retained, and W is the full quadratic
field in L183(4); no derivative of W enters a first directional
derivative. At fixed N these are finite polynomials with continuous
time-dependent coefficients, so dI[W] is their integral and
expectation can be interchanged with that finite-time integral.
The desired uniform cubic-scaled integral estimate for (8) remains
unproved. The proof of (7) cannot be applied to W: its two actual
prefixes are nonlocal, and the third-chaos tilt bound above concerns
the local action tensor, not the retracted action. Nor does the
linear-Gaussian norm estimate for U apply to the quadratic W slots.

Equations (1)-(2) isolate this remaining obstruction without
requiring separate limits for the two terms in (3). This result
does not establish a mesh limit even for the first term at fixed
delta; it supplies precisely its uniform small-interval bound.

## Mathlib

Full matching result and supporting tensor covariance, relative
Green and Gaussian-chaos statements: **not checked**. Unknown
availability is not evidence of absence. Isserlis' named Gaussian
pairing theorem is specialized explicitly in (4); tensor positivity,
the shell sum and the tilt estimate are justified above. The
boundary-sensitive kernel input is the canonical L166(11), not an
uninspected continuum estimate. The unchanged
[assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this bounded attempt on the joint response. This is local
progress by standard Gaussian and Green-kernel methods, classified
as REPRODUCTION, with no claim of progress beyond the checked sources.
