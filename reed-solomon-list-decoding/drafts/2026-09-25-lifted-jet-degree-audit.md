# Lifted-jet degree audit — 2026-09-25

## Gap, target, and test

The cover needed by L002 still lacks a checked degree bound. This single
step reviews the local lifting estimate in
[TR26-169, Lemmas 5.6–5.7, printed pp. 23–24](https://eccc.weizmann.ac.il/report/2026/169/download#page=23), before any
claim that its global solution cover works. Existing changes and the failed
q-polynomial transfer were inspected and preserved. No previous local
result treats this recurrence.

The intermediate target is a polynomial bound, for fixed differential
variable degree B, on the rational Taylor coefficients and all residual
equations after clearing their common denominator. The plausible use is
bounded-degree equations in a fixed number of initial-jet variables, followed
by geometric degree control. Singular branches, closure of the rational
graph, interpolation, field scope, and a sharp finite-code boundary remain
separate unresolved steps.

The discriminating test was to continue if Taylor order prevented
multiplicative denominator growth and all residual equations admitted a
uniform polynomial degree budget. A permitted monomial defeating that
budget would reject this passage. The test is complete and passes.

The September 5 version was inspected on September 25. Its hypotheses were
compared with the pinned local model, and the prize website was rechecked.
The unavailable July ABF comparison remains qualified. The work here is an
algebraic source review, not adoption of the preprint's full decoding claim.

## Result and saved reasoning

The working target and the simultaneous numerator/denominator idea were
saved before the detailed proof and symbolic check. The complete argument
is now [L003](../lemmas/L003-linear-degree-lifted-jets.md). With A=D+B, it
proves numerator degree <=A(2t-1) over denominator H^(2t-1). Putting
L=max(0,2(d-s)-1), the cleared residual degree is <=A(1+B L). This is linear
in d for fixed B,D and implies the source passage's weaker quadratic bound.

The decisive accounting is that the degree spent on a substituted numerator
and on its missing denominator power belongs to one shared budget. Counting
each as a separate full budget is unnecessary. The proof handles all Taylor
orders of the residual, not just the recursively solved initial orders.
No novelty is claimed for the improved estimate.

Only the nonsingular chart H!=0 is described. The base coefficient equation
must still be imposed; solving the recursive equations does not imply it.
Cleared equations can contain extraneous H=0 points. The local proof assumes
characteristic zero or p>d and H nonzero; it neither constructs charts on
singular solutions nor removes the global source's B<p condition.

## Checks

The proof was checked for repeated noninitial factors, t=1, s=0, d=s,
parameter-dependent H, residual orders greater than d-s, and the exact
characteristic requirement on binomial coefficients. Its induction uses
unreduced denominator powers, so cancellation can only improve the bound.

Run `python3 scripts/lifted-jets/verify.py` to reproduce the
[exact results](../scripts/lifted-jets/results.json). Five polynomial charts
were expanded over the rationals, checking triangularity, every recursive
identity, the proposed degree bounds, and all cleared residual coefficients.
They include a square-root equation, nonlinear first- and second-order
equations, a chart needing no lift, and a linear differential equation.
The same residual identities were checked at 120 nonsingular points over
F_5, F_7, and F_11, always with d<p. These checks support the symbolic proof;
they establish neither a global cover nor an asymptotic list theorem.

## Actual threshold and assessment

L003 supplies no value for the cumulative degree Delta in L002. If the
remaining geometric steps yield a uniform cover of dimension at most s_0
and cumulative degree Delta, L002 would certify the list threshold only
under q>=epsilon^(-1)(Delta sum_{j=0}^{s_0} n^j)^m at the covered radius.
The local degree estimate does not replace that inequality by the mere
existence condition epsilon q>=1, and does not determine a sharp boundary.

This is ADVANCE as a relevant mathematical input, with exploration turns
0/3. The route is retained because the local degree test passed. The next
missing passage is geometric degree control of the open chart's graph
closure, rather than a further refinement of this already polynomial
recurrence. Singular coverage, interpolation, concrete list constants,
field scope, and the exact radius still remain unresolved. No complete
candidate proof or disproof of the grand challenge appeared.
