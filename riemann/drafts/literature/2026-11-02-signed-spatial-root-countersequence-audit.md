# Proposed critical audit of the signed full-root countersequence

TARGET: Critically audit L669's signed full-root countersequence, including the fixed-K Gram limit, actual-n contraction, full-polynomial remainder, degree-drop path and diagonal quantifiers.
CHECKED: 2026-11-02
DECISION: EXPLORE
SEARCH_EVIDENCE: Separate approval review completed 2026-11-02: read all of L669 for source scope and compared its actual imports with the ready parent assessment, the two-offset audit and signed-finite-deweighting assessment; checked the focused source-review/countersequence histories and recorded stability stop. Reused the exact-family searches; no fresh search or novelty claim.
SOURCE_EVIDENCE: Reuse inspected Brunault--Zudilin, Propositions 1.4--1.5 pp.6--7; Sinclair arXiv:math/0509591v2, Theorem 1.1 pp.1--2 and Section 2 pp.12--14; and de Boor, Divided Differences, Proposition 7 p.48 via the ready signed-finite-deweighting assessment for L668 interpolation existence. L664 supplies its audited approximation and derivative bounds; L649/L666 supply definitions; only L668's finite nonzero identity is used. No root-regularity or quantitative inverse-function theorem is invoked.
COMPARISON: The sources supply the complete-root identity and fixed-ambient-degree continuity, not the countersequence. The new local proof instead gives an explicit finite Gram limit, a fully specified convergent iteration and a uniform-in-M Taylor majorant. Its prior EXPLORE target already permitted a rigorous admissible countersequence; this review nomination does not approve its correctness or establish originality.
GAP: Independently check all constants and quantifiers, especially choosing K then L then the finite-n onset; verify the real control rank, nonlinear solvability within the cube, complete spatial cancellation and the signed full-root conclusion. No unproved input should be substituted for those calculations.
REASON: Separate source-scope approval is now complete for exactly TARGET. The written construction introduces no essential unread external theorem: finite sums, iteration and Taylor bounds are proof obligations for the mathematical audit. EXPLORE authorizes that audit, not the correctness of L669, a new countersequence derivation or an extension to the weaker benchmark. No essential source blocker remains.
LITERATURE_REASON: The supervisor required a separate approval turn for this newly nominated continuation. This step checks actual proof imports against reusable coverage rather than browsing again or reapproving the mathematics.
SCOPE: Audit L669 and repair errors within its stated countersequence hypotheses. Keep every original residue, grid factor and M spatial moments. Do not extend to a uniform-in-K onset, the weaker linear-rate benchmark, arbitrary support or Xi signs without a separate target assessment.

## Exact audit and bounded decision

Read L669 in full. Use L664 only for its audited delta=1/4 full-polynomial
approximation, the fixed-angle baseline and g bounds. L668's short finite
identity must retain its distinct-node/nonzero-weight hypotheses; its
inverse-data cost is irrelevant. L666's other, unaudited quadrature claims
are not inputs. The full definitions from L649 are retained.

The load-bearing claim is solvability of the actual finite-n nonlinear
moment equations with real |e_r|<=1/8 for every fixed K, after choosing
one sufficiently large finite L=L_K and then all sufficiently large n.
Check the oscillatory Gram limit using exp(2i*kappa)!=1, positivity of
the real limit matrix, column bounds on the right inverse, the entire
control-cube Hessian estimate, and self-mapping/contraction constants.
Check that the signed old/new functional is only bookkeeping for final
unit residues and cancels the full T_M Taylor polynomial, not a spatial
prefix. The derivative majorant must be uniform in M and the remaining
L664 error must be absorbed only with K fixed.

For the endpoint conclusion, apply the complete root identity to the
nonzero polynomial at each point of its straight path. Fixed-degree-
space continuity is used separately for each n, never as a growing-degree
modulus or derivative. Actual leading coefficients, every multiplicity,
circle roots and degree loss are retained. No root labeling, separation,
relative coefficient estimate, or monic normalization is assumed.

Accept the local obstruction only if the actual-n solvability, complete
polynomial bound and diagonal choice all survive. Otherwise record the
precise failure and weaken or retract only the affected claim while
preserving the derivation. In either case the weaker linear-rate mean,
support, realization and actual-Xi mixed signs remain independent.
No new calculation or lemma is approved beyond this audit scope.

## Source and Mathlib reuse

The precise primary citations are
[Brunault--Zudilin](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf)
and [Sinclair v2](https://arxiv.org/pdf/math/0509591v2), with theorem
and page numbers above. The parent assessment inspected the root formula's
boundary cases and Sinclair's complete Section 2, including escaping
roots and leading factors. General root-regularity and quantitative
Mahler-continuity estimates are unnecessary for this endpoint argument.
The original Chern--Vaaler source remains optional and unused.

Reuse the supporting
[Mathlib MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html)
scope already recorded: full-root identity, logarithmic integrability
and positive measure for a nonzero polynomial. Full coverage for L669's
finite-control construction or the degree-drop continuity import has
not been checked. The proposed audit must not turn unknown coverage
into an absence claim. No separate audit was performed in the turn
that constructed L669.


## Separate source-scope approval — 2 November 2026

Read L669 in full to identify its imported inputs, without verifying its
new estimates or changing its mathematical status. This approval preserves
the exact TARGET and EXPLORE decision. It removes the pending source gate
for one conceptual audit; it does not certify the countersequence.

The source-to-obligation comparison is as follows:

- L669 sections 1 and 6 use Brunault--Zudilin for a nonzero complex
  polynomial of its actual degree. The reused two-offset audit records
  the interior, exterior and boundary-root cases. Constants, multiplicities
  and leading factors are included; logarithmic perturbation bounds are not.
- Sinclair requires a continuous positive root function asymptotic to
  absolute value at infinity. The choice max(1,|z|) is within the inspected
  theorem, on a fixed finite-dimensional coefficient space. Application
  remains conditional on the audit verifying the coefficient path and
  nonzero slices for each fixed n. No uniform-in-n modulus is imported.
- The nonzero-slice argument uses only L668's finite identity. Its
  interpolation existence input is C. de Boor, *Divided Differences*,
  Surveys in Approximation Theory 1 (2005), 46--69, version dated
  21 December 2004, [Proposition 7 and proof, p.48](https://surveys-in-approximation-theory.com/papers/2/2.pdf).
  The ready `2026-11-02-signed-finite-deweighting-cost.md` records its
  inspected complex-node scope. Distinct nodes and nonzero weights must
  be checked along the path. Neither its inverse-data cost nor the
  coefficient/Mahler inequality is used by L669's construction.
- L664's audited bounds and L649/L666 definitions are local inputs,
  not new external imports. L666's quadrature claims remain outside
  scope. The Gram limit, positive real rank, actual-n contraction,
  whole-polynomial Taylor remainder and diagonal quantifiers in L669
  are precisely the unverified mathematics to be audited; the sources
  do not prove them. Finite-dimensional compactness and the explicitly
  written geometric iteration do not require a new quantitative theorem.

The prior exact-family comparison remains adequate: L665's anchor and
absolute-cost stops and L668's prescribed inverse-data stop do not settle
the signed full mean. L669 is the unique local candidate obstruction
identified by these focused records; no originality inference follows.
Parusinski--Rainer's monic regularity and the inaccessible original
Chern--Vaaler lead remain unused, so neither blocks this endpoint audit.

The bounded next step is unchanged: accept the local obstruction only
if every stated construction and endpoint obligation survives; otherwise
locate the exact failure and repair or weaken only the affected claim.
A new mechanism, weaker linear-rate estimate or Xi transfer needs separate
coverage. Reuse the Mathlib qualifications above; no new coverage claim,
mathematical script, proof audit or lemma modification was made here.
