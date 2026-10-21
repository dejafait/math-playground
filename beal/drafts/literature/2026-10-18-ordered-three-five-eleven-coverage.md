# Ordered (3,5,11) — completed primary-source comparison

TARGET: Assess unconditional literature coverage for A^3+B^5=C^11 with positive primitive integer bases, retaining unit cases and all source hypotheses.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact-signature and equation searches found Putz (2024) and explicit-abc results; notebook-scoped searches found no matching prior import. Queries and inspected sources are recorded below.
SOURCE_EVIDENCE: Putz (2024), DOI 10.5463/thesis.832, Chapter 5 pp.163–173, Theorem 5.1, Proposition 5.7/Table 5.8, Remark 5.13, Propositions 5.18–5.20 and terminal proof cases 5.24–5.27; Chim–Shorey–Sinha MPIM 2018-51, Theorem 1.6 pp.4–5 and Section 5; L002, L029 and foundations/01-target-and-scope.md.
COMPARISON: No inspected unconditional exclusion covers coefficient one; general necessary algebra restrictions apply, whereas the terminal exclusion has different coefficient hypotheses and the alternative height bound assumes explicit abc.
GAP: Global algebra elimination and integer power lifting remain unproved for coefficient one; no effective unconditional height bound or complete computation is supplied by the inspected sources.
REASON: Import only the general necessary interface after separate approval; do not extend a nonunit-coefficient theorem or repeat the source's expensive enumeration. Partial known coverage establishes neither novelty nor literature-wide openness.
LITERATURE_REASON: Changed target from a fixed (3,4,11)-branch localization criterion to ordered (3,5,11); essential theorem coverage is missing, so the next step must be literature-only.

The main gap remains zero positive primitive integer solutions on every
residual signature. This review concerns one ordered signature only.
Its intermediate target is a precise coverage decision, supported by
primary theorem statements and the essential proof cases, for
A^3+B^5=C^11, A,B,C positive integers and gcd(A,B,C)=1.

Essential local inputs are L002 (prime/four reduction and preservation
of prime support) and L029 (all unit-base cases). The equation implies
pairwise coprimality as recorded in foundations/01-target-and-scope.md.
No cross-notebook result is needed. No local solvability, effective
height bound, GRH, complete packet list, rank or computational completeness
is assumed. Do not import a theorem on a different ordered signature
without verifying the proposed transformation and every sign condition.

The discriminating test is whether an inspected unconditional theorem
excludes all positive primitive triples for this exact ordering, or
supplies a concrete intermediate restriction with its independent gaps
explicit. Continue by a separately approved import/specialization if
coverage suffices. Otherwise record the exact remaining gap and at most
one testable mathematical target; inaccessible essential coverage must
not be turned into a theorem. Bounded searches, finiteness and conditional
classifications do not meet the zero-solution threshold.

A valid exclusion would remove one residual signature and could later
be transferred through L002 to its ordered exponent-divisor patterns.
That transfer is downstream context, not mathematics performed here.
The source review below is complete; no new lemma was derived or approved for invocation this turn.
Mathlib coverage for this new target is not checked.

## Completed review — 2026-10-18

Queries used: `"generalized Fermat" "(3,5,11)"`,
`"x^3" "y^5" "z^11" Fermat`,
`"signature (5, 3, 11)" Putz theorem`,
`"generalized Fermat" "3,5,11" solutions theorem`,
`"Putz" "Fermat" "11" theorem 2024`, and spaced signature variants.
The author repository https://github.com/CPutz/etale-algebra-family
identified `GFE/3511.m` as an implementation lead; no code was run.
The primary thesis was read at
https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf
after the shorter `/files/` endpoint failed. Shell retrieval lacked DNS;
the successful alternate primary-text read resolved source access.

Putz's Theorem 5.1 (p.163) assumes its displayed nine-element coefficient
set, which excludes (1,1,1). Its final proof (p.173) combines 5.24–5.27;
these retain that coefficient set and its special local data. Remark
5.13 (p.167) flags the much larger unit-coefficient Hunter search.
General Propositions 5.18–5.20 (pp.168–169) have broader hypotheses;
the proposed import is isolated in the next assessment. The terminal
proof cases were inspected to prevent extending them outside their scope.

The other primary lead is K. C. Chim, T. N. Shorey and Sneh Bala Sinha,
*Explicit abc-conjecture and its applications*, MPIM preprint 2018-51,
https://archive.mpim-bonn.mpg.de/3173/1/preprint_2018_51.pdf .
Theorem 1.6 (printed pp.4–5) treats positive primitive bases exceeding
one and assumes the explicit abc inequality (1.3). Its table retains
[3,5,11] and bounds the largest power strictly by 3.9·10^155.
Section 5 (pp.11–14) starts by invoking the conditional inequality
(1.11), not an unconditional zero-solution classification. That numeric
case was not independently verified and is not imported. The published
Chim–Nair–Shorey account at https://hrj.episciences.org/5117/pdf,
Section 3.C/Theorem 3.3, served as a discovery lead to this preprint.
No abc hypothesis is adopted.

L029 retains unit cases; interchanging the summands matches the source
ordering without sign changes. No other ordering, irreducibility,
complete global enumeration or successful power lifting is assumed.
The live Mauldin primary statement was also checked at
https://sites.math.unt.edu/~mauldin/beal.html and still agrees with
GOAL.md; the nominated AMS endpoint again failed retrieval. No change
in the mathematical target or prize administration is inferred.

Decision: abandon direct application of the nonunit-coefficient
exclusion. Continue only with the narrow cited necessary interface in
`2026-10-18-ordered-three-five-eleven-algebra-import.md`, subject to
separate approval. A future global method needs its own feasibility
test; the historical computational warning is not a ban on other methods.
No lemma, mathematical script, PROOF.md or DAG.md changed.
