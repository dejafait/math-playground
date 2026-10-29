# Distinct-line cancellation critical audit — completed coverage review

TARGET: Critically audit L291's complete distinct-line cubic asymptotic and its cancellation with L290(3), including the source-factor error and cross-half terms.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Compared all of L291 with L287 section 2, L288 sections 1–2, L290(3)–(4), the complete-cubic and quartic audit assessments, the L291 work note/history 509 and ATTEMPTS/047–049. Reused their exact-target searches; two focused source-factor/relative-boundary searches below established no matching theorem or independent completed audit.
SOURCE_EVIDENCE: Reopened Benzi–Razouk, ETNA 28 (2007), section 3.5, printed pp. 24–25: graph-power argument, Theorem 3.4 and its entire proof, including diagonal and normal cases. Reused the versioned scalar, interval and cubic-diagram readings identified below; those were not newly browsed.
COMPARISON: Polynomial graph locality is covered, but analytic inverse-decay bounds do not give uniform residual control at a closing spectral gap. Scalar bulk diagrams and numerical slab asymptotics do not establish L291's source-factor error, cross-half expectation or relative-box normalization. These are explicit local proof obligations rather than missing consequences of a known theorem.
GAP: Independently audit L291(4)–(26), especially the correlated source-factor construction, six residual products, full-half boundary estimates, two internal covariances, all source sums and cancellation with L290(3), conditional on the inherited unaudited inputs. Coverage approval does not verify any of these assertions.
REASON: The unchanged audit can proceed using the ready source scope and explicit finite Gaussian/matrix estimates, with no essential unread theorem. Approve one later RESEARCH / REPRODUCTION conceptual audit; retain all upstream qualifications and stop for source review if an essential new theorem is needed.
LITERATURE_REASON: The newly registered critical audit required separate comparison of its common-noise source factor, fixed-range cross-half argument and weighted integral with existing coverage. The focused primary reopening resolves that source-scope question without refreshing adequate broad searches.
SCOPE: Exactly TARGET, conditional on L280 L284 L285 L287 L288 L289 L290, with L002's exact product bump through those inputs; SU(2), even N>=2, a=8/N, all-face relative cube, boundary-contained pins, boundary-fixed gauges, every normal link, all colors and source orders, and L280's real source domain. Ambient Wilson jets stay on that slice; no stronger rate, higher remainder or continuum claim.
COVERED_TARGET: Critically audit L291's complete distinct-line cubic asymptotic and its cancellation with L290(3), including the source-factor error and cross-half terms.

## Main gap, intermediate target and use

The main gap remains an interacting continuum theory with a nonzero
physical sector and finite positive mass for every compact simple group.
The intermediate target is a separate critical audit of the final cubic
group and the claimed cancellation at scale N^2. If accepted, it makes
that coefficient comparison dependable for later subleading analysis;
it does not supply a uniform interacting lower bound. No creative
continuation is independently prepared. This essential audit takes
priority over discovering a new mechanism; its completion must not be
counted as resolving the construction or infrared gaps.

The official statement version already recorded in
`foundations/01-target-and-scope.md` is reused: this turn does not select
a new route. No cross-notebook mathematical input was read or used.

## Exact continuation and source reuse

The proposed audit concerns L291(2)–(3), conditional on the precise
inputs it actually uses: L280 L284 L285 L287 L288 L289 L290. Retain
L002's product bump through those inputs, SU(2), even N>=2, a=8/N,
all-face relative boundaries, every normal link, all colors and both
source orders, and L280's real source domain. Jets remain on the same
slice; there is no forest transport or added a^4 plaquette weight.

Reuse [the complete-cubic assessment](2026-10-26-complete-cubic-quadratic-asymptotic.md)
for the exact finite expression, all five groups and its source
comparisons. It inspected Luescher–Weisz, *Coordinate space methods for
the evaluation of Feynman diagrams in lattice field theories*,
[hep-lat/9502017v2](https://arxiv.org/pdf/hep-lat/9502017v2),
23 February 1995, sections 3.1–3.3, 4.1–4.2 and Appendix C.1,
pp. 6–14, 22–23. Its scalar infinite-lattice diagram subtractions do
not give this relative transverse two-source estimate. The section 4
remainder convention permits logarithms and must not be read as a
uniform finite-box estimate. Bode–Weisz–Wolff,
[hep-lat/9809175v1](https://arxiv.org/pdf/hep-lat/9809175v1),
25 September 1998, sections 2–3, pp. 2–7, treats SU(3), a temporal
Dirichlet/spatially periodic slab, boundary-field derivatives and
numerically extracted asymptotics. None imports L291's limit.

Reuse [the quartic audit coverage](2026-10-26-complete-quartic-critical-audit.md)
for the separated relative-mode and polynomial comparison scope. Its
scalar supporting sources include Dowker, 1207.2096v2, sections 7–8,
(29)–(37), pp. 10–13, with Dirichlet and shifted Neumann conventions;
Lawler–Limic (2010), Theorem 4.3.1 and Proposition 4.6.2(a); and the
quartic assessment's Luescher–Weisz Appendix A.1–A.2, pp. 18–21.
Their scalar results do not replace the projected covariance or prove
the full-half first-derivative estimates used in L291(7). Those estimates
have explicit local derivations to check under their exact endpoints.
The already recorded massless d=4,q=2 exclusion remains in force.

M. Benzi and N. Razouk, *Decay bounds and O(n) algorithms for
approximating functions of sparse matrices*, ETNA **28** (2007),
16–39, [published PDF](https://etna.ricam.oeaw.ac.at/vol.28.2007-2008/pp16-39.dir/pp16-39.pdf),
section 3.5, pp. 24–25, was reopened. The graph-power argument gives
polynomial locality. Theorem 3.4 assumes diagonalizability, spectrum
in a continuum F and analyticity on its specified enclosing domain;
its bound contains the eigenvector condition number. Its proof treats
off-diagonal entries by polynomial approximation, then the diagonal;
normal matrices permit a unitary eigenbasis. This supports the locality
tool already assessed. It does not supply a uniform inverse-error bound
as the relative-box spectrum approaches zero. Nor does it establish
L291's source-weighted residual estimates or cross-half expectation.
Those require the written finite estimates, not a fresh reproof of
this theorem. Polynomial locality alone is insufficient for the limit.

The finite Gaussian identities and positive Schur estimate are already
written in L279/L280 and L287(11); L288 supplies explicit residual
diagonals. They are available for independent checking, not accepted
as new source imports here. L288's independent covariance splitting
cannot simply be reused as independence of L291's retained and residual
fields. This distinction is the main scope refinement. L291's weighted
numerator in (24)–(26) is also an explicit local audit obligation, not
an evaluated integral supplied by the scalar sources. Its punctured-domain
integration must be checked; a known scalar normalization is insufficient.

No unread lead in the earlier assessments is essential to this direct
audit. Full and supporting Mathlib coverage remains **not checked**;
neither absence nor a matching theorem is inferred.

## Duplicate and failure comparison

The bounded local comparison read the full new L291 and its work note,
L287's weighted monomial bounds and Schur argument, L288's residual
covariance construction, L290's conclusion and the prior assessments.
It located the derivation awaiting review, not a separate completed
audit. It did not scan other notebooks or assert global novelty.

ATTEMPTS/047 retains the uncontrolled internal forest expectation;
048 retains the global absolute-norm loss; 049 shows why generic gauge
identities do not force the Wilson cancellation. They do not prohibit
checking this local source-factor construction. The audit must still
reject an uncontrolled summed error or a return to those insufficient
norm/identity arguments. History 509 confirms that upstream L286–L290
audits remain outstanding; a conditional acceptance of L291 cannot
silently discharge them.

Two narrow queries were made on 2026-10-26:

- `"lattice gauge" "source" "finite range" "polynomial" covariance`
- `"Wilson" "plaquette" "cubic" "relative boundary"`

Returned discovery snippets concerned other models, simulations or
different observables; none established coverage. They were not used
as theorem evidence. No novelty conclusion follows from these searches.
The stronger source comparisons are reused rather than repeated.

## Later audit obligations and decision test

The later audit must test the common-noise construction (retained and
residual fields are correlated), all six residual products, complete
time-half bounds, the exact cross-half vanishing at fixed m, the
constant-field tensor with two different internal covariances, and
the order N then m of the limits. Check the independent-field factor
four, internal color factor two, external color factor three, two
halves and the original one-half prefactor. Check the weighted integral
and its punctured-domain boundary term. The intended criterion is a
complete proof of o(N^2), not O(log N), with inherited upstream audit
gaps explicit. L286–L290 have not had separate critical audits.

Accept the new proof only if the complete normalized error tends to
zero and the exact tensor coefficient is obtained. Otherwise preserve
the completed attempt and isolate the precise failed assertion for
repair; do not infer a Yang–Mills disproof. Continuum existence, a
nonzero physical sector, uniform higher remainder and positive finite
mass remain independent gaps.

In particular, check that conditioning in each half preserves precisely
the independence actually used, while the complete two-half L2 estimate
retains correlations. Check covariance domination by congruence without
commuting source weights with L; the residual edge/curl diagonal bounds
and retained operator bound must suffice for every one of the six
products. Fixed-m support and covariance ranges must cover curl offsets,
the support-edge rows and all relative faces before taking N to infinity.
For the tensor calculation retain the two distinct internal covariances,
the actual Wilson phases, and the external direction restriction. Check
the full Riemann sum, not just a row or a formal bulk value. The final
substitution uses L290(3)–(4) conditionally on its still unaudited inputs.

Continue only with a complete conditional proof or a precise failed
assertion and repair target. If an essential theorem outside the saved
scope is needed, register its separate source gate before dependent
mathematics. This review approves scrutiny, not L291's truth. No new
lemma, mathematical script, DAG edge or PROOF.md argument is produced.
Completed outcome EXPLORATION, kind LITERATURE, classification
NOVELTY_UNCHECKED, actual task literature_comparison. Mathematical
exploration usage is zero; no supervisor counter reset is claimed.
