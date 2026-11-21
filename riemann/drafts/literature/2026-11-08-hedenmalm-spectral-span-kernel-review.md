# Actual spectral domain: completed kernel-intersection source review

TARGET: Assess whether ker L intersects H_finite trivially for Hedenmalm's full complex-zero eigenfunction span, without assuming RH or simplicity.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step145 searched the exact identifier with kernel/span/independence, Hedenmalm finite-domain terminology, distinct-eigenvalue independence, resolvent-vector independence and constant-coefficient ODE results; inspected primary statements below and narrowly checked local Hedenmalm stops. No exact matching intersection theorem was located; no novelty inference follows.
SOURCE_EVIDENCE: Hedenmalm arXiv:2606.17494v1 https://arxiv.org/pdf/2606.17494v1 pp5-8, (3.3.2), Theorem3.3.1 kernel proof, Theorem3.3.3 and Section4.2; Faris, Linear Algebra (4 May 2005), Theorem9.2 pp47-48 https://math.arizona.edu/~faris/linlecture.pdf; Tao, 245C Notes2 (6 April 2009), Exercise30, Definition32, Exercise38 and Fourier inversion (11) with its preceding Gaussian proof https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/; Cayley-Hamilton, precise finite-free-module statement LinearMap.aeval_self_charpoly https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Charpoly/Basic.html#LinearMap.aeval_self_charpoly.
COMPARISON: Eigenvector independence presupposes a genuine endomorphism and cannot validate the unconstructed inverse. Cayley-Hamilton and Schwartz Fourier differentiation/inversion supply standard inputs for an independent finite-family test, while L906 supplies audited theta endpoint estimates. The actual kernel-intersection specialization is not proved in this review.
GAP: Future work must justify the complex-parameter integral identity, a hypothetical finite invariant space, logarithmic Schwartz hypotheses and the Fourier contradiction with all constants and finite-dimensional hypotheses checked. No Mellin-to-Xi normalization, generalized eigenfunctions, positive form or symmetry is covered.
REASON: Approve only a bounded source specialization for the specified finite spectral domain. This can settle the representative ambiguity prerequisite without repeating the V obstruction; positive realization and all-degree mixed positivity remain independent gaps.
LITERATURE_REASON: The changed H_finite target was REVIEW_REQUIRED; the ready enlarged-domain assessment did not cover finite spectral-span injectivity or the requisite independence comparison.
SCOPE: Finite complex linear combinations of the source's explicitly defined u_alpha at all Xi zeros, without RH or simplicity; use L906's analytical estimates and the inspected standard algebra/Fourier inputs. No completion, generalized chain, new metric, or full eigenvalue-characterization reproof is covered. Separate supervisor acceptance precedes research using this changed ready assessment.
COVERED_TARGET: Assess whether ker L intersects H_finite trivially for Hedenmalm's full complex-zero eigenfunction span, without assuming RH or simplicity.

## Preserved nomination (before step145)

The nomination required a literature-only turn. Its exact question was
whether ker L intersect H_finite={0}, with the source's differential
operator and full complex-zero span. Use the source's exact definition
of its functions u_alpha and distinguish a span of eigenfunctions from
any unasserted generalized-eigenfunction extension at multiple zeros.
Neither RH, simplicity, completeness nor a positive metric may be
assumed. No answer or finite-family independence argument is derived
in this nomination.

Essential context is canonical L906 and the completed assessment
`2026-11-08-hedenmalm-operator-pair-source-review.md`. The kernel
formula and domain definitions are reusable source evidence; the
old SPECIALIZE assessment does not cover this changed domain.
Check exact statements, stronger results and recorded failures before
approving any proof attempt. If a Mellin argument is proposed, its
normalization and convergence need their own source verification;
the earlier normalization warning remains unresolved.

Plausible downstream use: a verified answer would settle whether the
specific representative ambiguity persists on the source's intended
domain. It would not supply symmetry, a nondegenerate positive form,
closure, completeness or actual-Xi all-degree mixed positivity.
Continue only with a precise covered claim and a bounded proof test;
park dependent research if essential source coverage stays blocked.
If the intersection is nontrivial, retain the corresponding domain
obstruction; if it is trivial, do not report a spectral realization.
Full and supporting Mathlib coverage was unchecked at nomination.

## Completed source comparison, 8 November 2026 (step145)

This turn reviewed sources only. It proves no kernel-intersection,
independence or spectral-realization result. The main gap remains
L030-L032/C032a actual-Xi all-degree mixed positivity. L906 is the
essential local analytical input; the prior pair assessment supplies
the reused comparison with positive-realization claims. No
cross-notebook input is used.

### Exact domain and omitted source obligations

The versioned PDF's Theorem3.3.1 proof, pp5-6, gives
Lf=w D(f/w) and hence its smooth kernel description. Equation
(3.3.2), p5, gives (D+alpha)u_alpha=w/i in the real case.
Theorem3.3.3, p7, specifies the same integral for complex alpha;
its proof is omitted. Section4.2, p7, explicitly uses finite sums
over every complex zero, not merely the known real zeros. Repeated
zeros label the same displayed function; no parameter derivatives
or generalized eigenfunctions are included. Theorem4.2.2 and
Corollary4.2.3, p8, assume the form/symmetry input; their individual
eigenfunction statements do not assert finite-span injectivity.
The PDF governs pagination; its corresponding HTML was cross-checked.

The future test may use the integral definition directly. It must
check convergence at zero and the product-rule identity for each
fixed complex alpha; the printed omitted complex proof is not an
audited substitute. This limited check is justified by the changed
complex hypotheses and is not a reproof of the full boundary-value
characterization. No identification of the Mellin integral with Xi
is needed merely to study this explicitly specified span. Preserve
the existing normalization warning for any later zero/positivity
transfer. Use L906's complete differentiated theta bounds, not the
source's unaudited small-t printed bound.

### Standard inputs inspected and applicability limits

Faris, Theorem9.2, pp47-48, assumes one already defined linear map
V to V and nonzero eigenvectors with distinct eigenvalues. Its
polynomial-separation proof was read completely. Calling the
u_alpha eigenvectors of -LDL^{-1} before proving descent would
leave that hypothesis unpaid. This theorem is comparison evidence,
not an injectivity import. No assertion of simplicity follows.

Cayley-Hamilton applies to an endomorphism of a finite-dimensional
complex vector space, without diagonalizability or distinct roots.
The inspected Mathlib statement more generally assumes a finite
free module over a commutative ring and annihilates the map by its
characteristic polynomial; charpoly_monic is on the same page.
Finite dimensionality and invariance of any proposed function space
must be established in the future specialization, not assumed from
the word spectral. No Cayley-Hamilton reproof is needed.

Tao's Notes2, Exercise30 and Remark31, state Fourier differentiation
under L1 derivative and fundamental-theorem-of-calculus hypotheses.
Definition32 requires rapid decrease of every derivative for the
Schwartz class. Exercise38 preserves that class under Fourier
transform. Formula(11) inverts the transform on that class pointwise;
the preceding proof uses Exercises40-42, Gaussian convolution and
Schwartz convergence. These statements and the whole displayed
inversion argument were read. The convention is exp(-2pi i x xi)
for the forward transform. It is ordinary Fourier analysis on the
logarithmic real variable, not an imported Mellin normalization.

These standard inputs are stronger tools than distinct-eigenvalue
independence for this purpose: they permit testing a finite invariant
space without defining L^{-1}, assuming real parameters, or assuming
semisimplicity. Their application to this particular span remains
to be written. No matching full theorem for the theta-domain
intersection was found among the sources inspected; a source citation
alone does not perform that application. General ODE and resolvent
search hits not listed as inspected above remain unread leads.

### Bounded proof test approved for a later turn

Test whether a hypothetical nonzero kernel representative in one
finite spectral span forces a finite D-invariant space containing w.
If so, seek a contradiction using Cayley-Hamilton and the Fourier
inputs on W(x)=w(exp(x)). The future proof must establish every
Schwartz seminorm from L906's logarithmic derivative estimates,
justify the complex integral relation, and verify the actual
polynomial multiplier and its nonvanishing requirements. This is a
proof plan with unresolved obligations, not a derived contradiction.
It avoids relying on zero simplicity, a zero-free region, the
unverified Mellin constants or an inverse operator.

Continue this finite-domain prerequisite only if those obligations
can be discharged. Record a concrete failure if invariance or the
analytic hypotheses fail; do not rescue it by silently changing the
domain, using generalized eigenfunctions, or restricting to real
zeros. If intersection is trivial, record precisely that result;
if nontrivial, give an actual finite representation and obstruction.
Neither answer supplies the missing positive form or symmetry.
This is routine specialization of standard inputs, not a creative
central mechanism or a novelty claim. The lack of independently
specified metric data still blocks such a creative realization test.

### Search record, duplicates and Mathlib

Queries included `Hedenmalm spectral linear independence`;
`2606.17494 kernel span`; `2606.17494 independent`;
`Hedenmalm H finite kernel zeta`; `linear independence eigenvectors
distinct eigenvalues theorem linear operator`; `2606.17494 kernel
independence`; `resolvent vectors linearly independent cyclic`;
`constant coefficient differential equation solutions exponential
polynomials theorem university notes`; and targeted Tao/Mathlib
Fourier and Cayley-Hamilton queries. Exact-paper searches mostly
returned listings and secondary summaries, which were not theorem
evidence. Failure to locate a match establishes no originality.

Narrow local searches and reads covered the pair source assessment,
L906's statement, complete endpoint estimates and audited scope,
the enlarged-domain and positive-pair ATTEMPTS stops, and the prior
formal-inverse assessment. No duplicate spectral-span result was
identified in that scope. Preserve both stops: L906 does not put w
in H_finite, and the missing metric stop is independent of injectivity.
Initial notebook-scoped git status output was oversized; it was
replaced by exact-path status/numstat checks. No conclusion uses a
truncated preview, and unfinished existing changes are preserved.

Supporting Mathlib coverage inspected: LinearMap.aeval_self_charpoly
and LinearMap.charpoly_monic on the direct documentation page above.
The FourierTransform page search found no injectivity match; this
single-file check establishes no absence. Full theta-domain coverage
and other Fourier/Schwartz supporting coverage remain unchecked.
No lemma, mathematical script, DAG edge or PROOF argument changed.
