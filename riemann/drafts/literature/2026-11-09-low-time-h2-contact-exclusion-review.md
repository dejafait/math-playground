# Uniform low-time H2 contact exclusion — completed source comparison

TARGET: Test whether the actual-theta matrix H2(lambda) is positive definite uniformly on 0<=lambda<=1/20 using full moment enclosures through order twelve under L914's arithmetic contracts.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step194 reused the completed degree-one and reciprocal-Hankel source comparisons, inspected L914/L036/L037 and L874's definitions, and searched exact heat-deformed/logarithmic-Hankel, S2/S4/S6 and twelfth-moment positivity formulations; queries and inspected versus unread leads are recorded below. No matching uniform H2 theorem was inspected; this is not evidence of novelty.
SOURCE_EVIDENCE: Choi arXiv:2611.04359v1, (5)-(10), Theorem4.1 and its complete proof, (19)-(20), Proposition5.1 statement and AppendixB tail argument, https://arxiv.org/html/2611.04359v1 ; Platt-Trudgian arXiv:2004.09765v1 Section3.4 Corollary2, https://arxiv.org/html/2004.09765v1 ; Polymath arXiv:1904.12438v2 introduction after (4), https://arxiv.org/html/1904.12438v2 ; official Decimal.exp/next_minus/next_plus contracts, https://docs.python.org/3/library/decimal.html . Detailed applicability and local method coverage follow.
COMPARISON: Known real-zero/Hankel structure applies above the local cutoff 1/20, not throughout its lower-time interior; the nearby unconditional certificate concerns S1*S3-S2^2. L914 certifies only the leading H1 block. Its general quadrature and arithmetic methods are reusable, but its eighth-moment tail constants and determinant sign do not certify H2.
GAP: Enclose the actual moments M0,M2,...,M12 with newly justified complete positive-tilt tails, extract S2,...,S6 by the local logarithm and certify strict H2 positivity uniformly; none of these higher-moment enclosures or signs has been calculated in this review.
REASON: Direct finite-degree contact exclusion is independently testable after the stopped Peano pilot. Adequate method coverage permits one bounded calculation; no missing optional GHS, raw-moment or derivative-kernel theorem is an essential input to that calculation.
LITERATURE_REASON: The changed degree and moment range were outside the ready H1 assessment; startup required a separate source comparison before any higher-moment derivation or mathematical script.
SCOPE: Exactly the saved TARGET, the actual L019/L058/L874 family and L037 arithmetic contracts. One fixed-budget full-moment enclosure attempt is covered below; no flux pilot, parameter sweep, arbitrary moment model, higher degree or RH inference is covered. Assessment completed in literature-only step194; separate supervisor approval precedes the next research invocation.

## Purpose, duplicates and failures

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target is strict positivity of the single finite matrix
H2 on the closed band, as defined in L874. Its downstream use would be
exclusion of d=2 contacts there, avoiding another contact-flux pilot
whose admissible domain might be empty. It would not pay the stopped
Peano budget or establish a sign at an existing boundary.

Read the completed comparisons
`2026-11-09-low-time-degree-one-contact-admissibility.md`,
`2026-11-09-low-time-h1-uniform-moment-test.md` and
`2026-11-06-reciprocal-hankel-heat-contact.md` in this directory.
L914's full canonical proof and audit establish H1 on the closed band
under L037's contracts. They do not establish a larger principal matrix.
L033 supplies finite logarithm identities only through S4; using the
same finite extraction procedure through S6 is a research obligation,
not an identity derived or approved as proved here.

The step193 stop in
`ATTEMPTS/2026-11-09-contact-two-cell-budget-unpaid-193.md`
concerns an insufficient absolute lower bound, not negative H2 or an
actual contact. The assessed degree-two one-crossing route and its
recorded failure are contrasts. L915/L916 and step193 are not positivity
premises. Targeted searches in those assessments, the low-time source
notes and histories 180/182 found no existing uniform H2 certificate.
No previously saved certificate was executed, and no sibling notebook
was read. The historical stops remain intact.

## Primary theorem comparison

Reuse the known cutoff rather than research a new zero-free region.
Platt and Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
Bull. London Math. Soc. **53** (2021), 792-797,
[arXiv:2004.09765v1](https://arxiv.org/html/2004.09765v1), Section3.4,
Corollary2, gives Lambda<=0.2. Polymath,
[arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), introduction
after (4), states the real-zero transition t>=Lambda. The already
recorded L488 normalization is F(lambda,z)=8H_(4lambda)(2z).
Consequently the cited theorem addresses lambda>=1/20; it supplies no
all-real-zero premise throughout 0<=lambda<1/20. This reuses the prior
normalization comparison, not a new specialization proof or stronger
bound. The underlying barrier computations were not replayed.

U. J. Choi, *RH-Conditional Positivity in a Theta-Kernel Langevin Model*,
[arXiv:2611.04359v1](https://arxiv.org/html/2611.04359v1), 3 November2026,
is an unreviewed preprint. Read (5)-(10), Theorem4.1's full proof and
(19)-(20). Its kernel is local K/4; normalization cancels this factor,
and its quadratic tilt a equals lambda. The theorem's Stieltjes/Gram
structure assumes RH for all a>=0, with an unconditional case a>=0.05.
The ensuing shifted-Hankel quadratic forms use positive reciprocal
real-zero nodes. This premise is unavailable in the lower-time interior.
Proposition5.1's stated unconditional calibration is at a=0; its
displayed low-order gap is S1*S3-S2^2, not det H2. Neither that calibration
nor the all-real-zero proof supplies the requested uniform certificate.
AppendixB's complete theta/spatial tail argument was read: it treats
untilted integrals, not the present positive quadratic tilt. Its
reported numerical certificate was not replayed. No new theorem from
this preprint is a premise of the proposed direct calculation.

The ready reciprocal-Hankel assessment already compares Deng-Yang-Lu,
[arXiv:2608.11520v1](https://arxiv.org/html/2608.11520v1), Proposition4.1
and Theorem4.2: moving contour coordinates of fixed Xi zeros are a
different parameter and a different matrix. Rechecked Proposition4.1's
crossing-free hypothesis and differentiation proof; no heat-time
positivity theorem is imported. Do not repeat this contour route.

## Search and optional leads

New bounded queries were `Riemann Xi heat deformation logarithmic Hankel
determinant cumulants positive definite finite moments`, `Riemann xi
heat flow Hankel Choi`, `Riemann heat S_6 Hankel`, `Riemann logarithmic
Hankel positivity heat theta`, `Riemann twelfth moments determinant
positivity`, `Riemann Xi S2 S4 S6 Hankel heat`, and `Riemann heat-deformed
Hankel determinant positive`, plus the exact Choi identifier/title.
Generic raw moment matrices, critical-line twelfth moments of zeta and
coefficient Hankel determinants are different objects. Search failure
does not establish absence of a theorem or originality.

The search surfaced Akihiro Koide, *Strict Positivity of the Fourth
Toda-Hankel Determinant for the Riemann Xi Kernel*,
[Zenodo DOI 10.5281/zenodo.22118052](https://doi.org/10.5281/zenodo.22118052).
Only a secondary indexed abstract was visible; the primary Zenodo record
returned an access error. This is an unread theorem lead, not accepted
coverage or an imported determinant result. No bridge from its indicated
derivative-kernel determinant to the present logarithmic moments was
inspected. It is optional to a self-contained finite certificate.
Earlier Csordas-Varga raw-moment and GHS source limits are retained from
the ready assessments; this target does not depend on resolving them.
No new access campaign is required before the direct test.

## Ready calculation scope and stopping test

Essential inputs are L019/L058/L874 for the full law and coefficients,
L036/L037 for quadrature and arithmetic, and audited L914 for the
existing H1 bounds and method. No cross-notebook theorem is used.
L058 supplies smoothness and domination at all finite moment orders;
it does not provide the numerical higher-moment tail errors sought.
L036's C8 integrand theorem is not restricted to eighth moments: a
later implementation must enclose the spatial derivatives of each
actual integrand, including u^10 and u^12, over the whole rectangle.
This is method applicability, not an enclosure computed in this review.

Use at most 256 equal closed lambda panels on [0,1/20], 64 equal spatial
Taylor panels on [0,2], four theta terms and 100-digit outward arithmetic
as in L914. This deliberately fixed first test does not assert that the
budget is sufficient for the smaller higher-degree determinant. Do not
silently refine it, enlarge the theta core, or change the parameter band.
Before finite integration, justify a complete uniform positive-tilt tail
for every moment through twelve. L914's common bound is stated only for
k=0,2,4,6,8; neither its constants nor its proof's polynomial envelope
may simply be asserted for k=10,12. Any changed inequalities and actual
constants must be proved in the research record.

The [official Python Decimal documentation](https://docs.python.org/3/library/decimal.html),
Decimal.exp, next_minus/next_plus and rounding modes, was checked.
Use L037's directed operations, widened nearest-rounded exponential and
exceptional-arithmetic rejection. No binary float or library correctness
beyond the stated contract is certified. Full/supporting Mathlib
coverage remains unchecked; unknown coverage is not absence.

Normalize by a strictly positive M0 lower enclosure on every panel.
Extract the finite local logarithm through z^12 and form the exact L874
H2, retaining parameter dependence over each entire closed panel.
Use the standard named Sylvester criterion for real symmetric positive
definiteness and explicitly record all required leading-minor bounds;
L914 may supply only the minors it actually certifies. Coefficient
extraction and determinant arithmetic must have an independent exact
rational replay. No product over deformed zeros, global logarithm,
contact existence or all-degree sign is an assumption.

Continue only on strictly positive lower enclosures for every required
minor over every panel, with complete theta/spatial tails and no
arithmetic exceptions. Save complete moment, coefficient, remainder,
minor and failure records under a fresh scripts/heat filename during
research; print only actual/required bounds, failures and paths.
Inspect complete load-bearing certificate values, not previews.

If the fixed budget is inconclusive, stop and retain the failed panels
and precise source of width or unpaid tail. An interval straddling zero
does not prove a contact, negativity or failure of positivity. An actual
negative needs a valid exact-law negative upper bound; equality/contact
would need separate rigorous evidence. Do not reopen the flux pilot or
launch a parameter sweep as part of this target.

No higher-moment estimate, S5/S6 formula, determinant sign, lemma or
mathematical script was produced in step194. Contact existence remains
unresolved. Even success would address only this finite matrix and band;
all-degree mixed positivity, initialization, tangency, global continuation
and RH remain open. The next substantive work is the bounded calculation
after separate approval, not more literature without a specific reason.
