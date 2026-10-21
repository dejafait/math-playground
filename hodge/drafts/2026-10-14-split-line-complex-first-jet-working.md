# Split-line complex first-jet attempt — step 268

Approved target: Test determinant-fixed two-parameter complex analytic realization of L094's I-complex plane with its prescribed first jet.

The ready SPECIALIZE assessment is drafts/literature/2026-10-14-split-line-complex-first-jet-realization.md. No new source scope is invoked.

Intermediate calculation: let b_1=v^(0,1), b_2=(Jv)^(0,1), with v=e_1+Je_2 from audited L094. Its real/Dolbeault bridge sends I to multiplication by i, so these give the chosen complex basis of W. Every complex combination is the (0,1) part of a real w in W. Its square is diagonal trace-free. Q(w)=0 kills its diagonal pairings with omega_J and omega_K; pairing with their (2,0) combination therefore kills its Serre trace. Since H^2(L^2)=H^2(L^-2)=0 and the diagonal H^2 is one-dimensional, its Yoneda square vanishes.

Trace-free transfer: End(E)=End_0(E) plus O id is a DG-module splitting, not merely a cohomology splitting. Aut(E)=(C*)^2 is reductive, so BMM 5.1/2.3 apply. Normalize the formal equivalence on cohomology before feeding it the linear two-variable MC element; an unspecified formality isomorphism cannot be assumed to retain the jet.

Completed bridge: order-by-order determinant-one smooth complex gauge over C[[s,t]], the complete finite analytic obstruction equations and Artin approximation modulo (s,t)^2 give the actual holomorphic family with this first jet. The complete proof is canonical in lemmas/L101-split-line-complex-first-jet-realization.md and awaits separate critical audit. No unitary ASD family, quaternionic germ, punctured stability, common F or global mixed action follows.

Continuation/abandonment test: retain the prescribed determinant and jet in the actual finite-equation solution, or stop at a failed comparison. Independent Hodge realization, reconstruction, separation and transport gaps remain.
