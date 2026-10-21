# Source coverage: critical audit of both repaired-law residuals

TARGET: Critically audit L442's two complete repaired-law quadratic residuals, including the quantitative centrally even sine estimate and all raw second contributions under the original cutoff.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 266 reused the ready calculation and L440/L441 audit assessments; searched the exact local quantitative-sine, Fejer, raw-second and failure interfaces; externally searched Fejer Lipschitz approximation rates and binomial/Euler-product hypotheses. Newly inspected Lorch's primary alpha=1 result and Huang's finite-product statements; no source located independently certifies these law-specific residuals, and no novelty inference is made.
SOURCE_EVIDENCE: Lorch, Canadian Mathematical Bulletin 5 (1962), 21--27, (1)--(5), pp. 21--22, and the complete alpha=1 proof on p. 23; Huang, 17 March 2016 author manuscript, finite kernel and Propositions 2.2--2.3, pp. 4--5, including product proof; NIST DLMF version 1.2.8, equations 4.6.1, 4.6.7 with its |z|<1 qualification, and 25.2.11 with Re(s)>1; reuse the inspected occupation, finite-Poisson and absolutely-continuous calculus statements in the step-264 and step-258 assessments.
COMPARISON: Known results cover C^1 necessary occupation identities, finite Poisson moments, Lipschitz calculus, the one-circle Fejer Lipschitz rate and the binomial/Euler-product starting formulas. They do not establish L442's complete H-dependent signed estimate, collision cancellation, angular coefficients or full raw-second assembly; these remain explicit audit obligations under the original cutoff.
GAP: Independently check all of L442, especially (9)--(12) at o((log H)^(-1/2)), the nonzero intermediate angular means, ties, fractional branch/tail, translation, full covariance and the final scale-one residuals. Adequate source scope is established here; none of those mathematical checks is completed in this literature turn.
REASON: Essential coverage is adequate for one later REPRODUCTION critical proof audit of exactly TARGET. The changed quantitative input has known approximation and series foundations; only its law-specific specialization requires checking, with no new law, test, cutoff or realization claim authorized.
LITERATURE_REASON: The saved new audit target was REVIEW_REQUIRED; prior approval covered the calculation, while its new quantitative sine estimate and nonzero angular means required a separate source-scope comparison. This turn completes that comparison and preserves the calculation outcome.
SCOPE: Exactly L442 in full for L441's unchanged complete Borel law, L440's eta and fixed omega=log 2, ordinary C^2 trajectories, and every real H on the original eventual cutoff ray; no actual critical-function sine theorem or growing-character assertion.

## Relevance and decision test

Global mixed positivity remains the main gap. The intermediate target
is a critical audit of the two claimed residuals, o(1) for xy and
log(2)/(360 sqrt(2))+o(1) for y^2. Its plausible downstream use is a
verified additional necessary constraint separating this representative
from trajectory occupation laws. It cannot establish failure of every
supported law, a clipped statistic, or an RH sign.

Continue the separation only if the full signed error is o(1) on the
unchanged real-H ray. In particular the sine estimate used with the
sqrt(log H) intermediate budget must meet its stated smaller threshold.
If an essential bound or leading cancellation fails, qualify the
conclusion and name the precise unresolved term; do not change the law,
test or cutoff to rescue it. This is source approval, not proof approval.

## Primary coverage and remaining specialization

Reuse `drafts/literature/2026-10-20-repaired-law-remaining-quadratic-occupation.md`
for Lasserre--Henrion--Prieur--Trelat, *Nonlinear optimal control via
occupation measures and LMI-relaxations*, SIAM J. Control Optim. 47
(2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5. Its necessary
C^1 identity admits the two fixed-H compact-box tests, with state (x,y)
and control z and vanishing endpoint tests. It requires neither atom
continuity nor a third derivative of f. It proves no law realization.
No new occupation theorem or reproof is needed.

The same ready assessment covers Aistleitner--Berkes--Seip, *GCD sums
from Poisson integrals and systems of dilated functions*, JEMS 17
(2015), 1517--1546, DOI 10.4171/JEMS/537,
[Section 3, p. 1527, identity before Lemma 1 and (23)](https://ems.press/content/serial-article-files/32047?nt=1).
The imported statement concerns finitely many radii below one. L440's
separately audited moving-height estimate, rather than this Haar
identity alone, is the relevant local input under L429's cutoff.

Newly inspected Lee Lorch, *On Approximation by Fejer Means to Periodic
Functions Satisfying a Lipschitz Condition*, Canadian Mathematical
Bulletin 5 (1962), 21--27, DOI 10.4153/CMB-1962-004-3,
[published primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3882561682569E0A63092BDD44372FC0/S000843950005102Xa.pdf/div-class-title-on-approximation-by-fejer-means-to-periodic-functions-satisfying-a-lipschitz-condition-div.pdf),
(1)--(5), pp. 21--22, gives the worst-case periodic Lipschitz
Fejer error of order log(n)/n and a sharper expansion. Read the
complete alpha=1 proof, p. 23; the alpha<1 case is unnecessary.
Nikolski's 1940 paper and Sz.-Nagy's treatment are cited there but
were not independently inspected. The standard rate is known, not a
new L442 result. Uniform normalization of the H-dependent Lipschitz
class, tensor convolution and finite Fourier mass remain audit checks.
The local elementary estimate can check those conventions and the
explicit moving truncation; reproving the general asymptotic is needless.

Rechecked Huichi Huang, *A generalized Fejer's theorem for locally
compact groups*, 17 March 2016 author manuscript,
[finite kernel and Propositions 2.2--2.3, pp. 4--5](https://huichihuang.wordpress.com/wp-content/uploads/2016/03/fejergr3.pdf),
including its full product proof. The one-circle kernel has finite
triangular Fourier coefficients, is nonnegative and has normalized
mass one; the d-dimensional kernel is its product. Rescale R/Z to
the 2pi circle, as in L436. These statements cover the finite kernels
used in L442; qualitative approximate-identity convergence alone
does not supply its moving error. Check its three-coordinate rate
and preservation of central symmetry in the later audit.

NIST DLMF, version 1.2.8 (2026-09-15),
[4.6.7 and its qualification](https://dlmf.nist.gov/4.6#E7), gives
the binomial expansion for arbitrary fixed real or complex exponent
and |z|<1. [4.6.1](https://dlmf.nist.gov/4.6#E1) specifies the
principal local logarithm. These support the real exponents 1 and
3/2 used locally. [25.2.11](https://dlmf.nist.gov/25.2#E11)
states the Euler product only for Re(s)>1. The audit must check the
Euler-log branch, real Dirichlet coefficients, absolute coefficient
majorant on Re(s)=3/2 and uniform truncation on Re(s)=5/2 in L442
(11)--(12). Those complete claims are not a matching DLMF theorem;
their elementary specialization is justified by the needed branch
and tail controls. No Euler product on the critical line is licensed.

Reuse `drafts/literature/2026-10-19-prime-two-quadratic-occupation-audit.md`
for Tao's *An Introduction to Measure Theory*, author preliminary
text, Theorem 1.6.40, pp. 172--174, Exercises 1.6.44--45 and
1.6.48(iii),(vi)--(vii). Its inspected absolutely-continuous calculus
supports L440's angular integration through finitely many jumps.
It does not evaluate nonzero angular means. Reusing L440 requires
checking the new amplitudes' uniform bounds and all tie contributions.

## Local audit scope, duplicate and failure comparison

Read L442 in full, L440's weighted-Poisson and angular interfaces,
L441's unchanged components and exact perturbation, L438's F_H and
complete raw matrix, L435's central symmetry and rational smoothness,
and L436's kernel interface. L419's exact K/forms and L424's ordinary
dynamics remain essential inputs for the audit, not independent
assumptions to be replaced by generic geometry.

The new proof obligations are precisely L442's finite-frequency
collision cancellation using central rather than coordinatewise
symmetry, uniform Lipschitz bounds for both signed parts, fractional
series and auxiliary truncations, signed intermediate means, slow
derivatives, translation, high states, constant covariance and every
zero matrix entry. Retain all raw seconds until their stated signed
bounds apply. Hold H and the law's parameters fixed when differentiating.
The auxiliary Fourier cutoff must not modify L429's Poisson cutoff.

The scoped histories for steps 259 and 263 validate the earlier
separation and x-squared repair only. Step 265 records the new
calculation, not its critical audit. L440's zero-angular-mean cross
entry argument cannot by itself justify L442's other entries;
qualitative Haar convergence cannot replace the claimed quantitative
sine estimate. No duplicate completed audit was found in these records.
`ATTEMPTS/2026-10-19-full-poisson-law-gaussian-occupation.md` parks
the fixed Gaussian nonzero-limsup diagnostic, not these polynomial
identities. L428's uniform-bulk-bound obstruction and all narrower
selected-law stops keep their original scope. No historical stop is
removed or treated as a global prohibition.

External queries included `Fejer kernel Lipschitz approximation log n n
lecture notes pdf`, `DLMF binomial theorem complex power Euler product
zeta log absolute convergence`, `site.math.uchicago.edu Fejer kernel
Lipschitz log N`, and `site.math.mit.edu Fejer kernel approximation
Lipschitz`. The inspected sources above supply the useful comparisons;
other hits are unused leads. These searches do not establish novelty.

SPECIALIZE approves exactly TARGET for a separate RESEARCH /
REPRODUCTION / proof_audit turn, without first repeating literature.
No mathematical derivation, script, lemma or canonical argument is
changed here. Full matching Mathlib coverage has not been checked;
unknown availability is not absence.

Exact finite-H compatibility, other occupation identities, actual sine
limits, growing-character uniformity, actual/global realization, clipping,
capped nondegeneracy, L413's full-error regulator margin and global mixed
positivity remain unproved and unassumed. No RH conclusion follows.
