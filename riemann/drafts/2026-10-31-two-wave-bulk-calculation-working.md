# Two-wave bulk calculation: saved reasoning

Approved scope: the COVERED_TARGET in
`drafts/literature/2026-10-31-stationary-hardy-path-feasibility.md`.
Main gap remains actual-Xi all-degree positivity; the intermediate is a
derivative-consistent stationary bulk for L473, not an actual Hardy law.
Existing uncommitted notebook work was inspected and is preserved.

For fixed frequencies u,v and phases b,c, put A=ux+b, B=vx+c.
Direct expansion gives

    S S''-(S')^2
      =-u^2-v^2-(u^2+v^2)cos A cos B-2uv sin A sin B
      =-((u+v)^2/2)(1+cos(A-B))
       -((u-v)^2/2)(1+cos(A+B)) <= 0.

Thus the exact clipped expectation is zero, below 1/288; no quadrature
is required. This kills the nominated equal-amplitude two-wave bulk,
not general stationary processes. Completed: checked the identity at
coincident/opposite/zero frequencies and zeros of S (no division), the
whole L473 covariance integral, conditional phase-shift stationarity
and the common scaled support onset ell^3>=21/2. Full canonical proof:
`lemmas/L576-two-wave-stationary-bulk-zero-clipped-mass.md`.
Fourth constraints and Hardy transfer stay unresolved.

Source coverage is reused, not refreshed: Rahimi--Recht's random-phase
formula supplies the known covariance comparison; clipping is the
bounded test left open by that assessment. No claim of certified novelty
or full matching Mathlib coverage is made.
