# Ready continuation: integer density and the L735 coefficient

TARGET: Determine whether L735's coefficient-1 psi asymptotic can coexist with N_P(x)=kappa x+O(x^theta), kappa>0 and 0<=theta<3/4, by specializing the inspected Mellin and zero-order inputs with all formal multiplicities.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 254 completed the coefficient/zero-multiplicity and Axiom-A search recorded in 2026-11-04-beurling-integer-density-coefficient-scope.md; reuse its three inspected primary chains without a repeated search.
SOURCE_EVIDENCE: https://arxiv.org/pdf/2202.01837v3 Section 1 (1)–(7), endpoint footnote, Section 7 pp. 17–18 (52)–(54); https://arxiv.org/pdf/2110.11463v1 Definition 1.1 and Lemma 2.1 (2.2),(2.4), complete proof pp. 4–5 (retrieved PDF bears v2 footer); https://dlmf.nist.gov/1.10 sections (i),(ii),(iv), especially https://dlmf.nist.gov/1.10.E9. Direct sources reopened in step 255; detailed evidence and version qualification retained in the completed source assessment.
COMPARISON: Standard continuation, Mellin and integer-order inputs suffice for an elementary local specialization, but no exact matching coefficient-1 necessity theorem was located. The prescribed-zero existence theorem cannot replace that specialization.
GAP: The combined compatibility verdict, analytic remainder justification, endpoint terms, common domain and theta=0 case remain unproved. No residue value for L735 is assumed as an input.
REASON: Test the additional integer-counting structure missing from the audited countermodel using existing analytic inputs; citing a different construction does not settle compatibility for this one system.
SCOPE: Fixed b=3/4 and L735's O(sqrt(x)log x) error only, for one locally finite free-semigroup system counting formal integers with multiplicity and including the unit. Separate scope approval completed in literature-only step 255; mathematical execution remains deferred to the next invocation.

Full source statements, read ranges, queries, version qualification and
limitations are in the [completed assessment](2026-11-04-beurling-integer-density-coefficient-scope.md).
This file scopes the continuation; it supplies no new proof.

Essential local input: audited L735. The N_P estimate is hypothetical,
with fixed kappa and theta, and is never asserted for the construction.
The specialization must retain compact endpoints and all formal
multiplicities; match N-kappa x with the source's N-kappa(x-1)
convention and its positive exponent when theta=0. Establish convergence
and local analyticity of the transformed remainder before using
uniqueness or the logarithmic derivative. Check the same zeta function
is being continued from the Euler-product half-plane. Compare local
residue/order only after these steps, without a branch-valued zeta
substitution or an assumed fractional multiplicity.

Continue if these checks give a definite compatibility verdict. If a
necessary hypothesis or analytic domain is unavailable, record the
precise failure and stop this specialization; do not broaden to other
coefficients or powers. No reproof of discretization, numerical script
or global explicit formula is needed. This is REPRODUCTION, not a
creative central sign mechanism. Mathlib coverage of the combined
statement is unchecked; full matching coverage is not claimed.

The downstream use is limited to identifying arithmetic structure that
the coarse countermodel omits. Ordinary-prime upper prefix norms,
actual-Xi sign transfer and complementary residual control remain
independent gaps. Even a negative compatibility verdict would not
exclude arbitrary zeros or resolve RH. Preserve L734/L639 and the
coarse self-generated-kernel stop at their existing scopes.

## Direct-source recovery and scope approval — step 255

LITERATURE_REASON: Supervisor recovery reported missing direct source URLs in this ready assessment; repair its own source field and check the saved scope, reusing step 254 rather than repeating discovery.

On 2026-11-04 the three direct URLs above were reopened. Checked the
Axiom A definition and endpoint footnote, Lemma 2.1 statement and
integration-by-parts proof, the Section 7 Mellin paragraph and
(52)–(54), and DLMF zero order, continuation and argument principle.
The requested-v1 URL again served the 29-page manuscript with a v2
footer; that qualification remains mandatory. The Section 7 rational
factorization belongs to its prescribed multiset construction and is
not an identity available for L735.

The saved target remains SPECIALIZE, approved for one later mathematical
attempt. The source exponent is strictly positive; theta=0 is still an
application obligation, not a case already settled by this review.
Likewise compact endpoint corrections, analyticity of the error transform
and agreement with the same Euler-product zeta remain proof obligations.
No coefficient residue or compatibility verdict has been derived.

The duplicate/failure check reused the completed assessment's comparison,
L735's exact statement and qualifications, its step-253 audit assessment,
and ATTEMPTS/2026-11-04-self-generated-coarse-kernel-discrimination-stop.md.
That stop does not decide the added integer-count hypothesis. L734/L639
are retained at their existing scopes. Mathlib matching coverage remains
unchecked; no reproof of discretization or source theorem is authorized.

This is a process repair and approval, honestly STALLED as mathematics: no
new source theorem, changed obstruction or mathematical conclusion. The
main gap, bounded continuation test and downstream limits stated above
are unchanged. No mathematical exploration budget is spent or renewed.
