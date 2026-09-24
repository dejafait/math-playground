# Right-quadrant Stieltjes sign test — 2026-09-23

Gap: actual-theta all-degree mixed positivity remains unproved. The intermediate target is Im G(z)≤0 for Re z>0, Im z>0, tested through a symmetrized theta double integral. Its plausible use is as part of a full upper-half-plane Stieltjes sign argument; analytic continuation without poles and the sign on the left upper quadrant remain separate requirements.

Discriminating test: continue a pointwise mechanism only if the double-integral kernel is everywhere nonpositive on actual theta support. Independently test whether the integrated quadrant sign already follows from the recorded zero sector and holds for L247's counterexample; if so, abandon that restricted sign as a sufficient bridge.

Redundancy screen: L242 treats real-axis derivative signs, L246 translated scalar signs, and L247 complete monotonicity. None records this complex-parameter integral or the conjugate-pair quadrant calculation. Existing changes and inactive branches are preserved.

Result: [L248](../lemmas/L248-right-quadrant-stieltjes-sign-and-kernel-obstruction.md) proves the exact integral, both pointwise signs on positive-weight regions, and strict integrated negativity throughout Re z≥0, Im z>0. The same restricted sign holds for both L247 counterexamples. The attained domain is therefore strictly weaker than the required full upper-half-plane holomorphy and sign, and supplies no all-degree mixed positivity.

WHY IT FAILS: the theta numerator oscillates on its actual support, ruling out this direct pointwise mechanism. Although conjugate pairing resolves the integrated right-quadrant inequality, existing coarse zero geometry already supplies it and nonreal poles in the left half-plane survive. Neither that inequality nor analytic continuation of the formula continues the sign across the imaginary axis. This is not evidence against RH or against other theta-specific cancellation arguments.

Decision: NEGATIVE; stop the pointwise-integrand mechanism and the right-quadrant sign as a sufficient bridge. One bounded test resolved; zero consecutive unresolved exploration turns. The next direction is a boundary-resolution test of the full upper-half-plane condition: write −π^(−1) Im G(−t+iε) as a signed sum and determine the ε range controlled by existing localization. This targets the missing domain rather than adding more right-quadrant signs. No RH candidate is obtained.
