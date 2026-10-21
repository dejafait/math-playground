# Exterior product placement through the joint energy kernel

Bounded proof attempt under the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The main gap is interacting ultraviolet control; independent continuum,
reflection and infrared requirements remain. The intermediate target is
an O(N^3) error for moving L114's common-index exterior product through
the joint E_j kernel, retaining all finite compressions. A controlled
placement could enable a later frozen-trace bound, not yet a limit.

Essential inputs: L110 L111 L113 L114. The relevant duplicate checks
are L111's generator move and L113's move through the finite P: neither
moves this product around the trace through the energy kernel. Preserve
ATTEMPTS/029 and 032; neither component-filter commutation through P nor
factorwise absolute moments is used. Ready literature coverage is reused.

Tested mechanism: let psi=phi_(l,alpha,s) phi_(k,beta,t), A_r=D T_r C_r,
and X_r=J_2^* A_r E_j M_b J_2. Cyclically write each trace on edges as
Tr[P_bulk M_psi^1 S_beta X_r S_alpha^T]. Compare M_psi^1 S_beta X_r
with S_beta J_2^* A_r E_j M_(b psi)^2 J_2. The exact difference splits
into the finite-stencil error (M_psi^1 S_beta-S_beta M_psi^2) X_r and
S_beta J_2^* ([M_psi^2,A_r]E_j+A_r[M_psi^2,E_j]) M_b J_2.
All multipliers commute with restriction on the same component grid.
The proposed HS bound is C a p(k)p(l) N^(3/2)(W_j+Q_j).
Pairing with S_alpha^T P_bulk costs N^(3/2); outside a and the weighted
level sum N^2 then give a^2 N^5=O(N^3).

Continue if this exact identity holds with every finite input row and
all heat labels retained. Abandon if it requires compact output of the
moved kernel, movement of a component filter through P, or a separate
absolute first kernel moment. A cubic error is not negligible. The
remaining finite compressions and signed frozen transfer, existence of
the H cubic limit, all other functionals' values, and comparison with
-12 gamma D_i remain unresolved. L091 assembles the group; L084 fixes
the mixed comparison with L079/L080/L082 qualifications.

Completed: L115 proves the exact identity and the O(N^3) placement
error by the complete W_j+Q_j sum. The hypotheses are unchanged, and
no mathematical script or numerical diagnostic is needed. This is
RESEARCH / REPRODUCTION, local standard-method progress only. The
proof uses L110 L111 L113 L114; no full frozen transfer or limit follows.

Continuation within the unchanged approved complete-group target:
test an O(N^3) comparison between L115(2)'s finite-compression trace
and the corresponding full-grid trace, using the compact combined
input multiplier. Retain both coefficient levels, all component/path
filters and every heat mode. Essential inputs for this test are L110
L111 L113 L114 L115; L088 L099 specify the frozen comparison and
L091 supplies group assembly. Continue if the boundary difference is
controlled in its actual order; stop if compact input is falsely
transferred to nonlocal output or if filters must cross P_inf without
an estimate. Do not assume this comparison, a cubic bound for R_prod,
a finite H limit, negligible L110/L111/L113/L115 errors, or evaluated
joint compensation. L097 L098 L100 L101 L104 L107 retain other limits;
L084 L079 L080 L082 fix the reference and its numerical qualifications.
