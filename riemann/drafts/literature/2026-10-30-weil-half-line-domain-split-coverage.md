# Retained half-line domain split — primary coverage

TARGET: Assess the interval-to-half-line form and operator domain split for G=(1/2)log(1-D_x^2), including Carleman's cross-kernel bound and smooth approximation across the interface.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Carleman kernel norm, logarithmic-Laplacian smooth-core density and Kato representation/perturbation; inspected primary statements and relevant density/closure proof cases. Scoped L512/L513 and Weil ATTEMPTS screening found the split retained, with no completed local audit.
SOURCE_EVIDENCE: Paper 67 v1 Section 3.1 after (3.6); Yafaev arXiv:1210.5709v2 (1.2)–(1.4), Section 2.1 (2.1)–(2.3); Chen–Weth arXiv:1710.03416v6 (2.9), Section 3 definitions and Theorem 3.1 with full cutoff/mollification proof; Kato, reprint of 1980 edition, VI.1.33 pp. 320–321 and VI.2.1 p. 322, including form-norm equivalence and core-testing proof pp. 324–325.
COMPARISON: The manuscript already asserts the bounded-interval split; known inputs cover the cross estimate, bounded-interval density and representation. The half-line core/closure application still needs an explicit specialization. Carleman alone does not identify form domains; Chen–Weth does not assert density on arbitrary unbounded domains.
GAP: Audit normalization and L2 bound, both form-domain inclusions through compact half-line tests and bounded interval density, then product operator domain and full exterior forcing by Kato. These application steps are not proved in this literature turn.
REASON: Essential primary coverage is available for a separate reproduction/specialization of the analytic input deliberately retained by L513/L512. No new domain theorem, arithmetic positivity or novelty is claimed.
LITERATURE_REASON: The target changed from signed trace inversion to the explicitly excluded domain split; its previously missing primary closure and representation coverage is the reason for this source turn.
SCOPE: Fixed ell>0, I=(0,ell), J=(ell,infinity), Psi(xi)=(1/2)log(1+xi^2), n(t)=exp(-|t|)/(2|t|), and zero-extension smooth-core part forms. Pure reference operator only; the split is sought for complex L2 data without boundedness of u or G_I u.
COVERED_TARGET: Audit the fixed-ell form-domain split Q_+=Q_I direct-sum Q_J plus its bounded cross form and the resulting product operator domain, including L513's full exterior forcing.

## Exact known inputs

[Yafaev, *Spectral and scattering theory for perturbations of the
Carleman operator*, arXiv:1210.5709v2, 31 October 2012](https://arxiv.org/html/1210.5709v2),
(1.2)–(1.4) and Section 2.1, diagonalizes the kernel (s+t)^(-1)
on L2(R_+) by the unitary Mellin transform, with multiplier
pi/cosh(pi k), hence norm pi. Import this classical result, rather
than reprove it. The pending application must check reflection,
restriction, zero extension and the factor 1/2. No sharpness claim
for the damped, restricted kernel is needed. This is not the
unrelated exponential-product Carleman inequality.

[Chen–Weth, *The Dirichlet Problem for the Logarithmic Laplacian*,
arXiv:1710.03416v6](https://arxiv.org/html/1710.03416v6),
Theorem 3.1, gives smooth-core density in H(Omega) for **bounded
Lipschitz** Omega. Its energy uses zero exterior values and
k(z)=c_N 1_(|z|<1)|z|^(-N), not just regional differences; see
(2.9), (3.1)–(3.5). The full proof was read: boundary cutoffs
using the killing weight (3.7), followed by interior mollification.
Real positive/negative parts are explicit; use real/imaginary parts
for complex data. Import the theorem with these hypotheses.

[Kato, *Perturbation Theory for Linear Operators*, corrected second
edition, reprint of the 1980 edition](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/kato1.pdf),
VI.1.33, pp. 320–321, treats relative form bound less than one,
including an L2-bounded perturbation (relative bound zero).
VI.2.1, p. 322, applies to densely defined closed sectorial forms;
part (iii) identifies operator membership from an H-valued
functional tested on a form core. Its proof pp. 324–325 extends
core testing by continuity and uses the adjoint operator. The
form-norm equivalence proof of VI.1.33 was also inspected. Common
form domains must be established before applying representation;
form boundedness alone is not operator boundedness.

[bramble_trace, *Boundary traces and support variation for localized
Weil operators*, paper 67 v1, 27 October 2026](https://rstation.ai/problems/riemann_hypothesis/papers/67),
Section 3.1's two paragraphs after (3.6), already asserts the
bounded-interval split: Carleman cross bound, restrictions of smooth
tests, split-norm convergence, and approximation of jumps. This
compressed source argument is the object to specialize/audit, not
an independently verified local input. Its Section 3.3 uses the
half-line extension retained in L513.

## Covered specialization and decisive test

The proposed audit must compare n with k/2 in N=1 in the form norm
with an added L2 norm. This is a kernel comparison and standard
Young-inequality application to be written next, not an identity of
Fourier symbols. The singularity of log|xi| at zero must not be
attributed to the positive reference multiplier.

For the half-line use its stipulated smooth-core closure. Apply
Chen–Weth only to bounded intervals containing each compactly
supported restricted test: I on the left and (ell,R) on the right.
First verify finite energy of those restrictions, then invoke
bounded-interval density. This is the proposed way to handle the
interface without asserting an unbounded-domain density theorem.
The next audit must justify this application, both closure inclusions
and the bounded cross-form identity. No H^s restriction theorem
needs to be reproved if this finite-energy method works.

Finally use the actual bounded off-diagonal L2 operator, not merely
a form-relative bound, in Kato's representation characterization.
The conclusion sought is the full product operator domain and the
piecewise exterior forcing in L513 (2). No pointwise singular
integral on a rough domain element may replace the core argument.
This is the remaining elementary application work approved in
scope, not a split proof derived in this literature turn.

Continue only if both form-domain inclusions and the exact operator
domain pass with the cited hypotheses; otherwise retain the first
failed implication and L513's split assumption. No numerical test
is appropriate. L513 and L512 motivate the application; they do
not prove it. Their eigenfunction boundedness, collars, varying
operators, near-zero uniformity and arithmetic positivity remain
independent. No cross-notebook input. Full Mathlib coverage is
unchecked; no absence claim is made.

## Search record and route

Queries: “Carleman operator integral kernel 1/(s+t) norm pi bounded
L2 theorem”; “Carleman operator spectrum [0 pi] Yafaev kernel t+s
arxiv”; “logarithmic Laplacian form domain density Cc infinity
Lipschitz domain Chen Weth theorem”; “Kato first representation
theorem VI 2.1 bounded perturbation forms operator domain”. Search
snippets and unrelated Carleman-kernel results were not used as
primary evidence. The browser could not render the rStation
markdown download and shell DNS was unavailable; canonical HTML
and the primary theorem texts were readable. No essential source
blocker or essential unread lead remains for the covered audit.

The original REVIEW_REQUIRED nomination is superseded only as
source coverage. A separate mathematical step must check the
specialization; the changed ready continuation receives separate
next-turn approval. No lemmas or mathematical scripts were changed.
The automatic-support, tail-dropping and rank-trace stops remain
at their stated scope. This standard analytic input supplies no
new arithmetic cancellation at a first null mode and thus no
justified creative central-gap mechanism.
