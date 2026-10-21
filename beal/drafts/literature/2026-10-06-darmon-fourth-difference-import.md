# Proposed scoped Darmon import

TARGET: Apply Darmon's Theorem I to exclude positive primitive a^4+b^p=c^4 for primes p>=11 with p congruent to 1 modulo 4, and for primes p>=11 with b even, then transfer only these ordered exclusions through L002.
CHECKED: 2026-10-06
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse the exact-equation searches and duplicate/failure comparison in drafts/literature/2026-10-06-fourth-prime-fourth-source-scope.md; no broader range is proposed.
SOURCE_EVIDENCE: https://www.math.mcgill.ca/darmon/pub/Articles/Research/10.Fermat-44p/paper.pdf — Darmon Theorem I and both essential parity cases, author-copy pp. 1–4, retrieved and confirmed 2026-10-06; BCDT Theorem A at https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/STW.pdf#page=1 is already verified in foundations/02-standard-results.md and discharges its modularity premise.
COMPARISON: This imports only inspected difference-equation clauses; it neither duplicates L027's plus placement nor uses Kihel–Levesque's unread Cao proof input.
GAP: Local identification, nontriviality, equation-implied pairwise coprimality and L002 ordered divisor transfer remain to be written; unrestricted odd b at p=3 mod 4 and small primes are outside this approved source scope.
REASON: Independent ready partial coverage supports a concrete citation application while the stronger full-range proof review is parked.

The separate literature review on 2026-10-06 confirms this unchanged target as IMPORT. The completed source comparison is preserved. Inputs: L002, foundations/01-target-and-scope.md, foundations/02-standard-results.md and the precise Darmon citation in the source-scope assessment. No exceptional-algebra or spectral assumption is allowed. Continue if (c,a,b) satisfies every source hypothesis and the divisor substitution preserves the even-b condition when used; restrict or abandon any clause that fails this test. The downstream use is a partial residual-signature exclusion; infinitely many signatures remain. No new descent or modular reproof is justified. Mathlib coverage: not checked.

## Source-URL recovery and separate approval

Henri Darmon, *The equation x^4-y^4=z^p*, C. R. Math. Rep. Acad. Sci. Canada **15** (6) (1993), 286–290, **Theorem I**; the retrieved author copy is internally dated September 9, 2007. Equality with the printed version has not been checked. The equation and coprimality convention are on manuscript p. 1, the theorem on p. 2, and the essential cases on pp. 3–4. The even power-base case uses level 2; the odd case uses level 32 and a split Cartan when p is 1 modulo 4. The source explicitly leaves the complementary nonsplit case unresolved. No lower bound excluding bases equal to one is stated. The historical modularity premise is covered by the existing BCDT citation, rather than a new modular reproof.

This review reuses the duplicate/failure comparison in the source-scope assessment: L027's plus placement and L012's cube boundary do not cover this target; the blocked Cao input and mixed-seventh packet data are unnecessary for these narrower clauses. Retrieval confirms existing coverage and repairs its direct URL; it adds no mathematical result. The next research step must still write the applicability and ordered divisor-transfer arguments, retaining the two clauses separately and making no full-range claim.
