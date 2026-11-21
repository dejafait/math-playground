# Coefficient-defined affine quotient: nominated residual obstruction test

TARGET: Test the affine-quotient embedding from U_6 to U_7 for a certified negative quadratic direction in P_6=B_7-E_6 B_6 E_6^t, using the full Jensen-weighted Kuznetsov coefficients and fixed existing input enclosures.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded comparison2020 in drafts/literature/2026-11-20-tilted-degree-evolution-source-scope-2019.md: exact-family, Euclidean/affine-quotient and positive-increment searches found no adequate actual-family theorem; scoped November20 tilted-family duplicate search found no prior test. No novelty inference.
SOURCE_EVIDENCE: Direct primary PDFs reaccessed 2026-11-20: Kuznetsov CMB51(2008), pp562–563/566/568–569, recurrence(2), coefficients(4)/(13), weighted family https://www.cambridge.org/core/services/aop-cambridge-core/content/view/FD79D70DF68748CCEC70097E3FB9F2FA/S0008439500012492a.pdf/expansion-of-the-riemann-function-in-meixnerpollaczek-polynomials.pdf ; Wu–Wu–Yang ELA21(2010), definition(1.1), Proposition3.7/(3.12)–(3.13) and complete proof pp165–166 https://emis.de/ft/34467 ; reuse C029n/C029o/C029p normalization, enclosures and audited baseline; precise applicability below.
COMPARISON: The multiplication representation is known, but no inspected theorem supplies the sign of this actual-coefficient residual. The quotient fixes the embedding independently of roots or inertia. This is distinct from generic coefficient dilation (L530/L955), identity bulk (C029n), and the closed finite-signature sequence (C029p).
GAP: Whether this one prescribed residual has an independently certifiable negative direction; even failure to find one is not PSD, and no all-degree propagation or RH premise is proved.
REASON: A bounded new coefficient-dependent mechanism can discriminate an actual-family propagation ansatz using ready finite algebra and source formulas, without another isolated root count or unavailable-runtime retry.
SCOPE: Separately reviewed and approved in literature-only recovery step2021; ready for the exact saved research target. Only the pair N=6,7, prescribed quotient embedding, fixed direction set and fixed existing 60-decimal enclosures; no spectral fitting, degree/precision campaign or new analytic claim.

## Proposed object, not a derived result

Use C029m's exact T_N with all odd coefficients and weights
N!/((N-k)!N^k). Put U_N=T_N/S with the same
S=sin(pi/8)/sqrt(2)>0 as C029n. No N-dependent monic or norm
renormalization is allowed. Reuse C029n's audited degree-six and
nonzero-leading-coefficient facts; U_7's actual degree must be checked.
If it is not certified seven, record that failure and stop this test
without assuming degree or choosing a replacement pair.

If the degree test passes, let q_6 be the unique affine quotient in
ordinary polynomial long division U_7=q_6 U_6+r_6, deg(r_6)<6.
This defines the proposal before sign inspection; its coefficients
have not been evaluated here. With

    Phi_6=(p_5,p_4,...,p_0)^t,  Phi_7=(p_6,p_5,...,p_0)^t,

define E_6 (7 by 6) by q_6(t)Phi_6(t)=E_6^t Phi_7(t).
Its finite construction uses the imported Pollaczek recurrence and
coefficient matching; Wu Proposition3.7 supplies the relevant general
kernel-multiplication interface. Verify reversal/transpose directly;
do not simply identify E_6 with a source matrix W.

B_j means the coefficient matrix of

    (U_j(x)U_j'(y)-U_j(y)U_j'(x))/(x-y)

in Phi_j, using C029o's convention. Define the proposed residual
P_6=B_7-E_6 B_6 E_6^t. This is a definition for a sign test, not an
asserted PSD decomposition, a novel representation theorem, or a
known common-factor specialization. A polynomial and its derivative
are not being assumed to share the quotient factor. No derivative
product identity or residual sign has been derived in this assessment.

## Bounded test and evidence threshold

The research attempt should seek a negative quadratic direction only
among v=e_i and v=e_i+e_j, e_i-e_j for 1<=i<j<=7 in the stated
descending coordinates. The set is fixed independently of the entries
or signatures. Construct coefficients, quotient, basis embedding and
residual exactly; verify the division identity, both defining kernel
identities and the embedding coefficient identity. Use C029n's fixed
60-decimal rational enclosures for pi and sqrt(2), with justified
interval reciprocals only for denominators separated from zero.
Coefficients may be handled as exact rational functions in
Q(sqrt(2))[pi], with every cleared denominator justified. No package
install, eigenvector fit or precision escalation is authorized.

Save the complete coefficients, denominator/degree checks, quotient
and remainder, E_6, P_6, identity residuals and all tested rational
quadratic forms with full interval endpoints and failures under
scripts/pollaczek/. Print only actual/required bounds, failures and
certificate paths. A useful negative result requires an explicit
rational v with a rigorous upper bound v^t P_6 v<0; a plot or
midpoint sign is not evidence. The canonical finite result must include
the proof, source applicability and Mathlib qualifications. If no such
direction is separated, the prescribed test is inconclusive: even
strict positivity on this finite direction set does not prove PSD.
Do not silently broaden the set or advance to N=8.

The intended downstream use would be a coefficient-controlled positive
increment for eventual index propagation in C029m. A negative witness
rejects this embedding's PSD claim at this pair only, not every
embedding, an eventual-only mechanism or RH. Even a future full PSD
certificate here would leave uniform signs, all-degree quotient/degree
control, singular cases, initialization and qualified compact
convergence/upstream[9] unresolved. This is a creative mechanism test;
the finite kernel algebra itself is standard and is not claimed new.

Essential inputs: C029m exact family; C029n coefficient field,
normalization and enclosure proof; C029o kernel convention; C029p
audited baseline; review2001/comparison2020 primary source coverage.
L530/L955 are obstruction contrasts, not mathematical premises of the
residual. No cross-notebook input. Full matching Mathlib coverage is
unchecked. Separate literature approval completed in recovery step2021;
no new mathematics or mathematical script execution occurred in either literature step.


## Separate source-gate approval2021

The direct URLs above are accessible primary PDFs, not search previews.
Reused comparison2020's searches and overlap decision; no changed target
or new discovery search is needed. Reinspected the following passages:

- H. Wu, X. Wu and Z. Yang, *More on polynomial Bezoutians with respect
  to a general basis*, Electronic Journal of Linear Algebra 21 (2010),
  154–171, DOI 10.13001/1081-3810.1421, [primary PDF](https://emis.de/ft/34467).
  Definition (1.1), p154, fixes the kernel order. Proposition3.7,
  (3.12)–(3.13), and its complete proof pp165–166 assume a degree-graded
  basis, specified factor degrees and an already factorized kernel.
  They give rectangular coefficient multiplication, without positivity.
  For the proposed affine multiplication the relevant size is n=7,
  r=s=1; reversing the basis and checking the defining identity remain
  required. This is an applicability prescription, not a computed E_6
  or a factorization claim for U_7 and U_7'. The displayed proof's final
  n-r versus n-s subscript does not affect this equal-degree case.
- A. Kuznetsov, *Expansion of the Riemann Xi Function in
  Meixner–Pollaczek Polynomials*, Canadian Mathematical Bulletin 51(4)
  (2008), 561–569, DOI 10.4153/CMB-2008-055-0, publisher PDF above.
  Reinspected basis p562, recurrence(2)/coefficients(4) p563, finite
  formula(13) and cancellation warning p566, and full weighted passage
  pp568–569. These specify the full family including odd coefficients.
  The one-pair degree6–20 observation is numerical; no inter-degree
  positive residual follows. The finite test needs no infinite-series
  convergence import or reproof of the source formulas.

Local comparison reused the scoped duplicate/failure check in
comparison2020, including C029n's support-restricted obstruction and
L530/L955's generic-flow stops. They do not settle this prescribed
actual-coefficient embedding. C029m hypotheses and analytic qualifications,
C029n coefficient normalization, and C029o/C029p hypotheses/conclusions
were consulted for scope; no numerical certificate was revalidated.
Mathlib full matching coverage remains unchecked.

Approval is limited to the unchanged EXPLORE target and its fixed bounds.
No sign, identity residual, degree-seven fact, mathematical advance or
novelty is established by this approval. The exact next research attempt
is now source-ready; no additional literature turn is warranted absent
changed hypotheses or new essential evidence.
