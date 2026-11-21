# Two-center Hermite residual test — ready tools, pending separate approval

TARGET: Test the degree-n two-center Hermite interpolant at t=n+1 and t=2(n+1), with balanced multiplicities, for an uncapped fixed-grid complete residual O(exp(-n/64)) on both spectral windows.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: Step382 completed the parent two-window review381, with scoped duplicate/failure searches and external varying-power, two-arc, Faber-Walsh and Hermite searches; no matching full-kernel rate was found or novelty inferred. Exact queries and comparisons are in that assessment.
SOURCE_EVIDENCE: Calvi, Lectures on Multivariate Polynomial Interpolation (Hanoi2005), Theorems1.9/1.17/1.18, pp14,20-21, full relevant proofs, https://www.math.univ-toulouse.fr/~calvi/res_fichiers/MPI.pdf ; DLMF3.3.3-6/37 https://dlmf.nist.gov/3.3#E6 ; audited C997c(1),(4)-(6), C997s(2)/step373. See completed review381 for precise hypotheses and stronger-source comparisons.
COMPARISON: The exact Hermite contour remainder covers repeated nodes, complex analytic functions and each finite degree, including n-dependent functions. It leaves the contour modulus, node product, separation and both complete-kernel weights to be paid. C997r's centered capped-norm/defect stop does not decide this uncapped two-center residual.
GAP: The candidate's actual branch/contour construction and fully charged degree-dependent error remain unpaid; no uniform residual rate or general impossibility is known from these inspected sources.
REASON: Ready exact finite-degree coverage supports one mathematical test without importing a fixed-function root limit as a growing-n estimate. This newly written continuation receives separate later approval; step382 derives no interpolant estimate or new lemma.
SCOPE: Integer n>=2; I=[7/4,9/4], z_star=1+i/8, gamma_j=15/8+j/(4n), 0<=j<=n; exactly the prospective interpolant below, unrestricted coefficients, complete kernel and both closed spectral windows. No coefficient-cap conclusion or all-polynomial obstruction is approved.

## Prospective recipe and bounded test

Use spectral coordinate y=exp(it/(4n)) and the analytic target obtained
by removing exp(15it/8) from exp(i z_star t), with its branch identity
to be explicitly verified. The proposed interpolation nodes are the
images of t=n+1 and t=2(n+1); prescribe multiplicities
floor((n+1)/2) and n+1-floor((n+1)/2), respectively. Multiplicity m
means matching derivatives of orders0 through m-1 in y. The resulting
degree-at-most-n Hermite interpolant and its grid coefficients are to
be constructed in the research attempt, not asserted here as a rate
certificate. These interpolation nodes impose no additional gamma grid.

Calvi's formula requires a simply connected holomorphy domain, a
piecewise C1 contour in that domain of index one around every node and
evaluation point, with the contour avoiding them. The later proof must
check the log branch, distinctness of the two node locations, both
images of [n,n+2] and [7n/4,9(n+2)/4], all contour distances and the
full n-dependent target modulus. Small-n overlap may be handled directly
or left below an explicitly stated eventual onset. No deletion of the
lower window, division by g_n, or discarded zero is allowed.

Import the exact Hermite remainder and known finite-measure bounds;
do not reprove interpolation theory. The required test is a uniform
bound C exp(-n/64) for the COMPLETE kernel residual on c in I,
all n beyond one onset, with C independent of n. Pay every polynomial
prefactor and every upper-window growth factor; a root rate equal to
the threshold alone does not imply the stated big-O bound. A rigorous
obstruction to this candidate is also informative. An inadequate upper
envelope alone is inconclusive, not a lower bound for its residual or
for optimal approximation. After one bounded inconclusive attempt,
park the recipe pending a materially new input or refined mechanism.

Its plausible downstream use is to control target action of unit-TV
measures with EXACT zero band pairings, and distinguish that question
from paid leakage under C997s's original exp(sqrt(n)) coefficient cap.
That implication must be justified in the later proof. Unrestricted
coefficients do not bound the capped E_n. Neither success nor failure
would resolve actual-Xi signs or the independent transfer assumptions.

Essential inputs are C997c(1),(4)-(6) and C997s(2)/step373; C997r/t/u
are scope contrasts, not quantitative premises for this target. The
interpolant rate itself, any later cap, C997a(8), selected/both-sign
transfer, assay/reconstruction, complements/regulators, L993, L984(H),
L966/L968 forcing and L030-L032/C032a positivity remain unresolved.
The main RH gap is unchanged. No cross-notebook input. Full matching
Mathlib coverage is unchecked and none is used.

Full source notes, citations, nonessential access failures and the
preserved nomination are in
[the completed parent review](2026-11-11-two-window-uncapped-approximation-review-381.md).
No mathematical result, coefficient bound or source-blocked theorem is
imported by this nomination. The next approved mathematical attempt
would be a specialization/reproduction of known tools, not a claim of
discovery beyond the literature searched.
