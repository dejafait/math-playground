# Step 579 working record — fixed base-tangent detector

Gate: the invocation-start SPECIALIZE assessment is
`literature/2026-10-26-semiregularity-base-tangent-detector.md`.
This is one mathematical specialization, not a new source review.
Existing notebook changes remain untouched except for the eventual
checkpoint and the argument/dependency updates required by this step.

Main gap: primitive algebraic realization; this branch also leaves F's
existence open. Target: identify the base trace–Atiyah map's Serre
transpose with the actual included tangent cohomology. Downstream use:
remove the 20 tangent directions from L167's allowable quadratic lift.
Continue only with that actual comparison; park failure of the global
lift or an uncontrolled point/complement cancellation. Independent
normal and point brackets remain uncomputed.

Partial reasoning saved before the full write-up:

- L171 constructs alpha:T_B[-1] -> C and proves H^1(alpha)=iota,
  L108's specific tangent inclusion. The global truncation triangle is
  M[-1] -> C -> W[-2] -> M. Applying Hom(T_B[-1],-) has outer
  terms Hom(T_B,W[-2]) and Hom(T_B,W[-1]), both zero by negative
  Ext between sheaves. Thus alpha=j iota[-1] globally. This uses
  H^0(C)=0; it does not glue stalk equalities or assume a globally
  projective sheaf.
- Let a_B be the trace-free base Atiyah class, with L171's universal
  KS sign. The degree-one semiregularity component projected to p*Omega_B
  is, up to this one sign, Tr(a_B x). Fibre trace by sigma_1 sends it
  to H^1(B,Omega_B). Its Serre transpose should be H^2(alpha), hence
  the actual i H^1(iota), with one fixed nonzero trace/sign scalar.
- L165 then gives pairing against i H^1(iota) as S(Rx,H^1(iota)u).
  L108's symplectic splitting makes its annihilator exactly H^1(N).
  The point quotient cannot cancel this detector because ker R is
  already Q-orthogonal to all i(K).
- Buchweitz–Flenner Corollary 4.8 kills the actual bracket's image.
  If the transpose check holds, R[j_1h,j_1h] lies in H^1(N).
  L167's degree-four identity then uses at most h^1(N)=704-s+2t
  quadratic squares; at the formal s=800,t=48 endpoint it forces
  the point quartic to vanish, not the point bracket itself.

The completed specialization is canonical in
`lemmas/L173-semiregularity-detects-actual-base-tangent-obstruction.md`.
It gives the global lift, rank-20 detector and exact normal-space square
constraint, including the empty-Z/t=0 cases. It uses the same trace
normalization and Atiyah representative on both sides of the transpose.
No separate critical audit has been performed; the new assessment
`literature/2026-10-26-semiregularity-tangent-detector-critical-audit.md`
is deferred for approval next turn. This record preserves the partial
reasoning above and is not a second canonical proof.
