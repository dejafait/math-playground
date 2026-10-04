# Auxiliary-first free BRST Ward identity — completed assessment

TARGET: At fixed mesh, test the free BRST Ward identity for L013's auxiliary-first prescription by extending it to polynomial b, c and bar c insertions and removing a positive connection regulator.
CHECKED: 2026-10-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched finite-dimensional BRST Gaussian Ward identities, real auxiliary contours, regulator-modified Slavnov–Taylor identities, polynomial Fourier transforms and Berezin integration; read Ellwanger, Witten, Caracciolo–Sokal–Sportiello, Melrose and Robinson, and reused the prior Gaussian and boundary assessments.
SOURCE_EVIDENCE: Read https://arxiv.org/pdf/hep-th/9402077v2 printed pp. 2–3 and 5–6, (7)–(10), (20)–(22); https://arxiv.org/pdf/1805.11559v3 printed pp. 8–9, (2.18)–(2.21); https://arxiv.org/pdf/1105.6270v2 Theorem A.3, (A.48)–(A.64), and Theorem A.16, printed pp. 101, 107–109, 116–117; https://math.mit.edu/~rbm/18.199-S08/Chapter1.pdf (1.8)–(1.10), (1.59)–(1.66), Theorem 1.3, printed pp. 14, 21–22; https://ems.press/content/serial-article-files/40708 finite-dimensional discussion and Remarks, p. 183. Reuse the Gaussian Fourier input already read at https://dlmf.nist.gov/1.14.T1.
COMPARISON: Known finite bosonic and fermionic Gaussian formulas cover polynomial insertions, graded Berezin rules supply the algebraic integration input, and an established modified Ward identity retains regulator variation. No inspected theorem proves their complete applicability to L013's real b-first prescription and removal of a connection regulator on the relative cube.
GAP: Fix BRST signs against L013's Fourier phase and Berezin orientation, define the polynomial extension, justify regulated integration by parts, and prove convergence of normalized polynomial expectations and disappearance of the breaking insertion at each fixed mesh. The unregulated joint modulus remains nonintegrable.
REASON: Approve reproduction of this bounded finite-dimensional applicability test, using the known inputs rather than reproving Gaussian or cochain theorems. Preserve the saved target; the Ward identity and regulator removal are not proved in this literature turn.
SCOPE: L013's quadratic three-colour theory at fixed even N >= 2, with unchanged relative cochains, real b, interior-vertex ghosts, polynomial insertions and a positive quadratic connection regulator removed before any mesh limit. Nonlinear forest-measure replacement, continuum boundary traces, physical-boundary counterterms and ultraviolet-uniform interacting estimates are outside coverage.
COVERED_TARGET: At fixed mesh, define the polynomial auxiliary/ghost extension of L013 by auxiliary-first integration and test convergence after removing a positive connection regulator.
COVERED_TARGET: At fixed mesh, test the regulator-modified free BRST Ward identity for L013's polynomial auxiliary/ghost extension, retaining the Grassmann parity sign and regulator variation.

## Preserved target, relevance and prior failures

The TARGET is exactly the saved Next action at turn start. The prior [covariance assessment](2026-10-03-auxiliary-boundary-gaussian-matching.md) remains unchanged and is reused within its scope. The [boundary counterterm assessment](2026-10-03-boundary-brst-counterterms.md) already delimits the bulk cohomology and smooth-domain claims. The official Yang–Mills target and finite-mass qualification are reused from that assessment's 2026-10-03 primary-statement check and the existing [source audit](../../foundations/01-target-and-scope.md).

Keep the same finite relative cube, quadratic fields, real Fourier auxiliary variable and interior vertex ghost spaces. The gap is a justified free Ward identity on the enlarged observable algebra, not another computation of curvature covariance. Its plausible downstream use is a legitimate regulated Gaussian starting point for a later boundary Ward formulation. L013 already establishes the connection law and nonzero normalization, but explicitly leaves this extension open. Its original joint modulus has flat gauge directions; formal changes of variables in that expression remain unjustified.

The whole overview, DAG, L013 and the preceding covariance working record were inspected for redundancy. L012's rejected unrestricted smooth normal-Neumann domain stays stopped. The exhausted bulk-locality route is not reopened, and its 3-of-3 budget remains recorded. A finite free identity would not invalidate that smooth-domain counterexample or permit replacement of L011's nonlinear forest measure.

Even a successful free identity would not replace L011's nonlinear forest measure, classify physical-boundary counterterms, control the O(1) remainder, establish finite interacting matching or supply the required reflected error <= c_box/2. Field construction, limiting reflection positivity, infrared control and finite positive mass remain separate gaps.

## Search and access record

The bounded search used these queries, with adaptive follow-ups to primary sources:

- BRST Gaussian finite dimensional Nakanishi Lautrup imaginary auxiliary polynomial Ward identity regulator
- Ellwanger modified Slavnov Taylor identities exact renormalization group infrared cutoff BRST 1994
- finite dimensional BRST integration by parts Berezin integral Ward identities Mathai Quillen
- Berezin integration Gaussian integration by parts finite dimensional pdf
- "Gaussian" "Nakanishi" "Ward identities" "finite"
- "auxiliary-first" "BRST"
- "Fourier transform" "derivative" "Schwartz" site:math.mit.edu
- "Algebraic/combinatorial proofs of Cayley-type identities" site:arxiv.org

These searches found applicable components, not a complete theorem for the exact prescription. The narrowly phrased auxiliary-first query supplied no match; that is not evidence of nonexistence or originality. Search snippets, secondary QFT pages and recent speculative preprints supply no mathematical premises.

Browser PDF text provided the inspected primary passages. The Robinson scan has imperfect mathematical OCR; its integration-by-parts discussion was read, while explicit sign conventions are taken from the legible Caracciolo–Sokal–Sportiello appendix instead. PDF screenshot requests supplied no usable additional formula evidence. A single command-line retrieval of the EMS PDF failed DNS resolution; no further command-line retry was made. Publisher landing pages also failed to open, but the primary PDFs were readable. No essential supporting source remains unread. Skinner's supersymmetry course and the broader Mathai–Quillen search are nonessential leads, not inspected theorems or inputs.

## Inspected statements and applicability

### Auxiliary BRST algebra

E. Witten, *A Note On Boundary Conditions In Euclidean Gravity*, [1805.11559v3](https://arxiv.org/pdf/1805.11559v3), 15 July 2023. Its gauge-theory example, printed pp. 8–9, (2.18)–(2.21), introduces the nilpotent ghost transformations, the independent antighost/auxiliary pair and a BRST-exact gauge-fixing addition, then eliminates the auxiliary field. This is supporting algebraic coverage. The trace, auxiliary and transformation conventions differ from L013's explicit positive real b Gaussian with an imaginary Fourier coupling. The future test must check that translation of conventions against the actual integrand; elimination alone cannot justify auxiliary insertions or a real integration contour. Smooth continuum boundary statements remain confined to the earlier assessment.

### Regulator-modified identities

U. Ellwanger, *Flow Equations and BRS Invariance for Yang-Mills Theories*, [hep-th/9402077v2](https://arxiv.org/pdf/hep-th/9402077v2), 29 July 1994; published in *Physics Letters B* 335 (1994), 364–370. Read the Euclidean transformations and cutoff action, printed pp. 2–3, (7)–(10), and the modified identity and continuation discussion, pp. 5–6, (20)–(22). Equation (20) retains the cutoff-action variation alongside source variations. The following identities describe compatibility with the renormalization-group flow and recovery of the standard identity as the infrared kernels vanish, with the stated nonexceptional-momentum qualification. The path-integral derivation assumes an invariant ultraviolet regularization; the subsequent flow formulation does not require that representation. Thus this is a close precedent for retaining a breaking term, not an existence or convergence theorem for L013's ordered auxiliary integral. Its auxiliary field has already been eliminated.

### Explicit finite Gaussian and Grassmann inputs

S. Caracciolo, A. D. Sokal and A. Sportiello, *Algebraic/combinatorial proofs of Cayley-type identities for derivatives of determinants and pfaffians*, [1105.6270v2](https://arxiv.org/pdf/1105.6270v2), submitted 31 December 2012, manuscript revision dated 27 November 2012; *Advances in Applied Mathematics* 50 (2013), 474–594. **Theorem A.3**, printed p. 101, gives finite real Gaussian source and moment formulas for a positive-definite matrix, allowing complex source vectors. Appendix A.4, (A.48)–(A.64), pp. 107–109, fixes odd differentiation, the graded product rule, top-degree integration and **Proposition A.11**, the finite Grassmann Fubini rule. **Theorem A.16**, pp. 116–117, gives the fermionic source and polynomial-insertion formulas, including the invertibility hypothesis for inverse-matrix expressions. These are matching supporting inputs for finite polynomial integration. Their exponential and orientation conventions must be reconciled with L013's; the theorem is not a combined BRST/regulator-removal statement.

P. L. Robinson, *The Berezin Calculus*, [*Publ. RIMS* 35 (1999), 123–194](https://ems.press/content/serial-article-files/40708). Read the finite-dimensional discussion around Theorems 1.11–1.13 and the graded integration-by-parts discussion in Remarks, printed p. 183. This confirms the finite algebraic integration framework. It supplies neither bosonic decay nor a theorem permitting arbitrary order in L013's original joint integral; the explicit conventions above avoid depending on imperfect scan transcription.

### Polynomial auxiliary Fourier transforms

R. Melrose, *Preliminaries: Distributions, the Fourier transform and operators*, [Chapter 1 in the MIT 18.199 Spring 2008 materials](https://math.mit.edu/~rbm/18.199-S08/Chapter1.pdf), as read on 2026-10-04; no separate revision date is asserted. Read (1.8)–(1.10), printed p. 14, and section 1.7, (1.59)–(1.66), **Theorem 1.3**, pp. 21–22. Gaussian functions are Schwartz; differentiation and polynomial multiplication preserve that space. The Fourier transform is an isomorphism on it, and the stated multiplication/differentiation formulas follow from absolutely convergent integrals and integration by parts. This supports polynomial auxiliary insertions at fixed A. Its Fourier convention differs from the reused [NIST Gaussian transform](https://dlmf.nist.gov/1.14.T1). Neither reference establishes normalized connection-regulator removal for this notebook; that is the remaining applicability argument.

## Comparison and continuation decision

| Obligation | Coverage and remaining difference |
| --- | --- |
| Nilpotent free transformations | Known auxiliary algebra is available; fix the local Fourier phase and parity conventions before using it. |
| Polynomial auxiliary and ghost expectations | Finite Gaussian, Fourier and Berezin formulas are covered; define the enlarged ordered functional and retain its normalization. |
| Positive connection regulator | A positive quadratic damping term is a concrete candidate; justify absolute bosonic convergence and integration by parts for it. |
| Regulated Ward identity | A modified-identity precedent explicitly retains regulator variation; check the complete local graded identity. |
| Removal at fixed mesh | Prove convergence of each normalized polynomial insertion and vanishing of the breaking expectation. No joint unregulated absolute-convergence claim is available. |
| Mesh limit and interacting boundary use | Outside coverage; no uniform estimate or nonlinear gauge replacement follows. |

**Decision: SPECIALIZE.** The unchanged TARGET and the two listed subtargets are ready for mathematical reproduction. Import the supporting Gaussian, Fourier and Berezin results by their precise citations. A repeat proof of L003's cochain positivity, L013's connection covariance, or the general Gaussian theorems would be redundant. The needed work is their applicability to the enlarged polynomial functional and the regulated Ward change of variables. No result beyond the checked literature is suggested.

For the proposed test, keep the real b contour and L013's ordered integration. A concrete candidate connection regulator is epsilon times the sum of the three squared connection norms divided by two, epsilon > 0. At fixed mesh, require a well-defined normalized extension on all polynomials in A, b, c and bar c; consistent nilpotence and action signs; and a justified regulated identity with the breaking insertion retained. Regulator removal must be proved on those normalized expectations, after auxiliary/ghost integration where necessary. In particular, a bare factor epsilon is not by itself a proof that its expectation vanishes. Any bounds may depend on the fixed mesh; this assessment does not approve exchanging regulator removal with mesh refinement.

Mixed insertions such as an antighost times a connection linear form, and an antighost times an auxiliary coordinate, are proposed sign and convergence tests in addition to the all-polynomial argument. No values or identities for these tests are calculated here. Continue this prescription only if both the regulated identity and its removal are justified. An undefined polynomial extension, phase inconsistency or surviving breaking term would stop this Ward realization and require an independent mechanism. A failure in this finite test would not disprove the Yang–Mills target.

The completed review is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED, with new source comparison and ready bounded coverage, not a mathematical advance. The intended mathematical step is REPRODUCTION. This literature turn spends no calculation turn: zero inconclusive mathematical attempts remain recorded on the auxiliary-field route. STATUS stays IN_PROGRESS, with no candidate resolution. No Ward result, lemma, mathematical script, argument assembly or DAG change is made.

## Mathlib

Coverage of the full prescribed free Ward identity, polynomial auxiliary/ghost extension and regulator-removal statement: **not checked**. Supporting Gaussian, Schwartz Fourier and Berezin library coverage: **not checked**. The theorem names and direct source links above identify supporting results, not a match for the full statement. No absence, originality or persistent source-blocker claim is made.
