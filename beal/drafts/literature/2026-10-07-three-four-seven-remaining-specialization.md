# Remaining-placement finite specialization coverage

TARGET: Specialize Poonen–Schaefer–Stoll Theorem 1.1 to positive primitive (7,4,3) and (3,7,4) by verifying signed substitutions and filtering all 16 triples for required signs and a square first coordinate.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact ordered-equation, signature and local duplicate checks completed in drafts/literature/2026-10-07-three-four-seven-remaining-placements.md; primary-title/correction discovery is reused from the classification-scope assessment.
SOURCE_EVIDENCE: https://math.mit.edu/~poonen/papers/pss.pdf — Poonen–Schaefer–Stoll, Duke Math. J. 137 (2007), no. 1, 103–158, Theorem 1.1, July 16, 2006 author PDF p. 1; Lemma 7.8/Section 8 pp. 21–22 and Section 13.7 p. 45 reaccessed in step 073.
COMPARISON: The source supplies the complete signed primitive (2,3,7) list; elementary substitutions, prime-support verification and sign/square filters for these placements remain to be justified locally.
GAP: No application proof or survivor count for either placement exists yet; require an exhaustive exact finite test without presuming its outcome.
REASON: Changed-sign source coverage is available; this bounded specialization may narrow two residual placements without a new descent or reopening blocked routes.
SCOPE: Positive primitive A^7+B^4=C^3 and A^3+B^7=C^4, including unit bases and summand interchanges only; no divisor extension or general mixed-signature claim.

Main gap: infinitely many residual primitive positive signatures remain. Intermediate target: exact signed-classification filters for these two placements. Downstream use: assemble whichever exclusions the complete test proves. Continue with an exclusion only if all source hypotheses are justified and actual survivors equal the required zero separately for each placement; a survivor requires checking its inverse substitution and blocks that exclusion rather than being discarded.

Essential inputs: Poonen–Schaefer–Stoll Theorem 1.1 with the complete signed list and computational/integral-C5 qualifications in the classification-scope and remaining-placements assessments; foundations/01-target-and-scope.md for positivity and primitivity. L030 is context only. No cross-notebook, L002, L029, L023, conjectural full-C5 or exceptional-algebra premise.

Prospective substitutions to verify, not established results: (B^2,-C,-A) and (C^2,-A,B), respectively. Prove each source identity and preservation of common prime divisors, with base one retained. Expand each sign individually, including both whole-triple signs of (0,1,1). Check required signs and positive-square first coordinate using exact integer bounds where needed. Record full relevant row evidence; a preview is insufficient. Import the classification by precise citation; rederive only the necessary application differences, not its global proof or computations. Any result belongs in a canonical lemma with Hypotheses, Conclusion, Proof and Mathlib sections. Mathlib coverage is not checked.

This newly written ready continuation receives separate approval next turn. No mathematics is authorized in the present literature turn. Applicability and both survivor outcomes remain unresolved; the all-signature gap and parked source-dependent routes remain independent.
