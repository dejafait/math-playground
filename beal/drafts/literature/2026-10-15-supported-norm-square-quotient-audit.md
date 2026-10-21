# Supported quotient critical audit — source scope approved

TARGET: Critically audit L074's supported norm-square quotient, including the localized norm diagram and S-unit lifting correction.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the bounded searches and inspected primary evidence in drafts/literature/2026-10-15-supported-norm-square-nonunit-quotient.md; compared L074's complete proof, L033's field hypotheses, L069's entire cubic-field argument, histories 234–235 and ATTEMPTS/032–033. No fresh external search or primary-source extraction was necessary or performed.
SOURCE_EVIDENCE: Reused Simon, LMS J. Comput. Math. 5 (2002), Proposition 1.3 pp.8–9; Milne ANT v3.08 (19 July 2020), Propositions 3.4–3.5 p.48, 3.23 p.55 and 4.1 pp.68–69, including the previously inspected proofs; Stacks Lemma 10.36.11 Tag 0307; BPT arXiv:2001.02263v3 Lemma 2.14 pp.12–13 only for the previously inspected odd-degree scalar method.
COMPARISON: The audit has the same maximal localized rings, complete support and degree-three extension as the ready quotient assessment; existing sources cover every general prerequisite. They do not certify L074's application, natural maps or representative-choice algebra, so an independent proof audit remains necessary.
GAP: Audit exactness, localized norm compatibility, square-class injections, the scalar S-unit correction, all choices and the class-norm section; neither this scope approval nor the sources compute the class kernel or a rank bound.
REASON: Approve the separate critical application audit using unchanged adequate coverage; no essential changed hypothesis or unread theorem requires further literature.
LITERATURE_REASON: The supervisor required separate scope approval for this newly saved audit target; this turn compares that scope with ready coverage and does not repeat browsing.
SCOPE: Exactly TARGET for L033's entire K and L069's entire cubic D/K with its fixed generator, maximal rings localized at all primes above 2 and 11, fractional ideals, ordinary S-class groups and no sign restrictions; REPRODUCTION is approved for the critical application audit only.

## Reused primary coverage and applicability

The prior [supported quotient assessment](2026-10-15-supported-norm-square-nonunit-quotient.md)
is the canonical record of the searches, source versions, inspected passages
and unread leads. Those sources and hypotheses have not changed. This
review read that record rather than claiming a fresh inspection of the
external documents. No novelty inference follows from the reused search.

Simon, *Computing the rank of elliptic curves over number fields*, LMS
J. Comput. Math. **5** (2002), 7–17, Section 1.2, Proposition 1.3,
printed pp.8–9 ([publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf)),
already treats finite support, S-units and actual S-class two-torsion.
Include infinite places without sign conditions. Its abstract isomorphism
supplies no norm-compatible section; checking the natural ideal-square
maps in L074 is an essential application audit, not a reproof of descent.

Milne, [*Algebraic Number Theory*, v3.08](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Propositions 3.4–3.5, 3.23 and 4.1, supplies Dedekind localization,
fractional ideal prime exponents and the principal/extended-ideal norm
identities, including the nonnormal case. [Stacks Tag 0307](https://stacks.math.columbia.edu/tag/0307)
supplies localization of integral closure. The support here is unchanged
from the assessed support: R_F=O_F[1/22] for F=K,D, retaining every
surviving prime. These sources require neither a polynomial order nor
normality nor class-number assumptions. The audit must check that L074
actually applies the identities to these rings and fractional ideals.

The prior ordinary [assessment](2026-10-15-even-valuation-unit-exhaustion.md)
records the inspected [BPT v3](https://arxiv.org/pdf/2001.02263v3)
Lemma 2.14 scalar method. Only its odd-degree method is relevant;
no positivity, class-number or Selmer conclusion is imported. Checking
that the scalar correction works on S-unit square classes is part of
the forthcoming audit. Surjectivity on unsquared unit norms is not a
source premise and must not be asserted. Simon's separate norm-equation
paper and the references behind Proposition 1.3 remain unread leads,
not essential sources for this audit scope.

## Exact audit boundary and discriminating test

The main gap remains primitive integer emptiness, including the unresolved
ordered (3,4,11) branch. This intermediate target checks a structural
input needed to control non-unit contributions before a filtered descent
could give a useful rank bound. It need not resolve independent gaps.

Essential inputs are L074's entire proof, L033's entire K, and L069's
entire cubic D/K and fixed generator. The scope comparison checked the
field definitions and L069's field argument; the later audit must read
every input range needed for its conclusions. L072 is an ordinary-support
comparison only. Audited L073 and ATTEMPTS/033 preserve the failure of
universal local evenness at eleven; ATTEMPTS/032 preserves the unfiltered
rank obstruction. This target duplicates neither stopped claim. No
cross-notebook input is used.

Continue if independent checking establishes exactness and a canonical
quotient without lost support or a remaining unit-norm obstruction.
Check localized square roots of units, norm/extension descent, kernel
lifting, simultaneous changes of representatives and generators, and
the two-torsion class section. Correct any error canonically or record
the precise remaining obstruction. Do not treat this source approval
as that mathematical check or as acceptance of L074's claimed result.

Full Kummer containment, S-unit completeness and dimension, actual
S-class arithmetic, global realization of local odd classes, simultaneous
local filtering, rank, indices/cosets and primitive integer lifting
remain unresolved. Ordinary class two-torsion images cannot silently
replace actual localized two-torsion; L069's ordinary-unit dimension
cannot silently replace the supported unit dimension. No complete Beal
candidate is present. Mathlib coverage of the full statement and its
supporting machinery remains not checked; no absence is inferred.
