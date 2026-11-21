# Working checkpoint: discrete support-edge transfer, step 194

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-signed-bump-support-edge-transfer.md`.
The exact target, original fixed bump and integer subsequence are unchanged.
This is a mathematical attempt, not another source review. Existing files
and unfinished work are preserved.

Completed write-up: [L721](../lemmas/L721-discrete-signed-bump-support-edge-transfer.md).
The intermediate notes below are preserved as unfinished-stage reasoning;
the canonical proof supersedes their provisional wording. A separate
conceptual audit is pending, not performed by this derivation turn.

Main gap: actual-Xi all-degree mixed positivity, with the complementary
spatial Jensen defect and realization still unpaid. Intermediate target:
the exact signed bump limsup in the assessment. Downstream use: comparison
with the actual residue, after a separate audit of that residue rate.

Inputs read: L703's fixed bump hypotheses; L714's audited (1)--(5);
L719's saddle/phase conclusions and phase identification; L720's full
factorial-symbol construction and exact-contour remainder. Reuse the
supplied source comparison and the specific common-phase/gamma-Rice stops.
Do not use L713, L714 (6), L717 or L718 as mathematical inputs.

Proposed bounded construction (unfinished, not yet a lemma):

1. L719 gives S'=(u*s_v-d)/A. Its saddle rectangle should give
   1/270<Re S'<1/60 and 11/180<Im S'<2/27 on I. Thus the actual right
   support endpoint maximizes Re S, and exp(-12*S) has no collisions.
2. Borel-transform L720's factorial coefficients locally. Integrate the
   resulting analytic germ along t=S(v)-S(v-h), with h>0 fixed and small,
   so the transformed exponential stays on the same phase curve. Check
   uniform factorial remainder bounds at every order, then truncate at
   order proportional to n to compare with the exact integer samples.
3. After exchanging only compact integrals, seek a fixed density near the
   right endpoint of the form a_0*chi plus an upper-triangular integral
   of chi. A nonzero diagonal and bounded kernel may preserve this
   endpoint by an elementary Volterra uniqueness estimate.
4. Form the sampled Cauchy germ only after this reduction. Its nearest
   endpoint must be nonremovable for the germ from the origin, not merely
   have a jump between arbitrarily chosen branches. Prove that extension
   through the endpoint would force the density to vanish just to its
   left. Control every remote contribution and exponential error.

Continue only with all these estimates, or retain a precise partial result
or obstruction. An unproved analytic inverse, a jump without endpoint
continuation geometry, or finite-order errors do not prove the limsup.
No signed rate, novelty beyond the checked sources or RH candidate is
claimed by this working checkpoint. No mathematical script is needed yet.

## Construction found; proof write-up and review pending

Use b=sup supp chi, v0=b-ell and a=b-2ell, all in I, with ell fixed
small enough for the analytic coefficient germ. Define
B(v,t)=sum_(k>=1) a_k(v)*t^(k-1)/(k-1)! on a fixed t disk.
For v in [v0,b], integrate B along t=S(v)-S(w), a<=w<=v.
Repeated integration by parts on this finite complex path gives the
same a_k/n^k expansion as L720, a factorial remainder, and endpoint
terms bounded by exp(-n*ell/270). Taking m proportional to n should
give equality to Q_n modulo O(exp(-c*n)), without any interpolation in n.

After compact Fubini and absorbing w<=v0 by strict monotonicity,
n^(-1/2)*K_n should equal integral_(v0)^b f(w)*exp(n*S(w))dw
plus O(exp(n*(Re S(b)-gamma))), where
f(w)=a_0(w)*chi(w)+S'(w)*integral_w^b chi(v)*B(v,S(v)-S(w))dv.
If f vanished on a terminal interval, the bounded kernel and nonzero
a_0 would force chi to vanish there by a short-interval sup norm
estimate. Thus f retains the actual right support edge.

For the final endpoint test use Z(v)=exp(-12*S(v)), rather than a
continuous-size theorem. The sampled generating integral is
integral f(v)*exp(3*S(v))*Z(v)/(Z(v)-z)dv. If its germ had larger
radius, a local biholomorphic Z chart at b identifies both sides of
the slit with that same extension. Integrate along Z(|w-b|=rho).
The contour meets the density arc transversally once. Absolute double
integrability near that crossing allows Fubini; the finite residue
theorem makes the contour integral -2*pi*i times the terminal density
integral. Holomorphy makes it zero for every small rho, forcing f=0
near b. This avoids confusing an interior branch jump with an endpoint
singularity. These details still need the canonical full write-up.
