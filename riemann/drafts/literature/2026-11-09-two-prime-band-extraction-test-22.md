# Fixed two-band extraction — bounded mathematical test

TARGET: Test whether the fixed two-prime-band moment map for L928's joint Hardy dictionary has a principal lower singular bound exceeding its full cutoff and other-branch leakage by enough to imply c*T*log(T)*N^(-1/4) coefficient coercivity.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step22's completed bounded two-band/shifted-Hardy, mean-value, nonstationary-phase and divisor-inversion comparison in drafts/literature/2026-11-09-two-prime-band-joint-extraction-21.md; no inspected theorem proves this combined estimate and no novelty claim follows.
SOURCE_EVIDENCE: Direct sources verified 2026-11-09: Hughes Theorem2.2 https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20 ; Montgomery–Vaughan TheoremG.14 https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=434 ; Tao Lemmas2.3/2.6 https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf#page=4 ; Rosser–Schoenfeld Theorem5 https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf#page=7 ; DLMF27.5.2–3 https://dlmf.nist.gov/27.5#E3 ; full inspected scope and reused L926/L637 sources remain in the step22 comparison.
COMPARISON: These named tools cover fixed-frequency synthesis, sharp-interval integration, smooth phase weights, finite arithmetic inversion and prime mass separately. The moment map's collective lower bound, its inverse conditioning and its full leakage are not covered conclusions; testing them is the mathematical task.
GAP: Bound the finite analysis map, identify its exact selected-branch coefficient map, bound that map below and pay every complementary contribution uniformly for arbitrary moving complex coefficients. No part of those target estimates is asserted here.
REASON: A concrete finite-map test with a quantitative leakage threshold gives an independently checkable mechanism different from the stopped inverse-polynomial surrogate. Step23 separately reviews this saved assessment and repairs its missing direct source URLs; EXPLORE approves only the unchanged bounded test, not its requested estimates.
SCOPE: Exactly L928's fixed w and actual Hardy Z/phase theta, L=log T, N=floor(T^(1/5)), T<=X<=2T, shifts s=+/-1 and arbitrary complex c_s depending on T,X. Only primes in [T^.22,T^.24] or [T^.27,T^.29], with integer multiplier m<=N. No optimization, length increase, matrix grid, L925/L929 theorem or cross-notebook input.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is a joint lower norm that could
pay L928's projection comparison; successful unsigned coercivity
would still leave signed realization and actual-Xi transfer open.

## Proposed finite test, not a mathematical result

Let K_T be the set of integers k=p*m with m<=N and p in the two
fixed prime bands. Use L928's U, S and weighted norm. As a candidate
analysis map define, for k in K_T,

    (E_T f)_k = T^(-1) integral w_XT(t) f(t)
                                exp(-i theta(t)) k^(it) dt.

This is a definition for the future test. It does not assert Bessel
bounds or orthogonality to any omitted sum. Repeated representations
of k must be checked rather than counted twice by assumption.
Keep both shifted phases theta(t+s/L) exactly.

The future proof should define A_T c as E_T applied only to the
positive-phase Riemann–Siegel branch terms whose arithmetic product
equals the selected output k, retaining the actual cutoff indicators,
all divisor collisions and shifts. Let R_T c=E_T U-A_T c. This
residual includes all other products in that branch, the complete
negative-phase branch, and the original Riemann–Siegel remainder.
Its definition supplies no smallness assertion. No phase freezing or
cutoff deletion is authorized without a separate error charge.

One explicit success certificate would supply C_w>0 and nonnegative
a_T,b_T, independent of X and the coefficient vectors, satisfying

    ||E_T f||_2^2 <= C_w T^(-1)||f||_T^2,
    ||A_T c||_2 >= a_T sqrt(S),
    ||R_T c||_2 <= b_T sqrt(S),
    a_T>b_T,
    (a_T-b_T)^2/C_w >= c log(T) N^(-1/4)

for one c>0 at a common sufficiently-large-T onset. These are
requested inequalities, not derived bounds. A different rigorously
paid inequality adequate for precisely the same projection comparison
may be recorded, with its actual and required scales explicit.
No positive mass asymptotic alone supplies the log(T) factor or the
two-channel inverse. Standard Hilbert, inversion and Schur theorems
are to be imported, with only the necessary changed specialization
proved; do not reprove general source results.

The bounded attempt ends after an analytic principal-map and full
leakage comparison for these fixed sets. Continue this mechanism only
with a paid positive margin or materially new informative evidence.
If the displayed certificate cannot be paid, record the exact loss;
an inadequate upper bound is inconclusive rather than a lower-bound
counterexample. No automatic new band search or pilot enlargement.

Essential local input IDs: L637 for actual normalization and smooth
phase estimates, L737 for windows and finite-form context, audited
L926 for established conditioning context and its scalar/Schur
inputs, and audited L928 for the unchanged dictionary and required
scale. The new downward divisor transform, if it occurs, needs its
own justified inverse orientation. L930/L932 and the recorded stops
are contrasts only. All selected/complementary leakage, the collective
inverse margin and its uniformity remain unresolved assumptions until
proved. No numerical preview can certify them. Mathlib full matching
coverage is unchecked.

Prospective purpose: proof_attempt/creative, because an explicit
frequency-analysis map, rather than surrogate inverse control, is
being tested against the two amplified blocks' cancellation. The
bounded test and decisive evidence are the five inequalities above.
This is preparation only; no new lemma, inequality for these maps or
mathematical script was produced in either literature turn.


## Separate source-link recovery review — step23, 9 November 2026

LITERATURE_REASON: Supervisor identified missing direct source URLs in this ready assessment; verify and attach the existing primary-tool references without repeating mathematical discovery or changing the target.

All six direct documents below resolved through the web reader. The
step22 comparison supplies the previously inspected proof cases and
duplicate/failure assessment; it is reused rather than newly claimed.

- [Hughes, July 2017, Theorem 2.2, printed pp18–19](https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20): rechecked the real-height moving-cutoff statement. Undifferentiated error only; the following heuristic is not a proof input.
- [Montgomery–Vaughan, Hilbert’s Inequality (1974), Theorem2 and Section4](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf): author-hosted original resolves; retain step22’s warning against extracting exact constants from garbled formulas.
- [Authors’ served MNT II draft, TheoremG.14, printed p422, (G.14)](https://personal.science.psu.edu/rcv4/571s25/montgomery-vaughanII.pdf#page=434): rechecked distinct real frequencies, uniform positive spacing and arbitrary complex vectors. This is a fixed-frequency tool, with no claimed draft publication date or joint extraction conclusion.
- [Tao, 247B Notes8, Lemma2.3/(4), pp4–5, and Lemma2.6, p6](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf#page=4): rechecked the nonstationary interval hypotheses and explicit boundary term. Reuse the inspected smooth-amplitude case; internal sharp cutoff jumps still require payment.
- [Rosser–Schoenfeld (1962), Theorem5, p70; proof pp86–87](https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf#page=7): primary-paper mirror resolves; theorem and proof-range split located. Retain the previous restriction to standard reciprocal-prime asymptotics, not a newly verified effective constant.
- [NIST DLMF 27.5.2–3](https://dlmf.nist.gov/27.5#E3): exact finite divisor identities rechecked; cited source Apostol (1976), Chapter2. No inverse norm follows by citation alone.

Decision remains EXPLORE, now separately reviewed with direct URLs.
This repairs a process omission and supplies no new mathematical
evidence: completed outcome STALLED, classification NOVELTY_UNCHECKED.
The proposed map, five requested inequalities, fixed bands, local input
IDs, unresolved assumptions and stop test above are unchanged. No
source blocker remains for attempting that test. Full Mathlib coverage
remains unchecked. No theorem specialization is derived in this review.
