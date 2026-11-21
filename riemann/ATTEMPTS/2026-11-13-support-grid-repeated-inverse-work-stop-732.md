# Unchanged support-grid inverse implementation: work stop732

Under the ready SPECIALIZE assessment729/comparison730, tested the
complete-work gate before extending the remaining61 blocks. Canonical
proof, exact source counts and limitations are in
[C998w Section4](../lemmas/C998w-support-grid-original-measure-residual-partial.md).
The certificate is `scripts/separation-seven/support-grid-work-stop-732.json`;
all15 static source/count checks pass.

WHY IT FAILS: the731 inverse routine solves35 full35-dimensional systems
separately per block. Its remaining61 inverses alone require at least
121,951,200 source units>10^8, even with all moments, candidates and the
three existing rules free. All64 selected Gram/inverse arithmetic alone
costs at least101,002,560. This stops the source-preserving731 extension
without any large-block run. It does not refute its three valid rules,
positive residual methods, optimized inverses or uniform validation.
No full G error, byte-storage bound, scalar or sign is established.

A distinct possible construction would fix the35 selected support
indices from the successful k=10 instance and certify one rule family
uniformly over the remaining block parameter, instead of rerunning
NNLS and recomputing inverses61 times. This is only a nomination;
uniform positivity, moment enclosure, conditioning and cost coverage
require a separate source review. No theorem or feasibility is asserted.
The old bisection/precision failures and all earlier stops are retained.
