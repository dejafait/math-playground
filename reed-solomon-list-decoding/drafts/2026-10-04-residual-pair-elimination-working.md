# Residual-pair elimination: working record

The saved EXPLORE target is unchanged. This turn tests the signed collision
energy from L017, not a new character estimate. For ordered 66-subset pairs
S,T put d_j=p_j(T)-p_j(S). Residual collision equations are
z^j-w^j=d_j. If d_1=0, they have Q solutions exactly when all required
d_j vanish. If d_1!=0, the first two equations fix z,w uniquely, and
the third is equivalent to 4d_1d_3=3d_2^2+d_1^4.

The completed test is preserved in
[L018](../lemmas/L018-residual-pair-elimination-and-root-count-limitation.md).
It resolves |S minus T|<=2 exactly and proves that the two-root upper
allowance exceeds the sufficient energy threshold by more than
6.14e14. This concerns the allowance, not actual energy. Exact small
audits passed; collision counts for larger symmetric differences remain unestimated. The
signed-energy route is parked, with no safety or unsafety conclusion.
