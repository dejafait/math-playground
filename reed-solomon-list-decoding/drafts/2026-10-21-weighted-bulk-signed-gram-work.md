# Weighted bulk signed-correlation attempt — step 390

Approved target: Bound L104's weighted disjoint-collision excess over r=4,...,67 by (T-C/D)^2-delta.

The preexisting EXPLORE assessment is
`drafts/literature/2026-10-21-translated-pole-weighted-bulk-collision-bound.md`.
Keep exactly L104's parameters, full group, ordered disjoint pairs and
signed subtraction. Inputs read: L104, the relevant L102 proof, C012a
and foundations/02. The main gap is arbitrary-center 67/68 safety;
success here would only exclude L102's family, conditional on L104's
pending critical audit. Existing work and all stopped estimates remain.

## Attempt tested

Test character averaging of the signed cycle expression before applying
any norm. L102's imported Li–Wan sieve, equation (9), writes W_chi as
a signed sum of cycle monomials. Squaring this expression and averaging
over characters keeps a Gram matrix of mixed cycle correlations; the
principal character must be subtracted exactly. The proposed closure
uses the degree-three residue rigidity underlying L104's r<=3 cases,
rather than an unsigned triangle inequality or a retuned pointwise cap.

The discriminating question is whether that rigidity evaluates enough
mixed correlations to give a numerical bound on the full degree-67
quadratic form. Every unevaluated block must remain unknown. In
particular, individual centered entries and bulk terms may be negative.
Do not infer a bound from positivity of the whole Gram matrix alone.

## Where the proposed closure remains incomplete

Here is the specific attempted use of the imported sieve, so that the
failure is not mistaken for another evaluation of the old allowance.
For a partition lambda of 67, with m_j parts of size j, the cycle
coefficient in L102 (9), after division by 67!, is
`a_lambda = (-1)^(67-sum m_j) / product_j(j^m_j m_j!)`.
Write `F_lambda(chi)=product_j C_j(chi)^m_j`, where C_j has exactly
L102's meaning. The expression to estimate is the quadratic form
obtained by substituting `W_chi=sum_lambda a_lambda F_lambda(chi)`
into L104 (2). Its mixed entries are the averages of
`F_lambda(chi) conjugate(F_nu(chi))` over nonprincipal characters,
with the factor 1/D retained. These are merely the cited identities
expanded as finite sums, not an additional energy theorem or estimate.

The proposed computation was to evaluate the mixed entries by character
orthogonality, use the degree-three rigidity on the resulting products,
and retain the signed coefficients a_lambda a_nu until after summation.
This does not close. Expanding a cycle monomial permits repeated root
labels. Each side has **total polynomial degree 67**, even when its
cycles have small individual lengths. Equality of the residues says
that the difference of these weighted monic root products is divisible
by (X-3)^3. It does not say that their individual cycles have equal
residues, or that the two products are identical. L104's rigidity
applies after cancellation only when the remaining degree is at most
three. There is no argument that cancellation leaves that degree in
these mixed entries. Partitioning by actual common factors returns the
unestimated larger-difference collisions; it does not determine them.

In particular, treating different cycle lengths as independent would
factor a character average unjustifiably: all cycles use the same chi.
Replacing the mixed matrix by its diagonal discards correlations of
uncontrolled sign. Its positive semidefiniteness gives no upper bound
on this quadratic form without further entry or spectral control.
Using Cauchy–Schwarz on every mixed entry and then taking absolute
cycle coefficients is precisely the unsigned-cycle step that
ATTEMPTS/007 rules out as a reopening mechanism. The present attempt
does not perform that substitution or report its allowance as evidence.

No mixed-entry estimate controlling the unresolved degree-67 bulk was
obtained. No K_r for r>=4 was evaluated. The required comparison remains
exactly L104 (3), with the relative budget in (5) between
5889972/10^12 and 5889973/10^12. There is no achieved numerical bound
to compare to it, no proof that the budget fails, and no family verdict.
No mathematical script or new lemma is justified by this incomplete
closure. Full matching Mathlib coverage was not checked.

## Outcome and mechanism reassessment

RESEARCH / REPRODUCTION / proof_attempt; EXPLORATION. The work applies
the already assessed sieve and orthogonality tools but establishes no
new mathematical input. This is the third mathematical exploration
turn, 3/3, without an advance or informative negative result on this
route. Park this low-degree closure of the signed Gram expression.
The target energy inequality itself is neither proved nor refuted.
Reopening requires a concrete estimate for the remaining mixed
correlations, not another reduction, norm, source recheck or pole rename.

Three continuation choices were compared without undertaking their
mathematics: another cycle envelope repeats ATTEMPTS/007 and 085;
another low-overlap enumeration does not yet explain control of the
weighted bulk; a fixed-pair exact-cardinality feasibility test addresses
a different, global-support consistency gap. Select the third for
separate source review. Unlike ATTEMPTS/082, that proposal fixes the
pair marginals, omits PSD, and seeks an exact scalar/contraction
certificate rather than restarting the capped full-variable numerical
prescription. L098 already has a critical audit (step 362), so repeating
that audit is not the continuation despite the stale overview wording.
No new feasibility formulation or certificate is derived here. The
new assessment remains REVIEW_REQUIRED and must check duplication,
normalization, permissible aggregation and a bounded method first.
