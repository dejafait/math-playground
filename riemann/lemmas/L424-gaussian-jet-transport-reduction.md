# Lemma 424: finite-interval Gaussian jet transport and the unresolved bulk defect

## Hypotheses

Let H>1, ell=log H, L(t)=log(2+t), and E denote H^(-1) times
integration over [H,2H]. For the trajectory statement let f be any real
C^2 function on this closed interval, with the ordinary jets of L405,

    x=f, y=f'/L, z=f''/L^2.

No bound uniform in H and no third derivative are assumed for this
statement. Set a=x/sqrt(ell), b=y/sqrt(ell), d=z/sqrt(ell), and define

    psi(a,b)=ab exp(-a^2-b^2),
    chi(a,b)=psi+b psi_b=2ab(1-b^2)exp(-a^2-b^2),
    Q(a,b,d)=b psi_a+d psi_b
      =exp(-a^2-b^2)[b^2(1-2a^2)+ad(1-2b^2)],
    kappa(t)=L'(t)/L(t)^2=1/((2+t)L(t)^2).

For the law comparison use exactly the complete L423 law, including
its fixed k=13,14 weight mixture, the high and intermediate components
of L421, its bounded translation m(t), full covariance correction,
actual response derivatives and curvature. Write its bulk as

    nu_(H,t)=p delta_Y+k delta_Zmid+w mu_t,
    w=1-p-k,
    mu_t=(1/6) sum_(i=1)^3 [delta_(m+sqrt(3) S u_i)
                              +delta_(m-sqrt(3) S u_i)],
    S=Sigma^(1/2), Sigma=ell g_H K+A_H.

Here K and every other quantity are precisely those in L423, not fitted
parameters. In particular m is uniformly bounded, ||A_H||=O(sqrt(ell)),
c_1 ell I<=Sigma<=c_2 ell I eventually, and u_i are L419's actual
Borel orthonormal basis for S J S with constant trace-average diagonal.
Keep this basis at its exact finite-H matrices, including branch ties.
The law has height marginal dt/H. E_nu includes its conditional states.
All bounds below hold for sufficiently large real H with fixed constants.

## Conclusion

Every such C^2 trajectory satisfies the exact identity

    E[Q(a,b,d)-kappa chi(a,b)]
      = [psi(a(t),b(t))/L(t)]_(t=H)^(2H)/H.          (1)

In particular, with c_psi=1/(2e) and
c_chi=1/e+3sqrt(3)/(2e^2),

    |E Q| <= delta_H,
    delta_H = {c_psi[1/L(H)+1/L(2H)]
                  +c_chi[1/L(H)-1/L(2H)]}/H
             =O(1/(H log H)).                       (2)

For the complete L423 law put

    V_i(t)=sqrt(3/ell) S(t)u_i(t),
    B_H=E[(w(t)/3) sum_(i=1)^3 Q(V_i(t))].           (3)

This is an actual finite-H bulk integral, not an independently averaged
phase model. Then

    E_nu Q(X/sqrt(ell))=B_H+O(ell^-1),
    E_nu[Q(X/sqrt(ell))-kappa chi(x/sqrt(ell),y/sqrt(ell))]
        =B_H+O(ell^-1)+O(1/(H ell^2)).               (4)

The high contribution to Q is O(ell^-3). The intermediate contribution
is exactly

    E k * exp(-5ell^2/9) [5ell^2/9-16ell^4/81],     (5)

and therefore is O(ell^(3/2)exp(-5ell^2/9)). All components, the
bounded bulk translation and the full covariance correction are included.

Consequently a nonzero limsup of |B_H| would separate this law from
trajectory occupation laws that agree on the displayed transport
observable up to o(1). No nonzero limsup, sign, vanishing, or quantitative
lower bound for B_H is proved here. This reduction does not reject or
realize L423. Its selected-moment obstruction, all actual clipping and
regulator gaps, and the main RH gap are unchanged. The completed attempt
is EXPLORATION / REPRODUCTION, not a new transport theorem or a claim of
novelty. The separate step-177 critical audit below validates this
reduction, without estimating B_H.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-jet-trajectory-compatibility.md`.
Its inspected primary necessary identity is J. B. Lasserre, D. Henrion,
C. Prieur and E. Trelat, *Nonlinear optimal control via occupation
measures and LMI-relaxations*, SIAM J. Control Optim. 47 (2008),
1643--1666, [DOI 10.1137/070685051](https://doi.org/10.1137/070685051),
[author manuscript dated 2008-01-30](https://homepages.laas.fr/henrion/Papers/ocp.pdf),
Sections 2.1--2.3, equations (2.7), (2.10)--(2.12), manuscript pp. 3--5.
Equation (2.12) integrates the time/state derivative of a C^1 test along
a trajectory, with both terminal values. No no-gap or realization theorem
is imported. The source is reused from the completed assessment.

The assessed integrability comparison is D. Henrion, M. Korda,
M. Kruzik and R. Rios-Zertuche, *Occupation measure relaxations in
variational problems: the role of convexity*,
[2023-03-04 manuscript](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
Definitions 2.4/2.7 and (6)--(8), pp. 3--4, and Lemma B.1 with proof,
pp. 17--18. It does not assert uniform integrability of this H-dependent
family. Here no weak limit is taken: at every fixed H, continuous
trajectory jets lie in a compact box, and L423's conditional states
are bounded. The smooth test is permitted on each finite box. The
following derivative and component calculations are the required local
specialization; neither source theorem is reproved.

### Exact dynamics, test derivatives and both endpoints

Differentiate before dividing, using only f in C^2:

    x'=L y, y'=L z-(L'/L)y.

Treat ell as constant on this interval. The test
g_H(t,x,y)=psi(x/sqrt(ell),y/sqrt(ell))/L(t) is C^1,
and its derivatives are

    partial_t g_H=-(L'/L^2)psi,
    partial_x g_H=psi_a/(L sqrt(ell)),
    partial_y g_H=psi_b/(L sqrt(ell)),
    psi_a=b(1-2a^2)exp(-a^2-b^2),
    psi_b=a(1-2b^2)exp(-a^2-b^2).

Thus its transport derivative is exactly Q-kappa chi, proving (1)
by the cited finite-interval identity. No derivative of z, response
freezing, phase averaging or stationarity assumption has occurred.

For s=a^2+b^2, |ab|<=s/2 gives |psi|<=1/(2e). Also

    |chi|<=2|ab|exp(-a^2-b^2)
                   +2|a||b|^3 exp(-a^2-b^2)
          <=1/e+3sqrt(3)/(2e^2)=c_chi.

The second bound uses the maxima of u exp(-u^2) and
u^3 exp(-u^2) on u>=0, attained respectively at u^2=1/2 and
u^2=3/2. Finally

    integral_[H,2H] kappa dt=1/L(H)-1/L(2H)>0.

These bounds prove the explicit budget (2), with no endpoint jet
estimate. The kappa contribution alone is O(1/(H ell^2)), since
kappa<=1/((H+2)ell^2). The same bound holds on every probability
kernel with this height marginal. This verifies scaling on the law
without assuming that it satisfies the dynamics.

### High and intermediate states

For s>=0, |(1-2s)exp(-s)|<=1: on [0,1/2] it is bounded by one;
on [1/2,infinity) its maximum is 2exp(-3/2)<1. Hence globally

    |Q(a,b,d)|<=b^2+|ad|<=a^2+b^2+d^2.              (6)

L421's complete high second-moment estimate is
E[p|Y|^2]=O(ell^-2), including both definitions of its radius and
the zero-state convention. Dividing (6) by ell proves O(ell^-3).
Thus no supposition that the Gaussian kills every high state is used;
states with small first two coordinates and large third coordinate
are also controlled. This comparison uses the saved moment bound,
not a maximum estimate for the actual critical jets.

L421's intermediate direction is, up to overall sign, either
(2/3,1/3,2/3) or (2/3,-1/3,2/3), with radius ell^(3/2).
After division by sqrt(ell), both choices have

    a^2=4ell^2/9, b^2=ell^2/9, ad=4ell^2/9.

Substituting these exact values in Q proves (5), regardless of which
direction or sign is selected at a given height. L421 gives
0<=k(t)<=C ell^-5/2 uniformly. Multiplication proves the stated
exponential bound. All response dependence in k remains in E k;
there is no independence assumption. The expression in brackets is
negative eventually, but its exponentially small size supplies no
order-one separator.

### Exact bulk and its bounded translation

Write M=m/sqrt(ell). The bounds in L423 give |M|<=C/sqrt(ell)
and |V_i|<=sqrt(3c_2), uniformly. Q is smooth on R^3, even under
simultaneous negation of its three arguments, and has bounded Hessian
on any fixed compact ball. Choose one such ball containing all
V_i+theta M, |theta|<=1, eventually, and let C_2 bound the operator
norm of its Hessian there. Taylor's formula with integral remainder
then gives

    |[Q(V_i+M)+Q(V_i-M)]/2-Q(V_i)|
          <=(C_2/2)|M|^2=O(ell^-1).                (7)

The conditional expectation over the original six translated atoms
is (1/6) times the sum of the two terms on the left of (7); Q's
evenness converts Q(M-V_i) to Q(V_i-M). Averaging with the actual
w<=1 therefore gives B_H+O(ell^-1). Add the high and intermediate
contributions to obtain the first line of (4); the global chi bound
gives its second line.

The matrix A_H, the normalization g_H, actual J and curvature, and
the exact Borel vectors u_i have all stayed in (3). In particular,
||A_H||/ell=O(ell^-1/2) alone does not justify replacing the chosen
u_i by a limiting basis: the algorithm changes branches. No continuity
or exceptional-set bound for that replacement is claimed. Formula (3)
is a well-defined bounded measurable integral at each finite H by the
L419/L423 construction. It remains to be estimated on actual heights.

### Bounded numerical screen and its limitations

The ancillary command

    python3 scripts/discriminant/explore_gaussian_jet_transport.py

saves all grid summaries to
`scripts/discriminant/gaussian-jet-transport-exploration.json`.
It uses 2048 midpoint phases and 101 covariance scales from .001 to
100, the leading normalized response matrix, covariance gK, zero
translation, and the coordinate rotation rule. It uses floating-point
arithmetic, not interval arithmetic. At g=1 the sampled phase mean is
approximately -0.007545, but individual phase values have both signs;
the sampled phase means also change sign across the tested g range.
These observations suggest no direct pointwise-sign shortcut. They
are not rigorous sign assertions, bounds on B_H, or proof of a
phase-averaged limit. None is an input to (1)--(7).

The certificate explicitly records three unresolved obligations:
rigorous quadrature error, control of branch transitions when replacing
the exact basis, and actual response-modulus/height averaging. The
small matrix residual checks only the floating implementation at its
sample points. It is not a verified mathematical margin. No actual
limiting distribution, weak-limit interchange, or realization follows.
The diagnostic stops without a certified separator; its remaining
bulk integral and all failures are preserved for review.

### Separate critical audit — 2026-10-17, step 177

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-gaussian-jet-transport-audit.md`.
No defect was found in (1)--(7) under their stated hypotheses. The result
is validation of an existing local specialization, not a new occupation
theorem, a separator, or an estimate of B_H. The two primary sources
and their exact locations above are reused within the assessed scope.

**Admissible trajectory and exact derivative.** L405 differentiates
f before dividing by L. Consequently, with ell fixed while t varies,

    a'=L b, b'=L d-(L'/L)b.

The two-coordinate curve (a,b) is C^1 when f is C^2, even though d
need only be continuous. The explicit time derivative of psi/L is
-(L'/L^2)psi, and its derivative through b contributes
-(L'/L^2)b psi_b. The two other terms are precisely b psi_a+d psi_b.
This verifies the nonautonomous substitution into the cited 2008
identity (2.12). At each fixed H the trajectory and third-jet control
are bounded on the closed interval; the dynamics are smooth in their
state/control variables and L>0. Restricting to a finite compact box
therefore meets the imported identity's hypotheses. No H-uniform box,
third derivative or sufficient realization theorem is used. The 2023
Lemma B.1 integrability discussion supplies no extra limiting assertion.

**Constants, signs and endpoint budget.** The bound for psi uses
max_(s>=0) s exp(-s)=1. For the second term of chi the product of
the separate maxima, including its factor two, is

    2 [2^(-1/2)e^(-1/2)] [(3/2)^(3/2)e^(-3/2)]
       =3sqrt(3)/(2e^2).

The first term is at most 1/e. Both constants in (2) are thus global,
independent of the endpoint jets. The signed integral of kappa is
1/L(H)-1/L(2H), which is positive because L increases. The absolute
terminal contribution is the sum c_psi[1/L(H)+1/L(2H)]/H, not a
difference and not a discarded endpoint. Together they give exactly
delta_H in (2). Moreover L(2H)-L(H)<log 2 and L(H)>ell, so the
kappa part is at most c_chi log 2/(H ell^2). The same bound applies
to E_nu(kappa chi): each fiber is a probability measure and its height
marginal is dt/H. This does not impose the dynamics on the artificial law.

**Global Q control and the complete high component.** Factoring the
first term of Q as b^2 exp(-b^2)(1-2a^2)exp(-a^2), and the second
as ad exp(-a^2)(1-2b^2)exp(-b^2), gives (6) from
sup_(s>=0)|(1-2s)exp(-s)|=1. Also |ad|<=(a^2+d^2)/2.
In L421 both nonzero radius branches satisfy r>=ell^3 and
p|Y|^2=rho0^4/r^2. Their integrated contribution is therefore at
most ell^(-6)E rho0^4=O(ell^-2); at rho0=0 it is zero. Applying
(6) to Y/sqrt(ell) gives O(ell^-3) with a fixed constant. This covers
large third coordinates even when the first two coordinates are small.
Neither pointwise smallness of p nor Gaussian decay of each high atom
has been assumed. L423 leaves this whole component unchanged.

**Intermediate component and normalization.** L421 selects n_+ or n_-
and may negate the entire vector. Thus both signs of its second
coordinate and both overall signs give the same a^2,b^2,ad in (5).
Inserting them into Q gives the quadratic coefficient (1+4)/9 and
the quartic coefficient -(8+8)/81. Since the radius is ell^(3/2),
the scaled radius is ell, not sqrt(ell). Hence (5) is the exact
conditional value times the actual probability k(t), integrated over
height. Its magnitude before multiplication by k is O(ell^4
exp(-5ell^2/9)); k<=C ell^(-5/2) gives the claimed
O(ell^(3/2)exp(-5ell^2/9)). The response-dependent choice of n and k
is never averaged independently of height. This component is also
unchanged in L423.

**Exact corrected bulk, branches and translation.** L423 (9)--(11)
and its step-172 audit give fixed bounds for g_H,m, the full
A_H=O(sqrt(ell)), and c1 ell I<=Sigma<=c2 ell I, with w in [1/4,1].
These are the corrected quantities, not L419's earlier rare-component
estimates. Positive matrix square root is continuous on positive
definite matrices. L419's strict branches use a nonzero positive
denominator and positive radicand; equality branches select coordinate
vectors. Finite deterministic comparisons, including the complementary
two-dimensional case, make all the u_i Borel. Their norms equal one
even near a branch tie. No continuity of this selected basis is needed.
It follows that V_i and Q(V_i) are bounded measurable functions of
height at every fixed H, so (3) exists with the exact height marginal.

On a fixed ball containing all V_i+sM, |s|<=1, the Hessian of Q is
bounded by a constant C_2 independent of H and i. The two Taylor
remainders are each bounded by C_2|M|^2/2. Their linear terms cancel,
and Q(-V_i+M)=Q(V_i-M) because Q is even under simultaneous
negation. Accordingly the bulk expectation is

    E [w/3 sum_i {Q(V_i+M)+Q(V_i-M)}/2]
       =B_H+O(ell^-1).

This checks both the factor 1/3 from the six equally weighted states
and the sharper translation error. The complete covariance correction
has not been charged to this error: it remains inside every V_i.
Combining this with the two preceding component bounds and the global
chi estimate proves both lines of (4). No original moment tolerance,
response derivative, curvature term, envelope or height marginal is
altered by evaluating this additional observable on the same law.

**Scope of the necessary test.** For genuine trajectories, (2) tends
to zero, independently of their sizes. For L423, (4) differs from B_H
by a quantity tending to zero. Therefore limsup |B_H|>0 would preclude
o(1) agreement on this specific observable. It would not follow merely
from weak convergence: Q is unbounded in its third coordinate. No such
limsup, weak-limit passage or agreement is assumed or established.
The numerical phase screen is not an input and was not rerun. Its
recorded failures remain: quadrature, basis replacement and actual-height
averaging are unverified. This audit validates only the exact reduction;
actual clipping, the full-error regulator margin and RH remain open.

## Mathlib

Full matching coverage has not been checked. Generic differentiation
and integration-by-parts support is not asserted to formalize this
H-dependent occupation-law comparison, the Borel basis construction,
or the unresolved bulk average. Unknown coverage is not absence.
