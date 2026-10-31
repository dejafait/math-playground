# Family 003 selection measures — completed source comparison

TARGET: Assess whether the witness and prime-profile separations used by family 003 lem:high-bin at commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a realize L533's pointwise external-density contract while keeping row-dependent internal coefficient measures at their fixed moment order.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched only family003 local assessments, audit notes and histories for selection measures, common measures, row-dependent densities, witness separations and prime profiles; no completed application audit was found. Reused L533 and completed external-order coverage. In the pinned primary TeX searched sec:selection, prop:detector-witness, coefficient measure, row-dependent, lem:marked, lem:plain, lem:detector-dyads and lem:bin-prime-bound, then followed their precise analytic interfaces.
SOURCE_EVIDENCE: OpenAI September 30, 2026 manuscript, commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a: smooth-calculus definitions/statement and relevant proof 1019–1166; detector-dyads 4117–4225; detector-witness statement and separation 4235–4400; external-contour-tails statement/proof/application 5337–5458; marked statement 8682–8730; finite-propagation hypotheses 8803–8870, indexed coefficient/common-row qualifications 8939–9026 and separation/order discussion 9096–9149; inverse-amplification statement and scale-supremum case 11681–11725; plain hypotheses/statement 11812–11894; prime amplitudes 14192–14254; selection coefficient orientation, Sobolev use and moment application 14285–14449; complete high-bin statement/proof 14858–14993. Stable labels and exact interfaces are recorded below. Internal recursive arithmetic proofs were not audited.
COMPARISON: The source already claims the analytic ingredients: a common witness Fourier density on each fixed dyadic pair, untwisted dyadic/prime Mellin tests, and parameter Sobolev for rowwise witness choices. Selected rowwise frequencies are not themselves a common integration density. Internal coefficient measures remain governed by their fixed moment/common-row contracts. A later bounded application audit can test these interfaces with the arithmetic moment assertions explicitly retained as source contracts; this review does not verify their realization throughout the recursions or all of high-bin.
GAP: Audit the separation between common external densities, rowwise Sobolev parameters and internal coefficient measures in this application, including physical Im(z) and independence of internal orders from late external N. Complete internal kernel realization, the full buffered-coordinate matrix, auxiliary central accounting and manuscript/import closure remain independent gaps.
REASON: Essential unread witness/prime formulas have now been located and compared with the exact source contracts. Coverage supports the separately nominated application audit; no new lemma, derivation or mathematical application verdict is made in this literature-only step.
LITERATURE_REASON: The actual detector-witness profile and selection Sobolev construction, rather than another reading of the ready conditional tail calculus, were essential missing coverage at invocation start.
SCOPE: Source comparison for one selection-measure application interface, conditional on the cited marked/plain/amplification moment assertions with their finite-seminorm and label uniformity. It neither imports their entire arithmetic proofs as independently verified nor covers whole high-bin, complete coordinates or Xi signs.

## Source identity and inspected interfaces

OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re(s)>7/8*,
September 30, 2026, pinned commit above,
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Numbers are rendered TeX retrieval lines; labels identify statements.
Reuse [completed analytic coverage](2026-10-30-family003-external-order-independence-scope.md)
and L533. The following are source statements/formulas being compared,
not locally proved specializations.

| Interface | Precise source location | What must be kept distinct in the audit |
| --- | --- | --- |
| Witness separation | `prop:detector-witness`, 4331–4379 | Fix D,N,U,t before using the density; selected nu and zero height can vary by row. |
| Rowwise choice | `eq:parameter-sobolev`, 1056–1066, 1141–1154; `sec:selection`, 14350–14355, 14407–14410 | Supremum via derivatives and parameter integration, not Minkowski with row-dependent densities. |
| Dyadic contours | `lem:detector-dyads`, 4124–4147, 4151–4224 | Untwisted Mellin test; original zero extensions; one buffer; global/absolute discarded pieces. |
| Prime contours | `lem:bin-prime-bound`, 14192–14253 | Physical Im(z) translated first; fixed positive slot lengths; logarithmic division on an annulus. |
| Internal measures | `sec:moment-propagation`, 8803–8808, 8848–8869, 8957–8993, 9096–9149 | Conditional weighted moment contracts and common-row requirement; no internal trace conclusion. |
| Use in high-bin | `lem:high-bin`, 14870–14882, 14915–14926, 14963–14974 | Cardinalities are hypotheses; subdivisions are pointwise after moving the full correction. |

The explicit witness factor in the source is
\[
 H_{D,N}(s)=\Omega(s)[1-V_{\le}(2DNs/D_*)]
             e^{-DNs/Y_*}V_{\rm term}(DNs/U^{21}),
 \qquad D_*=U^t,\quad Y_*=U^{20}.
\]
Its separation is \(\widehat H_{D,N}(\nu)\,d\nu/(2\pi)\).
The source states uniform logarithmic derivatives and Fourier weighted
tails here. Its witness profiles are
\[
 W_M(x)=W_1(x)V_{\le}(Dx/D_*)x^{-\sigma-i(\gamma-\nu)},
 \qquad W_S(y)=W_2(y)y^{-\sigma-i(\gamma-\nu)}.
\]
For selected primes the coefficient identity is
\[
 \overline{\nu(p)}1_{p\in1_T}
   =|T|^{-1}\sum_{\theta\in\widehat T}(\overline\nu\theta)(p).
\]
Here the finite-ray character denoted nu differs from the real witness
frequency nu; that source notation must not merge the two roles.
See 14323–14349 for conjugation of the whole product and retained zeros.

The later audit must use the moment assertions with all their qualifications:
`lem:marked` requires the two positive fixed width margins, common row
orientation, row-independent slot coefficients/supports and finitely many
seminorms. `lem:plain` requires its stated row/mask family and disjoint
supports, the short-slot mesh and width inequality for live slots, and
beta_* <= (1+kappa)/2 when kappa<1. The selection sets kappa=2 beta_*-1;
this equality does not verify the moment proof. `lem:inverse-amplification`
requires sixth-power-free physical rows and retains its rowwise-test clause.
These assertions are upstream contracts for this bounded analytic interface.

## Result of this source review and continuation boundary

There is now a precise later test rather than an unspecified demand that
every selection variable be an external trace coordinate. Source formulas
identify what to test, but their correct application has not been proved
in this turn. In particular, commonness of a density on fixed blocks does
not authorize a common-measure inequality after arbitrary rowwise selection.
The source itself specifies the Sobolev alternative and warns about this
distinction at 9107–9113. The full recursive realization is not covered by
merely citing the abstract propagation lemma, which disclaims it at 8803–8808.

The [nominated audit](2026-10-30-family003-selection-measure-application-audit.md)
retains the moment assertions as explicit contracts and tests only their
selection-level analytic use. Pass requires named common external tests,
no trace of a merely internal L1 measure, physical Im(z) bookkeeping, and
unchanged fixed internal orders when the external order increases. A missing
condition parks that dependent application; another abstract tail replay
would not resolve it. No proof of the whole coordinate list, arithmetic
moments, auxiliary accounting, bootstrap, H construction, manuscript/import
closure, initial signs or all-degree Xi positivity is asserted.

No new mathematics, lemma or mathematical script was written. Mathlib full
matching coverage was not checked; no formal certificate is claimed. The
exact manuscript is the direct known claim, so no broader novelty search is
needed for this reproduction scope. There is no cross-notebook input.
A creative central-sign mechanism is still unprepared; this source audit
cannot supply an actual-Xi positivity bridge merely by verifying contours.
