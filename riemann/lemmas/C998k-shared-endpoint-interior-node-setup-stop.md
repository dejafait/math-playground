# C998k: Shared endpoint proposal — fixed bisection setup stop

## Hypotheses

Consider ONLY the square-service target of C998i/audit682, with both
endpoint brackets, independent dotted data and all same-parity modes
0..255. C998g Section1/audit674 supplies its square coefficient1/4;
its scalar convention counts each real addition, subtraction,
multiplication, division, comparison or assignment separately. The
required complete square error is<=1e-10 and total scalar work<=20000000.
No source/core/operator or actual-Xi contract is validated here.

Assessment `drafts/literature/2026-11-13-shared-endpoint-moment-review-685.md`,
SPECIALIZE before this invocation, and source-notes686 license one
REPRODUCTION feasibility attempt. Reuse source-notes683 for quadrature
setup. The imported primary formula is Johansson--Mezzarobba,
*Fast and rigorous arbitrary-precision computation of Gauss-Legendre
quadrature nodes and weights*, arXiv:1802.03948v1, 12February2018,
Section1 equations(2)-(3), Section3 equation(9), pp2,6,
[primary PDF](https://arxiv.org/pdf/1802.03948v1).
The roots are simple and symmetric; the weight formula and Legendre
recurrence apply to these positive integer degrees. The source's
asymptotic complexity theorem is NOT a finite scalar bound used here.
Only the prescribed local recurrence cost is counted below.

Fix this partial algorithm, before evaluating any moments:

* Endpoint interval[0,1/8]: intend the128 even Taylor powers2..256
  of each density against the seven shared weights in C998i(4).
  A finite certified bank is still to be constructed. No Taylor
  remainder, bank accuracy, stability or bank-work bound is assumed.
* Interior: use Gauss-Legendre rules with117,81,63 points on
  [1/2,1],[1/4,1/2],[1/8,1/4], respectively. These sizes are fixed
  choices, motivated by C998j's schedule as comparison evidence;
  no C998j error claim is used as a mathematical premise.
* Construct those nodes afresh at512 fractional bits. Give initial
  exact-sign isolating brackets of width2^-16 for each positive root
  for free in the lower count. Failure to isolate stops even earlier.
  Each positive bracket then undergoes exactly496 midpoint/sign updates
  to width2^-512. There is no Newton step, early-exit shortcut,
  imported node table or polynomial-value reuse between midpoints.
  A midpoint that is exactly a root can be retained as an endpoint;
  the fixed iteration count is still performed. Negative nodes are
  obtained by symmetry and the zero node is supplied exactly, both free
  for this count. This fixed-loop choice is an implementation condition,
  not a claim that all bisection algorithms require this work.
* At every midpoint evaluate the full recurrence independently, using
  precomputed rational a_k=(2k+1)/(k+1), b_k=k/(k+1):

      P_0=1, P_1=x,
      P_(k+1)=(a_k*x)*P_k-b_k*P_(k-1), 1<=k<=N-1.       (1)

  Implement the displayed three multiplications and subtraction at each
  k>=2. No algebraic or parity-based polynomial evaluator replaces this
  recurrence. Give the initialization and k=1 step for free.

The proposed shared bank does not need to be completed to test this
mandatory prefix. The conclusion holds for EVERY bank completion
retaining this interior-node implementation, even if that completion
could make all other costs zero. The coefficient archive and C999q's
exact Z are unchanged and not loaded or used in the cost proof.

## Conclusion

The prescribed node setup alone performs at least

    4*496*[58*115+40*79+31*61]
      =23254464>20000000 scalar operations.                 (2)

Thus this partial shared-moment implementation cannot meet the total
square-service budget, independently of endpoint-bank feasibility.
Stop before isolation, bank construction or a quadrature batch. No
nodes, weights, moments, square entries or complete error bound are
computed. In particular no accuracy claim follows from the chosen
Taylor degree or precision. This is a prescription-specific negative
result, not a complexity lower bound for shared moments, Gauss rules,+bisection with shortcuts, or other certified node algorithms.

## Proof

For each of the three odd N, symmetry and the simple zero root leave
(N-1)/2 positive roots. These counts are58,40,31. After successful
isolation in the hypothesized width2^-16 bracket, each midpoint update
halves its width, so the specified496 updates give2^-512. This width
claim does not assert a sufficient final quadrature-error bound.

The fixed full evaluation in(1) contains N-2 steps k=2,...,N-1.
Each has the three explicitly prescribed real multiplications
a_k*x, its product with P_k, and b_k*P_(k-1), then one subtraction.
The scalar convention therefore charges at least4(N-2) per update,
even giving exact rational arithmetic, constants, prior values,
assignments and the zero test away. Multiplication and subtraction
are not a single operation under that convention. Independent
midpoint evaluations cannot reuse these products in this algorithm.

The three resulting work counts are

| N | positive roots | charged steps/update | mandatory scalar work |
| --- | --- | --- | --- |
|117|58|115|13233280|
|81|40|79|6269440|
|63|31|61|3751744|

Their sum is(2), exceeding the full budget by3254464. Root isolation,
rational coefficient preparation, bisection arithmetic, sign tests,
weights, interval overhead, bank construction/contraction, constants,
Z, entry assembly and final trial contraction only add nonnegative
work. Even a successful zero-cost realization of those tasks cannot
repair(2). An isolating failure is also a service failure. This proves
the stated early stop without making any endpoint error estimate.

Reproduction command from the notebook directory:

    python3 scripts/separation-seven/shared-endpoint-node-cost-687.py

The full exact-integer planning certificate is
`scripts/separation-seven/shared-endpoint-node-cost-687.json`.
All12 planning checks pass. The complete rows, checks and work ledger
were inspected, not merely their previews. The certificate reports the
excess and unpaid complete error explicitly. It does not certify node
isolation, evaluated quadrature or the intended shared moment bank.

This is local feasibility evidence using known numerical tools, with
no claimed mathematics beyond their general theory. Earlier stops
652/657/660/662/672/685 remain intact. A materially different node
construction needs its own coverage and finite certificate. A-square,
both mixed terms, projection, the full100000000 work bound, inverse
debt, signed S3, higher/mixed endpoints, C744q/H2, non-neutral and
actual-Xi assembly remain independent open gaps.

## Mathlib

Full matching coverage for this fixed algorithm and scalar ledger has
not been checked. Supporting Legendre-polynomial and natural-number
arithmetic theorems would not alone certify the requested service.
Unknown coverage is not evidence of absence. The imported recurrence
is cited above; no general quadrature or convergence theorem is reproved.
