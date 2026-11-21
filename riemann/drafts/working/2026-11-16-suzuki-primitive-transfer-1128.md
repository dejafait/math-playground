# Fixed-window primitive transfer1128 — work in progress

Approved target: the exact transfer in assessment1127, reused unchanged.
RESEARCH / REPRODUCTION / proof_attempt; no fresh literature assessment.
Main gap remains actual-Xi all-degree positivity (L030-L032/C032a).

Read C618a/C618b completely, the completed comparison1126 and working1127;
checked their relevant recorded failures. Rechecked Li paper45/v2
Theorem1.1/(2.1) and Suzuki2606.09096v3 Theorem1.1/(2.9), Sections3.1-3.2.
No source certificate or failed scalar test will be rerun.

Proposed proof, not yet completed: write m=integral phi and the
distributional derivative of C618a's primitive as mu=-phi dx+m delta_0.
It is a finite complex measure, with no atoms at the outer endpoints.
C618a gives O(1/|r|) Fourier decay, enough for a logarithmic form.
To establish membership at the exact radius a=log3, contract q to
q(s_k^{-1}x), s_k=1-1/k, and convolve with a nonnegative smooth
mollifier of radius a/(2k). These are smooth compact tests inside
(-a,a). Their Fourier transforms converge pointwise with a uniform
O(min(1,1/|r|)) bound; check the full weighted convergence.

For the anchored identity, their derivatives are the convolution of
the pushforward of mu under x -> s_k x with the mollifier. Uniform
continuity of each g_j on a fixed compact difference interval should
control the double integrals by ||mu||_TV^2 times its modulus of
continuity at 3a/k. Expanding mu keeps both anchor cross terms.
Match the pole factor, signed prime correlations and h=2W gamma
normalization before invoking lambda_a=inf spectrum(A_a)>0.

Continuation test: obtain the exact closed-form identity for arbitrary
complex phi, including m != 0, and Q_a >= lambda_a E0/(2pi).
Otherwise retain the failed domain or normalization claim explicitly.
No numerical gap, uniform-in-window positivity or RH conclusion follows.

Completed: the argument is now canonical in C618c. Contraction followed
by mollification proves membership at the exact radius, so no support
enlargement is needed. The double-measure limit is controlled by
||mu||_TV^2 omega_g(3a/k); expanding its atom retains both anchor terms.
Pole, finite prime and gamma contributions match Li's (2.1) exactly,
giving Q_a(phi)>=lambda_a E0/(2pi), with lambda_a>0 imported and
nonexplicit. This is local progress by known-result specialization,
not mathematics beyond the inspected positivity sources.

The initial plan above is preserved as a checkpoint. No failed domain
claim remains in this attempt; conceptual review is separately nominated
in assessment1128. The new proof is not itself that independent review.
