# Complete cubic asymptotic — completed coverage review

TARGET: Determine the N^2 leading asymptotic of L280(20)'s complete cubic response on the same relative box and compare it with L285(4).
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-10-26 searched two-cubic-vertex, three-propagator, position-space self-energy, local-coupling and plaquette-pair terminology; compared the primary passages below with L280(20), L285(4), selected recent work notes and ATTEMPTS/047–049. No matching complete theorem was established; no novelty follows from the search.
SOURCE_EVIDENCE: Newly read Luescher–Weisz hep-lat/9502017v2 sections 3.1–3.3, 4 opening/4.1 remainder convention, 4.2 and Appendix C.1, printed pp. 6–14, 22–23; Bode–Weisz–Wolff hep-lat/9809175v1 sections 2–3, pp. 2–7, including the three-propagator diagram and numerical asymptotic extraction. Reused the ready scalar, quotient, bulk BRS and momentum-integral assessments named below.
COMPARISON: Full-space scalar diagram subtractions and a numerically extrapolated slab boundary response do not give the complete bare cubic response with two local sources on the all-face relative box. L285(4) supplies the comparison coefficient, not the cubic contribution. The exact uncovered work is a Wilson-specific uniform vertex-pair estimate, not another coefficient extraction.
GAP: All five cubic groups need a combined finite-box N^-2 limit, or an informative obstruction, with complete internal vertex-pair and boundary errors. Neither the N^2 scale nor cancellation with L285(4) is established by the sources; scalar kernels and single-plaquette approximation do not discharge these requirements.
REASON: Approve one later direct exploratory attempt on the unchanged exact finite expression using existing audited local inputs and inspected supporting tools. No unread theorem is essential to that attempt. Any source-based renormalization, scalar replacement or additional theorem outside this scope needs separate review before use; this turn derives no estimate.
LITERATURE_REASON: The registered target changes single-plaquette quartic coverage to two cubic vertices and a full vertex-pair sum. This turn supplies the missing comparison, reusing adequate earlier coverage rather than repeating its searches.
SCOPE: Exactly TARGET for SU(2), even N>=2, a=8/N, D=[-4,4]^4, boundary-contained pins, boundary-fixed gauges, all variable normal links and colors, L002/L282's exact product bump and L280's real source domain. All five cubic terms use L280's own slice and ambient all-link Wilson jets. No flow, scalar projection, nonlinear forest transport, assumed bulk cancellation or higher-order uniformity.

## Gap, exact object and downstream use

The main gap is still the interacting continuum theory with nonzero
physical sector and finite positive mass. This intermediate target tests
the next missing contribution to the exact coefficient kappa_a. A complete
cubic limit could quantify compensation against the audited quartic and
density coefficient in L285(4); compensation is a question, not a premise.
An N^2 limit alone leaves the subleading coefficient and mesh-uniform
higher perturbative remainder unresolved, along with physical trajectory,
composite mixing, continuum axioms/positivity and infinite-volume mass.

Essential mathematical inputs for a later attempt are L003 L279 L280
L281 L282 L283 L284 L285, with L002's exact product bump through L282.
Retain SU(2), even N>=2, a=8/N, D=[-4,4]^4, boundary-contained pins,
boundary-fixed gauges, every normal link, three colors, both source
orders and (|s|+|t|)||f_*||_infinity<eta<1. The ambient all-link
jets stay on L280's own slice. The sources h_+=f_* and h_-=theta f_*
have supports in [-1/4,1/4]^3 times [1,2] and [-2,-1], respectively.
Keep the bare normalization with no additional a^4 in the plaquette sum.
Do not identify the old Ward response with this reflected coefficient or
transfer nonlinear forest jets.

The precise object is mathcal K_3^H in L280(20), with its existing
multiplicities and signs. It contains: the pair of cubic insertion
tensors with three undifferentiated covariances; each of the two mixed
insertion/action groups with the opposite differentiated covariance;
the action/action group with G_-+; and the action/action group with
G_- and G_+ on distinct lines. Both source orders, every vertex pair,
edge offset and color contraction are retained. L280 already proves
the finite extraction and vanishing of internal cubic contractions;
rederiving either would not establish this asymptotic.

## New primary comparison and exact scope limits

M. Luescher and P. Weisz, *Coordinate space methods for the evaluation
of Feynman diagrams in lattice field theories*, Nucl. Phys. B **445**
(1995), 429–450, [hep-lat/9502017v2, 23 February 1995](https://arxiv.org/pdf/hep-lat/9502017v2).
New reading: sections 3.1–3.3, pp. 6–10, (3.1)–(3.32); section 4
opening/4.1 and 4.2, pp. 10–14, especially (4.16)–(4.22); Appendix
C.1, pp. 22–23. These use the scalar massless propagator on Z^4 at
unit spacing. Section 3.3 treats trigonometric-polynomial numerators
and positive integer propagator powers through worked convergent
integrals, not an unconditional convergence theorem for (3.18).
Its examples distinguish differentiated G from subtracted inverse-square
and inverse-cube kernels. The zeta sum requires harmonic homogeneous
h of even degree d and Re(s)>2+d/2. Section 4.2 represents a scalar
three-line diagram by the Fourier sum of G(x)^3 and subtracts a
Laplacian of the logarithmic Fourier kernel; the remaining bracket
decays as |x|^-8. Crucially, section 4 defines O(p^n) by
R(p)/|p|^(n-epsilon)->0 for every epsilon>0, allowing logarithms.
No relative-box or local-source error is proved. This is supporting
method coverage, not an import of the cubic limit.

A. Bode, P. Weisz and U. Wolff (ALPHA Collaboration), *Two-loop
computation of the Schrödinger functional in pure SU(3) lattice gauge
theory*, Nucl. Phys. B **540** (1999), 491–499,
[hep-lat/9809175v1, 25 September 1998](https://arxiv.org/pdf/hep-lat/9809175v1).
Read section 2, pp. 2–4, (2.1)–(2.12) and its three-propagator
diagram; section 3, pp. 5–7, (3.1)–(3.8). The geometry has spatial
periodicity and temporal Dirichlet links, nonzero prescribed abelian
background fields and adjustable boundary plaquette weights c_t.
The observable differentiates the boundary-field parameter eta, not
two local plaquette weights. Section 2 computes position-space diagrams
and exact eta derivatives of vertices and propagators. Section 3
assumes the expected asymptotic expansion (3.3), extracts its constants
from finite-lattice data with estimated errors, and checks then fixes
universal logarithmic coefficients. Its quoted improved asymptotics
are therefore not rigorous uniform-remainder theorems for our sum.
The gauge group, geometry, background, derivative and extraction
method all prevent direct specialization. This is relevant evidence
for computational organization, with no bound imported.

These are the two new source comparisons. The scalar position-space
paper was previously read for its one-propagator sections; the
multi-line cases and momentum-remainder convention are the new scope.
The PDF text supplies the needed hypotheses and proof cases. Screenshot
requests for the position-space pages returned labels without visible
image payloads; no visual evidence is asserted.

## Ready assessments reused, duplicates and recorded failures

Reuse [the quartic review](2026-10-26-quartic-response-quadratic-asymptotic.md)
for its precise scalar asymptotics and bulk comparisons, and
[the transverse review](2026-10-25-transverse-complete-coefficient-log-growth.md)
with [the earlier reflected review](2026-10-25-exact-reflected-coefficient-log-growth.md)
for bulk BRS, slab and one-momentum-integral power counting. Their
known-result comparisons remain adequate in those scopes. In particular,
Adams–Lee 0709.0781v3 section II (7)–(15) and Appendix A require their
scaled smooth single-integral class, denominator bounds, absence of
extra zeros and infrared convergence. Neither perturbative order nor
two cubic vertices verifies these hypotheses or remaining-sum uniformity.
Luescher–Weisz hep-lat/9504006v1 sections 4 and 7 concern the complete
bulk vertex functional; they do not determine this isolated source family.
No new deduction from these sources is claimed here.

Reuse [the density-kernel review](2026-10-25-density-response-separated-kernel-asymptotic.md)
for Dowker's interval identities, Lawler–Limic's scalar full-space/exit
formulas, and the exclusions on Toeplitz and massless inverse-square
imports. These do not prove relative transverse vertex-pair estimates.
L281(15)–(16) controls its external separated-mode tail with the full
density sandwich; it does not already bound arbitrary two-cubic-vertex
sandwiches. L285(7)–(9) controls local differentiated covariance entries
within one plaquette. Uniform local entry convergence alone is not a
summation theorem for two independently moving plaquettes. Any use of
these inputs must justify the additional uniform summation.

Local duplicate checks inspected L279's hypotheses and jets, L280's
hypotheses and section 7, L285's conclusion and local approximation,
L281's tail qualification, the quartic attempt/distinct-line work notes
and the transverse full-sum note. The old Ward/flow cubic work has
different observables and coefficients, as already recorded in the ready
reviews. The selected paths contain no completed asymptotic for this
exact cubic family. This is a bounded duplicate check, not an assertion
about all literature or certified originality.

[ATTEMPTS/047](../../ATTEMPTS/047-internal-contraction-integration-by-parts.md)
preserves the uncontrolled internal forest expectation after integration
by parts. [048](../../ATTEMPTS/048-transverse-absolute-norm-growth-test.md)
preserves the inadequate global norm bound.
[049](../../ATTEMPTS/049-transverse-gauge-identity-cancellation.md)
shows that generic orbit/measure identities survive a nonlocal change
of phase with a power-growing response. It does not refute the local
Wilson target. The proposed direct vertex-separation test uses the
specified Wilson tensor and asks for a summed remainder; it does not
repeat those stopped mechanisms. No historical stop is a global ban.

New search queries included:

- `lattice gauge theory one loop position space three gluon vertices self energy quadratic divergence finite volume boundary`
- `Luscher Weisz coordinate space methods 9502017 two loop sunset three propagators lattice position space`
- `lattice Yang Mills plaquette plaquette correlation one loop Dirichlet boundary quadratic divergence source`
- `"lattice" "two cubic" "boundary" Yang Mills`
- `"plaquette" "correlation" "one-loop" perturbation finite volume`
- `"Coordinate space methods" "sunset" Luscher Weisz`
- `"Schrödinger functional" "two-loop" "position space" pure gauge Wolff Narayanan`
- `"lattice gauge" "local coupling" perturbation plaquette correlation`
- `"plaquette-plaquette" perturbation cubic Wilson`
- `"Yang-Mills" "relative boundary" lattice cubic vertex`

Search hits concerning plaquette expectations, simulations or continuum
three-gluon form factors were discovery leads only. The SU(2)
Schrödinger-functional calculation cited as reference [5] in Bode et al.,
original Reisz all-orders papers and vertex-generation papers remain
uninspected leads. No premise of the approved direct test depends on
them. No essential primary source access blocker remains for that test.

## Approved bounded attempt and continuation/abandonment test

Approve one later mathematical invocation on exactly TARGET, starting
from all five groups in L280(20), not a newly extracted formula. A
possible direct mechanism is to separate nearby and distant internal
vertex pairs at a fixed lattice-distance cutoff, retain their exact
Wilson tensors, and test a bound uniform in N for the entire discarded
tail before removing that cutoff. This is a proposed test, not a lemma,
summability assertion or authorization to assume the N^2 scale.
The terms with source insertion tensors, a mixed covariance derivative,
and two separately differentiated lines all remain obligations. Any
external mode truncation must be controlled in the complete cubic
contraction; density or quartic tail estimates cannot simply be copied.
Boundary anchors, corners and both normal-link endpoint cases stay in
the finite sum until an actual estimate disposes of them. A valid proof
must justify the order of all limits and the two source derivatives.

Continue if the complete N^-2 cubic response has an explicit finite
limit with a full o(N^2) error, or if a rigorous different scale or
obstruction supplies informative evidence. Compare any established
coefficient directly with L285(4), without requiring cancellation.
A controlled complete subfamily may be useful partial progress, but
must name all remaining groups and errors. Abandon this particular
vertex-localization mechanism if it leaves only an unestimated tail,
uncontrolled boundary sum, bulk numerical fit or the same global norm
loss. Preserve the obstruction and choose a materially different test;
failure would not disprove Yang–Mills or even the cubic target.

Known scalar identities should be imported by the precise citations
already assessed, with normalization and hypotheses verified locally.
No reproof is justified merely to replace a citation. The potential
new work is solely the uncovered finite relative-box specialization
and complete summation, not Wick extraction or scalar kernel identities.
Any newly needed theorem outside this assessment requires a separate
literature turn before dependent research. There is no theorem-based
approval of a previously unproved mathematical assertion in this turn.

Completed outcome EXPLORATION; kind LITERATURE; classification
NOVELTY_UNCHECKED; actual task literature_comparison. The earlier
REVIEW_REQUIRED registration is superseded by this separate review,
with its exact target unchanged. Zero mathematical exploration attempts
are spent here; no supervisor counter reset is claimed. No lemma,
mathematical script, DAG edge or main argument changes. Full and
supporting Mathlib coverage for the complete cubic limit is not checked.
STATUS remains IN_PROGRESS with no complete-solution candidate.
