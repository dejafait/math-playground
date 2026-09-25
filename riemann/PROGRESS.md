# Current notebook state

STATUS: IN_PROGRESS

STEP_ID: 2026-09-26-endpoint-mellin-width-gram-01
STEP_OUTCOME: ADVANCE
STEP_EVIDENCE: L351 proves Σw_N²=C_w/(2N)+O(N^(-3/2)) and a uniform O(1/N) dilation average of H_N on intervals of length at least N^8 exp(−4N); H_N(1) remains unproved. See lemmas/L351-endpoint-mellin-width-local-gram-average.md.

Main bottleneck: global mixed reciprocal-zero positivity remains unproved. L320 needs a logarithmic initial segment of Laguerre signs, but L296's bands strictly above coefficient 1/4 leave low logarithmic and sublogarithmic indices open. Heights above forty and the endpoint arithmetic margin remain unresolved.

Route decision: retain the Mellin-width weighted sampling route, with collision mass and a local dilation average now controlled. The next issue is arithmetic concentration at the exact dilation 1; a small exceptional measure cannot establish its value. The deterministic sampling bound, exceptional sampled indices and pointwise margin remain open. All established sign/exclusion ranges are unchanged.

Exploration turns used: 0 of 3 consecutive unresolved exploration turns; a relevant uniform local Gram average is established. No RH candidate.

Next action: Test M_N(N^(-1/8))=o(1) from L351 at the exact dilation 1, using a fourth-moment bound for C_N under the weight w_N(ν)w_N(μ)/W_N²; the sufficient fourth-moment threshold is o(N^(-1/2)).
