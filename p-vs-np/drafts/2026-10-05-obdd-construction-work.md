# Approved OBDD construction — working checkpoint

Gate: `drafts/literature/2026-10-05-obdd-reduced-data.md`, unchanged EXPLORE target. Inputs read: L025, L024's hypotheses/update, L020's full shared commutator proof; coefficient-degree assessment and Attempts 017–018. No cross-notebook input. Existing unfinished files are preserved.

Main gap: unconditional uniform SAT complexity. Intermediate target: construct L025's supplied reduced data from the promised common-order width-w diagrams. Downstream: conditional polynomial-degree circuit certificates on this restricted class. Unrestricted small width, tree conversion, all-certificate hardness and decision transfer remain unproved.

Proposed recurrence (not yet a final proof at this checkpoint): at level k let e0=1+x_k, e1=x_k, u=e0*u0+e1*u1, v=e0*v0+e1*v1. Let P_uv be the paired-diagram ordered representative. Let K_(a,k)(A)=r_a*x_k+x_k*r_a, using L020's ordered commutator identity on suffix states. Set

W_uv=(e0*K_(u0,k)+e1*K_(u1,k))*(v0+v1)
     + b_k*(u0+u1)*(v0+v1)
     + e0*W_(u0,v0)+e1*W_(u1,v1).

Seek W_uv(A)=uv+P_uv and W_uv(0)=0. Intended proof moves u_a past e_b with K, then uses e_a*e_b=delta_ab*e_a+(x_k^2+x_k). No Boolean factor is moved across a coefficient. Candidate bounds: suffix values degree s, K degree s, W degree at most max(1,2s-1), with sharing and no path unfolding. Reconcile P_root with the separately supplied output by injectivity of Boolean evaluation on ordered multilinear polynomials; negative roots must be exact complements.

Remaining checks before accepting: complete formal induction, terminal and sign cases, width/state count independent of extension depth, every separately written root and original identifier, and finite free-word tests with deliberately broken corrections. Continue only if all give a fixed polynomial full bound; otherwise record the concrete failure. No general-circuit multilinearization or exact lift of an unreduced extension is being attempted.

Completion: the proposed recurrence and its required cases/bounds are now proved in canonical `lemmas/L026-obdd-reduced-original-axiom-data.md`. The independent finite diagnostic passed; full evidence is in `scripts/obdd-reduced-data/suffix-witness-results.json`. This early working checkpoint is retained as saved reasoning, not a second canonical proof. A separate critical audit is the new continuation.
