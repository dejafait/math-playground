# Attempt: combine all established generic kernel and zero-geometry properties

Date: 2026-09-09

Outcome: failed sufficiency claim, now with full zero confinement verified.

The actual Ξ has a positive smooth even strictly log-concave superexponential kernel, order at most one, positive imaginary-axis values, alternating even coefficients, and all zeros in |Re z|>4, |Im z|<1/2. Lemma 55 constructs F_a sharing all these properties for every 0<a≤1/100.

Take g=exp(-cosh(2u)), c_a=cosh(a/10), and h_a=[c_a g+(g(u-a)+g(u+a))/2]/(c_a+1). The curvature estimates prove global strict log-concavity. Its transform is [c_a+cos(az)]G(z)/(c_a+1), with introduced zeros (2k+1)π/a±i/10. The separate integral differential equation and energy estimates of Lemmas 53–54 prove all G zeros real and of absolute value >4, so every zero of F_a satisfies the required geometric bounds.

**WHY IT FAILS.** These generic properties, even when imposed simultaneously, permit a small positive shift mixture to insert nonreal zeros while retaining both the kernel shape and the full zero confinement. The base-zero locations have now been proved rather than presumed, closing the limitation of the earlier comparison examples. The construction does not share the precise theta-series arithmetic coefficients of Ξ; a successful proof must use something more specific than the generic properties isolated so far.

Next lemma: show finite Hankel checks can also persist for this family as a tends to zero, rather than assuming finite positive certificates distinguish it from Ξ.
