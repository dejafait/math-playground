# Completed coverage review — actual three-branch normalization length

TARGET: Assess coverage for determining the normalization-quotient length at a three-branch span-two collision of L118's actual image, allowing nonlinear normal jets.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched smooth-branch delta/ordinary-multiple-point and filtered restriction terminology, stronger complete-filtered surjectivity results and local duplicates; reused the inspected Leahy--Vitulli/Greuel--Pfister assessment and ATTEMPTS/070--072. Queries and inspected theorem cases are recorded below.
SOURCE_EVIDENCE: Wen-Wei Li, Yanqi Lake Lectures on Algebra Part 3, version 2026-07-05, Lemma 5.2.3, printed p. 53, statement and complete proof; Stacks 00MA, 07N9, 00MC and 0C0S, statements and full relevant proofs; Stacks 0120, strictness and associated-graded exactness statements/proofs. Direct citations below.
COMPARISON: Known complete-filtered lifting and finite-completion theorems cover the required tools; L122 covers all degrees of the linear arrangement. None of the inspected sources identifies the actual restriction image under the present hypotheses. Their specialization must verify the nonlinear map's graded pieces and completion descent rather than assume simultaneous linearization or strictness.
GAP: The actual length-four transfer, including the full higher-order tail, first-jet image and algebraic length comparison, remains unproved. This review supplies source coverage for one bounded attempt, not a normalization-length theorem.
REASON: Essential tool coverage is now available without the parked all-orders source. Attempt the exact nonlinear local-ring comparison in a separate research turn; do not reprove general lifting or completion theorems.
SCOPE: Exactly three smooth branches of L118's actual image, distinct quaternionic tangent lines spanning quaternionic dimension two in ambient dimension 39, with L120/L121 and the full retained conditional F hypotheses below; arbitrary nonlinear holomorphic normal jets are allowed.
COVERED_TARGET: Determine the normalization-quotient length at a three-branch span-two collision of L118's actual image by complete filtered restriction, allowing nonlinear normal jets.
LITERATURE_REASON: The changed actual-image target needs complete filtered lifting and finite-completion hypotheses not covered by L122's flat calculation or L124's ready derivative assessment.

This completes the literature assessment only. The separate L124 audit's
outcome is preserved. No calculation, specialized local-ring theorem or
new lower bound is established here. The newly ready covered continuation
is subject to the supervisor's separate next-turn approval; this turn does
not invoke it.

The main gap remains universal primitive rational Hodge realization.
The intermediate question is the length of the actual image's normalization
quotient at a point with exactly three preimages and quaternionic tangent
span two. It could make the local image-gluing contribution usable in
subsequent global coherent-sheaf bookkeeping; an exclusion of F or a
complete Hodge route is not supplied. Common F, actual collisions and
transport remain independent gaps.

Essential inputs for the proposed comparison are L118's holomorphic
quaternionic immersion, L120's finite birational normalization, L121's
distinct tangent lines and reduced ordered coincidences, and L122's
canonical flat length-four countermodel. Retain the conditional rank-two
locally free Omega-polystable F, integral c_1=0,
ch_2=-14e_1-21e_2-tau_D on identical marked K3 factors, scale c=2lambda,
ambient quaternionic dimension 39, and exactly three preimages at the
chosen image point. No simultaneous holomorphic linearization, curvature
invariance of their span, or absence of nonlinear exterior normal jets
may be assumed. Other collision multiplicities are outside this target.

The new mechanism to assess is the filtration of the completed image
restriction map into the product of its three smooth branch rings:
compare its complete cokernel with the tangent-union calculation, retaining
all nonlinear corrections. Look for known multiple-point/normalization
delta-invariant or filtered local-algebra results, stronger statements and
counterexamples, and check exact smooth-branch and tangent hypotheses.
The discriminating target is a rigorous exact length-four transfer under
these hypotheses versus a counterexample or an explicit additional jet
condition preventing that transfer. L122's flat proof alone is insufficient
source coverage for this actual-image target; no novelty is inferred.

ATTEMPTS/070's failure of the smaller length r-1 remains evidence and is
not reopened: the proposed comparison retains its flat length-four model.
ATTEMPTS/071's order-zero conditions remain separate. ATTEMPTS/072's
full first-derivative range stays parked; changing derivative values or
angles is not the proposed mechanism. Do not retry the inaccessible
all-orders source, which is not needed to formulate this local-ring test.
Full matching Mathlib coverage has not been checked.

## Primary tools and exact applicability boundaries

[Wen-Wei Li, *Yanqi Lake Lectures on Algebra, Part 3*, version
2026-07-05, Lemma 5.2.3, printed p. 53, PDF p. 58](https://www.wwli.asia/downloads/YAlg3.pdf#page=58)
assumes a filtration-preserving module map, complete source, Hausdorff
exhaustive target and surjective associated graded map. It concludes
surjectivity. Read its whole proof: corrections have successively higher
order, their sum converges in the source, and separatedness identifies
its image with the prescribed target. This is the complete-filtration
tool; it imposes no finite-generation condition on those modules.
The proposed use is on the order-at-least-two restriction map, after
checking every graded component. This application has not been performed.
No convergence of analytic interpolating series is supplied by this
formal lifting theorem.

[Stacks, Lemma 10.97.1 (00MA)](https://stacks.math.columbia.edu/tag/00MA)
assumes a Noetherian base, an ideal and finite modules. Completion
preserves their short exact sequences and is tensoring with the completed
base. Read its complete proof, including the Artin--Rees comparison of
the induced and adic filtrations. The intended finite modules are the
actual local image ring, its finite normalization and their quotient;
identifying that completed quotient with a cokernel of the proposed
restriction map remains part of the research task.

[Stacks, Lemma 10.97.8 (07N9)](https://stacks.math.columbia.edu/tag/07N9)
assumes a finite ring map over a Noetherian ring. Completion over a prime
is the product of the maximal-ideal completions above that prime.
The entire proof was read: localization, Artinian quotient decomposition
and inverse limit, with equivalence of the relevant local adic topologies.
L120 supplies a finite normalization, so no theorem asserting that an
arbitrary normalization commutes with completion is needed or imported.
Exactly three preimages must still be retained when setting up the map.

[Stacks, Lemma 10.97.3 (00MC)](https://stacks.math.columbia.edu/tag/00MC)
gives faithful flatness of Noetherian completion when the ideal is in
the Jacobson radical, in particular at a local maximal ideal. Read its
flatness/residue-field proof. It supports descent of a finite-module
statement after the relevant module and map have been identified; it
does not assign a length by itself.

[Stacks, Lemma 10.160.10(2) (0C0S)](https://stacks.math.columbia.edu/tag/0C0S)
identifies a complete Noetherian regular local ring with a power-series
algebra over a coefficient field mapping isomorphically to the residue
field. Read its parameter-map surjectivity and dimension/injectivity
proof. Here the coefficient field is C. The smooth ambient germ and
individual smooth source branches supply the intended regular rings;
the singular image ring is not asserted regular. Holomorphic immersion
charts in L118 supply the individual branch maps, but do not linearize
them simultaneously.

[Stacks, Section 12.19 (0120), Definition 12.19.3 and Lemmas
12.19.12--13](https://stacks.math.columbia.edu/tag/0120) distinguishes
induced and quotient filtrations and strictness. Its finite-filtration
proofs were read. It supplies no unconditional equality between the
associated graded image and the image of the associated graded map.
In particular the intrinsic maximal-ideal filtration of the singular
image cannot silently replace branchwise order. These results are a
warning and bookkeeping reference; Li's theorem supplies the complete
lifting step.

The earlier completed
[normalization-quotient assessment](2026-10-17-opposite-image-normalization-quotient.md)
already inspected Leahy--Vitulli's simultaneous-union hypotheses,
the correction, and Greuel--Pfister's isolated nonnormal delta definition
and finiteness lemma. Reuse those readings. Their multicross length
r-1 does not cover this target, as L122 demonstrates. No general
seminormality criterion or curve delta formula is reproved or extended
to surfaces in this review.

## Search record and duplicates

External queries included `smooth branches delta invariant union tangent
spaces nonlinear higher dimension three planes normalization length`,
`filtered modules surjective associated graded map complete filtration
strict morphism Stacks project`, `complete filtered modules associated
graded surjective morphism Bourbaki proposition`, `delta invariant smooth
branches tangent surface`, `normalization three smooth branches length`,
and `ordinary multiple point surfaces normalization`.
The branch searches chiefly returned curve results or previously assessed
multicross criteria; no exact matching theorem was identified. Curve
search hits were discovery leads, not evidence for a surface length.
This bounded search establishes no novelty.

The Serre *Local Algebra*, II.A, Proposition 6 search lead was not
successfully opened: the web PDF request failed and a shell download
failed DNS resolution. Do not count its snippet as a theorem reading.
Li's author-hosted full statement and proof remove the essential access
gap; the proposed application does not depend on recovering Serre's PDF.
The previously inaccessible all-orders hypercomplex source was not retried.

The local comparison read L118/L120/L121's exact hypotheses and
conclusions and L122's complete all-degree restriction argument. Searches
were limited to the relevant recent local assessments, ATTEMPTS/070--072
and selected histories. No duplicate nonlinear transfer assessment was
found there. L122's degree-zero and degree-one defects and surjectivity
in every degree at least two are established only for its flat model.
ATTEMPTS/070's r-1 failure stays closed. The independent curvature stops
in ATTEMPTS/071--072 are neither inputs to this local-algebra test nor
reopened by it.

## Separate mathematical continuation and stopping test

The covered target is exactly the single COVERED_TARGET line above.
Set up the actual completed ambient restriction map into the three
completed smooth branch rings. Keep the branchwise maximal-ideal
filtration and all nonlinear coefficients. The finite normalization
and smooth branches must be justified using L118/L120/L121 before
comparing this cokernel with the actual normalization quotient.
L122 is the interpolation input for the tangent configuration, not an
identification of the nonlinear local rings.

The bounded attempt should check the change of tangent coordinates,
identify the graded restriction maps, test the complete order-two tail
with the cited lifting theorem, and compare the remaining first jets
and original algebraic length. These are work requirements, not results
proved here. Full linearization, equality of tangent-cone ideals,
unproved strictness and finite-jet extrapolation are forbidden shortcuts.

Continue the exact length-four transfer only if those checks succeed
for every allowed nonlinear jet. Otherwise retain the explicit failed
graded component, counterexample or missing jet hypothesis and abandon
the unconditional transfer for this target. There is no need to seek a
second lemma or to revisit curvature interpolation. Any resulting local
length would still be conditional on an actual collision and F; it
supplies no collision, global cohomological exclusion, common kernel,
cycle, transverse transport or primitive Hodge realization by itself.

This review is LITERATURE / REPRODUCTION. It adds usable source coverage
for a specialization of known tools and claims no mathematical result
beyond those sources or certified originality. Full matching Mathlib
coverage remains not checked. The proof attempt belongs to a later turn.
