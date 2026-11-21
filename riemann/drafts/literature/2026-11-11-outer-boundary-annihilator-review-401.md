# Nomination: an outer boundary annihilator for the capped sufficient objective

TARGET: Test a step-modulus outer Hardy annihilator on the fixed upper-window arc for an all-polynomial obstruction to C997s's capped two-window Delta_n=O(exp(-n/64)) sufficient objective.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step401's completed bounded searches in review400 for constrained arc approximation, outer-function lower certificates and coefficient-constrained superoscillations, including the local duplicate/failure check. No matching quantitative theorem was identified; no originality is inferred.
SOURCE_EVIDENCE: L. Baratchart, J. Leblond, F. Seyfert, Constrained L2-approximation by polynomials on subsets of the circle, author manuscript22 March2017, https://www-sop.inria.fr/members/Juliette.Leblond/Papiers/BLSFields2017.pdf , Section3 equations(2)-(7), printed pp2-4, and Theorem1 indicator perturbation(15), printed p6, directly retrieved and checked in step402; reuse review400 for Theorems2-3/proofs; its Hardy Cauchy and outer-function contracts are the prospective tools. Reuse C997c(4)-(6), C997s Hypotheses and review390's already inspected DLMF2.4(iii)-(iv) contour-hypothesis comparison. No general asymptotic theorem pays the proposed target pairing.
COMPARISON: This is a circle-boundary dual acting on arbitrary capped polynomials, with complementary-circle leakage charged directly. It is neither a prescribed-jet interpolant, an exact moment representer, a scalar slope-continuation prior nor a singular-value cutoff. The known fixed-data constrained approximation theorem does not determine its growing-n score.
GAP: The specialized bilinear annihilation identity, fully paid leakage inequality, complex target-pairing lower bound and asymptotic comparison remain unproved. The outer boundary limits need not be continuous at arc endpoints. A favorable absolute upper bound on an oscillatory integral is not a noncancelling lower bound.
REASON: Step402 separately approves tool coverage after direct primary-source retrieval and URL repair; the exact target, family and scope are unchanged. Step401 only nominated it; neither turn performs the attempt or establishes its score. EXPLORE is coverage for a test, not a theorem claim.
LITERATURE_REASON: Supervisor recovery requires a direct source URL in this ready assessment; verify that essential Hardy tools are accessible and repair their citation, reusing review400 rather than repeating discovery.
SCOPE: Original integer n>=64, z_star=1+i/8, gamma grid and complex coefficient cap of C997s; only review400's stronger sufficient Delta_n objective. One fixed-arc outer family with the parameter box below. No new polynomial upper construction, integrated E_n lower bound or actual-Xi statement is covered.

## Gap, purpose and proposed family

The main gap remains actual-Xi positivity L030-L032/C032a, signed
forcing L966/L968 and unpaid L984(H). The intermediate question is
whether the original coefficient cap allows review400's complete
two-window sufficient upper certificate. A universal obstruction to
that stronger objective would direct work toward genuinely integrated
cancellation or a different bridge. It would not resolve capped E_n.

The following definitions specify prospective work, not an established
identity, rate or lower certificate. Use normalized circle measure
dtheta/(2pi), and fix

    A={exp(i theta): 7/16<theta<9/16}, J=T\A,
    H_J(y)=(1/(2pi))*integral_J (exp(i theta)+y)
                                  /(exp(i theta)-y) dtheta, |y|<1.

Consider only

    h_n(y)=y^(1+floor(eta*n))*exp(-lambda*n*H_J(y)),
    lambda,eta fixed rational, 1/8<=lambda<=1/2, 0<=eta<=4.

Choose at most one parameter pair for a fully paid analytic attempt;
there is no instruction to run a numerical sweep or assume a favorable
pair exists. The family uses a boundary test rather than requiring the
approximating polynomial to match high derivatives. The choice of an
open fixed arc is for Hardy boundary integrals. The original residual
still has closed-window suprema and the original endpoints.

For its prospective nontangential boundary function h_n^*, define

    F_n(theta)=exp(4*n*i*(z_star-15/8)*theta),
    P_n=(1/(2pi))*integral_A F_n(theta)*h_n^*(exp(i theta)) dtheta,
    M_A=(1/(2pi))*integral_A |h_n^*| dtheta,
    M_J=(1/(2pi))*integral_J |h_n^*| dtheta.

Do not conjugate the bilinear test without adjusting the annihilation
identity. Verify its zero mean against every analytic polynomial using
the cited Hardy Cauchy formula; verify the boundary integrability and
M_A>0. Then establish, if valid, the prospective lower certificate

    sup_(7/16<=theta<=9/16)
        |F_n(theta)-p_n(exp(i theta))|
             >= (|P_n|-B_n*M_J)/M_A =: S_n,
    B_n=exp(sqrt(n)).

This displayed inequality is a target to prove, not a result of the
literature turn. The conversion from the original coefficient cap to
the circle bound must be explicit, with no reverse norm equivalence.
All complex signs and the normalizations of circle measure must be
checked. Source formulas are to be imported by citation; only this
kernel-specific dual specialization and its quantitative test need work.

## Decisive comparison and stopping rule

Use exactly C997c(5)'s T_U from review400, including its n-dependent
factor. An obstruction would follow only after proving a positive
certificate whose T_U*S_n*exp(n/64) is unbounded along an unbounded
integer sequence, with every error and leakage term included. This
would exclude every capped polynomial meeting the stated simultaneous
Delta_n big-O objective, whose uniform constant is unspecified.
Neither a finite-degree violation nor one failed approximant suffices.

The difficult part is a lower bound on |P_n| after its oscillatory
phase and endpoint singularities are paid. No formal saddle estimate,
pointwise size, absolute envelope or stationary point alone is evidence
of that bound. Any contour deformation must satisfy the already
inspected analytic-domain, endpoint and remainder hypotheses. If the
chosen family cannot discriminate the required rate in one coherent
attempt, record the exact failure or unresolved inequality and park it;
do not infer that all Hardy duals or the sufficient objective fail.

The fixed arc tests a necessary part of the upper-window bound and is
not a replacement for two-window control in an upper construction.
Even a universal obstruction here would leave open cancellation in
the original integrated residual. Essential local mathematical inputs
are C997c(4)-(6) and C997s's original cap/grid/kernel; C997x/y/z are
scope comparisons only. C997a(8), selected/both-sign transfer,
assay/reconstruction, complements/regulators, L993, L984(H), L966/L968
forcing and actual-Xi positivity remain unresolved. No cross-notebook
input is proposed. Full matching Mathlib coverage is unknown/unchecked.

The proposed purpose is proof_attempt/creative: construct and test a
new boundary dual at the capped bridge, rather than reproduce the known
fixed-data extremal theorem. Its escalation is the noncancelling
target-action versus paid complementary leakage comparison above.
No mathematical result or candidate RH solution is asserted.

## Separate source approval — step402, 11 November 2026

Retrieved the author-hosted manuscript linked in SOURCE_EVIDENCE.
Section3, printed pp2-4, specifies normalized circle measure, Hardy
nontangential limits and Lp radial convergence for finite p, and the
Cauchy formula (3). For real L1 boundary data, (5) gives a holomorphic
Riesz–Herglotz transform with the stated almost-everywhere boundary real
part. Equations (7) and its continuation on p4 require positive rho,
log(rho) in L1; the outer function has boundary modulus rho, and belongs
to Hp exactly when rho belongs to Lp. Theorem1's proof, (15), p6,
explicitly uses the transform of an indicator and its exponential.
These are the imported tool statements; no reproof is needed.

The source hypotheses admit discontinuous boundary data; continuity at
arc endpoints is not promised. Its Cauchy line integral and its
sesquilinear pairing must not be confused with the proposed bilinear
dtheta pairing. Verification for h_n, products with polynomials,
vanishing mean, leakage and the target action remains future work.
No local specialization or quantitative estimate is established here.

Reused review400's bounded discovery and duplicate/failure comparison;
targeted local searches in the dated capped/band records revealed no
reason to change that comparison. Read C997c(4)-(6) and C997s's original
hypotheses to confirm the unchanged input scope. The fixed-data extremal
convergence result remains insufficient for the proposed coupled rate.
No new asymptotic source is necessary to attempt this bounded family;
any later use of an additional theorem outside this scope needs review.

Decision remains EXPLORE, now separately source-approved for the exact
TARGET. This is a process repair, reported STALLED, with no mathematical
advance or exploration-counter reset. Full matching Mathlib coverage
remains unchecked. PROOF.md and DAG.md do not change.
