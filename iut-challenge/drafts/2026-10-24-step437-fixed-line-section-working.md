# Step437 — fixed line / variable places working record

Approved target: Test whether L105's SL_2(F_ell) image permits a full place section over F_mod=Q whose members above S minus {ell} identify L107's fixed U with the local Tate toric line, without changing C_o or K_C.

Invocation-start coverage: drafts/literature/2026-10-24-selected-prime-simultaneous-tate-line-place-section.md (SPECIALIZE). Actual task: proof_attempt; known-method REPRODUCTION.

Main gap: original finite B>=A. Intermediate test: geometric toric-line independence and covariance, actual Galois place-action direction, then a full section. Downstream use: later graph comparison only; sign/splitting/full-data and repair remain independent.

Inputs: L090, L103, L105, L107; their existing qualified source conventions and same member/order/ell/fields are retained. No C_o-defined U, split downstairs reduction, ell-integrality or K_C/Q Galoisness is assumed. Prior stops ATTEMPTS/029,030,031,034,035 are preserved. L053/L060 are old-object methods only.

Planned discriminating identity for sigma in Gal(K_C/C_o): with w'=sigma w and completion transport t_sigma:K_w -> K_w', covariance should read t_sigma(T_w)=T_w', and on global points t_sigma(i_w(P))=i_w'(sigma P). Thus align at w' by requiring sigma^(-1)U=T(w), not sigma U=T(w). This is an obligation, not yet a result.

Continue only if Tate comparison ambiguity preserves geometric mu_ell and this identity follows for actual completions. Otherwise narrow/stop. No new general group theorem is needed.

Completed: the bounded attempt passes in L108, with the actual completion identity and independent place choices fully written. No new mathematical script or source-authentication attempt was needed. L108's result is REPRODUCTION and awaits separate critical audit; the new audit scope is REVIEW_REQUIRED. The final checkpoint and history/437 record the limitations and exact continuation.
