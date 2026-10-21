# Primitive thirteen-adic two-descent image — completed source comparison

TARGET: Determine the exact primitive whole-fiber two-descent image at thirteen for L033's 54a1 algebra, retaining the common scalar and all field identifications.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed exact-family, standard local-Kummer and stronger good-reduction searches; compared L064/L066/L069, ATTEMPTS/029/038 and the ready primitive-eleven/dyadic assessments. No inspected theorem computes this correlated thirteen-adic set; queries, primary sources and remaining differences appear below, without a novelty claim.
SOURCE_EVIDENCE: Inspected BPT arXiv:2001.02263v3 Section 1, especially Definition 1.6, Theorem 1.8 and Corollary 1.9; Bruin–Stoll March 14 2008 manuscript Remark 2.1, Section 4 Lemmas 4.3–4.4 with proofs and all local algorithm cases, Section 9; FNS June 10 2019 Section 7.2 pp.25–26; Stacks 04GK statement and proof. Reused L064's assessed Clark/Milne lifting inputs.
COMPARISON: Known good-reduction equality describes the unrestricted Kummer image, not realization by entire fibers with common primitive witnesses. Finite-etale residue lifting and full-cubic square-class methods cover the proposed specialization; branch-residue fibers require explicit local proof rather than automatic use of etale lifting.
GAP: Essential method coverage is ready; exact scalar coverage, branch and exceptional cases, complete fiber identifications, simultaneous primitive realizations and the resulting restricted image remain unproved. No local strictness, subgroup, independent global restriction or dimension improvement is established.
REASON: Approve one subsequent REPRODUCTION attempt on the unchanged target using cited inputs; additional-filter equality stops this local mechanism, while properness still needs a separate global comparison. No general theorem needs reproof.
SCOPE: Exactly TARGET over L064's entire unramified degree-twelve field, L033/L034's modular map and L069's fixed cubic generator, using complete local residue/lifting and square-class methods; no global class backend, probe enlargement or rank conclusion.
LITERATURE_REASON: The gate explicitly required coverage for a different prime and connecting map; earlier five-isogeny membership and dyadic/eleven-adic assessments did not cover this exact restricted image.

## Proposed scope and relevance

The main gap remains positive primitive integer emptiness. The
intermediate target is the exact two-descent image of the tautological
points from all whole-fiber isomorphisms B_s -> A13, where A13 is
L064's entire K tensor Q13, one unramified degree-twelve field. Use
L033/L034's same modular map, L069's distinguished theta and class
[4x-theta], with the standard exceptional evaluations retained.
Require one common nonzero primitive triple a,b,c in Z13 with
a^3+b^4=c^11 and s=1728a^3/c^11, as in L064. Do not select field
factors or unrelated local points. Determine rather than assume the
role of any excluded or exceptional scalar.

A proper restricted image could supply an additional necessary test
for primitive classes in L084's T. This would still require a separate
global comparison to prove any independent restriction or dimension
improvement; a local set need not be a subgroup. If established known
results already force equality with the unrestricted local image, import
that conclusion with its applicability argument and retire this filter.
Neither outcome would bound full rank or settle integer lifting.

The continuation/abandonment test is first source-level: identify a
precise theorem or a justified finite residue/lifting method covering
the entire restricted image, including all identifications and exceptional
points. If a known equality or obstruction settles the target, use it;
if coverage is missing, do not calculate. If a later approved computation
proves equality, stop this particular additional-filter mechanism. A
proper image alone is not global independence.

Essential local input IDs are L033, L034, L064, L066, L069 and L084.
Their ready source assessments are reused where applicable; the exact
local two-descent theorem comparison is completed below.
No cross-notebook input is proposed. L064/ATTEMPTS/029's five-isogeny
survivor remains intact; this proposal does not reopen its removal.
ATTEMPTS/038's fixed reciprocity test and the exhausted affine and
uncertified class-backend routes remain stopped. No new image,
mathematical lemma or script has been derived for this proposal.

Mathlib coverage for a full matching image theorem and supporting
finite-field, good-reduction and Kummer results: not checked.

## Primary statements and comparison completed 2026-10-17

**Barrera Salazar–Pacetti–Tornaría**, *On 2-Selmer groups and quadratic
twists of elliptic curves*,
[arXiv:2001.02263v3, September 17 2020](https://arxiv.org/pdf/2001.02263v3),
Section 1 pp.3–6. Lemma 1.3 gives the unrestricted image order
[O:2O]|E(F)[2]| for finite F/Q_p. Definition 1.6 requires an integral
monic square-free cubic and one of four alternatives: cubic field;
maximal polynomial order; odd residue characteristic with odd
nonsingular-reduction index; or unramified dyadic base with good
reduction. Theorem 1.8 gives norm-square unit containment; Corollary
1.9 gives equality in odd residue characteristic. Inspected all split,
quadratic-factor and field proof cases and the corollary's cardinality
argument. Here L069's model has unit discriminant at thirteen, and
L066 certifies good curve reduction, so the odd-characteristic
good-reduction alternative applies. This imports the unrestricted
comparison theorem only; it says nothing about the primitive
whole-fiber restriction. No unrestricted cardinality or cubic splitting
at thirteen has been calculated in this turn.

**Bruin–Stoll**, *Two-cover descent on hyperelliptic curves*, Math.
Comp. **78** (2009), 2347–2370,
[March 14 2008 author manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/twocoverdescent.pdf).
Inspected Remark 2.1 p.3, Section 4 pp.6–10 and Section 9 p.15.
Odd degree uses the entire algebra modulo squares, without scalar
quotient. Root evaluations use (a−theta)+h(theta) for f=(X−a)h;
monic infinity has identity value. Lemma 4.3 assumes odd residue
characteristic, unit leading coefficient and discriminant valuation
at most one; equality additionally requires valuation zero and its
stated residue-size bound. This concerns unrestricted points.
Lemma 4.4 assumes irreducible h, integral x0, e>=0 and
ord(h(x0+epsilon*pi^e)−h(x0))>ord(h(x0)); it gives class constancy on
x0+pi^(e+ord(4))O. Its proof, recursion termination, square
realization tests, linear-root neighborhoods, reciprocal chart and
infinity cases were read. These cover local square-class calculations,
not automatic preservation of the common-scalar condition. Section 9
identifies the monic-cubic genus-one construction with usual two-descent.
The specialized constancy inequalities and restricted realizations
must therefore be proved, rather than sampled.

**Freitas–Naskręcki–Stoll**, *The generalized Fermat equation with
exponents 2, 3, n*, Compositio Math. **156** (2020), 77–113,
[June 10 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.25–26, inspected: whole-fiber transport via
the twelve cyclic subgroups, modular formula, branch points
0,1728,infinity and the explicit boundary where global Selmer
computations assume GRH. Its subsequent dyadic results, already
assessed for L082, are not thirteen-adic image theorems. The conditional
classification and stored global Selmer data are not imported.

**The Stacks Project**, [Lemma 10.153.7, tag 04GK](https://stacks.math.columbia.edu/tag/04GK),
live statement and full proof inspected 2026-10-17: finite etale
algebras over a henselian local ring are equivalent to finite etale
algebras over its residue field, including morphisms. Apply over
Z13 only after verifying that the relevant entire integral fiber is
finite etale. This covers all identifications on such a fiber, not a
selected root or a repeated polynomial reduction. L064's ready
[membership assessment](2026-10-13-thirteen-adic-canonical-class-membership.md)
supplies the inspected Milne unramified-extension and Clark strict
Hensel inputs. Their statements need no reproof. L066's chart
certificate supplies the integral map; good map reduction alone does
not imply that every specialized fiber is etale.

## Search, duplicates and bounded continuation

Actual web queries included `elliptic curve 2 descent local image good
reduction odd prime unramified Kummer Barrera Pacetti Tornaria`,
`"54a1" "13" descent Freitas Stoll`, `"X0(11)" "two-descent" local image`,
`"54a1" "thirteen" descent`, `"X0(11)" "13-adic" "descent"`,
`"primitive" "whole-fiber" "two-descent" thirteen`, and
`"two-cover descent" good reduction finite residue local image`.
Useful primary matches were the sources above; unrelated results and
snippets are not theorem evidence. The initial mistyped Bruin–Stoll
URL `twocov.pdf` failed; the correct author PDF was fully accessible.
There is no continuing source blocker and no inference of novelty
from unmatched exact phrases. No additional source lead is essential.

Local duplicate comparison used the hypotheses/conclusions and relevant
source ranges of L064/L066/L069, ATTEMPTS/029/038, and the ready
[primitive-eleven assessment](2026-10-17-primitive-eleven-two-descent-image.md)
and [primitive-dyadic assessment](2026-10-16-primitive-dyadic-two-descent-image.md).
L064's same-class witness concerns fifth powers. ATTEMPTS/038's
obstruction concerns the fixed reciprocity probes. Neither decides this
image; neither stop is reopened. The affine and uncertified class
backend remain parked. No cross-notebook input is used.

One bounded mathematical attempt may now determine the unchanged exact
set. It must account for every primitive scalar valuation pattern,
including neighborhoods of 0,1728,infinity, and the removable x=16
chart. Exclude a domain only by a uniform argument; if a finite
residue reduction is claimed, prove its completeness. Use complete
fiber reconstruction and all field identifications, fixing theta
throughout; handle two-torsion by the cited exceptional evaluation.
Each reported class must have an exact whole-fiber realization with
one common nonzero primitive triple, and every admissible point must
be covered. Do not infer restricted equality from unrestricted
good reduction, or use a residue table as proof of branch coverage.

Continue toward a separate global comparison only if a proper local
image is proved. Equality with the unrestricted image stops this
additional filter. An unresolved branch or realization case yields
an honestly partial attempt, not an exact image. Even a proper image
leaves independence on L084's T, the localized class kernel, useful
dimension bounds and integer lifting unresolved. No new mathematics,
lemma or mathematical script was produced in this literature turn.
