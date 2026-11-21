# Exact reciprocal-minor specialization — next-target coverage

TARGET: Import the dual Jacobi-Trudi specialization relating L785's reciprocal determinant to L776's D_(3,2), checking every sign, power of c_0 and R, and singular cases.
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse step461's completed reciprocal-minor-duality-comparison.md, including its targeted duality searches, local duplicate/failure comparison and inspected primary proofs; no changed hypotheses or additional discovery claim.
SOURCE_EVIDENCE: Macdonald, Symmetric Functions and Hall Polynomials, second edition (1995), I.2 (2.6)-(2.9') pp.21-23 and I.3 (3.4)-(3.7') pp.41-42, https://djvu.online/file/evBrSjuw4lsEJ ; Böttcher-Widom, Szegő via Jacobi, math/0604009v1, Theorem2.1 p.3 and Corollary2.3 with proof p.4, https://arxiv.org/pdf/math/0604009v1 .
COMPARISON: Known duality and complementary minors supply the identity after a finite scalar specialization; no new inequality or source theorem reproof is needed. The normalization and local block orientation remain to be written out as the mathematical task.
GAP: Determine the exact local determinant relation with all constants and signs; no source gives an independent actual-Xi coefficient sign or root-grouping theorem.
REASON: One bounded cited application can decide whether the proposed residual determinant is just the existing unpaid minor and prevent circular sign research.
SCOPE: Real local ordinary series g(z)=sum c_j z^j with c_0>0 and 1/g(z)=sum u_j z^j; only the reciprocal Hankel block on u_2,u_3,u_4, the coefficient three-by-three block c_(2+j-i), and g(z)=G(Rz), R>0. No other degree, model search, new positivity bound, inertia theorem or Xi realization.

Essential local inputs are L785's block and congruence statement and
L776's ordinary-coefficient normalization of G and D_(3,2). Reuse the
completed source comparison for the exact theorem/proof cases and
singular-minor applicability. The finite generating-series substitution
must account for c_0 before comparing the dual rectangular partitions
(2,2,2) and (3,3); alternatively use a finite triangular coefficient
matrix whose inverse is justified by the local reciprocal convolution.
Use one imported identity, not two full reproofs. Explain the Hankel row
or column reversal, cofactor orientation, all powers of c_0 and R, and
why neither H nor its determinant must be invertible. Zero determinants
must remain included. No reciprocal convergence at either root is needed.

The discriminating test is an exact cited scalar identity or a precise
hypothesis mismatch. If it identifies the existing D_(3,2) condition,
stop the putative independent algebraic sign mechanism and preserve the
unpaid theta inequality. This does not decide full inertia from det H.
Any later actual-Xi use of L785 still requires its two simple negative
roots, sigma>1 and zero-free complement, as well as global/all-order and
other-minor transfer. Do not assume these, RH, a positive alphabet, or
unproved total positivity. Mathlib matching coverage remains unchecked.

This newly written ready continuation receives separate supervisor
approval next turn. It authorizes only a KNOWN_IMPORTED specialization
once admitted, not a new discovery. No mathematical calculation or new
lemma is supplied by this assessment.
