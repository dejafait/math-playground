# L273 — Mass and projection comparison in the exterior-circulation static trace

## Hypotheses

Use precisely L272(3)'s T_(i,f,N), L123(2)'s K_(i,f) and L123(5)'s
E_(i,N)^f. Thus the group is SU(2), i=3,6 are both actual probes,
the box is (-4,4)^4 with all-face relative pinned links, the direction-1
forest is straight and lower rooted, N is sufficiently large, admitted
and even, a=8/N, tau=1/16, and coordinates are ordinary stored ones.
Take the bare coefficient at fixed mesh before refinement. Retain all
source/end rows, axial levels, allowed constant component indices,
actual path/generator filters and complete finite-mesh heat sums.
Import the qualifications of L272 and its inputs; this is not their
separate critical audit.

At each transverse level let E and F denote the finite relative edge
and plaquette spaces, D:E->F the circulation, d the relative vertex
gradient, Delta=Delta_T the edge Hodge Laplacian, P the gradient
projection and Q=I-P. Define the unprojected normalized local matrices

    Cbar_k(s)=C_k(s)/a^2,    Fbar_k(s)=F_k(s)/a,          (1)

where C_k,F_k are exactly L110's matrices. The letter Cbar is distinct
from the fixed generator clover selectors. L123 and L111 give

    beta_k=P Cbar_k Q,    alpha_k=P Fbar_k D,
    g(s)=H_s D,    H_s=sum_r T_r M_(b_(r,s)) C_r.        (2)

All coefficients in (1)--(2) remain finite-mesh coefficients at level s.
No continuum exterior or common-index frozen value is substituted.
For 0<epsilon,delta<=1 put

    R_epsilon=(Delta+epsilon I)^(-1),
    P_delta=d(d^*d+delta I)^(-1)d^*,    Q_delta=I-P_delta.

Also set R_0=Delta^(-1), P_0=P, Q_0=Q. The estimates below assume
N sqrt(epsilon)>=1 and N sqrt(delta)>=1 when these parameters are
positive. No operator norm convergence of P_delta to P is assumed.

## Conclusion

Define the following two ordered plaquette traces and their full sum:

    U_(i,N;epsilon,delta)=a^2 sum_(k,l)c_(i;kl,a) sum_(s=1)^(N-1) s
       {Tr_F[D R_epsilon Cbar_l(s)^* P_delta Fbar_k(s) D H_s]
        +Tr_F[D R_epsilon D^* Fbar_l(s)^* P_delta
                                             Cbar_k(s) Q_delta H_s]}.
                                                               (3)

Then U_(i,N;0,0)=T_(i,f,N) exactly, and

    |T_(i,f,N)-U_(i,N;epsilon,delta)|
       <= C_i N^3[epsilon log(e/epsilon)+delta^(3/4)].    (4)

In particular, with epsilon_N=N^(-1/2), delta_N=N^(-2/3),

    |E_(i,N)^f-U_(i,N;epsilon_N,delta_N)|
                              <= C_i N^(5/2)log(eN).    (5)

The comparison fits the approved N^(5/2)log(eN)^2 budget for both
probes. It does not establish that complete remainder: the remaining
obligation is the comparison of exactly (3) at this schedule with
a^(-3)K_(i,f). Boundary transfer, ordered coefficient freezing,
raw exterior/full heat matching and quadrature remain unproved here.
The inverse square-root scales N^(1/4), N^(1/3) merely identify possible
localization scales; they are not a proof of localization. No new
coefficient value, L011 assembly, interacting estimate or continuum/
infrared construction follows. The separate 2026-10-24 audit in proof
section 5 accepts (3)--(5) relative to the imported inputs; L272 and
the other upstream audit qualifications remain unresolved.

## Proof

### 1. Reduce the finite trace before regularizing any projection

The finite relative cochain identities give

    DP=0, DQ=D, QD^*=D^*, [Delta,P]=0,
    D^*D=Delta Q.                                      (6)

For the last identity, Delta=dd^*+D^*D, Dd=0, and
Delta P=dd^*, by P=d(d^*d)^(-1)d^*. The Dirichlet vertex inverse
exists. The edge inverse exists too: L095's transverse relative
spectrum has no zero eigenvalue, despite its retained constant
own-direction indices. These are relative cochain identities, not
scalar Dirichlet conditions imposed on all edge components.

For this paragraph only let T_epsilon be L272(3) with its single
Delta^(-1)Q replaced by R_epsilon Q. Substituting (2), its two
edge-trace products at a fixed k,l,s are

    Tr_E[R_epsilon Q Cbar_l^* P Fbar_k D H_s D],
    Tr_E[R_epsilon D^* Fbar_l^* P Cbar_k Q H_s D].      (7)

Here adjacent P^2=P and Q^2=Q have been used for the exact projections;
D Q=D removes the Q following alpha. Rectangular trace cyclicity
moves only the last D to the front. Since D R_epsilon Q=D R_epsilon,
(7) becomes the two traces in (3) with delta=0. This proves
T_epsilon=U_(i,N;epsilon,0), also at epsilon=0.

This reduction retains both mixed orientations individually. It does
not commute Cbar, Fbar, H_s or their scalar coefficients through an
inverse or projection. Only after (7) is reduced do we replace the
displayed P and Q by P_delta and Q_delta. In particular (3) is not
defined by replacing all projections in the unreduced expression and
then incorrectly applying P_delta^2=P_delta. There is no extra
orientation half or outside factor 3.

By L088(5), the actual bounded-multiplicity path stencils in L110,
and L111(1), one fixed polynomial p satisfies, uniformly on all rows
and levels,

    ||Cbar_k||+||Fbar_k||<=C p(k),
    ||D||+||H_s||<=C,
    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.               (8)

The first assertion uses the unprojected bounds for f_k/a^2 and
b_k/a,q_k/a, not an inference from norms after projection. No
coefficient regularity or remote-row cutoff is used in this step.

### 2. Keep the circulation on the inverse error

Write B_epsilon=R_0-R_epsilon. It is positive and commutes with P,
Q and Delta, with spectral multiplier epsilon/[lambda(lambda+epsilon)].
Equation (6) shows that the nonzero singular values of D B_epsilon
are

    epsilon/[sqrt(lambda)(lambda+epsilon)]           (9)

on the co-closed edge spectrum. The nonzero eigenvalues of the positive
plaquette matrix D B_epsilon D^* are epsilon/(lambda+epsilon).
These follow by taking (D B)^*(D B)=B Delta Q B and by the
singular-value correspondence on im D. No signed response is asserted
positive.

L095(14)'s full transverse spectrum has lambda>=c r^2/N^2 and at most
C r^2 eigenvalues in each shell r=1,...,N-1, including all components.
The function of lambda in (9) is decreasing. With M=N sqrt(epsilon),
1<=M<=N, summing the full spectrum therefore gives

    ||D B_epsilon||_1
       <= C epsilon N^3 sum_(r=1)^(N-1) r/(r^2+epsilon N^2)
       <= C N^3 epsilon log(e/epsilon).             (10)

Indeed the shells r<=M contribute at most
M^(-2) sum_(r<=M) r<=C to the last sum; the shells r>M contribute
at most sum_(M<r<N)1/r<=C+log(N/M). Empty ranges contribute zero.
Fixed constants in the eigenvalue lower bound only alter C. Thus
small modes, including the lowest transverse modes, are not omitted.
Similarly, using the already established full trace bound Tr Delta^-1
<=C N^3 from L095,

    ||D B_epsilon D^*||_1
       =Tr_Q[epsilon/(Delta+epsilon)]
       <=epsilon Tr Delta^-1<=C N^3 epsilon.         (11)

Apply the finite Schatten trace-ideal inequality
|Tr(XY)|<=||X||_1||Y|| to each difference of (7) after its cyclic
reduction. The two inverse errors stay respectively in the first
factors D B_epsilon and D B_epsilon D^*; all remaining factors have
the bounds (8). Hence the per-level error is at most
C p(k)p(l)N^3 epsilon log(e/epsilon). Multiplying by a^2 s and
summing gives

    |T_(i,f,N)-U_(i,N;epsilon,0)|
                       <=C_i N^3 epsilon log(e/epsilon),       (12)

since a^2 sum_(s=1)^(N-1)s<=32. This is a finite estimate on the
original spaces, not substitution of a varying mass in L123's
fixed-mass limit. The gain over an undifferentiated inverse trace
comes from (9), with its logarithm retained.

### 3. Estimate the surviving projection errors in their original order

L242(13), including its complete pinned vertex shell proof, applies to
exactly P_delta defined here. The vertex space, d, and d^*d are the
same transverse relative spaces; exterior coefficients are irrelevant
to that spectral estimate. Thus

    J_delta=P-P_delta=Q_delta-Q,
    ||J_delta||_HS<=C N^(3/2)delta^(3/4),
                                        N sqrt(delta)>=1.     (13)

Both P_delta and Q_delta are contractions. We import this shell result
without reproof; L242's differently ordered reverse-response estimate
is not imported.

The factors adjacent to R_epsilon have uniform Hilbert--Schmidt bounds:

    ||D R_epsilon||_HS^2
       =Tr_Q[Delta/(Delta+epsilon)^2]
       <=Tr Delta^-1<=C N^3,
    ||D R_epsilon D^*||_op<=1,
    ||D R_epsilon D^*||_HS<=C N^(3/2).              (14)

The second assertion uses its nonzero eigenvalues
lambda/(lambda+epsilon); the last then uses dim F<=C N^3.
These bounds are uniform down to epsilon=0. They use all covariance
inputs and outputs. No rough column is assigned smoothness.

In the first trace of (3) only P changes. Its error is bounded, in
the displayed order, by

    ||D R_epsilon||_HS ||Cbar_l|| ||J_delta||_HS
                              ||Fbar_k|| ||D|| ||H_s||
                    <=C p(k)p(l) N^3 delta^(3/4).    (15)

This is Hilbert--Schmidt duality followed by operator-norm bounds;
no coefficient is moved across J_delta. In the second trace use the
exact telescoping

    P Cbar_k Q-P_delta Cbar_k Q_delta
       =J_delta Cbar_k Q-P_delta Cbar_k J_delta.     (16)

Each term in (16), after the unchanged left factors
D R_epsilon D^* Fbar_l^* and right H_s are restored, is bounded
by (13)--(14) and (8) by the same right side of (15). The two
placements need not cancel, and neither is dropped. Sum all levels
and heat labels as in (12) to obtain

    |U_(i,N;epsilon,0)-U_(i,N;epsilon,delta)|
                                <=C_i N^3 delta^(3/4).        (17)

Equations (12) and (17) prove (4). This comparison uses the differentiated
inverse's full Hilbert--Schmidt norm instead of an epsilon^-1 inverse
operator bound. The mass and projection estimates are independent
finite inequalities before a schedule is chosen.

### 4. Compare with the original remainder and state the remaining test

At epsilon_N=N^(-1/2), delta_N=N^(-2/3), both shell hypotheses hold,
and (4) costs at most C_i N^(5/2)log(eN). L272(4) already includes
the complete f,f contribution, both axial endpoint deficits and its
two-level replacement error once. Adding that O(N^2 log(eN)) bound
proves (5). It is not added separately for either orientation.

Every estimate has the polynomial mode envelope (8), so both original
finite heat sums are retained throughout. No continuum heat matrix,
omitted continuum label or raw interior approximation is used in
(4)--(5). Those are obligations for the subsequent comparison with
exactly L123(2). In particular all original finite projections are
retained through their explicit errors, while every normal end row
and every relative inverse source remains in (3).

For normalization, (3) still satisfies a^3 a^2 s=a^4(as), as does
L272(14). Rectangular cyclicity does not alter the spatial counting
or physical lower-distance weight. The unchanged complete target is
therefore reduced, within its error budget, to the same target for
U_(i,N;epsilon_N,delta_N). Neither a fixed-mass limit nor sublinear
inverse square-root scales prove that last estimate. ATTEMPTS/030's
unsupported varying-mass limit and ATTEMPTS/032's separate absolute
kernel moments have not been used.

This is RESEARCH / REPRODUCTION under the unchanged invocation-start
EXPLORE assessment
`drafts/literature/2026-10-24-exterior-circulation-quantitative-remainder.md`.
The contribution is a local ordered specialization of finite cochain,
spectral-shell and Schatten estimates, not a claim of source-level
novelty or a complete solution. At production the comparison required
a separate critical audit; section 5 now supplies it, retaining all
upstream qualifications.

### 5. Separate critical audit, 2026-10-24

**Verdict:** accept the exact equality in (3), the uniform estimate (4)
and the conditional original-response comparison (5), relative to the
stated imported inputs. This is a RESEARCH / REPRODUCTION proof audit
under the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-24-exterior-circulation-static-regularization-critical-audit.md`.
It does not independently audit L272's axial reduction or prove any
interacting or continuum statement. No numerical or IEEE premise enters
this comparison. The named general inputs are finite-dimensional
self-adjoint spectral calculus, singular-value calculus, rectangular
trace cyclicity and Schatten Holder inequalities; the following checks
verify their particular application rather than reprove those theorems.

**Domains and exact order.** Write V for the pinned transverse vertex
space. Then d:V->E, D:E->F, Cbar_k:E->E, Fbar_k:F->E and H_s:F->E.
The definitions of Cbar and Fbar come directly from L110's unprojected
path matrices; H_s is precisely L111(1)'s relative restriction. Thus
both beta and alpha act on E and both words of (3) act on F. L242's
T is this same d, with Delta_0=d^*d, so its projection estimate is on
the required space, not on a substituted scalar edge domain.

In L272(3), beta_l^* alpha_k equals
Q Cbar_l^* P Fbar_k D, and alpha_l^* beta_k equals
D^* Fbar_l^* P Cbar_k Q. These follow from P^2=P, QD^*=D^*
and DQ=D, without any coefficient commutation. Multiplication by
R_epsilon Q on the left and H_s D on the right gives exactly (7).
Rectangular cyclicity moves the last D to the front, and
D R_epsilon Q=D R_epsilon removes just the adjacent Q. This checks
each orientation separately, including its adjoint and sign. Cbar's
skew symmetry is not used to cancel or identify the two orientations.
Regularization occurs only after this reduction; P_delta and Q_delta
are never used as projections in the algebra.

**Mass errors and full spectral count.** On im Q, D^*D=Delta;
on im P, D=0. For B=R_0-R_epsilon, the positive operator
(DB)^*(DB)=B Delta Q B therefore gives (9), including multiplicity.
The nonzero spectrum of D B D^* is epsilon/(lambda+epsilon) on
im D, with zero on its orthogonal complement in F. This justifies
using trace norms for these factors without any positivity assumption
on the complete words or their heat coefficients.

L095 section 4 gives, component by component, one own-direction
index in {0,...,N-1} and two indices in {1,...,N-1}. Hence there is
no edge zero eigenvalue. With r the maximum of the three indices,
the full multiplicity is at most C r^2 and lambda>=c r^2/N^2.
Inserting this lower bound into the decreasing multiplier (9) gives
C epsilon N^3 sum_{r=1}^{N-1} r/(r^2+epsilon N^2), as claimed.
The low shells through M=N sqrt(epsilon) have a bounded sum; the
high shells have sum at most C+log(N/M). This includes M=1, M=N
and empty ranges, and proves (10) uniformly on the stated domain.
For the second word, epsilon/(lambda+epsilon)<=epsilon/lambda
and the full inverse trace in L095 prove (11). The other factors
are bounded by (8) on every row. Trace-norm/operator-norm duality
therefore applies to the two rectangular or square products with
exactly the respective costs (10) and (11).

**All three projection placements.** L242(13) and its isometry
argument identify the nonzero singular values of J_delta as
delta/(lambda_v+delta) for the pinned vertex modes with all three
indices positive. This is distinct from the edge spectrum above.
Its hypotheses hold here and supply (13) with no covariance mass
dependence. P_delta has eigenvalues lambda_v/(lambda_v+delta)
on im d and zero on its complement, so both P_delta and Q_delta
are contractions. No idempotence is needed.

Put X=D R_epsilon:E->F and Z=D R_epsilon D^*:F->F. Their bounds
are ||X||_HS<=C N^(3/2) and ||Z||_HS<=C N^(3/2), uniformly in
epsilon, by (14). The first projection error is paired as

    Tr_F[X Y_1],  Y_1=Cbar_l^* J_delta Fbar_k D H_s:F->E.

The two errors in the second word are paired as Tr_F[Z Y_2] and
-Tr_F[Z Y_3], where

    Y_2=Fbar_l^* J_delta Cbar_k Q H_s,
    Y_3=Fbar_l^* P_delta Cbar_k J_delta H_s.

Both Y_2 and Y_3 act on F. Each Y_j has Hilbert--Schmidt norm at
most C p(k)p(l)||J_delta||_HS by the bounded factors (8).
Rectangular Hilbert--Schmidt duality for Y_1 and ordinary duality
for Y_2,Y_3 give (15)--(17) in exactly their original orders.
In particular no inverse operator norm, lost epsilon power,
coefficient/projection commutation or unproved cancellation enters.

**Complete response budget.** L088(5) bounds the unprojected
f_k/a^2, b_k/a and q_k/a globally on existing transverse rows;
bounded multiplicity of L110's paths proves (8). L111's complete
filtered generator supplies the uniform H_s bound. These statements
include normal end rows, all interior axial levels and both actual
probe heat matrices. Every spectral norm above includes all sources
and outputs. Finally

    a^2 sum_{s=1}^{N-1} s=32(1-1/N)<=32,

and the absolute polynomial heat envelope in (8) sums all mode pairs.
This verifies the full N^3 allowance in (4), without a hidden axial
factor or a cutoff on heat labels.

At epsilon=N^(-1/2), delta=N^(-2/3), the shell conditions read
N sqrt(epsilon)=N^(3/4)>=1 and N sqrt(delta)=N^(2/3)>=1.
The two allowances are respectively O(N^(5/2)log(eN)) and
O(N^(5/2)). Adding the single combined L272(4) allowance
O(N^2 log(eN)) proves (5). Its f,f and two endpoint contributions
are not added again. The weight remains a^3 a^2 s=a^4(as), and
no outside factor 3, orientation half or changed heat normalization
is introduced. All inequalities precede this schedule, so neither
ATTEMPTS/030's varying-mass qualitative limit nor ATTEMPTS/032's
separate absolute kernel moment is used.

No failed identity or budget was found within this audit scope.
This clears only L273's application of its imported premises.
It does not certify L272, the other upstream inputs, a complete
transverse-H/L011 assembly, or the Yang--Mills construction.

## Mathlib

Full matching pinned exterior-circulation mass/projection comparison:
**not checked**. Supporting finite Hodge identities, singular-value
calculus, rectangular trace cyclicity, Schatten Holder and spectral
shell estimates: **not checked**. Unknown availability is not absence.
No formal verification, continuum Ward theorem or positive-flow-time
finiteness theorem supplies the remaining ordered trace rate.
