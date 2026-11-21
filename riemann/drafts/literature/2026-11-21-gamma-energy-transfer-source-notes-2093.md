# Gamma energy transfer: source comparison2093

Literature-only completion of review2092's unchanged target. No new
estimate, specialization proof, numerical certificate or canonical
theorem import is made. The source assertions below remain to be
independently audited. Main gap: L030-L032/C032a actual-Xi all-degree
algebraic mixed positivity. A successful later audit could discharge
C034u's separate energy-interface premise; both signed uppers and
cumulative-energy control would still be unpaid.

## Primary sources and reading boundaries

Leonard van Hemert, *Exact Zero Detection and Compact Arithmetic
Realizations for the Riemann Xi Function*, v1.0.0, 11 October2026,
DOI10.5281/zenodo.23295277,
[tagged primary TeX](https://raw.githubusercontent.com/LeonardSEO/riemann-xi-zero-detection/refs/tags/v1.0.0/paper/paper.tex),
subsection `sec:integer-gamma-completion`, theorem
`thm:joint-integer-gamma-completion`. Read the entire setup, statement
and proof, lines11382-11600, GC1-GC11. Also inspected the following
projected/measurability discussion, lines11601-11612, solely to mark
its scope; no cumulative claim is approved here. Reuse source-notes2090
for the primitive-remainder comparison. Web retrieval worked; the
shell download failed DNS resolution, which is not a source blocker.

Ethan Simpson Lee and Nicol Leong, *New explicit bounds for Mertens
function and the reciprocal of the Riemann zeta function*,
[arXiv2208.06141v5](https://arxiv.org/html/2208.06141v5),
9 September2026. Reused2090 and reread Theorem2.2(18)-(23), the complete
third block of Table1 and its row-matching qualifications. Read (1)-(3)
for the constants and Section5.4, the complete parameter-substitution
case proving(23). The common Proposition5.2/Lemma5.3 argument and the
computational certificates were not replayed: Theorem2.2 is a cited
external input, not a theorem to be reproved in the later gamma audit.

## Exact scope of the manuscript assertion

Use q=2, Q=log2, E, translations, full theta convolution and the fixed
compact smooth h of C034r. GC2 uses the strict/inclusive window
X/2<d<=X, with nu_0(d)=mu(d), nu_1(d)=mu(d)log(X/d). Its centered
floor fields take their after-jump values at integers. GC3 retains
every k<=M and every divisor column, including prime powers. The
completed operator is G minus its displayed boundary operator, not
the finite head alone.

GC4 specifies the least integer minimizer of
|Dtilde_0(k)|^2+Q^(-2)|Dtilde_1(k)|^2 on T<=k<2T, for integer
T>=ceil(X), X>=2. The same cap serves j=0,1 and all h in E. GC5 claims
operator error at most
C_q[X^(1/4)T^(-1/4)+X^(5/4)T^(-3/4)]. GC6 claims, at T=ceil(X^3),
the absolute energy error at most
C_q[exp(-c_mu f_0(log X))+X^(-1)]||h||_E^2 eventually, where
f_0(L)=L^(3/5)(log L)^(-1/5). These are already stated source results,
not conclusions established by this review.

C034r supplies the actual input and the bounded theta convolution and
its first derivative, with the weighted-translation convention checked
in its proof section2. C034u assumes the GC6 interface rather than
proving it. Its primitive remainder is not an input to GC5/GC6. No
sector-sign, RH, rightmost-zero or zero-separation premise occurs in
the cited gamma theorem. The pole-moment clause and growing-input
clause of that theorem are not needed for the saved fixed-input energy
target; neither is an extra hypothesis of its GC5/GC6 inequalities.

## Mertens input: exact admissibility

Fix one third-block row throughout, for example W=54, R_3=5223 and
the corresponding exact x_3(54) of Theorem2.2. Table1 records
loglog x_3(54)=10.01 and c_3(x_3(54))=22.19. These are reported table
entries, not independently verified rounding certificates. Do not
replace the exact theorem threshold by an independently asserted
decimal cutoff. Section5.4 explicitly permits W in
{53.99,54,55,60,70}; equation(3) has Z_3=53.989. Rows of different
blocks may not be mixed. The prefactor is the c_3 of(20), with
the paper's H=3000175332800 from(1), and is bounded as specified in
Theorem2.2 for x>=x_3(W).

For those hypotheses the external theorem states

\[
 |M(x)|<c_3(x,W,R_3)x\log x\,
 \exp\!\left[-\left\{\frac5{3W^3}
 (1-\log W/\log\log x)^{-1}\right\}^{1/5}
 \frac{(\log x)^{3/5}}{(\log\log x)^{1/5}}\right],
 \qquad x\ge x_3(W).
\]

The later audit must justify the manuscript's reduction of this bound
to a fixed positive exponential constant, absorb its logarithmic
prefactor, and choose a common eventual X-threshold so the entire
[X/2,X] interval is above the external threshold. No explicit onset
or numerical value of c_mu is being certified. The finite-height
zero verification is part of the external theorem's unconditional
input; it is not an assumption of global RH.

## Essential proof cases for the later audit

The following table records inspected source coverage and outstanding
audit obligations, not newly derived assertions.

| Component | Primary locator | What the audit must check |
| --- | --- | --- |
| Coprime mu/n sums | GC7, lines11457-11479 | Finite floor identity; Y<1 and empty windows; squarefree r and the logarithmic Abel endpoints. Preserve the r-dependence and both j values. |
| Periodic variance | GC8, lines11480-11495 | Sawtooth covariance and Jordan-divisor identity, reduced frequencies and their X^(-2) spacing; a Fourier series value at a jump is not an endpoint value. |
| Interval mean square | GC9, lines11496-11512 | The enlarged interval majorant, Fourier support and truncation-to-L2 passage with the stated uniform constants; no pointwise convergence at jumps. |
| Simultaneous integer cap | GC10, lines11513-11528 | After-jump right unit intervals, slope kappa_j, T sampled integers, weighted joint minimization and the least-minimizer convention, including T=ceil(X). |
| Gamma operator identity | GC1/GC3/GC11, lines11387-11423 and11530-11569 | Weighted L1 bounds for A_Gamma, B_Gamma and required derivatives at both real ends; theta regrouping on compact inputs; exact moving boundary and sign; cancellation of m_j/2; absolute E-valued centered remainder and density extension. |
| Vector Abel step | lines11570-11587; C034r section2 | Operator differentiability after convolution, both real window endpoints and their integer cases, a uniform Mertens bound on [X/2,X], and a constant independent of h and X. No derivative of an arbitrary E-input may be assumed. |
| Absolute energy | GC5/GC6, lines11588-11594 | Substitute the integer T=ceil(X^3) into both terms of GC5 and use the separately paid source norm. Retain the full completed-vector boundary cross term. |

In particular the source explicitly treats the mean tail integral as
a pointwise calculation on compact inputs, not as an absolutely
convergent E-valued mean integral. Its subsequent centered remainder
is the proposed E-valued object. The distinction is essential to the
audit; reading the formula does not validate that passage.

Continue only if the later audit reproduces GC5 with the single
input-independent cap and then GC6 at the saved fixed input, uniformly
for all sufficiently large real X, retaining every endpoint and the
boundary cross term. Otherwise identify the first exact failed
inequality or unproved hypothesis, preserve any surviving restricted
statement and park that failed specialization. A bound requiring
arithmetic signs, a stronger Mertens estimate or an input-dependent
cap would fail this test. The saved target concerns no growing inputs,
integrated lower-bound transfer, signed upper or Xi mixed signs.

## Duplicates, failures and decision

Searched C034 lemma files and the November21 target-specific literature,
histories and attempts for GC5/GC6, cap, vector Abel and Mertens inputs.
C034r already pays the actual theta and derivative setup; C034u's
section5 leaves GC6 conditional. No canonical local cap/operator audit
was found in this bounded check. Reused2090's precise source comparison
and stop2089's analytic-boundary obstruction; the latter concerns a
different signed-upper mechanism, not the finite gamma transfer.
Stops2076/2077/2079/2084/2087 remain intact. No cross-notebook read.

Discovery queries included `"Joint integer caps and absolute energy transfer"`,
`"completed gamma" "energy" "Mertens"`,
`"Möbius" "sawtooth" "mean square" gamma`,
`"Mertens function" "Banach" "summation"`, and
`"riemann-xi-zero-detection" "gamma" "erratum"`.
They produced no inspected independent matching transfer theorem or
correction. The source repository describes the same cap result.
Other sawtooth/Nyman-Beurling search results and the margin preprints
were not inspected and are not premises or substitutes for GC5/GC6.
A failed search establishes no novelty. No general sawtooth or gcd
theorem is imported from those snippets.

Decision SPECIALIZE: full essential source coverage is now available
for one separate REPRODUCTION audit of the unchanged target. A direct
citation locates the existing assertion but would not independently
check the compressed operator/endpoint argument in this unaudited
manuscript. Reproduction is justified for that verification purpose,
not as a claim of stronger or original mathematics. No creative
mechanism is proposed. Full matching Mathlib coverage is unchecked;
supporting named inputs are Young's inequality, Parseval, elementary
finite Abel summation, Cauchy-Schwarz and density. No full Mathlib
match or absence is asserted. No mathematical exploration turn is
spent, and no scheduler state is changed.
