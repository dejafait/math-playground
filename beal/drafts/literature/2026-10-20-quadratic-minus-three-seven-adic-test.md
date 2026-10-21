# Quadratic minus-three component at seven — completed source comparison

TARGET: Test whether a primitive seven-adic fiber of phi(t)=(3t²+t+1)^5(1−5t) can have Q7 × (Q(sqrt(−3)) tensor Q7) as a direct product factor.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the assessed signature and quadratic searches; new exact-polynomial, signature/local/seven and Hensel-factorization searches located primary local methods and Putz's package, but no inspected statement deciding this simultaneous factor condition; queries and limits below.
SOURCE_EVIDENCE: Putz (2024), version of record, Theorem 2.72 pp.68–69 and Proposition 5.19 pp.168–169, with relevant proof cases; Sharifi, Algebraic Number Theory, online Chapter 5, Theorems 5.3.30 and 5.3.33 with proofs; Stacks Project 59.32.3–4, with their stated proof references; existing foundations/17-local-power-hensel-inputs.md reused.
COMPARISON: Known root/factor lifting and local branch methods support a finite witness search and a separately justified branch analysis, but unramifiedness alone does not count rational factors or give the simultaneous primitive tuple; no matching system-specific theorem is imported.
GAP: Compute and justify the quadratic completion and simultaneous whole-factor realizability at one common primitive scalar, or exclude it over every valuation branch; this review supplies no factorization or local witness.
REASON: Essential elementary method coverage is now available for one bounded attempt at the unchanged target, without a new backend or high-degree enumeration; EXPLORE makes no originality claim.
LITERATURE_REASON: The joint factor requirement at seven was outside earlier standalone local and quadratic-at-two assessments; this turn completes that missing comparison rather than refreshing an unchanged ready target.
SCOPE: Exactly TARGET with nonzero A,B,C in Z7, min(v7(A),v7(B),v7(C))=0, A³+B⁵=C¹¹, s=B⁵/C¹¹ distinct from 0 and 1, and the entire etale Q7-algebra Q7[t]/(phi(t)−s).

This literature-only turn completes coverage for a separate mathematical
attempt. The supervisor must separately approve this newly changed
assessment next turn. No result about splitting at seven, fiber factors
or primitive tuples is derived or approved as mathematics here.

The proposed factor must be realized simultaneously, with disjoint
whole local factors, in one fiber at one scalar from one common
primitive tuple. Equivalently the proposed test asks for an isomorphism
of that entire degree-eleven algebra with the stated degree-three
product times a degree-eight etale algebra. An arbitrary embedding as
a subalgebra, a selected root, or separate examples for its components
do not meet the target. Local positivity is not imposed.

Essential inputs are L093, L103 and L104. L095 explains the global
rational-factor branch; the proposed necessary local test does not
assert that a local rational factor is global or that an arbitrary
local tuple satisfies both global integer systems. A global solution
with the rational factor and this quadratic direct component would
necessarily pass the test after base change at seven.

Continue toward an exclusion only if all primitive valuation branches
and the entire product can be controlled. One exact common primitive
witness with the whole direct factor is a decisive negative result for
standalone exclusion at this prime. A residue sample alone proves
neither outcome. Even an exclusion leaves Q(sqrt(−11)), the branches
without quadratic components, integer lifting and other signatures open.

This differs from the recorded standalone local-solvability stops by
requiring the rational and specified quadratic factors simultaneously.
It leaves the complete high-degree classification park and ATTEMPTS/045
intact. Full matching Mathlib coverage is not checked; unknown coverage
does not establish absence. A failed search does not establish novelty.

## Existing work and the exact gap

The main gap is integer elimination of both L095 systems in the global
rational-factor branch of ordered (3,5,11); other component types and
residual Beal signatures remain independent gaps. L104's audited
necessary list leaves two quadratic alternatives against the desired
zero-alternative threshold. The intermediate target is exactly TARGET,
not a solution of either integer system.

Read the relevant L093 interface and full audit, L104's hypotheses and
classification proof, histories 353–354 and 356, the prior two-adic
complete-system assessment, the global-cover comparison, and the
ATTEMPTS/045 execution park. Targeted checks of the specified
rational-factor stop records and scoped assessments found no completed
joint test at seven. The known Hensel inputs in foundations/17 are
reused, without repeating their proofs. L103's whole-component argument
and audited L104 are already supplied in the overview and assessment;
their two-adic classification is retained, not recomputed here.

The earlier local points at 2,3,5,11 and L001's unrestricted local
solubility do not impose this joint algebra factor. ATTEMPTS/045's
class-backend blocker is independent of the proposed elementary test.
No cross-notebook result is used. A local degree-one factor remains
strictly a local condition; it is not evidence of a global rational root.

## Primary sources and applicability limits

P. H. C. Putz, *Enumeration of local and global étale algebras applied
to generalized Fermat equations*, VU Amsterdam thesis (2024), version
of record, [DOI 10.5463/thesis.832](https://doi.org/10.5463/thesis.832),
[primary PDF](https://research.vu.nl/ws/portalfiles/portal/367784086/Thesis_CasperPutz.pdf).
Inspected Theorem 2.72 and its proof, printed pp.68–69 (PDF indices
74–75), and Proposition 5.19 with all cases, pp.168–169 (174–175).
The former assumes integral f,g, monic f, deg(g)<=deg(f), unit leading
coefficient of g, unit radical discriminant and resultant, unit common
ramification index k, and nonzero s0 of positive valuation divisible
by k. It gives unramifiedness. Its proof controls every lifted block
by a separable residual binomial. The latter treats the regular case,
zero and one branches, and infinity via the reciprocal chart; its
statement concerns primitive integer solutions. These methods do not
determine the required direct factor. For arbitrary local tuples,
check the hypotheses locally rather than enlarging that statement.
No special-coefficient global elimination is imported.

Romyar Sharifi, *Algebraic Number Theory*,
[author's online Chapter 5](https://www.math.ucla.edu/~sharifi/notes/algnum-ch05.html),
accessed 2026-10-20; online version, no revision date identified.
Read Theorems 5.3.30 and 5.3.33 and their proofs, through the end of
the factor-lifting proof. They assume a complete nonarchimedean
valuation field. The first lifts a simple residue root uniquely in its
residue class. The second lifts a coprime residue factorization of a
primitive integral polynomial, preserving the degree of the specified
factor and a stronger prescribed congruence when available. Thus
repeated residue factors cannot be split internally by this theorem
alone. At seven, normalization and every derivative/coprimality test
are still to be supplied for the actual equations. No root extraction
or fiber factorization is asserted by this review.

[Stacks Project, Section 59.32](https://stacks.math.columbia.edu/tag/03QD),
accessed 2026-10-20, Theorems 59.32.3–4: complete local rings are
henselian; coprime factor lifting and finite-algebra product
decomposition are among the equivalent formulations. Read the
statements and proof attributions to Algebra 10.153.9 and 10.153.3;
those referenced full proofs were not independently reread. This
supports whole factors; an embedded subfield cannot replace a product
factor. The already audited L103 argument handles that distinction.

The existing Clark/Zábrádi inputs in foundations/17 supply the stronger
Newton inequality v(f)>2v(f') and lifting in one variable while holding
the others fixed. Their previous primary inspection is reused. Any
new application must display its actual residual error and derivative,
and preserve the same scalar throughout all identities. No reproof
is warranted for these named standard results.

## Discovery record and source scope

Queries used: `"3t" "1-5t" Putz Fermat`,
`"3t^2+t+1" "11"`, `"Putz" "Fermat" "seven"`,
`"Putz" "local" "5" "3" "11" algebras`,
`"3t^2+t+1" Putz seven`,
`"generalized Fermat" "3,5,11" "local" "7"`,
`"3t²+t+1"`, and a coprime-factor/simple-root Hensel query.
No inspected theorem supplies the requested existence or exclusion.
Unrelated (3,5,7) results do not answer a degree-eleven fiber question.

The author's [package README](https://github.com/CPutz/etale-algebra-family)
identifies `3511.m` as the matching map implementation. Its code and
outputs are uninspected, optional leads; a guessed raw `main/3511.m`
URL failed and supplies no evidence. No Magma execution is needed for
the approved elementary scope. The AMS prize-page request also failed;
the unchanged exact Beal statement is retained from the existing
foundations/01 source record, not reverified by that request. Neither
failure blocks the target's lifting coverage. No claim based on a
search snippet, package output or unreviewed signature exclusion is used.

## Bounded next attempt and stopping test

After separate approval, first determine the entire completion of
Q(sqrt(−3)) at seven using its defining quadratic and the cited lifting
criterion. Do not silently treat it as a quadratic field or discard
one factor if it splits. Then test the regular scalar residues modulo
seven with primitive coordinate residues from the original equation;
preserve complete degree-eleven factorizations and all multiplicities.
A candidate must yield disjoint whole factors of the required total
degree, with coprime complement, in one exact fiber.

Try to lift a single compatible residue tuple, fixing shared coordinates
as appropriate and recording exact nonzero valuations, derivative bounds,
s=B^5/C^11 and 1−s=A^3/C^11. Roots must belong to that same scalar's
fiber. A witness may lie in any one permitted valuation branch; it need
not classify all branches. Provide the entire complementary degree-eight
etale algebra or an exact coprime factor certificate of its degree and
separability. Independent examples for separate factors are insufficient.

If no regular witness is found, allow at most one normalized branch
calculation, with residue precision at most 7^3 before reassessment.
A universal exclusion must instead justify completeness across the
regular, B-divisible, A-divisible and C-divisible branches, including
arbitrarily large valuations. Apply Putz's local theorem only after
checking its full normalization, radical, resultant and index conditions;
unramifiedness alone is not a factor count. Finite-depth failure is only
a search failure. Changed machinery outside this scope needs a new review.

One exact common primitive witness with the full joint factor parks
standalone exclusion at seven. An exhaustive exclusion removes only the
minus-three alternative in the global rational-factor branch. Otherwise
save the bounded evidence and reassess this mechanism. The minus-eleven
alternative, branches without quadratic factors, compatibility of larger
fields, both integer systems and other signatures remain unresolved.
This review ran no mathematical calculation and changed no lemma or script.
