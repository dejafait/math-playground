# 2026-10-04 — Radial quartic action contraction

Reuse the unchanged SPECIALIZE assessment in
`drafts/literature/2026-09-26-current-target.md`. The bounded target is
the radial action occurrence `-kappa(f_(i,0),r_0,S_(4,rad))` in L011,
not the already bounded radial flow vertex. Existing changes are retained.

The gap is the full coefficient's logarithm and possible faster cutoff
terms. Contracting this separate curvature polynomial can locate its
remaining ultraviolet loop without the nonlinear transfer blocked by
L022. The test is whether the connected contraction is bounded or
vanishes; an unbounded estimate must not be called a zero logarithm.
Finite matching and the reflected-error threshold c_box/2 remain later
requirements.

## Working reasoning saved before verification

In orthonormal coordinates put H=d Delta^(-1/2), T_i=E_tau B_i E_tau,
and write the quadratic residual with matrix R. For a plaquette row h,
let v=h h*, alpha=h T_i h*, beta=h R h*, chi=h T_i R h*.
The stored circulation D x is H xi, with no residual a factor.

The color Wick decomposition of (sum_c Y_c^2)^2 has quadratic term
2(n+2)v sum_c :Y_c^2: and a fourth-chaos term. Connected contractions
suggest n(n+2)/12 times sum_p (alpha beta + 2 v chi), including the
minus sign on S_(4,rad)=-sum_p |Y_p|^4/96. For n=3 the prefactor is 5/4.
An independent eight-field pairing check is needed for both classes.

The direct norm estimate is only O(a^-1), not enough to exclude a log.
There is a sharper route for the quadratic Wick term: prove
||R E_tau||_1 -> 0 using strong smooth-mode consistency of the symmetric
residual operator and a uniform polynomial bound on its mode columns.
Then |sum_p v_p chi_p| <= ||T_i R||_1 -> 0 without smoothness of v_p.
The alpha beta term still contains an unflowed local residual loop.
Its cutoff behavior is not yet determined.

## Completed result

[L023](../lemmas/L023-radial-action-connected-contraction.md) proves the
exact contraction and ||R_a E_tau||_1 -> 0. The key additional argument
is strong convergence of each fixed residual mode column, proved by
the actual compactly supported local stencils, with a uniform cubic
polynomial column bound. A summable heat-weighted rank-one expansion
then gives the trace-norm limit. Merely citing L009's entry convergence
would not have sufficed. The quadratic Wick pairing class is o(1) for
both probes even though v_p need not commute with heat or be smooth.

The fourth-chaos class still has only an O(a^-1) bound, not the desired
O(1) bound or a known logarithmic coefficient. The exact rational check
passes 16 cases, separately checking both pairing classes with
indefinite matrices and one through four colors. Its full certificate
is under scripts/combined-ward-response/. This is one local ADVANCE
by reproduction/specialization. The required interacting bound
c_box/2 and the main construction gaps are unchanged. The reason for
the next direction is the specific remaining unflowed diagonal beta_p,
which fixed-mode convergence and final-time heat suppression do not
control.
