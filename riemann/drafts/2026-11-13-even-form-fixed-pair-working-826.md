# Fixed even pair — unfinished calculation, step826

Approved target: assessment824's single COVERED_TARGET, unchanged.
Inputs: C759a(1),(5)-(6), Proof1; C759h Proof1-2; the imported
regularized digamma identities recorded in C998z Proof2 are a formula
reference, not an even-sign premise. Standard order necessity is
Manavi–Vogt–Voigt Corollary2.6/Remark2.7 as assessed in823/824.

Main gap: actual-Xi all-degree mixed positivity. This calculation only
tests the even all-times positivity-preserving mechanism. Seek strict
Delta_e>0; a nonpositive or zero-containing result ends this fixed test
without an affirmative order conclusion. No sweeps or resolvent work.

Working observations (not yet a verified result): each bump radius is
1/40. The cross bands are [11/20,13/20] and [19/20,21/20]. Self terms
must cancel by polarization, including the v-v log5 contribution;
they must not be declared absent from each individual form. Candidate
kernel formula is Delta_e=2 integral (4cosh(d/2)-k(d)) H(d) dd,
H(d)=integral[u(x+d)v(x)+v(x+d)u(x)]dx,
k(d)=2exp(-d/2)/(1-exp(-2d)). Verify all factors and extend the
smooth identity to these H1 quartics by compact mollification.

Pending: rigorous log2/log3 exclusions covering all five delays;
uniform kernel bound at d>=11/20; exact H mass; ordered even-space
normalization, pair/modulus admissibility and shift-invariant application.
No sign, semigroup or RH conclusion is asserted in this checkpoint.

Completed later in the same step: the full analytic sign certificate
and qualified necessary-criterion application now live canonically in
C759i, `lemmas/C759i-even-fixed-quartic-form-order-obstruction.md`.
The unfinished observations above are preserved as working history;
they are superseded by that proof, which awaits independent review.
