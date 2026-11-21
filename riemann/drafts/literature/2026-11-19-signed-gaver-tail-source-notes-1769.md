# Signed Gaver tail source comparison1769

19 November 2026. Literature only, completing assessment1768's exact
saved target. Main gap: L030-L032/C032a actual-Xi all-degree positivity.
The intermediate aim is uniform finite-transform evaluation of C033j's
signed remainder densities at 7/8 and 9/8. It could support later jump
resolution/finite separation; cancellation, moments and Xi realization
remain independent. No mathematical estimate is proved in this review.

## Primary evidence and applicability

Reuse notes1764's primary Gaver1966 inspection, original pp448-451,
(13)-(29), including normalized kernel, exact cumulant sums, finite
binomial transform formula and concentration discussion. Full citation:
D. P. Gaver, Jr., *Observing Stochastic Processes, and Approximate
Transform Inversion*, Operations Research14(3) (1966), 444-459,
[DOI10.1287/opre.14.3.444](https://doi.org/10.1287/opre.14.3.444).
The university-hosted scan was reachable by the web tool but yielded
no extractable text; fresh screenshots were not available as readable
evidence in this interface, and shell download failed DNS. No fresh
inspection of that scan is claimed. Prior adequate primary coverage
is retained, not replaced by a search snippet.

Directly inspected A. Kuznetsov, *On the convergence of the
Gaver-Stehfest algorithm*, SIAM J. Numer. Anal.51(6) (2013), 2984-2998,
[1305.0715v2](https://arxiv.org/pdf/1305.0715v2), served manuscript
dated29 October2018, pp2-3, (2)-(4) and surrounding hypotheses.
For integer n>=1 the base kernel in (3) is

    p_n(u)=(2n)!/[n!(n-1)!]*(1-exp(-u))^n*exp(-n*u), u>=0.

The source states positivity/unit integral and supplies the finite
transform expression (2) and its binomial-theorem integral form (3).
These cases concern real locally integrable functions with transforms
finite at all positive arguments. Expansion (4) requires f in C^(2m)
and bounded derivatives through 2m, including globally bounded f.
Those hypotheses are unavailable for the full R_sigma, which has an
atom. Convergence in distribution alone does not justify expectations
of arbitrary unbounded continuous functions; that informal inference
is not imported. The signed-measure identity, tail supremum and
family-uniform rate remain separate obligations. The accelerated
Theorem1 proof is not imported.

Directly checked J. Abate and W. Whitt, *A Unified Framework for
Numerically Inverting Laplace Transforms*, INFORMS J. Computing18(4)
(2006), 408-421, DOI10.1287/ijoc.1050.0137,
[author-hosted published PDF](https://www.columbia.edu/~ww2040/AbateUnified2006.pdf),
p414, Section4/(28)-(29). Equation(28) confirms the base finite
transform formula and real positive nodes. This is formula coverage,
not a signed-family error theorem or certified precision rule. The
acceleration and empirical efficiency discussion is unused.

Reuse notes1764's full BMS2017 Propositions2.2/2.3/2.5 and proofs
Sections5.1-5.3. The statements on pp2-3 of the
[16 May2017 manuscript](https://www.wias-berlin.de/people/schoenma/BelomestnyMaiSchoenmakers_16_05acc.pdf)
were checked against the changed hypotheses: probability densities,
Post-Widder transform derivatives, local Lipschitz regularity and
fixed-x O(N^(-1/2)) rates. A kernel-mass tail bound is not a supremum
bound against an arbitrary variation measure. No direct application
to signed R_sigma or replacement by finite Gaver samples follows.
Prior proof coverage is reused without importing a signed extension.

## Remaining specialization and discriminator

Read C033j's hypotheses, family and (6)-(15), and C033p's hypotheses,
parameter bounds and normalization. These supply
R_sigma=exp(-M_sigma)delta_0+r_sigma(t)dt, sigma in[1,2], uniform
finite TV V, a common finite local height B on[3/4,5/4], and audited
Lipschitz constant L there. B,V,L have no numerical certificates.
Preserve the actual-divisor, conjugation/multiplicity, ordinate-zero
exclusion, strict-strip, gamma>14, counting, through100/retained-real-zero/
tail, separate fixed-j heat, half-variance and both fixed-v1 qualifications.

The sources specify a specialization attempt, not its conclusion.
It must justify integration against finite signed measures, separate
local density variation, local normalization leakage and the outside
integral against full variation, and evaluate the zero atom explicitly.
Probability-tail mass alone does not pay variation tails. Do not assert
positivity of R_sigma or apply a probability-density theorem to it.
Use exact source normalization and track finite coefficients. None of
these missing estimates is derived here.

The discriminator is a stated E_n(B,L,V)->0 uniformly over sigma and
both x. Failure of outside-interval supremum decay or a normalization
term under these hypotheses stops this kernel application. Success
would still leave numerical heat constants, inverse multipliers,
coefficient-amplified data errors, separator margin/runtime, uncapped
variation and Xi transfer unpaid. Acceleration and dictionary optimization
are outside scope. Assessment1769 records the new mathematical target
and awaits separate approval before mathematics.

## Search, duplicates, access limits and decision

Queries actually issued: `Gaver functionals Laplace inversion finite
signed measure local Lipschitz error kernel tail`; `Gaver 1966 approximate
transform inversion kernel equation 13 26 convergence`; `Gaver "signed
measures" inversion`; `Gaver inversion "Lipschitz" error`; `Abate Whitt
1992 numerical inversion Laplace transforms probability section 8 pdf`.
The bounded search did not find an exact signed-family theorem; that
is not a novelty claim. Primary formulas were inspected as above.

Optional lead: Deniskin-Poloni, *Error analysis of Abate-Whitt methods
for Inverse Laplace Transforms and a new algorithm for queuing theory
applications*, [2510.14799v1](https://arxiv.org/html/2510.14799v1),
16 October2025. Only abstract/introduction was exposed; theorem/proof
retrieval timed out. Its rational-approximation method is an unread
theorem-level lead, not coverage or evidence of nonapplicability.
Optional Abate-Whitt1992 Section8 also timed out. Neither is essential
to the selected unaccelerated attempt. Hofert's copula formulas were
visible but are not imported. Do not repeat access attempts to these
optional leads as essential-source recovery.

Scoped searches of November19 density/signed reviews found the existing
nomination/unpaid interface, not a completed signed Gaver bound. Read
stops1571/1576 in full; coarse robust boxes and literal common-disk
costs are not retried. Audit-loop closure1768 remains in force.
No lemma, mathematical script, DAG or PROOF edit: the argument is unchanged.

Decision SPECIALIZE: source ingredients are covered; the exact signed/
atomic uniform estimate remains mathematical work. Outcome EXPLORATION,
classification NOVELTY_UNCHECKED: completed comparison, no new bound or
claimed progress beyond the checked literature. Full matching Mathlib
coverage remains unchecked/unknown. Creative priority was considered;
there is no new independent central signed-height/Xi input beyond the
parked mechanisms in closure1768. This specialization is not creative.
