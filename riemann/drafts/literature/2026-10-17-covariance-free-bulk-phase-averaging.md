# Source assessment: actual-height averaging of the covariance-free bulk

TARGET: Derive an actual-height phase-averaging reduction for L425's covariance-free bulk observable, retaining L423's fixed mixture and L419's prescribed branches.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched continuous-time Weyl/Kronecker equidistribution, Riemann-integrable tests, compact-group probability laws and nonstationary integrals; inspected Kowalski B.6.3/B.6.5 and 3.2.5/3.2.6, Tao Proposition 1.1.2 and Lemma 2.3, and Morters--Peres Appendix Theorem 1.6(v); checked L423's fixed harmonics and the step-175 diagnostic stop.
SOURCE_EVIDENCE: Kowalski's compact-abelian-group Weyl criterion and prime-phase convergence, Tao's sharp-interval nonstationary bound, and Morters--Peres's bounded almost-everywhere-continuous test theorem supply the standard averaging framework; exact versions, hypotheses and inspected proof cases are recorded below.
COMPARISON: Known results cover character-to-law convergence, right-half-plane Euler-product continuity and null-discontinuity tests; they do not directly apply to the finite-H selected bulk, its gamma coordinate or its prescribed two-stage matrix rule. Only those local specialization obligations remain.
GAP: No actual-height reduction, limiting value or sign is proved here; the next proof must control exact J replacement, w and g_H normalization, every joint character and both branch stages before using the limiting test theorem.
REASON: This literature-only review completes essential coverage of the unchanged saved target; standard theorems should be imported, with only the exact observable specialization proved next. No new mathematical lemma or script is produced.
SCOPE: The exact TARGET only, at fixed k=13,14 mixture and fixed sigma=5/2, for qualitative o(1) as real H tends to infinity; retain the prescribed branches and full response through justified comparisons. No sign, effective rate, growing Fourier head, critical-line phase law or independence premise is covered.

## Exact scope and proposed use

Use L425's B_H^0 with the actual physical J, L423's exact fixed mixture,
normalization and mass w, L419's fixed coordinate/pair orders and equality
rule, and L424's Q. L368 and L369 supply the complete right-line response
and the actual carrier. A prospective averaging reduction must retain or
justify removal of each of these dependencies; it cannot replace the
actual response by arbitrary independent phases by definition.

The main gap remains global mixed positivity. This intermediate target
could make the remaining diagnostic integral amenable to a later rigorous
evaluation. No limit, nonzero value or sign is asserted. A transport defect,
actual capped nondegeneracy, negative-Bcal clipping, the full-error regulator
margin in L413, and actual critical-function realization remain independent
unresolved issues.

The desired threshold is an additive o(1) reduction of B_H^0 to a
specified phase integral for all real H tending to infinity, not a
nonzero sign margin. The averaged response must retain its actual
multiplicative prime correlations. A reduction to Haar variables is a
conclusion to justify, never a definition of the actual height law.

## Primary sources actually inspected

1. E. Kowalski, *Arithmetic Randonnee: An introduction to probabilistic
   number theory*, manuscript version January 19, 2021,
   [ETH course copy](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf).
   Theorem B.6.3, printed p. 146: on a compact abelian group,
   vanishing expectations of every nontrivial continuous character
   characterize convergence to Haar. Read B.6.5(2), its continuous
   linear-orbit proof and Example B.6.6(2), pp. 146--147. Proposition
   3.2.5/Lemma 3.2.6, pp. 42--43, give the prime-phase law for uniform
   t in [-T,T]; read finite-support characters, unique factorization
   and the exact integral. Read the special Re(s)>1 proof of Theorem
   3.2.1, pp. 43--44, including uniform Euler-log tails and composition.
   None directly treats gamma phases or discontinuous selection.

2. T. Tao, *Higher Order Fourier Analysis*, author preliminary version
   June 5, 2012, [AMS-author PDF](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf),
   Proposition 1.1.2, printed p. 5. Read the complete character,
   trigonometric-polynomial and uniform-density proof. Its statement
   concerns sequences in a finite torus; it is supporting explanation,
   rather than the theorem to import for the continuous height laws.
   Use Kowalski B.6.3 for that purpose.

3. T. Tao, *Lecture Notes 8 for 247B*, Winter 2007,
   [author PDF](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf),
   Lemma 2.3 and equation (4), printed pp. 4--5. For a smooth real
   phase on an interval J with |phase'|>=c>0 and |phase''|<=C, its
   integral with frequency lambda>0 has bound
   O(lambda^(-1)(c^(-1)+C|J|c^(-2))). Read both the endpoint term
   and differentiated reciprocal derivative. Lemma 2.4 additionally
   requires monotonicity of phase'; that hypothesis must not be inferred
   for the phase of RZ from its speed alone. Example 2.2 explicitly
   warns against a derivative lower bound as the sole argument.

4. P. Morters and Y. Peres, *Brownian Motion*, draft May 25, 2008,
   [author manuscript hosted at Berkeley](https://www.stat.berkeley.edu/users/aldous/205B/bmbook.pdf),
   Appendix, Section 1, Definition 1.1 and Theorem 1.6(v), printed
   pp. 331--333. For Borel random variables in a metric space,
   convergence in distribution extends to expectations of a bounded
   measurable test when its discontinuity set has zero limiting law.
   Read (i)--(v) and the proof, particularly (iv) to (v): choose level
   boundaries avoiding atoms and sandwich by elementary functions.
   The extracted proof's sentence defining elementary functions omits
   a boundary symbol in its zero-measure condition; the theorem and
   the subsequent level-set argument explicitly require null
   boundaries. This does not authorize arbitrary Borel tests or an
   H-dependent family without a separate approximation argument.

These are source imports for a future specialization, not a claimed
evaluation of the local observable. No standard theorem needs reproof.
Mathlib coverage of the full averaging reduction and these matching
source statements was not checked; unknown coverage is not absence.

## Hypothesis comparison and the bounded next attempt

The following are proof obligations for the unchanged TARGET, not
results established by this literature turn.

- **Exact finite-H observable.** Start from L425's B_H^0, not the
  floating leading-matrix screen. L423 (9) and its normalization
  paragraph supply N_H=1+O(H^-1+ell^-5/2) and E(1-w)=O(ell^-5/2).
  Its g0 is the fixed combination (5), a function of W=|Z|^2.
  Verify removal of w and replacement of g_H by g0 inside Q using
  boundedness on the fixed state ball. No derivative bound on w is
  available or needed for a bounded-error comparison.

- **Physical matrix and both branches.** L425 (3)--(8) give the full
  J approximation, positive-scalar invariance of the coordinate rule,
  branchwise continuity away from three gaps, their finite angular
  zero sets and actual-height exceptional-set control. Use those
  proved inputs to justify the new comparison with the leading
  selector; L425's conclusion itself only deletes A_H. Keep the
  coordinate/pair orders and equality rule at both stages. A different
  Schur--Horn basis is outside scope. Identify the discontinuities of
  the proposed limiting test and verify their nullity under the
  proposed limit law before invoking source 4. A smooth branchwise
  formula alone does not discharge this obligation.

- **Joint character tests.** For the proposed compact group consisting
  of the carrier circle and the prime circles, test every character,
  with fixed integer carrier index and fixed finite prime support.
  Separate zero and nonzero carrier index. Source 1's linear
  Kronecker theorem alone covers only the prime part; it says nothing
  about the accelerating gamma coordinate. L369's actual phi
  derivatives (6), and L423's fixed-harmonic argument, are the local
  inputs to compare with source 3 for the other case. Work on [H,2H]
  with both endpoints. Do not assume monotonicity of arg(RZ), uniform
  estimates over increasing character sets, or rational independence
  of composite-integer phases. Only prime coordinates are independent
  in the proposed Haar model; composite phases remain multiplicative.

- **Complete response and limits.** At sigma=5/2 the local L368
  bounds and source 1's absolutely convergent Euler-log construction
  are in their stated half-plane. Verify the full response as a
  continuous, nonvanishing function of the prime coordinates before
  forming its normalized circle phase. Avoid a globally chosen real
  argument on a torus: the circle-valued ratio Z/|Z| is the relevant
  object. The finite tie set from L425 concerns the combined phase
  phi+arg Z; it must not silently be interpreted as a tie set in phi
  alone. If using finite heads, fix the head and tie tolerance before
  H tends to infinity and prove both actual and limiting tail bounds
  before removing them. Alternatively apply source 1 directly on
  the countable compact product, checking its continuous characters
  and source 4's discontinuity hypothesis there. No formal interchange
  of an infinite Fourier expansion with an H-dependent limit is covered.

Thus SPECIALIZE is justified: there is a precise standard framework
and relevant local uniform inputs, while the exact selected-observable
application still requires a mathematical attempt. This is not IMPORT
of the final reduction, nor a novelty claim. Neither source supports
clipping, nonzero defect, or a regulator margin.

## Search, duplicates and recorded failures

Queries included: `Weyl criterion continuous time equidistribution torus
Riemann integrable functions theorem`; `Tao equidistribution Weyl
criterion continuous Kronecker flow Riemann integrable`; `Weyl
probability measures characters continuous compact group criterion`;
`Billingsley Convergence Probability Measures theorem 2.1 bounded
measurable discontinuities P measure zero pdf`; and `van der Corput
oscillatory integral lemma first derivative monotone Tao notes`.
Follow-up searches sought primary Portmanteau statements with null
discontinuities. Search snippets were discovery aids only.

Beck--Chen--Yang, [arXiv:2404.00077v2](https://arxiv.org/pdf/2404.00077v2), introduction and Theorem 1
hypotheses were screened: its polysquare/polycube orbit setting is not
a theorem for this gamma-driven observable, so it is not an input.
The Colorado Billingsley PDF and Berkeley Fristedt--Gray PDF returned
retrieval errors; neither is used. Source 4 supplies the required
theorem and full proof, so these failures are not essential blockers.
No critical-strip Bagchi theorem or universality proof is imported.
No claim of novelty follows from this bounded search.

Local reads were L425's complete pre-audit proof; L423 through its
fixed mixture, harmonics and full normalization; L424's hypotheses and
conclusions; L419's fixed coordinate rule and harmonic interface; and
the relevant L368/L369 bound/phase locations. They show that L423's
polynomial harmonic check is a reusable input, not a duplicate of the
nonlinear target. The step-175 stop is preserved in
`ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`: sampled
means of both signs, no certified quadrature and no actual-height
averaging. L425 repairs one comparison only; it does not revive
numerical signing. No sibling notebook was read.

## Continuation and abandonment test

Continue with one proof attempt at the exact TARGET, classified
REPRODUCTION: import the cited standard theorems and prove only the
four specialization obligations above. Success means a fully specified
averaging formula for B_H^0 with error o(1), retaining L423's exact
fixed coefficients and L419's two-stage rule; its value may remain
unevaluated. Save any incomplete argument before lengthy work.

If a joint character cannot be controlled, the limiting test has a
positive-measure discontinuity set, or full-response comparison cannot
be made uniformly off the recorded ties, identify that concrete failure
and stop the claimed reduction. Do not substitute free phases, change
the selected basis, or claim phase speed proves independence. A later
numerical/sign target is outside this assessment and requires its own
review. Global mixed positivity, actual realization, capped
nondegeneracy, negative-Bcal clipping and L413's full-error margin
remain independent unresolved assumptions; no RH progress is asserted.
