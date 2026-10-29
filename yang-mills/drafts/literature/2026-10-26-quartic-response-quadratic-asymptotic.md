# Complete quartic response — completed asymptotic coverage review

TARGET: Determine the N^2 leading asymptotic of L280(20)'s complete quartic action/insertion response on the same relative box and compare it with L282's density term.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-10-26 checked L279(8)–(12), L280 hypotheses and (16)–(20), L281's separated expansion, L282's conclusion, ATTEMPTS/047–049 and the saved transverse/density and older quartic assessments; searched exact plaquette-pair, quartic/tadpole, boundary and position-space terminology listed below. No inspected theorem supplies the complete quartic limit; failed searches do not establish novelty.
SOURCE_EVIDENCE: Newly read Luescher–Weisz hep-lat/9502017v2, 23 February 1995, sections 1 and 2.1–2.2, printed pp. 1–4, (1.1)–(1.4), (2.1)–(2.14), and Appendix A.1–A.2, pp. 18–21, (A.1)–(A.15), including both auxiliary-integral proof cases. Reused the precise Adams–Lee, bulk BRS, relative-boundary and scalar-kernel assessments below; reopened hep-lat/9504006v1 (5.10)–(5.11), p. 14, for its retained measure vertices.
COMPARISON: Full-space scalar propagator asymptotics and recursion, conditional one-loop momentum-integral theorems and bulk renormalizability do not evaluate this isolated quartic response in a finite relative box with local plaquette sources. L282 fixes the density comparison threshold only. No complete limit or cancellation is imported.
GAP: The actual local Wilson quartic contractions still require uniform finite-domain internal-kernel and boundary estimates, both insertion responses and the complete mixed-source sum; neither the coefficient nor the assumed N^2 scale is established by the sources.
REASON: This separate literature-only review approves one bounded direct test of the unchanged target from its already audited finite expression, without invoking an unread theorem. Known scalar identities should be cited if used; their transfer to the projected relative kernels must be justified in the later attempt. No new mathematical result is derived here.
LITERATURE_REASON: The saved next target was REVIEW_REQUIRED: the complete quartic asymptotic is outside the previously approved density-only asymptotic and stopped full-sum growth mechanisms. Essential new scope comparison is completed here, while adequate quotient, scalar and bulk source coverage is reused.
SCOPE: Exactly TARGET for SU(2), even N>=2, a=8/N, fixed cube [-4,4]^4, all boundary-contained pins, boundary-fixed gauges, every normal link variable, three colors, L002's exact product bump and L280's real source domain; own-slice L279 jets and all four quartic terms. No forest-jet transport, scalar projection, flow or assumed bulk replacement.

## Exact proposed target and downstream use

Use SU(2), even N>=2, a=8/N on [-4,4]^4, all boundary-contained
pins, boundary-fixed gauges, every normal link, three colors, L002's
exact product bump and L280's real source domain. The quantity is
exactly mathcal K_4^H in L280(20), including BOTH quartic insertion
responses and BOTH displayed action responses, using the all-link
jets of L279(8)–(9) evaluated on the L280 slice. Do not substitute a
forest quartic, an arbitrary gauge-invariant phase or a bulk-only term.

Essential prospective input IDs: L002 L003 L279 L280 L281 L282.
The accepted density limit is (3 d_*/32) S_f<0. Determining the quartic
N^2 term could quantify the remaining compensation required of the
cubic family. It need not itself cancel the density. The exact local
Wilson plaquette jets distinguish this target from the generic orbit
identity stopped in ATTEMPTS/049; the proposed finite-mode/internal
kernel test also differs from repeating ATTEMPTS/048's global norm.
These distinctions motivate review, not mathematical approval.

The later mathematical test, if approved, is a complete finite N^-2
limit with its coefficient or a rigorous obstruction/different leading
scale. Preserve all boundary and internal-contraction contributions.
A bulk calculation without a uniform remainder does not pass. If this
mechanism cannot control its internal contractions, preserve that
failure and reassess rather than assert cancellation. This registration
derives none of these estimates.

The original registration required a separate comparison of exact and
stronger known statements and their essential proof cases. The completed
comparison below supersedes REVIEW_REQUIRED without changing the target.
Full and supporting Mathlib coverage for that target remains not checked.
Even a successful quartic limit leaves the cubic response, uniform
higher remainder, physical trajectory/composite mixing, continuum
axioms, nonzero sector and finite positive mass unresolved.

## Completed primary comparison

M. Luescher and P. Weisz, *Coordinate space methods for the evaluation
of Feynman diagrams in lattice field theories*, Nucl. Phys. B **445**
(1995), 429–450, [hep-lat/9502017v2, 23 February 1995](https://arxiv.org/pdf/hep-lat/9502017v2).
Sections 1 and 2.1–2.2, pp. 1–4, assume infinite four-dimensional
hypercubic lattice, unit spacing and scalar propagator 1/hat(p)^2.
Equation (1.3) fixes its Fourier normalization. Equations (2.4) and
(2.9) give its large-distance expansion and recursion; the latter
requires sum_mu x_mu nonzero. They do not state a finite-box theorem.
Appendix A.1–A.2, pp. 18–21, proves the expansion: the auxiliary
numerator Q is homogeneous of degree d, n>=1 and d-2n>=-3;
n=1 uses a Gaussian integral, whereas n>=2 subtracts the Taylor
polynomial of degree 2n-4 before interchanging differentiation and
integration. The smooth cutoff isolates p=0; (A.15) controls the
large-distance remainder through O(|x|^-8). This covers scalar
full-space asymptotics, not uniform coincident-anchor errors or the
projected relative covariance. The quartic response is not evaluated
there. Thus these are possible tools after a justified local-kernel
comparison, not a citation for the target. No reproof is warranted.

Reuse the precise source readings in
[the complete-transverse review](2026-10-25-transverse-complete-coefficient-log-growth.md)
and [the reflected-growth review](2026-10-25-exact-reflected-coefficient-log-growth.md).
Adams–Lee, *Structure of logarithmically divergent one-loop lattice
Feynman integrals*, Phys. Rev. D **77** (2008), 045010,
[0709.0781v3](https://arxiv.org/pdf/0709.0781v3), section II (7)–(15)
and Appendix A (A1)–(A11), applies to its specified single momentum
integrals, scaled smooth numerator/denominator, denominator lower
bounds, absence of extra zeros, and infrared convergence. Its degree-zero
logarithmic structure is not an estimate for a degree-two local
contraction, nor has the finite-box response been reduced to its class.
Do not use perturbative order alone to assert the single-loop condition.

Luescher–Weisz, *Background field technique and renormalization in
lattice gauge theory*, Nucl. Phys. B **452** (1995), 213–233,
[hep-lat/9504006v1](https://arxiv.org/pdf/hep-lat/9504006v1), sections
4.1–4.3 and 7, pp. 8–12, 19–20, assumes the ordinary theory's
renormalizability and uses BRS/background/shift identities for the
complete vertex functional. Its background sources are not our local
plaquette weights. Reopened (5.10)–(5.11), p. 14, explicitly retains
Haar-induced measure vertices. Neither that theorem nor those vertices
give a separate quartic N^2 coefficient, and no identification with
L280's nonlinear quotient density is imported. The already inspected
continuum relative-boundary/half-space results in the transverse review
also supply no all-face lattice or corner remainder for this source pair.

Reuse [the density-kernel review](2026-10-25-density-response-separated-kernel-asymptotic.md):
Dowker 1207.2096v2 sections 7–8, (29)–(37), pp. 10–13, gives scalar
Dirichlet and half-step Neumann interval identities; Lawler–Limic,
*Random Walk: A Modern Introduction* (2010), Theorem 4.3.1 and
Proposition 4.6.2(a), gives scalar transient full-space asymptotics
and killed-domain exit subtraction. The recorded walk normalization
must be checked if used. Neither replaces the projected relative
matrix by a scalar kernel. Michta–Slade, ALEA **19** (2022),
Theorem 1.3(ii), requires d>2q in its massless case, so a bare
d=4,q=2 inverse-square import is still excluded. These covered tools
need not be searched or proved again. L282's bounded-density polynomial
comparison is not automatically a comparison for quartic internal G.

## Search, duplicates and obstruction comparison

Queries included `lattice Yang Mills one loop quartic vertex quadratic
divergence tadpole finite volume Dirichlet boundary Reisz power counting`,
`"lattice" "Wilson" "quartic" "plaquette" "one-loop" divergence`,
`Luscher Weisz coordinate space methods evaluation Feynman diagrams lattice
field theories 9502017 Green function`, `"plaquette" "correlation"
"quartic" "lattice" perturbation`, `"Yang Mills" "Dirichlet"
"one-loop" "plaquette" correlation`, `"Wilson" "plaquette-plaquette"
"one loop"`, `"lattice gauge" "quartic" "relative boundary"`, and
`"lattice" "quartic" "source" "tadpole" "boundary" Yang Mills`.
The last narrow searches did not expose a matching primary statement.
The newly inspected position-space paper is a relevant tool lead with
explicit scope limits, rather than an exact theorem match. Capitani's
review, Reisz's original all-orders papers, mean-field/tadpole-improvement
and plaquette simulation hits remain uninspected leads, not inputs.
No assertion that no stronger theorem exists follows from this search.

The [older quartic-probe review](2026-10-16-complete-quartic-probe-jet-scale.md)
and the quartic-residual reviews concern Ward/flow observables in the
forest and different normalizations. They are not the reflected
source coefficient on this slice. L280(20) already supplies all four
terms, so deriving another extraction formula would be redundant.
L281/L282 concern the full density family, not the Wilson quartic jet.
No duplicate complete quartic asymptotic was found in the selected paths.

[ATTEMPTS/047](../../ATTEMPTS/047-internal-contraction-integration-by-parts.md)
retains an uncontrolled internal forest expectation after integration
by parts; [048](../../ATTEMPTS/048-transverse-absolute-norm-growth-test.md)
stops an insufficient global norm bound. Neither tests the actual local
quartic family with an internal-kernel limit. The nonlocal comparison
phase in [049](../../ATTEMPTS/049-transverse-gauge-identity-cancellation.md)
shows that generic gauge identities cannot force the full bound; it
does not obstruct a Wilson-specific local calculation. This is the
specific new mechanism warranting the bounded attempt, without reopening
either stopped rearrangement. There is no persistent essential source
blocker: the direct test assumes none of the uninspected leads.

## Approved bounded attempt and decision test

Approve one later mathematical invocation on exactly TARGET. Use
L002 L003 L279 L280 L281 L282, retaining the all-link quartic jets
of L279(8)–(9) evaluated on L280's own slice. Begin from all four
mathcal U terms already in L280(20), including both source derivatives
of the quartic insertion and both action responses. Do not recalculate
the coefficient extraction or transfer higher jets from the forest.

The proposed mechanism is a local/internal-contraction comparison:
retain the finite edge offsets within each plaquette, test the internal
relative covariance against a controlled bulk limit, and use the
already covered separated-source modes for the external response.
These are proposed steps, not established contraction limits. In
particular, local Wilson support does not itself prove that an internal
Green kernel or its boundary contribution can be discarded. Preserve
the terms with two differentiated covariance factors as well as those
with a mixed derivative and an internal covariance. Any polynomial,
mode or bulk/boundary approximation must have an error uniform in the
remaining sums. Keep every normal-edge endpoint case and all colors.

Continue if the complete N^-2 quartic response has a finite limit with
its coefficient and a justified o(N^2) remainder, or if a rigorous
different scale/obstruction changes that research decision. Compare the
result with L282(5)'s (3d_*/32)S_f; quartic-only cancellation is not
required. A complete finite bound or a controlled subfamily can be
honest partial progress, with the unproved remainder named; it is not
the full asymptotic. If only a bulk coefficient, numerical fit, the
same global norm loss or an unestimated internal/boundary residual
survives, the full test has not passed. Record that outcome and reassess
the mechanism without calling the target false. Uncovered theorem use
requires a separate review before dependent work.

This turn performs no quartic derivation, mathematical script or lemma
write. Outcome EXPLORATION; kind LITERATURE; classification
NOVELTY_UNCHECKED. It spends zero mathematical exploration attempts.
The next turn defaults to mathematics on this approved target. The
uniform higher remainder, cubic compensation, physical trajectory,
composite mixing, continuum axioms, positive sector and mass gap all
remain unresolved. Mathlib coverage remains not checked.
