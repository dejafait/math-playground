# Saved work: signed Mellin residue test

The approved target is the exact TARGET in
[the prior EXPLORE assessment](literature/2026-09-27-signed-mellin-sampling.md).
The immediate gap is the deterministic sampled mean D_N^w=o(1).
Average control would still leave exceptional indices, the pointwise
endpoint margin and the lower Laguerre signs unresolved. The overview,
DAG, previous failures and existing changes were inspected and preserved.

The concrete test is whether the nonconstant reduced-ratio terms of the
centered two-Mellin-variable correlation acquire the residue-annihilating
Möbius factor suggested by the inspected Li–Radziwiłł example. The known
arithmetic-progression theorem is not being reproved or applied to the
nonlinear samples. This test keeps the same sample index in both factors.

Unfinished calculation, saved before its analytic verification:

- Fix sigma=1+r^(-1/2)>1. For Re alpha, Re beta>1, the product
  zeta(alpha+ia)zeta(beta+ia)/zeta(sigma+ia)^2 has multiplicative
  Dirichlet coefficients with prime generating function
  (1-p^(-sigma)X)^2/((1-p^(-alpha)X)(1-p^(-beta)X)).
- Multiplying by its opposite-height counterpart and reducing every
  ratio gives local sums of the form sum_j d_(j+k)d_j. Centering
  subtracts the two single-ratio products and adds one. It does not
  replace either product by a modulus square on the complex contours.
- A discriminating slice is alpha=beta=s real decreasing toward 1/2.
  Writing t=p^(-s), q=p^(-sigma), the local coefficients are
  d_0=1 and d_k=t^k[(k+1)-2k(q/t)+(k-1)(q/t)^2]. They are positive
  for k>=1 when 1/2<s<sigma. This suggests that nonconstant ratios
  retain the diagonal correlation's fourth-order pole at 2s=1.
- To finish, prove convergence after extracting zeta(2s)^4, verify a
  strictly positive limiting Euler product and all fixed-ratio local
  factors, and compare the lower-order poles in the two subtractions.
  Retain the r-dependence and, if possible, a positive lower bound on
  the residue factor as sigma decreases to one.

Pending statements above are not yet a lemma. Any continuation to this
boundary concerns coefficient functions only: termwise shifting the
full sampled Fourier series is not justified there. If the nonconstant
pole survives, stop automatic residue annihilation, without claiming a
lower bound on the actual sampled mean or refuting its o(1) target.
An algebraic identity alone will not be reported as an advance.

Completed check — 2026-09-27: [L353](../lemmas/L353-signed-mellin-correlation-pole-survives.md)
proves the exact two-variable grouping with uniform contour tails and
the surviving fourth-order pole for every fixed reduced ratio. Its
leading coefficient has a positive limit as sigma decreases to one;
the two centering terms have only first-order poles. This supplies the
discriminating negative result, beyond a formal restatement of the
sampled identity. It stops automatic local pole annihilation only.
No termwise shift of the full Fourier series is justified, and no
lower bound for D_N^w follows. The signed sampling target remains open.
The calculation uses elementary Euler-product methods and is recorded
as REPRODUCTION, without a claim of originality or a sampled estimate.
