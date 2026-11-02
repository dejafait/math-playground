# Actual-theta cancellation specialization — working checkpoint

Approved target: verify C604a's actual-theta specialization from L605
and Csordas Theorem 4.2(a), retaining every cancellation qualification.
The ready assessment is
`drafts/literature/2026-11-01-c604a-actual-theta-specialization.md`.

Use L605's fixed full-line p, not its auxiliary probability density.
Write Q(s)=Phi(sqrt(s)), T(s)=integral_s^infinity Q, and r=Q/T.
The imported source states (log T)''<0 for s>0. Since
(log T)'=-r, r'>0. L605 gives tau(u)=2/r(u^2/4), so the
chain rule gives tau'(u)=-u r'(u^2/4)/r(u^2/4)^2<0 for u>0.
The zero endpoint comes from L605, not from extending source strictness.

L605 already verifies all of L604/C604a's fixed-density assumptions.
Thus C604a's q=-tau' is positive on (0,infinity), and its A is positive.
Carry the exact floor term and explicit endpoint-error constants into
the canonical application; no zero floor or effective onset is needed.
The residual D is rapidly decreasing but has no established sign.
No new theta-shape/hazard proof, Fourier sign or compensation estimate
is attempted. Completed as `lemmas/C604b-actual-theta-layer-cancellation.md`;
the assembly sentence and the ID-only DAG now record that application.
