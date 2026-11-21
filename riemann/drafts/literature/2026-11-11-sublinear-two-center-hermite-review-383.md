# Sublinear lower-node multiplicity — completed scope review, step384

TARGET: Test the two-center Hermite interpolant with m_n=min{n,ceil(2n/log n)} at t=n+1 and n+1-m_n at t=2(n+1) for an uncapped complete residual O(exp(-n/64)) on both spectral windows.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step384 reused reviews381/382 and searched unequal-multiplicity two-point Hermite, sublinear multiplicities, varying analytic functions and complex powers; inspected Lopez-Temme primary statements and relevant remainder/convergence proofs. No matching uniform complete-kernel rate was identified; queries and source limits are below, with no novelty claim.
SOURCE_EVIDENCE: Reuse inspected Calvi, Lectures on Multivariate Polynomial Interpolation (Hanoi2005), Thms1.9/1.17/1.18 pp14,20-21, https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf ; newly inspect Lopez-Temme math/0410436v1 Def2.1/Thms2.3/2.5 pp2-7 https://arxiv.org/pdf/math/0410436 and CWI MAS-R0211 Thm1 pp2-3 https://ir.cwi.nl/pub/4247/04247D.pdf ; C997c(1),(4)-(6), C997s kernel/step373.
COMPARISON: Calvi's exact finite-degree Hermite remainder covers arbitrary prescribed positive multiplicities, including this allocation separately at each n; it supplies no favorable uniform rate. Multipoint Taylor convergence holds fixed the function and base multiplicities. Neither that limit nor the inspected fixed-target approximation results pay this coupled growing-n complete residual. Prior balanced and capped-norm stops do not exclude it.
GAP: The specific interpolant's branch/contour geometry, degree-dependent remainder and both fully weighted windows remain unpaid. There is no matching imported rate, rigorous candidate-specific obstruction, coefficient-cap bound or Xi transfer.
REASON: Essential finite-degree tool coverage and duplicate/obstruction comparison now suffice for one bounded mathematical attempt on the unchanged exact target. This approves exploration, not the desired estimate; no new mathematics is derived in this literature turn and no essential source blocker remains.
SCOPE: Integers n>=3, I=[7/4,9/4], z_star=1+i/8, original fixed gamma grid; the two existing spectral nodes, with the stated sublinear first multiplicity and remaining second multiplicity. No coefficient-cap assertion and no all-polynomial obstruction.
LITERATURE_REASON: Step383 changed balanced multiplicities to the stated sublinear allocation outside review382's approved scope; compare unequal-multiplicity and growing-function hypotheses while reusing Calvi and the stronger-source assessments.

## Original step383 nomination, now assessed

The main gaps remain L030–L032/C032a actual-Xi positivity,
L966/L968 signed forcing and unpaid L984(H). The intended use of a
complete O(exp(-n/64)) residual is still the exact-band-null unit-TV
action bound, not the original capped E_n or actual-Xi reconstruction.

The nominated review task was to compare the changed allocation with known
two-point Hermite/multipoint approximation results for an n-dependent
complex power, reusing the already inspected Calvi formula. It should
identify whether this is an IMPORT, SPECIALIZE or EXPLORE case without
treating fixed-function root convergence as a uniform growing-n rate.
The changed multiplicities were the specific reason for the separate
review. Step384 below completes it without repeating the balanced
calculation. No essential source is blocked.

No rate for this allocation, or success of any contour, is asserted.
Under the completed EXPLORE assessment, one attempt must construct and bound this
specific interpolant on both full closed windows. The discrimination
remains a uniform complete residual C exp(-n/64) with all polynomial
factors paid, or a rigorous obstruction to this candidate. A merely
insufficient upper envelope is inconclusive and parks that attempt.

Essential established inputs are C997c(1),(4)–(6), C997s's exact kernel
and step373, and Calvi's cited finite-degree theorem. C997v motivates
the refinement; a future proof must check its own geometry and bounds
without assuming C997v's unaudited quantitative statements. C997r/t/u
remain contrasts and retain their stop evidence. No cross-notebook
input is proposed. Full Mathlib matching coverage remains unchecked.

The interpolant rate itself, any later coefficient cap, C997a(8),
selected/both-sign transfer, assay/reconstruction, complements/regulators,
L993, L984(H), L966/L968 forcing and Xi signs remain unresolved.

At nomination this was REVIEW_REQUIRED. The separate literature-only
step384 below establishes tool coverage before a later research turn.
Neither step384 nor the nomination rejects the completed step383.

## Completed comparison — 11 November 2026, step384

### Reused exact tool and its applicability boundary

The completed [parent review381](2026-11-11-two-window-uncapped-approximation-review-381.md)
records the full Calvi theorem hypotheses and the repeated-node proof
cases. Reuse that inspected evidence rather than retrieve unchanged
sources or reprove interpolation theory. Theorems1.9/1.17/1.18 require
holomorphy on a simply connected domain and a piecewise C1 contour of
index one around the interpolation nodes and evaluation point, avoiding
those points. Multiplicities count in the degree and node product;
equal multiplicities are not a hypothesis. A varying function or list
of multiplicities is allowed in a separate finite-degree identity,
without any uniform bound being supplied by the theorem.

Thus this changed allocation is within the exact tool's scope. It is
outside the prior balanced quantitative attempt. A future proof must
check its own positive integer multiplicities, degree count, distinct
spectral images, logarithm branch, enclosure and contour separation.
It must bound the entire n-dependent complex-power target on the
contour, including every n-dependent constant. No asymptotic bound for
the changed allocation is computed here. There is no reason to reprove
the cited remainder; the unpaid work is its quantitative specialization.

### Newly inspected multipoint comparisons

J. L. Lopez and N. M. Temme,
[*Multi-point Taylor Expansions of Analytic Functions*, math/0410436v1,
20 October2004](https://arxiv.org/pdf/math/0410436), Definition2.1,
Theorems2.3/2.5, printed pp2-7, equations(2.9)-(2.15),(2.27)-(2.31):
analytic f on open Omega, finitely many distinct centers in Omega with
positive integer base multiplicities; a positively oriented simple
contour in Omega encloses the centers and evaluation point. The exact
remainder uses the ratio of the multiplicity-counted node products to
power N. Convergence holds inside the stated strict lemniscate for
fixed f and fixed centers/base multiplicities as N grows. Inspected
the finite-geometric-sum proof, its fixed contour maximum of |f|, and
the confluence argument in Theorem2.5. That maximum does not give
uniformity for the proposed coupled sequence. This is corroborating
tool coverage, not an imported rate or a replacement for Calvi.

Their [CWI report MAS-R0211, 30 April2002](https://ir.cwi.nl/pub/4247/04247D.pdf),
*Two-point Taylor Expansions of Analytic Functions*, Theorem1, printed
pp2-3, equations(3)-(9), was also inspected with its complete proof.
It assumes analytic f on an open set and two distinct centers, with a
simple positive contour enclosing the centers and evaluation point.
Its remainder uses equal powers N at both centers; its Cassini-region
convergence bounds a fixed f on a contour. It therefore does not
assert the present unequal-allocation uniform estimate. No rate is
imported from it. The 2004 generalization addresses confluence.

Kitahara and Okuno, [*A Note on Two Point Taylor Expansion III*, IJMO4
(2014),287-291, DOI10.7763/IJMO.2014.V4.387](https://www.ijmo.org/papers/387-M2005.pdf),
Definition1 and Theorem2 pp287-288 were inspected as a search lead.
Its theorem concerns a fixed piecewise polynomial on the real line
with knot1/3, centers -1,1 and multiplicities 2ell,ell, with an
additional matching-value qualification at the knot. This does not
match the complex, degree-dependent analytic target or moving arcs.
Its proof was not inspected and no result is imported from it.

Reuse review381's inspected Sete-Liesen fixed-function Faber-Walsh,
Charpentier-Levenberg-Wielonsky approximation-pair, and fixed-weight
circular-arc comparisons. Changing multiplicities does not discharge
their mismatched uniformity/weight hypotheses. Their earlier unread
Pritsker-Varga lead remains nonessential; no retry or conclusion from
its search excerpt is needed. Full matching Mathlib coverage remains
unchecked; no Mathlib theorem is assumed.

### Search and local failure comparison

New queries were `"two point" Hermite interpolation "varying" analytic
function multiplicities remainder`, `"Hermite interpolation" "sublinear"
multiplicities complex power`, `"two-point" "Taylor" expansions analytic
"unequal" remainder complex`, `"multipoint" "Hermite interpolation"
"varying functions"`, `"Hermite interpolation" "multiplicities"
"asymptotic" "analytic"`, `Lopez Temme two point Taylor expansions analytic
remainder multipoint unequal multiplicities`, and `"Hermite interpolation"
"complex powers" approximation two points`. Search hits outside these
analytic interpolation questions were not used as theorem evidence.
The arXiv HTML endpoint returned406; the PDF text was accessible.
PDF screenshot requests were unsupported, so proof inspection used
the readable complete relevant text, not images or snippets.

Targeted local searches covered reviews381/382/383, the two-window and
balanced histories, the balanced ATTEMPTS entry and its working draft.
They contain no assessed or completed sublinear-allocation rate.
Read C997c through its spectral variation bounds and C997s's complete
kernel and step373 pairing/kernel audit. Reuse review381's comparison
of C997r/t/u rather than load their proofs again. C997r's simultaneous
coefficient-norm/defect obstruction is not a lower bound for this
uncapped residual. C997t concerns constant-coefficient differential
densities; C997u's normalized determinant rate is unpaid. C997v's
balanced upper-envelope failure is not a residual lower bound and
is motivation only. No quantitative premise from that unaudited
corollary is needed here. Existing stops remain intact.

### Approval and one-attempt boundary

DECISION EXPLORE approves exactly the TARGET line, with the original
gamma_j=15/8+j/(4n), 0<=j<=n, and spectral coordinate exp(it/(4n)).
The interpolation centers are the spectral images of the two stated
t values; derivatives are taken in that coordinate. No extra band
frequencies are allowed. Coefficients are unrestricted. The complete
residual is the C997s kernel difference, uniformly for c in [7/4,9/4].
Both closed spectral windows [n,n+2] and [7n/4,9(n+2)/4] must be
retained, along with both beta terms, every zero and K's subtraction.

Continue only on a rigorous complete bound C exp(-n/64), for one fixed
C and all integers beyond one onset, with polynomial factors paid;
a bare root rate at equality is insufficient. A rigorous obstruction
to this specific interpolant is informative and stops the recipe.
An insufficient upper envelope remains inconclusive and parks this
allocation after one attempt, pending materially new evidence or a
refined mechanism. No upper envelope is a residual lower bound.

No construction, new bound, lemma or mathematical script was produced
in this source review. The exact-band-null action use and independent
unpaid assumptions are those stated above. This completes the review
of an existing nomination; the next turn defaults to mathematics on
this same target, not another general literature approval.
