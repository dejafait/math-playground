# Second ordered trace — bounded attempt

The unchanged ready target is the complete cubic residual/action response
in `drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md`.
The main gap remains the ultraviolet-uniform interacting reflected
comparison, then continuum and infrared control. This attempt tests cubic
control of L161(3)'s second trace as one input toward its complete limit.

Unfinished reasoning saved before writing the kernel proof: cycle only
to write Tr(Q_A(h) F N Sigma)=Tr(Sigma A B_h F N)
-Tr(B_(A h) F N Sigma). A has compact input support, so B_h there is
O(a). Try to prove |(A Sigma)_(e,x)| <= C/a [(1+dist(e,x))^-4+N^-4]
for compact e and every x. Use A=(L K_a+K_a^T L)/2-Q_3-Q_6,
two differences on the component Green kernel, discrete product rules
for the smooth compact generator coefficients, and L Sigma=P.
The required F_(v,y) bound has a COMPACT ROW, not the compact column
of L165; prove the global undifferenced relative Green estimate before
summing its full prefix. The anisotropic product with (1+|v_T-y_T|)^-1
would then be summable. N_b=O(a) gives O(N^3), while the actual upper
N_top=O(1) is separated and would give O(N^2). The smooth-residual
subtraction is bounded using A h=O(a^5) and full HS norms.

Continue this mechanism only if those kernel estimates retain every
source/end row; abandon its claimed cubic bound if a boundary term or
undifferentiated Green tail defeats the summation. O(N^3) is not
vanishing. Essential inputs: L018 L026 L028 L150 L156 L157 L161 L163
L164 L165. Both residual subtractions, every action face, signed E,
the upper jump, constant mode and full heat sum remain. The fourth
trace and the mixed/retained-trace limits are independent unresolved
steps. No positivity is assigned to F or E. Preserve ATTEMPTS/009,
/011, /036 and /037. No duplicate second-trace estimate was found in
the targeted recent drafts, histories or L16x proofs.

Completed outcome: L166 proves the proposed entire second-trace O(N^3)
bound. The global undifferenced image estimate supplies the missing
prefix-row case; two retained residual Green differences suffice. The
upper contribution is O(N^2), and the smooth-residual subtraction is
O(sqrt(log(eN))). Full proof and qualifications are canonical in
`lemmas/L166-cubic-residual-second-ordered-trace-cubic-bound.md`. No
scaled bulk limit or fourth-trace bound was established in this step.
