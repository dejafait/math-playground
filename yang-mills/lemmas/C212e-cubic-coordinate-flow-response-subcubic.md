# C212e — Remove the complete cubic coordinate-flow response at cubic scale

## Hypotheses

Use L212's SU(2) setting: relative box (-4,4)^4, admitted even
meshes a=8/N, straight lower-rooted direction-1 forest, complete
L008 displacement and both actual L010 probes i=3,6 at tau=1/16.
Take the bare expansion at fixed mesh before refinement. Coordinates,
transposes and norms are ordinary dimensionless full variable-link
coordinates, with three colors. Physically fixed links have zero
coordinates; retain every variable normal end edge and every physical
plaquette.

Use C212c's notation C=D_1, D=D_0, L=C^T C,
Delta=L+DD^T, P=I-D(D^TD)^(-1)D^T, S=P Delta^(-1)P,
H_s=exp(-s Delta/a^2), E_s=exp(-s L/a^2). Let z have three
independent colors with covariance S. Retain the actual symmetric
A=PAP, including both residual insertion subtractions, and put

    r(z)=sum_c (z^c)^T A z^c, v(z)=2SAz.

Let Q_3 be L011(10)'s entire homogeneous cubic term of the
exponential-coordinate Wilson-flow vector field specified by L010(3).
It includes all action and coordinate-metric contributions. Define

    Y_3(z)=integral_0^tau E_(tau-s) Q_3(H_s z) ds,
    P_(i,3flow)(z)=Dj_(i,2)(H_tau z)[Y_3(z)].        (1)

Here j_(i,2)(w)=sum_c (w^c)^T Q_i w^c is the actual unflowed
quadratic numerator, Q_i symmetric with Q_i D=0. Equation (1) is
the full Q_3 contribution to the co-closed quartic F_(i,4)(z) inside
L212's exact retraction. It is not the isolated summand evaluated
on the forest field Rz and does not include the nested DQ_2 z_2 term.

## Conclusion

For both actual probes,

    |Cov_S(P_(i,3flow),r)| <= C_i N^2,
    a^3 Cov_S(P_(i,3flow),r) -> 0.                  (2)

The bound includes the entire coordinate cubic, its initial and final
time endpoints, internal Gaussian pairs and all tilted placements.
Together with C212d it removes the entire Dj_(i,2)(z_1) z_3
contribution on the co-closed input at cubic scale. C212c's initial
square, C212b's endpoint limit, the other co-closed observable jets
and dF_(i,3)[b] remain unresolved. No complete quartic response bound
or limit, compensation, finer remainder, finite matching, interacting
reflected estimate <=c_box/2, continuum axioms or infrared finite mass
follows. This is local specialization of existing finite-coordinate,
heat and Gaussian estimates, without a claim beyond checked sources.

## Proof

### 1. Uniform locality of the complete coordinate cubic

We first verify the precise property of Q_3 needed in the estimate;
it is not enough to use only the radial action term. In the fixed
orthonormal Lie basis, put

    J(theta)xi = integral_0^1 exp(t ad(theta))xi dt.

Differentiating exp(theta) gives the left-trivialized velocity
(d exp_theta xi) exp(-theta)=J(theta)xi. Since J(0)=I,
J(theta)^(-1) is analytic in a fixed neighborhood of zero in this
three-dimensional Lie algebra. Define the full left-frame force

    F_e(theta)=sum_c (L_e^c script S)(exp(theta)) t^c.

L010(3) therefore gives the exact coordinate flow near identity,

    Q_e(theta)=-a^(-2) J(theta_e)^(-1) F_e(theta).   (3)

The force at e is the sum of derivatives of the plaquettes containing
e. There are at most 2(4-1)=6 such plaquettes. Each derivative is a
matrix word in their four oriented links exp(plus or minus theta_f),
with fixed matrices and the fixed action factor 4. Thus it is analytic
in a bounded number of local three-component coordinates. Boundary
plaquettes merely set some of those coordinates to zero. No derivative
in (3), apart from its displayed a^-2, introduces a mesh factor.

For completeness, if J^-1=I+J_1+J_2+... and
F_e=F_(e,1)+F_(e,2)+F_(e,3)+..., the complete cubic coefficient is

    a^2 Q_(3,e)=-F_(e,3)-J_1(theta_e)F_(e,2)
                              -J_2(theta_e)F_(e,1). (4)

There is no force constant term because flat links minimize each
plaquette action. Formula (4) keeps every coordinate contribution,
regardless of cancellations between its displayed pieces. It follows
directly by multiplying the finite Taylor series in (3); no left-frame
cubic is substituted for a coordinate cubic.

Let alpha label an output edge and color. The symmetric cubic
polarization T_alpha of a^2 Q_(3,alpha) consequently has a representation

    a^2 Q_(3,alpha)(y)=T_alpha(y,y,y)
             =sum_(beta,gamma,eta) t_(alpha;beta gamma eta)
                                      y_beta y_gamma y_eta,
    sum_(beta,gamma,eta)|t_(alpha;beta gamma eta)|<=C. (5)

Its source indices lie in the union of plaquettes incident to the
output link. The constant is uniform: there are finitely many oriented
word patterns, colors and choices of fixed entries; each has finite
Taylor coefficients in (3). Symmetrization averages at most six
permutations and preserves a uniform coefficient bound. The number
of output indices, including normal end edges and colors, is at most
C a^-4. These facts justify (5) without computing or dropping any
particular cubic coefficient. This is the needed specialization of
the finite analytic flow, not a reproof of flow renormalizability.

### 2. Contract the external probe leg before estimating Q_3

Write y_s=H_s z and

    h_s=H_(tau-s) Q_i H_tau z.

Since Q_i D=0 and Q_i is symmetric, Q_i H_tau z is co-closed.
E_t and H_t agree on this subspace. By self-adjointness of E_t,
(1) is therefore exactly

    P_(i,3flow)(z)
       =2 a^-2 integral_0^tau sum_alpha
                    (h_s)_alpha T_alpha(y_s,y_s,y_s) ds. (6)

Only the contracted external leg has been made co-closed here.
No such assertion about Q_3(y_s) or Y_3 is used; their gradient
components have not been evolved by a substituted H_t.

C212c(7), proved with the complete relative spectrum, gives for
every fixed p>=2

    sup_beta ||(y_s)_beta||_Lp <= C_p a/(s+a^2)^(1/2).

L193(5)--(7), with its auxiliary r=0, supplies for these exact
two compact smooth probe stencils

    sup_alpha ||(h_s)_alpha||_Lp <= C_(i,p) a^3.     (7)

Both bounds hold uniformly on 0<=s<=tau. In particular the second
bound at s=tau uses L193's full output-mode decay from the smooth
compact probe coefficients, not a positive remaining output heat time.
The first retains the normal end rows and constant own-direction
mode; it includes s<a^2. All external and internal modes remain.

C212c(8) gives the genuine covariance comparison

    Cov(v)=4SASAS<=C N^2 S.                         (8)

Applying any deterministic row functional to (8), then the ordinary
Gaussian moment formula, proves (7) for the corresponding replacements
y_s(v)=H_s v and h_s(v)=H_(tau-s) Q_i H_tau v with an extra factor
C_p N. Correlations between all these fields are retained. This
does not assign positivity to the signed 2SAS or smoothness to v.

Using Holder with four L4 factors in (5)--(7) and summing the full
O(a^-4) output count proves

    2a^-2 E|sum_alpha (h_s)_alpha T_alpha(y_s,y_s,y_s)|
        <= C_i a^-2 a^-4 a^3 [a/(s+a^2)^(1/2)]^3
        = C_i (s+a^2)^(-3/2).                       (9)

The inequality uses absolute moments of the complete polynomial,
so internal Wick pairings need not vanish and are all covered.

### 3. Keep all four tilt placements and integrate both endpoints

At fixed mesh the polynomial directional derivative of (6) is

    dP_(i,3flow)(z)[v(z)]
      =2a^-2 integral_0^tau sum_alpha {
         (h_s(v))_alpha T_alpha(y_s,y_s,y_s)
       +3(h_s)_alpha T_alpha(y_s,y_s,y_s(v)) } ds.  (10)

Symmetric polarization in (5) accounts for all three cubic inputs.
The fourth placement differentiates the external probe leg. The
direction is evaluated at z but is not itself differentiated in a
first directional derivative. Equations (7)--(9) show that the
absolute expectation of (10)'s integrand is at most
C_i N(s+a^2)^(-3/2).

The complete endpoint integral is explicit:

    integral_0^tau (s+a^2)^(-3/2) ds
        =2[a^-1-(tau+a^2)^(-1/2)] <= 2a^-1.         (11)

Thus no initial interval is dropped, and no mesh/time interchange
or uniform integrability at zero is assumed. At each fixed mesh all
polynomial moments and time integrals are finite, so differentiation
and integration in (10) are legitimate. We obtain

    E|dP_(i,3flow)[v]| <= C_i N a^-1.               (12)

Apply L212(12)'s normalized Gaussian tilt identity (equivalently
its conclusion (5)), valid also on the singular ambient covariance:

    Cov_S(P_(i,3flow),r)=(1/2)E[dP_(i,3flow)[v]].   (13)

The factor 1/2 is retained; the factor 2 in (6) came only from
Dj_(i,2). Both residual subtractions remain inside A throughout.
Since a=8/N, (12)--(13) give O(N^2), and their a^3-scaled upper
bound is O(1/N), proving (2). This bounds a signed response, not
just its probe polynomial, and supplies no limit for the other
quartic terms.

The verification is analytic: the exact local coordinate formula
(3)--(5), all four differentiated placements, the mesh-power count
(9) and the full endpoint integral (11). No numerical test or
finite-mode preview is used. L212 retains the forest corrections
separately in its exact joint identity. Accordingly L022's obstruction
to isolated forest-to-Hodge transfer is not invoked as a valid transfer.

## Mathlib

Full matching result: **not checked**. Supporting coverage of the
finite Lie-group exponential differential, Gaussian moments and
integration by parts, relative heat estimates and Holder's inequality:
**not checked**; unknown coverage is not evidence of absence. The
standard local exponential differential is written explicitly in (3),
and its needed cubic specialization is justified above. The reused
[assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
does not import renormalized-flow finiteness as a bound on this selected
bare response. Existing heat and tilt results are used with their
unchanged hypotheses; no general flow theorem is reproved.
