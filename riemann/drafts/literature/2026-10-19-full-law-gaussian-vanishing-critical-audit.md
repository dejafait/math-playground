# Coverage proposal: critical audit of the full-law Gaussian vanishing result

TARGET: Critically audit L439's vanishing Gaussian occupation statistic for the unchanged complete L438 law, including actual-height Poisson concentration and all component bounds.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 254 read L439 in full, compared L429's original cutoff, L438 (9)--(16), L424 (6), the step-252 exact-target discovery and step-204/209/250 source comparisons, and the recorded fixed-mixture and moving-test failures; no matching completed audit was identified in these scoped records and no novelty inference is made.
SOURCE_EVIDENCE: Reuse Aistleitner--Berkes--Seip, JEMS 17 (2015), DOI 10.4171/JEMS/537, section 3, p. 1527, identity preceding Lemma 1/(23), and arXiv:1210.0741v5 pp. 10--11 with the iterated-circle proof inspected at step 252; Euler reciprocal-prime divergence through Rusin's 328K Spring 2017 zeta note, unnamed theorem and proof pp. 1--2, inspected at step 204. Local audited interfaces are L424 (6), L429 (10), and L438 (9)--(16). No fresh primary retrieval is claimed.
COMPARISON: Finite Poisson identities and Euler divergence remain inside inspected coverage; neither establishes L439's moving-height concentration or complete-law estimate. Those explicit finite-H specializations require independent proof audit, without moving-test Haar convergence, independence, infinite-product singularity or uniform integrability of P_j.
GAP: Audit L439 (2)--(13), complete log tails and sum/difference frequencies, all-real-H cutoff and two-limit Holder passage, every rare component, full covariance and translated atoms at all basis ties; correctness and any finer rate remain uncertified by this source comparison.
REASON: Essential coverage is adequate for one separate RESEARCH proof_audit of exactly TARGET under SPECIALIZE; this literature-only comparison approves scope and neither verifies L439 nor rejects step 253's completed negative result.
LITERATURE_REASON: The newly written L439 critical audit extends the earlier attempt assessment to a specific concentration proof and complete component comparison; this separate approval reuses ready primary readings rather than repeating discovery.
SCOPE: Exactly L439's stated o(1) conclusion for the fixed Q and unchanged L438 family; no stronger rate, new observable, cutoff adjustment or realization assertion.

## Proposed audit and reuse

Essential inputs are L424 (fixed Q, global bound, trajectory benchmark),
L428 (only its imported Euler divergence), L429 (finite product, original
cutoff and E_H P_j=1+o(1)), and L438 (all rare second bounds, N_H->1,
bounded translation, full covariance and actual Borel unit vectors).
The prior assessment is
`drafts/literature/2026-10-19-full-three-prime-law-occupation-defect.md`.
Reuse that source coverage where its hypotheses match; additional
literature requires a specific changed hypothesis or essential unread
source, not repetition of its search queries.

The mathematical review must check (2)'s finite positive expansion,
(3)'s complete logarithmic tail, distinct prime powers and all sum and
difference frequencies in (7), the all-real-H cutoff estimate,
Euler/Chebyshev passage to changing height probability spaces, and the
two-limit Holder argument. For the complete law verify the linear
Gaussian envelope, both signed intermediate states, high states with
small first two coordinates, full A_H, translation and every basis tie.
None of this needs an independence or basis-continuity premise.

Pass only if the exact unchanged family satisfies the absolute o(1)
claim; otherwise identify and repair the concrete failure within scope.
Do not turn vanishing into a realization result or a rate comparison
with O(1/(H log H)). Actual/global realization, clipping, capped
nondegeneracy, L413's full-error regulator margin and mixed positivity
remain unresolved. Full matching Mathlib coverage remains unchecked.

## Completed source-scope comparison — step 254

This is a LITERATURE / NOVELTY_UNCHECKED / literature_comparison step
with outcome EXPLORATION. The proposal above now has adequate coverage
for a later mathematical audit; no audit conclusion is asserted.

The reused primary readings are documented in the step-252 assessment
`2026-10-19-full-three-prime-law-occupation-defect.md`, the step-209
assessment `2026-10-18-growing-prime-poisson-covariance.md`, and the
step-204 assessment `2026-10-17-finite-prime-covariance-domination.md`.
These record actual theorem/proof readings, rather than snippets or
unread leads. No new external query is necessary for unchanged inputs.

Aistleitner--Berkes--Seip's
[published finite kernel identity and Lemma 1/(23), p. 1527](https://ems.press/content/serial-article-files/32047?nt=1)
apply to a finite number of coordinates with radii strictly between
zero and one. Every finite prime head with radii p^(-1/2) is in that
scope. The iterated-circle proof was inspected in the
[2013-11-11 v5 manuscript, pp. 10--11](https://real.mtak.hu/33507/1/berkes.pdf).
The identity concerns Haar character integrals and polynomial squares;
it is not an actual-height theorem for a changing nonlinear test.
L429 (10), rather than this source alone, supplies the saved sharp-height
mean and cutoff. Import the finite identity without reproof. Auditing
L439's direct logarithmic truncation is justified because that changed
finite-H estimate is not supplied by the identity.

Euler's named divergence theorem is imported, not reproved. The inspected
[Rusin note, unnamed theorem and complete proof, pp. 1--2](https://web.ma.utexas.edu/users/rusin/328K-17a/zeta.pdf)
uses finite Euler products, unique factorization and harmonic divergence,
with no quantitative prime distribution or RH assumption. L439 requests
only divergence along j(H) tending to infinity. No rate is imported.
Chebyshev and Holder are standard named inequalities; the audit must
check their finite-H application and order of limits rather than infer
uniform integrability or a theorem on one common probability space.

Scope comparison used all of L439, L429's cutoff paragraph, L438
(9)--(16), and L424's global quadratic estimate (6). The latter local
interfaces supply the fixed Q, bounded translation, full matrix
correction and complete high/intermediate second integrals. No new
Schur--Horn application or continuity of the selected basis is requested:
L439 proposes a unit-vector norm estimate valid for every branch. Its
validity, including the new linear Gaussian envelope, remains an audit
obligation. There is no reason to reprove the occupation identity or
the source moment theorems to test these estimates.

The prior duplicate/failure comparison remains applicable: L425/L426
and C426a--C426c concern a fixed covariance mixture, while L438 uses
the unchanged growing Poisson covariance. The optional Kakutani lead
was unread/inaccessible at step 252 and is not an input; no essential
source blocker remains for this finite-H audit. The recorded stop in
`ATTEMPTS/2026-10-19-full-poisson-law-gaussian-occupation.md` is L439's
pending conclusion, not independent verification. No inspected source
directly supplies the full L439 result, and search failure is not a
novelty claim.

Continue if every stated estimate establishes exactly the absolute
o(1) conclusion for the saved family and cutoff. Otherwise isolate the
failed bound and repair within scope or retain a qualified failure.
Even a passed audit would justify only retiring the nonzero-limsup
diagnostic; comparison with the smaller trajectory budget and all
realization, clipping, regulator and RH gaps remain open. Full matching
Mathlib coverage is unchecked. No lemma, mathematical script, DAG or
PROOF.md is changed by this source comparison.
