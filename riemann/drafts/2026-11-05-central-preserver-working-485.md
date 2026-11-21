# Step485 — approved finite residual-preserver test

Target: the exact SPECIALIZE target in
`literature/2026-11-05-central-matched-residual-preserver-test.md`.
Inputs read: L791/L792, including the exact positive solution, matching,
full-box mismatch, and inherited analytic/evaluator/software qualifications.
No coefficients are being recomputed or narrowed.

Working calculation: F_5/S^5=-p_5=t_m and R_5/S^5=t_a, hence
c_5=R_5/F_5=t_a/t_m in (0,1), while c_0,...,c_4=1.
For epsilon=1-c_5 in (0,1), the real-rooted test (1+x)^5 maps to
H(x)=(1+x)^5-epsilon*x^5. Its reciprocal is
K(z)=z^5 H(1/z)=(z+1)^5-epsilon.
With r=epsilon^(1/5), its five roots are -1+r*exp(2*pi*i*k/5).
Only k=0 is real; every root is nonzero since r<1. Inversion therefore
gives exactly one real and four nonreal roots of H. Later diagonal
entries cannot change this degree-five witness.

This is a specialization of the assessed binomial/reciprocal rigidity
argument, not a new general theorem or a claim about actual Jensen roots.
Canonical proof, scope qualifications and final checkpoint follow below
in the completed artifacts; this preserves the reasoning before edits.
