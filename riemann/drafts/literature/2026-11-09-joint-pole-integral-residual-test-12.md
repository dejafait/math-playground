# Coupled pole-part integral residual: nomination for separate approval

TARGET: Test a cancellation-preserving pole-part integral representation of L929's combined operator at N=floor(T^(1/5)), charging the regular-zeta residual in both exact energy metrics and retaining the Hardy phase.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed bounded source comparison in drafts/literature/2026-11-09-joint-combined-operator-coverage-11.md, step12, including the exact complex-Jordan/divided-difference queries, primary statements and failure comparisons. No matching contraction theorem identified; no novelty claim.
SOURCE_EVIDENCE: de Boor arXiv:math/0502036v1 Section9 pp63-64 https://arxiv.org/pdf/math/0502036v1; Mattila v2 Proposition2.5 https://arxiv.org/pdf/1403.5907v2; Bhatia Propositions1.3.1-2/Theorem1.3.3 pp13-14 https://assets.press.princeton.edu/chapters/s8445.pdf; DLMF25.2(i),(4) https://dlmf.nist.gov/25.2#E4; audited L928 moment imports and their existing source comparison.
COMPARISON: Known finite calculus and incidence tools preserve paired endpoints before taking norms, but give neither their specific integral representation in the full energy metrics nor a uniform strict bound. The stopped termwise-modulus Schur certificate is not the proposed test.
GAP: Verify the finite pole-part integral and its endpoints directly against L928/L929, then bound ||B_pole|| and ||B-B_pole|| uniformly with their sum <=1-eta for fixed eta>0, or exhibit a quantitative residual loss stopping this selected estimate. No such identity or estimate is established here.
REASON: This nomination specifies one bounded application of inspected tools after the completed source comparison; it requires separate approval next turn before research invocation. No new mathematics was derived or approved in step12.
SCOPE: Fixed L928 w,Z, shifts +/-1/log T, T<=X<=2T, N=floor(T^(1/5)), arbitrary moving complex coefficient pairs, complete H_-,H_+ and exact Hardy phase. No longer dictionary, numerical grid, moment-remainder limit through zero-sum shifts, signed transfer or RH claim.

## Source-backed scope, still pending separate approval

This is a newly written nomination. Its EXPLORE decision records adequate
source tools for a possible bounded attempt, not approval to invoke that
attempt in step12. The supervisor's separate approval remains due.
Reuse the primary reads and qualifications in the completed comparison;
repeat browsing only for an identified essential omission.

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
This intermediate target concerns only L928(11)'s joint contraction and
could support a later fixed-bump joint projection decision. Even success
leaves signed realization, transfer and all Xi signs unresolved. It is
established-route development, not a central creative Xi-sign mechanism.

Use audited L928 as the established arithmetic interface, L737's finite
identities and step261 audit, L637's phase/normalization, and audited
L926/L927 for the existing downstream error scale. Read the relevant
canonical proofs when applying them. L929 is an unaudited proposed
coordinate expression: verify the endpoints used, including its
transpose versus adjoint, against L928 before using that expression.
L925 and cross-notebook inputs are excluded.

## Exact proposed finite operators and bounded test

The following are target definitions only, not identities newly proved
or norm estimates. Use L929(6),(8)'s W_+,W_-,H_-,H_+,ell_t,epsilon_t,
with L=log T. For this test define beta_pole,+ and beta_pole,- by keeping
the exact time integrals in beta_+ and beta_- and replacing only
zeta(1+2i/L) by L/(2i) and zeta(1-2i/L) by -L/(2i), respectively.
Define

    V_pole=beta_pole,+ W_+ + beta_pole,- W_-,
    B_pole=H_-^(-1/2) V_pole H_+^(-1/2),
    R_reg=B-B_pole.

The sought coefficient-uniform sufficient certificate is

    ||B_pole|| + ||R_reg|| <= 1-eta, eta>0 fixed,

uniformly eventually in T and X. This is the proposed norm test, not an
achieved inequality. Both pole summands must stay combined before any
norm or positive majorant is taken. The error term R_reg must be charged
as a full operator in the same metrics, even though its scalar zeta
coefficients are regular. No entrywise smallness suffices automatically.

Import the first-divided-difference integral from de Boor, rather than
reprove general calculus. Seek a finite holomorphic endpoint family
whose pole-part divided difference reproduces this V_pole, using the
complex incidence identity parameterwise. Specify the family and its
analytic domain, verify all endpoint factors and normalization constants,
and retain the exact w_XT and exp(i epsilon_t). If integration by parts
is used, display every boundary term. Keep finite-sum/differentiation
operations justified; do not invoke a shifted-moment remainder at an
uncovered collision limit. No such endpoint family has been constructed
in step12. Complex Jordan factors need not be positive or Hermitian.

For the bounded attempt, report actual bounds for the two displayed
norms and the required sum threshold. A quantitative bound that fails
may be informative; a mere coordinate identity is not a mathematical
advance. A weaker margin may justify continuing only after comparison
with L928(3)-(5)'s O(T^(-9/80)/log T) relative error. No such comparison
has been obtained here. If the chosen estimates consume the available
pole-part margin, stop this selected integral-norm estimate; reopening
requires a materially different estimate or new input, not more weights,
samples or relabeling. The already recorded termwise-modulus Schur,
step226 and approval-loop stops stay in force for their stated scopes.

This test may fail without invalidating joint contraction. It is not a
reviewed proof of L929, a theorem import of the desired gap, a joint
projection result or an RH candidate. Full matching Mathlib coverage is
unknown; standard supporting facts are not a matching formal theorem.
