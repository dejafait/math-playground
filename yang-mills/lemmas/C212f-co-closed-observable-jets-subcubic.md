# C212f — Remove the remaining co-closed observable jets at cubic scale

## Hypotheses

Use L212's fixed-mesh bare SU(2) expansion in the relative box
(-4,4)^4, admitted even N, a=8/N, straight lower-rooted direction-1
forest, complete L008 displacement and both actual L010 probes
i=3,6 at tau=1/16. All coordinates and norms below are ordinary
dimensionless full variable-link coordinates, including three colors
and every normal end edge. Fixed boundary links have zero coordinates.
The coefficients j_(i,m) are those of the unflowed g-independent
numerators in L011(1),(12), not coefficients of a changed probe.

Use C212c's notation C=D_1, D=D_0, L=C^T C,
Delta=L+DD^T, P=I-D(D^TD)^(-1)D^T, S=P Delta^(-1)P,
H_s=exp(-s Delta/a^2), E_s=exp(-s L/a^2).
Let z have three independent colors with covariance S and retain
the actual symmetric A=PAP, with both residual insertion subtractions.
Set

    r(z)=sum_c (z^c)^T A z^c, v(z)=2SAz,
    y=H_tau z,
    Z=integral_0^tau E_(tau-s) Q_2(H_s z) ds,
    P_(i,obs3)(z)=Dj_(i,3)(y)[Z],
    P_(i,obs4)(z)=j_(i,4)(y).                       (1)

Here Q_2 is the full coordinate quadratic Wilson-flow field from
L011, as used in C212d. These are the last two summands of the
co-closed F_(i,4)(z) in L212. They are not isolated forest-input
summands transferred by a linear gauge-quotient argument.

## Conclusion

For both actual probes,

    |Cov_S(P_(i,obs3),r)|<=C_i N^2,
    |Cov_S(P_(i,obs4),r)|<=C_i N.                   (2)

Both a^3-scaled responses tend to zero. Together with C212d,e,
this gives the quantitative reduction of the complete co-closed part

    Cov_S(F_(i,4)(z),r)
       =Cov_S(j_(i,2)(Z),r)+O_i(N^2 log(eN)).       (3)

In particular that co-closed response is O(N^3), by C212c. For
every fixed 0<delta<=tau/2 it may also be replaced in (3) by
Cov_S(j_(i,2)(Z_delta),r), with O_(i,delta)(N^2 log(eN)) error,
where Z_delta is C212c(1)'s initial-time integral.

The retained initial/initial square has no proved scaled limit.
L212's dF_(i,3)[b] and C212b's cubic endpoint remain outside (3).
Thus this does not bound the complete forest quartic response,
establish its limit or compensation, or give finer asymptotics,
finite matching, an interacting reflected error <=c_box/2,
continuum axioms or infrared finite mass. This is local reproduction
and specialization of existing estimates; no progress beyond checked
sources or originality is asserted.

## Proof

### 1. Keep the actual numerator coefficients and their local structure

L193, proof section 4, proves for both actual j_(i,3) that their
complete local expression is a sum of terms consisting of one
linear circulation and two link coordinates, with uniformly bounded
coefficients and bounded local incidence multiplicities. This uses
the plaquette-trace cubic for the triplet and both linear/quadratic
clover orders for the shear. We apply exactly that result: do not
replace the average of plaquette traces by a clover square.

More explicitly, collecting the fixed finite color contractions and
local shifts, one may write

    j_(i,3)(w)=sum_rho c_rho (Cw)_(p_rho)
                                     w_(e_rho) w_(f_rho), (4)

with |c_rho|<=C_i, O(a^-4) terms and a uniformly bounded number
of appearances of each selected edge or plaquette row in each slot.
Colors are included in these row indices. Strains and their transition
regions stay in c_rho. The same statements hold on all retained rows;
fixed coordinates are simply zero. Equation (4) is a finite polynomial
representation, not a positivity assertion or a curvature-only
representation of the nonlinear probe.

The complete quartic also has a local representation

    j_(i,4)(w)=sum_rho d_rho
              w_(e_rho,1) w_(e_rho,2) w_(e_rho,3) w_(e_rho,4),
    |d_rho|<=C_i, number of terms<=C_i a^-4.         (5)

Here no retained-circulation claim is needed. To check the coefficient
normalization in (5), L010(2) gives the numerators as 8 times weighted
plaquette traces and -2 times weighted traces of two clovers. L009(1)
defines each clover as 1/8 times a sum of four anti-Hermitian traceless
four-link words: it contains no inverse power of a. Substitute
U_e=exp(w_e^c t^c) and take degree four. Each word has bounded length,
each matrix exponential has fixed Taylor coefficients through this
degree, and the three fixed Lie basis matrices have fixed norm.
There are finitely many word, color and fixed-zero patterns, so the
sum of absolute degree-four coefficients per site is uniformly bounded.
L010's strain weights are uniformly bounded by the fixed smooth
displacement. All faces have bounded incidence count. Thus (5)
contains every degree-four term with no hidden a^-2 or a^-4 factor.
This is only a coefficient bound for the specified finite numerator,
not a reproof or use of renormalized-flow finiteness.

### 2. Use full-spectrum heat and quadratic-jet bounds

Let dot y=H_tau v and dot Z=dZ(z)[v(z)]. C212c(7)--(8) at
the fixed positive time tau gives, for every fixed finite p>=2,

    sup_e ||y_e||_Lp<=C_p a,
    sup_p' ||(Cy)_p'||_Lp<=C_p a^2.                (6)

The corresponding dot y and C dot y bounds have one additional
factor N. The input is the genuine covariance inequality
Cov(v)=4SASAS<=C N^2 S, not positivity of the signed tilt 2SAS.
All relative modes, including the constant own-direction mode and
all normal end rows, are included in (6).

C212d(4), with ||X||_(p,2)=(E||X||_ell2^p)^(1/p), gives

    ||Z||_(2,2)<=C a^-2,
    ||CZ||_(2,2)<=C a^-1,
    ||dot Z||_(2,2)<=C N a^-2,
    ||C dot Z||_(2,2)<=C N a^-1.                  (7)

The fixed tau was absorbed into the constants. C212d's proof
sections 1--2 retains both differentiated quadratic inputs and the
entire E_(tau-s), including its undamped gradient part. Its complete
time convolutions include s=0 and s=tau. In particular (7) is not
obtained by replacing E_t by H_t on a nonlinear output or by using
a strictly positive lower bound on remaining flow time.

Bounded multiplicity and Cauchy--Schwarz give, for any vector X
of random coordinates and any selected slot of (4),

    sum_rho ||X_(j_rho)||_L2
       <=C_i a^-2 (sum_j E|X_j|^2)^(1/2)
       =C_i a^-2 ||X||_(2,2).                     (8)

Indeed the first factor is the square root of the O(a^-4)
term count, and the sum of squared selected norms is bounded by
the slot's incidence multiplicity times the full sum. No spatial
independence is used.

### 3. Differentiate every observable and flow slot

Differentiate (4) in the full direction Z. The exact terms are

    P_(i,obs3)=sum_rho c_rho {
        (CZ)_(p_rho) y_(e_rho) y_(f_rho)
       +(Cy)_(p_rho) Z_(e_rho) y_(f_rho)
       +(Cy)_(p_rho) y_(e_rho) Z_(f_rho) }.         (9)

For each product use Holder with the two linear factors in L4
and the quadratic factor in L2. Equations (6)--(8) give

    E|P_(i,obs3)|
      <=C_i a^-2 [a^2 ||CZ||_(2,2)+a^3 ||Z||_(2,2)]
      <=C_i a^-1.                                 (10)

Now differentiate (9) in direction v(z). In its first line the
three replacements are CZ by C dot Z and either y by dot y.
In each of its other lines they are Cy by C dot y, Z by dot Z
and the other y by dot y. These nine displayed product-rule terms
include both inner quadratic-flow placements inside dot Z. They
therefore cover all four underlying Gaussian inputs, including
the two inputs of Z; none is held fixed. Every replacement costs
at most C N in the same Holder and incidence estimate, by (6)--(7).
Consequently

    E|dP_(i,obs3)(z)[v(z)]|<=C_i N a^-1.           (11)

This argument keeps all correlations and all internal Wick pairs.
Directional differentiation is evaluated at v(z); a first derivative
does not additionally differentiate its direction v.

For (5), four L4 factors and (6) give O(a^4) per monomial, hence
E|P_(i,obs4)|<=C_i. Its derivative is exactly the sum of four
terms replacing one y by dot y. Each has expectation bounded by
C_i N a^4 per monomial, so

    E|dP_(i,obs4)(z)[v(z)]|<=C_i N.                (12)

All color contractions and both shear clover orders have already
been included in (4)--(5); there is no additional outside color or
response factor to insert in (11)--(12).

### 4. Contract the actual signed response and assemble the co-closed part

L212, proof (12), gives for either quartic polynomial P

    Cov_S(P,r)=(1/2)E_S[dP(z)[v(z)]].              (13)

It includes the covariance subtraction, so neither P nor r needs
zero expectation, and holds also for the singular ambient S.
Apply it to (11)--(12), retaining its factor 1/2. Since a=8/N,
this proves (2), with scaled bounds O(N^-1) and O(N^-2).
Both residual insertion subtractions remain in A throughout;
no smoothness has been assigned to the rough direction v.

L011(11)--(12) splits the full co-closed F_(i,4) into j_(i,2)(Z),
the nested quadratic-flow term of C212d, the complete cubic
coordinate-flow term of C212e, and the two polynomials (1).
C212d bounds its response by O(N^2 log(eN)), and C212e by O(N^2).
Adding the four established errors proves (3). C212c(2) supplies
the cubic bound; its (3) supplies the fixed-delta initial-square
replacement, including both cross rectangles.

These are finite-mesh inequalities before any mesh limit. The
full time integrations have already been bounded in C212d; no
new time/mesh interchange or uniform removal as delta decreases
is used. L212 keeps the correlated gauge prefixes and their upper
jumps in its other terms. Those terms have not been omitted from
the complete target or subjected to an isolated forest-to-Hodge
transfer. Verification here is analytic: the local coefficient
normalization, all differentiated placements, and (10)--(13)'s
complete power counts. No numerical test or truncated heat sum
is used as evidence for these inequalities.

## Mathlib

Full matching result: **not checked**. Supporting coverage of
finite polynomial differentiation, Holder and Cauchy--Schwarz,
Gaussian moments and integration by parts, and relative heat
estimates: **not checked**. Unknown coverage is not absence.
The reused [assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
distinguishes the selected bare cumulant from full renormalized-flow
theorems. The canonical local estimates cited above retain their
original hypotheses; only their needed actual-numerator specialization
and finite derivative estimates are proved here.
