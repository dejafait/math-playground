# Bounded mixed five/eleven test — separate approval pending

TARGET: Test beta R=J^h Q^t for (h,t) in {1,2,3,4} x {1,2,3,4}, with Q=(5,k)R, after proving its exact prime extension and the conditional L045 specialization.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed mixed-prime comparison in 2026-10-12-mixed-five-eleven-power-order-certificate.md; the sixteen-product test is its fixed positive-certificate scope.
SOURCE_EVIDENCE: https://www.jmilne.org/math/CourseNotes/ANT.pdf v3.08 Corollary 3.13, Example 3.19, Theorem 3.20, Theorem 7.33/Remark 7.36 and Corollary 7.42; https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html Definition 1.3.19; https://crypto.stanford.edu/pbc/notes/commalg/extcon.html item 3; https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#mathnf flags 0,1; detailed inspected hypotheses/proof cases and reused LLL coverage in the companion comparison.
COMPARISON: Standard ideal and S-class methods justify a conditional positive certificate, subject to explicit applicability; neither the sources nor previous computations provide the mixed generator or an exhaustive generator bound.
GAP: Establish Q's exact extension using L038's two entire factors, justify the quotient consequence, construct sixteen exact product lattices and independently verify all candidates and any equality.
REASON: Independent individual prime-five freedom differs from the exhausted t=0 test; a fixed test is possible without certified maximal-order data or R-ideal inversion.
SCOPE: Fixed L033 field and power basis, J=(11,k-8)R and Q=(5,k)R; sixteen positive exponent pairs, at most 2,304 candidates; no search enlargement or negative class conclusion.

This newly written ready assessment requires separate supervisor approval
next turn. It contains no proof of a new field-specific result and no
mathematical execution.

Essential inputs: L033, L038, L041, audited L045 and L058; L044 retained
through L045. No cross-notebook input, GRH or assumed maximality of R.
Before computation, prove Q's exact extension at the degree-one and
degree-eleven five-adic places and all other primes. Justify the
conditional class consequence of a literal successful equality using
the cited general results. Preserve this proof in a canonical lemma
only during the approved research turn. No inverse in R is needed for
the positive product test; class algebra takes place in O_K.

Use exact generators [11I|T-8I] and [5I|T], reducing products in the
fixed power basis. Retain every pairwise product. Every compression
must include integer two-way inclusion certificates, with rank twelve
and k-stability checked. Every coefficient-lattice reduction must
include exact unimodular transforms/inverses and complete size/Lovasz
checks at delta=3/4, reusing the earlier audited procedure; none of its
candidate quality is a principality guarantee.

For each pair test only the twelve reduced basis vectors and bi+bj,
bi-bj for i<j. Verify beta R against the entire product lattice with
exact integer inclusions in both directions. An inclusion with a proved
sublattice index greater than one rejects that candidate only. A norm
or determinant without the inclusion cannot accept an equality.
Save full certificates and an independent replay under
`scripts/power-order-mixed-five-eleven/`; print counts against 16 and
2,304, actual/required ranks and equalities, failures and certificate
paths. Inspect complete load-bearing evidence, not previews.

Stop at the list, or a missing exact verifier/input. Preserve failed
evidence without claiming nonprincipality or a class value. An equality
can settle only the L045 projected-survival condition after its proof;
without one, u remains unknown. The ansatz does not cover arbitrary
fifth-power ideal factors. Units, other places, global points and integer
lifting remain unresolved even on success. No branch exclusion follows.

Full matching Mathlib coverage remains unestablished; the comparison
records the supporting Selmer definitions and its explicit TODO limits.
