# Fixed-gauge contour test, step 40

The supplied EXPLORE assessment `drafts/literature/2026-11-02-displaced-positive-cone-distance.md` is reused unchanged for its exact cone target. This is one mathematical attempt, not another source review. Essential inputs are L666's full family, L672's interpolation method, and L673's separately audited signs and finite-product estimates.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target: decide whether contour geometry alone, with L673's fixed gauge and nodal displacements, can deliver a full-angular exponent below -1/100 with polynomial finite-n costs. A passing nonnegative countersequence would refute a sufficient cone-separation mechanism; a cost barrier would stop only that contour method. The unit-residue application, H, support, Xi realization and signs remain unresolved.

Preserved comparisons: L673 section 5 rules out its unchanged rectangle, and the earlier bounded even-polynomial screen is inconclusive. L672 does not supply nonnegative coefficients. The scalar/Gram/spatial failures and all prior work remain in place. No duplicate nonrectangular-contour certificate was found in the scoped relevant files.

Bounded test: first inspect whether the fixed exponent admits any enclosing low-cost contour in the pole-free parameter region. If a real-axis or other separating barrier can be certified, park contour-only improvement for this fixed gauge. Otherwise select one concrete contour and certify its full angular and finite-n costs. A floating screen alone is inconclusive.

Work in progress: every common pole-free Jordan domain containing zero must exclude the real parameter-pole segment starting near z=1/4. Its positive real-axis crossing may give an independently checkable obstruction; the sign and uniform rate of that exponent remain to be calculated. No result is assumed.

## Real-crossing refinement saved before certification

The floating diagnostic `scripts/one-sided-hankel/positive-cone-real-crossing-screen.json` suggests a barrier, not a successful contour. At u=-1 and real 0<s<1/4, let E be L673's exact continuum exponent. Direct differentiation gives

    E(0)=0,
    E'(0+)=log 5+(121/100)log(121/41)-4/5-20*pi/27,
    E''(s)>=16/5-4096/5043+200/159-6/5.

The intended exact checks are E'(0+)>-21/100 and E''>12/5. They would imply E(s)>-147/16000>-1/100. Every Jordan contour containing zero with its closure in |x+z|>1 crosses this real segment. This would certify a barrier for the full-angular supremum of this fixed continuum exponent, independent of contour shape.

Scope requiring care: this is not a lower bound on the signed contour integral or on kappa. The zero of 1-z/rho and any n-dependent contour entering the thin finite-n pole-free collar need separate analysis; neither can silently be ruled out by a limiting-exponent argument. The planned conclusion only excludes E<=-1/100 on every point of a contour in the specified common region.

Completion: the exact constant certificate passes all 14 checks with zero failures. The full analytic proof, hypotheses and scope limitations are canonical in `lemmas/C673a-fixed-gauge-real-crossing-contour-obstruction.md`; no sampled minimum is used. The result parks only fixed-gauge contour-shape improvement of the continuum supremum criterion inside |x+z|>1. It does not decide the cone distance. The separate audit is pending. The exact target and its ready assessment remain unchanged; the single next attempt uses a direct real-polar Laurent-functional mechanism rather than extending this stopped contour calculation.
