# Four-row finiteness — completed source comparison

TARGET: Determine whether every pairwise-linear original quadruple whose supports split into two disjoint pairs has finitely many four-row rank-one planes over the algebraic closure of F_97, or give an explicit infinite family.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 498 searched four-plane common transversals, exceptional infinite families and the four-subspace problem; compared L109/C155a/L157, L115/L116/L119/L120/L125/L126/L127 and ATTEMPTS/041–043,/048–049. Exact queries, inspected passages and limits appear below; no novelty inferred.
SOURCE_EVIDENCE: Reuse step 490/494 Kostrikin–Manin arbitrary-field linear/projective tools; inspect Sottile alg-geom/9510017v1 section 7.1 pp. 14–15 and Breiding–Rydell–Shehu–Torres arXiv:2203.01694v2 section 1.2 Lemmas 1.6–1.8 pp. 6–8, including available proofs and complex-field convention p. 3. Medina–Zavadskij full text remains inaccessible and is not imported.
COMPARISON: Generic enumerative counts and complex projective-three-space exceptions do not imply finiteness for these characteristic-97 kernel planes. Fixed-label local finite loci are partial examples; L115's whole projective plane does not meet the two-disjoint-pairs condition. No inspected result settles the exact universal assertion or provides a matching counterfamily.
GAP: Decide finiteness for the actual original maps with both disjoint pairs, preserving decomposability and exact rank one; L157 bounds neither image-line choices nor the total locus. No locus-size result is established by this review.
REASON: Ready arbitrary-field tools suffice for a bounded exact proof/counterfamily attempt without importing an unread classification; an all-quadruple rank census and repeated source-blocker retrieval are not approved mechanisms.
LITERATURE_REASON: New finiteness scope from step 497 needs exceptional-locus and duplicate comparison beyond the completed shared-factor reconstruction audit; this review completes that comparison.
SCOPE: Original L109/C155a/L157 H/S/J and 756 labels; distinct a,b,c,d, a<b and c<d, disjoint supports within each pair and all six intersections at most one; E algebraic closure of F_97; E-valued planes only, rank(Q_j restricted to L)=1 for all four, without coding gates.

## Decision and relevance

The main gap is uniform twelve-row exclusion. The intermediate threshold
is finiteness of the four-row rank-one locus on precisely SCOPE, or an
explicit infinite family on that domain. Finiteness could leave finitely
many branches for later-row and coding tests. An infinite family would
require additional restrictions for that reduction. Second-pair extraction
is independent and unproved: C152a supplies only one disjoint pair.

This is an EXPLORE approval, not an import, a claim of novelty or a result.
Known linear/projective tools are reused by citation; no general theorem
needs reproof. Any claimed local result must justify the actual maps,
incidence, extension field and all rank-zero exclusions. Matching Mathlib
coverage is not checked; unknown coverage is not absence.

## Source comparison

Reuse A. I. Kostrikin and Yu. I. Manin, *Linear Algebra and Geometry*,
Gordon and Breach, 1997 paperback, ISBN 90-5699-049-7, Chapter 1 Theorem
3.12 pp. 20–21, sections 6.2–6.9 pp. 44–46; Chapter 3 sections 6.2–6.4
pp. 222–226, 6.8–6.10 pp. 227–228, 8.1 p. 233 and 8.10 pp. 239–240,
[primary book](https://www.math.mcgill.ca/darmon/courses/19-20/algebra2/manin.pdf).
The complete earlier primary-reading record and qualifications are in
`drafts/literature/2026-10-25-two-additional-row-factor-compatibility-review.md`
and `drafts/literature/2026-10-25-segre-additional-row-rank-one-review.md`.
These arbitrary-field results allow finite-dimensional kernels, images,
quotient cosets and projective normalization. They apply over the stated
algebraic closure; zero restrictions use linear definitions rather than
nonzero-summand projection constructions. They support exact local work,
not a theorem that intersections are finite. L157 supplies the already
written shared-representative construction; its first audit remains
conditional on inherited inputs. No new audit is performed here.

F. Sottile, *Explicit Enumerative Geometry for the Real Grassmannian of
Lines in Projective Space*, [arXiv:alg-geom/9510017v1](https://arxiv.org/pdf/alg-geom/9510017v1),
31 October 1995, section 7.1 pp. 14–15: inspected the complete subsection,
including its coordinate construction. Three mutually non-intersecting
(n−1)-planes in projective (2n−1)-space give a Segre family; a general
fourth plane gives n lines. The finite-field realization statement is
existential in the flags. It is not a universal result about special
flags, and the actual ambient space and cross intersections require
justification before any reduction to this theorem. No such reduction
or genericity proof is supplied or assumed.

P. Breiding, F. Rydell, E. Shehu and A. Torres, *Line Multiview Varieties*,
[arXiv:2203.01694v2](https://arxiv.org/pdf/2203.01694v2), 18 November 2022:
read the complex-field convention p. 3 and section 1.2 Lemmas 1.6–1.8,
pp. 6–8, including the displayed quadric model and complete proofs of
1.7–1.8. In complex projective 3-space, Lemma 1.6 separates four disjoint
lines on a smooth quadric from at-most-two transversals, referring its
proof to [Ste, Lemma 6.16], which was not read. Lemma 1.7 describes the
two rulings. Lemma 1.8 treats concurrent, intersecting and disjoint
cases in its three-transversals criterion. These are comparison results
only: our inputs are projective planes in projective 6-space over
characteristic 97. No dimension reduction or characteristic transfer is
proved here; no three-point criterion is imported.

G. Medina and A. Zavadskij, *The four subspace problem: An elementary
solution*, Linear Algebra Appl. 392 (2004), 11–23,
[DOI 10.1016/j.laa.2004.05.010](https://doi.org/10.1016/j.laa.2004.05.010):
the publisher abstract advertises arbitrary-field classification, but the
full-text URL returned 403. The author-related Spanish overview at
https://repositorio.konradlorenz.edu.co/bitstreams/d7430fff-e19b-4199-b76d-4c4afb486c7a/download
also returned 403. Both are unread theorem-level leads. They are not
essential to an elementary exact attempt using the ready tools, and no
classification or exceptional case from them is assumed. The previous
complex linear-relation normal form remains outside characteristic 97.
Do not spend the next turn retrying these persistent source blockers.

## Exact search and local duplicate comparison

Queries on 2026-10-26: `four projective planes P6 common transversal lines
infinitely many Schubert intersection`; `four subspace problem common
transversals projective planes Grassmannian exceptional`; `Line Multiview
Varieties arxiv`; `The four subspace problem Medina pdf`; `transversals
four planes projective finite`. Search snippets located sources only;
the comparisons above use the inspected primary passages. No exhaustive
bibliographic search or originality claim is made.

Read L109's map definition and kernel/rank/gate discussion, C155a's
original-domain statement and L157's joint-image parameters through its
scalar-set reconstruction. Narrow statement/proof reads compared:

- L116 excludes selected fixed-pair occurrences by factor/weight gates;
  it does not bound every rank-one locus.
- L120's 223 selected rank-19 occurrences have two decomposable points
  each, over extensions; they do not cover arbitrary pairs or all ranks.
- L125 partitions 100,764 occurrences for a different fixed pair and
  explicitly preserves deficient kernels. Its factor and omission filters
  are exclusions for coding, not automatic rank-one finiteness theorems.
- L115's proof gives an entire decomposable projective plane before
  projection/weight gates. Its displayed support table has only the
  first pair disjoint: rows three/four share 12 and every cross pair
  intersects. Thus it is not the required counterfamily. Do not remove
  the second-pair restriction to reuse it.
- L119/L126/L127 give two-point decomposable loci for their named inputs;
  L122's previously assessed rank-20 examples are singletons. These
  supply fixed-label evidence rather than uniformity. Weight failure
  cannot be substituted for the target's exact rank-one conditions.

ATTEMPTS/041–043 preserve deficient kernels and surviving four-row
planes; /048 stops pair-rank stratification only; /049 stops repeated
passed audits without a compatibility conclusion. This target asks for
an exact locus-size result, so those stops do not prohibit it. Their
failure evidence is preserved. No certificate was recalculated, and no
new finite enumeration or mathematical script was run.

## Bounded approved attempt and stopping test

Keep the exact TARGET as the next action. One research turn may use
L109, C155a and L156/L157 (inheriting L155/L153) to test an explicit
exceptional-family mechanism on at most three specified eligible
quadruples, or to attempt a structural finiteness proof retaining all
special cases. Start with the actual maps and exact shared-factor
conditions, not generic enumerative counts. Do not undertake an
all-quadruple census merely to collect ranks. Save unfinished reasoning
before lengthy work.

Continue only with a proof controlling all image-line choices on the
claimed domain, or a specified eligible quadruple and infinitely many
distinct planes with all four ranks exactly one. For a parameter family,
prove identities over the parameter field and describe excluded
parameters and distinctness; base-field samples are not sufficient.
A negative outcome on one quadruple is only local. If only exterior
kernel dimensions, implicit equations or finitely many sampled planes
are obtained, report the remaining locus-size gap honestly and reassess
the mechanism under the shared exploration budget. No result is derived
in this assessment. Any changed target outside SCOPE needs separate
review; no new lemma may be derived and approved in this literature turn.

Coding use still requires q=97^20, k=8, pinned cell, U_S, nonzero actual
D/locators, sixteen events, t=0, arbitrary weights/original chart and
L056/L069/L040, L051/L055 qualifications. Retain L104/L151 limits.
Uniform twelve-row exclusion, representation, challenge identification
and radius remain open. Algebraic-closure planes need not descend to
the coding field or satisfy weight gates.

## Preserved step-497 proposal

The following is the original REVIEW_REQUIRED proposal, retained verbatim
as historical evidence. The current fields and approval are above; its
next-turn instructions are superseded by this completed assessment.

> # Proposed four-row finiteness test
> 
> TARGET: Determine whether every pairwise-linear original quadruple whose supports split into two disjoint pairs has finitely many four-row rank-one planes over the algebraic closure of F_97, or give an explicit infinite family.
> CHECKED: 2026-10-25
> DECISION: REVIEW_REQUIRED
> SEARCH_EVIDENCE: Proposed after step 497's completed L157 audit; narrowly checked L116/L120/L125 statements and retained the step-494 fixed-label comparison and ATTEMPTS/041–043,/048–049. No external search or complete duplicate comparison for this new finiteness target has occurred.
> SOURCE_EVIDENCE: L157's arbitrary-field tools are covered by the step-494/496 Kostrikin–Manin reading record; they do not by themselves establish finiteness. No primary finiteness theorem for these four actual subspaces has been inspected for this target.
> COMPARISON: L157 parametrizes fibers over image lines without bounding the number of lines. L120 gives finite loci only on its selected fixed-pair rank-19 domain; L116/L125 are restricted filters, not the proposed arbitrary-pair finiteness statement. This comparison is preliminary, not an approval or a novelty claim.
> GAP: Whether the specified rank-one locus is always finite, and whether an existing result or recorded exceptional family already settles that question, remain unassessed. No finiteness or infinite-family result is asserted here.
> REASON: Finiteness of the union over image lines is a new substantive target beyond the approved fiber bijection; a separate literature comparison must approve or redirect it before any derivation or mathematical script.
> SCOPE: L157's original H/S/J and 756 labels; four distinct supports a,b,c,d with a<b, c<d, supports a and b disjoint, supports c and d disjoint, and every other pair intersecting in at most one label; actual L109 maps, field E equal to the algebraic closure of F_97, and field-valued planes only.
> 
> The main gap remains uniform twelve-row exclusion. The proposed
> intermediate threshold is finiteness of the set of two-dimensional
> E-subspaces L of E^S with
> rank(Q_j|_L)=1 for all four selected rows. The empty set counts as
> finite. The alternative deliverable is a fully specified original
> quadruple and an infinite family of distinct planes, with all four
> rank-one conditions proved. Merely reporting a positive-dimensional
> linear exterior kernel is insufficient: decomposability and exact
> projection ranks must be checked. Finite-field enumeration alone cannot
> settle the algebraic-closure target. No uniform numerical bound,
> algorithmic tractability or coding recovery is assumed from finiteness.
> 
> A finite locus could provide finitely many branches for additional-row
> and coding-gate tests. An explicit infinite family would show that this
> rank-one subproblem requires further restrictions before such a reduction.
> The two-disjoint-pairs condition is an extra proposed restriction:
> C152a currently supplies one disjoint pair, not this extraction. Applying
> the proposed result universally to equality families would therefore
> still require a separate incidence/extraction argument. That independent
> gap is not being proved or assumed in this step.
> 
> The next turn is one source comparison, not mathematics. Reuse the ready
> arbitrary-field Segre/quotient assessments, then compare primary results
> on lines meeting four projective planes and their exceptional infinite
> families only as relevant to these actual characteristic-97 maps.
> Inspect the hypotheses and essential exceptional cases; generic or
> complex-field enumerative results do not settle the exact target.
> Narrowly check existing fixed-pair canonical loci for a matching
> counterexample before selecting a new calculation. The already inspected
> rank-19 examples are not evidence for uniform finiteness. Previously
> inaccessible pencil/four-subspace classifications remain unread leads,
> not essential inputs unless this comparison identifies a concrete need.
> 
> LITERATURE_REASON: The approved L157 audit covers fiber reconstruction,
> not finiteness as the image lines vary; this new locus-size question
> needs exact theorem and duplicate comparison. Do not repeat the completed
> audit or assume the elementary fiber sources prove finiteness. Approve
> only a bounded discriminating proof or counterfamily attempt; do not
> launch an all-quadruple census merely to gather ranks. If a local or
> primary result already settles the target, import it with its hypotheses
> instead of redoing it. No result is derived or approved in this proposal.
> 
> Essential prospective inputs: L109, C155a, L156/L157 and inherited
> L155/L153 original-domain qualifications. L116/L120/L125 are comparisons,
> not theorem inputs without further inspection. C152a/L086/L152 and L154
> remain prospective for coding applications; no cross-notebook input is
> proposed. Preserve L104 survivors, L151's label limits and all stopped
> routes. No rank-only stop is treated as a global ban on this test.
> 
> The unresolved coding assumptions remain q=97^20, k=8, the pinned
> 1/4<=delta<5/16 cell, U_S, nonzero actual D and locators, sixteen original
> finite events, t=0, arbitrary weights and original chart, together with
> L056/L069/L040 and L051/L055 qualifications. Algebraic-closure planes
> need not be defined over the coding field or pass any recovery gate.
> Uniform twelve-row exclusion, representation, challenge identification
> and sharp radius remain open. Matching Mathlib coverage is not checked.
