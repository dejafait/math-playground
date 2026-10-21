# Actual Wronskian witnesses — bounded source comparison

TARGET: Assess whether unconditional value/derivative moments can force noncommon zeros of the actual Wronskian F_0'G−F_0G' arbitrarily far out.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Wronskian/shift/common-zero and Hardy derivative-moment searches listed below; inspected primary Bui–Hall sign theorems and their sign-set deduction, Young's twist hypotheses/proof cases, and Dimitrov–Xu's determinant definition/theorem statements; reused ready scalar coverage and searched specific local Wronskian records.
SOURCE_EVIDENCE: Bui–Hall arXiv:2304.05178v1 (11 April 2023), Theorems 1–2 pp. 2–4, (3)–(4) pp. 5–6, Proposition 1/(6)–(8) p. 8 and Section 6 p. 16; Young Arch. Math. 95 (2010), 539–548, (2.1)–(2.3) p. 540, Lemmas 4–5 and complete Lemma 5 proof pp. 542–543; Dimitrov–Xu arXiv:1606.05011v1 (16 June 2016), Theorems 1.1/1.3 and determinant definition pp. 2–3; reused Arias de Reyna Theorem 6 and DLMF coverage in the saved October 5 assessments.
COMPARISON: Inspected unconditional sign-set results concern fixed Hardy derivatives, not G's right-line real projection or noncommon Wronskian zeros; Young's smooth rational twists are not response-selected microscopic windows; the Fourier Wronskians are single-function derivative determinants. No matching witness theorem was established.
GAP: Actual Wronskian moment information and localization excluding common-zero resets remain unproved; a first mixed-moment feasibility test is covered, but higher moments or a witness implication are not licensed by these comparisons.
REASON: Complete the changed witness target's essential theorem-scope comparison, then narrow to one source-covered actual first-moment test rather than importing a sign or reopening the parked sharp-discriminant source.
LITERATURE_REASON: The changed noncommon-Wronskian target was REVIEW_REQUIRED; prior scalar and discriminant assessments did not compare moment sign sets with exclusion of common-zero resets.
SCOPE: The actual F_0,G of L366, ordinary real derivatives, unbounded positive heights; no RH, F_0 simplicity, eventual noncoincidence, D≤0 or common-zero count bound.

## Gap, target and use

Global actual-theta mixed positivity and the total L367 signed margin
remain missing. The reviewed target is a zero of W=F_0'G−F_0G' where
F_0,G are not both zero, arbitrarily far out. L374/L378 use the opposite
Wronskian convention, with identical zero sets. Their finite-order
argument and L368's eventual strict response Laguerre positivity could
test eventual physical D≤0 for an independent actual pair. Independence
and witness applicability must be justified later. No application is
proved here. The bounded review found no direct import, but adequate
scalar coverage for one narrower first-moment feasibility test.

## Queries and primary theorem comparison

Queries actually submitted (snippets only located leads):

- Riemann xi Wronskian shifted xi critical line zeros derivative moments
- Hardy Z derivative moments Wronskian sign changes noncommon zeros
- zeta value derivative joint moments unconditional Ingham second moment Hardy Z prime
- "zeta" "Wronskian" "shift" zeros; "Hardy" "Wronskian" moments; "xi" "Wronskian" zeros Riemann noncommon
- "zeta" "Wronskian" "moment"; "zeta" "Wronskian" "5/2"; "Riemann" "Wronskian" "common zeros"
- "Hardy" "derivatives" "sign" "moments" noncommon

**Bui–Hall**, *On the derivatives of Hardy's function Z(t)*,
[arXiv:2304.05178v1](https://arxiv.org/pdf/2304.05178v1).
Theorem 1 gives measure at least (3/25+o(1))T for ZZ''<0 on
[T,2T]. Theorem 2 gives a positive proportion for the prescribed sign of
Z^(k)Z^(ell), for fixed orders of even sum according to their residues
modulo four. Neither contains G or this Wronskian. Read the complete
Cauchy–Schwarz sign-set deduction (3)–(4), Proposition 1, the derivative
expansion (6)–(8), and Section 6's deduction from the moments; the
auxiliary fourth-moment proof is not imported. Its mollifier is a fixed
polynomial-weighted Möbius sum. Proposition 1 permits length exponent
below 4/7; Theorem 1's deduction takes 1/8−epsilon. The proof controls
sign-set measure, not transitions relative to common zeros. It supplies
a method comparison, not an actual witness or an approved full moment
formula for W.

**Young**, *A short proof of Levinson's theorem*,
[Arch. Math. 95 (2010), 539–548](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Lemma 5 assumes opposite-height critical-line shifts O(1/log T),
positive integer twists h,k with hk≤T^(2theta), theta<1/2, and a smooth
weight: 0≤w≤1, support in [T/4,2T], derivative bounds
O_j((T/log T)^(-j)). Both functional-equation contributions and the
exact hm=kn diagonal are retained. Read the complete proof, including
both off-diagonal orderings and their logarithmic separation followed
by integration by parts. Re s=5/2 is not an allowed critical-line shift;
its factor needs separately justified truncation. A response-phase
window is not supplied by this slow weight. No full W moment,
automatic differentiated/windowed specialization or noncommon-zero
control is imported.

**Dimitrov–Xu**, *Wronskians of Fourier and Laplace transforms*,
[arXiv:1606.05011v1, pp. 2–3](https://arxiv.org/pdf/1606.05011v1).
Their W_n(f;x) is det(f^(i+j)(x)), i,j=0,...,n−1, formed from
successive derivatives of one transform. Theorem 1.3 assumes an
integrable kernel and its absolute (2n−2)-moment and represents this
determinant by a correlation transform. It does not represent
W(F_0,G). Theorem 1.1 is an RH-equivalent translate-density condition,
not an unconditional witness assertion. Statements and definition were
read for this mismatch; no proof or specialization is imported.

Unread leads remain unused: CUE joint-moment conjectures, Gonek–Ki pair
correlation and off-critical-line phase articles provide no inspected
input here. Previously blocked Das–Pujahari sharp-discriminant coverage
stays parked; it is unnecessary for the narrowed first-moment test.
No essential new source blocker remains. The search establishes neither
novelty nor impossibility.

## Reuse, duplicates and failures

Reuse the ready assessment
drafts/literature/2026-10-05-gaussian-linear-response-sign.md for
Arias de Reyna, *On the approximation of the zeta function by Dirichlet
polynomials*, [arXiv:2406.16667v1, Theorem 6, pp. 5–6](https://arxiv.org/pdf/2406.16667v1#page=5):
sigma≥0, 0<Im s≤x, fixed x>0. It bounds the scalar truncation with its
pole correction; Cauchy jet estimates need their applicability argument.
The ready assessment inspected its full proof and supporting cases.
Reuse drafts/literature/2026-10-05-gaussian-response-quadratic-sign.md
for DLMF 25.2.1/11 on Re s>1 and 5.11/5.15's sector-controlled gamma
jets, version 1.2.8 (2026-09-15), as recorded there. No refresh is needed.

Read L366 (1), L368 (3), (5)–(10), L369 (4)–(9), (12)–(18),
L374's finite-order/dependence cases, L378's local argument and L373's
complete common-zero example. L369's bounded-variation weighted mixed
mean (16), including all diagonal/off-diagonal cases, is a ready local
input. Cite it where applicable; do not reprove it as a new result.
Actual Wronskian algebra and verification of its moving weights remain
a later specialization, not a result of this review. Specific L370
pointwise calculation/assessment/history searches found no prior
actual Wronskian first-mean computation.

L373's W=−2sin^3(t) in its convention changes sign entirely at common
zeros, with simple zeros and strict response Laguerre positivity.
Both signs of actual W therefore still require localization.
The supplied overview preserves L375/L376's exact-shift geometric
failures, L377/L378's unresolved actual common count, and L379's failed
absolute response-grid enclosure; no extra proof audit or new use of
those results is asserted. Full matching Mathlib coverage is **not
checked**; standard supporting tools are not witness theorems.

## One covered continuation and stopping test

The narrower assessment is
drafts/literature/2026-10-08-actual-wronskian-first-mean.md.
Propose the actual dyadic mean normalized by A^2 T^2 L,
T=1+t, L=log(2+t), A from L366. Retain gamma carrier, polynomial b,
Euler-line jets, diagonal collisions, pole/truncation errors and weight
variation. No moment value is asserted here. A controlled first mean
could test a signed-mean mechanism and supply one input to a later local
sign test; square/absolute moments and common-free localization remain
independent gaps.

Continue only if the complete leading term and error give usable sign
or quantitative cancellation information. Stop this certificate if the
error obscures the statistic or it yields only transitions allowed by
L373. A later higher-moment, phase-window or witness implication needs
its own assessed exact target. Global positivity, total margin, low
indices, heights above forty and endpoint margin remain unresolved.
This review is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION: no new
lemma, mathematical script, RH candidate or progress beyond the inspected
sources. Newly written ready continuation coverage awaits separate
supervisor approval next turn.
