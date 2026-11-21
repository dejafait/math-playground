# Degree/time improvement: completed source screen1193

TARGET: Assess primary coverage for coefficient-uniform positivity of C030e's heat form at t_N=log(N)/(4000000N) for all sufficiently large N, screening at most three signed arithmetic mechanisms against recorded failures.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Screen1193 compared three mechanisms using exact heat/Hankel, Hermite-prime, PNT-discrepancy and compact-window queries; reused1117/1121/1181 and1183. Primary hypotheses exclude the tempting Hermite theorem as an unconditional input; no matching coefficient-uniform sign estimate was located. Bounded coverage is not an absence or novelty claim.
SOURCE_EVIDENCE: Polson1708.02653v24 Lemmas7.6-7.7/(23)-(26) and Theorem7.4/join; Balanzario-Cardenas Romero2312.00108v1 Theorem1/(3)-(5), H1/H2 and residue proof; Johnston-Yang2204.01980v2 Theorem1.1/(1.3), Theorem1.4/(1.7), Section3.1 and opening3.2; Connes-Consani author4July2021 Theorem1; Zhu2608.24827v2 Theorem1.2 and Lemma3.2/Section14.1, with prior1121/step310 proof-case coverage reused.
COMPARISON: The retained heat bound covers the old window; the inspected Hermite theorem assumes RH and simplicity. Scalar PNT error has no stated polynomial-family sign estimate, and compact-window positivity has no paid noncompact transfer. None supplies the nominated logarithmic window or a concrete signed mechanism ready for research.
GAP: The proposed coefficient-uniform positivity at t_N=log(N)/(4000000N), both parities and all sufficiently large N, remains undecided; no contradiction or matching unconditional theorem is established. A specific signed prime-pole/coercivity bridge remains missing.
REASON: Completed bounded comparison parks this nomination as a research continuation: all three screened applications retain essential unpaid hypotheses or transfers. The newly identified RH/simplicity requirement changes the route decision. Preserve the question and nominate an independently testable far-time source-proof review instead of repeating absolute budgets.
LITERATURE_REASON: The hypothesis changes from fixed finite-degree admissibility to a degree-dependent sign estimate with unbounded N*t; the old import assessment covers no such estimate.

Main gap: L030-L032/C032a all-degree positivity of the actual Xi form.
The possible intermediate target concerns C030e's actual heat form,
both parities, all real coefficients, and all sufficiently large integer
N, at the displayed positive t_N. Seek a strictly positive lower bound
relative to its Gaussian polynomial norm; distinguish a bound depending
on N from a uniform positive margin. No RH, zero simplicity, modulus
replacement, numerical zero list or additional arithmetic hypothesis
may be silently imposed. The eventual times lie in C030e's small-time
domain, but positivity there is precisely the uncovered question.

Plausible use: a proved extension would reduce the degree/time gap in
the retained heat route while preserving the exact signed prime term.
It would still leave all degrees at one fixed positive time, far-time
source validation, actual-Xi transfer and graph realization unresolved.
This is not nomination of a full RH-equivalent positivity statement.

Next review must first compare exact statements and stronger known
results, including Polson's degree/time estimates and relevant signed
Fourier/Hermite estimates, using only narrowly relevant local records
before primary sources. Screen at most three materially distinct
mechanisms. Compare with stop1117's finite-block countermodels,
stop1181's unpaid class bridge and discovery1121's arithmetic-to-square
gap. C030c is a signed support discriminator, not a polynomial square.
Do not renew an exhausted absolute-envelope or generic Schur route by
changing its name; the present nomination supplies no signed mechanism.

Continuation test: import a matching theorem if one exists; otherwise
approve only one concrete independently testable estimate if the source
comparison identifies its signed arithmetic input and explains how it
can improve the degree/time scale. Abandon this proposed improvement as
a research continuation if the only available step repeats the old
absolute budgets, assumes the desired all-degree sign, or supplies no
discriminating test. A source review may honestly return no justified
mechanism. A historical stop remains local to its stated hypotheses.

Required continuation inputs are C030e's exact identity(B), C030d's
Gaussian norm/Fourier conventions, C030f's archimedean bounds and
C030g's multiplicity-preserving convergence. These are local results;
do not import another notebook. Full matching Mathlib coverage is
unchecked. No proof, calculation or mathematical script is authorized
under this REVIEW_REQUIRED nomination; a ready research continuation
needs a separately saved coverage assessment and separate approval.


## Completed comparison1193 — 16 November2026

The original nomination above is retained as the question and historical
gate language. This completion supersedes its pending status but approves
no research continuation. EXPLORE describes bounded source coverage;
the checkpoint's NEGATIVE describes the new conditional-source exclusion
and consequent decision to park this nomination. No inequality, lemma,
mathematical script or counterexample was produced.

### Local comparison

Read C030e in full, including identity(B), admissibility, algebraic
squares and finite-order qualifications. Reused C030d/f/g through their
specific source interfaces and existing audits, without rederivation.
Read stops1117/1181, working1121 and comparison1120's essential fields.
Comparison1183/application1113 distinguish reading from independent
validation. No change to the PROOF/DAG argument is needed.

[Polson v24](https://arxiv.org/html/1708.02653v24#S7.SS3), Section7.3,
Lemmas7.6-7.7/(23)-(26), printed pp19-20, supplies the retained
near-zero estimate. Read its full three-error proof and Theorem7.4's
hypothesis/joining argument, pp18,22. The all-time finite-block theorem
requires verification to a height depending on block size. Neither
statement supplies the proposed growing degree/time window. No new
evaluation of its error formula was performed.

The stop1117 countermodels change the arithmetic term, so do not refute
an exact-prime mechanism. Stop1181 leaves its strengthened implication
undecided. Discovery1121's signed support probe is not a polynomial-square
payment. These are reused obstructions, not fresh negative results.

### Three mechanisms screened

1. **Hermite-weighted prime identities.** E. P. Balanzario and
   D. E. Cardenas Romero, *An explicit formula for the zeros of the
   Riemann zeta function*, [arXiv:2312.00108v1,30November2023](https://arxiv.org/html/2312.00108v1),
   Theorem1/(3)-(5), explicitly assumes H1=RH and H2=simplicity.
   Read those hypotheses, the theorem and the residue/functional-equation
   proof following Lemma3; its real-ordinate spectral sum already uses
   the hypotheses. Its parameterized individual weights do not state
   the required uniform quadratic-form bound for arbitrary real
   polynomial coefficients. This is a decisive scope mismatch, not a
   discovered flaw in the paper. Removing H1/H2 or polarizing a main
   term would need additional proof. Do not use it as unconditional
   input toward RH.

2. **Prime-pole compensation through PNT.** D. R. Johnston and A. Yang,
   *Some explicit estimates for the error term in the prime number
   theorem*, [arXiv:2204.01980v2,20April2022](https://arxiv.org/pdf/2204.01980v2#page=2),
   Theorem1.1/(1.3), printed p2, proves unconditionally

       |psi(x)-x| <= 9.39*x*(log x)^1.515*exp(-0.8274*sqrt(log x)), x>=2.

   Theorem1.4/(1.7), same page, gives an asymptotically stronger
   Vinogradov-Korobov-shaped bound for x>=23. Read both statements,
   Section3.1's small-x cases and the opening zero-sum split of3.2;
   no independent proof audit. These scalar cumulative-error bounds
   do not state a signed coefficient-uniform pairing bound for F_q
   in C030e(B). Weighted control, endpoints and polar compensation
   remain unpaid. This does not prove PNT methods cannot help or
   that their variation bounds fail. No specific new signed step
   emerged to justify another absolute-variation calculation. No new
   zero-free region, reciprocal continuation or parked arithmetic
   estimate is proposed; this older bound is not called current best.

3. **Compact-window/semilocal positivity.** Reuse comparison1121 and
   step310's proof-case assessment. A. Connes and C. Consani,
   *Weil positivity and Trace formula, the archimedean place*,
   [author version4July2021,Theorem1 p2](https://alainconnes.org/wp-content/uploads/Selecta.pdf#page=2),
   requires multiplicative support [2^(-1/2),2^(1/2)] and transform
   zeros at i/2 and0; its conclusion is an archimedean Sonin-trace
   bound. Rechecked the statement, reusing the prior proof reading.
   X. Zhu, [arXiv:2608.24827v2,2September2026](https://arxiv.org/html/2608.24827v2),
   Theorem1.2, states certified positivity for real even tests supported
   in[-0.8,0.8]. Rechecked this statement, Lemma3.2 and Section14.1;
   reused prior proof-case reading. No certificate was replayed or
   imported as locally verified. Fixed compact support differs from
   the noncompact Gaussian-polynomial class. A cutoff argument still
   needs degree-uniform full-form tail and cross-term bounds, matching
   parity and normalization. Neither the compact theorem nor its
   pointwise prime-comb envelope supplies that transfer here.

### Queries and qualifications

Queries actually submitted included:

- `"Weil" "Hermite" "positivity" prime Gaussian polynomial`
- `"Polson" "heat" "log" "positivity" 1708.02653`
- `"explicit formula" "Hermite functions" primes positivity`
- `"Hermite" "prime" "explicit formula" Balanzario Cardenas`
- `"prime number theorem" "explicit" "error" Johnston Yang 2022`
- `"Weil" "positivity" "support" Burnol Connes Consani semilocal`
- `"heat" "Hankel" "positivity" "log" "Polson"`
- `"Gaussian" "polynomial" "prime sum" "uniform"`
- `"Hermite" "Weil positivity" -"openmaths.org" -site:github.com`
- `"heat trace" "positivity" "log N"`

Snippets, courses, repositories, SSRN abstracts and claimed RH solutions
were locators only. Gaussian-spectral-packet and November uncertainty-
operator preprints are unread nonessential leads. No essential source
was inaccessible. The bounded search proves neither novelty nor absence
of a theorem. Full matching Mathlib coverage remains unchecked. No
cross-notebook result or extra zero hypothesis is assumed.

### Decision

Park this proposed window extension as a research continuation: no
screened mechanism supplies an independently specified signed estimate
meeting the continuation test. The new conditional-source exclusion
changes the route decision, but establishes no new mathematical bound
or failure of the desired inequality. Reopening requires a precise
signed input or paid transfer and bounded test. Historical stops impose
no global ban.

The main gap and independent far-time/all-degree/realization gaps remain.
A separate reliability target is C030b's still imported far-time
interpolation-tail estimate. Its changed audit scope needs source
coverage; nomination1193 is REVIEW_REQUIRED. No creative central
mechanism is ready because the signed arithmetic payment is unspecified.
