# Source coverage for the fixed-profile joint-projection audit

TARGET: Conceptually audit L651's full joint Gram/projection transfer and its rate-1/16 lower bound for the fixed L703/L708 profile using L726.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 219 reuses the complete 2026-11-02-joint-full-grid-polynomial-dual.md assessment and its recorded exact/stronger-statement searches; read L651 in full, L650's complete polynomial response and close-pair proof, L649's coefficient/operator definitions and Fourier setup, C645y's complete-component construction, L666/L726 hypotheses and conclusions, and the joint-cost history/exposed-coefficient stop. No repeated broad search or numerical screen.
SOURCE_EVIDENCE: Rechecked Baratchart--Chevillard--Qian arXiv:1501.01161v2 (24 March 2015), Section 2 (1)--(4), printed pp.2--3, and Section 4 (17)--(19), pp.7--8; Levitt, Analyse de Fourier et applications, 2021--2022 course, Theorem 1.3/Exercise 1.2 and Remark 1.4 p.6, Definition 1.6 p.6, Theorem 1.11/Exercise 1.6 and Corollary 1.12 p.8; Howell--Mathews online Section 8.1, Theorems 8.1.5 and 8.1.7(1), including their proofs. URLs, hypotheses and reuse qualifications are below.
COMPARISON: The sources supply the orthogonal Hardy decomposition, Fourier/Parseval and finite orthogonal projection, and the simple-pole rule. They do not evaluate this prescribed joint range on F_u or supply its rate. The older assessment already compares the stronger approximation/Nehari results; those comparisons are reused. L651's explicit grid/Gram/correction argument and its fixed-profile application remain to be audited, using L726's audited scalar premise without promoting its onset to a uniform-family theorem.
GAP: Audit L651 (1)--(4), the exact inherited component/response formulas actually used, and their fixed-profile application to J_n>=c*exp(-n/16)*D for some c>0 eventually; retain the full joint space, original diagonal, normalized means and profile-dependent onset. No such application is proved by this source review.
REASON: Essential source coverage and local application scope are now sufficient for the exact saved conceptual audit. SPECIALIZE authorizes checking the existing finite Fourier/projection specialization and fixed-profile implication, not deriving a new mechanism or treating the published approximation theorems as the desired detector estimate.
LITERATURE_REASON: The changed observable is the actual Hardy projection of F_u, whose conjugations, joint Gram matrix and analytic correction were outside the paid-arc audit; resolve that scope by reusing the ready joint-space comparison and checking its elementary primary inputs.

SCOPE: One fixed actual L703/L708 profile; n=12q+3, q>=1, M=n/3; all original unit masses, full grid, inverse angle, anchor and finite endpoints. Check L651's complete M-dimensional joint space and original D_single,n against L726's D. No uniform-family onset, general-support bound, detector upper bound, Xi realization or sign conclusion is authorized.

At nomination in step 218 this continuation was REVIEW_REQUIRED.
Step 219 completes its literature-only comparison. The newly ready
assessment receives separate supervisor approval before the mathematical
audit; no projection inequality or mathematical audit is completed here.
The older joint-space assessment is reused without edits. L726's scalar
proof and completed paid arc need not be repeated.

## Primary input scope

L. Baratchart, S. Chevillard and T. Qian, *Minimax principle and lower
bounds in H2-rational approximation*, J. Approx. Theory 206 (2016),
17--47, [preprint v2](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Section 2 uses normalized circle measure, identifies H2 with nonnegative
Fourier modes and its orthogonal complement with strictly negative modes,
and defines the projections in (4). Section 4 defines the Hankel operator
for bounded symbols in (17); Theorem 2 assumes a bounded symbol, adding
continuity for compactness and its max-min characterization. Only the
decomposition/projection framework is needed here. Neither AAK nor that
max-min principle evaluates the prescribed finite joint range on F_u.
Section 2 is the more direct citation for the framework than (17)--(19)
alone. No typo-prone extracted adjoint/eigenvector formula is used.

A. Levitt, *Analyse de Fourier et applications*, 2021--2022 course,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
retrieved 3 November 2026. Theorem 1.3 gives Bessel for an orthonormal
family in a Hilbert space, and Parseval when that family is complete.
Exercise 1.2 supplies the finite-projection proof; Remark 1.4 records
componentwise inner products. Theorem 1.11 and Corollary 1.12 give
Fourier completeness and L2 Parseval. Exercises are proof outlines,
not independently certified solutions. This course uses ordinary
Lebesgue measure and exponential basis divided by sqrt(2*pi), whereas
the notebook uses normalized measure and unscaled exponentials. The
audit must translate that convention consistently for coefficients,
norms and inner products. The source does not assert the nonorthogonal
inverse-Gram identity or the explicit grid exponent; these are local
finite-algebra obligations. No general Fourier theorem needs reproving.

R. W. Howell and J. H. Mathews, *Complex Analysis*,
[online Section 8.1](https://complexanalysis.org/web/sec_residue-thm.html),
retrieved 3 November 2026, Theorems 8.1.5 and 8.1.7(1).
The residue theorem requires a simple positively oriented closed contour
in a simply connected domain, analyticity on it and only finitely many
interior isolated singularities. Part (1) gives the simple-pole rule.
Read both statements and their finite-contour/Laurent proofs. L650's
(9)--(10) and C645y's (6)--(8) are the local applications to check,
including the scaled pole locations, possible cancellations and absence
of a polynomial part. Multiplicity of a root of P does not license
omitting its original residue. No uniform limit theorem is imported.

The earlier assessment's inspected Theorem 4/Section 5.2/Theorem 7 of
Baratchart--Chevillard--Qian, Frazho--ter Horst--Kaashoek Theorem 3.1,
and Baratchart et al. arXiv:2603.16295v2 Theorem 3/Proposition 1 are
reused comparisons, not newly retrieved theorems. Their approximation
observables and extra hypotheses do not already identify the present
weighted projection. No additional unread lead is essential to this
audit; a failed search never certifies novelty. Full matching Mathlib
coverage is not checked; supporting Fourier/projection facts must be
distinguished from a matching theorem.

## Exact local audit obligations and overlap

The audit must check the particular identities used, rather than accept
all conclusions of unaudited inputs. C645y Section 1 constructs F_u by
finite rational partial fractions and gives (8). L650 Section 2 gives
the response for an arbitrary polynomial and its full-grid norm; L649
fixes c_k, h_k and D_single,n. No Biro estimate, recovered-input lower
bound or inverse-grid interpolation bound is required for this scope.
Their older route stops remain qualifications, not premises.

In L651 Sections 2--4 check all n grid factors in the small-circle
estimate, the coefficient bound and M<=n/3, anti-linearity of J, the
index convention G_(jk)=<d_k,d_j> with inner product linear in its first
entry, the inverse-Gram response, and the complete analytic correction.
Check the L2 angular triangle inequality and exponent comparison at the
square-root scale as written. A finite verification certificate is
secondary evidence and was not replayed here. It cannot prove the
uniform estimates. L650's close pair must retain its joint sum; the
separate-column stop is not a counterexample to this range.

For application, check the fixed L703/L708 profile against L666's
admissibility and finite endpoints, n=12q+3, unit original masses,
M=n/3, and the identical W_a and D_single,n=D definitions in L726.
Retain both L726 (2)'s audited scalar premise and (3)'s paid-arc
qualification. The later audit must explicitly justify whichever link
from these premises to L651's S_n it uses; this review asserts no new
moment or arc inequality. A pointwise angular maximum, positivity of
Gram matrices, or replacement by the first M grid coordinates is not
that link. Its onset can depend on the fixed profile.

The joint-cost history already records L651 as a conditional reduction,
not the response lower bound. The exposed-coefficient failure record
points to L670 and concerns a different denominator-cost certificate;
it does not veto this fixed-profile application. L652/L653's alternative
interpolation/remainder tests do not supply an independent audit of
L651. Earlier grid-prefix, polewise and ambient-recovery stops retain
their original scope. This step imports no cross-notebook input and
derives no new lemma, constant or counterexample.

The main gap is still actual-Xi positivity. A validated fixed-profile
projection lower bound would connect the scalar response to a concrete
detector norm; matching upper bounds, arbitrary support and Xi transfer
would remain independent. This is a different missing application from
the parked arbitrary-displacement signed-flow estimate. No claim that
those independent gaps are solved or contradicted is intended.

The later mathematical acceptance test is the stated eventual lower
bound for J_n with a positive constant for this fixed profile, retaining
all correction terms and norms. A failed conjugation, projection, norm
estimate or quantifier step must instead be isolated and the claim
narrowed. No numerical screen or inferred sign of a cross term suffices.
Essential input IDs are L651, L726, L666 and the exact inherited
C645y/L649/L650 formulas; L703/L708 fix the already-established profile.
Full matching Mathlib coverage for this projection specialization is
not checked. No fresh mathematical exploration is undertaken here.
