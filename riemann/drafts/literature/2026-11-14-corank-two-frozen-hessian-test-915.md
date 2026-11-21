# Frozen Hessian at a corank-two contact: bounded test coverage

TARGET: Test the frozen determinant-Hessian weight W(t)=d^2det_(A_*)[A_*',A_m(x_*-t)] at the stated corank-two contact for nonvanishing and a signed Volterra balance, recording any necessary extra jet condition.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed comparison915 in assessment914 searched higher determinant differentials, corank-two Hankel/Volterra contractions and simultaneous-zero theorems; no matching actual signed-weight result or local duplicate was found. No originality claim.
SOURCE_EVIDENCE: Bhatia--Jain (2009), Theorems1-4, Section2/Remarks2-3, https://www.academia.edu/7491948/Higher_order_derivatives_and_perturbation_bounds_for_determinants ; Gallier (2019), Section1 p2, https://www.cis.upenn.edu/~jean/schur-comp.pdf ; both relevant statements/proof cases rechecked in916. Reuse assessment886/887 scalar-law/convolution coverage for audited C466b and comparison915 exclusions.
COMPARISON: Polynomial second differentials and a size-(m-2) Schur reduction are known tools valid at singular matrices. They do not decide this frozen weight's nonvanishing or sign on the actual density curve; testing that distinction is a bounded specialization, not a new general higher-adjugate theorem.
GAP: Exact endpoint values and orders, the frozen-weight Volterra identity, nonvanishing on the Hankel curve, parity-correct signed quantity and any necessary extra finite-jet premise remain to be established. An actual contact and any such extra premise are unproved.
REASON: Recovery916 supplies direct source URLs and completes separate literature approval for the unchanged bounded diagnostic; no further browsing is essential for this fixed scope. Do not substitute a new higher-order observable if this one fails.
SCOPE: C466a/b actual smooth flat-at-zero p and actual C^1 positive decreasing integrable H, inherited L018 normalization and cited external qualifications; one finite m>=3 and x_*>0 with D_j>0 for j<=m-2, D_(m-1)=D_m=0, rank A_m=m-2. First-contact interpretation additionally has both determinants positive immediately left. No higher PF, finite-order contact, nonflatness, analytic determinant continuation or size-(m-1) inverse.

The main gap is L030-L032/C032a actual-Xi positivity at all degrees.
This diagnostic could supply a local observable for the simultaneous-contact
part of a later barrier, or reveal an additional necessary jet assumption.
It cannot itself pay rank-one head/anchor/tail signs, strict forcing,
propagation, global all-degree bounds or Xi transfer.

Use A_*=A_m(x_*), A_*'=dA_m/dx at x_* and freeze both in
W(t)=d^2det_(A_*)[A_*',A_m(x_*-t)], 0<=t<=x_*.
Here d^2 is the bilinear Frechet differential, as defined by
Bhatia--Jain (2009) equation(5); use Theorems2/3 equations(8)/(13),
not a formula involving A_*^(-1). The second differential is a known
matrix-space object; its proposed use here has not been calculated.
A permissible auxiliary reduction uses the invertible leading block
of size m-2 and Gallier's factorization, never D_(m-1)^(-1).

Primary citation details and exact inspected proof cases are preserved in
[completed comparison915](2026-11-14-corank-two-volterra-nomination-914.md#completed-comparison915).
Bhatia--Jain's primary manuscript was read through its full mirrored text;
the institutional PDF endpoints failed. The zero/counting/density and
scalar-law imports are inherited, not independently recertified.
No extra essential source blocker remains for this conditional test.
No source establishes the target, and no new calculation occurred in915.

Test only this frozen functional using C466b's localized recurrences.
Explicitly pay every endpoint and improper integral before giving a
balance. Avoid placing further derivatives on H at its singular endpoint.
A nonzero ambient Hessian is not proof of a nonzero W. Do not drop
first-contact hypotheses when interpreting a derivative's direction.

Continue only with a nonzero W, a valid local balance and an independently
checkable signed quantity. If the weight vanishes, or an extra
nondegeneracy/sign premise is needed, record the precise condition and
whether it is known for actual p; that may be an informative negative.
Stop this chosen weight if it supplies only another unpaid sign criterion.
Do not silently advance to third differentials or an unrestricted search.
No generic jet witness may be reported as an actual-density contact.
Any established result must have full proof and citations in its canonical
lemma file, with the DAG changed only for genuine mathematical inputs.

Mathlib: supporting Matrix.det_fromBlocks₁₁ and
Matrix.fromBlocks_eq_of_invertible₁₁ statements were inspected in915;
full matching Hessian/Volterra coverage remains unchecked. See914 for
links and hypotheses. Separate literature approval was completed in recovery916 below. This
approves the unchanged bounded target for a subsequent research turn;
no mathematics was performed or retrospectively approved in916.

This is an established-tool proof_attempt/development, not creative work.
No justified central creative mechanism is currently ready: the existence
of a usable signed corank-two observable remains the precise blocker.


## Recovery916: direct source URLs and separate approval

The supervisor required direct source URLs in this ready assessment.
On 2026-11-14 the following primary texts were accessed; the target and
hypotheses above are unchanged. This is a citation/access repair, not
new mathematical evidence or a repetition of the failed sign import.

- Bhatia and Jain, *Higher order derivatives and perturbation bounds for
  determinants*, LAA431 (2009),2102-2108,
  [DOI](https://doi.org/10.1016/j.laa.2009.07.003).
  The DOI fetch returned403; the
  [authors' May18 2009 manuscript, isid/ms/2009/05, full mirror](https://www.academia.edu/7491948/Higher_order_derivatives_and_perturbation_bounds_for_determinants)
  was accessible. Rechecked definition(5), Theorems1-3, formulas(8)/(13),
  and Section2's coefficient, Laplace and exterior-power proof cases,
  manuscript pp2-6. These polynomial identities allow arbitrary complex
  square matrices, including singular ones, and 1<=k<=n. Rechecked
  Theorem4(18) and Remarks2-3: ambient norm information is distinct
  from evaluation on a prescribed curve; the positivity statement
  requires positive semidefinite base and directions. Those sign
  hypotheses are not established here. No application to W is made.
- Gallier, *The Schur Complement and Symmetric Positive Semidefinite
  (and Definite) Matrices*, August24 2019,
  [Section1, printed p2](https://www.cis.upenn.edu/~jean/schur-comp.pdf).
  Rechecked the factorization and its direct-multiplication justification,
  including the remark for an invertible top-left block. The full
  matrix and complementary block need not be invertible. The stated
  D_(m-2)>0 pays this sole inverse hypothesis; no positivity conclusion
  for the frozen functional is imported.

Scalar-law and endpoint-tool coverage remains the previously inspected
[assessment886, completed887](2026-11-14-volterra-contact-cancellation-audit-886.md#completion887-hypothesis-comparison-and-bounded-audit),
including its direct Steutel--van Harn, Sra v1 and Mathlib links and
access qualifications. No changed scalar hypothesis requires retrieval
again. Comparison915's duplicate/failure search remains applicable.
Matching Mathlib coverage of the full target remains unchecked.

Decision: EXPLORE retained; the exact TARGET is approved for one
subsequent mathematical diagnostic. Continue/stop tests, unresolved
actual-density assumptions and the prohibition on automatic escalation
remain as stated above. This repair supplies no result toward RH.
