# Lemma 421: prescribed-response moments permit a vanishing capped cubic

## Hypotheses

Use L417/L418's actual response graph at every t in [H,2H], with
height marginal dt/H, ell=log H, and the exact conversion of L414.
The selected constraints are precisely L416's inherited list, including
the first Bcal tolerance from L415, all six raw critical second moments,
the signed cubic, all 23 quartic coefficients and the absolute and
qualitative pointwise bounds. Their constants may be fixed once on an
eventual real-H ray. No conditional critical moments, consistency of
the laws at different H, or realization by a single global critical
function is imposed. The response and its derivatives are never changed.

Write X0(t) for the actual critical triple, rho0=|X0|, and use the
exact polynomials B(X;t)=Bcal and D(X;t)=Delta. Thus D is normalized
Delta, not the unnormalized physical discriminant. In particular L405's
positive constant kappa_* and L409's positive constant beta_* are fixed
at their actual values; no constants in the selected list are fitted.
Use L418's E rho0^4=O(ell^4) and actual quartic limits, and L419's
bounded response matrices, negative trace, bounded weight g0, and
measurable six-state covariance construction. E denotes dt/H average;
E_nu additionally integrates a conditional critical-state kernel.

## Conclusion

For every sufficiently large real H there is a measurable probability
kernel nu_(H,t) satisfying the complete selected list with this exact
height/response marginal, one set of pointwise constants and one onset.
It additionally avoids {D>0,B<0}. For this same family, for every fixed
lambda>0,

    F_lambda^nu(H)
      :=E_nu[|DB| min(1,|X|/(lambda ell^2))]
       =O(ell)+O_lambda(ell^(3/2))+O_lambda(1)=o(ell^2).    (1)

The family does not depend on lambda. It has exactly

    E_nu XX^T=ell K, E_nu B=-b0,
    K=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]],
    b0=zeta(3)/(4pi),

and E_nu D=-a_* ell+o(ell), E_nu DB=beta_* ell^2+O(ell).
All 23 quartic leading coefficients, including kappa_*>0, are retained.
Both absolute third-power envelopes improve to O(ell^2).

Consequently the selected moment constraints, even with the prescribed
actual response and uniform height marginal, do not force the proposed
positive capped liminf. This is a counterlaw to that implication, not
a counterexample to the actual capped statistic, to RH, or to any
statement using additional actual critical-function structure. L418's
actual F_lambda remains unevaluated. The separate step-163 critical
audit below validates this selected-relaxation construction; no global
realization or regulator margin is claimed. The original classification
POTENTIALLY_NEW means only that the prior source comparison
did not supply this particular construction, not certified originality.

## Proof

The prior EXPLORE assessment is
`drafts/literature/2026-10-16-signed-quartic-capped-cubic-lower-bound.md`.
It permits a full prescribed-response counterlaw, rather than only a
scalar toy example. We reuse the actual moment inputs as imported in
L418 and the independently audited L419 construction; we do not reprove
a zeta moment theorem or invoke moment strong duality. L410/L414/L416's
different-response examples do not imply this conclusion. L420's
magnitude upper-certificate stop is a contrast, not an input.

### Exact forms and a uniformly positive cubic direction

Put e(t)=q(t)/L(t)^2. The exact conversion gives

    ell_F(X;t)=y^2-xz-e x^2,
    C(t)=v_1^2-v_0 v_2-e v_0^2,
    b(t)=(-v_2-2e v_0,2v_1,-v_0),
    B=b^T X, D=X^T J X=B^2-4 C ell_F.

L419 proves C>=Cmin>0, |b|>=bmin>0, bounded J,b and conversion
coefficients, and tr(JK)<=-delta0<0 uniformly on an eventual ray.
It also gives b=c(a/4,-h,-a)+O(1/L), c=1/(4pi), with
a^2+h^2>=zeta(5/2)^(-2) and e=o(1). All exact coefficients remain
in the definitions above; this approximation is used only for a
uniform lower bound on two candidate projections.

Consider the unit vectors n_+=(2/3,1/3,2/3) and
n_-=(2/3,-1/3,2/3). Both have

    ell_F(n_+;t)=ell_F(n_-;t)=-1/3-4e/9<=-1/4

eventually. Also B(n_+;t)=c(-a/2-h/3)+O(1/L) and
B(n_-;t)=c(-a/2+h/3)+O(1/L). Since

    max(|A+B|,|A-B|)>=sqrt(A^2+B^2),

their maximum absolute projection is at least
c sqrt(a^2+h^2)/3-O(1/L), hence at least a fixed b1>0
after one onset. Choose the one with larger absolute exact B value,
breaking ties in favor of n_+, and reverse its sign if needed to make
B positive. This defines a Borel unit vector n(t). Then

    B(n;t)>=b1, D(n;t)>=Cmin,
    h(t):=D(n;t)B(n;t) lies in [hmin,hmax],             (2)

for fixed positive hmin,hmax. The reversal leaves ell_F and D unchanged.
There is no response-zero division or independence assumption here.

### High component preserves every actual quartic

Set R_hi=ell^3 and, where rho0>0, define

    r(t)=max(R_hi,2^(1/4) rho0(t)),
    p(t)=(rho0(t)/r(t))^4,
    Y(t)=s(t) r(t) X0(t)/rho0(t),

where s=1 if D(X0;t)B(X0;t)>=0 and s=-1 otherwise.
At rho0=0 put p=0,Y=0. This gives 0<=p<=1/2 in every fiber.
Exactly as a homogeneity identity, for every degree-four homogeneous
critical polynomial Q4 at this same response,

    p Q4(Y;t)=Q4(X0;t).                                (3)

This includes each of D^2, DB^2, the six diagonal and fifteen
off-diagonal D omega_i omega_j, and |X|^4. Their signed values,
curvature and response derivatives are all retained. The high states
avoid {D>0,B<0}: if input D>0, s makes output B nonnegative;
otherwise output D is nonpositive. Their cubic is nonnegative.

Using |D(X;t)|<=C|X|^2, |B(X;t)|<=C|X| and
E rho0^4=O(ell^4), the unnormalized high integrals satisfy

    E p=O(ell^-8),
    tr Q_hi=E[p|Y|^2]=E[rho0^4/r^2]=O(ell^-2),
    |E[pD(Y)]|=O(ell^-2), |E[pB(Y)]|=O(ell^-5),
    0<=E[pD(Y)B(Y)]<=C E[rho0^4/r]=O(ell),
    E[p|Y|^3]=O(ell), E[p|B(Y)|^3]=O(ell).             (4)

These identities include both branches of r and the zero convention.
No bound on the maximum of the actual jets is substituted for their
fourth moment, and no rare integral is divided by its probability.

### Intermediate component supplies the signed cubic below the cap

Put R_mid=ell^(3/2), Z_mid(t)=R_mid n(t), and assign probability

    k(t)=beta_* ell^2/(R_mid^3 h(t)).                    (5)

By (2), k=O(ell^-5/2) uniformly, so k<=1/4 eventually. Its
conditional cubic contribution is exactly beta_* ell^2 at every t.
Both D and B are strictly positive on these states. Uniformly bounded
coefficients and |n|=1 give the following unnormalized bounds:

    E k=O(ell^-5/2), tr Q_mid=O(ell^1/2),
    |E[kD(Z_mid)]|=O(ell^1/2), |E[kB(Z_mid)]|=O(ell^-1),
    E[k|Z_mid|^3]+E[k|B(Z_mid)|^3]=O(ell^2),
    E[k|Z_mid|^4]=O(ell^7/2).                          (6)

Every selected quartic has absolute value <=C|X|^4, so each added
quartic is o(ell^4), including entries whose required coefficient is
zero. This is why the cubic calibration does not alter (3)'s leading
coefficients. This component is not claimed to preserve the quartics
pointwise or to be the actual critical jet.

### Full second-matrix correction and the negative bulk

Let Q=Q_hi+Q_mid be the integrated second matrix of the two components,
J_R their combined first B integral, and D_R their first D integral.
Equations (4)--(6) give

    Q positive semidefinite, ||Q||=O(ell^1/2),
    J_R=O(ell^-1), D_R=O(ell^1/2).

The remaining fiber mass is w(t)=1-p(t)-k(t)>=1/4 and <=1.
Its average W_H=Ew=1-O(ell^-5/2). Use the fixed bounded positive
function g0(t) constructed in L419, with

    E g0=1+O(H^-1), E[g0 tr(JK)]=-a_*+o(1).

These properties are independent of any rare kernel: L419 proves them
from its fixed right-line modulus weight and the complete gamma
harmonic. Define N_H=E(wg0), g_H=g0/N_H. Then
N_H=1+O(H^-1+ell^-5/2), g_H is uniformly bounded above and below,
E(wg_H)=1, and

    E[w g_H tr(JK)]=-a_*+o(1).                        (7)

Indeed replacing g0 by wg_H against any bounded response expression
costs O(H^-1+ell^-5/2); this uses only E(1-w), not a pointwise
smallness assumption for p.

Set

    d_H=(-b0-J_R)/W_H, m(t)=d_H b(t)/|b(t)|^2,
    A_H=-(Q+E[w m m^T])/W_H,
    Sigma(t)=ell g_H(t)K+A_H.                         (8)

The mean m is uniformly bounded and b^T m=d_H exactly. The symmetric
matrix A_H is constant in t and has norm O(ell^1/2)=o(ell).
Unlike L419's two-entry correction, it cancels the entire rare second
matrix. Positive definiteness of K, the bounds on g_H, boundedness of
J and tr(JK)<=-delta0 imply uniformly

    c1 ell I<=Sigma<=c2 ell I,
    tr(J Sigma)<=-delta1 ell                         (9)

eventually, with fixed positive constants. In particular subtracting
Q has not destroyed positive definiteness or the cone margin.

Apply L419's explicit Borel six-state construction to Sigma,J,m:
with S=Sigma^(1/2), choose its Borel orthonormal u_i such that
u_i^T SJS u_i=tr(J Sigma)/3 and give each
m+sqrt(3)S u_i and m-sqrt(3)S u_i probability 1/6.
The imported matrix existence input is the real Schur--Horn theorem,
as stated in E. A. Carlen and E. H. Lieb, *Short proofs of theorems of
Horn and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), pp. 1--2,
Horn's theorem after (1.1). The trace-average diagonal is majorized
by the eigenvalues. The needed Borel implementation is already proved
in L419 and is reused, not inferred from the citation alone.

Call the resulting conditional probability law mu_t. It has mean m,
centered covariance Sigma, centered symmetry, and |X|=O(sqrt(ell)).
Every centered state's D equals tr(J Sigma)<=-delta1 ell;
translation by bounded m adds O(sqrt(ell))+O(1). Thus all its
states have exact D<0 eventually. This use of L419 only requires the
properties (9) and bounded m, not its former O(1) covariance correction.

Define the full conditional law by

    nu_(H,t)=p(t) delta_Y(t)+k(t) delta_Z_mid(t)+w(t) mu_t.

Its nonnegative masses sum to one at each height, giving exactly dt/H
as height marginal. All components use the actual response at that t.

### Simultaneous verification of the selected moments

By (8), the full second matrix is exactly

    Q+E[w(Sigma+mm^T)]
       =Q+ell K+W_H A_H+E[wmm^T]=ell K.             (10)

Thus the four allowed O(1) errors are zero, and both much smaller odd
tolerances are met exactly. Also E_nu B=J_R+W_H d_H=-b0 exactly,
so the full L415 first-B error tolerance is met. For the first D,
boundedness of J,m, (7), (8) and D_R=O(sqrt(ell)) give

    E_nu D=D_R+ell E[w g_H tr(JK)]
                 +E[w(tr(J A_H)+m^T Jm)]
           =-a_* ell+o(ell).                          (11)

No unspecified stronger constant-term tolerance is imposed on (11).
For the bulk cubic, centered symmetry gives the exact identity

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                  +(m^T Jm)(b^T m)=O(ell).

Together with (4),(5) this proves E_nu DB=beta_* ell^2+O(ell).
There is no reliance on canceling two unbounded cubic error terms.

For each of the 23 quartics, the high contribution equals its actual
integral by (3); the intermediate absolute addition is O(ell^7/2)
and the bulk addition O(ell^2). Therefore each required leading
coefficient survives, including the signed off-diagonal coefficients
and L405's positive kappa_*. This invokes the actual limits already
recorded in L418 without introducing a limiting joint law. Likewise
E_nu |X|^4=O(ell^4). The two absolute third-power integrals are
O(ell)+O(ell^2)+O(ell^3/2)=O(ell^2), which satisfy the required
O(ell^9/4) envelopes. All support satisfies {D<=0 or B>=0}.

### Fixed pointwise constants and the capped observable

The response annulus, derivative bounds and Ccal lower bound are
unchanged actual quantities. Exact curvature and all alpha terms
remain in the conversion. On the high branch r=2^(1/4)rho0 the
critical physical jets are s2^(1/4) times the actual ones, hence
meet their qualitative bounds with one fixed enlargement. On the
other branch |Y|=ell^3 and bounded conversion gives |P_j|<=C ell^3.
The intermediate and bulk have smaller powers of ell. For j<=2,

    sup_(H<=t<=2H) ell^3 L(t)^j/T(t)^(1/2) -> 0.

Consequently one set of E_j works on every component after one onset.
No constants grow with H. All functions and branch rules are Borel;
at a fixed H the actual jets are bounded on the compact interval,
so all states and all listed signed integrands are bounded. Every
estimate holds for all sufficiently large real H, not a subsequence.

Finally evaluate the same radial payoff as L418 on this law. On the
high component, its cap factor is at most one, so (4) bounds its
nonnegative contribution by O(ell). On the intermediate component,
R_mid/(lambda ell^2)=lambda^-1 ell^-1/2<1 eventually for each
fixed lambda. Equations (2),(5) therefore give its exact contribution
beta_* lambda^-1 ell^3/2. On the bulk, |X|=O(sqrt(ell)) is also
below the cap eventually. Its payoff is bounded by

    C |X|^4/(lambda ell^2),

whose integral is O_lambda(1). These bounds handle all high-component
branches without assuming the original actual rho0 is below a cap.
They prove (1). Each component is nonnegative in this absolute
payoff, so no signed cancellation is used to obtain its vanishing limit.

The positive signed quartic is thus carried by amplitudes above the
fixed cap, while a distinct smaller amplitude supplies the signed
cubic at negligible quartic scale. This verifies a full counterlaw
in the selected relaxation. It asserts neither that the actual critical
function has this distribution nor that its own F_lambda vanishes.
The actual capped equality, clipping, regulator margin and global
mixed positivity remain unresolved.

### Separate critical audit — 2026-10-16, step 163

This RESEARCH / REPRODUCTION / proof_audit uses the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-16-prescribed-response-two-scale-counterlaw-audit.md`.
The conclusion passes in precisely its stated integrated-moment scope.
This is verification of the existing construction, not a new zeta
moment, originality claim, actual capped evaluation or global realization.
The following checks include the larger covariance correction; the
original bounded-correction conclusion of L419 is not applied to it.

**Inputs and exact tolerances.** L414 (1), L415 (1), and L416 (1)
require the 23 quartic leading coefficients with errors o(ell^4), the
cubic beta_* ell^2+o(ell^2), first D=-a_* ell+o(ell), and first
B=-b0+O(ell^-1+H^-1/2 ell^2). Four even raw second entries allow
O(1) errors; xy and yz allow respectively only O(H^-2/3 ell^-1)
and O(H^-2/3 ell^-3). They impose no critical-coordinate first means
or response-conditioned second moments. The qualitative bounds permit
one fixed enlargement of their constants. L417 fixes the actual response,
ordinary-derivative conventions and dt/H marginal, not a single critical
function realizing the kernels across heights or different H intervals.

The actual quartic inputs and E rho0^4=O(ell^4) are imported through
audited L418; the exact positive constants are L405 (1) and L409 (1).
The inherited second-moment normalization is L416's application of
Bui--Hall, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/pdf/2304.05178v1#page=1),
Introduction equation (1) and its preceding odd-order display.
The actual fourth-power bounds use that paper's Theorem 3 and
Proposition 3, as recorded in L418's audit. No source theorem is applied
to output states: their moments are checked below. In particular, their
absolute third envelopes follow directly from this construction and do
not require a new application of Curran--Heycock to a model law.
All source hypotheses and fixed constants remain those covered in the
step-162 assessment; no new shift, twist or conditional-moment theorem
is introduced or reproved.

**Exact support and positive direction.** Expanding the P,V conversion
cancels alpha and gives, with e=q/L^2,

    Fmat=[[-e,0,-1/2],[0,1,0],[-1/2,0,0]],
    ell_F=X^T Fmat X, b=(-v_2-2e v_0,2v_1,-v_0),
    C=v_1^2-v_0 v_2-e v_0^2, J=b b^T-4C Fmat.

These are exact identities, including at zeros. The two candidate unit
vectors have ell_F=-1/3-4e/9. For |e|<=3/16 this is at most -1/4.
Their leading B values are c(-a/2-h/3) and c(-a/2+h/3).
The maximum of their absolute values is at least
c sqrt(a^2/4+h^2/9), hence at least c/(3 zeta(5/2)).
The uniform O(1/L) errors leave a fixed positive lower bound b1.
Choosing the larger exact absolute projection and reversing its sign
makes B(n)>=b1. Then D(n)=B(n)^2-4C ell_F(n)>=Cmin>0.
Bounded J and b give a fixed upper bound too, so h=D(n)B(n)
lies between fixed positive constants. Finite comparisons, ties and
sign choices are Borel; neither a vanishing projection nor rho0 is
used as a denominator in this direction construction.

**Both high branches and all quartics.** If r=ell^3, its defining
inequality gives rho0<=2^(-1/4)ell^3, so p<=1/2. If
r=2^(1/4)rho0, then p=1/2 and Y=s2^(1/4)X0. The branches
agree at equality. At rho0=0, p=Y=0 and every homogeneous observable
in question vanishes. For rho0>0, p Q4(Y)=Q4(X0) follows from
s^4=1, regardless of the sign of Q4. Thus it holds for D^2, DB^2,
all six diagonal and fifteen off-diagonal D omega_i omega_j, and
U^2. No entry of the matrix, including a zero or negative leading
coefficient, is dropped. The support rule follows from D(Y) having
the sign of D(X0) and B(Y)=s(r/rho0)B(X0).

For j=0,1,2,3 the uniform bound r>=ell^3 gives

    E[p|Y|^j]=E[rho0^4/r^(4-j)]=O(ell^(3j-8)),

with the zero-state convention for j=0. The four bounds are
O(ell^-8), O(ell^-5), O(ell^-2), O(ell), respectively.
They are unnormalized integrals over the high component. Bounded
coefficients imply the corresponding first B, first D and absolute
cubic bounds in (4). Orientation makes its signed DB nonnegative.
This argument controls the large-rho0 branch without assuming it is
empty or uniformly rare in each fiber. Its integrated mass is small
even though p can equal 1/2 at some heights.

**Intermediate mass and costs.** Since beta_* is fixed and positive,
k=beta_* ell^(-5/2)/h is nonnegative and uniformly O(ell^-5/2).
After one onset it is at most 1/4. Consequently w=1-p-k>=1/4
at every height, not only on average. The exact contribution of
k delta_(ell^(3/2)n) to DB is beta_* ell^2 pointwise in t.
Its unnormalized norm moments of degrees 1,2,3,4 are respectively
O(ell^-1), O(ell^(1/2)), O(ell^2), O(ell^(7/2)).
Its first D therefore costs O(sqrt(ell)); its first B costs O(ell^-1).
Every added quartic costs o(ell^4), since its coefficients at the
unchanged response are uniformly bounded. It has B>0 and D>0,
so meets the support condition exactly. This verifies (5)--(6)
without confusing the required signed cubic with its absolute envelope.

**Weight normalization and the full covariance subtraction.** The two
high-amplitude components give Q>=0, ||Q||<=tr Q=O(sqrt(ell)),
J_R=O(ell^-1), D_R=O(sqrt(ell)), and
E(1-w)=O(ell^-5/2). The fixed g0 in L419 has bounds
0<g_-<=g0<=g_+ and the two stated average identities, proved there
with one fixed power of the absolutely convergent right-line series.
For any bounded response expression R(t),

    |E[w g_H R]-E[g0 R]|
       <= ||R||_infinity (|N_H^-1-1| g_+
                                      +g_+ E(1-w))
       =O_R(H^-1+ell^-5/2).

Here N_H=E(wg0)=1+O(H^-1+ell^-5/2) and g_H=g0/N_H.
This establishes (7), including the possible p=1/2 fibers; it does
not assume uniform convergence of w to one. Also E(wg_H)=1 exactly.
Since W_H>=1/2 eventually and |b| is uniformly separated from zero,
d_H and m=d_H b/|b|^2 are uniformly bounded. Thus the full A_H
in (8) has ||A_H||<=C_A sqrt(ell), not O(1).

To make the margin test explicit, let g_*>0 bound g_H below, let
kappa0>0 be the smallest eigenvalue of K, and let J_* bound ||J||.
The (x,z) block of K has determinant 1/180 and trace 81/80;
in particular kappa0>=4/729 is sufficient. With the fixed uniform
tr(JK)<=-delta0<0 from L419,

    lambda_min(Sigma)>=g_* kappa0 ell-C_A sqrt(ell),
    tr(J Sigma)<=-g_* delta0 ell+3 J_* C_A sqrt(ell).

Both have the needed strict margins for all sufficiently large real H.
Similarly lambda_max(Sigma)<=C ell with one fixed C. This is the
new interface check required to reuse L419's matrix algorithm; its
old O(1)-correction conclusion is unnecessary. The order-sqrt(ell)
error in the first D is allowed by o(ell), but would not be allowed
in any raw second entry or in the first B tolerance.

**Borel realization and translated cone.** The cited real Schur--Horn
theorem is Carlen--Lieb, [arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2),
pp. 1--2, Horn theorem after (1.1), proof through (1.2). It applies to
SJS for any positive definite Sigma=S^2; there is no hypothesis on
the size or sign of its correction matrix. The trace-average vector
is majorized by its ordered eigenvalues, as required. Borel dependence
comes instead from L419's explicit coordinate rotations. In a strict
branch the denominator d_j-tau is positive and the radicand is
e_ij^2+(d_j-tau)(tau-d_i)>e_ij^2. The displayed positive root solves
the Rayleigh equation. Equality branches use a coordinate vector;
the remaining restriction has trace 2tau, so the same procedure ends
after one more rotation. These finite Borel rules apply unchanged to
the present SJS, including repeated eigenvalues and off-diagonal
entries on equality branches.

For xi_i=sqrt(3)S u_i each xi_i^T J xi_i=tr(J Sigma)<=-delta1 ell
and |xi_i|<=C_x sqrt(ell). Hence, uniformly over all six signs,

    D(m +/- xi_i)<=-delta1 ell
                         +2 J_* ||m|| C_x sqrt(ell)+J_* ||m||^2<0

after one common onset. This checks support using the exact quadratic
form, rather than the leading response approximation. Opposite signs
give centered mean zero and covariance Sigma. The normalized mu_t
therefore has raw second matrix Sigma+mm^T. Combining it with p,k,w
gives nonnegative fiber masses summing to one, exactly dt/H marginal
and the actual response at every t. Bounded unit vectors, not bounds
on rotation parameters near branch transitions, control the atom sizes.

**Every selected moment on this same law.** The matrix identity (10)
cancels every entry of Q+E(wmm^T). Consequently all six raw second
moments equal ell K exactly, including xy=yz=0. The B integral is
J_R+W_H d_H=-b0 exactly. These equalities meet both tiny odd errors
and the full first-B tolerance. The D integral is

    ell E[w g_H tr(JK)]+O(sqrt(ell))
      =-a_* ell+o(ell),

using the checked weight normalization and bounded m,J. No O(1)
remainder for that integral is asserted. For the cubic, conditional
central symmetry cancels all odd centered terms; expansion gives

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                      +(m^T Jm)(b^T m)=O(ell).

The bulk contribution is thus O(ell), not merely bounded by its
O(ell^(3/2)) absolute norm estimate. Adding the high O(ell) term
and the exact intermediate beta_* ell^2 proves the stated cubic
tolerance. No equality for the actual capped statistic is used.

For each of the 23 quartics the full integral is its actual integral
plus O(ell^(7/2))+O(ell^2), which preserves its required coefficient.
The same estimates give E_nu U^2=O(ell^4). For U^(3/2) and |B|^3,
the high, intermediate and bulk absolute contributions are respectively
O(ell), O(ell^2), O(ell^(3/2)); their sum is O(ell^2), within both
required O(ell^(9/4)) envelopes. Actual annulus, V_j, response-error
and Ccal bounds never change. On the high r=2^(1/4)rho0 branch,
linearity gives P_j(Y)=s2^(1/4)P_j(X0). On the other branch the
bounded exact conversion gives |P_j(Y)|<=C ell^3. The intermediate
and bulk norms are smaller. Uniformly on [H,2H],
ell^3 L(t)^j/T(t)^(1/2)->0 for j<=2; therefore fixed E_j work
after one onset on all components, with curvature retained.

**Same-family capped limit and scope.** Nothing defining n,r,p,k,w,
g_H,m,Sigma or the atoms uses lambda. For this one family the high
payoff is bounded by its absolute cubic O(ell). For each fixed
lambda>0 the intermediate cap is eventually unsaturated and its payoff
is exactly beta_* ell^(3/2)/lambda. The bulk payoff is at most
C|X|^4/(lambda ell^2), hence O_lambda(1). After division by ell^2
these bounds tend to zero. The cap onset may depend on lambda;
the selected-law constants and their onset do not. The result is
not uniform for lambda tending to zero with H. All data are Borel
and bounded at each fixed H, so every signed and absolute integral
used here exists. The eventual estimates hold for all real H, not
only a sequence, and require no consistency across overlapping intervals.

No failed bound, tolerance or missing direct mathematical dependency
was found. The audit validates the selected-information obstruction
and its existing DAG row without adding a lemma or a numerical premise.
It does not evaluate L418's actual F_lambda, sign actual clipping,
supply L413's quantitative regulator margin, or advance the global
mixed-positivity/zero-exclusion assertion. Additional actual-function
information can still be tested; the scoped stop is not a global ban.

## Mathlib

Full matching coverage has not been checked. The cited Schur--Horn
input and the imported local matrix implementation are distinguished
from a formalization of this entire conditional law. Unknown coverage
is not absence. No mathematical script, numerical fit, moment optimizer
or numerical certificate is an input to the proof.
