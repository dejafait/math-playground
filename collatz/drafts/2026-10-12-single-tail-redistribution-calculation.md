# Single-tail redistribution calculation — completed bounded attempt

Approved target: classify the 24 literal L055 allocations with a_j=20
for one j<24, a_24=166504394 and all other tails 2, at their unique
cyclic endpoints, for the domain and every necessary own-input J guard.
Coverage: `literature/2026-10-12-single-tail-redistribution-j-guards.md`,
SPECIALIZE; completed work will be RESEARCH/REPRODUCTION.

Inputs: L055's literal J,H table and audited Lambda interval; L051 (3)–(4).
L063/C063a are scope boundaries only. No changed-tail bound is imported
from them. Existing prime stops and fixed-allocation results are preserved.

Plan: use the exact factored affine root with each changed tail. Prove a
uniform bound on B using c_0>10^8/2^18 and c_i>2 for 1<=i<24
(checking the tail-20 baseline at row 1). Establish the lower domain before
the J comparisons. Bound each log s_i above and below from the actual
prefix exponent sum; a strict negative upper guard margin rejects a case,
and 25 positive lower margins certify a survivor. Stop after these cases.
No H guards, seed, integrality, parity or exact valuations will be inferred.

The main gap is universal eventual descent. Additional guard exclusions
extend the tested necessary-subsystem obstruction; a survivor limits that
mechanism and leaves independent realization gaps.

Completed result: [L064](../lemmas/L064-single-tail-redistribution-j-guard-classification.md)
classifies the entire approved family. For j=0,...,22 the own-input guard
at i=j+1 fails by more than 9.32. For j=23 all 25 J guards pass, with
minimum certified margin greater than 0.402427610954. All exact tuples
satisfy s_i>18*10^9>540/11. The changed tails and full closing exponent
are included. No interval straddles zero. The certificate is
`scripts/postspell-word-count/single-tail-redistribution-certificate.json`.
It passed 20 rational and 168 integer/count checks; all decisive guard
records and their operands were inspected. This is local reproduction,
not a claim of progress beyond the inspected general affine machinery.

Stop the bounded test here. The J-only exclusion mechanism cannot reject
the entire family. No H, seed, integrality, parity or exact valuation
verdict is supplied. A separate critical audit is the proposed continuation;
its scope assessment requires a later approval turn. No wider allocation,
permutation or prime search was performed.
