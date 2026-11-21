# Finite left horizontal segment — working checkpoint, step527

Completed in L802; the proof and qualifications are canonical there.
The provisional checkpoint below is preserved as unfinished-work history,
not an additional proof or an outstanding task. Independent audit pending.

Approved target: the standalone T_L bound with coefficient 9 and
exponent 77/50 on all D, under the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-05-mellin-left-horizontal-segment-test.md`.
This is a source reproduction attempt, not a creative sign mechanism.
Main gap: actual-Xi all-degree mixed positivity. A paid left component
could support a separately assessed Mellin approximation with L800/L801.

Read L797's map proof, L798's phase proof, L799's normal convergence
and factorization, L801's right-ray proof for comparison, step526's
source assessment and the preserved global-import stop. No standalone
left proof found in that specific local scope. No new browsing needed.

Provisional analytic route, not yet a critically reviewed result:

- L797/L798 imply Im A has the sign of h. Thus for h>0, y_L>h,
  u/2<v_L<u; for h=0, y_L=0. Conjugation covers negative h.
  The whole segment has the endpoint's strict height clearance
  pi/4-|y_L|>13/(112u), with v>=u/2>0.
- Consequently tau=pi exp(2v)cos(2y_L) is greater than
  (1287/5600)pi exp(u)/u>3, using exp(3)>14 and u>3.
  The full normally convergent theta series then gives |1+rho|<2.
- Q/u>1000/3 implies Re(q-c)>0. For h>0 write alpha=arg x,
  psi=arg(q-c), gamma=arg(v+i y_L). Then gamma>=alpha,
  gamma<pi/4 and 0<psi<pi/2, so
  -pi/2<alpha+psi-2gamma<pi/2. Hence Re(s/z^2)>0 and
  the horizontal phase is strictly concave on the entire segment.
- Taylor of S' on the radius-d disc gives the positive endpoint slope
  greater than kappa=(105/256)Q/u. L798 pays the endpoint decrement
  (85/48)Qd^2. The left tangent envelope and |C|^{-1}<sqrt(Q)
  would then give T_L<(512/105)(u/sqrt(Q))exp(-(85/48)Qd^2),
  which is stronger than the nominated 9,77/50 allowance.

Finish checking and writing every inequality in a canonical lemma;
retain the full series, exact normalization and closed-boundary cases.
No numerical certificate or script is needed. The portion before u/2,
continued endpoint, global contour/assembly, quotient/inversion,
certificates and sufficient signs remain independent open obligations.
Continuation test is a uniform proof paying the allowance or an exact
obstruction to the selected sufficient envelope, never endpoint samples.
