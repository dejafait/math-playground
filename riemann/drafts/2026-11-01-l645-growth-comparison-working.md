# L645 growth comparison — working record

Approved target: Determine whether unconditional completion and zeta-derivative growth bounds force L645's inequality (7) to fail for every sufficiently high simple zero with fixed displacement delta in (0,1/2).

Gate: supplied prior SPECIALIZE assessment, drafts/literature/2026-11-01-l645-logarithmic-grid-growth-compatibility.md. Essential local inputs are L018 and L645. Reuse the inspected Gonek (1984), Section 2 (20), p.127, DLMF 5.11.9 and 27.4.3/5; no new browsing or reproof of convexity is needed.

Main gap: actual-Xi signs at unbounded heights/all-degree mixed positivity. Intermediate target: compare the exact H_rho with A_delta^(-1) exp(lambda_delta floor(log gamma)). Downstream use: decide whether this sufficient bound reaches logarithmic matrix size. Continue this test only if a strict exponent gap decides eventual compatibility; otherwise preserve the gap and stop this implementation. No actual PSD or smaller-witness conclusion follows from failure of (7).

Preliminary reasoning saved before completion: the entire-function maximum principle gives M_rho >= |xi(2+i gamma)|, even though the center is not on its defining circle. The reciprocal series gives |zeta(2+i gamma)| >= 1/zeta(2). Uniform Stirling therefore gives |xi(2+i gamma)| >= c gamma^(5/2) exp(-pi gamma/4). At the stipulated zero, differentiating the completion leaves only its prefactor times zeta'(rho). Gonek (20) gives |xi'(rho)| <= C_(delta,epsilon) gamma^(2+epsilon) exp(-pi gamma/4). Thus H_rho >= c_(delta,epsilon) gamma^(1/2-epsilon), using only 1+|F(s_*)|>=1. Check the nonzero derivative and every prefactor before canonizing.

Candidate elementary separation: q_delta >= d/R, hence lambda_delta <= log(R/d) < log(5/4) < 1/4 for 0<delta<1/2. Choosing epsilon=1/4 would give H_rho >= c_delta gamma^(1/4), strictly faster than the threshold. Floor(log gamma) only lowers the required upper bound. Pending: exact algebra, hypotheses, constants/onset and canonical proof. No off-line zero existence is assumed.

Completion: the exact estimates and exponent separation are written in lemmas/C645a-logarithmic-grid-growth-threshold-obstruction.md. The lower ratio bound and floor give strict eventual failure, not an inconclusive comparison. Outcome NEGATIVE for this sufficient logarithmic threshold. No mathematical script or numeric onset is needed; this is an analytic specialization. Independent audit is nominated with reused source coverage, not performed here.
