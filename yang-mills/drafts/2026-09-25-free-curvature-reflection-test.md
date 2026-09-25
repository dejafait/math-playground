# Free curvature-square reflection test, 2026-09-25

## Preflight and bounded target

Read the shared GOAL.md and PROMPT.md, local GOAL.md and PROGRESS.md, the whole PROOF.md overview and DAG.md, the existing diff, L001, and the two recorded failed approaches. Preserve all existing work. The current Clay page and linked Jaffe–Witten statement were reopened; section 4 on p. 6 still requires the axioms and a finite positive mass. No target change is indicated.

Gap: retain a nonvacuum gauge-invariant observable sector through removal of the ultraviolet cutoff. The independent-link white-noise obstruction and MRS source limitation do not evaluate a separated free curvature correlation.

Intermediate target: fix the free SU(2) normalization, specify a regularization of the centered magnetic curvature square, and compute its reflection form for one explicit smooth test function supported away from the reflection plane. Seek a finite, strictly positive limit as the regularization is removed. This is the previously recorded test, not a renewed import of positivity from MRS.

Plausible downstream use: a positive free coefficient can be the reference term in the proposed interacting observable comparison. A real, ultraviolet-uniform remainder smaller than that coefficient, convergence of the interacting moments, positivity of the full algebra, the remaining field axioms and gauge groups, and infrared control with finite positive mass remain separate unproved steps. The free model itself is not a Yang–Mills solution.

Continue this comparison only if the regularized separated reflection form has a rigorously finite positive limit. Reject this observable/test normalization if the limit vanishes or fails to exist. Compare any positive result with the actual required interacting lower bound; a free coefficient alone does not meet it.

## Saved reasoning before the calculation

Use Euclidean time x_4, three independent color copies of the free covariance delta_(mu,nu)/p^2, and B^a = partial_1 A_2^a - partial_2 A_1^a. For Hermitian SU(2) generators with Tr(T^a T^b) = delta_(a,b)/2, the free part of Tr(F_12^2) is (1/2) sum_a (B^a)^2. Smooth B with a compactly supported reflection-even mollifier before squaring and subtract its mean at each cutoff.

The expected two-point identity is (3/2) times the square of the B covariance. Reflection separates the two insertions, so that kernel can have a limit even if the ordinary unreflected variance of the composite diverges. This distinction must be checked rather than silently asserting a random-distribution limit for the Wick square.

For a positive time separation u, the spatial Fourier representation should carry the nonnegative weight (k_1^2+k_2^2)/(2|k|) times exp(-|k|u). Squaring should yield a nonnegative two-momentum integral for the reflection form. A product of explicit nonnegative bumps in space and positive time should make its transform nonzero on a positive-measure set. Constants, convergence, strict positivity, and the status of the composite limit remain to be established at this checkpoint.

## Completed assessment

The full calculation is stored in [L002](../lemmas/L002-free-curvature-square-has-positive-separated-reflection-form.md). Its separated covariance limit and nonnegative momentum representation are justified by uniform convergence away from the diagonal and an integrable exponential bound. A normalized bump supported at times 1 to 2 and in the spatial cube [-1/4,1/4]^3 gives an explicit strictly positive lower bound. Thus the proposed leading-coefficient test passes.

The regularization audit also establishes that the ordinary variance diverges as a positive constant times epsilon^-4. Only the separated reflection limit is obtained. The calculation does not establish a composite random-field limit, positivity of the full observable algebra, an interacting comparison, or a mass gap. Its massless infinite-volume covariance is not automatically the coefficient of a construction with a different infrared cutoff.

This is a relevant intermediate mathematical input, not a candidate solution. The reason for considering a fixed-box Wilson observable is to match gauge-invariant normalization and regulators before treating the free coefficient as a reference for an interacting error estimate. No such lattice calculation was performed in this step. Existing inactive branches and their evidence are preserved.
