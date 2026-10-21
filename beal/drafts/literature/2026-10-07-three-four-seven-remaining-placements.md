# Remaining (3,4,7) placement coverage proposal

TARGET: Assess Poonen–Schaefer–Stoll Theorem 1.1's applicability to the remaining positive primitive placements (7,4,3) and (3,7,4), retaining signed-coordinate and completeness hypotheses.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-title, signature and correction searches in drafts/literature/2026-10-07-three-four-seven-classification-scope.md; new exact ordered-equation queries found no inspected stronger direct theorem; scoped local assessment/L030/history checks found no remaining-placement application.
SOURCE_EVIDENCE: https://math.mit.edu/~poonen/papers/pss.pdf — Poonen–Schaefer–Stoll, Duke Math. J. 137 (2007), no. 1, 103–158, Theorem 1.1, July 16, 2006 author PDF p. 1; essential integral-completeness qualifications in Lemma 7.8/Section 8 pp. 21–22 and Section 13.7 p. 45, reused from the existing scope assessment.
COMPARISON: The complete signed primitive (2,3,7) theorem permits negative cube and seventh-power coordinates; both remaining placements admit prospective square-coordinate/sign tests within that scope, but neither application nor finite filter is performed here.
GAP: Prove each proposed substitution meets the source equation and gcd convention, expand all 16 signed rows and test required signs and a positive-square first coordinate; no new placement exclusion is established.
REASON: Essential changed-sign source coverage is available; a separately approved bounded specialization can test both placements without reopening saturated audits or blocked mechanisms.
SCOPE: Positive primitive (7,4,3) and (3,7,4), modulo summand interchange, including base one; no divisor extension or independent classification computation.

Main gap: infinitely many residual positive primitive signatures with bases greater than one remain. Proposed intermediate target: determine whether the same cited signed classification supplies adequate coverage for the two remaining placements of these exponents. Downstream use: a separately approved finite signed-coordinate and power filter, if applicability is established. This is a coverage proposal, not an application proof or approval of uncovered mathematics.

Continuation inputs: L030 for the completed ordered case only; Poonen–Schaefer–Stoll Theorem 1.1 and the retained source qualifications in drafts/literature/2026-10-07-three-four-seven-classification-scope.md; foundations/01-target-and-scope.md. No L002, L029, L023, cross-notebook result or conjectural premise is required. Unresolved assumptions are the proposed substitutions' source-equation and primitivity verification and the finite-filter outcomes; none is presumed proved.

The source-comparison test passes: signed integers, gcd one and a complete finite list are covered. The separate specialization assessment delimits future mathematical work and receives separate approval before invocation. Preserve the Cao, mixed-seventh and unit-base-saturation stops. No mathematical script or lemma was written in this literature turn. Mathlib coverage remains not checked.

LITERATURE_REASON: Changed target from ordered (3,4,7) to the remaining right-hand-exponent placements, which the saved assessments explicitly did not cover.

## Completed source comparison

Primary input: Bjorn Poonen, Edward F. Schaefer and Michael Stoll, *Twists of X(7) and primitive solutions to x^2+y^3=z^7*, Duke Math. J. 137 (2007), no. 1, 103–158, Theorem 1.1, [DOI](https://doi.org/10.1215/S0012-7094-07-13714-1). Reaccessed the [July 16, 2006 author PDF](https://math.mit.edu/~poonen/papers/pss.pdf#page=1), p. 1. The theorem assumes integer coordinates, X^2+Y^3=Z^7 and gcd(X,Y,Z)=1. Negative and zero coordinates are allowed; no base-size condition is imposed. The full signed list and sign convention in the existing scope assessment agree with the primary statement. Positivity of the Beal bases must be imposed by a placement-specific filter.

Prospective interfaces for the later test are (X,Y,Z)=(B^2,-C,-A) for A^7+B^4=C^3 and (X,Y,Z)=(C^2,-A,B) for A^3+B^7=C^4. These are proposed applicability tests, not proved substitutions this turn. Research must verify the identities and common-prime support, then require respectively X>0,Y<0,Z<0 or X>0,Y<0,Z>0, together with X a positive square. All 16 rows must be retained before filtering. No rejection, square bound or survivor count for these placements is established here. The prospective sign changes concern odd exponents, not the fourth power.

Completeness is imported. Reaccessed Lemma 7.8/Section 8, author pp. 21–22, and Section 13.7, p. 45; the integral-relevant C5 subset and subgroup-index qualification remain essential, whereas the full C5 rational-point conjecture is unnecessary. Remaining essential proof cases, version distinctions and computational qualifications are reused from the scope assessment. No independent descent, sieve, Magma or PARI/GP rerun is claimed. Changing required signs does not change the source theorem's integer domain.

New queries: `"x^7 + y^4 = z^3"`, `"x^3 + y^7 = z^4"`, `"generalized Fermat" "(3,4,7)"`, and both ordered equations with primitive and Poonen/Schaefer/Stoll terms. Results included unrelated equations, secondary discussions and references to the same primary classification. No stronger direct theorem was inspected or imported; unsuccessful discovery is not a novelty claim. Prior exact-title/correction coverage is reused. Relevant local comparison used the three-four-seven assessments, L030, histories 069–072 and named parked attempts; L030 excludes other placements from its conclusion. This finite-classification mechanism differs from the obstructed unrestricted congruence sieve, missing mixed-seventh packet data and parked Cao extension.

Decision: SPECIALIZE. Only elementary application and finite filters remain for the [new continuation](2026-10-07-three-four-seven-remaining-specialization.md), subject to separate approval. This is new local coverage of a known input, not a mathematical exclusion. Full matching Mathlib theorem and supporting declarations: not checked.
