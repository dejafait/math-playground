# Ordered (3,5,11) — exceptional-prime discriminant continuation

TARGET: Import Putz's coefficient-one discriminant valuation restrictions at 3, 5 and 11 for L093's entire algebra.
CHECKED: 2026-10-18
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the exact-signature searches in drafts/literature/2026-10-18-ordered-three-five-eleven-coverage.md; checked L093 and history/311 for duplication and scope; reopened the primary theorem and discriminant definition for this distinct target.
SOURCE_EVIDENCE: Putz (2024), DOI 10.5463/thesis.832, version of record: Section 1.5.2/Proposition 1.16 p.22; Section 5.2/Proposition 5.7 p.165, Table 5.8 and computational proof p.166; Remark 5.13 p.167, all inspected.
COMPARISON: Proposition 5.7/Table 5.8 covers the exact required maximal-algebra valuation restrictions; L093 supplies the matching entire algebra. No reproof, polynomial-discriminant substitution or new computation is needed.
GAP: Source scope is resolved; the cited computation is not independently replayed. Global algebra elimination, irreducibility and integer power lifting remain unresolved.
REASON: Approve a later citation-only application to coefficient one, retaining all factors and coordinate-divisor cases. This literature turn derives no result and changes no lemma or mathematical script.
LITERATURE_REASON: Changed target from auditing Propositions 5.18–5.20 to the essential exceptional-prime maximal-discriminant input in Proposition 5.7/Table 5.8.

Essential inputs for the eventual application: audited L093 and Putz's
Proposition 5.7/Table 5.8, for the unchanged positive primitive equation
A^3+B^5=C^11 and coefficients (1,1,1). No cross-notebook input.
Retain every global factor and distinguish a necessary covering list
from a list of realized algebras. Import the source computation by
precise citation if its hypotheses match; no algorithm replay is proposed.

Downstream use: bounded exceptional ramification could combine with
L093's real and two-adic restrictions to constrain global algebra
candidates. Global elimination and integer power lifting remain separate.
The application must preserve Remark 5.13's computational warning:
this is not authorization to begin a Hunter enumeration or to apply
the special-coefficient terminal exclusions.

Continuation test: approve only if the source bounds the discriminant
of the entire maximal étale algebra for coefficient one, including all
coordinate-divisor cases. Otherwise record the exact scope failure and
park this import. No lemma or calculation for this target was performed in this review. Mathlib coverage is not checked.


## Completed focused source review — 2026-10-18

Primary source: P. H. C. Putz, *Enumeration of local and global étale
algebras applied to generalized Fermat equations*, VU Amsterdam doctoral
thesis (2024), version of record, [DOI](https://doi.org/10.5463/thesis.832),
[primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf).
Printed pp.22,165–167 correspond to PDF indices 28,171–173.

The inspected statement is for nonzero pairwise coprime integer
coefficients and a nontrivial primitive solution as defined in (5.1).
It is not limited to Theorem 5.1's special coefficient set. Table 5.8's
condition is v_p(abc)=0. Its entries are:

| p | permitted v_p(delta) |
|---|---|
| 3 | 6, 8, 10 |
| 5 | 8, 10 |
| 11 | 9, 11 |

Here delta is the discriminant of the entire algebra, defined on p.22
using its integral closure; Proposition 1.16 retains every component.
It is not the discriminant of the displayed polynomial or power order.
The coefficient condition does not require unit solution coordinates.
Thus the statement includes each coordinate-divisor case; no bound on
coordinate valuations or selection of one field factor is added.

The proof cites Algorithm 2.74 and the accompanying Magma script
ramification.m. We accept that computational theorem by citation,
without claiming code inspection or independent execution. The proof's
extra model transformations concern nonunit-coefficient Table 5.11;
those cases are not needed here. No conditional hypothesis is stated
for Proposition 5.7. Remark 5.13 explicitly discusses coefficient one
and warns against the large degree-eleven Hunter workload. This is a
limitation of that proposed enumeration, not a global ban on the route.

The later application must identify coefficients (1,1,1), coordinates
(B,A,C), and the same parameter and entire algebra as L093, and cite
the table rather than reprove it. Table entries are necessary covering
possibilities, with no claim that every combination is globally realized.
The review resolves the essential coverage question only. L093 did not
already import this exceptional-prime input. No new theorem beyond the
checked source, complete field list or integer exclusion is claimed.

Decision: the continuation test passes. Reuse this IMPORT assessment
for its unchanged exact TARGET next turn; no additional source review
is needed before that application. Mathlib coverage remains not checked.
