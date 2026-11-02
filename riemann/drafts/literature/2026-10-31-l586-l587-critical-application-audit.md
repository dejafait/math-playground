# Second cone and bounded probability assembly: critical-audit coverage

TARGET: Critically audit L586 and L587 for finite-cone interiority, fixed-dictionary interpolation, probability normalization and all 147 eventual-ray bounds.
CHECKED: 2026-10-31
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the saved second-cone, full-moment assembly, L585 audit and bounded-occupation failure assessments; searched the complete L586/L587 for actual source uses, then retrieved the same primary theorem/proof passages. No broad search or claim of novelty.
SOURCE_EVIDENCE: Read Blekherman--Fialkow arXiv:1804.04276v1 setup p.1, section 2 setup p.5, Proposition 2.1/Corollary 2.2 and complete proofs p.6, Remark 2.4 p.7; Bayer--Teichmann math/0502473v2 Theorem 1/proof pp.2--3, Corollary 2/Remark 2/proof pp.3--4; Tao 245C Notes 2 (6 April 2009), (3), Theorem 21 torus proof and Corollary 22. Reused L585's completed audit and qualified L473 formulas.
COMPARISON: Inspected sources cover actual finite evaluation-cone interiority, integrable nonpolynomial finite cubature and circle Parseval. They do not verify L586's spectral/function-space specialization or L587's uniform finite-dictionary probability assembly; those are the unchanged mathematical audit target.
GAP: Source scope for the joint audit is ready, but L586/L587 remain critically unaudited. Spectral normalization/integrability, common span, strict positivity, fixed-dictionary uniformity and all 147 eventual-ray bounds still need mathematical verification. Arithmetic proofs remain imported.
REASON: Separate literature-only approval now permits the exact saved conceptual audit, using standard results without reproof. No new result or mathematical audit verdict is established in this step.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED nominated a joint critical audit after L587; compare its exact uses with existing ready coverage before undertaking it. This required approval is now complete; further unchanged-scope literature is unnecessary.
SCOPE: Audit L586 and L587 as stated from L473 (1)--(2), (6)--(9) and audited L585 (1); real smooth periodic paths with differing periods allowed, nonnegative finite weights, ordinary derivatives through order two and fixed lag one, all 21 second and 126 fourth entries on one eventual real-H ray. Clipping, full-law realization and Xi transfer are excluded conclusions.

## Completed source comparison, 31 October 2026

This is the separate source-scope approval of the exact TARGET, not its
mathematical execution. The main gap remains actual-Xi all-degree signs
at unbounded heights. Verifying the moment-feasibility interface could
support future sign-sensitive path constructions; positive order-ell
clipped mass, selected-law realization and actual-Xi transfer remain
independent. No new lemma, calculation, script or theorem reproof was
performed. The argument overview and DAG are unchanged.

Read the complete L586/L587 to locate their actual theorem uses; read
L473 through (1)--(2), (6)--(9), and L585 hypotheses/conclusion (1) and
the opening of its completed audit. Reused these assessments:
`2026-10-31-periodic-second-cone-interior.md`,
`2026-10-31-periodic-full-moment-probability-assembly.md`,
`2026-10-31-l585-periodic-carrier-audit-scope.md`, and
`2026-10-31-bounded-periodic-occupation-moment-compensation.md`.
Their recorded searches and stronger-result comparisons remain adequate
for unchanged hypotheses. A fresh general discovery search would repeat
that coverage. Direct source retrieval succeeded; no essential blocker
remains. All page numbers below are printed manuscript page numbers.

### Actual finite-cone interior

Blekherman--Fialkow, *The core variety and representing measures in the
truncated moment problem*, [arXiv:1804.04276v1](https://arxiv.org/pdf/1804.04276v1#page=6),
Proposition 2.1 and Corollary 2.2, p.6; setup pp.1,5 and Remark 2.4 p.7.
The setting is a nonempty T1 space and a finite-dimensional space of real
Borel functions. Strict positivity on its nonzero nonnegative functions
characterizes interior of the finite evaluation cone. Read the bipolar
argument, equality of interiors for convex cones, perturbation by an
evaluation and final atom-insertion argument. Remark 2.4 separates later
standing assumptions from this corollary. PDF extraction loses closure
bars in its proof; Proposition 2.1 concerns closure, whereas Corollary 2.2
explicitly concerns interior of the finite cone.

L586 proposes the interval I and the actual space E of spectral entry
functions. Its identification with the matrix span, quotient by zero
functions and strict-positivity check remain audit obligations. Ambient
PSD interior or positivity on a smaller collection of functions is not
this source hypothesis. No new general separation/interior theorem is
needed. This is sufficient source scope, not verification of the proposed
identification or positivity argument.

### Integrable spectral compression

Bayer--Teichmann, *The proof of Tchakaloff's theorem*, Proc. Amer. Math.
Soc. 134 (2006), 3035--3040,
[math/0502473v2](https://arxiv.org/pdf/math/0502473v2#page=3),
Theorem 1/proof pp.2--3 and Corollary 2/Remark 2/proof pp.3--4.
The corollary takes a positive measure, a measurable finite vector map,
a measurable full-measure node set and an integrable pushforward norm;
it gives positive finite quadrature for all components. Read the
lower-dimensional reduction, strict supporting-plane case and
pushforward/lift proof. Remark 2 explains the additional constant
coordinate needed to preserve finite mass.

This covers the nonpolynomial spectral observable proposed in L586;
the audit must check its measurability, integrability and zero-measure
case. Cubature alone does not establish prescribed moment feasibility
or a uniform normalized weight for varying targets. L587 instead claims
to obtain uniformity from two fixed representations and finite convex
interpolation; that application must be checked independently. Its
probability normalization is explicit and must not be inferred merely
from the conic quadrature theorem. Common period and compact unrestricted
frequency support are not source requirements.

### Circle Fourier input and other standard tools

Tao, [*245C, Notes 2: The Fourier transform*](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/),
6 April 2009, equation (3), Section 2 Theorem 21 and Corollary 22.
Read the torus proof by Stone--Weierstrass and density in L2, the
two-function Parseval formula and the translation convention. The
compact-group theorem assumes probability Haar measure; the torus case
is proved in this passage even though the general compact-group proof
is deferred. L586 uses only a circle with its normalized period average.
Check the angular-frequency units, derivative coefficients, forward-lag
phase, constant mode and conjugate-pair counting during the audit.
Pointwise Fourier convergence is not the needed theorem.

The holomorphic identity theorem is the named standard input for L586's
proposed common-span argument. Its entire extensions and annihilator
logic still need checking. L587's remaining operations use finite
linear algebra, finite-mixture integration and whole-path homogeneity;
no stronger representation theorem is needed. Rockafellar--Wets
relative-interior/closure coverage is already recorded in L585's audit
assessment; no new read or additional import is claimed here, and
L586 invokes the direct moment-cone corollary instead. The saved di Dio,
Richter and Bochner comparisons are not additional theorem premises.
Full matching Mathlib coverage remains unchecked.

### Mathematical audit still to perform

Keep L473's exact coordinate convention and reference estimates; its
arithmetic proofs, particularly Bui--Hall Proposition 3, remain imported
and unaudited. Audit L586's spectral zero/conjugate modes, absolute
summability and finite compression, the restricted/unrestricted span,
actual-function-space duality, strict positivity and absorption on a
single real-ell ray. Then audit L587's two fixed finite dictionaries,
normalization of whole paths, nonnegative interpolation, mass-one law,
every-phase support, every second/fourth entry and common onset.

In particular retain all four tight same-height odd second bounds from
L473 (2), with H^(-2/3)ell^(-1) or H^(-2/3)ell^(-3), as appropriate.
Do not substitute a generic O(1) error. Distinguish L587's claimed
O_m(ell^2) error relative to ell^4 q_m from its claimed O_m(ell^3)
error relative to the reference F_m(H). No numerical dictionary or
effective constants are required, but every finite choice must be
fixed before the eventual-ray assertion.

The saved failure comparison preserves L578/L579's packet-dictionary
restrictions, L581's exact corrected-law obstruction and L584's
absolute-budget stop. None is a general separator for this tolerance
problem. No stopped mechanism is reopened or cross-notebook input used.

Continue if the exact hypotheses and all load-bearing application
steps pass. Repair a concrete error if possible; otherwise retain the
failed claim and its scope and abandon that application mechanism.
An unresolved essential premise is not an audit pass. No new creative
central-sign target is justified by this source comparison: the pending
essential audit precedes any clipping/Xi-transfer mechanism. Next is
proof_audit/conceptual_audit, deep_research/xhigh, on the unchanged TARGET.

## Invocation-start nomination (historical; superseded by coverage above)

The nomination below records the previous unauthorised scope; approval
is supplied only by the completed source comparison above.

Reuse `2026-10-31-periodic-second-cone-interior.md` and
`2026-10-31-periodic-full-moment-probability-assembly.md`, together
with L585's completed audit coverage. This nomination is not a fresh
search, a source approval or a mathematical verdict. Assess the exact
audit target before its execution; avoid repeating unrelated searches.

Essential inputs are L473 (1)--(2), (6)--(9), L585 (1), the complete
L586 proof, and L587. Verify the Fourier zero-mode and conjugate-mode
normalizations, spectral integrability and finite compression, equality
of restricted/unrestricted spans, actual function-space duality, and
the interior theorem's exact hypotheses. Then audit L587's two fixed
finite representations, normalization of whole paths, nonnegative
interpolation, mass-one mixture, phasewise support, every second and
fourth entry and a common eventual real-H onset. No numerical dictionary
or effective constant is required by either statement.

Continue only if these claims hold with the saved source hypotheses;
repair a real error or retain a decisive obstruction if they do not.
Passing the audit would validate the moment-feasibility interface only.
Positive order-ell clipped mass, selected-law realization and actual-Xi
transfer remain independent. L473's arithmetic source proofs, especially
Bui--Hall Proposition 3, remain imported and unaudited. No cross-notebook
input is needed. Full matching Mathlib coverage remains unchecked.
