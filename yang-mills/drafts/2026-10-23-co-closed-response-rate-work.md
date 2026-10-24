# Co-closed response rate — bounded attempt

STEP_ID: YM-20261023-420-co-closed-response-quantitative-rate
Approved target: Prove that L193's complete co-closed cubic-probe response |E[F_i rho_F]| is at most C_i N^(5/2)log(eN)^2 for both actual probes.
Assessment: drafts/literature/2026-10-23-co-closed-cubic-response-quantitative-rate.md (EXPLORE before invocation).

Main gap: interacting continuum construction, nontrivial physical sector and finite positive infrared mass. This attempt addresses only a component of the quantitative bare response; transverse-H, complete assembly and upstream audits remain independent.

Inputs: L181 L182 L183 L189 L190 L191 L192 L193; supporting relative kernel input L166 as used by L190. Preserve both Q forms, full three-color tensors, all derivative placements, normal end rows, correlated prefixes, upper jump and complete heat sums. Existing local modifications are preserved.

Saved pre-proof attempt: integrate L193's uniform W envelopes separately. For rho_H, test exact common-input heat transfer with time proportional to s. Bound the transferred residual by retaining two heat-smoothed covariance slots even in each action-tilt placement. In whitened coordinates the tilt is M=2 S^(1/2) A S^(1/2), ||M||=O(N); it need not commute with heat. Proposed bound (unproved when checkpointed): ||rho_H(H_r z)||_2 <= C N^3 (1+r/a^2)^(-1/2). A joint two-smoothed/one-raw Green product could supply the gain. Combine with the full probe time envelope only after proving a uniform finite-mesh inequality.

Continuation test: complete response within N^(5/2)log(eN)^2, including s=0 and s=tau. If the mixed covariance norm or transferred probe envelope loses more, record the actual allowance, not signed growth. Do not use a varying cutoff in L193's fixed-delta conclusion, the failed O(N^4) full-residual norm, or termwise quotient transfer.

Completed attempt: the complete proof is canonical in [L265](../lemmas/L265-co-closed-cubic-response-quantitative-rate.md). Scalar heat positivity and diagonal spectral control combine with L166's full relative Green estimate to bound the two-smoothed/one-raw covariance product. In coefficient space the tilted slot is J M; the other two heat slots remain before its operator norm is used. This proves the proposed uniform residual estimate. Exact heat transfer then gives an integrated rho_H allowance N^2 log(eN)^(5/4). Imported complete W envelopes give N^(5/2)log(eN), and the final observable is N^2. The requested complete co-closed threshold is met, subject to a separate critical audit and unchanged imported premises. No mathematical scripts or finite-mode diagnostics were used.

Outcome ADVANCE / RESEARCH / REPRODUCTION, actual task proof_attempt. This is local progress by standard methods, not a claim of novelty beyond inspected sources. No failed route was reopened: ATTEMPTS/043 concerns the full forest residual, which is never assigned the new local bound. Mathematical exploration usage remains zero of three after this advance. The new audit continuation is REVIEW_REQUIRED; its source-scope approval belongs to the next invocation.
