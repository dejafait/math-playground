# Exceptional angular integral — shrinking-box modulus discriminator

TARGET: Test whether the actual-Xi angular modulus mass outside the scalar-saddle box max_j|theta_j|<=k^(-2/5), k=r-1, exceeds its inside mass by at least exp(r^2 log(r)/10) eventually, thereby deciding whether that box can support a core-versus-absolute-complement sign certificate.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Prepared by step418's bounded actual-Xi/Heine/Toeplitz/growing-dimension comparison and local duplicate check; step389 covers the exact identity, but no inspected theorem provides this growing-order mass ratio. Absence of a match is not a novelty finding.
SOURCE_EVIDENCE: Katkova, math/0505174v1, https://arxiv.org/pdf/math/0505174v1#page=7 (Lemmas1–2/(10)–(13), pp.7–8; reuse step389); https://arxiv.org/pdf/math/0505174v1#page=11 (Lemma4(c), proof pp.11–12); https://arxiv.org/pdf/math/0505174v1#page=14 ((33), p.14). Recovery step419 reopened the latter two passages; reuse step418 for the changed-scope comparison in 2026-11-04-exceptional-toeplitz-unit-circle-discovery.md.
COMPARISON: Known identity and actual-Xi compact-sector modulus estimates are available. Fixed-order positivity and the inspected real-potential varying-symbol theorem do not establish this ratio when r=k+1. This tests one error-budget mechanism, not a determinant sign theorem.
GAP: Prove or fail to prove the dimension-uniform modulus-mass lower bound while retaining actual G and Vandermonde; validate the scalar radius and all uniform constants. No ratio bound has yet been calculated or derived.
REASON: A successful obstruction would require collective angular cancellation or another contour rather than absolute complement payment from this shrinking scalar core. Failure to prove it is inconclusive and supplies no minor sign.
SCOPE: One analytic proof attempt for r tending through integers, k=r-1. No finite minor scan, generic measure substitution, q-Pascal perturbation, phase-free determinant replacement or full manuscript audit. Coverage approved in literature-only recovery step419; the mathematical attempt remains unperformed.
COVERED_TARGET: Test whether the actual-Xi angular modulus mass outside the scalar-saddle box max_j|theta_j|<=k^(-2/5), k=r-1, exceeds its inside mass by at least exp(r^2 log(r)/10) eventually, thereby deciding whether that box can support a core-versus-absolute-complement sign certificate.

## Objects, threshold and remaining hypotheses

Use L018/L021: G(z)=xi(1/2+sqrt(z)/2)/8=sum a_n z^n,
a_n=M_(2n)/(8*4^n*(2n)!). Cite the known angular identity without
reproof. For sufficiently large k, let R_k>0 solve
R_k G'(R_k)/G(R_k)=k, the source's scalar saddle condition (33).
Verify existence/uniqueness for this normalization from positive
coefficients and the cited unbounded positive-axis growth. No
determinant sign or conjectural zero location is assumed.

For theta in [-pi,pi]^r define the nonnegative weight

    w_r(theta) = product_j |G(R_k exp(i theta_j))/G(R_k)|
                 * product_(alpha<beta) |exp(i theta_alpha)-exp(i theta_beta)|^2.

Let B_r be max_j|theta_j|<=k^(-2/5),
C_in=integral_(B_r) w_r and
C_out=integral_([-pi,pi]^r minus B_r) w_r.
These definitions specify the future test; they assert no estimate.
The target is

    C_out/C_in >= exp(r^2 log(r)/10)

eventually through integer r. Verify C_in>0 and finite integrals.
An existential onset suffices; no effective onset or small-r result
is requested.

Prospective ingredients, without deriving them here: a Vandermonde
upper bound on the shrinking box; lower mass on a fixed subarc in
the source's compact zero-free sector; uniform actual-Xi modulus
estimates there; explicit r-dependent volume and spacing costs.
A pointwise configuration alone cannot lower-bound an integral.
Include every positive-volume region and accumulated error. Compare
on the r^2 log r scale, not merely r or at fixed dimension.
Lemma4(c) specializes through G(z)=xi_1(z/4)/8; retain the dilation
and normalization. Only the compact-sector input and scalar saddle
construction are covered, not the auxiliary generic-C derivative
estimates flagged by step389. Cite the known Stirling/Euler-product
inputs and justify their exact specialization rather than reprove them.

## Decision rule and downstream use

If the ratio bound is proved, compare it with the budget for a positive
central contribution to exceed the full complement modulus. Distinguish
integral of modulus from modulus of the signed integral. The result
would stop only this box and this payment rule; actual cancellations,
other boxes and other contours remain open. It supplies neither a
negative D_(r,r-1) nor an RH conclusion.

If the bound cannot be justified in one bounded attempt, save exact
partial inequalities and the obstruction; record an inconclusive result.
Do not repeatedly adjust exponents or boxes merely to secure a result.
Reopening needs a materially new input or refined test. Evidence of
concentration would still need a separately assessed signed phase/tail
threshold before any positivity claim.

The main gap is all-degree mixed positivity. Exceptional coefficient
signs, other indices, initial orders and actual signed cancellation
remain unresolved. L765/L774 and unaudited L766 are contrasts only.
Full matching Mathlib coverage is unchecked; no cross-notebook theorem
is used. This develops an existing saddle method; it is not a protected
creative attempt or certified novelty.

## Direct-source gate repair — step419

Primary source: Olga M. Katkova, *Multiple positivity and the Riemann
zeta-function*, [arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174v1).
Reopened [Lemma4(c) and its proof, pp.11–12](https://arxiv.org/pdf/math/0505174v1#page=11)
and [the scalar saddle equation (33), p.14](https://arxiv.org/pdf/math/0505174v1#page=14).
The former states an angular modulus asymptotic for |theta|<=pi/2;
its proof uses two-sided zeta bounds in Re(s)>=2 and sectorial Stirling.
The latter states eventual unique solvability for the source functions.
Use only the previously assessed actual-Xi specialization; retain the
dilation, and verify uniform constants and radius specialization during
the attempt. Do not import auxiliary generic-C derivative estimates.

The exact angular identity and fixed-order limitation remain covered by
step389; step418 already compared the varying-symbol theorem and recorded
its unpaid hypotheses. No fresh broad search or full manuscript audit is
needed for this unchanged target. These citations supply inputs, not the
proposed mass bound. Direct access removes the reported process defect;
EXPLORE is retained and the exact TARGET/COVERED_TARGET is unchanged.
No new mathematical claim, proof, numerical test or novelty finding is
made in this recovery. Mathlib coverage remains unchecked.
