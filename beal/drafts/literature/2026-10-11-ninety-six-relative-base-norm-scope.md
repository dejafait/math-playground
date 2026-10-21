# Relative-base norm certification — source comparison

TARGET: Assess whether BFHP's normal-extension certification can apply to L96 over Q(T), using L051-L053 and the exact relative-base hypotheses.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Located the exact relative-base statements within BFHP Sections 3 and 4; checked L051-L053, the prior square-class and normality assessments, histories 144-145 and ATTEMPTS/020 for overlap and recorded stops.
SOURCE_EVIDENCE: BFHP author manuscript dated April 2, 2025, 39 pages: Section 3 opening p.17, Proposition 3.7 and full proof p.20, Section 4 opening p.21, Section 4.3 p.22, Section 4.5 p.29, and Proposition 4.28 pp.32-33; prior full certification proof-case assessment reused.
COMPARISON: The primary framework permits a number-field base F without requiring F/Q normality; it still requires normality of the top extension over F. L053 settles only the different base Q.
GAP: Relative normality is not decided here; norm-relation and global arithmetic certification obligations remain unmet, and the specific Proposition 4.28 route also needs the Section 4.5 group hypotheses.
REASON: The changed base required precise primary scope comparison; the sources now support a separate bounded normality test without certifying its outcome.
LITERATURE_REASON: Q(T) lies outside the previously approved direct-over-Q scope; essential relative-base premises required inspection.
SCOPE: Source comparison only; no field-specific relative normality or class-certificate conclusion.

## Primary scope and qualifications

Biasse–Fieker–Hofmann–Page, *Norm relations and computational problems
in number fields*, [author manuscript](https://www.normalesup.org/~page/Recherche/Documents/articles/brauer.pdf),
April 2, 2025; [published DOI](https://doi.org/10.1112/jlms.12563).
Sections 3 and 4 take a normal number-field extension K/F; F/Q need
not be normal. Proposition 3.7 assumes d=sum ai N_Hi bi, with d>0
and ai,bi in Z[G]. Its norm/extension maps compose to multiplication
by d; localization at d gives injection, surjection and a direct
summand. Read the full proof, including the finite-abelian subquotient case.
Section 4.3 additionally needs finite G-stable prime support and subfield
S-units followed by d-saturation. Section 4.5 requires abelian G.
Proposition 4.28 inherits Algorithm 4.23's nontrivial p-group-factor
case, correct subfield classes and roots of unity, finite unit indices
bounded by Bi and prime to p, S-unit indices prime to p, and its strict
inequality. Prior complete pp.32-33 proof-case coverage is reused;
Theorem 4.11's effective GRH bound is not an unconditional input.

## Local comparison and bounded continuation

Main gap: unconditional global emptiness of L032's five surviving
branches, together with other residual signatures. The intermediate
target is a relative normality applicability test. Downstream use is
to reject this variant before class arithmetic or motivate a separate
review of its remaining group and arithmetic premises.

L051 supplies the exact compositum K96(T), its cubic generator T and
field degrees. L052 supplies audited maximal-ring ramification; L053
and ATTEMPTS/020 preserve the failed direct-over-Q route. None records
a decision for L96/Q(T). The source's K is to be L96 and F is to be
Q(T), not K96. No relative normality, base-field normality, abelian
group, norm relation or class completeness is assumed. We do not
apply Proposition 4.28 merely from normality, nor substitute ordinary
class-group invariants fixed by G for subfield class groups.

The existing normality assessment already inspected Milne ANT v3.08
Theorem 3.34 pp.59-60, Sutherland Fall 2021 Lecture 5 Lemmas 5.28,5.30
pp.8-9, and Milne FT v5.10 Proposition 2.20 and Definitions 3.6-3.9.
Their hypotheses cover arbitrary number-field bases and finite separable
towers, so reuse is adequate for the proposed test. Maximal primes,
prime existence, tower multiplicativity and the Galois degree constraint
must all be retained; divisibility by the degree is conditional on
Galoisness. No polynomial-index assumption or new reproof is needed.

Continue with exactly one normality test after separate approval of the
new continuation assessment. Failure parks only this relative-base
variant; a positive conclusion needs sufficient normality evidence,
not absence of one obstruction. All norm relations, subfield certificates,
unit indices, torsion lifts, support/norm maps and full-disk disjointness
remain independent gaps. No GRH, cross-notebook input, new lemma,
mathematical script or change to PROOF/DAG is used. Mathlib coverage
is not checked. This is source coverage, not progress beyond the
checked literature or a branch exclusion.
