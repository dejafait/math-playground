# Signed Mellin–Euler sampling: literature assessment

TARGET: Test D_N^w=o(1) at the prescribed pairs (2n,a_n) by retaining the signs and n-dependence of b_(2n)^w inside the Mellin–Euler integrals.
CHECKED: 2026-09-27
DECISION: EXPLORE
SEARCH_EVIDENCE: Searches on 2026-09-27 for discrete mollified moments, zeta-ratio means, nonlinear/exponential sampling, and joint universality found adjacent results but no theorem covering the exact moving ratios and prescribed samples; queries and theorem-level comparisons are recorded below.
SOURCE_EVIDENCE: Li–Radziwiłł, arXiv:1208.2684v1, Theorem 3 p. 2, Proposition 1 p. 5 and §3 Lemma 1 pp. 8–10, https://arxiv.org/pdf/1208.2684v1; Lee–Sourmelidis–Steuding–Suriajaya, arXiv:1710.11367v2, (9) and Lemmas 7–8 pp. 9–10, https://arxiv.org/pdf/1710.11367v2; Nakai, arXiv:2312.04269v2, Theorem 1.2 p. 2 and Lemmas 3.1–3.2 pp. 4–5, https://arxiv.org/pdf/2312.04269v2; further inspected ratio and universality statements below.
COMPARISON: Signed mollification has a proved discrete analogue for arithmetic progressions, while the checked exponential-shift results average a continuous parameter. Neither supplies the joint sampled moment with σ_n=1+(2n)^(-1/2), moving shifts and complex kernels. L352 and the narrower-normalization L344–L345 concern failed certificates, not a lower bound for D_N^w.
GAP: Control the complete signed sampled squared Mellin–Euler expressions with r=2n and a_n=sqrt(4π²exp(8n)−25) by o(1), including the moving coefficients, every equal-ratio collision and uniform tails; no inspected result supplies this estimate.
REASON: The source comparison is complete enough for one bounded test of whether signed Möbius cancellation survives in the exact sampled integrals. Preserve the target, reuse covered statements by citation, and test the full normalized error before continuing; this review proves no estimate and does not establish originality.

## Scope, gap and downstream use

This completes the source-only assessment requested by the initial
REVIEW_REQUIRED gate. The exact TARGET is unchanged. The shared/local
goals, checkpoint, full overview, DAG, relevant obstruction statements,
and L349–L350's definitions were read. Existing tracked and untracked
work, including L352 and its script, is preserved. No new identity,
estimate or specialization is derived in this turn.

The main gap remains global mixed reciprocal-zero positivity. The
intermediate gap here is deterministic sampling in the endpoint branch.
Using exactly L349–L350's notation, the proposed target is

\[
D_N^w=\frac1N\sum_{n=N}^{2N-1}|R_{2n}^w(a_n)|^2=o(1),\qquad
R_r^w(a)=\frac{S_r(a)}{|\zeta(1+r^{-1/2}+ia)|^2}-1.
\]

L350 (4) already represents 1+R_r^w(a) as the integral of
k_r(t)Q_r(t;a)Q_r(t;−a). Both ratios use the same scaled shift
r^(-1/2)t; their product is not a modulus square, and k_r is complex.
The saved test keeps those features and the common index n through
the squared sampled expression. Merely restating that identity is
not a mathematical advance.

Existing achieved scales are the fixed-r long-height mean square
C_w/r+O(r^(-3/2)) in L349 and the O(1/N) local dilation average in
L351. Neither is the discrete mean at dilation exactly one. L352's
specified grid-transfer budget tends to one, against its sufficient
fourth-moment threshold o(N^(-1/2)); that auxiliary threshold is not
the present direct target o(1). No actual sampled bound is achieved here.

Even D_N^w=o(1) would leave exceptional sampled indices. The endpoint
assembly needs a positive margin exceeding (1+2n)²exp(−2n/256),
and the global low-index Laguerre signs also remain unresolved. The
plausible use is therefore average control of endpoint relative errors,
followed by a separate exceptional-index argument. It would not by
itself prove the required endpoint signs or RH.

## Search record

Queries included the following exact strings:

- `Riemann zeta discrete moments exponential sequence lacunary ratios`
- `zeta function mollified moments discrete nonlinear sequences sampling exponential`
- `"zeta" "discrete" "mollified" moments Li Radziwill`
- `"discrete second moment" "Li" "Radziwill"`
- `"Riemann zeta" "geometric progression"`
- `"zeta" "discrete" "exponential shifts"`
- `"ratios of the Riemann zeta" "mean"`
- `Riemann zeta discrete universality nonlinear shifts general sequence mean square`
- `"Notes on universality in short intervals and exponential shifts"`

The last query followed Nakai's reference [1]. The continuous/discrete
equivalence lead was followed to Andersson's stronger unconditional
statement, rather than treating an earlier conditional result as the
end of that search. Search summaries, secondary pages and numerical
claims were not used as mathematical evidence. This was a bounded
search for coverage, not an exhaustive novelty investigation.

## Inspected primary statements

### Discrete signed mollification

Li and Radziwiłł, *The Riemann zeta function on vertical arithmetic
progressions*, [v1, 13 August 2012](https://arxiv.org/pdf/1208.2684v1#page=2):
Theorem 3 compares the smoothly weighted discrete and continuous
second moments of ζM_θ on 1/2+i(αℓ+β), for fixed α>0, β real and
0<θ<1/2, with error O(T(log T)^(-1+ε)). Here
M_θ(s)=Σ_(m≤T^θ)μ(m)m^(-s)(1−log m/log(T^θ)).
Proposition 1 (PDF p. 5) and §3's first Lemma 1 (PDF pp. 8–10)
were inspected, including the Euler factorization and contour argument.
For coprime A,B with AB>1, that lemma bounds its particular correlation
F(A,B,t) by (AB)^ε T(log T)^(-1+ε). A Möbius Euler factor vanishes
at the contour residue when A>1.

Applicability inference: this suggests a cancellation to test, but its
correlation, fixed mollifier and arithmetic-progression sampling differ
from this target. Its T controls both sample count and height; here
N samples extend to heights of order exp(8N). No source bound is imported
for the moving b_(2n)^w.

### Discrete approximation with general separated samples

Lee, Sourmelidis, Steuding and Suriajaya, *The Values of the Riemann
Zeta-Function on Discrete Sets*, [v2, 13 December 2018, §3, PDF
pp. 9–10](https://arxiv.org/pdf/1710.11367v2#page=9): equation (9) gives
mean-square approximation by finite Euler products for increasing
nonnegative x_n with x_n=O(n) and x_(n+1)−x_n=Ω(1), uniformly on
fixed compact subsets of 1/2<Re s<1. Lemma 7 states its density
consequence. Lemma 8 additionally assumes joint uniform distribution
of the finite prime-phase vectors.

The exponential a_n fails the linear-growth hypothesis. The moving
line above one is outside that compact-strip statement, and prime-phase
equidistribution is a premise, not a conclusion for arbitrary samples.
Separation alone therefore does not authorize this transfer.

### Exponential shifts and the continuous/discrete distinction

Nakai, *Joint Universality for the Riemann zeta-function with general
shifts*, [v2, 17 November 2024, Theorem 1.2, PDF
p. 2](https://arxiv.org/pdf/2312.04269v2#page=2), permits admissible
increasing shifts, including exponential examples. It asserts positive
Lebesgue density of approximation parameters τ∈[T,2T], on fixed compact
sets inside 1/2<Re s<1. Conditions (F1)–(F3), admissibility and
Lemmas 3.1–3.2 (PDF pp. 4–5) were inspected. The mean-square mechanism
uses oscillatory integrals in τ. This is not a count over integer τ,
nor a moment theorem for the present moving ratios.

The referenced Andersson et al., *Notes on Universality in Short
Intervals and Exponential Shifts*, [v2, 8 December 2023, §5, Theorem 5,
PDF pp. 11–12](https://arxiv.org/pdf/2312.04255v2#page=11), likewise
uses Lebesgue measure for exponential shifts in its class Φ. Its
change-of-variables argument does not select the prescribed integers.
The definitions of Φ and the theorem were read; its separate
short-interval improvements are not inputs here.

Johan Andersson, *Discrete universality, continuous universality and
hybrid universality are equivalent*, [v1, 5 October 2023, Definitions
1–4 and Theorem 1, PDF pp. 2–4](https://arxiv.org/pdf/2310.03619v1#page=2),
proves an unconditional equivalence, but the discrete shifts are nα
for fixed α. Thus even this stronger transfer does not assert a
nonlinear sampling result. The earlier Sourmelidis [August 2023
preprint, Theorems 1.2–1.3, PDF pp. 3–4](https://arxiv.org/pdf/2308.07031#page=3)
was also inspected; its RH-dependent equivalence is not used as a
premise or presented as the strongest available theorem.

### Proved and conjectural ratio moments

Daodao Yang, *Mean values of ratios of the Riemann zeta function*,
[v2, 29 May 2024, Theorem 1, PDF pp. 1–2](https://arxiv.org/pdf/2307.08091v2#page=1),
proves, for fixed integer a≥1 and B>0, a continuous second-moment
formula for ζ(1/2+it)/ζ(1+iat) on [T,2T], with main terms
D_1(a)T log T+D_0(a)T and error O_(a,B)(T(log T)^(-B)).
This is an unconditional ratio result, but has different real parts,
height coupling and averaging measure. It supplies no discrete or
moving-parameter estimate for Q_r.

Conrey and Snaith, *Applications of the L-functions ratios conjectures*,
[author manuscript, Conjecture 2.1, (2.10)–(2.11), PDF
p. 6](https://people.maths.bris.ac.uk/~mancs/papers/new_ratiosI.pdf#page=6),
gives the familiar two-over-two shifted-zeta average as a conjecture.
The inspected formula is a continuous t-integral based at
s=1/2+it, with specified shift ranges; Theorem 2.5 explicitly
assumes that conjecture. Neither its status nor its sampling domain
allows it to be used as an unconditional answer here. The manuscript
is identified by its author-hosted URL and inspected equation numbers;
no correspondence to a particular arXiv revision is asserted.

## Reuse, nonredundancy and bounded test

The previous [fourth-moment assessment](2026-09-26-current-target.md)
already sufficiently screens Guth–Maynard's Lemma 11.6 and the metric
real-lacunary result of Tan–Zhou for the unchanged auxiliary mechanism.
That review is reused; those sources were not mechanically reread.
Its Guth–Maynard citation remains
[v2, Lemma 11.6, PDF pp. 41–42](https://arxiv.org/pdf/2405.20552v2#page=41).
L352 has since supplied the negative grid-transfer test. An
almost-everywhere dilation conclusion still does not fix dilation one.

L344–L345 concern the narrower normalization σ=1+1/r. They stop the
specified absolute frequency-by-frequency derivative certificates and
their stationary dual. They do not prove that the present signed mean
is large. L347–L348 also use the earlier normalization; L349 removes
their diverging coefficient-mass obstruction, while leaving nonvanishing
absolute mass. None of these qualifications should be erased when
comparing a proposed new estimate.

The concrete intermediate test within TARGET is whether the nonconstant
reduced-ratio terms, formed while retaining the two Mellin variables and
the same sample index, possess a usable Möbius Euler-factor cancellation
at the relevant contour residues. The external example motivates this
test; its existence and usefulness here are unproved. Do not reprove the
known arithmetic-progression theorem. What needs investigation is the
changed correlation and its actual nonlinear sample dependence.

Continue only if that calculation gives a signed bound whose complete
normalized sum is o(1), or a proved intermediate cancellation with a
specific remaining term and credible route to that scale. Include all
ratio collisions, contour tails and dependence on n throughout. Stop
the implementation if the proposed cancellation is absent, or its
justified estimate returns to the already tested absolute coefficient
or operator-norm budgets without a saving. Merely obtaining a formal
Euler product, a fixed-parameter average, or an unproved
equidistribution assumption does not pass this test. No such
calculation has been performed in this review.

This is EXPLORATION, using one of three consecutive unresolved exploration
turns after L352's informative negative. The assessment now supports a
later bounded research turn. It neither imports nor reproduces the target
theorem. A successful exact-sample estimate would exceed the conclusions
checked here, but no originality or mathematical advance is claimed.
STEP_CLASSIFICATION for this source-only step is NOVELTY_UNCHECKED.

## Access scope and Mathlib

All sources essential to the above comparisons were accessible at the
cited statement locations. Only the stated portions were inspected;
reading a theorem for scope is not an independent verification of its
whole proof. The 2024 Kobayashi arithmetic-progression moment paper and
the Conrey–Keating ratio/divisor-correlation paper appeared as search
leads; their theorem texts were not read and no claims depend on them.
They are not asserted to cover or rule out this target.

Mathlib coverage of the full target: **not checked**. The supporting
references inherited from L349 remain qualified as supporting inputs:
[`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius),
[`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff),
[`riemannZeta_ne_zero_of_one_lt_re`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#riemannZeta_ne_zero_of_one_lt_re), and
[`riemannZeta_eulerProduct_exp_log`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
These links were not rechecked. Their recorded presence supports Euler
and reciprocal products in their domain; it is not full-target coverage.
