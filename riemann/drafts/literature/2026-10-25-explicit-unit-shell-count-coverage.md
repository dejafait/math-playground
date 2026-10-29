# Explicit unit-shell zero count — source comparison

TARGET: Assess primary source coverage for an explicit numerical A such that N(u+1)-N(u)<=A log(u+2) for every real u>=1, as the unit-shell input to L464.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched explicit N(T+1)-N(T), Trudgian and Hasanalizade–Shen–Wong bounds; inspected Bellotti–Wong v2 and the published HSW paper; scoped local searches located qualitative or assumed counts, not a numerical duplicate.
SOURCE_EVIDENCE: Bellotti–Wong, arXiv:2412.15470v2 (7 July 2025), Theorem 1.1, printed p. 1, definition of N, p. 1, correction footnote p. 2, and complete Section 5, pp. 23–24; HSW, JNT 235 (2022), Corollary 1.2, p. 221, DOI 10.1016/j.jnt.2021.06.032.
COMPARISON: Bellotti–Wong supplies an unconditional explicit global counting error for every T>=e; it covers the needed count input after elementary numerical specialization, including a separate compact-height bound. L464 itself leaves A unspecified.
GAP: No numerical A or closed-shell constant is proved here; the next research step must give full inequalities, all-height coverage, multiplicities and endpoint justification. The full effective tail onset remains outside scope.
REASON: Essential numerical source coverage is now available; use the corrected primary theorem rather than reprove zero counting or reopen the parked common-onset package.

Here N(v) counts nontrivial zeta zeros with 0<Im(rho)<=v, with
multiplicity. Natural logarithms are intended. Essential continuation
inputs are L464 and L018, and the saved effective-onset comparison.
No cross-notebook input or fixed-half-plane premise is proposed.

Downstream use: replace one unspecified constant in L464's quantitative
shell estimates. Independent saddle, zeta-strip, amplitude and common
onset constants remain missing even if this component succeeds. The
earlier numerical-overlap stop remains recorded. Continue only if the
specialization supplies a numerical constant with every height and
endpoint accounted for; abandon that certificate if any uncovered range
or unproved computational premise is silently required.

## Inspected primary input

Chiara Bellotti and Peng-Jie Wong (appendix by Andrew Fiori),
[*Improved estimates for the argument and zero-counting function of the
Riemann zeta-function*, v2](https://arxiv.org/pdf/2412.15470v2),
Theorem 1.1, printed p. 1, states, for every real T>=e,

    |N(T) - (T/(2pi)) log(T/(2pi e))|
       <= 0.10076 log T + 0.24460 log log T + 8.08344.

Its N uses 0<Im(rho)<=T. Section 5, pp. 23–24, combines Table 2's
analytic bounds above 30,610,046,000 with Platt's computed |S|<=2.5167
below that height and the gamma remainder. This is a citation input;
neither its parameter computations nor the zero computation was rerun.
Footnote 1, p. 2, corrects HSW's 9.3675 to 9.4925. HSW's
[published Corollary 1.2](https://www-math.nsysu.edu.tw/~pjwong/stuff/CountingRiemannZeros.pdf),
p. 221, was inspected as a predecessor, not selected for specialization.
The search-result abstract's Bellotti–Wong constant 8.08292 is superseded
by v2's 8.08344. Corollary 1.6 supplies a more tailored increment bound;
it is unnecessary for the proposed coarse specialization and is not
imported here. The full manuscript has not been independently audited.

## Applicability and remaining specialization

The global error theorem is stronger source information than the
qualitative count in L464, but does not literally state the requested
single A. The next step is elementary specialization, not a reproof of
its analytic estimates. It must use the standard multiplicity-counted
N of the argument principle, rather than read the displayed set notation
as counting distinct locations. No simplicity or RH assumption is allowed.
If using off-ordinate formulas, it must justify the chosen one-sided
limits, with the continuous error bound retained.

For low heights, the proposed proof may bound a compact interval by
monotonicity and one source-covered endpoint >=e. It must not assume
the location or simplicity of the first zero from a decimal table.
For L464, a second endpoint issue remains: its equation (6) counts
closed [v,v+1] shells for every v>=0, whereas the saved target counts
(u,u+1] for u>=1. A justified one-sided limit or an enlarged interval
and a separately explicit compact-range estimate is required. These
are approved proof obligations, not results derived in this review.

## Duplicates and recorded stops

The relevant local hits were L464 Section 3 and its approved local-factor
assessment, L133's assumed multiset count, L076's additional bounded-count
hypothesis, and L384's asymptotic Backlund count (source discussion,
lines 70–92). None of those cited passages supplies a numerical A for
the present target. The prior effective-onset assessment, lines 54–67,
leaves this component open alongside independent analytic constants.
No exact numerical duplicate was located by the scoped count searches;
this is not a novelty claim. Generic multiset estimates and empty-cell
arguments do not establish actual-Xi signs.

Queries included “explicit bound N(T+1)-N(T) zeta zeros Trudgian 2015”
and “Hasanalizade Shen Wong number zeroes Riemann zeta 0.1038 0.2573
theorem”. Primary statements were read before the relevant Section 5
proof cases. Mathlib coverage was not checked; no matching formal
explicit-count theorem is claimed. No new mathematical result, lemma
or mathematical script was written during this literature-only step.
