# Collision boundary degree: completed source comparison

TARGET: Assess a boundary-degree test for F(w,t)=(G(w,t),G_t(w,t)) on [1,3/2] x [40,45], seeking a certified nonzero signed collision count from all four boundary sides, and determine whether an analytic boundary certificate can avoid the blocked numerical backend.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step442 inspected primary degree/sign-covering results and the actual-family collision passage, reusing reviews423/429/435 and the Pólya census method comparison; exact queries and read ranges below. No adequate analytic boundary certificate was identified; no novelty inference.
SOURCE_EVIDENCE: Franek–Ratschan arXiv1207.6331v3, Definitions2.3/2.6/2.7, Theorem2.9/proof pp8–10, Theorem3.6 p18; Brezis Degree theory: old and new, Section1/(1.1)–(1.8), Lemma1/Property1 pp1–4; Lagarias–Rains math/0104176v5 Section8/Lemma8.1/full proof p44. Primary links and scope below.
COMPARISON: Standard degree theory covers continuous real maps conditional on boundary exclusion and certified oriented boundary data; it supplies no actual-theta margin. The interval algorithm still needs a convergent enclosure evaluator. The numerical collision passage is not an all-side certificate. Park this specific boundary-degree nomination, not degree theory or all analytic alternatives.
GAP: Neither a positive boundary lower bound nor winding integer is known. No independently controlled approximation with error smaller than its boundary separation is identified. Individual signed events additionally require regularity at every common zero; a nonzero degree would give neither their common sign nor global transport.
REASON: New theorem-level comparison identifies the exact retained data obligation and no source-supported escape from the evaluator/sign bottleneck. Complete this literature-only step without a generic degree lemma or backend retry, and route to an already covered independent audit.
SCOPE: Completed comparison only for the exact saved target. EXPLORE records the bounded search, not approval of a boundary calculation: no concrete independent boundary estimate was found. The original nomination below is historical. Reopening requires changed signed approximation/evaluator evidence and its assessment.

LITERATURE_REASON: Changed observable and hypotheses: an oriented common-zero
census of (G,G_t) needs primary boundary-degree and nondegeneracy coverage
not supplied by the Mellin audit or the previous enclosure contracts.

The intended bounded test, after coverage, concerns F on the four
sides of R=[1,3/2] x [40,45]. Fix coordinate order (w,t) and positive
boundary orientation before interpreting any degree. Require a
certified positive lower bound for ||F|| on the entire boundary,
including corners, and a rigorous winding value. A nonzero integer
would be the event-existence threshold. To interpret it as a signed
sum of ordinary collisions additionally require isolation and the
actual hypotheses of the degree theorem at every interior common
zero; G_w!=0 and G_tt!=0 are not presently known. No formula for that
sum or its orientation is being established here. Zero degree need
not exclude events, and an unresolved boundary box proves nothing.

Continue only if the primary source matches this actual real map and
the review identifies a concrete independent boundary estimate with
all errors retained. Do not approve merely the abstract degree
identity with unspecified boundary values. If the only available
certificate requires the same unavailable backend, assumed absence
of boundary events, or the desired interior sign, park this specific
nomination and record that precise obstruction. Do not produce a
routine degree lemma simply to prolong the route.

Reuse C999g's normalized family and C999h's smooth real representation;
L018/L019 fix the inherited Xi slice. C999i is a checked optional
correction input, not evidence for a degree. C999f is not a premise.
The current main gap is L030-L032/C032a actual-Xi positivity, with
L966/L968 forcing, L984(H) and the C997s integrated bridge separate.
Event existence, multiplicities, initialization, all other heights
and global transport remain open. No cross-notebook theorem is needed.

For the duplicate/failure comparison, inspect only the relevant parts
of review423's fixed-slice target and stop425, review429/stop430's
mixed determinant, review435/stop436's signed jump budget, and stop439's
backend failure. The search also identified the local
2026-11-05-polya-certified-event-census assessment as a possible source
method lead, not an input theorem for the actual theta-power family.
The unrelated polynomial homotopy has different functions; its
coefficients, certificates and positivity are not transferable here.
Preserve stops427/429 and all earlier evidence. No substantive overlap
assessment for this new target is claimed complete.

A central creative proof attempt is not ready at this checkpoint:
no independent boundary certificate has been identified. This next
turn prepares coverage for a candidate mechanism; it does not label
a standard degree specialization creative to meet a scheduling target.
Full matching Mathlib coverage is not checked and remains unknown.

## Completed source comparison — step442, 11 November 2026

The preceding nomination is retained as history. The main gap remains
L030–L032/C032a actual-Xi positivity; L966/L968 forcing, L984(H) and
the C997s integrated bridge remain separate. A nonzero degree in this
one rectangle could establish event existence and, with regularity,
a net orientation useful for investigating decreasing-w transport.
It would not establish the sign of every event or transport to w=1.

### Primary theorem scope actually inspected

[Franek–Ratschan, arXiv:1207.6331v3](https://arxiv.org/pdf/1207.6331v3),
*Effective Topological Degree Computation Based on Interval Arithmetic*:
Section2.1/(1), p4, gives the determinant-sign sum for a smooth map
at a regular value outside the boundary image. Definition2.3, p5,
fixes induced face orientations. Definitions2.6–2.7, pp6–8, require
inclusion enclosures shrinking with box diameter and a strict component
sign on each boundary box. Theorem2.9 and its full proof, pp8–10,
show how a sufficient sign covering determines degree; inspected the
one-dimensional base, component reduction and insufficient-data case.
Theorem3.6, p18, guarantees algorithmic termination conditional on
interval computability and boundary nonvanishing; read its statement
and base/reduction proof cases, not all implementation lemmas. Neither
the theorem nor the combinatorial stage constructs the needed theta
evaluator. Its insufficient-data argument concerns general continuous
maps, not a counterexample within the theta family.

[Brezis, *Degree theory: old and new*, author PDF](https://sites.math.rutgers.edu/~brezis/PUBlications/149.pdf),
Section1, pp1–4: (1.1)–(1.3) fix winding and determinant conventions;
Lemma1/Property1 give stability and homotopy invariance; (1.7)–(1.8)
relate domain degree to the normalized boundary map. Read this entire
introductory scope. Its ball formulation does not itself calculate a
rectangle certificate; the cubical theorem above covers the rectangle
directly. Boundary nonvanishing is a hypothesis, not a consequence of
entireness. For our intended convention use domain coordinates (w,t),
target components (G,G_t), and positive boundary traversal through
(1,40), (3/2,40), (3/2,45), (1,45), (1,40). Changing one orientation
changes a signed interpretation. No value of the degree is inferred.

[Lagarias–Rains, math/0104176v5](https://arxiv.org/pdf/math/0104176v5),
Section8/Lemma8.1 and full proof, printed p44, explicitly use numerical
tracking for the two zeros near heights42.04 and42.90, including the
w=3/2 slice. No validated error bound, four-side nonvanishing estimate,
or winding certificate is provided there. The final published version
[AIF53(2003), pp56–57](https://www.numdam.org/item/10.5802/aif.1939.pdf#page=57)
was also inspected at this passage; its PDF text extraction garbles
some formulas, so the explicit numerical-slice reading here uses v5.
No branch-connectivity conclusion is imported. C999g/C999h's audited
normalization and smooth real representation are reused; their source
coverage is unchanged. In particular the actual completion uses
s(s-w)/(2w), not the opposite sign appearing in some abstracts.

### Four-side obligation and local overlap

For w=1 and w=3/2, the complete t intervals must be controlled;
for t=40 and t=45, the complete w intervals must be controlled.
Corners belong to this obligation. No certified lower bound for the
norm of F, sufficient component-sign covering, winding value, or
comparison map with a strictly paid boundary error is currently supplied.
C999g's stopped first-exponential enclosure concerns G_w, a different
observable, and cannot fill these missing values. C999h/C999i give exact
identities but no boundary separation. No new specialization, boundary
estimate, determinant formula, quadrature or mathematical script was
derived in this source turn.

Reused review423's fixed-slice contract and stop425's missing-backend
evidence; review429/stop430's mixed-sign obstruction; review435/stop436's
unpaid far-jump/curvature budget; and stop439's distinct failed backend
attempt. These are scoped failures, not zero exclusions. The inspected
method section of the Pólya census assessment supplies interval inclusion
and tail obligations for a different function, not transferable signs
or certificates. No cross-notebook input is used. Full matching Mathlib
coverage remains unchecked and unknown.

Queries were `Brouwer degree winding number boundary regular value
determinant theorem computational degree Franek Ratschan`, `Lagarias
Rains two variable zeta function zeros collisions parameter w theta
power`, `"Lagarias" "Rains" "1.5" zeros coalesce`, `"two-variable zeta"
"degree" collision`, `"theta" "power" "Lagarias" "boundary" zeros`,
`"Lagarias" "Rains" "boundary" "degree" theta`, `"xi_Q" "collision"
zeros`, and `"two-variable zeta" "coalescence" certificate`. Unrelated
results and uninspected leads are not theorem evidence. This bounded
search establishes no novelty or universal absence of a certificate.

### Decision and independently executable continuation

The discriminating test required a concrete independent boundary
estimate, not only a general identity. That source-readiness test fails:
the degree method relocates the unpaid signed information to the boundary.
This is informative negative source-scope evidence, not a zero count or
an impossibility theorem. Park this exact nomination. Reopen only with
an explicit actual-family comparison/enclosure and full boundary error
budget, plus separately assessed implementation if needed; an attested
backend alone does not furnish a sign or nonzero degree.

For an independent next step, reuse unchanged review418, separately
approved in step419, for the still-unperformed C984a audit. Its exact
rational model needs no numerical backend. Only the existing statement,
external-input inventory and approval were inspected for this routing
choice; the audit itself was not performed. It can validate or repair
the retained radial-recovery obstruction, leaving actual L984(H) unpaid.
No new next assessment is written. A justified creative central target
is still absent: neither degree theory nor this model supplies an
independent actual-zeta sign, domain or arithmetic payment mechanism.
Do not reclassify the bounded model audit as creative work.
