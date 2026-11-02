# Full corrected-law quartic test: working checkpoint

Approved target: the exact TARGET in
`literature/2026-10-31-corrected-law-quartic-defect-scope.md`, saved
SPECIALIZE before invocation. Completed source comparison is reused.
Main gap: actual-Xi all-degree positivity and unbounded-height initial
signs. Intermediate test: eventual nonzero expectation of
P(v)=x_0^3 z_0+3x_0^2 y_0^2 under exactly L473's nu_H. A positive
liminf after division by ell^2 excludes this particular stationary C2
extension; zero stops this separator and proves no realization.

Read L473's full construction/application audit, L580's full proof and
the uncorrected-bulk failure. No duplicate full-law calculation is
recorded in these relevant inputs. Existing unfinished files preserved.

Working calculation, not yet a verified result: fourth homogeneity
makes the rare contribution equal to the actual finite-interval average
of P(Y). For fixed ell, the chain rule should express this as
[Z(t)^3 Z'(t)]_H^(2H)/(H ell^2). The assessed fixed-order pointwise
bound would make it O(H^(-1/3)ell^(-2)), retaining both endpoints.
The other contribution is exactly ell^2/w_H times E P(A_H B).
L580 gives E P(B)=1/6 and L473 gives ||A_H-I||=O(ell^(-1)) on a
fixed bounded B, suggesting the limit 1/6 after division by ell^2.
Check the noncommuting correction by a polynomial norm bound, not by
commuting R_H and K or by dropping the rare fourth moments.

Outstanding checks: fixed-divisor rescaling, both boundary terms,
uniform endpoint constants, a complete perturbation inequality and
common eventual ray. No stationarity of dyadic sampling, limit-law
realization, derivative-preserving correction or actual-Xi transfer is
assumed. No mathematical script is needed for this symbolic test.

Completed: all outstanding symbolic checks are written in canonical
L581. Its explicit error bound proves normalized limit 1/6 and an
eventual lower bound ell^2/12 for the full defect. This is a local
specialization, not a new arithmetic theorem. Independent critical
application audit is nominated separately with REVIEW_REQUIRED.
