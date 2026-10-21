# Quadratic components of the rational-factor complement — source assessment

TARGET: Determine the complete list of imaginary quadratic field components compatible with L103's degree-ten complement using L093's ramification support and whole two-adic factors.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact quadratic-discriminant/splitting and Putz quadratic-component searches located primary course notes and the thesis; checked the existing complement assessments, history/349 and ATTEMPTS/045; no completed local candidate list was found.
SOURCE_EVIDENCE: Inspected Shotton, Number Theory III (Michaelmas 2026), Proposition 5.14 and Theorem 5.17; Oh, An Invitation to Modern Algebraic Number Theory, Example 1.28 pp.19–20, Theorem 2.9 pp.33, Exercise 2.1 solution p.222 and Theorem 4.11 pp.78–79; Putz (2024), Proposition 5.26 with both proof cases pp.171–172, DOI 10.5463/thesis.832.
COMPARISON: Standard quadratic classification, discriminant and splitting results cover the field-theoretic inputs; the finite support enumeration and direct-factor compatibility test under L093/L103 remain a specialization. Putz's stronger exclusion assumes special coefficients and stronger local tables and cannot be imported here.
GAP: No candidate enumeration or complete compatible list has been derived; compatibility here means only the stated support, signature and whole two-adic necessary conditions, not realization by a complementary algebra or a fiber.
REASON: Approve a bounded source-backed finite specialization without high-degree databases or class-group execution; it can constrain the quadratic branches while leaving all larger-component and integer gaps open.
SCOPE: Exactly TARGET for quadratic direct components of the entire complement in L095's global rational-factor branch, using audited L093 and L103; no quadratic-subfield classification, L094 discriminant refinement, product realization or signature exclusion.
LITERATURE_REASON: This previously REVIEW_REQUIRED target required unread quadratic classification/splitting coverage and comparison with Putz's stronger restricted elimination.

## Gap, intermediate use and discriminating test

The main gap remains elimination of both L095 simultaneous integer power
systems, with independent residual signatures unresolved. The intermediate
target is a complete necessary quadratic direct-component list under the
saved premises. Such a list could restrict the (8,2) and (4,4,2) branches
before later fiber comparisons. It need not solve the larger components.

Continue with a finite exhaustive classification and retain every local
factor and multiplicity. Success requires a proof that every possible
quadratic direct component is covered and that each listed field passes
these tests; passing must not be called actual fiber realization. Abandon
any shortcut needing uninspected special-coefficient local tables or an
unavailable high-degree database. An empty list would affect only branches
requiring a quadratic component. No list is calculated in this turn.

## Primary coverage inspected

[Jack Shotton, Number Theory III](https://www.maths.dur.ac.uk/users/jack.g.shotton/Teaching/number-theory/notes.html),
Michaelmas 2026, based on Alexander Stasinski's notes: Proposition 5.14
classifies quadratic fields by a unique squarefree integer d different
from 0 and 1; Definition 5.15 distinguishes d<0. Theorem 5.17 gives the
full integer ring: Z[sqrt(d)] for d congruent to 2 or 3 modulo 4,
and Z[(1+sqrt(d))/2] for d congruent to 1 modulo 4. These hypotheses
include imaginary fields; no class-number or coefficient hypothesis occurs.

[Gyujin Oh, An Invitation to Modern Algebraic Number Theory](https://www.math.columbia.edu/~gyujinoh/ANT_revised.pdf),
250-page author-hosted revised PDF, accessed 2026-10-20 (no dated revision
identifier established). Example 1.28 gives discriminant d or 4d in the
two integral-basis cases. Theorem 4.11 equates ramification with division
of the maximal-ring discriminant. Theorem 2.9 treats d congruent to 2,3
modulo 4, including ramification at two. For d congruent to 1 modulo 4,
the complete Exercise 2.1 solution supplies the missing case: two splits
at d congruent to 1 modulo 8 and is inert at d congruent to 5 modulo 8.
Its proof tests X²−X+(1−d)/4 over F2. PDF indices 18–19,32,77–78,221;
printed pages are one greater. Use the latter case rather than incorrectly
applying Theorem 2.9 to odd discriminants. No reproof of these inputs is
needed; the future work is finite specialization and whole-factor matching.

[P. H. C. Putz, Enumeration of local and global étale algebras applied to generalized Fermat equations](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf),
VU thesis (2024), version of record, [DOI](https://doi.org/10.5463/thesis.832),
Proposition 5.26, printed pp.171–172 (PDF indices 177–178): its first
eleven-adic case uses C4 and ramification only at eleven. The other uses
ramification confined to three and eleven and the specified ramified
quadratic completion at eleven to identify Q(sqrt(-11)). Its remaining
arguments use a degree-nine discriminant bound or the five-adic Table 5.16.
All these cases were read. The proposition assumes coefficients in C;
L093 instead retains support {3,5,11}. Neither identification nor terminal
exclusion transfers from this proof. Proposition 5.25's elimination of
other small degrees likewise uses stronger restricted local data.

## Search, overlap and bounded authorization

Queries: `quadratic fields discriminant splitting prime 2 theorem university
notes squarefree d`; `Putz thesis Proposition 5.24 quadratic fields 3 5 11`.
Search results also included secondary pages, which were not used as
mathematical evidence. The first Durham version inspected ends at the
quadratic integer-ring theorem; it was not treated as splitting coverage.
Oh's explicit exercise solution fills that source gap. Search failure
makes no novelty claim. No exact-target stronger classification was
established beyond these standard inputs and Putz's restricted theorem.

Reused audited L093/L103 canonical proofs and their hypotheses. Read the
prior complementary-algebra assessment and history/349: complete high-degree
algebra lookup remains parked. ATTEMPTS/045's class-group execution blocker
remains intact; no backend probe or database query was repeated. This
bounded quadratic target needs neither execution mechanism.

The next mathematical step may enumerate negative squarefree parameters,
apply the maximal-discriminant support criterion, and compare the resulting
two-adic completions against whole factors of each L103 local product.
It must justify exhaustion from the cited results and keep the distinction
between direct components and subfields. Do not use a quadratic subfield
inside U4 or U10 as a direct factor. No new lemma, enumeration, mathematical
script or claimed list has been produced or approved as a theorem here.
Classification of the completed literature step is NOVELTY_UNCHECKED;
future finite specialization should be REPRODUCTION, without novelty claims.
Mathlib coverage is not checked.

The startup REVIEW_REQUIRED proposal and its separate-review requirement
are discharged by this source comparison only. This assessment now covers
the unchanged exact TARGET. Any stronger target requires separate review.
