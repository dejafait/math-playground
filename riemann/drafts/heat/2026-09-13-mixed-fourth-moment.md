# Mixed fourth moment checkpoint — 2026-09-13

The prior L179 step is complete. Current task: exact expansion of its actual
X,Y, without promoting an L² approximation to a fourth-moment identity.

Write P=F_p, Q=F_q, A=e^(−iθ/2)P, D=e^(−iθ/2)Q.
Then 16X²Y²=(A+conjugate(A))²(2|D|²−D²−conjugate(D)²).
Collecting gives 4|P|²|Q|²−2Re(P² conjugate(Q)²)
+4Re(e^(−iθ)(P²|Q|²−|P|²Q²))−2Re(e^(−2iθ)P²Q²).

Resume: check the signed finite-kernel expansion, then apply the product
frequency Hilbert estimate with bounded signed profiles. Expected available
upper bound is O((1+N²/h)log(2N)); improvement is unproved.

Completed: the exact expansion and the qualified arithmetic bound are
stored in L180. A deterministic complex algebra check passes. No small
L² error has been used to transfer fourth moments. The pending research
direction is recorded solely in PROGRESS.md.
