# Gaussian-flow route: completed bounded source review

TARGET: Assess a Gaussian-smoothing route to neutral Weil positivity, seeking a sign-propagating differential inequality with the complete infinite prime-power sum and a separately justified starting sign.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact Weil/Gaussian/heat-semigroup and differential-sign searches, followed by primary explicit-formula and heat-kernel passages; local L058-L060/L616-L617 and L740/L744 scope checks and reuse of earlier heat and Suzuki assessments. Queries and exclusions below; failed searches establish neither absence nor novelty.
SOURCE_EVIDENCE: Carneiro-Milinovich 2403.17803v1 Section 2.2 Lemma 4; Hunter PDE notes revised 2014-06-18 Proposition 5.3, Theorem 5.4 and proofs pp.129-130, Theorem 5.27 and proof p.143; Connes-Consani July 4 2021 Appendix C Proposition C.1 and proof p.48; Suzuki 2301.00421v2 Theorems 1.1-1.2; Rodgers-Tao 1801.05914v3 Introduction (4), Theorem 1.1 and Theorem 4.1 with proof.
COMPARISON: The unconditional analytic-strip explicit formula supplies an identity rather than a sign. Ordinary heat contraction is in ordinary L2; Suzuki's norm identification assumes RH; the neutral compact criterion remains RH-equivalent. These statements supply neither backward Weil-sign propagation nor an independent starting sign.
GAP: The Gaussian weighted-domain, exact-neutrality, complete-tail and two-derivative specialization remains to be proved. An independent starting sign and a useful differential comparison remain separate gaps.
REASON: Complete the source question without approving a new sign theorem; nominate one bounded standard domain-and-differentiation specialization using the now-inspected unconditional identity source.
SCOPE: Source comparison only. No unrestricted Gaussian sign research is approved; the single bounded mathematical continuation has a separate SPECIALIZE assessment.
LITERATURE_REASON: The saved target changed from finite-window absorption to full-line test smoothing; essential strip-decay and heat-domain source hypotheses were missing at invocation.

Investigate the proposed f_tau=G_tau*f with the ordinary Gaussian heat
kernel and compact smooth initial f having both moments zero. This
defines a question, not domain membership, preserved neutrality or
positivity. The prospective use is to propagate a separately proved
sign toward the initial test. Neither starting sign nor propagation
inequality is available or assumed.

Search exact neutral-Weil/heat-flow terminology and stronger known
results first. Compare at most three genuinely distinct sign-control
mechanisms and nominate at most one bounded test. Check whether an
inequality merely restates the missing positivity. Keep complex tests,
both moments, the scalar/poles and all prime powers: smoothing loses
compact support, so L744's finite cutoff cannot simply be inherited.
Retrieve primary hypotheses and essential proof cases before new math.
No finite starting sign or generic spectral gap may be inserted.

For local overlap first search the specific heat-flow foundations and
L058-L060/L616-L617 terminology; read only matches needed to distinguish
test-function smoothing from their zero-motion arguments. Preserve the
generic-gap, corrected-localization and fixed-sine stops; do not rename
one of those mechanisms. No cross-notebook input is needed.

A useful review must identify a precise source input, a materially
different independently testable differential estimate or an informative
obstruction. A variational restatement with unpaid starting sign does
not justify a creative invocation. If coverage remains inadequate,
record the limit and continue bounded discovery without repeating the
finite absorption test. Full matching Mathlib coverage is unchecked.

## Completed source comparison, step 325

The original main gap and discriminator above remain unchanged. The
result is a source-supported preliminary identity task, not a sign law.
No new mathematics is established in this literature-only review.

### Primary statements and proof cases inspected

1. E. Carneiro and M. B. Milinovich, *On Littlewood's estimate for the
   modulus of the zeta function on the critical line*,
   [arXiv:2403.17803v1](https://arxiv.org/html/2403.17803v1#S2.SS2),
   Section 2.2, Lemma 4, explicitly unconditional. It assumes h analytic
   on |Im z|<=1/2+epsilon, epsilon>0, with uniform
   O((1+|z|)^(-1-delta)) decay there, delta>0. Its zero sum uses complex
   ordinates (rho-1/2)/i with multiplicities, not presumed real ordinates.
   Both pole evaluations, the gamma integral and the complete von
   Mangoldt sum are retained. The Fourier convention is exp(-2pi i x xi);
   prime arguments are +/-log(n)/(2pi), with coefficient
   -Lambda(n)/(2pi sqrt(n)). Read the whole lemma and its proof attribution
   to Iwaniec--Kowalski, *Analytic Number Theory* (2004), Theorem 5.12.
   That book proof was not independently read. The neighboring Lemma 5
   assumes RH and is excluded. Gaussian-square applicability,
   normalization and differentiated interchanges require a later proof,
   rather than a reproof of the known formula.

2. J. K. Hunter, *Notes on Partial Differential Equations*,
   [revision June 18, 2014](https://www.math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
   Section 5.1.1, Proposition 5.3 and Theorem 5.4, printed pp.129-130
   (PDF pp.135-136). Read their full proofs: Schwartz-seminorm difference
   quotients, Fourier ODE, induction at zero and Gaussian inversion.
   Schwartz data give a C^infinity([0,infinity);S) solution, multiplier
   exp(-t|k|^2), and convolution with
   (4pi t)^(-n/2)exp(-|x|^2/(4t)). The notes first specify real data;
   complex data require separate application to real and imaginary parts.
   Theorem 5.27 and proof, printed p.143, give ordinary L2 contraction;
   the following paragraph explains the failure of a backward L2 map.
   Exponential-weight continuity, neutral moments and the Weil-form sign
   are outside those conclusions.

3. A. Connes and C. Consani, *Weil positivity and Trace formula, the
   archimedean place*,
   [author PDF dated July 4, 2021](https://alainconnes.org/wp-content/uploads/Selecta.pdf),
   Introduction (1)-(4), Appendix C Proposition C.1 and its whole proof,
   printed p.48. For complex smooth compact multiplicative tests, impose
   Mellin vanishings on a finite set disjoint from the nontrivial zeros
   and containing {0,1}. Nonpositivity of their total local-place
   functional on the involutive convolution squares is equivalent to RH.
   The forward proof uses pole vanishings; the converse adds this finite
   set to Yoshida's interpolation construction. Yoshida's original 1992
   proof is an unread reference, not reproduced here. Thus both pole
   conditions do not themselves supply an unconditional sign. This
   compact-test criterion does not supply a Gaussian-flow law or a
   starting sign.

4. M. Suzuki, *On the Hilbert space derived from the Weil distribution*,
   [arXiv:2301.00421v2](https://arxiv.org/html/2301.00421v2), Theorem 1.1
   assumes RH; Theorem 1.2 is an RH-equivalent norm identity for every
   compact smooth complex test. Section 3.1 (3.3) is an unconditional
   explicit formula, not that norm identity. These hypotheses prevent
   using a positive Weil spectral measure or Hilbert norm as an
   unconditional initial sign.

5. B. Rodgers and T. Tao, *The De Bruijn--Newman constant is
   non-negative*, [arXiv:1801.05914v3](https://arxiv.org/html/1801.05914v3),
   Introduction (4), Theorem 1.1 and Section 4 Theorem 4.1 with its proof.
   Their deformed-Xi flow solves backward heat; zero motion is stated
   for Lambda<t<=0 with principal-value interactions in the real-zero
   regime of their contradiction argument. Lambda>=0 supplies neither
   the opposite bound needed for RH nor a test-smoothing sign law.

### Three mechanisms and duplicates

- Ordinary Gaussian test smoothing: the explicit formula and heat
  theorem support the single later admissibility/differentiation task.
  They give no favourable derivative sign or independent starting sign.
- Deformed-Xi heat and zero motion: a different object and direction.
  Read L058's proof and scope, L059/L060's splitting scopes and
  L616/L617's hypotheses/conclusions. Reuse the ready
  `2026-10-30-backward-heat-negative-energy-coverage.md` and
  `2026-11-01-xi-heat-time-semiconcavity-scope.md` for existing collision
  and uniformity limitations. No repeat is nominated.
- Hilbert-norm or abstract-semigroup positivity: Suzuki's RH hypothesis
  and Hunter's ordinary-L2 scope defeat these direct imports. Reuse
  `2026-11-04-suzuki-generator-energy-source-scope.md` and
  `2026-11-04-suzuki-parameter-descent-scope.md` for existing domain,
  compression and unpaid-sign stops. L740 is a different causal flow.

L744(6)-(7) is for compact smooth tests and a finite delay sum; it cannot
be used unchanged after Gaussian smoothing. The L751/L752 absorption
stop is preserved. Earlier Gaussian regulator assessments concern
regulated Dirichlet families and arithmetic return thresholds, not
neutral Weil test convolution. L466's finite-height signs assert no
complete infinite-zero pairing sign for every smoothed complex test.

### Search record and exclusions

Representative actual queries: `Weil explicit formula Gaussian heat flow
positivity test functions Riemann hypothesis`; `Suzuki Weil distribution
heat semigroup positivity Gaussian Riemann hypothesis`; `"Weil" "heat
semigroup"`; `"Weil" "Gaussian" "positivity" Burnol`; `"Weil" "heat
flow" "differential inequality"`; `"Weil" "Gaussian" "log convexity"
zeta`; `Guinand Weil explicit formula holomorphic strip decay theorem
Gaussian test Iwaniec Kowalski 5.12`; `Micah Milinovich On Littlewood
estimate modulus zeta critical line pdf Guinand`; `"heat kernel"
"Fourier transform" "Schwartz" lecture notes Gaussian convolution`.

The Open Mathematics Courses Gaussian criterion hit is an AI-authored
secondary exposition, not an input. Its bibliography led to inspected
Connes--Consani and Carneiro--Milinovich statements. Claimed-RH and
2026 de Bruijn-divergence hits were not inspected or relied on. Guessed
Stanford/Cambridge note URLs failed; Hunter's author-hosted notes resolved
the needed elementary heat coverage. Tao's exam-solution PDF had garbled
text and is not an input. No essential source blocker persists, and no
cross-notebook input is used. Full matching Mathlib coverage is unchecked.

### Decision and continuation

The negative source-scope finding rejects direct unconditional-sign
imports from the inspected theorems. It is not a counterexample to the
Gaussian mechanism or RH, and makes no exhaustive absence claim.
One narrowed standard specialization is nominated in
`2026-11-04-neutral-gaussian-domain-differentiation.md`. A creative
propagation attempt remains unready: its independent starting sign and
concrete differential estimate with the correct comparison direction
are missing. The new assessment is for separate approval before work,
not execution in this literature turn.
