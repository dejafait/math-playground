# Exact reflected coefficient — completed coverage review

TARGET: Assess coverage for extracting the fixed-mesh coefficient kappa_a=lim_(g->0)g^(-2)[Q_(a,g)(f)-q_a(f)] of L003's exact reflected observable, retaining both centered plaquette insertions and all Wilson-action and quotient-Haar corrections.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the current-target and uniform-reflected-error assessments; searched local L003/L004/L011 and the saved ultraviolet-normalization diagnostic for duplicates and failures; searched “Kirwin higher asymptotics Laplace approximation theorem 1.1 0810.1700” and “lattice gauge plaquette plaquette connected correlation weak coupling fixed volume Laplace expansion boundary forest gauge”. No exact coefficient match was established; this is not a novelty claim.
SOURCE_EVIDENCE: Newly inspected Kirwin, arXiv:0810.1700v2 (5 June 2010), Theorems 1.1 and 2.1, pp. 3–5, Lemma 2.3 statement and signed-amplitude reduction, p. 7, and section 3.2 proof including parity, pp. 14–15. Reused primary renormalization comparisons recorded in 2026-09-26-current-target.md and 2026-10-25-uniform-reflected-error-source-coverage.md; read full L003, L004 and L011.
COMPARISON: Known finite-dimensional Laplace asymptotics cover the analytic expansion mechanism; L003 supplies the exact gauge reduction and minimum/Hessian premises, and L011 supplies connected-subtraction and Haar machinery for a different covariance. None is an evaluated coefficient for Q. Specialize these inputs to both exact reflected plaquette sums without repeating bulk renormalization theory.
GAP: Write and justify the exact two-insertion fixed-mesh formula, including moving means, both insertion jets, all action vertices, quotient-Haar density, and a remainder strong enough after the negative coupling powers. No ultraviolet growth, sign, uniform error or physical trajectory is approved.
REASON: The new primary input resolves the essential asymptotic-coverage question. Remaining work is a finite-dimensional specialization of known mathematics, not another Ward assembly or a claim of new perturbation theory.
LITERATURE_REASON: The registered target changed from a uniform physical-trajectory bound to an exact two-insertion fixed-mesh coefficient; high-order remainder coverage was essential and absent from the reused primary assessments.
SCOPE: L003's exact SU(2) model, real f=f_*, even a=8/N fixed before g tends to zero, all-face boundary-contained links pinned, normal links variable, exact forest quotient, ordinary two-dimensional trace and bare 4/g^2 insertion factors. No flow, new observable, continuum matching or changed gauge measure.
COVERED_TARGET: Extract the fixed-mesh coefficient kappa_a=lim_(g->0)g^(-2)[Q_(a,g)(f)-q_a(f)] for L003's exact centered reflected observable, with both insertion jets, all Wilson-action and quotient-Haar corrections, and an o_a(g^2) remainder for Q.

## Primary input and its limits

William D. Kirwin, *Higher Asymptotics of Laplace's Approximation*,
Asymptotic Analysis 70 (2010), 231–248,
[DOI](https://doi.org/10.3233/ASY-2010-1016),
[inspected preprint v2](https://arxiv.org/pdf/0810.1700v2).
Theorem 2.1 assumes a measurable region containing the minimum internally,
a unique zero minimum with a positive gap away from its neighborhood,
radial expansions with continuous positive leading phase coefficient,
positive radial orders, and convergence of an exponentially weighted
amplitude integral. It gives a finite expansion with little-o remainder.
Theorem 1.1 treats a smooth nondegenerate minimum; section 3.2 reduces
its Hessian to the identity and checks vanishing odd coefficients.
Lemma 2.3 explicitly addresses signed amplitudes. Use Theorem 2.1's
little-o statement for remainder bookkeeping rather than relying on the
weaker displayed big-O in (1.3). The dimension and constants stay fixed;
no uniformity in dimension or mesh is supplied.

## Applicability obligations for the later specialization

L003 proof section 1 establishes an exact product-Haar forest quotient,
a unique flat minimum, and positive definite quadratic action on that
slice. These are existing local results, not a formal interacting Hodge
gauge prescription. Its compact-complement gap and local exponential
chart permit the theorem's local setting. The physical boundary of the
lattice does not place the identity on the boundary of this coordinate
chart. Retain its variable normal end links and omitted forest links.

The amplitude functions to compare with the theorem are the reduced
Haar density times: one, either uncentered plaquette-sum numerator, or
their product. These are smooth, real functions on the finite compact
link manifold; localization makes the coordinate integrals absolutely
convergent, including sign-changing amplitudes. Their external powers
of g must be handled explicitly after expansion. The theorem is not
applied to a coupling-dependent centered amplitude without explaining
its moving expectation. The later proof must expand the partition
function and all three needed moments to sufficient order, or justify
the equivalent rescaled connected expansion. It must identify the
leading covariance with L003's q_a using only the established quadratic
curvature-law comparison. Higher jets remain on the forest slice.

L011 equations (2)–(4), (7)–(9) and proof sections 1–2 give the existing
Taylor, cumulant and density method. Its observable pair is different;
its formula (6) cannot simply be relabeled as kappa_a. The permissible
reproduction changes those two numerators to L003's actual reflected
and unreflected plaquette sums. No nonlinear flow or Ward-divergence
insertion is present in Q; the coordinate Haar correction is still
required. Derive the connected subtraction for this pair in the later
research turn, not in this review. Reproving the general Laplace theorem
or the previously established forest reduction would be redundant;
explaining their applicability and the new observable bookkeeping is
necessary.

## Duplicate and failure comparison

L004 and drafts/2026-09-25-plaquette-ultraviolet-normalization.md
explicitly leave the full reflected correction unresolved: scalar,
stress and remaining tensor sectors cannot be collapsed into one pole.
L011 concerns a Ward covariance; Gamma and kappa_a are not identified.
The current-target assessment's flowed perturbative finiteness and
stress matching inputs are reused only as context. The completed
uniform-error assessment and ATTEMPTS/046 park direct import of a
physical-trajectory bound. They do not prohibit this finite-mesh test.
No duplicate formula for this exact observable was located in the
specific local material searched. Search results about strong coupling,
one-plaquette models and continuum mesh expansions were not read as
matching theorem inputs and supply no premise here.

## Relevance and continuation test

The main gap remains an interacting continuum theory and finite positive
infinite-volume mass for every compact simple group. This intermediate
coefficient could expose the terms whose cutoff growth and mixing must
be studied before any uniform reflected-error estimate. Continue if a
complete finite Gaussian expression and justified o_a(g^2) remainder
for Q can be written with both centered insertions. Stop an incomplete
formula if it omits moving means, action or Haar terms, transfers higher
jets to the Hodge law without justification, or substitutes Gamma or a
scalar-only pole. No cutoff-growth or uniformity conclusion follows
from success; in particular the c_box/2 threshold remains unmet.

Essential inputs are L003 and L011's finite-dimensional method; L004 is
a scope warning. No physical running-coupling prescription, renormalized
interaction, limiting composite algebra, continuum positivity/axioms,
box removal or infrared mass is assumed. Mathlib coverage of the full
specialization and supporting high-order Laplace/cumulant results is
not checked. No mathematical result for kappa_a is proved this turn.
