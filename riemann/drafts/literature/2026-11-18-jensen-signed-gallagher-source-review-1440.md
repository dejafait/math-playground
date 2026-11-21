# Signed frozen-J Gallagher coverage — review1440

TARGET: Assess source coverage for a signed Gallagher bound of Bq^2 for the mean-square integral of the original frozen-J polynomial, retaining all four tapers and the midpoint translation.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Scoped Jensen literature/working/attempt/history searches found nomination1439 and reusable1436, but no matching completed signed-energy estimate. New bounded queries and their results are recorded below; failure to locate a match is not a novelty claim.
SOURCE_EVIDENCE: Read Coppola--Laporta1411.1739v1 Section1 (star), Dirichlet inequality (star-shaped symbol), weighted Lemma (star-star), Remark2, and Section2 compact-weight proof, PDF pp1-2,5; also its Theorem1 and logarithmic-to-additive proof pp3,6-7. Compared1301.0008v1 Theorem and Lemma proof pp2-3. Reuse1436 for Matomaki--Teravainen Lemma3.3 and Heath-Brown Theorem4.
COMPARISON: A signed exact multiplicative-window inequality accepts the full complex midpoint-translated frozen array; it does not require positive coefficients or a balanced arithmetic function. Its energy remains unestimated. Absolute majorization returns an unpaid budget; additive Cesaro replacement carries an extra absolute error. No inspected source proves this witness's O(Bq^2) norm.
GAP: Estimate the complete signed logarithmic-window energy at O(Bq^2/U^2), uniformly in Y0 and the prescribed integer d. Fixed-to-moving transfer, the real denominator, numerator, E_P and Xi transfer remain separate. This review establishes coverage for a bounded test, not the energy estimate.
REASON: Missing signed-window hypotheses and normalization in1439 required this literature-only turn. The inspected exact window avoids an essential source blocker and supplies a discriminating threshold without changing the witness or deriving a new estimate.
SCOPE: Finite frozen J only, with C019y (1),(3)-(5), C019z audits1433/1435 and C020h audit1439. The precise energy and future test are defined below. No lemma or mathematical script is changed.

## Primary statement and proof cases actually inspected

Coppola--Laporta, [*A generalization of Gallagher's lemma for exponential
sums*, arXiv:1411.1739v1](https://arxiv.org/html/1411.1739v1),
21 October2014, Section1, PDF p1, displays the Dirichlet inequality
(star-shaped symbol; HTML renders it as (I)):

\[
 \int_{-T}^{T}\left|\sum_n a_n n^{it}\right|^2dt
 \ll T^2\int_0^\infty
        \left|\sum_{y<n\le ye^{1/T}}a_n\right|^2\frac{dy}{y}.
\]

Coefficients are complex; absolute convergence suffices. The underlying
frequency inequality fixes delta*T=theta in (0,1); the displayed
Dirichlet form fixes theta=1/(2*pi), hence an absolute constant.
The weighted Lemma, p2, covers locally integrable compactly truncated
weights, with multiplier minimum m=min_(|t|<=T)|hat(w_delta)(t)|^2.
Its compact-weight proof, p5, separates infinite right-hand energy
from the finite case, uses Fourier multiplication and Plancherel,
then bounds below by m. Remark2 recovers the original indicator.
The unrestricted-L1 extension is unnecessary here.

The historical attribution is Gallagher, *A large sieve density
estimate near sigma=1*, Invent. Math.11(1970),329--339,
[DOI](https://doi.org/10.1007/BF01403187), Lemma1/Theorem1.
Its original proof was **not** inspected: the PDF request redirected
to a landing page. The independently proved compact-weight result
above is the inspected primary input; no reproof is needed.

Coppola--Laporta, [*A modified Gallagher's Lemma*,
arXiv:1301.0008v1](https://arxiv.org/pdf/1301.0008v1),
31 December2012, pp2--3, gives the triangular alternative and its
Fourier/Plancherel proof. Its additive-window Theorem retains an
absolute-coefficient error integral, with Delta=y/T+O(y/T^2).
Dropping that error is not justified. The later paper's Theorem1
and proof, pp3,6--7, retain the same issue.

## Local applicability, sufficient threshold, and limits

Use the **existing** C019y/C020h definitions without shortening N=Z_*,
changing U=|D|/2, or replacing any coefficient. For each fixed Y0 in D
write the coefficient to be passed to the displayed source theorem as

\[
 \beta_k(Y_0)=J_k(Y_0)k^{-1/2-iY_c},\qquad 1\le k\le N,
\]

and zero elsewhere. Yc is D's midpoint. This array is finite, so
absolute convergence is automatic. Distinct k have distinct logarithmic
frequencies; sorting them meets the frequency-order convention.
Complex coefficients are explicitly allowed. Reflection t to -t on
the symmetric interval handles the source's positive exponent. The
coefficient phase k^(-iYc) stays inside every short sum. There is no
restriction on how this fixed array depends on parameters Y0 or d;
uniformity of any subsequent estimate is an additional local obligation.

Define the proposed energy, **not an estimate**, by

\[
 E(Y_0)=\int_0^\infty
   \left|\sum_{y<k\le ye^{1/U}}
                J_k(Y_0)k^{-1/2-iY_c}\right|^2\frac{dy}{y}.
\]

The sufficient research threshold read from the source is

\[
                  E(Y_0)\le C Bq^2/U^2
\]

with one absolute C for every Y0 in D and every sufficiently large
prescribed integer d. This is a target for a later attempt; no bound
on E is proved here. The known inequality would then supply the saved
frozen O(Bq^2) norm. Do not strengthen this sufficient condition into an
equivalence or a necessary condition for that norm. Neither a large
upper envelope nor a failed proof refutes the frozen norm bound.

No smoothness, positivity or mean-zero assumption is needed for this
exact window. In particular, do not invoke the paper's real/balanced
Selberg-integral statements for beta without verifying their extra
hypotheses. Do not replace ye^(1/U) by y+y/U, introduce additive taper
weights, truncate the y integral, or subtract a presumed mean while
discarding a remainder. The source proof explicitly shows why an
additive replacement can create an absolute error. The exact formula
avoids needing that replacement; it does not pay any signed correlation.

All original unordered distinct witness-prime pairs, c_s with its four
individual linear tapers, h shifts, and both own heat times stay in J.
The heat factors are frozen at Y0 and Y0+h, rather than replaced by
their leading constant. C019z/C020h give coefficient bounds and support,
not the short-window cancellation. C020h's subset argument lower-bounds
only a nonnegative absolute budget: a subset of this signed sum cannot
be removed to obtain a lower bound for E. Conversely, allowing the
midpoint phase in a theorem does not itself prove cancellation.

The plausible downstream use is a frozen component of a denominator
estimate. The moving J_k(Y), the real nonconjugate channel in C019y(5),
signed numerator, E_P and actual-Xi realization are still unpaid.
No every-degree Jensen hyperbolicity or RH conclusion follows.

## Search, reuse, and recorded failures

Actual new queries included `Gallagher mean value estimate exponential
sums 1970 lemma short interval Dirichlet polynomials pdf`, `Gallagher
lemma Dirichlet polynomial complex coefficients delta theta T integral
signed short sums`, `Gallagher 1970 A large sieve density estimate near
pdf Lemma 1`, `Gallagher mollifier prime mean square Dirichlet polynomial`,
`Dirichlet polynomial four mollifier short interval mean square`, and
`Gallagher signed complex coefficients short interval mean square`.
The two Coppola--Laporta manuscripts were opened as primary sources;
snippets were discovery only. The arXiv PDF/HTML supplied the statements
and relevant proof cases above. Shell download failed DNS; web access
worked, so this is not an essential source blocker.

Reuse [source-review1436](2026-11-18-jensen-full-denominator-spacing-source-review-1436.md)
for Montgomery--Vaughan G.16, Matomaki--Teravainen2207.05038v2
Lemma3.3, and Heath-Brown1808.02947v1 Theorem4(iii),(iv), with their
already inspected hypotheses and good/bad-pair costs. Those results do
not supply a matching signed-energy evaluation; the full absolute
neighbor framework is stopped by canonical C020h/audit1439.
Stops1407/1408 concern other absolute G-array budgets; mixed G-J
completion1431 has exhausted three attempts. None is reopened or reset.
The new independent target is frozen J-J signed energy.

A new search lead was Arguin--Bailey, *Lower bounds for the large
deviations of Selberg's central limit theorem*, Mathematika71(2025),
e70002, AppendixA/LemmaA.1. The publisher extraction omitted essential
formulas; the Oxford PDF returned403. This lead is **not a theorem
inspected with complete hypotheses**, is not imported or rejected on
mathematical grounds, and is not needed for the general window test.
No claim about its applicability is made. Likewise the1970 proof is
unread, not silently substituted for the inspected generalization.
No matching full energy estimate was located in this bounded search;
this does not establish originality or absence from the literature.
Full matching Mathlib coverage was not checked.

## Decision and bounded handoff

EXPLORE: source hypotheses accept the complete translated polynomial
and give a concrete sufficient scale. The future attempt must estimate
the signed prime-product/four-taper correlations or prove an informative
obstruction to that sufficient estimate. An exact expansion alone,
renaming the norm as energy, or repeating the failed absolute envelope
does not establish the target. Stop a method if its final bound divided
by Bq^2/U^2 has an unbounded loss. Preserve partial reasoning and report
an inconclusive attempt honestly if no comparison is obtained.

This is literature-only EXPLORATION with NOVELTY_UNCHECKED: new source
coverage, no new witness bound and no mathematical exploration turn
spent. The [research nomination1440](2026-11-18-jensen-signed-gallagher-energy-nomination-1440.md)
requires separate next-turn approval before calculation. This source
comparison supplies no justified new central creative mechanism; the
next target develops an established tool at an independent norm gap.
PROOF/DAG remain unchanged because the assembled argument did not change.
