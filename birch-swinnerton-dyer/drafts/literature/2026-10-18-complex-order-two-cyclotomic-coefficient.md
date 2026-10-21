# Complex order two to a cyclotomic quadratic coefficient — source comparison

TARGET: Assess whether known complex-to-cyclotomic leading-term comparisons imply a nonzero primitive ordinary quadratic coefficient from analytic order two under L026's other hypotheses, without assuming rational rank, finite primary Sha or a nondegenerate rational height regulator.
CHECKED: 2026-10-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the two saved coefficient/corank and analytic-order/Kurihara assessments, the 2026-10-03 cyclotomic-derivative assessment and foundations/04; five targeted discovery queries located the primary statements compared below. No adequate proved implication was found in this bounded comparison; no absence or originality claim follows.
SOURCE_EVIDENCE: Freshly inspected Stein--Wuthrich (2013), Theorems 6.1/7.3/7.5; Disegni's author PDF, Hypothesis BSD-infinity, Conjecture BSD-p, Remark 1.1.3, Theorem 3.2.1 and its good-reduction proof; BKS arXiv:1910.07404v2 (2020-04-17), Hypothesis 2.2, Conjectures 1.5/4.9, Proposition 4.15, Theorem 6.2(i), Corollaries 6.6/6.7 and their good-reduction proof, Theorem 7.3/Corollary 7.4; BDV author-final PDF, Theorem A and Sections 1.2--1.3. Published BKS numbering is reused only with the earlier assessment's qualifications.
COMPARISON: The higher-rank complex-to-p-adic formula is conditional on generalized Perrin--Riou and retains rational-rank/finite-primary-Sha inputs; its regulator factor is not certified nonzero. Proved low-rank comparisons exclude complex order two. Algebraic characteristic leading terms and main-conjecture equality do not identify their order with the complex order. L026 still assumes the desired coefficient.
GAP: No inspected theorem supplies a_2!=0 on the exact retained hypotheses; the missing comparison, rational-rank index and regulator nonvanishing cannot be inserted as consequences of complex order two. The direct-import mechanism is parked, rather than reported false or source-blocked.
REASON: The changed target received a completed theorem-level negative import test. No new lemma, counterexample, reproof or workaround is established; return to an independent, already assessed finite-certificate audit.
LITERATURE_REASON: Changed hypothesis: replace L026's independently certified nonzero quadratic coefficient with exact complex analytic order two, retaining its other hypotheses; existing ready coverage assumes the coefficient instead of producing it.
SCOPE: Non-CM E/Q at p>=5 with all of L026's arithmetic and residual-family hypotheses unchanged, except that its coefficient premise is the sought conclusion. Use its primitive ordinary series, trivial branch and total minimal real period. Grant complex order exactly two; do not grant rational rank two, finite primary Sha, nondegenerate rational height or a p-adic BSD conjecture.

## Target, use and discriminating test

The main gap is rational rank equal to complex order for arbitrary E/Q
of order at least two. The intermediate threshold is a rigorously nonzero
quadratic coefficient in L026's exact primitive series. Its downstream use
would be L026's corank-two squeeze and then the conditional actual-pair
route. Rational Kummer membership, finite-quotient production and higher
orders remain independent. No hypothesis asserting rational rank, finite
primary Sha, height nondegeneracy or p-adic BSD is permitted here.

The test was a proved implication meeting that threshold, with a finite
applicability check. The inspected sources fail this import test for the
specific reasons below. EXPLORE records a bounded search without an
adequate match; it does not approve an uncovered proof of the implication.
Reopening this mechanism requires a specific new theorem or independently
testable comparison. No new mathematics is derived in this review.

## Local reuse and duplicate checks

Read complete L026 and the two named saved assessments before discovery.
L026 imports Kim's infinitude/parity results and Kato's upper-bound
direction, but assumes a_2!=0. L027's certification interface and L033's
fixed instance are already described in the supplied complete overview;
their detailed finite proofs were unnecessary for this theorem comparison.
Neither is a uniform coefficient-production theorem. L002/L004's directions
are reused through the ready 2026-10-06 assessment, without re-auditing
control or parity. L082 is a known-rank fixed-case contrast only.

The 2026-10-05 review concerns a minimal two-prime residual index, not
the present coefficient. The 2026-10-03 cyclotomic-derivative review already
separates a cohomological regulator from a rational exterior square; its
BKS version/access distinctions and later-source comparisons are reused.
ATTEMPTS/031 and /034 were read: generic semisimplicity and a conditional
full-descent interface supply neither the missing comparison nor its
arithmetic inputs. This review does not reopen those mechanisms, repeat
L033, or schedule the completed L035/L082 audits again.

## Primary comparisons

**Algebraic leading terms.** William Stein and Christian Wuthrich,
*Algorithms for the arithmetic of elliptic curves using Iwasawa theory*,
Math. Comp. 82 (2013), 1757--1792,
[Theorem 6.1, p.1776](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=20),
states that the characteristic order is at least rational rank, with
equality exactly when the cyclotomic height is nondegenerate and primary
Sha is finite. Its leading-term valuation is then arithmetic. It is a
theorem about f_X, not a complex-to-cyclotomic comparison. The retained
ordinary/non-CM scope matches the already checked foundations/04.
[Theorems 7.3/7.5, p.1778](https://wstein.org/papers/mcom2649-iwasawa-alg.pdf#page=22)
give Kato divisibility and, under an extra ramified multiplicative prime,
main-conjecture equality. Even equality compares L_p with f_X; neither
statement substitutes complex order for rational rank or supplies the
missing nondegeneracy. The stronger equality is therefore not silently
imported on L026's hypotheses. No reproof is needed.

**Proved complex comparisons in low rank.** Daniel Disegni,
*On the p-adic Birch and Swinnerton-Dyer conjecture for elliptic curves
over number fields*, Kyoto J. Math. 60 (2020), 473--510; inspected
[author PDF, Sections 1.1--1.2 and 3.2](https://disegni-daniel.perso.math.cnrs.fr/exc.pdf#page=4).
This 26-page author text has no version stamp identified here; its page
numbers differ from the journal and the arXiv record's 2016 v1.
Theorem 3.2.1 (author pp.12--13) assumes analytic order at most one;
its good-reduction proof uses Gross--Zagier and a nonvanishing twist.
The quadratic exceptional-zero formulas concern split multiplicative
reduction and analytic rank one, outside our good-ordinary target.
The general Conjecture BSD-p assumes BSD-infinity parts 1--2, including
rank equality and rationality of the complex regulator quotient.
Remark 1.1.3 explicitly retains regulator nonvanishing for exact order.
Thus neither its proved theorem nor its conjectural general formula
passes the present test. The good-reduction proof case was inspected,
not extended to rank two.

**Higher-rank bridge.** Burns--Kurihara--Sano,
*On derivatives of Kato's Euler system for elliptic curves*,
[arXiv:1910.07404v2, 17 April 2020](https://arxiv.org/pdf/1910.07404v2),
Hypothesis 2.2 (p.12) assumes positive rational rank and finite primary
Sha. Conjecture 1.5 (p.6) explicitly assumes rank equality;
Conjecture 4.9/Proposition 4.15 (pp.26--27) supply the conjectural
complex leading-element identification. The proved Theorem 6.2(i)
(p.39) pairs its derived class with rational points; it does not prove
that identification. Corollary 6.7 (p.41), conditional on Conjecture 4.9,
has good-reduction formula
\[
(1-\alpha^{-1})^{-1}(1-\beta^{-1})L_{S,p}^{(r)}
=\frac{L_S^*(E,1)}{\Omega_\xi R_\infty}R_p.
\]
Here r is rational rank; R_p is the cyclotomic height regulator.
The good-reduction proofs of Corollaries 6.6--6.7 (pp.40--41) use
Theorem 6.2 and the regulator comparison. The right side is not
certified nonzero without R_p!=0. Theorem 7.3/Corollary 7.4 (p.51)
retain Hypothesis 2.2 even for their main-conjecture consequence.
These are precise obstructions, not a matching import. No removal of
S-truncation, period change or coefficient specialization is asserted.

**Classical Perrin--Riou is not the higher-rank conjecture.** Bertolini,
Darmon and Venerucci, *Heegner points and Beilinson--Kato elements:
a conjecture of Perrin-Riou*,
[author-final PDF, Theorem A, p.2 and Sections 1.2--1.3, pp.5--7](https://www.esaga.uni-due.de/f/massimo.bertolini/publications/BDV-Final.pdf#page=2),
has no version date identified in this read. It assumes semistability
at an odd p and central vanishing. Its point has infinite order exactly
for a simple complex zero; its logarithm-square formula concerns the
bottom-layer local Kato class. The outlined Heegner-point/Beilinson--Flach
comparison does not assert quadratic cyclotomic nonvanishing in complex
order two. It cannot be used as a proof of BKS Conjecture 4.9 in rank two.
No proof of the full BDV theorem was needed for this scope exclusion.

## Search/access record and limits

Discovery queries, 2026-10-18:

- `elliptic curve analytic rank two cyclotomic p-adic L-function second derivative nonvanishing theorem`
- `Bertolini Darmon Venerucci rank two p-adic Birch Swinnerton Dyer theorem cyclotomic leading term`
- `"cyclotomic" "analytic rank two" "nonvanishing"`
- `"p-adic" "leading term" "analytic rank" "two" BSD cyclotomic theorem`
- `Burns Kurihara Sano generalized Perrin Riou conjecture cyclotomic leading term elliptic curves rank two theorem`

Search hits are locators only. The Banwait CM/rational-rank-two lead
was already compared in the 2026-10-03 assessment and is reused with its
stated preprint qualifications. Anticyclotomic/BDP and Garrett-function
hits concern different functions; no conclusion from them is imported.
Recent low-Selmer-corank and claimed complete-proof hits were not read
or used as inputs. Two unrelated arXiv locator guesses were discarded.
None is represented as theorem-level coverage or a proof of absence.

The published BKS author mirror, King's mirror and J-STAGE PDF endpoint
were inaccessible through the browser. The accessible v2 supplied the
essential hypotheses, good-reduction cases and proofs above. Do not
transfer its numbering to the 2024 journal article: the saved review
records journal Conjecture 1.6 and Corollary 1.11 with different numbering.
This is not a persistent essential-source blocker or an exhaustive survey.
No essential unread source is needed to establish these scope mismatches.

## Decision and continuation boundary

The test yields a negative direct-import decision: the inspected
comparisons require an excluded premise or cover different rank/reduction
or L-function scope. This adds source-level evidence to the changed
coefficient-production question; it proves no new rank bound, coefficient
vanishing or nonexistence theorem. L026 remains conditional and the main
gap is unchanged. PROOF.md and DAG.md need no mathematical change.

Park this mechanism. The independent ready continuation is the separate
L081 critical audit under the unchanged
[local-seven audit assessment](2026-10-18-known-point-local-seven-critical-audit.md).
It checks newly produced exact local evidence, rather than asking another
conditional interface or source review to produce global arithmetic.
Its use toward L062 still requires all L026 premises and an independently
supplied finite-quotient exponent; local nondivisibility alone supplies
neither strict rationality nor arbitrary-curve rank equality.

Mathlib: full matching theorem and supporting coverage not checked.
No absence or formalization claim is made. Literature-only work creates
no lemma or mathematical script; the existing proof and unfinished
order/descent artifacts are preserved.
