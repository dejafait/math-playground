# Coupled first-Laguerre comparison — working checkpoint

Approved target and unchanged SPECIALIZE coverage:
`drafts/literature/2026-10-05-gaussian-coupled-laguerre-transfer.md`.
The main gap is global actual-theta mixed positivity. This step only
specializes L357's product subtraction using L358's positive envelope
and audited L366's j≤2 bounds. A controlled conditional sign margin
could support the missing low-index comparison; it supplies neither
the margin itself nor higher levels or an RH candidate.

Set T=1+|ξ|, L=log(2+|ξ|), δ=εT², H=F_0+εG and R=F_ε−H.
All frequency derivatives hold ε fixed. The intended normalized jets
are H^(j)/(A L^j), not derivatives of H/A. L366 bounds
|R^(j)|/(A L^j) by C_j δ². Product subtraction should therefore
bound the error divided by A²L² by
δ²(2C_1|H′/(AL)|+C_2|H/A|+C_0|H″/(AL²)|)
+δ⁴(C_1²+C_0C_2).
This is unfinished reasoning pending the complete algebra check.

Retain Lag(H)=Lag(F_0)+ε(2F_0′G′−F_0G″−GF_0″)
+ε²(G′²−GG″). There is no division by F_0 and no assumed
nonvanishing. The continuation test is a controlled error in a
specified shrinking-regulator regime, with explicit positive/negative
margin conditions. The upper boundary need not yield vanishing error.
L365's common-global-threshold stop is preserved. Relevant proofs read:
L366 in full, L357's concluding product estimate and L358's (3).
Local search found no existing nonlinear coupled specialization.

## Completion

The product algebra and the covered L320 growth specialization are
written in full in the canonical result
`lemmas/L367-gamma-normalized-first-laguerre-transfer-error.md`.
The provisional expression above survived the calculation. The bound
is a conditional margin rather than a sign theorem. No mathematical
script was needed. A separate critical audit remains pending; this
working snapshot is not an independent proof. The current status and
next action remain solely in PROGRESS.md.
