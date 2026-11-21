# Balanced Type II blocks in the actual fixed state: diagnostic2101

TARGET: Test whether C034r's fixed-state frequency average permits a uniform X^(1/2+epsilon) energy upper for balanced Type II blocks with arbitrary 1-bounded factor coefficients.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: The bounded Type I/II, low-frequency, fixed-state and local duplicate comparison is recorded in source-notes2101; no inspected result states this exact balanced-rectangle estimate or its negation. No novelty claim is made.
SOURCE_EVIDENCE: Green-Tao https://arxiv.org/html/math/0606087v2 (22 September 2007), Lemma4.1/Proposition4.2 and both proof cases expose coefficient removal and the rectangle test; C034r section2 supplies the actual weighted translation/multiplier, continuity and nonzero band mass; C034w(7)-(9) supplies the finite Fourier identity. The unrestricted norm/different Riesz state in2096 does not decide this fixed-state problem.
COMPARISON: Standard Type II estimates remove factor coefficients using their moments. This test fixes the actual theta-smoothed h and logarithmic band, and checks a finite balanced block instead of an unrestricted norm or different state. Failure rules out only this coefficient-blind intermediate bound, never the original Mobius energy upper.
GAP: Establish or reject the uniform bound for V_X below, with an averaged-frequency argument, correct weights, multiplicities and real-X endpoints. No lower bound, counterexample or actual-Mobius consequence is established here.
REASON: Source comparison2101 parks direct imports but leaves a checkable question: whether integration in the actual state repairs coefficient removal. This finite diagnostic differs from the local residue, contour-boundary, localization and unrestricted norm tests.
SCOPE: One balanced rectangle, unchanged h,E,Phi,J and Pi_(4 log X), no zero premise; uniformly 1-bounded factor coefficients. Elementary Hilbert-space continuity and finite Plancherel only. No full Heath-Brown decomposition, Mobius upper or new analytic continuation is approved.

## Exact test and relevance

Use precisely C034r's input h, psi=C_Phi h, space E and translations.
For all sufficiently large real X define

    I_X = {m in N: 3 sqrt(X)/4 < m <= 5 sqrt(X)/6},
    V_X(alpha,beta) = sum_(m,n in I_X; X/2<mn<=X)
       alpha_m beta_n log(X/(mn)) (mn)^(-1/2)
       T_(log(mn/X)) psi.

The uniformity being tested is

    ||Pi_(4 log X) V_X(alpha,beta)||_E^2
       <= C_(h,epsilon) X^(1/2+epsilon),
    |alpha_m|<=1, |beta_n|<=1, for every epsilon>0.

Retain ordered-pair multiplicities of repeated products. These diagnostic
coefficients are not mu(mn); no substitution into the original signed
core is authorized. Failure would leave the Mobius target unresolved,
while excluding this particular uniform block inequality from a proof.

One bounded test: examine alpha_m=beta_n=1 and try to establish a lower
c_h X, with c_h>0, for its projected energy for every sufficiently large
real X. This is a proposed discriminant, not a result. It requires a
positive-measure frequency argument or Hilbert-space comparison; a value
at u=0 is insufficient. Retain (mn/X)^(1/4) after J, the actual W, and
the full finite square. C034r supplies nonzero W on a band; justify
any stronger premise separately.

Continue the coefficient-blind route only if this test supports the
displayed power and uniformity. If the proposed lower holds, record a
uniform-block stop and require a different mechanism retaining arithmetic
coefficients or signed cross-block cancellation. If neither direction is
proved, save the precise gap. No sweep of rectangles or tail refinements
is part of this action; one block does not control the signed recombination.

## Qualifications

Essential inputs: C034r's nonzero theta-convolved h, weighted translations
and band noncancellation, and C034w's exact finite Fourier formula.
C034u's signed square and C034v's whole G-B transfer explain downstream
restrictions, without identifying the diagnostic coefficients with mu.
Full-core/cumulative upper and mixed positivity remain unresolved.

Full matching Mathlib coverage is unchecked; Plancherel and strong
continuity of translations are standard supporting inputs. This is an
ordinary analytic exponent/obstruction calculation, not a creative
signed-cancellation mechanism. Separate literature approval was completed in recovery2102 below. No
mathematical result or script is produced in this assessment.


## Separate source approval2102 (2026-11-21)

LITERATURE_REASON: Supervisor recovery requires a direct source URL in the ready assessment; verify the cited primary text without changing the target or repeating discovery.

Primary source: Ben Green and Terence Tao, *Quadratic uniformity of the
Möbius function*, arXiv:math/0606087v2, 22 September 2007,
[Section 4](https://arxiv.org/html/math/0606087v2#S4).
Read Lemma4.1, its proof, Proposition4.2 and both proof cases
(HTML lines361-466). The lemma assumes positive integer U,V,N with
UV<=N. The proposition additionally assumes bounded f and a correlation
at least delta>0. It gives a Type I/II inverse alternative. Its proof
uses coefficient moments, dyadic decomposition and cutoff removal,
then a four-point rectangle. It gives no fixed-state averaged power
upper or lower. These results are comparison inputs, not a theorem
being applied to V_X. No reproof is warranted.

Reused the bounded search and failure comparison in source-notes2101;
no target or hypothesis changed. Rechecked C034r's hypotheses and
section2, and C034w(7)-(9): these fix the actual weighted space,
translation convention, multiplier and finite Fourier normalization.
They do not already decide this arbitrary-factor diagnostic. The
unrestricted/different-state comparison2096 and direct-import stop2101
remain in force within their recorded scopes.

DECISION remains EXPLORE for exactly the TARGET above. Essential source
coverage is adequate for that finite test; no additional literature is
required before attempting it. This approval establishes neither the
proposed lower c_h X nor the uniform upper. The positive-measure-band
requirement, ordered multiplicities, real-X endpoints and all unresolved
arithmetic/whole-vector obligations above remain unchanged. Full matching
Mathlib coverage remains unchecked. This is a process repair and source
approval, not mathematical progress or novelty evidence.
