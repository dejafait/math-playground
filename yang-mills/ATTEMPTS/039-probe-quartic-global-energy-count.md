# Global Gaussian energy count for the probe retraction quartic

WHY IT FAILS: [L183, proof section 5](../lemmas/L183-effective-cubic-residual-retraction.md)
tests the whole quartic correction E[dJ_i[W]], with both pinned prefixes
and Phi W retained. The third-chaos energy identity and the full residual
form/prefix covariance bounds give only O(N^5), versus the required
O(N^3). The W energy norm is bounded only by O(N^4), whereas O(N^2)
would suffice in this inequality with ||J_i||_2=O(N). These are upper
bounds, not sharp exponents or evidence of signed growth. This stops
that absolute global count as cubic closure, not L183's exact identities
or the joint response target. The signed Wick contraction before norms
remains independently testable; the sextic and zero-time flow terms
remain unresolved.
