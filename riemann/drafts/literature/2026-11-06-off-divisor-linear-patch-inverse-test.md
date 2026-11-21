# Off-divisor linear patch inverse — prepared continuation

TARGET: Test a quantitative supported right-inverse criterion for L850's phase linearization on compact off-divisor graph patches, retaining explicit ellipticity, boundary and adjoint-kernel conditions.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed full-phase-elliptic-deformation-scope comparison and the earlier collar-preserving-linear-phase comparison; exact operator identities were checked against L850 and residual limitations against L851-L853. No new search or novelty claim is needed for this restricted specialization.
SOURCE_EVIDENCE: Delay 1003.0535v4 Definitions1.1-1.2/Theorem1.3, Proposition3.6/Theorem3.8, Section4/Theorem5.1 and Section8/9.1 were inspected this turn; Teixeira 1608.06213v7 Theorem3/Remark3 and proofs were previously inspected in the reused collar assessment. Precise citations and qualifications are recorded below and in the parent comparison.
COMPARISON: Supported ordinary divergence and conditional underdetermined-elliptic solvability are known. L850 already computes the actual coefficient matrix and its determinant. The only intended work is the actual patch specialization: symbol, adjoint compatibility, coefficient regularity and a bound displaying its matrix-inverse and domain dependence, or a scoped obstruction.
GAP: No such controlled patch application is recorded locally. Off F=0 does not itself supply an ellipticity lower bound. No uniform inverse at det M=0, singular global lift, nonlinear correction, actual seed, global sign or RH conclusion is covered.
REASON: Prepare one bounded mathematical feasibility test of the changed equality method using ready linear sources. This newly written ready continuation requires separate next-turn approval; this assessment performs no mathematical test.
SCOPE: Actual L847 G,R,C,F and real smooth graph u, on the closure of a bounded connected smooth coordinate patch disjoint from F(Phi_u)=0; retain the full density and L850 first variation. Test rather than assume symbol surjectivity. A conditional positive result may impose uniform matrix invertibility up to the patch boundary and regularity bounds. Sources to be corrected must have specified boundary-collar support; all compatibility and regularity hypotheses must be stated. No global graph, exchange-preserving extension or nonlinear existence theorem is included.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
A controlled patch inverse could later support correction of a specified
approximate contour. It does not supply that contour, compatibility between
patches, correction convergence, extension through the divisor, fixed-order
nonnegativity or all-degree signs. No such downstream step is assumed.

Use the identities already recorded in L850, after checking their signs in
its (2)-(5) proof. Do not present the matrix or its determinant formula as
a new result. L851's exterior lift and residual strips, L852's forced
transition zeros, and L853's finite jets retain their original scopes;
this target does not solve the singular global range problem they leave.

For the standard linear input, cite Pedro Teixeira, *Dacorogna-Moser theorem
on the Jacobian determinant equation with control of support*, DCDS37
(2017), 4071-4089, DOI10.3934/dcds.2017173,
[arXiv:1608.06213v7, Section4 Theorem3/Remark3 and proofs, pp8-10](https://arxiv.org/pdf/1608.06213v7#page=8).
For integer r>=0 and 0<alpha<1, on a bounded connected smooth domain in
R^n, n>=2, C^(r,alpha) signed data of zero integral, zero on a prescribed
boundary collar, have a bounded linear C^(r+1,alpha) divergence preimage
zero on that collar. Constants depend on the domain, collar and regularity.
The operator is independent of regularity indices and preserves smooth data.
The source hypotheses, coordinate orientation, allowed variations and all
matrix lifting estimates remain application obligations. Do not reprove
the divergence theorem or silently claim uniform constants.

The broader reference is Erwann Delay, *Smooth compactly supported solutions
of some underdetermined elliptic PDE, with gluing applications*,
[arXiv:1003.0535v4, 17 November 2011, pp2,7-10,12-14](https://arxiv.org/pdf/1003.0535v4).
The actual symbol must be surjective for each nonzero real covector; API,
KRC and orthogonality to the entire adjoint kernel are additional hypotheses,
as specified in Definitions1.1-1.2 and Theorems1.3/5.1. The weighted
coercivity/isomorphism and boundary-flat extension are detailed in the
[completed parent comparison](2026-11-06-full-phase-elliptic-deformation-scope.md).
Its Section9.6 is not a general nonlinear theorem. McLean/Hamilton/Hintz
unread leads are not needed for the linear application and cannot be used
as theorem evidence. Full matching Mathlib coverage remains unchecked.

Continue only if the patch test yields a supported real right inverse with
a stated norm and complete compatibility, or an explicit scoped failure
of ellipticity/compatibility. Compare any achieved bound with the required
positive lower singular-value bound and stated coefficient norms. If all
conclusions duplicate L850 or ordinary divergence without a controlled
application, record no mathematical advance and reassess this mechanism.
Do not extrapolate a conditional patch result to a seed, to prescribed
annular gluing or to a divisor-uniform estimate. No numerical script is
needed. No new theorem was derived or invoked in preparing this assessment.

Proposed routing is calculation, standard/high: the task specializes a
known first-order operator and a ready support-preserving divergence theorem.
It is not a creative construction at the central gap. A creative route is
still blocked by the missing global seed and singular/global inverse control.
