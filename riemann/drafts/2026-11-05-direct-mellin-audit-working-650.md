# Fixed L829 audit — working record

Step650, 5 November 2026. Prior SPECIALIZE assessment:
`drafts/literature/2026-11-05-direct-mellin-fixed-test-audit.md`.
Only its fixed audit is being attempted. Main gap: actual-Xi all-degree
mixed positivity; this necessary-condition check cannot supply membership.

Read L829 in full, L828 Section2, C828a Section1, L019 and both programs.
Reused step647's precise Patrick/Runckel comparison and recorded stops.
No representation-conditioned assertion in L828 is used. For |s|<=1/8,
the bounded-density endpoint majorant x^(-1/4)(1+|log x|^2) and the
superexponential tail justify both Mellin derivatives. Factors 2 and 4,
normalization cancellation, E(0)=1 and the trigamma sign in (2) check.

Analytic review: the n>=2 geometric envelope has first term <1/2 and
ratio <1/2, hence its sum <1. The n>=5 envelope has ratio <1/2 and
negative x derivative; 8*pi^2*625<50000 gives (4). Endpoint integrals
are exactly a,21a,442a. On x>=2, log weights <=x^2<=exp(x);
H(2)<-151 and H'<-318 pay (5). The t=log x change of variables,
positive summand formula, dyadic grid, t-square across zero, outward
Machin rational bounds and Decimal exp-neighbor enclosure check.
Both contexts trap exceptional cases; no ambient-context arithmetic
was found in the evaluator's numeric expressions. Backend correctness
remains an explicit assumption.

Replay obligation (now completed): replay all saved cells and all analytic-error
constants against the reviewed program, preserve a new audit report,
and run exact rational arithmetic verification without overwriting
step648 artifacts. Accept only full chain plus necessary-only scope;
identify a specific correction on any failure. No new sampling stage.
The final selected evaluation/bounds and first-stage counterparts have
been inspected in full; none substitutes for the complete cell replay.

Completed: every original cell and both complete stage objects match;
the exact rational verifier also passed. Failures are empty in
`scripts/direct-mellin/fixed-laguerre-audit-650.json` and
`scripts/direct-mellin/recorded-arithmetic-replay-650.json`. Canonical
audit and qualifications are in L829 Section4a. No flaw was found and
the diagnostic is closed at its original necessary-only conclusion.
