# Entire reciprocal finite-factor source comparison1689

Completed 19 November 2026. This is a source review, not a mathematical
construction. The saved target is nomination1688's exact TARGET.
The main gap is L030-L032/C032a actual-Xi positivity; C028g's S_F=0
remains unpaid. The intended intermediate use is to test whether the
entire order-1/2 and coefficient assumptions rescue the generic bridge
already refuted by C028m without those assumptions.

## Reuse and duplicate/failure screen

Reused source-notes1685, approved assessment1686 and stop1686 for the
half-stable result's exact scope. Read C028g's hypotheses and relevant
source interface and C028m's statement and beginning of its method;
the completed audit is not repeated. Narrow filename/content searches
covered PF, reciprocal, self-decomposable, stable, Schoenberg,
complex-pole and conjugate-perturbation assessments/attempts. The
relevant additional matches were review1247 in the finite-reference
atom-budget1246 file and the 31 October strict-PF256 polynomial-transfer
assessment. Read their target, comparison and source-scope passages.

The atom-budget question concerns actual-Xi divided by a fixed finite
reference and a signed-measure unit budget. It is not the present
countermodel construction. The October diagnostic assumes finite-order
global strict PF for a bilateral rational kernel; it supplies neither
the one-sided entire order-1/2 example nor its self-decomposability.
L837/L838/L840 and C466a have the statement/method coverage recorded in
source-notes1685. No new reading of those unchanged proofs is needed.
No matching completed combined construction was found in these paths;
this is not a claim of originality or an exhaustive archive search.
No sibling notebook or cross-notebook mathematical input was used.

## Primary statements and essential proof cases inspected

**Sra.** Suvrit Sra, *On some positivity properties of the Riemann Xi
function*, arXiv:2611.02944v1, 2 November 2026, 53-page manuscript,
[accessible manuscript](https://arxiv.cnoctave.top/pdf/2611.02944).
Printed pages are used below. This is the same version already
identified in source-notes1685, not an inferred identification with
another author-hosted version.

New relevant reading: Lemma C.17 and its entire proof, pp38-39,
including (C.49), positivity before the remaining convolutions,+boundary regularity, normalized determinants at zero, compact
continuity and the pole-obstruction conclusion. For each m>=2 and
finite L>0 it produces a positive density with a C^(2m-2) zero
extension, strictness on the finite support window in (C.48), and
failure of global PF_m. Its transform is rational with m-1 slow real
rates, one pair A+/-ib and m-1 faster real rates. The proof's
three-factor positivity block assumes only 0<q_1<A and b>0; the
smallness of b is used later for the finite-window determinant signs.
The full lemma's choice of law depends on m and L. It does not
assert self-decomposability or one C-infinity law working for all m.

Reused C.1/C.16 coverage (pp20,37-38) from source-notes1685, and read
Proposition C.25's full proof pp44-45 at the changed scope. Its
statement concerns the actual Xi density. The load-bearing cases
are the complex-half-plane expansion, positive variance and coverage
of a whole interval by the tilted mean, all-frequency Fourier
domination with every fixed polynomial weight, Gaussian derivative
limits, the signed Gaussian Gram determinant, and tilt/scale
congruences. Those are the proof tools for a later specialization;
C.25 itself cannot simply be invoked for an arbitrary perturbed law.
Finite sampling or weak Gaussian convergence would miss essential
steps. The derivative limit must hold through 2m-2 for arbitrary
fixed m for the same law, followed by the interval criterion.

The Section2.3/Proposition2.3 pp5-6 complex Frullani and absolute
summation cases and AppendixB.4's complete density proof p19 were
also inspected/reused. They explain which convergence and gamma
extraction checks a new spectral construction must pay. The actual-Xi
zero-count and verified-height hypotheses are not imported for a
different function. No general preservation theorem is asserted.

**Schoenberg interface.** Alexander Belton, Dominique Guillot,
Apoorva Khare and Mihai Putinar, *Hirschman-Widder densities*,
[arXiv:2101.02129v2](https://arxiv.org/pdf/2101.02129v2), 9 April
2022, Definition1.1 and Theorem1.2, pp1-2. Reused the characterization
already assessed in1685 and read its entire smoothness clause:
for a one-sided PF function supported in [0,infinity), its reciprocal
has the form C exp(delta s) product(1+alpha_j s), C>0, delta>=0,
alpha_j>=0, 0<sum alpha_j<infinity. Conversely this product gives
such a PF function. It is positive beyond delta and smooth precisely
when infinitely many alpha_j are nonzero. Normalization and the
transform strip must be checked. This covers the proposed infinite
real-zero base once its product hypotheses are verified. It also
supplies a rigorous global-PF obstruction once the SAME proposed
positive law and its reciprocal have been established. A pole alone
does not establish that law. The original 1951 proof's access limit
from1685 is not an essential blocker; no new access claim is made.

**Self-decomposability.** Thomas Simon, *Positive stable densities
and the bell-shape*, [arXiv:1302.0956v1](https://arxiv.org/pdf/1302.0956v1),
5 February2013, Section3.2 pp9-10, was inspected at the general
spectral criterion already covered in1685. A positive law has this
property when its Laplace transform is exp(-gamma_0 s-
integral (1-exp(-st)) k(t)dt/t), gamma_0>=0 and k nonnegative
nonincreasing, with a finite defining integral. It is the monotonicity
of k, not just positivity of k/t or Taylor coefficients, that matters.
Simon records the smooth-flat conclusion for k(0+)=infinity with
references to Sato Theorem28.4(ii) and a further endpoint lemma.
No bell-shape conjecture is imported. For this prospective test,
smoothness/positivity can instead use the preceding real-product
theorem and a positive convolution block; Simon's endpoint statement
need not be relied on without its own applicability check.

**Elementary analytic inputs.** NIST DLMF, version1.2.8, release
15 September2026, [4.28.2](https://dlmf.nist.gov/4.28#E2),
[4.33.2](https://dlmf.nist.gov/4.33#E2),
[4.36.2](https://dlmf.nist.gov/4.36#E2), inspected in full at those
formulas: exponential definition, entire Maclaurin series and
infinite product for cosh. Their use with the even entire series
cosh(sqrt(s)) requires no branch at zero. A later proof must still
check exact order, coefficient positivity, convergence of the
product parameters, and complex bounds for the new reciprocal.

**Stronger-looking but insufficient general inverse theorem.** Andrew
Bakan and Stephan Ruscheweyh, *On the Existence of Generalized Polya
Frequency Functions Corresponding to Entire Functions with Zeros in
Angular Sectors*, Complex Variables47(7) (2002),565-576,
[DOI](https://doi.org/10.1080/02781070290016232),
[accessible primary text mirror](https://www.academia.edu/18815669/On_the_Existence_of_Generalized_Polya_Frequency_Functions_Corresponding_to_Entire_Functions_with_Zeros_in_Angular_Sectors).
Read the class definitions pp565-567, Theorem1 pp567-568 and
Lemma1/product-bound proof cases pp569-571. Its one-sided theorem
assumes a real entire product exp(bs) product(1+s/alpha_k), b>=0,
rates in |arg alpha_k|<=pi/4, and 0<sum 1/|alpha_k|<infinity,
excluding the pure exponential. It gives a continuous inverse
transform with a specified strip and endpoint behavior. The
statement does not say that this inverse is nonnegative. It gives
neither the required self-decomposability nor the all-fixed-order
local minors. Thus its terminology "generalized PF" cannot be
substituted for the requested positivity. The paper's sharpness
counterexamples do not cover the combined target. The displayed
mirror has a full-text OCR; only these stated ranges are claimed
read. PDF screenshots of Sra pp38-39 timed out; the complete text
proof was accessible. No essential statement is source-blocked.

## Search scope and comparison

Queries actually issued included `self decomposable distribution
rational Laplace transform complex poles spectral function`,
`Polya frequency density finite perturbation reciprocal entire
function self decomposable`, exact self-decomposable with complex
poles, `self-decomposable reciprocal entire nonreal`,
`finite perturbation local Polya frequency`, cosh/sqrt with
Laplace/exit-time and total positivity, and the exact title of
Bakan-Ruscheweyh. Brownian exit-time and special-function law results
were returned as leads, but are not needed or imported. No inspected
source supplied the full single-law combined countermodel, or an
impossibility theorem for it. This bounded comparison establishes
neither novelty nor absence from the literature.

## One bounded continuation; no construction proved

Nominate the single prospective object

    F_*(s)=((1+s)((s+2)^2+1)/5) cosh(sqrt(s)).

The expression after cosh denotes its entire even series. The
finite factor is selected from C.17's three-factor block with
q_1=1,A=2,b=1, not selected by a numerical sweep. The source inputs
are adequate for an established-method SPECIALIZE attempt, rather
than an IMPORT of the full conclusion. A new reproof of Schoenberg,
general self-decomposable theory or the Wronskian criterion is
unnecessary. What requires a proof is this changed specialization:
the same-law spectral monotonicity, exact analytic hypotheses and
fixed-order boundary determinant limits for this one finite factor.
In particular its changed cosh growth is not C.25's Xi asymptotic.

The test must establish a single positive smooth probability density
on the positive half-line, smooth zero extension, Laplace transform
1/F_* for s>=0, self-decomposability, F_*(0)=1, exact order1/2,
strictly positive Taylor coefficients, and the local minor assertion
for every fixed m on some (0,epsilon_m), independently of the choice
of law. For the local step pay polynomially weighted Fourier
domination (or an equally rigorous complete analytic derivative
argument), all required cancellations, both Wronskians and full
interval coverage. For global failure apply the characterized
reciprocal only after the law and transform have been identified;
do not presume a negative minor of size two.

Continue only if all these obligations hold for this fixed object.
Any failed obligation rejects this object, not the generic enriched
implication. Do not silently tune the factor or change the all-m
quantifier. Unfinished rigorous work may be preserved, but success
must await a later critical audit. No assertion about actual Xi,
global log-concavity, arithmetic identities or S_F=0 follows.
The independently open Xi realization/sign mechanism remains the
central research bottleneck. This specialization is not relabeled
creative to fill a scheduling target. Matching Mathlib coverage is
unchecked.

Outcome: EXPLORATION, useful complete source comparison and one
independently testable continuation, with no proved countermodel or
advance beyond the sources checked. Nomination1688 is SPECIALIZE;
the newly written continuation assessment1689 needs a separate
supervisor approval next turn before mathematical invocation.
