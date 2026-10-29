# Complete quartic target: distinct-line work checkpoint

STEP_ID: YM-20261026-500-quartic-distinct-line-limit

The supplied unchanged EXPLORE assessment approves exactly the complete
quartic target in PROGRESS.md. Reuse its source comparison and the current
official scope recorded in foundations/01-target-and-scope.md. Existing
L283/L284 partial proofs and ATTEMPTS/047–049 were checked; preserve them.
No external theorem beyond that coverage is proposed.

Main gap: uniform interacting reflection control and the continuum theory
remain open. Intermediate target: evaluate L284(6), then assemble all four
quartic terms. Downstream use: identify the quadratic-scale compensation
required from the still unresolved cubic response. Pass requires all-anchor
uniform o(N^2) error, or a rigorous different scale/obstruction. A bulk-only
coefficient fails. Essential inputs: L003 L279 L280 L282 L283 L284, with
their SU(2), relative-domain, source and own-slice qualifications retained.

Unfinished reasoning saved before the calculation: split plaquettes by
the sign of their time center. On either half, one source stays uniformly
separated. For the other source use
G_h=L^-1 C_12^* h C_12 L^-1 and replace L^-1 by L283's h_m(L).
Column energy of C_12(L^-1-h_m(L)) is at most 16 s_m because
C_12^* C_12 <= L and lambda e_m(lambda)^2 <= e_m(lambda).
Cauchy–Schwarz should give an all-entry error O(sqrt(s_m)). Fixed
polynomial paths then replace the weight locally by h(x), with zero
paths near boundary faces where the compactly supported source vanishes.
The prospective bulk covariance is H_12=L_infinity^-1 C_12^* C_12
L_infinity^-1, not the bare transverse G.

Provisional coefficient, NOT yet a result: for a constant external field
in direction 1, L283(13) applied to H_12 gives b_parallel=4 times the
sum of its single-plaquette coefficients in orientations 12,13,14.
The separated other covariance has only directions 1 and 2. Check the
finite color/factorial contraction, the spatial offsets, source partition,
mesh normalization and uniform error before recording a limit. No critical
audit of L283/L284 or this prospective result is claimed.

Completed attempt: the full proof is now canonical in L285. The local
entry error is bounded by 8||h||_infinity sqrt(30 s_m), followed by a
fixed-polynomial source-weight approximation and the finite-offset
Fourier limit. On each time half the other covariance is uniformly
O(a^2); the complete normalized error is therefore o(1). The explicit
anisotropic row-sum coefficient is b_*=-2Z_0/3+20I_1/3-1/6, and all
four quartic terms are assembled in L285(3)–(4). The finite rational
check passes all three 35-word contractions with zero failures. This
does not audit the analytic proof. The next target is separately
registered REVIEW_REQUIRED; no audit or new literature approval was
performed in this mathematical turn.
