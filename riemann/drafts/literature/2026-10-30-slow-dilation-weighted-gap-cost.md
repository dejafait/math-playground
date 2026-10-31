# Slow dilation: a bounded weighted gap-cost test

TARGET: Calculate whether the slow-dilation family f(z)=p(z)e(z/D), D>=max(1,B), satisfies |Q_a(f)|<=C_R a M(f)/B uniformly in T, polynomial degree and coefficients.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed 2026-10-30-genuine-positive-class-runge-flux-test.md review: fixed-bandwidth approximation, superoscillation norm costs, exact weighted-L1 and quantitative Runge searches; compare L504 definitions and the narrowly inspected existing K-weight conversion in L503. No originality is asserted.
SOURCE_EVIDENCE: Chremmos--Fikioris, Superoscillations with arbitrary polynomial shape, https://arxiv.org/pdf/1504.04822v1, Section II (2)--(4), printed pp. 4--5 and Section V p. 8, directly rechecked 2026-10-30; standard named Fourier inversion theorem for Schwartz functions is already an input of L504. Version qualifications below and in the parent assessment.
COMPARISON: The source covers polynomial multiplication of a sufficiently smooth bandlimited envelope and dilation, including a C-infinity bump option. The remaining work is a routine quantitative Fourier estimate with the notebook's K weight and D>=B, uniform over all finite polynomial degrees; no complex approximation theorem or positivity implication is assumed.
GAP: Establish or refute the stated uniform O_R(a M/B) bound for this restricted family, treating the zero of K and the actual Fourier bandwidth. This is an unproved target, not an imported inequality and not the full H_a conjecture.
REASON: An explicit source family permits an independently testable norm calculation without unresolved approximation coverage. Replaying the elementary K-weight conversion is justified to keep the new calculation independent of the unaudited remainder of L503.
SCOPE: One calculation from cited Fourier-support facts and Fourier inversion; REPRODUCTION if successful. No general Runge claim, H_a nonemptiness, actual-Xi application, arbitrary-measure optimization or new creative mechanism. Separate literature approval completed 2026-10-30 for this unchanged target; the calculation remains unperformed.

## Exact family and threshold, all still to be tested

Use L504's definitions of R>0, L=log T, a=log L/pi, b=a/4,
B=L/(4pi), lambda=pi/(2a), K(0)=0 and

    K(x)=1-(sin(pi x)/(pi x))^2,
    M(f)=integral_R |f(x)|K(x)dx,
    Q_a(f)=-integral_0^b exp(-lambda y)
                      [Re f(a+iy)+Re f(-a+iy)]dy.

Fix an even entire envelope e, real on R, with e(0)=1 and smooth
compact Fourier data supported in [-R,R] in the exp(2pi i v z)
convention. Let p range over all even real polynomials of finite degree,
with no uniform bound on degree or coefficients, and let

    f(z)=p(z)e(z/D),   D>=max(1,B).

Allow p and D to vary with T. The desired constant C_R is independent
of T, D, polynomial degree and coefficients; aim also for independence
of the chosen envelope within this class. There is no uniform Fourier-
derivative bound. The proposed inequality is

    |Q_a(f)| <= C_R a M(f)/B

for every sufficiently large real T. This display is a research target,
not a mathematical conclusion of the source review. The stronger
absolute bound is deliberately tested on the whole explicit family;
a member satisfying H_a would then be included. H_a membership itself
is neither assumed for the calculation nor asserted to be possible.

The source statements about multiplication/dilation must be translated
with the correct angular-versus-2pi normalization and global spectral
smoothness before using a Fourier estimate. Check integrability and the
weight-zero conversion explicitly; no source L2 estimate controls M by
itself. Use the ambient fixed R for any constants that must remain
uniform as D grows. These are proof obligations, not completed steps.
The prior K conversion is overlap, not a new discovery; no L503 detector
conclusion or first-mode identity is an input. L504 supplies definitions;
standard Fourier inversion and the cited source supply the analytic inputs.
Full Mathlib coverage is unchecked.

## Why this test and its limits

The main gap is actual-Xi all-degree positivity and initial signs at
unbounded height. A genuine H_a family with unbounded positive Q_a/(a M)
would refute one proposed geometric estimate on the detector route;
independent realization, signs and height-transfer gaps would survive.
The parent review found no source that establishes such a family.

The present test instead isolates a quantitatively specified use of the
known polynomial-envelope construction. D>=B is an explicit design choice
for this slow-dilation test, not a consequence of admissibility or a
necessary condition for any complex-domain approximation. No conclusion
about faster-dilated, modulated, summed, or other full-bandwidth families
is licensed. Qualitative Runge remains parked on its recorded evidence.

Continue this specific construction only if the calculation defeats the
proposed bound with complete weighted-norm evidence; even then, distinguish
failure of O(1/B) from the much stronger unbounded positive ratio and
supply positivity separately. If the bound holds, stop the slow-dilation
family as a route to that ratio and retain its exact scope without
creating a lemma merely to record a routine specialization. If the test
is inconclusive after one attempt, save the precise residual and reassess;
do not repeat qualitative approximation or reopen L504/L505's full-space
certificate families. No new mathematics is derived in this nomination.

## Separate source-gate approval, 2026-10-30

LITERATURE_REASON: Supervisor recovery identified a missing direct source URL
in this ready assessment. This turn repairs that omission and checks the
exact cited construction; it does not repeat the broader discovery search.

Primary artifact: [Chremmos--Fikioris v1 PDF](https://arxiv.org/pdf/1504.04822v1).
The arXiv footer identifies v1, 19 April 2015; the retrieved title page
says 6 July 2021. Read Section II (2)--(4), printed pp. 4--5,
and Section V, printed p. 8. Section II assumes a real finite-degree
polynomial and an envelope in PW_pi with globally C^(N-1) spectrum
and Nth derivative of bounded variation. Its Fourier-differentiation
argument preserves spectral support; dilation by D>=1 narrows it.
Section V explicitly permits compactly supported smooth bump spectra
for arbitrary finite degree. The source uses angular frequency.

Applicability review: the nominated smooth compact spectral data are
stronger than the source's degree-dependent regularity assumptions.
Evenness is an additional restriction of the test family. The source's
real-interval approximation does not give complex positivity, a uniform
weighted-L1 inequality, or degree-uniform constants. No such conclusion
is imported. Fourier normalization, integrability, K's zero and the
claimed uniform bound remain obligations of the saved calculation.

The parent assessment's duplicate/obstruction comparisons were reused;
L504's hypotheses and definitions were checked narrowly. L504/L505's
full-space certificate stops do not decide this restricted family.
No new lemma, bound, mathematical script or Mathlib claim was produced.
Full Mathlib coverage remains unchecked. SPECIALIZE is approved for
the exact TARGET, with REPRODUCTION classification if successful.
This repair provides no mathematical evidence and does not reset the
mathematical exploration count.
