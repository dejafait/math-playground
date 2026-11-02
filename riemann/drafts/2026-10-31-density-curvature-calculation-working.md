# Density/curvature interface: calculation checkpoint

2026-10-31. Work is restricted to the pre-existing SPECIALIZE assessment
`literature/2026-10-31-density-curvature-peano-transfer.md`; the startup
snapshot and relevant L477/L481 definitions were read, with the prior
density source comparison and L572 certificate stop. Existing changes
are preserved. No fresh source search or analytic density estimate is
needed for this finite calculation.

Finite differentiation gives F_M''=-U_T with all ordered pairs. The
de Boor Section 9 normalization gives Delta_h^2 F_M(t) as the integral
of F_M'' against (h-|x-t|)_+, without an additional factor. Integrating
over J=[T+h,2T-h] produces a symmetric five-piece weight: quadratic
rise, quadratic approach to h^2, central plateau, and their reflections.
It vanishes at T,2T and reaches h^2 at T+2h,2T-2h. This establishes
the proposed bound by h^2; all boundary pieces will be retained in the
canonical corollary. The density lower bound and full-residual transfer
are still unproved. No mathematical script is required.

Completed: the full normalization, boundary pieces, finite Fubini
argument and conditional scale implication are canonical in
`../lemmas/C481a-finite-interval-density-curvature-transfer.md`.
This note is a preserved checkpoint, not a second proof or current
next-action record.
