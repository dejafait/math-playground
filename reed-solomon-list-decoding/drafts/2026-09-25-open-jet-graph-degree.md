# Open jet graph degree review — 2026-09-25

## Gap, intermediate target, and test

L003 bounds the rational coordinates and residual equations on one
nonsingular Taylor chart. The missing passage is a polynomial cumulative
degree bound after taking that chart's graph closure. L002 could use such
bounds after a uniform collection of charts covers every candidate.
Singular solutions, the interpolation input, field scope, concrete list
constants, and the exact finite-code boundary remain separate obligations.

Existing changes, the whole overview and DAG, L002–L003, and the recorded
failed q-polynomial transfer were inspected and preserved. No existing
local proof gives this graph bound. The prize page was rechecked on
September 25; its base-field threshold and existence proviso agree with
the frozen model. The September 5 version of
[TR26-169, Lemmas 5.3–5.4 and the chart construction on printed p. 25](https://eccc.weizmann.ac.il/report/2026/169/download#page=20)
is the source passage being reviewed. The unavailable ABF comparison
remains qualified.

The discriminating test is whether degree growth depends on the fixed
number of initial variables, rather than the growing number of lifted
coordinates, without counting components supported entirely on H=0.
A rigorous polynomial bound passes; a required exponent growing with d,
or an uncontrolled contribution from the boundary of the rational map,
rejects this passage.

## Result

The working bound and proposed section argument were saved before detailed
proof work. The completed proof is now
[L004](../lemmas/L004-degree-of-open-jet-graphs.md). Put A=D+B,
L=max(0,2(d-s)-1), E=A(1+B L), and T=A L+1. The total chart closure has
dimension at most s+1 and cumulative degree at most A(E T)^(s+1). The closure
constructed separately at any fixed parameter z has dimension at most s
and cumulative degree at most B(E T)^s. Empty charts are allowed.

The proof bounds intersections by a component tree weighted with degree
and remaining dimension. It then pulls a general finite section of each
graph closure back to equations of degree at most T on its base component.
The section avoids the graph boundary. Any extra components of the pulled-
back equations on H=0 do not prevent bounding the isolated preimages.
Thus the exponent depends on the initial dimension, not on d or the number
of lifted coordinates. For fixed s,B and D,d=O(n), E,T=O_B(n^2), so the
fixed-parameter chart bound is O_{s,B}(n^(4s)). The constants implicit in
D,d=O(n) remain assumptions about a future interpolation input.

Only components of the closed base meeting H!=0 contribute. The graph
closure itself lies in the full differential solution set because the
solution identities are polynomial and hold on its dense open graph. It
may include some singular limiting solutions, but no coverage of all
singular solutions follows. The earlier denominator-clearing cautions are
retained. This is an explicit local source review, with no novelty claim.

## Checks and qualifications

The argument was checked for mixed component dimensions, points present
before any cut, empty intersections, zero residuals, H constant and nonzero,
the no-lift case d=s, and s=0. The standard generic linear-section fact and
proper hypersurface degree bound are recorded in the
[geometric foundation](../foundations/03-proper-hyperplane-sections.md).
No graph-image degree theorem is adopted without the pullback argument.

Two exact algebraic examples in L004 test the delicate boundary steps.
The graph of y/x on V(xy) with x!=0 loses the spurious denominator line
present in the naive cleared equations. The primitive differential
polynomial Q=Y_0(Y_0+Z) has two simple constant solutions for z!=0 which
merge into a singular one at z=0. Its total closure has a nonempty zero
fiber, while the specialized nonsingular chart there is empty. At z!=0
the same example attains the bound B in (5) for s=0. These are exact
calculations in the proof; no numerical experiment or new script is needed.

No equality between a fiber of the total closure and a separately closed
fixed-parameter chart is used. The characteristic condition of L003
persists. The source's entire singular induction is still unverified here.
Mathlib coverage of the new result and supporting geometry is not checked;
the existing direct references and their qualifications are preserved.

## Actual threshold and assessment

Suppose, as an additional unproved hypothesis, that every scalar candidate
list at agreement at least h>=k is covered by at most J fixed-parameter
charts of this type, all of order s with common B,D,d bounds. Then L002 would apply with
Delta<=J B(E T)^s. It would certify the covered radius only under

\[
 q\ge(\varepsilon^*)^{-1}
 \left[J B(ET)^s\sum_{j=0}^s n^j\right]^m.
\]

Polynomially many charts would make this polynomial in n for fixed s,B,m
and D,d=O(n), improving the possible fixed-slack field requirement. It
neither proves that such charts cover every candidate nor replaces the
displayed inequality by epsilon* q>=1. No sharp boundary or new
unconditional safe radius has been obtained.

The discriminating test passes, so the result is ADVANCE and the
exploration streak is 0/3. The geometric route is retained because its
nonsingular chart-closure degree is now bounded. Singular-branch coverage
is the remaining construction issue; optimizing the already polynomial
local degree estimate would not remove it. The full field scope and ABF
comparison also remain open. No complete candidate proof or disproof of
the grand challenge appeared.
