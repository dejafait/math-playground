# Sextic family: one bounded first-sign test

TARGET: Test global Stein nonincrease and a negative first Laguerre sign for p_b proportional to exp(-u^6-bu^2) with one heat-collision search restricted to 0<b<=16 and |x|<=64.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact-family searches and primary cases in 2026-11-01-sextic-damping-stein-collision-review.md; no matching BOTH-property counterexample or first-sign collision theorem was found in the inspected sources. No novelty certification.
SOURCE_EVIDENCE: Newman https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf Theorem 2/(1.8)-(1.10), pp. 246-247 and necessity pp. 248-251; Bagnoli-Bergstrom https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf Theorem 3/Corollary 2 p. 4 and Appendix 8.2 concave case p. 25; Saumard https://arxiv.org/pdf/1804.03926v3 (5)-(6) qualifications reused from L605/L606; Csordas https://arxiv.org/pdf/1309.0055v2 (2.1), Proposition 4.9 p. 12, with no generic collision import. Actual reading and access limits are in the completed comparison.
COMPARISON: Known all-damping zero classification motivates the sextic diagnostic after the closed quartic model; it does not give a negative first sign. Hazard monotonicity covers the spatial step only after its exact local hypotheses and coordinate change are checked. Direct first-sign certification is the uncovered difference.
GAP: Establish all density/decay/endpoint hypotheses and global Stein nonincrease at the witness parameter, then certify F_b'(x)^2-F_b(x)F_b''(x)<0. Finite collision existence and nondegeneracy are not premises. Actual-Xi transfer and all higher signs stay open.
REASON: A finite direct determinant test avoids dependence on the missing global collision theorem. This newly written continuation needs separate next-turn approval; no mathematical result or local specialization has been derived or approved here.
SCOPE: Exactly this family and finite rectangle, global spatial hypothesis verification, and one direct first-sign certificate or fully justified local collision argument. No unbounded sweep or presumed finite collision at a threshold.

Define p_b(u)=Z_b^(-1)exp(-u^6-bu^2), its full-line Fourier transform
F_b(z), and tau_b(u)=integral_u^infinity v*p_b(v)dv/p_b(u).
The main gap is actual-Xi all-degree signs at unbounded heights.
A BOTH-property counterexample would stop generic monotone-Stein
first-sign transfer; it would not give a negative actual-Xi sign.

First check the global spatial premise using the named hazard theorem.
The proposed auxiliary density is proportional to p_b(sqrt(s)) on
(0,infinity). Verify its normalization, C1 regularity, log-concavity,
weighted-tail substitution and endpoint limits. This auxiliary law
is not the squared-variable law with a Jacobian. Also verify every
original density, centering, smoothness and derivative-decay condition,
including the zero endpoint and negative tail. Import the known hazard
theorem rather than reprove it. No check is established by this plan.

Perform at most 256 exploratory function/derivative evaluations within
the rectangle, using heat evolution or local extrema to choose them.
Attempt one rigorous certificate at the strongest candidate. Record
complete integral tails, differentiation and cancellation error bounds.
Alternatively certify finite collision data and a local implication to
a negative first sign, with parameter orientation and Taylor remainders
justified. A collision's existence, multiplicity or zero branch must
not be assumed. Direct determinant certification requires no crossing
theorem. The endpoint b=0 may guide the search but is not the requested
positive-damping witness. The rectangle/evaluation cap is an exploration
budget, not a theorem that a witness exists there.

Pass only with BOTH global Stein nonincrease and strict negativity at
the same parameter. Nonreal zeros, uncertified quadrature and conditional
Taylor statements do not pass. Save useful partial results with their
qualifications. If no witness is certified within this budget, stop the
finite test as inconclusive, with actual bounds and failures preserved.
No unsampled positivity or global family obstruction follows; do not
automatically enlarge the rectangle or renew the search by a parameter
change. Further work requires materially new evidence or a new target.

Essential inputs are the named theorems above. L606 is contrast;
C233b/L604/L605 are context, not mathematical premises. Newman–Wu's
finite-threshold account is motivation only; unread original Pólya
and collision proofs are unnecessary for a direct certificate. No
cross-notebook input. Full matching Mathlib coverage is unchecked.

This is a bounded calculation and ordinary theorem specialization,
not a creative actual-Xi mechanism. POTENTIALLY_NEW may describe only
an actually established uncovered conclusion, never the imported
hazard or zero-location results.
