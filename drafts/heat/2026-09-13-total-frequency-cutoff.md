# Total-frequency cutoff checkpoint — 2026-09-13

The prior L159 step is complete. New calculation: strengthen χ to C².
For x=log(r/s), y=log(m/n), ω=x+y≠0, h=(x/y+y/x)/2,
define U=Σ h p exp(i(t−π/2)ω)/(iω), p=A_r A_s A_m A_n,
and U_amp with p replaced by p'. Then U'=K_non+U_amp.
Integration by parts predicts
R_non=−[χ'(Q/M)U]/(MT)+E_T[χ'(Q/M)U_amp]/M
       +E_T[χ''(Q/M)Q'U]/M².
The last term is unestimated uniformly in T. Importantly
h/ω=(1/x+1/y)/2−1/ω, so a naive product of all inverse gaps
is avoidable. Individual ω can still be order N^(−2):
r=m=k, s=k−1, n=k+1. Full collected primitive coefficient
has modulus asymptotic to 2k². This is algebraic, not a lower
bound on the evaluated cutoff integral.
Resume by proving elementary absolute bounds and auditing signs and
regularity; store a scoped lemma, preserving the uniform bound as unproved.

Completed as L160. Improved the initial elementary-bound plan by proving
U=B(Q+D)−V, where V is the full product-frequency Hilbert form.
Product spacing and L159's pointwise F bound give |U|≤CN²log(2T),
with the analogous amplitude bound divided by T. The C² chain rule,
exclusions, and signs were checked analytically. The new signed derivative
correlation is still unproved uniformly at fixed M.
