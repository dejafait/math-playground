# Degree-six Hermite product-kernel attempt — step496

Invocation-start coverage: `drafts/literature/2026-11-05-central-hermite-product-kernel-test.md`, EXPLORE, unchanged target. This is one conventional exact calculation, not a new hyperbolicity theorem.

Main gap: actual-Xi all-degree mixed positivity. Intermediate target: construct the specified denominator-cleared symmetric theta product kernel for the central degree-six Newton-sum matrix, and test only `(1,...,1,t)`, `t>=1`. Downstream use: decide whether direct pointwise signing of this representation is viable. A certified negative rational quadratic value stops this representation only; a passing family is limited, and failed construction is inconclusive.

Inputs inspected: L019's strictly positive theta K and L021's finite positive moments; L018/L776/L791/L792 fix the coefficient convention only. The completed parent source comparison imports Nathanson's Newton-sum/Hermite convention, not a positive root representation. L766's distinct Toeplitz stop is not an input. No evaluator, root premise or L793 tolerance is used.

Work in progress: writing the monic polynomial as `x^6+c_1 x^5+...+c_6`, its coefficients must be `c_k=(-1)^k binom(6,k) ((6-k)!/(12-2k)!)/(6!/12!) m_(6-k)/m_6`. Compute Newton sums through s_10 exactly. Verify the least denominator exponent and homogeneity before polarization. No multivariate sign search or degree sweep is authorized.

Initial checkpoint, now resolved: the full rational expansion, denominator exponent, symmetric product identity, and one-outlier sign were uncomputed. Actual all-degree signs and any integrated compensation remain independently unresolved.

Completed outcome: L794 supplies the canonical construction, N=10 minimality proof, finite absolute-integral justification and integer-vector negative witness at t=4. The certificate is `scripts/central-hermite/product-kernel-496.json`; reproduction uses the adjacent `product_kernel_496.py`. The leading-matrix LDL test found its first negative pivot in the 3x3 block, allowing a proof using only s_0,...,s_4. The complete s_0,...,s_10 expansion remains saved, not discarded. The bound requires t^2>352249253/28504137 and t=4 has t^2=16, giving the exact integer value -1281831933403422720 for the integer witness.

This is an informative negative for the fixed pointwise mechanism, not negative integrated positivity. The source comparison in `drafts/literature/2026-11-04-actual-theta-signed-compensation-review.md` and its ATTEMPTS record were consulted only to choose a responsible continuation: merely asking again for an uncontrolled integration-by-parts remainder would repeat a source-limited mechanism. No new independently controlled theta compensation or degree-uniform central mechanism is available here. Nominate an independent audit of the new exact obstruction; do not label its conventional algebra creative. The newly written audit assessment requires separate next-turn approval.
