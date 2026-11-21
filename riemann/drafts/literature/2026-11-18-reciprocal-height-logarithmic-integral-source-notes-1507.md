# Reciprocal-height signed-log source review1507

## Scope and local evidence

Literature-only review of assessment1506's exact target. Read C028a's
actual monic polynomial and Gaussian normalization, complete C028b,
L025, source-notes1500 and history1506. Preserve both reference-family
stops. The main gap is actual-Xi all-degree positivity; H_d=o(d) is
already RH-equivalent, not an imported estimate.

The initial working checkpoint was saved before the last source extraction.
The completed comparison follows. No new formula is proved in this review;
no lemma, mathematical script, PROOF or DAG edit is made.

## Inspected primary statements and essential proof cases

**Min Ru**, *Nevanlinna Theory*, undated author-hosted notes, accessed
2026-11-18, [Theorem A1.1.1, printed pp.1--2](https://www.math.uh.edu/~minru/log.pdf).
For nonzero meromorphic f on a neighborhood of the closed disk |z|<=R,
finite R, and interior z avoiding zeros/poles, it states

    log|f(z)| = integral_0^(2pi) [(R^2-|z|^2)/|R exp(it)-z|^2]
                              log|f(R exp(it))| dt/(2pi)
               - sum_a log|(R^2-conj(a)z)/(R(z-a))|
               + sum_b log|(R^2-conj(b)z)/(R(z-b))|.

The sums contain interior zeros a and poles b with multiplicities.
Read the complete proof: the zero-free case uses harmonic averaging;
finite disk factors remove zeros/poles without changing boundary modulus.
Boundary zeros/poles are treated by f(rho*z), rho tending to 1.
This supplies finite-disk coverage, not unweighted real-line convergence
or degree-uniform domination. Its brief boundary-limit instruction is
not an independently checked uniform-integrability estimate. No global
logarithm of the actual polynomial is imported.

**Abbas Emami-Naeini and Dick de Roover**, *Bode's Sensitivity Integral
Constraints: The Waterbed Effect Revisited*, arXiv:1902.11302v1,
9 January 2019, [Theorem1/(12), Corollary3/(18), AppendixA/(23)--(27)](https://arxiv.org/html/1902.11302v1).
Read those statements and the complete relevant appendix. For the
closed-loop stable proper rational SISO setting, with sensitivity
S=1/(1+L), its normalized equal-degree factorization gives

    integral_0^infinity log|S(iw)| dw
      = (pi/2)[sum Re(closed-loop poles)-sum Re(open-loop poles)
                    +2 sum_(open-loop RHP poles) Re(pole)].

Multiplicity is retained. The proof factors the rational function,
pairs conjugates, integrates logarithms of quadratic ratios using (25),
and separates stable/unstable open-loop cases. It does not state our
arbitrary-real-polynomial identity. Rotation need not retain real
coefficients or stability; half-line doubling is therefore unavailable
without justification. Equation (25) has denominators b,d: its zero
boundary parameters require a separate limit. The normalized factorization
must be checked, not inferred from the word proper alone. No control
stability theorem or displayed antiderivative is imported blindly.

## Comparison and one bounded continuation

The strongest inspected conclusions are exact accounting identities,
not unconditional small-height estimates for unshifted actual Jensen
polynomials. No direct source for their H_d=o(d) was located. The search
does not certify originality or nonexistence of stronger literature.

Use C028a's unchanged P_d=R_d/gamma_0, b_1=gamma_1/gamma_0,
and C028b's multiplicity-counted H_d. Nominate the reference
A_d(x)=(x+b_1)^d solely for a signed logarithmic integral; this is not
an orthogonal-basis Schmeisser budget. The proposed finite test is to
establish the identity

    integral_R [log|P_d(x)|-d log|x+b_1|] dx = pi H_d

and determine the first nonzero symmetric-tail term after y=x+b_1,
with an explicit fixed-d remainder. This is a target, NOT a theorem
proved during this literature turn. Finite singular sets are interpreted
almost everywhere with locally integrable logarithms, not by assigning
finite values at zeros. The matching monic degree and next coefficient
are recorded in C028a; their adequacy for tail cancellation must be
proved in the continuation. No limit d->infinity under the integral is
preapproved. A constant depending on d supplies no uniform saving.

Why specialization/reproof is justified: the disk theorem needs a new
real-line limiting argument, and the control theorem's hypotheses do
not match. A finite-factor proof checking local logarithms, both tails,
normalization and constants is a known-method specialization. Reproving
general Poisson-Jensen or control theory is unnecessary. Any broader
asymptotic estimate requires new assessment. Full matching Mathlib
coverage has not been checked; no absence is claimed.

Plausible downstream use: an exact signed functional and explicit tails
would permit a later bulk/tail comparison that retains cancellation,
instead of squaring all residual coefficients. The unpaid threshold
remains the full integral o(d), equivalently C028b's RH criterion if the
proposed identity is verified. Establishing the identity alone is only
an interface. Continue only after finite integrability, sign/factor and
tail checks pass; abandon any shortcut requiring hyperbolicity, an
unknown stable denominator, a global log, or degree-uniform domination
from fixed-d bounds. Do not prolong identity-only work into an audit
chain without a concrete signed estimate.

## Search and retrieval record

Queries included `polynomial integral log absolute value real line sum
imaginary parts roots integral`; `Poisson Jensen formula upper half
plane polynomial logarithmic integral real zeros`; `"polynomial"
"integral" "sum" "absolute imaginary parts"`; `"Schmeisser" "integral"
"imaginary" zeros`; `"Bode integral" "rational function" zeros poles
proof`; `"Bode" "integral" "complex coefficients"`; `"Poisson-Jensen"
"polynomials" "real line"`; and the exact Bode paper title/arXiv ID.
Snippets and secondary mirrors were discovery leads only.

Scoped duplicate/failure searches covered November18 actual-Jensen,
actual-Xi-Jensen and penultimate-Jacobi assessments, C028a--c and the
named Jensen/Jacobi attempts; source-notes1500's three mechanisms were
read. No matching finite signed-log proof was located in that scope.
C028a's Gaussian and C028c's penultimate-Jacobi norm stops do not refute
an actual signed-log comparison, and C028b prevents calling its o(d)
threshold a weakening of RH. No cross-notebook input is used.

Cambridge Chapter5 retrieval returned502; IISc notes were restricted;
Goldberg--Ostrovskii's Citeseer copy returned403; the Math-Net sm3761
link redirected to its homepage. These are unread leads, not inspected
theorems. Chiang's Chapter4 metadata was reachable but its relevant
theorem extraction timed out; it is unused. Koosis/Cartwright and the
complex-coefficient control paper remain unread and nonessential for
the bounded finite specialization. Min Ru's full theorem/proof and
the Bode appendix were readable through web text. Screenshot calls
yielded no inspectable image; no visual verification is claimed.
Shell download failed DNS and supplied no evidence.

Outcome EXPLORATION: essential identity-level coverage obtained and one
finite test nominated, with no new mathematical result or actual-height
upper bound. Assessment1507 awaits separate next-turn approval. This
turn spends no mathematical exploration attempt and resets no budget.
