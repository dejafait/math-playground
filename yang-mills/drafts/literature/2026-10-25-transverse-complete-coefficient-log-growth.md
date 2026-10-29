# Complete transverse coefficient — completed growth-test coverage

TARGET: Test whether L280(7)'s complete transverse source coefficient satisfies |partial_s partial_t R_H(0,0)|<=C log(eN) for all sufficiently large even N, retaining every source jet, both quotient-density determinant terms and all variable normal links.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the inspected source comparisons in 2026-10-25-exact-reflected-coefficient-log-growth.md and the quotient assessments; checked L280's complete audited cumulants and ATTEMPTS/047. New bounded searches for lattice BRS renormalization and relative-boundary gauge/ghost estimates led to the two primary readings below; no matching complete box bound was located.
SOURCE_EVIDENCE: Read Luescher–Weisz hep-lat/9504006v1 sections 4.1–4.3, 5.1–5.2 and 7, printed pp. 8–15, 19–20; Christiansen Murguizur–Manzo–Pisani 2604.05082v2 sections 2–3 through the boundary-kernel proof and sections 4 opening/4.3, printed pp. 7–19, 29–30. These do not supply the target estimate; precise cases and qualifications are below.
COMPARISON: Bulk renormalized vertex functions, continuum boundary effective actions, conditional momentum-integral power counting and contracted composite matching do not cover the complete bare oriented pair with all-face pins. The audited nonlinear quotient density permits a direct transverse test without assuming any of those transfers.
GAP: Cancellation and estimates for the whole signed transverse contraction sum, including both determinant terms, insertion corrections, internal contractions and all physical boundary rows, remain unproved. No sign, divergence, mesh bound or novelty is established.
REASON: The bounded comparison now supports one exploratory complete-coefficient test on an exact finite expression. No essential unread theorem is needed for that direct test; theorem-based renormalization or boundary replacement would need a separate assessment.
LITERATURE_REASON: Step 488 approved the quotient identity, not its cutoff-growth mechanism; this separate review checks new BRS-renormalization and relative-boundary leads against the changed representation, while reusing adequate tensor, slab and momentum-power-counting coverage.
SCOPE: SU(2), positive even N, a=8/N, fixed cube [-4,4]^4, real f_* of L003, exact bare reflected pair of L279, all boundary-contained links pinned, boundary-fixed gauge group, every normal link variable, L280's own nonlinear jets and density. C may depend on the cube and f_* but not N; no flow, scalar projection, normalized-source replacement or nonlinear Hodge transport.

## Gap, relevance and prior coverage

The main gap remains construction of a nonzero interacting continuum
sector with the required axioms and finite positive infinite-volume mass.
The intermediate target is the stated logarithmic bound for precisely
L279's coefficient, represented by L280(7). It could constrain the first
correction to L003's positive Gaussian reflection coefficient. It cannot
control higher orders, establish the c_box/2 interacting comparison on a
physical trajectory, or close any continuum/infrared gap by itself.

Read L003 section 1, L279 hypotheses, (7)–(11) and (20)–(22), and the
full L280 representation and separate audit. L280 section 6 already
writes all seven transverse cumulants: simply extracting them again
would be duplicate work. Its exact identity is not a cutoff estimate.

Reuse the [earlier completed growth review](2026-10-25-exact-reflected-coefficient-log-growth.md):
Adams–Lee 0709.0781v3 section II and Appendix A require the specified
momentum-integral class and summation control; Detmold–Shanahan
1606.04505v3 section III.B and Appendix A do not compute the needed
uncontracted-tensor matching factors; Luescher et al. hep-lat/9207009v1
sections 2.1, 3.3–3.5 concern a temporal slab, spatial periodicity and
an effective action. The recorded scalar/stress and corner qualifications
remain in force. These sources are assessed evidence, not newly imported
premises. No repeat derivation or repeat search of these settled scopes
is needed.

[ATTEMPTS/047](../../ATTEMPTS/047-internal-contraction-integration-by-parts.md)
stops two forest rearrangements: the exact Gaussian integration by parts
retains the same uncontrolled expectation and its residual is not
pointwise zero. This is not a disproof of integrated cancellation. The
new test must exploit the actual relative transverse covariance together
with L280's full quotient density. Renaming the forest tensors or
repeating its pointwise-zero test would not qualify.

## New primary comparisons

M. Luescher and P. Weisz, *Background field technique and renormalization
in lattice gauge theory*, Nucl. Phys. B **452** (1995), 213–233,
[hep-lat/9504006v1, 11 April 1995](https://arxiv.org/pdf/hep-lat/9504006v1).
Sections 4.1–4.3, (4.2)–(4.22), pp. 8–12, assume renormalizability
without background fields, classify the remaining local singular terms,
use BRS to eliminate c2,c3 and shift symmetry to eliminate c1. Sections
5.1–5.2, (5.1)–(5.14), pp. 12–15, keep Wilson, gauge-fixing, ghost and
Haar measure vertices. Section 7(a)–(e), (7.1)–(7.2), pp. 19–20,
uses nonexceptional momenta, logarithmic renormalization constants and
the same symmetry argument. This establishes background-field
renormalizability without additional counterterms. Its background and
BRS sources are not L280's local plaquette weights. No all-face domain,
composite-pair mixing or uniform position-space bound is supplied.
Consequently it cannot authorize discarding either determinant jet or
inferring our bare bound. Reisz's original all-orders papers, cited
there, remain uninspected leads, not inputs.

S. Christiansen Murguizur, L. Manzo and P. Pisani, *Worldline Images for
Yang-Mills Theory within Boundaries*,
[arXiv:2604.05082v2, 21 October 2026](https://arxiv.org/pdf/2604.05082v2).
Section 2, (2.5)–(2.15), pp. 7–11, retains boundary terms, relative
conditions (tangential Dirichlet, normal Robin, Dirichlet ghosts), the
alternative absolute conditions, and the gauge-minus-ghost determinant.
Its relative gauge-parameter discussion uses Laplacian eigenfunctions;
it is not an unrestricted nonlinear boundary-slice theorem. Section 3,
(3.1)–(3.21), pp. 12–17, uses a half-space chart, smooth coefficient and
projector extensions, and checks both Dirichlet and Robin kernel cases.
Section 4, (4.1), p. 19, and section 4.3, (4.49)–(4.60), pp. 29–30,
compute a0,a1,a2. These are continuum background-effective-action
results, not the complete source-dependent lattice coefficient. No
intersecting-face/corner comparison or bare plaquette tensor matching
is supplied. No conclusion for L280 is imported.

## Bounded search and exact permitted attempt

Queries included `lattice Yang Mills perturbative renormalization
relative boundary conditions box composite operators one loop lattice
gauge BRS Luscher Weisz`, `"lattice gauge" "Faddeev-Popov"
"logarithmic" "boundary"`, `Thomas Reisz lattice Yang Mills
renormalization all orders BRS theorem 1989 pdf`, `"relative boundary
conditions" "Yang-Mills" "renormalization"`, `"relative Coulomb"
"lattice" coefficient logarithmic`, and `"lattice gauge" "composite
operators" "boundaries" renormalization power counting`. Abstracts
were discovery leads only; the primary ranges above support the scope
comparison. This bounded search is not evidence of originality.

Approve one direct exploratory proof attempt on the unchanged TARGET.
Start with L280 section 6's complete seven cumulants, its own jets in
(6), relative transverse quadratic law (13), and full ell_2 in (4).
Organize the connected position-space contractions of the whole signed
sum and test cancellation of candidate power-growing internal terms
before absolute estimates. The test must account for action and density
contractions together with both cubic/quartic insertion corrections and
moving means. Use the actual finite incidence domains, Dirichlet vertex
inverse Delta^{-1} and transverse covariance, including both normal-edge
endpoint cases. This is a prescribed test, not an identity or estimate
proved in this literature turn.

The discriminating question is whether these exact finite-domain terms
cancel or leave an explicitly controlled remainder whose full sum is
bounded by C log(eN). Keep every boundary contribution in an exact
bulk/boundary decomposition if one is used; separated supports alone
do not remove internal boundary sums. Do not assume a translation-
invariant symbol, a scalar-only mixing law, or the continuum BRS
counterterm classification. Any use of a new such theorem requires
separate coverage. The direct calculation depends on none of the unread
leads, so their absence is not an essential-source blocker.

Success requires the full stated uniform bound, or an honestly partial
result identifying a complete signed contraction family and the precise
remaining bound. A single summand, numerical fit, or formal rearrangement
with the same uncontrolled residual is insufficient. Abandon this
particular cancellation mechanism if it reduces to the stopped forest
identity, needs an unverified boundary/source replacement, or produces
no discriminating finite-domain estimate. Preserve that outcome and
select a materially different test; the target itself is not disproved.

Initial routing record: step 488 wrote REVIEW_REQUIRED coverage only;
it neither calculated growth nor approved this attempt. Step 489 is the
separate literature approval. Mathematical exploration usage remains
zero on the transverse mechanism; the two forest explorations remain
parked. Completed kind/classification: LITERATURE / NOVELTY_UNCHECKED;
outcome EXPLORATION. No new mathematical result, lemma, script, DAG edge
or main argument is added. Mathlib coverage of the complete bound and
its analytic support is not checked.
