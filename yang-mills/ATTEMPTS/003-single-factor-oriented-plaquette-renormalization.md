# Single-factor renormalization of an oriented plaquette

Tested 2026-09-25. As part of examining the ultraviolet correction to the Wilson-normalized 12 plaquette, test whether its continuum curvature-square insertion can be treated as one multiplicatively renormalized scalar operator.

## WHY IT FAILS

[L004](../lemmas/L004-oriented-curvature-square-renormalization-mismatch.md) converts the cited one-loop MS identities to the observable's actual normalization, including 1/g_0^2. Its scalar projection requires residue b_0, while its traceless stress-tensor projection requires residue zero. A rotation-covariant common factor cannot satisfy both. The oriented square also has an additional tensor component whose counterterm has not been computed. This stops the single-factor or scalar-only operator prescription, not the observable-comparison program or the Yang–Mills target. It does not prove divergence of the particular fixed-box reflection coefficient: a full mixing calculation and interacting error control remain missing. The complementary-plane difference isolates a stress-tensor component and gives a distinct concrete observable to test.
