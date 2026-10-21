# Lemma 423: a fixed two-weight covariance law matches the added correlation

## Hypotheses

Use precisely L421's selected integrated-moment relaxation at the actual
response on [H,2H], with height marginal dt/H, ell=log H, and its exact
forms B(X;t)=b(t)^T X and D(X;t)=X^T J(t)X. All response coordinates,
derivatives and envelope curvature stay actual. Retain its constants,
all 23 quartic leading coefficients, both first means, six critical raw
second moments, signed cubic, support and qualitative fixed envelopes.
Use the actual coefficient T of L422 (1) and require additionally

    E_nu[W(t)^2 x^2]=T ell+o(ell),
    W(t)=|zeta(5/2+it)|^2, E=H^(-1) integral_[H,2H].       (1)

No conditional critical-moment constraints, consistency across different
H intervals, or realization by one global critical function are imposed.
The choice tested here changes only L421's covariance weight to a fixed
convex combination of the individually calibrated L419 weights at
k=13,14; its high and intermediate components are unchanged.

## Conclusion

This specified mixture is feasible for every sufficiently large real H.
There is one measurable family of conditional laws, independent of any
cap parameter lambda, satisfying L421's entire selected list and (1).
In fact its six raw second entries and first B mean obey exactly

    E_nu XX^T=ell K, E_nu B=-b0,
    K=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]],

and its added mean is T ell+O(sqrt(ell)). The family avoids
{D>0,B<0}, and for every fixed lambda>0 has

    E_nu[|DB| min(1,|X|/(lambda ell^2))]
        =O(ell)+O_lambda(ell^(3/2))+O_lambda(1)=o(ell^2). (2)

Thus adding this one response-weighted second-moment coefficient still
does not force a positive capped liminf in this relaxation. This is an
elementary known-input specialization, validated by the separate step-172
critical audit below. L422's single-power separation remains valid. No actual capped
statistic, negative-B clipping value, global critical-function realization,
full-error regulator margin, global mixed positivity or RH is decided.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-16-mixed-covariance-weight-added-correlation.md`.
Reuse audited L419/L421/L422; the work is REPRODUCTION, not a new
zeta moment theorem or a claim of originality. In particular the actual
T is imported from L422's specialization of M. P. Young, *A short proof
of Levinson's theorem*, Arch. Math. 95 (2010), 539--548,
[Lemmas 4--5, (4.1)--(4.5), pp. 542--543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Its fixed twists, zero shifts, combined diagonals, sharp bracketing and
sequential full-tail limit are already checked there. The observable and
its source hypotheses have not changed; no source theorem is applied
to the artificial critical states constructed below.

### Both calibrated weights are admissible

Use L419/L422's constants C_j, R_k=C_(k+1)/C_k,
C_1=zeta(5), and S=zeta(5)zeta(3)^2/zeta(6). The audited exact
bounds of L422 give the following convenient weaker rational bounds:

    C_13<51, 78<C_14<79, C_15>122,
    C_1<S<3/2.

Consequently

    R_13>78/51=26/17>3/2>S,
    R_14>122/79>3/2>S.                               (3)

Both integer choices therefore satisfy L419's admissibility hypothesis.
For j=13,14 put

    theta_j=(S-C_1)/(R_j-C_1),
    g_j(t)=1-theta_j+theta_j W(t)^j/C_j.

Equation (3) implies 0<theta_j<1. Each weight has a fixed positive
lower bound 1-theta_j and finite upper bound
1-theta_j+theta_j zeta(5/2)^(2j)/C_j. Every parameter is independent
of H. L419 (3) at fixed powers gives

    E g_j=1+O(H^-1), E(g_j W)=S+O(H^-1),
    E(g_j W^2)=B_j+O(H^-1),                          (4)

where B_j is exactly L422 (2).

### The fixed mixture and all its required averages

L422's strict certified bounds give B_13<T<B_14. Define, once,

    alpha=(B_14-T)/(B_14-B_13),
    g0(t)=alpha g_13(t)+(1-alpha)g_14(t).             (5)

Then 0<alpha<1 and alpha B_13+(1-alpha)B_14=T exactly. This
mixes the two functions, not whole conditional laws. There are fixed
constants 0<g_-<=g0<=g_+<infinity by the constituent bounds. By (4),

    E g0=1+O(H^-1), E(g0 W)=S+O(H^-1),
    E(g0 W^2)=T+O(H^-1).                            (6)

For explicit arithmetic verification, the script

    python3 scripts/discriminant/check_mixed_covariance_weight.py

reads L422's audited rational certificate and performs exact Fraction
arithmetic only. Its complete output is
`scripts/discriminant/mixed-covariance-weight-certificate.json`.
Its full `/bounds`, `/checks` and `/failures` fields were inspected:
all ten checks pass and the failures list is empty. It verifies (3),
the strict coefficient brackets and the stronger bound

    1880541626951111/4746507673417200
      <=alpha<=2084346992935393/4563054773374156,
    1/3<alpha<2/3.                                  (7)

For example its lower bound is
(B_14,lower-T_upper)/(B_14,upper-B_13,lower), with positive
denominator; the analogous upper bound uses the opposite endpoints.
This certificate specializes the saved audited enclosures; it is not
a fresh independent verification of their Euler tails. Correct Python
integer/Fraction execution remains its implementation contract. The
analytic construction needs only (3) and 0<alpha<1, not decimal fits.

The complete gamma harmonic also vanishes. In L419's notation write
Z=zeta(5/2+it), R=exp(i phi), so

    a^2=(W+Re(R^2 Z^2))/2,
    h^2=(W-Re(R^2 Z^2))/2.

Each g_j Z^2 is an absolutely uniformly convergent fixed-frequency
series, since j is fixed and Z has an absolutely convergent Dirichlet
series on Re s=5/2. L419 (5) gives E(g_j R^2 Z^2)=o(1) separately
for j=13,14. Its argument first fixes a finite frequency head; each
phase 2phi(t)+ut has derivative log(t/(2pi))+u+O(t^-2), bounded
below by (log H)/2 eventually, and second derivative O(1/H).
Integration by parts bounds its normalized integral by O_u(1/(H log H)).
Then the uniform absolute series tail tends to zero. The fixed linear
combination (5) has the same vanishing harmonic, with no independence
assumption or growing-frequency interchange. Hence (6) implies

    E[g0(a^2/20+h^2/12)]=S/15+o(1).

Using L419's uniform exact-form trace
tr(JK)=-c^2(a^2/20+h^2/12)+O(1/L), c=1/(4pi), yields

    E[g0 tr(JK)]=-a_*+o(1), a_*=c^2 S/15.           (8)

This verifies the full first-D calibration, not just the new correlation.

### Normalization, full correction and exact negative support

Retain exactly L421's high states p(t) delta_Y(t), intermediate states
k(t) delta_Zmid(t), and their Borel direction choice. Their remaining
fiber mass w=1-p-k is in [1/4,1], with E(1-w)=O(ell^-5/2).
Write W_H=Ew, Q for their combined integrated raw second matrix,
J_R for their first B mean, and D_R for their first D mean. The
audited bounds L421 (4)--(6) give

    Q>=0, ||Q||=O(sqrt(ell)),
    J_R=O(ell^-1), D_R=O(sqrt(ell)), W_H=1-O(ell^-5/2).

Normalize the new weight by N_H=E(wg0), g_H=g0/N_H. The fixed
bounds and (6) give N_H=1+O(H^-1+ell^-5/2). Thus g_H has
fixed positive bounds and E(wg_H)=1 exactly. For every uniformly
bounded response expression R0(t),

    E[w g_H R0]-E[g0 R0]=O_R0(H^-1+ell^-5/2).        (9)

Indeed write the difference as (N_H^-1-1)E(wg0 R0)
-E[(1-w)g0 R0] and use the fixed suprema. This controls fibers
where p=1/2 without assuming pointwise smallness of p. Equations
(6),(8),(9) apply respectively to W^2 and tr(JK).

Define exactly as in L421, now with this g_H,

    d_H=(-b0-J_R)/W_H, m(t)=d_H b(t)/|b(t)|^2,
    A_H=-(Q+E[w m m^T])/W_H,
    Sigma(t)=ell g_H(t)K+A_H.                        (10)

Here b0=zeta(3)/(4pi). The audited uniform lower bound on |b|
makes m bounded and B(m)=d_H exactly. No real response projection
is divided by. The symmetric constant matrix A_H has norm
O(sqrt(ell)); its whole matrix, including all odd and even entries,
is retained. With kappa0=lambda_min(K)>0, g_*>0 a lower bound for
g_H, ||J||<=J_*, ||A_H||<=C_A sqrt(ell), and the uniform exact
tr(JK)<=-delta0<0 from L419, one has

    lambda_min(Sigma)>=g_* kappa0 ell-C_A sqrt(ell),
    tr(J Sigma)<=-g_* delta0 ell+3J_* C_A sqrt(ell).

Therefore c1 ell I<=Sigma<=c2 ell I and
tr(J Sigma)<=-delta1 ell for fixed positive constants eventually.
The new weight changes these constants but not their strict margins.

Apply L419's Borel six-state coordinate construction to J,Sigma,m.
Its named existence input is the real Schur--Horn theorem, in
E. A. Carlen and E. H. Lieb, *Short proofs of theorems of Horn and
Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), pp. 1--2,
Horn's theorem after (1.1), proof through (1.2). The trace-average
diagonal is majorized by the eigenvalues of SJS, S=Sigma^(1/2).
L419's explicit Borel rotations, beyond pointwise theorem existence,
give an orthonormal basis u_i with u_i^T SJS u_i=tr(J Sigma)/3.
Use the six atoms m +/- sqrt(3)S u_i with probabilities 1/6.
Their mean is m, centered covariance Sigma and centered symmetry
is exact. Their centered D values are tr(J Sigma). Translation by
bounded m changes each by O(sqrt(ell))+O(1), so all six have exact
D<0 eventually and |X|=O(sqrt(ell)), with uniform constants.
Let mu_t be this conditional law and set

    nu_(H,t)=p(t)delta_Y(t)+k(t)delta_Zmid(t)+w(t)mu_t. (11)

All masses are nonnegative and sum to one in every fiber. Borel
coefficients and the imported explicit rotation rules make (11)
measurable. Its height marginal and complete response are exact.

### Every original constraint and the added correlation

The full matrix correction gives, without an error term,

    E_nu XX^T=Q+ell K+W_H A_H+E[wmm^T]=ell K.

Thus the four even second entries meet their O(1) tolerances with
zero errors, and xy=yz=0 meets their respective much smaller
O(H^-2/3 ell^-1), O(H^-2/3 ell^-3) tolerances. Separately
E_nu B=J_R+W_H d_H=-b0 exactly, meeting the full first-B error
O(ell^-1+H^-1/2 ell^2). For the first D, (8)--(10) give

    E_nu D=D_R+ell E[w g_H tr(JK)]
                +E[w(tr(J A_H)+m^T Jm)]
           =-a_* ell+o(ell),

because the retained remaining terms are O(sqrt(ell)). This is the
required first-D tolerance; an O(1) residual is not claimed.

In the new weighted x^2 observable, bounded W^2 makes the high and
intermediate contributions O(ell^-2) and O(sqrt(ell)). The full bulk
contribution, including its mean, is

    E[w W^2(Sigma_11+m_1^2)]
       =ell E[w g_H W^2]+O(sqrt(ell))
       =T ell+O(sqrt(ell)).

The last equality uses (6),(9); ell/H+ell^-3/2=o(1). This proves
(1) for the complete law, not just its leading bulk covariance.

Centered symmetry of mu_t gives the exact cubic expansion

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                      +(m^T Jm)(b^T m)=O(ell).

The unchanged high component contributes O(ell), and the unchanged
intermediate component contributes exactly beta_* ell^2. Thus the
full signed cubic is beta_* ell^2+O(ell), within o(ell^2).

For each of the 23 quartics D^2, DB^2, D omega_i omega_j (i<=j),
L421's high homogeneity identity preserves its actual integral exactly,
including signed off-diagonal and zero leading coefficients. The
unchanged intermediate addition is O(ell^(7/2)); bounded response
coefficients and |X|=O(sqrt(ell)) bound the new bulk addition by
O(ell^2). Both errors are o(ell^4). Every required actual leading
coefficient therefore survives. The same component estimates give
E_nu |X|^4=O(ell^4). For each of |X|^3 and |B|^3 their high,
intermediate and bulk absolute contributions are respectively
O(ell), O(ell^2), O(ell^(3/2)). Hence both full third-power
envelopes are O(ell^2), within the specified O(ell^(9/4)) bounds.

The actual response annulus, derivative bounds, strict Ccal lower
bound, approximation bounds and curvature never change. The high
states still have either |Y|=ell^3 or Y=s2^(1/4)X_actual; L421's
qualitative physical-jet bounds on both branches remain valid. The
intermediate norm is ell^(3/2) and the new bulk norm O(sqrt(ell)).
Since the exact conversion matrix is bounded and
ell^3 L(t)^j/T(t)^(1/2)->0 uniformly for H<=t<=2H, j<=2,
one fixed set of qualitative constants works on all components.
All onsets needed for this fixed mixture have a finite maximum, so
the selected constraints hold for every sufficiently large real H.
At each fixed H all states are bounded on the height interval; all
signed and absolute observables used here are integrable.

Finally, high support avoids the joint sign by L421's orientation,
intermediate support has B,D>0, and the new bulk has D<0. For (2),
the unchanged high absolute cubic is O(ell), so also bounds its
capped contribution. For fixed lambda the intermediate cap eventually
equals lambda^-1 ell^-1/2, giving exactly beta_* ell^(3/2)/lambda.
The bulk cap is eventually unsaturated and its payoff is at most
C|X|^4/(lambda ell^2), whose integral is O_lambda(1).
The law (11) does not use lambda. Its constraint onset is fixed;
the later cap onset may depend on lambda. Dividing these three
nonnegative bounds by ell^2 proves (2), without cancellation.

This completes the specified local feasibility construction. The separate
audit below validates its stated scope; it supplies no actual-function
realization or conclusion about the actual clipped statistic.

### Separate critical audit — 2026-10-16, step 172

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-16-mixed-covariance-counterlaw-audit.md`.
The construction passes in its stated integrated-moment relaxation.
This establishes reliability of the existing local obstruction, not a
new zeta theorem, original general moment theorem or actual capped value.
The precise Young and Carlen--Lieb inputs above are reused through
audited L422 and L419 respectively. No additional theorem hypotheses,
growing twist, conditional actual moment or independent phase law enter.

**Arithmetic and fixed calibration.** The full generator was read and
rerun with the command above. Its complete `/bounds`, `/checks` and
`/failures` were inspected, together with the complete inherited
`/bounds` of L422's source certificate. All ten checks pass; failures
are empty. The inherited rational endpoints imply C_13<51,
78<C_14<79 and C_15>122. Both lower ratio bounds therefore exceed
3/2>S>C_1. In the generator, positive-interval division is used on
C_13,C_14 and B_14-B_13. The numerator B_14-T is positive throughout
its interval, so the lower and upper quotient endpoints used for alpha
are valid even without assuming independence of the constants. They
are exactly (7). This checks the specialization of already audited
Euler bounds, not a fresh independent verification of their infinite
tails. Correct integer/Fraction execution is the implementation contract;
decimal previews are not evidence.

The exact alpha in (5), rather than a rational approximation from (7),
is used in the law. Both theta_j lie strictly between zero and one.
At each j, the three averages in (4) use respectively the fixed moments
C_j, C_(j+1), C_(j+2) and their O(H^-1) errors. Their fixed linear
combination gives (6), including the exact T coefficient. Upper and
strictly positive lower bounds for g0 are independent of H. For the
gamma term, g_j Z^2 has absolutely summable fixed-frequency coefficients.
At each finite head the complete integration-by-parts formula has two
endpoint terms O(1/log H) and an integral O(1/log^2 H), before division
by H. The remaining series has a uniform absolute tail. Taking H first
and then the head limit proves the harmonic vanishing for both weights.
No rate is needed beyond o(1): first D allows o(ell). The coefficients
(1/20+1/12)/2=1/15 then give (8), with all gamma terms retained.

**Remaining mass and matrix margins.** L421 (4)--(6) are unchanged:
the high branch has p<=1/2, the intermediate k<=1/4 eventually,
E(1-w)=O(ell^-5/2), and Q>=0 with norm O(sqrt(ell)). These are
unnormalized component integrals. Uniform smallness of p is unnecessary
and is not assumed. For bounded R0 the difference in (9) is exactly

    (N_H^-1-1) E(wg0 R0)-E[(1-w)g0 R0].

Fixed bounds on g0,R0 and N_H=1+O(H^-1+ell^-5/2) prove its stated
error. In particular E(wg_H)=1 exactly, not just asymptotically.
The actual lower bound for |b| and W_H bounded away from zero imply
bounded d_H,m. Thus the whole symmetric A_H, including both odd
entries, is O(sqrt(ell)). The two displayed spectral/trace inequalities
after (10) follow from the operator norm bound and
|tr(J A_H)|<=3||J|| ||A_H||. The strictly positive eigenvalue of K
and the strictly negative tr(JK) give margins of order ell, dominating
this correction uniformly. An O(1) correction has not been assumed.

The constant trace-average diagonal of SJS is majorized by its real
eigenvalues, so the cited real Schur--Horn theorem applies. Borel
dependence is checked separately using L419's explicit rotations.
On each strict branch d_i<tau<d_j, the denominator d_j-tau is positive
and the radicand e^2+(d_j-tau)(tau-d_i)>e^2. The given positive root
solves (d_j-tau)eta^2+2e eta+d_i-tau=0. Equality branches select a
coordinate vector; the complementary restriction has trace 2tau, so
one more such rotation suffices. Finite comparisons and deterministic
ties are Borel, including repeated eigenvalues. Only the resulting
unit vectors need be bounded, not the rotation parameters near ties.

For xi_i=sqrt(3)S u_i, opposite signs give mean zero and covariance
Sigma, while xi_i^T J xi_i=tr(J Sigma)<=-delta1 ell. If |m|<=M_0
and |xi_i|<=C_x sqrt(ell), every translated atom satisfies

    D(m +/- xi_i)<=-delta1 ell
                       +2J_* M_0 C_x sqrt(ell)+J_* M_0^2<0

after one common onset. This is exact negative support, with curvature
included. The masses in (11) sum to one at each t, so the height and
response marginal are unchanged. Parameter integration over t=Hu,
1<=u<=2, makes the defining H-dependent averages Borel as well: their
integrands are Borel and locally bounded on compact eventual H ranges.
This also gives a measurable family if that phrase is read jointly
in (H,t); no consistency of different H laws is claimed.

**Exact tolerances and every component.** L421's selected list, checked
against L414 (1), L415 (1) and L416 (1), requires first D with o(ell),
first B with O(ell^-1+H^-1/2 ell^2), four even second errors O(1),
and odd errors O(H^-2/3 ell^-1), O(H^-2/3 ell^-3). It imposes no
critical first means or response-conditioned covariance. The full
matrix identity after (11) gives zero error in all six entries, and
J_R+W_H d_H=-b0 gives zero first-B error. The remaining O(sqrt(ell))
terms in first D are permissible; they are not left in a second entry.

For the added observable, bounded W^2 controls the complete high and
intermediate contributions by O(ell^-2) and O(sqrt(ell)). In the bulk,
K_11=1 and both A_H,11 and m_1^2 are retained. Hence its mean is
ell E(wg_H W^2)+O(sqrt(ell))=T ell+O(sqrt(ell)); the normalization
error is O(ell/H+ell^-3/2). This verifies the claimed complete-law
coefficient, rather than only its centered bulk approximation.

The six-state central symmetry gives the displayed exact cubic expansion:
the two surviving centered quadratic terms are
(b^T m)tr(J Sigma) and 2m^T J Sigma b, in addition to the constant
term. They are O(ell). The high cubic is O(ell), and the intermediate
cubic is exactly beta_* ell^2. For all 23 quartics, including signed
and zero leading entries, the high contribution is the actual integrand
by degree-four homogeneity. The extra costs are O(ell^(7/2)) and
O(ell^2), both o(ell^4). The fourth envelope is O(ell^4); the high,
intermediate and bulk third envelopes sum to O(ell)+O(ell^2)+
O(ell^(3/2))=O(ell^2), within the required O(ell^(9/4)).

The response annulus, derivatives, approximation errors and Ccal lower
bound remain actual. On the high scaling branch the exact physical jets
are s2^(1/4) times the actual jets; on its other branch their size is
O(ell^3). The intermediate and bulk sizes are smaller. The uniform
limit ell^3 L(t)^j/T(t)^(1/2)->0 for j<=2 permits one fixed enlargement
of qualitative constants. All constraint onsets have a finite maximum
for this fixed alpha, giving every sufficiently large real H. At each
fixed H all atoms and response functions are bounded, so the integrals
exist. No preassigned smaller pointwise constants are being claimed.

**One law, every fixed cap.** High support has D<=0 or B>=0 by the
unchanged orientation; intermediate support has D,B>0; bulk support
has D<0. The nonnegative capped contributions of these components are
bounded respectively by O(ell), exactly beta_* ell^(3/2)/lambda
eventually, and O_lambda(1). The last follows from
|DB| min(1,|X|/(lambda ell^2))<=C|X|^4/(lambda ell^2)
and the bulk fourth bound. After division by ell^2 each tends to zero.
No parameter defining the law uses lambda. Constraint constants and
their onset are fixed; the cap onset may depend on each fixed lambda.
No assertion uniform in a shrinking lambda is made.

No failed interface or missing direct mathematical input was found.
The DAG row remains L419 L421 L422. L422's single-power stop and
L421's original selected-list obstruction both survive this extension.
The audit supplies no actual critical-function realization, actual
clipping, full-error regulator margin, global positivity or RH result.

## Mathlib

Full matching coverage for this conditional-law specialization has not
been checked. The precise Young and real Schur--Horn inputs are cited
above; L419 supplies the extra Borel implementation. Supporting facts
do not constitute a formalization of this complete construction.
Unknown coverage is not absence. No Lean verification is claimed.
