# Finite supported graph mass descent — prepared specialization

TARGET: Test whether a smooth radial-graph deformation of a minimizing coordinate torus yields B<B_tor and the universal bound K>=-B in L868's unchanged actual-F class, with its variation supported off F=0.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed the post-first-jet three-mechanism comparison and specific local/web duplicate searches recorded in 2026-11-06-post-first-jet-global-period-discovery.md; known local mass stationarity is relevant, but no completed actual-G best-coordinate-torus comparison was located. No novelty claim.
SOURCE_EVIDENCE: Lawrence-Yamauchi 2311.13002v2 Section II B (11)-(16), pp3-4, complete necessary-stationarity argument inspected; reuse L847's assessed compact Laurent/Stokes inputs and Guillemin-Sternberg Sections13.13-13.14 pullback differentiation from the collar-preserving assessment. Exact scope below.
COMPARISON: The general necessary stationarity condition is known; the intended specialization must establish coordinate-torus attainment, varying phase, an allowed supported radial descent and the one-sided bound in the actual-G problem. Neither local perfection nor abstract convex duality supplies these application steps or the sharp threshold.
GAP: Obtain a strict improvement over the infimum over all coordinate tori, or a precise failure of a stated obligation. A decrease from one nonoptimal torus is insufficient; even B<B_tor need not yield B=|M|.
REASON: Finite supported descent uses full domination away from the diagonal without a moving trace limit, normal filtering, prescribed phase inverse or global flow. This new ready continuation requires separate approval before mathematics.
SCOPE: Exact L847 actual entire G, positive R,C, full F and omega; all L868 global real C1 periodic admissible triples; arbitrary finite coordinate radii, smooth real periodic radial test graphs and fixed angular orientation. No growth, summability, zero simplicity, uniform collar, C2 on the admissible triple, perfect graph or RH premise.

## Exact proposed mathematical test

Let B_tor be the infimum, over x in R2, of the normalized absolute
integral of omega on the coordinate torus z_j=R exp(x_j+i theta_j).
This is the existing quantity in L868(11), not a new bound. Let B be
the normalized absolute integral on a proposed smooth radial test
graph, using L847's complete pullback including det(I-iDu).

First establish whether B_tor is attained at finite radii. Then test
for one smooth real angularly periodic variation of such a minimizing
torus whose support is compactly contained in a zero-free angular
patch, and one finite parameter for which B<B_tor. Prove the universal
inequality K>=-B for every original admissible q,r,h, if that graph
exists. None of these claims is established by this assessment.

Essential inputs are L847 and L868. C868a/b/c identify the unresolved
mean/period and the relaxation's scope; L872/L873 are recorded failures
to avoid, not inputs licensing a limit. Use the existing entire power
series with positive ordinary coefficients from L847, with all its
normalizations. No cross-notebook result is involved. No prescribed
local branch, seed graph or L850 right inverse is an input.

## Known inputs and unproved application obligations

Precise primary reference for the necessary stationarity condition:
Scott Lawrence and Yukari Yamauchi, *Convex optimization and contour
deformations*, arXiv:2311.13002v2, PDF dated 14 August 2024,
[Section II B (11)–(16), pp3–4](https://arxiv.org/pdf/2311.13002v2#page=3).
The complete relevant argument was read in the parent assessment.
Do not import a sufficiency assertion, a global logarithmic action,
flow convergence, strong duality or contour attainment. Specializing
the local first-variation argument is necessary because of radial
variation constraints and the global density zeros; this is not a
request to reprove a general variational theorem.

Reuse the standard smooth pullback differentiation input in
`2026-11-06-collar-preserving-linear-phase-correction.md`:
Guillemin–Sternberg, *Semi-classical analysis*, manuscript dated
13 January 2010, [Sections13.13–13.14.1, (13.7)–(13.9), pp449–455](https://math.mit.edu/~vwg/semiclassGuilleminSternberg.pdf#page=449).
It applies to smooth parameterized maps and smooth forms, without
nonvanishing. Use only differentiation, not Moser existence. A direct
graph specialization is allowed if needed to check signs/support;
L850's proof passage is existing overlap, not a new identity to claim.

For compact coefficient operations and holomorphic identity/uniqueness
reuse the inspected inputs of L847: Lebl, *Guide to Cultivating Complex
Analysis*, v1.10, Theorem2.4.7 pp49–50, Theorem3.3.8 p79 and
[Theorem4.4.2, pp104–107](https://www.jirka.org/ca/ca.pdf#page=104).
For C1 Stokes reuse Lebl, *Tasty Bits of Several Complex Variables*,
v4.4, [Appendix C Theorem C.6 and following remark, p224](https://www.jirka.org/scv/scv.pdf#page=224).
The test graph and homotopy are compact, smooth and inside X=(C*)2;
the certificate remains only C1. Verify these hypotheses for any actual
construction. Standard continuity/compactness does not prove radial
coercivity; that remains an application obligation.

Full domination must be used at points of the actual deformed graph.
A support disjoint from F=0 is a choice of test variation, not removal
of any original divisor or addition of a zero-free hypothesis to the
admissible class. Justify local logarithms and Jacobian invertibility
only where needed; leave the rest of the graph, including all its
zeros, untouched. No normal convolution of q,r,h is permitted by this
assessment. No global equality-solving or second derivatives of the
admissible triple may be silently introduced.

## Use, acceptance and stop

A bound with |M|<=B<B_tor would sharpen the existing whole-class
period restriction and test a quantitative global mechanism. The
required no-gain threshold is B=|M|. General graph existence, possible
strict gain for a different certificate class, growing-order mixed
positivity and Xi/RH transfer remain unresolved even if the test passes.

Accept only a proved strict comparison with the best coordinate-torus
value and its valid universal period consequence, or an informative
obstruction to an exact application step. A merely conditional bound,
a formal negative derivative without finite descent, or a decrease from
an arbitrary radius does not meet that acceptance test. Preserve partial
reasoning and require new input before repeating an inconclusive test.
No numerical ansatz expansion is prescribed. Mathlib full matching and
supporting coverage is unchecked; no absence claim is made.

This is a prepared SPECIALIZE continuation, awaiting separate next-turn
approval. It authorizes no mathematical conclusion in the source turn.
If later approved, classify known specialization honestly as
REPRODUCTION, unless the actual assessed scope warrants another label.
