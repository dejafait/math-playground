# Prescribed-pair Hardy budget: calculation checkpoint

One mathematical specialization under the pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-31-disk-hardy-negative-witness-interpolation.md`.
No new literature search or cross-notebook input.

Main gap: actual-Xi all-degree positivity. Intermediate target: compare
minimum admissible and nonnegative-D_1 normalized boundary norms with
exact prescribed multiplicity. Downstream use requires a separate proved
actual-Xi norm bound at a nonzero center. Continue only for a nonempty
attainable sign-forcing interval; otherwise park the norm-only test.

Partial reasoning saved before final proof checks:

- Set q=r^2, b=q^m, c=m(q^(-1)-q)>0 and
  B(z)=((z^2+q)/(1+q*z^2))^m. Its boundary modulus is one.
- Set h=b*f/B, which extends across both removable prescribed zeros
  and the closed disk. Then h(0)=1 and ||f||^2=b^(-2)||h||^2.
  Exact order is equivalent to h(+/-ir)!=0.
- If h=1+u*z+v*z^2+..., its real coefficients satisfy
  D_1(f;0)=u^2-2v-2c and ||h||^2>=1+u^2+v^2.
- For D_1>=0 minimize x+v^2 with x=u^2>=0 and v<=x/2-c.
  Proposed minimum is c^2 for c<=1; 2c-1 for c>=1.
  Proposed endpoint polynomials are 1-c*z^2 and
  1+/-sqrt(2(c-1))*z-z^2. Both have positive real part at ir.
- Minimum unconstrained h=1 has D_1=-2c. A z^3 tail preserves
  that sign and exact order while realizing every larger norm.
  A nonnegative z^4 tail at the competing-sign optimizer preserves
  D_1=0 and exact order while realizing all budgets above its norm.

Completed checks: both constrained minima and all equality cases;
strictly positive sign at every larger exact norm; neighborhood
analyticity, exact multiplicities and Xi derivative scaling. The complete
proof and qualifications are canonical in L571. This checkpoint is
retained as unfinished-work evidence; L571 now supersedes its proposed
formulas. No independent audit, script, numerical evidence or actual-Xi
norm estimate is claimed.
