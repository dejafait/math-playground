# Fixed minus-three genus — critical-audit source coverage

TARGET: Critically audit L106's fixed-field marked model, geometric connectedness and normalization genus 75 against its complete ramification certificate.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-polynomial and fixed-field comparison in drafts/literature/2026-10-20-global-rational-quadratic-fiber-genus.md; read complete L106, its attempt note, history/361–362 and ATTEMPTS/045 plus ATTEMPTS/046-minus-three-joint-factor-at-seven.md; no broad repeat search.
SOURCE_EVIDENCE: Reinspected Jones arXiv:1209.5169v1 Theorem 1.1 p.1/comment 5 p.2; Stacks 58.6.2, 53.8.2, 53.12.2/4 and 53.18.2 statements and relevant proof passages; reuse Milne LEC v2.21 Theorems 3.1/21.3 pp.27/130–131 from the prior assessment.
COMPARISON: The inspected cover and genus theorems cover the audit methods, but do not certify this marked model, its actual monodromy, descent or finite certificate; these instance-specific obligations remain for a separate proof audit.
GAP: Independent critical verification of L106 and complete certificate replay remain undone; no essential source gap was found for that bounded audit.
REASON: Approve this newly selected audit scope using existing primary coverage; this literature turn neither performs the mathematical audit nor certifies genus 75.
SCOPE: Exactly TARGET; inspect all model, group, closure, constant-field and ramification claims and repair a demonstrated defect if necessary; no rational-point classification, other marking field or integer elimination.
LITERATURE_REASON: The newly selected audit had REVIEW_REQUIRED coverage; compare its precise hypotheses with the already inspected sources before routing to mathematics.

## Gap, use and stopping test

The main gap remains primitive integer elimination in both L095 systems
and compatibility of global factors, within the larger unresolved Beal
target. The intermediate target is independent verification of L106's
fixed-field geometry. Reliable geometry could guide a later rational-point
method; it supplies no point classification by itself.

Continue only if the exact marked model, unique geometric component,
degree 990 and normalization genus 75 withstand independent review of all
load-bearing reasoning and the complete evidence. Otherwise record the
precise correction or obstruction. Do not silently substitute an unmarked
quotient, an arithmetic genus or a different quadratic field.

## Primary theorem comparison

Jones, *Primitive permutation groups containing a cycle*,
[arXiv:1209.5169v1](https://arxiv.org/pdf/1209.5169v1), Theorem 1.1 p.1,
requires a primitive finite permutation group containing a prime-length
cycle fixing at least three points. Comment 5 p.2 relates branch cycles
to monodromy. Audit these premises on the actual cover; individual stored
cycle representatives cannot establish them. The PDF still bears the
v1 date 24 September 2012 and internal date 27 November 2024. The later
classification theorem is unnecessary; Jordan is imported, not reproved.

[Stacks Theorem 58.6.2, tag 0BND](https://stacks.math.columbia.edu/tag/0BND)
identifies finite étale covers of a connected scheme with finite
fundamental-group sets. Its fiber-functor statement and proof support the
component/orbit framework. Reuse Milne's comparison in the prior assessment:
*Lectures on Étale Cohomology*, v2.21, 22 March 2013, Theorems 3.1 and 21.3,
pp.27 and 130–131, [author PDF](https://www.jmilne.org/math/CourseNotes/LECc.pdf).
Apply to the branch-deleted smooth cover. Its applicability to the displayed
coefficient equations and distinct-root locus must be checked separately.

[Stacks Lemmas 53.12.2/4, tag 0C1B](https://stacks.math.columbia.edu/tag/0C1B)
require a generically étale morphism of smooth proper curves and both global
function fields of constants equal to the base field. They express genus
through the different, with multiplicity e−1 precisely in the tame case.
The audit must justify the proper normalized model, full constants and all
branch contributions, including infinity; characteristic zero supplies
tameness once that setup is established. Cycle lengths must be related to
local ramification on that normalization. No guessed passport is sufficient.

[Stacks Lemma 53.8.2, tag 0BY6](https://stacks.math.columbia.edu/tag/0BY6)
preserves genus under field extension for a proper dimension-one scheme
with H0 equal to the ground field; its proof uses cohomology base change.
[Stacks Lemma 53.18.2, tag 0CE0](https://stacks.math.columbia.edu/tag/0CE0)
preserves geometric genus under reduction and normalization; its proof
compares component function fields on dense opens. These statements do not
establish geometric integrality or constants for L106. Audit those claims
before applying them. Mathlib coverage remains not checked.

## Evidence and duplicate/failure controls

Read L106 in full for source-scope comparison, without deciding its proof.
The script's certificate fields include all ordered labels, induced actions,
disjoint cycles, partition checks and failures. No script was run and no
certificate arithmetic was verified in this literature-only step. Next
turn must inspect and independently replay the complete load-bearing data;
a bounded preview or the reported 857 checks is insufficient verification.

Essential inputs are L106, scripts/global-fiber-genus/certify.py and its
complete certificate.json. L095 is needed only if discussing retained
integer conditions; it is no premise of the standalone geometry claim.
Check the coefficient model in both directions, embedding involution,
base-change isomorphism, finite étale descent, prime-degree primitivity,
Jordan applicability, actual branch generation, triple transitivity,
closure and constant fields, then full induced cycle counts. Do not infer
a branch-generator relation for the independently chosen representatives.

ATTEMPTS/045's class-backend park and ATTEMPTS/046's exact seven-adic
witness concern different mechanisms and remain preserved. The prior
assessment found no inspected classification supplying this exact geometry;
that is neither a novelty certificate nor a reason to repeat discovery.
Rational points, L095 powers/gcd/positivity, the minus-eleven branch and
remaining global factors stay open downstream. No lemmas, mathematical
scripts, PROOF.md or DAG.md changed. This assessment approves the separate
next-turn audit and does not approve its mathematical conclusion.
